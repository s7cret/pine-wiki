#!/usr/bin/env python3
"""Mutation checks proving that the verifier rejects damaged release data.

Only a fresh temporary fixture is changed. Manifest hashes are rebuilt before
each verification, so a hash mismatch cannot masquerade as an invariant check.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def load(path, prefix):
    source = path.read_text(encoding='utf-8')
    return json.loads(source.split(prefix, 1)[1].strip().removesuffix(';'))


def write(path, prefix, value):
    path.write_text(prefix + json.dumps(value, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    results = []
    environment = dict(os.environ, PYTHONIOENCODING='utf-8')
    scratch = (ROOT / '.runtime').resolve()
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='pine-verifier-', dir=scratch) as temporary:
        fixture = Path(temporary).resolve()
        # Cleanup is restricted to the freshly created temporary directory.
        assert fixture.parent == scratch and fixture.name.startswith('pine-verifier-')
        (fixture / 'tools').mkdir()
        for source in [*ROOT.glob('*.js'), ROOT / 'index.html']:
            shutil.copy2(source, fixture / source.name)
        # Test the data/UI verifier alone; generated release prose is not part
        # of this intentionally malformed fixture.
        for name in ('verify_catalog.py', 'build_manifest.py'):
            shutil.copy2(ROOT / 'tools' / name, fixture / 'tools' / name)
        (fixture / 'tools' / 'migrations').mkdir()
        for name in ('02_parameter_description_hints.py', 'catalog_io.py'):
            shutil.copy2(ROOT / 'tools' / 'migrations' / name, fixture / 'tools' / 'migrations' / name)

        def verify(name, expected=None):
            subprocess.run([sys.executable, str(fixture / 'tools' / 'build_manifest.py')], check=True, capture_output=True, env=environment)
            run = subprocess.run([sys.executable, str(fixture / 'tools' / 'verify_catalog.py')], capture_output=True, text=True, encoding='utf-8', env=environment)
            output = run.stdout + run.stderr
            passed = run.returncode == 0 if expected is None else run.returncode != 0 and expected in output
            passed = passed and 'wrong sha256' not in output and 'wrong size:' not in output
            results.append({'name': name, 'passed': passed, 'expected': expected, 'exit_code': run.returncode})
            print(('PASS ' if passed else 'FAIL ') + name)
            if not passed:
                print(output)

        verify('clean isolated fixture')
        target = fixture / 'catalog-v5.js'
        prefix = 'window.PINE_CATALOG[5]='
        catalog = load(target, prefix)
        entry = next(e for e in catalog['entries'] if e['name'] == 'ta.sar')
        entry['examples']['items'].append({'code': '//@version=5', 'source': entry['examples']['items'][0]['source']})
        write(target, prefix, catalog)
        verify('isolated version directive rejected after hash rebuild', 'isolated version-directive example fragment')
        shutil.copy2(ROOT / target.name, target)

        # A real source, valid donor parameter and identical text still cannot
        # establish a relationship between unrelated functions.
        target = fixture / 'catalog-v4.js'
        prefix = 'window.PINE_CATALOG[4]='
        catalog = load(target, prefix)
        donor_catalog = load(fixture / 'catalog-v5.js', 'window.PINE_CATALOG[5]=')
        entry = next(e for e in catalog['entries'] if e['name'] == 'na' and e['category'] == 'functions')
        parameter = next(p for p in entry['parameters'] if p['name'] == 'x')
        donor = next(e for e in donor_catalog['entries'] if e['name'] == 'math.abs' and e['category'] == 'functions')
        donor_parameter = next(p for p in donor['parameters'] if p['name'] == 'number')
        parameter['description_hint'] = {'version': 5, 'entry_id': donor['id'], 'parameter': 'number', 'text': donor_parameter['description'], 'sources': donor['sources']}
        catalog['texts'][donor_parameter['description']] = donor_catalog['texts'][donor_parameter['description']]
        write(target, prefix, catalog)
        verify('foreign description donor rejected despite valid text/source', 'description hint donor belongs to a different family')
        shutil.copy2(ROOT / target.name, target)

        target = fixture / 'wiki-i18n.js'
        prefix = 'window.PINE_UI='
        ui = load(target, prefix)
        del ui['roleApi']
        write(target, prefix, ui)
        verify('missing dynamically assembled role key rejected', 'missing UI string: roleApi')
        shutil.copy2(ROOT / target.name, target)
        ui = load(target, prefix)
        ui['unusedRegressionSentinel'] = ['Не используется', 'Unused']
        write(target, prefix, ui)
        verify('unused UI key rejected', 'unused UI string: unusedRegressionSentinel')

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({'checks': results}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return 0 if all(result['passed'] for result in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
