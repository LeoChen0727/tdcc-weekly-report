# VOLUME BREAKOUT CHATGPT PACKET

## Metadata
- generated_at: `2026-05-26 05:19:29 Asia/Taipei`
- main_price_date: `20260526`
- watch_rows: `56`
- strict_60d_volume_breakout_count: `0`
- selected_but_routed_to_other_category_count: `43`
- not_selected_by_candidate_model_count: `13`
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
| 1 | 3041 | 揚智 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.1546 | 9.2555 | 15.5319 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 2 | 2332 | 友訊 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 2.2415 | 5.8219 | 11.1511 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 3 | 3528 | 安馳 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.6843 | 9.9648 | 17.25 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 4 | 4306 | 炎洲 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.7199 | 1.8116 | 5.6391 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 5 | 2603 | 長榮 | neckline_volume_breakout | A_valid_breakout_watch | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 1.5638 | 3.3019 | 8.6849 |  | next day holds breakout area; volume does not collapse; TDCC not distribution_warning |
| 6 | 9928 | 中視 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.3094 | 1.6997 | 2.5714 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 7 | 2488 | 漢平 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.2161 | 3.8168 | 5.8366 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 8 | 6792 | 詠業 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.1245 | 6.2016 | 16.8942 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 9 | 1506 | 正道 | right_side_volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.5439 | 8.4158 | 0.9217 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 10 | 3311 | 閎暉 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.9315 | 3.5168 | 9.0177 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 11 | 2373 | 震旦行 | neckline_volume_breakout | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8571 | 0.0 | -1.3889 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 12 | 3686 | 達能 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8445 | 8.9552 | 4.8851 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 13 | 1617 | 榮星 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.6078 | 2.4055 | -2.2951 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 14 | 4108 | 懷特 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.3814 | 7.5 | 4.4534 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 15 | 4545 | 銘鈺 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.0955 | 4.5669 | 7.0968 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 16 | 7740 | 熙特爾-創 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.8357 | 3.6932 | 0.8287 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 17 | 3563 | 牧德 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 1.5637 | -3.9657 | 2.1665 | not_in_candidate_model/false_breakout_risk | confirm close above MA20/EMA23 and avoid long upper shadow |
| 18 | 7730 | 暉盛-創 | volume_expansion_watch | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.57 | 3.3708 | 39.3939 | not_in_candidate_model/false_breakout_risk/overheated_breakout | confirm close above MA20/EMA23 and avoid long upper shadow |
| 19 | 2453 | 凌群 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | stale_signal | 1.9263 | 2.693 | 6.7164 | stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 20 | 6214 | 精誠 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | distribution_warning | repeated_but_no_breakout | 1.9055 | 1.9608 | 6.9959 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 21 | 3706 | 神達 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | distribution_warning | stale_signal | 1.7656 | 5.1497 | 8.1281 | tdcc_distribution_warning/stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 22 | 6215 | 和椿 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | C_watch_only | distribution_warning | repeated_but_no_breakout | 1.6237 | 6.746 | 25.7009 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 23 | 4952 | 凌通 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | distribution_warning | repeated_but_no_breakout | 1.616 | 2.6667 | 15.7895 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 24 | 2236 | 百達-KY | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | strong_accumulation | stale_signal | 1.5974 | 6.1594 | 10.9848 | stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 25 | 2352 | 佳世達 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.5103 | 5.6985 | 18.0698 | false_breakout_risk | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 26 | 6799 | 來頡 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | distribution_warning | stale_signal | 1.6883 | 4.1451 | 12.2905 | tdcc_distribution_warning/stale_signal/false_breakout_risk/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 27 | 6835 | 圓裕 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | pattern | 預備發動型 | D_risk_downgrade | distribution_warning | repeated_but_no_breakout | 1.6727 | 0.2551 | -1.2563 | tdcc_distribution_warning/false_breakout_risk/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 28 | 1773 | 勝一 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | strong_accumulation | stale_signal | 1.6642 | 4.2373 | 7.2674 | stale_signal/false_breakout_risk/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 29 | 3704 | 合勤控 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | continued_overheated | 2.1514 | 6.2802 | 30.1775 | continued_overheated/overheated_breakout/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 30 | 6243 | 迅杰 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | distribution_warning | repeated_but_no_breakout | 2.1316 | 5.6769 | 9.009 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 31 | 5244 | 弘凱 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | distribution_warning | first_seen | 2.038 | 7.7124 | -5.9361 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 32 | 6456 | GIS-KY | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | distribution_warning | stale_signal | 1.9684 | 8.8698 | -3.6709 | tdcc_distribution_warning/stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 33 | 2421 | 建準 | neckline_volume_breakout | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | stale_signal | 1.915 | 4.2763 | 8.1911 | stale_signal/false_breakout_risk/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 34 | 2258 | 鴻華先進-創 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | strong_accumulation | first_seen | 1.908 | 8.5714 | 6.6667 | decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 35 | 3714 | 富采 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | platform_right_side | D_risk_downgrade | mild_accumulation | stale_signal | 1.6971 | 10.0 | 10.4478 | stale_signal/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 36 | 2439 | 美律 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | first_seen | 1.6176 | 2.9138 | -0.1131 | decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 37 | 8105 | 凌巨 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | platform_right_side | C_watch_only | distribution_warning | repeated_but_no_breakout | 1.6032 | 5.7751 | 28.8889 | tdcc_distribution_warning | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 38 | 4763 | 材料*-KY | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | D_risk_downgrade | mild_accumulation | first_seen | 1.6013 | 3.3097 | 1.8648 | decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 39 | 2515 | 中工 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | revenue_breakout_low_response |  | D_risk_downgrade | distribution_warning | stale_signal | 2.1212 | -3.6101 | 0.3759 | tdcc_distribution_warning/stale_signal/false_breakout_risk/decision_layer_downgrade | risk first: avoid chasing until heat/TDCC/repeat risk improves |
| 40 | 3031 | 佰鴻 | volume_expansion_watch | D_risk_downgrade | selected_but_routed_to_other_category | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.1177 | 0.4464 | 2.8963 | false_breakout_risk | risk first: avoid chasing until heat/TDCC/repeat risk improves |

