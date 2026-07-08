# volume_range_breakout v2 feature slice analysis

Research-only artifact. This does not change production model conditions, ranking, scoring, registry, or PDF behavior.

Source population: 808 raw-market events for `prev60_high_next_day_continuation` after source sync.
Purpose: compare low-base vs high/extended setups, narrow vs wide consolidation, locked limit-up behavior, overheat proxies, and top/bottom return feature differences before any v2 promotion discussion.

## Performance Slices

| slice_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | top_minus_bottom_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_all_v2_raw_events | 808 | 52.48 | 47.03 | 4.9893 | 1.3482 | 0.0 | baseline_reference |
| overheat_flag_true | 751 | 52.46 | 47.14 | 5.0897 | 1.3605 | -0.66 | mixed_or_weak_difference_research_only |
| locked_limit_up | 600 | 53.5 | 46.0 | 5.4362 | 1.8198 | 0.0 | mixed_or_weak_difference_research_only |
| volume_ratio_2_to_6 | 598 | 52.51 | 46.99 | 4.7091 | 1.3312 | 0.83 | mixed_or_weak_difference_research_only |
| non_consolidation | 540 | 55.74 | 44.07 | 6.1709 | 2.5711 | 0.74 | possible_positive_gate_or_score_candidate_research_only |
| range20_gt25_wide | 506 | 55.73 | 44.07 | 6.2657 | 2.7667 | 0.99 | possible_positive_gate_or_score_candidate_research_only |
| signal_return_ge9_8 | 501 | 52.3 | 47.11 | 4.9663 | 1.3605 | -1.4 | mixed_or_weak_difference_research_only |
| off60_le50_range60_le45 | 370 | 48.38 | 51.08 | 3.0223 | -0.8012 | -1.08 | possible_risk_tag_or_deduct_candidate_research_only |
| range60_le35_narrow | 293 | 43.34 | 55.97 | 2.3964 | -1.978 | -2.05 | possible_risk_tag_or_deduct_candidate_research_only |
| consolidated_any | 268 | 45.9 | 52.99 | 2.6086 | -1.2586 | -1.49 | possible_risk_tag_or_deduct_candidate_research_only |
| off60_gt75_or_range60_gt60 | 258 | 54.65 | 44.96 | 5.9121 | 2.5711 | -1.55 | mixed_or_weak_difference_research_only |
| high_wide_non_consolidation | 258 | 54.65 | 44.96 | 5.9121 | 2.5711 | -1.55 | mixed_or_weak_difference_research_only |
| range60_gt60_very_wide | 256 | 54.3 | 45.31 | 5.9183 | 2.4188 | -1.56 | mixed_or_weak_difference_research_only |
| low_base_loose_and_consolidated | 254 | 45.28 | 53.94 | 2.3197 | -1.6494 | -1.18 | possible_risk_tag_or_deduct_candidate_research_only |
| off60_le40_range60_le35 | 246 | 43.5 | 55.69 | 2.2157 | -2.1009 | -2.03 | possible_risk_tag_or_deduct_candidate_research_only |
| high_or_wide_overheat | 243 | 53.5 | 46.09 | 5.6462 | 2.0804 | -2.88 | mixed_or_weak_difference_research_only |
| not_locked_limit_up | 208 | 49.52 | 50.0 | 3.7001 | -0.2258 | 0.0 | possible_risk_tag_or_deduct_candidate_research_only |
| range20_le15_tight | 127 | 43.31 | 56.69 | 1.8046 | -2.1739 | -3.15 | possible_risk_tag_or_deduct_candidate_research_only |
| low_base_loose_not_locked | 112 | 42.86 | 56.25 | 1.6033 | -1.9156 | 1.79 | possible_risk_tag_or_deduct_candidate_research_only |
| volume_ratio_gt6 | 81 | 45.68 | 54.32 | 3.7009 | -1.2214 | -8.65 | mixed_or_weak_difference_research_only |
| overheat_flag_false | 57 | 52.63 | 45.61 | 3.6663 | 1.3265 | 8.77 | mixed_or_weak_difference_research_only |
| low_base_loose_not_overheat | 32 | 34.38 | 62.5 | -1.3451 | -2.5461 | 3.12 | insufficient_sample_do_not_use_as_gate |

## Strongest Top/Bottom Return Feature Differences

