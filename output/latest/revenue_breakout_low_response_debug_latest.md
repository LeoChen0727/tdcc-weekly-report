# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-30 13:04:00 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 606636 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 363 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 709 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 90 |
| already_priced_in_excluded | 43 |
| overheat_pass | 47 |
| score_pass | 47 |
| theme_priority_pass | 30 |
| final_rows | 30 |

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
| fail_low_response_condition | 206 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 17 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 152.96178992534956 | 138.94580810199872 | -1.43 | 2.48 | -14.81 | -32.57 | 3.5 | 3.5 | False |  | distribution_warning | -0.86 | -1.1 | 1 | 0 | -2.5 | -2.13 | -16.87 | 14 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -1.83 | -3.15 | -6.93 | -10.42 | 0.47 | 0.47 | False |  | distribution_warning | -0.65 | -0.61 | 1 | 0 | -3.7 | -2.83 | -9.66 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -0.83 | -3.51 | -6.3 | -10.08 | 5.31 | 5.31 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | -3.4 | -2.43 | -10.75 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 16.26 | 30.4 | 29.57 | 34.27 | 41.74 | 41.74 | True | 近20日漲幅>25% | strong_accumulation | 0.56 | 0.56 | 3 | 3 | 14.93 | 16.99 | 0.0 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -2.86 | -0.45 | -10.37 | 16.36 | 11.65 | 18.55 | False |  | mild_accumulation | 0.28 | 0.63 | 1 | 1 | -3.36 | -2.1 | -14.53 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -7.21 | -8.65 | 20.41 | 8.92 | 18.2 | 22.07 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -6.65 | -5.24 | -15.31 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -12.38 | -23.33 | 47.75 | 91.4 | 53.33 | 104.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.12 | 0.76 | 3 | 1 | -11.42 | -11.62 | -37.56 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -4.25 | -3.91 | 3.97 | -4.7 | 7.28 | 7.28 | False |  | mild_accumulation | 0.7 | 0.01 | 1 | 1 | -4.07 | -2.41 | -12.8 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 3.0 | 98.95 | 97.49 | 132.19 | 109.53 | 137.44 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.62 | -1.38 | 1 | 1 | 22.29 | 21.12 | -8.7 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | -2.29 | 1.36 | -4.01 | -13.33 | 6.6 | 6.6 | False |  | mild_accumulation | 0.07 | -0.05 | 2 | 1 | -3.73 | -2.65 | -9.8 | 22 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -7.45 | 9.66 | 13.48 | 39.27 | 21.96 | 36.79 | False |  | distribution_warning | -0.38 | -1.45 | 1 | 0 | -4.34 | -2.5 | -17.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | -5.83 | 40.38 | 114.48 | 87.85 | 118.77 | 147.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -1.39 | 0 | 1 | 9.13 | 9.94 | -8.79 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -12.64 | -10.85 | -14.12 |  | 0.66 |  | False |  | distribution_warning | -0.05 | 0.0 | 2 | 0 | -14.37 | -12.62 | -26.57 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -0.62 | 5.99 | -12.5 | -15.29 | 7.97 | 7.97 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | -1.52 | -0.56 | -15.74 | 18 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -2.3 | 51.89 | 117.12 | 231.65 | 139.4 | 237.85 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 1.92 | 3 | 3 | 25.63 | 22.55 | -9.63 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -14.56 | -4.8 | 5.67 | 309.03 | 34.32 | 304.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.3 | -1.24 | 2 | 1 | -0.63 | -1.24 | -17.45 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -8.56 | 28.48 | 112.34 | 142.53 | 142.24 | 147.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.57 | -0.72 | 1 | 1 | 8.83 | 10.45 | -13.06 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -9.83 | -3.7 | 36.84 | 96.64 | 40.12 | 114.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.33 | -0.27 | 2 | 2 | -4.05 | -3.47 | -13.97 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -2.14 | 6.52 | 12.82 | 55.88 | 15.68 | 58.58 | False |  | strong_accumulation | 0.41 | 0.18 | 3 | 2 | 0.52 | 1.27 | -5.77 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -9.96 | -17.46 | 20.58 | 163.29 | 19.2 | 169.78 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.19 | -0.02 | 2 | 1 | -10.4 | -8.35 | -25.58 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | -0.58 | 2.69 | 41.8 | 46.95 | 47.74 | 50.49 | True | 近60日漲幅>40% | mild_accumulation | 4.16 | 4.43 | 1 | 2 | 8.18 | 6.32 | -9.72 |  | fail_already_priced_in |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -17.2 | -12.5 | 15.73 | 66.91 | 15.5 | 94.77 | True | 距120日低點反彈>80% | distribution_warning | -0.62 | -0.66 | 2 | 2 | -12.76 | -11.4 | -26.9 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 94.38123673778152 | 82.59499806151248 | -3.42 | 8.26 | 19.35 | 39.54 | 27.21 | 39.28 | False |  | distribution_warning | -0.46 | -0.5 | 0 | 0 | -2.92 | 0.67 | -16.21 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -6.44 | 6.45 | 71.92 | 231.31 | 71.38 | 256.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.52 | 1.68 | 3 | 3 | 5.26 | 4.34 | -9.84 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | -16.23 | -8.06 | 29.49 | 33.4 | 33.4 | 65.19 | False |  | strong_accumulation | 2.18 | 2.19 | 2 | 2 | -2.38 | -4.56 | -22.56 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 6.25 | 17.75 | 50.44 | 49.78 | 52.81 | 65.65 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.77 | 2.78 | 1 | 3 | 9.24 | 9.28 | -6.21 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 121.1993165447746 | 152.01807699959255 | 6.74 | 9.99 | 16.56 | 43.94 | 34.99 | 64.5 | False |  | distribution_warning | -5.7 | -7.4 | 0 | 0 | 5.5 | 7.38 | -12.24 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -10.3 | 30.55 | 103.14 | 132.9 | 127.64 | 139.05 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.8 | 0.86 | 1 | 1 | 10.41 | 11.73 | -10.3 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -6.64 | 16.34 | 36.49 | 44.5 | 37.12 | 48.49 | False |  | mild_accumulation | 0.91 | 0.0 | 2 | 1 | 1.95 | 2.81 | -9.08 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 4.45 | 15.45 | 52.22 | 35.42 | 57.17 | 63.75 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 4.55 | 4.6 | 3 | 2 | 9.3 | 8.83 | -5.41 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -2.11 | 5.48 | 4.49 | 9.2 | 10.71 | 20.52 | False |  | distribution_warning | -0.19 | 0.0 | 1 | 0 | -1.39 | -0.86 | -12.68 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -11.15 | -18.64 | 10.89 | 40.31 | 20.61 | 43.6 | False |  | distribution_warning | -3.87 | -2.31 | 1 | 0 | -11.84 | -9.73 | -28.2 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 0.71 | 8.95 | 30.74 | 76.5 | 26.52 | 81.03 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.58 | -0.87 | 0 | 0 | 3.0 | 1.8 | -15.95 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -11.34 | -14.98 | 17.92 | 20.55 | 22.65 | 46.82 | False |  | distribution_warning | -0.96 | -1.22 | 1 | 1 | -11.88 | -10.49 | -24.95 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -9.68 | -8.08 | 26.73 | 131.77 | 25.61 | 146.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.41 | 0.87 | 1 | 1 | -2.38 | -2.54 | -17.77 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -4.41 | -3.3 | 47.77 | 52.29 | 49.55 | 76.28 | True | 近60日漲幅>40% | distribution_warning | -3.02 | -2.08 | 0 | 1 | -2.17 | -0.27 | -8.29 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral | D_降級_TDCC轉弱 | 131.02269543289438 | 40.6738369557123 | -1.57 | 1.62 | -2.33 | -6.09 | 4.52 | 4.52 | False |  | distribution_warning | -0.09 | -0.32 | 1 | 0 | -1.46 | -0.88 | -3.93 | 15 | selected |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | -4.43 | -0.38 | -4.07 | -0.77 | 7.02 | 7.02 | False |  | mild_accumulation | 0.18 | 0.02 | 2 | 1 | -0.8 | -1.0 | -10.38 | 15 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 1.47 | 15.58 | 8.66 | -0.29 | 21.05 | 21.05 | False |  | strong_accumulation | 0.73 | 1.61 | 2 | 3 | 2.61 | 3.22 | -7.63 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -3.0 | -0.24 | -14.08 | -31.21 | 5.25 | 5.25 | False |  | mild_accumulation | -0.2 | 0.28 | 1 | 3 | -2.85 | -3.11 | -14.6 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -0.47 | 8.72 | -6.61 | -18.3 | 11.29 | 11.29 | False |  | distribution_warning | -0.94 | -1.17 | 1 | 1 | 0.71 | 0.84 | -6.61 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | -1.8 | 15.34 | 4.81 | -9.92 | 16.2 | 16.2 | False |  | distribution_warning | -1.12 | -1.16 | 1 | 0 | 0.19 | 0.85 | -12.1 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 1.68 | 7.38 | -18.04 | -19.71 | 18.73 | 18.73 | False |  | mild_accumulation | -0.15 | 0.07 | 1 | 1 | 2.71 | 2.06 | -18.55 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 0.94 | 2.74 | 18.9 | 7.21 | 27.89 | 27.89 | False |  | strong_accumulation | 0.68 | 0.84 | 2 | 2 | -1.32 | -0.54 | -8.49 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -10.01 | -15.8 | -33.93 | -36.54 | 4.32 | 4.32 | False |  | strong_accumulation | 0.12 | 0.04 | 2 | 2 | -13.89 | -11.37 | -34.04 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 0.46 | 11.56 | 2.33 | -0.45 | 12.13 | 12.13 | False |  | mild_accumulation | -0.03 | 0.06 | 1 | 1 | 1.7 | 2.22 | -4.35 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | 1.99 | -14.23 | -19.29 | -13.5 | 3.02 | 3.02 | False |  | distribution_warning | -1.57 | -0.84 | 1 | 2 | -1.43 | -3.98 | -22.64 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -3.27 | 5.89 | 51.96 | 110.46 | 63.05 | 111.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.6 | -1.34 | 0 | 0 | -2.96 | 1.22 | -15.89 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | -7.22 | 16.82 | 44.06 | 32.47 | 48.21 | 53.89 | True | 近60日漲幅>40% | mild_accumulation | 0.32 | 0.34 | 1 | 1 | 1.9 | 3.18 | -8.87 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | -2.31 | 31.78 | 38.88 | 69.43 | 47.88 | 72.89 | True | 近20日漲幅>25% | strong_accumulation | 0.44 | 0.42 | 2 | 2 | 4.83 | 6.54 | -4.97 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 2.96 | 41.33 | 33.6 | 60.58 | 44.42 | 62.16 | True | 近20日漲幅>25% | strong_accumulation | 0.71 | 0.81 | 3 | 3 | 9.49 | 10.93 | -1.64 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | -0.75 | 31.67 | 20.8 | 37.15 | 37.87 | 40.32 | True | 近20日漲幅>25% | strong_accumulation | 0.75 | 0.81 | 3 | 3 | 11.07 | 10.28 | -3.42 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 8.54 | 1.76 | 33.59 | 28.96 | 38.2 | 52.79 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 5.88 | 6.45 | -12.73 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | -4.23 | 4.63 | 31.2 | 35.12 | 31.59 | 44.81 | False |  | strong_accumulation | 0.54 | 0.24 | 2 | 2 | 0.38 | 0.58 | -7.99 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | -8.33 | 2.43 | 12.95 | 23.41 | 17.13 | 28.43 | False |  | mild_accumulation | 0.83 | 0.2 | 1 | 2 | -3.03 | -2.48 | -11.23 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -12.01 | -9.33 | 39.25 | 107.91 | 52.04 | 95.2 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.04 | 0.49 | 2 | 2 | -3.56 | -3.1 | -18.28 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -4.96 | -13.7 | 3.14 | 50.33 | 5.26 | 81.82 | True | 距120日低點反彈>80% | strong_accumulation | 0.12 | 0.22 | 2 | 2 | -7.71 | -6.58 | -23.59 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | -1.08 | 10.03 | 32.32 | 26.81 | 33.17 | 48.56 | False |  | strong_accumulation | 0.8 | 0.19 | 3 | 3 | 0.46 | 2.06 | -7.53 | 20 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -6.15 | -9.93 | 4.52 | 3.07 | 17.31 | 25.42 | False |  | mild_accumulation | 1.68 | -0.21 | 2 | 0 | -4.99 | -4.04 | -21.06 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -1.33 | -0.12 | 48.54 | 117.07 | 39.15 | 118.52 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.96 | 1 | 1 | 3.76 | 3.83 | -7.81 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -7.11 | -27.56 | -10.49 | 52.55 | 6.09 | 55.39 | False |  | distribution_warning | -2.02 | -2.52 | 0 | 0 | -13.49 | -12.1 | -32.14 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -13.41 | 4.48 | 21.82 | 10.52 | 26.42 | 26.42 | False |  | mild_accumulation | 2.13 | 1.43 | 1 | 1 | 0.35 | -1.03 | -17.54 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -14.92 | -14.44 | 72.55 | 47.19 | 76.25 | 81.98 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.21 | 0.15 | 2 | 2 | -11.96 | -9.35 | -24.79 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -5.71 | -6.14 | 0.8 | 97.17 | 1.79 | 120.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | 0.0 | 3 | 0 | -9.9 | -7.27 | -25.27 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -12.56 | -30.52 | 58.77 | 113.44 | 63.06 | 109.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.33 | -1.23 | 0 | 0 | -12.74 | -10.26 | -31.95 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -3.85 | -2.64 | 43.6 | 220.5 | 38.71 | 285.07 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.37 | -0.58 | 2 | 1 | -7.26 | -4.26 | -23.74 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -6.78 | -15.25 | 123.14 | 48.76 | 126.76 | 137.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -7.51 | -5.61 | -22.89 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | -9.18 | -15.24 | 21.36 | 26.54 | 31.53 | 40.38 | False |  | distribution_warning | -1.91 | -1.78 | 0 | 1 | -8.15 | -5.78 | -21.24 | 11 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -6.2 | -9.26 | 11.74 | 9.9 | 12.12 | 24.72 | False |  | distribution_warning | -0.13 | -0.22 | 1 | 1 | -4.91 | -3.97 | -15.05 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -6.86 | -6.12 | 9.63 | 28.83 | 12.78 | 28.83 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.49 | -4.71 | -24.41 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -7.05 | -5.35 | 76.1 | 115.61 | 79.67 | 113.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.11 | 0.49 | 1 | 2 | -3.28 | -4.73 | -25.71 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -10.73 | -16.43 | 46.79 | 48.11 | 48.56 | 61.51 | True | 近60日漲幅>40% | mild_accumulation | -0.95 | 1.71 | 2 | 2 | -17.91 | -11.06 | -31.09 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -12.84 | -8.57 | -7.44 | 19.53 | 0.45 | 32.86 | False |  | distribution_warning | -2.43 | -0.16 | 2 | 0 | -12.09 | -10.19 | -25.83 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -7.11 | -11.06 | 13.71 | 80.8 | 15.34 | 81.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.79 | -1.09 | 0 | 0 | -5.34 | -4.83 | -18.04 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -14.65 | -4.32 | -14.65 | 37.19 | 8.5 | 44.35 | False |  | strong_accumulation | 6.24 | 7.1 | 3 | 3 | -4.17 | -4.7 | -17.41 | 19 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | -4.11 | 3.74 | -7.31 | -23.89 | 4.67 | 4.67 | False |  | mild_accumulation | 0.77 | -0.13 | 3 | 1 | -3.28 | -2.57 | -15.38 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -17.97 | -2.78 | 32.58 | 59.33 | 31.74 | 70.18 | False |  | distribution_warning | -3.49 | -4.13 | 1 | 1 | -11.26 | -8.24 | -21.93 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -8.38 | -14.49 | 69.07 | 65.58 | 73.96 | 80.83 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -9.23 | -9.01 | 0 | 0 | -11.24 | -5.71 | -24.55 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 281.10296953335904 | 153.94170544805627 | -3.74 | -2.9 | 1.52 | 20.5 | 12.42 | 27.38 | False |  | strong_accumulation | 1.11 | 2.31 | 2 | 2 | -1.73 | -2.19 | -15.4 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 8.55 | 2.17 | -12.15 | -21.67 | 10.59 | 10.59 | False |  | mild_accumulation | 0.27 | 0.01 | 1 | 1 | 4.5 | 4.03 | -16.07 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 112.585794273422 | 77.27049729091536 | -7.21 | -4.35 | 17.59 | 53.49 | 25.12 | 54.84 | False |  | distribution_warning | -4.96 | -9.67 | 1 | 1 | -5.72 | -4.16 | -18.27 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -6.4 | 12.5 | 24.03 | 33.97 | 26.26 | 35.0 | False |  | distribution_warning | -0.05 | 0.0 | 1 | 0 | -1.54 | -0.18 | -13.12 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | -6.07 | -10.73 | -5.15 | -2.52 | 1.57 | 3.34 | False |  | distribution_warning | -1.75 | -2.16 | 1 | 0 | -8.78 | -6.76 | -18.1 | 13 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -3.18 | -6.46 | 7.29 | 19.22 | 24.93 | 39.24 | False |  | mild_accumulation | 0.56 | -0.04 | 1 | 0 | -8.69 | -4.01 | -22.58 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 1.94 | 6.54 | 2.4 | 2.4 | 8.92 | 14.19 | False |  | mild_accumulation | 0.49 | 0.0 | 3 | 0 | 2.17 | 1.93 | -3.39 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -13.41 | -12.1 | -13.18 | -17.01 | 0.79 | 0.79 | False |  | distribution_warning | -0.58 | -0.43 | 2 | 2 | -13.83 | -11.42 | -23.84 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -1.83 | 1.18 | -15.42 | -24.25 | 4.65 | 4.65 | False |  | distribution_warning | -0.17 | -0.01 | 0 | 0 | -2.84 | -2.67 | -15.91 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.36 | 0.0 | -3.11 | -3.78 | 2.56 | 2.56 | False |  | strong_accumulation | 0.57 | 0.1 | 3 | 3 | 0.09 | 0.09 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -0.51 | 5.94 | -2.48 | -8.93 | 7.98 | 7.98 | False |  | mild_accumulation | 1.08 | 0.7 | 1 | 1 | -0.83 | -0.65 | -10.29 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 17.9 | 21.81 | 72.38 | 74.27 | 69.63 | 100.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.48 | 2 | 2 | 18.19 | 17.31 | -1.04 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -5.63 | -12.42 | -19.28 | 24.07 | 3.08 | 32.67 | False |  | mild_accumulation | 0.06 | 0.05 | 1 | 2 | -8.44 | -7.43 | -28.34 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -11.71 | 5.68 | 135.24 | 119.0 | 132.11 | 146.03 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.34 | 1 | 1 | 0.59 | 1.46 | -15.45 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -1.31 | 6.84 | -4.73 | -15.64 | 9.03 | 9.03 | False |  | mild_accumulation | 0.11 | -0.67 | 2 | 2 | -1.44 | -1.18 | -12.38 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -5.34 | 4.11 | 76.16 | 94.52 | 76.16 | 111.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.14 | 0.02 | 1 | 1 | 0.43 | 2.07 | -10.89 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -18.52 | -3.06 | 45.32 | 16.64 | 44.53 | 64.32 | True | 近60日漲幅>40% | distribution_warning | -4.67 | -3.73 | 1 | 1 | -8.38 | -7.15 | -24.21 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -9.26 | -18.33 | -2.73 | 7.1 | 14.29 | 21.74 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -14.44 | -14.16 | -44.08 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -11.24 | -23.81 | 64.32 | 119.1 | 76.74 | 123.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.12 | -3.04 | 1 | 1 | -12.7 | -9.24 | -31.76 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -12.44 | -28.84 | 7.95 | 89.05 | 11.11 | 118.89 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.2 | 0.0 | 2 | 0 | -12.42 | -13.05 | -35.37 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -23.26 | -13.28 | -26.1 | 16.36 | 1.59 | 33.33 | False |  | mild_accumulation | -1.99 | 2.47 | 0 | 3 | -16.63 | -15.35 | -34.96 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 15.98 | 36.56 | 95.99 | 168.78 | 119.72 | 171.95 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.04 | 2 | 2 | 24.47 | 24.01 | 0.0 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -15.27 | -7.5 | 2.62 | 178.78 | 6.8 | 190.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.83 | 0.65 | 0 | 2 | -9.94 | -10.97 | -30.24 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -12.11 | -17.65 | 105.02 | 121.47 | 106.32 | 150.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 1.84 | 1 | 2 | -2.35 | -2.72 | -24.9 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -7.64 | 0.77 | -8.18 | -30.32 | 5.36 | 5.36 | False |  | mild_accumulation | -0.21 | 0.23 | 1 | 1 | -4.12 | -3.23 | -13.82 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -3.79 | -7.68 | 0.22 | 3.86 | 6.53 | 6.53 | False |  | mild_accumulation | 1.08 | -0.03 | 3 | 1 | -5.19 | -4.3 | -11.61 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | -1.25 | 1.02 | -3.53 | -19.25 | 3.39 | 3.39 | False |  | distribution_warning | -0.05 | -0.02 | 0 | 0 | -1.11 | -0.89 | -9.06 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 9.2 | 22.31 | 36.6 | 44.28 | 36.36 | 45.34 | False |  | strong_accumulation | 1.74 | 2.63 | 3 | 3 | 14.4 | 12.37 | -4.68 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -3.31 | -11.05 | 36.98 | 96.02 | 54.71 | 100.76 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.04 | 2 | 2 | 3.6 | 4.55 | -16.51 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -9.14 | -8.21 | -9.6 | 9.82 | 1.32 | 7.4 | False |  | distribution_warning | -1.33 | 0.0 | 0 | 0 | -8.84 | -7.38 | -13.67 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | -2.24 | 44.95 | 235.38 | 283.13 | 227.82 | 317.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.18 | -3.65 | 0 | 1 | 20.24 | 17.31 | -16.79 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -15.59 | -27.39 | 144.83 | 433.39 | 148.64 | 441.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.05 | 0.0 | 2 | 0 | -6.72 | -8.76 | -34.8 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -5.24 | -17.44 | 0.33 | -22.74 | 2.73 | 4.39 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -8.45 | -8.06 | -25.6 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 4.03 | 45.56 | 29.39 | 7.12 | 49.79 | 49.79 | True | 近20日漲幅>25% | distribution_warning | -0.15 | -0.78 | 1 | 0 | 12.58 | 12.07 | -12.38 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -16.17 | 42.37 | 374.04 | 1263.64 | 387.8 | 1432.85 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.48 | 0.23 | 2 | 2 | 8.42 | 11.53 | -17.49 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 27.34 | 41.6 | 60.18 | 38.28 | 64.65 | 66.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.03 | 0.02 | 2 | 2 | 30.58 | 27.02 | -0.84 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -10.26 | -5.08 | -15.32 | 37.92 | 2.07 | 49.08 | False |  | mild_accumulation | 1.47 | 0.0 | 2 | 0 | -9.6 | -8.21 | -25.7 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -7.14 | -19.19 | -14.08 | -5.68 | 6.03 | 8.33 | False |  | mild_accumulation | -1.27 | 1.37 | 0 | 1 | -9.23 | -8.35 | -27.25 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -13.48 | -16.45 | 13.58 | -2.24 | 16.62 | 19.14 | False |  | mild_accumulation | 1.16 | 0.49 | 1 | 1 | -13.42 | -12.72 | -26.07 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -9.83 | -13.6 | 42.91 | 140.12 | 45.42 | 147.31 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.12 | 0.0 | 1 | 0 | -6.07 | -6.89 | -32.74 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | -7.52 | -22.58 | 50.12 | 86.44 | 58.1 | 108.99 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | -0.14 | 1 | 1 | -9.37 | -8.37 | -24.45 |  | fail_low_response_condition |