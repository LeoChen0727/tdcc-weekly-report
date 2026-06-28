# Structured Neckline Selected Exit Loss Diagnostics

- generated_at: `2026-06-29 01:00:59 Asia/Taipei`
- research_id: `structured_neckline_selected_exit_loss_diagnostics`
- selected_exit_rule_comparison_id: `tp10_close_with_5pct_pullback_neutral`
- research_selection_reason: `close_based_exit_selected_intraday_price_not_repeatable_rule`
- sample_size: `23`
- loss_count: `5`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Interpretation

- This audit compares the five selected-rule losses against the remaining win/neutral rows.
- Diagnostic flags are candidate failure features only; they are not production filters.
- The strongest next step is manual chart review of the five loss rows before promoting any additional exclusion.

## Cohort Summary

| diagnostic_cohort | sample_size | mixed_context_count | bullish_context_count | median_selected_return_pct | median_selected_mfe_pct | median_selected_mae_pct | median_visual_pre_signal_return_pct | median_visual_pre_signal_range_pct | median_base_width_pct | median_low_position_120_pct | top_diagnostic_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| selected_rule_loss | 5 | 3 | 2 | -14.5756 | 5.5794 | -18.2403 | 1.7065 | 66.6667 | 20.5970 | 50.1089 | below_success_p25_selected_mfe_pct:5;below_success_p25_selected_mae_pct:4;large_adverse_move_mae_below_minus10pct:4;wide_base_over_20pct:4;below_success_p25_base_age_sessions:3 |
| selected_rule_success_or_neutral | 18 | 8 | 8 | 4.7219 | 11.5902 | -3.7174 | 7.1143 | 49.4622 | 23.8603 | 36.2927 | wide_base_over_20pct:11;wide_support_pair_span_over_25_sessions:9;neckline_anchor_very_recent_le1_session:8;older_base_age_over_55_sessions:7;wide_pre_signal_range_over_60pct:7 |
| selected_rule_win | 8 | 3 | 5 | 11.3862 | 12.5556 | -4.6940 | 19.2067 | 150.5341 | 23.5084 | 24.0806 | below_success_p25_low_position_120_pct:5;wide_base_over_20pct:5;above_success_p75_visual_pre_signal_range_pct:4;below_success_p25_selected_mae_pct:4;wide_pre_signal_range_over_60pct:4 |
| selected_rule_neutral | 10 | 5 | 3 | 3.0836 | 10.6672 | -3.7174 | 1.0302 | 43.5304 | 23.8603 | 51.5474 | near_upper_low_position_band_over_50pct:6;wide_base_over_20pct:6;wide_support_pair_span_over_25_sessions:6;above_success_p75_low_position_120_pct:5;above_success_p75_support_pair_span_sessions:5 |

## Loss Rows

