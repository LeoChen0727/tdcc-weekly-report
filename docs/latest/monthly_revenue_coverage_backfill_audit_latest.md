# Monthly Revenue Coverage / Backfill Audit

- generated_at: `2026-07-04 21:04:00 Asia/Taipei`
- audit_id: `monthly_revenue_coverage_backfill_audit`
- audit_version: `coverage_backfill_audit_v1`
- formal_model_revenue_gate_ready: `True`
- formal_scope_backfill_required: `False`
- candidate_snapshot_pit_panel_full_market_ready: `False`
- rule: canonical monthly revenue joins require `source_table_date <= signal_date`.
- rule: candidate snapshot PIT revenue is coverage-limited and cannot be used as full-market historical backfill.

## Coverage Summary

| scope | source_status | history_revenue_period_count | history_revenue_period_min | history_revenue_period_max | signal_rows | asof_row_coverage_pct | asof_stock_coverage_pct | formal_model_revenue_gate_ready | backfill_required | blocker_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canonical_monthly_revenue_history | history_found | 25 | 202405 | 202605 | 0 |  |  | True | False | signal_scope_not_evaluated_in_history_row |
| monthly_revenue_point_in_time_panel | panel_found | 1 | 202605 | 202605 | 0 |  |  | False | True | coverage_limited_candidate_snapshot_observed_values_not_full_market_history |
| daily_model_signal_log_all_models | signal_rows_found | 25 | 202405 | 202605 | 10074 | 99.44 | 99.04 | True | False |  |
| model:price_pullback_23ema | signal_rows_found | 25 | 202405 | 202605 | 3677 | 99.18 | 99.27 | True | False |  |
| model:revenue_unreacted_range | signal_rows_found | 25 | 202405 | 202605 | 1943 | 100.00 | 100.00 | True | False |  |
| model:hot_theme_pullback | signal_rows_found | 25 | 202405 | 202605 | 755 | 100.00 | 100.00 | True | False |  |
| model:near_high_neckline_challenge | signal_rows_found | 25 | 202405 | 202605 | 36 | 100.00 | 100.00 | True | False |  |
| model:platform_strengthening | signal_rows_found | 25 | 202405 | 202605 | 33 | 100.00 | 100.00 | True | False |  |
| model:pullback_short_reclaim | signal_rows_found | 25 | 202405 | 202605 | 1587 | 98.93 | 99.16 | True | False |  |
| model:tdcc_short_term_continuation_d5_d10 | signal_rows_found | 25 | 202405 | 202605 | 458 | 100.00 | 100.00 | True | False |  |
| model:tdcc_stealth_accumulation | signal_rows_found | 25 | 202405 | 202605 | 555 | 100.00 | 100.00 | True | False |  |
| model:volume_range_breakout | signal_rows_found | 25 | 202405 | 202605 | 965 | 99.07 | 98.92 | True | False |  |
| model:w_bottom_right_side | signal_rows_found | 25 | 202405 | 202605 | 65 | 100.00 | 100.00 | True | False |  |

## Target Models

| model_id | signal_rows | signal_date_min | signal_date_max | asof_covered_rows | asof_row_coverage_pct | missing_asof_rows | formal_model_revenue_gate_ready | backfill_recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| price_pullback_23ema | 3677 | 20260529 | 20260703 | 3647 | 99.18 | 0 | True | no_backfill_required_for_this_scope |
| revenue_unreacted_range | 1943 | 20260529 | 20260703 | 1943 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| hot_theme_pullback | 755 | 20260601 | 20260703 | 755 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| near_high_neckline_challenge | 36 | 20260529 | 20260624 | 36 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| platform_strengthening | 33 | 20260529 | 20260624 | 33 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| pullback_short_reclaim | 1587 | 20260529 | 20260703 | 1570 | 98.93 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_short_term_continuation_d5_d10 | 458 | 20260529 | 20260703 | 458 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_stealth_accumulation | 555 | 20260529 | 20260605 | 555 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| volume_range_breakout | 965 | 20260529 | 20260703 | 956 | 99.07 | 0 | True | no_backfill_required_for_this_scope |
| w_bottom_right_side | 65 | 20260529 | 20260703 | 65 | 100.00 | 0 | True | no_backfill_required_for_this_scope |

## Detail Sample

| signal_date | model_id | stock_id | coverage_status | matched_revenue_period | matched_source_table_date | blocker_reason |
| --- | --- | --- | --- | --- | --- | --- |
| 20260529 | near_high_neckline_challenge | 8103 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | near_high_neckline_challenge | 1808 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | near_high_neckline_challenge | 2645 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | near_high_neckline_challenge | 2850 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | near_high_neckline_challenge | 4739 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 2328 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 3023 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 3515 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 1210 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 1808 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 2646 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | platform_strengthening | 4306 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1471 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1514 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1519 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1536 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1597 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1608 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1612 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1616 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 1717 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2323 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2330 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2340 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2345 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2347 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2354 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2365 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2367 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2368 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
