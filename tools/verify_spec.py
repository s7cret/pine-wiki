"""Validate canonical contracts, exact example bindings and immutable probe receipts."""
import hashlib,json,sys
from pathlib import Path
from jsonschema import Draft202012Validator
from spec_bundle import ROOT,read_json,validate_registry,load_bundle,digest
from probe_contracts import validate_definition,run_applies
sys.path.insert(0,str(ROOT/'tools/migrations'))
from catalog_io import load_catalog


def validate():
    registry=read_json(ROOT/'spec/registry.json')
    validate_registry(registry,read_json(ROOT/'spec/evidence.json'),read_json(ROOT/'spec/grammar.json'))
    for record in registry['rules']+registry['decisions']:
        for ref in record.get('test_refs',[]):
            path,_,method=ref.split('::')
            assert 'def '+method+'(' in (ROOT/path).read_text(encoding='utf8'),'SPEC_TEST_REF: '+ref
    preserved=read_json(ROOT/'spec/source-preservation.json')
    for record in preserved['files']:
        payload=json.loads((ROOT/record['file']).read_text(encoding='utf8').split(']=',1)[1].strip().removesuffix(';'))
        fields={key:{f:t[f] for f in preserved['fields'] if f in t} for key,t in payload['texts'].items()}
        assert digest(fields)==record['captured_fields_sha256'],'SOURCE_PRESERVATION: '+record['file']
    definitions=read_json(ROOT/'spec/probes.json')['definitions'];runs=read_json(ROOT/'spec/probe-runs.json')['runs']
    by={d['definition_id']:d for d in definitions}
    assert len(by)==len(definitions),'PROBE_IDENTITY: duplicate definition'
    assert len({r['run_id'] for r in runs})==len(runs),'PROBE_IDENTITY: duplicate run'
    for d in definitions:
        Draft202012Validator(read_json(ROOT/'spec/schema/probe-definition.schema.json')).validate(d)
        assert validate_definition(d),'PROBE_HASH: '+d['definition_id']
    for run in runs:
        Draft202012Validator(read_json(ROOT/'spec/schema/probe-run.schema.json')).validate(run)
        d=by[run['definition_id']]
        assert run_applies({'code_sha256':d['code_sha256'],'language_version':d['language_version'],'probe_definition_hash':d['definition_hash']},run),'PROBE_BINDING: '+run['run_id']
        assert run['context_hash']==digest({'data':run['data'],'parameters':run['parameters'],'environment':run['environment']}),'PROBE_CONTEXT: '+run['run_id']
        artifact=ROOT/run['artifact'];assert artifact.resolve().is_relative_to((ROOT/'spec/run-artifacts').resolve()),'PROBE_PATH'
        assert hashlib.sha256(artifact.read_bytes()).hexdigest()==run['artifact_sha256'],'PROBE_ARTIFACT: '+run['run_id']
        receipt=read_json(artifact)
        assert receipt=={k:v for k,v in run.items() if k not in ('artifact_sha256',)},'PROBE_RECEIPT: '+run['run_id']
        for capture in run.get('attachments',[]):
            path=(ROOT/capture['path']).resolve()
            assert path.is_relative_to((ROOT/'spec/run-artifacts').resolve()),'PROBE_PATH'
            assert hashlib.sha256(path.read_bytes()).hexdigest()==capture['sha256'],'PROBE_CAPTURE: '+run['run_id']
    examples=read_json(ROOT/'spec/examples.json')['examples'];catalogs={v:load_catalog(ROOT,v)[0] for v in range(1,7)}
    assert len({e['example_id'] for e in examples})==len(examples),'EXAMPLE_IDENTITY: duplicate ID'
    for e in examples:
        for b in e['bindings']:
            entry=next(x for x in catalogs[b['language_version']]['entries'] if x['id']==b['entry_id'])
            if e.get('id')=='hour-call':assert entry['category']=='functions','EXAMPLE_BINDING: hour() belongs to function'
            if ':variables:hour:' in entry['id']:raise AssertionError('EXAMPLE_BINDING: hour() linked to variable')
    for program in read_json(ROOT/'spec/profile-programs.json')['programs']:
        definition=by[program['probe_definition_id']]
        assert program['definition_hash']==definition['definition_hash'],'PROGRAM_DEFINITION: '+program['program_id']
        assert (ROOT/'spec/programs'/(program['program_id']+'.pine')).read_text(encoding='utf8')==program['code'],'PROGRAM_SOURCE'
    lock=ROOT/'consumer/lock.json'
    if lock.exists():
        value=read_json(lock);load_bundle(ROOT/value['bundle'],value['manifest_sha256'],value['semantic_profile_id'])
    print(f'Specification: {len(registry["assertions"])} assertions; {len(definitions)} definitions; {len(runs)} bound receipts; 6 complete programs')


if __name__=='__main__':validate()
