# QA — Pine Wiki

Дата прогона (Москва): `2026-10-20T03:41:36+03:00`.
Ревизия: `2026-10-20.semantic-mvp.1`.
Карточек: 4631; семейств: 1292; ключей UI: 243.

Результат: **PASS**.
SHA-256 проверенного кода, данных и тестов: `443a6cd39a0d7c0a0872a180a39edf5c2d33257ab20671b36e18838cbbeed508`.

| Команда | Код завершения | Секунды |
|---|---:|---:|
| `python.exe tools/build_manifest.py --check` | 0 | 0.062 |
| `python.exe tools/verify_catalog.py` | 0 | 2.875 |
| `python.exe tools/verify_spec.py` | 0 | 0.875 |
| `python.exe tools/project_spec.py --check` | 0 | 1.079 |
| `python.exe tools/test_spec.py` | 0 | 2.718 |
| `node.EXE tools/test_example_status.js` | 0 | 0.047 |
| `python.exe tools/test_release_consumer.py` | 0 | 2.094 |
| `python.exe tools/test_verifier.py --json test-results/verifier-guards.json` | 0 | 76.984 |
| `python.exe tools/test_verifier.py --reverse --json test-results/verifier-guards-reverse.json` | 0 | 76.485 |
| `python.exe tools/test_audit_v5_examples.py` | 0 | 1.672 |
| `python.exe tools/test_semantic_contracts.py` | 0 | 0.328 |
| `node.EXE tools/search_regression.js` | 0 | 0.843 |
| `python.exe tools/e2e_smoke.py --screenshots test-results/screenshots --json test-results/e2e-results.json` | 0 | 31.954 |

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
catalog invariants: {'type_hints': 92, 'search_rank': 46, 'description_hints': 73, 'descriptions_missing': 23, 'templates': 752, 'pointers': 90, 'neighbor_descriptions': 1, 'legacy_params': 9, 'requiredness_conflicts': 27}
ui strings: 243 keys used, 243 defined (ru+en); 45 dynamic keys checked
js syntax: node --check passed for all files
release documentation: generated files are current
release counts: {'v1': 315, 'v2': 365, 'v3': 361, 'v4': 626, 'v5': 1444, 'v6': 1520}
ALL CHECKS PASSED
```

### `python.exe tools/verify_spec.py`

```text
Specification: 56 assertions; 24 definitions; 18 bound receipts; 6 complete programs
```

### `python.exe tools/project_spec.py --check`

```text
Semantic card/history/search projections: current
```

### `python.exe tools/test_spec.py`

```text
test_A01_unordered_records_and_stable_identity (__main__.SpecGates.test_A01_unordered_records_and_stable_identity) ... ok
test_A02_translation_does_not_invalidate_semantic_cache (__main__.SpecGates.test_A02_translation_does_not_invalidate_semantic_cache) ... ok
test_A03_one_reviewed_fact_changes_all_views_and_runtime (__main__.SpecGates.test_A03_one_reviewed_fact_changes_all_views_and_runtime) ... ok
test_A04_positional_order_affects_hash_but_not_parameter_identity (__main__.SpecGates.test_A04_positional_order_affects_hash_but_not_parameter_identity) ... ok
test_A05_needed_unknown_is_spec_unresolved (__main__.SpecGates.test_A05_needed_unknown_is_spec_unresolved) ... ok
test_A06_explicit_argument_bypasses_unused_unknown (__main__.SpecGates.test_A06_explicit_argument_bypasses_unused_unknown) ... ok
test_A07_locked_bundle_and_consumer_are_offline (__main__.SpecGates.test_A07_locked_bundle_and_consumer_are_offline) ... ok
test_A08_missing_implementation_is_distinct (__main__.SpecGates.test_A08_missing_implementation_is_distinct) ... ok
test_A09_context_absence_is_not_language_invalid (__main__.SpecGates.test_A09_context_absence_is_not_language_invalid) ... ok
test_A10_external_pin_schema_and_artifact_integrity (__main__.SpecGates.test_A10_external_pin_schema_and_artifact_integrity) ... ok
test_A11_export_is_byte_deterministic (__main__.SpecGates.test_A11_export_is_byte_deterministic) ... ok
test_A12_successful_run_is_bound_to_definition_code_context (__main__.SpecGates.test_A12_successful_run_is_bound_to_definition_code_context) ... ok
test_A13_hour_binding_rejects_name_ambiguity (__main__.SpecGates.test_A13_hour_binding_rejects_name_ambiguity) ... ok
test_A14_six_complete_programs_match_independent_series (__main__.SpecGates.test_A14_six_complete_programs_match_independent_series) ... ok
test_A15_duplicate_examples_and_placeholders_do_not_raise_rule_coverage (__main__.SpecGates.test_A15_duplicate_examples_and_placeholders_do_not_raise_rule_coverage) ... ok
test_A16_stateful_context_sequences_events_and_rollback (__main__.SpecGates.test_A16_stateful_context_sequences_events_and_rollback) ... ok
test_A17_source_grammar_scope_precedence_and_square_wrap (__main__.SpecGates.test_A17_source_grammar_scope_precedence_and_square_wrap) ... ok
test_R01_semantic_spelling_not_arbitrary_substring (__main__.SpecGates.test_R01_semantic_spelling_not_arbitrary_substring) ... ok
test_R03_content_origin_is_not_translation_method (__main__.SpecGates.test_R03_content_origin_is_not_translation_method) ... ok
test_footprint_access_and_counter_are_separate (__main__.SpecGates.test_footprint_access_and_counter_are_separate) ... ok
test_probe_coverage_rejects_stale_definition_or_context (__main__.SpecGates.test_probe_coverage_rejects_stale_definition_or_context) ... ok
test_review_queue_never_activates_changed_sources (__main__.SpecGates.test_review_queue_never_activates_changed_sources) ... ok
test_rule_runtime_obligations_and_request_counter (__main__.SpecGates.test_rule_runtime_obligations_and_request_counter) ... ok
test_schema_and_typed_binding_edge_cases (__main__.SpecGates.test_schema_and_typed_binding_edge_cases) ... ok
test_unreviewed_value_changes_and_unresolved_competitors_fail_gate (__main__.SpecGates.test_unreviewed_value_changes_and_unresolved_competitors_fail_gate) ... ok

