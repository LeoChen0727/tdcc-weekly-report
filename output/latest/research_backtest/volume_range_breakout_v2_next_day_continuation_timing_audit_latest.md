# Volume Range Breakout V2 Next-Day Continuation Timing Audit

- research_id: `volume_range_breakout_v2_next_day_continuation_timing_audit`
- artifact_version: `volume_range_breakout_v2_next_day_continuation_timing_audit_20260708`
- source_research_id: `volume_range_breakout_v2_semantic_audit`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This timing audit is research-only and does not change `stock_model_contract_registry.csv`.
- `next_day_continuation` is not known at signal-date close; it is known after the next trading day close.
- Because formal entry is `confirmation_next_open`, the condition is available before the formal buy open in this sample.
- The audit checks date impact separately from performance; no row uses post-entry information.

## Timing Availability

| sample_size | known_before_entry_open_count | known_before_entry_open_rate_pct | future_leak_count | status | value_a | value_b | value_c |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1369 | 1369 | 100.0 | 0 | timing_verified_research_only | information_cutoff=confirmation_date_close | entry_rule=confirmation_next_open | not_known_on_signal_date_close |

## 20/40/60 High-Window Timing Rows

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | known_before_entry_open_rate_pct | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| previous_20d_high_next_day_continuation | 1369 | 49.01 | 50.33 | 3.2892 | -0.2169 | 100.0 | timing_verified_research_only |
| previous_40d_high_next_day_continuation | 1022 | 50.68 | 48.83 | 4.0508 | 0.4626 | 100.0 | timing_verified_research_only |
| previous_60d_high_next_day_continuation | 798 | 52.51 | 46.99 | 5.0304 | 1.4049 | 100.0 | timing_verified_research_only |

## Selected Trigger Breakdown

| audit_key | sample_size | known_before_entry_open_rate_pct | selected_other_same_confirmation_count | would_change_confirmation_date_count | would_change_entry_date_count | status |
| --- | --- | --- | --- | --- | --- | --- |
| next_day_break_signal_high_confirmed | 1343 | 100.0 | 1343 | 0 | 0 | selected_trigger_is_date_equivalent |
| pullback_5ma_confirmed | 26 | 100.0 | 26 | 0 | 0 | selected_trigger_is_date_equivalent |

## Operation Date Impact

| sample_size | known_before_entry_open_count | would_change_confirmation_date_count | would_change_entry_date_count | status | value_c |
| --- | --- | --- | --- | --- | --- |
| 1369 | 1369 | 0 | 0 | does_not_change_current_confirmation_or_entry_dates | formal_entry_remains_confirmation_next_open |

## Future-Leak Check

| sample_size | known_before_entry_open_count | future_leak_count | status | value_a | value_b | value_c |
| --- | --- | --- | --- | --- | --- | --- |
| 1369 | 1369 | 0 | no_future_leak_detected | uses_post_entry_information=False | known_before_entry_open=True | confirmation_age_trading_days=1 |

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_next_day_continuation_timing_audit_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_next_day_continuation_timing_audit_detail_latest.csv`
- detail_rows: `1369`
