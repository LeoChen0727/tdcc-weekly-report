# W-Bottom Early-Entry Stability Audit

- generated_at: `2026-06-27 00:20:19 Asia/Taipei`
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

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Stability failures block promotion; they do not imply production drift.
