# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-26 22:09:04 Asia/Taipei`
- main_price_date: `20260526`
- watch_rows: `206`
- strict_60d_volume_breakout_count: `38`
- broad_recall_watch_count: `57`
- selected_but_routed_to_other_category_count: `65`
- not_selected_by_candidate_model_count: `91`
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
| 1 | 2453 | 凌群 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_many_days | 7.4734 | 13.0275 | 15.7895 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 3311 | 閎暉 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | strong_accumulation | first_seen | 5.4784 | 14.5161 | 14.3317 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 6799 | 來頡 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | first_seen | 4.6182 | 20.5212 | 23.1964 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 2476 | 鉅祥 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 2.0875 | 13.913 | 8.7137 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 6277 | 宏正 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 3.033 | 7.8838 | 12.3919 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 6491 | 晶碩 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | first_seen | 2.6131 | 6.383 | 13.438 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 2881 | 富邦金 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | continued_many_days | 2.5933 | 6.4815 | 17.7474 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 1563 | 巧新 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 1.8392 | 11.6998 | 24.0196 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 1618 | 合機 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | first_seen | 5.6527 | 11.0236 | 8.6008 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 2731 | 雄獅 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | first_seen | 2.8349 | 4.6729 | 5.9937 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 2606 | 裕民 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | repeated_but_no_breakout | 1.9709 | 10.2362 | 15.894 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 12 | 1530 | 亞崴 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.7153 | 17.033 | 21.0227 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 3168 | 眾福科 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.4814 | 16.165 | 19.6326 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 2908 | 特力 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6993 | 2.1531 | 3.1401 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 6855 | 數泓科 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.5135 | 8.2927 | 5.7143 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 2321 | 東訊 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1832 | 13.4921 | 7.5188 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 8342 | 益張 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.1268 | 0.3289 | -1.6129 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 8416 | 實威 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.0592 | 0.5831 | 0.0 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 4305 | 世坤 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.2512 | 0.0 | 0.0 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 8077 | 洛碁 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.0 | 4.3779 | 9.1566 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 2937 | 集雅社 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.6863 | 3.355 | 6.8233 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 7708 | 全家餐飲 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.5938 | 0.4348 | 0.8734 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 4198 | 欣大健康 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.5616 | 6.9705 | 3.9062 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4719 | 1.072 | 5.6 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 1583 | 程泰 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.3226 | 3.9625 | 5.7264 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 4771 | 望隼 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9814 | 0.5038 | 5.277 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 2459 | 敦吉 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9434 | 1.3616 | 0.2994 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 3426 | 台興 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6216 | 0.0 | 0.2099 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 1733 | 五鼎 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6133 | 2.5597 | 5.6239 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 1256 | 鮮活果汁-KY | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5543 | 6.812 | 24.4444 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 1709 | 和益 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  | continued_2_3d | 1.5537 | 5.4795 | 0.7853 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 7747 | 昕奇雲端 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.2121 | 2.3622 | -0.7634 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 8466 | 美吉吉-KY | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8563 | 10.3806 | -0.6231 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 6680 | 鑫創電子 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.3728 | 8.2707 | 0.3484 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 5205 | 中茂 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.7429 | 11.1888 | -0.4175 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 6904 | 伯鑫 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 7.5974 | 0.0 | -1.2658 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 8921 | 沈氏 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7308 | 3.9326 | 8.8235 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 4139 | 馬光-KY | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6727 | 2.5751 | 1.7021 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 2882 | 國泰金 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | revenue_pullback |  | B_confirm_needed | mild_accumulation | continued_many_days | 1.4589 | 6.8123 | 11.5436 |  | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 2885 | 元大金 | loose_platform_volume_watch | broad_watch | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.3889 | 4.7532 | 12.7953 |  | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1618 | 合機 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 2731 | 雄獅 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2606 | 裕民 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1530 | 亞崴 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3168 | 眾福科 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2908 | 特力 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6855 | 數泓科 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2321 | 東訊 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8342 | 益張 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8416 | 實威 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4305 | 世坤 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8077 | 洛碁 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2937 | 集雅社 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 7708 | 全家餐飲 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4198 | 欣大健康 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1583 | 程泰 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4771 | 望隼 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2459 | 敦吉 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3426 | 台興 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1733 | 五鼎 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1256 | 鮮活果汁-KY | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1709 | 和益 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 7747 | 昕奇雲端 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8466 | 美吉吉-KY | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6680 | 鑫創電子 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 5205 | 中茂 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6904 | 伯鑫 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8921 | 沈氏 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4139 | 馬光-KY | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 975 | 964 | 0.2892 | 41.39 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3049 | 2840 | 0.7042 | 43.2 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok |
| volume_breakout_type | loose_platform_volume_watch | 7430 | 6932 | 0.4971 | 42.34 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok |
| volume_breakout_type | loose_right_side_volume_watch | 1081 | 984 | 0.9715 | 45.63 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok |
| volume_breakout_type | neckline_volume_breakout | 3423 | 3118 | 0.8926 | 44.23 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3510 | 3470 | 1.1457 | 44.9 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3118 | 3025 | 2.1753 | 47.87 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2314 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10147 | 9996 | 0.6773 | 43.17 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok |
| volume_watch_scope | broad_watch | 11560 | 10756 | 0.5952 | 42.87 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok |
| volume_watch_scope | confirmed_attack | 6933 | 6588 | 1.0259 | 44.58 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok |
| volume_watch_scope | strict_breakout | 2314 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_watch_scope | volume_attack | 14240 | 13985 | 0.9746 | 44.06 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok |
| false_breakout_risk | False | 20649 | 19760 | 0.9534 | 43.53 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok |
| false_breakout_risk | True | 14398 | 13785 | 0.9083 | 44.79 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok |
| overheated_breakout | False | 30293 | 29036 | 0.7945 | 43.44 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok |
| overheated_breakout | True | 4754 | 4509 | 1.8388 | 47.97 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

