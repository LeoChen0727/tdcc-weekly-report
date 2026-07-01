# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-01 12:06:03 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 608600 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 363 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 709 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 91 |
| already_priced_in_excluded | 43 |
| overheat_pass | 48 |
| score_pass | 48 |
| theme_priority_pass | 32 |
| final_rows | 32 |

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
| fail_low_response_condition | 205 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 16 |
| missing_or_insufficient_price_metrics | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 152.96178992534956 | 138.94580810199872 | 1.46 | 0.97 | -13.28 | -31.7 | 4.5 | 4.5 | False |  | distribution_warning | -0.86 | -1.1 | 1 | 0 | -1.6 | -1.09 | -16.06 | 14 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -0.46 | -3.56 | -6.47 | -9.21 | 1.4 | 1.4 | False |  | distribution_warning | -0.65 | -0.61 | 1 | 0 | -2.63 | -1.77 | -8.82 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -1.11 | -6.81 | -5.57 | -10.33 | 5.01 | 5.01 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | -3.33 | -2.48 | -11.0 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 29.48 | 32.94 | 44.05 | 48.84 | 55.83 | 55.83 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.56 | 0.56 | 3 | 3 | 24.4 | 25.62 | 0.0 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -1.53 | 0.0 | -9.24 | 20.21 | 14.43 | 21.51 | False |  | mild_accumulation | 0.28 | 0.63 | 1 | 1 | -0.95 | 0.31 | -12.4 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -1.91 | -9.66 | 16.88 | 10.94 | 19.6 | 24.14 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -4.58 | -3.34 | -13.88 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -8.44 | -21.88 | 56.49 | 95.83 | 42.28 | 108.89 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.12 | 0.76 | 3 | 1 | -8.34 | -8.96 | -36.2 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -1.67 | -3.4 | 7.3 | -2.6 | 8.86 | 8.86 | False |  | mild_accumulation | 0.7 | 0.01 | 1 | 1 | -2.48 | -0.89 | -11.51 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 10.08 | 100.31 | 107.72 | 143.19 | 117.85 | 146.86 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.62 | -1.38 | 1 | 1 | 23.22 | 23.26 | -5.07 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | 0.0 | 3.09 | -1.32 | -12.02 | 6.95 | 6.95 | False |  | mild_accumulation | 0.07 | -0.05 | 2 | 1 | -3.55 | -2.13 | -9.5 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -1.09 | 14.71 | 19.74 | 32.52 | 27.57 | 35.82 | False |  | distribution_warning | -0.38 | -1.45 | 1 | 0 | -0.58 | 1.81 | -13.88 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | -1.54 | 41.13 | 124.73 | 96.27 | 125.42 | 156.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -1.39 | 0 | 1 | 11.14 | 12.51 | -5.58 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -12.82 | -10.26 | -17.3 |  | 3.03 |  | False |  | distribution_warning | -0.05 | 0.0 | 2 | 0 | -13.38 | -11.16 | -26.09 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 0.16 | -1.88 | -14.21 | -15.7 | 6.44 | 6.44 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | -2.82 | -1.8 | -16.93 | 18 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 3.77 | 67.03 | 118.13 | 250.0 | 154.97 | 259.81 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 1.92 | 3 | 3 | 30.3 | 27.28 | -3.75 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -9.59 | -7.16 | 9.51 | 294.17 | 31.78 | 288.26 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.3 | -1.24 | 2 | 1 | -2.14 | -2.85 | -19.01 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -1.89 | 23.51 | 128.02 | 151.21 | 147.61 | 152.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.57 | -0.72 | 1 | 1 | 10.08 | 11.7 | -11.13 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 2.46 | -0.6 | 47.63 | 110.55 | 45.06 | 128.9 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.33 | -0.27 | 2 | 2 | 2.34 | 2.67 | -8.27 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 1.0 | 5.32 | 12.33 | 57.34 | 15.17 | 57.89 | False |  | strong_accumulation | 0.41 | 0.18 | 3 | 2 | -0.17 | 0.75 | -6.18 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -4.64 | -16.28 | 17.39 | 178.71 | 22.73 | 178.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.19 | -0.02 | 2 | 1 | -6.11 | -4.44 | -22.72 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 4.7 | 2.83 | 46.34 | 48.07 | 48.39 | 51.15 | True | 近60日漲幅>40% | mild_accumulation | 4.16 | 4.43 | 1 | 2 | 8.49 | 6.18 | -9.33 |  | fail_already_priced_in |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -5.14 | -9.43 | 9.59 | 74.67 | 15.38 | 102.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.62 | -0.66 | 2 | 2 | -8.94 | -7.33 | -24.05 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 94.38123673778152 | 82.59499806151248 | -1.21 | -1.21 | 17.57 | 35.29 | 27.56 | 37.06 | False |  | distribution_warning | -0.46 | -0.5 | 0 | 0 | -2.6 | 0.86 | -15.98 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -5.44 | 6.31 | 67.39 | 227.66 | 65.34 | 252.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.52 | 1.68 | 3 | 3 | 3.78 | 2.92 | -10.84 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | -7.91 | -2.01 | 35.24 | 40.69 | 37.78 | 71.26 | False |  | strong_accumulation | 2.18 | 2.19 | 2 | 2 | 1.32 | -0.97 | -19.72 | 21 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 4.76 | 12.34 | 45.53 | 39.09 | 48.31 | 60.78 | True | 近60日漲幅>40% | mild_accumulation | 0.77 | 2.78 | 1 | 3 | 5.41 | 5.54 | -8.97 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 23.67 | 16.43 | 32.28 | 65.54 | 48.49 | 80.95 | True | 距120日低點反彈>80% | distribution_warning | -5.7 | -7.4 | 0 | 0 | 15.11 | 16.36 | -3.46 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -0.44 | 18.61 | 120.73 | 134.46 | 127.39 | 136.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.8 | 0.86 | 1 | 1 | 9.34 | 10.53 | -10.4 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -1.47 | 17.09 | 39.42 | 47.43 | 39.75 | 51.51 | False |  | mild_accumulation | 0.91 | 0.0 | 2 | 1 | 3.24 | 4.47 | -7.23 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 14.87 | 23.16 | 69.29 | 48.44 | 72.85 | 80.08 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 4.55 | 4.6 | 3 | 2 | 18.86 | 17.75 | 0.0 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -1.55 | 7.32 | 4.19 | 12.16 | 13.49 | 23.54 | False |  | distribution_warning | -0.19 | 0.0 | 1 | 0 | 0.74 | 1.49 | -10.49 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -11.31 | -25.45 | 14.38 | 35.97 | 12.45 | 39.16 | False |  | distribution_warning | -3.87 | -2.31 | 1 | 0 | -13.31 | -11.6 | -30.42 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 0.82 | 13.11 | 27.93 | 84.58 | 27.71 | 88.32 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.58 | -0.87 | 0 | 0 | 7.58 | 6.37 | -11.67 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -7.53 | -19.55 | 20.88 | 22.76 | 22.76 | 48.49 | False |  | distribution_warning | -0.96 | -1.22 | 1 | 1 | -9.91 | -8.75 | -24.09 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 6.9 | -2.67 | 25.63 | 147.5 | 27.84 | 168.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.41 | 0.87 | 1 | 1 | 6.52 | 5.65 | -10.4 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 87.19923905471303 | 44.102711379154506 | -4.19 | -1.18 | 39.14 | 52.19 | 45.17 | 78.05 | False |  | distribution_warning | -3.02 | -2.08 | 0 | 1 | -1.13 | 0.67 | -7.37 | 16 | selected |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -1.58 | 0.11 | -2.57 | -6.53 | 3.8 | 3.8 | False |  | distribution_warning | -0.09 | -0.32 | 1 | 0 | -2.14 | -1.43 | -4.59 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | -1.88 | 1.95 | -1.51 | 1.95 | 7.85 | 7.85 | False |  | mild_accumulation | 0.18 | 0.02 | 2 | 1 | -0.13 | -0.21 | -9.69 | 16 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | -1.31 | 9.87 | 9.69 | 0.59 | 19.12 | 19.12 | False |  | strong_accumulation | 0.73 | 1.61 | 2 | 3 | 0.52 | 1.44 | -9.1 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -1.41 | 4.22 | -12.86 | -30.35 | 5.0 | 5.0 | False |  | mild_accumulation | -0.2 | 0.28 | 1 | 3 | -3.27 | -3.07 | -14.81 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -0.94 | 6.58 | -6.03 | -19.04 | 10.5 | 10.5 | False |  | distribution_warning | -0.94 | -1.17 | 1 | 1 | -0.31 | 0.11 | -6.44 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 0.46 | 7.96 | 4.83 | -9.21 | 15.67 | 15.67 | False |  | distribution_warning | -1.12 | -1.16 | 1 | 0 | -0.63 | 0.35 | -12.5 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 0.65 | 5.99 | -18.53 | -19.79 | 17.52 | 17.52 | False |  | mild_accumulation | -0.15 | 0.07 | 1 | 1 | 1.37 | 0.93 | -19.29 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 0.82 | 1.06 | 19.09 | 7.09 | 27.74 | 27.74 | False |  | strong_accumulation | 0.68 | 0.84 | 2 | 2 | -1.48 | -0.6 | -8.6 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -7.89 | -17.98 | -32.96 | -35.86 | 4.05 | 4.05 | False |  | strong_accumulation | 0.12 | 0.04 | 2 | 2 | -13.3 | -10.73 | -34.22 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 0.46 | 10.89 | 3.29 | 0.92 | 12.13 | 12.13 | False |  | mild_accumulation | -0.03 | 0.06 | 1 | 1 | 1.2 | 2.03 | -4.35 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | 0.49 | -16.73 | -20.93 | -12.45 | 2.51 | 2.51 | False |  | distribution_warning | -1.57 | -0.84 | 1 | 2 | -0.94 | -4.09 | -23.02 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -1.19 | 3.73 | 59.24 | 109.21 | 62.07 | 110.08 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.6 | -1.34 | 0 | 0 | -3.71 | 0.56 | -16.39 |  | fail_already_priced_in |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | -5.82 | 17.19 | 46.33 | 34.76 | 49.37 | 55.09 | True | 近60日漲幅>40% | mild_accumulation | 0.32 | 0.34 | 1 | 1 | 1.93 | 3.64 | -8.16 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | -4.65 | 26.71 | 34.74 | 66.38 | 43.14 | 67.35 | True | 近20日漲幅>25% | strong_accumulation | 0.44 | 0.42 | 2 | 2 | 0.39 | 2.86 | -8.01 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 3.42 | 35.16 | 34.89 | 62.99 | 45.51 | 63.39 | True | 近20日漲幅>25% | strong_accumulation | 0.71 | 0.81 | 3 | 3 | 8.76 | 10.68 | -0.89 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 0.25 | 31.03 | 20.54 | 39.51 | 39.27 | 41.74 | True | 近20日漲幅>25% | strong_accumulation | 0.75 | 0.81 | 3 | 3 | 10.73 | 10.35 | -2.44 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 6.84 | 6.42 | 43.57 | 36.75 | 45.09 | 60.41 | True | 近60日漲幅>40% | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 10.8 | 10.68 | -8.38 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | -3.07 | 6.92 | 32.01 | 36.49 | 33.2 | 46.58 | False |  | strong_accumulation | 0.54 | 0.24 | 2 | 2 | 1.27 | 1.65 | -6.87 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 2.29 | 8.5 | 19.64 | 29.47 | 21.27 | 36.04 | False |  | mild_accumulation | 0.83 | 0.2 | 1 | 2 | 2.31 | 3.02 | -5.96 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -7.76 | -9.6 | 45.81 | 91.53 | 53.74 | 93.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.04 | 0.49 | 2 | 2 | -1.97 | -1.86 | -17.37 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 4.12 | -9.34 | 12.98 | 67.22 | 15.56 | 99.6 | True | 距120日低點反彈>80% | strong_accumulation | 0.12 | 0.22 | 2 | 2 | 1.85 | 2.34 | -16.11 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | 2.32 | 10.41 | 34.08 | 29.92 | 27.55 | 51.26 | False |  | strong_accumulation | 0.8 | 0.19 | 3 | 3 | 1.8 | 3.59 | -5.84 | 20 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -1.72 | -5.52 | 6.2 | 7.03 | 19.76 | 28.04 | False |  | mild_accumulation | 1.68 | -0.21 | 2 | 0 | -2.73 | -1.87 | -19.41 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 5.32 | 2.47 | 38.04 | 122.49 | 42.05 | 123.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.96 | 1 | 1 | 5.79 | 5.47 | -5.89 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -2.95 | -25.57 | -4.46 | 56.2 | 8.63 | 56.2 | False |  | distribution_warning | -2.02 | -2.52 | 0 | 0 | -10.06 | -9.24 | -30.52 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -8.33 | 11.5 | 32.1 | 19.92 | 34.91 | 34.91 | False |  | mild_accumulation | 2.13 | 1.43 | 1 | 1 | 6.5 | 5.13 | -12.0 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -9.24 | -8.04 | 79.46 | 51.38 | 76.69 | 85.82 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.21 | 0.15 | 2 | 2 | -9.75 | -6.86 | -23.2 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -4.99 | -8.32 | -8.19 | 93.53 | 1.95 | 120.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | 0.0 | 3 | 0 | -9.39 | -6.57 | -25.15 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -7.47 | -28.34 | 58.85 | 101.46 | 58.85 | 107.27 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.33 | -1.23 | 0 | 0 | -11.96 | -10.18 | -32.52 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 7.95 | 7.12 | 46.18 | 245.08 | 50.09 | 318.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.37 | -0.58 | 2 | 1 | 0.55 | 3.79 | -17.04 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -15.15 | -22.79 | 124.0 | 51.62 | 127.03 | 137.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -6.12 | -5.06 | -22.79 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | 0.0 | -17.01 | 28.11 | 34.3 | 36.95 | 46.16 | False |  | distribution_warning | -1.91 | -1.78 | 0 | 1 | -3.42 | -1.75 | -17.99 | 12 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 52.42017987518027 | 32.00359768097935 | 3.5 | -3.53 | 18.33 | 18.73 | 19.53 | 32.96 | False |  | distribution_warning | -0.13 | -0.22 | 1 | 1 | 1.56 | 2.17 | -9.44 | 14 | selected |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -2.15 | -3.19 | 12.0 | 32.36 | 16.29 | 32.85 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.36 | -1.6 | -22.06 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 2.54 | 4.08 | 82.49 | 128.0 | 88.16 | 126.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.11 | 0.49 | 1 | 2 | 5.8 | 4.04 | -18.57 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -4.86 | -22.56 | 49.1 | 50.91 | 49.1 | 64.31 | True | 近60日漲幅>40% | mild_accumulation | -0.95 | 1.71 | 2 | 2 | -15.46 | -8.8 | -29.89 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -4.92 | -13.75 | -4.92 | 24.33 | 4.04 | 37.6 | False |  | distribution_warning | -2.43 | -0.16 | 2 | 0 | -8.28 | -6.44 | -23.18 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -0.93 | -9.7 | 17.2 | 83.85 | 17.84 | 84.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.79 | -1.09 | 0 | 0 | -2.57 | -2.35 | -16.08 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -2.22 | -3.3 | -5.88 | 38.04 | 15.03 | 53.04 | False |  | strong_accumulation | 6.24 | 7.1 | 3 | 3 | 1.78 | 0.95 | -12.44 | 20 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 2.62 | 2.33 | -3.3 | -7.12 | 4.76 | 4.76 | False |  | strong_accumulation | 0.03 | 0.09 | 2 | 2 | 0.83 | 1.16 | -8.33 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | -4.31 | 1.05 | -7.38 | -25.06 | 3.59 | 3.59 | False |  | mild_accumulation | 0.77 | -0.13 | 3 | 1 | -4.32 | -3.28 | -16.26 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -6.15 | 5.05 | 38.45 | 75.61 | 40.15 | 85.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.49 | -4.13 | 1 | 1 | -3.46 | 0.06 | -14.87 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 2.5 | -13.87 | 84.02 | 79.82 | 83.36 | 92.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -9.23 | -9.01 | 0 | 0 | -4.7 | 0.43 | -19.61 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 2.51 | 6.36 | 13.93 | 32.85 | 23.49 | 39.92 | False |  | strong_accumulation | 1.11 | 2.31 | 2 | 2 | 7.6 | 6.78 | -7.07 | 24 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 6.48 | 0.86 | -14.82 | -24.74 | 10.24 | 10.24 | False |  | mild_accumulation | 0.27 | 0.01 | 1 | 1 | 4.12 | 3.38 | -16.34 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 112.585794273422 | 77.27049729091536 | -3.12 | -8.82 | 19.77 | 39.42 | 24.88 | 54.55 | False |  | distribution_warning | -4.96 | -9.67 | 1 | 1 | -5.47 | -3.99 | -18.42 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -2.72 | 11.18 | 24.74 | 26.06 | 27.86 | 37.69 | False |  | distribution_warning | -0.05 | 0.0 | 1 | 0 | -0.08 | 1.66 | -11.39 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 1.13 | -10.32 | -6.48 | 1.51 | 6.04 | 7.88 | False |  | distribution_warning | -1.75 | -2.16 | 1 | 0 | -4.25 | -2.45 | -14.5 | 14 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | 0.44 | -14.74 | 4.94 | 20.9 | 25.21 | 39.54 | False |  | mild_accumulation | 0.56 | -0.04 | 1 | 0 | -7.76 | -3.5 | -22.41 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 2.37 | 7.98 | 3.45 | 4.55 | 9.87 | 15.19 | False |  | mild_accumulation | 0.49 | 0.0 | 3 | 0 | 2.67 | 2.59 | -2.54 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -10.77 | -12.94 | -12.47 | -15.56 | 1.89 | 1.89 | False |  | distribution_warning | -0.58 | -0.43 | 2 | 2 | -12.32 | -9.67 | -23.0 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -0.69 | -1.15 | -14.31 | -23.72 | 5.38 | 5.38 | False |  | distribution_warning | -0.17 | -0.01 | 0 | 0 | -2.1 | -1.83 | -15.32 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.72 | 0.72 | -2.77 | -3.1 | 2.93 | 2.93 | False |  | strong_accumulation | 0.57 | 0.1 | 3 | 3 | 0.41 | 0.41 | -5.39 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -0.76 | 4.82 | -6.9 | -8.53 | 7.7 | 7.7 | False |  | mild_accumulation | 1.08 | 0.7 | 1 | 1 | -1.3 | -0.83 | -10.51 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 16.69 | 18.79 | 52.56 | 67.21 | 56.71 | 93.3 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.48 | 2 | 2 | 13.21 | 12.13 | -5.04 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -1.09 | -9.6 | -25.21 | 31.25 | 5.0 | 35.15 | False |  | mild_accumulation | 0.06 | 0.05 | 1 | 2 | -6.27 | -5.26 | -27.01 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -10.86 | 4.49 | 129.44 | 120.73 | 129.44 | 146.03 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.34 | 1 | 1 | 0.38 | 1.34 | -15.45 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -1.74 | 3.44 | -4.04 | -16.01 | 8.54 | 8.54 | False |  | mild_accumulation | 0.11 | -0.67 | 2 | 2 | -2.04 | -1.48 | -12.77 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 2.4 | 7.99 | 73.94 | 101.45 | 76.15 | 120.28 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.14 | 0.02 | 1 | 1 | 4.18 | 5.74 | -7.2 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -10.63 | -4.5 | 45.93 | 20.81 | 47.26 | 67.43 | True | 近60日漲幅>40% | distribution_warning | -4.67 | -3.73 | 1 | 1 | -6.43 | -4.96 | -22.78 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -9.76 | -16.77 | 0.25 | 11.81 | 18.66 | 26.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -10.36 | -10.06 | -41.94 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -9.59 | -23.09 | 67.95 | 122.1 | 78.2 | 119.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.12 | -3.04 | 1 | 1 | -10.8 | -7.84 | -31.2 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -11.52 | -28.09 | 6.96 | 96.12 | 3.23 | 121.2 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.2 | 0.0 | 2 | 0 | -9.94 | -11.24 | -34.69 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -17.17 | -13.0 | -22.46 | 20.59 | 4.13 | 36.67 | False |  | mild_accumulation | -1.99 | 2.47 | 0 | 3 | -14.0 | -12.27 | -33.33 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 22.37 | 39.29 | 112.36 | 185.11 | 131.83 | 185.11 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.04 | 2 | 2 | 28.95 | 27.56 | -2.9 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -14.44 | -7.12 | 1.13 | 184.68 | 7.73 | 193.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.83 | 0.65 | 0 | 2 | -8.83 | -9.42 | -29.63 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -4.95 | -11.29 | 107.7 | 122.77 | 102.85 | 154.92 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 1.84 | 1 | 2 | 0.08 | -0.85 | -23.52 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -8.55 | -3.14 | -2.2 | -27.09 | 7.51 | 7.51 | False |  | mild_accumulation | -0.21 | 0.23 | 1 | 1 | -2.02 | -1.15 | -12.06 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -2.56 | -5.58 | 4.82 | 3.86 | 6.53 | 6.53 | False |  | mild_accumulation | 1.08 | -0.03 | 3 | 1 | -4.92 | -3.95 | -11.61 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | -0.38 | -0.5 | -1.85 | -21.96 | 3.78 | 3.78 | False |  | distribution_warning | -0.05 | -0.02 | 0 | 0 | -0.71 | -0.47 | -8.72 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | 6.88 | 17.44 | 26.83 | 36.38 | 28.98 | 37.36 | False |  | strong_accumulation | 1.74 | 2.63 | 3 | 3 | 8.62 | 6.89 | -8.75 | 21 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | 1.4 | -8.39 | 47.59 | 101.52 | 56.27 | 102.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.04 | 2 | 2 | 5.16 | 5.11 | -15.66 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -7.55 | -10.17 | -8.8 | 0.37 | 1.7 | 7.8 | False |  | distribution_warning | -1.33 | 0.0 | 0 | 0 | -8.03 | -6.48 | -13.34 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 6.73 | 54.55 | 253.64 | 317.54 | 257.89 | 355.94 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.18 | -3.65 | 0 | 1 | 28.29 | 25.14 | -9.16 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -6.98 | -15.91 | 146.67 | 461.55 | 159.14 | 459.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.05 | 0.0 | 2 | 0 | -1.88 | -4.52 | -32.04 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -1.82 | -16.92 | 1.89 | -21.54 | 2.0 | 6.0 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -6.14 | -6.11 | -24.44 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 10.91 | 42.97 | 36.73 | 13.94 | 56.02 | 56.02 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.15 | -0.78 | 1 | 0 | 15.23 | 15.12 | -8.74 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -7.66 | 38.08 | 392.82 | 1459.44 | 390.11 | 1527.74 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.48 | 0.23 | 2 | 2 | 13.33 | 16.64 | -12.38 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 16.36 | 28.0 | 44.14 | 24.03 | 48.84 | 50.94 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | -0.03 | 0.02 | 2 | 2 | 16.53 | 13.42 | -10.36 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -1.92 | -10.5 | -14.66 | 44.06 | 5.76 | 54.48 | False |  | mild_accumulation | 1.47 | 0.0 | 2 | 0 | -5.81 | -4.5 | -23.01 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -2.57 | -11.92 | -8.73 | -4.11 | 7.45 | 9.78 | False |  | mild_accumulation | -1.27 | 1.37 | 0 | 1 | -7.44 | -6.57 | -26.28 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -11.32 | -15.23 | 19.15 | -0.94 | 18.65 | 21.73 | False |  | mild_accumulation | 1.16 | 0.49 | 1 | 1 | -10.83 | -10.01 | -24.46 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -7.16 | -10.67 | 41.55 | 133.18 | 41.55 | 140.72 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.12 | 0.0 | 1 | 0 | -8.07 | -8.66 | -34.53 |  | fail_low_response_condition |