# W-Bottom Early-Entry Stability Audit

- generated_at: `2026-06-27 00:34:13 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- scope: variant nearest-micro event replay, split by signal month and quarter.
- limitation: current backfilled signal window is `2024-10 to 2026-06`; this remains a short-window stability check, not long-term evidence.

## Strict Segment Monthly Rollup

| segment_id | period_count | periods_with_mature_ge5 | periods_with_mature_ge10 | sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | min_period_win_rate_pct | max_period_win_rate_pct | win_rate_range_mature_ge5_pct | win_rate_range_mature_ge10_pct | stability_status | mature_period_stability_status | next_review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 20 | 8 | 3 | 172 | 96 | 44 | 46 | 52 | 45.8333 | 32.3944 | 0.0000 | 100.0000 | 63.3333 | 50.0000 | unstable_period_win_rate | mature_ge5_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| smooth_price_le40_right_rebound_5_20 | 20 | 8 | 1 | 158 | 87 | 39 | 41 | 48 | 44.8276 | 32.0312 | 0.0000 | 100.0000 | 61.1111 | 0.0000 | insufficient_period_coverage_for_promotion | mature_ge5_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| smooth_core_mainstream_right_rebound_5_20 | 17 | 4 | 1 | 95 | 53 | 29 | 28 | 24 | 54.7170 | 34.5679 | 0.0000 | 100.0000 | 71.4286 | 0.0000 | insufficient_period_coverage_for_promotion | insufficient_mature_periods_research_only | blocked_by_insufficient_monthly_repetition |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 17 | 4 | 0 | 85 | 45 | 24 | 26 | 21 | 53.3333 | 36.6197 | 0.0000 | 100.0000 | 71.4286 |  | insufficient_period_coverage_for_promotion | insufficient_mature_periods_research_only | blocked_by_insufficient_monthly_repetition |
| smooth_right_rebound_5_20_red_ratio_gt_first | 19 | 5 | 0 | 100 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | 0.0000 | 100.0000 | 63.3333 |  | insufficient_period_coverage_for_promotion | insufficient_mature_periods_research_only | blocked_by_insufficient_monthly_repetition |
| smooth_right_rebound_5_20_near_neckline | 18 | 6 | 0 | 102 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | 0.0000 | 100.0000 | 63.3333 |  | insufficient_period_coverage_for_promotion | insufficient_mature_periods_research_only | blocked_by_insufficient_monthly_repetition |
| price_le30_rebound_3_20_volume_red | 21 | 19 | 16 | 606 | 351 | 143 | 156 | 208 | 40.7407 | 30.7692 | 19.2308 | 60.0000 | 40.7692 | 40.7692 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| price_le30_rebound_5_20_volume_red | 21 | 18 | 10 | 401 | 233 | 100 | 106 | 133 | 42.9185 | 31.2684 | 16.6667 | 70.5882 | 53.9215 | 53.9215 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| price_le30_rebound_3_20_volume_red_below_neckline5 | 21 | 15 | 9 | 344 | 192 | 75 | 93 | 117 | 39.0625 | 32.6316 | 0.0000 | 100.0000 | 58.9286 | 42.5000 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | 21 | 16 | 12 | 388 | 231 | 100 | 102 | 131 | 43.2900 | 30.6306 | 0.0000 | 70.5882 | 50.5882 | 44.2724 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| core_mainstream_price_le30_rebound_3_20_volume_red | 21 | 16 | 8 | 322 | 192 | 87 | 82 | 105 | 45.3125 | 29.9270 | 11.1111 | 100.0000 | 73.5043 | 64.6154 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| core_or_hot_price_le30_rebound_3_20_volume_red | 21 | 16 | 8 | 322 | 192 | 87 | 82 | 105 | 45.3125 | 29.9270 | 11.1111 | 100.0000 | 73.5043 | 64.6154 | unstable_period_win_rate | mature_ge10_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| smooth_price_le30_rebound_3_20_volume_red | 19 | 8 | 0 | 124 | 70 | 32 | 30 | 38 | 45.7143 | 30.0000 | 0.0000 | 100.0000 | 57.1429 |  | insufficient_period_coverage_for_promotion | mature_ge5_unstable_or_weak_research_only | blocked_by_unstable_or_weak_monthly_result |
| smooth_price_le30_rebound_5_20_volume_red | 18 | 4 | 0 | 79 | 44 | 22 | 20 | 22 | 50.0000 | 31.2500 | 0.0000 | 100.0000 | 43.3333 |  | insufficient_period_coverage_for_promotion | insufficient_mature_periods_research_only | blocked_by_insufficient_monthly_repetition |

## smooth_right_rebound_5_20 Monthly Detail

| period_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | incomplete_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-10 | 3 | 3 | 2 | 1 | 1 | 1 | 0 | 50.0000 | 33.3333 | too_small_for_period_decision |
| 2024-11 | 4 | 4 | 4 | 2 | 0 | 2 | 0 | 50.0000 | 0.0000 | too_small_for_period_decision |
| 2024-12 | 18 | 18 | 10 | 3 | 8 | 7 | 0 | 30.0000 | 44.4444 | not_directionally_positive_period |
| 2025-01 | 8 | 8 | 4 | 1 | 4 | 3 | 0 | 25.0000 | 50.0000 | too_small_for_period_decision |
| 2025-02 | 10 | 10 | 4 | 3 | 6 | 1 | 0 | 75.0000 | 60.0000 | too_small_for_period_decision |
| 2025-03 | 8 | 8 | 8 | 2 | 0 | 6 | 0 | 25.0000 | 0.0000 | not_directionally_positive_period |
| 2025-04 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0.0000 | 0.0000 | too_small_for_period_decision |
| 2025-06 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 100.0000 | 0.0000 | too_small_for_period_decision |
| 2025-07 | 10 | 10 | 8 | 5 | 2 | 3 | 0 | 62.5000 | 20.0000 | directionally_positive_period |
| 2025-08 | 9 | 9 | 7 | 5 | 2 | 2 | 0 | 71.4286 | 22.2222 | directionally_positive_period |
| 2025-09 | 4 | 4 | 2 | 0 | 2 | 2 | 0 | 0.0000 | 50.0000 | too_small_for_period_decision |
| 2025-10 | 2 | 2 | 1 | 0 | 1 | 1 | 0 | 0.0000 | 50.0000 | too_small_for_period_decision |
| 2025-11 | 6 | 6 | 4 | 1 | 2 | 3 | 0 | 25.0000 | 33.3333 | too_small_for_period_decision |
| 2025-12 | 9 | 9 | 4 | 2 | 5 | 2 | 0 | 50.0000 | 55.5556 | too_small_for_period_decision |
| 2026-01 | 18 | 18 | 12 | 6 | 6 | 6 | 0 | 50.0000 | 33.3333 | not_directionally_positive_period |
| 2026-02 | 7 | 7 | 6 | 1 | 1 | 5 | 0 | 16.6667 | 14.2857 | not_directionally_positive_period |
| 2026-03 | 12 | 12 | 8 | 3 | 4 | 5 | 0 | 37.5000 | 33.3333 | not_directionally_positive_period |
| 2026-04 | 14 | 12 | 10 | 8 | 2 | 2 | 2 | 80.0000 | 16.6667 | directionally_positive_period |
| 2026-05 | 14 | 0 | 0 | 0 | 0 | 0 | 14 |  |  | future_window_incomplete |
| 2026-06 | 14 | 0 | 0 | 0 | 0 | 0 | 14 |  |  | future_window_incomplete |

## Market Regime Rollup

| segment_id | period_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | correction | 21 | 19 | 15 | 6 | 4 | 9 | 40.0000 | 21.0526 | not_directionally_positive_period |
| smooth_right_rebound_5_20 | mild_bull | 19 | 18 | 12 | 5 | 6 | 7 | 41.6667 | 33.3333 | not_directionally_positive_period |
| smooth_right_rebound_5_20 | range_or_mixed | 59 | 53 | 30 | 11 | 23 | 19 | 36.6667 | 43.3962 | not_directionally_positive_period |
| smooth_right_rebound_5_20 | strong_bull | 66 | 45 | 33 | 19 | 12 | 14 | 57.5758 | 26.6667 | directionally_positive_period |
| smooth_right_rebound_5_20 | unknown | 7 | 7 | 6 | 3 | 1 | 3 | 50.0000 | 14.2857 | not_directionally_positive_period |
| smooth_price_le40_right_rebound_5_20 | correction | 19 | 17 | 14 | 5 | 3 | 9 | 35.7143 | 17.6471 | not_directionally_positive_period |
| smooth_price_le40_right_rebound_5_20 | mild_bull | 18 | 17 | 12 | 5 | 5 | 7 | 41.6667 | 29.4118 | not_directionally_positive_period |
| smooth_price_le40_right_rebound_5_20 | range_or_mixed | 54 | 48 | 28 | 10 | 20 | 18 | 35.7143 | 41.6667 | not_directionally_positive_period |
| smooth_price_le40_right_rebound_5_20 | strong_bull | 63 | 42 | 30 | 17 | 12 | 13 | 56.6667 | 28.5714 | directionally_positive_period |
| smooth_price_le40_right_rebound_5_20 | unknown | 4 | 4 | 3 | 2 | 1 | 1 | 66.6667 | 25.0000 | too_small_for_period_decision |
| smooth_core_mainstream_right_rebound_5_20 | correction | 11 | 11 | 11 | 6 | 0 | 5 | 54.5455 | 0.0000 | not_directionally_positive_period |
| smooth_core_mainstream_right_rebound_5_20 | mild_bull | 6 | 5 | 2 | 1 | 3 | 1 | 50.0000 | 60.0000 | too_small_for_period_decision |
| smooth_core_mainstream_right_rebound_5_20 | range_or_mixed | 34 | 33 | 16 | 7 | 17 | 9 | 43.7500 | 51.5152 | not_directionally_positive_period |
| smooth_core_mainstream_right_rebound_5_20 | strong_bull | 38 | 26 | 18 | 12 | 8 | 6 | 66.6667 | 30.7692 | directionally_positive_period |
| smooth_core_mainstream_right_rebound_5_20 | unknown | 6 | 6 | 6 | 3 | 0 | 3 | 50.0000 | 0.0000 | not_directionally_positive_period |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | correction | 10 | 10 | 10 | 5 | 0 | 5 | 50.0000 | 0.0000 | not_directionally_positive_period |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | mild_bull | 6 | 5 | 2 | 1 | 3 | 1 | 50.0000 | 60.0000 | too_small_for_period_decision |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | range_or_mixed | 30 | 29 | 14 | 6 | 15 | 8 | 42.8571 | 51.7241 | not_directionally_positive_period |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | strong_bull | 36 | 24 | 16 | 10 | 8 | 6 | 62.5000 | 33.3333 | directionally_positive_period |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | unknown | 3 | 3 | 3 | 2 | 0 | 1 | 66.6667 | 0.0000 | too_small_for_period_decision |
| smooth_right_rebound_5_20_red_ratio_gt_first | correction | 11 | 10 | 9 | 3 | 1 | 6 | 33.3333 | 10.0000 | not_directionally_positive_period |
| smooth_right_rebound_5_20_red_ratio_gt_first | mild_bull | 10 | 10 | 8 | 3 | 2 | 5 | 37.5000 | 20.0000 | not_directionally_positive_period |
| smooth_right_rebound_5_20_red_ratio_gt_first | range_or_mixed | 38 | 34 | 18 | 6 | 16 | 12 | 33.3333 | 47.0588 | not_directionally_positive_period |
| smooth_right_rebound_5_20_red_ratio_gt_first | strong_bull | 37 | 25 | 18 | 11 | 7 | 7 | 61.1111 | 28.0000 | directionally_positive_period |
| smooth_right_rebound_5_20_red_ratio_gt_first | unknown | 4 | 4 | 4 | 3 | 0 | 1 | 75.0000 | 0.0000 | too_small_for_period_decision |
| smooth_right_rebound_5_20_near_neckline | correction | 12 | 11 | 10 | 4 | 1 | 6 | 40.0000 | 9.0909 | not_directionally_positive_period |
| smooth_right_rebound_5_20_near_neckline | mild_bull | 12 | 11 | 7 | 3 | 4 | 4 | 42.8571 | 36.3636 | not_directionally_positive_period |
| smooth_right_rebound_5_20_near_neckline | range_or_mixed | 33 | 31 | 20 | 6 | 11 | 14 | 30.0000 | 35.4839 | not_directionally_positive_period |
| smooth_right_rebound_5_20_near_neckline | strong_bull | 41 | 29 | 21 | 13 | 8 | 8 | 61.9048 | 27.5862 | directionally_positive_period |
| smooth_right_rebound_5_20_near_neckline | unknown | 4 | 4 | 3 | 2 | 1 | 1 | 66.6667 | 25.0000 | too_small_for_period_decision |
| price_le30_rebound_3_20_volume_red | correction | 112 | 104 | 80 | 30 | 24 | 50 | 37.5000 | 23.0769 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red | mild_bull | 55 | 49 | 36 | 17 | 13 | 19 | 47.2222 | 26.5306 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red | range_or_mixed | 183 | 169 | 111 | 45 | 58 | 66 | 40.5405 | 34.3195 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red | strong_bull | 233 | 162 | 111 | 46 | 51 | 65 | 41.4414 | 31.4815 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red | unknown | 23 | 23 | 13 | 5 | 10 | 8 | 38.4615 | 43.4783 | not_directionally_positive_period |
| price_le30_rebound_5_20_volume_red | correction | 80 | 75 | 59 | 23 | 16 | 36 | 38.9831 | 21.3333 | not_directionally_positive_period |
| price_le30_rebound_5_20_volume_red | mild_bull | 41 | 38 | 27 | 12 | 11 | 15 | 44.4444 | 28.9474 | not_directionally_positive_period |
| price_le30_rebound_5_20_volume_red | range_or_mixed | 121 | 110 | 71 | 31 | 39 | 40 | 43.6620 | 35.4545 | not_directionally_positive_period |
| price_le30_rebound_5_20_volume_red | strong_bull | 143 | 100 | 67 | 30 | 33 | 37 | 44.7761 | 33.0000 | not_directionally_positive_period |
| price_le30_rebound_5_20_volume_red | unknown | 16 | 16 | 9 | 4 | 7 | 5 | 44.4444 | 43.7500 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red_below_neckline5 | correction | 77 | 73 | 52 | 21 | 21 | 31 | 40.3846 | 28.7671 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red_below_neckline5 | mild_bull | 22 | 18 | 15 | 7 | 3 | 8 | 46.6667 | 16.6667 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red_below_neckline5 | range_or_mixed | 107 | 97 | 64 | 27 | 33 | 37 | 42.1875 | 34.0206 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red_below_neckline5 | strong_bull | 123 | 82 | 54 | 18 | 28 | 36 | 33.3333 | 34.1463 | not_directionally_positive_period |
| price_le30_rebound_3_20_volume_red_below_neckline5 | unknown | 15 | 15 | 7 | 2 | 8 | 5 | 28.5714 | 53.3333 | not_directionally_positive_period |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | correction | 64 | 60 | 43 | 17 | 17 | 26 | 39.5349 | 28.3333 | not_directionally_positive_period |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | mild_bull | 39 | 36 | 28 | 12 | 8 | 16 | 42.8571 | 22.2222 | not_directionally_positive_period |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | range_or_mixed | 123 | 114 | 71 | 30 | 43 | 41 | 42.2535 | 37.7193 | not_directionally_positive_period |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | strong_bull | 152 | 113 | 82 | 38 | 31 | 44 | 46.3415 | 27.4336 | not_directionally_positive_period |
| bottom_or_low_rebound_3_20_volume_red_exclude_wv | unknown | 10 | 10 | 7 | 3 | 3 | 4 | 42.8571 | 30.0000 | not_directionally_positive_period |
| core_mainstream_price_le30_rebound_3_20_volume_red | correction | 53 | 52 | 41 | 17 | 11 | 24 | 41.4634 | 21.1538 | not_directionally_positive_period |
| core_mainstream_price_le30_rebound_3_20_volume_red | mild_bull | 27 | 24 | 18 | 10 | 6 | 8 | 55.5556 | 25.0000 | directionally_positive_period |
| core_mainstream_price_le30_rebound_3_20_volume_red | range_or_mixed | 110 | 101 | 64 | 29 | 37 | 35 | 45.3125 | 36.6337 | not_directionally_positive_period |
| core_mainstream_price_le30_rebound_3_20_volume_red | strong_bull | 117 | 82 | 60 | 27 | 22 | 33 | 45.0000 | 26.8293 | not_directionally_positive_period |
| core_mainstream_price_le30_rebound_3_20_volume_red | unknown | 15 | 15 | 9 | 4 | 6 | 5 | 44.4444 | 40.0000 | not_directionally_positive_period |
| core_or_hot_price_le30_rebound_3_20_volume_red | correction | 53 | 52 | 41 | 17 | 11 | 24 | 41.4634 | 21.1538 | not_directionally_positive_period |
| core_or_hot_price_le30_rebound_3_20_volume_red | mild_bull | 27 | 24 | 18 | 10 | 6 | 8 | 55.5556 | 25.0000 | directionally_positive_period |
| core_or_hot_price_le30_rebound_3_20_volume_red | range_or_mixed | 110 | 101 | 64 | 29 | 37 | 35 | 45.3125 | 36.6337 | not_directionally_positive_period |
| core_or_hot_price_le30_rebound_3_20_volume_red | strong_bull | 117 | 82 | 60 | 27 | 22 | 33 | 45.0000 | 26.8293 | not_directionally_positive_period |
| core_or_hot_price_le30_rebound_3_20_volume_red | unknown | 15 | 15 | 9 | 4 | 6 | 5 | 44.4444 | 40.0000 | not_directionally_positive_period |
| smooth_price_le30_rebound_3_20_volume_red | correction | 13 | 10 | 8 | 2 | 2 | 6 | 25.0000 | 20.0000 | not_directionally_positive_period |
| smooth_price_le30_rebound_3_20_volume_red | mild_bull | 11 | 10 | 8 | 4 | 2 | 4 | 50.0000 | 20.0000 | not_directionally_positive_period |
| smooth_price_le30_rebound_3_20_volume_red | range_or_mixed | 42 | 38 | 23 | 9 | 15 | 14 | 39.1304 | 39.4737 | not_directionally_positive_period |
| smooth_price_le30_rebound_3_20_volume_red | strong_bull | 54 | 38 | 28 | 15 | 10 | 13 | 53.5714 | 26.3158 | not_directionally_positive_period |
| smooth_price_le30_rebound_3_20_volume_red | unknown | 4 | 4 | 3 | 2 | 1 | 1 | 66.6667 | 25.0000 | too_small_for_period_decision |
| smooth_price_le30_rebound_5_20_volume_red | correction | 8 | 7 | 6 | 2 | 1 | 4 | 33.3333 | 14.2857 | not_directionally_positive_period |
| smooth_price_le30_rebound_5_20_volume_red | mild_bull | 8 | 8 | 6 | 3 | 2 | 3 | 50.0000 | 25.0000 | not_directionally_positive_period |
| smooth_price_le30_rebound_5_20_volume_red | range_or_mixed | 30 | 27 | 16 | 6 | 11 | 10 | 37.5000 | 40.7407 | not_directionally_positive_period |
| smooth_price_le30_rebound_5_20_volume_red | strong_bull | 31 | 20 | 14 | 9 | 6 | 5 | 64.2857 | 30.0000 | directionally_positive_period |
| smooth_price_le30_rebound_5_20_volume_red | unknown | 2 | 2 | 2 | 2 | 0 | 0 | 100.0000 | 0.0000 | too_small_for_period_decision |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Stability failures block promotion; they do not imply production drift.
