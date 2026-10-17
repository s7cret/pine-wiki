# Pine Script v3–v6: функции без прямого раздела Returns

Проверка по сохранённым снимкам каталога 16.10.2026: **1051 записей**, **371 уникальных имён** (перегрузки учитываются отдельно).

Отсутствие отдельного раздела Returns **не** означает отсутствие возвращаемого значения. Пометка «Описание» может быть общим описанием функции, а не контрактом результата. Подсказки типов из других версий и схемы вызова не подтверждены Pine Editor.

В версии v1/v2 раздел Returns в метаданных не оценивался тем же методом, поэтому в этот отчёт они не включены.

## Версия v6 — 343 записей

### `alert`
`primary:v6:functions:alert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_alert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `message` | series string / simple string / input string / const string | required | не установлено |
| `freq` | input string / const string | optional | alert.freq_once_per_bar |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `alertcondition`
`primary:v6:functions:alertcondition:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_alertcondition)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `message` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.abs`
`primary:v6:functions:array.abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.abs)

**Тип результата:** `array<float>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v6:functions:array.abs:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.abs)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v6:methods:array.abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.abs)

**Тип результата:** `array<float>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v6:methods:array.abs:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.abs)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search`
`primary:v6:functions:array.binary_search:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если значение элемента совпадает с искомым, функция возвращает его индекс. В противном случае она возвращает -1.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search`
`primary:v6:functions:array.binary_search:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если значение элемента совпадает с искомым, функция возвращает его индекс. В противном случае она возвращает -1.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search`
`primary:v6:methods:array.binary_search:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если значение элемента совпадает с искомым, функция возвращает его индекс. В противном случае она возвращает -1.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search`
`primary:v6:methods:array.binary_search:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если значение элемента совпадает с искомым, функция возвращает его индекс. В противном случае она возвращает -1.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search_leftmost`
`primary:v6:functions:array.binary_search_leftmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс первого элемента, значение котор…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_leftmost`
`primary:v6:functions:array.binary_search_leftmost:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс первого элемента, значение котор…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_leftmost`
`primary:v6:methods:array.binary_search_leftmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс первого элемента, значение котор…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_leftmost`
`primary:v6:methods:array.binary_search_leftmost:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс первого элемента, значение котор…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v6:functions:array.binary_search_rightmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс последнего элемента, значение ко…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v6:functions:array.binary_search_rightmost:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс последнего элемента, значение ко…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v6:methods:array.binary_search_rightmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс последнего элемента, значение ко…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v6:methods:array.binary_search_rightmost:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Выполняет [бинарный поиск](https://en.wikipedia.org/wiki/Binary_search) в отсортированном массиве, чтобы найти элемент, соответствующий искомому значению. Если функция находит искомое значение среди элементов массива или в полях объектов, на которые они ссылаются, она возвращает индекс последнего элемента, значение ко…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float / series string / simple string / input string / const string | required | не установлено |
| `sort_field` | const int / const string | optional | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.clear`
`primary:v6:functions:array.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.clear`
`primary:v6:methods:array.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.every`
`primary:v6:functions:array.every:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.every)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если все элементы массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.every`
`primary:v6:methods:array.every:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.every)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если все элементы массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.fill`
`primary:v6:functions:array.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |
| `index_from` | series int / simple int / input int / const int | unknown | 0 |
| `index_to` | series int / simple int / input int / const int | unknown | na |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.fill`
`primary:v6:methods:array.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |
| `index_from` | series int / simple int / input int / const int | unknown | 0 |
| `index_to` | series int / simple int / input int / const int | unknown | na |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.first`
`primary:v6:functions:array.first:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.first)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает первый элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.first`
`primary:v6:methods:array.first:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.first)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает первый элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.insert`
`primary:v6:functions:array.insert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.insert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | unknown | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.insert`
`primary:v6:methods:array.insert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.insert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | unknown | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.join`
`primary:v6:functions:array.join:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.join)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Функция создает и возвращает новую строку путем объединения всех элементов массива, разделённых заданной строкой-разделителем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.join`
`primary:v6:methods:array.join:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.join)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Функция создает и возвращает новую строку путем объединения всех элементов массива, разделённых заданной строкой-разделителем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.last`
`primary:v6:functions:array.last:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.last)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает последний элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.last`
`primary:v6:methods:array.last:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.last)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает последний элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.percentile_linear_interpolation`
`primary:v6:functions:array.percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v6:functions:array.percentile_linear_interpolation:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v6:methods:array.percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v6:methods:array.percentile_linear_interpolation:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v6:functions:array.percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_nearest_rank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v6:functions:array.percentile_nearest_rank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_nearest_rank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v6:methods:array.percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_nearest_rank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v6:methods:array.percentile_nearest_rank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentile_nearest_rank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v6:functions:array.percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentrank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v6:functions:array.percentrank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentrank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v6:methods:array.percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentrank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v6:methods:array.percentrank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.percentrank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.push`
`primary:v6:functions:array.push:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.push)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.push`
`primary:v6:methods:array.push:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.push)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.reverse`
`primary:v6:functions:array.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.reverse`
`primary:v6:methods:array.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.set`
`primary:v6:functions:array.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.set`
`primary:v6:methods:array.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.some`
`primary:v6:functions:array.some:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.some)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если хотя бы один из элементов массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.some`
`primary:v6:methods:array.some:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.some)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если хотя бы один из элементов массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.sort`
`primary:v6:functions:array.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort`
`primary:v6:functions:array.sort:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort`
`primary:v6:methods:array.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort`
`primary:v6:methods:array.sort:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v6:functions:array.sort_indices:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v6:functions:array.sort_indices:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v6:methods:array.sort_indices:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v6:methods:array.sort_indices:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.unshift`
`primary:v6:functions:array.unshift:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.unshift)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.unshift`
`primary:v6:methods:array.unshift:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_array.unshift)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `barcolor`
`primary:v6:functions:barcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_barcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series color / simple color / input color / const color | required | не установлено |
| `offset` | simple int / input int / const int | unknown | 0 |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bgcolor`
`primary:v6:functions:bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series color / simple color / input color / const color | required | не установлено |
| `offset` | simple int / input int / const int | unknown | 0 |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.copy`
`primary:v6:functions:box.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.copy)

**Тип результата:** `series box`.
**Описание в сохранённой карточке:** Клонирует объект box.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.copy`
`primary:v6:methods:box.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.copy)

**Тип результата:** `series box`.
**Описание в сохранённой карточке:** Клонирует объект box.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.delete`
`primary:v6:functions:box.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.delete`
`primary:v6:methods:box.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bgcolor`
`primary:v6:functions:box.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bgcolor`
`primary:v6:methods:box.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_color`
`primary:v6:functions:box.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_color`
`primary:v6:methods:box.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#cloning-boxes), ссылка составлена по заметкам.

---

### `box.set_border_style`
`primary:v6:functions:box.set_border_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_border_style`
`primary:v6:methods:box.set_border_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_border_width`
`primary:v6:functions:box.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_width`
`primary:v6:methods:box.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#cloning-boxes), ссылка составлена по заметкам.

---

### `box.set_bottom`
`primary:v6:functions:box.set_bottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_bottom`
`primary:v6:methods:box.set_bottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_bottom_right_point`
`primary:v6:functions:box.set_bottom_right_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bottom_right_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bottom_right_point`
`primary:v6:methods:box.set_bottom_right_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_bottom_right_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_extend`
`primary:v6:functions:box.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_extend`
`primary:v6:methods:box.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_left`
`primary:v6:functions:box.set_left:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_left)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_left`
`primary:v6:methods:box.set_left:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_left)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_lefttop`
`primary:v6:functions:box.set_lefttop:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_lefttop)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_lefttop`
`primary:v6:methods:box.set_lefttop:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_lefttop)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_right`
`primary:v6:functions:box.set_right:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_right)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#deleting-boxes), ссылка составлена по заметкам.

---

### `box.set_right`
`primary:v6:methods:box.set_right:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_right)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_rightbottom`
`primary:v6:functions:box.set_rightbottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_rightbottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_rightbottom`
`primary:v6:methods:box.set_rightbottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_rightbottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_text`
`primary:v6:functions:box.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#deleting-boxes), ссылка составлена по заметкам.

---

### `box.set_text`
`primary:v6:methods:box.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_text_color`
`primary:v6:functions:box.set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_color`
`primary:v6:methods:box.set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_font_family`
`primary:v6:functions:box.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.set_text_font_family`
`primary:v6:methods:box.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.set_text_formatting`
`primary:v6:functions:box.set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_formatting`
`primary:v6:methods:box.set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_halign`
`primary:v6:functions:box.set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_halign`
`primary:v6:methods:box.set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_size`
`primary:v6:functions:box.set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_size`
`primary:v6:methods:box.set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_valign`
`primary:v6:functions:box.set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_valign`
`primary:v6:methods:box.set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_wrap`
`primary:v6:functions:box.set_text_wrap:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_wrap)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_wrap` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_text_wrap`
`primary:v6:methods:box.set_text_wrap:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_text_wrap)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_wrap` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_top`
`primary:v6:functions:box.set_top:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_top)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top`
`primary:v6:methods:box.set_top:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_top)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top_left_point`
`primary:v6:functions:box.set_top_left_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_top_left_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top_left_point`
`primary:v6:methods:box.set_top_left_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_top_left_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_xloc`
`primary:v6:functions:box.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `box.set_xloc`
`primary:v6:methods:box.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_box.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-boxes), ссылка составлена по заметкам.

---

### `chart.point.copy`
`primary:v6:functions:chart.point.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.copy)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт копию объекта [chart.point](#type_chart.point) с заданным значением `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.copy`
`primary:v6:methods:chart.point.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.copy)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт копию объекта [chart.point](#type_chart.point) с заданным значением `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.from_index`
`primary:v6:functions:chart.point.from_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.from_index)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `index` в качестве его x-координаты и `price` — y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `index` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `chart.point.from_time`
`primary:v6:functions:chart.point.from_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.from_time)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `time` в качестве его x-координаты и `price` — y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `chart.point.new`
`primary:v6:functions:chart.point.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.new)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт новый объект [chart.point](#type_chart.point) с заданными `time`, `index` и `price`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series int / simple int / input int / const int | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.now`
`primary:v6:functions:chart.point.now:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_chart.point.now)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `price` в качестве y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | close |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v6:functions:fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `plot1` | plot | required | не установлено |
| `plot2` | plot | required | не установлено |
| `top_value` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `bottom_value` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `top_color` | series color / simple color / input color / const color | unknown | не установлено |
| `bottom_color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `fillgaps` | const bool | unknown | false |
| `editable` | input bool / const bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v6:functions:fill:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `hline1` | hline | required | не установлено |
| `hline2` | hline | required | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `fillgaps` | const bool | unknown | false |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v6:functions:fill:overload:2` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `plot1` | plot | required | не установлено |
| `plot2` | plot | required | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `fillgaps` | const bool | unknown | false |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `indicator`
`primary:v6:functions:indicator:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_indicator)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `shorttitle` | const string | optional | не установлено |
| `overlay` | const bool | optional | false |
| `format` | const string | optional | format.inherit |
| `precision` | const int | optional | не установлено |
| `scale` | const scale_type | optional | не установлено |
| `max_bars_back` | const int | optional | не установлено |
| `timeframe` | const string | optional | не установлено |
| `timeframe_gaps` | const bool | optional | true |
| `explicit_plot_zorder` | const bool | optional | false |
| `max_lines_count` | const int | optional | не установлено |
| `max_labels_count` | const int | optional | не установлено |
| `max_boxes_count` | const int | optional | не установлено |
| `calc_bars_count` | const int | optional | 0 |
| `max_polylines_count` | const int | optional | не установлено |
| `dynamic_requests` | const bool | optional | true |
| `behind_chart` | const bool | optional | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.delete`
`primary:v6:functions:label.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.delete`
`primary:v6:methods:label.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_color`
`primary:v6:functions:label.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_color`
`primary:v6:methods:label.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_point`
`primary:v6:functions:label.set_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_point`
`primary:v6:methods:label.set_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_size`
`primary:v6:functions:label.set_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `size` | series int / simple int / input int / const int / series string / simple string / input string / const string | required | size.normal |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_size`
`primary:v6:methods:label.set_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `size` | series int / simple int / input int / const int / series string / simple string / input string / const string | required | size.normal |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_style`
`primary:v6:functions:label.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_style`
`primary:v6:methods:label.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text`
`primary:v6:functions:label.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text`
`primary:v6:methods:label.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text_font_family`
`primary:v6:functions:label.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.set_text_font_family`
`primary:v6:methods:label.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.set_text_formatting`
`primary:v6:functions:label.set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_text_formatting`
`primary:v6:methods:label.set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textalign`
`primary:v6:functions:label.set_textalign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_textalign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textalign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textalign`
`primary:v6:methods:label.set_textalign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_textalign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textalign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textcolor`
`primary:v6:functions:label.set_textcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_textcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textcolor` | series color / simple color / input color / const color | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://tradingview.com/pine-script-docs/faq/strings-and-formatting/), ссылка составлена по заметкам.

---

### `label.set_textcolor`
`primary:v6:methods:label.set_textcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_textcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textcolor` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_tooltip`
`primary:v6:functions:label.set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_tooltip`
`primary:v6:methods:label.set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_x`
`primary:v6:functions:label.set_x:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_x)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_x`
`primary:v6:methods:label.set_x:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_x)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xloc`
`primary:v6:functions:label.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xloc`
`primary:v6:methods:label.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xy`
`primary:v6:functions:label.set_xy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_xy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xy`
`primary:v6:methods:label.set_xy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_xy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_y`
`primary:v6:functions:label.set_y:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_y)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://tradingview.com/pine-script-docs/faq/strings-and-formatting/), ссылка составлена по заметкам.

---

### `label.set_y`
`primary:v6:methods:label.set_y:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_y)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_yloc`
`primary:v6:functions:label.set_yloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_yloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `yloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_yloc`
`primary:v6:methods:label.set_yloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_label.set_yloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `yloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `library`
`primary:v6:functions:library:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_library)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `overlay` | const bool | unknown | false |
| `dynamic_requests` | const bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `line.delete`
`primary:v6:functions:line.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.delete`
`primary:v6:methods:line.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_color`
`primary:v6:functions:line.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_color`
`primary:v6:methods:line.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_extend`
`primary:v6:functions:line.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_extend`
`primary:v6:methods:line.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_first_point`
`primary:v6:functions:line.set_first_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_first_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_first_point`
`primary:v6:methods:line.set_first_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_first_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_second_point`
`primary:v6:functions:line.set_second_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_second_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_second_point`
`primary:v6:methods:line.set_second_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_second_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_style`
`primary:v6:functions:line.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_style`
`primary:v6:methods:line.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#cloning-lines), ссылка составлена по заметкам.

---

### `line.set_width`
`primary:v6:functions:line.set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_width`
`primary:v6:methods:line.set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_x1`
`primary:v6:functions:line.set_x1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_x1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_x1`
`primary:v6:methods:line.set_x1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_x1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#modifying-lines), ссылка составлена по заметкам.

---

### `line.set_x2`
`primary:v6:functions:line.set_x2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_x2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_x2`
`primary:v6:methods:line.set_x2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_x2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xloc`
`primary:v6:functions:line.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x1` | series int / simple int / input int / const int | required | не установлено |
| `x2` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xloc`
`primary:v6:methods:line.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x1` | series int / simple int / input int / const int | required | не установлено |
| `x2` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xy1`
`primary:v6:functions:line.set_xy1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xy1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#filling-the-space-between-lines), ссылка составлена по заметкам.

---

### `line.set_xy1`
`primary:v6:methods:line.set_xy1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xy1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xy2`
`primary:v6:functions:line.set_xy2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xy2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** в каталоге отсутствует; [пример в документации](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/#filling-the-space-between-lines), ссылка составлена по заметкам.

---

### `line.set_xy2`
`primary:v6:methods:line.set_xy2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_xy2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y1`
`primary:v6:functions:line.set_y1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_y1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y1`
`primary:v6:methods:line.set_y1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_y1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y2`
`primary:v6:functions:line.set_y2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_y2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y2`
`primary:v6:methods:line.set_y2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_line.set_y2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `linefill.delete`
`primary:v6:functions:linefill.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.delete`
`primary:v6:methods:linefill.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line1`
`primary:v6:functions:linefill.get_line1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.get_line1)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID первой линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line1`
`primary:v6:methods:linefill.get_line1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.get_line1)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID первой линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line2`
`primary:v6:functions:linefill.get_line2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.get_line2)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID второй линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line2`
`primary:v6:methods:linefill.get_line2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.get_line2)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID второй линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.set_color`
`primary:v6:functions:linefill.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.set_color`
`primary:v6:methods:linefill.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_linefill.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `map.clear`
`primary:v6:functions:map.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.clear`
`primary:v6:methods:map.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.contains`
`primary:v6:functions:map.contains:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.contains)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если в объекте map `id` был найден `key`, [false](#const_false), если нет.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.contains`
`primary:v6:methods:map.contains:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.contains)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если в объекте map `id` был найден `key`, [false](#const_false), если нет.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.get`
`primary:v6:functions:map.get:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.get)

**Тип результата:** `<value_type>`.
**Описание в сохранённой карточке:** Возвращает значение, ассоциированное с указанным `key` в `id` объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.get`
`primary:v6:methods:map.get:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.get)

**Тип результата:** `<value_type>`.
**Описание в сохранённой карточке:** Возвращает значение, ассоциированное с указанным `key` в `id` объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.keys`
`primary:v6:functions:map.keys:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.keys)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех ключей в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.keys`
`primary:v6:methods:map.keys:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.keys)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех ключей в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.put_all`
`primary:v6:functions:map.put_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.put_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `id2` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.put_all`
`primary:v6:methods:map.put_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.put_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `id2` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.size`
`primary:v6:functions:map.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.size)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает количество пар ключ-значение в объекте map типа `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.size`
`primary:v6:methods:map.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.size)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает количество пар ключ-значение в объекте map типа `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.values`
`primary:v6:functions:map.values:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.values)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех значений в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.values`
`primary:v6:methods:map.values:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_map.values)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех значений в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.add_col`
`primary:v6:functions:matrix.add_col:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | optional | не установлено |
| `array_id` | array<> | conflict | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_col`
`primary:v6:methods:matrix.add_col:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | optional | не установлено |
| `array_id` | array<> | conflict | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v6:functions:matrix.add_row:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | optional | не установлено |
| `array_id` | array<> | conflict | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v6:methods:matrix.add_row:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | optional | не установлено |
| `array_id` | array<> | conflict | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.elements_count`
`primary:v6:functions:matrix.elements_count:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.elements_count)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает общее количество всех элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.elements_count`
`primary:v6:methods:matrix.elements_count:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.elements_count)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает общее количество всех элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.fill`
`primary:v6:functions:matrix.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |
| `from_row` | series int / simple int / input int / const int | unknown | 0 |
| `to_row` | series int / simple int / input int / const int | unknown | не установлено |
| `from_column` | series int / simple int / input int / const int | unknown | 0 |
| `to_column` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.fill`
`primary:v6:methods:matrix.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |
| `from_row` | series int / simple int / input int / const int | unknown | 0 |
| `to_row` | series int / simple int / input int / const int | unknown | не установлено |
| `from_column` | series int / simple int / input int / const int | unknown | 0 |
| `to_column` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v6:functions:matrix.median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.median)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v6:functions:matrix.median:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.median)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v6:methods:matrix.median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.median)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v6:methods:matrix.median:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.median)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reshape`
`primary:v6:functions:matrix.reshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.reshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `rows` | series int / simple int / input int / const int | required | не установлено |
| `columns` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reshape`
`primary:v6:methods:matrix.reshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.reshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `rows` | series int / simple int / input int / const int | required | не установлено |
| `columns` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reverse`
`primary:v6:functions:matrix.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reverse`
`primary:v6:methods:matrix.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.set`
`primary:v6:functions:matrix.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.set`
`primary:v6:methods:matrix.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v6:functions:matrix.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> / matrix<string> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v6:functions:matrix.sort:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v6:methods:matrix.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> / matrix<string> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v6:methods:matrix.sort:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |
| `sort_field` | const int / const string | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_columns`
`primary:v6:functions:matrix.swap_columns:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.swap_columns)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column1` | series int / simple int / input int / const int | required | не установлено |
| `column2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_columns`
`primary:v6:methods:matrix.swap_columns:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.swap_columns)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column1` | series int / simple int / input int / const int | required | не установлено |
| `column2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_rows`
`primary:v6:functions:matrix.swap_rows:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.swap_rows)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row1` | series int / simple int / input int / const int | required | не установлено |
| `row2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_rows`
`primary:v6:methods:matrix.swap_rows:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_matrix.swap_rows)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row1` | series int / simple int / input int / const int | required | не установлено |
| `row2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotarrow`
`primary:v6:functions:plotarrow:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_plotarrow)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `colorup` | series color / simple color / input color / const color | unknown | не установлено |
| `colordown` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | simple int / input int / const int | unknown | 0 |
| `minheight` | input int / const int | unknown | 5 |
| `maxheight` | input int / const int | unknown | 100 |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotbar`
`primary:v6:functions:plotbar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_plotbar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `high` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `low` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `close` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotcandle`
`primary:v6:functions:plotcandle:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_plotcandle)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `high` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `low` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `close` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `wickcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `show_last` | input int / const int | optional | не установлено |
| `bordercolor` | series color / simple color / input color / const color | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotchar`
`primary:v6:functions:plotchar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_plotchar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float / series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `char` | input string / const string | unknown | не установлено |
| `location` | input string / const string | unknown | location.abovebar |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | simple int / input int / const int | unknown | 0 |
| `text` | const string | unknown | не установлено |
| `textcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | input int / const int | optional | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotshape`
`primary:v6:functions:plotshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_plotshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float / series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `style` | input string / const string | unknown | shape.xcross |
| `location` | input string / const string | unknown | location.abovebar |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | simple int / input int / const int | unknown | 0 |
| `text` | const string | unknown | не установлено |
| `textcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | input bool / const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | input int / const int | optional | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `polyline.delete`
`primary:v6:functions:polyline.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_polyline.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series polyline | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `polyline.delete`
`primary:v6:methods:polyline.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_polyline.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series polyline | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `request.currency_rate`
`primary:v6:functions:request.currency_rate:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_request.currency_rate)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Предоставляет курс, по которому можно конвертировать значение, выраженное в валюте `from`, в другое значение в валюте `to`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `from` | series string / simple string / input string / const string | required | не установлено |
| `to` | series string / simple string / input string / const string | required | не установлено |
| `ignore_invalid_currency` | series bool / simple bool / input bool / const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `runtime.error`
`primary:v6:functions:runtime.error:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_runtime.error)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `message` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `str.repeat`
`primary:v6:functions:str.repeat:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.repeat)

**Тип результата:** `const string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | const string | required | не установлено |
| `repeat` | const int | required | не установлено |
| `separator` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v6:functions:str.repeat:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.repeat)

