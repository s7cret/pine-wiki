#!/usr/bin/env python3
"""Import reviewed examples, with origin independent of compile/runtime status."""
import copy, hashlib, json, re
from urllib.parse import unquote
from catalog_io import ROOT, load_catalog, save_catalog


def main():
    additions = json.loads((ROOT/'tools/migrations/audit_20261020_examples.json').read_text(encoding='utf8'))
    attached = 0
    for v in range(1,7):
        c,w = load_catalog(ROOT,v)
        for e in c['entries']:
            for record in additions['items']:
                if record['version'] != v:
                    continue
                matches = any(unquote(target[3:]) == unquote(e['id']) if target.startswith('id:') else target == e['name'] for target in record['targets'])
                if not matches:
                    continue
                x = e['examples']
                if not any(i['code']==record['code'] for i in x['items']):
                    item={k:copy.deepcopy(val) for k,val in record.items() if k not in ('targets','version')}
                    item['documentation_version']=v
                    item['captured_date']='2026-10-20'
                    item['version_directive']=v
                    x['items'].append(item);attached+=1
                if x['status']=='missing':
                    x['status']='source_occurrence' if record['origin']=='official_source' else 'editorial_probe'
                x.pop('template',None);x.pop('pointers',None)
                x['version']=v
                # Preserve the original note through a separate field; its
                # former "no example" statement is no longer current.
                x.setdefault('previous_note',x.get('note'))
                x['note']={'ru':'Происхождение и статус каждого примера указаны отдельно. Импорт и статический просмотр не означают запуск.', 'en':'Origin and validation status are stated separately for each example. Import and static review do not imply execution.'}
            for item in e['examples']['items']:
                item.setdefault('origin','syntax_illustration' if e['examples']['status']=='syntax_illustration' else 'compatibility_example' if e['examples']['status']=='compatibility_example' else 'official_source')
                directive=re.search(r'(?m)^\s*//\s*@version\s*=\s*(\d+)',item['code'])
                item.setdefault('version_directive',int(directive[1]) if directive else None)
                item.setdefault('documentation_version',e['examples']['version'])
                item.setdefault('role','full_script' if directive and re.search(r'(?m)^\s*(?:indicator|study|strategy|library)\(',item['code']) else 'snippet')
                item.setdefault('code_sha256',hashlib.sha256(item['code'].encode()).hexdigest())
                item.setdefault('compilation_status','not_compiled')
                item.setdefault('execution_status','not_executed')
                item.setdefault('static_review_status','not_reviewed')
                item.setdefault('preconditions',{'ru':'Условия выполнения отдельно не проверялись.','en':'Execution preconditions have not been separately verified.'})
                item.setdefault('expected_result',{'ru':'Демонстрация из сохранённого источника; наблюдаемый результат не зарегистрирован.','en':'Captured source illustration; no observed execution result is recorded.'})
            if v==4 and e['name'] in ('min','max','avg','rising','falling'):
                changes=[]
                if e['name'] in ('min','max','avg'):
                    changes.append(('2019-12', 'В декабре 2019 release notes увеличили число аргументов до десяти. Это датированный исторический факт, а не бессрочный текущий лимит.', 'December 2019 release notes increased the argument count to ten. This is a dated historical statement, not a permanent current limit.'))
                else:
                    changes.extend([('2020-10','В октябре 2020 объявлено изменение rising/falling: для rising(close,3) приведена последовательность close[0] > close[1] > close[2] > close[3]. Современное выполнение отдельно не проверялось.','October 2020 announced a rising/falling behavior change, illustrating rising(close,3) with close[0] > close[1] > close[2] > close[3]. Current execution was not separately verified.'),('2021-01','С января 2021 release notes допускают series length для rising/falling.','January 2021 release notes added series length support for rising/falling.')])
                e['release_changes']=[{'version':4,'effective_from':date,'date_precision':'month','text':{'ru':ru,'en':en},'source':{'url':'https://www.tradingview.com/pine-script-docs/v4/release-notes/#'+{'2019-12':'december-2019','2020-10':'october-2020','2021-01':'january-2021'}[date]},'verification':'documentation_checked_runtime_not_executed'} for date,ru,en in changes]
            if e['id']=='wiki:v6:line-wrap':
                e['release_changes']=[{'version':6,'effective_from':'2026-09','date_precision':'month','text':{'ru':'Расширено правило переноса внутри квадратных скобок: разрешены любые отступы, в том числе кратные четырём.','en':'Square-bracket wrapping now accepts any indentation, including multiples of four.'},'source':{'url':'https://www.tradingview.com/pine-script-docs/release-notes/#september-2026'},'verification':'documentation_checked_runtime_not_executed'}]
        save_catalog(c,w)
    print(json.dumps({'new_example_bindings':attached}))


if __name__=='__main__':main()
