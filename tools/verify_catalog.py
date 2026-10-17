#!/usr/bin/env python3
"""Integrity and invariant checks for the static Pine Wiki release (stdlib only, Python 3.10+).

Run from anywhere:  python tools/verify_catalog.py
Exit code 0 = all checks passed. Release counts are printed, not hard-coded.
"""
from pathlib import Path
from importlib import import_module
import collections, hashlib, json, re, shutil, subprocess, sys
from data_integrity import (catalog_aggregates, family_version_aggregate, has_text,
                            normalized_history_aggregate, text_pool_errors)

ROOT = Path(__file__).resolve().parents[1]
# Share the migration's reviewed correspondences so validation cannot drift
# from the exact family/parameter renames used to create description hints.
sys.path.insert(0, str(ROOT / 'tools' / 'migrations'))
DESCRIPTION_RENAMES = import_module('02_parameter_description_hints').RENAMED_PARAMETERS
sys.path.pop(0)
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
ENTRIES = {v: {e['id']: e for e in c['entries']} for v, c in CAT.items()}


def resolve_text(ref, pool):
    return ref if isinstance(ref, dict) else pool.get(ref)


def js_call_arguments(source, name):
    """Split ordinary JS call arguments, respecting nested brackets and strings.

    This is intentionally limited to UI calls (no regex/template literals in
    their arguments), not a general JavaScript parser.
    """
    for match in re.finditer(r'\b' + name + r'\(', source):
        args, start, depth, quote, escape = [], match.end(), 0, None, False
        for i in range(start, len(source)):
            char = source[i]
            if quote:
                if escape:
                    escape = False
                elif char == '\\':
                    escape = True
                elif char == quote:
                    quote = None
                continue
            if char in "'\"`":
                quote = char
            elif char in '([{':
                depth += 1
            elif char == ')' and depth == 0:
                args.append(source[start:i].strip())
                yield args
                break
            elif char in ')]}':
                depth -= 1
            elif char == ',' and depth == 0:
                args.append(source[start:i].strip())
                start = i + 1


def static_ui_keys(source):
    """Find keys at T() call sites and their local maps/arrays/caption sources."""
    found = set(re.findall(r'data-i18n="([A-Za-z0-9_]+)"', source))
    token = r"['\"]([A-Za-z0-9_]+)['\"]"
    arguments = [args[0] for args in js_call_arguments(source, 'T') if args]
    for argument in arguments:
        direct = re.fullmatch(token, argument)
        if direct:
            found.add(direct[1])
        # Conditional outcomes and fallback values are keys; comparison values
        # (e.g. basis==='official_translation') are deliberately not included.
        found.update(re.findall(r'(?:\?|:|\|\|)\s*' + token, argument))
        if argument.startswith('['):
            found.update(re.findall(token, argument))
    for name in ('key', 'typeNames', 'labels'):
        if any(re.search(r'\b' + name + r'\b', a) for a in arguments):
            for mapping in re.findall(r'\b' + name + r'\s*=\s*\{([^}]+)\}([^;]*);', source):
                found.update(re.findall(r':\s*' + token, mapping[0]))
                found.update(re.findall(r'\|\|\s*' + token, mapping[1]))
    # options(id, items, caption, value) passes caption to T(caption).
    for args in js_call_arguments(source, 'options'):
        if len(args) >= 3:
            caption = re.fullmatch(token, args[2])
            if caption:
                found.add(caption[1])
    # T(k) consumes these navigation and paragraph lists.
    arrays = re.findall(r'\b(?:categories)\s*=\s*\[([^\]]*)\]', source)
    arrays += re.findall(r'for\(const k of \[([^\]]*)\]\)[^;]*\bT\(k\)', source)
    arrays += re.findall(r'\[([^\[\]]*)\]\.map\(k=>', source)
    for array in arrays:
        found.update(re.findall(token, array))
    return found