**Тип результата:** `input string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | input string / const string | required | не установлено |
| `repeat` | input int / const int | required | не установлено |
| `separator` | input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v6:functions:str.repeat:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.repeat)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | simple string / input string / const string | required | не установлено |
| `repeat` | simple int / input int / const int | required | не установлено |
| `separator` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v6:functions:str.repeat:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.repeat)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series string / simple string / input string / const string | required | не установлено |
| `repeat` | series int / simple int / input int / const int | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v6:functions:str.trim:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.trim)

**Тип результата:** `const string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v6:functions:str.trim:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.trim)

**Тип результата:** `input string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v6:functions:str.trim:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.trim)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v6:functions:str.trim:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_str.trim)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy`
`primary:v6:functions:strategy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `format` | const string | unknown | format.inherit |
| `precision` | const int | unknown | не установлено |
| `scale` | const scale_type | optional | не установлено |
| `pyramiding` | const int | unknown | 0 |
| `calc_on_order_fills` | const bool | optional | false |
| `calc_on_every_tick` | const bool | optional | false |
| `max_bars_back` | const int | unknown | 0 |
| `backtest_fill_limits_assumption` | const int | unknown | 0 |
| `default_qty_type` | const string | unknown | strategy.percent_of_equity |
| `default_qty_value` | const int / const float | unknown | 100 |
| `initial_capital` | const int / const float | unknown | 100000 |
| `currency` | const string | unknown | syminfo.currency |
| `slippage` | const int | unknown | 0 |
| `commission_type` | const string | unknown | strategy.commission.percent |
| `commission_value` | const int / const float | unknown | 0 |
| `process_orders_on_close` | const bool | unknown | false |
| `close_entries_rule` | const string | unknown | "FIFO" |
| `margin_long` | const int / const float | unknown | 100 |
| `margin_short` | const int / const float | unknown | 100 |
| `explicit_plot_zorder` | const bool | unknown | false |
| `max_lines_count` | const int | unknown | 50 |
| `max_labels_count` | const int | unknown | 50 |
| `max_boxes_count` | const int | unknown | 50 |
| `calc_bars_count` | const int | unknown | 0 |
| `risk_free_rate` | const int / const float | unknown | 2 |
| `use_bar_magnifier` | const bool | optional | false |
| `fill_orders_on_standard_ohlc` | const bool | unknown | false |
| `max_polylines_count` | const int | unknown | 50 |
| `dynamic_requests` | const bool | unknown | true |
| `behind_chart` | const bool | optional | true |
| `calc_on_every_history_tick` | const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel`
`primary:v6:functions:strategy.cancel:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.cancel)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel_all`
`primary:v6:functions:strategy.cancel_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.cancel_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| — | Нет отдельных параметров | — | — |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close`
`primary:v6:functions:strategy.close:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.close)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `qty_percent` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | 100 |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `immediately` | series bool / simple bool / input bool / const bool | optional | false |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close_all`
`primary:v6:functions:strategy.close_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.close_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `immediately` | series bool / simple bool / input bool / const bool | optional | false |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.commission`
`primary:v6:functions:strategy.closedtrades.commission:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.commission)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает сумму комиссий за вход и выход, уплаченных по закрытой сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_bar_index`
`primary:v6:functions:strategy.closedtrades.entry_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.entry_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index входа закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_comment`
`primary:v6:functions:strategy.closedtrades.entry_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.entry_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария входа закрытой сделки или [na](#var_na), если нет входа с таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_price`
`primary:v6:functions:strategy.closedtrades.entry_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.entry_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену входа закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_time`
`primary:v6:functions:strategy.closedtrades.entry_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.entry_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время входа закрытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_bar_index`
`primary:v6:functions:strategy.closedtrades.exit_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.exit_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index выхода закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_comment`
`primary:v6:functions:strategy.closedtrades.exit_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.exit_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария выхода закрытой сделки или [na](#var_na), если нет входа с таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_price`
`primary:v6:functions:strategy.closedtrades.exit_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.exit_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену выхода закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://blog.traderspost.io/article/pine-script-v6-strategy-changes), ссылка составлена по заметкам.

---

### `strategy.closedtrades.exit_time`
`primary:v6:functions:strategy.closedtrades.exit_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.exit_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время выхода закрытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.max_drawdown`
`primary:v6:functions:strategy.closedtrades.max_drawdown:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.max_drawdown)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по закрытой сделке, т.е. максимально возможный убыток в ходе сделки, выраженный в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.max_drawdown_percent`
`primary:v6:functions:strategy.closedtrades.max_drawdown_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.max_drawdown_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по закрытой сделке, т.е. максимально возможный убыток за время торговли, выраженный в процентах и рассчитываемый по формуле: `Lowest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.max_runup`
`primary:v6:functions:strategy.closedtrades.max_runup:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.max_runup)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по закрытой сделке, т.е. максимально возможную прибыль по сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.max_runup_percent`
`primary:v6:functions:strategy.closedtrades.max_runup_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.max_runup_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по закрытой сделке, т.е. максимально возможную прибыль за время торговли, выраженную в процентах и рассчитываемую по формуле: `Highest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.profit`
`primary:v6:functions:strategy.closedtrades.profit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.profit)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток закрытой сделки в валюте счета стратегии, уменьшенные на комиссии сделки. Положительное возвращаемое значение представляет прибыль, а отрицательное значение представляет убыток.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.profit_percent`
`primary:v6:functions:strategy.closedtrades.profit_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.profit_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение прибыли/убытка по закрытой сделке, выраженное в процентах. Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.size`
`primary:v6:functions:strategy.closedtrades.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.closedtrades.size)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает направление и число торгуемых контрактов в закрытой сделке. Если это значение > 0, рыночная позиция была длинной. Если значение < 0, позиция была короткой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.convert_to_account`
`primary:v6:functions:strategy.convert_to_account:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.convert_to_account)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Конвертирует значение из валюты, в которой торгуется инструмент на графике ([syminfo.currency](#var_syminfo.currency)) в валюту стратегии ([strategy.account_currency](#var_strategy.account_currency)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.convert_to_symbol`
`primary:v6:functions:strategy.convert_to_symbol:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.convert_to_symbol)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Конвертирует значение из валюты стратегии ([strategy.account_currency](#var_strategy.account_currency)) в валюту, в которой торгуется инструмент на графике ([syminfo.currency](#var_syminfo.currency)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.default_entry_qty`
`primary:v6:functions:strategy.default_entry_qty:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.default_entry_qty)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Рассчитывает размер заявки на открытие позиции по умолчанию в единицах из [strategy.entry()](#fun_strategy.entry) или [strategy.order()](#fun_strategy.order), если она будет исполнена при указанном значении `fill_price`. Расчёт зависит от нескольких свойств стратегии, включая `default_qty_type`, `default_qty_value`, `…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `fill_price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.entry`
`primary:v6:functions:strategy.entry:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.entry)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `direction` | series strategy_direction / simple strategy_direction / input strategy_direction / const strategy_direction | required | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `oca_type` | input string / const string | optional | strategy.oca.none |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.exit`
`primary:v6:functions:strategy.exit:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.exit)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `from_entry` | series string / simple string / input string / const string | optional | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `qty_percent` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | 100 |
| `profit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `loss` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_price` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_points` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_offset` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `comment_profit` | series string / simple string / input string / const string | optional | не установлено |
| `comment_loss` | series string / simple string / input string / const string | optional | не установлено |
| `comment_trailing` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `alert_profit` | series string / simple string / input string / const string | optional | не установлено |
| `alert_loss` | series string / simple string / input string / const string | optional | не установлено |
| `alert_trailing` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.opentrades.commission`
`primary:v6:functions:strategy.opentrades.commission:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.commission)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает сумму комиссий за вход и выход, уплаченных по открытой сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.entry_bar_index`
`primary:v6:functions:strategy.opentrades.entry_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.entry_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index входа открытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.entry_comment`
`primary:v6:functions:strategy.opentrades.entry_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.entry_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария входа открытой сделки или [na](#var_na), если нет входа с таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.opentrades.entry_price`
`primary:v6:functions:strategy.opentrades.entry_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.entry_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену входа открытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.opentrades.entry_time`
`primary:v6:functions:strategy.opentrades.entry_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.entry_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время входа открытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.opentrades.max_drawdown`
`primary:v6:functions:strategy.opentrades.max_drawdown:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.max_drawdown)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку открытой сделки, т.е. максимально возможный убыток в ходе сделки, выраженный в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_drawdown_percent`
`primary:v6:functions:strategy.opentrades.max_drawdown_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.max_drawdown_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по открытой сделке, т.е. максимально возможный убыток за время торговли, выраженный в процентах и рассчитываемый по формуле: `Lowest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_runup`
`primary:v6:functions:strategy.opentrades.max_runup:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.max_runup)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по открытой сделке, т.е. максимально возможную прибыль во время сделки, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_runup_percent`
`primary:v6:functions:strategy.opentrades.max_runup_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.max_runup_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по открытой сделке, т.е. максимально возможную прибыль за время торговли, выраженную в процентах и рассчитываемую по формуле: `Highest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.profit`
`primary:v6:functions:strategy.opentrades.profit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.profit)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток по открытой сделке, выраженные в [strategy.account_currency](#var_strategy.account_currency). Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.profit_percent`
`primary:v6:functions:strategy.opentrades.profit_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.profit_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток по открытой сделке, выраженные в процентах. Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.size`
`primary:v6:functions:strategy.opentrades.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.opentrades.size)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает направление и число торгуемых контрактов в открытой сделке. Если это значение > 0, рыночная позиция была длинной. Если значение < 0, позиция была короткой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.order`
`primary:v6:functions:strategy.order:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.order)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `direction` | series strategy_direction / simple strategy_direction / input strategy_direction / const strategy_direction | required | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `oca_type` | input string / const string | optional | strategy.oca.none |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.risk.allow_entry_in`
`primary:v6:functions:strategy.risk.allow_entry_in:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.allow_entry_in)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_cons_loss_days`
`primary:v6:functions:strategy.risk.max_cons_loss_days:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.max_cons_loss_days)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | simple int / input int / const int | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_drawdown`
`primary:v6:functions:strategy.risk.max_drawdown:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.max_drawdown)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple int / input int / const int / simple float / input float / const float | required | не установлено |
| `type` | simple string / input string / const string | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.risk.max_intraday_filled_orders`
`primary:v6:functions:strategy.risk.max_intraday_filled_orders:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.max_intraday_filled_orders)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | simple int / input int / const int | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_loss`
`primary:v6:functions:strategy.risk.max_intraday_loss:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.max_intraday_loss)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple int / input int / const int / simple float / input float / const float | required | не установлено |
| `type` | simple string / input string / const string | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.risk.max_position_size`
`primary:v6:functions:strategy.risk.max_position_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_strategy.risk.max_position_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `contracts` | simple int / input int / const int / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.max`
`primary:v6:functions:ta.max:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.max)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение максимума за все время для `source` с начала графика до текущего бара.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ta.min`
`primary:v6:functions:ta.min:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.min)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение минимума за все время для `source` с начала графика до текущего бара.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ta.valuewhen`
`primary:v6:functions:ta.valuewhen:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.valuewhen)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v6:functions:ta.valuewhen:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.valuewhen)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series int / simple int / input int / const int | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v6:functions:ta.valuewhen:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.valuewhen)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series bool / simple bool / input bool / const bool | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v6:functions:ta.valuewhen:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.valuewhen)

**Тип результата:** `series color`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series color / simple color / input color / const color | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell`
`primary:v6:functions:table.cell:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | color.black |
| `text_halign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_valign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | unknown | size.normal |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |
| `text_font_family` | series string / simple string / input string / const string | unknown | font.family_default |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | unknown | text.format_none |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell`
`primary:v6:methods:table.cell:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | color.black |
| `text_halign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_valign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | unknown | size.normal |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |
| `text_font_family` | series string / simple string / input string / const string | unknown | font.family_default |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | unknown | text.format_none |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell_set_bgcolor`
`primary:v6:functions:table.cell_set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell_set_bgcolor`
`primary:v6:methods:table.cell_set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell_set_height`
`primary:v6:functions:table.cell_set_height:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_height)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_height`
`primary:v6:methods:table.cell_set_height:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_height)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text`
`primary:v6:functions:table.cell_set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text`
`primary:v6:methods:table.cell_set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_color`
`primary:v6:functions:table.cell_set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_color`
`primary:v6:methods:table.cell_set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_font_family`
`primary:v6:functions:table.cell_set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_font_family`
`primary:v6:methods:table.cell_set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_formatting`
`primary:v6:functions:table.cell_set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_formatting`
`primary:v6:methods:table.cell_set_text_formatting:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_formatting)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_formatting` | series text_format / simple text_format / input text_format / const text_format | required | text.format_none |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_halign`
`primary:v6:functions:table.cell_set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_halign`
`primary:v6:methods:table.cell_set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_size`
`primary:v6:functions:table.cell_set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | unknown | size.normal |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_size`
`primary:v6:methods:table.cell_set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_size` | series int / simple int / input int / const int / series string / simple string / input string / const string | unknown | size.normal |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_valign`
`primary:v6:functions:table.cell_set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_text_valign`
`primary:v6:methods:table.cell_set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_tooltip`
`primary:v6:functions:table.cell_set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_tooltip`
`primary:v6:methods:table.cell_set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_width`
`primary:v6:functions:table.cell_set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.cell_set_width`
`primary:v6:methods:table.cell_set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.cell_set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.clear`
`primary:v6:functions:table.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | unknown | не установлено |
| `end_row` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.clear`
`primary:v6:methods:table.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | unknown | не установлено |
| `end_row` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.delete`
`primary:v6:functions:table.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.delete`
`primary:v6:methods:table.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.merge_cells`
`primary:v6:functions:table.merge_cells:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.merge_cells)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | required | не установлено |
| `end_row` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.merge_cells`
`primary:v6:methods:table.merge_cells:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.merge_cells)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | required | не установлено |
| `end_row` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.set_bgcolor`
`primary:v6:functions:table.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_bgcolor`
`primary:v6:methods:table.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_border_color`
`primary:v6:functions:table.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_border_color`
`primary:v6:methods:table.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_border_width`
`primary:v6:functions:table.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_border_width`
`primary:v6:methods:table.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_frame_color`
`primary:v6:functions:table.set_frame_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_frame_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_frame_color`
`primary:v6:methods:table.set_frame_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_frame_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_frame_width`
`primary:v6:functions:table.set_frame_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_frame_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_frame_width`
`primary:v6:methods:table.set_frame_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_frame_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_position`
`primary:v6:functions:table.set_position:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_position)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `position` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `table.set_position`
`primary:v6:methods:table.set_position:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_table.set_position)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `position` | series string / simple string / input string / const string | required | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/visuals/tables/#modifying-table-and-cell-properties), ссылка составлена по заметкам.

---

### `ticker.inherit`
`primary:v6:functions:ticker.inherit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ticker.inherit)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Составляет идентификатор тикера для указанного `symbol` с дополнительными параметрами, унаследованными от идентификатора тикера, переданного в вызов функции, что позволяет скрипту запрашивать данные по инструменту с использованием тех же модификаторов, что и у `from_tickerid`, включая расширенную сессию, корректировку…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `from_tickerid` | simple string / input string / const string | required | не установлено |
| `symbol` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ticker.inherit`
`primary:v6:functions:ticker.inherit:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v6/#fun_ticker.inherit)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Составляет идентификатор тикера для указанного `symbol` с дополнительными параметрами, унаследованными от идентификатора тикера, переданного в вызов функции, что позволяет скрипту запрашивать данные по инструменту с использованием тех же модификаторов, что и у `from_tickerid`, включая расширенную сессию, корректировку…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `from_tickerid` | series string / simple string / input string / const string | required | не установлено |
| `symbol` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

## Версия v5 — 327 записей

### `alert`
`primary:v5:functions:alert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_alert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `message` | series string / simple string / input string / const string | required | не установлено |
| `freq` | input string / const string | unknown | alert.freq_once_per_bar |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `alertcondition`
`primary:v5:functions:alertcondition:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `message` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.abs`
`primary:v5:functions:array.abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.abs)

**Тип результата:** `array<float>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v5:functions:array.abs:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.abs)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v5:methods:array.abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.abs)

