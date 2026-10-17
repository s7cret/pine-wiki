# QA — Pine Wiki

Дата прогона (Москва): `2026-10-17T20:59:46+03:00`.
Ревизия: `2026-10-17.audit-fixes`.
Карточек: 4631; семейств: 1292; ключей UI: 222.

Результат: **PASS**.
SHA-256 проверенного кода, данных и тестов: `94b086fbf1e8dd0a64cd593d3ec29637ea5771eaf6d701011d9e2f2a5454369b`.

| Команда | Код завершения | Секунды |
|---|---:|---:|
| `python.exe tools/build_manifest.py --check` | 0 | 0.078 |
| `python.exe tools/verify_catalog.py` | 0 | 2.828 |
| `python.exe tools/test_verifier.py --json test-results/verifier-guards.json` | 0 | 48.203 |
| `python.exe tools/test_audit_v5_examples.py` | 0 | 1.5 |
| `node.EXE tools/search_regression.js` | 0 | 0.281 |
| `python.exe tools/e2e_smoke.py --screenshots test-results/screenshots --json test-results/e2e-results.json` | 0 | 24.516 |

## Фактический вывод проверок

### `python.exe tools/build_manifest.py --check`

```text
manifest: all 22 hashes and sizes are current
```

### `python.exe tools/verify_catalog.py`

```text
manifest: 22 files checked
history: 1292 families, all referenced, all links resolved
text pools: full catalog/history references, orphans, and empty texts checked
catalog invariants: {'type_hints': 92, 'search_rank': 46, 'description_hints': 73, 'descriptions_missing': 24, 'templates': 766, 'pointers': 91, 'neighbor_descriptions': 1, 'legacy_params': 8, 'requiredness_conflicts': 27}
ui strings: 222 keys used, 222 defined (ru+en); 45 dynamic keys checked
js syntax: node --check passed for all files
release documentation: generated files are current
release counts: {'v1': 315, 'v2': 365, 'v3': 361, 'v4': 626, 'v5': 1444, 'v6': 1520}
ALL CHECKS PASSED
```

### `python.exe tools/test_verifier.py --json test-results/verifier-guards.json`

```text
PASS clean isolated fixture
PASS catalog-v5 orphan text rejected after hash rebuild
PASS history-2 orphan text rejected after hash rebuild
PASS missing history supplement text rejected
PASS missing history default-contract text rejected
PASS missing history related note rejected
PASS empty history text without basis rejected
PASS wrong public record count rejected
PASS wrong category record count rejected
PASS wrong distinct structure count rejected
PASS wrong history parameters aggregate rejected
PASS wrong history types aggregate rejected
PASS wrong history requiredness aggregate rejected
PASS wrong history return_types aggregate rejected
PASS history cleanup preserves live data and is byte-idempotent
PASS literal hex identifiers do not masquerade as text references
PASS isolated version directive rejected after hash rebuild
PASS foreign description donor rejected despite valid text/source
PASS missing dynamically assembled role key rejected
PASS unused UI key rejected
```

### `python.exe tools/test_audit_v5_examples.py`

```text
PASS: absent output regenerates all 574 reviewed records byte for byte
PASS: corrupt output is detected read-only and can be regenerated
PASS: missing canonical catalog entry is rejected without overwriting output
```

### `node.EXE tools/search_regression.js`

```text
PASS sma                          rank=1       top=ta.sma, ta.bb, ta.correlation
PASS ta.sma                       rank=1       top=ta.sma, ta.correlation, ta.dev
PASS скользящая                   rank=1       top=ta.sma, ta.ema, ta.rma
PASS moving average               rank=1       top=ta.sma, ta.ema, ta.alma
PASS ema                          rank=1       top=ta.ema
PASS rsi                          rank=1       top=ta.rsi, ta.rma
PASS relative strength index      rank=1       top=ta.rsi
PASS индекс относительной силы    rank=1       top=ta.rsi
PASS macd                         rank=1       top=ta.macd
PASS bollinger                    rank=1       top=ta.bb, ta.bbw
PASS bollinger bands              rank=1       top=ta.bb, ta.bbw
PASS полосы боллинджера           rank=1       top=ta.bb, ta.bbw
PASS bb                           rank=1       top=ta.bb, Отбрасывание результата через _
PASS highest                      rank=1       top=ta.highest, ta.highestbars, footprint.rows
PASS стохастик                    rank=1       top=ta.stoch
PASS crossover                    rank=1       top=ta.crossover
PASS ta.crossover                 rank=1       top=ta.crossover
PASS security                     rank=1       top=request.security, request.security_lower_tf, syminfo.isin
PASS график                       rank=1       top=plot, plot, plotarrow
PASS отрисовка                    rank=1       top=plot, plotarrow, plotbar
PASS оповещение                   rank=1       top=alert, alertcondition, alert.freq_all
PASS входной параметр             rank=1       top=input, input, input
PASS цена закрытия                rank=1       top=close, time_close, settlement_as_close.inherit
PASS объем                        rank=1       top=volume, strategy.position_size, footprint.buy_volume
PASS условие                      rank=1       top=if, alertcondition, switch с условиями
PASS индикатор                    rank=1       top=indicator, ta.cog, ta.kc
PASS стратегия                    rank=1       top=strategy, strategy.equity, strategy.entry
PASS массив                       rank=1       top=array, array.abs, array.abs
PASS массивы                      rank=1       top=array, array.abs, array.abs
PASS массивов                     rank=1       top=array, Прежняя запись типа массива, for…in по массиву
PASS метка                        rank=1       top=label, label, label.all
PASS метки                        rank=1       top=label, label, label.new
PASS метку                        rank=1       top=label, label, label.new
PASS меток                        rank=1       top=label, label, !=
PASS линия                        rank=1       top=line, line, line.set_extend
PASS линии                        rank=1       top=line, line, line.get_x1
PASS линию                        rank=1       top=line, line, plot
PASS линий                        rank=1       top=line, line, !=
PASS среднеквадратичное           rank=1       top=ta.stdev
PASS библиотека                   rank=1       top=library, Импорт версии библиотеки, Экспорт из библиотеки
PASS матрица                      rank=1       top=matrix, matrix.avg, matrix.avg
PASS словарь                      rank=1       top=map, map.clear, map.clear
PASS карта                        rank=1       top=map, Шаблоны типов коллекций
PASS карты                        rank=1       top=map, map.clear, map.clear
PASS карту                        rank=1       top=map
PASS бокс                         rank=1       top=box, box, box.all
PASS бокса                        rank=1       top=box, box
PASS боксы                        rank=1       top=box, box
PASS боксов                       rank=1       top=box, box, box.all
PASS таблица                      rank=1       top=table, table, table.cell
PASS таблицы                      rank=1       top=table, table, table.cell
PASS line.set_xy1                 rank=1       top=line.set_xy1, line.set_xy1
PASS guard: line: no short-prefix or unrelated-word match
PASS guard: label: no short-prefix or unrelated-word match
PASS guard: map: no short-prefix or unrelated-word match
PASS guard: box: no short-prefix or unrelated-word match
PASS guard: array: no short-prefix or unrelated-word match
PASS guard: table: no short-prefix or unrelated-word match
PASS guard: body text is not given alias inflections
PASS guard: a word inside a phrase is not a whole alias
PASS guard: three-letter Russian aliases are not expanded
PASS guard: case and outer whitespace normalize before alias matching
PASS guard: explicit alias outranks a generated inflection
PASS guard: concept alias inflection outranks an incidental title match
PASS guard: exact API name outranks its Russian alias forms
PASS guard: short API names keep token boundaries
PASS guard: empty search still matches all entries
score: median 0.47 ms for 1520 cards (informational; hardware-dependent)
52/52 search regression cases passed
15/15 alias matching guards passed
```

### `python.exe tools/e2e_smoke.py --screenshots test-results/screenshots --json test-results/e2e-results.json`

```text
PASS HTTP v1/ru/390: count and layout
PASS HTTP v1/ru/390: semantics and live status
PASS HTTP v1/en/390: count and layout
PASS HTTP v1/en/390: semantics and live status
PASS HTTP v1/en/390: translated chrome
PASS HTTP v2/ru/390: count and layout
PASS HTTP v2/ru/390: semantics and live status
PASS HTTP v2/en/390: count and layout
PASS HTTP v2/en/390: semantics and live status
PASS HTTP v2/en/390: translated chrome
PASS HTTP v3/ru/390: count and layout
PASS HTTP v3/ru/390: semantics and live status
PASS HTTP v3/en/390: count and layout
PASS HTTP v3/en/390: semantics and live status
PASS HTTP v3/en/390: translated chrome
PASS HTTP v4/ru/390: count and layout
PASS HTTP v4/ru/390: semantics and live status
PASS HTTP v4/en/390: count and layout
PASS HTTP v4/en/390: semantics and live status
PASS HTTP v4/en/390: translated chrome
PASS HTTP v5/ru/390: count and layout
PASS HTTP v5/ru/390: semantics and live status
PASS HTTP v5/en/390: count and layout
PASS HTTP v5/en/390: semantics and live status
PASS HTTP v5/en/390: translated chrome
PASS HTTP v6/ru/390: count and layout
PASS HTTP v6/ru/390: semantics and live status
PASS HTTP v6/en/390: count and layout
PASS HTTP v6/en/390: semantics and live status
PASS HTTP v6/en/390: translated chrome
PASS HTTP v1/ru/800: count and layout
PASS HTTP v1/ru/800: semantics and live status
PASS HTTP v1/en/800: count and layout
PASS HTTP v1/en/800: semantics and live status
PASS HTTP v1/en/800: translated chrome
PASS HTTP v2/ru/800: count and layout
PASS HTTP v2/ru/800: semantics and live status
PASS HTTP v2/en/800: count and layout
PASS HTTP v2/en/800: semantics and live status
PASS HTTP v2/en/800: translated chrome
PASS HTTP v3/ru/800: count and layout
PASS HTTP v3/ru/800: semantics and live status
PASS HTTP v3/en/800: count and layout
PASS HTTP v3/en/800: semantics and live status
PASS HTTP v3/en/800: translated chrome
PASS HTTP v4/ru/800: count and layout
PASS HTTP v4/ru/800: semantics and live status
PASS HTTP v4/en/800: count and layout
PASS HTTP v4/en/800: semantics and live status
PASS HTTP v4/en/800: translated chrome
PASS HTTP v5/ru/800: count and layout
PASS HTTP v5/ru/800: semantics and live status
PASS HTTP v5/en/800: count and layout
PASS HTTP v5/en/800: semantics and live status
PASS HTTP v5/en/800: translated chrome
PASS HTTP v6/ru/800: count and layout
PASS HTTP v6/ru/800: semantics and live status
PASS HTTP v6/en/800: count and layout
PASS HTTP v6/en/800: semantics and live status
PASS HTTP v6/en/800: translated chrome
PASS HTTP v1/ru/1000: count and layout
PASS HTTP v1/ru/1000: semantics and live status
PASS HTTP v1/en/1000: count and layout
PASS HTTP v1/en/1000: semantics and live status
PASS HTTP v1/en/1000: translated chrome
PASS HTTP v2/ru/1000: count and layout
PASS HTTP v2/ru/1000: semantics and live status
PASS HTTP v2/en/1000: count and layout
PASS HTTP v2/en/1000: semantics and live status
PASS HTTP v2/en/1000: translated chrome
PASS HTTP v3/ru/1000: count and layout
PASS HTTP v3/ru/1000: semantics and live status
PASS HTTP v3/en/1000: count and layout
PASS HTTP v3/en/1000: semantics and live status
PASS HTTP v3/en/1000: translated chrome
PASS HTTP v4/ru/1000: count and layout
PASS HTTP v4/ru/1000: semantics and live status
PASS HTTP v4/en/1000: count and layout
PASS HTTP v4/en/1000: semantics and live status
PASS HTTP v4/en/1000: translated chrome
PASS HTTP v5/ru/1000: count and layout
PASS HTTP v5/ru/1000: semantics and live status
PASS HTTP v5/en/1000: count and layout
PASS HTTP v5/en/1000: semantics and live status
PASS HTTP v5/en/1000: translated chrome
PASS HTTP v6/ru/1000: count and layout
PASS HTTP v6/ru/1000: semantics and live status
PASS HTTP v6/en/1000: count and layout
PASS HTTP v6/en/1000: semantics and live status
PASS HTTP v6/en/1000: translated chrome
PASS HTTP v1/ru/1400: count and layout
PASS HTTP v1/ru/1400: semantics and live status
PASS HTTP v1/en/1400: count and layout
PASS HTTP v1/en/1400: semantics and live status
PASS HTTP v1/en/1400: translated chrome
PASS HTTP v2/ru/1400: count and layout
PASS HTTP v2/ru/1400: semantics and live status
PASS HTTP v2/en/1400: count and layout
PASS HTTP v2/en/1400: semantics and live status
PASS HTTP v2/en/1400: translated chrome
PASS HTTP v3/ru/1400: count and layout
PASS HTTP v3/ru/1400: semantics and live status
PASS HTTP v3/en/1400: count and layout
PASS HTTP v3/en/1400: semantics and live status
PASS HTTP v3/en/1400: translated chrome
PASS HTTP v4/ru/1400: count and layout
PASS HTTP v4/ru/1400: semantics and live status
PASS HTTP v4/en/1400: count and layout
PASS HTTP v4/en/1400: semantics and live status
PASS HTTP v4/en/1400: translated chrome
PASS HTTP v5/ru/1400: count and layout
PASS HTTP v5/ru/1400: semantics and live status
PASS HTTP v5/en/1400: count and layout
PASS HTTP v5/en/1400: semantics and live status
PASS HTTP v5/en/1400: translated chrome
PASS HTTP v6/ru/1400: count and layout
PASS HTTP v6/ru/1400: semantics and live status
PASS HTTP v6/en/1400: count and layout
PASS HTTP v6/en/1400: semantics and live status
PASS HTTP v6/en/1400: translated chrome
PASS file v1/ru: catalog loads
PASS file v1/en: catalog loads
PASS file v2/ru: catalog loads
PASS file v2/en: catalog loads
PASS file v3/ru: catalog loads
PASS file v3/en: catalog loads
PASS file v4/ru: catalog loads
PASS file v4/en: catalog loads
PASS file v5/ru: catalog loads
PASS file v5/en: catalog loads
PASS file v6/ru: catalog loads
PASS file v6/en: catalog loads
PASS search 'sma': first is ta.sma
PASS search 'скользящая': first is ta.sma
PASS search 'ta.sma': first is ta.sma
PASS search 'line.set_xy1': first is line.set_xy1
PASS search 'индикатор': first is indicator
PASS search 'стратегия': first is strategy
PASS search 'массив': first is array
PASS search 'бокс': finds box
PASS search 'таблица': finds table
PASS search 'отрисовка': finds plot
PASS search 'закрытые сделки': finds closedtrades
PASS search 'sma' has no 'small'
PASS pointer + template rendered
PASS floor v4: exact result donor link
PASS floor v3: signature note without donor
PASS cross v3: signature note without donor
PASS parameter type hints rendered
PASS na v4: description hint with exact donor
PASS legacy parameter note rendered
PASS ta.sar v5: one complete example
PASS color.red: Russian value-type label
PASS color.red: value-type label switches to English
PASS alert: void result retains signature provenance
PASS v1/variables: result semantics on all 54 cards
PASS v1/constants: result semantics on all 91 cards
PASS v1/types: result semantics on all 7 cards
PASS v1/syntax: result semantics on all 30 cards
PASS v1/annotations: result semantics on all 2 cards
PASS v1/operators: result semantics on all 20 cards
PASS v1/technical: result semantics on all 1 cards
PASS v2/variables: result semantics on all 56 cards
PASS v2/constants: result semantics on all 93 cards
PASS v2/types: result semantics on all 26 cards
PASS v2/keywords: result semantics on all 7 cards
PASS v2/syntax: result semantics on all 30 cards
PASS v2/annotations: result semantics on all 1 cards
PASS v2/operators: result semantics on all 21 cards
PASS v2/technical: result semantics on all 15 cards
PASS v3/variables: result semantics on all 64 cards
PASS v3/constants: result semantics on all 111 cards
PASS v3/types: result semantics on all 10 cards
PASS v3/keywords: result semantics on all 7 cards
PASS v3/syntax: result semantics on all 33 cards
PASS v3/annotations: result semantics on all 2 cards
PASS v3/operators: result semantics on all 21 cards
PASS v4/variables: result semantics on all 81 cards
PASS v4/constants: result semantics on all 185 cards
PASS v4/types: result semantics on all 20 cards
PASS v4/keywords: result semantics on all 9 cards
PASS v4/syntax: result semantics on all 34 cards
PASS v4/annotations: result semantics on all 2 cards
PASS v4/operators: result semantics on all 26 cards
PASS v5/variables: result semantics on all 153 cards
PASS v5/constants: result semantics on all 198 cards
PASS v5/types: result semantics on all 28 cards
PASS v5/keywords: result semantics on all 18 cards
PASS v5/syntax: result semantics on all 60 cards
PASS v5/annotations: result semantics on all 10 cards
PASS v5/operators: result semantics on all 28 cards
PASS v6/variables: result semantics on all 161 cards
PASS v6/constants: result semantics on all 239 cards
PASS v6/types: result semantics on all 31 cards
PASS v6/keywords: result semantics on all 19 cards
PASS v6/syntax: result semantics on all 62 cards
PASS v6/annotations: result semantics on all 10 cards
PASS v6/operators: result semantics on all 28 cards
PASS examples-only counts real examples
PASS keyboard version v1: focus retained
PASS keyboard version v2: focus retained
PASS keyboard version v3: focus retained
PASS keyboard version v4: focus retained
PASS keyboard version v5: focus retained
PASS keyboard version v6: focus retained
PASS keyboard category all: focus retained
PASS keyboard category syntax: focus retained
PASS keyboard category operators: focus retained
PASS keyboard category keywords: focus retained
PASS keyboard category types: focus retained
PASS keyboard category functions: focus retained
PASS keyboard category methods: focus retained
PASS keyboard category variables: focus retained
PASS keyboard category constants: focus retained
PASS keyboard category annotations: focus retained
PASS keyboard filter: focus retained
PASS keyboard search: focus retained
PASS keyboard pagination: heading focused
PASS keyboard history: dialog focus
PASS keyboard history: Tab stays in dialog
PASS keyboard history: close returns focus
PASS sources/ru: initial accessible state
PASS sources/ru: announces panel and hides entry banner
PASS sources/ru: restores the same entry
PASS sources/ru: category navigation resets panel state
PASS history/ru/#compare-from: absent versions labeled and selectable
PASS history/ru/#compare-to: absent versions labeled and selectable
PASS history/ru: absent version can be compared
PASS history/ru: existing version remains accessible
PASS sources/en: initial accessible state
PASS sources/en: announces panel and hides entry banner
PASS sources/en: restores the same entry
PASS sources/en: category navigation resets panel state
PASS history/en/#compare-from: absent versions labeled and selectable
PASS history/en/#compare-to: absent versions labeled and selectable
PASS history/en: absent version can be compared
PASS history/en: existing version remains accessible
PASS history: missing family offers recovery
PASS history: retry recovers a restored family
PASS JSON export
PASS page parameter
PASS manifest hash on data requests
PASS console/network clean

243/243 browser checks passed
```

## Границы проверки

Проверены сохранённые каталоги и поведение справочника. Pine-код не компилировался и не исполнялся; содержимое не сверялось заново с текущей документацией TradingView. Указанные источники и подсказки не подтверждают поведение Pine Editor.

Повторить: `python tools/qa_report.py`. Отчёт создаётся даже при ошибке; успешность берётся из кодов завершения, а не из заранее написанного текста.
