# W-Bottom Early-Entry Stability Audit

- generated_at: `2026-06-26 21:31:47 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- scope: variant nearest-micro event replay, split by signal month and quarter.
- limitation: current available signal window is 2026-01 to 2026-06, so this is a short-window stability check, not long-term evidence.

## Strict Segment Monthly Rollup

| segment_id | period_count | periods_with_mature_ge5 | periods_with_mature_ge10 | sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | min_period_win_rate_pct | max_period_win_rate_pct | stability_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 20 | 8 | 2 | 172 | 95 | 43 | 46 | 52 | 45.2632 | 32.6241 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_price_le40_right_rebound_5_20 | 20 | 8 | 1 | 158 | 86 | 38 | 41 | 48 | 44.1860 | 32.2835 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_core_mainstream_right_rebound_5_20 | 17 | 4 | 1 | 95 | 52 | 28 | 28 | 24 | 53.8462 | 35.0000 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 17 | 3 | 0 | 85 | 44 | 23 | 26 | 21 | 52.2727 | 37.1429 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_right_rebound_5_20_red_ratio_gt_first | 19 | 5 | 0 | 100 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_right_rebound_5_20_near_neckline | 18 | 6 | 0 | 102 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | 0.0000 | 100.0000 | insufficient_period_coverage_for_promotion |

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
| 2026-04 | 14 | 11 | 9 | 7 | 2 | 2 | 3 | 77.7778 | 18.1818 | directionally_positive_period |
| 2026-05 | 14 | 0 | 0 | 0 | 0 | 0 | 14 |  |  | future_window_incomplete |
| 2026-06 | 14 | 0 | 0 | 0 | 0 | 0 | 14 |  |  | future_window_incomplete |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Stability failures block promotion; they do not imply production drift.
