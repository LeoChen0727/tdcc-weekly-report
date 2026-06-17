# Daily PDF Template Independence Inventory

Scope: daily production PDF template/layout independence only. This document does not authorize changes to stock models, scoring, ranking, selection logic, research/backtest logic, or `output/latest/*.csv`.

## PDF Template Scope

The scope is every repo code path that owns a PDF template or renderer, not the
number of already-generated PDF artifacts in `output/` or `docs/`.

Current PDF template entrypoints are:

- Warrant market: `scripts/build_warrant_market_report.py::write_pdf`
- Market risk/background: `scripts/build_market_regime_dashboard.py::build_pdf`
- TDCC weekly highlight: `scripts/build_tdcc_weekly_candidate_reports.py::write_tdcc_weekly_highlight_pdf`
- TDCC weekly full: `scripts/build_tdcc_weekly_candidate_reports.py::write_tdcc_weekly_full_pdf`
- Individual stock report: `scripts/generate_individual_stock_report.py::build_pdf`
- Signal performance weekly: `scripts/generate_daily_signal_performance_report.py::write_weekly_signal_performance_pdf_from_markdown`
- Signal performance monthly: `scripts/generate_daily_signal_performance_report.py::write_monthly_signal_performance_pdf_from_markdown`
- ChatGPT-side mainstream curated: `scripts/generate_chatgpt_side_daily_reports.py::build_mainstream_curated_pdf`
- ChatGPT-side mainstream full: `scripts/generate_chatgpt_side_daily_reports.py::build_mainstream_full_candidate_pdf`
- ChatGPT-side non-mainstream curated: `scripts/generate_chatgpt_side_daily_reports.py::build_non_mainstream_curated_pdf`
- ChatGPT-side non-mainstream full: `scripts/generate_chatgpt_side_daily_reports.py::build_non_mainstream_full_candidate_pdf`
- ChatGPT-side warrant auxiliary: `scripts/generate_chatgpt_side_daily_reports.py::build_warrant_market_auxiliary_pdf`
- ChatGPT-side market risk/background: `scripts/generate_chatgpt_side_daily_reports.py::build_market_risk_background_pdf`

## Retired Fixed Daily Market PDF Path

The old fixed daily market PDF generator path has been retired from formal
delivery and public `docs/latest` publishing. It must not be restored as the
ChatGPT-side daily recommendation PDF source.

Retired outputs:

- old `output/latest/daily_market_*` fixed daily market PDF aliases
- old root-level mainstream / non-mainstream daily recommendation PDF aliases

Formal daily recommendation PDFs must be generated through:

- `scripts/run_chatgpt_daily_report_entrypoint.py`
- `scripts/generate_chatgpt_side_daily_reports.py`

## Shared Paths That Must Not Own Report Layout

The following shared paths are allowed only as low-level utilities. They must not choose sections, table columns, report line, row limits, model interpretation, or operation blocks:

- Font registration and page setup helpers.
- Pure text cleanup / display-token normalization.
- Raw PDF table construction primitives when the caller supplies all columns, widths, and rows.
- File loading helpers that do not filter by report semantics.

The following shared paths are risky if a formal PDF builder calls them directly, because a single edit can silently change multiple PDFs:

- Generic stock-PDF dispatchers such as `build_model_line_pdf(report_line, full, ...)`.
- Shared model loop helpers that decide report line, model order, section order, or per-section limits.
- Shared table-row renderers for model summary/detail tables.
- Shared stock-card renderers for highlight PDFs.
- Shared appendix renderers for event-watch and group-rotation sections.
- TDCC weekly PDF writers that accept `report_kind` to switch highlight/full layout.
- Signal performance PDF writers shared by weekly/monthly outputs.

## Required Independence Rule

Each multi-output PDF family must have its own renderer namespace or function set
per output for:

- Main PDF builder entrypoint.
- Model loop and section iteration.
- Summary table rows.
- Detail table rows.
- Highlight stock-card renderer, when applicable.
- Event-watch appendix renderer.
- Group-rotation appendix renderer.

`volume_range_breakout` must not be rendered through the general model-hit table path when its operation adapter section is present. Its PDF display must come from its own operation section and must read `buy_rank_eligible` for buy-rank eligibility.

New-listed and consecutive/repeated-listed candidates must remain separate tables or separately headed sections, not one mixed table with a status column.
