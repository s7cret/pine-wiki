"""Append bound *own consumer* regressions; never claim independent TradingView runs."""
import copy,hashlib,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from spec_bundle import ROOT,read_json,encode,digest,export_bundle,load_bundle
from probe_contracts import definition_digest,run_status_consistent
sys.path.insert(0,str(ROOT))
from consumer.frontend import Frontend
from consumer.runtime import Runtime,lower,source_identity
from consumer.errors import Diagnostic


CASES=[
 ('untyped-na','x=na','rule.types','compile',3,1),
 ('void-initializer','x=indicator("Bad")','rule.types','compile',3,1),
 ('literal-history','plot(1[1])','rule.history','compile',3,6),
 ('bool-ordering','plot(true < false ? 1 : 0)','rule.types','compile',3,11),
 ('dotted-variable','foo.bar=1','rule.grammar','parse',3,1),
 ('annotated-reassignment','float x=1.0\nfloat x:=2.0','rule.grammar','parse',4,1),
 ('zero-ema-expression','plot(ta.ema(close,0+0))','rule.ema.length','compile',3,6),
 ('series-length','int length=1\nif close>20\n    length:=2\nplot(ta.ema(close,length))','rule.types','compile',6,6),
 ('array-low-bound','plot(array.get(array.from(1),-2))','rule.array.index','runtime',3,6),
 ('array-high-bound','plot(array.get(array.from(1),1))','rule.array.index','runtime',3,6),
]
POSITIVES=[
 ('negative-index','plot(array.get(array.from(1),-1),"value")',[1]*4,['rule.array.index']),
 ('floor-modulo','plot(-1 % 100,"value")',[99]*4,['rule.numeric.modulo']),
 ('bool-history','bool b=false\nplot(b[1]==false?1:0,"value")',[1]*4,['rule.history']),
 ('declared-float','float x=1.0\nx:=2\nx:=2.5\nplot(x,"value")',[2.5]*4,['rule.types']),
 ('request-capture','int n=3\nplot(request.security(syminfo.tickerid,"120",ta.ema(close,n),calc_bars_count=20),"value")',[None,20,20,30],['rule.request.alignment']),
]


def main():
    import tempfile
    (ROOT/'.runtime').mkdir(exist_ok=True)
    definitions=read_json(ROOT/'spec/probes.json');runs=read_json(ROOT/'spec/probe-runs.json')
    existing={d['definition_id'] for d in definitions['definitions']};context=read_json(ROOT/'spec/fixtures/context.json')
    with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as tmp:
        dest=Path(tmp);_,pin=export_bundle(dest,source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip());bundle=load_bundle(dest,pin)
        programs=[]
        for name,body,rid,phase,line,column in CASES:
            expected={'category':'LANGUAGE_INVALID','phase':phase,'rule_id':rid,'source_span':{'line':line,'column':column}}
            programs.append((name,body,[rid],expected,'diagnostic'))
        for name,body,values,refs in POSITIVES:programs.append((name,body,refs,{'plots':{'value':values}},'typed_series'))
        for name,body,refs,expected,kind in programs:
            did='probe.audit6091.'+name
            if did in existing:continue
            code='//@version=6\nindicator("Audit6091")\n'+body+'\n'+('plot(0)\n' if 'plot(' not in body else '')
            definition={'definition_id':did,'code':code,'code_sha256':hashlib.sha256(code.encode()).hexdigest(),'language_version':6,
                'rule_refs':refs,'overload_refs':[],'settings':{'profile':'pine6.core-mvp.1','purpose':'own_consumer_regression'},
                'data':{'fixture':'spec/fixtures/context.json','sha256':digest(context)},'expected':expected,
                'expected_origin':'primary documentation + explicit independent audit counterexample expectation; not derived from actual consumer result',
                'comparator':{'kind':kind,'na':'exact','absolute_tolerance':0,'relative_tolerance':0,'event_order':'exact'}}
            definition['definition_hash']=definition_digest(definition)
            compiler={'status':'compiled','diagnostic':None};runtime={'status':'not_executed','observed':None,'reason':None}
            try:
                resolved=Frontend(bundle).compile(code)
                try:out=Runtime(bundle).run(lower(resolved),copy.deepcopy(context));runtime.update(status='executed',observed={'plots':out['plots']})
                except Diagnostic as exc:runtime.update(status='error',observed=exc.data,reason=exc.data['category']);raise
            except Diagnostic as exc:
                if runtime['status']!='error':compiler={'status':'error','diagnostic':exc.data['message']}
                actual={'category':exc.data['category'],'phase':exc.data.get('phase'),'rule_id':exc.data['rule_id'],
                    'source_span':{k:exc.data['source_span'][k] for k in ('line','column')}}
                comparison={'passed':kind=='diagnostic' and actual==expected,'diagnostic':actual,'origin':'own_consumer_regression'}
            else:comparison={'passed':runtime['observed']==expected,'origin':'own_consumer_regression'}
            assert comparison['passed'],(name,comparison,expected)
            artifact='spec/run-artifacts/audit6091-'+name+'.json'
            run={'run_id':'run.consumer.audit6091.'+name+'.20261020','definition_id':did,'definition_hash':definition['definition_hash'],'code_sha256':definition['code_sha256'],
                'language_version':6,'date':datetime.now(timezone.utc).isoformat(),'environment':{'implementation':'Pine Wiki offline consumer regression','build':source_identity(),'mode':'own synthetic historical fixture'},
                'parameters':{},'data':definition['data'],'compiler':compiler,'runtime':runtime,'comparison':comparison,'artifact':artifact}
            run['context_hash']=digest({k:run[k] for k in ('data','parameters','environment')})
            assert run_status_consistent(run,definition)
            payload=encode(run);(ROOT/artifact).write_bytes(payload);run['artifact_sha256']=hashlib.sha256(payload).hexdigest()
            definitions['definitions'].append(definition);runs['runs'].append(run)
    (ROOT/'spec/probes.json').write_bytes(encode(definitions));(ROOT/'spec/probe-runs.json').write_bytes(encode(runs))
    print('Bound own-consumer corpus: 10 negative + 5 positive probes; no independent Pine coverage increment')


if __name__=='__main__':main()
