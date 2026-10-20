#!/usr/bin/env python3
"""One release check command; persist actual subprocess results for QA reporting."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def source_fingerprint():
    # QA outputs and generated documentation are excluded to avoid circular hashes.
    files = sorted([*ROOT.glob('*.js'), *ROOT.glob('*.css'), ROOT / 'index.html',
                    *ROOT.glob('tools/*.py'), *ROOT.glob('tools/*.js'), *ROOT.glob('tools/*.json'),
                    *ROOT.glob('tools/migrations/*.py'), *ROOT.glob('tools/migrations/*.json'),
                    *ROOT.glob('consumer/*.py'), *ROOT.glob('consumer/*.json'),
                    ROOT/'requirements-dev.txt', ROOT/'package.json', ROOT/'docs/SEMANTIC_PROFILE.md', ROOT/'docs/AUDIT_V2_2026-10-20.md', ROOT/'docs/AUDIT_6091_2026-10-20.md',
                    *[p for p in (ROOT/'spec').rglob('*') if p.is_file() and p.suffix in ('.json','.js','.html','.pine','.txt','.jpg')],
                    *[p for p in (ROOT/'bundles').rglob('*') if p.is_file()]])
    h = hashlib.sha256()
    for path in files:
        h.update(path.relative_to(ROOT).as_posix().encode())
        h.update(b'\0')
        h.update(path.read_bytes())
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'test-results/check-results.json')
    args = parser.parse_args()
    node = shutil.which('node') or 'node'
    commands = [
        [sys.executable, 'tools/build_manifest.py', '--check'],
        [sys.executable, 'tools/verify_catalog.py'],
        [sys.executable, 'tools/verify_spec.py'],
        [sys.executable, 'tools/project_spec.py', '--check'],
        [sys.executable, 'tools/test_spec.py'],
        [sys.executable, 'tools/test_audit_6091.py'],
        [node, 'tools/test_example_status.js'],
        [sys.executable, 'tools/test_release_consumer.py'],
        [sys.executable, 'tools/test_verifier.py', '--json', 'test-results/verifier-guards.json'],
        [sys.executable, 'tools/test_verifier.py', '--reverse', '--json', 'test-results/verifier-guards-reverse.json'],
        [sys.executable, 'tools/test_audit_v5_examples.py'],
        [sys.executable, 'tools/test_semantic_contracts.py'],
        [node, 'tools/search_regression.js'],
        [sys.executable, 'tools/e2e_smoke.py', '--screenshots', 'test-results/screenshots', '--json', 'test-results/e2e-results.json'],
    ]
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    results = []
    fingerprint = source_fingerprint()
    for command in commands:
        print('RUN ' + ' '.join([Path(command[0]).name, *command[1:]]), flush=True)
        started = time.monotonic()
        try:
            run = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
            code, stdout, stderr = run.returncode, run.stdout, run.stderr
        except OSError as exc:
            code, stdout, stderr = 127, '', str(exc)
        print(stdout, end='', flush=True)
        if stderr:
            print(stderr, file=sys.stderr, end='', flush=True)
        results.append({'command': [Path(command[0]).name, *command[1:]], 'exit_code': code,
                        'seconds': round(time.monotonic() - started, 3), 'stdout': stdout, 'stderr': stderr})
    stable = source_fingerprint() == fingerprint
    report = {'checked_at': datetime.now(timezone(timedelta(hours=3))).isoformat(timespec='seconds'),
              'source_sha256': fingerprint, 'source_unchanged_during_run': stable,
              'passed': stable and all(r['exit_code'] == 0 for r in results), 'checks': results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    if not stable:
        print('FAIL: source changed during the check; run again')
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
