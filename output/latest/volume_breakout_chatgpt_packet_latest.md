# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-26 05:53:31 Asia/Taipei`
- main_price_date: `20260526`
- watch_rows: `71`
- strict_60d_volume_breakout_count: `0`
- selected_but_routed_to_other_category_count: `46`
- not_selected_by_candidate_model_count: `25`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Why Strict Breakout May Look Empty

- `breakout_latest.csv` only reflects strict 60-day volume-confirmed breakout logic.
- Many volume attacks are routed to `range_rebound` or `pattern_watch` when they are near a neckline/platform but not a strict 60-day breakout.
- ChatGPT should read this packet when the user asks about 帶量突破 / 放量突破 / 放量攻擊.

## Top Volume Breakout Watch

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2353 | 宏碁 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | 接近突破型 | C_watch_only | mild_accumulation | repeated_but_no_breakout | 2.4741 | 14.4366 | 18.83 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2493 | 揚博 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.0025 | 9.9631 | 19.6787 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 1709 | 和益 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.4398 | 4.0761 | 1.3228 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 2030 | 彰源 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | continued_2_3d | 2.1309 | 6.6282 | 12.8049 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 6668 | 中揚光 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.0442 | 4.0558 | 21.0914 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 3004 | 豐達科 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.8289 | 11.5079 | 20.6009 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 2328 | 廣宇 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.6423 | 8.4453 | 19.7034 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 2637 | 慧洋-KY | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.8873 | 4.4506 | 4.8883 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 2031 | 新光鋼 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | continued_2_3d | 1.6737 | 3.2595 | -3.06 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 1409 | 新纖 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.5373 | 3.8348 | 3.5294 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 3168 | 眾福科 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.5963 | 8.8428 | 14.4661 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 12 | 3021 | 鴻名 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  | continued_2_3d | 4.3136 | 20.7602 | 25.5319 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 1568 | 倉佑 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.7986 | 12.3023 | 12.3023 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 1525 | 江申 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.3194 | 20.339 | 13.6 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 2032 | 新鋼 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.2837 | 9.3373 | 9.6677 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 8201 | 無敵 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9323 | 6.1303 | 7.7821 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 1713 | 國化 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2552 | 2.1898 | 4.9251 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 1733 | 五鼎 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.223 | 1.528 | 4.1812 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 0055 | 元大MSCI金融 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9299 | -0.1177 | 1.3433 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 3038 | 全台 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8299 | 4.2129 | 2.3965 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 3617 | 碩天 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6448 | 4.3147 | 7.874 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 4581 | 光隆精密-KY | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6077 | 1.9211 | 1.4085 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 2114 | 鑫永銓 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5659 | 2.2321 | 3.386 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 1232 | 大統益 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5226 | 0.3378 | -0.3356 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 1530 | 亞崴 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.1332 | 4.4964 | 9.6226 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 6464 | 台數科 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.6375 | 0.0 | 3.1746 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 1419 | 新紡 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9819 | 5.44 | 3.6164 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 1423 | 利華 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9678 | 1.2107 | 0.0 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 6277 | 宏正 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7628 | 1.4745 | 8.2976 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 3025 | 星通 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  | continued_2_3d | 1.941 | 20.8978 | 27.6144 | not_in_candidate_model/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 8499 | 鼎炫-KY | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.619 | 13.4948 | 26.1538 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 6906 | 現觀科 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.2702 | 20.8605 | 47.8469 | not_in_candidate_model/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 2484 | 希華 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  | repeated_but_no_breakout | 2.1549 | 20.8473 | 34.8259 | not_in_candidate_model/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 2911 | 麗嬰房 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9184 | 20.8861 | 79.8493 | not_in_candidate_model/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 4919 | 新唐 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6661 | 20.6612 | 51.5571 | not_in_candidate_model/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 3013 | 晟銘電 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | continued_overheated | 3.8068 | 20.8955 | 8.4821 | continued_overheated/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 37 | 2002 | 中鋼 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | continued_2_3d | 3.7377 | 9.6154 | 5.0 | decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 38 | 9103 | 美德醫療-DR | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | distribution_warning | continued_2_3d | 2.7535 | 11.0 | 18.0851 | tdcc_distribution_warning/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 39 | 6552 | 易華電 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | continued_overheated | 2.7375 | 20.9059 | 5.6317 | continued_overheated/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 40 | 2324 | 仁寶 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | pattern | 預備發動型 | D_risk_downgrade | mild_accumulation | stale_signal | 2.7105 | 14.168 | 16.6667 | stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2353 | 宏碁 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | 接近突破型 |  |
| 2493 | 揚博 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1709 | 和益 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2030 | 彰源 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 6668 | 中揚光 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3004 | 豐達科 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2328 | 廣宇 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2637 | 慧洋-KY | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2031 | 新光鋼 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1409 | 新纖 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3168 | 眾福科 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3021 | 鴻名 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1568 | 倉佑 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1525 | 江申 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2032 | 新鋼 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8201 | 無敵 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1713 | 國化 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1733 | 五鼎 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 0055 | 元大MSCI金融 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3038 | 全台 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3617 | 碩天 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4581 | 光隆精密-KY | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2114 | 鑫永銓 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1232 | 大統益 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1530 | 亞崴 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 6464 | 台數科 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 1419 | 新紡 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 1423 | 利華 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 6277 | 宏正 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 3025 | 星通 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/overheated_breakout |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 975 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| volume_breakout_type | neckline_volume_breakout | 3420 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| volume_breakout_type | platform_volume_breakout | 3495 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| volume_breakout_type | right_side_volume_attack | 3102 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| volume_breakout_type | strict_60d_volume_breakout | 2276 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| volume_breakout_type | volume_expansion_watch | 10130 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| false_breakout_risk | False | 14320 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| false_breakout_risk | True | 9078 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| overheated_breakout | False | 19236 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |
| overheated_breakout | True | 4162 | 0 |  |  | 0 |  |  | 0 |  |  | insufficient_sample |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

