# W-Bottom Candidate Slope Curvature Audit

- generated_at: `2026-06-25 10:21:41 Asia/Taipei`
- model_id: `w_bottom_right_side`
- source_research_id: `w_bottom_candidate_chart_review`
- source_candidate_set_id: `grid_gap_2_20_rebound_7_12_vol_1_2`
- rows: `68`
- slope_review_root: `output\latest\research_backtest\w_bottom_candidate_slope_curvature_review`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.

## Classification Logic

- Uses close-to-close daily slope and 3-day smoothed slope.
- Flags sharp V when 3-day average slope before a low is strongly negative, after the low is strongly positive, and the slope reversal is abrupt.
- Flags WV/multiple-turn risk when the smoothed close path has too many significant turns.
- Flags slope discontinuity when slope changes or direction switches are too frequent.

## Slope Category Counts

| slope_curvature_category | slope_category_folder | chart_count |
| --- | --- | --- |
| smooth_rounded_w_like | 01_smooth_rounded_w_like | 6 |
| sharp_v_bottom_risk | 02_sharp_v_bottom_risk | 13 |
| wv_multiple_turn_risk | 03_wv_multiple_turn_risk | 43 |
| slope_break_discontinuous | 04_slope_break_discontinuous | 6 |

## Issue Reasons

| issue_reason | count |
| --- | --- |
| too_many_significant_turns | 43 |
| second_low_sharp_v | 10 |
| smooth_enough_for_manual_review | 6 |
| too_many_direction_switches | 6 |
| first_low_sharp_v | 3 |
| large_single_slope_break | 1 |

## Outcome X Slope Category

| outcome_category_id | slope_curvature_category | count |
| --- | --- | --- |
| candidate_selected_too_near_neckline | smooth_rounded_w_like | 1 |
| candidate_selected_too_near_neckline | wv_multiple_turn_risk | 1 |
| completion_too_late_for_w | sharp_v_bottom_risk | 1 |
| completion_too_late_for_w | slope_break_discontinuous | 2 |
| completion_too_late_for_w | smooth_rounded_w_like | 2 |
| completion_too_late_for_w | wv_multiple_turn_risk | 10 |
| did_not_complete_w | sharp_v_bottom_risk | 3 |
| did_not_complete_w | slope_break_discontinuous | 1 |
| did_not_complete_w | smooth_rounded_w_like | 1 |
| did_not_complete_w | wv_multiple_turn_risk | 11 |
| passed_volume_breakout_confirmation | sharp_v_bottom_risk | 2 |
| passed_volume_breakout_confirmation | slope_break_discontinuous | 1 |
| passed_volume_breakout_confirmation | wv_multiple_turn_risk | 8 |
| right_low_failed | sharp_v_bottom_risk | 6 |
| right_low_failed | slope_break_discontinuous | 1 |
| right_low_failed | smooth_rounded_w_like | 1 |
| right_low_failed | wv_multiple_turn_risk | 6 |
| shape_completed_but_volume_missing | sharp_v_bottom_risk | 1 |
| shape_completed_but_volume_missing | slope_break_discontinuous | 1 |
| shape_completed_but_volume_missing | smooth_rounded_w_like | 1 |
| shape_completed_but_volume_missing | wv_multiple_turn_risk | 7 |

## Review Index Sample

