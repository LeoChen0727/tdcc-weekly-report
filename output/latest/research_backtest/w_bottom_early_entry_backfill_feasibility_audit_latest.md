# W-Bottom Early-Entry Backfill Feasibility Audit

- generated_at: `2026-06-26 19:03:08 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_data_coverage_audit`
- production impact: `none`
- scope: research/backtest data governance only.
- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, daily_full_pipeline, or GitHub Actions triggers.
- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.

## Conclusion

- can extend with repo-existing data: `false`
- max signal start with repo-existing data: `20260105`
- status: `blocked_requires_external_price_backfill`
- required external source: `TWSE MI_INDEX daily OHLCV; TPEx DAILY_CLOSE_quotes daily OHLCV`
- required action: `formal historical price backfill decision before rebuilding W-bottom research outputs`
- required follow-up owner: `research_backtest_data_governance`

## Current Data Window

| daily_price_min_date | daily_price_max_date | daily_price_unique_dates | price_history_file_count | price_history_files_ge_180 | earliest_180th_observed_date | status |
| --- | --- | --- | --- | --- | --- | --- |
| 20250407 | 20260624 | 294 | 2373 | 1054 | 20260105 | blocked_existing_data_window |

## Supporting Artifacts

| audit_item_id | source_artifact | status | finding |
| --- | --- | --- | --- |
| stock_price_history_manifest | output/latest/stock_price_history_manifest.csv | available | Manifest documents current per-stock price history paths and date ranges. |
| w_bottom_data_coverage_audit | output/latest/research_backtest/w_bottom_early_entry_data_coverage_audit_latest.md | available | Existing W-bottom coverage audit records 20250407 to 20260624 price coverage and 20260105 signal start. |
| stock_price_history_builder | scripts/build_stock_price_history.py | available | Can rebuild per-stock history after daily price files exist; it does not create pre-20250407 source data by itself. |
| range_repair_backfill_script | scripts/repair_daily_price_range.py | available | Can fetch selected date ranges through the official price fetcher, but earlier 2025 requires an approved external-source backfill run. |
| official_price_backfill_script | backfill_official_daily_price.py | available | Manual backfill helper uses a rolling 420 calendar-day lookback and does not extend earlier than the current repo start for this audit. |
| price_history_continuity_validator | scripts/validate_daily_price_history_continuity.py | available | Validates recent daily price/history continuity, not full historical W-bottom research coverage by itself. |
| w_bottom_coverage_validator | scripts/validate_w_bottom_early_entry_data_coverage_audit.py | available | Validates the existing research-only W-bottom coverage audit and blocks accidental production decision fields. |

## Handoff

- Do not promote W-bottom early-entry variants from this evidence window.
- Do not write research variants or recommendations into the production baseline.
- A real extension requires approved historical official price backfill before `20250407`, then `scripts/build_stock_price_history.py`, W-bottom research rebuilds, and coverage validation.
- Keep PR #194 draft until a separate promotion or production sync is explicitly requested.