**Тип результата:** `array<float>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.abs`
`primary:v5:methods:array.abs:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.abs)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив, содержащий абсолютное значение каждого элемента исходного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search`
`primary:v5:functions:array.binary_search:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения или -1, если значение не найдено. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search`
`primary:v5:methods:array.binary_search:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения или -1, если значение не найдено. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.binary_search_leftmost`
`primary:v5:functions:array.binary_search_leftmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения, если оно найдено. Если значение не найдено, функция возвращает индекс следующего наименьшего элемента слева от того, где находилось бы значение, если бы оно было в массиве. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_leftmost`
`primary:v5:methods:array.binary_search_leftmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search_leftmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения, если оно найдено. Если значение не найдено, функция возвращает индекс следующего наименьшего элемента слева от того, где находилось бы значение, если бы оно было в массиве. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v5:functions:array.binary_search_rightmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения, если оно найдено. Если значение не найдено, функция возвращает индекс элемента справа от того, где находилось бы значение, если бы оно было в массиве. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.binary_search_rightmost`
`primary:v5:methods:array.binary_search_rightmost:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.binary_search_rightmost)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает индекс значения, если оно найдено. Если значение не найдено, функция возвращает индекс элемента справа от того, где находилось бы значение, если бы оно было в массиве. Массив для поиска должен быть отсортирован по возрастанию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `val` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.clear`
`primary:v5:functions:array.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.clear`
`primary:v5:methods:array.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.every`
`primary:v5:functions:array.every:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.every)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если все элементы массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.every`
`primary:v5:methods:array.every:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.every)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если все элементы массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.fill`
`primary:v5:functions:array.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |
| `index_from` | series int / simple int / input int / const int | unknown | 0 |
| `index_to` | series int / simple int / input int / const int | unknown | na |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.fill`
`primary:v5:methods:array.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |
| `index_from` | series int / simple int / input int / const int | unknown | 0 |
| `index_to` | series int / simple int / input int / const int | unknown | na |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.first`
`primary:v5:functions:array.first:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.first)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает первый элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.first`
`primary:v5:methods:array.first:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.first)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает первый элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.insert`
`primary:v5:functions:array.insert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.insert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | unknown | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.insert`
`primary:v5:methods:array.insert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.insert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | unknown | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.join`
`primary:v5:functions:array.join:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.join)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Функция создает и возвращает новую строку путем объединения всех элементов массива, разделённых заданной строкой-разделителем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.join`
`primary:v5:methods:array.join:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.join)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Функция создает и возвращает новую строку путем объединения всех элементов массива, разделённых заданной строкой-разделителем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.last`
`primary:v5:functions:array.last:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.last)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает последний элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.last`
`primary:v5:methods:array.last:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.last)

**Тип результата:** `series <type>`.
**Описание в сохранённой карточке:** Возвращает последний элемент массива или ошибку времени выполнения, если массив пустой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.percentile_linear_interpolation`
`primary:v5:functions:array.percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v5:functions:array.percentile_linear_interpolation:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v5:methods:array.percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_linear_interpolation`
`primary:v5:methods:array.percentile_linear_interpolation:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_linear_interpolation)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя линейную интерполяцию.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v5:functions:array.percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_nearest_rank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v5:functions:array.percentile_nearest_rank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_nearest_rank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v5:methods:array.percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_nearest_rank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentile_nearest_rank`
`primary:v5:methods:array.percentile_nearest_rank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentile_nearest_rank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение, для которого указанный процент значений массива (процентиль) меньше или равен ему, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `percentage` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v5:functions:array.percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentrank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v5:functions:array.percentrank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentrank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v5:methods:array.percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentrank)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.percentrank`
`primary:v5:methods:array.percentrank:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.percentrank)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает процентильный ранг элемента заданного `index`

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.push`
`primary:v5:functions:array.push:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.push)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.push`
`primary:v5:methods:array.push:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.push)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.reverse`
`primary:v5:functions:array.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.reverse`
`primary:v5:methods:array.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.set`
`primary:v5:functions:array.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.set`
`primary:v5:methods:array.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.some`
`primary:v5:functions:array.some:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.some)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если хотя бы один из элементов массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.some`
`primary:v5:methods:array.some:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.some)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если хотя бы один из элементов массива `id` — [true](#const_true). В противном случае — [false](#const_false).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<bool> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `array.sort`
`primary:v5:functions:array.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort`
`primary:v5:methods:array.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v5:functions:array.sort_indices:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort_indices`
`primary:v5:methods:array.sort_indices:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.sort_indices)

**Тип результата:** `array<int>`.
**Описание в сохранённой карточке:** Возвращает массив индексов, при использовании которых для индексации исходного массива доступ к его элементам будет осуществляться в отсортированном порядке. Не изменяет исходный массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<int> / array<float> / array<string> | required | не установлено |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.unshift`
`primary:v5:functions:array.unshift:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.unshift)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.unshift`
`primary:v5:methods:array.unshift:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_array.unshift)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array<> | required | не установлено |
| `value` | series <type of the array's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `barcolor`
`primary:v5:functions:barcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_barcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series color / simple color / input color / const color | required | не установлено |
| `offset` | series int / simple int / input int / const int | unknown | 0 |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bgcolor`
`primary:v5:functions:bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series color / simple color / input color / const color | required | не установлено |
| `offset` | series int / simple int / input int / const int | unknown | 0 |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `force_overlay` | const bool | unknown | false |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.copy`
`primary:v5:functions:box.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.copy)

**Тип результата:** `series box`.
**Описание в сохранённой карточке:** Клонирует объект box.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.copy`
`primary:v5:methods:box.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.copy)

**Тип результата:** `series box`.
**Описание в сохранённой карточке:** Клонирует объект box.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.delete`
`primary:v5:functions:box.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.delete`
`primary:v5:methods:box.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bgcolor`
`primary:v5:functions:box.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bgcolor`
`primary:v5:methods:box.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_color`
`primary:v5:functions:box.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_color`
`primary:v5:methods:box.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_border_style`
`primary:v5:functions:box.set_border_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_border_style`
`primary:v5:methods:box.set_border_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_border_width`
`primary:v5:functions:box.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_width`
`primary:v5:methods:box.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_bottom`
`primary:v5:functions:box.set_bottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_bottom`
`primary:v5:methods:box.set_bottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_bottom_right_point`
`primary:v5:functions:box.set_bottom_right_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bottom_right_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_bottom_right_point`
`primary:v5:methods:box.set_bottom_right_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_bottom_right_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_extend`
`primary:v5:functions:box.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_extend`
`primary:v5:methods:box.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_left`
`primary:v5:functions:box.set_left:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_left)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_left`
`primary:v5:methods:box.set_left:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_left)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_lefttop`
`primary:v5:functions:box.set_lefttop:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_lefttop)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_lefttop`
`primary:v5:methods:box.set_lefttop:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_lefttop)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `left` | series int / simple int / input int / const int | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_right`
`primary:v5:functions:box.set_right:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_right)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_right`
`primary:v5:methods:box.set_right:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_right)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_rightbottom`
`primary:v5:functions:box.set_rightbottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_rightbottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_rightbottom`
`primary:v5:methods:box.set_rightbottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_rightbottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `right` | series int / simple int / input int / const int | required | не установлено |
| `bottom` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_text`
`primary:v5:functions:box.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text`
`primary:v5:methods:box.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_text_color`
`primary:v5:functions:box.set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_color`
`primary:v5:methods:box.set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_font_family`
`primary:v5:functions:box.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.set_text_font_family`
`primary:v5:methods:box.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.set_text_halign`
`primary:v5:functions:box.set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_halign`
`primary:v5:methods:box.set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_size`
`primary:v5:functions:box.set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_size` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_size`
`primary:v5:methods:box.set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_size` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_valign`
`primary:v5:functions:box.set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_valign`
`primary:v5:methods:box.set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_wrap`
`primary:v5:functions:box.set_text_wrap:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_wrap)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_wrap` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_text_wrap`
`primary:v5:methods:box.set_text_wrap:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_text_wrap)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `text_wrap` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_top`
`primary:v5:functions:box.set_top:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_top)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top`
`primary:v5:methods:box.set_top:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_top)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `top` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top_left_point`
`primary:v5:functions:box.set_top_left_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_top_left_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top_left_point`
`primary:v5:methods:box.set_top_left_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_box.set_top_left_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series box | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.copy`
`primary:v5:functions:chart.point.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.copy)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт копию объекта [chart.point](#type_chart.point) с заданным значением `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.copy`
`primary:v5:methods:chart.point.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.copy)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт копию объекта [chart.point](#type_chart.point) с заданным значением `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.from_index`
`primary:v5:functions:chart.point.from_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.from_index)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `index` в качестве его x-координаты и `price` — y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `index` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `chart.point.from_time`
`primary:v5:functions:chart.point.from_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.from_time)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `time` в качестве его x-координаты и `price` — y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `chart.point.new`
`primary:v5:functions:chart.point.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.new)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Создаёт новый объект [chart.point](#type_chart.point) с заданными `time`, `index` и `price`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series int / simple int / input int / const int | required | не установлено |
| `index` | series int / simple int / input int / const int | required | не установлено |
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `chart.point.now`
`primary:v5:functions:chart.point.now:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.now)

**Тип результата:** `chart.point`.
**Описание в сохранённой карточке:** Возвращает объект [chart.point](#type_chart.point) с `price` в качестве y-координаты.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `price` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | close |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v5:functions:fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `plot1` | plot | required | не установлено |
| `plot2` | plot | required | не установлено |
| `top_value` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `bottom_value` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `top_color` | series color / simple color / input color / const color | unknown | не установлено |
| `bottom_color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `fillgaps` | const bool | unknown | false |
| `editable` | const bool | unknown | true |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v5:functions:fill:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `hline1` | hline | required | не установлено |
| `hline2` | hline | required | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `fillgaps` | const bool | unknown | false |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `fill`
`primary:v5:functions:fill:overload:2` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `plot1` | plot | required | не установлено |
| `plot2` | plot | required | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `fillgaps` | const bool | unknown | false |
| `display` | input plot_simple_display / const plot_simple_display | unknown | display.all |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `indicator`
`primary:v5:functions:indicator:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `format` | const string | unknown | format.inherit |
| `precision` | const int | unknown | не установлено |
| `scale` | const scale_type | unknown | не установлено |
| `max_bars_back` | const int | unknown | 0 |
| `timeframe` | const string | unknown | timeframe.period |
| `timeframe_gaps` | const bool | unknown | true |
| `explicit_plot_zorder` | const bool | unknown | false |
| `max_lines_count` | const int | unknown | 50 |
| `max_labels_count` | const int | unknown | 50 |
| `max_boxes_count` | const int | unknown | 50 |
| `calc_bars_count` | const int | unknown | 0 |
| `max_polylines_count` | const int | unknown | 50 |
| `dynamic_requests` | const bool | unknown | false |
| `behind_chart` | const bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.delete`
`primary:v5:functions:label.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.delete`
`primary:v5:methods:label.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_color`
`primary:v5:functions:label.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_color`
`primary:v5:methods:label.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_point`
`primary:v5:functions:label.set_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_point`
`primary:v5:methods:label.set_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_size`
`primary:v5:functions:label.set_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `size` | series string / simple string / input string / const string | required | size.auto |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_size`
`primary:v5:methods:label.set_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `size` | series string / simple string / input string / const string | required | size.auto |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_style`
`primary:v5:functions:label.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_style`
`primary:v5:methods:label.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text`
`primary:v5:functions:label.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text`
`primary:v5:methods:label.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_text_font_family`
`primary:v5:functions:label.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.set_text_font_family`
`primary:v5:methods:label.set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.set_textalign`
`primary:v5:functions:label.set_textalign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_textalign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textalign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textalign`
`primary:v5:methods:label.set_textalign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_textalign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textalign` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textcolor`
`primary:v5:functions:label.set_textcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_textcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textcolor` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textcolor`
`primary:v5:methods:label.set_textcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_textcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `textcolor` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_tooltip`
`primary:v5:functions:label.set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_tooltip`
`primary:v5:methods:label.set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_x`
`primary:v5:functions:label.set_x:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_x)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_x`
`primary:v5:methods:label.set_x:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_x)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xloc`
`primary:v5:functions:label.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xloc`
`primary:v5:methods:label.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xy`
`primary:v5:functions:label.set_xy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_xy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xy`
`primary:v5:methods:label.set_xy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_xy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_y`
`primary:v5:functions:label.set_y:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_y)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_y`
`primary:v5:methods:label.set_y:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_y)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_yloc`
`primary:v5:functions:label.set_yloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_yloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `yloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_yloc`
`primary:v5:methods:label.set_yloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_label.set_yloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series label | required | не установлено |
| `yloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `library`
`primary:v5:functions:library:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_library)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `overlay` | const bool | unknown | false |
| `dynamic_requests` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `line.delete`
`primary:v5:functions:line.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.delete`
`primary:v5:methods:line.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_color`
`primary:v5:functions:line.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_color`
`primary:v5:methods:line.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_extend`
`primary:v5:functions:line.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_extend`
`primary:v5:methods:line.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `extend` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_first_point`
`primary:v5:functions:line.set_first_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_first_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_first_point`
`primary:v5:methods:line.set_first_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_first_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_second_point`
`primary:v5:functions:line.set_second_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_second_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_second_point`
`primary:v5:methods:line.set_second_point:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_second_point)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `point` | chart.point | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_style`
`primary:v5:functions:line.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_style`
`primary:v5:methods:line.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `style` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_width`
`primary:v5:functions:line.set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_width`
`primary:v5:methods:line.set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `width` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_x1`
`primary:v5:functions:line.set_x1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_x1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_x1`
`primary:v5:methods:line.set_x1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_x1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_x2`
`primary:v5:functions:line.set_x2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_x2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_x2`
`primary:v5:methods:line.set_x2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_x2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xloc`
`primary:v5:functions:line.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x1` | series int / simple int / input int / const int | required | не установлено |
| `x2` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xloc`
`primary:v5:methods:line.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x1` | series int / simple int / input int / const int | required | не установлено |
| `x2` | series int / simple int / input int / const int | required | не установлено |
| `xloc` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xy1`
`primary:v5:functions:line.set_xy1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xy1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_xy1`
`primary:v5:methods:line.set_xy1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xy1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xy2`
`primary:v5:functions:line.set_xy2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xy2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_xy2`
`primary:v5:methods:line.set_xy2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_xy2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `x` | series int / simple int / input int / const int | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y1`
`primary:v5:functions:line.set_y1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_y1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y1`
`primary:v5:methods:line.set_y1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_y1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y2`
`primary:v5:functions:line.set_y2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_y2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_y2`
`primary:v5:methods:line.set_y2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_line.set_y2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series line | required | не установлено |
| `y` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `linefill.delete`
`primary:v5:functions:linefill.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.delete`
`primary:v5:methods:linefill.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line1`
`primary:v5:functions:linefill.get_line1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.get_line1)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID первой линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line1`
`primary:v5:methods:linefill.get_line1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.get_line1)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID первой линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line2`
`primary:v5:functions:linefill.get_line2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.get_line2)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID второй линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.get_line2`
`primary:v5:methods:linefill.get_line2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.get_line2)

**Тип результата:** `series line`.
**Описание в сохранённой карточке:** Возвращает ID второй линии, использованной в объекте linefill, который передан в `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.set_color`
`primary:v5:functions:linefill.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linefill.set_color`
`primary:v5:methods:linefill.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_linefill.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series linefill | required | не установлено |
| `color` | series color / simple color / input color / const color | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `map.clear`
`primary:v5:functions:map.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.clear`
`primary:v5:methods:map.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.contains`
`primary:v5:functions:map.contains:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.contains)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если в объекте map `id` был найден `key`, [false](#const_false), если нет.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.contains`
`primary:v5:methods:map.contains:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.contains)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает [true](#const_true), если в объекте map `id` был найден `key`, [false](#const_false), если нет.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.get`
`primary:v5:functions:map.get:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.get)

**Тип результата:** `<value_type>`.
**Описание в сохранённой карточке:** Возвращает значение, ассоциированное с указанным `key` в `id` объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.get`
`primary:v5:methods:map.get:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.get)

**Тип результата:** `<value_type>`.
**Описание в сохранённой карточке:** Возвращает значение, ассоциированное с указанным `key` в `id` объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `key` | series <type of the map's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.keys`
`primary:v5:functions:map.keys:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.keys)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех ключей в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.keys`
`primary:v5:methods:map.keys:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.keys)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех ключей в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.put_all`
`primary:v5:functions:map.put_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.put_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `id2` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.put_all`
`primary:v5:methods:map.put_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.put_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |
| `id2` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.size`
`primary:v5:functions:map.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.size)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает количество пар ключ-значение в объекте map типа `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.size`
`primary:v5:methods:map.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.size)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает количество пар ключ-значение в объекте map типа `id`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.values`
`primary:v5:functions:map.values:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.values)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех значений в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `map.values`
`primary:v5:methods:map.values:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_map.values)

**Тип результата:** `array<type>`.
**Описание в сохранённой карточке:** Возвращает массив всех значений в `id` объекте map. Полученный массив является копией, и любые изменения в нем не отражаются на исходном объекте map.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | map<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.add_col`
`primary:v5:functions:matrix.add_col:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | matrix.columns |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_col`
`primary:v5:functions:matrix.add_col:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | matrix.columns |
| `array_id` | array<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_col`
`primary:v5:methods:matrix.add_col:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | matrix.columns |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_col`
`primary:v5:methods:matrix.add_col:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_col)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | matrix.columns |
| `array_id` | array<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v5:functions:matrix.add_row:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | unknown | matrix.rows |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v5:functions:matrix.add_row:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | unknown | matrix.rows |
| `array_id` | array<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v5:methods:matrix.add_row:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | unknown | matrix.rows |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.add_row`
`primary:v5:methods:matrix.add_row:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.add_row)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | unknown | matrix.rows |
| `array_id` | array<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.elements_count`
`primary:v5:functions:matrix.elements_count:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.elements_count)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает общее количество всех элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.elements_count`
`primary:v5:methods:matrix.elements_count:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.elements_count)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция возвращает общее количество всех элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `matrix.fill`
`primary:v5:functions:matrix.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |
| `from_row` | series int / simple int / input int / const int | unknown | 0 |
| `to_row` | series int / simple int / input int / const int | unknown | matrix.rows |
| `from_column` | series int / simple int / input int / const int | unknown | 0 |
| `to_column` | series int / simple int / input int / const int | unknown | matrix.columns |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.fill`
`primary:v5:methods:matrix.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |
| `from_row` | series int / simple int / input int / const int | unknown | 0 |
| `to_row` | series int / simple int / input int / const int | unknown | matrix.rows |
| `from_column` | series int / simple int / input int / const int | unknown | 0 |
| `to_column` | series int / simple int / input int / const int | unknown | matrix.columns |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v5:functions:matrix.median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.median)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v5:functions:matrix.median:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.median)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v5:methods:matrix.median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.median)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.median`
`primary:v5:methods:matrix.median:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.median)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Функция вычисляет [медиану](https://en.wikipedia.org/wiki/Median) ("серединное" значение) элементов матрицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reshape`
`primary:v5:functions:matrix.reshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.reshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `rows` | series int / simple int / input int / const int | required | не установлено |
| `columns` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reshape`
`primary:v5:methods:matrix.reshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.reshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `rows` | series int / simple int / input int / const int | required | не установлено |
| `columns` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reverse`
`primary:v5:functions:matrix.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.reverse`
`primary:v5:methods:matrix.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.set`
`primary:v5:functions:matrix.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.set`
`primary:v5:methods:matrix.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `value` | series <type of the matrix's elements> | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v5:functions:matrix.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> / matrix<string> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.sort`
`primary:v5:methods:matrix.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<int> / matrix<float> / matrix<string> | required | не установлено |
| `column` | series int / simple int / input int / const int | unknown | 0 |
| `order` | series sort_order / simple sort_order / input sort_order / const sort_order | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_columns`
`primary:v5:functions:matrix.swap_columns:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.swap_columns)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column1` | series int / simple int / input int / const int | required | не установлено |
| `column2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_columns`
`primary:v5:methods:matrix.swap_columns:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.swap_columns)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `column1` | series int / simple int / input int / const int | required | не установлено |
| `column2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_rows`
`primary:v5:functions:matrix.swap_rows:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.swap_rows)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row1` | series int / simple int / input int / const int | required | не установлено |
| `row2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `matrix.swap_rows`
`primary:v5:methods:matrix.swap_rows:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix.swap_rows)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | matrix<> | required | не установлено |
| `row1` | series int / simple int / input int / const int | required | не установлено |
| `row2` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotarrow`
`primary:v5:functions:plotarrow:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_plotarrow)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `colorup` | series color / simple color / input color / const color | unknown | не установлено |
| `colordown` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | series int / simple int / input int / const int | unknown | 0 |
| `minheight` | input int / const int | unknown | 5 |
| `maxheight` | input int / const int | unknown | 100 |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotbar`
`primary:v5:functions:plotbar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_plotbar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `high` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `low` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `close` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotcandle`
`primary:v5:functions:plotcandle:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_plotcandle)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `high` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `low` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `close` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `wickcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `show_last` | input int / const int | unknown | не установлено |
| `bordercolor` | series color / simple color / input color / const color | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotchar`
`primary:v5:functions:plotchar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_plotchar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float / series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `char` | input string / const string | unknown | не установлено |
| `location` | input string / const string | unknown | location.abovebar |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | series int / simple int / input int / const int | unknown | 0 |
| `text` | const string | unknown | не установлено |
| `textcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | input int / const int | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotshape`
`primary:v5:functions:plotshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_plotshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series int / simple int / input int / const int / series float / simple float / input float / const float / series bool / simple bool / input bool / const bool | required | не установлено |
| `title` | const string | unknown | не установлено |
| `style` | input string / const string | unknown | shape.xcross |
| `location` | input string / const string | unknown | location.abovebar |
| `color` | series color / simple color / input color / const color | unknown | не установлено |
| `offset` | series int / simple int / input int / const int | unknown | 0 |
| `text` | const string | unknown | не установлено |
| `textcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | input int / const int | unknown | не установлено |
| `display` | input plot_display / const plot_display / input plot_simple_display / const plot_simple_display | unknown | display.all |
| `format` | input string / const string | unknown | не установлено |
| `precision` | input int / const int | unknown | не установлено |
| `force_overlay` | const bool | unknown | false |
| `transp` | **не указан** | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `polyline.delete`
`primary:v5:functions:polyline.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_polyline.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series polyline | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `polyline.delete`
`primary:v5:methods:polyline.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_polyline.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series polyline | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `request.currency_rate`
`primary:v5:functions:request.currency_rate:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_request.currency_rate)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Предоставляет курс, по которому можно конвертировать значение, выраженное в валюте `from`, в другое значение в валюте `to`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `from` | series string / simple string / input string / const string | required | не установлено |
| `to` | series string / simple string / input string / const string | required | не установлено |
| `ignore_invalid_currency` | series bool / simple bool / input bool / const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `runtime.error`
`primary:v5:functions:runtime.error:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_runtime.error)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `message` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `str.repeat`
`primary:v5:functions:str.repeat:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.repeat)

**Тип результата:** `const string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | const string | required | не установлено |
| `repeat` | const int | required | не установлено |
| `separator` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v5:functions:str.repeat:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.repeat)

