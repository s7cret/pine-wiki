#!/usr/bin/env python3
"""Run release checks and generate QA_REPORT.md from their actual outputs."""
import json
from pathlib import Path
import subprocess
import sys
from metrics import collect

ROOT = Path(__file__).resolve().parents[1]


def main():
    evidence = ROOT / 'test-results/check-results.json'
    run = subprocess.run([sys.executable, str(ROOT / 'tools/check.py'), '--output', str(evidence)], cwd=ROOT)
    data = json.loads(evidence.read_text(encoding='utf-8'))
    metrics = collect()
    lines = ['# QA — Pine Wiki', '', f"Дата прогона (Москва): `{data['checked_at']}`.",
             f"Ревизия: `{metrics['revision']}`.", f"Карточек: {metrics['cards_total']}; семейств: {metrics['families']}; ключей UI: {metrics['ui_keys_defined']}.",
             '', 'Результат: **' + ('PASS' if data['passed'] else 'FAIL') + '**.',
             f"SHA-256 проверенного кода, данных и тестов: `{data['source_sha256']}`.",
             '', '| Команда | Код завершения | Секунды |', '|---|---:|---:|']
    for check in data['checks']:
        lines.append(f"| `{' '.join(check['command'])}` | {check['exit_code']} | {check['seconds']} |")
    lines += ['', '## Фактический вывод проверок', '']
    for check in data['checks']:
        lines += [f"### `{' '.join(check['command'])}`", '', '```text', (check['stdout'] + check['stderr']).strip(), '```', '']
    lines += ['## Границы проверки', '',
              'Проверены сохранённые каталоги и поведение справочника. Pine-код не компилировался и не исполнялся; выбранные темы аудита 20.10.2026 сверены с первичными страницами TradingView, без сплошной проверки корпуса. Указанные источники и подсказки не подтверждают поведение Pine Editor.', '',
              'Повторить: `python tools/qa_report.py`. Отчёт создаётся даже при ошибке; успешность берётся из кодов завершения, а не из заранее написанного текста.', '']
    (ROOT / 'QA_REPORT.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    (ROOT / 'docs/qa-results.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    return run.returncode


if __name__ == '__main__':
    sys.exit(main())
