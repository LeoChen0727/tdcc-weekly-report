# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-03 07:08:27 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 612522 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 363 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 709 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 97 |
| already_priced_in_excluded | 39 |
| overheat_pass | 58 |
| score_pass | 58 |
| theme_priority_pass | 40 |
| final_rows | 40 |

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
| fail_low_response_condition | 199 |
| fail_already_priced_in | 39 |
| fail_defensive_or_traditional_excluded | 18 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 152.96178992534956 | 138.94580810199872 | 2.43 | -0.94 | -12.45 | -27.49 | 5.5 | 5.5 | False |  | distribution_warning | -0.86 | -1.1 | 1 | 0 | -0.66 | -0.01 | -15.26 | 14 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 3.24 | -4.7 | -4.29 | -6.3 | 4.21 | 4.21 | False |  | distribution_warning | -0.65 | -0.61 | 1 | 0 | 0.59 | 0.97 | -6.3 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 1.4 | -2.95 | -3.21 | -10.17 | 6.78 | 6.78 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | -1.19 | -0.56 | -9.5 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 44.3 | 33.69 | 50.83 | 67.5 | 73.91 | 73.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.56 | 0.56 | 3 | 3 | 34.12 | 32.61 | -2.44 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | -3.05 | 2.88 | -4.67 | 28.83 | 18.67 | 41.58 | False |  | distribution_warning | -0.79 | -0.23 | 0 | 1 | -0.73 | 1.11 | -14.88 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -0.67 | -9.33 | -4.69 | 19.52 | 13.16 | 20.16 | False |  | mild_accumulation | 0.28 | 0.63 | 1 | 1 | -1.52 | -0.65 | -13.37 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -2.98 | -6.27 | 16.59 | 3.76 | 19.1 | 23.62 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -4.36 | -3.15 | -14.23 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | 2.28 | -5.71 | 44.04 | 118.36 | 53.17 | 132.59 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.12 | 0.76 | 3 | 1 | 3.27 | 1.85 | -28.96 |  | fail_already_priced_in |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.61 | -9.85 | 5.43 | -3.55 | 7.52 | 7.8 | False |  | mild_accumulation | 0.7 | 0.01 | 1 | 1 | -2.72 | -1.56 | -12.37 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 11.89 | 88.18 | 103.94 | 159.4 | 129.49 | 159.07 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.62 | -1.38 | 1 | 1 | 22.5 | 24.74 | 0.0 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | 1.59 | -2.04 | -18.99 | -30.94 | 5.49 | 5.49 | False |  | distribution_warning | -0.31 | -0.47 | 1 | 0 | -0.83 | -0.82 | -20.66 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | -4.51 | -3.73 | -1.33 | -10.83 | 5.7 | 5.7 | False |  | mild_accumulation | 0.07 | -0.05 | 2 | 1 | -4.61 | -2.84 | -10.56 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -1.12 | 7.76 | 13.79 | 21.66 | 23.36 | 27.54 | False |  | distribution_warning | -0.38 | -1.45 | 1 | 0 | -4.57 | -1.3 | -16.72 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 7.72 | 47.29 | 136.28 | 145.87 | 131.76 | 174.09 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -1.39 | 0 | 1 | 14.57 | 16.94 | 0.0 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -15.76 | -16.0 | -19.45 |  | 0.68 |  | False |  | distribution_warning | -0.05 | 0.0 | 2 | 0 | -15.48 | -12.64 | -28.99 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 2.22 | -1.67 | -12.94 | -12.35 | 9.49 | 9.49 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | 0.21 | 1.11 | -13.52 | 19 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -0.53 | 59.66 | 89.9 | 249.77 | 149.01 | 249.77 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 1.92 | 3 | 3 | 21.37 | 19.54 | -8.29 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -9.91 | -10.19 | -1.36 | 205.35 | 23.31 | 205.03 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.3 | -1.24 | 2 | 1 | -7.01 | -7.67 | -24.22 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -16.4 | 3.38 | 94.39 | 92.15 | 118.97 | 118.97 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.57 | -0.72 | 1 | 1 | -2.95 | -1.29 | -21.41 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 15.55 | 6.38 | 51.1 | 132.07 | 48.65 | 152.29 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.33 | -0.27 | 2 | 2 | 11.88 | 11.14 | -1.08 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -2.11 | 2.09 | 13.41 | 56.83 | 17.57 | 57.09 | False |  | strong_accumulation | 0.41 | 0.18 | 3 | 2 | 1.69 | 2.34 | -4.22 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 1.14 | -13.16 | 17.55 | 172.5 | 21.43 | 169.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.19 | -0.02 | 2 | 1 | -2.91 | -2.08 | -20.93 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | -6.57 | 8.72 | 52.09 | 54.06 | 51.6 | 55.75 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 4.16 | 4.43 | 1 | 2 | 10.71 | 7.49 | -6.57 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -0.4 | -10.83 | 17.06 | 94.79 | 11.26 | 108.26 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.62 | -0.66 | 2 | 2 | -5.54 | -3.83 | -21.84 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 94.38123673778152 | 82.59499806151248 | 0.68 | -11.51 | 15.67 | 32.73 | 27.9 | 37.43 | False |  | distribution_warning | -0.46 | -0.5 | 0 | 0 | -1.34 | 0.89 | -15.75 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 0.27 | 17.08 | 70.08 | 249.07 | 62.03 | 269.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.52 | 1.68 | 3 | 3 | 7.33 | 6.8 | -6.45 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | -5.54 | -2.45 | 29.24 | 40.94 | 28.78 | 67.29 | False |  | strong_accumulation | 2.18 | 2.19 | 2 | 2 | -0.61 | -2.71 | -21.58 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 1.47 | 19.91 | 48.61 | 39.62 | 52.7 | 68.7 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.77 | 2.78 | 1 | 3 | 8.95 | 9.43 | -4.48 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 17.61 | 9.87 | 32.54 | 78.04 | 48.31 | 78.42 | True | 近120日漲幅>70% | distribution_warning | -5.7 | -7.4 | 0 | 0 | 13.7 | 13.65 | -9.14 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -14.68 | 1.37 | 80.49 | 95.67 | 104.52 | 105.04 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.8 | 0.86 | 1 | 1 | -1.74 | -0.75 | -19.41 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 1.5 | 16.86 | 36.47 | 50.8 | 37.23 | 51.93 | False |  | mild_accumulation | 0.91 | 0.0 | 2 | 1 | 3.01 | 4.99 | -6.15 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | -0.47 | 15.64 | 43.12 | 36.19 | 48.42 | 67.93 | True | 近60日漲幅>40% | strong_accumulation | 4.55 | 4.6 | 3 | 2 | 8.95 | 7.82 | -9.35 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -1.4 | 1.26 | 2.37 | 9.34 | 11.51 | 21.38 | False |  | distribution_warning | -0.19 | 0.0 | 1 | 0 | -1.15 | -0.3 | -12.05 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -10.42 | -27.93 | 5.31 | 24.94 | 7.5 | 34.73 | False |  | distribution_warning | -3.87 | -2.31 | 1 | 0 | -13.06 | -12.23 | -32.64 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | -6.17 | 5.49 | 8.31 | 50.21 | 25.65 | 79.36 | False |  | distribution_warning | -0.58 | -0.87 | 0 | 0 | 5.49 | 3.98 | -13.1 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -8.89 | -14.61 | 14.59 | 17.44 | 21.06 | 47.45 | False |  | distribution_warning | -0.96 | -1.22 | 1 | 1 | -8.82 | -8.08 | -24.63 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 12.48 | 6.99 | 19.85 | 135.42 | 35.67 | 185.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.41 | 0.87 | 1 | 1 | 12.08 | 10.16 | -4.91 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 87.19923905471303 | 44.102711379154506 | -6.36 | -5.11 | 27.16 | 63.46 | 44.59 | 77.35 | False |  | distribution_warning | -3.02 | -2.08 | 0 | 1 | -1.08 | 0.27 | -7.73 | 16 | selected |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -0.91 | -2.24 | -2.68 | -4.91 | 3.69 | 3.69 | False |  | distribution_warning | -0.09 | -0.32 | 1 | 0 | -2.13 | -1.3 | -4.7 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | 4.6 | 2.63 | 2.63 | 5.0 | 12.81 | 12.81 | False |  | mild_accumulation | 0.18 | 0.02 | 2 | 1 | 4.1 | 3.86 | -5.54 | 16 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 1.02 | 9.49 | 12.7 | 8.46 | 21.4 | 21.4 | False |  | strong_accumulation | 0.73 | 1.61 | 2 | 3 | 1.53 | 2.9 | -7.36 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral | B_可觀察 | 506.2302328794015 | -80.54983396731191 | 6.98 | 9.52 | -3.77 | -23.33 | 15.0 | 15.0 | False |  | mild_accumulation | -0.2 | 0.28 | 1 | 3 | 4.93 | 5.35 | -6.69 | 19 | selected |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -0.24 | 4.95 | -5.15 | -16.54 | 11.29 | 11.29 | False |  | distribution_warning | -0.94 | -1.17 | 1 | 1 | -0.12 | 0.82 | -5.78 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | -2.7 | 7.46 | 2.37 | -4.0 | 15.14 | 15.14 | False |  | distribution_warning | -1.12 | -1.16 | 1 | 0 | -1.8 | -0.09 | -12.9 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 0.39 | 7.12 | -17.68 | -17.51 | 18.13 | 18.13 | False |  | mild_accumulation | -0.15 | 0.07 | 1 | 1 | 1.13 | 1.19 | -18.71 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -0.46 | 0.23 | 17.12 | 10.65 | 27.89 | 27.89 | False |  | strong_accumulation | 0.68 | 0.84 | 2 | 2 | -1.37 | -0.28 | -8.49 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -3.77 | -16.38 | -33.51 | -42.41 | 3.37 | 3.37 | False |  | strong_accumulation | 0.12 | 0.04 | 2 | 2 | -12.39 | -9.68 | -34.53 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 2.74 | 9.22 | 2.74 | 5.63 | 14.68 | 14.68 | False |  | mild_accumulation | -0.03 | 0.06 | 1 | 1 | 2.58 | 3.63 | -2.17 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 9203.558823529413 | 30000.69173757892 | -0.97 | 0.99 | -19.05 | -10.53 | 2.51 | 2.51 | False |  | distribution_warning | -1.57 | -0.84 | 1 | 2 | -0.87 | -3.46 | -23.02 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -1.29 | -8.38 | 60.48 | 103.89 | 59.46 | 104.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.6 | -1.34 | 0 | 0 | -3.85 | -0.03 | -16.81 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 4.35 | 3.53 | 27.85 | 29.73 | 33.33 | 54.84 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 6.55 | 5.44 | -11.56 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | -4.52 | 4.63 | 21.75 | 40.41 | 25.72 | 44.59 | False |  | strong_accumulation | 0.54 | 0.24 | 2 | 2 | -0.63 | 0.18 | -8.13 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 5.41 | 8.33 | 14.71 | 21.88 | 23.53 | 38.58 | False |  | mild_accumulation | 0.83 | 0.2 | 1 | 2 | 3.1 | 4.06 | -4.21 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | A_優先追蹤 | 296.8056658653291 | 223.4596397756601 | -9.17 | -15.99 | 36.68 | 56.83 | 48.3 | 65.15 | False |  | mild_accumulation | -0.04 | 0.49 | 2 | 2 | -3.43 | -4.36 | -20.29 | 22 | selected |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 9.38 | -4.03 | 24.55 | 88.97 | 23.42 | 116.6 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.12 | 0.22 | 2 | 2 | 10.95 | 9.53 | -8.97 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | 5.33 | 12.84 | 28.13 | 36.58 | 31.62 | 57.04 | False |  | strong_accumulation | 0.8 | 0.19 | 3 | 3 | 4.72 | 6.67 | -2.25 | 19 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -3.88 | -8.48 | 6.02 | 4.86 | 16.96 | 25.05 | False |  | mild_accumulation | 1.68 | -0.21 | 2 | 0 | -4.2 | -3.48 | -21.29 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 6.3 | -0.84 | 38.29 | 109.9 | 39.7 | 114.81 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.96 | 1 | 1 | 5.55 | 4.33 | -6.34 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | 0.0 | -25.64 | -4.61 | 55.91 | 10.41 | 55.36 | False |  | distribution_warning | -2.02 | -2.52 | 0 | 0 | -5.52 | -6.4 | -29.38 | 16 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -3.25 | 6.79 | 28.64 | 13.2 | 28.64 | 33.49 | False |  | mild_accumulation | 2.13 | 1.43 | 1 | 1 | 4.57 | 3.45 | -12.92 | 18 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -4.03 | -7.08 | 62.99 | 44.33 | 76.65 | 89.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.21 | 0.15 | 2 | 2 | -6.78 | -4.21 | -21.49 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -6.55 | -19.34 | -15.1 | 91.56 | 3.2 | 115.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | 0.0 | 3 | 0 | -9.85 | -7.43 | -26.94 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -3.93 | -23.06 | 58.19 | 103.89 | 62.39 | 111.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.33 | -1.23 | 0 | 0 | -7.08 | -6.36 | -31.02 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 1.66 | -13.26 | 29.97 | 257.85 | 30.39 | 297.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.37 | -0.58 | 2 | 1 | -4.02 | -1.78 | -21.38 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -5.43 | -8.67 | 88.3 | 63.72 | 82.26 | 140.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -3.26 | -2.81 | -21.6 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | -0.37 | -17.48 | 13.03 | 28.71 | 32.51 | 41.43 | False |  | distribution_warning | -1.91 | -1.78 | 0 | 1 | -4.88 | -4.22 | -20.65 | 12 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 5.0 | -2.19 | 14.06 | 22.26 | 19.0 | 33.71 | False |  | distribution_warning | -0.13 | -0.22 | 1 | 1 | 2.34 | 2.25 | -8.93 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | 1.38 | -2.13 | 13.93 | 31.9 | 14.64 | 34.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.0 | -0.35 | -21.2 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 9.9 | 15.74 | 92.07 | 129.74 | 87.35 | 149.07 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.11 | 0.49 | 1 | 2 | 14.84 | 12.39 | -10.42 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -2.06 | -28.39 | 42.51 | 51.82 | 42.71 | 64.31 | True | 近60日漲幅>40% | mild_accumulation | -0.95 | 1.71 | 2 | 2 | -12.93 | -7.38 | -29.89 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -4.15 | -14.76 | -11.49 | 22.74 | 3.59 | 37.01 | False |  | distribution_warning | -2.43 | -0.16 | 2 | 0 | -7.14 | -5.81 | -23.51 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 0.93 | -8.47 | 11.8 | 81.51 | 16.13 | 82.12 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.79 | -1.09 | 0 | 0 | -0.8 | -1.35 | -15.29 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -0.85 | 0.86 | -5.9 | 47.48 | 14.71 | 52.61 | False |  | strong_accumulation | 6.24 | 7.1 | 3 | 3 | 1.49 | 0.71 | -12.69 | 19 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 1.75 | 0.58 | -5.43 | -8.18 | 3.57 | 3.57 | False |  | strong_accumulation | 0.03 | 0.09 | 2 | 2 | -0.43 | -0.04 | -9.38 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | -3.48 | -0.68 | -5.37 | -17.09 | 4.49 | 4.49 | False |  | mild_accumulation | 0.77 | -0.13 | 3 | 1 | -3.4 | -1.88 | -15.53 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -1.76 | -2.62 | 25.99 | 63.73 | 35.48 | 80.71 | True | 距120日低點反彈>80% | distribution_warning | -3.49 | -4.13 | 1 | 1 | -6.03 | -2.16 | -17.1 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 15.58 | -7.63 | 98.28 | 103.54 | 98.96 | 116.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -9.23 | -9.01 | 0 | 0 | 7.47 | 10.64 | -9.8 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 3.72 | 3.13 | 15.65 | 36.09 | 21.48 | 35.07 | False |  | strong_accumulation | 1.11 | 2.31 | 2 | 2 | 5.48 | 4.39 | -8.59 | 24 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 8.59 | 5.06 | -13.02 | -27.52 | 10.0 | 10.0 | False |  | mild_accumulation | 0.27 | 0.01 | 1 | 1 | 3.43 | 2.62 | -16.14 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 112.585794273422 | 77.27049729091536 | -7.25 | -14.38 | 16.63 | 31.96 | 21.33 | 50.15 | False |  | distribution_warning | -4.96 | -9.67 | 1 | 1 | -6.54 | -5.56 | -20.74 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 0.27 | 9.91 | 17.31 | 24.07 | 26.21 | 40.77 | False |  | distribution_warning | -0.05 | 0.0 | 1 | 0 | 1.16 | 3.48 | -9.41 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 0.37 | -12.6 | -4.51 | -0.62 | 5.64 | 7.48 | False |  | distribution_warning | -1.75 | -2.16 | 1 | 0 | -3.15 | -2.29 | -14.81 | 14 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | 9.17 | -9.36 | 26.99 | 31.21 | 35.34 | 50.84 | False |  | mild_accumulation | 0.56 | -0.04 | 1 | 0 | 1.51 | 4.35 | -16.13 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 0.58 | 7.31 | 3.92 | 5.83 | 9.87 | 15.19 | False |  | mild_accumulation | 0.49 | 0.0 | 3 | 0 | 1.91 | 2.16 | -2.54 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -3.04 | -16.27 | -10.64 | -12.0 | 0.63 | 0.63 | False |  | distribution_warning | -0.58 | -0.43 | 2 | 2 | -12.04 | -9.3 | -23.96 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -2.05 | -2.05 | -15.38 | -23.12 | 4.89 | 4.89 | False |  | distribution_warning | -0.17 | -0.01 | 0 | 0 | -2.41 | -1.98 | -15.55 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.36 | -0.36 | -3.78 | -2.44 | 2.56 | 2.56 | False |  | strong_accumulation | 0.57 | 0.1 | 3 | 3 | 0.07 | 0.05 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -0.13 | 6.93 | -5.07 | -6.64 | 8.25 | 8.25 | False |  | mild_accumulation | 1.08 | 0.7 | 1 | 1 | -1.45 | -0.3 | -10.06 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 7.31 | 19.77 | 53.93 | 57.82 | 51.94 | 96.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.48 | 2 | 2 | 13.06 | 11.84 | -3.4 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -2.57 | -16.14 | -26.39 | 28.02 | 1.92 | 30.54 | False |  | mild_accumulation | 0.06 | 0.05 | 1 | 2 | -7.54 | -6.81 | -28.38 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -8.16 | 6.3 | 105.17 | 112.6 | 101.49 | 138.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.34 | 1 | 1 | -3.05 | -1.33 | -18.18 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -1.41 | 2.6 | -2.68 | -12.62 | 9.15 | 9.15 | False |  | mild_accumulation | 0.11 | -0.67 | 2 | 2 | -1.94 | -0.9 | -12.28 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 5.19 | 15.29 | 83.46 | 110.38 | 80.65 | 133.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.14 | 0.02 | 1 | 1 | 9.22 | 10.35 | -1.67 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 70.65666417439758 | 55.92683953560652 | -10.18 | -0.37 | 32.73 | 22.97 | 36.33 | 66.6 | False |  | distribution_warning | -4.67 | -3.73 | 1 | 1 | -6.88 | -4.51 | -23.16 | 12 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 1.4 | -8.98 | 15.04 | 20.78 | 27.11 | 35.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.1 | -3.21 | -37.8 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -7.04 | -20.65 | 75.43 | 95.81 | 76.45 | 111.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.12 | -3.04 | 1 | 1 | -9.54 | -7.29 | -31.87 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -10.05 | -20.62 | -11.09 | 98.45 | 8.45 | 121.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.2 | 0.0 | 2 | 0 | -7.11 | -9.32 | -34.52 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -12.33 | -20.82 | -26.68 | 23.4 | 10.1 | 36.25 | False |  | mild_accumulation | -1.99 | 2.47 | 0 | 3 | -12.58 | -10.53 | -33.54 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 16.74 | 55.17 | 115.61 | 184.4 | 141.35 | 181.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.04 | 2 | 2 | 28.35 | 26.49 | -0.71 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 2.31 | 13.26 | 8.76 | 204.25 | 24.05 | 205.75 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.83 | 0.65 | 0 | 2 | 3.87 | 3.96 | -18.97 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -12.64 | -12.64 | 69.49 | 100.63 | 73.15 | 145.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 1.84 | 1 | 2 | -2.39 | -3.83 | -26.36 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -0.49 | -1.82 | -1.46 | -23.49 | 8.71 | 8.71 | False |  | mild_accumulation | -0.21 | 0.23 | 1 | 1 | -0.67 | -0.04 | -11.07 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -0.66 | -5.6 | 0.66 | 1.79 | 6.06 | 6.06 | False |  | mild_accumulation | 1.08 | -0.03 | 3 | 1 | -4.71 | -3.62 | -11.99 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.13 | -0.75 | -0.5 | -18.97 | 4.17 | 4.17 | False |  | distribution_warning | -0.05 | -0.02 | 0 | 0 | -0.26 | -0.03 | -8.37 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | -3.89 | 18.76 | 22.76 | 34.15 | 29.83 | 38.02 | False |  | strong_accumulation | 1.74 | 2.63 | 3 | 3 | 7.59 | 6.49 | -8.15 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -10.22 | -11.7 | 37.06 | 71.92 | 46.47 | 73.32 | True | 近120日漲幅>70% | distribution_warning | -1.2 | -1.04 | 2 | 2 | -0.02 | -1.21 | -20.95 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -1.82 | -11.8 | -11.51 | -0.19 | 1.51 | 7.6 | False |  | distribution_warning | -1.33 | 0.0 | 0 | 0 | -7.02 | -5.62 | -13.5 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 3.59 | 67.74 | 252.78 | 338.45 | 286.9 | 398.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.18 | -3.65 | 0 | 1 | 32.54 | 29.43 | -4.06 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -0.6 | -7.79 | 150.19 | 400.0 | 153.05 | 441.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.05 | 0.0 | 2 | 0 | -1.24 | -4.02 | -32.35 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -2.77 | -15.56 | -7.13 | -20.7 | 1.33 | 5.31 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -5.03 | -5.72 | -24.94 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | -5.28 | 25.09 | 32.47 | 12.89 | 48.96 | 48.96 | True | 近20日漲幅>25% | distribution_warning | -0.15 | -0.78 | 1 | 0 | 7.12 | 7.96 | -12.86 |  | fail_already_priced_in |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 10.89 | 50.3 | 356.12 | 1669.5 | 371.64 | 1721.17 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.48 | 0.23 | 2 | 2 | 21.9 | 24.75 | -1.96 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | -3.69 | 25.2 | 40.99 | 22.27 | 44.91 | 47.64 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | -0.03 | 0.02 | 2 | 2 | 11.31 | 8.86 | -12.32 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | 0.13 | -4.26 | -15.3 | 54.26 | 9.6 | 60.09 | False |  | mild_accumulation | 1.47 | 0.0 | 2 | 0 | -1.86 | -0.51 | -20.22 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -4.79 | -19.68 | -13.87 | -6.87 | 5.67 | 7.97 | False |  | mild_accumulation | -1.27 | 1.37 | 0 | 1 | -7.42 | -6.99 | -27.49 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -5.18 | -8.92 | 17.22 | -7.58 | 15.22 | 26.33 | False |  | mild_accumulation | 1.16 | 0.49 | 1 | 1 | -6.4 | -5.42 | -21.61 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | 1.67 | -6.97 | 35.13 | 143.44 | 36.42 | 155.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.12 | 0.0 | 1 | 0 | -1.66 | -2.22 | -30.46 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | 1.59 | -6.58 | 71.46 | 110.48 | 71.88 | 129.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | -0.14 | 1 | 1 | 0.88 | 1.21 | -16.95 |  | fail_low_response_condition |
| 7803 | 雲象科技-創 | 生技醫療業 | defensive_or_traditional |  | 1440.6307977736549 | 2.7893555626803463 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |