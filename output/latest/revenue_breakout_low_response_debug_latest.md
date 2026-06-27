# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-27 21:29:15 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 604676 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 377 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 708 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 99 |
| already_priced_in_excluded | 49 |
| overheat_pass | 50 |
| score_pass | 50 |
| theme_priority_pass | 34 |
| final_rows | 34 |

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
| fail_low_response_condition | 197 |
| fail_already_priced_in | 49 |
| fail_defensive_or_traditional_excluded | 16 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 152.96178992534956 | 138.94580810199872 | -7.76 | 0.0 | -16.53 | -33.55 | 1.0 | 1.0 | False |  | distribution_warning | -0.79 | -0.14 | 1 | 1 | -4.74 | -4.68 | -18.88 | 14 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -2.7 | -2.7 | -4.85 | -9.24 | 0.93 | 0.93 | False |  | mild_accumulation | -0.22 | 0.46 | 1 | 1 | -3.4 | -2.63 | -9.24 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -3.78 | -3.78 | -6.56 | -10.1 | 5.01 | 5.01 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -3.84 | -2.92 | -11.0 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -5.02 | -1.81 | -6.45 | 12.69 | 10.13 | 16.94 | False |  | mild_accumulation | 0.22 | 0.0 | 1 | 1 | -4.7 | -3.62 | -15.7 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -6.54 | -7.87 | 22.26 | 11.74 | 23.1 | 23.1 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -6.27 | -4.89 | -14.59 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -11.71 | -22.5 | 55.69 | 91.36 | 55.0 | 106.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.33 | 1.4 | 2 | 1 | -11.65 | -11.59 | -36.88 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | B_可觀察 | 153.16268341919277 | -7.777041541987246 | -5.26 | -6.16 | 4.35 | -9.49 | 4.76 | 4.76 | False |  | strong_accumulation | 1.4 | 0.62 | 2 | 2 | -6.5 | -4.91 | -14.84 | 19 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | -8.85 | 95.26 | 95.06 | 126.22 | 105.65 | 133.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.03 | 1.32 | 2 | 2 | 23.79 | 21.21 | -10.39 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | -5.12 | 3.73 | 0.0 | -13.07 | 9.09 | 9.09 | False |  | strong_accumulation | 0.36 | 0.45 | 2 | 2 | -1.42 | -0.61 | -7.69 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -8.51 | 8.4 | 16.74 | 38.12 | 20.56 | 38.12 | False |  | distribution_warning | -0.07 | -1.49 | 1 | 0 | -5.04 | -3.84 | -18.61 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 1.82 | 38.01 | 120.16 | 85.66 | 115.08 | 143.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.5 | 1.14 | 0 | 2 | 9.0 | 9.07 | -10.33 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -6.0 | -3.52 | -3.52 |  | 1.23 |  | False |  | mild_accumulation | 0.82 | -0.02 | 3 | 0 | -7.8 | -6.51 | -20.53 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -4.01 | 3.66 | -12.25 | -17.81 | 5.59 | 5.59 | False |  | strong_accumulation | 0.26 | 0.1 | 2 | 2 | -3.41 | -2.8 | -17.59 | 19 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 4.31 | 47.48 | 118.01 | 220.55 | 132.45 | 228.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.61 | 2 | 2 | 24.66 | 21.48 | -12.25 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -3.85 | -2.4 | 19.05 | 325.95 | 37.71 | 324.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.0 | -0.75 | 2 | 1 | 1.63 | 1.14 | -15.36 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -5.49 | 30.7 | 130.98 | 168.53 | 146.42 | 167.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.43 | 0.22 | 1 | 1 | 12.06 | 13.43 | -11.56 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -2.26 | -2.06 | 47.37 | 95.88 | 42.51 | 118.35 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | -0.35 | 2 | 1 | -2.59 | -2.13 | -12.5 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -0.64 | 8.03 | 17.77 | 59.72 | 17.77 | 61.67 | False |  | mild_accumulation | 0.07 | -0.03 | 2 | 2 | 2.26 | 2.82 | -4.43 | 25 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -11.9 | -19.25 | 29.62 | 160.56 | 18.31 | 163.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.03 | 0.56 | 1 | 1 | -13.16 | -11.01 | -27.19 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 9.06 | 2.54 | 44.88 | 45.49 | 47.53 | 50.27 | True | 近60日漲幅>40% | distribution_warning | -0.53 | -0.85 | 1 | 1 | 8.18 | 6.78 | -9.86 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -12.18 | -9.85 | 28.37 | 70.73 | 22.18 | 100.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.15 | 0.35 | 2 | 2 | -10.68 | -9.65 | -24.68 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | -3.72 | 6.78 | 25.26 | 37.64 | 25.48 | 38.96 | False |  | mild_accumulation | 0.54 | 0.68 | 1 | 1 | -3.89 | -0.64 | -17.35 | 18 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -6.16 | 2.64 | 82.15 | 213.73 | 67.62 | 243.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.4 | -0.15 | 2 | 2 | 1.82 | 1.0 | -13.07 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | -12.9 | -7.8 | 42.66 | 33.52 | 40.67 | 65.65 | True | 近60日漲幅>40% | distribution_warning | -0.54 | -0.2 | 1 | 1 | -2.52 | -4.69 | -22.34 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 5.93 | 16.02 | 56.73 | 45.34 | 53.67 | 63.22 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.43 | -0.23 | 1 | 2 | 8.52 | 8.59 | -6.29 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | -0.86 | 0.0 | 12.54 | 32.38 | 22.74 | 49.57 | False |  | mild_accumulation | 0.9 | 0.44 | 1 | 1 | -3.61 | -1.71 | -20.21 | 19 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -2.29 | 29.39 | 117.96 | 138.2 | 125.63 | 137.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.77 | 1.74 | 2 | 2 | 10.86 | 11.93 | -11.09 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -6.53 | 15.55 | 37.63 | 43.0 | 36.51 | 47.49 | False |  | mild_accumulation | 0.54 | 0.01 | 2 | 1 | 1.99 | 2.37 | -9.69 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 0.13 | 10.81 | 50.57 | 28.71 | 50.86 | 57.17 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 2.44 | 0.5 | 2 | 1 | 5.69 | 5.3 | -9.21 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -3.16 | 4.35 | 5.14 | 7.6 | 9.52 | 19.22 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -2.2 | -2.0 | -13.62 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -10.59 | -17.6 | 19.27 | 51.77 | 22.15 | 54.29 | False |  | distribution_warning | -2.69 | -2.38 | 1 | 0 | -11.62 | -9.39 | -27.28 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 3.45 | 11.11 | 35.59 | 76.9 | 37.14 | 84.62 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -0.5 | 0 | 0 | 5.49 | 3.98 | -14.29 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -11.25 | -13.29 | 32.23 | 21.08 | 28.67 | 49.74 | False |  | distribution_warning | -2.2 | -0.43 | 1 | 1 | -10.82 | -9.57 | -23.45 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -6.51 | -9.53 | 37.09 | 130.45 | 31.76 | 142.95 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.98 | 0.04 | 1 | 1 | -4.34 | -4.31 | -19.08 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -3.45 | -2.33 | 56.7 | 61.22 | 53.59 | 78.05 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -3.82 | -3.37 | 0 | 1 | -1.35 | 0.7 | -7.37 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -2.01 | 1.5 | -1.79 | -6.4 | 4.4 | 4.4 | False |  | distribution_warning | -0.1 | -0.18 | 1 | 0 | -1.49 | -1.08 | -4.04 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | -3.0 | -0.38 | -1.15 | -2.26 | 7.02 | 7.02 | False |  | strong_accumulation | 0.18 | 0.32 | 2 | 2 | -0.82 | -1.09 | -10.38 | 16 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | -6.32 | 14.24 | 8.6 | -2.01 | 19.65 | 19.65 | False |  | strong_accumulation | 1.22 | 1.81 | 3 | 3 | 2.13 | 2.33 | -8.7 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -6.7 | -0.95 | -15.04 | -30.79 | 4.5 | 4.5 | False |  | mild_accumulation | -0.11 | 0.81 | 1 | 3 | -3.55 | -4.07 | -15.73 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -6.04 | 7.69 | -6.04 | -20.0 | 10.24 | 10.24 | False |  | distribution_warning | -0.21 | -0.15 | 1 | 2 | 0.17 | -0.04 | -7.89 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 128.48525684217282 | 290.35375415914626 | -9.58 | 14.81 | 4.83 | -9.21 | 15.67 | 15.67 | False |  | distribution_warning | -0.1 | -0.89 | 2 | 1 | 0.4 | 0.46 | -12.5 | 12 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | -4.63 | 4.1 | -20.54 | -22.8 | 15.11 | 15.11 | False |  | distribution_warning | -0.32 | -0.32 | 0 | 0 | -0.07 | -0.87 | -21.04 | 11 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -4.13 | 2.26 | 20.34 | 6.72 | 27.3 | 27.3 | False |  | strong_accumulation | 1.24 | 1.43 | 3 | 3 | -1.64 | -1.05 | -8.92 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -13.15 | -16.56 | -33.16 | -38.62 | 3.37 | 3.37 | False |  | strong_accumulation | 1.25 | 1.32 | 3 | 3 | -15.35 | -13.07 | -34.97 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | -2.68 | 10.55 | 1.87 | -1.36 | 11.11 | 11.11 | False |  | mild_accumulation | -0.04 | 0.37 | 1 | 2 | 1.31 | 1.5 | -5.22 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -0.97 | -14.23 | -15.98 | -13.14 | 3.02 | 3.02 | False |  | distribution_warning | -4.59 | -4.76 | 1 | 2 | -2.23 | -4.33 | -22.64 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -4.21 | 5.26 | 54.56 | 107.47 | 62.07 | 110.08 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.07 | -1.24 | 1 | 0 | -3.28 | 0.73 | -16.39 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | -2.9 | 21.82 | 52.79 | 36.46 | 54.56 | 60.48 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.33 | 0.36 | 2 | 1 | 7.05 | 7.91 | -4.96 |  | fail_already_priced_in |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | -8.23 | 23.69 | 47.43 | 39.47 | 48.25 | 57.5 | True | 近60日漲幅>40% | strong_accumulation | 0.39 | 0.51 | 3 | 3 | 3.63 | 4.49 | -9.79 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | -2.76 | 32.89 | 45.5 | 69.89 | 49.13 | 74.34 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 1.08 | 1.28 | 3 | 3 | 7.06 | 8.09 | -4.17 |  | fail_already_priced_in |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | -2.5 | 11.24 | 42.58 | 66.37 | 42.89 | 70.0 | True | 近60日漲幅>40% | distribution_warning | 0.0 | -0.03 | 1 | 1 | 3.01 | 4.03 | -4.88 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | -1.69 | 36.62 | 31.01 | 56.37 | 39.61 | 57.14 | True | 近20日漲幅>25% | strong_accumulation | 1.41 | 1.67 | 3 | 3 | 7.56 | 8.3 | -4.92 |  | fail_already_priced_in |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | -1.63 | 30.5 | 21.21 | 35.47 | 36.65 | 39.08 | True | 近20日漲幅>25% | strong_accumulation | 0.84 | 0.86 | 3 | 3 | 11.58 | 10.34 | -4.28 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 0.64 | -7.42 | 32.03 | 16.75 | 32.03 | 39.0 | False |  | mild_accumulation | 0.06 | 0.0 | 3 | 0 | -3.58 | -2.58 | -20.6 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 52.80006873442736 | 30.333657817463656 | -6.01 | 4.78 | 34.22 | 35.88 | 32.86 | 45.03 | False |  | mild_accumulation | 0.58 | -0.06 | 2 | 1 | 0.76 | 0.78 | -7.85 | 19 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | -5.2 | 3.24 | 12.83 | 18.6 | 18.06 | 29.44 | False |  | mild_accumulation | 1.88 | -2.09 | 2 | 1 | -2.15 | -1.92 | -10.53 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -4.42 | -7.91 | 44.59 | 131.4 | 54.42 | 117.22 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.66 | -4.4 | 1 | 1 | -2.53 | -1.86 | -17.0 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -6.04 | -15.38 | 11.08 | 45.95 | 4.88 | 78.26 | False |  | distribution_warning | -0.55 | -0.88 | 1 | 1 | -10.18 | -8.96 | -25.08 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 92.4008479108611 | 7.500180953989433 | -3.79 | 8.69 | 33.72 | 25.46 | 32.63 | 46.75 | False |  | strong_accumulation | 1.8 | 1.51 | 3 | 3 | -0.31 | 1.01 | -8.65 | 18 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -5.49 | -9.93 | 7.53 | 4.84 | 17.31 | 25.42 | False |  | distribution_warning | -1.86 | -0.81 | 1 | 0 | -5.49 | -4.39 | -21.06 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 7.87 | -0.74 | 53.22 | 118.06 | 49.54 | 118.06 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.17 | -1.84 | 0 | 1 | 3.12 | 3.55 | -8.38 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -3.15 | -25.3 | -5.27 | 58.46 | 9.39 | 60.82 | False |  | distribution_warning | -1.64 | -1.92 | 0 | 0 | -12.25 | -10.35 | -30.03 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -3.02 | 6.43 | 25.23 | 11.43 | 28.77 | 28.77 | False |  | mild_accumulation | 2.83 | 2.41 | 1 | 1 | 2.44 | 0.73 | -16.0 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -14.29 | -12.5 | 85.02 | 54.41 | 81.03 | 86.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -6.02 | -5.88 | 1 | 1 | -10.63 | -8.07 | -23.08 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -9.01 | -7.78 | 1.48 | 101.97 | 4.05 | 116.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.02 | -0.03 | 2 | 0 | -11.74 | -9.5 | -26.58 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -6.06 | -28.6 | 78.85 | 141.25 | 73.02 | 141.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.91 | -4.92 | 0 | 0 | -12.02 | -8.63 | -30.08 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -6.71 | -3.77 | 56.12 | 218.75 | 56.12 | 280.6 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.63 | 0.24 | 2 | 2 | -8.45 | -5.74 | -24.63 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -6.99 | -14.04 | 126.93 | 51.42 | 130.0 | 140.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -6.96 | -4.74 | -21.78 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 71.36506452239956 | 62.24907879043217 | -11.3 | -17.78 | 26.96 | 18.81 | 27.59 | 36.17 | False |  | distribution_warning | -1.34 | -2.3 | 1 | 1 | -11.63 | -9.08 | -23.6 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -7.1 | -10.9 | 13.15 | 7.21 | 12.76 | 22.47 | False |  | strong_accumulation | 0.41 | 0.23 | 2 | 2 | -7.08 | -6.04 | -16.58 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -4.28 | -4.79 | 8.81 | 28.78 | 14.38 | 31.62 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.44 | -3.77 | -23.34 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -9.05 | -5.35 | 86.89 | 115.09 | 87.29 | 115.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.41 | -0.77 | 1 | 2 | -3.55 | -5.14 | -25.71 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -12.49 | -17.7 | 49.69 | 44.11 | 47.86 | 59.05 | True | 近60日漲幅>40% | mild_accumulation | -0.19 | 2.13 | 2 | 3 | -19.81 | -13.3 | -32.14 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -16.42 | -8.57 | -1.32 | 22.27 | 0.0 | 32.86 | False |  | mild_accumulation | 3.78 | 0.61 | 3 | 1 | -12.45 | -11.01 | -25.83 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -4.91 | -9.36 | 19.53 | 85.54 | 18.99 | 88.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.87 | -1.06 | 0 | 0 | -4.1 | -3.44 | -16.47 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -5.87 | -2.88 | -7.16 | 41.0 | 10.13 | 46.52 | False |  | strong_accumulation | 0.49 | 1.68 | 2 | 2 | -2.94 | -3.68 | -16.17 | 19 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -14.17 | -1.85 | 41.33 | 58.45 | 40.21 | 71.8 | True | 近60日漲幅>40% | strong_accumulation | 0.37 | 2.91 | 2 | 2 | -10.53 | -8.05 | -21.19 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -7.54 | -14.93 | 76.24 | 60.57 | 73.06 | 79.89 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -6.07 | -4.47 | 0 | 1 | -12.36 | -6.68 | -24.94 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | -4.68 | -5.51 | 2.52 | 17.69 | 9.4 | 23.95 | False |  | strong_accumulation | 1.05 | 1.36 | 2 | 2 | -4.51 | -5.01 | -17.68 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 1.43 | -0.11 | -17.95 | -25.89 | 8.12 | 8.12 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 2.28 | 2.08 | -19.39 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 112.585794273422 | 77.27049729091536 | -4.85 | -3.99 | 24.71 | 59.16 | 25.59 | 59.64 | False |  | mild_accumulation | 0.04 | 0.28 | 1 | 2 | -5.57 | -4.16 | -17.96 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -7.14 | 12.5 | 25.36 | 35.0 | 26.26 | 36.58 | False |  | mild_accumulation | 0.67 | -0.01 | 1 | 0 | -1.0 | -0.19 | -13.12 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth |  | 69.95652184172461 | 55.27975193155594 | -9.03 | -11.65 | -2.92 | -4.37 | 0.52 | 2.27 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 0 | -10.22 | -8.29 | -18.94 |  | fail_low_response_condition |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -6.6 | -9.95 | 4.9 | 13.14 | 20.27 | 34.05 | False |  | mild_accumulation | 1.12 | -0.18 | 1 | 0 | -12.37 | -7.93 | -25.47 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | -1.31 | 5.92 | 2.56 | 1.95 | 8.28 | 13.52 | False |  | mild_accumulation | 0.17 | 0.02 | 2 | 1 | 1.89 | 1.52 | -3.95 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -13.84 | -11.83 | -11.83 | -15.66 | 1.1 | 1.1 | False |  | strong_accumulation | 0.62 | 0.51 | 3 | 3 | -14.08 | -12.06 | -23.6 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -4.21 | 2.13 | -12.02 | -23.54 | 5.62 | 5.62 | False |  | distribution_warning | -0.12 | -0.02 | 0 | 0 | -1.87 | -2.0 | -15.13 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | -0.71 | -0.71 | -3.14 | -5.12 | 1.83 | 1.83 | False |  | strong_accumulation | 0.35 | 0.06 | 3 | 3 | -0.63 | -0.61 | -6.4 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -5.41 | 6.21 | -2.6 | -8.91 | 8.25 | 8.25 | False |  | mild_accumulation | 0.97 | 1.08 | 1 | 1 | -0.3 | -0.46 | -10.06 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 6.68 | 11.99 | 69.83 | 61.1 | 65.35 | 83.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.55 | -1.13 | 1 | 1 | 9.83 | 9.58 | -4.88 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -10.0 | -14.71 | -19.44 | 17.57 | 0.38 | 29.21 | False |  | mild_accumulation | 0.33 | 0.0 | 1 | 1 | -11.41 | -10.46 | -30.21 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -8.68 | 7.58 | 146.53 | 118.8 | 144.83 | 150.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.37 | 0.83 | 2 | 2 | 2.68 | 3.42 | -13.94 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -9.42 | 7.67 | -4.0 | -14.51 | 9.87 | 9.87 | False |  | mild_accumulation | 0.22 | -0.06 | 3 | 2 | -0.37 | -0.52 | -11.7 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -6.35 | 3.91 | 81.85 | 95.58 | 80.0 | 111.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.16 | -1.02 | 1 | 0 | 0.44 | 2.07 | -11.06 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -16.27 | -0.49 | 64.08 | 20.8 | 58.79 | 68.67 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.98 | 1.2 | 1 | 2 | -6.08 | -5.3 | -22.2 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -10.42 | -10.42 | 9.69 | 19.44 | 25.36 | 33.54 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -7.04 | -7.04 | -38.66 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -15.38 | -24.19 | 58.38 | 114.54 | 75.87 | 123.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.65 | -0.9 | 2 | 2 | -14.3 | -10.44 | -32.1 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -8.31 | -27.72 | 11.56 | 95.15 | 12.87 | 122.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.81 | -2.68 | 1 | 0 | -12.59 | -12.72 | -34.35 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -13.62 | -8.94 | -19.81 | 31.25 | 0.0 | 40.0 | False |  | mild_accumulation | 1.43 | 3.33 | 1 | 3 | -13.02 | -12.34 | -31.71 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 8.96 | 24.19 | 81.03 | 138.39 | 99.83 | 147.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.33 | 1 | 2 | 15.12 | 15.29 | -4.94 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -13.33 | -5.48 | 15.35 | 195.14 | 8.05 | 199.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.12 | 0.81 | 0 | 2 | -8.31 | -9.93 | -28.72 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -3.41 | -16.81 | 109.97 | 140.88 | 109.52 | 152.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.36 | 2.23 | 1 | 2 | -2.37 | -1.96 | -24.14 |  | fail_already_priced_in |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | -0.75 | 9.37 | -17.38 | -26.0 | 14.82 | 14.82 | False |  | distribution_warning | -0.23 | -0.2 | 0 | 2 | 2.26 | 1.81 | -18.26 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -5.59 | -7.88 | 1.11 | 2.24 | 6.29 | 6.29 | False |  | strong_accumulation | 0.77 | 1.06 | 3 | 2 | -5.77 | -4.88 | -11.8 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | -3.06 | 1.02 | -1.37 | -19.9 | 3.39 | 3.39 | False |  | distribution_warning | -0.07 | -0.03 | 0 | 0 | -1.06 | -0.97 | -9.06 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 10.14 | 22.0 | 41.1 | 43.4 | 38.15 | 46.04 | True | 近60日漲幅>40% | mild_accumulation | -0.06 | 1.67 | 2 | 2 | 15.31 | 13.37 | -2.82 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | 5.53 | -11.72 | 45.0 | 97.48 | 53.53 | 99.24 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.8 | -5.63 | 1 | 1 | 2.16 | 4.18 | -17.14 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -9.61 | -8.38 | -5.63 | 9.5 | 0.19 | 10.63 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -9.38 | -8.17 | -13.83 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 19.21 | 60.9 | 287.2 | 324.56 | 279.91 | 363.6 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.33 | -5.25 | 1 | 1 | 36.01 | 32.31 | -7.63 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -18.33 | -31.14 | 140.48 | 414.43 | 135.8 | 418.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.49 | 1.08 | 1 | 1 | -13.07 | -14.16 | -38.16 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -6.72 | -17.63 | 2.38 | -22.91 | 2.5 | 4.16 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -9.53 | -8.93 | -25.76 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 10.57 | 47.58 | 31.65 | 9.25 | 51.87 | 51.87 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.04 | -0.5 | 1 | 1 | 16.19 | 14.89 | -11.17 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -12.53 | 37.29 | 387.36 | 1301.38 | 375.35 | 1378.1 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.04 | 3.47 | 1 | 3 | 6.26 | 8.69 | -20.43 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 24.71 | 31.2 | 47.09 | 28.12 | 52.56 | 54.72 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 2.29 | 0.13 | 3 | 2 | 23.35 | 20.66 | -2.96 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -6.52 | -3.57 | -16.13 | 41.25 | 3.69 | 51.46 | False |  | distribution_warning | -0.38 | 0.0 | 1 | 0 | -8.38 | -7.44 | -24.52 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -9.29 | -23.51 | -16.52 | -9.0 | 0.35 | 2.54 | False |  | mild_accumulation | -0.61 | 1.27 | 1 | 1 | -15.0 | -13.9 | -31.14 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -13.93 | -15.84 | 19.48 | -3.47 | 17.46 | 20.0 | False |  | mild_accumulation | 1.14 | 0.49 | 1 | 1 | -13.53 | -13.09 | -25.54 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -15.4 | -16.11 | 40.21 | 135.05 | 46.89 | 140.12 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.73 | 0.0 | 0 | 0 | -9.47 | -10.16 | -34.69 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | -6.81 | -21.31 | 62.09 | 92.31 | 60.69 | 112.42 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.49 | 0 | 0 | -9.08 | -7.57 | -23.21 |  | fail_low_response_condition |