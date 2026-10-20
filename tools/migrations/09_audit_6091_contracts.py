"""Reviewed, bounded corrections from the 6091d18 audit. Never rewrite r1 bundles."""
import copy,hashlib,json,sys,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from spec_bundle import read_json,encode,digest


def main():
    registry=read_json(ROOT/'spec/registry.json');evidence=read_json(ROOT/'spec/evidence.json')
    assertions={a['assertion_id']:a for a in registry['assertions']};decisions={d['decision_id']:d for d in registry['decisions']}
    test='tools/test_audit_6091.py::AuditRegressions::'
    def review(aid,update,method,source_refs=()):
        a=assertions[aid];update(a['value']);a['semantic_revision']='2'
        a['evidence_refs']=sorted(set(a['evidence_refs'])|set(source_refs))
        d=decisions[a['decision_ref']];d['value_sha256']=digest(a['value']);d['date']='2026-10-20'
        d['rationale']='6091d18 audit correction, primary documentation review and independent regression expectation; not a new TradingView execution.'
        d['test_refs']=sorted(set(d['test_refs'])|{test+method})
    sources={s['source_id'] for s in evidence['sources']}
    for key,route in [('identifiers','language/identifiers/'),('declarations','language/variable-declarations/')]:
        sid='source.audit6091.'+key
        if sid not in sources:
            url='https://www.tradingview.com/pine-script-docs/'+route
            raw=urllib.request.urlopen(url,timeout=45).read()
            evidence['sources'].append({'source_id':sid,'url':url,'source_documentation_version':6,'snapshot_sha256':hashlib.sha256(raw).hexdigest(),
                'retrieved_on':'2026-10-20','review_events':[{'kind':'primary_page_review','date':'2026-10-20','status':'reviewed','subject':key,'runtime_observation':False}]})
    review('assertion.rule.array.index.semantics',lambda v:v.update(min_inclusive='-array.size',negative_indices='relative_to_size',language_version=6),'test_N01_array_modulo_bool',['source.migration6'])
    review('assertion.rule.types.semantics',lambda v:v.update(declared_type='preserved_across_reassignment',mutable_qualifier='series',
        untyped_na_declaration='forbidden',void_assignment='forbidden',ordering_operands=['int','float'],static_expression_vocabulary=['literal','constant_name','unary','binary','conditional']),
        'test_N02_declared_type_and_qualifiers',['source.migration6','source.operators','source.audit6091.declarations'])
    review('assertion.rule.grammar.semantics',lambda v:v.update(variable_identifier='[A-Za-z_][A-Za-z_0-9]*',annotated_reassignment='forbidden'),
        'test_N03_language_rejections',['source.audit6091.identifiers','source.audit6091.declarations'])
    def observation(v):
        v.pop('effective_from',None);v.pop('date_precision',None)
        v.update(observed_on='2026-10-20',platform_effective_from=None,profile_effective_from='2026-10-20',date_semantics='Observation and own profile activation only; platform introduction is unknown.')
    review('assertion.rule.platform.request.unique.semantics',observation,'test_N11_observed_date')
    for rid,value,refs,method in [
        ('rule.numeric.modulo',{'language_version':6,'quotient':'floor','formula':'a - b * floor(a / b)','zero_divisor':'na'},['source.operators'],'test_N01_array_modulo_bool'),
        ('rule.history',{'language_version':6,'literal_history':'forbidden','missing_bool':False,'missing_numeric':'na'},['source.migration6'],'test_N01_array_modulo_bool')]:
        aid='assertion.'+rid+'.semantics';did='decision.'+rid+'.semantics'
        if aid not in assertions:
            a={'assertion_id':aid,'subject_ref':rid,'property_path':'semantics','value':value,'scope':copy.deepcopy(registry['assertions'][0]['scope']),
                'method':'manual','review_status':'corroborated','evidence_refs':refs,'issue_refs':[],'decision_ref':did,'semantic_revision':'2'}
            d={'decision_id':did,'assertion_refs':[aid],'selected_assertion':aid,'alternatives':[{'assertion_ref':aid,'reason':'documented v6 rule'}],
                'rationale':'Primary documentation and 6091d18 regression; not a Pine execution claim.','author':'Codex','reviewer':'Codex','date':'2026-10-20',
                'status':'accepted','test_refs':[test+method],'value_sha256':digest(value)}
            registry['assertions'].append(a);registry['decisions'].append(d)
            registry['rules'].append({'rule_id':rid,'semantic_assertion':aid,'applies_to':['pine6.core-mvp.1'],'version_conditions':[6],
                'argument_conditions':[],'validation_phase':'compile' if rid=='rule.history' else 'runtime','outcome':'error','kind':'semantics','evidence_refs':refs,'test_refs':[test+method]})
    dependencies={
        'ta.ema':['rule.ema','rule.ema.length'], 'ta.tr':['rule.tr.true','rule.tr.false'],
        'math.round':['rule.numeric.round'],'array.from':['rule.array.element'],'array.get':['rule.array.index'],
        'request.security':['rule.request.alignment','rule.request.chart_bars','rule.platform.request.unique','rule.request.lookahead.default']}
    registry['identity_policy']['symbol_rule_dependencies']={s['symbol_id']:dependencies.get(s['name'],[]) for s in registry['symbols']}
    registry['registry_revision']='2026-10-20.mvp.audit6091.r2'
    for s in registry['symbols']:
        for o in s['overloads']:
            if s['name'] in ('indicator','plot'):o['semantic_revision']='2'
    # Explicit harness policy; this is not TradingView's plot-handle return contract.
    registry['documentation']['en']+=' Plot is an observation harness with a void adapter result; assignment of its result is outside this profile. Actual Pine plot returns a plot ID.' if 'void adapter result' not in registry['documentation']['en'] else ''
    registry['documentation']['ru']+=' Plot здесь — адаптер наблюдений с внутренним void-результатом; присваивание его результата вне профиля. Настоящий Pine plot возвращает plot ID.' if 'адаптер наблюдений' not in registry['documentation']['ru'] else ''
    for source in evidence['sources']:
        if source['source_id']=='source.limits':source.update(observed_on='2026-10-20',platform_effective_from=None)
    for profile in registry['profiles']:
        profile['rule_refs']=sorted(set(profile['rule_refs'])|{'rule.numeric.modulo','rule.history'})
    programs=read_json(ROOT/'spec/profile-programs.json')
    programs['transitive_dependencies']['rule_refs']=sorted(set(programs['transitive_dependencies']['rule_refs'])|{'rule.numeric.modulo','rule.history'})
    schema=read_json(ROOT/'spec/schema/probe-run.schema.json')
    schema['allOf']=[
        {'if':{'properties':{'runtime':{'properties':{'status':{'enum':['executed','error']}}}}},
         'then':{'properties':{'compiler':{'properties':{'status':{'const':'compiled'}}}}}},
        {'if':{'properties':{'compiler':{'properties':{'status':{'enum':['error','not_compiled','blocked']}}}}},
         'then':{'properties':{'runtime':{'properties':{'status':{'enum':['not_executed','blocked','unknown']}}}}}}]
    workflow=read_json(ROOT/'spec/workflow.json')
    workflow['update_cycle']=['queue changed source hash without activation','review scope, competing claims and effective semantic diff','add versioned positive/negative definitions','record own regressions separately from independent Pine runs','accept explicit value-hashed decision','generate projections and impact','export new immutable bundle and lock; old bundle unchanged']
    for name,value in [('registry.json',registry),('evidence.json',evidence),('profile-programs.json',programs),('schema/probe-run.schema.json',schema),('workflow.json',workflow)]:
        (ROOT/'spec'/name).write_bytes(encode(value))
    print('Canonical audit6091 revision generated; old bundles and published receipts untouched')


if __name__=='__main__':main()
