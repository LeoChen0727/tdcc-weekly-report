# W-Bottom Candidate Definition Audit

- generated_at: `2026-06-25 11:16:25 Asia/Taipei`
- model_id: `w_bottom_right_side`
- source_research_id: `w_bottom_candidate_chart_review`
- source_candidate_set_id: `grid_gap_2_20_rebound_7_12_vol_1_2`
- rows: `68`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.

## Definition Rules Tested

- prior downtrend: left peak to first low decline at least `8.0%`.
- support zone: second low must be within `+/-6.0%` of first low.
- effective break: second low must not be more than `3.0%` below first low.
- neckline: middle rebound high must be at least `6.0%` above both lows.
- right-side support: right low must not later be broken by `3.0%`.

## Headline Counts

| metric | count | rate |
| --- | ---: | ---: |
| definition base ok | 66 | 97.06% |
| price neckline breakout confirmed | 23 | 33.82% |
| volume confirmed breakout | 11 | 16.18% |

## Definition Status Counts

| definition_status | count |
| --- | --- |
| late_or_no_breakout | 29 |
| support_failed | 15 |
| definition_confirmed_with_volume | 11 |
| price_confirmed_without_volume | 11 |
| invalid_definition_structure | 2 |

## Issue Reasons

| issue_reason | count |
| --- | --- |
| right_low_support_broken_after_signal | 15 |
| no_neckline_breakout_observed | 15 |
| neckline_completion_or_breakout_too_late | 14 |
| neckline_price_confirmed_volume_missing | 11 |
| definition_confirmed_and_volume_breakout | 11 |
| prior_downtrend_missing | 2 |

## Definition X Slope Category

| definition_status | slope_curvature_category | count |
| --- | --- | --- |
| definition_confirmed_with_volume | sharp_v_bottom_risk | 2 |
| definition_confirmed_with_volume | slope_break_discontinuous | 1 |
| definition_confirmed_with_volume | wv_multiple_turn_risk | 8 |
| invalid_definition_structure | slope_break_discontinuous | 1 |
| invalid_definition_structure | wv_multiple_turn_risk | 1 |
| late_or_no_breakout | sharp_v_bottom_risk | 4 |
| late_or_no_breakout | slope_break_discontinuous | 2 |
| late_or_no_breakout | smooth_rounded_w_like | 3 |
| late_or_no_breakout | wv_multiple_turn_risk | 20 |
| price_confirmed_without_volume | sharp_v_bottom_risk | 1 |
| price_confirmed_without_volume | slope_break_discontinuous | 1 |
| price_confirmed_without_volume | smooth_rounded_w_like | 1 |
| price_confirmed_without_volume | wv_multiple_turn_risk | 8 |
| support_failed | sharp_v_bottom_risk | 6 |
| support_failed | slope_break_discontinuous | 1 |
| support_failed | smooth_rounded_w_like | 2 |
| support_failed | wv_multiple_turn_risk | 6 |

## Review Sample