**Тип результата:** `input string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | input string / const string | required | не установлено |
| `repeat` | input int / const int | required | не установлено |
| `separator` | input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v5:functions:str.repeat:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.repeat)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | simple string / input string / const string | required | не установлено |
| `repeat` | simple int / input int / const int | required | не установлено |
| `separator` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.repeat`
`primary:v5:functions:str.repeat:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.repeat)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Создаёт новую строку, содержащую строку `source`, повторённую `repeat` раз с `separator`, вставленным между каждым повтором.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series string / simple string / input string / const string | required | не установлено |
| `repeat` | series int / simple int / input int / const int | required | не установлено |
| `separator` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v5:functions:str.trim:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.trim)

**Тип результата:** `const string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v5:functions:str.trim:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.trim)

**Тип результата:** `input string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v5:functions:str.trim:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.trim)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.trim`
`primary:v5:functions:str.trim:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_str.trim)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Создаёт новую строку, в которой все последовательные пробелы и другие управляющие символы (например, "\n", "\ " и т. д.) удалены слева и справа от `source`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy`
`primary:v5:functions:strategy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | required | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `format` | const string | unknown | format.inherit |
| `precision` | const int | unknown | не установлено |
| `scale` | const scale_type | unknown | не установлено |
| `pyramiding` | const int | unknown | 0 |
| `calc_on_order_fills` | const bool | unknown | false |
| `calc_on_every_tick` | const bool | unknown | false |
| `max_bars_back` | const int | unknown | 0 |
| `backtest_fill_limits_assumption` | const int | unknown | 0 |
| `default_qty_type` | const string | unknown | strategy.fixed |
| `default_qty_value` | const int / const float | unknown | 1 |
| `initial_capital` | const int / const float | unknown | 1000000 |
| `currency` | const string | unknown | currency.NONE |
| `slippage` | const int | unknown | 0 |
| `commission_type` | const string | unknown | strategy.commission.percent |
| `commission_value` | const int / const float | unknown | 0 |
| `process_orders_on_close` | const bool | unknown | false |
| `close_entries_rule` | const string | unknown | "FIFO" |
| `margin_long` | const int / const float | unknown | 0 |
| `margin_short` | const int / const float | unknown | 0 |
| `explicit_plot_zorder` | const bool | unknown | false |
| `max_lines_count` | const int | unknown | 50 |
| `max_labels_count` | const int | unknown | 50 |
| `max_boxes_count` | const int | unknown | 50 |
| `calc_bars_count` | const int | unknown | 0 |
| `risk_free_rate` | const int / const float | unknown | 2 |
| `use_bar_magnifier` | const bool | unknown | false |
| `fill_orders_on_standard_ohlc` | const bool | unknown | false |
| `max_polylines_count` | const int | unknown | 50 |
| `dynamic_requests` | const bool | unknown | false |
| `behind_chart` | const bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel`
`primary:v5:functions:strategy.cancel:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.cancel)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel_all`
`primary:v5:functions:strategy.cancel_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.cancel_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close`
`primary:v5:functions:strategy.close:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.close)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `qty_percent` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | 100 |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `immediately` | series bool / simple bool / input bool / const bool | optional | false |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close_all`
`primary:v5:functions:strategy.close_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.close_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close_all`
`primary:v5:functions:strategy.close_all:overload:1` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.close_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `immediately` | series bool / simple bool / input bool / const bool | optional | false |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.commission`
`primary:v5:functions:strategy.closedtrades.commission:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.commission)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает сумму комиссий за вход и выход, уплаченных по закрытой сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_bar_index`
`primary:v5:functions:strategy.closedtrades.entry_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.entry_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index входа закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_comment`
`primary:v5:functions:strategy.closedtrades.entry_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.entry_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария входа закрытой сделки или [na](#var_na), если нет входа c таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_price`
`primary:v5:functions:strategy.closedtrades.entry_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.entry_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену входа закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.entry_time`
`primary:v5:functions:strategy.closedtrades.entry_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.entry_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время входа закрытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_bar_index`
`primary:v5:functions:strategy.closedtrades.exit_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.exit_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index выхода закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_comment`
`primary:v5:functions:strategy.closedtrades.exit_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.exit_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария выхода закрытой сделки или [na](#var_na), если нет входа c таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.exit_price`
`primary:v5:functions:strategy.closedtrades.exit_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.exit_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену выхода закрытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.exit_time`
`primary:v5:functions:strategy.closedtrades.exit_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.exit_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время выхода закрытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.closedtrades.max_drawdown`
`primary:v5:functions:strategy.closedtrades.max_drawdown:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.max_drawdown)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по закрытой сделке, т.е. максимально возможный убыток в ходе сделки, выраженный в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.max_drawdown_percent`
`primary:v5:functions:strategy.closedtrades.max_drawdown_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.max_drawdown_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по закрытой сделке, т.е. максимально возможный убыток за время торговли, выраженный в процентах и рассчитываемый по формуле: `Lowest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.max_runup`
`primary:v5:functions:strategy.closedtrades.max_runup:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.max_runup)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по закрытой сделке, т.е. максимально возможную прибыль по сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.max_runup_percent`
`primary:v5:functions:strategy.closedtrades.max_runup_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.max_runup_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по закрытой сделке, т.е. максимально возможную прибыль за время торговли, выраженную в процентах и рассчитываемую по формуле: `Highest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.profit`
`primary:v5:functions:strategy.closedtrades.profit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.profit)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток от закрытой сделки, выраженные в [strategy.account_currency](#var_strategy.account_currency). Убытки выражены отрицательными значениями.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.closedtrades.profit_percent`
`primary:v5:functions:strategy.closedtrades.profit_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.profit_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение прибыли/убытка по закрытой сделке, выраженное в процентах. Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.closedtrades.size`
`primary:v5:functions:strategy.closedtrades.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.closedtrades.size)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает направление и число торгуемых контрактов в закрытой сделке. Если это значение > 0, рыночная позиция была длинной. Если значение < 0, позиция была короткой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.convert_to_account`
`primary:v5:functions:strategy.convert_to_account:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.convert_to_account)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Конвертирует значение из валюты, в которой торгуется инструмент на графике ([syminfo.currency](#var_syminfo.currency)) в валюту стратегии ([strategy.account_currency](#var_strategy.account_currency)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.convert_to_symbol`
`primary:v5:functions:strategy.convert_to_symbol:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.convert_to_symbol)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Конвертирует значение из валюты стратегии ([strategy.account_currency](#var_strategy.account_currency)) в валюту, в которой торгуется инструмент на графике ([syminfo.currency](#var_syminfo.currency)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.default_entry_qty`
`primary:v5:functions:strategy.default_entry_qty:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.default_entry_qty)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Рассчитывает размер заявки на открытие позиции по умолчанию в единицах из [strategy.entry](#fun_strategy.entry) или [strategy.order](#fun_strategy.order), если она будет исполнена при указанном значении `fill_price`. Расчёт зависит от нескольких свойств стратегии, включая `default_qty_type`, `default_qty_value`, `curr…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `fill_price` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.entry`
`primary:v5:functions:strategy.entry:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.entry)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `direction` | series strategy_direction / simple strategy_direction / input strategy_direction / const strategy_direction | required | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `oca_type` | input string / const string | optional | strategy.oca.none |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.exit`
`primary:v5:functions:strategy.exit:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.exit)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `from_entry` | series string / simple string / input string / const string | optional | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `qty_percent` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | 100 |
| `profit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `loss` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_price` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_points` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `trail_offset` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `comment_profit` | series string / simple string / input string / const string | optional | не установлено |
| `comment_loss` | series string / simple string / input string / const string | optional | не установлено |
| `comment_trailing` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `alert_profit` | series string / simple string / input string / const string | optional | не установлено |
| `alert_loss` | series string / simple string / input string / const string | optional | не установлено |
| `alert_trailing` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.opentrades.commission`
`primary:v5:functions:strategy.opentrades.commission:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.commission)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает сумму комиссий за вход и выход, уплаченных по открытой сделке, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.entry_bar_index`
`primary:v5:functions:strategy.opentrades.entry_bar_index:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.entry_bar_index)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает bar_index входа открытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.entry_comment`
`primary:v5:functions:strategy.opentrades.entry_comment:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.entry_comment)

**Тип результата:** `series string`.
**Описание в сохранённой карточке:** Возвращает сообщение комментария входа открытой сделки или [na](#var_na), если нет входа c таким параметром `trade_num`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.opentrades.entry_price`
`primary:v5:functions:strategy.opentrades.entry_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.entry_price)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает цену входа открытой сделки.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.opentrades.entry_time`
`primary:v5:functions:strategy.opentrades.entry_time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.entry_time)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает UNIX-время входа открытой сделки, выраженное в миллисекундах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.opentrades.max_drawdown`
`primary:v5:functions:strategy.opentrades.max_drawdown:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.max_drawdown)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку открытой сделки, т.е. максимально возможный убыток в ходе сделки, выраженный в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_drawdown_percent`
`primary:v5:functions:strategy.opentrades.max_drawdown_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.max_drawdown_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальную просадку по открытой сделке, т.е. максимально возможный убыток за время торговли, выраженный в процентах и рассчитываемый по формуле: `Lowest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_runup`
`primary:v5:functions:strategy.opentrades.max_runup:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.max_runup)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по открытой сделке, т.е. максимально возможную прибыль во время сделки, выраженную в [strategy.account_currency](#var_strategy.account_currency).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.max_runup_percent`
`primary:v5:functions:strategy.opentrades.max_runup_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.max_runup_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает максимальный рост по открытой сделке, т.е. максимально возможную прибыль за время торговли, выраженную в процентах и рассчитываемую по формуле: `Highest Value During Trade / (Entry Price x Quantity) * 100`.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.profit`
`primary:v5:functions:strategy.opentrades.profit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.profit)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток по открытой сделке, выраженные в [strategy.account_currency](#var_strategy.account_currency). Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.profit_percent`
`primary:v5:functions:strategy.opentrades.profit_percent:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.profit_percent)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает прибыль/убыток по открытой сделке, выраженные в процентах. Убытки выражаются в виде отрицательных значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.opentrades.size`
`primary:v5:functions:strategy.opentrades.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.opentrades.size)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает направление и число торгуемых контрактов в открытой сделке. Если это значение > 0, рыночная позиция была длинной. Если значение < 0, позиция была короткой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `trade_num` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.order`
`primary:v5:functions:strategy.order:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.order)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series string / simple string / input string / const string | required | не установлено |
| `direction` | series strategy_direction / simple strategy_direction / input strategy_direction / const strategy_direction | required | не установлено |
| `qty` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `limit` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `stop` | series int / simple int / input int / const int / series float / simple float / input float / const float | optional | na |
| `oca_name` | series string / simple string / input string / const string | optional | не установлено |
| `oca_type` | input string / const string | optional | strategy.oca.none |
| `comment` | series string / simple string / input string / const string | optional | не установлено |
| `alert_message` | series string / simple string / input string / const string | optional | не установлено |
| `disable_alert` | series bool / simple bool / input bool / const bool | optional | false |
| `when` | bool | optional | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `strategy.risk.allow_entry_in`
`primary:v5:functions:strategy.risk.allow_entry_in:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.allow_entry_in)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_cons_loss_days`
`primary:v5:functions:strategy.risk.max_cons_loss_days:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.max_cons_loss_days)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | simple int / input int / const int | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_drawdown`
`primary:v5:functions:strategy.risk.max_drawdown:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.max_drawdown)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple int / input int / const int / simple float / input float / const float | required | не установлено |
| `type` | simple string / input string / const string | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.risk.max_intraday_filled_orders`
`primary:v5:functions:strategy.risk.max_intraday_filled_orders:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.max_intraday_filled_orders)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | simple int / input int / const int | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_loss`
`primary:v5:functions:strategy.risk.max_intraday_loss:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.max_intraday_loss)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | simple int / input int / const int / simple float / input float / const float | required | не установлено |
| `type` | simple string / input string / const string | required | не установлено |
| `alert_message` | simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy.risk.max_position_size`
`primary:v5:functions:strategy.risk.max_position_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy.risk.max_position_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `contracts` | simple int / input int / const int / simple float / input float / const float | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.max`
`primary:v5:functions:ta.max:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.max)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение максимума за все время для `source` с начала графика до текущего бара.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ta.min`
`primary:v5:functions:ta.min:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.min)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение минимума за все время для `source` с начала графика до текущего бара.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ta.valuewhen`
`primary:v5:functions:ta.valuewhen:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.valuewhen)

**Тип результата:** `series float`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series int / simple int / input int / const int / series float / simple float / input float / const float | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v5:functions:ta.valuewhen:overload:1` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.valuewhen)

**Тип результата:** `series int`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series int / simple int / input int / const int | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v5:functions:ta.valuewhen:overload:2` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.valuewhen)

**Тип результата:** `series bool`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series bool / simple bool / input bool / const bool | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ta.valuewhen`
`primary:v5:functions:ta.valuewhen:overload:3` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ta.valuewhen)

**Тип результата:** `series color`.
**Описание в сохранённой карточке:** Возвращает значение `source` на баре там, где `condition` — true на n-ном самом недавнем событии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series bool / simple bool / input bool / const bool | required | не установлено |
| `source` | series color / simple color / input color / const color | required | не установлено |
| `occurrence` | simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell`
`primary:v5:functions:table.cell:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | color.black |
| `text_halign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_valign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_size` | series string / simple string / input string / const string | unknown | size.normal |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |
| `text_font_family` | series string / simple string / input string / const string | unknown | font.family_default |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell`
`primary:v5:methods:table.cell:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | color.black |
| `text_halign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_valign` | series string / simple string / input string / const string | unknown | text.align_center |
| `text_size` | series string / simple string / input string / const string | unknown | size.normal |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |
| `text_font_family` | series string / simple string / input string / const string | unknown | font.family_default |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell_set_bgcolor`
`primary:v5:functions:table.cell_set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_bgcolor`
`primary:v5:methods:table.cell_set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_height`
`primary:v5:functions:table.cell_set_height:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_height)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_height`
`primary:v5:methods:table.cell_set_height:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_height)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `height` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text`
`primary:v5:functions:table.cell_set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text`
`primary:v5:methods:table.cell_set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_color`
`primary:v5:functions:table.cell_set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_color`
`primary:v5:methods:table.cell_set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_font_family`
`primary:v5:functions:table.cell_set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_font_family`
`primary:v5:methods:table.cell_set_text_font_family:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_font_family)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_font_family` | series string / simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_halign`
`primary:v5:functions:table.cell_set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_halign`
`primary:v5:methods:table.cell_set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_halign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_size`
`primary:v5:functions:table.cell_set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_size` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_size`
`primary:v5:methods:table.cell_set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_size` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_valign`
`primary:v5:functions:table.cell_set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_valign`
`primary:v5:methods:table.cell_set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `text_valign` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_tooltip`
`primary:v5:functions:table.cell_set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_tooltip`
`primary:v5:methods:table.cell_set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `tooltip` | series string / simple string / input string / const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_width`
`primary:v5:functions:table.cell_set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_width`
`primary:v5:methods:table.cell_set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.cell_set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `column` | series int / simple int / input int / const int | required | не установлено |
| `row` | series int / simple int / input int / const int | required | не установлено |
| `width` | series int / simple int / input int / const int / series float / simple float / input float / const float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.clear`
`primary:v5:functions:table.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | unknown | не установлено |
| `end_row` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.clear`
`primary:v5:methods:table.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | unknown | не установлено |
| `end_row` | series int / simple int / input int / const int | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.delete`
`primary:v5:functions:table.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.delete`
`primary:v5:methods:table.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.merge_cells`
`primary:v5:functions:table.merge_cells:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.merge_cells)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | required | не установлено |
| `end_row` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.merge_cells`
`primary:v5:methods:table.merge_cells:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.merge_cells)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `start_column` | series int / simple int / input int / const int | required | не установлено |
| `start_row` | series int / simple int / input int / const int | required | не установлено |
| `end_column` | series int / simple int / input int / const int | required | не установлено |
| `end_row` | series int / simple int / input int / const int | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.set_bgcolor`
`primary:v5:functions:table.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_bgcolor`
`primary:v5:methods:table.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `bgcolor` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_color`
`primary:v5:functions:table.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_color`
`primary:v5:methods:table.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_width`
`primary:v5:functions:table.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_width`
`primary:v5:methods:table.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `border_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_color`
`primary:v5:functions:table.set_frame_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_frame_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_color`
`primary:v5:methods:table.set_frame_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_frame_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_color` | series color / simple color / input color / const color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_width`
`primary:v5:functions:table.set_frame_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_frame_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_width`
`primary:v5:methods:table.set_frame_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_frame_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `frame_width` | series int / simple int / input int / const int | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_position`
`primary:v5:functions:table.set_position:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_position)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `position` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_position`
`primary:v5:methods:table.set_position:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_table.set_position)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series table | required | не установлено |
| `position` | series string / simple string / input string / const string | required | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ticker.inherit`
`primary:v5:functions:ticker.inherit:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker.inherit)

