# W-Bottom Candidate Chart Review Packet

- generated_at: `2026-06-24 22:51:18 Asia/Taipei`
- model_id: `w_bottom_right_side`
- source_candidate_set_id: `grid_gap_2_20_rebound_7_12_vol_1_2`
- chart_root: `output\latest\research_backtest\w_bottom_candidate_chart_review`
- chart_count: `68`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this packet does not update production model conditions, scoring, ranking, or baseline.

## Candidate Filter

| rule | value |
| --- | ---: |
| neckline gap min pct | 2.0 |
| neckline gap max pct | 20.0 |
| right rebound min pct | 7.0 |
| right rebound max pct | 12.0 |
| second arc volume ratio min | 1.2 |

## Folder Counts

| category_id | category_folder | chart_count |
| --- | --- | --- |
| passed_volume_breakout_confirmation | 01_passed_volume_breakout_confirmation | 11 |
| shape_completed_but_volume_missing | 02_shape_completed_but_volume_missing | 10 |
| candidate_selected_too_near_neckline | 03_candidate_selected_too_near_neckline | 2 |
| right_low_failed | 04_right_low_failed | 14 |
| completion_too_late_for_w | 05_completion_too_late_for_w | 15 |
| did_not_complete_w | 06_did_not_complete_w | 16 |

## Review Index Sample

| stock_id | signal_date | category_id | signal_distance_to_neckline_pct | signal_rebound_from_right_low_pct | second_arc_volume_ratio | chart_path |
| --- | --- | --- | --- | --- | --- | --- |
| 2611 | 20260303 | candidate_selected_too_near_neckline | -2.5157 | 8.3916 | 1.3042 | output/latest/research_backtest/w_bottom_candidate_chart_review/03_candidate_selected_too_near_neckline/20260303_2611_candidate_selected_too_near_neckline.png |
| 2365 | 20260430 | candidate_selected_too_near_neckline | -2.4457 | 9.9541 | 1.3889 | output/latest/research_backtest/w_bottom_candidate_chart_review/03_candidate_selected_too_near_neckline/20260430_2365_candidate_selected_too_near_neckline.png |
| 4562 | 20260106 | completion_too_late_for_w | -10.4215 | 9.1298 | 2.0782 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260106_4562_completion_too_late_for_w.png |
| 2027 | 20260107 | completion_too_late_for_w | -4.2146 | 8.0692 | 1.2655 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260107_2027_completion_too_late_for_w.png |
| 2359 | 20260107 | completion_too_late_for_w | -9.1837 | 7.2289 | 1.4389 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260107_2359_completion_too_late_for_w.png |
| 2474 | 20260122 | completion_too_late_for_w | -5.1643 | 10.3825 | 1.3878 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260122_2474_completion_too_late_for_w.png |
| 3592 | 20260209 | completion_too_late_for_w | -6.2241 | 8.134 | 2.021 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260209_3592_completion_too_late_for_w.png |
| 4961 | 20260209 | completion_too_late_for_w | -3.3113 | 8.5502 | 2.1664 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260209_4961_completion_too_late_for_w.png |
| 3034 | 20260223 | completion_too_late_for_w | -6.8966 | 7.3864 | 1.2333 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260223_3034_completion_too_late_for_w.png |
| 6141 | 20260224 | completion_too_late_for_w | -3.0172 | 10.2941 | 1.4822 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260224_6141_completion_too_late_for_w.png |
| 3311 | 20260303 | completion_too_late_for_w | -4.1311 | 10.3279 | 1.438 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260303_3311_completion_too_late_for_w.png |
| 1805 | 20260408 | completion_too_late_for_w | -10.6996 | 8.5 | 2.5066 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260408_1805_completion_too_late_for_w.png |
| 2364 | 20260408 | completion_too_late_for_w | -4.2042 | 7.2269 | 1.2701 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260408_2364_completion_too_late_for_w.png |
| 2911 | 20260414 | completion_too_late_for_w | -12.8028 | 7.234 | 1.2109 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260414_2911_completion_too_late_for_w.png |
| 2438 | 20260415 | completion_too_late_for_w | -12.0482 | 7.8818 | 1.2215 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260415_2438_completion_too_late_for_w.png |
| 2636 | 20260420 | completion_too_late_for_w | -2.1583 | 9.5008 | 1.3901 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260420_2636_completion_too_late_for_w.png |
| 1805 | 20260603 | completion_too_late_for_w | -9.465 | 10.0 | 1.2098 | output/latest/research_backtest/w_bottom_candidate_chart_review/05_completion_too_late_for_w/20260603_1805_completion_too_late_for_w.png |
| 6916 | 20260225 | did_not_complete_w | -11.5023 | 8.6455 | 2.2352 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260225_6916_did_not_complete_w.png |
| 6582 | 20260326 | did_not_complete_w | -15.9326 | 7.4503 | 1.501 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260326_6582_did_not_complete_w.png |
| 2387 | 20260401 | did_not_complete_w | -15.0 | 7.3925 | 2.3607 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260401_2387_did_not_complete_w.png |
| 1339 | 20260423 | did_not_complete_w | -5.7834 | 11.1663 | 1.4504 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260423_1339_did_not_complete_w.png |
| 1722 | 20260504 | did_not_complete_w | -7.2115 | 7.8212 | 2.1478 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260504_1722_did_not_complete_w.png |
| 3011 | 20260521 | did_not_complete_w | -16.1994 | 11.157 | 1.2547 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260521_3011_did_not_complete_w.png |
| 1536 | 20260522 | did_not_complete_w | -9.9476 | 7.7244 | 1.3305 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260522_1536_did_not_complete_w.png |
| 1467 | 20260601 | did_not_complete_w | -12.5741 | 7.7485 | 1.5089 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260601_1467_did_not_complete_w.png |
| 2022 | 20260604 | did_not_complete_w | -2.8846 | 7.7333 | 1.3629 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260604_2022_did_not_complete_w.png |
| 4763 | 20260604 | did_not_complete_w | -7.9218 | 11.3184 | 1.2026 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260604_4763_did_not_complete_w.png |
| 1909 | 20260608 | did_not_complete_w | -14.2601 | 8.6364 | 1.5423 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260608_1909_did_not_complete_w.png |
| 2723 | 20260611 | did_not_complete_w | -2.0086 | 10.8766 | 1.3399 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260611_2723_did_not_complete_w.png |
| 3515 | 20260615 | did_not_complete_w | -10.2377 | 8.3885 | 1.2667 | output/latest/research_backtest/w_bottom_candidate_chart_review/06_did_not_complete_w/20260615_3515_did_not_complete_w.png |

## Reading Notes

- Start with `01_passed_volume_breakout_confirmation` to see the cleanest successful examples.
- Use `02_shape_completed_but_volume_missing` to judge whether volume confirmation is too strict or correctly filtering weak W completions.
- Use `04_right_low_failed` to inspect which shapes should be rejected earlier.
- This packet is for manual shape review only and is not a production model change.