| stock_id | stock_name | signal_date | retest_entry_date | visual_pre_signal_context | selected_return_pct | selected_mfe_pct | selected_mae_pct | visual_pre_signal_return_pct | visual_pre_signal_range_pct | base_width_pct | low_position_120_pct | diagnostic_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1528 | 恩德 | 20250221 | 20250227 | mixed | 0.0000 | 7.0946 | -1.3514 | 1.7065 | 81.7490 | 20.3036 | 32.2870 | below_success_p25_base_age_sessions;below_success_p25_selected_mfe_pct;below_success_p25_support_pair_span_sessions;wide_base_over_20pct;wide_pre_signal_range_over_60pct |
| 3051 | 力特 | 20260116 | 20260121 | mixed | -14.5756 | 8.4871 | -18.4502 | -5.6156 | 35.9551 | 24.7191 | 55.9524 | above_success_p75_low_position_120_pct;below_success_p25_base_age_sessions;below_success_p25_selected_mae_pct;below_success_p25_selected_mfe_pct;below_success_p25_support_pair_span_sessions;below_success_p25_visual_pre_signal_return_pct;large_adverse_move_mae_below_minus10pct;near_upper_low_position_band_over_50pct;wide_base_over_20pct |
| 2363 | 矽統 | 20260121 | 20260128 | mixed | -17.7419 | 2.4194 | -19.3548 | -4.7794 | 44.6254 | 15.0923 | 52.7981 | above_success_p75_low_position_120_pct;below_success_p25_base_age_sessions;below_success_p25_selected_mae_pct;below_success_p25_selected_mfe_pct;below_success_p25_visual_pre_signal_return_pct;large_adverse_move_mae_below_minus10pct;near_upper_low_position_band_over_50pct;neckline_anchor_very_recent_le1_session;weak_follow_through_mfe_below_5pct;wide_support_pair_span_over_25_sessions |
| 6290 | 良維 | 20260224 | 20260306 | bullish | -16.9528 | 5.5794 | -18.2403 | 129.5082 | 332.7522 | 20.5970 | 50.1089 | above_success_p75_visual_pre_signal_range_pct;above_success_p75_visual_pre_signal_return_pct;below_success_p25_selected_mae_pct;below_success_p25_selected_mfe_pct;below_success_p25_support_pair_span_sessions;large_adverse_move_mae_below_minus10pct;large_pre_signal_runup_over_50pct;near_upper_low_position_band_over_50pct;neckline_anchor_very_recent_le1_session;older_base_age_over_55_sessions;wide_base_over_20pct;wide_pre_signal_range_over_60pct |
| 6488 | 環球晶 | 20260421 | 20260428 | bullish | -7.9602 | 0.1658 | -11.4428 | 60.1744 | 66.6667 | 30.8191 | 39.9856 | above_success_p75_base_age_sessions;above_success_p75_visual_pre_signal_return_pct;below_success_p25_selected_mae_pct;below_success_p25_selected_mfe_pct;large_adverse_move_mae_below_minus10pct;large_pre_signal_runup_over_50pct;neckline_anchor_very_recent_le1_session;older_base_age_over_55_sessions;weak_follow_through_mfe_below_5pct;wide_base_over_20pct;wide_pre_signal_range_over_60pct;wide_support_pair_span_over_25_sessions |

## Loss Flag Counts

| diagnostic_flag | loss_event_count | success_or_neutral_event_count | total_event_count | loss_share_with_flag_pct |
| --- | --- | --- | --- | --- |
| below_success_p25_selected_mfe_pct | 5 | 5 | 10 | 50.0000 |
| large_adverse_move_mae_below_minus10pct | 4 | 2 | 6 | 66.6667 |
| below_success_p25_selected_mae_pct | 4 | 5 | 9 | 44.4444 |
| wide_base_over_20pct | 4 | 11 | 15 | 26.6667 |
| below_success_p25_base_age_sessions | 3 | 5 | 8 | 37.5000 |
| below_success_p25_support_pair_span_sessions | 3 | 5 | 8 | 37.5000 |
| near_upper_low_position_band_over_50pct | 3 | 6 | 9 | 33.3333 |
| wide_pre_signal_range_over_60pct | 3 | 7 | 10 | 30.0000 |
| neckline_anchor_very_recent_le1_session | 3 | 8 | 11 | 27.2727 |
| large_pre_signal_runup_over_50pct | 2 | 2 | 4 | 50.0000 |
| above_success_p75_low_position_120_pct | 2 | 5 | 7 | 28.5714 |
| above_success_p75_visual_pre_signal_return_pct | 2 | 5 | 7 | 28.5714 |
| below_success_p25_visual_pre_signal_return_pct | 2 | 5 | 7 | 28.5714 |
| older_base_age_over_55_sessions | 2 | 7 | 9 | 22.2222 |
| wide_support_pair_span_over_25_sessions | 2 | 9 | 11 | 18.1818 |
| weak_follow_through_mfe_below_5pct | 2 | 0 | 2 | 100.0000 |
| above_success_p75_base_age_sessions | 1 | 5 | 6 | 16.6667 |
| above_success_p75_visual_pre_signal_range_pct | 1 | 5 | 6 | 16.6667 |

## Boundary Notes

- This is research/backtest advisory-only output.
- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.
- No production model condition, scoring, ranking, PDF logic, or baseline was changed.
