# W-Bottom Left-Anchor Rule Grid

- generated_at: `2026-06-25 14:00:38 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- research_id: `w_bottom_left_anchor_rule_grid`
- source_research_id: `w_bottom_left_anchor_pattern_family_audit`
- source_rows: `471`
- detail_rows: `2355`
- summary_rows: `5`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: this is a research-only comparison of left-anchor selection rules for standard-W candidates.

## Rule Summary

| rule_id | selected_count | anchor_changed_count | human_match_count | avg_candidate_days_before_left_low | median_candidate_days_before_left_low | avg_drop_to_left_low_pct | avg_left_descent_wrong_direction_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| current_detector_left_peak | 471 | 0 | 0 | 32.1231 | 35.0 | -16.6756 | 33.0573 |
| highest_high_45d_before_left_low | 471 | 104 | 0 | 35.552 | 40.0 | -17.378 | 33.8072 |
| highest_high_90d_before_left_low | 471 | 401 | 0 | 66.6008 | 71.0 | -23.7616 | 36.0618 |
| nearest_micro_pressure_45d_min15_before_left_low | 309 | 253 | 1 | 22.4693 | 21.0 | -15.8061 | 30.2674 |
| nearest_micro_pressure_90d_min15_before_left_low | 425 | 369 | 1 | 32.5035 | 27.0 | -15.6492 | 31.9549 |

## Key Cases

| stock_id | stock_name | rule_id | human_left_peak_date | baseline_current_left_peak_date | candidate_left_peak_date | candidate_days_before_left_low | candidate_drop_to_left_low_pct | candidate_matches_human_left_peak | candidate_selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6415 | 矽力*-KY | current_detector_left_peak |  | 20250918 | 20250918 | 41 | -41.443 | false | selected_current_detector_left_peak |
| 6415 | 矽力*-KY | highest_high_45d_before_left_low |  | 20250918 | 20250909 | 45 | -42.1227 | false | selected_highest_high_in_45d_window |
| 6415 | 矽力*-KY | highest_high_90d_before_left_low |  | 20250918 | 20250718 | 81 | -51.257 | false | selected_highest_high_in_90d_window |
| 6415 | 矽力*-KY | nearest_micro_pressure_45d_min15_before_left_low |  | 20250918 | 20251107 | 11 | -22.2717 | false | selected_nearest_micro_peak_with_min_15pct_drop_and_min_8d_left_leg |
| 6415 | 矽力*-KY | nearest_micro_pressure_90d_min15_before_left_low |  | 20250918 | 20251107 | 11 | -22.2717 | false | selected_nearest_micro_peak_with_min_15pct_drop_and_min_8d_left_leg |
| 8069 | 元太 | current_detector_left_peak | 20260312 | 20260211 | 20260211 | 26 | -29.7158 | false | selected_current_detector_left_peak |
| 8069 | 元太 | highest_high_45d_before_left_low | 20260312 | 20260211 | 20260211 | 26 | -29.7158 | false | selected_highest_high_in_45d_window |
| 8069 | 元太 | highest_high_90d_before_left_low | 20260312 | 20260211 | 20251121 | 82 | -32.5062 | false | selected_highest_high_in_90d_window |
| 8069 | 元太 | nearest_micro_pressure_45d_min15_before_left_low | 20260312 | 20260211 | 20260311 | 14 | -17.3252 | true | selected_nearest_micro_peak_with_min_15pct_drop_and_min_8d_left_leg |
| 8069 | 元太 | nearest_micro_pressure_90d_min15_before_left_low | 20260312 | 20260211 | 20260311 | 14 | -17.3252 | true | selected_nearest_micro_peak_with_min_15pct_drop_and_min_8d_left_leg |

## Reading Notes

- `current_detector_left_peak` preserves the existing research detector output.
- `highest_high_90d_before_left_low` exposes whether the current 45-day window truncates a much earlier, higher structural start.
- `nearest_micro_pressure_*` tests a human-like idea: prefer the nearest small-turn pressure high before the first low instead of the absolute highest high, while still requiring at least `15.0`% drop and `8` trading days for the left leg.
- This grid compares anchor choices only. It does not prove a production model improvement and must not be promoted without a separate backtest/promotion PR.
