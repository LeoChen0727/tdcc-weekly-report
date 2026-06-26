# W-Bottom Early-Entry Backfill Feasibility Audit

- generated_at: `2026-06-26 23:51:16 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_data_coverage_audit`
- production impact: `none`
- scope: research/backtest data governance only.
- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, daily_full_pipeline, or GitHub Actions triggers.
- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.

## Conclusion

- can extend with repo-existing data: `true`
- max signal start with repo-existing data: `20240930`
- status: `completed_approved_official_price_backfill`
- required external source: `completed official TWSE MI_INDEX and TPEx DAILY_CLOSE_quotes backfill`
- required action: `completed_official_price_backfill_rebuild_stock_price_history_and_w_bottom_outputs`
- required follow-up owner: `research_backtest_data_governance`

## Current Data Window

| daily_price_min_date | daily_price_max_date | daily_price_unique_dates | price_history_file_count | price_history_files_ge_180 | earliest_180th_observed_date | status |
| --- | --- | --- | --- | --- | --- | --- |
| 20240102 | 20260626 | 595 | 2389 | 2020 | 20240930 | extended_after_approved_official_price_backfill |

## Supporting Artifacts

| audit_item_id | source_artifact | status | finding |
| --- | --- | --- | --- |
| stock_price_history_manifest | output/latest/stock_price_history_manifest.csv | available | Manifest documents current per-stock price history paths and date ranges. |
| w_bottom_data_coverage_audit | output/latest/research_backtest/w_bottom_early_entry_data_coverage_audit_latest.md | available | W-bottom coverage audit records the extended price coverage and signal window after approved backfill. |
| stock_price_history_builder | scripts/build_stock_price_history.py | available | Rebuilds per-stock history after daily price files exist; this run rebuilt history after approved pre-20250407 backfill. |
| range_repair_backfill_script | scripts/repair_daily_price_range.py | available | Fetched approved historical date ranges through the official TWSE/TPEx price fetcher; non-trading/no-target-source dates were not written. |
| official_price_backfill_script | backfill_official_daily_price.py | available | Manual backfill helper uses a rolling 420 calendar-day lookback and does not extend earlier than the current repo start for this audit. |
| price_history_continuity_validator | scripts/validate_daily_price_history_continuity.py | available | Validates recent daily price/history continuity, not full historical W-bottom research coverage by itself. |
| w_bottom_coverage_validator | scripts/validate_w_bottom_early_entry_data_coverage_audit.py | available | Validates the existing research-only W-bottom coverage audit and blocks accidental production decision fields. |

## Handoff

- Do not promote W-bottom early-entry variants from this evidence window.
- Do not write research variants or recommendations into the production baseline.
- Approved historical official price backfill, `scripts/build_stock_price_history.py`, W-bottom research rebuilds, and coverage validation have completed for available official trading dates.
- Remaining promotion blockers belong to research stability/mature-sample review, not to the original 20250407 price-history start.
- Keep PR #194 draft until a separate promotion or production sync is explicitly requested.
