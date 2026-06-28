# W-Bottom Path Quality Filter Audit

- generated_at: `2026-06-25 12:09:17 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- source_research_id: `w_bottom_observation_confirmation_audit`
- rows: `470` dedup candidates
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: path-quality filters are research-only candidates for manual review and later promotion analysis.

## Path Category Counts

| slope_curvature_category | count |
| --- | --- |
| wv_multiple_turn_risk | 286 |
| slope_break_discontinuous | 104 |
| smooth_rounded_w_like | 54 |
| sharp_v_bottom_risk | 26 |

## Filter Performance

| filter_id | sample_size | mature_sample_size | win_rate | avg_a_return_pct | median_a_return_pct | smooth_count | sharp_v_count | wv_multiple_turn_count | slope_break_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_volume_confirmed | 56 | 52 | 30.77% | 0.1621 | -1.7857 | 3 | 4 | 37 | 12 |
| observation_to_volume_confirmation | 44 | 40 | 32.50% | 0.8501 | -1.7857 | 3 | 3 | 27 | 11 |
| observation_volume_exclude_sharp_v | 41 | 38 | 28.95% | 0.4480 | -1.9085 | 3 | 0 | 27 | 11 |
| observation_volume_exclude_wv_multiple_turn | 17 | 15 | 40.00% | 1.6152 | -1.6568 | 3 | 3 | 0 | 11 |
| observation_volume_exclude_slope_break | 33 | 30 | 36.67% | 1.4272 | -1.0882 | 3 | 3 | 27 | 0 |
| observation_volume_exclude_sharp_v_and_wv | 14 | 13 | 30.77% | 0.5575 | -1.7857 | 3 | 0 | 0 | 11 |
| observation_volume_smooth_only | 3 | 3 | 66.67% | 5.3538 | 8.4000 | 3 | 0 | 0 | 0 |
| observation_volume_smooth_or_slope_break | 14 | 13 | 30.77% | 0.5575 | -1.7857 | 3 | 0 | 0 | 11 |

## Transition X Path Category

| transition_status | slope_curvature_category | count |
| --- | --- | --- |
| near_neckline_or_above_volume_confirmation | sharp_v_bottom_risk | 1 |
| near_neckline_or_above_volume_confirmation | slope_break_discontinuous | 1 |
| near_neckline_or_above_volume_confirmation | wv_multiple_turn_risk | 10 |
| not_observation_near_neckline_or_above | sharp_v_bottom_risk | 1 |
| not_observation_near_neckline_or_above | slope_break_discontinuous | 17 |
| not_observation_near_neckline_or_above | smooth_rounded_w_like | 5 |
| not_observation_near_neckline_or_above | wv_multiple_turn_risk | 46 |
| observation_future_window_incomplete | sharp_v_bottom_risk | 2 |
| observation_future_window_incomplete | slope_break_discontinuous | 3 |
| observation_future_window_incomplete | smooth_rounded_w_like | 3 |
| observation_future_window_incomplete | wv_multiple_turn_risk | 22 |
| observation_late_confirmation_not_w | sharp_v_bottom_risk | 4 |
| observation_late_confirmation_not_w | slope_break_discontinuous | 18 |
| observation_late_confirmation_not_w | smooth_rounded_w_like | 4 |
| observation_late_confirmation_not_w | wv_multiple_turn_risk | 32 |
| observation_no_confirmation | sharp_v_bottom_risk | 3 |
| observation_no_confirmation | slope_break_discontinuous | 7 |
| observation_no_confirmation | smooth_rounded_w_like | 7 |
| observation_no_confirmation | wv_multiple_turn_risk | 21 |
| observation_support_failed | sharp_v_bottom_risk | 8 |
| observation_support_failed | slope_break_discontinuous | 22 |
| observation_support_failed | smooth_rounded_w_like | 16 |
| observation_support_failed | wv_multiple_turn_risk | 82 |
| observation_to_price_only_confirmation | sharp_v_bottom_risk | 4 |
| observation_to_price_only_confirmation | slope_break_discontinuous | 25 |
| observation_to_price_only_confirmation | smooth_rounded_w_like | 16 |
| observation_to_price_only_confirmation | wv_multiple_turn_risk | 46 |
| observation_to_volume_confirmation | sharp_v_bottom_risk | 3 |
| observation_to_volume_confirmation | slope_break_discontinuous | 11 |
| observation_to_volume_confirmation | smooth_rounded_w_like | 3 |
| observation_to_volume_confirmation | wv_multiple_turn_risk | 27 |

## Review Sample

| stock_id | signal_date | transition_status | slope_curvature_category | slope_issue_reasons | a_return_pct |
| --- | --- | --- | --- | --- | --- |
| 1102 | 20260105 | observation_support_failed | smooth_rounded_w_like | smooth_enough_for_manual_review |  |
| 2033 | 20260105 | observation_no_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2305 | 20260105 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2504 | 20260105 | not_observation_near_neckline_or_above | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2615 | 20260105 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6409 | 20260105 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2347 | 20260106 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2379 | 20260106 | observation_to_price_only_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 3617 | 20260106 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 4562 | 20260106 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 9937 | 20260106 | observation_to_price_only_confirmation | slope_break_discontinuous | too_many_direction_switches |  |
| 2027 | 20260107 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2359 | 20260107 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 3027 | 20260107 | observation_to_volume_confirmation | wv_multiple_turn_risk | too_many_significant_turns | -9.5324 |
| 3062 | 20260107 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 4938 | 20260107 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6994 | 20260107 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 1906 | 20260108 | observation_support_failed | smooth_rounded_w_like | smooth_enough_for_manual_review |  |
| 2017 | 20260108 | not_observation_near_neckline_or_above | wv_multiple_turn_risk | too_many_significant_turns |  |
| 3592 | 20260108 | observation_to_price_only_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 4961 | 20260108 | not_observation_near_neckline_or_above | wv_multiple_turn_risk | too_many_significant_turns |  |
| 5871 | 20260108 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6176 | 20260108 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6414 | 20260108 | observation_late_confirmation_not_w | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6592 | 20260108 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 8374 | 20260108 | observation_to_price_only_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 2393 | 20260109 | observation_to_price_only_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 3022 | 20260109 | observation_support_failed | slope_break_discontinuous | too_many_direction_switches |  |
| 3714 | 20260109 | not_observation_near_neckline_or_above | wv_multiple_turn_risk | too_many_significant_turns |  |
| 6901 | 20260109 | observation_to_price_only_confirmation | slope_break_discontinuous | too_many_direction_switches |  |
| 1310 | 20260112 | observation_late_confirmation_not_w | sharp_v_bottom_risk | first_low_sharp_v |  |
| 4919 | 20260112 | near_neckline_or_above_volume_confirmation | wv_multiple_turn_risk | too_many_significant_turns | -0.6711 |
| 5388 | 20260112 | observation_to_price_only_confirmation | slope_break_discontinuous | too_many_direction_switches |  |
| 6550 | 20260112 | observation_to_price_only_confirmation | wv_multiple_turn_risk | too_many_significant_turns |  |
| 8222 | 20260112 | not_observation_near_neckline_or_above | wv_multiple_turn_risk | too_many_significant_turns |  |
| 8454 | 20260112 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 1454 | 20260113 | observation_late_confirmation_not_w | slope_break_discontinuous | too_many_direction_switches |  |
| 2547 | 20260113 | observation_to_volume_confirmation | slope_break_discontinuous | too_many_direction_switches | -1.7857 |
| 4737 | 20260113 | observation_support_failed | wv_multiple_turn_risk | too_many_significant_turns |  |
| 5269 | 20260113 | near_neckline_or_above_volume_confirmation | wv_multiple_turn_risk | too_many_significant_turns | -4.1353 |
