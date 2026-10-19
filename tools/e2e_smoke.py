#!/usr/bin/env python3
"""Real Chromium HTTP/file checks. Requires playwright and a Chromium browser.

Run: python tools/e2e_smoke.py [--screenshots DIR] [--json FILE]
E2E_BROWSER_EXECUTABLE optionally selects an installed Chrome/Chromium binary.
"""
import argparse, functools, http.server, json, os, re, sys, threading
from pathlib import Path
from urllib.parse import parse_qs, urlparse, quote
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--screenshots', type=Path)
parser.add_argument('--json', type=Path)
args = parser.parse_args()
results, problems, data_requests = [], [], []


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass


def ok(name, cond, info=''):
    results.append({'name': name, 'passed': bool(cond), 'info': str(info)})
    print(('PASS ' if cond else 'FAIL ') + name + ('' if cond or not info else ' | ' + str(info)), flush=True)


def count(pg):
    return int(re.sub(r'\D', '', pg.inner_text('#result-count').split('·')[0]))


def loaded(pg, url):
    pg.goto(url)
    pg.wait_for_selector('#wiki-layout:not([hidden])', timeout=30000)
    pg.wait_for_selector('#rows tr', state='attached', timeout=30000)


def active(pg):
    return pg.evaluate("()=>({tag:document.activeElement.tagName,id:document.activeElement.id,category:document.activeElement.dataset.category,version:document.activeElement.dataset.version})")


def donor_link(pg, selector, donor):
    hrefs = pg.locator(selector).evaluate_all('(nodes)=>nodes.map(n=>n.href)')
    return any(parse_qs(urlparse(href).query).get('id') == [donor['entry_id']] and parse_qs(urlparse(href).query).get('v') == [str(donor['version'])] for href in hrefs)


def check_october_audit(pg, base):
    for lang in ('ru','en'):
        for symbol in ('+', '[]', ':=', '==', '!=', '=>', '?:', '//'):
            loaded(pg,f'{base}?v=6&lang={lang}&q={quote(symbol,safe="")}')
            ok(f'audit search/{lang}/{symbol}: results', count(pg)>0)
            pg.locator('#rows .entry-tools a[data-entry]').first.click()
            ok(f'audit search/{lang}/{symbol}: direct route retains query', parse_qs(urlparse(pg.url).query).get('q')==[symbol] and bool(parse_qs(urlparse(pg.url).query).get('id')))
        loaded(pg,f'{base}?v=4&lang={lang}&id=primary:v4:functions:timestamp:overload:0')
        links=pg.locator('#rows .parameter a').evaluate_all('(nodes)=>nodes.map(n=>n.href)')
        ok(f'audit timestamp/{lang}: normalized RFC and ISO anchors', 'https://tools.ietf.org/html/rfc2822#section-3.3' in links and 'https://en.wikipedia.org/wiki/ISO_8601' in links)
        for name in ('request.security','request.security_lower_tf'):
            loaded(pg,f'{base}?v=6&lang={lang}&id=primary:v6:functions:{name}:overload:0')
            issue=pg.locator('#rows [data-issue="SOURCE.GAP.V6.REQUEST_SECURITY_UNIQUE_LIMIT_PLAN"]')
            ok(f'audit limit/{lang}/{name}: shared caveat at card',issue.count()==1 and '40' in issue.inner_text() and '64' in issue.inner_text() and 'Ultimate' in issue.inner_text())
        loaded(pg,f'{base}?v=4&lang={lang}&id=primary:v4:functions:cross:overload:0')
        pg.locator('#rows .history-button').click();pg.wait_for_selector('#history-differences h3')
        pg.select_option('#compare-from','3');pg.select_option('#compare-to','4')
        expected=pg.evaluate(f'window.PINE_UI.descriptionMissingComparison[{1 if lang=="en" else 0}]')
        ok(f'audit cross/{lang}: absence separated from manual supplement',expected in pg.inner_text('#history-differences') and pg.locator('#history-columns section').nth(1).locator('.meta').count()>0)
        pg.keyboard.press('Escape')
    loaded(pg,f'{base}?v=4&lang=ru&id=primary:v4:functions:array.from:overload:0')
    ok('audit array.from: one variadic group',pg.locator('#rows .parameter').count()==1 and pg.locator('#rows .parameter>code').text_content()=='args')
    loaded(pg,f'{base}?v=4&lang=ru&id=primary:v4:functions:round:overload:0')
    forms=pg.locator('#rows details[data-detail="parameters"]>code.syntax').all_text_contents()
    ok('audit round: two call forms, no three-argument template',forms==['round(x)','round(number, precision)'] and 'round(bar_index, close, 2)' not in pg.locator('#rows').text_content())


