#!/usr/bin/env python3
"""Integrity and invariant checks for the static Pine Wiki release (stdlib only, Python 3.10+).

Run from anywhere:  python tools/verify_catalog.py
Exit code 0 = all checks passed. Release counts are printed, not hard-coded.
"""
from pathlib import Path
import collections, hashlib, json, re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
CYR = re.compile('[А-Яа-я]')
failures = []


def check(cond, message):
    if not cond:
        failures.append(message)


def load_js(filename, prefix):
    s = (ROOT / filename).read_text(encoding='utf-8')
    if prefix not in s:
        raise SystemExit('Unexpected JS wrapper: ' + filename)
    return json.loads(s.split(prefix, 1)[1].strip().removesuffix(';'))


# 1. manifest hashes -----------------------------------------------------------
manifest = load_js('wiki-manifest.js', 'window.PINE_MANIFEST=')
n_files = 0
for group in ('versions', 'histories'):
    for item in manifest[group].values():
        data = (ROOT / item['file']).read_bytes()
        n_files += 1
        check(len(data) == item['bytes'], 'wrong size: ' + item['file'])
        check(hashlib.sha256(data).hexdigest() == item['sha256'], 'wrong sha256: ' + item['file'])
print(f'manifest: {n_files} files checked')

CAT = {v: load_js(f'catalog-v{v}.js', f'window.PINE_CATALOG[{v}]=') for v in range(1, 7)}
HIST = {k: load_js(f'history-{k}.js', f'window.PINE_HISTORY["{k}"]=') for k in manifest['histories']}

# 2. history graph -------------------------------------------------------------
families = {fid: f for h in HIST.values() for fid, f in h['families'].items()}
entry_ids = {e['id'] for c in CAT.values() for e in c['entries']}
referenced = {e['family']['id'] for c in CAT.values() for e in c['entries']}
check(set(families) == referenced, f'unreferenced families: {len(set(families) - referenced)}, missing: {len(referenced - set(families))}')
for fid, f in families.items():
    for r in f['related']:
        check(r['id'] in families, f'broken related link {fid} -> {r["id"]}')
    for z in f['versions']:
        for i in z['entry_ids']:
            check(i in entry_ids, f'family {fid} lists unknown entry {i}')
for v, c in CAT.items():
    for e in c['entries']:
        fam = families.get(e['family']['id'])
        check(fam is not None and v in [z['version'] for z in fam['versions']], f'entry {e["id"]} is not listed in its family')
print(f'history: {len(families)} families, all referenced, all links resolved')

# 3. per-catalog invariants ------------------------------------------------------
stats = collections.Counter()
for v, c in CAT.items():
    ids = [e['id'] for e in c['entries']]
    check(len(set(ids)) == len(ids), f'duplicate ids in v{v}')
    texts = c['texts']

    def need(ref, where):
        if isinstance(ref, str) and re.fullmatch(r'[0-9a-f]{16}', ref):
            check(ref in texts, f'v{v}: missing text {ref} ({where})')

    for e in c['entries']:
        x = e['examples']
        items = x.get('items', [])
        check(bool(items) == (x['status'] != 'missing'), f'v{v} {e["id"]}: examples.status does not match items')
        tpl = x.get('template')
        if tpl:
            stats['templates'] += 1
            check(not items, f'v{v} {e["id"]}: template on an entry that has real examples')
            check(tpl.count('(') == tpl.count(')'), f'v{v} {e["id"]}: unbalanced template {tpl!r}')
            check(not re.search(r'<(?!float>)', tpl), f'v{v} {e["id"]}: unresolved placeholder in {tpl!r}')
        for p in x.get('pointers', []):
            stats['pointers'] += 1
            check(p['url'].startswith('https://'), f'v{v} {e["id"]}: pointer url')
            check(p['kind'] in ('example', 'mention') and isinstance(p['official'], bool), f'v{v} {e["id"]}: pointer fields')
            for k in ('where', 'note'):
                check(bool(CYR.search(p[k].get('ru', ''))) and bool(p[k].get('en')), f'v{v} {e["id"]}: pointer {k} is not bilingual')
            check(not items, f'v{v} {e["id"]}: pointer on an entry that has real examples')
        for p in e['parameters']:
            if p.get('type_candidates'):
                stats['type_hints'] += 1
                check(not p.get('types'), f'v{v} {e["id"]}: type hint on a parameter that already has types')
            if p.get('type_issue'):
                stats['legacy_params'] += 1
            need(p.get('description'), e['id'])
        r = e['result']
        need(r.get('description'), e['id'])
        if r.get('description_basis') == 'family_neighbor_description':
            stats['neighbor_descriptions'] += 1
            d = r.get('description_donor') or {}
            check(d.get('entry_id') in entry_ids and d.get('version'), f'v{v} {e["id"]}: donor missing')
        if v >= 3 and e['category'] in ('functions', 'methods'):
            check(bool(texts.get(r.get('description'))), f'v{v} {e["id"]}: function without any result description')
        if e.get('search_rank'):
            stats['search_rank'] += 1
            syn = ' '.join(e.get('synonyms') or []).lower()
            check(('скользящ' in syn or 'moving average' in syn) and e['search_rank'] <= 350, f'v{v} {e["id"]}: unsupported search_rank')
        check(len(set(e['search_terms'])) == len(e['search_terms']), f'v{v} {e["id"]}: duplicate search terms')
        need(e.get('description'), e['id'])
        need(e.get('remarks'), e['id'])
        for q in e['restrictions']:
            need(q.get('text'), e['id'])
print('catalog invariants:', dict(stats))

# 4. UI strings ----------------------------------------------------------------
ui = json.loads((ROOT / 'wiki-i18n.js').read_text(encoding='utf-8').split('window.PINE_UI=', 1)[1].strip().removesuffix(';'))
app = (ROOT / 'wiki-app.js').read_text(encoding='utf-8') + (ROOT / 'index.html').read_text(encoding='utf-8')
used = set(re.findall(r"\bT\('([A-Za-z0-9_]+)'", app)) | set(re.findall(r'data-i18n="([A-Za-z0-9_]+)"', app))
for k in sorted(used):
    check(k in ui, 'missing UI string: ' + k)
for k, val in ui.items():
    check(isinstance(val, list) and len(val) == 2 and all(isinstance(s, str) and s for s in val), 'malformed UI string: ' + k)
print(f'ui strings: {len(used)} keys used, {len(ui)} defined (ru+en)')

# 5. JS syntax (only when node is installed) ---------------------------------------
node = shutil.which('node')
if node:
    for f in sorted(ROOT.glob('*.js')):
        r = subprocess.run([node, '--check', str(f)], capture_output=True, text=True)
        check(r.returncode == 0, f'syntax error in {f.name}: {r.stderr[:200]}')
    print('js syntax: node --check passed for all files')
else:
    print('js syntax: node not found, skipped')

print('release counts:', {f'v{v}': len(c['entries']) for v, c in CAT.items()})
if failures:
    print(f'\n{len(failures)} FAILED CHECKS:')
    for m in failures[:40]:
        print(' -', m)
    sys.exit(1)
print('ALL CHECKS PASSED')
