# W-Bottom Observation vs Confirmation Audit

- generated_at: `2026-06-25 11:27:05 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- source_research_id: `w_bottom_candidate_quality_audit`
- rows: `470` dedup candidates
- manual_review_packet_rows: `68`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: observation-stage candidates and neckline-confirmation candidates are intentionally evaluated as separate research surfaces.

## Headline Counts

| metric | count | rate |
| --- | ---: | ---: |
| observation-stage eligible | 389 | 82.77% |
| volume-confirmed neckline breakout | 56 | 11.91% |
| price-confirmed without volume | 160 | 34.04% |
| in manual chart review packet | 68 | 14.47% |

## Initial Stage Counts

| bucket | count |
| --- | --- |
| right_side_observation_zone | 389 |
| near_neckline_at_signal | 43 |
| already_above_neckline_at_signal | 38 |

## Confirmation Stage Counts

| bucket | count |
| --- | --- |
| price_confirmed_without_volume | 160 |
| right_low_support_failed | 128 |
| late_confirmation_not_w | 58 |
| volume_confirmed_neckline_breakout | 56 |
| no_confirmation_within_symmetry | 38 |
| future_window_incomplete | 30 |

## Transition Status Counts

| bucket | count |
| --- | --- |
| observation_support_failed | 128 |
| observation_to_price_only_confirmation | 91 |
| not_observation_near_neckline_or_above | 69 |
| observation_late_confirmation_not_w | 58 |
| observation_to_volume_confirmation | 44 |
| observation_no_confirmation | 38 |
| observation_future_window_incomplete | 30 |
| near_neckline_or_above_volume_confirmation | 12 |

## Initial Stage X Confirmation Stage

| initial_stage | confirmation_stage | count |
| --- | --- | --- |
| already_above_neckline_at_signal | price_confirmed_without_volume | 28 |
| already_above_neckline_at_signal | volume_confirmed_neckline_breakout | 10 |
| near_neckline_at_signal | price_confirmed_without_volume | 41 |
| near_neckline_at_signal | volume_confirmed_neckline_breakout | 2 |
| right_side_observation_zone | future_window_incomplete | 30 |
| right_side_observation_zone | late_confirmation_not_w | 58 |
| right_side_observation_zone | no_confirmation_within_symmetry | 38 |
| right_side_observation_zone | price_confirmed_without_volume | 91 |
| right_side_observation_zone | right_low_support_failed | 128 |
| right_side_observation_zone | volume_confirmed_neckline_breakout | 44 |

## A-Path Performance By Transition Status

| transition_status | sample_size | mature_sample_size | win_rate | avg_a_return_pct | tdcc_any_age7_count |
| --- | --- | --- | --- | --- | --- |
| observation_support_failed | 128 | 0 |  |  | 0 |
| observation_to_price_only_confirmation | 91 | 0 |  |  | 0 |
| not_observation_near_neckline_or_above | 69 | 0 |  |  | 0 |
| observation_late_confirmation_not_w | 58 | 0 |  |  | 0 |
| observation_to_volume_confirmation | 44 | 40 | 32.50% | 0.8501 | 2 |
| observation_no_confirmation | 38 | 0 |  |  | 0 |
| observation_future_window_incomplete | 30 | 0 |  |  | 0 |
| near_neckline_or_above_volume_confirmation | 12 | 12 | 25.00% | -2.1312 | 0 |

## Manual Review Packet Cross-Check

| bucket | count |
| --- | --- |
| observation_late_confirmation_not_w | 15 |
| observation_support_failed | 14 |
| observation_to_price_only_confirmation | 12 |
| observation_to_volume_confirmation | 11 |
| observation_no_confirmation | 9 |
| observation_future_window_incomplete | 7 |

## Review Sample

| stock_id | signal_date | initial_stage | confirmation_stage | transition_status | primary_review_flag | definition_status | slope_curvature_category | a_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1102 | 20260105 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 2033 | 20260105 | right_side_observation_zone | no_confirmation_within_symmetry | observation_no_confirmation | did_not_complete_w |  |  |  |
| 2305 | 20260105 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 2504 | 20260105 | near_neckline_at_signal | price_confirmed_without_volume | not_observation_near_neckline_or_above | candidate_selected_too_near_neckline |  |  |  |
| 2615 | 20260105 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 6409 | 20260105 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed | support_failed | wv_multiple_turn_risk |  |
| 2347 | 20260106 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 2379 | 20260106 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 3617 | 20260106 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 4562 | 20260106 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w | late_or_no_breakout | wv_multiple_turn_risk |  |
| 9937 | 20260106 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 2027 | 20260107 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w | late_or_no_breakout | wv_multiple_turn_risk |  |
| 2359 | 20260107 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w | late_or_no_breakout | wv_multiple_turn_risk |  |
| 3027 | 20260107 | right_side_observation_zone | volume_confirmed_neckline_breakout | observation_to_volume_confirmation | passed_volume_breakout_confirmation | definition_confirmed_with_volume | wv_multiple_turn_risk | -9.5324 |
| 3062 | 20260107 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 4938 | 20260107 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 6994 | 20260107 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 1906 | 20260108 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 2017 | 20260108 | near_neckline_at_signal | price_confirmed_without_volume | not_observation_near_neckline_or_above | candidate_selected_too_near_neckline |  |  |  |
| 3592 | 20260108 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 4961 | 20260108 | near_neckline_at_signal | price_confirmed_without_volume | not_observation_near_neckline_or_above | candidate_selected_too_near_neckline |  |  |  |
| 5871 | 20260108 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 6176 | 20260108 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 6414 | 20260108 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 6592 | 20260108 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 8374 | 20260108 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | candidate_selected_too_near_neckline |  |  |  |
| 2393 | 20260109 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 3022 | 20260109 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 3714 | 20260109 | already_above_neckline_at_signal | price_confirmed_without_volume | not_observation_near_neckline_or_above | candidate_selected_too_near_neckline |  |  |  |
| 6901 | 20260109 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing | price_confirmed_without_volume | slope_break_discontinuous |  |
| 1310 | 20260112 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 4919 | 20260112 | already_above_neckline_at_signal | volume_confirmed_neckline_breakout | near_neckline_or_above_volume_confirmation | passed_volume_breakout_confirmation |  |  | -0.6711 |
| 5388 | 20260112 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 6550 | 20260112 | right_side_observation_zone | price_confirmed_without_volume | observation_to_price_only_confirmation | shape_completed_but_volume_missing |  |  |  |
| 8222 | 20260112 | near_neckline_at_signal | price_confirmed_without_volume | not_observation_near_neckline_or_above | candidate_selected_too_near_neckline |  |  |  |
| 8454 | 20260112 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 1454 | 20260113 | right_side_observation_zone | late_confirmation_not_w | observation_late_confirmation_not_w | completion_too_late_for_w |  |  |  |
| 2547 | 20260113 | right_side_observation_zone | volume_confirmed_neckline_breakout | observation_to_volume_confirmation | passed_volume_breakout_confirmation |  |  | -1.7857 |
| 4737 | 20260113 | right_side_observation_zone | right_low_support_failed | observation_support_failed | right_low_failed |  |  |  |
| 5269 | 20260113 | already_above_neckline_at_signal | volume_confirmed_neckline_breakout | near_neckline_or_above_volume_confirmation | passed_volume_breakout_confirmation |  |  | -4.1353 |
