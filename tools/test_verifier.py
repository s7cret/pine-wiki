#!/usr/bin/env python3
"""Mutation checks proving that the verifier rejects damaged release data.

Only a fresh temporary fixture is changed. Manifest hashes are rebuilt before
each verification, so a hash mismatch cannot masquerade as an invariant check.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from data_integrity import text_references

ROOT = Path(__file__).resolve().parents[1]


def load(path, prefix):
    source = path.read_text(encoding='utf-8')
    return json.loads(source.split(prefix, 1)[1].strip().removesuffix(';'))


def write(path, prefix, value):
    path.write_text(prefix + json.dumps(value, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    parser.add_argument('--reverse', action='store_true', help='Run independent mutations in reverse order')
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
        for name in ('verify_catalog.py', 'build_manifest.py', 'data_integrity.py', 'semantic_contracts.py'):
            shutil.copy2(ROOT / 'tools' / name, fixture / 'tools' / name)
        (fixture / 'tools' / 'migrations').mkdir()
        for name in ('02_parameter_description_hints.py', 'catalog_io.py', '05_clean_history_texts.py'):
            shutil.copy2(ROOT / 'tools' / 'migrations' / name, fixture / 'tools' / 'migrations' / name)

        baseline = {p.name: p.read_bytes() for p in fixture.iterdir() if p.is_file()}
        previous_scenario = 'fixture creation'

        def assert_clean():
            changed = [name for name, raw in baseline.items() if (fixture / name).read_bytes() != raw]
            if changed:
                raise AssertionError(f'Fixture contamination after {previous_scenario}: {changed[:5]}')

        def verify(name, expected=None):
            nonlocal previous_scenario
            subprocess.run([sys.executable, str(fixture / 'tools' / 'build_manifest.py')], check=True, capture_output=True, env=environment)
            run = subprocess.run([sys.executable, str(fixture / 'tools' / 'verify_catalog.py')], capture_output=True, text=True, encoding='utf-8', env=environment)
            output = run.stdout + run.stderr
            passed = run.returncode == 0 if expected is None else run.returncode != 0 and expected in output
            passed = passed and 'wrong sha256' not in output and 'wrong size:' not in output
            results.append({'name': name, 'passed': passed, 'expected': expected, 'exit_code': run.returncode})
            print(('PASS ' if passed else 'FAIL ') + name)
            if not passed:
                print(output)
            # Restore every fixture file, including the rebuilt manifest, from
            # immutable bytes. A scenario can affect more than its named file.
            for filename, raw in baseline.items():
                (fixture / filename).write_bytes(raw)
            previous_scenario = name
            assert_clean()

        verify('clean isolated fixture')

        pending_mutations = []

        def mutation(filename, prefix, change, name, expected):
            pending_mutations.append((filename,prefix,change,name,expected))

        def run_mutation(filename, prefix, change, name, expected):
            assert_clean()
            target = fixture / filename
            data = load(target, prefix)
            change(data)
            write(target, prefix, data)
            verify(name, expected)
            shutil.copy2(ROOT / filename, target)

        dummy_text = {'ru': 'Проверка отсутствующей ссылки', 'en': 'Unreferenced mutation fixture', 'original': 'Unreferenced mutation fixture', 'basis': 'editorial_summary'}
        for filename, prefix, label in (
            ('catalog-v5.js', 'window.PINE_CATALOG[5]=', 'catalog-v5'),
            ('history-2.js', 'window.PINE_HISTORY["2"]=', 'history-2'),
        ):
            mutation(filename, prefix, lambda data: data['texts'].update({'0123456789abcdef': dummy_text}),
                     f'{label} orphan text rejected after hash rebuild', f'{label}: orphan text 0123456789abcdef')

        # Exercise the nested fields omitted by the original cleanup proposal.
        # Replacing links with unknown hashes proves detection is independent of
        # membership in the text pool, not only a lookup of existing text IDs.
        def break_supplement(data):
            data['families']['functions:ta.cross']['versions'][3]['description_supplements'][0]['description'] = '0123456789abcdef'
        mutation('history-2.js', 'window.PINE_HISTORY["2"]=', break_supplement,
                 'missing history supplement text rejected', 'history-2: missing text 0123456789abcdef')

        def break_evidence(data):
            for family in data['families'].values():
                for version in family['versions']:
                    for contract in version.get('default_contracts', {}).values():
                        if contract['evidence']:
                            contract['evidence'][0]['text_ref'] = '0123456789abcdef'
                            return
            raise AssertionError('No default-contract evidence in fixture')
        mutation('history-0.js', 'window.PINE_HISTORY["0"]=', break_evidence,
                 'missing history default-contract text rejected', 'history-0: missing text 0123456789abcdef')

        def break_related(data):
            for family in data['families'].values():
                for related in family['related']:
                    if related.get('note'):
                        related['note'] = '0123456789abcdef'
                        return
            raise AssertionError('No related note in fixture')
        mutation('history-0.js', 'window.PINE_HISTORY["0"]=', break_related,
                 'missing history related note rejected', 'history-0: missing text 0123456789abcdef')

        def erase_used_text(data):
            ref = data['families']['functions:ta.cross']['versions'][3]['description_supplements'][0]['description']
            data['texts'][ref] = {'ru': '', 'en': '', 'original': ''}
        mutation('history-2.js', 'window.PINE_HISTORY["2"]=', erase_used_text,
                 'empty history text without basis rejected', 'history-2: empty text')

        mutation('catalog-v5.js', 'window.PINE_CATALOG[5]=',
                 lambda data: data['counts'].__setitem__('public_records', data['counts']['public_records'] + 1),
                 'wrong public record count rejected', 'counts mismatch: public_records')
        mutation('catalog-v5.js', 'window.PINE_CATALOG[5]=',
                 lambda data: data['counts']['categories']['functions'].__setitem__('records', data['counts']['categories']['functions']['records'] + 1),
                 'wrong category record count rejected', 'counts mismatch: categories')
        mutation('catalog-v5.js', 'window.PINE_CATALOG[5]=',
                 lambda data: data['structure_counts'].__setitem__('api', data['structure_counts']['api'] + 1),
                 'wrong distinct structure count rejected', 'structure_counts mismatch')

        for field in ('parameters', 'types', 'requiredness', 'return_types'):
            def change_aggregate(data, field=field):
                version = data['families']['functions:indicator']['versions'][0]
                if isinstance(version[field], dict):
                    del version[field][next(iter(version[field]))]
                else:
                    version[field].pop()
            mutation('history-0.js', 'window.PINE_HISTORY["0"]=', change_aggregate,
                     f'wrong history {field} aggregate rejected', f'history aggregate mismatch: {field}')

        def flip_default(data):
            e=next(e for e in data['entries'] if e['name']=='indicator')
            p=next(p for p in e['parameters'] if p['name']=='overlay')
            p['default_contract']['values']=['true']
        mutation('catalog-v6.js','window.PINE_CATALOG[6]=',flip_default,
                 'default changed despite unchanged evidence rejected','DEFAULT_EVIDENCE')

        def foreign_result(data):
            e=next(e for e in data['entries'] if e['name']=='floor')
            e['result']['description_donor']={'version':4,'entry_id':'primary:v4:functions:abs:overload:0'}
        mutation('catalog-v4.js','window.PINE_CATALOG[4]=',foreign_result,
                 'unrelated result donor rejected','RESULT_DONOR')

        def wrong_shard(data):
            next(e for e in data['entries'] if e['name']=='indicator')['family']['shard']='f'
        mutation('catalog-v6.js','window.PINE_CATALOG[6]=',wrong_shard,
                 'family absent from declared shard rejected','FAMILY_ROUTE')

        def truncated_number(data):
            e=next(e for e in data['entries'] if e['name']=='request.security')
            p=next(p for p in e['parameters'] if p['name']=='calc_bars_count')
            p['default_contract']['values']=['100']
            p['default_contract']['evidence'][0]['value']='100'
        mutation('catalog-v5.js','window.PINE_CATALOG[5]=',truncated_number,
                 'truncated thousands literal rejected','DEFAULT_EVIDENCE')

        def fake_execution(data):
            next(e for e in data['entries'] if e['examples']['items'])['examples']['items'][0]['execution_status']='executed'
        mutation('catalog-v6.js','window.PINE_CATALOG[6]=',fake_execution,
                 'execution claim without run evidence rejected','EXAMPLE_STATUS')

        for scenario in reversed(pending_mutations) if args.reverse else pending_mutations:
            run_mutation(*scenario)

        # The cleanup must remove only the newly injected orphan, preserve the
        # entire original family graph/text pool, and be byte-idempotent.
        assert_clean()
        target = fixture / 'history-2.js'
        prefix = 'window.PINE_HISTORY["2"]='
        clean_history = load(target, prefix)
        dirty_history = load(target, prefix)
        dirty_history['texts']['0123456789abcdef'] = dummy_text
        write(target, prefix, dirty_history)
        migration = [sys.executable, str(fixture / 'tools' / 'migrations' / '05_clean_history_texts.py')]
        first_run = subprocess.run(migration, check=True, capture_output=True, text=True, env=environment)
        first_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in fixture.glob('history-*.js')}
        second_run = subprocess.run(migration, check=True, capture_output=True, text=True, env=environment)
        unchanged = first_hashes == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in fixture.glob('history-*.js')}
        passed = (load(target, prefix) == clean_history and unchanged and
                  json.loads(first_run.stdout)['total_removed'] == 1 and json.loads(second_run.stdout)['total_removed'] == 0)
        results.append({'name': 'history cleanup preserves live data and is byte-idempotent', 'passed': passed})
        print(('PASS ' if passed else 'FAIL ') + results[-1]['name'])
        shutil.copy2(ROOT / target.name, target)

        # Hex-looking literal IDs and parameter names are not text references.
        refs = list(text_references({'id': '1' * 16, 'entry_id': '2' * 16,
                    'entry_ids': ['3' * 16], 'family': {'id': '4' * 16},
                    'parameters': [{'name': '5' * 16, 'description': 'a' * 16}],
                    'texts': {'b' * 16: dummy_text}}))
        passed = refs == [('a' * 16, 'parameters.0.description')]
        results.append({'name': 'literal hex identifiers do not masquerade as text references', 'passed': passed})
        print(('PASS ' if passed else 'FAIL ') + results[-1]['name'])

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
