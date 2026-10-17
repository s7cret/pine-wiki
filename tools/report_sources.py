#!/usr/bin/env python3
"""Generate reproducible source URL inventory and requiredness backlog CSV."""
import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
from metrics import load_catalog

ROOT = Path(__file__).resolve().parents[1]


def walk(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == 'url' and isinstance(child, str) and child.startswith(('https://', 'http://')):
                yield child
            else:
                yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    counts = Counter()
    conflicts = []
    for version in range(1, 7):
        catalog = load_catalog(version)
        counts.update(walk(catalog))
        for entry in catalog['entries']:
            for param in entry.get('parameters', []):
                if param.get('state') != 'conflict':
                    continue
                issues = [issue['id'] for issue in catalog.get('source_issues', [])
                          if issue.get('entry_id') == entry['id'] and issue.get('parameter') == param['name']]
                conflicts.append([version, entry['name'], param['name'], entry['id'],
                                  param.get('metadata_state'), param.get('prose_state'), '|'.join(issues)])
    (ROOT / 'docs').mkdir(exist_ok=True)
    with (ROOT / 'docs/source-inventory.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['domain', 'url', 'occurrences_in_catalogs'])
        writer.writerows((urlparse(url).netloc, url, n) for url, n in sorted(counts.items()))
    with (ROOT / 'docs/requiredness-conflicts.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['version', 'function', 'parameter', 'entry_id', 'metadata_state', 'prose_state', 'source_issue_ids'])
        writer.writerows(conflicts)
    print(f'sources: {len(counts)} distinct URLs; requiredness conflicts: {len(conflicts)}')
    print(f'conflicts without an explicit source issue: {sum(not c[-1] for c in conflicts)}')


if __name__ == '__main__':
    main()
