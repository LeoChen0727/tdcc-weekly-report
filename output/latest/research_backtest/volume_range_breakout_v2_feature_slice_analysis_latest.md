# volume_range_breakout v2 feature slice analysis

Research-only artifact. This does not change production model conditions, ranking, scoring, registry, or PDF behavior.

Source population: 808 raw-market events for `prev60_high_next_day_continuation` after source sync.
Purpose: compare low-base vs high/extended setups, narrow vs wide consolidation, locked limit-up behavior, overheat proxies, and top/bottom return feature differences before any v2 promotion discussion.

## Performance Slices

| slice_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | top_minus_bottom_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_all_v2_raw_events | 811 | 52.4 | 47.1 | 4.9629 | 1.3359 | 0.0 | baseline_reference |
| overheat_flag_true | 754 | 52.39 | 47.21 | 5.061 | 1.3482 | -0.66 | mixed_or_weak_difference_research_only |
| locked_limit_up | 602 | 53.49 | 46.01 | 5.4259 | 1.8198 | 0.16 | mixed_or_weak_difference_research_only |
| volume_ratio_2_to_6 | 601 | 52.41 | 47.09 | 4.675 | 1.3265 | 0.67 | mixed_or_weak_difference_research_only |
| non_consolidation | 543 | 55.62 | 44.2 | 6.125 | 2.4691 | 0.55 | possible_positive_gate_or_score_candidate_research_only |
| range20_gt25_wide | 509 | 55.6 | 44.2 | 6.2162 | 2.7419 | 0.79 | possible_positive_gate_or_score_candidate_research_only |
| signal_return_ge9_8 | 503 | 52.29 | 47.12 | 4.9559 | 1.3605 | -1.2 | mixed_or_weak_difference_research_only |
| off60_le50_range60_le45 | 373 | 48.26 | 51.21 | 2.9808 | -0.8671 | -1.07 | possible_risk_tag_or_deduct_candidate_research_only |
| range60_le35_narrow | 296 | 43.24 | 56.08 | 2.3505 | -2.0071 | -2.03 | possible_risk_tag_or_deduct_candidate_research_only |
| consolidated_any | 268 | 45.9 | 52.99 | 2.6086 | -1.2586 | -1.12 | possible_risk_tag_or_deduct_candidate_research_only |
| off60_gt75_or_range60_gt60 | 258 | 54.65 | 44.96 | 5.9121 | 2.5711 | -1.55 | mixed_or_weak_difference_research_only |
| high_wide_non_consolidation | 258 | 54.65 | 44.96 | 5.9121 | 2.5711 | -1.55 | mixed_or_weak_difference_research_only |
| range60_gt60_very_wide | 256 | 54.3 | 45.31 | 5.9183 | 2.4188 | -1.56 | mixed_or_weak_difference_research_only |
| low_base_loose_and_consolidated | 254 | 45.28 | 53.94 | 2.3197 | -1.6494 | -0.79 | possible_risk_tag_or_deduct_candidate_research_only |
| off60_le40_range60_le35 | 248 | 43.55 | 55.65 | 2.1898 | -2.1009 | -2.02 | possible_risk_tag_or_deduct_candidate_research_only |
| high_or_wide_overheat | 243 | 53.5 | 46.09 | 5.6462 | 2.0804 | -2.88 | mixed_or_weak_difference_research_only |
| not_locked_limit_up | 209 | 49.28 | 50.24 | 3.6293 | -0.4515 | -0.48 | possible_risk_tag_or_deduct_candidate_research_only |
| range20_le15_tight | 127 | 43.31 | 56.69 | 1.8046 | -2.1739 | -2.36 | possible_risk_tag_or_deduct_candidate_research_only |
| low_base_loose_not_locked | 113 | 42.48 | 56.64 | 1.491 | -2.0362 | 0.89 | possible_risk_tag_or_deduct_candidate_research_only |
| volume_ratio_gt6 | 81 | 45.68 | 54.32 | 3.7009 | -1.2214 | -7.41 | mixed_or_weak_difference_research_only |
| overheat_flag_false | 57 | 52.63 | 45.61 | 3.6663 | 1.3265 | 8.77 | mixed_or_weak_difference_research_only |
| low_base_loose_not_overheat | 32 | 34.38 | 62.5 | -1.3451 | -2.5461 | 3.12 | insufficient_sample_do_not_use_as_gate |

## Strongest Top/Bottom Return Feature Differences

