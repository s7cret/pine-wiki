"""Read-only semantic diff and an explicit queue for reviewed upstream updates."""
import argparse,copy,hashlib,json
from pathlib import Path
from spec_bundle import ROOT,read_json,encode,digest,semantic_projection,effective


def impact(before,after,programs):
    old={a['assertion_id']:a for a in before['assertions']}
    new={a['assertion_id']:a for a in after['assertions']}
    changed=sorted(i for i in old.keys()|new.keys() if digest(semantic_projection(old.get(i,{})))!=digest(semantic_projection(new.get(i,{}))) or digest(effective(old[i],before) if i in old else {})!=digest(effective(new[i],after) if i in new else {}))
    old_decisions={d['decision_id']:d for d in before['decisions']};new_decisions={d['decision_id']:d for d in after['decisions']}
    changed_decisions=sorted(i for i in old_decisions.keys()|new_decisions.keys() if digest(semantic_projection(old_decisions.get(i,{})))!=digest(semantic_projection(new_decisions.get(i,{}))))
    changed=sorted(set(changed)|{a['assertion_id'] for a in after['assertions'] if a.get('decision_ref') in changed_decisions})
    subjects=sorted({a['subject_ref'] for i in changed for a in [old.get(i),new.get(i)] if a})
    symbols=sorted(s['symbol_id'] for s in after['symbols'] if s.get('value_assertion_ref') in changed or any(o['signature_assertion'] in changed for o in s['overloads']))
    rules=sorted(r['rule_id'] for r in after['rules'] if r['semantic_assertion'] in changed)
    dependencies=programs['transitive_dependencies']
    affected=bool(set(symbols)&set(dependencies['symbol_refs']) or set(rules)&set(dependencies['rule_refs']))
    definitions=read_json(ROOT/'spec/probes.json')['definitions']
    affected_overloads={o['overload_id'] for s in after['symbols'] if s['symbol_id'] in symbols for o in s['overloads']}
    return {'semantic_changed':digest(semantic_projection(before))!=digest(semantic_projection(after)),
            'changed_assertion_refs':changed,'changed_decision_refs':changed_decisions,'subjects':subjects,'symbol_refs':symbols,'rule_refs':rules,
            'affected_programs':[p['program_id'] for p in programs['programs']] if affected else [],
            'affected_probes':sorted(d['definition_id'] for d in definitions if set(d['rule_refs'])&set(rules) or set(d['overload_refs'])&affected_overloads),
            'impact_precision':'conservative profile closure; no claim of call-level dependency minimization'}


def queue_source(workflow,evidence,source_id,snapshot):
    source=next(s for s in evidence['sources'] if s['source_id']==source_id)
    sha=hashlib.sha256(snapshot).hexdigest();old=source.get('snapshot_sha256')
    out=copy.deepcopy(workflow)
    if sha!=old and not any(q['source_id']==source_id and q['candidate_sha256']==sha for q in out['upstream_queue']):
        out['upstream_queue'].append({'source_id':source_id,'previous_sha256':old,'candidate_sha256':sha,'status':'pending_review',
            'activation':'none','required_review':['scope','semantic diff','tests','decision with value hash','reviewer and rationale']})
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--before',type=Path);p.add_argument('--after',type=Path,default=ROOT/'spec/registry.json');p.add_argument('--queue-source');p.add_argument('--snapshot',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    if a.queue_source:
        if not a.snapshot or not a.output:p.error('--queue-source requires --snapshot and --output; canonical data is never overwritten')
        result=queue_source(read_json(ROOT/'spec/workflow.json'),read_json(ROOT/'spec/evidence.json'),a.queue_source,a.snapshot.read_bytes())
    elif a.before:result=impact(read_json(a.before),read_json(a.after),read_json(ROOT/'spec/profile-programs.json'))
    else:p.error('choose --before or --queue-source')
    if a.output:a.output.write_bytes(encode(result))
    else:print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
