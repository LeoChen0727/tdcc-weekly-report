# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-27 21:17:40 Asia/Taipei`
- main_price_date: `20260527`
- watch_rows: `196`
- strict_60d_volume_breakout_count: `25`
- broad_recall_watch_count: `52`
- selected_but_routed_to_other_category_count: `72`
- not_selected_by_candidate_model_count: `90`
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
| 1 | 2438 | 翔耀 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 6.2077 | 17.6744 | 12.9464 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2881 | 富邦金 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | strong_accumulation | continued_many_days | 2.1933 | 14.8225 | 24.1535 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 2606 | 裕民 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | strong_accumulation | continued_many_days | 1.9354 | 12.4031 | 20.0331 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 2425 | 承啟 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | first_seen | 1.8984 | 11.7917 | 21.6667 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 2929 | 淘帝-KY | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | strong_accumulation | continued_2_3d | 2.4955 | 28.6267 | 18.75 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 1810 | 和成 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 4.5796 | 8.1522 | 14.0401 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 6691 | 洋基工程 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | first_seen | 2.1038 | 9.9511 | 5.6426 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 2637 | 慧洋-KY | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.027 | 5.7103 | 6.1538 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 2535 | 達欣工 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 1.786 | 4.5576 | 3.8615 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 2206 | 三陽工業 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.5011 | 2.5729 | 4.9123 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 3321 | 同泰 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | strong_accumulation | continued_overheated | 4.0543 | 24.5098 | 17.2308 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 12 | 1583 | 程泰 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9986 | 14.2251 | 13.3825 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 4545 | 銘鈺 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.6991 | 21.2625 | 21.8698 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 3131 | 弘塑 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9885 | 32.7519 | 19.338 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 3067 | 全域 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.989 | 6.9364 | 0.5435 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 6957 | 裕慶-KY | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9052 | 5.625 | 7.3016 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 7791 | 皇家可口 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.797 | 4.9285 | 2.3256 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 2434 | 統懋 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.3728 | 11.7845 | 9.9338 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 4198 | 欣大健康 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.125 | 4.1885 | 3.781 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 2373 | 震旦行 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9371 | 2.6549 | 1.9332 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 6606 | 建德工業 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.8765 | 5.5328 | 5.102 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1922 | -0.9091 | 4.9759 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 2727 | 王品 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6831 | -0.2132 | 2.407 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 3426 | 台興 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.641 | 0.1048 | 0.2099 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 2849 | 安泰銀 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5072 | 4.943 | -0.7194 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 5274 | 信驊 | abnormal_volume_up | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.7819 | 17.1594 | 13.265 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 1418 | 東華 | abnormal_volume_up | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.7486 | 5.0279 | 5.0279 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 7770 | 君曜 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2388 | 14.3035 | -4.8654 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 2254 | 巨鎧精密-創 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.553 | 11.7241 | -11.1111 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 3310 | 佳穎 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.3358 | 11.1756 | 9.8996 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 3285 | 微端 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.2133 | 11.5789 | 13.369 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 6680 | 鑫創電子 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.0446 | 8.8346 | 6.2385 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 1315 | 達新 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.097 | 2.649 | -1.2739 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 3226 | 龍鋒 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.8777 | 4.4025 | 4.798 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 1259 | 安心 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.6977 | 1.7544 | -2.3569 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 2949 | 欣新網 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.5767 | 4.8253 | 12.5 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 7732 | 金興精密 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0199 | 3.4783 | 0.8475 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 7716 | 昱臺國際 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0161 | 3.2653 | 0.0 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 6670 | 復盛應用 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8607 | 1.1583 | 4.175 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 4737 | 華廣 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7012 | 3.0928 | -4.7619 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2929 | 淘帝-KY | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1810 | 和成 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 6691 | 洋基工程 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 2637 | 慧洋-KY | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2535 | 達欣工 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2206 | 三陽工業 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1583 | 程泰 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4545 | 銘鈺 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3131 | 弘塑 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3067 | 全域 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6957 | 裕慶-KY | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 7791 | 皇家可口 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2434 | 統懋 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4198 | 欣大健康 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2373 | 震旦行 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6606 | 建德工業 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2727 | 王品 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3426 | 台興 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2849 | 安泰銀 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 5274 | 信驊 | abnormal_volume_up | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1418 | 東華 | abnormal_volume_up | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 7770 | 君曜 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2254 | 巨鎧精密-創 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3310 | 佳穎 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3285 | 微端 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6680 | 鑫創電子 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1315 | 達新 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3226 | 龍鋒 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1259 | 安心 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 980 | 964 | 0.2892 | 41.39 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3063 | 2840 | 0.7042 | 43.2 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok |
| volume_breakout_type | loose_platform_volume_watch | 7463 | 6932 | 0.4971 | 42.34 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok |
| volume_breakout_type | loose_right_side_volume_watch | 1086 | 984 | 0.9715 | 45.63 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok |
| volume_breakout_type | neckline_volume_breakout | 3450 | 3118 | 0.8926 | 44.23 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3518 | 3470 | 1.1457 | 44.9 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3135 | 3025 | 2.1753 | 47.87 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2339 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10209 | 9996 | 0.6773 | 43.17 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok |
| volume_watch_scope | broad_watch | 11612 | 10756 | 0.5952 | 42.87 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok |
| volume_watch_scope | confirmed_attack | 6968 | 6588 | 1.0259 | 44.58 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok |
| volume_watch_scope | strict_breakout | 2339 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_watch_scope | volume_attack | 14324 | 13985 | 0.9746 | 44.06 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok |
| false_breakout_risk | False | 20752 | 19760 | 0.9534 | 43.53 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok |
| false_breakout_risk | True | 14491 | 13785 | 0.9083 | 44.79 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok |
| overheated_breakout | False | 30453 | 29036 | 0.7945 | 43.44 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok |
| overheated_breakout | True | 4790 | 4509 | 1.8388 | 47.97 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

