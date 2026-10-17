#!/usr/bin/env python3
"""Print factual release metrics as JSON; no dependencies or data mutation."""
import argparse
import json
from pathlib import Path
from build_manifest import load_manifest

ROOT = Path(__file__).resolve().parents[1]


def load_catalog(version):
    return json.loads((ROOT / f'catalog-v{version}.js').read_text(encoding='utf-8').split(f'window.PINE_CATALOG[{version}]=', 1)[1].strip().removesuffix(';'))


def has_text(catalog, ref):
    t = catalog['texts'].get(ref, {})
    return any(str(t.get(k) or '').strip() for k in ('ru', 'en', 'original'))


def collect():
    manifest = load_manifest()
    versions = {}
    families = set()
    for version in range(1, 7):
        c = load_catalog(version)
        entries = c['entries']
        params = [p for e in entries for p in e.get('parameters', [])]
        families.update(e['family']['id'] for e in entries)
        empty = [p for p in params if not has_text(c, p.get('description'))]
        result_empty = [e for e in entries if not has_text(c, e.get('result', {}).get('description'))]
        versions[str(version)] = {
            'cards': len(entries),
            'example_items': sum(len(e['examples'].get('items', [])) for e in entries),
            'fragmented_example_cards': sum(len(e['examples'].get('items', [])) > 1 and all('\n' not in i['code'] for i in e['examples']['items']) for e in entries),
            'parameters': len(params),
            'empty_parameter_descriptions': len(empty),
            'parameter_description_hints': sum(bool(p.get('description_hint')) for p in params),
            'parameters_without_description_or_hint': sum(not p.get('description_hint') for p in empty),
            'unknown_requiredness': sum(p.get('state') == 'unknown' for p in params),
            'conflicting_requiredness': sum(p.get('state') == 'conflict' for p in params),
            'empty_result_descriptions': len(result_empty),
            'noncallable_empty_result_descriptions': sum(e['category'] not in ('functions', 'methods') for e in result_empty),
            'type_hints': sum(bool(p.get('type_candidates')) for p in params),
            'legacy_parameters': sum(bool(p.get('type_issue')) for p in params),
            'neighbor_result_descriptions': sum(e['result'].get('description_basis') == 'family_neighbor_description' for e in entries),
            'templates': sum(bool(e['examples'].get('template')) for e in entries),
            'pointers': sum(len(e['examples'].get('pointers', [])) for e in entries),
            'search_rank_entries': sum(bool(e.get('search_rank')) for e in entries),
            'catalog_bytes': (ROOT / f'catalog-v{version}.js').stat().st_size,
        }
    ui = json.loads((ROOT / 'wiki-i18n.js').read_text(encoding='utf-8').split('window.PINE_UI=', 1)[1].strip().removesuffix(';'))
    return {'revision': manifest['revision'], 'cards_total': sum(v['cards'] for v in versions.values()), 'families': len(families), 'ui_keys_defined': len(ui), 'versions': versions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = json.dumps(collect(), ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding='utf-8', newline='\n')
    else:
        print(output, end='')


if __name__ == '__main__':
    main()
