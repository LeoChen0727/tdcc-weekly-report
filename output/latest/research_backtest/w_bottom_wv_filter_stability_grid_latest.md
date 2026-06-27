# W-Bottom WV/WVV Filter Stability Grid

- generated_at: `2026-06-25 12:21:26 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- source_research_id: `w_bottom_path_quality_filter_audit`
- rows: `210`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: stability signals are research-only and require promotion review before any production use.

## Overall Filter Comparison

| filter_id | sample_size | mature_sample_size | win_rate | avg_a_return_pct | median_a_return_pct | delta_win_rate_pct | delta_avg_a_return_pct | sample_retention_rate | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| observation_to_volume_confirmation | 44 | 40 | 32.50% | 0.8501 | -1.7857 | 0.0000 | 0.0000 | 100.00% | baseline | sample_size_ok_for_research_review |
| exclude_wv_multiple_turn | 17 | 15 | 40.00% | 1.6152 | -1.6568 | 7.5000 | 0.7652 | 38.64% | directionally_improved | directional_only_below_promotion_review_size |
| exclude_slope_break | 33 | 30 | 36.67% | 1.4272 | -1.0882 | 4.1667 | 0.5771 | 75.00% | directionally_improved | sample_size_ok_for_research_review |
| exclude_wv_or_slope_break | 6 | 5 | 80.00% | 6.6084 | 8.4000 | 47.5000 | 5.7583 | 13.64% | directionally_improved | directional_only_below_promotion_review_size |
| exclude_sharp_v | 41 | 38 | 28.95% | 0.4480 | -1.9085 | -3.5526 | -0.4021 | 93.18% | not_improved | sample_size_ok_for_research_review |
| smooth_only | 3 | 3 | 66.67% | 5.3538 | 8.4000 | 34.1667 | 4.5038 | 6.82% | insufficient_sample | too_small_for_directional_read |

## Exclude WV/WVV Stability Signal Counts

| segment_dimension | stability_signal | segment_count |
| --- | --- | --- |
| effective_mainstream_label | directionally_improved | 1 |
| effective_mainstream_label | not_improved | 1 |
| has_hot_theme | directionally_improved | 1 |
| has_hot_theme | insufficient_sample | 1 |
| overall | directionally_improved | 1 |
| signal_half | directionally_improved | 1 |
| signal_month | insufficient_sample | 6 |
| signal_quarter | directionally_improved | 1 |
| signal_quarter | not_improved | 1 |
| structural_theme_bucket | insufficient_sample | 20 |
| structural_theme_bucket | not_improved | 1 |

## Exclude WV/WVV By Month

| segment_value | sample_size | mature_sample_size | win_rate | avg_a_return_pct | baseline_mature_sample_size | baseline_win_rate | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01 | 3 | 3 | 33.33% | 3.5796 | 7 | 14.29% | 19.0476 | 6.1148 | insufficient_sample | too_small_for_directional_read |
| 2026-02 | 4 | 4 | 50.00% | 2.8680 | 9 | 33.33% | 16.6667 | 3.8720 | insufficient_sample | too_small_for_directional_read |
| 2026-03 | 1 | 1 | 0.00% | -2.2472 | 5 | 20.00% | -20.0000 | 0.4442 | insufficient_sample | too_small_for_directional_read |
| 2026-04 | 2 | 2 | 50.00% | 2.9343 | 5 | 60.00% | -10.0000 | 0.9620 | insufficient_sample | too_small_for_directional_read |
| 2026-05 | 4 | 4 | 50.00% | 0.0133 | 12 | 41.67% | 8.3333 | -5.9681 | insufficient_sample | too_small_for_directional_read |
| 2026-06 | 3 | 1 | 0.00% | -1.6568 | 2 | 0.00% | 0.0000 | 2.0405 | insufficient_sample | too_small_for_directional_read |

## Exclude WV/WVV By Quarter

| segment_value | sample_size | mature_sample_size | win_rate | avg_a_return_pct | baseline_mature_sample_size | baseline_win_rate | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026Q1 | 8 | 8 | 37.50% | 2.4954 | 21 | 23.81% | 13.6905 | 4.4117 | directionally_improved | directional_only_below_promotion_review_size |
| 2026Q2 | 9 | 7 | 42.86% | 0.6093 | 19 | 42.11% | 0.7519 | -3.2983 | not_improved | directional_only_below_promotion_review_size |

## Exclude WV/WVV By Mainstream Label

| segment_value | sample_size | mature_sample_size | win_rate | avg_a_return_pct | baseline_mature_sample_size | baseline_win_rate | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core_mainstream | 10 | 9 | 66.67% | 4.5533 | 22 | 50.00% | 16.6667 | 2.4638 | directionally_improved | directional_only_below_promotion_review_size |
| non_mainstream | 7 | 6 | 0.00% | -2.7919 | 18 | 11.11% | -11.1111 | -2.1271 | not_improved | directional_only_below_promotion_review_size |

## Exclude WV/WVV By Hot Theme Flag

| segment_value | sample_size | mature_sample_size | win_rate | avg_a_return_pct | baseline_mature_sample_size | baseline_win_rate | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| false | 15 | 13 | 38.46% | 1.3310 | 37 | 32.43% | 6.0291 | 0.5231 | directionally_improved | directional_only_below_promotion_review_size |
| true | 2 | 2 | 50.00% | 3.4629 | 3 | 33.33% | 16.6667 | 2.0921 | insufficient_sample | too_small_for_directional_read |

## Exclude WV/WVV By Structural Theme Bucket With At Least 5 Mature Baseline Rows

| segment_value | sample_size | mature_sample_size | win_rate | avg_a_return_pct | baseline_mature_sample_size | baseline_win_rate | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| computer_peripheral_general_theme | 3 | 3 | 100.00% | 7.8593 | 5 | 80.00% | 20.0000 | -0.7360 | insufficient_sample | too_small_for_directional_read |
| non_mainstream_theme | 7 | 6 | 0.00% | -2.7919 | 18 | 11.11% | -11.1111 | -2.1271 | not_improved | directional_only_below_promotion_review_size |