| stock_id | signal_date | definition_status | definition_issue_reasons | support_gap_pct | prior_downtrend_pct | right_low_to_neckline_pct | chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2611 | 20260303 | support_failed | right_low_support_broken_after_signal | -2.7211 | -9.816 | 11.1888 | output/latest/research_backtest/w_bottom_candidate_chart_review/03_candidate_selected_too_near_neckline/20260303_2611_candidate_selected_too_near_neckline.png |
| 2365 | 20260430 | price_confirmed_without_volume | neckline_price_confirmed_volume_missing | 4.9839 | -29.3182 | 12.7106 | output/latest/research_backtest/w_bottom_candidate_chart_review/03_candidate_selected_too_near_neckline/20260430_2365_candidate_selected_too_near_neckline.png |
| 4562 | 20260106 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 3.6982 | -33.5953 | 21.826 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260106_4562_completion_too_late_for_w.png |
| 2027 | 20260107 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -0.8571 | -18.6047 | 12.8242 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260107_2027_completion_too_late_for_w.png |
| 2359 | 20260107 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 5.5085 | -23.3766 | 18.0723 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260107_2359_completion_too_late_for_w.png |
| 2474 | 20260122 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 3.9773 | -19.2661 | 16.3934 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260122_2474_completion_too_late_for_w.png |
| 3592 | 20260209 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 1.7032 | -32.5123 | 15.311 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260209_3592_completion_too_late_for_w.png |
| 4961 | 20260209 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -1.4652 | -23.743 | 12.2677 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260209_4961_completion_too_late_for_w.png |
| 3034 | 20260223 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -2.2222 | -10.0 | 15.3409 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260223_3034_completion_too_late_for_w.png |
| 6141 | 20260224 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 0.4926 | -21.3178 | 13.7255 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260224_6141_completion_too_late_for_w.png |
| 3311 | 20260303 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 0.1642 | -11.4826 | 15.082 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260303_3311_completion_too_late_for_w.png |
| 1805 | 20260408 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 0.0 | -23.0769 | 21.5 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260408_1805_completion_too_late_for_w.png |
| 2364 | 20260408 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -0.1678 | -12.9927 | 11.9328 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260408_2364_completion_too_late_for_w.png |
| 2911 | 20260414 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -0.4237 | -17.6265 | 22.9787 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260414_2911_completion_too_late_for_w.png |
| 2438 | 20260415 | late_or_no_breakout | neckline_completion_or_breakout_too_late | -0.2457 | -18.7625 | 22.6601 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260415_2438_completion_too_late_for_w.png |
| 2636 | 20260420 | invalid_definition_structure | prior_downtrend_missing | -2.3585 | -7.4236 | 11.9163 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260420_2636_completion_too_late_for_w.png |
| 1805 | 20260603 | late_or_no_breakout | neckline_completion_or_breakout_too_late | 0.0 | -23.0769 | 21.5 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260603_1805_completion_too_late_for_w.png |
| 6916 | 20260225 | late_or_no_breakout | no_neckline_breakout_observed | 3.5821 | -18.2927 | 22.7666 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260225_6916_did_not_complete_w.png |
| 6582 | 20260326 | late_or_no_breakout | no_neckline_breakout_observed | -1.4682 | -14.3855 | 27.8146 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260326_6582_did_not_complete_w.png |
| 2387 | 20260401 | late_or_no_breakout | no_neckline_breakout_observed | -1.3263 | -8.8271 | 26.3441 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260401_2387_did_not_complete_w.png |
| 1339 | 20260423 | late_or_no_breakout | no_neckline_breakout_observed | -2.8916 | -13.9004 | 17.9901 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260423_1339_did_not_complete_w.png |
| 1722 | 20260504 | invalid_definition_structure | prior_downtrend_missing | -2.5054 | -7.7387 | 16.2011 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260504_1722_did_not_complete_w.png |
| 3011 | 20260521 | late_or_no_breakout | no_neckline_breakout_observed | 3.4188 | -25.9494 | 32.6446 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260521_3011_did_not_complete_w.png |
| 1536 | 20260522 | late_or_no_breakout | no_neckline_breakout_observed | 1.6985 | -30.531 | 19.6242 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260522_1536_did_not_complete_w.png |
| 1467 | 20260601 | late_or_no_breakout | no_neckline_breakout_observed | -2.1459 | -14.5477 | 23.2456 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260601_1467_did_not_complete_w.png |
| 2022 | 20260604 | late_or_no_breakout | no_neckline_breakout_observed | 0.2674 | -24.8241 | 10.9333 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260604_2022_did_not_complete_w.png |
| 4763 | 20260604 | late_or_no_breakout | no_neckline_breakout_observed | -1.8315 | -28.1579 | 20.8955 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260604_4763_did_not_complete_w.png |
| 1909 | 20260608 | late_or_no_breakout | no_neckline_breakout_observed | -2.9768 | -12.7885 | 26.7045 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260608_1909_did_not_complete_w.png |
| 2723 | 20260611 | late_or_no_breakout | no_neckline_breakout_observed | 0.0 | -19.3717 | 13.1494 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260611_2723_did_not_complete_w.png |
| 3515 | 20260615 | late_or_no_breakout | no_neckline_breakout_observed | 4.3779 | -14.5669 | 20.7506 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260615_3515_did_not_complete_w.png |
