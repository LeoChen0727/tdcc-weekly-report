# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-26 19:38:40 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 602714 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 377 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 708 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 92 |
| already_priced_in_excluded | 45 |
| overheat_pass | 47 |
| score_pass | 47 |
| theme_priority_pass | 31 |
| final_rows | 31 |

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
| fail_already_priced_in | 45 |
| fail_defensive_or_traditional_excluded | 16 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 152.96178992534956 | 138.94580810199872 | -9.01 | 0.0 | -16.18 | -36.08 | 1.0 | 1.0 | False |  | distribution_warning | -0.79 | -0.14 | 1 | 1 | -4.65 | -4.94 | -18.88 | 14 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -3.14 | -2.7 | -5.26 | -9.62 | 0.93 | 0.93 | False |  | mild_accumulation | -0.22 | 0.46 | 1 | 1 | -3.53 | -2.87 | -9.24 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -3.78 | -3.78 | -4.81 | -10.1 | 5.01 | 5.01 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -4.0 | -3.15 | -11.0 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -5.02 | -1.81 | -4.4 | 13.87 | 10.13 | 16.94 | False |  | mild_accumulation | 0.22 | 0.0 | 1 | 1 | -4.63 | -3.67 | -15.7 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -5.68 | -7.87 | 21.84 | 11.04 | 23.1 | 23.1 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -6.49 | -5.04 | -14.59 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -5.1 | -22.5 | 62.78 | 93.48 | 61.27 | 106.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.33 | 1.4 | 2 | 1 | -12.39 | -11.87 | -36.88 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | B_可觀察 | 153.16268341919277 | -7.777041541987246 | -5.49 | -6.16 | 3.12 | -9.28 | 4.76 | 4.76 | False |  | strong_accumulation | 1.4 | 0.62 | 2 | 2 | -6.63 | -5.06 | -14.84 | 18 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | -3.64 | 95.26 | 94.65 | 125.94 | 105.65 | 133.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.03 | 1.32 | 2 | 2 | 27.62 | 23.55 | -10.39 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | -5.56 | 3.73 | 0.66 | -13.07 | 9.09 | 9.09 | False |  | strong_accumulation | 0.36 | 0.45 | 2 | 2 | -1.17 | -0.54 | -7.69 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -8.83 | 8.4 | 14.16 | 39.91 | 20.56 | 40.07 | False |  | distribution_warning | -0.07 | -1.49 | 1 | 0 | -4.53 | -3.91 | -18.61 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 5.59 | 38.01 | 108.97 | 89.43 | 120.5 | 143.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.5 | 1.14 | 0 | 2 | 10.94 | 10.44 | -9.16 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -6.0 | -3.52 | -3.52 |  | 1.23 |  | False |  | mild_accumulation | 0.82 | -0.02 | 3 | 0 | -7.8 | -6.51 | -20.53 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -6.46 | 3.66 | -17.48 | -17.59 | 5.59 | 5.59 | False |  | strong_accumulation | 0.26 | 0.1 | 2 | 2 | -3.18 | -2.93 | -17.59 | 19 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 14.71 | 47.48 | 116.67 | 217.65 | 132.45 | 228.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.61 | 2 | 2 | 27.83 | 24.89 | -10.34 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | 0.62 | -2.4 | 25.97 | 314.54 | 37.71 | 327.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.0 | -0.75 | 2 | 1 | 1.47 | 1.2 | -15.36 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | 3.77 | 30.7 | 124.95 | 169.93 | 146.42 | 173.15 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.43 | 0.22 | 1 | 1 | 13.96 | 15.53 | -11.56 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -4.61 | -2.06 | 49.69 | 95.88 | 48.75 | 118.35 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | -0.35 | 2 | 1 | -2.69 | -2.32 | -12.5 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 0.43 | 8.03 | 19.9 | 61.11 | 19.9 | 61.67 | False |  | mild_accumulation | 0.07 | -0.03 | 2 | 2 | 2.78 | 3.3 | -4.43 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -8.74 | -19.25 | 32.57 | 157.92 | 30.87 | 163.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.03 | 0.56 | 1 | 1 | -13.78 | -11.41 | -27.19 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 16.27 | 2.54 | 48.16 | 45.19 | 47.53 | 50.27 | True | 近60日漲幅>40% | distribution_warning | -0.53 | -0.85 | 1 | 1 | 8.97 | 8.5 | -7.55 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -13.14 | -9.85 | 31.49 | 70.73 | 29.63 | 100.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.15 | 0.35 | 2 | 2 | -10.94 | -10.15 | -24.68 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | -3.21 | 6.78 | 27.24 | 37.64 | 27.46 | 38.96 | False |  | mild_accumulation | 0.54 | 0.68 | 1 | 1 | -3.54 | -0.6 | -17.35 | 18 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 1.06 | 2.64 | 88.69 | 220.43 | 84.39 | 243.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.4 | -0.15 | 2 | 2 | 2.33 | 1.72 | -13.07 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 88.0613471994038 | 34.31162647538102 | -5.72 | -7.8 | 37.94 | 33.02 | 42.66 | 65.65 | False |  | distribution_warning | -0.54 | -0.2 | 1 | 1 | -2.59 | -4.57 | -22.34 | 14 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 4.69 | 16.02 | 61.64 | 42.4 | 61.64 | 63.22 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.43 | -0.23 | 1 | 2 | 9.45 | 9.64 | -6.29 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | -4.56 | 0.0 | 12.18 | 26.56 | 22.74 | 49.57 | False |  | mild_accumulation | 0.9 | 0.44 | 1 | 1 | -3.48 | -1.64 | -20.21 | 19 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 2.75 | 29.39 | 123.94 | 137.57 | 125.63 | 143.36 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.77 | 1.74 | 2 | 2 | 12.67 | 13.83 | -11.09 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -3.29 | 15.55 | 36.83 | 42.82 | 37.79 | 47.49 | False |  | mild_accumulation | 0.54 | 0.01 | 2 | 1 | 2.82 | 2.8 | -9.69 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | -4.36 | 10.81 | 51.73 | 30.2 | 51.73 | 57.17 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 2.44 | 0.5 | 2 | 1 | 6.65 | 6.5 | -9.21 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -1.43 | 4.35 | 3.95 | 7.81 | 9.52 | 19.22 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -1.84 | -1.91 | -13.62 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -10.45 | -17.6 | 19.53 | 55.59 | 22.15 | 59.14 | False |  | distribution_warning | -2.69 | -2.38 | 1 | 0 | -12.31 | -9.92 | -27.28 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 1.41 | 11.11 | 43.43 | 72.25 | 43.14 | 84.62 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -0.5 | 0 | 0 | 6.5 | 5.1 | -12.62 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -12.22 | -13.29 | 37.55 | 19.87 | 37.55 | 49.74 | False |  | distribution_warning | -2.2 | -0.43 | 1 | 1 | -11.11 | -9.81 | -23.45 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -4.27 | -9.53 | 42.86 | 136.29 | 42.49 | 142.95 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.98 | 0.04 | 1 | 1 | -4.62 | -4.34 | -19.08 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -6.51 | -2.33 | 57.19 | 58.43 | 59.68 | 78.05 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -3.82 | -3.37 | 0 | 1 | -1.15 | 1.31 | -7.37 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -2.77 | 1.5 | -1.35 | -6.4 | 4.4 | 4.4 | False |  | distribution_warning | -0.1 | -0.18 | 1 | 0 | -1.41 | -1.15 | -4.04 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | -2.63 | -0.38 | -1.52 | -4.07 | 7.02 | 7.02 | False |  | strong_accumulation | 0.18 | 0.32 | 2 | 2 | -0.8 | -1.12 | -10.38 | 16 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | -5.67 | 14.24 | 6.73 | -4.21 | 19.65 | 19.65 | False |  | strong_accumulation | 1.22 | 1.81 | 3 | 3 | 2.8 | 2.58 | -8.7 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -6.07 | -0.95 | -16.4 | -31.81 | 4.5 | 4.5 | False |  | mild_accumulation | -0.11 | 0.81 | 1 | 3 | -3.46 | -4.2 | -17.06 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -1.87 | 7.69 | -5.19 | -20.6 | 10.24 | 10.24 | False |  | distribution_warning | -0.21 | -0.15 | 1 | 2 | 0.59 | 0.06 | -7.89 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 128.48525684217282 | 290.35375415914626 | -9.58 | 14.81 | 4.83 | -12.5 | 15.67 | 15.67 | False |  | distribution_warning | -0.1 | -0.89 | 2 | 1 | 1.17 | 0.7 | -12.5 | 12 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | -3.3 | 4.1 | -19.87 | -21.69 | 15.11 | 15.11 | False |  | distribution_warning | -0.32 | -0.32 | 0 | 0 | 0.24 | -0.77 | -21.04 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -5.61 | 2.26 | 22.57 | 7.12 | 27.3 | 27.3 | False |  | strong_accumulation | 1.24 | 1.43 | 3 | 3 | -1.49 | -1.07 | -8.92 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -17.55 | -16.56 | -33.28 | -38.23 | 3.37 | 3.37 | False |  | strong_accumulation | 1.25 | 1.32 | 3 | 3 | -15.92 | -13.85 | -34.97 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | -2.68 | 10.55 | 3.32 | -1.36 | 11.11 | 11.11 | False |  | mild_accumulation | -0.04 | 0.37 | 1 | 2 | 1.83 | 1.68 | -5.22 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -5.09 | -14.23 | -15.98 | -14.94 | 3.02 | 3.02 | False |  | distribution_warning | -4.59 | -4.76 | 1 | 2 | -3.0 | -4.66 | -22.64 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -3.1 | 5.26 | 56.49 | 109.21 | 62.07 | 110.08 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.07 | -1.24 | 1 | 0 | -3.01 | 0.86 | -16.39 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | -1.11 | 21.82 | 52.62 | 38.14 | 54.91 | 60.48 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.33 | 0.36 | 2 | 1 | 8.17 | 8.84 | -4.96 |  | fail_already_priced_in |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | -6.61 | 23.69 | 47.63 | 41.71 | 49.3 | 57.5 | True | 近60日漲幅>40% | strong_accumulation | 0.39 | 0.51 | 3 | 3 | 4.96 | 5.4 | -9.79 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | -0.99 | 32.89 | 50.25 | 72.33 | 49.13 | 74.34 | True | 近20日漲幅>25%；近60日漲幅>40%；近120日漲幅>70% | strong_accumulation | 1.08 | 1.28 | 3 | 3 | 8.62 | 9.08 | -4.17 |  | fail_already_priced_in |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | -0.6 | 11.24 | 44.6 | 65.75 | 44.76 | 70.0 | True | 近60日漲幅>40% | distribution_warning | 0.0 | -0.03 | 1 | 1 | 3.59 | 4.46 | -4.88 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | -2.15 | 36.62 | 31.01 | 54.85 | 39.61 | 57.92 | True | 近20日漲幅>25% | strong_accumulation | 1.41 | 1.67 | 3 | 3 | 9.13 | 9.11 | -4.92 |  | fail_already_priced_in |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 7.7 | 30.5 | 23.11 | 35.23 | 36.65 | 39.08 | True | 近20日漲幅>25% | strong_accumulation | 0.84 | 0.86 | 3 | 3 | 13.18 | 11.59 | -4.28 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | -7.06 | -7.42 | 37.79 | 17.33 | 37.39 | 39.0 | False |  | mild_accumulation | 0.06 | 0.0 | 3 | 0 | -3.64 | -2.27 | -20.6 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 52.80006873442736 | 30.333657817463656 | -1.94 | 4.78 | 33.0 | 36.31 | 34.91 | 45.03 | False |  | mild_accumulation | 0.58 | -0.06 | 2 | 1 | 1.22 | 1.23 | -7.85 | 19 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | -4.85 | 3.24 | 23.79 | 24.39 | 18.06 | 29.44 | False |  | mild_accumulation | 1.88 | -2.09 | 2 | 1 | -1.92 | -1.97 | -10.53 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 0.89 | -7.91 | 50.83 | 116.19 | 54.42 | 134.99 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.66 | -4.4 | 1 | 1 | -2.67 | -1.57 | -17.0 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -4.65 | -15.38 | 8.94 | 48.36 | 11.91 | 78.26 | False |  | distribution_warning | -0.55 | -0.88 | 1 | 1 | -10.46 | -8.93 | -25.08 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 92.4008479108611 | 7.500180953989433 | -2.87 | 8.69 | 30.92 | 27.03 | 34.16 | 46.75 | False |  | strong_accumulation | 1.8 | 1.51 | 3 | 3 | 0.17 | 1.24 | -8.65 | 18 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -4.82 | -9.93 | 16.9 | 0.3 | 17.31 | 25.42 | False |  | distribution_warning | -1.86 | -0.81 | 1 | 0 | -5.81 | -4.49 | -21.06 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 8.88 | -0.74 | 61.16 | 113.18 | 58.63 | 118.06 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.17 | -1.84 | 0 | 1 | 2.87 | 3.54 | -8.38 |  | fail_low_response_condition |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -3.79 | -25.3 | -3.79 | 53.93 | 9.39 | 60.82 | False |  | distribution_warning | -1.64 | -1.92 | 0 | 0 | -13.5 | -11.13 | -30.03 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -5.86 | 6.43 | 25.52 | 10.75 | 28.77 | 28.77 | False |  | mild_accumulation | 2.83 | 2.41 | 1 | 1 | 3.14 | 1.4 | -16.0 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -13.22 | -12.5 | 84.48 | 51.44 | 86.12 | 86.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -6.02 | -5.88 | 1 | 1 | -10.94 | -8.3 | -23.08 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -9.14 | -7.78 | -8.61 | 121.98 | 4.05 | 120.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.02 | -0.03 | 2 | 0 | -11.82 | -9.84 | -26.58 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -3.38 | -28.6 | 77.99 | 142.5 | 78.85 | 141.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.91 | -4.92 | 0 | 0 | -13.44 | -9.16 | -30.08 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -5.2 | -3.77 | 71.72 | 218.75 | 59.38 | 280.6 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.63 | 0.24 | 2 | 2 | -8.51 | -6.03 | -24.63 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -3.62 | -14.04 | 129.38 | 53.06 | 136.39 | 140.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -7.41 | -4.7 | -21.78 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 71.36506452239956 | 62.24907879043217 | -9.12 | -17.78 | 27.59 | 18.81 | 27.59 | 36.17 | False |  | distribution_warning | -1.34 | -2.3 | 1 | 1 | -12.31 | -9.54 | -23.6 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -6.3 | -10.9 | 13.94 | 8.64 | 14.34 | 22.47 | False |  | strong_accumulation | 0.41 | 0.23 | 2 | 2 | -7.43 | -6.26 | -16.58 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -2.72 | -4.79 | 9.48 | 28.78 | 14.38 | 31.62 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.61 | -3.99 | -23.34 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -12.91 | -5.35 | 90.52 | 108.98 | 90.11 | 116.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.41 | -0.77 | 1 | 2 | -3.36 | -4.86 | -25.71 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -21.06 | -17.7 | 51.33 | 44.33 | 50.62 | 59.05 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.19 | 2.13 | 2 | 3 | -20.32 | -13.99 | -32.14 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -16.73 | -8.57 | 8.21 | 22.67 | 3.7 | 32.86 | False |  | mild_accumulation | 3.78 | 0.61 | 3 | 1 | -12.52 | -11.4 | -25.83 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -0.47 | -9.36 | 21.02 | 86.19 | 20.48 | 88.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.87 | -1.06 | 0 | 0 | -4.55 | -3.7 | -16.47 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -4.26 | -2.88 | -2.03 | 36.44 | 10.13 | 46.52 | False |  | strong_accumulation | 0.49 | 1.68 | 2 | 2 | -2.84 | -3.61 | -16.17 | 19 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -13.82 | -1.85 | 38.74 | 56.8 | 41.52 | 71.8 | False |  | strong_accumulation | 0.37 | 2.91 | 2 | 2 | -10.32 | -8.23 | -21.19 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -3.04 | -14.93 | 75.27 | 61.66 | 79.89 | 79.89 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -6.07 | -4.47 | 0 | 1 | -12.88 | -6.96 | -24.94 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | -6.32 | -5.51 | 2.19 | 14.79 | 9.4 | 23.95 | False |  | strong_accumulation | 1.05 | 1.36 | 2 | 2 | -4.45 | -4.91 | -17.68 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 2.11 | -0.11 | -14.11 | -25.89 | 8.12 | 8.12 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 1.95 | 1.72 | -19.39 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 112.585794273422 | 77.27049729091536 | -3.64 | -3.99 | 26.79 | 66.14 | 27.4 | 69.87 | False |  | mild_accumulation | 0.04 | 0.28 | 1 | 2 | -5.57 | -4.2 | -17.96 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -8.12 | 12.5 | 24.91 | 35.0 | 26.26 | 36.58 | False |  | mild_accumulation | 0.67 | -0.01 | 1 | 0 | -0.26 | 0.12 | -13.12 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth |  | 69.95652184172461 | 55.27975193155594 | -10.2 | -11.65 | -4.01 | -4.37 | 0.52 | 2.27 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 0 | -10.56 | -8.65 | -18.94 |  | fail_low_response_condition |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -7.38 | -9.95 | 1.27 | 12.56 | 20.27 | 34.05 | False |  | mild_accumulation | 1.12 | -0.18 | 1 | 0 | -12.67 | -8.37 | -25.47 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | -2.16 | 5.92 | 2.41 | 0.15 | 8.28 | 13.52 | False |  | mild_accumulation | 0.17 | 0.02 | 2 | 1 | 2.22 | 1.73 | -3.95 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -14.53 | -11.83 | -11.83 | -20.67 | 0.0 | 0.94 | False |  | strong_accumulation | 0.62 | 0.51 | 3 | 3 | -14.47 | -12.85 | -23.6 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -4.0 | 2.13 | -12.2 | -23.54 | 5.62 | 5.62 | False |  | distribution_warning | -0.12 | -0.02 | 0 | 0 | -1.71 | -2.07 | -15.13 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | -1.42 | -0.71 | -3.47 | -6.08 | 1.83 | 1.83 | False |  | strong_accumulation | 0.35 | 0.06 | 3 | 3 | -0.64 | -0.64 | -6.4 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -7.63 | 6.21 | 1.29 | -9.23 | 8.25 | 8.25 | False |  | mild_accumulation | 0.97 | 1.08 | 1 | 1 | 0.0 | -0.49 | -10.06 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 8.93 | 11.99 | 68.52 | 49.07 | 71.15 | 83.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.55 | -1.13 | 1 | 1 | 10.45 | 10.51 | -4.88 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -10.31 | -14.71 | -20.91 | 14.98 | 0.38 | 29.21 | False |  | mild_accumulation | 0.33 | 0.0 | 1 | 1 | -11.91 | -11.02 | -30.21 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -0.35 | 7.58 | 149.12 | 119.47 | 150.44 | 150.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.37 | 0.83 | 2 | 2 | 3.24 | 4.06 | -13.94 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -5.39 | 7.67 | -2.67 | -14.35 | 9.87 | 9.87 | False |  | mild_accumulation | 0.22 | -0.06 | 3 | 2 | 0.03 | -0.5 | -11.7 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -1.85 | 3.91 | 88.3 | 93.44 | 91.01 | 111.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.16 | -1.02 | 1 | 0 | 0.9 | 2.73 | -11.06 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -15.05 | -0.49 | 61.95 | 19.91 | 64.08 | 68.67 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.98 | 1.2 | 1 | 2 | -5.66 | -5.01 | -22.2 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -9.47 | -10.42 | 10.82 | 18.78 | 25.36 | 33.54 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -7.54 | -7.63 | -38.66 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -6.92 | -24.19 | 62.85 | 113.03 | 75.87 | 123.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.65 | -0.9 | 2 | 2 | -15.17 | -10.76 | -32.1 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -1.03 | -27.72 | 22.54 | 82.94 | 16.97 | 122.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.81 | -2.68 | 1 | 0 | -13.63 | -13.03 | -34.35 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -8.45 | -8.94 | -16.0 | 27.76 | 0.0 | 40.0 | False |  | mild_accumulation | 1.43 | 3.33 | 1 | 3 | -12.98 | -12.62 | -31.71 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 14.36 | 24.19 | 82.75 | 136.2 | 99.83 | 147.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.33 | 1 | 2 | 16.66 | 17.31 | -4.94 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -13.33 | -5.48 | 24.0 | 182.9 | 22.24 | 199.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.12 | 0.81 | 0 | 2 | -8.08 | -9.99 | -28.72 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | 6.11 | -16.81 | 125.0 | 140.29 | 111.09 | 152.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.36 | 2.23 | 1 | 2 | -2.8 | -1.24 | -24.14 |  | fail_already_priced_in |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 1.43 | 9.37 | -19.55 | -26.12 | 14.82 | 14.82 | False |  | distribution_warning | -0.23 | -0.2 | 0 | 2 | 2.78 | 2.09 | -19.83 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -6.56 | -7.88 | -1.3 | 3.4 | 6.29 | 6.29 | False |  | strong_accumulation | 0.77 | 1.06 | 3 | 2 | -6.12 | -5.26 | -11.8 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | -4.23 | 1.02 | -1.37 | -18.75 | 3.39 | 3.39 | False |  | distribution_warning | -0.07 | -0.03 | 0 | 0 | -0.98 | -1.0 | -9.06 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 12.8 | 22.0 | 41.35 | 40.35 | 41.86 | 46.04 | True | 近60日漲幅>40% | mild_accumulation | -0.06 | 1.67 | 2 | 2 | 16.56 | 14.82 | -2.82 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | 11.54 | -11.72 | 46.36 | 95.51 | 53.53 | 99.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.8 | -5.63 | 1 | 1 | 1.79 | 5.15 | -17.14 |  | fail_low_response_condition |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -9.0 | -8.38 | -5.96 | 9.5 | 0.19 | 10.63 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -9.67 | -8.69 | -13.83 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 30.95 | 60.9 | 286.58 | 321.6 | 289.69 | 363.6 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.33 | -5.25 | 1 | 1 | 39.97 | 36.89 | -2.02 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -10.22 | -31.14 | 134.88 | 425.13 | 140.48 | 424.22 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.49 | 1.08 | 1 | 1 | -14.38 | -14.64 | -38.16 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -6.72 | -17.63 | 1.92 | -21.9 | 3.32 | 4.16 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -10.24 | -9.39 | -25.76 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 13.31 | 47.58 | 28.42 | 12.96 | 51.87 | 51.87 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.04 | -0.5 | 1 | 1 | 18.66 | 16.86 | -11.17 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -3.8 | 37.29 | 435.71 | 1439.92 | 425.97 | 1378.1 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.04 | 3.47 | 1 | 3 | 8.46 | 10.67 | -20.43 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 26.64 | 33.88 | 47.09 | 25.67 | 52.56 | 54.72 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 2.29 | 0.13 | 3 | 2 | 25.12 | 22.85 | -2.96 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -8.95 | -3.57 | -9.54 | 40.4 | 3.69 | 51.46 | False |  | distribution_warning | -0.38 | 0.0 | 1 | 0 | -8.31 | -7.67 | -24.52 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -13.19 | -23.51 | -18.44 | -6.29 | 0.35 | 2.54 | False |  | mild_accumulation | -0.61 | 1.27 | 1 | 1 | -15.72 | -14.33 | -31.14 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -14.11 | -15.84 | 17.46 | -0.71 | 20.0 | 20.0 | False |  | mild_accumulation | 1.14 | 0.49 | 1 | 1 | -13.82 | -13.43 | -25.54 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -9.68 | -16.11 | 49.63 | 130.2 | 46.89 | 140.12 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.73 | 0.0 | 0 | 0 | -10.06 | -10.67 | -34.69 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | -11.32 | -21.31 | 69.49 | 91.74 | 67.1 | 112.42 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.49 | 0 | 0 | -9.93 | -7.74 | -23.21 |  | fail_low_response_condition |