**Тип результата:** `simple string`.
**Описание в сохранённой карточке:** Составляет идентификатор тикера для указанного `symbol` с дополнительными параметрами, унаследованными от идентификатора тикера, переданного в вызов функции, что позволяет скрипту запрашивать данные по инструменту с использованием тех же модификаторов, что и у `from_tickerid`, включая расширенную сессию, корректировку…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `from_tickerid` | simple string / input string / const string | required | не установлено |
| `symbol` | simple string / input string / const string | required | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

## Версия v4 — 268 записей

### `abs`
`primary:v4:functions:abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_abs)

**Тип результата:** `integer / input integer / const integer / series[integer] / float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Абсолютное значение 'x' — это 'x', если x >= 0, иначе -x.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `acos`
`primary:v4:functions:acos:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_acos)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'acos' возвращает арккосинус (в радианах) числа, таким образом, cos(acos(y)) = y for y in range [-1, 1].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `alert`
`primary:v4:functions:alert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_alert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `message` | series[string] | unknown | не установлено |
| `freq` | string | unknown | alert.freq_once_per_bar |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `alertcondition`
`primary:v4:functions:alertcondition:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_alertcondition)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `alma`
`primary:v4:functions:alma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_alma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Скользящее среднее Арно Легу. Использует распределение Гаусса в качестве весового коэффициента для скользящей средней.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `offset` | float | unknown | не установлено |
| `sigma` | float | unknown | не установлено |
| `floor` | bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.avg`
`primary:v4:functions:array.avg:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.avg)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает среднее элементов массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.clear`
`primary:v4:functions:array.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.concat`
`primary:v4:functions:array.concat:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.concat)

**Тип результата:** `id1`.
**Описание в сохранённой карточке:** Функция объединяет два массива. Она переносит все элементы из второго массива в первый и возвращает первый массив.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id1` | array | unknown | не установлено |
| `id2` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.copy`
`primary:v4:functions:array.copy:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.copy)

**Тип результата:** `float[] / int[] / color[] / bool[] / string[] / line[] / label[]`.
**Описание в сохранённой карточке:** Функция создаёт копию существующего массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.covariance`
`primary:v4:functions:array.covariance:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.covariance)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция возвращает ковариантность двух массивов.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id1` | array | unknown | не установлено |
| `id2` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.fill`
`primary:v4:functions:array.fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float, string, label, line | unknown | не установлено |
| `index_from` | integer | unknown | 0 |
| `index_to` | integer | unknown | na |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.from`
`primary:v4:functions:array.from:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.from)

**Тип результата:** `int[] / bool[] / color[] / float[] / line[] / label[] / box[] / table[] / string[]`.
**Описание в сохранённой карточке:** Функция использует переменное число аргументов с одним из типов: int, float, bool, string, label, line, color, box, table и возвращает массив соответствующего типа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `..args` | **не указан** | unknown | не установлено |
| `arg0, arg1, ...` | const  (const int, float, bool, string, label, line, color, box, table) | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.get`
`primary:v4:functions:array.get:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.get)

**Тип результата:** `series[float] / series[int] / series[color] / series[bool] / series[string] / series[line] / series[label]`.
**Описание в сохранённой карточке:** Функция возвращает значение элемента на указанном индексе.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `index` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.includes`
`primary:v4:functions:array.includes:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.includes)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Функция возвращает 'true', если значение было найдено в массиве. Если нет — возвращает 'false'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.indexof`
`primary:v4:functions:array.indexof:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.indexof)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает индекс первого события значения или -1, если значение не найдено.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.insert`
`primary:v4:functions:array.insert:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.insert)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `index` | integer | unknown | не установлено |
| `value` | float, string, label, line | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.join`
`primary:v4:functions:array.join:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.join)

**Тип результата:** `series[string]`.
**Описание в сохранённой карточке:** Функция создает и возвращает новую строку путем объединения всех элементов массива, разделённых заданной строкой-разделителем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `separator` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.lastindexof`
`primary:v4:functions:array.lastindexof:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.lastindexof)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает индекс последнего события значения или -1, если значение не найдено.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.max`
`primary:v4:functions:array.max:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.max)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает самое большое значение заданного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.median`
`primary:v4:functions:array.median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.median)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает медиану элементов массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.min`
`primary:v4:functions:array.min:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.min)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает наименьшее значение заданного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.mode`
`primary:v4:functions:array.mode:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.mode)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает моду элементов в массиве. Если несколько значений встречаются в массиве с одинаковой частотой, то возвращается меньшее значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_bool`
`primary:v4:functions:array.new_bool:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_bool)

**Тип результата:** `bool[]`.
**Описание в сохранённой карточке:** Функция создаёт новый объект массива элементов логического типа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | bool | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_box`
`primary:v4:functions:array.new_box:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_box)

**Тип результата:** `box[]`.
**Описание в сохранённой карточке:** Функция создаёт новый объект массива элементов типа прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | box | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_color`
`primary:v4:functions:array.new_color:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_color)

**Тип результата:** `color[]`.
**Описание в сохранённой карточке:** Функция создаёт новый объект массива элементов для типов цветов.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | color | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_float`
`primary:v4:functions:array.new_float:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_float)

**Тип результата:** `float[]`.
**Описание в сохранённой карточке:** Функция создает новый объект массива элементов типа float.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | float | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_int`
`primary:v4:functions:array.new_int:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_int)

**Тип результата:** `int[]`.
**Описание в сохранённой карточке:** Функция создает новый объект массива элементов типа int.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | integer | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_label`
`primary:v4:functions:array.new_label:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_label)

**Тип результата:** `label[]`.
**Описание в сохранённой карточке:** Функция создаёт новый объект массива элементов label типа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | label | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_line`
`primary:v4:functions:array.new_line:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_line)

**Тип результата:** `line[]`.
**Описание в сохранённой карточке:** Функция создает новый объект массива элементов типа line.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | line | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_string`
`primary:v4:functions:array.new_string:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_string)

**Тип результата:** `string[]`.
**Описание в сохранённой карточке:** Функция создает новый объект массива элементов типа string.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | string | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.new_table`
`primary:v4:functions:array.new_table:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.new_table)

**Тип результата:** `table[]`.
**Описание в сохранённой карточке:** Функция создаёт новый объект массива элементов типа таблицы.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `size` | integer | unknown | 0 |
| `initial_value` | table | unknown | 'na' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.pop`
`primary:v4:functions:array.pop:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.pop)

**Тип результата:** `series[float] / series[int] / series[color] / series[bool] / series[string] / series[line] / series[label]`.
**Описание в сохранённой карточке:** Эта функция удаляет последний элемент из массива и возвращает его значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.push`
`primary:v4:functions:array.push:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.push)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float, string, label, line | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.range`
`primary:v4:functions:array.range:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.range)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает разницу между мин. и макс. значениями от данного массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.remove`
`primary:v4:functions:array.remove:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.remove)

**Тип результата:** `series[float] / series[int] / series[color] / series[bool] / series[string] / series[line] / series[label]`.
**Описание в сохранённой карточке:** Функция изменяет содержимое массива, удаляя элемент с указанным индексом.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `index` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.reverse`
`primary:v4:functions:array.reverse:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.reverse)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.set`
`primary:v4:functions:array.set:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.set)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `index` | integer | unknown | не установлено |
| `value` | float, string, label, line | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.shift`
`primary:v4:functions:array.shift:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.shift)

**Тип результата:** `series[float] / series[int] / series[color] / series[bool] / series[string] / series[line] / series[label]`.
**Описание в сохранённой карточке:** Функция удаляет первый элемент массива и возвращает его значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.size`
`primary:v4:functions:array.size:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.size)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает число элементов в массиве.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.slice`
`primary:v4:functions:array.slice:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.slice)

**Тип результата:** `array`.
**Описание в сохранённой карточке:** Функция создает вырезку из существующего массива. Если объект из вырезки меняется, изменения применяются и к новому, и к исходному массивам.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `index_from` | integer | unknown | не установлено |
| `index_to` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sort`
`primary:v4:functions:array.sort:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.sort)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `order` | bool | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.standardize`
`primary:v4:functions:array.standardize:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.standardize)

**Тип результата:** `float[] / int[]`.
**Описание в сохранённой карточке:** Функция возвращает массив стандартизированных элементов.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.stdev`
`primary:v4:functions:array.stdev:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.stdev)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает стандартное отклонение элементов массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.sum`
`primary:v4:functions:array.sum:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.sum)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает сумму элементов массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.unshift`
`primary:v4:functions:array.unshift:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.unshift)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |
| `value` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `array.variance`
`primary:v4:functions:array.variance:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_array.variance)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Функция возвращает вариантность элементов массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | array | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `asin`
`primary:v4:functions:asin:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_asin)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'asin' возвращает арксинус (в радианах) числа, таким образом, sin(asin(y)) = y для 'y' в пределах [-1, 1].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `atan`
`primary:v4:functions:atan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_atan)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'atan' возвращает арктангенс (в радианах) числа, таким образом, tan(atan(y)) = y для любого 'y'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `atr`
`primary:v4:functions:atr:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_atr)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция atr (средний истинный диапазон) возвращает RMA истинного диапазона. Истинный диапазон — это max(high - low, abs(high - close[1]), abs(low - close[1])).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `avg`
`primary:v4:functions:avg:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_avg)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Просчитывает среднее всех данных серий (поэлементно).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x1` | **не указан** | unknown | не установлено |
| `x2` | **не указан** | unknown | не установлено |
| `...` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `barcolor`
`primary:v4:functions:barcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_barcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | color | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `title` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `barssince`
`primary:v4:functions:barssince:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_barssince)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Рассчитывает количество баров с момента, когда условие выполнилось последний раз.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bb`
`primary:v4:functions:bb:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_bb)

**Тип результата:** `[series[float], series[float], series[float]]`.
**Описание в сохранённой карточке:** Полосы Боллинджера. Полосы Боллинджера — это инструмент технического анализа, характеризующийся двумя стандартными отклонениями (положительным и отрицательным) от простого скользящего среднего (SMA) цены инструмента, но может быть настроено пользователем.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `mult` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bbw`
`primary:v4:functions:bbw:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_bbw)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Ширина полос Боллинджера. Ширина полос Боллинджера — это разница между верхней и нижней полосами Боллинджера, разделенная средней полосой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `mult` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bgcolor`
`primary:v4:functions:bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `title` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bool`
`primary:v4:functions:bool:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_bool)

**Тип результата:** `const bool / input bool / bool / series[bool]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа bool

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box`
`primary:v4:functions:box:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box)

**Тип результата:** `series[box]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа box.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.delete`
`primary:v4:functions:box.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.get_bottom`
`primary:v4:functions:box.get_bottom:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.get_bottom)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает ценовой уровень нижней границы прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.get_left`
`primary:v4:functions:box.get_left:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.get_left)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает индекс бара или UNIX-время (в зависимости от последнего значения для 'xloc') левой границы прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.get_right`
`primary:v4:functions:box.get_right:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.get_right)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает индекс бара или UNIX-время (в зависимости от последнего значения для 'xloc') правой границы прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.get_top`
`primary:v4:functions:box.get_top:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.get_top)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает ценовой уровень верхней границы прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.new`
`primary:v4:functions:box.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.new)

**Тип результата:** `series[box]`.
**Описание в сохранённой карточке:** Создает новый объект прямоугольника.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `left` | series[integer] | unknown | не установлено |
| `top` | series[float] | unknown | не установлено |
| `right` | series[integer] | unknown | не установлено |
| `bottom` | series[float] | unknown | не установлено |
| `border_color` | series[color] | unknown | color.blue |
| `border_width` | series[integer] | unknown | 1 |
| `border_style` | series[string] | unknown | line.style_solid |
| `extend` | series[string] | unknown | extend.none |
| `xloc` | series[string] | unknown | xloc.bar_index |
| `bgcolor` | series[color] | unknown | color.blue |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `box.set_bgcolor`
`primary:v4:functions:box.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_border_color`
`primary:v4:functions:box.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `color` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_border_style`
`primary:v4:functions:box.set_border_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_border_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `style` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_border_width`
`primary:v4:functions:box.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `width` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_bottom`
`primary:v4:functions:box.set_bottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_bottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `bottom` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_extend`
`primary:v4:functions:box.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `extend` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_left`
`primary:v4:functions:box.set_left:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_left)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `left` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_lefttop`
`primary:v4:functions:box.set_lefttop:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_lefttop)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `left` | series[integer] | unknown | не установлено |
| `top` | series[float] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_right`
`primary:v4:functions:box.set_right:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_right)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `right` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `box.set_rightbottom`
`primary:v4:functions:box.set_rightbottom:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_rightbottom)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `right` | series[integer] | unknown | не установлено |
| `bottom` | series[float] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `box.set_top`
`primary:v4:functions:box.set_top:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_box.set_top)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[box] | unknown | не установлено |
| `top` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cci`
`primary:v4:functions:cci:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_cci)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** CCI (индекс товарного канала) рассчитывается как разница между обычной ценой товара и его простого скользящего среднего, делённого на среднее абсолютное отклонение обычной цены. Индекс масштабируется при помощи обратного коэффициента 0,015, чтобы числа были более читаемыми.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ceil`
`primary:v4:functions:ceil:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_ceil)

**Тип результата:** `integer / input integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Функция ceil возвращает самое маленькое (близкое к отрицательной бесконечности) целое число, которое больше, либо равно аргументу.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `change`
`primary:v4:functions:change:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_change)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Разница между текущим и предыдущим значением, x - x[y].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `cmo`
`primary:v4:functions:cmo:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_cmo)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Моментум-осциллятор Чанде. Рассчитывает разницу между суммой недавних доходов и суммой недавних убытков и делит ее на сумму всех движений цены за один и тот же период.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `cog`
`primary:v4:functions:cog:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_cog)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Индикатор Cog (Центр тяжести) основан на статистике и золотом сечении Фибоначчи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color`
`primary:v4:functions:color:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color)

**Тип результата:** `const color / input color / color / series[color]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа color

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `color.b`
`primary:v4:functions:color.b:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.b)

**Тип результата:** `series[float] / const float / input float`.
**Описание в сохранённой карточке:** Получает значение компонента синего цвета.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.from_gradient`
`primary:v4:functions:color.from_gradient:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.from_gradient)

**Тип результата:** `series[color]`.
**Описание в сохранённой карточке:** Основывается на относительной позиции значения в диапазоне от bottom_value до top_value, функция возвращает цвет градиента, заданного bottom_color и top_color.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | series[float] | unknown | не установлено |
| `bottom_value` | series[float] | unknown | не установлено |
| `top_value` | series[float] | unknown | не установлено |
| `bottom_color` | series[color] | unknown | не установлено |
| `top_color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.g`
`primary:v4:functions:color.g:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.g)

**Тип результата:** `series[float] / const float / input float`.
**Описание в сохранённой карточке:** Получает значение компонента зелёного цвета.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.new`
`primary:v4:functions:color.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.new)

**Тип результата:** `const color / series[color] / input color`.
**Описание в сохранённой карточке:** Функций 'color' применяет заданную прозрачность к выбранному цвету.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | input color | unknown | не установлено |
| `transp` | input float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.r`
`primary:v4:functions:color.r:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.r)

**Тип результата:** `series[float] / const float / input float`.
**Описание в сохранённой карточке:** Получает значение компонента красного цвета.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.rgb`
`primary:v4:functions:color.rgb:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.rgb)

**Тип результата:** `series[color] / const color / input color`.
**Описание в сохранённой карточке:** Создаёт новый цвет с прозрачностью, используя цветовую модель RGB.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `red` | series[float] | unknown | не установлено |
| `green` | series[float] | unknown | не установлено |
| `blue` | series[float] | unknown | не установлено |
| `transp` | series[float] | optional | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color.t`
`primary:v4:functions:color.t:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_color.t)

**Тип результата:** `series[float] / const float / input float`.
**Описание в сохранённой карточке:** Получает прозрачность цвета.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `correlation`
`primary:v4:functions:correlation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_correlation)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Коэффициент корреляции. Описывает степень, на которую две серии стремятся отклониться от своих [sma](#fun_sma) значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source_a` | series[float] | unknown | не установлено |
| `source_b` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cos`
`primary:v4:functions:cos:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_cos)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'cos' возвращает тригонометрический косинус угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `crossover`
`primary:v4:functions:crossover:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_crossover)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Считается, что `x`-серия была пересечена над `y`-серией, если значение `x` больше, чем значение `y`, а значение `x` было меньше, чем значение `y` на баре, непосредственно предшествующем текущему.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | float | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `crossunder`
`primary:v4:functions:crossunder:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_crossunder)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Считается, что `x`-серия была пересечена под `y`-серией, если значение `x` меньше, чем значение `y`, а значение `x` было больше, чем значение `y` на баре, непосредственно предшествующем текущему.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | float | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cum`
`primary:v4:functions:cum:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_cum)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Общая сумма 'x'. То есть это сумма всех элементов 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `dayofmonth`
`primary:v4:functions:dayofmonth:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_dayofmonth)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает день месяца для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v4/essential/sessions-and-time-functions), ссылка составлена по заметкам.

---

### `dayofweek`
`primary:v4:functions:dayofweek:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_dayofweek)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает день недели для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `dev`
`primary:v4:functions:dev:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_dev)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Показатель разницы между серией и её [sma](#fun_sma)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `dividends`
`primary:v4:functions:dividends:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_dividends)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Запрашивает данные по дивидендам для определённого символа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `ticker` | string | unknown | не установлено |
| `field` | string | unknown | dividends.gross |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `lookahead` | bool | unknown | barmerge.lookahead_off |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `dmi`
`primary:v4:functions:dmi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_dmi)

**Тип результата:** `[series[float], series[float], series[float]]`.
**Описание в сохранённой карточке:** Функция dmi возвращает индекс направленного движения.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `diLength` | integer | unknown | не установлено |
| `adxSmoothing` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `earnings`
`primary:v4:functions:earnings:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_earnings)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Запрашивает данные по отчётности для определённого символа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `ticker` | string | unknown | не установлено |
| `field` | string | unknown | earnings.actual |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `lookahead` | bool | unknown | barmerge.lookahead_off |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ema`
`primary:v4:functions:ema:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_ema)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция ema возвращает экспоненциальное взвешенное скользящее среднее. В ema весовые коэффициенты уменьшаются экспоненциально. Считается по формуле: EMA = alpha * x + (1 - alpha) * EMA[1], где alpha = 2 / (y + 1)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `exp`
`primary:v4:functions:exp:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_exp)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'exp' для 'x' — это e^x, где 'x' — аргумент, а 'e' — это число Эйлера.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `falling`
`primary:v4:functions:falling:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_falling)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Проверяет, снижается ли 'x' в течение 'y' баров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `fill`
`primary:v4:functions:fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `hline1` | hline | unknown | не установлено |
| `hline2` | hline | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `editable` | bool | unknown | true |
| `fillgaps` | bool | unknown | false |
| `plot1` | plot | unknown | не установлено |
| `plot2` | plot | unknown | не установлено |
| `show_last` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `financial`
`primary:v4:functions:financial:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_financial)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Запрашивает финансовые данные для символа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `financial_id` | string | unknown | не установлено |
| `period` | string | unknown | не установлено |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `fixnan`
`primary:v4:functions:fixnan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_fixnan)

**Тип результата:** `series[float] / series[integer] / series[bool] / series[color]`.
**Описание в сохранённой карточке:** Для заданной серии заменяет NaN значения на ближайшее предыдущее не NaN значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `float`
`primary:v4:functions:float:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_float)

**Тип результата:** `const float / input float / float / series[float]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа float

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `floor`
`primary:v4:functions:floor:overload:0` · описание по соседней версии (не доказано для этой версии) · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_floor)

**Тип результата:** `integer / input integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Наибольшее целое число, которое меньше, либо равно данному числу.
**Донор:** v5, ID `primary:v5:functions:math.floor:overload:0` — историческая аналогия.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `heikinashi`
`primary:v4:functions:heikinashi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_heikinashi)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Хейкен Аши.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `highest`
`primary:v4:functions:highest:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_highest)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Максимальное значение для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `highestbars`
`primary:v4:functions:highestbars:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_highestbars)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Максимальное значение отступа для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `hline`
`primary:v4:functions:hline:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_hline)