def check_sources_and_history(pg, base):
    """Check accessible mode changes and a known family missing from v1-v4."""
    loaded(pg, f'{base}?v=6&lang=ru')
    entry = pg.evaluate("()=>window.PINE_CATALOG[6].entries.find(e=>e.name==='polyline.new'&&e.category==='functions')")
    if not entry or entry['family']['versions'] != [5, 6]:
        raise AssertionError('Expected polyline.new history fixture in v5 and v6 only')
    messages = {
        'ru': ('Показаны источники и ограничения для Pine Script v6.',
               'Панель источников закрыта. Восстановлен просмотр справочника.', 'нет записи в снимке'),
        'en': ('Sources and limitations for Pine Script v6 are shown.',
               'Sources panel closed. Returned to the reference view.', 'no saved entry'),
    }
    for lang, (opened, closed, missing) in messages.items():
        loaded(pg, f'{base}?v=6&lang={lang}&id={entry["id"]}')
        button = pg.locator('#sources-button')
        ok(f'sources/{lang}: initial accessible state', button.get_attribute('aria-pressed') == 'false' and button.get_attribute('aria-controls') == 'source-panel' and pg.locator('#entry-banner').is_visible())
        button.focus()
        pg.keyboard.press('Enter')
        ok(f'sources/{lang}: announces panel and hides entry banner', button.get_attribute('aria-pressed') == 'true' and pg.locator('#source-panel').is_visible() and pg.locator('#entry-banner').is_hidden() and pg.locator('#table-wrap').is_hidden() and active(pg)['id'] == 'sources-button' and pg.locator('#status-live').text_content() == opened and parse_qs(urlparse(pg.url).query).get('id') == [entry['id']])
        pg.keyboard.press('Enter')
        ok(f'sources/{lang}: restores the same entry', button.get_attribute('aria-pressed') == 'false' and pg.locator('#source-panel').is_hidden() and pg.locator('#entry-banner').is_visible() and pg.locator('#table-wrap').is_visible() and pg.locator('#rows tr').count() == 1 and pg.locator('#rows tr').get_attribute('id') == entry['id'] and pg.locator('#status-live').text_content() == closed and parse_qs(urlparse(pg.url).query).get('id') == [entry['id']])
        button.click()
        pg.locator('[data-category="functions"]').click()
        ok(f'sources/{lang}: category navigation resets panel state', button.get_attribute('aria-pressed') == 'false' and pg.locator('#source-panel').is_hidden() and pg.locator('#status-live').text_content() == closed)

        loaded(pg, f'{base}?v=6&lang={lang}&id={entry["id"]}')
        pg.locator('.history-button').click()
        pg.wait_for_selector('#history-differences h3')
        expected_labels = {str(v): f'v{v}' if v in (5, 6) else f'v{v} — {missing}' for v in range(1, 7)}
        for selector in ('#compare-from', '#compare-to'):
            options = pg.locator(selector + ' option').evaluate_all('(nodes)=>nodes.map(n=>({value:n.value,label:n.textContent,disabled:n.disabled}))')
            ok(f'history/{lang}/{selector}: absent versions labeled and selectable', len(options) == 6 and {o['value']: o['label'] for o in options} == expected_labels and not any(o['disabled'] for o in options), options)
        pg.select_option('#compare-from', '1')
        left = pg.locator('#history-columns section').first
        ok(f'history/{lang}: absent version can be compared', pg.locator('#compare-from').input_value() == '1' and left.locator('.missing-note').count() == 1 and left.locator('a[data-entry]').count() == 0)
        pg.select_option('#compare-from', '5')
        ok(f'history/{lang}: existing version remains accessible', left.locator('.missing-note').count() == 0 and left.locator('a[data-entry]').count() == 1)
        pg.keyboard.press('Escape')

    # Remove only the in-memory fixture to exercise the existing recovery path.
    pg.evaluate("family=>{window.__e2eFamily=PINE_HISTORY[family.shard].families[family.id];delete PINE_HISTORY[family.shard].families[family.id]}", entry['family'])
    try:
        pg.locator('.history-button').click()
        pg.wait_for_selector('#retry-history')
        ok('history: missing family offers recovery', bool(pg.locator('#history-note').text_content().strip()) and pg.locator('.history-controls').is_hidden() and active(pg)['id'] == 'history-close')
    finally:
        pg.evaluate("family=>{PINE_HISTORY[family.shard].families[family.id]=window.__e2eFamily;delete window.__e2eFamily}", entry['family'])
    pg.locator('#retry-history').click()
    pg.wait_for_selector('#history-differences h3')
    ok('history: retry recovers a restored family', pg.locator('.history-controls').is_visible() and pg.locator('#history-title').text_content() == 'polyline.new' and pg.locator('#retry-history').count() == 0)
    pg.keyboard.press('Escape')


