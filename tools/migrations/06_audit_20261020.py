#!/usr/bin/env python3
"""Apply the October audit without changing captured source strings. Idempotent."""
import copy, hashlib, json, re, sys
from pathlib import Path
from catalog_io import ROOT, load_catalog, save_catalog
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data_integrity import catalog_aggregates, family_version_aggregate, text_references
from semantic_contracts import PLACEHOLDER_REFS, default_number, explicit_optional, history_contracts

DATE = '2026-10-20'
MANUAL = 'https://www.tradingview.com/pine-script-docs/'


def localized(ru, en):
    return {'ru': ru, 'en': en}


def supplement(entry, ru, en, url):
    entry.setdefault('editorial_supplements', [])
    item = {'text': localized(ru, en), 'source': {'url': url}, 'reviewed_on': DATE,
            'basis': 'editorial_summary', 'scope_version': entry['v']}
    if item not in entry['editorial_supplements']:
        entry['editorial_supplements'].append(item)


def main():
    cats = {}
    counts = {}
    for v in range(1, 7):
        c, wrapper = load_catalog(ROOT, v)
        cats[v] = c
        n = 0
        for ref in PLACEHOLDER_REFS:
            if ref in c['texts']:
                c['texts'][ref]['content_status'] = 'missing_description_notice'
        for e in c['entries']:
            for p in e['parameters']:
                raw = c['texts'].get(p.get('description'), {})
                if raw.get('content_status') == 'missing_description_notice':
                    p['description_content_status'] = 'missing_description_notice'
                if p.get('state') == 'unknown' and explicit_optional(raw.get('en', '')):
                    p['prose_state'] = 'optional'
                    p['state'] = 'conflict' if p.get('metadata_state') == 'required' else 'optional'
                    p['requiredness_evidence'] = {'text_ref': p['description'], 'quote': 'Optional.', 'basis': 'direct_parameter_prose'}
                    n += 1
                if v == 5 and e['name'] in ('request.security', 'request.security_lower_tf', 'request.seed') and p['name'] == 'calc_bars_count':
                    numeric = default_number(raw['en'])
                    assert numeric['value'] == '100000'
                    p['default_contract'] = {'state': 'explicit_value', 'values': ['100000'], 'evidence': [dict(numeric, text_ref=p['description'])]}
                if v in (5, 6) and e['name'] == 'request.security' and p['name'] == 'lookahead':
                    off = re.search(r'The default is \[barmerge.lookahead_off\].*?starting from Pine Script® v3', raw['en'])[0]
                    on = re.search(r'The default is \[barmerge.lookahead_on\].*?in v1 and v2', raw['en'])[0]
                    p['default_contract'] = {'state': 'explicit_value', 'values': ['barmerge.lookahead_off'],
                        'evidence': [{'value': 'barmerge.lookahead_off', 'quote': off, 'text_ref': p['description'], 'scope': {'versions': [3,4,5,6]}}],
                        'historical_semantics': [{'value': 'barmerge.lookahead_on', 'quote': on, 'text_ref': p['description'],
                            'versions': [1,2], 'kind': 'equivalent_behavior_without_parameter'}]}
                    supplement(e, 'У v1/v2 параметра lookahead ещё не было. Историческое поведение security эквивалентно позднейшему lookahead_on; это не второй default для данной карточки.',
                        'v1/v2 had no lookahead parameter. Historical security behavior was equivalent to the later lookahead_on; this is not a second default for this entry.', MANUAL+'concepts/other-timeframes-and-data/#lookahead')
            if v == 6 and e['name'] == 'switch' and e['category'] == 'keywords':
                supplement(e, 'В v6, если ни одна ветка switch не выбрана и нет ветки по умолчанию, результат bool равен false. Для остальных соответствующих типов результат — na. Исходная общая формулировка ниже требует этого исключения.',
                    'In v6, an unmatched switch without a default branch returns false for a bool result; other applicable types return na. The captured general rule below requires this exception.', MANUAL+'language/conditional-structures/#switch-structure')
            if v == 4 and e['name'] == 'array.from':
                e.setdefault('parameters_raw', copy.deepcopy(e['parameters']))
                p = copy.deepcopy(e['parameters_raw'][-1])
                p.update(name='args', kind='variadic_group', raw_aliases=['..args','arg0, arg1, ...'], types=[],
                         type_basis='editorial_source_correction', type_issue='raw_const_qualifier_not_a_series_restriction')
                p['description_content_status'] = 'substantive'
                e['parameters'] = [p]
                e['call_forms'] = [{'syntax': 'array.from(arg0, arg1, ...)','parameters':['args'], 'variadic':True}]
                e['examples'].pop('template',None)
                supplement(e, 'Одна вариадическая группа. Имена ..args и arg0, arg1, ... — исходные обозначения одной группы. Пример v4 передаёт close/open через f_arr: исходная аннотация const не доказывает запрет series. Допустимые именованные вызовы отдельно не установлены.',
                    'One variadic group; ..args and arg0, arg1, ... are raw aliases. The v4 example passes close/open through f_arr, so the captured const annotation cannot establish a series restriction. Named-call support is not established.', 'https://www.tradingview.com/blog/en/new-pine-funtions-for-strings-and-arrays-24554/')
            if v == 4 and e['name'] == 'round':
                e['call_forms'] = [{'syntax':'round(x)', 'parameters':['x'], 'max_arity':1}, {'syntax':'round(number, precision)', 'parameters':['number','precision'], 'max_arity':2}]
                e['examples']['template'] = 'round(close)\nround(close, 2)'
                for p in e['parameters']:
                    p['call_forms'] = [i for i,f in enumerate(e['call_forms']) if p['name'] in f['parameters']]
            if v == 4 and e['name'] == 'timestamp':
                item = c['texts']['6ddfb67a860a0398']
                item['normalized'] = {lang: re.sub(r'\]\x27\((https?://[^\s"\)]+)" rel="nofollow\)\x27', r'](\1)', item[lang]) for lang in ('ru','en')}
                item['normalization'] = {'kind':'editorial_link_repair', 'reviewed_on':DATE, 'raw_preserved':True}
            if v == 4 and e['name'] == 'rsi' and e['category'] == 'functions':
                e['call_forms'] = [{'syntax':'rsi(series float x, simple int y)', 'parameters':['x','y']}, {'syntax':'rsi(series float x, series float y)', 'parameters':['x','y'], 'removed_in':5}]
                descriptions = [localized('В первой форме — ценовой ряд; во второй — числитель отношения.', 'Price series in the first form; numerator of a ratio in the second form.'),
                    localized('simple int: длина обычного RSI. series float: знаменатель отношения; результат 100.0 - 100.0 / (1.0 + x / y). series int выбирает ratio-форму после приведения, а не динамическую длину RSI. Эта форма удалена в v5.', 'simple int: ordinary RSI length. series float: ratio denominator; result 100.0 - 100.0 / (1.0 + x / y). A series int selects the ratio form after conversion, not a dynamic RSI length. This form was removed in v5.')]
                for p,desc in zip(e['parameters'],descriptions):
                    p['description_supplement'] = {'text':desc, 'source':{'url':MANUAL+'v5/migration-guides/to-pine-version-5/#removed-an-rsi-overload'}, 'basis':'editorial_summary', 'scope_version':4}
                supplement(e, 'Две исторические формы v4 подтверждены руководством миграции v5. Удалена ratio-форма; в v1–v3 это уточнение автоматически не переносится.',
                    'The v5 migration guide documents two historical v4 forms and removal of the ratio form. This evidence is not automatically applied to v1–v3.',MANUAL+'v5/migration-guides/to-pine-version-5/#removed-an-rsi-overload')
            if v == 6 and e['id'] == 'wiki:v6:line-wrap':
                supplement(e, 'С сентября 2026 переносы внутри круглых () и квадратных [] скобок допускают отступ, кратный четырём. Вне скобок прежние ограничения отступов сохраняются.',
                    'Since September 2026, wrapped lines inside parentheses () and square brackets [] may use indentation divisible by four. Outside brackets the usual indentation restrictions still apply.',MANUAL+'language/script-structure/#line-wrapping')
        if v == 6:
            issue = next(i for i in c['source_issues'] if i['id'] == 'SOURCE.GAP.V6.REQUEST_SECURITY_UNIQUE_LIMIT_PLAN')
            issue['entry_ids'] = [e['id'] for e in c['entries'] if e['name'] in ('request.security','request.security_lower_tf')]
            issue['reviewed_on'] = DATE
            issue['card_note'] = localized('Общий лимит уникальных request.* — 40; для плана Ultimate — до 64. Проверено 20.10.2026. Отдельное ограничение request.footprint здесь не описывается.',
                'The shared unique request.* limit is 40, or up to 64 on Ultimate. Checked 2026-10-20. The separate request.footprint restriction is not covered here.')
            issue['card_source'] = {'url':MANUAL+'writing/limitations/#request-calls'}
        c['counts'], c['structure_counts'] = catalog_aggregates(c)
        save_catalog(c, wrapper)
        counts[v] = n
    # Rebuild dependent aggregates from the same entries, preserving raw hashes,
    # migration notes and independently captured source pools.
    for path in sorted(ROOT.glob('history-*.js')):
        prefix = 'window.PINE_HISTORY["'+path.stem[-1]+'"]='
        raw = path.read_text(encoding='utf8'); before, tail=raw.split(prefix,1)
        h = json.loads(tail.strip().removesuffix(';'))
        for fid,f in h['families'].items():
            if fid == 'functions:request.security':
                f['historical_semantics'] = [{'versions':[1,2], 'parameter_exists':False,
                    'text':localized('В v1/v2 security ещё не имел параметра lookahead. Его поведение соответствовало позднейшему lookahead_on.',
                        'v1/v2 security had no lookahead parameter. Its behavior corresponded to the later lookahead_on.'),
                    'source':{'url':MANUAL+'concepts/other-timeframes-and-data/#lookahead'}, 'reviewed_on':DATE}]
            for z in f['versions']:
                es=[e for e in cats[z['version']]['entries'] if e['family']['id']==fid]
                z.update(family_version_aggregate(es));z['default_contracts']=history_contracts(es)
                z['description_content_status'] = 'missing_description_notice' if all(x.startswith('d16318992318f93e') for x in z['description_hashes']) else 'substantive'
                for p in [p for e in es for p in e['parameters']]:
                    for ev in p.get('default_contract',{}).get('evidence',[]):
                        if ev.get('text_ref'):h['texts'][ev['text_ref']]=cats[z['version']]['texts'][ev['text_ref']]
        used={ref for ref,_ in text_references(h)}
        h['texts']={ref:t for ref,t in h['texts'].items() if ref in used}
        path.write_text(before+prefix+json.dumps(h,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8',newline='\n')
    print(json.dumps({'direct_optional_added':counts}))


if __name__ == '__main__':
    main()