# 2. history graph -------------------------------------------------------------
families = {fid: f for h in HIST.values() for fid, f in h['families'].items()}
entry_ids = {e['id'] for c in CAT.values() for e in c['entries']}
referenced = {e['family']['id'] for c in CAT.values() for e in c['entries']}
check(set(families) == referenced, f'unreferenced families: {len(set(families) - referenced)}, missing: {len(referenced - set(families))}')
for fid, f in families.items():
    for r in f['related']:
        check(r['id'] in families, f'broken related link {fid} -> {r["id"]}')
    for z in f['versions']:
        version_entries = ENTRIES.get(z['version'], {})
        for i in z['entry_ids']:
            check(i in version_entries, f'family {fid} lists unknown entry {i} in v{z["version"]}')
        check(len(z['entry_ids']) == len(set(z['entry_ids'])), f'family {fid} v{z["version"]}: duplicate entry_ids')
        expected_ids = {e['id'] for e in version_entries.values() if e['family']['id'] == fid}
        check(set(z['entry_ids']) == expected_ids, f'family {fid} v{z["version"]}: entry_ids differ from catalog family')
        if all(i in version_entries for i in z['entry_ids']):
            expected = family_version_aggregate([version_entries[i] for i in z['entry_ids']])
            actual = normalized_history_aggregate(z)
            for field, value in expected.items():
                check(actual[field] == value, f'family {fid} v{z["version"]}: history aggregate mismatch: {field}')
for v, c in CAT.items():
    for e in c['entries']:
        fam = families.get(e['family']['id'])
        check(fam is not None and v in [z['version'] for z in fam['versions']], f'entry {e["id"]} is not listed in its family')
print(f'history: {len(families)} families, all referenced, all links resolved')

# Pools are independent: even identical hashes must exist in the local shard.
for label, document in [(f'catalog-v{v}', c) for v, c in CAT.items()] + [(f'history-{k}', h) for k, h in HIST.items()]:
    failures.extend(text_pool_errors(document, label))
print('text pools: full catalog/history references, orphans, and empty texts checked')

# 3. per-catalog invariants ------------------------------------------------------
stats = collections.Counter()
for v, c in CAT.items():
    ids = [e['id'] for e in c['entries']]
    check(len(set(ids)) == len(ids), f'duplicate ids in v{v}')
    texts = c['texts']
    expected_counts, expected_structure = catalog_aggregates(c)
    for field, value in expected_counts.items():
        check(c['counts'].get(field) == value, f'v{v}: counts mismatch: {field}')
    check(c['structure_counts'] == expected_structure, f'v{v}: structure_counts mismatch')
    conflict_issues = {(issue.get('entry_id'), issue.get('parameter')) for issue in c.get('source_issues', []) if issue.get('type') == 'source_conflict'}
    for tid, item in texts.items():
        # The empty remarks sentinel is deliberately retained by the source
        # schema. No other text may present empty content as editorial evidence.
        if tid != 'e3b0c44298fc1c14' and item.get('basis'):
            check(has_text(item), f'v{v}: empty text with basis: {tid}')

    def need(ref, where):
        if isinstance(ref, str) and re.fullmatch(r'[0-9a-f]{16}', ref):
            check(ref in texts, f'v{v}: missing text {ref} ({where})')

    for e in c['entries']:
        x = e['examples']
        items = x.get('items', [])
        check(bool(items) == (x['status'] != 'missing'), f'v{v} {e["id"]}: examples.status does not match items')
        check(not any(re.fullmatch(r'\s*//\s*@version\s*=\s*\d+\s*', item.get('code', '')) for item in items), f'v{v} {e["id"]}: isolated version-directive example fragment')
        # Historical operator syntax illustrations can list three independent
        # forms (binary '+', unary '+', token '+'); these are not split programs.
        syntax_forms = x.get('status') == 'syntax_illustration' and e['category'] == 'operators'
        check(not (not syntax_forms and len(items) >= 3 and all('\n' not in item.get('code', '') for item in items)), f'v{v} {e["id"]}: three or more single-line example fragments')
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
            if p.get('state') == 'conflict':
                stats['requiredness_conflicts'] += 1
                check((e['id'], p['name']) in conflict_issues, f'v{v} {e["id"]}.{p["name"]}: requiredness conflict has no source issue')
            if p.get('type_candidates'):
                stats['type_hints'] += 1
                check(not p.get('types'), f'v{v} {e["id"]}: type hint on a parameter that already has types')
            if p.get('type_issue'):
                stats['legacy_params'] += 1
            need(p.get('description'), e['id'])
            description = resolve_text(p.get('description'), texts)
            hint = p.get('description_hint')
            missing = p.get('description_missing') is True
            check(has_text(description) or bool(hint) or missing, f'v{v} {e["id"]}.{p["name"]}: parameter description has no explicit availability state')
            check(not (missing and (has_text(description) or hint)), f'v{v} {e["id"]}.{p["name"]}: contradictory description_missing')
            if hint:
                stats['description_hints'] += 1
                check(isinstance(hint, dict), f'v{v} {e["id"]}.{p["name"]}: malformed description_hint')
                if not isinstance(hint, dict):
                    continue
                donor = ENTRIES.get(hint.get('version'), {}).get(hint.get('entry_id'))
                donor_param = next((q for q in (donor or {}).get('parameters', []) if q['name'] == hint.get('parameter')), None)
                local_text = resolve_text(hint.get('text'), texts)
                donor_text = resolve_text((donor_param or {}).get('description'), CAT.get(hint.get('version'), {}).get('texts', {}))
                check(donor is not None and hint.get('version') != v, f'v{v} {e["id"]}.{p["name"]}: description donor is missing or not a neighbour version')
                check(donor is not None and donor['family']['id'] == e['family']['id'], f'v{v} {e["id"]}.{p["name"]}: description hint donor belongs to a different family')
                check(donor is not None and donor['category'] == e['category'], f'v{v} {e["id"]}.{p["name"]}: description hint donor belongs to a different category')
                allowed_names = {p['name']}
                renamed = DESCRIPTION_RENAMES.get((e['family']['id'], p['name']))
                if renamed:
                    allowed_names.add(renamed)
                check(hint.get('parameter') in allowed_names, f'v{v} {e["id"]}.{p["name"]}: description hint uses an unreviewed parameter rename')
                check(donor_param is not None and has_text(local_text) and local_text == donor_text, f'v{v} {e["id"]}.{p["name"]}: description hint differs from its nonempty donor text')
                check(bool(hint.get('sources')) and hint['sources'] == (donor or {}).get('sources'), f'v{v} {e["id"]}.{p["name"]}: description hint source provenance differs from donor')
                check(not has_text(description), f'v{v} {e["id"]}.{p["name"]}: description hint masks an available source description')
            elif missing:
                stats['descriptions_missing'] += 1
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
            # Core constructs use exact aliases and a generic category bonus
            # in wiki-search.js; the older editorial rank remains MA-only.
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
literal_used = static_ui_keys(app)
dynamic_used = set()
for c in CAT.values():
    for e in c['entries']:
        dynamic_used.add(e['basis'])
        role = e['structure']['role']
        dynamic_used.add('role' + role[0].upper() + role[1:])
        dynamic_used.add('count' + role[0].upper() + role[1:])
        # part/detail rows render their role kind instead of category kind.
        dynamic_used.add(role + 'Kind' if role in ('part', 'detail') else e['category'] + 'Kind')
        dynamic_used.add(e['category'])  # category navigation
        for p in e['parameters']:
            for field in ('state', 'metadata_state', 'prose_state'):
                dynamic_used.add(p.get(field) or 'notSpecified')
