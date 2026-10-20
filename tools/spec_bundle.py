#!/usr/bin/env python3
"""Deterministic, externally pinned offline specification bundles."""
import argparse,copy,hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCHEMA_VERSION='1.0.0'
UNORDERED={'assertions':'assertion_id','decisions':'decision_id','symbols':'symbol_id','overloads':'overload_id','rules':'rule_id','profiles':'semantic_profile_id','sources':'source_id'}


def reject_duplicates(pairs):
    obj={}
    for key,value in pairs:
        if key in obj:raise ValueError('Duplicate JSON key: '+key)
        obj[key]=value
    return obj


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf8'),object_pairs_hook=reject_duplicates,
                      parse_constant=lambda token:(_ for _ in ()).throw(ValueError('Non-finite number: '+token)))


def canonical(value):
    if isinstance(value,dict):
        return {k:canonical(sorted(v,key=lambda item:item[UNORDERED[k]])) if k in UNORDERED and isinstance(v,list) and all(isinstance(item,dict) and UNORDERED[k] in item for item in v) else canonical(v) for k,v in sorted(value.items())}
    if isinstance(value,list):return [canonical(v) for v in value]
    return value


def encode(value):
    return (json.dumps(canonical(value),ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()


def digest(value):return hashlib.sha256(encode(value)).hexdigest()


def semantic_projection(registry):
    excluded={'documentation','reviewer','author','date','rationale','evidence_refs','test_refs','review_events','retrieved_on'}
    def walk(value,in_semantic_value=False):
        if isinstance(value,dict):return {k:walk(v,in_semantic_value or k=='value') for k,v in value.items() if in_semantic_value or k not in excluded}
        if isinstance(value,list):return [walk(v,in_semantic_value) for v in value]
        return value
    return walk(registry)


def scopes_overlap(left,right):
    return bool(set(left['language_versions'])&set(right['language_versions'])) and all(left[k]==right[k] for k in ('semantic_profile_id','platform_profile_id'))


def resolution_problem(assertion,registry,version=None,profile_id=None):
    assertions={a['assertion_id']:a for a in registry['assertions']}
    decisions={d['decision_id']:d for d in registry['decisions']}
    decision=decisions.get(assertion.get('decision_ref'))
    if assertion['review_status']!='corroborated' or not decision or decision['status']!='accepted':return 'fact has no accepted review'
    if version is not None and version not in assertion['scope']['language_versions']:return 'language version outside assertion scope'
    if profile_id is not None and profile_id!=assertion['scope']['semantic_profile_id']:return 'profile outside assertion scope'
    selected=assertions.get(decision.get('selected_assertion'))
    if not selected or selected['assertion_id'] not in decision['assertion_refs'] or assertion['assertion_id'] not in decision['assertion_refs']:return 'selected assertion is not a decision member'
    if selected['review_status']!='corroborated':return 'selected assertion is not corroborated'
    if selected['subject_ref']!=assertion['subject_ref'] or selected['property_path']!=assertion['property_path']:return 'selected assertion describes another fact'
    if not set(assertion['scope']['language_versions'])<=set(selected['scope']['language_versions']) or any(assertion['scope'][k]!=selected['scope'][k] for k in ('semantic_profile_id','platform_profile_id')):return 'selected assertion does not cover requested scope'
    if decision.get('value_sha256')!=digest(selected['value']):return 'selected value differs from reviewed value'
    covered=set(decision['assertion_refs']);resolved=set(decision.get('resolves_issues',[]))
    for other in assertions.values():
        if other['subject_ref']!=assertion['subject_ref'] or other['property_path']!=assertion['property_path'] or not scopes_overlap(assertion['scope'],other['scope']):continue
        if other['assertion_id'] not in covered and (other['review_status']=='unresolved' or digest(other['value'])!=digest(selected['value'])):return 'unreviewed competing assertion: '+other['assertion_id']
        if other['assertion_id'] in covered and not set(other['issue_refs'])<=resolved:return 'unresolved competing issue: '+other['assertion_id']
    return None


def validate_registry(registry,evidence,grammar,schema=None):
    from jsonschema import Draft202012Validator
    schema=schema or read_json(ROOT/'spec/schema/registry.schema.json')
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(registry)
    assertions={a['assertion_id']:a for a in registry['assertions']}
    decisions={d['decision_id']:d for d in registry['decisions']}
    sources={s['source_id'] for s in evidence['sources']}
    for collection,key in [('assertions','assertion_id'),('decisions','decision_id'),('symbols','symbol_id'),('rules','rule_id')]:
        ids=[x[key] for x in registry[collection]]
        if len(ids)!=len(set(ids)):raise ValueError('SPEC_IDENTITY: duplicate '+key)
    for assertion in registry['assertions']:
        if not set(assertion['evidence_refs'])<=sources:raise ValueError('SPEC_EVIDENCE: dangling source')
        decision=decisions.get(assertion['decision_ref'])
        if assertion['review_status']=='corroborated' and (not decision or decision['status']!='accepted'):
            raise ValueError('SPEC_DECISION: effective fact requires an accepted decision')
        if assertion['review_status']=='unresolved' and assertion['decision_ref']:
            raise ValueError('SPEC_DECISION: unresolved assertion cannot have an active decision')
        if decision and assertion['assertion_id'] not in decision['assertion_refs']:
            raise ValueError('SPEC_DECISION: decision does not cover assertion')
        if decision and decision['status']=='accepted':
            if not all(decision.get(k) for k in ('author','reviewer','date','rationale','test_refs')):
                raise ValueError('SPEC_REVIEW: accepted decision needs author/reviewer/date/rationale/tests')
            selected=assertions.get(decision['selected_assertion'])
            if not selected or selected['subject_ref']!=assertion['subject_ref'] or selected['property_path']!=assertion['property_path']:
                raise ValueError('SPEC_DECISION: selected assertion describes another fact')
            if decision.get('value_sha256')!=digest(selected['value']):
                raise ValueError('SPEC_DECISION: changed value has no matching review decision')
        if assertion['issue_refs'] and assertion['review_status']=='corroborated':
            if not decision.get('resolves_issues') or not set(assertion['issue_refs'])<=set(decision['resolves_issues']):
                raise ValueError('SPEC_UNRESOLVED: active fact has unresolved competing evidence')
        if assertion['review_status']=='corroborated':
            problem=resolution_problem(assertion,registry)
            if problem:raise ValueError('SPEC_UNRESOLVED: '+problem)
    owned_overloads=set();owned_parameters=set();owned_signatures=set()
    for symbol in registry['symbols']:
        for overload in symbol['overloads']:
            oid=overload['overload_id']
            if oid in owned_overloads:raise ValueError('SPEC_IDENTITY: duplicate overload_id '+oid)
            owned_overloads.add(oid)
            if overload['signature_assertion'] not in assertions:raise ValueError('SPEC_SIGNATURE: missing assertion')
            claim=assertions[overload['signature_assertion']]
            if claim['subject_ref']!=oid or claim['property_path']!='signature' or claim['assertion_id'] in owned_signatures:raise ValueError('SPEC_IDENTITY: signature owner mismatch')
            owned_signatures.add(claim['assertion_id']);signature=claim['value']
            ids=[p['parameter_id'] for p in signature['parameters']]
            if len(ids)!=len(set(ids)) or set(ids)&owned_parameters:raise ValueError('SPEC_IDENTITY: repeated parameter')
            if any(not p['parameter_id'].startswith('parameter.'+oid+'.') for p in signature['parameters']):raise ValueError('SPEC_IDENTITY: parameter owner mismatch')
            owned_parameters.update(ids)
    live=set(assertions)|set(decisions)|{s['symbol_id'] for s in registry['symbols']}|{r['rule_id'] for r in registry['rules']}|owned_overloads|owned_parameters
    retired=[t if isinstance(t,str) else t.get('id') for t in registry['tombstones']]
    if None in retired or len(retired)!=len(set(retired)) or set(retired)&live:raise ValueError('SPEC_IDENTITY: invalid or reused tombstone')
    if grammar.get('format')!='pine-wiki.pratt-grammar.1':raise ValueError('Unsupported grammar format')
    return True


def effective(assertion,registry,version=None,profile_id=None):
    problem=resolution_problem(assertion,registry,version,profile_id)
    if problem:return {'kind':'unknown','reason':'SPEC_UNRESOLVED','detail':problem,'assertion_ref':assertion['assertion_id'],'issue_refs':assertion['issue_refs']}
    decision=next(d for d in registry['decisions'] if d['decision_id']==assertion['decision_ref'])
    selected=next(a for a in registry['assertions'] if a['assertion_id']==decision['selected_assertion'])
    return copy.deepcopy(selected['value'])


def validate_identities(identities):
    aliases=identities['aliases'];params=identities['parameters']
    entries={a['entry_id']:a for a in aliases}
    if len(entries)!=len(aliases):raise ValueError('SPEC_IDENTITY: duplicate entry alias')
    owners={}
    for a in aliases:
        oid=a['overload_id'];owner=(a['symbol_id'],a['language_version'])
        if oid in owners and owners[oid]!=owner:raise ValueError('SPEC_IDENTITY: alias overload owner mismatch')
        owners[oid]=owner
    ids=set();logical=set();parameter_owners={}
    for p in params:
        entry=entries.get(p['entry_id']);key=(p['entry_id'],p['name'])
        if not entry or key in logical:raise ValueError('SPEC_IDENTITY: duplicate or dangling parameter alias')
        owner=(entry['overload_id'],p['name'],entry['language_version'])
        if p['parameter_id'] in parameter_owners and parameter_owners[p['parameter_id']]!=owner:raise ValueError('SPEC_IDENTITY: alias parameter reused by another owner')
        parameter_owners[p['parameter_id']]=owner
        if not p['parameter_id'].startswith('parameter.'+entry['overload_id']+'.'):raise ValueError('SPEC_IDENTITY: alias parameter owner mismatch')
        ids.add(p['parameter_id']);logical.add(key)
    live=set(entries)|set(owners)|ids|{a['symbol_id'] for a in aliases}
    retired=[t if isinstance(t,str) else t.get('id') for t in identities['tombstones']]
    if None in retired or len(retired)!=len(set(retired)) or set(retired)&live:raise ValueError('SPEC_IDENTITY: reused alias tombstone')
    return True


def export_bundle(destination,source_commit=None,registry=None,evidence=None,grammar=None):
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    registry=registry or read_json(ROOT/'spec/registry.json')
    evidence=evidence or read_json(ROOT/'spec/evidence.json')
    grammar=grammar or read_json(ROOT/'spec/grammar.json')
    validate_registry(registry,evidence,grammar)
    validate_identities(read_json(ROOT/'spec/identities.json'))
    semantic={'registry':semantic_projection(registry),'grammar':grammar}
    documentation={'registry':registry.get('documentation',{}),'symbols':[{ 'symbol_id':s['symbol_id'],'documentation':s.get('documentation',{})} for s in registry['symbols']]}
    evidence_view={'sources':evidence,'assertion_evidence':[{k:a[k] for k in ('assertion_id','evidence_refs','method','review_status','decision_ref')} for a in registry['assertions']],
                   'decisions':registry['decisions'],'examples':read_json(ROOT/'spec/examples.json'),'probe_definitions':read_json(ROOT/'spec/probes.json'),'probe_runs':read_json(ROOT/'spec/probe-runs.json')}
    evidence_view['artifacts']={run['artifact']:read_json(ROOT/run['artifact']) for run in evidence_view['probe_runs']['runs']}
    evidence_view['probe_schemas']={name:read_json(ROOT/f'spec/schema/probe-{name}.schema.json') for name in ('definition','run')}
    evidence_view['rule_evidence']=[{k:r.get(k,[]) for k in ('rule_id','evidence_refs','test_refs')} for r in registry['rules']]
    evidence_view['source_preservation']=read_json(ROOT/'spec/source-preservation.json')
    evidence_view['material_notices']={name:(ROOT/name).read_text(encoding='utf8') for name in ('LICENSE','NOTICE','THIRD_PARTY.md')}
    files={'semantic.json':semantic,'documentation.json':documentation,'evidence.json':evidence_view,
           'registry.schema.json':read_json(ROOT/'spec/schema/registry.schema.json'),
           'identities.json':read_json(ROOT/'spec/identities.json'),
           'profile-programs.json':read_json(ROOT/'spec/profile-programs.json')}
    hashes={name:hashlib.sha256(encode(data)).hexdigest() for name,data in files.items()}
    if source_commit is None:source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    manifest={'schema_version':SCHEMA_VERSION,'catalog_revision':registry['registry_revision'],'source_commit':source_commit,
              'language_version':6,'semantic_profile_id':'pine6.core-mvp.1','platform_profiles':['historical.confirmed.1'],
              'semantic_hash':digest(semantic),'documentation_hash':digest(documentation),'evidence_hash':digest(evidence_view),
              'compatibility':{'reader_schema_major':1,'consumer_contract':'pine-wiki.resolved-program.1'},'files':hashes,
              'materials':evidence['export_policy']}
    existing=destination/'manifest.json'
    if existing.exists() and existing.read_bytes()!=encode(manifest):
        raise ValueError('IMMUTABLE_BUNDLE: use a new release directory')
    for name,data in files.items():(destination/name).write_bytes(encode(data))
    existing.write_bytes(encode(manifest))
    return manifest,hashlib.sha256(encode(manifest)).hexdigest()


def load_bundle(directory,expected_manifest_digest,profile_id='pine6.core-mvp.1'):
    directory=Path(directory)
    raw=(directory/'manifest.json').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected_manifest_digest:raise ValueError('ARTIFACT_INCOMPATIBLE: external manifest digest mismatch')
    manifest=read_json(directory/'manifest.json')
    if manifest.get('schema_version')!=SCHEMA_VERSION or manifest.get('semantic_profile_id')!=profile_id:
        raise ValueError('ARTIFACT_INCOMPATIBLE: schema or profile mismatch')
    required={'schema_version','catalog_revision','source_commit','language_version','semantic_profile_id','platform_profiles','semantic_hash','documentation_hash','evidence_hash','compatibility','files','materials'}
    if set(manifest)!=required or manifest.get('language_version')!=6 or type(manifest.get('language_version')) is not int:
        raise ValueError('ARTIFACT_INCOMPATIBLE: manifest schema or language version')
    if manifest.get('compatibility')!={'reader_schema_major':1,'consumer_contract':'pine-wiki.resolved-program.1'}:
        raise ValueError('ARTIFACT_INCOMPATIBLE: unsupported reader/consumer compatibility')
    if manifest.get('platform_profiles')!=['historical.confirmed.1']:raise ValueError('ARTIFACT_INCOMPATIBLE: unsupported platform profile')
    if set(manifest['files'])!={'semantic.json','documentation.json','evidence.json','registry.schema.json','identities.json','profile-programs.json'}:
        raise ValueError('ARTIFACT_INCOMPATIBLE: unexpected file set')
    for name,sha in manifest['files'].items():
        if hashlib.sha256((directory/name).read_bytes()).hexdigest()!=sha:
            raise ValueError('ARTIFACT_INCOMPATIBLE: file hash mismatch: '+name)
    semantic=read_json(directory/'semantic.json');evidence=read_json(directory/'evidence.json')
    profiles=semantic['registry']['profiles'];profile=next((p for p in profiles if p['semantic_profile_id']==profile_id),None)
    if not profile or profile['language_version']!=manifest['language_version'] or profile['platform_profiles']!=manifest['platform_profiles'] or semantic['registry']['registry_revision']!=manifest['catalog_revision']:
        raise ValueError('ARTIFACT_INCOMPATIBLE: manifest differs from payload profile')
    from jsonschema import Draft202012Validator
    schema=read_json(directory/'registry.schema.json');Draft202012Validator.check_schema(schema)
    reviewed=copy.deepcopy(semantic['registry']);proofs={a['assertion_id']:a for a in evidence['assertion_evidence']}
    if digest({'decisions':semantic_projection(evidence['decisions'])})!=digest({'decisions':reviewed['decisions']}):
        raise ValueError('ARTIFACT_INCOMPATIBLE: decision evidence differs from semantic selection')
    reviewed['decisions']=copy.deepcopy(evidence['decisions'])
    for a in reviewed['assertions']:a['evidence_refs']=proofs[a['assertion_id']]['evidence_refs']
    validate_registry(reviewed,evidence['sources'],semantic['grammar'],schema)
    # The external lock authenticates the schema too; semantic identity must
    # still match the actual machine payload, not only its declared file hash.
    for name,field in [('semantic.json','semantic_hash'),('documentation.json','documentation_hash'),('evidence.json','evidence_hash')]:
        if digest(read_json(directory/name))!=manifest[field]:raise ValueError('ARTIFACT_INCOMPATIBLE: identity mismatch')
    identities=read_json(directory/'identities.json');validate_identities(identities)
    return {'manifest':manifest,'semantic':semantic,'evidence':evidence,'identities':identities}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--source-commit');parser.add_argument('--write-lock',type=Path)
    args=parser.parse_args();args.output=args.output.resolve();manifest,sha=export_bundle(args.output,args.source_commit)
    if args.write_lock:
        sys.path.insert(0,str(ROOT))
        from consumer.runtime import source_identity
        args.write_lock.write_bytes(encode({'bundle':args.output.relative_to(ROOT).as_posix(),'manifest_sha256':sha,'semantic_profile_id':manifest['semantic_profile_id'],'semantic_hash':manifest['semantic_hash'],
            'implementation_commit':manifest['source_commit'],'consumer_source_sha256':source_identity()}))
    print(json.dumps({'manifest_sha256':sha,'semantic_hash':manifest['semantic_hash']}))


if __name__=='__main__':main()
