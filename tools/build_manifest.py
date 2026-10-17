#!/usr/bin/env python3
"""Rebuild the existing manifest without changing its schema or key order."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'window.PINE_MANIFEST='


def load_manifest():
    return json.loads((ROOT / 'wiki-manifest.js').read_text(encoding='utf-8').split(PREFIX, 1)[1].strip().removesuffix(';'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision')
    parser.add_argument('--check', action='store_true', help='Check without rewriting any file')
    args = parser.parse_args()
    manifest = load_manifest()
    changed = []
    for group in ('versions', 'histories'):
        for item in manifest[group].values():
            data = (ROOT / item['file']).read_bytes()
            actual = (len(data), hashlib.sha256(data).hexdigest())
            if actual != (item['bytes'], item['sha256']):
                changed.append(item['file'])
            item['bytes'], item['sha256'] = actual
    if args.revision and args.revision != manifest.get('revision'):
        changed.append('revision')
        manifest['revision'] = args.revision
    if args.check:
        if changed:
            raise SystemExit('Manifest is stale: ' + ', '.join(changed))
        print('manifest: all 22 hashes and sizes are current')
        return
    # Keep created_utc as the original snapshot timestamp. Rebuilds are deterministic.
    target = ROOT / 'wiki-manifest.js'
    output = PREFIX + json.dumps(manifest, ensure_ascii=False, separators=(',', ':')) + ';\n'
    if target.read_bytes() != output.encode('utf-8'):
        target.write_text(output, encoding='utf-8', newline='\n')
    print('manifest: ' + (', '.join(changed) if changed else 'unchanged'))


if __name__ == '__main__':
    main()
