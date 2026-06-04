# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-06-05 02:11:55 Asia/Taipei`
- main_price_date: `20260603`
- watch_rows: `507`
- strict_60d_volume_breakout_count: `56`
- broad_recall_watch_count: `148`
- selected_but_routed_to_other_category_count: `156`
- not_selected_by_candidate_model_count: `302`
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
| 1 | 1608 | 華榮 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 5.3553 | 17.0877 | 19.2133 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 1618 | 合機 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | neutral | repeated_but_no_breakout | 4.2669 | 8.134 | 17.4026 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 4588 | 玖鼎電力 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 3.7257 | 13.5714 | 5.6478 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 4976 | 佳凌 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.6388 | 12.1359 | 20.7317 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 5522 | 遠雄 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | revenue_breakout_low_response |  | C_watch_only | mild_accumulation | repeated_but_no_breakout | 1.723 | 7.0225 | 10.275 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 3050 | 鈺德 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | platform_right_side | B_confirm_needed | strong_accumulation | continued_2_3d | 5.9386 | 13.7097 | 16.0494 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 1110 | 東泥 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 4.7822 | 13.1206 | 5.6291 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 1313 | 聯成 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | early_entry_watch | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 4.2837 | 15.534 | 10.1852 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 5225 | 東科-KY | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 3.8922 | 11.3314 | 2.2107 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 1805 | 寶徠 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | strong_accumulation | first_seen | 3.0038 | 10.2204 | 2.3256 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 6768 | 志強-KY | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 2.1399 | 16.747 | 21.5809 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 12 | 2406 | 國碩 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.0168 | 8.8825 | 16.7435 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 13 | 1457 | 宜進 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | first_seen | 3.402 | 5.7348 | 1.0274 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 14 | 3622 | 洋華 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.89 | 5.4291 | 8.2734 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 15 | 2903 | 遠百 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.1409 | 3.653 | 1.3393 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 16 | 2915 | 潤泰全 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | platform_right_side | C_watch_only | mild_accumulation | continued_2_3d | 1.8575 | 9.6441 | 9.8964 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 17 | 1909 | 榮成 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 1.6651 | 5.1685 | 4.3478 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 18 | 1808 | 潤隆 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | revenue_breakout_low_response |  | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 2.865 | 8.2601 | 8.8339 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 19 | 8072 | 陞泰 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | first_seen | 1.9011 | 7.9566 | 5.291 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 20 | 2032 | 新鋼 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | early_entry_watch | C_watch_only | mild_accumulation | continued_2_3d | 1.6432 | 3.6111 | 18.038 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 21 | 2440 | 太空梭 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | continued_2_3d | 1.5839 | 7.4928 | 5.9659 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 22 | 1714 | 和桐 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 6.5187 | 17.0213 | 19.8257 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 2816 | 旺旺保 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 4.8735 | 9.8592 | 17.0 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 2009 | 第一銅 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 4.6628 | 13.8539 | 17.7083 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 3038 | 全台 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.9674 | 8.3871 | 8.6207 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 4306 | 炎洲 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.687 | 8.3333 | 14.1221 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 8077 | 洛碁 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.6309 | 15.4545 | 16.916 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 9934 | 成霖 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 3.2816 | 7.4423 | 12.8855 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 2852 | 第一保 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4719 | 3.9106 | 7.1017 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 3570 | 大塚 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7871 | 8.7719 | 13.4146 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 2392 | 正崴 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7738 | 17.4202 | 15.1239 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 1614 | 三洋電 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5685 | 9.3548 | 6.1033 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 2883 | 凱基金 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_as_strict_breakout | true_breakout | platform_breakout | C_watch_only | strong_accumulation | continued_overheated | 1.5656 | 15.2466 | 15.7658 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 2727 | 王品 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.524 | 2.5641 | 3.4483 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 1314 | 中石化 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 5.9679 | 17.1014 | 11.7566 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 1708 | 東鹼 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_as_strict_breakout | true_breakout | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 4.9856 | 12.7438 | 10.5867 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 1467 | 南緯 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.4345 | 13.2565 | 9.7765 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 3027 | 盛達 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 3.4158 | 18.8679 | 19.1892 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 1340 | 勝悅-KY | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.2138 | 9.2391 | 7.6786 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 1603 | 華電 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.1408 | 9.7913 | 6.875 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1608 | 華榮 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1618 | 合機 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 4588 | 玖鼎電力 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 4976 | 佳凌 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 5522 | 遠雄 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_revenue_breakout_low_response; strict_breakout_requires_60d_high_breakout | revenue_breakout_low_response |  |  |
| 3050 | 鈺德 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | platform_right_side |  |
| 1110 | 東泥 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1313 | 聯成 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | early_entry_watch |  |
| 5225 | 東科-KY | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1805 | 寶徠 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 6768 | 志強-KY | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2406 | 國碩 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1457 | 宜進 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 3622 | 洋華 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2903 | 遠百 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2915 | 潤泰全 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | platform_right_side |  |
| 1909 | 榮成 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 1808 | 潤隆 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_revenue_breakout_low_response; strict_breakout_requires_60d_high_breakout | revenue_breakout_low_response |  |  |
| 8072 | 陞泰 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2032 | 新鋼 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | early_entry_watch |  |
| 2816 | 旺旺保 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2009 | 第一銅 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | continued_overheated |
| 3038 | 全台 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4306 | 炎洲 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8077 | 洛碁 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2852 | 第一保 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3570 | 大塚 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2392 | 正崴 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1614 | 三洋電 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2727 | 王品 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 993 | 964 | 0.2892 | 41.39 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3101 | 2840 | 0.7042 | 43.2 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok |
| volume_breakout_type | loose_platform_volume_watch | 7596 | 6932 | 0.4971 | 42.34 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok |
| volume_breakout_type | loose_right_side_volume_watch | 1097 | 984 | 0.9715 | 45.63 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok |
| volume_breakout_type | neckline_volume_breakout | 3584 | 3118 | 0.8926 | 44.23 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3552 | 3470 | 1.1457 | 44.9 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3187 | 3025 | 2.1753 | 47.87 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2408 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10384 | 9996 | 0.6773 | 43.17 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok |
| volume_watch_scope | broad_watch | 11794 | 10756 | 0.5952 | 42.87 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok |
| volume_watch_scope | confirmed_attack | 7136 | 6588 | 1.0259 | 44.58 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok |
| volume_watch_scope | strict_breakout | 2408 | 2216 | 2.0624 | 48.06 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok |
| volume_watch_scope | volume_attack | 14564 | 13985 | 0.9746 | 44.06 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok |
| false_breakout_risk | False | 21074 | 19760 | 0.9534 | 43.53 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok |
| false_breakout_risk | True | 14828 | 13785 | 0.9083 | 44.79 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok |
| overheated_breakout | False | 30977 | 29036 | 0.7945 | 43.44 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok |
| overheated_breakout | True | 4925 | 4509 | 1.8388 | 47.97 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

