# W-Bottom Candidate Filter Grid

- generated_at: `2026-06-24 22:42:18 Asia/Taipei`
- model_id: `w_bottom_right_side`
- source_research_id: `w_bottom_candidate_quality_audit`
- rows: `170` candidate filter sets
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.
- purpose: compare research-only filters for reducing candidates that are too close to neckline or break the right-side low.

## Baseline

| metric | value |
| --- | ---: |
| sample_size | 470 |
| neckline_volume_breakout_rate | 11.9149% |
| right_low_failed_rate | 27.234% |
| too_near_neckline_rate | 16.383% |
| w_shape_completed_rate | 45.9574% |

## Promising Sets

| candidate_set_id | sample_size | neckline_volume_breakout_rate | right_low_failed_rate | too_near_neckline_rate | w_shape_completed_rate | review_score | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| grid_gap_2_20_rebound_7_12_vol_1_2 | 68 | 16.1765 | 20.5882 | 2.9412 | 33.8235 | 14.2647 | promising_for_manual_shape_review |

## Top Reviewable Sets By Descriptive Score

| candidate_set_id | sample_size | neckline_volume_breakout_rate | right_low_failed_rate | too_near_neckline_rate | w_shape_completed_rate | review_score | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| grid_gap_2_30_rebound_7_12_vol_1_2 | 69 | 15.942 | 20.2899 | 2.8986 | 34.7826 | 14.3478 | mixed_needs_chart_review |
| grid_gap_2_20_rebound_7_12_vol_1_2 | 68 | 16.1765 | 20.5882 | 2.9412 | 33.8235 | 14.2647 | promising_for_manual_shape_review |
| grid_gap_3_20_rebound_7_15_vol_1_2 | 72 | 15.2778 | 20.8333 | 1.3889 | 34.7222 | 14.2361 | mixed_needs_chart_review |
| grid_gap_3_15_rebound_7_15_vol_1_2 | 65 | 13.8462 | 18.4615 | 1.5385 | 35.3846 | 13.6923 | mixed_needs_chart_review |
| grid_gap_3_30_rebound_7_15_vol_1_2 | 74 | 14.8649 | 21.6216 | 1.3514 | 35.1351 | 13.6487 | mixed_needs_chart_review |
| grid_gap_3_30_rebound_7_12_vol_1_2 | 59 | 15.2542 | 22.0339 | 0.0 | 30.5085 | 13.644 | mixed_needs_chart_review |
| grid_gap_3_20_rebound_7_12_vol_1_2 | 58 | 15.5172 | 22.4138 | 0.0 | 29.3103 | 13.5344 | mixed_needs_chart_review |
| grid_gap_2_20_rebound_7_15_vol_1_2 | 85 | 15.2941 | 18.8235 | 5.8824 | 38.8235 | 13.5294 | mixed_needs_chart_review |
| grid_gap_2_30_rebound_7_15_vol_1_2 | 87 | 14.9425 | 19.5402 | 5.7471 | 39.0805 | 13.046 | mixed_needs_chart_review |
| grid_gap_2_15_rebound_7_15_vol_1_2 | 78 | 14.1026 | 16.6667 | 6.4103 | 39.7436 | 13.0128 | mixed_needs_chart_review |
| grid_gap_2_15_rebound_7_12_vol_1_2 | 62 | 14.5161 | 19.3548 | 3.2258 | 33.871 | 12.9032 | mixed_needs_chart_review |
| grid_gap_3_15_rebound_7_12_vol_1_2 | 52 | 13.4615 | 21.1538 | 0.0 | 28.8462 | 11.8269 | mixed_needs_chart_review |
| grid_gap_2_15_rebound_5_15_vol_1_2 | 143 | 11.1888 | 18.1818 | 4.8951 | 44.7552 | 11.3287 | mixed_needs_chart_review |
| grid_gap_2_15_rebound_5_12_vol_1_2 | 127 | 11.0236 | 19.685 | 3.1496 | 42.5197 | 11.063 | mixed_needs_chart_review |
| grid_gap_2_20_rebound_5_15_vol_1_2 | 161 | 11.8012 | 21.118 | 4.3478 | 41.6149 | 10.559 | mixed_needs_chart_review |
| grid_gap_2_20_rebound_5_12_vol_1_2 | 144 | 11.8056 | 22.2222 | 2.7778 | 39.5833 | 10.5556 | mixed_needs_chart_review |
| grid_gap_2_30_rebound_5_12_vol_1_2 | 148 | 11.4865 | 22.973 | 2.7027 | 39.1892 | 9.9324 | mixed_needs_chart_review |
| grid_gap_2_30_rebound_5_15_vol_1_2 | 166 | 11.4458 | 22.2892 | 4.2169 | 40.9639 | 9.7289 | mixed_needs_chart_review |
| grid_gap_3_15_rebound_5_15_vol_1_2 | 115 | 9.5652 | 20.8696 | 0.8696 | 39.1304 | 9.6521 | breakout_conversion_weaker_than_baseline |
| grid_gap_2_15_rebound_3_15_vol_1_2 | 325 | 12.3077 | 28.9231 | 2.4615 | 40.0 | 8.9539 | right_low_failure_still_high |

## Reading Notes

- `neckline_gap_min_pct=3` means the signal must be at least 3% below the neckline, which removes candidates already too close to the neckline.
- `neckline_gap_max_pct=15` means the signal cannot still be more than 15% below the neckline, which removes candidates that may be too early or not actually completing a W.
- `right_rebound_min_pct` tests whether waiting for a stronger rebound from the second low reduces right-low failure.
- `second_arc_volume_ratio_min` tests the user's W-bottom volume idea: the second arc average volume should exceed the first arc.
- `review_score` is only a descriptive research sorting aid, not a production ranking rule.
