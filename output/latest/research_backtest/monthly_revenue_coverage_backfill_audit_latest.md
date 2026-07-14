# Monthly Revenue Coverage / Backfill Audit

- generated_at: `2026-07-14 16:14:28 Asia/Taipei`
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
| canonical_monthly_revenue_history | history_found | 26 | 202405 | 202606 | 0 |  |  | True | False | signal_scope_not_evaluated_in_history_row |
| monthly_revenue_point_in_time_panel | panel_found | 2 | 202605 | 202606 | 0 |  |  | False | True | coverage_limited_candidate_snapshot_observed_values_not_full_market_history |
| daily_model_signal_log_all_models | signal_rows_found | 26 | 202405 | 202606 | 10960 | 99.58 | 99.27 | True | False |  |
| model:price_pullback_23ema | signal_rows_found | 26 | 202405 | 202606 | 3750 | 99.28 | 99.26 | True | False |  |
| model:revenue_unreacted_range | signal_rows_found | 26 | 202405 | 202606 | 2821 | 100.00 | 100.00 | True | False |  |
| model:hot_theme_pullback | signal_rows_found | 26 | 202405 | 202606 | 1043 | 100.00 | 100.00 | True | False |  |
| model:pullback_short_reclaim | signal_rows_found | 26 | 202405 | 202606 | 2102 | 99.10 | 99.26 | True | False |  |
| model:tdcc_short_term_continuation_d5_d10 | signal_rows_found | 26 | 202405 | 202606 | 587 | 100.00 | 100.00 | True | False |  |
| model:tdcc_stealth_accumulation | signal_rows_found | 26 | 202405 | 202606 | 555 | 100.00 | 100.00 | True | False |  |
| model:volume_range_breakout_v2_high_position_volume_attack | signal_rows_found | 26 | 202405 | 202606 | 7 | 100.00 | 100.00 | True | False |  |
| model:volume_range_breakout_v2_low_position_volume_attack | signal_rows_found | 26 | 202405 | 202606 | 6 | 100.00 | 100.00 | True | False |  |
| model:w_bottom_right_side | signal_rows_found | 26 | 202405 | 202606 | 89 | 100.00 | 100.00 | True | False |  |

## Target Models

| model_id | signal_rows | signal_date_min | signal_date_max | asof_covered_rows | asof_row_coverage_pct | missing_asof_rows | formal_model_revenue_gate_ready | backfill_recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| price_pullback_23ema | 3750 | 20260529 | 20260713 | 3723 | 99.28 | 0 | True | no_backfill_required_for_this_scope |
| revenue_unreacted_range | 2821 | 20260529 | 20260713 | 2821 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| hot_theme_pullback | 1043 | 20260601 | 20260713 | 1043 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| pullback_short_reclaim | 2102 | 20260529 | 20260713 | 2083 | 99.10 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_short_term_continuation_d5_d10 | 587 | 20260529 | 20260713 | 587 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| tdcc_stealth_accumulation | 555 | 20260529 | 20260605 | 555 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| volume_range_breakout_v2_high_position_volume_attack | 7 | 20260709 | 20260713 | 7 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| volume_range_breakout_v2_low_position_volume_attack | 6 | 20260708 | 20260713 | 6 | 100.00 | 0 | True | no_backfill_required_for_this_scope |
| w_bottom_right_side | 89 | 20260529 | 20260713 | 89 | 100.00 | 0 | True | no_backfill_required_for_this_scope |

## Detail Sample

| signal_date | model_id | stock_id | coverage_status | matched_revenue_period | matched_source_table_date | blocker_reason |
| --- | --- | --- | --- | --- | --- | --- |
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
| 20260529 | price_pullback_23ema | 2371 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2374 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2379 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2385 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2388 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2392 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2402 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2412 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2413 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2417 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2419 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
| 20260529 | price_pullback_23ema | 2421 | ready_asof_history_row | 202604 | 20260517 | coverage row exists but formal gate still requires sufficient history coverage audit |
