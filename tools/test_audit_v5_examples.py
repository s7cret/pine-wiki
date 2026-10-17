#!/usr/bin/env python3
"""Check that the v5 audit is independent of its previous output (stdlib only)."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/audit_v5_examples.py'
EXPECTED_COUNTS = {'same_except_version_and_empty_lines': 466,
                   'trailing_whitespace_only': 64, 'reviewed_difference': 44}


def run(*args, success=True):
    result = subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                            capture_output=True, text=True, encoding='utf-8')
    if (result.returncode == 0) != success:
        raise AssertionError(result.stdout + result.stderr)
    return result


def main():
    expected = (ROOT / 'docs/v5-example-audit.json').read_bytes()
    temporary_root = (ROOT / '.runtime').resolve()
    temporary_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='pine-v5-audit-', dir=temporary_root) as directory:
        scratch = Path(directory).resolve()
        assert scratch.parent == temporary_root and scratch.name.startswith('pine-v5-audit-')
        output = scratch / 'audit.json'
        run('--output', output)
        assert output.read_bytes() == expected, 'Fresh audit differs from the reviewed report'
        report = json.loads(output.read_bytes())
        assert len(report['entries']) == 574 and report['counts'] == EXPECTED_COUNTS
        print('PASS: absent output regenerates all 574 reviewed records byte for byte')

        output.write_text('{corrupt output', encoding='utf-8')
        run('--output', output, '--check', success=False)
        assert output.read_text('utf-8') == '{corrupt output', '--check modified the file'
        run('--output', output)
        assert output.read_bytes() == expected, 'Audit depends on previous output'
        run('--output', output, '--check')
        print('PASS: corrupt output is detected read-only and can be regenerated')

        # A missing canonical input must fail loudly rather than silently reduce
        # the audited set, even when a complete previous report is available.
        sys.path.insert(0, str(ROOT / 'tools/migrations'))
        from catalog_io import load_catalog, save_catalog
        shutil.copyfile(ROOT / 'catalog-v5.js', scratch / 'catalog-v5.js')
        shutil.copyfile(ROOT / 'catalog-v6.js', scratch / 'catalog-v6.js')
        catalog, wrapper = load_catalog(scratch, 5)
        removed = report['entries'][0]['entry_id']
        catalog['entries'] = [e for e in catalog['entries'] if e['id'] != removed]
        save_catalog(catalog, wrapper)
        result = run('--root', scratch, '--output', output, success=False)
        assert 'Merged v5 entries missing from catalog' in result.stderr
        assert output.read_bytes() == expected, 'Failed audit overwrote the existing report'
        print('PASS: missing canonical catalog entry is rejected without overwriting output')
    return 0


if __name__ == '__main__':
    sys.exit(main())
