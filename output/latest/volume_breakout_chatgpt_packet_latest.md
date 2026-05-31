# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-31 12:12:08 Asia/Taipei`
- main_price_date: `20260529`
- watch_rows: `315`
- strict_60d_volume_breakout_count: `35`
- broad_recall_watch_count: `96`
- selected_but_routed_to_other_category_count: `162`
- not_selected_by_candidate_model_count: `153`
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
| 1 | 2362 | 藍天 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | continued_2_3d | 4.4863 | 7.8335 | 14.4156 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2850 | 新產 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | revenue_pullback |  | B_confirm_needed | mild_accumulation | continued_2_3d | 3.5426 | 6.5934 | 9.3985 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 1447 | 力鵬 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | repeated_but_no_breakout | 1.8391 | 3.5 | 24.4489 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 1605 | 華新 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.807 | 6.1644 | 28.524 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 2405 | 輔信 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 4.8109 | 6.6465 | 18.0602 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 2206 | 三陽工業 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | 接近突破型 | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.0938 | 0.8319 | 9.1892 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 2601 | 益航 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.8611 | 4.175 | 4.5908 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 2597 | 潤弘 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.7659 | 1.5291 | 5.7325 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 8070 | 長華* | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | repeated_but_no_breakout | 2.0312 | 16.9265 | 9.4891 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 2610 | 華航 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 6.8362 | 2.965 | 6.7039 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 5876 | 上海商銀 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound |  | B_confirm_needed | mild_accumulation | continued_2_3d | 1.9764 | -0.7491 | 1.7926 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 12 | 5522 | 遠雄 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.9298 | 4.6043 | 5.6686 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 13 | 2882 | 國泰金 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.724 | 7.5282 | 11.0104 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 14 | 2883 | 凱基金 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | strong_accumulation | repeated_but_no_breakout | 1.6007 | 3.6866 | 4.6512 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 15 | 4306 | 炎洲 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.524 | 0.0 | 6.4394 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 16 | 2374 | 佳能 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.5163 | -0.2398 | 6.1224 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 17 | 1521 | 大億 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 6.725 | 22.5673 | 19.1147 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 4935 | 茂林-KY | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.8923 | 10.5405 | 9.0667 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 8077 | 洛碁 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.735 | 6.2569 | 9.7506 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 20 | 2114 | 鑫永銓 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2889 | 4.3285 | 6.2147 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 21 | 0057 | 富邦摩台 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2745 | 6.98 | 14.4547 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 22 | 2816 | 旺旺保 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5253 | 5.1613 | 7.4135 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 23 | 1522 | 堤維西 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 6.1023 | 17.3175 | 11.6317 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 24 | 1319 | 東陽 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.1425 | 16.5441 | 27.139 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 25 | 3226 | 龍鋒 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4581 | 11.375 | 12.0755 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 26 | 8472 | 夠麻吉 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.3511 | 12.536 | 15.7037 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 27 | 2247 | 汎德永業 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 5.6107 | 7.971 | 5.1765 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 5520 | 力泰 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.5169 | 0.9732 | 5.7325 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 1617 | 榮星 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.177 | 7.047 | 6.3333 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 2949 | 欣新網 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1212 | 2.5848 | 16.7279 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 5209 | 新鼎 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0479 | 3.3033 | 5.5215 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 3067 | 全域 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8905 | 13.0435 | 11.4286 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 6894 | 衛司特 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7569 | 8.6471 | 16.0954 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 6881 | 潤德 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.0474 | -0.9158 | 6.7061 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 4305 | 世坤 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.6829 | -0.565 | 1.3825 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 2382 | 廣達 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | stale_signal | 2.5198 | 7.2785 | 8.48 | stale_signal | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 6556 | 勝品 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4476 | -0.9901 | 0.0 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 7708 | 全家餐飲 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.4306 | 0.6536 | 0.7634 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 5878 | 台名 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2841 | 0.4878 | 0.8568 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 0061 | 元大寶滬深 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1851 | 2.0656 | 3.2787 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2362 | 藍天 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2850 | 新產 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_revenue_pullback; strict_breakout_requires_60d_high_breakout | revenue_pullback |  |  |
| 1447 | 力鵬 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1605 | 華新 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2405 | 輔信 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2206 | 三陽工業 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | 接近突破型 |  |
| 2601 | 益航 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2597 | 潤弘 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 8070 | 長華* | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2610 | 華航 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 5876 | 上海商銀 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound |  |  |
| 5522 | 遠雄 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2882 | 國泰金 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2883 | 凱基金 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 4306 | 炎洲 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2374 | 佳能 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1521 | 大億 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4935 | 茂林-KY | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8077 | 洛碁 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2114 | 鑫永銓 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 0057 | 富邦摩台 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2816 | 旺旺保 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1522 | 堤維西 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | continued_overheated |
| 1319 | 東陽 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3226 | 龍鋒 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 8472 | 夠麻吉 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2247 | 汎德永業 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 5520 | 力泰 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1617 | 榮星 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2949 | 欣新網 | platform_volume_breakout | confirmed_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |

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