| slice_id | sample_size | overall_share_pct | high_return_share_pct | low_return_share_pct | high_minus_low_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- |
| off_60d_low_bucket=off60_50_75_extended | 199 | 24.63 | 29.01 | 23.46 | 5.56 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_le35_low_base | 181 | 22.4 | 17.28 | 22.22 | -4.94 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_ge9_8_limit_up_like | 501 | 62.0 | 64.2 | 68.52 | -4.32 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_gt6_overheat | 81 | 10.02 | 9.88 | 14.2 | -4.32 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_45_60_wide | 141 | 17.45 | 19.75 | 16.05 | 3.7 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_le35_narrow | 293 | 36.26 | 29.63 | 33.33 | -3.7 | weak_or_mixed_feature_difference |
| risk_type=high_position_chase | 743 | 91.96 | 94.44 | 98.15 | -3.7 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_3_to_7_strong | 131 | 16.21 | 13.58 | 9.88 | 3.7 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_2_to_6_controlled_attack | 598 | 74.01 | 70.37 | 67.28 | 3.09 | weak_or_mixed_feature_difference |
| overheat_flag=False | 57 | 7.05 | 4.32 | 1.23 | 3.09 | weak_or_mixed_feature_difference |
| consolidation_type=long_consolidation | 252 | 31.19 | 23.46 | 26.54 | -3.09 | weak_or_mixed_feature_difference |
| overheat_flag=True | 751 | 92.95 | 95.68 | 98.77 | -3.09 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_gt25_wide | 506 | 62.62 | 72.22 | 69.14 | 3.09 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_le15_tight | 127 | 15.72 | 11.73 | 14.2 | -2.47 | weak_or_mixed_feature_difference |
| candle_quality=standard_candle | 82 | 10.15 | 5.56 | 8.02 | -2.47 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_gt60_very_wide | 256 | 31.68 | 37.65 | 40.12 | -2.47 | weak_or_mixed_feature_difference |
| range_width_60_bucket=range60_35_45_moderate | 118 | 14.6 | 12.96 | 10.49 | 2.47 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_gt75_high_extended | 235 | 29.08 | 34.57 | 37.04 | -2.47 | weak_or_mixed_feature_difference |
| attack_method=volume_attack | 125 | 15.47 | 14.81 | 12.35 | 2.47 | weak_or_mixed_feature_difference |
| attack_method=general_breakout | 83 | 10.27 | 5.56 | 8.02 | -2.47 | weak_or_mixed_feature_difference |
| consolidation_type=non_consolidation | 540 | 66.83 | 74.69 | 72.22 | 2.47 | weak_or_mixed_feature_difference |
| risk_type=normal_risk | 47 | 5.82 | 3.09 | 1.23 | 1.85 | weak_or_mixed_feature_difference |
| off_60d_low_bucket=off60_35_50_low_mid_base | 193 | 23.89 | 19.14 | 17.28 | 1.85 | weak_or_mixed_feature_difference |
| volume_ratio_bucket=volume_lt2_weak | 129 | 15.97 | 19.75 | 18.52 | 1.23 | weak_or_mixed_feature_difference |
| signal_return_bucket=signal_return_7_to_9_8_extended | 169 | 20.92 | 22.22 | 21.6 | 0.62 | weak_or_mixed_feature_difference |
| candle_quality=close_at_high | 613 | 75.87 | 80.25 | 79.63 | 0.62 | weak_or_mixed_feature_difference |
| range_width_20_bucket=range20_15_25_moderate | 175 | 21.66 | 16.05 | 16.67 | -0.62 | weak_or_mixed_feature_difference |
| locked_limit_up_flag=True | 600 | 74.26 | 79.63 | 79.63 | 0.0 | weak_or_mixed_feature_difference |
| locked_limit_up_flag=False | 208 | 25.74 | 20.37 | 20.37 | 0.0 | weak_or_mixed_feature_difference |
| limit_up_like=True | 600 | 74.26 | 79.63 | 79.63 | 0.0 | weak_or_mixed_feature_difference |

## Numeric Top/Bottom Median Comparison

| slice_id | sample_size | numeric_overall_median | numeric_top20_median | numeric_bottom20_median | numeric_top_minus_bottom_median | decision_hint |
| --- | --- | --- | --- | --- | --- | --- |
| off_60d_low_pct | 808 | 53.2477 | 60.9361 | 59.3344 | 1.6017 | numeric_difference_diagnostic_only |
| position_in_60d_range_pct | 808 | 120.3811 | 119.6323 | 120.8316 | -1.1993 | numeric_difference_diagnostic_only |
| range_width_20_pct | 808 | 30.6467 | 32.8689 | 34.8706 | -2.0017 | numeric_difference_diagnostic_only |
| range_width_40_pct | 808 | 38.8705 | 45.3003 | 45.8424 | -0.5421 | numeric_difference_diagnostic_only |
| range_width_60_pct | 808 | 43.6753 | 48.5544 | 48.9804 | -0.426 | numeric_difference_diagnostic_only |
| breakout_over_prev60_pct | 808 | 6.363 | 6.6209 | 7.2757 | -0.6548 | numeric_difference_diagnostic_only |
| volume_ratio | 808 | 3.0734 | 3.0271 | 3.0041 | 0.023 | numeric_difference_diagnostic_only |
| signal_return_1d_pct | 808 | 9.8709 | 9.8745 | 9.8804 | -0.0059 | numeric_difference_diagnostic_only |
| mfe_pct | 808 | 13.8855 | 38.5773 | 3.6251 | 34.9522 | numeric_difference_diagnostic_only |
| mae_pct | 808 | -7.8202 | -3.7618 | -17.1361 | 13.3743 | numeric_difference_diagnostic_only |

## Promotion Boundary

These rows are diagnostic and research-only. A hard gate, score, risk tag, or model split still requires a separate promotion review with operation contract and production parity evidence.
