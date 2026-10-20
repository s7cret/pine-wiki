"""Independent expectations for the audit counterexamples, not Pine oracle receipts."""
import copy,hashlib,json,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT),str(ROOT/'tools')]
from test_spec import SpecGates
from spec_bundle import read_json,encode,digest,export_bundle,load_bundle,validate_registry,effective,validate_identities
from project_spec import project_catalog,project_history,coverage,implementation_coverage
from spec_review import impact,queue_source
from probe_contracts import run_status_consistent,run_applies,definition_digest
from consumer.frontend import Frontend
from consumer.runtime import Runtime,lower,DEFAULT_OPERATIONS,implemented_operations
from consumer.errors import Diagnostic


class AuditRegressions(unittest.TestCase):
    setUpClass=classmethod(SpecGates.setUpClass.__func__)
    tearDownClass=classmethod(SpecGates.tearDownClass.__func__)
    compile=SpecGates.compile
    run_source=SpecGates.run_source
    export=SpecGates.export
    reviewed_change=SpecGates.reviewed_change
    assertDiagnostic=SpecGates.assertDiagnostic

    def test_N01_array_modulo_bool(self):
        for offset,expected in [(-3,1),(-1,3),(0,1),(2,3)]:
            _,out=self.run_source(f'plot(array.get(array.from(1,2,3),{offset}),"value")')
            self.assertEqual(out['plots']['value'],[expected]*4)
        for offset in (-4,3):self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.run_source(f'plot(array.get(array.from(1,2,3),{offset}))'))
        self.assertEqual(self.run_source('plot(-1 % 100,"value")')[1]['plots']['value'],[99]*4)
        self.assertEqual(self.run_source('plot(1 % -100,"value")')[1]['plots']['value'],[-99]*4)
        self.assertEqual(self.run_source('bool b=false\nplot(b[1]==false?1:0,"value")')[1]['plots']['value'],[1]*4)
        self.assertEqual(self.run_source('plot(close[1],"value")')[1]['plots']['value'],[None,10,20,30])

    def test_N02_declared_type_and_qualifiers(self):
        resolved,out=self.run_source('float x=1.0\nx:=2\nx:=2.5\nplot(x,"value")')
        self.assertEqual(out['plots']['value'],[2.5]*4)
        self.assertTrue(all(type(v) is float for v in out['plots']['value']))
        for body in ('int length=1\nif close>20\n    length:=2\nplot(ta.ema(close,length))',
                     'int length=1\nplot(ta.ema(close,length))\nlength:=2'):
            self.assertEqual(self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile(body))['rule_id'],'rule.types')
        self.compile('int length=3\nplot(ta.ema(close,length))')
        # Mutating a shadowed local must not strengthen the unrelated outer binding.
        self.compile('int length=3\nif true\n    int length=1\n    length:=2\nplot(ta.ema(close,length))')

    def test_N03_language_rejections(self):
        for body in ('x=na','x=indicator("Bad")','plot(1[1])','plot(true<false?1:0)','foo.bar=1','float x=1.0\nfloat x:=2.0'):
            with self.subTest(body=body):
                d=self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile(body))
                for key in ('rule_id','source_span','evidence_refs','decision_ref'):self.assertTrue(d[key],d)
        for body in ('float x=na\nplot(x)','x=float(na)\nplot(x)','plot(close[1])','x=1\nx:=2\nplot(x)'):
            self.compile(body)

    def test_N04_request_constant_capture(self):
        literal=self.run_source('plot(request.security(syminfo.tickerid,"120",ta.ema(close,3),calc_bars_count=20),"value")')[1]
        captured=self.run_source('int n=3\nplot(request.security(syminfo.tickerid,"120",ta.ema(close,n),calc_bars_count=20),"value")')[1]
        self.assertEqual(literal['plots'],captured['plots']);self.assertEqual(captured['plots']['value'],[None,20,20,30])
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:self.compile('x=close\nplot(request.security(syminfo.tickerid,"120",x,calc_bars_count=20))'),reason='PROFILE_UNCOVERED')

    def test_N05_competing_facts_and_scope(self):
        aid='assertion.rule.request.lookahead.default.semantics'
        r=copy.deepcopy(self.registry);a=next(a for a in r['assertions'] if a['assertion_id']==aid)
        other=copy.deepcopy(a);other.update(assertion_id='assertion.audit.competitor',review_status='unresolved',decision_ref=None)
        other['value']['active_default']['symbol_ref']='barmerge.lookahead_on';r['assertions'].append(other)
        with self.assertRaisesRegex(ValueError,'SPEC_UNRESOLVED'):validate_registry(r,self.evidence,self.grammar)
        self.assertEqual(effective(a,r)['kind'],'unknown')
        other['scope']['language_versions']=[1]
        self.assertTrue(validate_registry(r,self.evidence,self.grammar))
        d=next(d for d in r['decisions'] if d['decision_id']==a['decision_ref']);d['selected_assertion']=other['assertion_id'];d['value_sha256']=digest(other['value'])
        with self.assertRaises(ValueError):validate_registry(r,self.evidence,self.grammar)
        self.assertEqual(effective(a,r)['kind'],'unknown')

    def test_N06_global_identity(self):
        r=copy.deepcopy(self.registry);s=next(s for s in r['symbols'] if s['name']=='math.round');s['overloads'][0]['overload_id']='overload.math.abs.number'
        with self.assertRaisesRegex(ValueError,'SPEC_IDENTITY'):validate_registry(r,self.evidence,self.grammar)
        r=copy.deepcopy(self.registry);s=next(s for s in r['symbols'] if s['name']=='math.abs');r['tombstones']=[{'id':s['overloads'][0]['overload_id']}]
        with self.assertRaisesRegex(ValueError,'SPEC_IDENTITY'):validate_registry(r,self.evidence,self.grammar)
        ids=read_json(ROOT/'spec/identities.json');ids['aliases'].append(copy.deepcopy(ids['aliases'][0]))
        with self.assertRaisesRegex(ValueError,'SPEC_IDENTITY'):validate_identities(ids)
        ids=read_json(ROOT/'spec/identities.json');ids['parameters'][0]['parameter_id']='parameter.another.owner'
        with self.assertRaisesRegex(ValueError,'SPEC_IDENTITY'):validate_identities(ids)

    def test_N07_readiness_dependencies(self):
        from catalog_io import load_catalog
        r=copy.deepcopy(self.registry);a=next(a for a in r['assertions'] if a['subject_ref']=='rule.types');a.update(review_status='unresolved',decision_ref=None)
        cat=load_catalog(ROOT,6)[0];entry=next(e for e in cat['entries'] if e['name']=='math.abs')
        cat={'version':6,'entries':[entry],'source_issues':[]};project_catalog(cat,r,read_json(ROOT/'spec/identities.json'))
        contract=entry['semantic_contract'];self.assertEqual(contract['signature_status'],'resolved');self.assertEqual(contract['status'],'unresolved')
        self.assertIn('rule.types',[d['rule_id'] for d in contract['unresolved_dependencies']])
        h={'families':{'sample':{'versions':[{'version':6,'entry_ids':[entry['id']]}]}}}
        self.assertEqual(project_history(h,{6:cat})['families']['sample']['versions'][0]['semantic_contracts'][0],contract)

    def test_N08_decision_impact_and_full_cycle(self):
        before=copy.deepcopy(self.registry);a=next(a for a in before['assertions'] if a['subject_ref']=='overload.request.security.expression')
        alt=copy.deepcopy(a);alt['assertion_id']='assertion.audit.alternative.gaps';next(p for p in alt['value']['parameters'] if p['name']=='gaps')['default']['symbol_ref']='barmerge.gaps_on'
        before['assertions'].append(alt);d=next(d for d in before['decisions'] if d['decision_id']==a['decision_ref']);d['assertion_refs'].append(alt['assertion_id']);d['alternatives'].append({'assertion_ref':alt['assertion_id'],'reason':'synthetic reviewed alternative'})
        after=copy.deepcopy(before);d=next(d for d in after['decisions'] if d['decision_id']==a['decision_ref']);d['selected_assertion']=alt['assertion_id'];d['value_sha256']=digest(alt['value'])
        self.assertTrue(validate_registry(before,self.evidence,self.grammar));self.assertTrue(validate_registry(after,self.evidence,self.grammar))
        change=impact(before,after,read_json(ROOT/'spec/profile-programs.json'))
        self.assertIn('request',change['affected_programs']);self.assertIn('probe.mvp.request',change['affected_probes']);self.assertTrue(change['changed_decision_refs'])
        metadata=copy.deepcopy(before);metadata['decisions'][0]['reviewer']='another reviewer'
        self.assertFalse(impact(before,metadata,read_json(ROOT/'spec/profile-programs.json'))['semantic_changed'])
        # Source queue -> review -> actual regression -> new bundle; original remains byte-identical.
        queued=queue_source(read_json(ROOT/'spec/workflow.json'),self.evidence,'source.types',b'audit synthetic upstream revision')
        self.assertEqual(queued['upstream_queue'][-1]['activation'],'none')
        old=self.path/'manifest.json';old_bytes=old.read_bytes()
        evidence=copy.deepcopy(self.evidence);source=next(s for s in evidence['sources'] if s['source_id']=='source.types')
        source['snapshot_sha256']=queued['upstream_queue'][-1]['candidate_sha256']
        source['review_events'].append({'kind':'synthetic_test_review','status':'reviewed','date':'2026-10-20','runtime_observation':False})
        _,bundle=self.export('audit-update-cycle',after,evidence)
        self.assertEqual(next(s for s in bundle['evidence']['sources']['sources'] if s['source_id']=='source.types')['snapshot_sha256'],source['snapshot_sha256'])
        result=self.run_source('plot(request.security(syminfo.tickerid,"120",close,calc_bars_count=20),"value")',bundle)[1]
        self.assertEqual(result['plots']['value'],[None,20,None,40]);self.assertEqual(old.read_bytes(),old_bytes)

    def test_N09_manifest_compatibility(self):
        for key,value in [('language_version',5),('compatibility',{'reader_schema_major':999,'consumer_contract':'pine-wiki.resolved-program.1'}),('compatibility',{'reader_schema_major':1,'consumer_contract':'future.contract.999'}),('platform_profiles',['future'])]:
            with self.subTest(key=key,value=value):
                with tempfile.TemporaryDirectory(dir=self.work) as tmp:
                    dest=Path(tmp);export_bundle(dest,source_commit='139453f352d95cc54e4b658b2bf02643aeea0c5e')
                    m=read_json(dest/'manifest.json');m[key]=value;(dest/'manifest.json').write_bytes(encode(m));pin=hashlib.sha256((dest/'manifest.json').read_bytes()).hexdigest()
                    with self.assertRaisesRegex(ValueError,'ARTIFACT_INCOMPATIBLE'):load_bundle(dest,pin)
        old=ROOT/'bundles/pine6.core-mvp.1-20261020.r1';pin=hashlib.sha256((old/'manifest.json').read_bytes()).hexdigest();load_bundle(old,pin)

    def test_N10_output_ids_and_context(self):
        _,out=self.run_source('plot(close,"same")\nplot(open,"same")')
        self.assertEqual(len(out['outputs']),2);self.assertEqual(len(out['plots']),2)
        self.assertEqual([x['title'] for x in out['outputs']],['same','same'])
        self.assertEqual([x['values'] for x in out['outputs']],[[10,20,30,40],[9.5,10,20,30]])
        context=copy.deepcopy(self.context);del context['context_id']
        d=self.assertDiagnostic('CONTEXT_UNAVAILABLE',lambda:self.run_source('plot(close)',context=context));self.assertIn('context_id',d['message'])

    def test_N11_observed_date(self):
        value=next(a['value'] for a in self.registry['assertions'] if a['subject_ref']=='rule.platform.request.unique')
        self.assertNotIn('effective_from',value);self.assertIsNone(value['platform_effective_from']);self.assertEqual(value['observed_on'],'2026-10-20')

    def test_N12_operation_coverage(self):
        stats=implementation_coverage(self.registry);self.assertEqual((stats['numerator'],stats['denominator']),(10,10));self.assertFalse(stats['missing'])
        changed=implementation_coverage(self.registry,implemented_operations()-{'series.ema'})
        self.assertEqual(changed['numerator'],9);self.assertEqual(changed['missing'],['series.ema']);self.assertIn('ema',changed['affected_programs'])
        self.assertEqual(implemented_operations(),DEFAULT_OPERATIONS)

    def test_N14_receipt_consistency_and_static_rejection(self):
        from jsonschema import Draft202012Validator,ValidationError
        run=copy.deepcopy(read_json(ROOT/'spec/probe-runs.json')['runs'][0]);run['compiler']['status']='error'
        self.assertFalse(run_status_consistent(run))
        with self.assertRaises(ValidationError):Draft202012Validator(read_json(ROOT/'spec/schema/probe-run.schema.json')).validate(run)
        original=coverage(self.registry,read_json(ROOT/'spec/examples.json'),{'runs':[]})
        fake=coverage(self.registry,read_json(ROOT/'spec/examples.json'),{'runs':[run]})
        self.assertEqual(original['independently_probed_rules'],fake['independently_probed_rules'])
        d=self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile('plot(ta.ema(close,0+0))'));self.assertEqual(d['rule_id'],'rule.ema.length')
        expected={'category':'LANGUAGE_INVALID','phase':'compile','rule_id':'rule.types','source_span':{'line':3,'column':1}}
        definition={'comparator':{'kind':'diagnostic'},'expected':expected}
        run['runtime']['status']='not_executed';run['comparison']={'passed':True,'diagnostic':expected}
        self.assertTrue(run_status_consistent(run,definition));self.assertFalse(run_status_consistent(run))

    def test_original_published_evidence_is_preserved(self):
        base='6091d1802b0ceecaf3b50daab064ddb50ed2c797'
        for filename,key,id_key in [('spec/probes.json','definitions','definition_id'),('spec/probe-runs.json','runs','run_id')]:
            old=json.loads(subprocess.check_output(['git','show',base+':'+filename],cwd=ROOT))
            current={record[id_key]:record for record in read_json(ROOT/filename)[key]}
            for record in old[key]:self.assertEqual(digest(current[record[id_key]]),digest(record),record[id_key])
        files=subprocess.check_output(['git','ls-tree','-r','--name-only',base,'--','bundles/pine6.core-mvp.1-20261020.r1','spec/run-artifacts'],cwd=ROOT,text=True).splitlines()
        for name in files:self.assertEqual((ROOT/name).read_bytes(),subprocess.check_output(['git','show',base+':'+name],cwd=ROOT),name)


del SpecGates
if __name__=='__main__':unittest.main(verbosity=2)