**Тип результата:** `hline`.
**Описание в сохранённой карточке:** Отображает горизонтальную линию на заданном фиксированном ценовом уровне.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `price` | float | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `linestyle` | integer | unknown | не установлено |
| `linewidth` | integer | unknown | 1 |
| `editable` | bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `hma`
`primary:v4:functions:hma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_hma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция hma возвращает Скользящее среднее Хала.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `hour`
`primary:v4:functions:hour:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_hour)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает час для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v4/essential/sessions-and-time-functions), ссылка составлена по заметкам.

---

### `iff`
`primary:v4:functions:iff:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_iff)

**Тип результата:** `bool / integer / float / color / series[float] / series[integer] / series[color] / string / input bool / input integer / input float / input string / input color / const bool / const integer / const float / const string / const color / series[bool] / series[string] / series[line] / series[label] / series[table] / series[box] / array[<array_type>]`.
**Описание в сохранённой карточке:** Если … то … иначе …

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series | unknown | не установлено |
| `then` | series | unknown | не установлено |
| `_else` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `input`
`primary:v4:functions:input:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_input)

**Тип результата:** `input bool / input color / input integer / input float / input string / series[float]`.
**Описание в сохранённой карточке:** Добавляет входной параметр в скрипт вашего индикатора. Пользователь может видеть и редактировать входные параметры в окне настроек индикатора. Входные параметры скрипта выглядят и работают точно так же, как и у встроенных индикаторов технического анализа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `defval` | Its type must match the type defined with the 'type' parameter's value | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `type` | const string | unknown | не установлено |
| `confirm` | const bool | unknown | false |
| `tooltip` | const string | unknown | не установлено |
| `inline` | const string | unknown | не установлено |
| `group` | const string | unknown | не установлено |
| `minval` | const integer, float | unknown | не установлено |
| `maxval` | const integer, float | unknown | не установлено |
| `step` | const integer, float | unknown | 1 |
| `options` | List of constants: [<type>...] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `int`
`primary:v4:functions:int:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_int)

**Тип результата:** `integer / input integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Преобразует значение типа na или значение типа float (отбрасывая дробную часть) к значению типа int

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `kagi`
`primary:v4:functions:kagi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_kagi)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Каги.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `reversal` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `kc`
`primary:v4:functions:kc:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_kc)

**Тип результата:** `[series[float], series[float], series[float]]`.
**Описание в сохранённой карточке:** Канал Кельтнера. Канал Кельтнера — это индикатор технического анализа, показывающий центральную скользящую среднюю линию и линии канала над и под скользящей средней.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `mult` | float | unknown | не установлено |
| `useTrueRange` | bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `kcw`
`primary:v4:functions:kcw:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_kcw)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Ширина каналов Кельтнера. Ширина каналов Кельтнера — это разница между верхним и нижним каналами, разделенными средним каналом.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `mult` | float | unknown | не установлено |
| `useTrueRange` | bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label`
`primary:v4:functions:label:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label)

**Тип результата:** `series[label]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа label

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.delete`
`primary:v4:functions:label.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.get_text`
`primary:v4:functions:label.get_text:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.get_text)

**Тип результата:** `series[string]`.
**Описание в сохранённой карточке:** Возвращает текст этого объекта label.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.get_x`
`primary:v4:functions:label.get_x:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.get_x)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает UNIX-время или индекс бара (в зависимости от последнего заданного значения xloc) позиции этого объекта label.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.get_y`
`primary:v4:functions:label.get_y:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.get_y)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает цену этой позиции объекта label.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.new`
`primary:v4:functions:label.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.new)

**Тип результата:** `series[label]`.
**Описание в сохранённой карточке:** Создаёт новый объект label.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | series | unknown | не установлено |
| `text` | string | unknown | не установлено |
| `xloc` | string | unknown | xloc.bar_index |
| `yloc` | string | unknown | yloc.price |
| `color` | color | unknown | не установлено |
| `style` | string | unknown | label.style_label_down |
| `textcolor` | color | unknown | не установлено |
| `size` | string | unknown | size.normal |
| `textalign` | string | unknown | text.align_center |
| `tooltip` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `label.set_color`
`primary:v4:functions:label.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `color` | color | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_size`
`primary:v4:functions:label.set_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `size` | string | unknown | size.auto |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_style`
`primary:v4:functions:label.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `style` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_text`
`primary:v4:functions:label.set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `text` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textalign`
`primary:v4:functions:label.set_textalign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_textalign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `textalign` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_textcolor`
`primary:v4:functions:label.set_textcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_textcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `textcolor` | color | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_tooltip`
`primary:v4:functions:label.set_tooltip:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_tooltip)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `tooltip` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_x`
`primary:v4:functions:label.set_x:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_x)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xloc`
`primary:v4:functions:label.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `x` | series | unknown | не установлено |
| `xloc` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `label.set_xy`
`primary:v4:functions:label.set_xy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_xy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `x` | series | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_y`
`primary:v4:functions:label.set_y:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_y)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `label.set_yloc`
`primary:v4:functions:label.set_yloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_label.set_yloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | label | unknown | не установлено |
| `yloc` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line`
`primary:v4:functions:line:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line)

**Тип результата:** `series[line]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа line

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.delete`
`primary:v4:functions:line.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.get_price`
`primary:v4:functions:line.get_price:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.get_price)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает уровень цены линии на данном индексе бара.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `line.get_x1`
`primary:v4:functions:line.get_x1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.get_x1)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает UNIX-время или индекс бара (в зависимости от заданного последнего xloc значения) первой точки линии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `line.get_x2`
`primary:v4:functions:line.get_x2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.get_x2)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает UNIX-время или индекс бара (в зависимости от заданного последнего xloc значения) второй точки линии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.get_y1`
`primary:v4:functions:line.get_y1:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.get_y1)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает цену первой точки линии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.get_y2`
`primary:v4:functions:line.get_y2:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.get_y2)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает цену второй точки линии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.new`
`primary:v4:functions:line.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.new)

**Тип результата:** `series[line]`.
**Описание в сохранённой карточке:** Создаёт новый объект линии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x1` | series | unknown | не установлено |
| `y1` | series | unknown | не установлено |
| `x2` | series | unknown | не установлено |
| `y2` | series | unknown | не установлено |
| `xloc` | string | unknown | xloc.bar_index |
| `extend` | string | unknown | extend.none |
| `color` | color | unknown | не установлено |
| `style` | string | unknown | не установлено |
| `width` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `line.set_color`
`primary:v4:functions:line.set_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `color` | color | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_extend`
`primary:v4:functions:line.set_extend:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_extend)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `extend` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_style`
`primary:v4:functions:line.set_style:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_style)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `style` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_width`
`primary:v4:functions:line.set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `width` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_x1`
`primary:v4:functions:line.set_x1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_x1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_x2`
`primary:v4:functions:line.set_x2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_x2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xloc`
`primary:v4:functions:line.set_xloc:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_xloc)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x1` | series | unknown | не установлено |
| `x2` | series | unknown | не установлено |
| `xloc` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `line.set_xy1`
`primary:v4:functions:line.set_xy1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_xy1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x` | series | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_xy2`
`primary:v4:functions:line.set_xy2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_xy2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `x` | series | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_y1`
`primary:v4:functions:line.set_y1:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_y1)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `line.set_y2`
`primary:v4:functions:line.set_y2:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_line.set_y2)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | line | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `linebreak`
`primary:v4:functions:linebreak:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_linebreak)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Линейного прорыва.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `number_of_lines` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `linreg`
`primary:v4:functions:linreg:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_linreg)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Кривая линейной регрессии — это линия, которая лучше всего соответствует ценам за указанный пользователем период времени. Она рассчитывается, используя метод наименьших квадратов. Результат этой функции вычисляется по формуле: linreg = intercept + slope * (length - 1 - offset), где length (длина) — аргумент y, offset …

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `offset` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `log`
`primary:v4:functions:log:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_log)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Натуральным логарифмом любого x > 0 является единственное `y` такое, что, e^y = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `log10`
`primary:v4:functions:log10:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_log10)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Логарифм при основании 10 любого x > 0 является единственным `y`, таким, что 10^y = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `lowest`
`primary:v4:functions:lowest:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_lowest)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Минимальное значение для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `lowestbars`
`primary:v4:functions:lowestbars:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_lowestbars)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Минимальное значение отступа для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `macd`
`primary:v4:functions:macd:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_macd)

**Тип результата:** `[series[float], series[float], series[float]]`.
**Описание в сохранённой карточке:** MACD (схождение/расхождение скользящих средних). Показывает изменение силы, направления, динамики и длительности тренда цены акции.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `fastlen` | integer | unknown | не установлено |
| `slowlen` | integer | unknown | не установлено |
| `siglen` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `max`
`primary:v4:functions:max:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_max)

**Тип результата:** `const integer / input integer / integer / series[integer] / const float / input float / float / series[float]`.
**Описание в сохранённой карточке:** Возвращает большее из нескольких значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x1` | **не указан** | unknown | не установлено |
| `x2` | **не указан** | unknown | не установлено |
| `...` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `max_bars_back`
`primary:v4:functions:max_bars_back:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_max_bars_back)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `var` | series, color, bool | unknown | не установлено |
| `num` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `median`
`primary:v4:functions:median:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_median)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Возвращает медиану серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `mfi`
`primary:v4:functions:mfi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_mfi)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Индекс денежного потока. Индекс денежного потока (MFI) — это технический осциллятор, использующий цену и объем для определения условий перекупленности или перепроданности актива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `min`
`primary:v4:functions:min:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_min)

**Тип результата:** `const integer / input integer / integer / series[integer] / const float / input float / float / series[float]`.
**Описание в сохранённой карточке:** Возвращает меньшее из нескольких значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x1` | **не указан** | unknown | не установлено |
| `x2` | **не указан** | unknown | не установлено |
| `...` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `minute`
`primary:v4:functions:minute:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_minute)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает минуту для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v4/essential/sessions-and-time-functions), ссылка составлена по заметкам.

---

### `mode`
`primary:v4:functions:mode:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_mode)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Возвращает [режим](https://en.wikipedia.org/wiki/Mode_(statistics)) серии. Если есть несколько значений одной и той же частоты, то возвращается меньшее значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `mom`
`primary:v4:functions:mom:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_mom)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Динамика движения цены 'x' и цены 'x' 'y' баров назад. Это просто разница x - x[y].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `month`
`primary:v4:functions:month:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_month)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает месяц для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `na`
`primary:v4:functions:na:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_na)

**Тип результата:** `bool / series[bool]`.
**Описание в сохранённой карточке:** Проверяет, является ли значение NaN.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `nz`
`primary:v4:functions:nz:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_nz)

**Тип результата:** `integer / float / color / bool / series[integer] / series[float] / series[color] / series[bool]`.
**Описание в сохранённой карточке:** Заменяет NaN значения с нулями (или заданным значением) в серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `offset`
`primary:v4:functions:offset:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_offset)

**Тип результата:** `series[bool] / series[color] / series[integer] / series[float]`.
**Описание в сохранённой карточке:** Сдвигает серию 'x' на 'y' баров вправо.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `offset` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `percentile_linear_interpolation`
`primary:v4:functions:percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_percentile_linear_interpolation)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Считает процентиль, используя метод линейной интерполяции между двумя ближайшими рангами.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `percentage` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `percentile_nearest_rank`
`primary:v4:functions:percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_percentile_nearest_rank)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Считает процентиль, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |
| `percentage` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `percentrank`
`primary:v4:functions:percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_percentrank)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Процентный рейтинг — это процент от количества предыдущих значений, которые были меньше или равны текущему значению данной серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `pivothigh`
`primary:v4:functions:pivothigh:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_pivothigh)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Эта функция возвращает цену верхней точки разворота. Возвращает 'NaN', если не было верхней точки разворота.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `leftbars` | series | unknown | не установлено |
| `rightbars` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pivotlow`
`primary:v4:functions:pivotlow:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_pivotlow)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Эта функция возвращает цену нижней точки разворота. Возвращает 'NaN', если не было нижней точки разворота.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `leftbars` | series | unknown | не установлено |
| `rightbars` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plot`
`primary:v4:functions:plot:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plot)

**Тип результата:** `plot`.
**Описание в сохранённой карточке:** Графически изображает серию данных на графике.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `linewidth` | integer | unknown | 1 |
| `style` | integer | unknown | plot.style_line |
| `trackprice` | bool | unknown | false |
| `transp` | integer | unknown | не установлено |
| `histbase` | float | unknown | 0.0 |
| `offset` | integer | unknown | 0 |
| `join` | bool | unknown | false |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotarrow`
`primary:v4:functions:plotarrow:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plotarrow)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `colorup` | series[color] | unknown | не установлено |
| `colordown` | series[color] | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `minheight` | integer | unknown | 5 |
| `maxheight` | integer | unknown | 100 |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotbar`
`primary:v4:functions:plotbar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plotbar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series | unknown | не установлено |
| `high` | series | unknown | не установлено |
| `low` | series | unknown | не установлено |
| `close` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotcandle`
`primary:v4:functions:plotcandle:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plotcandle)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series | unknown | не установлено |
| `high` | series | unknown | не установлено |
| `low` | series | unknown | не установлено |
| `close` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `wickcolor` | series[color] | unknown | не установлено |
| `editable` | bool | unknown | true |
| `show_last` | integer | unknown | не установлено |
| `bordercolor` | series[color] | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotchar`
`primary:v4:functions:plotchar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plotchar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `char` | string | unknown | не установлено |
| `location` | string | unknown | location.abovebar |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `text` | string | unknown | не установлено |
| `textcolor` | color | unknown | не установлено |
| `editable` | bool | unknown | true |
| `size` | string | unknown | size.auto |
| `show_last` | integer | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotshape`
`primary:v4:functions:plotshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_plotshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | string | unknown | не установлено |
| `style` | string | unknown | shape.xcross |
| `location` | string | unknown | location.abovebar |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `text` | string | unknown | не установлено |
| `textcolor` | color | unknown | не установлено |
| `editable` | bool | unknown | true |
| `size` | string | unknown | size.auto |
| `show_last` | integer | unknown | не установлено |
| `display` | integer | unknown | display.all |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pointfigure`
`primary:v4:functions:pointfigure:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_pointfigure)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Крестики-нолики.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `source` | string | unknown | не установлено |
| `style` | string | unknown | не установлено |
| `param` | float | unknown | не установлено |
| `reversal` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pow`
`primary:v4:functions:pow:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_pow)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция математической степени.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `base` | series[float] | unknown | не установлено |
| `exponent` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `quandl`
`primary:v4:functions:quandl:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_quandl)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Запрашивает данные от [quandl](https://www.quandl.com) по символу.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `ticker` | string | unknown | не установлено |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `index` | integer | unknown | не установлено |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `random`
`primary:v4:functions:random:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_random)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает псевдослучайное значение. Функция сгенерирует разную последовательность значений для каждого исполнения скрипта. При использовании одного и того же значения для опционального начального аргумента создаст повторяющийся ряд чисел.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `min` | series[float] | unknown | 0 |
| `max` | series[float] | unknown | 1 |
| `seed` | input integer | optional | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `range`
`primary:v4:functions:range:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_range)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Возвращает разницу между мин. и макс. значениями в серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `renko`
`primary:v4:functions:renko:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_renko)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Ренко.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `style` | string | unknown | не установлено |
| `param` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `rising`
`primary:v4:functions:rising:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_rising)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Проверяет, растёт ли 'x' в течение 'y' баров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `rma`
`primary:v4:functions:rma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_rma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Скользящее среднее, используемое в RSI. Это экспоненциально взвешенное скользящее среднее с alpha = 1 / length.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `roc`
`primary:v4:functions:roc:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_roc)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция roc (скорость изменения цены) показывает разницу между текущим значением 'x' и значением 'x', которое было 'y' дней назад. Считается по формуле: 100 * change(src, length) / src[length].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `round`
`primary:v4:functions:round:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_round)

**Тип результата:** `integer / input integer / const integer / series[integer] / float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Возвращает значение x, округлённое до ближайшего целого числа с округлением в большую по модулю строну. Если используется параметр точности, возвращает плавающее значение, округлённое до заданного количества десятичных знаков.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `number` | **не указан** | unknown | не установлено |
| `precision` | integer | optional | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `round_to_mintick`
`primary:v4:functions:round_to_mintick:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_round_to_mintick)

**Тип результата:** `float / series[float]`.
**Описание в сохранённой карточке:** Возвращает значение, округленное до минитика инструмента, т. е. до ближайшего значения, которое можно разделить на [syminfo.mintick](#var_syminfo.mintick) без остатка с округлением в большую по модулю строну.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `rsi`
`primary:v4:functions:rsi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_rsi)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Индекс относительной силы. Считается на основе rma от восходящих и нисходящих изменений 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | integer, series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sar`
`primary:v4:functions:sar:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sar)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Параболическая система SAR (параболическая остановка и разворот) — это метод, разработанный J. Welles Wilder, Jr., чтобы найти потенциальные изменение направления рыночной цены нужных товаров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `start` | float | unknown | не установлено |
| `inc` | float | unknown | не установлено |
| `max` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `second`
`primary:v4:functions:second:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_second)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает секунду для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `security`
`primary:v4:functions:security:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_security)

**Тип результата:** `series[float] / series[integer] / series[bool] / series[color] / <arg_expr_type>`.
**Описание в сохранённой карточке:** Запросить другой инструмент/интервал

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `resolution` | string | unknown | не установлено |
| `expression` | series[bool], series[integer], series[float], series[color] | unknown | не установлено |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `lookahead` | bool | unknown | barmerge.lookahead_off |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sign`
`primary:v4:functions:sign:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sign)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Сигнум 'x' — это нуль, если 'x' равен нулю, 1.0, если 'x' больше нуля, -1.0, если 'x' меньше нуля.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `sin`
`primary:v4:functions:sin:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sin)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'sin' возвращает тригонометрический синус угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series[float] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `sma`
`primary:v4:functions:sma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция 'sma' возвращает скользящее среднее, то есть сумму последних 'y' значений 'x', делённых на 'y'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `splits`
`primary:v4:functions:splits:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_splits)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Запрашивает данные по сплитам для определённого символа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `ticker` | string | unknown | не установлено |
| `field` | string | unknown | не установлено |
| `gaps` | bool | unknown | barmerge.gaps_off |
| `lookahead` | bool | unknown | barmerge.lookahead_off |
| `ignore_invalid_symbol` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sqrt`
`primary:v4:functions:sqrt:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sqrt)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Квадратный корень любого x >= 0 является единственное y >= 0 такое, что y^2 = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `stdev`
`primary:v4:functions:stdev:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_stdev)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Это смещённая оценка стандартного отклонения.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `stoch`
`primary:v4:functions:stoch:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_stoch)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Стохастик. Считается по формуле: 100 * (close - lowest(low, length)) / (highest(high, length) - lowest(low, length)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `high` | series[float] | unknown | не установлено |
| `low` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `str.format`
`primary:v4:functions:str.format:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_str.format)

**Тип результата:** `string / series[string]`.
**Описание в сохранённой карточке:** Преобразует форматирующую строку и значение(я) в отформатированную строку. Форматирующая строка может содержать текст или место в фигурных скобках {} для каждого значения к форматированию. Каждое такое место состоит из индекса запрошенного аргумента (начиная с 0), который заменит его, и необязательного спецификатора ф…

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `formatString` | series[string] | unknown | не установлено |
| `arg0, arg1, ...` | const integer, float, string, bool, na, series[integer], series[float], series[string], series[bool], series[na], array[series[integer]], array[series[float]], array[series[string]], array[series[bool]] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `str.length`
`primary:v4:functions:str.length:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_str.length)

**Тип результата:** `const integer / integer / series[integer]`.
**Описание в сохранённой карточке:** Возвращает целое число, соответствующее количеству знаков в этой строке.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `string` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `str.replace_all`
`primary:v4:functions:str.replace_all:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_str.replace_all)

