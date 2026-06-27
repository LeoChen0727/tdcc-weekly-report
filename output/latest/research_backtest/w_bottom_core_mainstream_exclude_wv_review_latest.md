# W-Bottom Core-Mainstream Exclude-WV Review Packet

- generated_at: `2026-06-25 12:32:12 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- research_id: `w_bottom_core_mainstream_exclude_wv_review`
- source_research_id: `w_bottom_wv_filter_stability_grid`
- segment: `effective_mainstream_label=core_mainstream`
- filter: `exclude_wv_multiple_turn`
- transition_status: `observation_to_volume_confirmation`
- chart_root: `output\latest\research_backtest\w_bottom_core_mainstream_exclude_wv_review`
- candidate_count: `10`
- mature_sample_size: `9`
- win_rate: `66.67%`
- avg_a_return_pct: `4.5533`
- median_a_return_pct: `6.1947`
- tdcc_any_age7_count: `0`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this packet does not update production model conditions, scoring, ranking, or baseline.
- promotion boundary: `not_production_ready_research_only`; this is a manual chart-review packet for candidate quality.

## Why This Packet Exists

The prior WV/WVV stability grid showed the broad `exclude_wv_multiple_turn` filter is not stable enough for production.
The only segment with a useful research lead was `core_mainstream`, so this packet isolates those rows for manual shape review before any further model discussion.

## Path Category Counts

| slope_curvature_category | candidate_count |
| --- | --- |
| sharp_v_bottom_risk | 3 |
| slope_break_discontinuous | 4 |
| smooth_rounded_w_like | 3 |

## Review Index

| stock_id | stock_name | signal_date | slope_curvature_category | a_mature | a_return_pct | tdcc_any_age7 | structural_theme_bucket | chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1618 | 合機 | 20260114 | smooth_rounded_w_like | true | -1.3216 | false | power_grid_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260114_1618_smooth_rounded_w_like.png |
| 6415 | 矽力*-KY | 20260115 | sharp_v_bottom_risk | true | 13.8462 | false | semiconductor_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260115_6415_sharp_v_bottom_risk.png |
| 3596 | 智易 | 20260204 | slope_break_discontinuous | true | 8.2474 | false | low_earth_orbit_satellite_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260204_3596_slope_break_discontinuous.png |
| 3029 | 零壹 | 20260223 | slope_break_discontinuous | true | -3.3898 | false | information_service_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260223_3029_slope_break_discontinuous.png |
| 3005 | 神基 | 20260225 | smooth_rounded_w_like | true | 8.4 | false | computer_peripheral_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260225_3005_smooth_rounded_w_like.png |
| 6414 | 樺漢 | 20260401 | smooth_rounded_w_like | true | 8.9831 | false | computer_peripheral_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260401_6414_smooth_rounded_w_like.png |
| 3168 | 眾福科 | 20260409 | slope_break_discontinuous | true | -3.1146 | false | optoelectronics_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260409_3168_slope_break_discontinuous.png |
| 3694 | 海華 | 20260518 | sharp_v_bottom_risk | true | 3.1343 | false | networking_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260518_3694_sharp_v_bottom_risk.png |
| 2362 | 藍天 | 20260521 | slope_break_discontinuous | true | 6.1947 | false | computer_peripheral_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260521_2362_slope_break_discontinuous.png |
| 6243 | 迅杰 | 20260616 | sharp_v_bottom_risk | false |  | false | semiconductor_general_theme | output/latest/research_backtest/w_bottom_core_mainstream_exclude_wv_review/20260616_6243_sharp_v_bottom_risk.png |

## Reading Notes

- Confirm whether each chart is visually close enough to a real W-bottom path.
- Pay special attention to `sharp_v_bottom_risk` and `slope_break_discontinuous`; they are allowed here only because this packet excludes WV/WVV, not every other path issue.
- `tdcc_any_age7_count=0` means this packet does not prove TDCC support for the W-bottom observation stage.
- Keep this research-only unless a separate promotion PR is explicitly requested.
