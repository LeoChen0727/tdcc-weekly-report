# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-09 19:37:49 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 622355 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 297 |
| low_response_pass | 93 |
| already_priced_in_excluded | 40 |
| overheat_pass | 53 |
| score_pass | 53 |
| theme_priority_pass | 38 |
| final_rows | 38 |

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
| fail_low_response_condition | 204 |
| fail_already_priced_in | 40 |
| fail_defensive_or_traditional_excluded | 15 |
| missing_or_insufficient_price_metrics | 3 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 152.96178992534956 | 138.94580810199872 | -1.9 | -5.91 | -13.03 | -29.11 | 3.5 | 3.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | -2.36 | -1.81 | -13.75 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -0.9 | 1.38 | -5.15 | -6.75 | 3.27 | 3.27 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | 0.34 | -0.13 | -7.14 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 6.08 | 4.07 | 4.63 | -4.24 | 13.27 | 13.27 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 5.03 | 4.71 | -4.71 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | -3.15 | -6.1 | -7.05 | 11.69 | 14.94 | 37.13 | False |  | distribution_warning | -0.77 | -1.61 | 0 | 0 | -3.25 | -2.29 | -17.56 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -2.68 | -1.14 | -7.64 | 5.84 | 10.13 | 10.13 | False |  | mild_accumulation | -0.2 | 0.64 | 1 | 1 | -3.95 | -3.37 | -15.7 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 2.79 | -3.66 | 18.11 | 15.16 | 22.43 | 27.07 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -0.79 | -0.58 | -11.84 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -11.78 | -6.1 | 19.91 | 86.16 | 35.12 | 105.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | -4.24 | 3 | 0 | -6.51 | -8.08 | -37.33 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | D_降級_TDCC轉弱 | 153.16268341919277 | -7.777041541987246 | -4.79 | -10.6 | 0.13 | -7.29 | 2.37 | 2.65 | False |  | distribution_warning | -0.34 | -0.57 | 1 | 1 | -6.11 | -5.71 | -16.56 | 12 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | -16.67 | 31.68 | 77.1 | 94.04 | 91.24 | 96.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | -7.31 | -1.62 | -31.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | 1.52 | -4.44 | 0.84 | -12.75 | 7.31 | 7.31 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -2.52 | -1.26 | -9.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -8.33 | -16.26 | -0.82 | 3.42 | 13.08 | 16.91 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -10.52 | -7.87 | -23.66 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 4.7 | 29.51 | 120.29 | 145.17 | 136.05 | 186.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 11.76 | 14.33 | -3.62 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | 0.0 | -19.67 | -18.78 |  | 2.44 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -9.94 | -8.48 | -28.99 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 5.26 | 3.82 | -4.09 | -7.86 | 15.25 | 15.25 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 4.16 | 4.2 | -5.56 | 22 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -4.26 | 58.94 | 109.91 | 190.32 | 138.41 | 206.38 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 3.26 | 6.66 | -15.59 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -1.37 | 6.3 | 19.09 | 134.48 | 16.19 | 144.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -7.63 | -5.55 | -25.26 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -3.81 | 18.46 | 105.95 | 73.04 | 110.12 | 110.62 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -8.71 | -3.39 | -24.41 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -10.18 | 4.44 | 23.19 | 104.98 | 22.89 | 126.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | -0.44 | -0.98 | -12.57 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -4.84 | -4.01 | 5.36 | 37.85 | 11.88 | 39.15 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | -3.8 | -2.74 | -9.97 | 25 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -17.65 | -17.65 | -11.22 | 90.78 | 1.68 | 96.12 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -16.08 | -15.93 | -34.88 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.80451818624007 | 107.89432287557707 | -7.74 | 19.06 | 17.99 | 33.6 | 28.12 | 43.7 | False |  | mild_accumulation | 2.17 | 2.99 | 1 | 2 | -1.02 | -1.4 | -13.8 | 18 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -12.96 | -24.3 | -11.16 | 61.41 | 0.94 | 81.28 | True | 距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -14.34 | -13.55 | -31.96 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 1.22 | -1.84 | 13.53 | 33.16 | 29.46 | 39.11 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 0.51 | 1.16 | -14.73 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -6.37 | 7.19 | 37.53 | 228.88 | 38.25 | 242.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | -2.19 | -1.01 | -15.28 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | 2.09 | 14.04 | 10.42 | 41.12 | 17.71 | 70.79 | False |  | strong_accumulation | 2.08 | 2.37 | 2 | 2 | -0.04 | 0.1 | -19.93 | 21 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 85.01370770897306 | 83.4020606995027 | -12.27 | 5.65 | 18.54 | 23.73 | 28.57 | 47.99 | False |  | strong_accumulation | 1.5 | 0.92 | 2 | 2 | -6.12 | -3.92 | -16.21 | 19 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 121.1993165447746 | 152.01807699959255 | -7.78 | 7.39 | 11.76 | 37.25 | 36.77 | 45.28 | False |  | distribution_warning | -3.53 | -3.16 | 1 | 1 | 1.63 | 1.89 | -16.21 | 15 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 7.0 | 30.78 | 110.39 | 82.22 | 118.84 | 119.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | 1.78 | 5.9 | -13.76 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 0.98 | 7.13 | 35.83 | 50.61 | 37.5 | 53.42 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 1.05 | 3.92 | -5.23 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | -4.98 | 20.81 | 33.5 | 27.14 | 41.02 | 59.56 | False |  | mild_accumulation | 1.29 | -0.26 | 2 | 2 | -0.55 | 1.07 | -13.87 | 19 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.36 | 0.89 | -2.76 | 13.25 | 11.9 | 21.81 | False |  | distribution_warning | -0.1 | 0.0 | 2 | 0 | -1.01 | -0.18 | -11.74 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -1.74 | -13.48 | 1.2 | 6.96 | 4.97 | 32.38 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -10.36 | -9.86 | -33.81 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 71.83340834565679 | 63.183650278464505 | -6.03 | 10.47 | -2.0 | 45.96 | 18.07 | 68.55 | False |  | distribution_warning | -0.06 | -1.16 | 1 | 0 | -4.76 | -4.12 | -18.33 | 12 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 26.59 | 16.08 | 34.79 | 53.25 | 38.12 | 86.65 | True | 距120日低點反彈>80% | distribution_warning | -0.29 | 0.0 | 2 | 1 | 16.31 | 15.03 | -4.58 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -15.5 | 2.96 | -2.46 | 118.9 | 14.64 | 141.21 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | -6.12 | -6.75 | -19.65 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 4.79 | 9.15 | 23.67 | 61.54 | 51.52 | 85.84 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.39 | -1.69 | 0 | 1 | 2.31 | 3.76 | -5.58 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 2.06 | -1.11 | 0.34 | -2.2 | 5.83 | 5.83 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.06 | 0.38 | -2.73 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | 1.83 | 8.59 | 1.46 | 3.73 | 14.88 | 14.88 | False |  | strong_accumulation | 0.69 | 0.7 | 3 | 2 | 3.71 | 3.07 | -9.15 | 16 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 1.45 | -1.4 | 12.5 | 4.31 | 23.16 | 23.16 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 1.28 | 2.93 | -6.02 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -2.39 | 0.45 | -2.6 | -25.29 | 12.25 | 12.25 | False |  | strong_accumulation | 0.15 | 0.52 | 2 | 3 | 1.87 | 1.8 | -3.85 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral | D_降級_TDCC轉弱 | 367.4305802571221 | 58.17838010197999 | -7.78 | -9.49 | -11.74 | -22.88 | 3.71 | 3.71 | False |  | distribution_warning | -1.6 | -1.07 | 0 | 1 | -7.27 | -5.48 | -12.92 | 15 | selected |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 3.7 | 0.9 | 7.69 | -3.86 | 19.4 | 19.4 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | -0.07 | 2.55 | -9.68 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 0.51 | -0.13 | -14.47 | -18.72 | 18.73 | 18.73 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 0.49 | 0.97 | -15.12 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2114.205326762877 | 1780.7414522786555 | 1.16 | -4.07 | 27.3 | 9.82 | 29.38 | 29.38 | False |  | distribution_warning | -0.74 | -0.81 | 1 | 1 | -0.58 | 0.31 | -7.43 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | 1.31 | -20.65 | -29.71 | -38.51 | 4.72 | 4.72 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -6.31 | -5.76 | -29.84 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 1.78 | 2.69 | 7.01 | 5.53 | 16.72 | 16.72 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 2.81 | 3.61 | -2.97 | 19 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 9203.558823529413 | 30000.69173757892 | -0.98 | -4.27 | -21.09 | -12.93 | 1.51 | 1.51 | False |  | distribution_warning | -1.46 | -1.04 | 1 | 1 | -1.73 | -3.15 | -23.77 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 1.31 | -1.75 | 52.73 | 89.12 | 53.42 | 90.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | -0.95 | 0.31 | -15.72 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 4.18 | 1.63 | 42.78 | 31.05 | 42.78 | 49.1 | True | 近60日漲幅>40% | distribution_warning | -0.1 | -0.13 | 0 | 0 | -3.38 | 0.41 | -11.7 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 7.71 | 6.56 | 44.47 | 70.25 | 49.88 | 72.21 | True | 近60日漲幅>40%；近120日漲幅>70% | distribution_warning | -0.33 | -0.55 | 1 | 1 | 2.18 | 5.18 | -3.69 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 11.67 | 27.51 | 51.96 | 76.32 | 61.27 | 77.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.69 | 0.78 | 3 | 3 | 12.33 | 14.33 | -0.81 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 2.84 | 23.41 | -4.06 | 36.78 | 37.12 | 59.24 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 5.39 | 4.9 | -8.43 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | 0.92 | 3.12 | 19.53 | 43.07 | 26.87 | 44.01 | False |  | strong_accumulation | 0.61 | 0.58 | 3 | 3 | -0.9 | 0.7 | -7.29 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 12.45 | 16.73 | 30.64 | 32.33 | 38.91 | 55.84 | False |  | strong_accumulation | 1.66 | 2.35 | 2 | 3 | 11.53 | 11.13 | -5.83 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 8.72 | 17.33 | 57.48 | 62.33 | 57.48 | 79.55 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.2 | 1.06 | 2 | 2 | 4.73 | 5.07 | -13.35 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -14.23 | -0.42 | -5.62 | 73.43 | 5.86 | 85.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | -4.39 | -5.92 | -21.93 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 92.4008479108611 | 7.500180953989433 | 2.3 | 4.71 | 26.06 | 31.27 | 34.64 | 60.65 | False |  | distribution_warning | -1.06 | -0.7 | 2 | 2 | 4.58 | 5.65 | -7.0 | 12 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -10.61 | -13.33 | -7.14 | -20.27 | 4.55 | 11.78 | False |  | mild_accumulation | 1.34 | -0.37 | 2 | 0 | -12.19 | -11.0 | -29.65 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -9.07 | -0.66 | 22.68 | 82.08 | 27.03 | 89.9 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | -3.93 | -4.37 | -14.84 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | -2.76 | -11.69 | -2.53 | 46.88 | 7.36 | 46.88 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -3.38 | -6.49 | -31.33 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -6.54 | 11.37 | 17.56 | 0.0 | 18.88 | 24.76 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | -5.14 | -3.24 | -18.62 | 18 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -6.69 | -18.14 | 52.48 | 43.71 | 64.84 | 77.25 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -10.64 | -7.92 | -26.74 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 3.43 | -6.49 | -14.09 | 108.55 | 6.73 | 122.46 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -1.88 | -2.39 | -24.43 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -6.27 | -17.51 | 52.21 | 66.18 | 49.57 | 72.0 | True | 近60日漲幅>40% | distribution_warning | -2.8 | -1.3 | 0 | 0 | -7.77 | -9.01 | -35.34 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -2.88 | -9.67 | 15.67 | 234.05 | 26.63 | 285.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | -4.93 | -5.53 | -23.65 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -9.14 | -9.88 | 14.81 | 55.31 | 11.51 | 118.93 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -10.04 | -8.69 | -28.77 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | -5.2 | -6.59 | 7.59 | 4.94 | 25.62 | 34.07 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -7.27 | -7.22 | -24.78 | 11 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 1.68 | 4.01 | 14.51 | 21.0 | 21.0 | 35.96 | False |  | strong_accumulation | 0.5 | 0.46 | 2 | 2 | 2.93 | 1.88 | -7.4 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -1.63 | 1.12 | 8.38 | 25.69 | 10.03 | 29.29 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.63 | -1.59 | -22.48 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -18.57 | 7.83 | 21.23 | 78.23 | 20.39 | 102.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -7.94 | -7.13 | -27.06 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -0.6 | -19.27 | 37.92 | 42.67 | 37.92 | 63.32 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -6.68 | -4.97 | -30.32 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -9.52 | -15.04 | -16.06 | 22.37 | 0.97 | 23.96 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -12.31 | -11.11 | -30.79 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 82.90674676519687 | 39.84386199206386 | -1.39 | -2.29 | 5.97 | 67.45 | 14.52 | 71.77 | False |  | distribution_warning | -0.54 | -1.12 | 1 | 0 | -1.39 | -2.25 | -16.47 | 14 | selected |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.11391792521879 | 34.318355180717255 | -13.96 | -7.08 | -20.73 | 4.5 | 3.42 | 17.05 | False |  | strong_accumulation | 4.42 | 4.81 | 2 | 2 | -11.48 | -10.41 | -24.5 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 1.44 | -0.84 | -2.22 | -13.69 | 5.06 | 5.06 | False |  | strong_accumulation | 0.23 | 0.11 | 2 | 2 | 0.99 | 0.72 | -4.34 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | -0.34 | -6.3 | -10.63 | -20.11 | 4.13 | 4.13 | False |  | distribution_warning | -0.24 | -0.56 | 2 | 0 | -2.99 | -1.79 | -15.82 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -11.21 | -20.8 | 7.03 | 38.85 | 20.29 | 60.45 | False |  | distribution_warning | -3.16 | -5.47 | 1 | 0 | -14.23 | -11.63 | -26.39 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -6.09 | -3.14 | 57.66 | 74.19 | 78.81 | 103.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 2.63 | 1.63 | -15.29 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 281.10296953335904 | 153.94170544805627 | -4.7 | 6.15 | 1.17 | 18.97 | 15.77 | 21.91 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | -1.19 | -0.67 | -12.88 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -8.02 | -4.97 | -21.46 | -30.36 | 1.18 | 1.18 | False |  | distribution_warning | -0.35 | 0.0 | 0 | 0 | -4.18 | -4.17 | -21.82 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -8.98 | -13.38 | 7.37 | 15.35 | 5.43 | 36.66 | False |  | mild_accumulation | -1.13 | 0.33 | 1 | 2 | -12.09 | -11.13 | -27.86 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 3.83 | 2.98 | 11.76 | 27.52 | 31.03 | 46.15 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 3.05 | 5.29 | -5.94 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 5.09 | 0.71 | 1.56 | 5.88 | 11.02 | 12.95 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | 2.87 | 2.44 | -10.48 | 15 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -0.2 | -1.3 | 26.25 | 23.87 | 35.07 | 50.53 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | 5.05 | 4.4 | -16.3 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral | B_可觀察 | 88.65151498619764 | -2.528158661804875 | -0.14 | 1.92 | 5.67 | 6.99 | 9.71 | 15.03 | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | 0.5 | 1.38 | -2.68 | 18 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | 1.41 | -21.29 | -6.37 | -11.25 | 2.37 | 2.37 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -6.88 | -5.18 | -22.88 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 1.86 | -2.02 | -12.25 | -19.52 | 6.85 | 6.85 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.19 | -0.02 | -12.95 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | -3.21 | -3.9 | -6.87 | -4.91 | 0.37 | 0.37 | False |  | strong_accumulation | 0.31 | 0.42 | 3 | 3 | -3.35 | -3.24 | -7.19 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 0.64 | -5.15 | 1.93 | -6.38 | 8.94 | 8.94 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | -1.37 | 0.02 | -9.49 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -6.82 | 18.72 | 16.51 | 51.12 | 33.59 | 83.25 | True | 距120日低點反彈>80% | strong_accumulation | 1.8 | 1.98 | 2 | 2 | 1.34 | 1.76 | -11.35 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | 1.51 | -8.5 | -16.72 | 21.72 | 3.46 | 26.89 | False |  | strong_accumulation | 0.68 | 0.05 | 2 | 2 | -3.17 | -3.59 | -19.22 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -0.37 | 7.17 | 71.34 | 120.13 | 83.24 | 137.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.49 | 0.47 | 0 | 2 | -3.84 | -0.64 | -18.48 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | -0.11 | -2.79 | 1.0 | -14.53 | 9.03 | 9.03 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -2.19 | -0.81 | -12.38 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -6.63 | 9.8 | 39.16 | 101.47 | 51.45 | 118.29 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | -0.79 | 1.13 | -8.19 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 70.65666417439758 | 55.92683953560652 | 0.62 | -0.25 | 22.61 | 35.8 | 37.18 | 67.63 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -4.85 | -1.83 | -22.68 | 12 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 6.88 | -1.06 | 32.01 | 35.47 | 35.86 | 44.72 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 3.74 | 2.13 | -33.52 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -8.24 | -19.97 | 51.56 | 75.71 | 61.92 | 93.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.95 | 0.74 | 1 | 2 | -11.76 | -11.1 | -37.49 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -2.6 | -9.86 | -24.85 | 103.8 | 5.63 | 116.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -5.47 | -8.16 | -36.22 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -9.48 | -21.69 | -37.55 | 4.59 | 2.78 | 23.33 | False |  | mild_accumulation | -2.38 | 0.82 | 0 | 2 | -15.39 | -14.26 | -39.84 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | -7.89 | 30.32 | 95.29 | 148.55 | 122.32 | 151.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 6.59 | 5.57 | -18.15 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -16.6 | -4.43 | -28.07 | 123.78 | 4.3 | 128.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -13.43 | -11.24 | -32.42 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -4.06 | 3.13 | 35.19 | 95.34 | 30.41 | 135.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -5.65 | -5.56 | -29.35 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 0.62 | 3.16 | 0.99 | -20.0 | 9.38 | 9.38 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | -0.06 | 0.12 | -10.53 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 2.88 | 6.04 | -1.53 | -24.25 | 20.17 | 20.17 | False |  | mild_accumulation | -0.03 | 0.59 | 1 | 2 | 1.97 | 1.68 | -9.98 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 0.44 | -8.23 | 0.66 | -5.77 | 6.53 | 6.53 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | -2.55 | -2.25 | -11.61 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.13 | 0.25 | -2.44 | -19.6 | 4.3 | 4.3 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | -0.27 | -0.05 | -8.26 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | -7.57 | 12.03 | 6.47 | 19.39 | 20.0 | 27.57 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | -3.92 | -2.08 | -15.11 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 58.86220189113607 | 31.41858931023004 | -4.82 | 10.4 | 38.33 | 42.77 | 37.79 | 48.12 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -4.8 | -4.16 | -24.76 | 18 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | 3.53 | -6.86 | -5.43 | -3.97 | 5.09 | 11.4 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -1.49 | -1.24 | -10.45 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 0.0 | 85.71 | 242.11 | 296.34 | 286.9 | 398.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 16.0 | 18.42 | -7.14 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -11.92 | -7.89 | 64.51 | 344.44 | 65.44 | 377.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.0 | 3 | 0 | -10.82 | -12.06 | -40.41 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 1.75 | -7.66 | -7.2 | -28.62 | 3.11 | 7.16 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -0.67 | -2.49 | -23.62 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 15.6 | 28.88 | 44.6 | 22.78 | 72.2 | 72.2 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 16.15 | 16.8 | -7.37 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 6.21 | 53.62 | 314.06 | 1344.14 | 400.95 | 1360.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 18.66 | 21.19 | -2.93 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | -1.92 | 21.34 | 12.04 | 2.68 | 28.99 | 44.81 | False |  | distribution_warning | -0.22 | -0.19 | 1 | 1 | 3.66 | 3.9 | -14.01 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -4.31 | -7.31 | -12.99 | 47.61 | 4.87 | 53.18 | False |  | distribution_warning | -0.79 | 0.0 | 1 | 0 | -4.21 | -3.49 | -18.48 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -1.01 | -12.72 | -14.74 | -7.52 | 4.61 | 6.88 | False |  | mild_accumulation | 0.4 | -2.35 | 1 | 0 | -4.47 | -5.05 | -28.22 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -7.97 | -22.75 | -2.88 | -9.01 | 0.87 | 16.26 | False |  | mild_accumulation | 0.02 | 0.5 | 1 | 1 | -10.79 | -9.57 | -27.86 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -3.28 | -3.28 | 7.83 | 132.81 | 9.26 | 144.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | 0.0 | 1 | 0 | -3.81 | -4.33 | -32.74 |  | fail_low_response_condition |