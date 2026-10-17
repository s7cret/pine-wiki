#!/usr/bin/env python3
"""Browser smoke test over a real local HTTP server.
Requires: pip install playwright && playwright install chromium
Run:      python tools/e2e_smoke.py
"""
import functools, http.server, json, re, sys, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass


handler = functools.partial(Quiet, directory=str(ROOT))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = f'http://127.0.0.1:{server.server_address[1]}/index.html'
results, problems = [], []


def ok(name, cond, info=''):
    results.append((name, bool(cond), info))


def count(pg):
    return int(re.sub(r'\D', '', pg.inner_text('#result-count').split('·')[0]))


with sync_playwright() as p:
    browser = p.chromium.launch(args=['--no-sandbox'])
    ctx = browser.new_context(viewport={'width': 1400, 'height': 900}, accept_downloads=True)
    pg = ctx.new_page()
    pg.on('console', lambda m: problems.append(m.text[:160]) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: problems.append('pageerror: ' + str(e)[:160]))
    pg.on('response', lambda r: problems.append(f'HTTP {r.status} {r.url[-60:]}') if r.status >= 400 else None)

    # every version loads and the card count equals the catalog
    for v in range(1, 7):
        pg.goto(f'{BASE}?v={v}&lang=ru'); pg.wait_for_selector('#rows tr', timeout=30000)
        expected = pg.evaluate(f'window.PINE_CATALOG[{v}].counts.public_records')
        ok(f'v{v}: card count equals catalog', count(pg) == expected, f'{count(pg)} vs {expected}')

    # search relevance
    pg.goto(f'{BASE}?v=6&lang=ru'); pg.wait_for_selector('#rows tr')
    def top(q, k=4):
        pg.fill('#search', q); pg.wait_for_timeout(350)
        n = pg.locator('#rows tr .symbol').count()
        return [pg.locator('#rows tr .symbol').nth(i).inner_text() for i in range(min(k, n))]
    for q, first in [('sma', 'ta.sma'), ('скользящая', 'ta.sma'), ('ta.sma', 'ta.sma'), ('line.set_xy1', 'line.set_xy1')]:
        t = top(q); ok(f'search {q!r}: first is {first}', t[:1] == [first], str(t))
    for q, part in [('бокс', 'box'), ('таблица', 'table'), ('отрисовка', 'plot'), ('закрытые сделки', 'closedtrades')]:
        t = top(q, 6); ok(f'search {q!r}: finds {part}', any(part in x for x in t), str(t))
    ok("search 'sma' has no 'small' in top results", not any('small' in x for x in top('sma', 8)))
    pg.fill('#search', '')

    # new blocks: pointers + template, neighbour result, type hints, legacy parameter
    def open_entry(v, js):
        pg.goto(f'{BASE}?v={v}&lang=ru'); pg.wait_for_selector('#rows tr')  # make sure this version's catalog is loaded
        eid = pg.evaluate(f'()=>window.PINE_CATALOG[{v}].entries.find({js})?.id')
        pg.goto(f'{BASE}?v={v}&lang=ru&id=' + eid); pg.wait_for_selector('#rows tr'); return pg.inner_html('#rows')
    h = open_entry(6, "e=>e.name==='line.set_xy1'&&e.category==='functions'")
    ok('pointer + template block rendered', 'Ссылки на документацию' in h and 'Схематический вызов' in h and 'line.set_xy1(myLine' in h)
    h = open_entry(3, "e=>e.name==='floor'&&e.category==='functions'")
    ok('neighbour result note with donor link', 'source-inferred' in h and 'data-entry' in h)
    h = open_entry(3, "e=>e.parameters.some(p=>p.type_candidates?.length&&!p.type_issue)")
    ok('type hints rendered (v3 parameter without a documented type)', 'type-hint' in h)
    h = open_entry(5, "e=>e.name==='plot'&&e.parameters.some(p=>p.type_issue)")
    ok('legacy parameter note rendered', 'source-inferred' in h)

    # "examples only" counts real examples, never templates or pointers
    pg.goto(f'{BASE}?v=6&lang=ru'); pg.wait_for_selector('#rows tr'); pg.check('#examples-only'); pg.wait_for_timeout(300)
    real = pg.evaluate("()=>window.PINE_CATALOG[6].entries.filter(e=>['source_example','source_occurrence','compatibility_example'].includes(e.examples.status)&&!e.technical).length")
    ok('examples-only counts real examples only', count(pg) == real, f'{count(pg)} vs {real}')
    pg.uncheck('#examples-only')

    # language switch, mobile layout
    pg.select_option('#language', 'en'); pg.wait_for_timeout(400)
    ok('EN: <html lang>', pg.evaluate('document.documentElement.lang') == 'en')
    ok('EN: page chrome translated', not re.search('[А-Яа-я]', pg.evaluate("()=>[...document.querySelectorAll('header .eyebrow, .intro, th, .toolbar label > span')].map(e=>e.textContent).join(' ')")))
    mobile = ctx.new_page(); mobile.set_viewport_size({'width': 390, 'height': 800}); mobile.goto(f'{BASE}?v=6&lang=en'); mobile.wait_for_selector('#rows tr')
    ok('mobile: no horizontal overflow', mobile.evaluate('document.documentElement.scrollWidth<=window.innerWidth+2'))
    ok('mobile: EN cell labels', not re.search('[А-Яа-я]', ' '.join(mobile.evaluate("()=>[...document.querySelectorAll('#rows tr:first-child td')].map(t=>t.dataset.label)"))))
    mobile.close(); pg.select_option('#language', 'ru')

    # history dialog and related families
    pg.goto(f'{BASE}?v=6&q=study&lang=ru'); pg.wait_for_selector('#rows tr')
    pg.locator('.history-button').first.click(); pg.wait_for_selector('#history-differences h3', timeout=15000)
    ok('history dialog opens', 'indicator' in pg.inner_text('#history-title'))
    pg.keyboard.press('Escape')

    # export and routing
    pg.goto(f'{BASE}?v=5&lang=ru'); pg.wait_for_selector('#rows tr')
    with pg.expect_download() as d:
        pg.click('#download')
    data = json.load(open(d.value.path(), encoding='utf-8'))
    ok('JSON export', d.value.suggested_filename == 'pine-v5-reference.json' and len(data['entries']) == pg.evaluate('window.PINE_CATALOG[5].entries.length'))
    pg.goto(f'{BASE}?v=6&lang=ru&page=3'); pg.wait_for_selector('#rows tr')
    ok('page parameter', pg.inner_text('#page-label').startswith('4'))
    browser.close()

for name, cond, info in results:
    print(('PASS ' if cond else 'FAIL ') + name + ('' if cond or not info else '  | ' + info))
failed = [n for n, c, _ in results if not c]
print('\nconsole/network problems:', problems[:8] or 'none')
sys.exit(1 if failed or problems else 0)
