# Pine Script Reference Wiki

[Открыть вики / Open the wiki](https://s7cret.github.io/pine-wiki/)

A bilingual Russian/English reference for Pine Script v1–v6, with search,
version comparisons, source attribution, and JSON export. The site is static
and can also be opened locally through `index.html`.

- [Русский интерфейс](https://s7cret.github.io/pine-wiki/?lang=ru)
- [English interface](https://s7cret.github.io/pine-wiki/?lang=en)
- [Документация, запуск и ограничения](README_RU.md)
- [Pine v6 semantic profile](spec/index.html) · [offline consumer / bundle](docs/SEMANTIC_PROFILE.md)
- [Приёмка ТЗ v2](docs/AUDIT_V2_2026-10-20.md)
- [Проверки качества](QA_REPORT.md)
- [Источники и права](THIRD_PARTY.md)

GitHub Pages serves the `main` branch from the repository root. The `.nojekyll`
file keeps the static files unchanged. Updates are published after a push to
`main`; GitHub Actions also runs the repository's validation suite.

Pine Wiki is unofficial and is not affiliated with or endorsed by TradingView.
The project's own application and tooling code is licensed under [MIT](LICENSE).
Third-party documentation, examples, snapshots, and derived translations retain
their separate terms; see [NOTICE](NOTICE) and [THIRD_PARTY.md](THIRD_PARTY.md).