server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(ROOT)))
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = f'http://127.0.0.1:{server.server_address[1]}/index.html'
try:
    with sync_playwright() as p:
        launch = {'args': ['--no-sandbox']}
        if os.environ.get('E2E_BROWSER_EXECUTABLE'):
            launch['executable_path'] = os.environ['E2E_BROWSER_EXECUTABLE']
        browser = p.chromium.launch(**launch)
        ctx = browser.new_context(viewport={'width': 1400, 'height': 900}, accept_downloads=True)
        pg = ctx.new_page()
        pg.on('console', lambda m: problems.append(m.text[:300]) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: problems.append('pageerror: ' + str(e)[:300]))
        pg.on('response', lambda r: problems.append(f'HTTP {r.status} {r.url}') if r.status >= 400 else None)
        pg.on('requestfailed', lambda r: problems.append(f'requestfailed: {r.url}: {r.failure}'))
        pg.on('request', lambda r: data_requests.append(r.url) if re.search(r'/(catalog-v\d|history-[^/?]+)\.js(?:\?|$)', r.url) else None)

        for width in (390, 800, 1000, 1400):
            pg.set_viewport_size({'width': width, 'height': 900})
            for v in range(1, 7):
                for lang in ('ru', 'en'):
                    loaded(pg, f'{BASE}?v={v}&lang={lang}')
                    expected = pg.evaluate(f'window.PINE_CATALOG[{v}].counts.public_records')
                    ok(f'HTTP v{v}/{lang}/{width}: count and layout', count(pg) == expected and pg.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'), f'{count(pg)}/{expected}')
                    ok(f'HTTP v{v}/{lang}/{width}: semantics and live status', pg.locator('th:not([scope="col"])').count() == 0 and bool(pg.locator('table caption').text_content().strip()) and bool(pg.locator('#status-live').text_content().strip()))
                    if lang == 'en':
                        chrome = pg.evaluate("()=>[...document.querySelectorAll('header .eyebrow, .intro, th, .toolbar label > span')].map(e=>e.textContent).join(' ')")
                        labels = pg.locator('#rows tr:first-child td').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.label).join(" ")')
                        ok(f'HTTP v{v}/en/{width}: translated chrome', pg.evaluate('document.documentElement.lang') == 'en' and not re.search('[А-Яа-я]', chrome + labels))
            if args.screenshots and width in (390, 800, 1400):
                args.screenshots.mkdir(parents=True, exist_ok=True)
                pg.screenshot(path=str(args.screenshots / f'v6-en-{width}.png'), full_page=True)

        for v in range(1, 7):
            for lang in ('ru', 'en'):
                loaded(pg, f'{(ROOT / "index.html").as_uri()}?v={v}&lang={lang}')
                expected = pg.evaluate(f'window.PINE_CATALOG[{v}].counts.public_records')
                ok(f'file v{v}/{lang}: catalog loads', count(pg) == expected)

        loaded(pg, f'{BASE}?v=6&lang=ru')
        def top(q, k=4):
            pg.fill('#search', q)
            pg.wait_for_function('(q)=>new URL(location.href).searchParams.get("q")===q', arg=q)
            return pg.locator('#rows tr .symbol').all_text_contents()[:k]
        for q, first in [('sma', 'ta.sma'), ('скользящая', 'ta.sma'), ('ta.sma', 'ta.sma'), ('line.set_xy1', 'line.set_xy1'), ('индикатор', 'indicator'), ('стратегия', 'strategy'), ('массив', 'array')]:
            found = top(q)
            ok(f'search {q!r}: first is {first}', found[:1] == [first], found)
        for q, part in [('бокс', 'box'), ('таблица', 'table'), ('отрисовка', 'plot'), ('закрытые сделки', 'closedtrades')]:
            found = top(q, 6)
            ok(f'search {q!r}: finds {part}', any(part in x for x in found), found)
        ok("search 'sma' has no 'small'", not any('small' in x for x in top('sma', 20)))

        def open_entry(v, predicate):
            loaded(pg, f'{BASE}?v={v}&lang=ru')
            entry = pg.evaluate(f'()=>window.PINE_CATALOG[{v}].entries.find({predicate})')
            if not entry:
                raise AssertionError(f'Missing fixture v{v}: {predicate}')
            loaded(pg, f'{BASE}?v={v}&lang=ru&id={entry["id"]}')
            return entry
        open_entry(6, "e=>e.name==='line.set_xy1'&&e.category==='functions'")
        html = pg.inner_html('#rows')
        ok('pointer + template rendered', 'Ссылки на документацию' in html and 'Схематический вызов' in html and 'line.set_xy1(myLine' in html)
        entry = open_entry(4, "e=>e.name==='floor'&&e.category==='functions'")
        ok('floor v4: exact result donor link', donor_link(pg, '#rows .result .source-inferred a[data-entry]', entry['result']['description_donor']))
        for name in ('floor', 'cross'):
            open_entry(3, f"e=>e.name==='{name}'&&e.category==='functions'")
            ok(f'{name} v3: signature note without donor', pg.locator('#rows .result .source-inferred').count() > 0 and pg.locator('#rows .result .source-inferred a[data-entry]').count() == 0)
        open_entry(3, "e=>e.parameters.some(p=>p.type_candidates?.length&&!p.type_issue)")
        ok('parameter type hints rendered', pg.locator('#rows .type-hint').count() > 0)
        entry = open_entry(4, "e=>e.name==='na'&&e.category==='functions'")
        hint = next(param['description_hint'] for param in entry['parameters'] if param.get('description_hint'))
        ok('na v4: description hint with exact donor', pg.locator('#rows .description-hint .source-inferred').count() > 0 and donor_link(pg, '#rows .description-hint a[data-entry]', hint))
        open_entry(5, "e=>e.name==='plot'&&e.parameters.some(p=>p.type_issue)")
        ok('legacy parameter note rendered', pg.locator('#rows .parameter .source-inferred').count() > 0)
        open_entry(5, "e=>e.name==='ta.sar'&&e.category==='functions'")
        ok('ta.sar v5: one complete example', pg.locator('#rows .example').count() == 1 and '\n' in pg.locator('#rows .example pre code').text_content())
        open_entry(6, "e=>e.name==='color.red'&&e.category==='constants'")
        ru_label = pg.evaluate('window.PINE_UI.valueType[0]')
        en_label = pg.evaluate('window.PINE_UI.valueType[1]')
        ok('color.red: Russian value-type label', pg.locator('#rows .value-type strong').text_content() == ru_label)
        pg.select_option('#language', 'en')
        ok('color.red: value-type label switches to English', pg.locator('#rows .value-type strong').text_content() == en_label and pg.locator('#rows .result').count() == 0)
        entry = open_entry(6, "e=>e.name==='alert'&&e.category==='functions'")
        ok('alert: void result retains signature provenance', pg.locator('#rows .result code').first.text_content() == 'void' and pg.evaluate('window.PINE_UI.resultFromVoid[0]') in pg.locator('#rows .result').text_content() and entry['result']['description_source']['url'] in pg.locator('#rows .result a').evaluate_all('(nodes)=>nodes.map(n=>n.href)'))

        # Exhaust every non-callable category in every version, with pagination.
        for v in range(1, 7):
            loaded(pg, f'{BASE}?v={v}&lang=ru')
            entries = {e['id']: e for e in pg.evaluate(f'window.PINE_CATALOG[{v}].entries')}
            texts = pg.evaluate(f'window.PINE_CATALOG[{v}].texts')
            for category in ('variables', 'constants', 'types', 'keywords', 'syntax', 'annotations', 'operators', 'technical'):
                if not any(e['category'] == category for e in entries.values()):
                    continue
                loaded(pg, f'{BASE}?v={v}&lang=ru&category={category}')
                checked, incorrect = 0, []
                while True:
                    rows = pg.evaluate("()=>[...document.querySelectorAll('#rows tr')].map(r=>({id:r.id,result:!!r.querySelector('.result'),value:!!r.querySelector('.value-type')}))")
                    for row in rows:
                        checked += 1
                        desc = texts.get(entries[row['id']]['result'].get('description'), {})
                        expected_result = category == 'operators' and bool(desc.get('ru'))
                        if row['result'] != expected_result or row['value'] != (category in ('variables', 'constants')):
                            incorrect.append(row['id'])
                    if pg.locator('#next').is_disabled():
                        break
                    pg.locator('#next').click()
                ok(f'v{v}/{category}: result semantics on all {checked} cards', not incorrect, incorrect[:5])

        loaded(pg, f'{BASE}?v=6&lang=ru')
        pg.check('#examples-only')
        real = pg.evaluate("()=>window.PINE_CATALOG[6].entries.filter(e=>['source_example','source_occurrence','compatibility_example','editorial_probe'].includes(e.examples.status)&&!e.technical).length")
        ok('examples-only counts real examples', count(pg) == real, f'{count(pg)}/{real}')
        pg.uncheck('#examples-only')
        for v in range(1, 7):
            pg.locator(f'#versions [data-version="{v}"]').focus()
            pg.keyboard.press('Enter')
            pg.wait_for_selector('#wiki-layout:not([hidden])')
            ok(f'keyboard version v{v}: focus retained', active(pg).get('version') == str(v), active(pg))
        categories = pg.locator('#categories [data-category]').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.category)')
        for category in categories:
            pg.locator(f'#categories [data-category="{category}"]').focus()
            pg.keyboard.press('Enter')
            pg.wait_for_selector('#wiki-layout:not([hidden])')
            ok(f'keyboard category {category}: focus retained', active(pg).get('category') == category, active(pg))
        loaded(pg, f'{BASE}?v=6&lang=ru')
        pg.locator('#examples-only').focus()
        pg.keyboard.press('Space')
        ok('keyboard filter: focus retained', active(pg)['id'] == 'examples-only')
        pg.keyboard.press('Space')
        pg.locator('#search').focus()
        pg.keyboard.insert_text('sma')
        ok('keyboard search: focus retained', active(pg)['id'] == 'search')
        pg.fill('#search', '')
        pg.locator('#next').focus()
        pg.keyboard.press('Enter')
        ok('keyboard pagination: heading focused', active(pg)['id'] == 'category-title')
        loaded(pg, f'{BASE}?v=6&q=study&lang=ru')
        pg.locator('.history-button').first.focus()
        pg.keyboard.press('Enter')
        pg.wait_for_selector('#history-differences h3', timeout=15000)
        ok('keyboard history: dialog focus', 'indicator' in pg.inner_text('#history-title') and pg.evaluate("document.activeElement.closest('#history-dialog')!==null"))
        pg.keyboard.press('Tab')
        ok('keyboard history: Tab stays in dialog', pg.evaluate("document.activeElement.closest('#history-dialog')!==null"))
        pg.keyboard.press('Escape')
        ok('keyboard history: close returns focus', pg.evaluate("document.activeElement.matches('.history-button')"), active(pg))

        check_sources_and_history(pg, BASE)
        check_october_audit(pg, BASE)

        loaded(pg, f'{BASE}?v=5&lang=ru')
        with pg.expect_download() as download:
            pg.click('#download')
        data = json.loads(Path(download.value.path()).read_text(encoding='utf-8'))
        ok('JSON export', download.value.suggested_filename == 'pine-v5-reference.json' and len(data['entries']) == pg.evaluate('window.PINE_CATALOG[5].entries.length'))
        loaded(pg, f'{BASE}?v=6&lang=ru&page=3')
        ok('page parameter', pg.inner_text('#page-label').startswith('4'))
        ok('manifest hash on data requests', bool(data_requests) and all(re.search(r'\?v=[0-9a-f]{8}$', url) for url in data_requests))
        browser.close()
except Exception as error:
    ok('browser run completed', False, f'{type(error).__name__}: {error}')
finally:
    server.shutdown()
ok('console/network clean', not problems, problems[:8])
summary = {'checks': results, 'passed': sum(item['passed'] for item in results), 'failed': sum(not item['passed'] for item in results), 'problems': problems}
if args.json:
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'\n{summary["passed"]}/{len(results)} browser checks passed')
sys.exit(1 if summary['failed'] else 0)
