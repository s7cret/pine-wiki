#!/usr/bin/env python3
"""Generate README and final metrics from current catalogs; --check is read-only."""
import argparse
import json
from pathlib import Path
from metrics import collect

ROOT = Path(__file__).resolve().parents[1]


def readme(m):
    v = m['versions']
    total = lambda key: sum(row[key] for row in v.values())
    rows = '\n'.join(f"| v{key} | {r['cards']} | {r['example_items']} | {r['parameters']} | {r['empty_parameter_descriptions']} | {r['parameter_description_hints']} | {r['parameters_without_description_or_hint']} |" for key, r in v.items())
    required = '\n'.join(f"| v{key} | {r['unknown_requiredness']} / {r['parameters']} ({100*r['unknown_requiredness']/r['parameters']:.1f} %) | {r['conflicting_requiredness']} |" for key, r in v.items() if r['parameters'])
    return f'''# Pine Script Reference Wiki · v1–v6

Статическая двуязычная (RU/EN) справка по Pine Script. Ревизия: `{m['revision']}`. Всего {m['cards_total']} карточка, {m['families']} семейства истории, {m['ui_keys_defined']} используемых ключей интерфейса RU/EN. Приложение не требует сборщика, внешних библиотек или серверной части.

## Запуск

Откройте `index.html` напрямую (`file://`) либо запустите из папки проекта:

```sh
python -m http.server 8000
```

Адрес: [localhost:8000](http://localhost:8000/). Прямые ссылки поддерживают `?v=6&lang=ru&id=<id>`, `q`, `category`, `purpose`, `namespace`, `level`, `page`, `gaps`, `examples`. Каталоги и история загружаются по требованию с хешем в URL. JSON создаётся только по нажатию «Скачать каталог»; временный Blob освобождается.

`http.server` удобен для локальной проверки, но не сжимает ответы. Для раздачи со сжатием приложен `deploy/Caddyfile`: запуск из корня проекта `caddy run --config deploy/Caddyfile`. Конфигурация использует [encode gzip/zstd](https://caddyserver.com/docs/caddyfile/directives/encode) и перепроверку кэша; публикация сайта автоматически не выполняется.

## Данные текущей сборки

| Версия | Карточки | Элементы примеров | Параметры | Без первичного описания | С подсказкой | Без описания и подсказки |
|---|---:|---:|---:|---:|---:|---:|
{rows}

Подсказка из другой версии не считается первичным описанием. Метрики генерирует `tools/metrics.py`; исходная линия сохранена в `docs/metrics-baseline.json`, итог — в `docs/metrics-final.json`.

## Исправления

- 574 карточки v5: построчные фрагменты объединены в цельные примеры. Итог v5 — {v['5']['example_items']} элементов. Все 44 отличающихся от v6 случая разобраны в `docs/v5-example-review.md`; исходный код v5 не заменялся кодом v6.
- Пустые редакторские тексты удалены. У {total('parameter_description_hints')} параметров есть отдельная подсказка с версией, донорской карточкой и источником; {total('parameters_without_description_or_hint')} остаются без описания и подсказки. Разбор — `docs/parameter-description-review.md`.
- Русские базовые термины добавлены в синонимы. Точное совпадение синонима у функции или конструкции получает приоритет; короткие совпадения по телу описания стоят после имён. Эталон поиска — `tools/search_gold.json`.
- Переменные и константы показывают «Тип значения» без заглушки результата. Типы, ключевые слова, синтаксис и аннотации скрывают этот блок. Функции и методы сохраняют описание и происхождение результата.
- Исправлены сохранение фокуса, live-регион, подпись таблицы и scope заголовков; читаемый текст не мельче 12 px. CSS объединён; экспорту и загрузке добавлены ленивое создание Blob и версия URL соответственно.
- Историческое исправление результатов уточнено: `floor` v4 использует описание соседней версии ({total('neighbor_result_descriptions')} донорское описание во всей сборке). `floor` и `cross` v3 имеют редакторское описание по сигнатуре, прежние тексты хранятся в `result.description_previous`.
- Сохранены {total('type_hints')} подсказки типов, {total('legacy_parameters')} пометок устаревших параметров, {total('search_rank_entries')} приоритетов скользящих средних, {total('pointers')} указатель на документацию и {total('templates')} схематических шаблонов. Шаблоны и указатели не считаются реальными примерами.

## Проверка и воспроизведение

Нужны Python 3.10+ и Node.js. Браузерные проверки используют Playwright:

```sh
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
npm run check
python tools/qa_report.py
```

`npm run check` запускает `build_manifest.py --check`, `verify_catalog.py`, отрицательные проверки валидатора (`test_verifier.py`), Node-регрессию поиска и `e2e_smoke.py`. Альтернатива без npm: `python tools/check.py`. CI GitHub Actions выполняет ту же команду на push/PR. При необходимости установленный браузер задаётся переменной `E2E_BROWSER_EXECUTABLE`.

`QA_REPORT.md` и `docs/qa-results.json` генерируются из фактического прогона с кодами завершения и отпечатком проверенных файлов; ошибки не заменяются сообщением об успехе. Скриншоты и подробности прогона находятся в `test-results/` (не включаются в git).

Правки каталогов воспроизводятся стандартной библиотекой Python:

```sh
python tools/migrations/01_merge_v5_examples.py
python tools/migrations/02_parameter_description_hints.py
python tools/migrations/03_search_aliases.py
python tools/migrations/04_register_requiredness_conflicts.py
python tools/build_manifest.py --revision {m['revision']}
python tools/report_sources.py
python tools/release_docs.py
python tools/qa_report.py
```

Миграции идемпотентны. `build_manifest.py` обновляет bytes/SHA-256 в прежнем формате; `created_utc` сохраняет дату исходного снимка. `--check` не переписывает манифест. `release_docs.py --check` проверяет актуальность этой документации и итоговых метрик.

## Известные ограничения

- У {total('empty_parameter_descriptions')} параметров нет первичного описания; из них {total('parameters_without_description_or_hint')} без безопасной подсказки. CSV: `docs/empty-parameter-descriptions.csv` и `docs/parameter-descriptions-without-hints.csv`. Неоднозначные `rsi`, вариадические группы `min/max/avg` и `array.from(..args)` не заполнялись предположениями.
- Пустые строки, потерянные при исходной нарезке примеров v5, не восстановлены: первичный снимок с ними не приложен. Сохранены порядок строк и отступы; Pine-код не компилировался и не исполнялся.
- Неизвестная обязательность и конфликты остаются фактами сохранённых источников:

| Версия | Неизвестная обязательность | Конфликты |
|---|---:|---:|
{required}

- Конфликты перечислены в `docs/requiredness-conflicts.csv` и зарегистрированы в `source_issues`. Отсутствие значения по умолчанию не доказывает обязательность; противоречивые свидетельства не подменяются выводом из сигнатуры.
- В v1/v2 исторические источники неполны; отсутствующие записи не достраивались. Один параметр `array.from(..args)` v4 остаётся без типа и подсказки типа.
- {v['6']['editorial_texts_without_provenance']} редакторских текстов v6 не имеют машинной записи происхождения. Это ограничение сохранённого снимка; новые миграции не заявляют, что провели их внешнюю проверку.
- Содержимое не сверялось заново с живыми страницами TradingView. Краткое описание функции вместо отсутствующего Returns — пояснение, не спецификация поведения.
- Устаревший `pine-result-less-functions.md` исключён из текущей поставки: он не используется интерфейсом и противоречил исправленным каталогам. Его исходная версия доступна в git-теге `baseline-2026-10-16`.

Уточнения и противоречия ТЗ обоснованы в `docs/TZ_DECISIONS.md`.

## Лицензия и источники

Собственный код распространяется по [MIT](LICENSE), как выбрал владелец. Документация, примеры, снимки и производные переводы сторонних авторов описаны отдельно в [NOTICE](NOTICE) и [THIRD_PARTY.md](THIRD_PARTY.md); их лицензия не заменяется MIT проекта. Перечень источников: `docs/source-inventory.csv`. Права на публичную раздачу сторонних материалов в этой задаче не устанавливались; сайт и репозиторий не публиковались.

Pine Wiki — неофициальный справочник, не связанный с TradingView. Поддержка описанных конструкций другими реализациями языка здесь не оценивается. В сохранённых пояснениях происхождения встречается OpenPine — название отдельного проекта реализации Pine Script; эти записи сообщают, что его совместимость здесь не проверялась.
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    metrics = collect()
    outputs = {ROOT / 'README_RU.md': readme(metrics),
               ROOT / 'docs/metrics-final.json': json.dumps(metrics, ensure_ascii=False, indent=2) + '\n'}
    stale = []
    for path, output in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != output:
                stale.append(path.name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(output, encoding='utf-8', newline='\n')
    if stale:
        raise SystemExit('Release documentation is stale: ' + ', '.join(stale))
    print('release documentation: ' + ('current' if args.check else 'generated'))


if __name__ == '__main__':
    main()