**Тип результата:** `string / series[string]`.
**Описание в сохранённой карточке:** Заменяет каждое событие целевой строки в исходной строке замещающей строкой.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[string] | unknown | не установлено |
| `target` | series[string] | unknown | не установлено |
| `replacement` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `str.split`
`primary:v4:functions:str.split:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_str.split)

**Тип результата:** `string[]`.
**Описание в сохранённой карточке:** Делит строку на массив подстрок и возвращает ID этого массива.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `string` | series[string] | unknown | не установлено |
| `separator` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy`
`primary:v4:functions:strategy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | unknown | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `format` | const string | unknown | format.inherit |
| `precision` | const integer | unknown | не установлено |
| `scale` | const integer | unknown | не установлено |
| `pyramiding` | const integer | unknown | 0 |
| `calc_on_order_fills` | const bool | unknown | 'false' |
| `calc_on_every_tick` | const bool | unknown | 'false' |
| `max_bars_back` | const integer | unknown | не установлено |
| `backtest_fill_limits_assumption` | const integer | unknown | не установлено |
| `default_qty_type` | const string | unknown | не установлено |
| `default_qty_value` | const float | unknown | не установлено |
| `initial_capital` | const float | unknown | 100000 |
| `currency` | const string | unknown | не установлено |
| `max_lines_count` | const integer | unknown | 50 |
| `max_labels_count` | const integer | unknown | 50 |
| `slippage` | const integer | unknown | не установлено |
| `commission_type` | const string | unknown | не установлено |
| `commission_value` | const float | unknown | не установлено |
| `process_orders_on_close` | const bool | unknown | 'false' |
| `close_entries_rule` | const string | unknown | 'FIFO' |
| `margin_long` | const integer | unknown | 100 |
| `margin_short` | const integer | unknown | 100 |
| `max_boxes_count` | const integer | unknown | 50 |
| `explicit_plot_zorder` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel`
`primary:v4:functions:strategy.cancel:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.cancel)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[string] | unknown | не установлено |
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel_all`
`primary:v4:functions:strategy.cancel_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.cancel_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close`
`primary:v4:functions:strategy.close:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.close)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[string] | unknown | не установлено |
| `when` | bool | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `qty_percent` | float | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close_all`
`primary:v4:functions:strategy.close_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.close_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `when` | bool | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.entry`
`primary:v4:functions:strategy.entry:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.entry)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[string] | unknown | не установлено |
| `long` | bool | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `limit` | float | unknown | не установлено |
| `stop` | float | unknown | не установлено |
| `oca_name` | string | unknown | не установлено |
| `oca_type` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.exit`
`primary:v4:functions:strategy.exit:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.exit)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[string] | unknown | не установлено |
| `from_entry` | series[string] | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `qty_percent` | float | unknown | не установлено |
| `profit` | float | unknown | 'NaN' |
| `limit` | float | unknown | 'NaN' |
| `loss` | float | unknown | 'NaN' |
| `stop` | float | unknown | 'NaN' |
| `trail_price` | float | unknown | 'NaN' |
| `trail_points` | float | unknown | 'NaN' |
| `trail_offset` | float | unknown | 'NaN' |
| `oca_name` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.order`
`primary:v4:functions:strategy.order:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.order)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | series[string] | unknown | не установлено |
| `long` | bool | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `limit` | float | unknown | не установлено |
| `stop` | float | unknown | не установлено |
| `oca_name` | string | unknown | не установлено |
| `oca_type` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.allow_entry_in`
`primary:v4:functions:strategy.risk.allow_entry_in:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.allow_entry_in)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_cons_loss_days`
`primary:v4:functions:strategy.risk.max_cons_loss_days:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.max_cons_loss_days)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | float | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_drawdown`
`primary:v4:functions:strategy.risk.max_drawdown:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.max_drawdown)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | float | unknown | не установлено |
| `type` | string | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_filled_orders`
`primary:v4:functions:strategy.risk.max_intraday_filled_orders:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.max_intraday_filled_orders)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | float | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_loss`
`primary:v4:functions:strategy.risk.max_intraday_loss:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.max_intraday_loss)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | float | unknown | не установлено |
| `type` | string | unknown | не установлено |
| `alert_message` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_position_size`
`primary:v4:functions:strategy.risk.max_position_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy.risk.max_position_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `contracts` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `string`
`primary:v4:functions:string:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_string)

**Тип результата:** `const string / input string / string / series[string]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа string

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `study`
`primary:v4:functions:study:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_study)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | unknown | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `format` | const string | unknown | format.inherit |
| `precision` | const integer | unknown | не установлено |
| `scale` | const integer | unknown | не установлено |
| `max_bars_back` | const integer | unknown | не установлено |
| `max_lines_count` | const integer | unknown | 50 |
| `max_labels_count` | const integer | unknown | 50 |
| `resolution` | const string | unknown | не установлено |
| `resolution_gaps` | const bool | unknown | true |
| `max_boxes_count` | const integer | unknown | 50 |
| `explicit_plot_zorder` | const bool | unknown | false |
| `linktoseries` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sum`
`primary:v4:functions:sum:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_sum)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция 'sum' возвращает скользящую сумму последних 'y' значений 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `supertrend`
`primary:v4:functions:supertrend:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_supertrend)

**Тип результата:** `[series[float], series[float]]`.
**Описание в сохранённой карточке:** Supertrend индикатор — это индикатор, следующий за трендом.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `factor` | series | unknown | не установлено |
| `atrPeriod` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `swma`
`primary:v4:functions:swma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_swma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Симметрично взвешенное скользящее среднее с фиксированной длиной: 4. Весовые коэффициенты: [1/6, 2/6, 2/6, 1/6].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table`
`primary:v4:functions:table:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table)

**Тип результата:** `series[table]`.
**Описание в сохранённой карточке:** Преобразует значение типа na к значению типа table

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell`
`primary:v4:functions:table.cell:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text` | series[string] | unknown | не установлено |
| `width` | series[float] | unknown | не установлено |
| `height` | series[float] | unknown | не установлено |
| `text_color` | series[color] | unknown | color.black |
| `text_halign` | series[string] | unknown | text.align_center |
| `text_valign` | series[string] | unknown | text.align_center |
| `text_size` | series[string] | unknown | size.normal |
| `bgcolor` | series[color] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `table.cell_set_bgcolor`
`primary:v4:functions:table.cell_set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `bgcolor` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_height`
`primary:v4:functions:table.cell_set_height:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_height)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `height` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text`
`primary:v4:functions:table.cell_set_text:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_text)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text` | series[string] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.cell_set_text_color`
`primary:v4:functions:table.cell_set_text_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_text_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text_color` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_halign`
`primary:v4:functions:table.cell_set_text_halign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_text_halign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text_halign` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_size`
`primary:v4:functions:table.cell_set_text_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_text_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text_size` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_text_valign`
`primary:v4:functions:table.cell_set_text_valign:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_text_valign)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `text_valign` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.cell_set_width`
`primary:v4:functions:table.cell_set_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.cell_set_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `column` | series[integer] | unknown | не установлено |
| `row` | series[integer] | unknown | не установлено |
| `width` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.clear`
`primary:v4:functions:table.clear:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.clear)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `start_column` | series[integer] | unknown | не установлено |
| `start_row` | series[integer] | unknown | не установлено |
| `end_column` | series[integer] | unknown | не установлено |
| `end_row` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.delete`
`primary:v4:functions:table.delete:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.delete)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.new`
`primary:v4:functions:table.new:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.new)

**Тип результата:** `series[table]`.
**Описание в сохранённой карточке:** Функция создает новую таблицу.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `position` | series[string] | unknown | не установлено |
| `columns` | series[integer] | unknown | не установлено |
| `rows` | series[integer] | unknown | не установлено |
| `bgcolor` | series[color] | unknown | не установлено |
| `frame_color` | series[color] | unknown | не установлено |
| `frame_width` | series[integer] | unknown | 0 |
| `border_color` | series[color] | unknown | не установлено |
| `border_width` | series[integer] | unknown | 0 |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `table.set_bgcolor`
`primary:v4:functions:table.set_bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `bgcolor` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_color`
`primary:v4:functions:table.set_border_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_border_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `border_color` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_border_width`
`primary:v4:functions:table.set_border_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_border_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `border_width` | series[integer] | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_color`
`primary:v4:functions:table.set_frame_color:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_frame_color)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `frame_color` | series[color] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_frame_width`
`primary:v4:functions:table.set_frame_width:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_frame_width)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `frame_width` | series[integer] | unknown | 0 |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `table.set_position`
`primary:v4:functions:table.set_position:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_table.set_position)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `table_id` | series[table] | unknown | не установлено |
| `position` | series[string] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tan`
`primary:v4:functions:tan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tan)

**Тип результата:** `float / input float / const float / series[float]`.
**Описание в сохранённой карточке:** Функция 'tan' возвращает тригонометрический тангенс угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series[float] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tickerid`
`primary:v4:functions:tickerid:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tickerid)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса дополнительных данных для скрипта.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `prefix` | string | unknown | не установлено |
| `ticker` | string | unknown | не установлено |
| `session` | string | unknown | не установлено |
| `adjustment` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `time`
`primary:v4:functions:time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_time)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Функция time возвращает UNIX-время текущего бара для указанного интервала и сессии или NaN, если временная точка находится вне сессии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `resolution` | string | unknown | не установлено |
| `session` | string | unknown | не установлено |
| `timezone` | string | unknown | syminfo.timezone |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `time_close`
`primary:v4:functions:time_close:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_time_close)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Функция time_close возвращает UNIX-время закрытия текущего бара для указанного интервала и сессии или NaN, если временная точка находится вне сессии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `resolution` | string | unknown | не установлено |
| `session` | string | unknown | не установлено |
| `timezone` | string | unknown | syminfo.timezone |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `timestamp`
`primary:v4:functions:timestamp:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_timestamp)

**Тип результата:** `const integer / integer / series[integer]`.
**Описание в сохранённой карточке:** Функция 'timestamp' возвращает UNIX-время для указанной даты и времени.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `dateString` | string | unknown | не установлено |
| `year` | integer | unknown | не установлено |
| `month` | integer | unknown | не установлено |
| `day` | integer | unknown | не установлено |
| `hour` | integer | unknown | 0 |
| `minute` | integer | unknown | 0 |
| `second` | integer | unknown | 0 |
| `timezone` | string | unknown | syminfo.timezone |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `todegrees`
`primary:v4:functions:todegrees:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_todegrees)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает приблизительно эквивалентный угол в градусах от угла, измеряемого в радианах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `radians` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tonumber`
`primary:v4:functions:tonumber:overload:0` · редакционная сводка аргументов · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tonumber)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает число типа float, преобразованное из строкового представления целого или дробного числа x. Обработка некорректной строки в этой записи источника не описана.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `toradians`
`primary:v4:functions:toradians:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_toradians)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Возвращает приблизительно эквивалентный угол в радианах от угла, измеряемого в градусах.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `degrees` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tostring`
`primary:v4:functions:tostring:overload:0` · редакционная сводка аргументов · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tostring)

**Тип результата:** `series[string] / string`.
**Описание в сохранённой карточке:** Возвращает строковое представление значения x или элементов переданного массива; формат задаётся необязательным аргументом y.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | integer, float, bool, string, array ID | unknown | не установлено |
| `y` | string | unknown | '#.##########' |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `tr`
`primary:v4:functions:tr:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tr)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** tr(false) — это то же, что и [tr](#var_tr).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `handle_na` | bool | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `tsi`
`primary:v4:functions:tsi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_tsi)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Индекс истинной силы. Использует скользящие средние лежащей в его основе динамики движения финансового инструмента.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `short_length` | integer | unknown | не установлено |
| `long_length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `valuewhen`
`primary:v4:functions:valuewhen:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_valuewhen)

**Тип результата:** `series[float] / series[integer]`.
**Описание в сохранённой карточке:** Значение главной серии в n раз назад, когда условие выполнялось.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | **не указан** | unknown | не установлено |
| `source` | **не указан** | unknown | не установлено |
| `occurrence` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `variance`
`primary:v4:functions:variance:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_variance)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Дисперсия — это математическое ожидание квадратного отклонения серии данных от его среднего значения ([sma](#fun_sma)); оно показывает, как сильно разбросаны числа от их среднего значения.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `vwap`
`primary:v4:functions:vwap:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_vwap)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Взвешенная по объёму средняя цена.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `vwma`
`primary:v4:functions:vwma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_vwma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция vwma возвращает объёмно-взвешенное скользящее среднее от 'x' для 'y' баров назад. То же самое, что: sma(x * volume, y) / sma(volume, y)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `weekofyear`
`primary:v4:functions:weekofyear:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_weekofyear)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает номер недели года для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v4/essential/sessions-and-time-functions), ссылка составлена по заметкам.

---

### `wma`
`primary:v4:functions:wma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_wma)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Функция wma возвращает взвешенное скользящее среднее от 'x' для 'y' баров назад. В wma весовые коэффициенты уменьшаются в арифметической прогрессии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series[float] | unknown | не установлено |
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `wpr`
`primary:v4:functions:wpr:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_wpr)

**Тип результата:** `series[float]`.
**Описание в сохранённой карточке:** Процентный диапазон Вильямса (%R) — это осциллятор, показывающий текущую цену закрытия по отношению к макс. и мин. цене прошлых 'length' баров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `length` | series[integer] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `year`
`primary:v4:functions:year:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v4/#fun_year)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Возвращает год для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи. Перегрузка с timezone использует указанный часовой пояс.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |
| `timezone` | string | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

## Версия v3 — 113 записей

### `abs`
`primary:v3:functions:abs:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_abs)

**Тип результата:** `integer / const integer / float / const float / series`.
**Описание в сохранённой карточке:** Абсолютное значение 'x' — это 'x', если x >= 0, иначе -x.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `acos`
`primary:v3:functions:acos:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_acos)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'acos' возвращает арккосинус (в радианах) числа, таким образом, cos(acos(y)) = y for y in range [-1, 1].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `alertcondition`
`primary:v3:functions:alertcondition:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_alertcondition)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `message` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `alma`
`primary:v3:functions:alma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_alma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Скользящее среднее Арно Легу. Использует распределение Гаусса в качестве весового коэффициента для скользящей средней.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `offset` | float | unknown | не установлено |
| `sigma` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `asin`
`primary:v3:functions:asin:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_asin)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'asin' возвращает арксинус (в радианах) числа, таким образом, sin(asin(y)) = y для 'y' в пределах [-1, 1].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `atan`
`primary:v3:functions:atan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_atan)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'atan' возвращает арктангенс (в радианах) числа, таким образом, tan(atan(y)) = y для любого 'y'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `atr`
`primary:v3:functions:atr:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_atr)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция atr (средний истинный диапазон) возвращает RMA истинного диапазона. Истинный диапазон — это max(high - low, abs(high - close[1]), abs(low - close[1])).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `avg`
`primary:v3:functions:avg:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_avg)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Просчитывает среднее всех данных серий (поэлементно).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |
| `y` | **не указан** | unknown | не установлено |
| `z` | **не указан** | unknown | не установлено |
| `a` | **не указан** | unknown | не установлено |
| `b` | **не указан** | unknown | не установлено |
| `c` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `barcolor`
`primary:v3:functions:barcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_barcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | color | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |
| `title` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `barssince`
`primary:v3:functions:barssince:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_barssince)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Рассчитывает количество баров с момента, когда условие выполнилось последний раз.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `bgcolor`
`primary:v3:functions:bgcolor:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_bgcolor)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |
| `title` | const string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `cci`
`primary:v3:functions:cci:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_cci)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** CCI (индекс товарного канала) рассчитывается как разница между обычной ценой товара и его простого скользящего среднего, делённого на среднее абсолютное отклонение обычной цены. Индекс масштабируется при помощи обратного коэффициента 0,015, чтобы числа были более читаемыми.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `ceil`
`primary:v3:functions:ceil:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_ceil)

**Тип результата:** `integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Функция ceil возвращает самое маленькое (близкое к отрицательной бесконечности) целое число, которое больше, либо равно аргументу.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `change`
`primary:v3:functions:change:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_change)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Разница между текущим и предыдущим значением, x - x[y].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cog`
`primary:v3:functions:cog:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_cog)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Индикатор Cog (Центр тяжести) основан на статистике и золотом сечении Фибоначчи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `color`
`primary:v3:functions:color:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_color)

**Тип результата:** `color`.
**Описание в сохранённой карточке:** Функций 'color' применяет заданную прозрачность к выбранному цвету.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `color` | color | unknown | не установлено |
| `transp` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `correlation`
`primary:v3:functions:correlation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_correlation)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Коэффициент корреляции. Описывает степень, на которую две серии стремятся отклониться от своих [sma](#fun_sma) значений.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source_a` | series | unknown | не установлено |
| `source_b` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cos`
`primary:v3:functions:cos:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_cos)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'cos' возвращает тригонометрический косинус угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cross`
`primary:v3:functions:cross:overload:0` · описание по соседней версии (не доказано для этой версии) · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_cross)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Возвращает 1, если два ряда пересеклись, иначе 0.
**Донор:** v2, ID `wiki:v2:functions:cross` — историческая аналогия.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `crossover`
`primary:v3:functions:crossover:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_crossover)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Считается, что `x`-серия была пересечена над `y`-серией, если значение `x` больше, чем значение `y`, а значение `x` было меньше, чем значение `y` на баре, непосредственно предшествующем текущему.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | float | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `crossunder`
`primary:v3:functions:crossunder:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_crossunder)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Считается, что `x`-серия была пересечена под `y`-серией, если значение `x` меньше, чем значение `y`, а значение `x` было больше, чем значение `y` на баре, непосредственно предшествующем текущему.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | float | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `cum`
`primary:v3:functions:cum:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_cum)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Общая сумма 'x'. То есть это сумма всех элементов 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `dayofmonth`
`primary:v3:functions:dayofmonth:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_dayofmonth)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает день месяца для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v3/essential/sessions-and-time-functions/), ссылка составлена по заметкам.

---

### `dayofweek`
`primary:v3:functions:dayofweek:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_dayofweek)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает день недели для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `dev`
`primary:v3:functions:dev:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_dev)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Показатель разницы между серией и её [sma](#fun_sma)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `ema`
`primary:v3:functions:ema:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_ema)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция sma возвращает экспоненциальное взвешенное скользящее среднее. В ema весовые коэффициенты уменьшаются экспоненциально. Считается по формуле: EMA = alpha * x + (1 - alpha) * EMA[1], где alpha = 2 / (y + 1)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `exp`
`primary:v3:functions:exp:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_exp)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'exp' для 'x' — это e^x, где 'x' — аргумент, а 'e' — это число Эйлера.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `falling`
`primary:v3:functions:falling:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_falling)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Проверяет, снижается ли 'x' в течение 'y' баров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `fill`
`primary:v3:functions:fill:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_fill)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `hline1` | hline | unknown | не установлено |
| `hline2` | hline | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `plot1` | plot | unknown | не установлено |
| `plot2` | plot | unknown | не установлено |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `fixnan`
`primary:v3:functions:fixnan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_fixnan)

**Тип результата:** `series / series[integer] / series[bool] / series[color]`.
**Описание в сохранённой карточке:** Для заданной серии заменяет NaN значения на ближайшее предыдущее не NaN значение.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `floor`
`primary:v3:functions:floor:overload:0` · описание по соседней версии (не доказано для этой версии) · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_floor)

