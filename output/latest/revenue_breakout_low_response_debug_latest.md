# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-17 16:42:53 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 587007 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 294 |
| low_response_pass | 54 |
| already_priced_in_excluded | 25 |
| overheat_pass | 29 |
| score_pass | 28 |
| theme_priority_pass | 21 |
| final_rows | 21 |

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
| fail_low_response_condition | 240 |
| fail_already_priced_in | 25 |
| fail_defensive_or_traditional_excluded | 7 |
| missing_or_insufficient_price_metrics | 6 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | 4.72 | 3.26 | -9.76 | -27.45 | 11.0 | 11.0 | False |  | mild_accumulation | -0.56 | 0.51 | 2 | 2 | 5.79 | 3.42 | -12.25 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -4.7 | 0.45 | -3.04 | -5.11 | 2.76 | 2.76 | False |  | mild_accumulation | -0.35 | 0.51 | 1 | 1 | -0.82 | -1.04 | -6.3 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -0.8 | 3.35 | -2.12 | -6.57 | 9.14 | 9.14 | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | 0.64 | -0.05 | -7.5 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 3.21 | 18.82 | 12.94 | 15.71 | 22.96 | 22.96 | False |  | strong_accumulation | 0.5 | 0.57 | 3 | 3 | 8.09 | 6.36 | -10.51 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -0.65 | 10.36 | -11.75 | 13.65 | 15.95 | 24.12 | False |  | mild_accumulation | 0.24 | -0.01 | 1 | 1 | 2.13 | 1.3 | -13.42 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -5.14 | -5.02 | 25.96 | 16.46 | 30.52 | 30.52 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -2.38 | 0.06 | -9.45 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -12.24 | -11.71 | 75.42 | 103.32 | 80.15 | 117.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.05 | -0.88 | 1 | 1 | -15.82 | -10.97 | -33.48 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.24 | 7.44 | 5.01 | -1.41 | 10.85 | 10.85 | False |  | strong_accumulation | 1.82 | 1.2 | 2 | 2 | 0.17 | 0.75 | -9.01 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 67.39 | 96.43 | 103.06 | 128.08 | 113.41 | 141.83 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.76 | 2.47 | 2 | 2 | 64.99 | 54.11 | 0.0 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 2.53 | 10.02 | 6.75 | 1.57 | 15.51 | 15.51 | False |  | strong_accumulation | 0.36 | 0.4 | 2 | 2 | 7.75 | 6.28 | -1.52 | 24 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 5.6 | 21.46 | 10.98 | 45.58 | 32.24 | 53.64 | False |  | distribution_warning | -0.5 | -1.49 | 0 | 0 | 11.0 | 9.84 | -7.52 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 17.79 | 35.24 | 94.71 | 82.62 | 110.16 | 130.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.13 | 0.18 | 1 | 2 | 20.09 | 18.37 | -7.99 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 4.39 | 7.07 | -3.76 | -12.94 | 12.88 | 12.88 | False |  | strong_accumulation | 0.17 | 0.42 | 2 | 3 | 5.63 | 3.27 | -13.17 | 20 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 36.0 | 72.88 | 118.57 | 179.45 | 120.94 | 185.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.49 | 2 | 2 | 31.09 | 31.33 | -8.25 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | 7.67 | 14.54 | 8.75 | 325.56 | 39.83 | 348.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.27 | 3.81 | 2 | 2 | 2.17 | 2.88 | -10.28 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | 22.84 | 74.56 | 85.12 | 179.89 | 137.47 | 189.24 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.98 | 1.71 | 1 | 1 | 24.28 | 24.7 | -1.0 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 0.2 | 0.6 | 59.42 | 106.2 | 66.89 | 128.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.34 | -1.03 | 1 | 0 | 0.83 | 2.24 | -7.42 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 4.64 | 9.48 | 20.0 | 55.29 | 23.53 | 61.26 | False |  | mild_accumulation | 0.06 | -0.01 | 2 | 2 | 5.39 | 5.13 | -4.15 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -13.06 | -1.76 | 46.71 | 189.99 | 52.22 | 206.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.58 | 0.44 | 2 | 1 | -8.15 | -5.43 | -20.21 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 88.80451818624007 | 107.89432287557707 | -5.6 | -6.05 | 20.16 | 24.21 | 27.71 | 29.24 | False |  | distribution_warning | -0.75 | -1.18 | 1 | 1 | -8.4 | -4.86 | -18.06 | 13 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 4.18 | 6.61 | 42.41 | 127.2 | 60.42 | 137.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.32 | 0.63 | 1 | 2 | 2.05 | 2.87 | -9.87 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | -4.23 | 21.43 | 33.57 | 31.23 | 34.53 | 43.85 | False |  | mild_accumulation | 0.31 | 0.26 | 1 | 1 | 6.08 | 5.17 | -14.61 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 6.45 | 10.87 | 86.05 | 223.99 | 100.39 | 254.95 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -0.49 | 1 | 1 | 2.69 | 5.35 | -7.72 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | 9.14 | -12.56 | 34.05 | 22.48 | 51.31 | 75.7 | True | 距60日低點反彈>50% | distribution_warning | -3.38 | -3.51 | 0 | 0 | -0.98 | 2.18 | -17.63 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 6.22 | 16.36 | 39.89 | 38.38 | 55.91 | 55.91 | True | 距60日低點反彈>50% | mild_accumulation | 1.21 | 1.08 | 1 | 2 | 5.96 | 7.83 | -10.49 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | 4.47 | 17.15 | 1.26 | 35.58 | 28.6 | 56.71 | False |  | strong_accumulation | 4.5 | 4.21 | 2 | 2 | 2.49 | 2.23 | -16.4 | 21 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 21.39 | 49.15 | 95.96 | 168.92 | 120.15 | 182.85 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.76 | 0.63 | 2 | 2 | 22.46 | 22.55 | 0.0 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 14.96 | 21.16 | 40.51 | 47.87 | 42.49 | 52.51 | True | 近60日漲幅>40% | mild_accumulation | 0.64 | 0.02 | 3 | 1 | 13.18 | 12.12 | -6.62 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 16.36 | 21.15 | 40.78 | 36.82 | 58.65 | 64.34 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.8 | 0.79 | 1 | 1 | 13.98 | 14.48 | -5.06 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -1.75 | 6.67 | 3.51 | 6.46 | 11.11 | 20.95 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 3.13 | 2.05 | -6.98 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -3.27 | -0.8 | 14.34 | 75.21 | 49.16 | 85.12 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.73 | 1 | 0 | -4.64 | -2.8 | -18.8 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 10.42 | 12.52 | 43.43 | 71.5 | 48.23 | 86.84 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -0.17 | 1 | 0 | 7.61 | 6.84 | -13.83 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -1.8 | -1.56 | 44.52 | 27.81 | 61.98 | 70.59 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.29 | -0.07 | 1 | 1 | -2.19 | 0.42 | -12.79 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 0.86 | 0.0 | 64.56 | 138.29 | 63.87 | 162.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.97 | -3.65 | 1 | 0 | -3.59 | -0.8 | -15.46 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 8.69 | 32.35 | 46.99 | 89.44 | 70.79 | 94.22 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.83 | -0.01 | 1 | 1 | 9.04 | 11.83 | -0.92 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 0.56 | 4.03 | 0.44 | -4.34 | 7.37 | 7.37 | False |  | distribution_warning | -0.06 | -0.17 | 2 | 1 | 2.58 | 1.97 | -1.31 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_降級_TDCC轉弱 | 57.09899455038421 | 42.50276733448348 | 1.14 | -3.97 | -3.97 | 1.14 | 9.92 | 9.92 | False |  | distribution_warning | -0.61 | -0.82 | 1 | 1 | 1.99 | 1.91 | -7.96 | 12 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 12.62 | 17.56 | 13.86 | 10.55 | 26.84 | 26.84 | False |  | strong_accumulation | 1.26 | 2.12 | 3 | 3 | 14.31 | 12.33 | -0.14 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -4.71 | 0.68 | -17.59 | -25.83 | 11.25 | 11.25 | False |  | mild_accumulation | -0.08 | 0.82 | 1 | 3 | 2.37 | 1.17 | -18.35 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | 3.88 | 6.73 | -3.6 | -18.48 | 12.34 | 12.34 | False |  | distribution_warning | -0.19 | -0.29 | 1 | 1 | 5.78 | 3.72 | -6.14 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 18.23 | 22.08 | 18.23 | 13.21 | 27.93 | 27.93 | False |  | strong_accumulation | 0.25 | 0.31 | 2 | 2 | 17.92 | 14.37 | -1.23 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 5.49 | 2.6 | -17.4 | -17.92 | 19.03 | 19.03 | False |  | distribution_warning | -0.42 | -0.75 | 0 | 0 | 6.05 | 3.27 | -19.84 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 5.7 | 4.12 | 27.49 | 22.51 | 34.87 | 34.87 | False |  | strong_accumulation | 1.17 | 1.27 | 2 | 3 | 5.0 | 5.09 | -3.5 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 86.14284031322353 | 42.934476141944494 | -5.78 | 0.0 | -28.54 | -23.85 | 25.37 | 25.37 | False |  | strong_accumulation | 0.76 | 0.51 | 2 | 2 | 2.27 | 1.15 | -30.46 | 18 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 69.90066780612314 | 22.241457982263142 | 6.67 | 11.44 | 4.67 | 4.67 | 14.17 | 14.17 | False |  | distribution_warning | -0.49 | -0.3 | 0 | 1 | 8.77 | 7.0 | -1.75 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | 4.35 | -12.55 | -8.09 | 2.86 | 8.54 | 8.54 | False |  | distribution_warning | -5.18 | -5.76 | 0 | 1 | -4.88 | -4.11 | -18.49 | 12 | selected |
| 2851 | 中再保 | 金融保險業 | defensive_or_traditional |  | 1113.1485058158516 | 203.7258536468597 | 9.89 | 14.06 | 32.95 | 55.66 | 39.59 | 57.17 | False |  | mild_accumulation | 0.15 | -0.02 | 2 | 1 | 12.2 | 12.29 | -0.49 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -12.69 | 28.36 | 64.59 | 112.35 | 68.35 | 116.81 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.51 | -1.09 | 1 | 0 | 7.24 | 7.54 | -13.71 |  | fail_already_priced_in |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 72.52927583818101 | 37.88073490992248 | 9.48 | 18.88 | 16.51 | 22.12 | 28.72 | 28.72 | False |  | mild_accumulation | 0.26 | 0.2 | 2 | 1 | 14.19 | 11.02 | -1.3 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 14.83 | 41.0 | 56.11 | 41.74 | 57.93 | 62.28 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.75 | 0.76 | 3 | 2 | 20.55 | 19.37 | -2.52 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | 13.5 | 44.22 | 58.3 | 61.91 | 64.25 | 68.65 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.45 | 0.52 | 3 | 3 | 24.55 | 22.56 | -2.99 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 9.42 | 41.12 | 52.53 | 76.09 | 57.29 | 78.17 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.1 | 1.32 | 3 | 3 | 23.04 | 19.85 | -3.05 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 2.14 | 21.94 | 50.9 | 73.7 | 51.59 | 75.76 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 0.01 | 0.02 | 1 | 1 | 10.21 | 9.99 | -1.04 |  | fail_low_response_condition |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 13.99 | 36.69 | 36.4 | 68.48 | 42.67 | 69.79 | True | 近20日漲幅>25% | strong_accumulation | 0.86 | 0.99 | 2 | 2 | 23.9 | 20.05 | -2.83 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 11.16 | 22.39 | 16.51 | 30.99 | 26.88 | 32.18 | False |  | strong_accumulation | 0.34 | 0.41 | 2 | 2 | 15.49 | 12.58 | -1.22 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 341.3211844301598 | 175.7452659074452 | 6.61 | 23.48 | 37.86 | 51.87 | 38.4 | 53.35 | False |  | strong_accumulation | 0.16 | 0.18 | 2 | 2 | 12.16 | 11.44 | -2.34 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 2.0 | 19.72 | 45.71 | 16.44 | 49.56 | 49.56 | True | 近60日漲幅>40% | mild_accumulation | 0.05 | 0.0 | 2 | 0 | 4.85 | 4.35 | -14.57 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 52.80006873442736 | 30.333657817463656 | 6.52 | 10.74 | 37.15 | 41.35 | 38.72 | 47.9 | False |  | distribution_warning | -0.47 | -0.09 | 1 | 1 | 6.07 | 6.97 | -1.76 | 14 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 3.08 | 6.35 | 32.67 | 36.18 | 36.04 | 39.44 | False |  | distribution_warning | -1.44 | -4.06 | 1 | 0 | 3.94 | 4.81 | -5.96 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 1.12 | 1.35 | 25.0 | 176.07 | 53.06 | 190.7 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.07 | -4.52 | 1 | 1 | -4.94 | -1.55 | -17.73 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -9.04 | -5.21 | 18.55 | 71.38 | 23.5 | 86.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.07 | -0.86 | 0 | 1 | -8.59 | -6.77 | -21.43 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 92.4008479108611 | 7.500180953989433 | 8.14 | 19.74 | 30.78 | 26.63 | 38.81 | 51.08 | False |  | strong_accumulation | 2.59 | 2.62 | 3 | 3 | 8.44 | 7.99 | -5.96 |  | fail_low_response_condition |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -0.14 | 9.13 | 16.53 | 11.55 | 26.34 | 31.78 | False |  | mild_accumulation | -1.59 | 2.36 | 1 | 1 | -3.44 | 0.04 | -17.06 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -5.59 | -10.8 | 38.1 | 91.99 | 53.2 | 100.27 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.0 | 0 | 1 | -7.23 | -4.65 | -15.86 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -20.28 | -23.16 | -7.05 | 51.35 | 13.71 | 67.16 | False |  | distribution_warning | -0.98 | -1.16 | 1 | 1 | -18.2 | -13.63 | -27.27 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 97.9444020544591 | 26.69919866889564 | 17.65 | 16.7 | 21.85 | 15.77 | 36.79 | 36.79 | False |  | mild_accumulation | -0.95 | 0.4 | 1 | 1 | 11.1 | 12.89 | 0.0 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | 9.5 | 7.08 | 88.08 | 84.5 | 114.48 | 114.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.21 | -5.65 | 1 | 1 | 0.83 | 7.31 | -11.36 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -19.09 | 1.5 | -4.91 | 161.27 | 15.9 | 160.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.07 | -0.03 | 1 | 0 | -2.96 | -3.1 | -19.19 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -15.38 | -1.53 | 31.4 | 196.15 | 92.5 | 214.03 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.44 | -1.29 | 1 | 1 | -14.63 | -9.06 | -27.63 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -15.05 | 6.75 | 148.31 | 241.95 | 165.46 | 301.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.06 | 1.34 | 3 | 2 | -3.35 | -1.05 | -15.05 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -0.45 | 17.26 | 105.83 | 67.23 | 145.28 | 149.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -3.07 | -0.11 | -18.84 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 71.36506452239956 | 62.24907879043217 | -8.65 | 2.52 | 42.5 | 34.43 | 45.26 | 49.84 | True | 近60日漲幅>40% | strong_accumulation | 1.66 | 1.79 | 2 | 2 | -7.11 | -2.73 | -15.93 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -3.59 | 0.58 | 15.56 | 15.95 | 23.76 | 30.71 | False |  | distribution_warning | -0.32 | -0.23 | 1 | 1 | -3.66 | -1.12 | -10.97 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -0.27 | -3.16 | 11.85 | 28.67 | 17.57 | 35.29 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.41 | -2.18 | -21.2 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 15.08 | 0.2 | 95.95 | 130.68 | 137.15 | 157.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -2.98 | 2 | 1 | 6.15 | 8.46 | -14.71 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -11.23 | 43.61 | 97.58 | 78.05 | 98.86 | 101.48 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 1.72 | 2 | 2 | 5.49 | 7.36 | -14.04 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | A_優先追蹤 | 2229.0254683224584 | 499.8539070006186 | 3.07 | 8.03 | 16.96 | 53.01 | 30.58 | 59.55 | False |  | strong_accumulation | 2.79 | 0.77 | 2 | 2 | 4.73 | 4.62 | -10.93 | 23 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -6.55 | -13.36 | 17.97 | 69.57 | 23.7 | 89.05 | True | 距120日低點反彈>80% | distribution_warning | -0.76 | -0.66 | 0 | 0 | -7.64 | -4.86 | -16.08 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | 3.53 | 7.32 | 3.23 | 49.15 | 10.69 | 60.0 | False |  | distribution_warning | -0.06 | -0.75 | 2 | 2 | 1.27 | 1.58 | -13.51 | 13 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | -1.96 | -0.57 | -4.63 | -9.56 | 4.17 | 4.17 | False |  | mild_accumulation | 0.32 | -0.07 | 3 | 1 | 0.65 | -0.01 | -8.85 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 2.16 | 7.34 | -0.32 | -20.47 | 10.23 | 10.23 | False |  | strong_accumulation | 0.46 | 0.93 | 2 | 3 | 5.13 | 3.78 | -10.89 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 4.24 | 30.02 | 43.69 | 76.72 | 64.22 | 99.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.54 | 6.07 | 3 | 3 | 11.1 | 11.4 | -6.11 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -17.75 | -0.1 | 61.01 | 69.88 | 85.53 | 85.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -4.49 | -3.45 | 0 | 1 | -8.42 | -3.08 | -22.59 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 5.14 | 2.65 | -4.92 | 20.42 | 16.0 | 32.32 | False |  | mild_accumulation | 0.13 | -0.05 | 2 | 1 | 0.45 | 0.69 | -12.12 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 1.12 | 0.56 | -20.35 | -36.17 | 5.88 | 5.88 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | -0.11 | -1.29 | -23.73 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -1.43 | 3.19 | 7.42 | 102.21 | 38.54 | 111.54 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -4.27 | 1 | 1 | -1.25 | -1.0 | -14.86 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 14.71 | 26.07 | 38.41 | 45.8 | 39.93 | 48.64 | True | 近20日漲幅>25% | mild_accumulation | 0.78 | -0.01 | 2 | 0 | 16.07 | 13.49 | -5.45 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -4.8 | 2.77 | 11.07 | 3.77 | 13.89 | 13.89 | False |  | mild_accumulation | 2.03 | 1.42 | 2 | 1 | -1.72 | -0.62 | -9.74 | 18 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -18.13 | 12.99 | 20.76 | 22.96 | 29.86 | 44.73 | False |  | distribution_warning | -0.89 | -0.23 | 0 | 0 | -4.83 | -1.91 | -19.52 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 6.27 | 6.11 | 2.81 | 6.6 | 9.62 | 16.03 | False |  | mild_accumulation | -0.33 | 0.02 | 1 | 1 | 5.95 | 5.02 | -0.71 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 191.64415257562703 | 643.5739953148809 | -1.45 | 6.53 | 9.33 | 19.05 | 10.13 | 21.56 | False |  | strong_accumulation | 0.48 | 0.49 | 2 | 3 | 1.69 | 1.01 | -10.61 | 21 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -1.32 | 0.9 | -10.54 | -21.6 | 10.02 | 10.02 | False |  | mild_accumulation | -0.04 | 0.01 | 1 | 1 | 3.52 | 1.45 | -13.29 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.71 | 1.81 | -1.74 | -1.4 | 3.3 | 3.3 | False |  | strong_accumulation | 0.6 | 0.04 | 3 | 2 | 0.88 | 0.49 | -5.05 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 10.08 | 12.4 | 11.96 | 6.5 | 17.19 | 17.19 | False |  | mild_accumulation | 0.57 | 0.69 | 1 | 1 | 10.83 | 8.97 | -0.23 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 155.54062108558796 | 134.80726693594198 | -12.43 | 24.84 | 45.04 | 57.17 | 45.57 | 65.41 | True | 近60日漲幅>40% | mild_accumulation | 0.07 | 0.25 | 1 | 1 | 4.15 | 4.96 | -13.39 |  | fail_already_priced_in |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -0.25 | 2.81 | 34.78 | 36.61 | 57.12 | 68.8 | True | 距60日低點反彈>50% | distribution_warning | -2.6 | -2.77 | 0 | 0 | 1.57 | 3.16 | -8.93 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -7.91 | -5.52 | -21.98 | 51.4 | 8.58 | 50.78 | False |  | mild_accumulation | 0.94 | 0.62 | 2 | 1 | -4.9 | -4.05 | -25.38 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | 7.14 | 20.25 | 139.5 | 116.24 | 151.32 | 151.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | 0.24 | 3 | 1 | 8.16 | 12.72 | -4.36 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 149.18224366317995 | 540.6620723440313 | 6.16 | 8.06 | 1.9 | 2.01 | 16.13 | 16.13 | False |  | distribution_warning | -0.46 | -1.03 | 2 | 1 | 8.8 | 6.59 | -1.43 | 15 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 7.34 | 25.96 | 97.81 | 112.99 | 101.49 | 118.15 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | 0.1 | 2 | 1 | 7.11 | 9.08 | -9.38 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | 8.87 | 10.38 | 76.24 | 53.86 | 98.55 | 98.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -8.34 | -6.8 | 0 | 1 | 13.35 | 16.09 | -8.42 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 0.64 | -8.83 | 3.71 | 41.37 | 38.48 | 47.52 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -2.28 | -1.7 | -32.24 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -14.47 | 13.84 | 120.34 | 156.92 | 124.14 | 162.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 0.65 | 2 | 2 | -10.13 | -4.31 | -27.05 |  | fail_already_priced_in |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -15.03 | -25.71 | 27.87 | 82.24 | 43.38 | 124.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -2.77 | 2 | 0 | -21.06 | -16.78 | -33.67 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -10.71 | 2.8 | -0.81 | 30.14 | 8.58 | 66.06 | False |  | strong_accumulation | 1.66 | 0.37 | 2 | 2 | -5.3 | -4.64 | -25.41 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 7.79 | 26.57 | 64.5 | 97.65 | 74.74 | 116.27 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.29 | 1 | 2 | 11.29 | 12.85 | -0.98 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 12.17 | -0.63 | 19.85 | 239.32 | 43.95 | 271.32 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.95 | 0.01 | 0 | 2 | 5.9 | 3.33 | -17.75 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -7.62 | 6.51 | 78.39 | 140.77 | 112.29 | 150.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.65 | -1.13 | 2 | 1 | -10.05 | -6.17 | -28.51 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -3.46 | 3.85 | -2.76 | -32.47 | 8.45 | 8.45 | False |  | mild_accumulation | 0.26 | -0.07 | 3 | 0 | 2.29 | 1.45 | -7.22 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional | D_降級_TDCC轉弱 | 56.34771899764404 | 43.25386406944739 | 2.48 | 4.12 | -18.98 | -30.72 | 13.2 | 13.2 | False |  | distribution_warning | -0.07 | -0.25 | 1 | 2 | 4.52 | 2.53 | -24.0 | 7 | fail_score_lt_8 |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -0.41 | 0.41 | 0.62 | 14.82 | 13.75 | 16.19 | False |  | mild_accumulation | 0.18 | 0.89 | 2 | 1 | -0.55 | 0.28 | -5.61 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 3.89 | 4.28 | -3.72 | -14.02 | 7.95 | 7.95 | False |  | distribution_warning | -0.18 | -0.13 | 0 | 0 | 4.4 | 3.37 | -5.05 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 9.5 | 13.2 | 14.68 | 11.41 | 26.67 | 29.47 | False |  | mild_accumulation | -0.8 | 0.2 | 2 | 2 | 6.9 | 6.08 | -10.1 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -5.9 | 18.78 | 1.59 | 100.86 | 37.65 | 111.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.59 | 4.65 | 1 | 1 | -7.06 | -3.12 | -25.71 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -3.76 | 0.68 | -7.82 | 19.96 | 5.75 | 21.57 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | -0.74 | -0.56 | -10.21 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 32.0 | 38.74 | 204.45 | 226.5 | 210.59 | 254.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.41 | -3.62 | 1 | 1 | 19.84 | 25.67 | -0.11 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -3.98 | -21.05 | 140.21 | 481.9 | 171.08 | 497.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.75 | 1.15 | 0 | 2 | -13.9 | -7.73 | -31.12 |  | fail_already_priced_in |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -7.02 | -13.27 | 7.56 | -17.0 | 11.15 | 11.66 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -8.93 | -6.9 | -20.41 |  | fail_low_response_condition |