| stock_id | signal_date | outcome_category_id | slope_curvature_category | full_path_significant_turn_count | full_path_abrupt_slope_change_count | first_low_sharp_v_flag | second_low_sharp_v_flag | slope_review_chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2611 | 20260303 | candidate_selected_too_near_neckline | smooth_rounded_w_like | 3 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/01_smooth_rounded_w_like/20260303_2611_candidate_selected_too_near_neckline.png |
| 2365 | 20260430 | candidate_selected_too_near_neckline | wv_multiple_turn_risk | 7 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260430_2365_candidate_selected_too_near_neckline.png |
| 4562 | 20260106 | completion_too_late_for_w | wv_multiple_turn_risk | 10 | 6 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260106_4562_completion_too_late_for_w.png |
| 2027 | 20260107 | completion_too_late_for_w | wv_multiple_turn_risk | 6 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260107_2027_completion_too_late_for_w.png |
| 2359 | 20260107 | completion_too_late_for_w | wv_multiple_turn_risk | 7 | 2 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260107_2359_completion_too_late_for_w.png |
| 2474 | 20260122 | completion_too_late_for_w | wv_multiple_turn_risk | 8 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260122_2474_completion_too_late_for_w.png |
| 3592 | 20260209 | completion_too_late_for_w | wv_multiple_turn_risk | 9 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260209_3592_completion_too_late_for_w.png |
| 4961 | 20260209 | completion_too_late_for_w | wv_multiple_turn_risk | 8 | 2 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260209_4961_completion_too_late_for_w.png |
| 3034 | 20260223 | completion_too_late_for_w | smooth_rounded_w_like | 3 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/01_smooth_rounded_w_like/20260223_3034_completion_too_late_for_w.png |
| 6141 | 20260224 | completion_too_late_for_w | sharp_v_bottom_risk | 11 | 4 | false | true | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/02_sharp_v_bottom_risk/20260224_6141_completion_too_late_for_w.png |
| 3311 | 20260303 | completion_too_late_for_w | smooth_rounded_w_like | 3 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/01_smooth_rounded_w_like/20260303_3311_completion_too_late_for_w.png |
| 1805 | 20260408 | completion_too_late_for_w | wv_multiple_turn_risk | 5 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260408_1805_completion_too_late_for_w.png |
| 2364 | 20260408 | completion_too_late_for_w | slope_break_discontinuous | 4 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/04_slope_break_discontinuous/20260408_2364_completion_too_late_for_w.png |
| 2911 | 20260414 | completion_too_late_for_w | slope_break_discontinuous | 3 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/04_slope_break_discontinuous/20260414_2911_completion_too_late_for_w.png |
| 2438 | 20260415 | completion_too_late_for_w | wv_multiple_turn_risk | 7 | 2 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260415_2438_completion_too_late_for_w.png |
| 2636 | 20260420 | completion_too_late_for_w | wv_multiple_turn_risk | 5 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260420_2636_completion_too_late_for_w.png |
| 1805 | 20260603 | completion_too_late_for_w | wv_multiple_turn_risk | 8 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260603_1805_completion_too_late_for_w.png |
| 6916 | 20260225 | did_not_complete_w | wv_multiple_turn_risk | 10 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260225_6916_did_not_complete_w.png |
| 6582 | 20260326 | did_not_complete_w | wv_multiple_turn_risk | 7 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260326_6582_did_not_complete_w.png |
| 2387 | 20260401 | did_not_complete_w | wv_multiple_turn_risk | 6 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260401_2387_did_not_complete_w.png |
| 1339 | 20260423 | did_not_complete_w | wv_multiple_turn_risk | 5 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260423_1339_did_not_complete_w.png |
| 1722 | 20260504 | did_not_complete_w | slope_break_discontinuous | 3 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/04_slope_break_discontinuous/20260504_1722_did_not_complete_w.png |
| 3011 | 20260521 | did_not_complete_w | sharp_v_bottom_risk | 7 | 1 | false | true | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/02_sharp_v_bottom_risk/20260521_3011_did_not_complete_w.png |
| 1536 | 20260522 | did_not_complete_w | wv_multiple_turn_risk | 9 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260522_1536_did_not_complete_w.png |
| 1467 | 20260601 | did_not_complete_w | wv_multiple_turn_risk | 5 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260601_1467_did_not_complete_w.png |
| 2022 | 20260604 | did_not_complete_w | sharp_v_bottom_risk | 5 | 0 | true | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/02_sharp_v_bottom_risk/20260604_2022_did_not_complete_w.png |
| 4763 | 20260604 | did_not_complete_w | wv_multiple_turn_risk | 11 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260604_4763_did_not_complete_w.png |
| 1909 | 20260608 | did_not_complete_w | wv_multiple_turn_risk | 7 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260608_1909_did_not_complete_w.png |
| 2723 | 20260611 | did_not_complete_w | wv_multiple_turn_risk | 7 | 0 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/03_wv_multiple_turn_risk/20260611_2723_did_not_complete_w.png |
| 3515 | 20260615 | did_not_complete_w | smooth_rounded_w_like | 4 | 1 | false | false | output/latest/research_backtest/w_bottom_candidate_slope_curvature_review/01_smooth_rounded_w_like/20260615_3515_did_not_complete_w.png |
