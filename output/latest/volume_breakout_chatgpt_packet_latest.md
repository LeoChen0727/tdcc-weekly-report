# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-06-03 15:03:58 Asia/Taipei`
- main_price_date: `20260602`
- watch_rows: `300`
- strict_60d_volume_breakout_count: `45`
- broad_recall_watch_count: `96`
- selected_but_routed_to_other_category_count: `146`
- not_selected_by_candidate_model_count: `93`
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
| 1 | 6890 | 來億-KY | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 3.5075 | 13.3136 | 21.2025 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2883 | 凱基金 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | strong_accumulation | continued_many_days | 2.8325 | 8.5847 | 7.3394 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 2379 | 瑞昱 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | continued_many_days | 2.1024 | 10.678 | 22.5141 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 0055 | 元大MSCI金融 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch |  | first_seen | 2.654 | 6.6764 | 9.781 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 2498 | 宏達電 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | strong_accumulation | continued_many_days | 1.8688 | 12.7396 | 21.9512 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 2881 | 富邦金 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | platform_right_side | B_confirm_needed | strong_accumulation | continued_many_days | 1.7172 | 9.6618 | 23.102 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 7 | 2603 | 長榮 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | platform_right_side | B_confirm_needed | strong_accumulation | continued_2_3d | 1.5702 | 9.2199 | 11.0577 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 8 | 3022 | 威強電 | strict_60d_volume_breakout | strict_breakout | A_valid_breakout_watch | selected_as_strict_breakout | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | continued_many_days | 1.5328 | 3.6 | 3.6 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 9 | 3060 | 銘異 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | repeated_but_no_breakout | 5.0434 | 14.9912 | 14.1856 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 10 | 3047 | 訊舟 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | strong_accumulation | continued_2_3d | 3.5934 | 12.2517 | 13.3779 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 11 | 2323 | 中環 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 3.3312 | 13.7255 | 11.0048 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 12 | 1314 | 中石化 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | first_seen | 3.1967 | 8.0344 | 2.5886 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 13 | 6885 | 全福生技 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | first_seen | 2.3874 | 14.186 | 3.5865 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 14 | 2461 | 光群雷 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | strong_accumulation | continued_2_3d | 2.2308 | 9.0062 | 1.7391 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 15 | 2104 | 國際中橡 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 1.7365 | 9.879 | 4.3062 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 16 | 2387 | 精元 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | A_priority_watch | mild_accumulation | continued_2_3d | 1.9109 | 4.4686 | 4.5949 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 17 | 2646 | 星宇航空 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.668 | 3.4653 | 1.4563 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 18 | 3050 | 鈺德 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | strong_accumulation | continued_2_3d | 1.6036 | 6.8826 | 6.8826 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 19 | 1307 | 三芳 | platform_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 1.6024 | 7.4554 | 5.7416 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 20 | 1319 | 東陽 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 3.0222 | 14.9813 | 20.5497 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 21 | 2867 | 三商壽 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | strong_accumulation | repeated_but_no_breakout | 2.1194 | 2.7704 | 2.3653 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 22 | 2912 | 統一超 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 1.9803 | 11.2172 | 4.0179 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 23 | 2352 | 佳世達 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | pattern | 已突破但未過熱 | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.8595 | 12.0996 | 26.2525 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 24 | 2332 | 友訊 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | repeated_but_no_breakout | 1.5797 | 11.6129 | 22.2615 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 25 | 1460 | 宏遠 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | platform_breakout | A_priority_watch | mild_accumulation | first_seen | 1.7698 | 2.7338 | 1.8545 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 26 | 3311 | 閎暉 | neckline_volume_breakout | confirmed_attack | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 1.5536 | 3.5211 | 19.5122 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 27 | 2462 | 良得電 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | selected_as_strict_breakout | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 4.1121 | 15.8273 | 14.455 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 28 | 6957 | 裕慶-KY | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.0109 | 13.4796 | 13.125 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 29 | 1423 | 利華 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 7.2197 | 5.3856 | 5.774 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 30 | 2459 | 敦吉 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.6985 | 5.8209 | 6.1377 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 31 | 6606 | 建德工業 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.8602 | 5.5336 | 10.559 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 32 | 6272 | 驊陞 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.7201 | 15.3153 | 18.5185 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 33 | 2439 | 美律 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5582 | 1.3001 | 4.4693 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 34 | 2908 | 特力 | strict_60d_volume_breakout | strict_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5055 | 1.8735 | 5.5825 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 35 | 3002 | 歐格 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 7.3726 | 19.5906 | 10.2426 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 36 | 3058 | 立德 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 4.2713 | 21.8293 | 16.8421 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 37 | 3049 | 精金 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 3.5649 | 18.5185 | 9.5057 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 38 | 8101 | 華冠 | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 3.0192 | 12.782 | 20.9677 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 39 | 3338 | 泰碩 | platform_volume_breakout | confirmed_attack | B_confirm_needed | selected_but_routed_to_other_category | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 2.7388 | 13.1378 | 19.8649 | continued_overheated | confirm close above MA20/EMA23 and avoid long upper shadow |
| 40 | 9110 | 越南控-DR | platform_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0578 | 27.907 | 11.4865 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | volume_watch_scope | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2881 | 富邦金 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | platform_right_side |  |
| 2603 | 長榮 | strict_60d_volume_breakout | strict_breakout | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | platform_right_side |  |
| 3060 | 銘異 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 3047 | 訊舟 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2323 | 中環 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1314 | 中石化 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 6885 | 全福生技 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2461 | 光群雷 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 2104 | 國際中橡 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2387 | 精元 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2646 | 星宇航空 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3050 | 鈺德 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 1307 | 三芳 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 1319 | 東陽 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2867 | 三商壽 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 2912 | 統一超 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout |  |
| 2352 | 佳世達 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | 已突破但未過熱 |  |
| 2332 | 友訊 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 1460 | 宏遠 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | platform_breakout |  |
| 3311 | 閎暉 | neckline_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 6957 | 裕慶-KY | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1423 | 利華 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2459 | 敦吉 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6606 | 建德工業 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6272 | 驊陞 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2439 | 美律 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2908 | 特力 | strict_60d_volume_breakout | strict_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3002 | 歐格 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout | continued_overheated |
| 3058 | 立德 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout | continued_overheated |
| 3049 | 精金 | platform_volume_breakout | confirmed_attack | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_breakout | continued_overheated |

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

