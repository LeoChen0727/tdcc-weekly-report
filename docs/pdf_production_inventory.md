# PDF Production Inventory

Scope: repository-owned PDF producers, validators, and publishers. This file is a production boundary document. It does not define stock selection, model parameters, scoring, ranking, or operation guidance.

## Official Producers

| Purpose | Producer | Validator | Publisher / Exposure |
| --- | --- | --- | --- |
| ChatGPT-side daily six-PDF deliverables | `scripts/run_chatgpt_daily_report_entrypoint.py` -> `scripts/generate_chatgpt_side_daily_reports.py` | `scripts/validate_chatgpt_side_pdf_contract.py`, `scripts/validate_chatgpt_side_pdf_layout_independence.py`, `scripts/validate_chatgpt_side_volume_operation_pdf_integration.py` | User-selected output directory only. These PDFs are not produced by Daily Full Pipeline and are not published to `docs/latest`. |
| Daily repo market source artifacts | `build_daily_market_report_artifacts.py` | `scripts/validate_daily_production_boundaries.py`, `scripts/validate_daily_report_source_preflight.py`, `scripts/validate_daily_staged_paths.py` | `output/latest` and `output/history/reports` only. These are source/reference artifacts and must not be presented as completed ChatGPT-side daily recommendation PDFs. |
| TDCC weekly candidate reports | `scripts/build_tdcc_weekly_candidate_reports.py` | `scripts/validate_tdcc_weekly_candidate_reports.py`, `scripts/validate_pdf_facing_display_text.py` | `output/latest`, `output/history`, and `docs/latest` through `tdcc_weekly.yml`. |
| Market risk/background dashboard | `scripts/build_market_regime_dashboard.py` | `scripts/validate_market_regime_dashboard.py` | `output/latest` only in daily production. It may be cited as structured background but must not be published to `docs/latest` as a daily recommendation PDF. |
| Warrant market auxiliary report | `scripts/build_warrant_market_report.py` | `tests/test_warrant_market_report_fallback.py` and daily freshness validation | `output/latest` only in daily production. It may be cited as structured background but must not be published to `docs/latest` as a daily recommendation PDF. |
| Daily signal performance reports | `scripts/generate_daily_signal_performance_report.py` | `scripts/validate_daily_signal_performance.py` | Research/backtest-owned performance output. It is not a daily recommendation PDF. |
| Individual stock report | `scripts/generate_individual_stock_report.py` | `scripts/validate_individual_stock_outputs.py` | `docs/latest/individual_stock_reports/` through individual-stock workflows. It is not a daily full-market report. |

## Publisher Inventory

| Publisher | Owns | Must Not Do |
| --- | --- | --- |
| `.github/workflows/daily_full_pipeline.yml` | Daily source data, packet, rules, current README, source/reference artifacts | Must not publish retired fixed daily PDFs or repo artifact daily PDFs to `docs/latest`. Must not publish warrant/market-risk PDFs as daily recommendation PDFs. |
| `publish_chatgpt_report_readme_and_check.py` | README entrypoints, packet/rules copies, publish checks | Must not expose retired fixed daily PDF links. Must keep only the current `main_price_date` date-stamped README in `docs/latest`. |
| `.github/workflows/tdcc_weekly.yml` | TDCC weekly PDFs and TDCC weekly Pages artifacts | Must not publish daily recommendation PDFs. |
| `.github/workflows/research_backtest_pipeline.yml` | Research/backtest and signal performance artifacts | Must not mutate production daily model parameters or publish daily recommendation PDFs. |
| `.github/workflows/individual_stock_report.yml` and `.github/workflows/individual_stock_data_refresh.yml` | Individual-stock data and per-stock report artifacts | Must not publish daily full-market recommendation PDFs. |
| `.github/workflows/pages.yml` | Deploys existing `docs/` content | Must not create or transform PDFs. |

## Retired Daily PDF Paths

The old root-level daily recommendation PDF aliases are retired and must not be
regenerated, linked from packet/README, staged for public Pages, or restored as
formal daily recommendation PDFs. Active guidance must describe them by category
instead of publishing their exact filenames, so new report conversations cannot
copy a retired path as the current deliverable.

## Repo Artifact Daily PDFs

These files may exist only as repo source/reference artifacts. They are not final ChatGPT-side deliverables and must not be copied or linked as public `docs/latest` daily recommendation PDFs.

Human-facing daily market PDFs are date-stamped published reports under `output/latest/published_reports/daily_market/`. The date segment must come from `output/latest/data_freshness_latest.csv` field `main_price_date`, not from wall-clock runtime.

| File | Current role | Lifecycle status |
| --- | --- | --- |
| `output/latest/daily_market_summary_latest.pdf` | compatibility_alias for packet/raw-health consumers | must_keep_until_packet_and_raw_health_consumers_move |
| `output/latest/daily_market_full_latest.pdf` | compatibility_alias for packet/raw-health consumers | must_keep_until_packet_and_raw_health_consumers_move |
| `output/latest/published_reports/daily_market/每日全市場候選股監測報告_精華版_YYYYMMDD.pdf` | published_human_pdf generated from the daily market summary PDF | published_date_stamped_daily_market_pdf |
| `output/latest/published_reports/daily_market/完整候選股清單_完整版_YYYYMMDD.pdf` | published_human_pdf generated from the daily market full PDF | published_date_stamped_daily_market_pdf |

The legacy root Chinese PDFs `output/latest/每日全市場候選股監測報告_精華版.pdf` and `output/latest/完整候選股清單_完整版表格.pdf` are retired. They must not be regenerated, retained in `output/latest` root, or restored as compatibility aliases. Retiring the English compatibility aliases requires a later reviewed PR that first moves packet/raw-health consumers.

## Auxiliary Internal PDFs

These files may exist in `output/latest` for internal source/reference use. Daily production must not publish them to `docs/latest` as daily recommendation PDFs:

- `warrant_market_report_latest.pdf`
- `market_risk_dashboard_latest.pdf`

## Enforced Validator

`scripts/validate_pdf_production_inventory.py` is the executable gate for this inventory. It must fail closed when:

- a retired fixed daily PDF producer or validator file returns;
- a retired daily PDF filename appears in Daily Full Pipeline, README publisher, packet builder, current README, packet, or `docs/latest`;
- a repo artifact daily PDF or auxiliary internal PDF is published under `docs/latest`;
- `output/latest` or `docs/latest` keeps stale date-stamped daily README files from dates other than the current `main_price_date`;
- `docs/latest` contains root-level PDF filenames outside the approved public set.
