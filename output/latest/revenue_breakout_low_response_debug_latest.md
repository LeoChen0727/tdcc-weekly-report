# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-04 22:04:23 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 614492 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 83 |
| already_priced_in_excluded | 28 |
| overheat_pass | 55 |
| score_pass | 55 |
| theme_priority_pass | 37 |
| final_rows | 37 |

## 營收欄位狀態

- revenue_schema_status：`ok`

### selected_revenue_columns

| field | selected column |
|---|---|
| code_col | `ticker` |
| name_col | `name` |
| industry_col | `industry` |
| date_col | `revenue_period` |
| latest_revenue_col | `monthly_revenue` |
| latest_yoy_col | `revenue_yoy_pct` |
| cumulative_yoy_col | `cumulative_yoy_pct` |

### raw_revenue_columns

- `ticker`
- `name`
- `industry`
- `revenue_period`
- `monthly_revenue`
- `revenue_yoy_pct`
- `cumulative_yoy_pct`
- `market`

## 主要刷掉原因

| reason | count |
|---|---:|
| fail_revenue_condition | 1666 |
| fail_low_response_condition | 213 |
| fail_already_priced_in | 28 |
| fail_defensive_or_traditional_excluded | 18 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 152.96178992534956 | 138.94580810199872 | 8.42 | 2.82 | -9.13 | -23.96 | 9.5 | 9.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | 2.96 | 3.45 | -12.05 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 3.7 | -5.08 | -3.03 | -6.28 | 4.67 | 4.67 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | 1.31 | 1.3 | -5.88 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 3.65 | -1.86 | -1.07 | -7.75 | 8.85 | 8.85 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 0.82 | 1.25 | -7.75 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 34.28 | 38.97 | 48.07 | 66.67 | 73.04 | 73.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.67 | -0.3 | 2 | 2 | 31.0 | 28.53 | -2.93 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround | B_可觀察 | 158.34377836365994 | -8.228649642919668 | 6.21 | -4.55 | -1.49 | 22.55 | 16.96 | 23.2 | False |  | mild_accumulation | -0.2 | 0.64 | 1 | 1 | 2.03 | 2.45 | -10.47 | 18 | selected |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 5.04 | -2.09 | 21.36 | 10.95 | 24.58 | 29.31 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | 0.15 | 1.2 | -10.29 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | 11.83 | -9.57 | 30.54 | 109.68 | 52.2 | 131.11 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | -4.24 | 3 | 0 | 3.17 | 1.1 | -29.41 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | 5.3 | -5.76 | 7.47 | -1.77 | 10.03 | 10.32 | False |  | distribution_warning | -0.34 | -0.57 | 1 | 1 | -0.14 | 0.67 | -10.32 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 22.64 | 88.02 | 125.25 | 182.26 | 152.22 | 181.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | 30.52 | 32.98 | 0.0 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | 9.02 | -0.75 | -14.93 | -26.65 | 9.62 | 9.62 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 0 | 3.09 | 2.79 | -17.56 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | -0.65 | -4.1 | 1.67 | -10.06 | 8.38 | 8.38 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -1.99 | -0.35 | -8.3 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 5.81 | 11.89 | 18.7 | 26.98 | 27.57 | 31.88 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -1.83 | 1.89 | -13.88 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 14.45 | 49.53 | 132.22 | 149.61 | 132.9 | 178.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 14.11 | 16.9 | -1.84 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -10.64 | -18.78 | -18.11 |  | 0.68 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -14.65 | -11.71 | -28.99 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 7.22 | 2.93 | -8.62 | -10.09 | 13.22 | 13.22 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 3.47 | 4.16 | -9.36 | 21 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 10.54 | 72.06 | 116.76 | 228.81 | 156.95 | 244.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 22.04 | 21.0 | -5.37 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -12.31 | -8.95 | -8.36 | 171.95 | 20.76 | 168.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -8.52 | -8.85 | -25.78 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -10.65 | 2.79 | 97.33 | 77.4 | 120.17 | 120.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -2.55 | -0.69 | -20.99 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 14.92 | 8.96 | 44.71 | 120.56 | 46.26 | 150.92 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | 10.76 | 9.58 | -2.32 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 2.16 | 5.45 | 15.33 | 55.16 | 19.85 | 56.69 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | 3.38 | 3.94 | -3.56 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 11.3 | -13.55 | 23.1 | 164.6 | 22.43 | 150.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | 0.29 | 0.33 | -18.96 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 2.92 | 11.89 | 46.63 | 51.83 | 46.93 | 54.65 | True | 近60日漲幅>40% | mild_accumulation | 2.17 | 2.99 | 1 | 2 | 9.3 | 6.14 | -7.23 |  | fail_already_priced_in |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 9.66 | -3.33 | 13.48 | 97.13 | 15.49 | 120.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -0.02 | 1.48 | -17.41 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 4.14 | -6.68 | 16.72 | 33.69 | 30.68 | 40.41 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 1.17 | 2.81 | -13.93 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 15.7 | 25.88 | 68.65 | 258.7 | 64.32 | 297.39 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | 14.04 | 13.43 | 0.0 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | 0.42 | -2.86 | 25.35 | 39.61 | 22.97 | 66.36 | False |  | strong_accumulation | 2.08 | 2.37 | 2 | 2 | -1.02 | -2.99 | -22.02 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 0.75 | 9.76 | 47.54 | 32.35 | 48.84 | 64.43 | True | 近60日漲幅>40% | strong_accumulation | 1.5 | 0.92 | 2 | 2 | 5.7 | 6.07 | -6.9 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 19.1 | 6.88 | 28.79 | 71.82 | 46.18 | 74.36 | True | 近120日漲幅>70% | distribution_warning | -3.53 | -3.16 | 1 | 1 | 11.66 | 10.91 | -10.45 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -8.8 | 3.67 | 86.14 | 79.21 | 105.78 | 106.3 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | -1.31 | -0.13 | -18.91 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 4.77 | 15.38 | 37.74 | 51.66 | 38.36 | 53.18 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 3.14 | 5.34 | -5.38 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | 7.35 | 18.46 | 39.77 | 39.77 | 49.12 | 68.73 | False |  | mild_accumulation | 1.29 | -0.26 | 2 | 2 | 8.54 | 7.58 | -8.92 | 20 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 3.62 | 2.14 | 2.14 | 12.6 | 13.49 | 23.54 | False |  | distribution_warning | -0.1 | 0.0 | 2 | 0 | 0.5 | 1.35 | -10.49 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -5.57 | -26.33 | 5.41 | 21.48 | 9.58 | 37.34 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -9.95 | -9.74 | -31.33 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 7.64 | 15.67 | 12.32 | 61.12 | 33.39 | 90.42 | True | 距120日低點反彈>80% | distribution_warning | -0.06 | -1.16 | 1 | 0 | 11.15 | 9.44 | -7.74 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 2.23 | -13.85 | 21.12 | 23.15 | 25.68 | 53.08 | False |  | distribution_warning | -0.29 | 0.0 | 2 | 1 | -4.61 | -4.2 | -21.75 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 9.82 | -1.76 | 12.23 | 130.34 | 26.8 | 166.81 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | 4.85 | 2.71 | -11.13 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 2.98 | 1.57 | 26.03 | 70.96 | 49.49 | 83.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.39 | -1.69 | 0 | 1 | 2.19 | 3.35 | -4.6 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral | B_可觀察 | 131.02269543289438 | 40.6738369557123 | 1.59 | 0.34 | -0.78 | -2.41 | 6.06 | 6.06 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | 0.1 | 0.88 | -2.51 | 21 | selected |
| 2515 | 中工 | 建材營造 | neutral |  | 57.09899455038421 | 42.50276733448348 | 10.42 | 7.92 | 6.72 | 10.42 | 18.18 | 18.18 | False |  | strong_accumulation | 0.69 | 0.7 | 3 | 2 | 8.62 | 8.01 | -1.04 |  | fail_low_response_condition |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 2.2 | 9.59 | 12.78 | 8.91 | 22.28 | 22.28 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 1.8 | 3.33 | -6.69 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 9.09 | 7.29 | -5.2 | -23.87 | 14.0 | 14.0 | False |  | strong_accumulation | 0.15 | 0.52 | 2 | 3 | 3.65 | 4.05 | -7.51 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral | D_降級_TDCC轉弱 | 367.4305802571221 | 58.17838010197999 | 2.14 | 6.72 | -3.6 | -15.72 | 12.6 | 12.6 | False |  | distribution_warning | -1.6 | -1.07 | 0 | 1 | 0.74 | 1.84 | -4.67 | 18 | selected |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 128.48525684217282 | 290.35375415914626 | 3.23 | 11.44 | 6.67 | -1.32 | 19.4 | 19.4 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | 1.31 | 3.3 | -9.68 | 13 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 3.15 | 3.01 | -17.26 | -17.26 | 18.73 | 18.73 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 1.49 | 1.56 | -17.78 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2114.205326762877 | 1780.7414522786555 | 1.75 | 1.28 | 22.44 | 12.07 | 29.53 | 29.53 | False |  | distribution_warning | -0.74 | -0.81 | 1 | 1 | -0.17 | 0.91 | -7.32 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | 2.35 | -14.97 | -31.83 | -40.24 | 5.8 | 5.8 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -9.61 | -6.97 | -32.88 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 5.96 | 11.59 | 5.96 | 8.96 | 17.74 | 17.74 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 4.74 | 5.83 | -1.28 | 19 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | 0.98 | 3.71 | -19.77 | -8.81 | 4.02 | 4.02 | False |  | distribution_warning | -1.46 | -1.04 | 1 | 1 | 0.41 | -1.88 | -21.89 | 13 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 3.8 | -6.49 | 63.98 | 108.43 | 63.72 | 108.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | 0.66 | 3.92 | -13.21 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 7.05 | 19.61 | 39.67 | 63.4 | 49.45 | 66.18 | False |  | strong_accumulation | 0.69 | 0.78 | 3 | 3 | 8.59 | 10.73 | -2.15 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 15.4 | 5.6 | 21.83 | 36.75 | 38.13 | 60.41 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 10.06 | 8.4 | -8.38 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | -0.61 | 4.48 | 20.04 | 39.68 | 25.34 | 44.15 | False |  | strong_accumulation | 0.61 | 0.58 | 3 | 3 | -1.14 | -0.11 | -8.42 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 17.65 | 18.11 | 28.76 | 30.43 | 35.75 | 52.28 | False |  | strong_accumulation | 1.66 | 2.35 | 2 | 3 | 12.32 | 13.0 | 0.0 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | A_優先追蹤 | 296.8056658653291 | 223.4596397756601 | -6.83 | -13.67 | 31.78 | 46.37 | 43.88 | 60.23 | False |  | strong_accumulation | 0.2 | 1.06 | 2 | 2 | -5.61 | -6.65 | -22.67 | 22 | selected |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 22.39 | 1.85 | 19.48 | 93.68 | 24.32 | 118.18 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | 11.65 | 9.38 | -8.31 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 92.4008479108611 | 7.500180953989433 | 7.13 | 14.61 | 28.85 | 38.03 | 31.77 | 57.22 | False |  | distribution_warning | -1.06 | -0.7 | 2 | 2 | 4.15 | 6.19 | -2.13 | 14 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | 1.34 | -3.0 | 8.11 | 5.43 | 18.88 | 27.1 | False |  | mild_accumulation | 1.34 | -0.37 | 2 | 0 | -2.48 | -1.74 | -20.0 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 1.36 | -2.03 | 27.93 | 98.55 | 38.51 | 112.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | 4.77 | 3.15 | -7.13 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | 2.78 | -21.45 | -2.64 | 51.19 | 12.44 | 54.9 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -2.5 | -4.3 | -28.08 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | 5.49 | 13.83 | 29.44 | 15.9 | 30.91 | 35.85 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | 5.74 | 4.82 | -11.38 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | 2.22 | -5.01 | 65.13 | 46.53 | 76.92 | 90.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -6.4 | -3.73 | -21.37 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 4.38 | -23.09 | -9.18 | 99.07 | 8.25 | 125.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -4.08 | -2.66 | -23.36 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -0.81 | -23.28 | 49.39 | 105.23 | 63.27 | 113.05 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.8 | -1.3 | 0 | 0 | -5.23 | -5.39 | -30.64 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 14.64 | -2.66 | 30.51 | 289.78 | 43.3 | 336.32 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | 5.64 | 7.23 | -13.6 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | 0.47 | -8.06 | 74.49 | 77.39 | 78.12 | 141.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -2.61 | -2.37 | -21.42 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | 5.02 | -15.0 | 13.81 | 24.77 | 33.99 | 43.01 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -3.0 | -2.9 | -19.76 | 12 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 14.37 | 3.89 | 15.79 | 26.35 | 24.67 | 40.07 | False |  | strong_accumulation | 0.5 | 0.46 | 2 | 2 | 6.99 | 6.49 | -4.59 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | 3.07 | -0.27 | 13.54 | 33.21 | 14.6 | 33.7 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.29 | -0.07 | -20.99 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 14.03 | 14.55 | 65.25 | 102.82 | 64.17 | 135.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | 7.85 | 5.72 | -15.29 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | 2.17 | -29.43 | 38.57 | 50.61 | 41.14 | 62.5 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -12.31 | -7.75 | -30.67 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | 4.02 | -14.96 | -10.04 | 27.18 | 4.48 | 38.2 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -5.55 | -4.6 | -22.85 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 3.29 | -5.58 | 13.99 | 80.92 | 18.28 | 81.52 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.54 | -1.12 | 1 | 0 | 1.34 | 0.44 | -13.73 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | 2.08 | 1.78 | -7.77 | 45.76 | 12.42 | 49.57 | False |  | strong_accumulation | 4.42 | 4.81 | 2 | 2 | -0.62 | -1.19 | -14.43 | 19 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 0.34 | -1.66 | -3.73 | -15.5 | 6.64 | 6.64 | False |  | distribution_warning | -0.24 | -0.56 | 2 | 0 | -1.33 | 0.13 | -13.79 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 7.08 | -4.22 | 27.67 | 64.97 | 37.91 | 83.95 | True | 距120日低點反彈>80% | distribution_warning | -3.16 | -5.47 | 1 | 0 | -4.14 | -0.37 | -15.61 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 20.17 | -6.12 | 96.92 | 104.99 | 95.91 | 116.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 7.85 | 9.67 | -9.8 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 281.10296953335904 | 153.94170544805627 | 11.96 | 6.73 | 13.35 | 25.0 | 22.48 | 32.73 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | 6.0 | 4.79 | -7.83 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -2.07 | 0.56 | -16.28 | -30.5 | 5.88 | 5.88 | False |  | distribution_warning | -0.35 | 0.0 | 0 | 0 | -0.47 | -1.12 | -19.28 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 112.585794273422 | 77.27049729091536 | -1.89 | -13.91 | 17.65 | 28.08 | 23.22 | 52.49 | False |  | mild_accumulation | -1.13 | 0.33 | 1 | 2 | -4.34 | -3.76 | -19.5 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 5.41 | 11.11 | 7.87 | 25.85 | 27.59 | 42.31 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 1.75 | 4.21 | -8.42 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 6.53 | -8.21 | -0.12 | 5.7 | 7.09 | 8.95 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | -1.4 | -0.88 | -13.65 | 14 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | 8.31 | -12.11 | 20.38 | 14.86 | 30.27 | 45.19 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | -1.63 | 0.4 | -19.27 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 1.62 | 6.97 | 3.75 | 5.18 | 10.03 | 15.36 | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | 1.71 | 2.12 | -2.4 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | 0.16 | -13.71 | -9.58 | -10.71 | 1.58 | 1.58 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -10.86 | -8.06 | -23.48 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 0.93 | -1.58 | -13.66 | -21.86 | 6.6 | 6.6 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.74 | -0.35 | -14.17 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 2.16 | 1.07 | -2.74 | -1.05 | 4.03 | 4.03 | False |  | strong_accumulation | 0.31 | 0.42 | 3 | 3 | 1.45 | 1.35 | -4.38 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 452.5877921790185 | 13.290185830553815 | 2.29 | 8.49 | -0.37 | -4.62 | 10.73 | 10.73 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | 0.41 | 1.81 | -8.0 | 15 | selected |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 7.97 | 14.91 | 49.29 | 57.21 | 52.9 | 98.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.8 | 1.98 | 2 | 2 | 13.3 | 11.71 | -3.95 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | 3.83 | -11.15 | -24.51 | 29.67 | 4.23 | 33.5 | False |  | strong_accumulation | 0.68 | 0.05 | 2 | 2 | -4.88 | -4.33 | -25.96 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -5.63 | 3.47 | 85.34 | 102.72 | 93.36 | 136.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.49 | 0.47 | 0 | 2 | -3.93 | -1.89 | -18.79 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | -0.22 | 2.02 | -0.76 | -13.24 | 9.63 | 9.63 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -1.6 | -0.43 | -11.9 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 10.73 | 16.67 | 77.64 | 98.65 | 80.65 | 133.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | 8.37 | 9.4 | -1.67 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 70.65666417439758 | 55.92683953560652 | -1.6 | -5.55 | 27.39 | 25.0 | 35.82 | 65.98 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -6.98 | -4.48 | -23.44 | 12 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 11.4 | 4.36 | 31.59 | 32.32 | 39.65 | 48.76 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 6.22 | 5.78 | -31.67 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | 2.48 | -21.52 | 75.14 | 103.28 | 80.23 | 115.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.95 | 0.74 | 1 | 2 | -6.42 | -4.89 | -30.42 |  | fail_already_priced_in |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | 4.15 | -17.11 | 1.01 | 114.51 | 13.24 | 131.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -2.02 | -4.89 | -31.63 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -2.38 | -23.54 | -20.96 | 26.15 | 10.44 | 36.67 | False |  | mild_accumulation | -2.38 | 0.82 | 0 | 2 | -11.11 | -9.48 | -33.33 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 20.78 | 48.72 | 117.29 | 179.0 | 141.35 | 180.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 25.7 | 23.76 | -2.45 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 20.88 | 14.45 | 16.88 | 216.29 | 31.91 | 220.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | 9.68 | 9.58 | -13.84 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -0.3 | -6.45 | 62.87 | 106.7 | 72.25 | 152.11 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | 0.6 | -1.13 | -24.37 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 7.39 | 0.61 | 2.1 | -20.69 | 10.99 | 10.99 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | 1.38 | 1.88 | -9.21 |  | fail_low_response_condition |
| 6550 | 北極星藥業-KY | 生技醫療業 | defensive_or_traditional |  | 248.65366759517173 | 233.5268264366863 | 9.6 | 4.58 | -23.89 | -54.79 | 9.6 | 9.6 | False |  | distribution_warning | -0.04 | -0.13 | 1 | 1 | 3.38 | 0.79 | -31.84 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 1.1 | -5.92 | 1.99 | 2.9 | 7.46 | 7.46 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | -3.16 | -2.16 | -10.83 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 1.89 | 1.0 | 1.13 | -17.97 | 5.35 | 5.35 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | 0.81 | 1.0 | -7.34 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | -3.91 | 20.0 | 20.19 | 32.29 | 29.15 | 37.3 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | 6.08 | 5.41 | -8.63 | 21 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 58.86220189113607 | 31.41858931023004 | -6.26 | -9.38 | 34.43 | 53.72 | 43.92 | 64.21 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -1.26 | -2.69 | -22.33 | 18 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | 2.24 | -9.12 | -10.31 | -1.44 | 3.4 | 9.6 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -4.84 | -3.55 | -11.9 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 9.09 | 83.33 | 246.0 | 345.95 | 292.86 | 405.75 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 30.59 | 28.07 | -2.58 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | 8.09 | -6.03 | 125.09 | 377.41 | 130.63 | 435.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.0 | 3 | 0 | -2.12 | -4.77 | -33.16 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 1.77 | -13.8 | -7.65 | -20.86 | 2.0 | 6.0 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -3.67 | -4.7 | -24.44 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 3.28 | 30.34 | 35.48 | 17.39 | 56.85 | 56.85 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 11.32 | 12.39 | -8.25 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 25.93 | 47.4 | 324.29 | 1646.58 | 382.04 | 1695.77 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 22.14 | 24.64 | -0.78 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | -2.13 | 26.38 | 47.93 | 14.64 | 47.93 | 51.42 | True | 近20日漲幅>25%；近60日漲幅>40% | distribution_warning | -0.22 | -0.19 | 1 | 1 | 12.81 | 10.57 | -10.08 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | 7.69 | -0.79 | -15.06 | 55.56 | 11.67 | 63.11 | False |  | distribution_warning | -0.79 | 0.0 | 1 | 0 | 0.03 | 1.25 | -18.71 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | 6.01 | -17.36 | -17.13 | -5.06 | 6.38 | 8.7 | False |  | mild_accumulation | 0.4 | -2.35 | 1 | 0 | -5.88 | -5.87 | -27.01 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | 3.72 | -10.64 | 8.53 | -6.39 | 8.4 | 24.46 | False |  | mild_accumulation | 0.02 | 0.5 | 1 | 1 | -7.27 | -6.29 | -22.77 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | 9.48 | -3.94 | 32.63 | 150.0 | 36.34 | 162.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | 0.0 | 1 | 0 | 1.32 | 0.48 | -28.5 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | 5.62 | -7.04 | 64.04 | 110.58 | 64.23 | 124.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.06 | 0.53 | 1 | 1 | -1.12 | -1.07 | -18.9 |  | fail_low_response_condition |
| 7803 | 雲象科技-創 | 生技醫療業 | defensive_or_traditional |  | 1440.6307977736549 | 2.7893555626803463 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |