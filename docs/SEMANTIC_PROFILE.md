# Pine v6: `pine6.core-mvp.1`

Этот выпуск содержит работающий офлайн CLI в `consumer/`, а также статическую вики. CLI — отдельный ограниченный потребитель спецификации; интеграция в библиотеки OpenPine этим выпуском не заявляется. Закреплённый SHA реализации и digest комплекта находятся в [consumer/lock.json](../consumer/lock.json).

## Запуск опубликованного комплекта

```sh
python -m pip install -r requirements-dev.txt
python -m consumer.cli --lock consumer/lock.json --source spec/programs/request.pine --context spec/fixtures/context.json
python -m consumer.cli --lock consumer/lock.json --source spec/programs/ema.pine --compile-only
python tools/test_release_consumer.py
```

После установки зависимостей сеть для чтения bundle, компиляции и исполнения не нужна. `--output result.json` сохраняет AST, разрешённые вызовы, lowered artifact и наблюдаемые последовательности. Вывод содержит semantic hash, хеш сборки реализации, SHA её исходников, закреплённый commit и хеш контекста. Код выхода 2 означает диагностированный отказ.

Шесть цельных программ: `abs`, `ema`, `round`, `tr`, `array`, `request`. Собственный синтетический набор OHLC и независимые арифметические ожидания находятся в `spec/fixtures/`. Это не выгрузка рыночных данных и не эталон, полученный из OpenPine. `indicator`, `plot`, приведения чисел и чтение массива имеют явные контракты и обработчики. Замыкание зависимостей перечислено в `spec/profile-programs.json`.

## Единственный реестр и проекции

`spec/registry.json` — источник машинных сигнатур, defaults, правил и review decisions. Метод получения факта (`extracted`, `derived`, `probed`, `manual`) независим от его статуса. У каждой активной записи есть scope, evidence и принятое решение с хешем выбранного значения. Изменить значение, оставив старый decision hash, нельзя. Конкурирующее свидетельство требует явного решения по issue.

`tools/project_spec.py` создаёт представления контрактов в карточках, истории и `spec-data.js`. Это генерация, а не второе место ручного редактирования defaults. Приёмочный A-03 меняет один проверенный default `gaps`, его решение и одновременно проверяет проекцию в карточке/истории, binding и изменение результирующей последовательности. Старый artifact отвергается.

Исходные описания в карточках сохраняют статус снимка: они не становятся исполняемым правилом только из-за наличия prose. В v5 у трёх `calc_bars_count` сохранены противоречивые свидетельства `100000` и `0`. Машинный default имеет `kind=unknown`, issue связан с тремя API; интерфейс не показывает его как активное значение. Если неизвестное значение необходимо — `SPEC_UNRESOLVED`; явный аргумент позволяет не использовать неизвестный default. Это проверяется A-05/A-06.

4631 существующий `entry_id`, 1292 семейства и 5955 привязок параметров сохранены. `spec/identities.json` связывает их со стабильными logical symbol/overload/parameter IDs. Переменная `ta.tr` и функция `ta.tr()` имеют разные symbol IDs; аналогично `hour` и `time`. Parameter ID не зависит от позиции. Переименование сохраняет ID через aliases; удаление требует tombstone, повторное использование ID запрещено политикой реестра. Позиция параметра остаётся семантически значимой.

## Путь исполнения и границы

`grammar.json` задаёт ограниченную нормативную грамматику профиля; это редакционный контракт, а не объявленная TradingView полная грамматика. Parser строит AST с source spans. Frontend один раз разрешает имена, перегрузки, qualifier constraints, positional/named/variadic arguments и defaults. Lowering получает эти bindings и не разбирает prose или текстовую сигнатуру повторно. Runtime принимает уже разрешённые операции.

Проверяются приоритеты операторов, области видимости, затенение, reassignment, история `[]` и переносы внутри `()`/`[]`. Статически известные нарушения отвергаются до запуска; остальные условия остаются runtime obligations. Правила имеют фазу parse/bind/compile/admission/runtime и идентификатор в диагностике.

EMA хранит состояние по месту вызова и контексту; seed, NA policy, формулы и skipped-call policy берутся из реестра. `request.security` вычисляет выражение на барах запрошенного контекста **до** выравнивания на график. Тест сравнивает восемь значений и события обновлений с независимыми ожидаемыми рядами: EMA внутри request отличается от EMA после выравнивания. Отдельно проверены v5 strict/v6 lazy boolean policies и helper фаз commit/rollback с обычным состоянием и `varip`. Это не поддержка всего v5 frontend или realtime engine.