for f in families.values():
    for version in f['versions']:
        for states in version.get('requiredness', {}).values():
            dynamic_used.update(states or ['unknown'])
used = literal_used | dynamic_used
for k in sorted(used):
    check(k in ui, 'missing UI string: ' + k)
for k, val in ui.items():
    check(isinstance(val, list) and len(val) == 2 and all(isinstance(s, str) and s for s in val), 'malformed UI string: ' + k)
for k in sorted(set(ui) - used):
    check(False, 'unused UI string: ' + k)
print(f'ui strings: {len(used)} keys used, {len(ui)} defined (ru+en); {len(dynamic_used)} dynamic keys checked')

# 5. JS syntax (only when node is installed) ---------------------------------------
node = shutil.which('node')
if node:
    for f in sorted(ROOT.glob('*.js')):
        r = subprocess.run([node, '--check', str(f)], capture_output=True, text=True)
        check(r.returncode == 0, f'syntax error in {f.name}: {r.stderr[:200]}')
    print('js syntax: node --check passed for all files')
else:
    print('js syntax: node not found, skipped')

# 6. Generated release documentation -------------------------------------------
release_docs = ROOT / 'tools' / 'release_docs.py'
if release_docs.exists():
    result = subprocess.run([sys.executable, str(release_docs), '--check'], capture_output=True, text=True, encoding='utf-8')
    check(result.returncode == 0, 'stale release documentation: ' + (result.stdout + result.stderr).strip()[:500])
    if result.returncode == 0:
        print('release documentation: generated files are current')

print('release counts:', {f'v{v}': len(c['entries']) for v, c in CAT.items()})
if failures:
    print(f'\n{len(failures)} FAILED CHECKS:')
    for m in failures[:40]:
        print(' -', m)
    sys.exit(1)
print('ALL CHECKS PASSED')
