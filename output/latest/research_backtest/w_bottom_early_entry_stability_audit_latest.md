# W-Bottom Early-Entry Stability Audit

- generated_at: `2026-06-26 18:42:18 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- scope: variant nearest-micro event replay, split by signal month and quarter.
- limitation: current available signal window is 2026-01 to 2026-06, so this is a short-window stability check, not long-term evidence.

## Strict Segment Monthly Rollup

| segment_id | period_count | periods_with_mature_ge5 | periods_with_mature_ge10 | sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | min_period_win_rate_pct | max_period_win_rate_pct | stability_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 6 | 1 | 0 | 40 | 17 | 11 | 8 | 6 | 64.7059 | 32.0000 | 33.3333 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_price_le40_right_rebound_5_20 | 6 | 1 | 0 | 33 | 13 | 8 | 5 | 5 | 61.5385 | 27.7778 | 33.3333 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_core_mainstream_right_rebound_5_20 | 6 | 1 | 0 | 22 | 10 | 7 | 6 | 3 | 70.0000 | 37.5000 | 62.5000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 5 | 1 | 0 | 17 | 7 | 4 | 4 | 3 | 57.1429 | 36.3636 | 50.0000 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_right_rebound_5_20_red_ratio_gt_first | 6 | 1 | 0 | 25 | 9 | 5 | 6 | 4 | 55.5556 | 40.0000 | 33.3333 | 100.0000 | insufficient_period_coverage_for_promotion |
| smooth_right_rebound_5_20_near_neckline | 6 | 1 | 0 | 22 | 12 | 7 | 5 | 5 | 58.3333 | 29.4118 | 33.3333 | 100.0000 | insufficient_period_coverage_for_promotion |

## smooth_right_rebound_5_20 Monthly Detail

| period_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | incomplete_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01 | 13 | 13 | 9 | 5 | 4 | 4 | 0 | 55.5556 | 30.7692 | directionally_positive_period |
| 2026-02 | 4 | 4 | 3 | 1 | 1 | 2 | 0 | 33.3333 | 25.0000 | too_small_for_period_decision |
| 2026-03 | 3 | 3 | 1 | 1 | 2 | 0 | 0 | 100.0000 | 66.6667 | too_small_for_period_decision |
| 2026-04 | 7 | 5 | 4 | 4 | 1 | 0 | 2 | 100.0000 | 20.0000 | too_small_for_period_decision |
| 2026-05 | 5 | 0 | 0 | 0 | 0 | 0 | 5 |  |  | future_window_incomplete |
| 2026-06 | 8 | 0 | 0 | 0 | 0 | 0 | 8 |  |  | future_window_incomplete |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Stability failures block promotion; they do not imply production drift.