Профиль исполнения — подтверждённая история, стандартные свечи, явно переданные контексты, `lookahead_off`, `currency.NONE`. Точность `math.round` ограничена редакционным профилем [-15, 15]. Произвольные outer captures в request, nested requests, currency conversion, ignored invalid symbols, realtime, стратегии, imports/exports, UDT/enums, пользовательские функции/методы и циклы требуют другого профиля. Аналогично переносы вне скобок и tab indentation не реализованы в этом parser. Отказ содержит `PROFILE_UNCOVERED`; он не объявляет допустимый Pine-код ошибкой языка. Лимиты unique requests 40/64 и доступность footprint — разные правила.

Диагностики разделены:

| Категория | Значение |
|---|---|
| `LANGUAGE_INVALID` | Нарушена установленная норма в покрытом срезе |
| `SPEC_UNRESOLVED` | Необходимого разрешённого факта нет |
| `IMPLEMENTATION_MISSING` | Контракт известен, обработчика в сборке нет |
| `CONTEXT_UNAVAILABLE` | Нет необходимых данных/контекста/доступа |
| `ARTIFACT_INCOMPATIBLE` | Не совпали schema/profile/hash/build; либо известная конструкция вне профиля с reason `PROFILE_UNCOVERED` |

## Комплект, hashes и совместимость

`tools/spec_bundle.py --output bundles/<new-release> --source-commit <sha> --write-lock consumer/lock.json` создаёт неизменяемый комплект. При отличающихся входах нужен новый каталог; прежний bundle не перезаписывается. Для выпуска сначала фиксируется код реализации и канонические входы, затем экспортируется bundle с этим SHA, после чего отдельным коммитом публикуются bundle и внешний lock.

Manifest фиксирует source commit, schema/catalog/profile, platform scope, semantic/documentation/evidence hashes и SHA-256 каждого файла. Reader проверяет внешний закреплённый digest manifest, точный набор файлов, их hashes, schema, review decisions и внутренние identities до исполнения. Подмена одновременно данных и внутренних hashes без изменения внешнего lock обнаруживается.

Канонизация сортирует ключи объектов и только явно неупорядоченные коллекции assertions/decisions/symbols/overloads/rules/profiles/sources. Порядок параметров, tuple members, argument evaluation и событий сохраняется. Перевод меняет documentation hash, source reviews и новые наблюдения — evidence hash, тип/default/активное решение — semantic hash. Повторный export с теми же входами побайтово идентичен; это проверяется и для опубликованного bundle.

В evidence view входят компактные run receipts, схемы probes, источники и notices. Скриншоты и append-only Pine instrumentation сохраняются рядом в `spec/run-artifacts/`, их hashes привязаны к receipts. Полные HTML, идентификаторы аккаунта и полный набор рыночных данных не экспортируются. Собственный код — MIT; сторонние материалы сохраняют отдельные условия из `NOTICE`/`THIRD_PARTY.md`.

## Пробы, coverage и обновления

`Example`, точная `Binding`, `ProbeDefinition` и фактический `ProbeRun` разделены. Старые общие expected/preconditions помечены `legacy_metadata_not_test_oracle`. Успех применим только к исходному code SHA, версии языка, definition hash и context hash. Измерительные расширения — отдельные definitions с parent code hash; их результаты не приписываются исходной программе.

Фактические Pine Editor records: [spec/probe-runs.json](../spec/probe-runs.json). Проверены 12 редакторских программ; footprint скомпилирован, выполнение заблокировано `RE10063` из-за тарифного доступа к секундным данным. У ISIN наблюдался fallback, у scope на последнем баре не проверена bullish-ветка. Эти ограничения сохранены в результатах. Отдельные диапазонные пробы lookahead v5/v6: 12901 бар, max error 0, NA mismatches 0. RSI v4: 12900 определённых баров, NA mismatches 0; отдельная проба подтверждает предикат `maximum <= 1e-10` самим Pine. Исторические семь импортированных программ этим не объявляются исполненными.

[Coverage JSON](../spec/coverage.json) разделяет структурный срез, разрешённые семантические факты, независимо проверенные правила, примеры/привязки и исполнение конкретного consumer. Один пример на нескольких карточках не умножает доказательства. Сейчас независимая Pine-проба подтверждает только явно перечисленное правило lookahead default; остальные правила не получают этот статус из-за прохождения наших unit tests.

`tools/spec_review.py --before old-registry.json` показывает semantic diff и консервативную карту влияния на срез. `--queue-source source.types --snapshot downloaded.html --output pending.json` помещает новую revision в **pending review**, не активируя её. Прежний snapshot/hash сохраняется. Для активации нужны scope, semantic diff, тест, новый decision с value hash, reviewer и rationale. Принятые решения текущего выпуска — редакционная проверка Codex, а не независимый человеческий review. Очередь, unresolved facts, decisions и runs доступны на [странице профиля](../spec/index.html).

Полный повтор: `python tools/qa_report.py`. A-01–A-17 находятся в `tools/test_spec.py`; отдельный `test_release_consumer.py` проверяет опубликованный комплект и CLI, а e2e — HTTP/file, RU/EN и реальный renderer статусов.
