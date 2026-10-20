"""Integration gates for the actual offline compiler/lowering/runtime consumer."""
import copy,hashlib,importlib.util,json,math,socket,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from jsonschema import Draft202012Validator,ValidationError

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'tools/migrations'))
from spec_bundle import read_json,encode,digest,export_bundle,load_bundle,semantic_projection,validate_registry
from project_spec import project_catalog,project_history,coverage
from semantic_contracts import contract_errors
from content_provenance import classify_content
from probe_contracts import definition_digest,run_applies
from spec_review import impact,queue_source
from catalog_io import load_catalog
from consumer.errors import Diagnostic
from consumer.frontend import Frontend
from consumer.runtime import Runtime,lower,DEFAULT_OPERATIONS,StatePhases,boolean_evaluation


class SpecGates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory(prefix='spec-gates-',dir=ROOT/'.runtime');cls.work=Path(cls.temp.name)
        cls.registry=read_json(ROOT/'spec/registry.json');cls.evidence=read_json(ROOT/'spec/evidence.json');cls.grammar=read_json(ROOT/'spec/grammar.json')
        cls.path=cls.work/'base';cls.manifest,cls.pin=export_bundle(cls.path,source_commit='139453f352d95cc54e4b658b2bf02643aeea0c5e')
        cls.bundle=load_bundle(cls.path,cls.pin);cls.context=read_json(ROOT/'spec/fixtures/context.json')

    @classmethod
    def tearDownClass(cls):cls.temp.cleanup()

    def compile(self,body,bundle=None):return Frontend(bundle or self.bundle).compile('//@version=6\nindicator("Test")\n'+body+'\n'+('plot(0)\n' if 'plot(' not in body else ''))
    def run_source(self,body,bundle=None,context=None):
        bundle=bundle or self.bundle;resolved=self.compile(body,bundle)
        return resolved,Runtime(bundle).run(lower(resolved),copy.deepcopy(context or self.context))

    def export(self,name,registry=None,evidence=None,grammar=None):
        dest=self.work/name;m,pin=export_bundle(dest,source_commit='139453f352d95cc54e4b658b2bf02643aeea0c5e',registry=registry,evidence=evidence,grammar=grammar)
        return m,load_bundle(dest,pin)

    def reviewed_change(self,registry,aid,change):
        a=next(a for a in registry['assertions'] if a['assertion_id']==aid);change(a['value'])
        d=next(d for d in registry['decisions'] if d['decision_id']==a['decision_ref']);d['value_sha256']=digest(a['value']);d['reviewer']='synthetic test fixture'

    def assertDiagnostic(self,category,operation,reason=None):
        with self.assertRaises(Diagnostic) as error:operation()
        self.assertEqual(error.exception.data['category'],category,error.exception.data)
        if reason:self.assertEqual(error.exception.data['reason'],reason)
        return error.exception.data

    def test_A01_unordered_records_and_stable_identity(self):
        r=copy.deepcopy(self.registry)
        for key in ('assertions','decisions','symbols','rules'):r[key].reverse()
        for s in r['symbols']:s['overloads'].reverse()
        self.assertEqual(digest(semantic_projection(r)),digest(semantic_projection(self.registry)))
        identity=read_json(ROOT/'spec/identities.json');self.assertEqual(len(identity['aliases']),4631)
        by={(x['category'],x['entry_id']):x for x in identity['aliases']}
        for v,name in [(4,'hour'),(6,'ta.tr'),(6,'time')]:
            variable=by[('variables',f'primary:v{v}:variables:{name}:overload:0')]
            function=by[('functions',f'primary:v{v}:functions:{name}:overload:0')]
            self.assertNotEqual(variable['symbol_id'],function['symbol_id'])

    def test_A02_translation_does_not_invalidate_semantic_cache(self):
        r=copy.deepcopy(self.registry);r['symbols'][0]['documentation']['ru']+=' Новый перевод.'
        m,b=self.export('translated',r)
        self.assertEqual(m['semantic_hash'],self.manifest['semantic_hash']);self.assertNotEqual(m['documentation_hash'],self.manifest['documentation_hash'])
        artifact=lower(self.compile('plot(math.abs(-2.5))'))
        self.assertEqual(Runtime(b).run(artifact,self.context)['semantic_hash'],m['semantic_hash'])

    def test_A03_one_reviewed_fact_changes_all_views_and_runtime(self):
        r=copy.deepcopy(self.registry);aid='assertion.overload.request.security.expression.signature'
        self.reviewed_change(r,aid,lambda value:next(p for p in value['parameters'] if p['name']=='gaps')['default'].update(symbol_ref='barmerge.gaps_on'))
        m,b=self.export('gaps-on',r);self.assertNotEqual(m['semantic_hash'],self.manifest['semantic_hash'])
        catalog,_=load_catalog(ROOT,6);target=next(e for e in catalog['entries'] if e['name']=='request.security')
        small={'version':6,'entries':[copy.deepcopy(target)],'source_issues':[]}
        projected=project_catalog(small,r,read_json(ROOT/'spec/identities.json'));contract=projected['entries'][0]['semantic_contract']
        default=next(p for p in contract['overloads'][0]['contract']['parameters'] if p['name']=='gaps')['default']
        self.assertEqual(default['symbol_ref'],'barmerge.gaps_on')
        history={'families':{'sample':{'versions':[{'version':6,'entry_ids':[target['id']]}]}}}
        self.assertEqual(project_history(history,{6:projected})['families']['sample']['versions'][0]['semantic_contracts'][0],contract)
        program=(ROOT/'spec/programs/request.pine').read_text(encoding='utf8');resolved=Frontend(b).compile(program)
        result=Runtime(b).run(lower(resolved),self.context)
        self.assertEqual(result['plots']['remote close'],[None,20.0,None,40.0])
        old=lower(Frontend(self.bundle).compile(program))
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:Runtime(b).run(old,self.context))

    def test_A04_positional_order_affects_hash_but_not_parameter_identity(self):
        r=copy.deepcopy(self.registry);a=next(a for a in r['assertions'] if a['subject_ref']=='overload.math.round.precision')
        before=[p['parameter_id'] for p in a['value']['parameters']];a['value']['parameters'].reverse()
        self.assertEqual(set(before),{p['parameter_id'] for p in a['value']['parameters']})
        self.assertNotEqual(digest(semantic_projection(r)),digest(semantic_projection(self.registry)))

    def unresolved_default_bundle(self):
        r=copy.deepcopy(self.registry)
        def change(value):
            p=next(p for p in value['parameters'] if p['name']=='calc_bars_count');p['default']={'kind':'unknown','reason':'test conflicting source','assertion_ref':'assertion.v5.request.security.calc_bars_count.default','issue_refs':['SOURCE.GAP.V5.RELEASE_2024_CALC_DEFAULT']}
        self.reviewed_change(r,'assertion.overload.request.security.expression.signature',change)
        return self.export('unresolved',r)[1]

    def test_A05_needed_unknown_is_spec_unresolved(self):
        b=self.unresolved_default_bundle();d=self.assertDiagnostic('SPEC_UNRESOLVED',lambda:self.compile('plot(request.security(syminfo.tickerid,"120",close))',b))
        self.assertEqual(d['rule_id'],'assertion.v5.request.security.calc_bars_count.default');self.assertIn('SOURCE.GAP.V5.RELEASE_2024_CALC_DEFAULT',d['issue_refs'])

    def test_A06_explicit_argument_bypasses_unused_unknown(self):
        b=load_bundle(self.work/'unresolved',hashlib.sha256((self.work/'unresolved/manifest.json').read_bytes()).hexdigest()) if (self.work/'unresolved').exists() else self.unresolved_default_bundle()
        _,out=self.run_source('plot(request.security(syminfo.tickerid,"120",close,calc_bars_count=20), "value")',b)
        self.assertEqual(out['plots']['value'],[None,20,20,40])
        self.compile('plot(math.abs(-1))',b)

    def test_A07_locked_bundle_and_consumer_are_offline(self):
        with patch.object(socket,'create_connection',side_effect=AssertionError('Network is disabled')):
            b=load_bundle(self.path,self.pin)
            self.assertEqual(self.run_source('plot(math.abs(-1),"value")',b)[1]['plots']['value'],[1]*4)

    def test_A08_missing_implementation_is_distinct(self):
        resolved=self.compile('plot(ta.ema(close,3))')
        self.assertDiagnostic('IMPLEMENTATION_MISSING',lambda:lower(resolved,DEFAULT_OPERATIONS-{'series.ema'}))

    def test_A09_context_absence_is_not_language_invalid(self):
        artifact=lower(self.compile('plot(request.security(syminfo.tickerid,"120",close,calc_bars_count=20))'))
        context=copy.deepcopy(self.context);context['requested_contexts']=[]
        d=self.assertDiagnostic('CONTEXT_UNAVAILABLE',lambda:Runtime(self.bundle).run(artifact,context));self.assertEqual(d['rule_id'],'rule.request.alignment')

    def test_A10_external_pin_schema_and_artifact_integrity(self):
        m,b=self.export('corrupt');dest=self.work/'corrupt';pin=hashlib.sha256((dest/'manifest.json').read_bytes()).hexdigest()
        semantic=read_json(dest/'semantic.json');semantic['registry']['schema_version']='999.0.0';(dest/'semantic.json').write_bytes(encode(semantic))
        manifest=read_json(dest/'manifest.json');manifest['files']['semantic.json']=hashlib.sha256((dest/'semantic.json').read_bytes()).hexdigest();(dest/'manifest.json').write_bytes(encode(manifest))
        with self.assertRaisesRegex(ValueError,'ARTIFACT_INCOMPATIBLE'):load_bundle(dest,pin)
        ir=lower(self.compile('plot(math.abs(-2.5))'));ir['ast']['statements'][0]['kind']='tampered'
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:Runtime(self.bundle).run(ir,self.context))

    def test_A11_export_is_byte_deterministic(self):
        self.export('deterministic-a');self.export('deterministic-b')
        first={p.name:p.read_bytes() for p in (self.work/'deterministic-a').iterdir()};second={p.name:p.read_bytes() for p in (self.work/'deterministic-b').iterdir()}
        self.assertEqual(first,second)

    def test_A12_successful_run_is_bound_to_definition_code_context(self):
        item={'code_sha256':'a'*64,'language_version':6,'probe_definition_hash':'b'*64,'validation_context_hash':'c'*64}
        run={'code_sha256':'a'*64,'language_version':6,'definition_hash':'b'*64,'context_hash':'c'*64,'date':'2026-10-20','data':{'fixture':'fixed'},'parameters':{},'environment':{'build':'unknown'},'artifact':'spec/run-artifacts/test.json'}
        self.assertTrue(run_applies(item,run));item['code_sha256']='d'*64;self.assertFalse(run_applies(item,run))
        item['code_sha256']='a'*64;run['context_hash']='e'*64;self.assertFalse(run_applies(item,run))

    def test_A13_hour_binding_rejects_name_ambiguity(self):
        path=ROOT/'tools/migrations/07_audit_examples.py';module_spec=importlib.util.spec_from_file_location('example_migration',path);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
        entries=[{'id':'f','name':'hour','category':'functions'},{'id':'v','name':'hour','category':'variables'}]
        with self.assertRaisesRegex(ValueError,'EXAMPLE_BINDING'):module.resolve_targets({'targets':['hour']},entries)
        self.assertEqual(module.resolve_targets({'targets':['id:f']},entries),['f'])
        c,_=load_catalog(ROOT,4);e=next(e for e in c['entries'] if e['id']=='primary:v4:variables:hour:overload:0')
        self.assertFalse(any('hour(1591012800000' in i['code'] for i in e['examples']['items']))

    def test_A14_six_complete_programs_match_independent_series(self):
        expected=read_json(ROOT/'spec/fixtures/expected.json')
        symbols=set();rules=set()
        for p in sorted((ROOT/'spec/programs').glob('*.pine')):
            with self.subTest(program=p.stem):
                resolved=Frontend(self.bundle).compile(p.read_text(encoding='utf8'));out=Runtime(self.bundle).run(lower(resolved),self.context)
                self.assertEqual(out['plots'],expected['plots'][p.stem]);symbols.update(c['symbol_id'] for c in resolved['resolved_calls']);rules.update(resolved['rule_refs'])
                for fact in resolved['resolved_calls']:self.assertEqual(fact['semantic_hash'],self.manifest['semantic_hash']);self.assertIn('source_span',fact)
        declared=self.registry['profiles'][0]
        self.assertLessEqual(symbols,set(declared['symbol_refs']));self.assertLessEqual(rules,set(declared['rule_refs']))

    def test_A15_duplicate_examples_and_placeholders_do_not_raise_rule_coverage(self):
        examples=read_json(ROOT/'spec/examples.json');runs=read_json(ROOT/'spec/probe-runs.json');a=coverage(self.registry,examples,runs)
        examples['examples'].append(copy.deepcopy(examples['examples'][0]));b=coverage(self.registry,examples,runs)
        self.assertEqual(a['independently_probed_rules'],b['independently_probed_rules'])
        self.assertEqual(classify_content({'en':'Missing description','content_status':'missing_description_notice'}),'missing')

    def test_A16_stateful_context_sequences_events_and_rollback(self):
        context=copy.deepcopy(self.context)
        for i in range(4,8):context['chart_bars'].append({'time':i*3600,'close_time':(i+1)*3600,'open':i*10.0,'high':(i+1)*10+1.0,'low':i*10-1.0,'close':(i+1)*10.0})
        context['requested_contexts'][0]['bars'] += [{'time':14400,'close_time':21600,'open':40.0,'high':61.0,'low':39.0,'close':60.0},{'time':21600,'close_time':28800,'open':60.0,'high':81.0,'low':59.0,'close':80.0}]
        body='remote = request.security(syminfo.tickerid,"120",ta.ema(close,3),calc_bars_count=20)\naligned = request.security(syminfo.tickerid,"120",close,calc_bars_count=20)\nplot(remote,"inside")\nplot(ta.ema(aligned,3),"after")'
        _,out=self.run_source(body,context=context);expected=read_json(ROOT/'spec/fixtures/expected.json')['context_contrast']
        self.assertEqual(out['plots']['inside'],expected['requested_ema_aligned']);self.assertEqual(out['plots']['after'],expected['ema_after_alignment']);self.assertNotEqual(out['plots']['inside'],out['plots']['after'])
        _,out=self.run_source('flag = bar_index > 1 and ta.ema(close,3) > 0\nplot(close)')
        events=[e for e in out['events'] if e['event']=='state_update'];self.assertEqual([e['value'] for e in events],[30.0,35.0])
        policy=next(a['value'] for a in self.registry['assertions'] if a['subject_ref']=='rule.execution.skipped_call')
        for version,expected_calls in [(5,3),(6,0)]:
            calls=[]
            for _ in range(3):boolean_evaluation(policy,version,'and',lambda:False,lambda:calls.append('state update') or True)
            self.assertEqual(len(calls),expected_calls)
        rollback=next(a['value'] for a in self.registry['assertions'] if a['subject_ref']=='rule.execution.rollback');phase=StatePhases(rollback)
        ordinary,varip=phase.update();ordinary['x']=1;varip['x']=1;ordinary,varip=phase.update();self.assertNotIn('x',ordinary);self.assertEqual(varip['x'],1)
        ordinary['x']=2;phase.commit();ordinary,varip=phase.update();self.assertEqual(ordinary['x'],2)

    def test_A17_source_grammar_scope_precedence_and_square_wrap(self):
        body='float x = 1 + 2 * 3\nif true\n    float x = 99\nplot(x,"outer")\nif true\n    x := 9\nplot(x,"assigned")\nplot(close[1],"previous")'
        _,out=self.run_source(body);self.assertEqual(out['plots']['outer'],[7.0]*4);self.assertEqual(out['plots']['assigned'],[9.0]*4);self.assertEqual(out['plots']['previous'],[None,10,20,30])
        self.compile('[\n    first,\n    second\n] = request.security(syminfo.tickerid,"120",[close,open],calc_bars_count=20)\nplot(first)')
        d=self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile('missing := 2'));self.assertEqual(d['rule_id'],'rule.scope');self.assertTrue(d['source_span']);self.assertTrue(d['evidence_refs'])
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:self.compile('strategy("No")'),reason='PROFILE_UNCOVERED')

    def test_schema_and_typed_binding_edge_cases(self):
        schema=read_json(ROOT/'spec/schema/registry.schema.json');bad=copy.deepcopy(self.registry)
        a=next(a for a in bad['assertions'] if a['property_path']=='signature');a['value']['parameters'][0]['type']={'kind':'python_eval','code':'unsafe'}
        with self.assertRaises(ValidationError):Draft202012Validator(schema).validate(bad)
        for body in ('plot(ta.ema(close,bar_index))','plot(ta.ema(close,0))','plot(ta.ema(close,-1))','plot(math.round(close,1,2))','plot(math.round(close,number=1))','plot(math.abs(unknown=1))','array.from(true,1)'):
            with self.subTest(body=body):self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile(body))
        for code in ('ta.ema(close,3)','math.round(close)','math.round(close,1)','array.from(1,2.5)','ta.tr(false)','math.abs(float(na))'):
            self.compile(code)
        tags=[{'kind':'none'},{'kind':'na'},{'kind':'literal','value':False},{'kind':'literal','value':0},{'kind':'literal','value':''},{'kind':'literal','value':None},{'kind':'unknown','reason':'not documented'}]
        self.assertEqual(len({digest(t) for t in tags}),7)

    def test_R01_semantic_spelling_not_arbitrary_substring(self):
        for value,spelling in [('true','false'),('barmerge.lookahead_on','barmerge.lookahead_off')]:
            c={'values':[value],'evidence':[{'value':value,'source_spelling':spelling,'quote':'The default is '+spelling,'text_ref':'raw'}]}
            self.assertTrue(any('DEFAULT_EVIDENCE' in e for e in contract_errors(c,{'raw':{'en':'The default is '+spelling}})))
        c={'values':['100000'],'evidence':[{'value':'100000','source_spelling':'100,000','quote':'The default is 100,000','text_ref':'raw'}]}
        self.assertFalse(list(contract_errors(c,{'raw':{'en':'The default is 100,000'}})))

    def test_R03_content_origin_is_not_translation_method(self):
        for v,name,param in [(1,'study','precision'),(6,'max_bars_back','var')]:
            c,_=load_catalog(ROOT,v);e=next(e for e in c['entries'] if e['name']==name and e['category']=='functions');p=next(p for p in e['parameters'] if p['name']==param)
            self.assertEqual(classify_content(c['texts'][p['description']]),'primary_source')
        self.assertEqual(classify_content({'original':'An editorial explanation','en':'An editorial explanation','basis':'editorial_summary'}),'editorial')
        self.assertEqual(classify_content({'original':'Unattributed text','en':'Unattributed text','basis':'editorial_translation'}),'unknown')

    def test_unreviewed_value_changes_and_unresolved_competitors_fail_gate(self):
        r=copy.deepcopy(self.registry);a=next(a for a in r['assertions'] if a['property_path']=='signature');a['value']['parameters'][0]['type']={'kind':'primitive','name':'string'}
        with self.assertRaisesRegex(ValueError,'SPEC_DECISION'):validate_registry(r,self.evidence,self.grammar)
        r=copy.deepcopy(self.registry);a=next(a for a in r['assertions'] if a['review_status']=='corroborated');a['issue_refs']=['unresolved.competing.claim']
        with self.assertRaisesRegex(ValueError,'SPEC_UNRESOLVED'):validate_registry(r,self.evidence,self.grammar)

    def test_review_queue_never_activates_changed_sources(self):
        workflow=read_json(ROOT/'spec/workflow.json')
        updated=queue_source(workflow,self.evidence,'source.types',b'changed upstream document')
        self.assertEqual(updated['upstream_queue'][-1]['status'],'pending_review')
        self.assertEqual(updated['upstream_queue'][-1]['activation'],'none')
        self.assertEqual(queue_source(updated,self.evidence,'source.types',b'changed upstream document'),updated)
        self.assertEqual(workflow,read_json(ROOT/'spec/workflow.json'))
        r=copy.deepcopy(self.registry)
        self.reviewed_change(r,'assertion.overload.math.round.precision.signature',lambda v:v['parameters'].reverse())
        change=impact(self.registry,r,read_json(ROOT/'spec/profile-programs.json'))
        self.assertTrue(change['semantic_changed']);self.assertIn('symbol.function.math.round',change['symbol_refs']);self.assertIn('round',change['affected_programs'])

    def test_rule_runtime_obligations_and_request_counter(self):
        self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.run_source('a = array.from(1,2)\nplot(array.get(a,2))'))
        self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.run_source('plot(ta.ema(close,int(0)))'))
        _,out=self.run_source('plot(math.round(-1.5),"negative")\nplot(math.round(1.25,1),"positive")')
        self.assertEqual(out['plots'],{'negative':[-1]*4,'positive':[1.3]*4})
        context=copy.deepcopy(self.context);context['chart_bars'][0]['close']=None
        _,out=self.run_source('plot(ta.ema(close,3),"value")',context=context)
        self.assertEqual(out['plots']['value'],[None,20.0,25.0,32.5])
        # Separate allocations expose argument evaluation order without prose parsing.
        resolved=self.compile('a = array.from(array.get(array.from(1),0),array.get(array.from(2),0))\nplot(array.get(a,0),"first")')
        out=Runtime(self.bundle).run(lower(resolved),self.context)
        calls=[c['call_node'] for c in resolved['resolved_calls'] if c['operation']=='collection.from']
        allocations=[e['node'] for e in out['events'] if e['event']=='allocate_array' and e['bar']==0]
        self.assertEqual(allocations,calls);self.assertEqual(out['plots']['first'],[1]*4)
        body='\n'.join('x'+str(i)+' = request.security(syminfo.tickerid,"120",close,calc_bars_count='+str(i+1)+')' for i in range(41))+'\nplot(x0)'
        program=self.compile(body)
        self.assertDiagnostic('CONTEXT_UNAVAILABLE',lambda:Runtime(self.bundle).run(lower(program),self.context))
        context=copy.deepcopy(self.context);context['plan']='ultimate'
        Runtime(self.bundle).run(lower(program),context)
        same=self.compile('a = request.security(syminfo.tickerid,"120",close)\nb = request.security(syminfo.tickerid,"120",close)\nplot(a)')
        runtime=Runtime(self.bundle);runtime.run(lower(same),self.context);self.assertEqual(len(runtime.request_keys),1)
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:self.compile('f(x) => x'),reason='PROFILE_UNCOVERED')
        self.assertDiagnostic('LANGUAGE_INVALID',lambda:Frontend(self.bundle).compile('//@version=6\nplot(1)'))
        self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile('if true\n    plot(1)'))
        self.assertDiagnostic('LANGUAGE_INVALID',lambda:self.compile('indicator("Duplicate")\nplot(1)'))
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:Frontend(self.bundle).compile('//@version=6\nindicator("No observation")'),reason='PROFILE_UNCOVERED')
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:self.compile('plot(volume)'),reason='PROFILE_UNCOVERED')
        _,out=self.run_source('plot(close > 10 ? 1 : 2.5,"mixed")\nplot(close > 10 ? close : na,"na")')
        self.assertEqual(out['plots']['mixed'],[2.5,1.0,1.0,1.0]);self.assertTrue(all(type(x) is float for x in out['plots']['mixed']))
        self.assertEqual(out['plots']['na'],[None,20.0,30.0,40.0])

    def test_probe_coverage_rejects_stale_definition_or_context(self):
        examples=read_json(ROOT/'spec/examples.json');runs=read_json(ROOT/'spec/probe-runs.json')
        baseline=coverage(self.registry,examples,runs)['independently_probed_rules']
        self.assertGreaterEqual(baseline['numerator'],1)
        changed=copy.deepcopy(runs)
        for run in changed['runs']:run['context_hash']='invalid'
        self.assertEqual(coverage(self.registry,examples,changed)['independently_probed_rules']['numerator'],0)
        changed=copy.deepcopy(runs)
        for run in changed['runs']:run['definition_hash']='invalid'
        self.assertEqual(coverage(self.registry,examples,changed)['independently_probed_rules']['numerator'],0)

    def test_footprint_access_and_counter_are_separate(self):
        policy=next(a['value'] for a in self.registry['assertions'] if a['subject_ref']=='rule.platform.footprint')
        self.assertEqual(policy['scope'],'separate_footprint_counter')
        self.assertEqual(policy['profile_status'],'uncovered')
        self.assertNotIn('rule.platform.footprint',self.registry['profiles'][0]['rule_refs'])
        self.assertDiagnostic('ARTIFACT_INCOMPATIBLE',lambda:self.compile('request.footprint(100)'),reason='PROFILE_UNCOVERED')


if __name__=='__main__':unittest.main(verbosity=2)