| slice_id | sample_size | overall_share_pct | high_return_share_pct | low_return_share_pct | high_minus_low_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- |
| off_60d_low_bucket=off60_50_75_extended | 199 | 24.54 | 28.83 | 23.31 | 5.52 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_le35_low_base | 182 | 22.44 | 17.79 | 22.09 | -4.29 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_le35_narrow | 296 | 36.5 | 30.06 | 33.74 | -3.68 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_45_60_wide | 141 | 17.39 | 19.63 | 15.95 | 3.68 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_ge9_8_limit_up_like | 503 | 62.02 | 64.42 | 68.1 | -3.68 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_gt6_overheat | 81 | 9.99 | 10.43 | 14.11 | -3.68 | weak_or_mixed_feature_difference |
| risk_type=high_position_chase | 745 | 91.86 | 94.48 | 97.55 | -3.07 | weak_or_mixed_feature_difference |
| candle_quality=standard_candle | 83 | 10.23 | 5.52 | 8.59 | -3.07 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_3_to_7_strong | 132 | 16.28 | 13.5 | 10.43 | 3.07 | weak_or_mixed_feature_difference |
| overheat_flag=False | 57 | 7.03 | 4.29 | 1.23 | 3.07 | weak_or_mixed_feature_difference |
| overheat_flag=True | 754 | 92.97 | 95.71 | 98.77 | -3.07 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_gt75_high_extended | 235 | 28.98 | 34.36 | 36.81 | -2.45 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_2_to_6_controlled_attack | 601 | 74.11 | 69.94 | 67.48 | 2.45 | weak_or_mixed_feature_difference |
| consolidation_type=long_consolidation | 252 | 31.07 | 23.93 | 26.38 | -2.45 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_35_45_moderate | 118 | 14.55 | 12.88 | 10.43 | 2.45 | weak_or_mixed_feature_difference |
| attack_method=general_breakout | 83 | 10.23 | 5.52 | 7.98 | -2.45 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_gt60_very_wide | 256 | 31.57 | 37.42 | 39.88 | -2.45 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_gt25_wide | 509 | 62.76 | 71.78 | 69.33 | 2.45 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_le15_tight | 127 | 15.66 | 12.27 | 14.11 | -1.84 | weak_or_mixed_feature_difference |
| consolidation_type=non_consolidation | 543 | 66.95 | 74.23 | 72.39 | 1.84 | weak_or_mixed_feature_difference |
| attack_method=volume_attack | 126 | 15.54 | 14.72 | 12.88 | 1.84 | weak_or_mixed_feature_difference |
| risk_type=normal_risk | 47 | 5.8 | 3.07 | 1.23 | 1.84 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_35_50_low_mid_base | 195 | 24.04 | 19.02 | 17.79 | 1.23 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_lt2_weak | 129 | 15.91 | 19.63 | 18.4 | 1.23 | weak_or_mixed_feature_difference |
| candle_quality=close_at_high | 615 | 75.83 | 80.37 | 79.14 | 1.23 | weak_or_mixed_feature_difference |
| limit_up_like=False | 209 | 25.77 | 20.25 | 20.86 | -0.61 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_15_25_moderate | 175 | 21.58 | 15.95 | 16.56 | -0.61 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_7_to_9_8_extended | 169 | 20.84 | 22.09 | 21.47 | 0.61 | weak_or_mixed_feature_difference |
| attack_method=locked_limit_up | 602 | 74.23 | 79.75 | 79.14 | 0.61 | weak_or_mixed_feature_difference |
| limit_up_like=True | 602 | 74.23 | 79.75 | 79.14 | 0.61 | weak_or_mixed_feature_difference |

## Numeric Top/Bottom Median Comparison

| slice_id | sample_size | numeric_overall_median | numeric_top20_median | numeric_bottom20_median | numeric_top_minus_bottom_median | decision_hint |
| --- | --- | --- | --- | --- | --- | --- |
| off_60d_low_pct | 811 | 53.0837 | 60.7843 | 58.7786 | 2.0057 | numeric_difference_diagnostic_only |
| position_in_60d_range_pct | 811 | 120.354 | 119.7115 | 120.7592 | -1.0477 | numeric_difference_diagnostic_only |
| range_width_20_pct | 811 | 30.6483 | 32.7189 | 34.6062 | -1.8873 | numeric_difference_diagnostic_only |
| range_width_40_pct | 811 | 38.8479 | 45.098 | 45.3744 | -0.2764 | numeric_difference_diagnostic_only |
| range_width_60_pct | 811 | 43.5115 | 48.2993 | 48.1481 | 0.1512 | numeric_difference_diagnostic_only |
| breakout_over_prev60_pct | 811 | 6.3462 | 6.6351 | 7.21 | -0.5749 | numeric_difference_diagnostic_only |
| volume_ratio | 811 | 3.0755 | 3.0337 | 3.0096 | 0.0241 | numeric_difference_diagnostic_only |
| signal_return_1d_pct | 811 | 9.8712 | 9.8765 | 9.8795 | -0.003 | numeric_difference_diagnostic_only |
| mfe_pct | 811 | 13.8686 | 38.488 | 3.6946 | 34.7934 | numeric_difference_diagnostic_only |
| mae_pct | 811 | -7.8431 | -3.75 | -17.0663 | 13.3163 | numeric_difference_diagnostic_only |

## Promotion Boundary

These rows are diagnostic and research-only. A hard gate, score, risk tag, or model split still requires a separate promotion review with operation contract and production parity evidence.
