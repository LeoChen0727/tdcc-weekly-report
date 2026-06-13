# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-14 03:20:43 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1959 |
| standardized_revenue_rows | 1959 |
| price_rows | 581112 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 295 |
| price_metrics_pass | 290 |
| low_response_pass | 50 |
| already_priced_in_excluded | 24 |
| overheat_pass | 26 |
| score_pass | 26 |
| theme_priority_pass | 19 |
| final_rows | 19 |

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
| fail_revenue_condition | 1664 |
| fail_low_response_condition | 240 |
| fail_already_priced_in | 24 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 5 |
| fail_non_mainstream_score_lt_11 | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 152.96178992534956 | 138.94580810199872 | 9.71 | 5.12 | -12.4 | -25.17 | 13.0 | 13.0 | False |  | mild_accumulation | -0.56 | 0.51 | 2 | 2 | 8.29 | 5.98 | -14.07 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -3.91 | 0.0 | -5.96 | -5.15 | 1.84 | 1.84 | False |  | mild_accumulation | -0.35 | 0.51 | 1 | 1 | -1.56 | -2.12 | -7.14 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -3.14 | 1.93 | -2.12 | -7.27 | 9.14 | 9.14 | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | 1.18 | 0.06 | -7.5 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 6.62 | 21.85 | 11.88 | 19.05 | 26.09 | 26.09 | False |  | strong_accumulation | 0.5 | 0.57 | 3 | 3 | 13.9 | 11.33 | -8.23 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | 3.99 | 15.73 | 20.59 | 40.69 | 30.45 | 42.08 | False |  | distribution_warning | -0.49 | -0.15 | 1 | 2 | 10.49 | 7.9 | -15.84 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | 2.9 | 14.64 | -17.65 | 20.94 | 16.96 | 25.89 | False |  | mild_accumulation | 0.24 | -0.01 | 1 | 1 | 4.71 | 2.64 | -19.09 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 0.52 | 11.11 | 23.4 | 22.22 | 32.76 | 32.76 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -0.41 | 2.09 | -7.89 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -11.21 | -20.58 | 86.26 | 108.74 | 93.2 | 122.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.05 | -0.88 | 1 | 1 | -15.4 | -11.23 | -31.9 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | B_可觀察 | 153.16268341919277 | -7.777041541987246 | -1.29 | 9.67 | -0.24 | -0.36 | 10.98 | 10.98 | False |  | strong_accumulation | 1.82 | 1.2 | 2 | 2 | 1.62 | 1.25 | -8.9 | 21 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 52.0 | 55.9 | 57.84 | 86.05 | 68.51 | 90.95 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.76 | 2.47 | 2 | 2 | 45.85 | 40.28 | -3.18 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | 9.06 | 9.06 | 1.75 | -0.93 | 13.73 | 13.73 | False |  | strong_accumulation | 0.36 | 0.4 | 2 | 2 | 7.75 | 6.53 | -1.54 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 16.53 | 20.0 | 31.78 | 47.49 | 35.58 | 53.09 | False |  | distribution_warning | -0.5 | -1.49 | 0 | 0 | 14.38 | 13.65 | -7.84 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 36.16 | 45.02 | 102.64 | 91.15 | 119.37 | 140.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.13 | 0.18 | 1 | 2 | 33.06 | 31.55 | -1.85 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 3.57 | 9.88 | -1.91 | -12.58 | 13.05 | 13.05 | False |  | strong_accumulation | 0.17 | 0.42 | 2 | 3 | 7.24 | 4.6 | -13.04 | 20 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 7.26 | 51.2 | 66.78 | 139.05 | 81.23 | 141.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.49 | 2 | 2 | 17.02 | 17.18 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -16.52 | -8.44 | 2.09 | 295.95 | 26.84 | 308.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.27 | 3.81 | 2 | 2 | -5.5 | -5.7 | -18.61 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -6.78 | 31.8 | 34.38 | 154.81 | 105.25 | 154.81 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.98 | 1.71 | 1 | 1 | 16.04 | 15.49 | -10.88 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -3.71 | -6.41 | 45.94 | 114.22 | 56.19 | 114.22 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.34 | -1.03 | 1 | 0 | -5.22 | -3.81 | -13.36 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -2.62 | 8.92 | 11.38 | 48.25 | 19.12 | 55.5 | False |  | mild_accumulation | 0.06 | -0.01 | 2 | 2 | 3.12 | 2.83 | -7.57 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -5.17 | 5.03 | 46.65 | 186.88 | 56.66 | 215.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.58 | 0.44 | 2 | 1 | -4.63 | -3.71 | -17.89 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 88.80451818624007 | 107.89432287557707 | -12.43 | -4.72 | 10.8 | 23.16 | 26.62 | 28.15 | False |  | distribution_warning | -0.75 | -1.18 | 1 | 1 | -9.46 | -6.71 | -18.75 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 3.53 | 5.6 | 43.95 | 114.29 | 54.57 | 128.77 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.32 | 0.63 | 1 | 2 | -0.83 | -0.55 | -13.16 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | -7.12 | 24.0 | 26.96 | 27.18 | 35.03 | 43.08 | False |  | mild_accumulation | 0.31 | 0.26 | 1 | 1 | 8.88 | 5.79 | -15.07 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -0.62 | 6.27 | 78.89 | 201.87 | 86.13 | 229.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -0.49 | 1 | 1 | -2.96 | -1.03 | -14.29 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | -12.33 | -12.8 | 27.85 | 1.85 | 33.0 | 54.44 | False |  | distribution_warning | -3.38 | -3.51 | 0 | 0 | -14.53 | -10.94 | -27.6 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 13.91 | 30.35 | 39.66 | 49.37 | 59.56 | 59.56 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.21 | 1.08 | 1 | 2 | 11.92 | 13.55 | -2.6 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 8.94 | 22.83 | 5.69 | 71.81 | 38.54 | 68.83 | True | 近120日漲幅>70% | strong_accumulation | 4.5 | 4.21 | 2 | 2 | 13.16 | 11.16 | -9.93 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -10.85 | 22.62 | 35.51 | 139.74 | 88.41 | 142.07 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.76 | 0.63 | 2 | 2 | 11.28 | 10.79 | -13.12 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 18.15 | 24.64 | 38.15 | 48.18 | 43.66 | 53.77 | False |  | mild_accumulation | 0.64 | 0.02 | 3 | 1 | 17.89 | 17.19 | -5.85 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 95.17088148345744 | 80.48460599503228 | -0.28 | 4.66 | 16.16 | 26.14 | 38.27 | 43.23 | False |  | mild_accumulation | 0.8 | 0.79 | 1 | 1 | 2.15 | 2.96 | -10.24 | 17 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.18 | 7.9 | -1.58 | 6.06 | 11.11 | 20.95 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 4.33 | 2.8 | -6.98 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -15.96 | -7.0 | -2.55 | 72.11 | 46.52 | 81.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.73 | 1 | 0 | -6.27 | -5.29 | -20.23 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | -11.62 | -2.02 | 20.19 | 52.42 | 31.73 | 66.05 | False |  | distribution_warning | -0.17 | -0.17 | 1 | 0 | -2.7 | -3.48 | -23.42 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -14.14 | 0.66 | 19.91 | 39.09 | 51.49 | 59.54 | True | 距60日低點反彈>50% | distribution_warning | -0.29 | -0.07 | 1 | 1 | -8.0 | -6.15 | -18.44 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -6.12 | -7.07 | 37.66 | 149.77 | 59.08 | 147.53 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.97 | -3.65 | 1 | 0 | -8.96 | -7.07 | -20.23 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -2.52 | 37.06 | 39.92 | 75.87 | 59.68 | 83.58 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.83 | -0.01 | 1 | 1 | 6.24 | 6.7 | -6.51 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 3.89 | 5.22 | 2.95 | -4.22 | 7.85 | 7.85 | False |  | distribution_warning | -0.06 | -0.17 | 2 | 1 | 3.73 | 3.1 | -0.55 |  | fail_low_response_condition |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 12.18 | 13.27 | 8.02 | 6.87 | 22.81 | 22.81 | False |  | strong_accumulation | 1.26 | 2.12 | 3 | 3 | 13.09 | 11.86 | -3.31 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 11.39 | 1.35 | -16.97 | -25.0 | 12.5 | 12.5 | False |  | mild_accumulation | -0.08 | 0.82 | 1 | 3 | 3.7 | 2.84 | -18.77 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | 11.7 | 9.2 | -3.09 | -17.79 | 15.22 | 15.22 | False |  | distribution_warning | -0.19 | -0.29 | 1 | 1 | 9.65 | 7.73 | -4.15 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 14.23 | 16.8 | 13.43 | 9.62 | 21.54 | 21.54 | False |  | strong_accumulation | 0.25 | 0.31 | 2 | 2 | 15.62 | 12.95 | -2.56 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | 7.78 | 2.78 | -20.41 | -19.17 | 17.22 | 17.22 | False |  | distribution_warning | -0.42 | -0.75 | 0 | 0 | 4.77 | 2.46 | -21.85 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 5.89 | 0.78 | 23.15 | 19.39 | 33.38 | 33.38 | False |  | strong_accumulation | 1.17 | 1.27 | 2 | 3 | 4.43 | 5.44 | -4.56 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 86.14284031322353 | 42.934476141944494 | 2.4 | 23.61 | -32.78 | -21.66 | 26.45 | 26.45 | False |  | strong_accumulation | 0.76 | 0.51 | 2 | 2 | 4.62 | 2.57 | -36.69 | 18 | selected |
| 2547 | 日勝生 | 建材營造 | neutral |  | 69.90066780612314 | 22.241457982263142 | 8.29 | 11.9 | -0.45 | 3.74 | 13.15 | 13.15 | False |  | distribution_warning | -0.49 | -0.3 | 0 | 1 | 9.5 | 7.96 | -2.63 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 2.12 | 26.88 | 48.97 | 106.54 | 64.76 | 112.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.51 | -1.09 | 1 | 0 | 9.13 | 7.85 | -15.55 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 7.49 | 28.15 | 36.31 | 28.15 | 43.02 | 46.11 | True | 近20日漲幅>25% | strong_accumulation | 0.75 | 0.76 | 3 | 2 | 13.91 | 12.93 | -5.43 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | 12.67 | 30.86 | 36.92 | 46.72 | 45.44 | 49.33 | True | 近20日漲幅>25% | strong_accumulation | 0.45 | 0.52 | 3 | 3 | 16.18 | 14.68 | -4.74 |  | fail_low_response_condition |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 15.71 | 28.78 | 22.76 | 57.7 | 32.17 | 57.7 | True | 近20日漲幅>25% | strong_accumulation | 0.86 | 0.99 | 2 | 2 | 20.53 | 17.73 | -1.95 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 10.16 | 13.83 | 6.55 | 24.41 | 19.2 | 25.55 | False |  | strong_accumulation | 0.34 | 0.41 | 2 | 2 | 11.56 | 9.15 | -2.29 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 341.3211844301598 | 175.7452659074452 | 5.46 | 23.36 | 26.83 | 50.89 | 34.13 | 51.91 | False |  | strong_accumulation | 0.16 | 0.18 | 2 | 2 | 10.39 | 9.67 | -4.11 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | -10.31 | 12.98 | 25.0 | 8.29 | 37.83 | 37.83 | False |  | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -0.58 | -2.42 | -21.27 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 52.80006873442736 | 30.333657817463656 | 3.4 | 8.31 | 25.79 | 34.38 | 32.3 | 41.06 | False |  | distribution_warning | -0.47 | -0.09 | 1 | 1 | 2.8 | 3.72 | -6.3 | 12 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 11.72 | 0.38 | 25.35 | 34.98 | 35.53 | 39.06 | False |  | distribution_warning | -1.44 | -4.06 | 1 | 0 | 4.83 | 6.16 | -5.99 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -18.88 | -13.89 | 1.64 | 164.96 | 47.62 | 180.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.07 | -4.52 | 1 | 1 | -8.49 | -5.6 | -20.66 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -10.93 | -0.21 | 30.0 | 68.77 | 31.06 | 90.12 | True | 距120日低點反彈>80% | distribution_warning | -1.07 | -0.86 | 0 | 1 | -7.19 | -6.91 | -20.1 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 92.4008479108611 | 7.500180953989433 | 12.1 | 28.85 | 39.81 | 32.37 | 44.44 | 57.22 | True | 近20日漲幅>25% | strong_accumulation | 2.59 | 2.62 | 3 | 3 | 16.3 | 15.18 | -2.13 |  | fail_low_response_condition |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -1.39 | 18.5 | 15.05 | 22.8 | 27.42 | 32.9 | False |  | mild_accumulation | -1.59 | 2.36 | 1 | 1 | -0.39 | 1.34 | -16.35 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -10.71 | -7.64 | 27.33 | 92.8 | 54.64 | 102.16 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.0 | 0 | 1 | -7.78 | -4.85 | -15.06 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -21.34 | -13.28 | -10.74 | 51.83 | 15.99 | 70.52 | False |  | distribution_warning | -0.98 | -1.16 | 1 | 1 | -19.01 | -15.43 | -25.81 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -4.29 | 4.25 | 2.94 | -3.54 | 15.8 | 15.8 | False |  | mild_accumulation | -0.95 | 0.4 | 1 | 1 | -3.9 | -2.35 | -11.05 | 18 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -2.93 | 27.4 | 76.54 | 71.36 | 115.66 | 115.66 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.21 | -5.65 | 1 | 1 | 3.66 | 10.2 | -10.87 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -5.56 | 1.19 | -24.7 | 184.52 | 16.24 | 180.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.07 | -0.03 | 1 | 0 | -2.46 | -3.79 | -24.44 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -19.79 | -7.45 | 48.08 | 187.74 | 92.5 | 214.03 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.44 | -1.29 | 1 | 1 | -14.5 | -11.32 | -27.63 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -4.05 | 13.04 | 130.95 | 235.14 | 165.13 | 301.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.06 | 1.34 | 3 | 2 | -2.73 | -1.21 | -15.16 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -16.9 | 13.43 | 121.75 | 110.05 | 136.16 | 136.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -5.81 | -5.0 | -23.16 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 71.36506452239956 | 62.24907879043217 | -8.25 | 5.47 | 28.44 | 49.43 | 47.3 | 51.95 | False |  | strong_accumulation | 1.66 | 1.79 | 2 | 2 | -5.34 | -2.21 | -14.75 | 18 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -4.66 | 3.26 | 13.36 | 16.39 | 23.4 | 30.34 | False |  | distribution_warning | -0.32 | -0.23 | 1 | 1 | -3.35 | -1.64 | -11.22 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -0.53 | -4.83 | 14.02 | 32.62 | 19.49 | 37.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.44 | -1.39 | -19.91 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -3.42 | -7.59 | 74.16 | 102.78 | 104.67 | 122.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -2.98 | 2 | 1 | -7.73 | -4.78 | -26.39 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -5.91 | 43.98 | 87.01 | 72.44 | 95.58 | 96.55 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 1.72 | 2 | 2 | 8.79 | 7.79 | -16.14 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -8.73 | 4.58 | 2.03 | 44.25 | 21.84 | 49.23 | False |  | strong_accumulation | 2.79 | 0.77 | 2 | 2 | -1.78 | -1.91 | -16.89 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -11.76 | -4.98 | 12.78 | 64.06 | 21.39 | 85.51 | True | 距120日低點反彈>80% | distribution_warning | -0.76 | -0.66 | 0 | 0 | -10.43 | -7.77 | -17.65 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | -4.03 | -2.35 | -4.03 | 42.31 | 4.72 | 51.36 | False |  | distribution_warning | -0.06 | -0.75 | 2 | 2 | -3.48 | -4.08 | -18.18 | 13 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 2.62 | 0.28 | -2.75 | -10.86 | 5.06 | 5.06 | False |  | mild_accumulation | 0.32 | -0.07 | 3 | 1 | 1.61 | 0.91 | -8.07 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 7.48 | 8.23 | -0.64 | -14.64 | 10.95 | 10.95 | False |  | strong_accumulation | 0.46 | 0.93 | 2 | 3 | 7.1 | 5.72 | -10.3 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 13.02 | 29.67 | 46.56 | 71.37 | 62.22 | 96.92 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.54 | 6.07 | 3 | 3 | 13.89 | 13.14 | -5.81 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -5.7 | 44.49 | 73.95 | 105.94 | 102.07 | 111.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.49 | -3.45 | 0 | 1 | 1.0 | 4.71 | -15.69 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | B_可觀察 | 281.10296953335904 | 153.94170544805627 | 3.81 | 5.36 | -7.81 | 31.6 | 18.0 | 35.11 | False |  | mild_accumulation | 0.13 | -0.05 | 2 | 1 | 2.86 | 2.88 | -14.9 | 21 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 0.67 | -1.31 | -21.9 | -34.11 | 6.59 | 6.59 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 0.66 | -0.87 | -24.5 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -10.67 | -2.33 | 10.34 | 94.98 | 37.03 | 109.23 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -4.27 | 1 | 1 | -1.58 | -2.31 | -15.79 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 19.06 | 29.15 | 37.55 | 42.7 | 40.59 | 48.25 | True | 近20日漲幅>25% | mild_accumulation | 0.78 | -0.01 | 2 | 0 | 19.87 | 16.81 | -5.69 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -8.57 | 9.92 | 7.3 | 3.14 | 13.89 | 13.89 | False |  | mild_accumulation | 2.03 | 1.42 | 2 | 1 | -1.05 | -0.8 | -9.74 | 18 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -13.76 | 19.57 | 17.44 | 26.6 | 35.62 | 51.15 | False |  | distribution_warning | -0.89 | -0.23 | 0 | 0 | 1.56 | 1.97 | -15.96 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 8.49 | 7.48 | 1.32 | 8.66 | 8.83 | 15.19 | False |  | mild_accumulation | -0.33 | 0.02 | 1 | 1 | 6.16 | 5.72 | -1.0 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 191.64415257562703 | 643.5739953148809 | 6.52 | 10.8 | 13.96 | 31.58 | 17.47 | 34.45 | False |  | strong_accumulation | 0.48 | 0.49 | 2 | 3 | 9.73 | 8.61 | -4.65 | 20 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 2.29 | -1.33 | -13.4 | -21.62 | 9.05 | 9.05 | False |  | mild_accumulation | -0.04 | 0.01 | 1 | 1 | 2.54 | 0.76 | -16.79 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 1.07 | 2.17 | -1.39 | -1.74 | 3.66 | 3.66 | False |  | strong_accumulation | 0.6 | 0.04 | 3 | 2 | 1.49 | 0.96 | -4.71 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 13.16 | 9.31 | 6.92 | 8.03 | 14.72 | 14.72 | False |  | mild_accumulation | 0.57 | 0.69 | 1 | 1 | 10.14 | 8.82 | -2.11 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 155.54062108558796 | 134.80726693594198 | -5.45 | 27.66 | 33.56 | 56.31 | 43.91 | 63.52 | True | 近20日漲幅>25% | mild_accumulation | 0.07 | 0.25 | 1 | 1 | 6.68 | 5.57 | -14.38 |  | fail_already_priced_in |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 5.64 | 11.65 | 37.61 | 58.46 | 56.92 | 68.59 | True | 距60日低點反彈>50% | distribution_warning | -2.6 | -2.77 | 0 | 0 | 3.14 | 5.07 | -5.63 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 78.63452035793752 | 28.54441429888791 | -1.96 | -3.85 | -21.05 | 69.68 | 11.94 | 71.43 | False |  | mild_accumulation | 0.94 | 0.62 | 2 | 1 | -2.41 | -2.0 | -30.07 | 17 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -2.65 | 13.22 | 109.97 | 93.23 | 126.63 | 126.63 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | 0.24 | 3 | 1 | 0.35 | 5.15 | -11.38 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 9.65 | 3.85 | -0.42 | 0.11 | 13.48 | 13.48 | False |  | distribution_warning | -0.46 | -1.03 | 2 | 1 | 7.32 | 5.7 | -6.08 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 6.0 | 33.5 | 91.94 | 129.77 | 104.1 | 125.05 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | 0.1 | 2 | 1 | 13.16 | 14.26 | -1.08 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | 4.04 | 21.18 | 42.81 | 42.07 | 70.95 | 70.95 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -8.34 | -6.8 | 0 | 1 | -0.02 | 3.86 | -9.35 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -3.32 | -26.38 | 3.56 | 41.21 | 35.86 | 44.72 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -6.31 | -4.33 | -33.52 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -8.58 | 28.33 | 121.05 | 170.18 | 139.79 | 179.44 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 0.65 | 2 | 2 | -2.7 | -0.45 | -22.22 |  | fail_already_priced_in |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -25.29 | -27.93 | 22.08 | 139.78 | 42.28 | 144.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -2.77 | 2 | 0 | -24.0 | -20.83 | -34.18 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -1.33 | 2.2 | 0.27 | 48.4 | 9.76 | 67.87 | False |  | strong_accumulation | 1.66 | 0.37 | 2 | 2 | -3.44 | -4.35 | -24.59 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 5.21 | 17.74 | 41.01 | 83.91 | 64.19 | 103.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.29 | 1 | 2 | 7.96 | 9.36 | -3.95 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 18.69 | -6.35 | 32.83 | 257.17 | 46.08 | 276.82 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.95 | 0.01 | 0 | 2 | 8.22 | 7.0 | -16.54 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -13.3 | -17.89 | 62.94 | 131.27 | 112.06 | 150.2 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.65 | -1.13 | 2 | 1 | -10.51 | -8.06 | -28.58 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -5.73 | 1.94 | -9.0 | -32.68 | 5.76 | 5.76 | False |  | mild_accumulation | 0.26 | -0.07 | 3 | 0 | 0.51 | -0.68 | -10.34 |  | fail_low_response_condition |
| 6550 | 北極星藥業-KY | 生技醫療業 | defensive_or_traditional |  | 248.65366759517173 | 233.5268264366863 | -0.75 | -18.27 | -41.33 | -54.48 | 3.12 | 3.12 | False |  | strong_accumulation | 1.74 | 2.29 | 3 | 3 | -9.26 | -10.09 | -40.0 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 1.82 | 1.01 | -24.49 | -39.8 | 11.71 | 11.71 | False |  | distribution_warning | -0.07 | -0.25 | 1 | 2 | 3.67 | 1.79 | -25.0 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 1.23 | 0.41 | -0.81 | 14.69 | 14.69 | 20.0 | False |  | mild_accumulation | 0.18 | 0.89 | 2 | 1 | 0.4 | 1.41 | -4.84 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | -0.12 | 1.27 | -8.69 | -19.46 | 4.17 | 4.17 | False |  | distribution_warning | -0.18 | -0.13 | 0 | 0 | 1.22 | 0.26 | -8.37 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | 6.99 | 10.59 | 11.49 | 20.88 | 24.14 | 26.89 | False |  | mild_accumulation | -0.8 | 0.2 | 2 | 2 | 7.35 | 6.8 | -1.43 | 19 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -21.77 | 8.39 | -6.54 | 93.66 | 31.76 | 103.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.59 | 4.65 | 1 | 1 | -8.66 | -7.66 | -28.89 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -2.78 | 4.39 | -14.76 | 20.69 | 6.82 | 22.81 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.7 | 0.44 | -21.19 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 15.21 | 59.58 | 164.05 | 197.17 | 182.69 | 222.22 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.41 | -3.62 | 1 | 1 | 15.43 | 22.12 | -1.06 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -17.84 | -33.19 | 88.24 | 420.55 | 144.18 | 438.05 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.75 | 1.15 | 0 | 2 | -24.88 | -19.19 | -37.96 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -13.36 | -13.36 | 2.14 | -14.91 | 9.54 | 10.05 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -11.78 | -10.11 | -21.56 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 22.73 | 18.68 | 11.34 | 1.25 | 34.44 | 34.44 | False |  | distribution_warning | -0.17 | -0.48 | 0 | 1 | 18.77 | 16.33 | -3.57 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -5.64 | 54.37 | 395.33 | 1264.81 | 421.31 | 1338.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.29 | 3.07 | 2 | 2 | 12.71 | 16.35 | -12.15 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 0.0 | 1.63 | 5.93 | -1.19 | 16.28 | 17.92 | False |  | strong_accumulation | 2.17 | 0.13 | 3 | 2 | -0.26 | -0.44 | -16.67 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | 8.06 | 11.75 | 64.59 | 67.11 | 74.6 | 76.48 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.36 | 0.0 | 1 | 0 | 7.02 | 6.76 | -12.04 |  | fail_low_response_condition |