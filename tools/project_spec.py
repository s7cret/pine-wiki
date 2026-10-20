#!/usr/bin/env python3
"""Generate card/history/search projections from the single semantic registry."""
import argparse,copy,json,sys
from pathlib import Path
from spec_bundle import ROOT,read_json,encode,digest,effective,semantic_projection,resolution_problem
sys.path.insert(0,str(ROOT/'tools/migrations'))
from catalog_io import load_catalog,save_catalog
from probe_contracts import validate_definition,run_applies,run_status_consistent


def project_examples(examples,runs,definitions):
    examples=copy.deepcopy(examples)
    by={d['definition_id']:d for d in definitions['definitions']}
    for example in examples['examples']:
        candidates=[]
        for run in runs['runs']:
            d=by.get(run['definition_id'])
            if d and validate_definition(d) and run_status_consistent(run,d) and d.get('parent_example_id')==example['example_id'] and d['code_sha256']==example['code_sha256'] and run_applies({'code_sha256':d['code_sha256'],'language_version':d['language_version'],'probe_definition_hash':d['definition_hash'],'definition':d},run):candidates.append((run,d))
        if candidates:
            run,d=max(candidates,key=lambda pair:pair[0]['date'])
            example.update(probe_definition_id=d['definition_id'],probe_definition_hash=d['definition_hash'],validation_context_hash=run['context_hash'],validation_run=run,
                           compilation_status=run['compiler']['status'],execution_status=run['runtime']['status'],oracle_status='runtime_blocked_by_platform_plan' if run['runtime']['status']=='blocked' else 'observed_in_recorded_context')
    return examples


def project_catalog(catalog,registry,identities):
    aliases={a['entry_id']:a for a in identities['aliases']};parameters={(p['entry_id'],p['name']):p['parameter_id'] for p in identities['parameters']}
    symbols={s['symbol_id']:s for s in registry['symbols']};assertions={a['assertion_id']:a for a in registry['assertions']}
    revision=digest(semantic_projection(registry))
    for e in catalog['entries']:
        identity=aliases[e['id']];e['symbol_id']=identity['symbol_id'];e['overload_contract_id']=identity['overload_id']
        for p in e['parameters']:p['parameter_id']=parameters[(e['id'],p['name'])]
        if catalog['version']==6 and identity['symbol_id'] in symbols:
            s=symbols[identity['symbol_id']];overloads=[]
            for o in s['overloads']:
                a=assertions[o['signature_assertion']]
                overloads.append({'overload_id':o['overload_id'],'assertion_ref':a['assertion_id'],'decision_ref':a['decision_ref'],'review_status':a['review_status'],
                                  'evidence_refs':a['evidence_refs'],'contract':effective(a,registry)})
            common=['rule.grammar','rule.types','rule.scope']
            if overloads:common+=['rule.binding','rule.overload','rule.arguments.left_to_right','rule.context.current','rule.state.call_site_context','rule.execution.skipped_call']
            specific=registry['identity_policy'].get('symbol_rule_dependencies',{}).get(s['symbol_id'],[])
            needed=sorted(set(common+specific));rules={r['rule_id']:r for r in registry['rules']}
            dependencies=[{'rule_id':rid,'assertion_ref':rules[rid]['semantic_assertion'],'status':'unresolved' if effective(assertions[rules[rid]['semantic_assertion']],registry).get('kind')=='unknown' else 'resolved'} for rid in needed]
            unresolved=[d for d in dependencies if d['status']=='unresolved']
            value=effective(assertions[s['value_assertion_ref']],registry) if s.get('value_assertion_ref') else None
            signature_ready=all(o['contract'].get('kind')!='unknown' for o in overloads)
            e['semantic_contract']={'semantic_profile_id':'pine6.core-mvp.1','registry_revision':registry['registry_revision'],'projection_sha256':revision,
                'symbol_id':s['symbol_id'],'signature_status':'resolved' if signature_ready else 'unresolved',
                'status':'resolved' if signature_ready and not unresolved and (not value or value.get('kind')!='unknown') else 'unresolved',
                'required_dependencies':dependencies,'unresolved_dependencies':unresolved,
                'overloads':overloads,'value':value,
                'rule_refs':registry['profiles'][0]['rule_refs']}
        if catalog['version']==5 and e['name'] in ('request.security','request.security_lower_tf','request.seed'):
            a=assertions['assertion.v5.'+e['name']+'.calc_bars_count.default']
            for p in e['parameters']:
                if p['name']=='calc_bars_count':
                    p['semantic_default']=effective(a,registry)
                    p['default_contract']['activation_status']='unresolved'
                    p['default_contract']['issue_refs']=a['issue_refs']
            e['semantic_contract']={'semantic_profile_id':'pine5.unresolved-reference.1','registry_revision':registry['registry_revision'],'projection_sha256':revision,
                                    'symbol_id':identity['symbol_id'],'status':'unresolved','overloads':[],'value':None,'rule_refs':[],'assertion_refs':[a['assertion_id']]}
    issue=next((i for i in catalog.get('source_issues',[]) if i['id']=='SOURCE.GAP.V5.RELEASE_2024_CALC_DEFAULT'),None)
    if issue:
        issue['entry_ids']=[e['id'] for e in catalog['entries'] if e['name'] in ('request.security','request.security_lower_tf','request.seed')]
        issue['assertion_refs']=[a['assertion_id'] for a in registry['assertions'] if a['assertion_id'].startswith('assertion.v5.')]
    return catalog


def project_history(history,catalogs):
    for family in history['families'].values():
        for z in family['versions']:
            entries={e['id']:e for e in catalogs[z['version']]['entries']}
            z['semantic_contracts']=[entries[i]['semantic_contract'] for i in z['entry_ids'] if entries[i].get('semantic_contract')]
            z['semantic_defaults']={p['parameter_id']:p['semantic_default'] for i in z['entry_ids'] for p in entries[i]['parameters'] if p.get('semantic_default')}
    return history


def coverage(registry,examples,runs):
    profile=registry['profiles'][0];assertions=[a for a in registry['assertions'] if a['scope']['semantic_profile_id']==profile['semantic_profile_id']]
    valid_runs=[r for r in runs['runs'] if r['environment']['implementation']=='TradingView Pine Editor' and r['compiler']['status']=='compiled' and r['runtime']['status']=='executed' and r.get('comparison',{}).get('passed') is True]
    probed=set()
    definitions=read_json(ROOT/'spec/probes.json')['definitions'];definitions={d['definition_id']:d for d in definitions}
    for run in valid_runs:
        d=definitions.get(run['definition_id'])
        if d and d['comparator']['kind']!='diagnostic' and validate_definition(d) and run_status_consistent(run,d) and run_applies({'code_sha256':d['code_sha256'],'language_version':d['language_version'],'probe_definition_hash':d['definition_hash'],'definition':d},run) and run.get('context_hash')==digest({k:run[k] for k in ('data','parameters','environment')}) and d['language_version']==6:
            probed.update(d.get('proves_rule_refs',[]))
    rule_refs=set(profile['rule_refs'])
    return {'semantic_profile_id':profile['semantic_profile_id'],'structural_coverage':{'symbols':len(profile['symbol_refs']),'rules':len(rule_refs),'whole_programs':6},
            'resolved_semantic_facts':{'numerator':sum(resolution_problem(a,registry) is None for a in assertions),'denominator':len(assertions)},
            'independently_probed_rules':{'numerator':len(probed&rule_refs),'denominator':len(rule_refs),'rule_refs':sorted(probed&rule_refs)},
            'examples':{'unique_programs':len(examples['examples']),'bindings':sum(len(x['bindings']) for x in examples['examples'])},
            'observed_runs':{'compilations':sum(r['compiler']['status']=='compiled' for r in runs['runs']),'executions':sum(r['runtime']['status']=='executed' for r in runs['runs']),
                             'blocked':sum(r['runtime']['status']=='blocked' or r['compiler']['status']=='blocked' for r in runs['runs']),
                             'by_implementation':{name:{'runs':sum(r['environment']['implementation']==name for r in runs['runs']),
                                 'executions':sum(r['environment']['implementation']==name and r['runtime']['status']=='executed' for r in runs['runs'])} for name in sorted({r['environment']['implementation'] for r in runs['runs']})}},
            'implementation_coverage':implementation_coverage(registry),
            'exclusions':profile['uncovered'],'content_gaps':'Separate content metrics; neither translations nor duplicate bindings count as independent probes.'}


def implementation_coverage(registry,operations=None):
    sys.path.insert(0,str(ROOT))
    from consumer.frontend import Frontend
    from consumer.runtime import implemented_operations,source_identity
    profile=registry['profiles'][0];grammar=read_json(ROOT/'spec/grammar.json')
    semantic={'registry':semantic_projection(registry),'grammar':grammar};sha=digest(semantic)
    bundle={'semantic':semantic,'manifest':{'semantic_profile_id':profile['semantic_profile_id'],'semantic_hash':sha},'identities':read_json(ROOT/'spec/identities.json'),
            'evidence':{'assertion_evidence':[{'assertion_id':a['assertion_id'],'evidence_refs':a['evidence_refs']} for a in registry['assertions']]}}
    available=set(implemented_operations() if operations is None else operations);programs=[];needed=set()
    for p in read_json(ROOT/'spec/profile-programs.json')['programs']:
        try:
            resolved=Frontend(bundle).compile(p['code']);required=set(resolved['required_operations']);needed.update(required)
            programs.append({'program_id':p['program_id'],'needed':sorted(required),'missing':sorted(required-available)})
        except Exception as exc:
            from consumer.errors import Diagnostic
            if not isinstance(exc,Diagnostic):raise
            programs.append({'program_id':p['program_id'],'needed':[],'missing':[],'blocked':exc.data})
    return {'consumer':'consumer.cli','semantic_hash':sha,'build_identity':{'implementation':'pine-wiki-offline-consumer.1','consumer_source_sha256':source_identity(),'operations':sorted(available)},
            'program_ids':[p['program_id'] for p in programs],'programs':programs,'needed':sorted(needed),'implemented':sorted(needed&available),'missing':sorted(needed-available),
            'numerator':len(needed&available),'denominator':len(needed),'blocked_programs':[p['program_id'] for p in programs if p.get('blocked')],
            'affected_programs':[p['program_id'] for p in programs if p['missing'] or p.get('blocked')],'meaning':'Operation availability for the fixed six-program corpus; not correctness or complete Pine support.'}


def outputs(registry,identities):
    catalogs={};result={}
    runs=read_json(ROOT/'spec/probe-runs.json')
    examples=project_examples(read_json(ROOT/'spec/examples.json'),runs,read_json(ROOT/'spec/probes.json'))
    by_example={e['example_id']:e for e in examples['examples']}
    result[ROOT/'spec/examples.json']=encode(examples)
    for v in range(1,7):
        c,w=load_catalog(ROOT,v);project_catalog(c,registry,identities);catalogs[v]=c
        for entry in c['entries']:
            for item in entry['examples']['items']:
                example=by_example.get(item.get('example_id'))
                if example:
                    for key in ('probe_definition_id','probe_definition_hash','validation_context_hash','validation_run','compilation_status','execution_status','oracle_status'):
                        if key in example:item[key]=copy.deepcopy(example[key])
        path,prefix,suffix,old=w;result[path]=(prefix+json.dumps(c,ensure_ascii=False,separators=(',',':'))+suffix).encode()
    for path in ROOT.glob('history-*.js'):
        prefix=f'window.PINE_HISTORY["{path.stem[-1]}"]=';before,tail=path.read_text(encoding='utf8').split(prefix,1)
        h=project_history(json.loads(tail.strip().removesuffix(';')),catalogs)
        result[path]=(before+prefix+json.dumps(h,ensure_ascii=False,separators=(',',':'))+';\n').encode()
    stats=coverage(registry,examples,runs)
    result[ROOT/'spec/coverage.json']=encode(stats)
    from spec_review import impact
    programs=read_json(ROOT/'spec/profile-programs.json')
    view={'registry':registry,'coverage':stats,'sources':read_json(ROOT/'spec/evidence.json')['sources'],'workflow':read_json(ROOT/'spec/workflow.json'),
          'runs':runs['runs'],'programs':programs,'impact_map':[impact({**registry,'assertions':[a for a in registry['assertions'] if a['assertion_id']!=assertion['assertion_id']]},registry,programs) for assertion in registry['assertions']]}
    result[ROOT/'spec-data.js']=b'window.PINE_SPEC='+encode(view).rstrip()+b';\n'
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    result=outputs(read_json(ROOT/'spec/registry.json'),read_json(ROOT/'spec/identities.json'));stale=[]
    for p,data in result.items():
        if args.check:
            if not p.exists() or p.read_bytes()!=data:stale.append(p.name)
        else:p.write_bytes(data)
    if stale:raise SystemExit('SPEC_PROJECTION: stale: '+', '.join(stale))
    print('Semantic card/history/search projections: '+('current' if args.check else 'generated'))


if __name__=='__main__':main()
