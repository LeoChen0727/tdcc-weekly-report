# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-28 20:04:45 Asia/Taipei`
- main_price_date: `20260528`
- watch_rows: `215`
- strict_60d_volume_breakout_count: `19`
- broad_recall_watch_count: `63`
- selected_but_routed_to_other_category_count: `89`
- not_selected_by_candidate_model_count: `103`
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
| 1 | 1339 | 昭輝 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | neckline_breakout | A_priority_watch | strong_accumulation | first_seen | 5.4687 | 9.9265 | 7.1685 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 8454 | 富邦媒 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 2.9936 | 9.9476 | 21.7391 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 6862 | 三集瑞-KY | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | B_confirm_needed | neutral | repeated_but_no_breakout | 3.3862 | 12.0548 | 18.8953 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 1710 | 東聯 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.7134 | 3.0534 | 2.2727 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 1709 | 和益 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.7804 | 6.5217 | 3.7037 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 2434 | 統懋 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 6.8253 | 24.1497 | 23.3108 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 7 | 8416 | 實威 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.8028 | 8.6207 | 11.8343 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 8 | 4106 | 雃博 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.3152 | 3.0303 | 7.2072 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 9 | 1521 | 大億 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.9008 | 11.134 | 7.8 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 10 | 8104 | 錸寶 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.0941 | 18.6957 | 21.6939 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 11 | 2239 | 英利-KY | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0205 | 8.8889 | 11.6173 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 12 | 8077 | 洛碁 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9677 | 4.3527 | 5.1744 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 6605 | 帝寶 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.575 | 7.2519 | 11.5079 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 8342 | 益張 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.1458 | -0.8696 | -2.0408 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 6881 | 潤德 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.6061 | -0.1838 | 7.3123 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 5878 | 台名 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.5387 | 1.353 | 0.7335 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 3611 | 鼎翰 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1502 | 0.8 | -0.5263 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9814 | -2.4024 | 0.4637 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 6690 | 安碁資訊 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9042 | 0.5935 | 2.1084 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 8923 | 時報 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7021 | 3.3679 | -0.9926 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 1256 | 鮮活果汁-KY | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6236 | 5.3191 | 21.4724 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 2235 | 謚源 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1908 | 8.6735 | -2.5915 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 7728 | 光焱科技 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0852 | 8.3565 | 10.9843 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 3346 | 麗清 | right_side_volume_attack | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.2257 | 20.743 | 12.3919 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 1472 | 三洋實業 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.5846 | 1.9144 | -0.8762 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 1338 | 廣華-KY | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4616 | 0.9404 | -3.8806 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 4584 | 君帆 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.15 | -5.8824 | 3.7215 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 3531 | 先益 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1495 | -0.641 | 0.6494 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 6534 | 正瀚-創 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7603 | -0.9288 | 2.7837 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 2024 | 志聯 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6667 | 2.1739 | -0.3534 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 4706 | 大恭 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6244 | 3.2258 | -1.5385 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 6235 | 華孚 | right_side_volume_attack | volume_attack | C_watch_only | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | first_seen | 2.49 | 6.1743 | 0.0 |  | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 33 | 1522 | 堤維西 | right_side_volume_attack | volume_attack | C_watch_only | selected_but_routed_to_other_category | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.2812 | 6.0708 | 0.64 |  | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 34 | 1319 | 東陽 | right_side_volume_attack | volume_attack | C_watch_only | selected_but_routed_to_other_category | range_rebound | platform_right_side | B_confirm_needed | mild_accumulation | first_seen | 1.3189 | 7.99 | 15.6417 |  | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 35 | 6680 | 鑫創電子 | loose_platform_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 2.7553 | 8.2243 | 9.4518 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 36 | 2201 | 裕隆 | volume_expansion_watch | volume_attack | C_watch_only | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 1.7162 | 2.0522 | 0.5515 |  | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 37 | 1259 | 安心 | loose_platform_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 2.4116 | 2.8419 | -2.3609 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 38 | 2949 | 欣新網 | loose_platform_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 2.3596 | 4.1322 | 13.3094 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 39 | 6855 | 數泓科 | loose_right_side_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 3.1195 | 5.3659 | 2.3697 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |
| 40 | 8921 | 沈氏 | loose_platform_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 1.6 | 0.0 | 3.6415 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6862 | 三集瑞-KY | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1710 | 東聯 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1709 | 和益 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2434 | 統懋 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8416 | 實威 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4106 | 雃博 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1521 | 大億 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8104 | 錸寶 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2239 | 英利-KY | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8077 | 洛碁 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6605 | 帝寶 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8342 | 益張 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6881 | 潤德 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 5878 | 台名 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3611 | 鼎翰 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6844 | 諾貝兒 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6690 | 安碁資訊 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8923 | 時報 | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1256 | 鮮活果汁-KY | neckline_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2235 | 謚源 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 7728 | 光焱科技 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3346 | 麗清 | right_side_volume_attack | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1472 | 三洋實業 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1338 | 廣華-KY | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4584 | 君帆 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3531 | 先益 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6534 | 正瀚-創 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2024 | 志聯 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4706 | 大恭 | volume_expansion_watch | volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6235 | 華孚 | right_side_volume_attack | volume_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 987 | 964 | 0.2892 | 41.39 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3086 | 2840 | 0.7042 | 43.2 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok |
| volume_breakout_type | loose_platform_volume_watch | 7524 | 6932 | 0.4971 | 42.34 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok |
| volume_breakout_type | loose_right_side_volume_watch | 1088 | 984 | 0.9715 | 45.63 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok |
| volume_breakout_type | neckline_volume_breakout | 3527 | 3118 | 0.8926 | 44.23 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3533 | 3470 | 1.1457 | 44.9 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3154 | 3025 | 2.1753 | 47.87 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2373 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10314 | 9996 | 0.6773 | 43.17 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok |
| volume_watch_scope | broad_watch | 11698 | 10756 | 0.5952 | 42.87 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok |
| volume_watch_scope | confirmed_attack | 7060 | 6588 | 1.0259 | 44.58 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok |
| volume_watch_scope | strict_breakout | 2373 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_watch_scope | volume_attack | 14455 | 13985 | 0.9746 | 44.06 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok |
| false_breakout_risk | False | 20885 | 19760 | 0.9534 | 43.53 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok |
| false_breakout_risk | True | 14701 | 13785 | 0.9083 | 44.79 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok |
| overheated_breakout | False | 30712 | 29036 | 0.7945 | 43.44 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok |
| overheated_breakout | True | 4874 | 4509 | 1.8388 | 47.97 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

