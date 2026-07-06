# Monthly Revenue Coverage / Backfill Audit

- generated_at: `2026-07-06 17:42:23 Asia/Taipei`
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
| daily_model_signal_log_all_models | signal_rows_found | 25 | 202405 | 202605 | 10257 | 99.48 | 99.04 | True | False |  |
| model:price_pullback_23ema | signal_rows_found | 25 | 202405 | 202605 | 3501 | 99.23 | 99.25 | True | False |  |
| model:revenue_unreacted_range | signal_rows_found | 25 | 202405 | 202605 | 2102 | 100.00 | 100.00 | True | False |  |
| model:hot_theme_pullback | signal_rows_found | 25 | 202405 | 202605 | 808 | 100.00 | 100.00 | True | False |  |
| model:near_high_neckline_challenge | signal_rows_found | 25 | 202405 | 202605 | 36 | 100.00 | 100.00 | True | False |  |
| model:platform_strengthening | signal_rows_found | 25 | 202405 | 202605 | 33 | 100.00 | 100.00 | True | False |  |
| model:pullback_short_reclaim | signal_rows_found | 25 | 202405 | 202605 | 1671 | 98.98 | 99.19 | True | False |  |
| model:tdcc_short_term_continuation_d5_d10 | signal_rows_found | 25 | 202405 | 202605 | 491 | 100.00 | 100.00 | True | False |  |
| model:tdcc_stealth_accumulation | signal_rows_found | 25 | 202405 | 202605 | 555 | 100.00 | 100.00 | True | False |  |
| model:volume_range_breakout | signal_rows_found | 25 | 202405 | 202605 | 989 | 99.09 | 98.93 | True | False |  |
| model:w_bottom_right_side | signal_rows_found | 25 | 202405 | 202605 | 71 | 100.00 | 100.00 | True | False |  |

## Target Models

| model_id | signal_rows | signal_date_min | signal_date_max | asof_covered_rows | asof_row_coverage_pct | missing_asof_rows | formal_model_revenue_gate_ready | backfill_recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| price_pullback_23ema | 3501 | 20260529 | 20260706 | 3474 | 99.23 | 0 | True | no_backfill_required_for_this_scope |
| revenue_unreacted_range | 2102 | 20260529 | 20260706 | 2102 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| hot_theme_pullback | 808 | 20260601 | 20260706 | 808 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| near_high_neckline_challenge | 36 | 20260529 | 20260624 | 36 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| platform_strengthening | 33 | 20260529 | 20260624 | 33 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| pullback_short_reclaim | 1671 | 20260529 | 20260706 | 1654 | 98.98 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_short_term_continuation_d5_d10 | 491 | 20260529 | 20260706 | 491 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_stealth_accumulation | 555 | 20260529 | 20260605 | 555 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| volume_range_breakout | 989 | 20260529 | 20260706 | 980 | 99.09 | 0 | True | no_backfill_required_for_this_scope |
| w_bottom_right_side | 71 | 20260529 | 20260706 | 71 | 100.00 | 0 | True | no_backfill_required_for_this_scope |

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
