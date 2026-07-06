# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-06 20:26:20 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 616462 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 93 |
| already_priced_in_excluded | 37 |
| overheat_pass | 56 |
| score_pass | 56 |
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
| fail_low_response_condition | 203 |
| fail_already_priced_in | 37 |
| fail_defensive_or_traditional_excluded | 16 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | 3.86 | 1.42 | -11.89 | -26.87 | 7.5 | 7.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | 1.01 | 1.43 | -13.65 | 20 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 4.19 | -4.27 | -3.86 | -5.49 | 4.67 | 4.67 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | 1.54 | 1.19 | -5.88 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 3.92 | -0.54 | 0.54 | -6.78 | 9.44 | 9.44 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 1.39 | 1.64 | -7.94 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 12.27 | 33.58 | 38.01 | 51.74 | 59.13 | 59.13 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.67 | -0.3 | 2 | 2 | 18.67 | 16.43 | -10.73 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | 5.22 | 0.65 | -2.93 | 20.83 | 17.47 | 23.73 | False |  | mild_accumulation | -0.2 | 0.64 | 1 | 1 | 2.44 | 2.65 | -10.08 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 5.93 | -6.02 | 21.16 | 9.01 | 24.58 | 29.31 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | 0.48 | 1.09 | -10.29 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | 9.78 | -9.55 | 31.17 | 105.56 | 47.8 | 124.44 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | -4.24 | 3 | 0 | 0.73 | -1.67 | -31.45 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | D_降級_TDCC轉弱 | 153.16268341919277 | -7.777041541987246 | 4.07 | 0.48 | 8.07 | -1.52 | 11.35 | 11.64 | False |  | distribution_warning | -0.34 | -0.57 | 1 | 1 | 1.03 | 1.72 | -9.25 | 15 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 10.58 | 81.74 | 110.69 | 156.13 | 131.71 | 146.46 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | 16.76 | 19.95 | -16.4 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 5.35 | -0.32 | 5.35 | -7.22 | 12.3 | 12.3 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | 1.57 | 2.98 | -4.98 | 22 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 3.07 | 0.37 | 16.45 | 13.98 | 25.7 | 29.95 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -3.29 | 0.36 | -15.14 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 9.49 | 38.52 | 126.31 | 139.17 | 126.31 | 170.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 9.36 | 12.47 | -4.48 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -2.96 | -25.88 | -14.99 |  | 1.03 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -13.06 | -10.56 | -28.74 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 7.22 | 7.05 | -6.44 | -8.81 | 15.76 | 15.76 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 5.43 | 5.93 | -7.33 | 21 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 17.98 | 89.56 | 142.33 | 262.98 | 182.45 | 279.11 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 30.03 | 29.45 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -8.83 | -3.67 | 1.76 | 150.87 | 22.46 | 153.51 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -7.07 | -6.98 | -24.74 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -9.85 | 12.96 | 102.88 | 71.83 | 118.38 | 118.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -3.87 | -1.38 | -21.63 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 13.03 | 6.22 | 34.26 | 119.5 | 33.92 | 142.66 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | 6.78 | 5.44 | -6.37 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 2.51 | 6.23 | 14.11 | 50.56 | 18.58 | 51.78 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | 1.98 | 2.6 | -4.58 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 4.81 | -15.01 | 7.92 | 136.44 | 17.84 | 138.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -2.65 | -3.16 | -22.0 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | -0.58 | 9.28 | 40.82 | 41.12 | 39.39 | 49.62 | True | 近60日漲幅>40% | mild_accumulation | 2.17 | 2.99 | 1 | 2 | 5.26 | 2.46 | -10.25 |  | fail_already_priced_in |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 6.06 | -6.84 | 5.15 | 90.51 | 6.99 | 106.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -5.82 | -4.36 | -22.47 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 3.0 | -3.2 | 22.53 | 34.04 | 31.02 | 40.78 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 1.61 | 2.82 | -13.7 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 0.46 | 12.08 | 43.7 | 246.52 | 47.18 | 255.52 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | 2.13 | 1.96 | -12.4 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | 0.71 | 3.34 | 14.1 | 38.25 | 17.49 | 66.36 | False |  | strong_accumulation | 2.08 | 2.37 | 2 | 2 | -1.18 | -2.74 | -22.02 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | -2.94 | 9.54 | 45.05 | 32.0 | 45.37 | 60.78 | True | 近60日漲幅>40% | strong_accumulation | 1.5 | 0.92 | 2 | 2 | 2.88 | 3.39 | -8.97 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 9.08 | 19.62 | 25.42 | 68.15 | 47.25 | 70.93 | False |  | distribution_warning | -3.53 | -3.16 | 1 | 1 | 11.45 | 10.63 | -9.79 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -7.17 | 16.81 | 98.82 | 74.48 | 111.31 | 111.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | 0.61 | 2.34 | -16.73 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 4.4 | 16.86 | 36.96 | 51.97 | 38.81 | 53.67 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 2.71 | 5.18 | -5.08 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | 1.22 | 17.35 | 32.91 | 37.07 | 46.48 | 65.74 | False |  | mild_accumulation | 1.29 | -0.26 | 2 | 2 | 5.79 | 5.18 | -10.54 | 19 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 2.69 | 0.53 | 2.32 | 14.14 | 13.69 | 23.76 | False |  | distribution_warning | -0.1 | 0.0 | 2 | 0 | 0.65 | 1.39 | -10.33 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 469.8305876051363 | 430.4543077358013 | -1.64 | -15.86 | 9.07 | 13.66 | 12.71 | 41.25 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -6.56 | -6.61 | -29.37 | 15 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 11.9 | 22.86 | 11.9 | 69.89 | 35.97 | 94.1 | True | 距120日低點反彈>80% | distribution_warning | -0.06 | -1.16 | 1 | 0 | 12.12 | 10.49 | -5.95 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 7.24 | -9.36 | 27.1 | 26.89 | 29.28 | 57.46 | False |  | distribution_warning | -0.29 | 0.0 | 2 | 1 | -1.38 | -1.34 | -19.51 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 15.11 | 12.93 | 28.43 | 149.05 | 35.05 | 184.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | 10.96 | 8.54 | -5.35 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 5.62 | 6.26 | 16.37 | 57.96 | 51.8 | 86.19 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.39 | -1.69 | 0 | 1 | 3.46 | 4.52 | -3.13 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 2.5 | 0.33 | 0.0 | -1.31 | 7.13 | 7.13 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | 1.09 | 1.74 | -1.53 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral |  | 57.09899455038421 | 42.50276733448348 | 10.04 | 8.37 | 6.74 | 9.2 | 17.77 | 17.77 | False |  | strong_accumulation | 0.69 | 0.7 | 3 | 2 | 7.79 | 6.96 | -1.72 |  | fail_low_response_condition |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 2.17 | 9.81 | 12.98 | 7.96 | 23.68 | 23.68 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 2.5 | 4.12 | -5.62 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 7.13 | -3.43 | -7.01 | -24.46 | 12.75 | 12.75 | False |  | strong_accumulation | 0.15 | 0.52 | 2 | 3 | 2.7 | 2.66 | -8.52 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral | D_降級_TDCC轉弱 | 367.4305802571221 | 58.17838010197999 | 1.89 | 4.85 | -3.36 | -15.13 | 13.39 | 13.39 | False |  | distribution_warning | -1.6 | -1.07 | 0 | 1 | 1.21 | 2.33 | -4.0 | 18 | selected |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 128.48525684217282 | 290.35375415914626 | 2.75 | 10.34 | 7.18 | -5.88 | 19.4 | 19.4 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | 0.83 | 3.01 | -9.68 | 13 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 1.02 | 6.29 | -15.98 | -15.62 | 19.94 | 19.94 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 2.21 | 2.37 | -16.33 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2114.205326762877 | 1780.7414522786555 | 4.41 | 4.65 | 27.3 | 15.53 | 33.53 | 33.53 | False |  | distribution_warning | -0.74 | -0.81 | 1 | 1 | 2.68 | 3.68 | -4.46 | 15 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | 2.07 | -19.98 | -31.75 | -36.58 | 6.48 | 6.48 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -7.99 | -5.88 | -32.33 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 5.45 | 10.48 | 6.42 | 8.41 | 18.25 | 18.25 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 4.67 | 5.74 | -1.69 | 19 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 9203.558823529413 | 30000.69173757892 | 0.49 | -0.48 | -20.46 | -9.65 | 3.52 | 3.52 | False |  | distribution_warning | -1.46 | -1.04 | 1 | 1 | -0.05 | -2.16 | -22.26 |  | fail_low_response_condition |
| 2851 | 中再保 | 金融保險業 | defensive_or_traditional |  | 1113.1485058158516 | 203.7258536468597 | 12.84 | 5.96 | 24.92 | 47.55 | 34.6 | 48.39 | False |  | distribution_warning | -1.04 | -1.13 | 0 | 0 | 3.67 | 5.08 | -4.05 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 3.78 | -11.68 | 58.9 | 107.97 | 61.11 | 104.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | 1.92 | 4.12 | -12.71 |  | fail_already_priced_in |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 4.11 | 4.75 | 35.71 | 70.15 | 37.49 | 70.79 | True | 近120日漲幅>70% | distribution_warning | -0.11 | -0.18 | 1 | 1 | 4.05 | 5.39 | -1.87 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 3.94 | 19.93 | 39.43 | 64.51 | 50.11 | 66.91 | True | 距60日低點反彈>50% | strong_accumulation | 0.69 | 0.78 | 3 | 3 | 8.08 | 10.18 | -1.72 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 3.8 | 25.38 | 23.12 | 41.62 | 43.11 | 45.65 | True | 近20日漲幅>25% | strong_accumulation | 0.59 | 0.62 | 3 | 3 | 9.18 | 9.88 | 0.0 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 3.26 | 7.6 | 9.35 | 34.5 | 35.86 | 57.77 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 7.84 | 6.03 | -9.88 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | 1.07 | 5.41 | 23.93 | 41.06 | 27.26 | 46.36 | False |  | strong_accumulation | 0.61 | 0.58 | 3 | 3 | 0.11 | 1.3 | -7.01 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 26.09 | 22.69 | 38.1 | 41.78 | 44.34 | 61.93 | False |  | strong_accumulation | 1.66 | 2.35 | 2 | 3 | 18.13 | 18.17 | -2.15 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -2.01 | -1.57 | 40.38 | 49.49 | 48.98 | 65.91 | True | 近60日漲幅>40% | strong_accumulation | 0.2 | 1.06 | 2 | 2 | -2.19 | -3.07 | -19.93 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 16.09 | 2.69 | 14.84 | 94.18 | 20.27 | 111.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | 7.86 | 5.31 | -11.3 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 92.4008479108611 | 7.500180953989433 | 5.47 | 12.14 | 28.78 | 35.62 | 31.32 | 56.68 | False |  | distribution_warning | -1.06 | -0.7 | 2 | 2 | 3.21 | 5.31 | -5.24 | 14 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | 1.94 | -3.12 | 7.04 | -3.53 | 19.58 | 27.85 | False |  | mild_accumulation | 1.34 | -0.37 | 2 | 0 | -1.75 | -1.06 | -19.53 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -1.6 | 1.78 | 27.34 | 88.92 | 35.3 | 108.05 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | 2.25 | 0.69 | -9.29 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | 4.78 | -22.06 | -4.58 | 48.47 | 11.17 | 53.15 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -2.26 | -4.96 | -28.9 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | 5.97 | 15.21 | 29.09 | 11.59 | 27.93 | 33.96 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | 3.56 | 3.07 | -12.62 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | 4.87 | -2.56 | 62.11 | 49.19 | 77.47 | 90.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -6.0 | -3.16 | -21.12 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 1.44 | -24.11 | -4.5 | 94.5 | 7.07 | 123.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -3.67 | -3.42 | -24.2 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | 1.1 | -19.56 | 46.4 | 90.62 | 61.95 | 111.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.8 | -1.3 | 0 | 0 | -4.91 | -5.68 | -31.2 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 16.93 | -4.74 | 29.1 | 322.9 | 47.88 | 350.25 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | 9.31 | 9.68 | -10.84 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -0.6 | -5.98 | 63.85 | 63.53 | 49.19 | 135.59 | True | 近60日漲幅>40%；距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -4.72 | -4.39 | -23.35 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | 2.25 | -12.5 | 14.71 | 25.81 | 34.48 | 43.53 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -1.96 | -2.34 | -19.47 | 12 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 12.31 | 3.31 | 17.98 | 25.5 | 24.67 | 40.07 | False |  | strong_accumulation | 0.5 | 0.46 | 2 | 2 | 6.81 | 5.92 | -4.59 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | 4.25 | -0.27 | 12.54 | 30.5 | 14.29 | 32.85 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.03 | -0.32 | -21.2 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 4.19 | 4.42 | 50.0 | 84.94 | 46.66 | 115.19 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -1.67 | -3.13 | -22.61 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | 2.34 | -27.17 | 42.55 | 52.27 | 43.57 | 65.3 | True | 近60日漲幅>40% | distribution_warning | -1.3 | -1.68 | 1 | 1 | -9.3 | -5.68 | -29.47 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 2229.0254683224584 | 499.8539070006186 | 0.89 | -13.41 | -12.4 | 23.63 | 1.35 | 34.05 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -7.74 | -6.89 | -25.17 | 16 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 5.26 | -3.93 | 12.82 | 79.45 | 18.28 | 80.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.54 | -1.12 | 1 | 0 | 1.55 | 0.4 | -13.73 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -0.6 | -2.94 | -11.05 | 41.03 | 7.84 | 40.43 | False |  | strong_accumulation | 4.42 | 4.81 | 2 | 2 | -4.53 | -4.8 | -17.91 | 19 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 1.2 | -1.83 | -4.53 | -15.95 | 5.92 | 5.92 | False |  | distribution_warning | -0.24 | -0.56 | 2 | 0 | -1.9 | -0.5 | -14.37 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 10.0 | -2.12 | 32.15 | 64.3 | 40.34 | 87.2 | True | 距120日低點反彈>80% | distribution_warning | -3.16 | -5.47 | 1 | 0 | -2.35 | 1.27 | -14.13 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 16.94 | -6.25 | 86.57 | 97.37 | 86.26 | 111.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 5.88 | 6.64 | -11.76 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 5.97 | 7.25 | 6.93 | 20.75 | 19.13 | 29.09 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | 2.73 | 1.76 | -10.35 | 24 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -5.53 | -0.22 | -12.94 | -31.43 | 4.47 | 4.47 | False |  | distribution_warning | -0.35 | 0.0 | 0 | 0 | -1.79 | -2.24 | -20.36 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 112.585794273422 | 77.27049729091536 | -1.14 | -6.45 | 20.83 | 29.85 | 23.7 | 53.08 | False |  | mild_accumulation | -1.13 | 0.33 | 1 | 2 | -3.65 | -3.12 | -19.2 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 6.27 | 12.01 | 12.69 | 22.7 | 28.62 | 43.46 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 2.01 | 4.62 | -7.67 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 5.17 | -9.15 | -1.33 | 2.26 | 6.82 | 8.68 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | -1.15 | -1.03 | -13.86 | 14 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | 4.71 | -17.53 | 21.81 | 17.9 | 30.82 | 45.8 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | -0.17 | 0.76 | -18.93 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral | B_可觀察 | 88.65151498619764 | -2.528158661804875 | 1.02 | 5.66 | 3.44 | 5.02 | 10.03 | 15.36 | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | 1.44 | 1.94 | -2.4 | 18 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | 1.41 | -14.85 | -7.56 | -11.72 | 2.53 | 2.53 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -9.32 | -6.64 | -22.77 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 2.1 | -4.17 | -13.64 | -21.4 | 6.85 | 6.85 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.3 | -0.11 | -13.98 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 1.43 | 1.43 | -2.41 | -0.35 | 4.03 | 4.03 | False |  | strong_accumulation | 0.31 | 0.42 | 3 | 3 | 1.37 | 1.24 | -4.38 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 2.29 | 3.75 | -1.83 | -5.19 | 10.45 | 10.45 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | -0.02 | 1.42 | -8.23 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -2.41 | 15.35 | 48.17 | 56.64 | 47.24 | 95.18 | True | 近60日漲幅>40%；距120日低點反彈>80% | strong_accumulation | 1.8 | 1.98 | 2 | 2 | 10.57 | 8.93 | -5.57 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | 2.24 | -13.29 | -22.16 | 20.18 | 5.38 | 34.98 | False |  | strong_accumulation | 0.68 | 0.05 | 2 | 2 | -3.11 | -3.0 | -24.73 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -6.45 | -1.88 | 82.01 | 93.91 | 88.31 | 130.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.49 | 0.47 | 0 | 2 | -6.35 | -4.1 | -20.91 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 1.99 | 1.65 | -0.22 | -13.64 | 11.19 | 11.19 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -0.28 | 0.91 | -10.64 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 7.14 | 13.1 | 61.47 | 87.19 | 75.12 | 126.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | 4.42 | 5.52 | -4.68 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 70.65666417439758 | 55.92683953560652 | 2.4 | -7.74 | 32.3 | 31.44 | 37.69 | 68.26 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -5.32 | -2.91 | -22.39 | 12 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 19.9 | -0.42 | 28.42 | 29.12 | 37.03 | 45.96 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 4.25 | 3.47 | -32.95 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | 0.99 | -19.21 | 69.38 | 99.03 | 78.49 | 113.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.95 | 0.74 | 1 | 2 | -6.3 | -5.35 | -31.09 |  | fail_already_priced_in |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -1.05 | -18.08 | -4.81 | 108.89 | 5.92 | 116.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -7.42 | -10.22 | -36.05 |  | fail_already_priced_in |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -0.31 | -22.38 | -23.68 | 23.17 | 7.41 | 32.92 | False |  | mild_accumulation | -2.38 | 0.82 | 0 | 2 | -12.46 | -11.08 | -35.16 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 13.78 | 54.22 | 122.31 | 185.01 | 150.0 | 185.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 27.3 | 25.25 | -1.7 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 11.23 | 5.82 | -1.65 | 169.74 | 18.79 | 185.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -1.5 | -1.21 | -22.41 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -2.65 | -5.54 | 61.42 | 109.44 | 66.49 | 143.68 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -2.49 | -4.08 | -26.9 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 5.98 | -0.6 | 2.21 | -20.67 | 11.66 | 11.66 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | 2.03 | 2.29 | -8.66 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 6.64 | 15.9 | -0.19 | -17.63 | 28.02 | 28.02 | False |  | mild_accumulation | -0.03 | 0.59 | 1 | 2 | 10.3 | 9.65 | -4.1 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 1.75 | -5.1 | 1.97 | 4.26 | 8.39 | 8.39 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | -2.06 | -1.2 | -10.06 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 1.89 | 1.38 | 0.5 | -17.97 | 5.35 | 5.35 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | 0.74 | 0.92 | -7.34 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | -5.91 | 16.51 | 17.24 | 31.92 | 26.78 | 34.77 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | 3.37 | 3.17 | -10.31 | 20 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 58.86220189113607 | 31.41858931023004 | -7.98 | -2.68 | 36.47 | 47.56 | 42.35 | 62.42 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -2.2 | -3.45 | -23.17 | 18 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | 2.42 | -10.13 | -10.28 | -2.83 | 3.77 | 10.0 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -3.97 | -2.94 | -11.58 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 17.43 | 82.86 | 228.21 | 346.77 | 280.95 | 390.42 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 23.1 | 21.74 | -8.57 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | 0.63 | -8.53 | 112.21 | 384.92 | 120.96 | 425.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.0 | 3 | 0 | -3.48 | -6.0 | -34.39 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 2.77 | -10.67 | -6.35 | -21.27 | 3.22 | 7.27 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -1.95 | -3.27 | -23.54 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 4.71 | 32.17 | 28.14 | 14.89 | 56.85 | 56.85 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 9.84 | 11.24 | -8.25 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 21.19 | 45.43 | 288.55 | 1574.34 | 381.1 | 1631.29 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 19.62 | 21.92 | -1.74 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | -12.71 | 22.13 | 30.38 | 12.77 | 34.93 | 45.75 | False |  | distribution_warning | -0.22 | -0.19 | 1 | 1 | 7.53 | 5.87 | -13.45 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | 3.47 | -8.68 | -18.47 | 49.27 | 5.61 | 54.26 | False |  | distribution_warning | -0.79 | 0.0 | 1 | 0 | -4.96 | -3.9 | -22.2 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -3.01 | -15.94 | -18.54 | -7.64 | 2.84 | 5.07 | False |  | mild_accumulation | 0.4 | -2.35 | 1 | 0 | -8.23 | -8.32 | -29.44 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | 3.14 | -8.17 | 5.56 | -9.44 | 5.69 | 22.88 | False |  | mild_accumulation | 0.02 | 0.5 | 1 | 1 | -8.08 | -6.9 | -23.75 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | 6.05 | -3.1 | 31.93 | 156.74 | 36.02 | 162.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | 0.0 | 1 | 0 | 1.25 | 0.23 | -28.66 |  | fail_low_response_condition |