----------------------------------------------------------------------
Ran 25 tests in 2.541s

OK
```

### `node.EXE tools/test_example_status.js`

```text
40 example-status cases passed (negative/success/error/blocked/unknown/stale, RU/EN)
```

### `python.exe tools/test_release_consumer.py`

```text
7 release-consumer checks passed: 6 full CLI programs offline; byte-identical re-export; pinned implementation c12954ba3494f46048cfbf241eec9a9c343c7ed9
```

### `python.exe tools/test_verifier.py --json test-results/verifier-guards.json`

```text
PASS clean isolated fixture
PASS hour() occurrence attached to variable rejected
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
PASS default changed despite unchanged evidence rejected
PASS source-spelling bypass rejected with synchronized history
PASS unrelated result donor rejected
PASS family absent from declared shard rejected
PASS truncated thousands literal rejected
PASS execution claim without run evidence rejected
PASS history cleanup preserves live data and is byte-idempotent
PASS literal hex identifiers do not masquerade as text references
PASS isolated version directive rejected after hash rebuild
PASS foreign description donor rejected despite valid text/source
PASS missing dynamically assembled role key rejected
PASS unused UI key rejected
```

### `python.exe tools/test_verifier.py --reverse --json test-results/verifier-guards-reverse.json`

```text
PASS clean isolated fixture
PASS execution claim without run evidence rejected
PASS truncated thousands literal rejected
PASS family absent from declared shard rejected
PASS unrelated result donor rejected
PASS source-spelling bypass rejected with synchronized history
PASS default changed despite unchanged evidence rejected
PASS wrong history return_types aggregate rejected
PASS wrong history requiredness aggregate rejected
PASS wrong history types aggregate rejected
PASS wrong history parameters aggregate rejected
PASS wrong distinct structure count rejected
PASS wrong category record count rejected
PASS wrong public record count rejected
PASS empty history text without basis rejected
PASS missing history related note rejected
PASS missing history default-contract text rejected
PASS missing history supplement text rejected
PASS history-2 orphan text rejected after hash rebuild
PASS catalog-v5 orphan text rejected after hash rebuild
PASS hour() occurrence attached to variable rejected
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

### `python.exe tools/test_semantic_contracts.py`

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.247s

OK
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
182/182 exact symbolic search cases passed across v1–v6
score: median 0.46 ms for 1520 cards (informational; hardware-dependent)
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
PASS audit search/ru/+: results
PASS audit search/ru/+: direct route retains query
PASS audit search/ru/[]: results
PASS audit search/ru/[]: direct route retains query
PASS audit search/ru/:=: results
PASS audit search/ru/:=: direct route retains query
PASS audit search/ru/==: results
PASS audit search/ru/==: direct route retains query
PASS audit search/ru/!=: results
PASS audit search/ru/!=: direct route retains query
PASS audit search/ru/=>: results
PASS audit search/ru/=>: direct route retains query
PASS audit search/ru/?:: results
PASS audit search/ru/?:: direct route retains query
PASS audit search/ru///: results
PASS audit search/ru///: direct route retains query
PASS audit timestamp/ru: normalized RFC and ISO anchors
PASS audit limit/ru/request.security: shared caveat at card
PASS audit limit/ru/request.security_lower_tf: shared caveat at card
PASS audit cross/ru: absence separated from manual supplement
PASS audit search/en/+: results
PASS audit search/en/+: direct route retains query
PASS audit search/en/[]: results
PASS audit search/en/[]: direct route retains query
PASS audit search/en/:=: results
PASS audit search/en/:=: direct route retains query
PASS audit search/en/==: results
PASS audit search/en/==: direct route retains query
PASS audit search/en/!=: results
PASS audit search/en/!=: direct route retains query
PASS audit search/en/=>: results
PASS audit search/en/=>: direct route retains query
PASS audit search/en/?:: results
PASS audit search/en/?:: direct route retains query
PASS audit search/en///: results
PASS audit search/en///: direct route retains query
PASS audit timestamp/en: normalized RFC and ISO anchors
PASS audit limit/en/request.security: shared caveat at card
PASS audit limit/en/request.security_lower_tf: shared caveat at card
PASS audit cross/en: absence separated from manual supplement
PASS audit array.from: one variadic group
PASS audit round: two call forms, no three-argument template
PASS spec/ru: card links formal contract
PASS spec/ru: actual renderer not_compiled/not_executed
PASS spec/ru: actual renderer compiled/executed
PASS spec/ru: actual renderer error/not_executed
PASS spec/ru: actual renderer compiled/blocked
PASS spec/ru: actual renderer unknown/unknown
PASS spec/ru: conflicting v5 default stays unresolved
PASS spec/en: card links formal contract
PASS spec/en: actual renderer not_compiled/not_executed
PASS spec/en: actual renderer compiled/executed
PASS spec/en: actual renderer error/not_executed
PASS spec/en: actual renderer compiled/blocked
PASS spec/en: actual renderer unknown/unknown
PASS spec/en: conflicting v5 default stays unresolved
PASS spec http/ru: facts, runs and review queue
PASS spec http/ru/390: no horizontal overflow
PASS spec http/ru/1400: no horizontal overflow
PASS spec http/en: facts, runs and review queue
PASS spec http/en/390: no horizontal overflow
PASS spec http/en/1400: no horizontal overflow
PASS spec file/ru: facts, runs and review queue
PASS spec file/ru/390: no horizontal overflow
PASS spec file/ru/1400: no horizontal overflow
PASS spec file/en: facts, runs and review queue
PASS spec file/en/390: no horizontal overflow
PASS spec file/en/1400: no horizontal overflow
PASS JSON export
PASS page parameter
PASS manifest hash on data requests
PASS console/network clean

311/311 browser checks passed
```

## Границы проверки

Проверены каталоги, интерфейс, формальные контракты, bundle и офлайн CLI. Отдельные фактические прогоны Pine Editor сохранены в spec/probe-runs.json с кодом, definition/context hashes и условиями наблюдения. Они не означают сплошной проверки корпуса: footprint заблокирован тарифом, realtime и полный язык вне MVP. PW-16: загрязнение fixture сейчас не воспроизведено, первопричина неизвестна.

Повторить: `python tools/qa_report.py`. Отчёт создаётся даже при ошибке; успешность берётся из кодов завершения, а не из заранее написанного текста.