## Not Selected / Routed Elsewhere Diagnostics

| stock_id | stock_name | volume_breakout_type | selection_status | not_selected_reason | category | pattern_stage | risk_flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3041 | 揚智 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2332 | 友訊 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 3528 | 安馳 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 4306 | 炎洲 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 2603 | 長榮 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge |  |
| 9928 | 中視 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 2488 | 漢平 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 6792 | 詠業 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 1506 | 正道 | right_side_volume_attack | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 3311 | 閎暉 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 2373 | 震旦行 | neckline_volume_breakout | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 3686 | 達能 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 1617 | 榮星 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model |
| 4108 | 懷特 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 4545 | 銘鈺 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 7740 | 熙特爾-創 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 3563 | 牧德 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk |
| 7730 | 暉盛-創 | volume_expansion_watch | not_selected_by_candidate_model | volume breakout detected from price history but not selected by existing candidate filters |  |  | not_in_candidate_model/false_breakout_risk/overheated_breakout |
| 2453 | 凌群 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | stale_signal/decision_layer_downgrade |
| 6214 | 精誠 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning |
| 3706 | 神達 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning/stale_signal/decision_layer_downgrade |
| 6215 | 和椿 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning |
| 4952 | 凌通 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning |
| 2236 | 百達-KY | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | stale_signal/decision_layer_downgrade |
| 2352 | 佳世達 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | false_breakout_risk |
| 6799 | 來頡 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning/stale_signal/false_breakout_risk/decision_layer_downgrade |
| 6835 | 圓裕 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_pattern; strict_breakout_requires_60d_high_breakout | pattern | 預備發動型 | tdcc_distribution_warning/false_breakout_risk/decision_layer_downgrade |
| 1773 | 勝一 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | stale_signal/false_breakout_risk/decision_layer_downgrade |
| 3704 | 合勤控 | neckline_volume_breakout | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | continued_overheated/overheated_breakout/decision_layer_downgrade |
| 6243 | 迅杰 | volume_expansion_watch | selected_but_routed_to_other_category | routed_to_range_rebound; strict_breakout_requires_60d_high_breakout | range_rebound | neckline_challenge | tdcc_distribution_warning |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 975 | 964 | 0.2861 | 41.29 | 944 | 1.6473 | 43.64 | 893 | 3.9517 | 45.58 | ok |
| volume_breakout_type | neckline_volume_breakout | 3350 | 3118 | 0.8726 | 44.29 | 2930 | 2.6764 | 47.3 | 2418 | 5.3177 | 49.88 | ok |
| volume_breakout_type | platform_volume_breakout | 3495 | 3470 | 1.1411 | 44.87 | 3427 | 1.7022 | 44.94 | 3251 | 3.6066 | 45.65 | ok |
| volume_breakout_type | right_side_volume_attack | 3102 | 3025 | 2.1361 | 47.93 | 2908 | 3.4376 | 49.59 | 2619 | 8.0072 | 53.49 | ok |
| volume_breakout_type | strict_60d_volume_breakout | 2276 | 2216 | 2.0414 | 48.01 | 2066 | 5.2533 | 52.27 | 1677 | 9.3365 | 53.73 | ok |
| volume_breakout_type | volume_expansion_watch | 10130 | 9996 | 0.6723 | 43.17 | 9788 | 1.4337 | 44.41 | 9171 | 3.0603 | 46.51 | ok |
| false_breakout_risk | False | 14267 | 13916 | 1.2069 | 44.57 | 13507 | 2.5474 | 46.59 | 12300 | 5.0014 | 48.28 | ok |
| false_breakout_risk | True | 9061 | 8873 | 0.8866 | 44.66 | 8556 | 1.8356 | 45.75 | 7729 | 4.0482 | 48.21 | ok |
| overheated_breakout | False | 19183 | 18753 | 0.8983 | 43.84 | 18218 | 1.7962 | 45.01 | 16768 | 3.7819 | 47.38 | ok |
| overheated_breakout | True | 4145 | 4036 | 1.9367 | 48.14 | 3845 | 4.5225 | 52.2 | 3261 | 9.013 | 52.74 | ok |

## Rules

- This layer is for visibility and performance tracking, not standalone buy advice.
- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.
- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.
- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.
- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.
- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.

