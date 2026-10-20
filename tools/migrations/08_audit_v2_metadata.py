#!/usr/bin/env python3
"""Separate content/source/run metadata without rewriting captured prose/code."""
import copy, hashlib, json
from catalog_io import ROOT, load_catalog, save_catalog


SECTIONS = {
 'switch-bool': ('language/conditional-structures/', 'switch-structure', 'switch structure'),
 'footprint': ('concepts/other-timeframes-and-data/', 'requestfootprint', 'request.footprint()'),
 'once-confirmed': ('language/conditional-structures/', 'once-structure', 'once structure'),
 'line-wrapping': ('language/script-structure/', 'line-wrapping', 'Line wrapping'),
 'isin': ('concepts/chart-information/', 'symbol-information', 'Symbol information'),
 'scope': ('language/variable-declarations/', 'shadowing', 'Shadowing'),
 'loop-return': ('language/loops/', 'keywords-and-return-expressions', 'Keywords and return expressions'),
 'overload': ('language/user-defined-functions/', 'function-overloading', 'Function overloading'),
 'method-overload': ('language/methods/', 'method-overloading', 'Method overloading'),
 'rsi-contracts': ('v5/migration-guides/to-pine-version-5/', 'removed-an-rsi-overload', 'Removed an rsi overload'),
 'lookahead-5': ('concepts/other-timeframes-and-data/', 'lookahead', 'Lookahead'),
 'lookahead-6': ('concepts/other-timeframes-and-data/', 'lookahead', 'Lookahead'),
}


def main():
    catalogs = {v:load_catalog(ROOT,v) for v in range(1,7)}
    path=ROOT/'tools/migrations/audit_20261020_examples.json'
    manifest=json.loads(path.read_text(encoding='utf8'))
    definitions=[]
    for index, record in enumerate(manifest['items']):
        version=record['version']; catalog=catalogs[version][0]
        # Explicit identities fix hour and document dual method/function links.
        exact=[]
        for target in record['targets']:
            if target.startswith('id:'):
                exact.append(target)
            else:
                exact.extend('id:'+e['id'] for e in catalog['entries'] if e['name']==target)
        record['targets']=exact
        record.setdefault('example_id', 'example.audit.'+record.get('id',f'source-{index+1}'))
        record['language_version']=version
        record['source_documentation_version']=3 if version==2 else 5 if record.get('id')=='rsi-contracts' else 6 if record.get('id') in SECTIONS else version
        record['version_directive']=version
        record['expected_origin']='editorial_documentation_expectation' if record['origin']=='editorial_probe' else 'source_documentation'
        record['oracle_status']='specific_expected_not_observed'
        if record.get('id') in SECTIONS:
            url,anchor,section=SECTIONS[record['id']]
            record['source'].update(url='https://www.tradingview.com/pine-script-docs/'+url+'#'+anchor, section=section, anchor=anchor)
        claim={'section':record['source'].get('section'),'code_sha256':record['code_sha256'],'expected':record['expected_result']}
        record['source']['claim_sha256']=hashlib.sha256((json.dumps(claim,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
        record['source']['claim_hash_kind']='editorial claim identity; not an upstream source-text digest'
        bindings=[{'entry_id':t[3:], 'relation':'occurrence' if ':methods:' in t or not any(m[3:].replace(':methods:',':functions:')==t[3:] for m in exact if ':methods:' in m) else 'related',
                   'language_version':version} for t in exact]
        definitions.append({**copy.deepcopy(record), 'bindings':bindings})
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
    lookup={item['code_sha256']:item for item in definitions}
    for version,(catalog,wrapper) in catalogs.items():
        for e in catalog['entries']:
            for p in e['parameters']:
                if (version,e['name'],p['name']) in ((1,'study','precision'),(6,'max_bars_back','var')):
                    text=catalog['texts'][p['description']]
                    text['content_provenance']={'kind':'primary_source','method':'saved_primary_field_attribution','reviewed_on':'2026-10-20',
                        'evidence':[{'entry_id':e['id'],'field':'parameters.'+p['name']+'.description','source':e['sources'][0],
                                     'original_sha256':hashlib.sha256(text['original'].encode()).hexdigest()}]}
            for item in e['examples']['items']:
                definition=lookup.get(item['code_sha256'])
                if definition:
                    for key in ('example_id','source','source_documentation_version','language_version','version_directive','expected_origin','oracle_status'):
                        item[key]=copy.deepcopy(definition[key])
                    item['documentation_version']=definition['source_documentation_version']
                    item['binding']=next(b for b in definition['bindings'] if b['entry_id']==e['id'])
                else:
                    item['oracle_status']='legacy_metadata_not_test_oracle'
                    item['language_version']=item.get('version_directive') or e['examples']['version']
                    item.setdefault('source_documentation_version',item.get('documentation_version'))
            if version==6:
                for issue in catalog.get('source_issues',[]):
                    if issue['id']=='SOURCE.GAP.V6.REQUEST_SECURITY_UNIQUE_LIMIT_PLAN':
                        issue['verification_events']=[
                            {'kind':'saved_snapshot_review','date':'2026-10-17','status':'reviewed','subject':'captured source issue; no new runtime validation'},
                            {'kind':'current_page_review','date':'2026-10-20','status':'reviewed','subject':'40/64 unique request calls by plan','source':issue['card_source']},
                            {'kind':'runtime_observation','date':None,'status':'not_performed','subject':'platform request limit'}]
                        issue['review']['scope_note']='Legacy review describes the saved snapshot only; see verification_events for the current-page review.'
                        proof=json.loads((ROOT/'spec/evidence.json').read_text(encoding='utf8'))
                        source=next(s for s in proof['sources'] if s['source_id']=='source.limits')
                        issue['verification_events'][1]['snapshot_sha256']=source['snapshot_sha256']
        save_catalog(catalog,wrapper)
    out=ROOT/'spec/examples.json';out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'schema_version':'1.0.0','examples':definitions,'legacy_bindings_policy':'legacy_metadata_not_test_oracle'},ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
    print('19 example definitions; exact typed bindings; independent content/source metadata')


if __name__=='__main__':main()
