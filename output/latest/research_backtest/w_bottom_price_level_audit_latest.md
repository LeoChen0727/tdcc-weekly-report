# W-Bottom Price Level Audit

- generated_at: `2026-06-25 12:42:20 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- source_research_id: `w_bottom_path_quality_filter_audit`
- detail_rows: `470`
- lookback_days_requested: `252`
- min_price_history_days: `180`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: the existing W-bottom source already applies a coarse long-position gate of signal close <= 252-day median close; this audit makes that gate visible and adds low/high-range position buckets.

## Price Level Buckets

| bucket | definition |
| --- | --- |
| bottom_quartile_level | signal close is in the bottom 0-25% of the lookback low/high range |
| low_level | signal close is in the 25-40% range |
| mid_level | signal close is in the 40-60% range |
| high_level | signal close is above 60% of the lookback range |

## Bucket Counts

| price_level_bucket | candidate_count |
| --- | --- |
| bottom_quartile_level | 259 |
| high_level | 5 |
| low_level | 149 |
| mid_level | 57 |

## Summary

| summary_scope | price_level_bucket | sample_size | mature_sample_size | win_rate_pct | avg_a_return_pct | median_a_return_pct | volume_confirmation_rate_pct | avg_price_position_252_pct | below_252_median_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_w_bottom_candidates | all | 470 | 52 | 30.7692 | 0.1621 | -1.7857 | 9.3617 | 24.9680 | 470 |
| all_w_bottom_candidates | bottom_quartile_level | 259 | 24 | 33.3333 | 1.4497 | -1.7857 | 7.7220 | 15.6181 | 259 |
| all_w_bottom_candidates | low_level | 149 | 21 | 33.3333 | -0.7633 | -1.6568 | 12.0805 | 31.5496 | 149 |
| all_w_bottom_candidates | mid_level | 57 | 7 | 14.2857 | -1.4765 | -3.1146 | 10.5263 | 46.9733 | 57 |
| all_w_bottom_candidates | high_level | 5 | 0 |  |  |  | 0.0000 | 62.3001 | 5 |
| observation_to_volume_confirmation | all | 44 | 40 | 32.5000 | 0.8501 | -1.7857 | 100.0000 | 26.9060 | 44 |
| observation_to_volume_confirmation | bottom_quartile_level | 20 | 18 | 33.3333 | 1.6232 | -1.7857 | 100.0000 | 16.6363 | 20 |
| observation_to_volume_confirmation | low_level | 18 | 16 | 37.5000 | 0.8917 | -0.8284 | 100.0000 | 31.3989 | 18 |
| observation_to_volume_confirmation | mid_level | 6 | 6 | 16.6667 | -1.5801 | -3.2522 | 100.0000 | 47.6597 | 6 |
| core_mainstream_observation_volume_exclude_wv | all | 10 | 9 | 66.6667 | 4.5533 | 6.1947 | 100.0000 | 33.5419 | 10 |
| core_mainstream_observation_volume_exclude_wv | bottom_quartile_level | 3 | 3 | 100.0000 | 9.4294 | 8.2474 | 100.0000 | 17.7030 | 3 |
| core_mainstream_observation_volume_exclude_wv | low_level | 3 | 2 | 100.0000 | 5.7671 | 5.7671 | 100.0000 | 31.6584 | 3 |
| core_mainstream_observation_volume_exclude_wv | mid_level | 4 | 4 | 25.0000 | 0.2893 | -2.2181 | 100.0000 | 46.8338 | 4 |

## Core-Mainstream Exclude-WV Detail

| stock_id | stock_name | signal_date | price_level_bucket | price_position_252_pct | below_252_median | below_252_mean | a_mature | a_return_pct | slope_curvature_category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1618 | 合機 | 20260114 | mid_level | 50.905 | true | true | true | -1.3216 | smooth_rounded_w_like |
| 6415 | 矽力*-KY | 20260115 | bottom_quartile_level | 12.8295 | true | true | true | 13.8462 | sharp_v_bottom_risk |
| 3596 | 智易 | 20260204 | bottom_quartile_level | 16.2651 | true | true | true | 8.2474 | slope_break_discontinuous |
| 3029 | 零壹 | 20260223 | mid_level | 45.8824 | true | true | true | -3.3898 | slope_break_discontinuous |
| 3005 | 神基 | 20260225 | low_level | 36.9104 | true | true | true | 8.4 | smooth_rounded_w_like |
| 6414 | 樺漢 | 20260401 | mid_level | 50.4348 | true | true | true | 8.9831 | smooth_rounded_w_like |
| 3168 | 眾福科 | 20260409 | mid_level | 40.113 | true | true | true | -3.1146 | slope_break_discontinuous |
| 3694 | 海華 | 20260518 | low_level | 27.0191 | true | true | true | 3.1343 | sharp_v_bottom_risk |
| 2362 | 藍天 | 20260521 | bottom_quartile_level | 24.0143 | true | true | true | 6.1947 | slope_break_discontinuous |
| 6243 | 迅杰 | 20260616 | low_level | 31.0458 | true | true | false |  | sharp_v_bottom_risk |

## Reading Notes

- If low-level buckets outperform mid/high buckets consistently, price level can become a candidate research filter.
- If the current 252-day median gate already removes every high-level case, the next discussion should focus on whether bottom-quartile or low-level should be required for W-bottom observation.
- This is research-only evidence. Any formal W-bottom production change still needs a separate promotion/model-change PR.
