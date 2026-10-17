#!/usr/bin/env python3
"""Add basic Russian concept aliases without changing source descriptions.

Idempotent, standard-library-only migration. Preserve the catalogue wrapper,
JSON key order, and existing aliases. Search priorities remain generic.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALIASES = {
    'indicator': ('индикатор',),
    'strategy': ('стратегия',),
    'library': ('библиотека',),
    'array': ('массив',),
    'matrix': ('матрица',),
    'map': ('словарь', 'карта'),
    'label': ('метка',),
    'line': ('линия',),
    'box': ('бокс',),
    'table': ('таблица',),
    'ta.stdev': ('среднеквадратичное отклонение', 'стандартное отклонение'),
    'stdev': ('среднеквадратичное отклонение', 'стандартное отклонение'),
}


def main():
    total = 0
    for version in range(1, 7):
        path = ROOT / f'catalog-v{version}.js'
        original = path.read_text(encoding='utf-8')
        match = re.fullmatch(r'(.*?window\.PINE_CATALOG\[' + str(version) + r'\]\s*=\s*)(\{.*\})(;\s*)', original, re.S)
        if not match:
            raise ValueError(f'Unexpected wrapper: {path.name}')
        cat = json.loads(match[2])
        changes = 0
        for entry in cat['entries']:
            if entry['category'] not in ('functions', 'types', 'keywords'):
                continue
            aliases = entry.setdefault('synonyms', [])
            for alias in ALIASES.get(entry['name'], ()):
                if alias not in aliases:
                    aliases.append(alias)
                    changes += 1
        if changes:
            # Existing files use compact JSON; preserve their preamble/trailer.
            path.write_text(match[1] + json.dumps(cat, ensure_ascii=False, separators=(',', ':')) + match[3], encoding='utf-8', newline='\n')
        total += changes
        print(f'v{version}: {changes} aliases added')
    print(f'total: {total} aliases added')


if __name__ == '__main__':
    main()