**Тип результата:** `integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Возвращает наибольшее математически целое значение, не большее аргумента. Тип результата — float. Для результата типа integer используйте `round`.
**Донор:** v2, ID `wiki:v2:functions:floor` — историческая аналогия.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `heikinashi`
`primary:v3:functions:heikinashi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_heikinashi)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Хейкен Аши.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `highest`
`primary:v3:functions:highest:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_highest)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Максимальное значение для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series, integer | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `highestbars`
`primary:v3:functions:highestbars:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_highestbars)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Максимальное значение отступа для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series, integer | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `hline`
`primary:v3:functions:hline:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_hline)

**Тип результата:** `hline`.
**Описание в сохранённой карточке:** Отображает горизонтальную линию на заданном фиксированном ценовом уровне.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `price` | float | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | const color | unknown | не установлено |
| `linestyle` | integer | unknown | не установлено |
| `linewidth` | integer | unknown | 1 |
| `editable` | const bool | unknown | true |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `hour`
`primary:v3:functions:hour:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_hour)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает час для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v3/essential/sessions-and-time-functions/), ссылка составлена по заметкам.

---

### `iff`
`primary:v3:functions:iff:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_iff)

**Тип результата:** `bool / integer / float / color / series / series[integer] / series[color] / string / const bool / const integer / const float / const string / const color / series[bool]`.
**Описание в сохранённой карточке:** Если … то … иначе …

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | series | unknown | не установлено |
| `then` | series | unknown | не установлено |
| `_else` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `input`
`primary:v3:functions:input:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_input)

**Тип результата:** `bool / integer / float / string / series`.
**Описание в сохранённой карточке:** Добавляет входной параметр в скрипт вашего индикатора. Пользователь может видеть и редактировать входные параметры в окне настроек индикатора. Входные параметры скрипта выглядят и работают точно так же, как и у встроенных индикаторов технического анализа.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `defval` | Depends on 'type' argument | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `type` | const string | unknown | не установлено |
| `confirm` | bool | unknown | false |
| `minval` | integer, float | unknown | не установлено |
| `maxval` | integer, float | unknown | не установлено |
| `step` | integer, float | unknown | 1 |
| `options` | List of constants: [<type>...] | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `kagi`
`primary:v3:functions:kagi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_kagi)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Каги.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `source` | string | unknown | не установлено |
| `reversal` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `linebreak`
`primary:v3:functions:linebreak:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_linebreak)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Линейного прорыва.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `source` | string | unknown | не установлено |
| `number_of_lines` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `linreg`
`primary:v3:functions:linreg:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_linreg)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Кривая линейной регрессии — это линия, которая лучше всего соответствует ценам за указанный пользователем период времени. Она рассчитывается, используя метод наименьших квадратов. Результат этой функции вычисляется по формуле: linreg = intercept + slope * (length - 1 - offset), где length (длина) — аргумент y, offset …

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `offset` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `log`
`primary:v3:functions:log:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_log)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Натуральным логарифмом любого x > 0 является единственное `y` такое, что, e^y = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `log10`
`primary:v3:functions:log10:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_log10)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Логарифм при основании 10 любого x > 0 является единственным `y`, таким, что 10^y = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `lowest`
`primary:v3:functions:lowest:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_lowest)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Минимальное значение для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series, integer | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `lowestbars`
`primary:v3:functions:lowestbars:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_lowestbars)

**Тип результата:** `series[integer]`.
**Описание в сохранённой карточке:** Минимальное значение отступа для указанного количества баров назад.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series, integer | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `macd`
`primary:v3:functions:macd:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_macd)

**Тип результата:** `[series, series, series]`.
**Описание в сохранённой карточке:** MACD (схождение/расхождение скользящих средних). Показывает изменение силы, направления, динамики и длительности тренда цены акции.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `fastlen` | integer | unknown | не установлено |
| `slowlen` | integer | unknown | не установлено |
| `siglen` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `max`
`primary:v3:functions:max:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_max)

**Тип результата:** `const integer / integer / series[integer] / const float / float / series`.
**Описание в сохранённой карточке:** Возвращает большее из двух значений

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |
| `y` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `min`
`primary:v3:functions:min:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_min)

**Тип результата:** `const integer / integer / series[integer] / const float / float / series`.
**Описание в сохранённой карточке:** Возвращает меньшее из двух значений

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |
| `y` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `minute`
`primary:v3:functions:minute:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_minute)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает минуту для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v3/essential/sessions-and-time-functions/), ссылка составлена по заметкам.

---

### `mom`
`primary:v3:functions:mom:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_mom)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Динамика движения цены 'x' и цены 'x' 'y' баров назад. Это просто разница x - x[y].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `month`
`primary:v3:functions:month:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_month)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает месяц для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `na`
`primary:v3:functions:na:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_na)

**Тип результата:** `bool / series[bool]`.
**Описание в сохранённой карточке:** Проверяет, является ли значение NaN.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `nz`
`primary:v3:functions:nz:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_nz)

**Тип результата:** `integer / float / color / bool / series[integer] / series[bool] / series[color] / series`.
**Описание в сохранённой карточке:** Заменяет NaN значения с нулями (или заданным значением) в серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `offset`
`primary:v3:functions:offset:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_offset)

**Тип результата:** `series[bool] / series[color] / series[integer] / series`.
**Описание в сохранённой карточке:** Сдвигает серию 'x' на 'y' баров вправо.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `offset` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `percentile_linear_interpolation`
`primary:v3:functions:percentile_linear_interpolation:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_percentile_linear_interpolation)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Считает процентиль, используя метод линейной интерполяции между двумя ближайшими рангами.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `percentage` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `percentile_nearest_rank`
`primary:v3:functions:percentile_nearest_rank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_percentile_nearest_rank)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Считает процентиль, используя метод ближайшего ранга.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |
| `percentage` | float | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `percentrank`
`primary:v3:functions:percentrank:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_percentrank)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Процентный рейтинг — это процент от количества предыдущих значений, которые были меньше или равны текущему значению данной серии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `pivothigh`
`primary:v3:functions:pivothigh:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_pivothigh)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Эта функция возвращает цену верхней точки разворота. Возвращает 'NaN', если не было верхней точки разворота.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `leftbars` | series | unknown | не установлено |
| `rightbars` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pivotlow`
`primary:v3:functions:pivotlow:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_pivotlow)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Эта функция возвращает цену нижней точки разворота. Возвращает 'NaN', если не было нижней точки разворота.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `leftbars` | series | unknown | не установлено |
| `rightbars` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plot`
`primary:v3:functions:plot:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plot)

**Тип результата:** `plot`.
**Описание в сохранённой карточке:** Графически изображает серию данных на графике.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `linewidth` | integer | unknown | 1 |
| `style` | integer | unknown | line |
| `trackprice` | bool | unknown | false |
| `transp` | integer | unknown | не установлено |
| `histbase` | float | unknown | 0.0 |
| `offset` | integer | unknown | 0 |
| `join` | bool | unknown | false |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotarrow`
`primary:v3:functions:plotarrow:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plotarrow)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `colorup` | color | unknown | не установлено |
| `colordown` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `minheight` | integer | unknown | 5 |
| `maxheight` | integer | unknown | 100 |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotbar`
`primary:v3:functions:plotbar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plotbar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series | unknown | не установлено |
| `high` | series | unknown | не установлено |
| `low` | series | unknown | не установлено |
| `close` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotcandle`
`primary:v3:functions:plotcandle:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plotcandle)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `open` | series | unknown | не установлено |
| `high` | series | unknown | не установлено |
| `low` | series | unknown | не установлено |
| `close` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `color` | color | unknown | не установлено |
| `wickcolor` | color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `show_last` | const integer | unknown | не установлено |
| `bordercolor` | color | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotchar`
`primary:v3:functions:plotchar:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plotchar)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `char` | string | unknown | не установлено |
| `location` | string | unknown | location.abovebar |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `text` | string | unknown | не установлено |
| `textcolor` | color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `plotshape`
`primary:v3:functions:plotshape:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_plotshape)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `series` | series | unknown | не установлено |
| `title` | const string | unknown | не установлено |
| `style` | string | unknown | shape.xcross |
| `location` | string | unknown | location.abovebar |
| `color` | color | unknown | не установлено |
| `transp` | integer | unknown | не установлено |
| `offset` | integer | unknown | 0 |
| `text` | string | unknown | не установлено |
| `textcolor` | color | unknown | не установлено |
| `editable` | const bool | unknown | true |
| `size` | const string | unknown | size.auto |
| `show_last` | const integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pointfigure`
`primary:v3:functions:pointfigure:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_pointfigure)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Крестики-нолики.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `source` | string | unknown | не установлено |
| `style` | string | unknown | не установлено |
| `param` | float | unknown | не установлено |
| `reversal` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `pow`
`primary:v3:functions:pow:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_pow)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция математической степени.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `base` | series | unknown | не установлено |
| `exponent` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `renko`
`primary:v3:functions:renko:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_renko)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса значений для Ренко.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `source` | string | unknown | не установлено |
| `style` | string | unknown | не установлено |
| `param` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `rising`
`primary:v3:functions:rising:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_rising)

**Тип результата:** `series[bool]`.
**Описание в сохранённой карточке:** Проверяет, растёт ли 'x' в течение 'y' баров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `rma`
`primary:v3:functions:rma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_rma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Скользящее среднее, используемое в RSI. Это экспоненциально взвешенное скользящее среднее с alpha = 1 / length.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `roc`
`primary:v3:functions:roc:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_roc)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция roc (скорость изменения цены) показывает разницу между текущим значением 'x' и значением 'x', которое было 'y' дней назад. Считается по формуле: 100 * change(src, length) / src[length].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `round`
`primary:v3:functions:round:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_round)

**Тип результата:** `integer / const integer / series[integer]`.
**Описание в сохранённой карточке:** Функция round возвращает значение аргумента, округлённого до ближайшего целого числа с округлением в большую по модулю строну.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `rsi`
`primary:v3:functions:rsi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_rsi)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Индекс относительной силы. Считается на основе rma от восходящих и нисходящих изменений 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |
| `y` | integer, series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sar`
`primary:v3:functions:sar:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sar)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Параболическая система SAR (параболическая остановка и разворот) — это метод, разработанный J. Welles Wilder, Jr., чтобы найти потенциальные изменение направления рыночной цены нужных товаров.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `start` | float | unknown | не установлено |
| `inc` | float | unknown | не установлено |
| `max` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `second`
`primary:v3:functions:second:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_second)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает секунду для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `security`
`primary:v3:functions:security:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_security)

**Тип результата:** `series[integer] / series / series[bool] / series[color]`.
**Описание в сохранённой карточке:** Запросить другой инструмент/интервал

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `symbol` | string | unknown | не установлено |
| `resolution` | string | unknown | не установлено |
| `expression` | series | unknown | не установлено |
| `gaps` | const bool | unknown | barmerge.gaps_off |
| `lookahead` | const bool | unknown | barmerge.lookahead_off |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sign`
`primary:v3:functions:sign:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sign)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Сигнум 'x' — это нуль, если 'x' равен нулю, 1.0, если 'x' больше нуля, -1.0, если 'x' меньше нуля.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `sin`
`primary:v3:functions:sin:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sin)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'sin' возвращает тригонометрический синус угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `sma`
`primary:v3:functions:sma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция 'sma' возвращает скользящее среднее, то есть сумму последних 'y' значений 'x', делённых на 'y'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sqrt`
`primary:v3:functions:sqrt:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sqrt)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Квадратный корень любого x >= 0 является единственное y >= 0 такое, что y^2 = x

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `stdev`
`primary:v3:functions:stdev:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_stdev)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Это смещённая оценка стандартного отклонения.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `stoch`
`primary:v3:functions:stoch:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_stoch)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Стохастик. Считается по формуле: 100 * (close - lowest(low, length)) / (highest(high, length) - lowest(low, length)).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `high` | series | unknown | не установлено |
| `low` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `strategy`
`primary:v3:functions:strategy:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | unknown | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `precision` | const integer | unknown | 4 |
| `scale` | const integer | unknown | не установлено |
| `pyramiding` | const integer | unknown | 0 |
| `calc_on_order_fills` | const bool | unknown | 'false' |
| `calc_on_every_tick` | const bool | unknown | 'false' |
| `max_bars_back` | const integer | unknown | не установлено |
| `backtest_fill_limits_assumption` | const integer | unknown | не установлено |
| `default_qty_type` | const string | unknown | не установлено |
| `default_qty_value` | const float | unknown | не установлено |
| `initial_capital` | **не указан** | unknown | не установлено |
| `currency` | const string | unknown | не установлено |
| `slippage` | const integer | unknown | не установлено |
| `commission_type` | const string | unknown | не установлено |
| `commission_value` | const float | unknown | не установлено |
| `linktoseries` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel`
`primary:v3:functions:strategy.cancel:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.cancel)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.cancel_all`
`primary:v3:functions:strategy.cancel_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.cancel_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close`
`primary:v3:functions:strategy.close:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.close)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | string | unknown | не установлено |
| `when` | bool | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.close_all`
`primary:v3:functions:strategy.close_all:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.close_all)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `when` | bool | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.entry`
`primary:v3:functions:strategy.entry:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.entry)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | string | unknown | не установлено |
| `long` | bool | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `limit` | float | unknown | не установлено |
| `stop` | float | unknown | не установлено |
| `oca_name` | string | unknown | не установлено |
| `oca_type` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.exit`
`primary:v3:functions:strategy.exit:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.exit)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | string | unknown | не установлено |
| `from_entry` | string | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `qty_percent` | float | unknown | не установлено |
| `profit` | float | unknown | 'NaN' |
| `limit` | float | unknown | 'NaN' |
| `loss` | float | unknown | 'NaN' |
| `stop` | float | unknown | 'NaN' |
| `trail_price` | float | unknown | 'NaN' |
| `trail_points` | float | unknown | 'NaN' |
| `trail_offset` | float | unknown | 'NaN' |
| `oca_name` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.order`
`primary:v3:functions:strategy.order:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.order)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `id` | string | unknown | не установлено |
| `long` | bool | unknown | не установлено |
| `qty` | float | unknown | 'NaN' |
| `limit` | float | unknown | не установлено |
| `stop` | float | unknown | не установлено |
| `oca_name` | string | unknown | не установлено |
| `oca_type` | string | unknown | не установлено |
| `comment` | string | unknown | не установлено |
| `when` | bool | unknown | 'true' |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.allow_entry_in`
`primary:v3:functions:strategy.risk.allow_entry_in:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.allow_entry_in)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_cons_loss_days`
`primary:v3:functions:strategy.risk.max_cons_loss_days:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.max_cons_loss_days)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_drawdown`
`primary:v3:functions:strategy.risk.max_drawdown:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.max_drawdown)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | float | unknown | не установлено |
| `type` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_filled_orders`
`primary:v3:functions:strategy.risk.max_intraday_filled_orders:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.max_intraday_filled_orders)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `count` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_intraday_loss`
`primary:v3:functions:strategy.risk.max_intraday_loss:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.max_intraday_loss)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `value` | float | unknown | не установлено |
| `type` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `strategy.risk.max_position_size`
`primary:v3:functions:strategy.risk.max_position_size:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_strategy.risk.max_position_size)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `contracts` | float | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `study`
`primary:v3:functions:study:overload:0` · void по сигнатуре · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_study)

**Тип результата:** `void`.
**Описание в сохранённой карточке:** Не возвращает значение (void); действие функции описано выше.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `title` | const string | unknown | не установлено |
| `shorttitle` | const string | unknown | не установлено |
| `overlay` | const bool | unknown | false |
| `precision` | const integer | unknown | 4 |
| `scale` | const integer | unknown | не установлено |
| `max_bars_back` | const integer | unknown | не установлено |
| `linktoseries` | const bool | unknown | false |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `sum`
`primary:v3:functions:sum:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_sum)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция 'sum' возвращает скользящую сумму последних 'y' значений 'x'.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `swma`
`primary:v3:functions:swma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_swma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Симметрично взвешенное скользящее среднее с фиксированной длиной: 4. Весовые коэффициенты: [1/6, 2/6, 2/6, 1/6].

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `tan`
`primary:v3:functions:tan:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_tan)

**Тип результата:** `float / const float / series`.
**Описание в сохранённой карточке:** Функция 'tan' возвращает тригонометрический тангенс угла.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tickerid`
`primary:v3:functions:tickerid:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_tickerid)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Создаёт идентификатор тикера для запроса дополнительных данных для скрипта.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `prefix` | string | unknown | не установлено |
| `ticker` | string | unknown | не установлено |
| `session` | string | unknown | не установлено |
| `adjustment` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `time`
`primary:v3:functions:time:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_time)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция 'time' возвращает UNIX-время текущего бара для заданного интервала и сессии, либо NaN, если момент времени находится вне сессии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `resolution` | string | unknown | не установлено |
| `session` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `timestamp`
`primary:v3:functions:timestamp:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_timestamp)

**Тип результата:** `integer`.
**Описание в сохранённой карточке:** Функция 'timestamp' возвращает UNIX-время для указанной даты и времени.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `year` | integer | unknown | не установлено |
| `month` | integer | unknown | не установлено |
| `day` | integer | unknown | не установлено |
| `hour` | integer | unknown | не установлено |
| `minute` | integer | unknown | не установлено |
| `second` | integer | unknown | 0 |
| `timezone` | string | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `tostring`
`primary:v3:functions:tostring:overload:0` · редакционная сводка аргументов · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_tostring)

**Тип результата:** `string`.
**Описание в сохранённой карточке:** Возвращает строковое представление числа x; формат задаётся необязательным аргументом y.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | float | unknown | не установлено |
| `y` | string | unknown | '#.##########' |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `tr`
`primary:v3:functions:tr:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_tr)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** tr(false) — это то же, что и [tr](#var_tr).

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `handle_na` | bool | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_occurrence`), не проверялся компилятором.

---

### `tsi`
`primary:v3:functions:tsi:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_tsi)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Индекс истинной силы. Использует скользящие средние лежащей в его основе динамики движения финансового инструмента.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `short_length` | integer | unknown | не установлено |
| `long_length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `valuewhen`
`primary:v3:functions:valuewhen:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_valuewhen)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Значение главной серии в n раз назад, когда условие выполнялось.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `condition` | **не указан** | unknown | не установлено |
| `source` | **не указан** | unknown | не установлено |
| `occurrence` | **не указан** | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `variance`
`primary:v3:functions:variance:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_variance)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Дисперсия — это математическое ожидание квадратного отклонения серии данных от его среднего значения ([sma](#fun_sma)); оно показывает, как сильно разбросаны числа от их среднего значения.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `vwap`
`primary:v3:functions:vwap:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_vwap)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Взвешенная по объёму средняя цена.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `x` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

### `vwma`
`primary:v3:functions:vwma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_vwma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция vwma возвращает объёмно-взвешенное скользящее среднее от 'x' для 'y' баров назад. То же самое, что: sma(x * volume, y) / sma(volume, y)

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `weekofyear`
`primary:v3:functions:weekofyear:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_weekofyear)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает номер недели года для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** в каталоге отсутствует; [упоминание в документации](https://www.tradingview.com/pine-script-docs/v3/essential/sessions-and-time-functions/), ссылка составлена по заметкам.

---

### `wma`
`primary:v3:functions:wma:overload:0` · общее описание функции · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_wma)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Функция wma возвращает взвешенное скользящее среднее от 'x' для 'y' баров назад. В wma весовые коэффициенты уменьшаются в арифметической прогрессии.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `source` | series | unknown | не установлено |
| `length` | integer | unknown | не установлено |

**Пример:** код есть в сохранённом каталоге (`source_example`), не проверялся компилятором.

---

### `year`
`primary:v3:functions:year:overload:0` · редакционная сводка руководства · [Источник](https://www.tradingview.com/pine-script-reference/v3/#fun_year)

**Тип результата:** `series`.
**Описание в сохранённой карточке:** Возвращает год для переданной временной метки UNIX. По умолчанию календарные значения определяются в часовом поясе биржи.

| Параметр | Тип в этой версии | Обязательность | Значение по умолчанию |
|---|---|---|---|
| `time` | series | unknown | не установлено |

**Пример:** только схематический вызов (не исполняемый пример).

---

