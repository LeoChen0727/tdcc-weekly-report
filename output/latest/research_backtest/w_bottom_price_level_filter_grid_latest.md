# W-Bottom Price-Level Filter Grid

- generated_at: `2026-06-25 12:51:19 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- source_research_id: `w_bottom_price_level_audit`
- filter_candidate: `price_position_252_le_40`
- rule: `price_position_252_pct <= 40.0`
- rows: `38`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: this is a research filter candidate and must not be promoted without a separate model-change PR.

## Overall Base-Scope Comparison

| base_scope_id | filter_id | sample_size | mature_sample_size | win_rate_pct | avg_a_return_pct | median_a_return_pct | baseline_mature_sample_size | delta_win_rate_pct | delta_avg_a_return_pct | sample_retention_rate_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_w_bottom_candidates | baseline_no_price_level_filter | 470 | 52 | 30.7692 | 0.1621 | -1.7857 | 52 | 0.0000 | 0.0000 | 100.0000 | baseline | sample_size_ok_for_research_review |
| all_w_bottom_candidates | price_position_252_le_40 | 408 | 45 | 33.3333 | 0.4170 | -1.7857 | 52 | 2.5641 | 0.2549 | 86.8085 | directionally_improved | sample_size_ok_for_research_review |
| observation_to_volume_confirmation | baseline_no_price_level_filter | 44 | 40 | 32.5000 | 0.8501 | -1.7857 | 40 | 0.0000 | 0.0000 | 100.0000 | baseline | sample_size_ok_for_research_review |
| observation_to_volume_confirmation | price_position_252_le_40 | 38 | 34 | 35.2941 | 1.2789 | -1.7212 | 40 | 2.7941 | 0.4289 | 86.3636 | directionally_improved | sample_size_ok_for_research_review |
| observation_volume_exclude_wv | baseline_no_price_level_filter | 17 | 15 | 40.0000 | 1.6152 | -1.6568 | 15 | 0.0000 | 0.0000 | 100.0000 | baseline | directional_only_below_promotion_review_size |
| observation_volume_exclude_wv | price_position_252_le_40 | 13 | 11 | 45.4545 | 2.0974 | -1.6568 | 15 | 5.4545 | 0.4822 | 76.4706 | directionally_improved | directional_only_below_promotion_review_size |
| core_mainstream_observation_volume_exclude_wv | baseline_no_price_level_filter | 10 | 9 | 66.6667 | 4.5533 | 6.1947 | 9 | 0.0000 | 0.0000 | 100.0000 | baseline | directional_only_below_promotion_review_size |
| core_mainstream_observation_volume_exclude_wv | price_position_252_le_40 | 6 | 5 | 100.0000 | 7.9645 | 8.2474 | 9 | 33.3333 | 3.4112 | 60.0000 | directionally_improved | directional_only_below_promotion_review_size |

## Price Filter Stability Counts

| base_scope_id | stability_signal | segment_count |
| --- | --- | --- |
| all_w_bottom_candidates | directionally_improved | 5 |
| core_mainstream_observation_volume_exclude_wv | directionally_improved | 2 |
| core_mainstream_observation_volume_exclude_wv | insufficient_sample | 2 |
| observation_to_volume_confirmation | directionally_improved | 5 |
| observation_volume_exclude_wv | directionally_improved | 3 |
| observation_volume_exclude_wv | mixed_flat_to_slightly_better | 1 |
| observation_volume_exclude_wv | not_improved | 1 |

## Price Filter By Quarter

| base_scope_id | segment_value | sample_size | mature_sample_size | win_rate_pct | avg_a_return_pct | baseline_mature_sample_size | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_w_bottom_candidates | 2026Q1 | 207 | 23 | 21.7391 | -2.3694 | 26 | 2.5084 | 0.1055 | directionally_improved | directional_only_below_promotion_review_size |
| all_w_bottom_candidates | 2026Q2 | 201 | 22 | 45.4545 | 3.3300 | 26 | 3.1469 | 0.5309 | directionally_improved | directional_only_below_promotion_review_size |
| observation_to_volume_confirmation | 2026Q1 | 18 | 18 | 27.7778 | -1.6883 | 21 | 3.9683 | 0.2279 | directionally_improved | directional_only_below_promotion_review_size |
| observation_to_volume_confirmation | 2026Q2 | 20 | 16 | 43.7500 | 4.6170 | 19 | 1.6447 | 0.7095 | directionally_improved | directional_only_below_promotion_review_size |
| observation_volume_exclude_wv | 2026Q1 | 6 | 6 | 50.0000 | 4.1125 | 8 | 12.5000 | 1.6171 | directionally_improved | directional_only_below_promotion_review_size |
| observation_volume_exclude_wv | 2026Q2 | 7 | 5 | 40.0000 | -0.3207 | 7 | -2.8571 | -0.9300 | not_improved | directional_only_below_promotion_review_size |
| core_mainstream_observation_volume_exclude_wv | 2026Q1 | 3 | 3 | 100.0000 | 10.1645 | 5 | 40.0000 | 5.0081 | insufficient_sample | too_small_for_directional_read |
| core_mainstream_observation_volume_exclude_wv | 2026Q2 | 3 | 2 | 100.0000 | 4.6645 | 4 | 25.0000 | 0.8651 | insufficient_sample | too_small_for_directional_read |

## Price Filter By Mainstream Label

| base_scope_id | segment_value | sample_size | mature_sample_size | win_rate_pct | avg_a_return_pct | baseline_mature_sample_size | delta_win_rate_pct | delta_avg_a_return_pct | stability_signal | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_w_bottom_candidates | core_mainstream | 183 | 27 | 48.1481 | 1.3611 | 32 | 4.3981 | 0.3483 | directionally_improved | directional_only_below_promotion_review_size |
| all_w_bottom_candidates | non_mainstream | 225 | 18 | 11.1111 | -0.9993 | 20 | 1.1111 | 0.1998 | directionally_improved | directional_only_below_promotion_review_size |
| observation_to_volume_confirmation | core_mainstream | 19 | 17 | 58.8235 | 2.9594 | 22 | 8.8235 | 0.8699 | directionally_improved | directional_only_below_promotion_review_size |
| observation_to_volume_confirmation | non_mainstream | 19 | 17 | 11.7647 | -0.4015 | 18 | 0.6536 | 0.2633 | directionally_improved | directional_only_below_promotion_review_size |
| observation_volume_exclude_wv | core_mainstream | 6 | 5 | 100.0000 | 7.9645 | 9 | 33.3333 | 3.4112 | directionally_improved | directional_only_below_promotion_review_size |
| observation_volume_exclude_wv | non_mainstream | 7 | 6 | 0.0000 | -2.7919 | 6 | 0.0000 | 0.0000 | mixed_flat_to_slightly_better | directional_only_below_promotion_review_size |
| core_mainstream_observation_volume_exclude_wv | core_mainstream | 6 | 5 | 100.0000 | 7.9645 | 9 | 33.3333 | 3.4112 | directionally_improved | directional_only_below_promotion_review_size |

## Reading Notes

- `sample_retention_rate_pct` shows how much sample remains after requiring bottom/low level.
- A positive directional read is not enough for production if mature sample size remains below promotion review size.
- This grid tests price level only; path shape quality and neckline-volume confirmation remain separate research gates.
