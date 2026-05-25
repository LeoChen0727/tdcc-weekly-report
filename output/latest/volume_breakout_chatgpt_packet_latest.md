# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-26 06:32:51 Asia/Taipei`
- main_price_date: `20260526`
- watch_rows: `305`
- strict_60d_volume_breakout_count: `0`
- broad_recall_watch_count: `234`
- selected_but_routed_to_other_category_count: `181`
- not_selected_by_candidate_model_count: `124`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Why Strict Breakout May Look Empty

- `breakout_latest.csv` only reflects strict 60-day volume-confirmed breakout logic.
- Many volume attacks are routed to `range_rebound` or `pattern_watch` when they are near a neckline/platform but not a strict 60-day breakout.
- Broad recall rows are intentionally listed to reduce missed W-bottom/right-side/platform setups; they must be ranked by score and risk context before interpretation.
- ChatGPT should read this packet when the user asks about 帶量突破 / 放量突破 / 放量攻擊.

## Top Volume Breakout Watch

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2353 | 宏碁 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | 接近突破型 | C_watch_only | mild_accumulation | repeated_but_no_breakout | 2.4741 | 14.4366 | 18.83 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2493 | 揚博 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.0025 | 9.9631 | 19.6787 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 1709 | 和益 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.4398 | 4.0761 | 1.3228 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 2030 | 彰源 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | continued_2_3d | 2.1309 | 6.6282 | 12.8049 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 6668 | 中揚光 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.0442 | 4.0558 | 21.0914 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 3004 | 豐達科 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.8289 | 11.5079 | 20.6009 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 2328 | 廣宇 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.6423 | 8.4453 | 19.7034 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 2637 | 慧洋-KY | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.8873 | 4.4506 | 4.8883 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 2031 | 新光鋼 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | continued_2_3d | 1.6737 | 3.2595 | -3.06 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 1409 | 新纖 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.5373 | 3.8348 | 3.5294 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 3168 | 眾福科 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.5963 | 8.8428 | 14.4661 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 12 | 3021 | 鴻名 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  | continued_2_3d | 4.3136 | 20.7602 | 25.5319 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 1568 | 倉佑 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.7986 | 12.3023 | 12.3023 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 1525 | 江申 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.3194 | 20.339 | 13.6 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 2032 | 新鋼 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.2837 | 9.3373 | 9.6677 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 8201 | 無敵 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9323 | 6.1303 | 7.7821 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 1713 | 國化 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2552 | 2.1898 | 4.9251 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 1733 | 五鼎 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.223 | 1.528 | 4.1812 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 0055 | 元大MSCI金融 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9299 | -0.1177 | 1.3433 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 3038 | 全台 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8299 | 4.2129 | 2.3965 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 3617 | 碩天 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6448 | 4.3147 | 7.874 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 4581 | 光隆精密-KY | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6077 | 1.9211 | 1.4085 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 2114 | 鑫永銓 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5659 | 2.2321 | 3.386 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 1232 | 大統益 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5226 | 0.3378 | -0.3356 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 2014 | 中鴻 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 3.8737 | 9.2754 | 4.4321 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 2022 | 聚亨 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 3.3612 | 8.4656 | -0.4854 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 6226 | 光鼎 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 3.1731 | 12.0 | 5.2632 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 2369 | 菱生 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.0908 | 14.3333 | 13.5762 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 2017 | 官田鋼 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 3.1925 | 7.6023 | 4.3084 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 3050 | 鈺德 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | first_seen | 2.1389 | 4.9383 | 4.0816 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 2323 | 中環 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | neutral | first_seen | 1.9378 | 8.5193 | 4.3902 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 4755 | 三福化 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 1.6446 | 8.8968 | -1.9231 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 2406 | 國碩 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.3061 | 9.7087 | 10.9656 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 3229 | 晟鈦 | loose_right_side_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | continued_2_3d | 1.2414 | 15.6707 | 16.2884 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 1723 | 中碳 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | first_seen | 1.8451 | 1.5971 | 6.0256 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 1402 | 遠東新 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.8103 | 0.0 | 4.4146 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 1710 | 東聯 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.6712 | 0.3817 | -0.3788 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 1618 | 合機 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 1.6689 | 1.9231 | 1.7926 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 2009 | 第一銅 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.4867 | 4.768 | 6.9737 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 2882 | 國泰金 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | revenue_pullback |  | C_watch_only | mild_accumulation | repeated_but_no_breakout | 1.3403 | 3.5578 | 3.6896 |  | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2353 | 宏碁 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | 接近突破型 |  |
| 2493 | 揚博 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1709 | 和益 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2030 | 彰源 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 6668 | 中揚光 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3004 | 豐達科 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2328 | 廣宇 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2637 | 慧洋-KY | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2031 | 新光鋼 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1409 | 新纖 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3168 | 眾福科 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3021 | 鴻名 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1568 | 倉佑 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1525 | 江申 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2032 | 新鋼 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8201 | 無敵 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1713 | 國化 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1733 | 五鼎 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 0055 | 元大MSCI金融 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3038 | 全台 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3617 | 碩天 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4581 | 光隆精密-KY | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2114 | 鑫永銓 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1232 | 大統益 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2014 | 中鴻 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2022 | 聚亨 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 6226 | 光鼎 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2369 | 菱生 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2017 | 官田鋼 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3050 | 鈺德 | loose_platform_volume_watch | broad_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 974 | 964 | 0.2892 | 41.39 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3041 | 2840 | 0.7042 | 43.2 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok |
| volume_breakout_type | loose_platform_volume_watch | 7396 | 6932 | 0.4971 | 42.34 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok |
| volume_breakout_type | loose_right_side_volume_watch | 1077 | 984 | 0.9715 | 45.63 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok |
| volume_breakout_type | neckline_volume_breakout | 3397 | 3118 | 0.8926 | 44.23 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3495 | 3470 | 1.1457 | 44.9 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3101 | 3025 | 2.1753 | 47.87 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2276 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10100 | 9996 | 0.6773 | 43.17 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok |
| volume_watch_scope | broad_watch | 11514 | 10756 | 0.5952 | 42.87 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok |
| volume_watch_scope | confirmed_attack | 6892 | 6588 | 1.0259 | 44.58 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok |
| volume_watch_scope | strict_breakout | 2276 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_watch_scope | volume_attack | 14175 | 13985 | 0.9746 | 44.06 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok |
| false_breakout_risk | False | 20524 | 19760 | 0.9534 | 43.53 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok |
| false_breakout_risk | True | 14333 | 13785 | 0.9083 | 44.79 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok |
| overheated_breakout | False | 30160 | 29036 | 0.7945 | 43.44 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok |
| overheated_breakout | True | 4697 | 4509 | 1.8388 | 47.97 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

