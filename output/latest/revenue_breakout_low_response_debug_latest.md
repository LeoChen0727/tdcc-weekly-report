# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-18 16:46:13 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 588970 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 294 |
| low_response_pass | 50 |
| already_priced_in_excluded | 19 |
| overheat_pass | 31 |
| score_pass | 30 |
| theme_priority_pass | 22 |
| final_rows | 22 |

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
| fail_low_response_condition | 244 |
| fail_already_priced_in | 19 |
| fail_defensive_or_traditional_excluded | 8 |
| missing_or_insufficient_price_metrics | 6 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | 1.39 | 5.29 | -10.98 | -27.72 | 9.5 | 9.5 | False |  | mild_accumulation | -0.56 | 0.51 | 2 | 2 | 4.09 | 1.85 | -13.44 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 0.45 | -0.45 | -2.63 | -5.53 | 2.3 | 2.3 | False |  | mild_accumulation | -0.35 | 0.51 | 1 | 1 | -1.25 | -1.37 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -1.07 | 4.23 | -2.63 | -5.85 | 9.14 | 9.14 | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | 0.43 | -0.05 | -7.5 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -1.08 | 9.05 | -9.13 | 19.58 | 15.95 | 24.12 | False |  | mild_accumulation | 0.24 | -0.01 | 1 | 1 | 1.7 | 1.19 | -11.75 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 0.26 | -1.67 | 27.76 | 18.08 | 31.72 | 31.72 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -1.39 | 0.9 | -8.61 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | 10.1 | -13.66 | 92.92 | 121.91 | 92.45 | 134.07 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.05 | -0.88 | 1 | 1 | -8.87 | -3.97 | -28.51 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.83 | 6.36 | 4.11 | 1.83 | 10.58 | 10.58 | False |  | strong_accumulation | 1.82 | 1.2 | 2 | 2 | -0.37 | 0.46 | -9.23 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 41.32 | 110.44 | 116.95 | 142.26 | 125.61 | 155.65 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.76 | 2.47 | 2 | 2 | 66.78 | 54.8 | -1.69 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | -0.52 | -3.98 | -5.16 | -32.4 | 3.21 | 3.21 | False |  | strong_accumulation | 0.11 | 0.02 | 2 | 2 | -1.32 | -2.51 | -20.25 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 3.37 | 12.57 | 5.91 | -1.07 | 14.97 | 14.97 | False |  | strong_accumulation | 0.36 | 0.4 | 2 | 2 | 6.61 | 5.28 | -2.71 | 24 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 1.44 | 13.71 | 17.99 | 47.64 | 31.78 | 53.09 | False |  | distribution_warning | -0.5 | -1.49 | 0 | 0 | 9.88 | 8.6 | -7.84 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 7.27 | 34.87 | 95.03 | 91.23 | 117.94 | 138.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.13 | 0.18 | 1 | 2 | 22.56 | 20.46 | -4.59 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -1.67 | 5.7 | -7.15 | -14.72 | 10.0 | 10.0 | False |  | strong_accumulation | 0.17 | 0.42 | 2 | 3 | 2.65 | 0.58 | -15.38 | 20 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 47.26 | 78.99 | 132.87 | 203.15 | 132.87 | 214.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.49 | 2 | 2 | 39.71 | 39.27 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | 20.71 | 13.04 | 23.81 | 354.91 | 46.32 | 363.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.27 | 3.81 | 2 | 2 | 6.26 | 6.98 | -6.11 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | 39.62 | 74.8 | 119.6 | 209.49 | 160.74 | 211.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.98 | 1.71 | 1 | 1 | 32.58 | 32.84 | 0.0 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 7.03 | -1.42 | 58.63 | 109.91 | 62.88 | 123.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.34 | -1.03 | 1 | 0 | -1.53 | -0.2 | -9.65 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 2.86 | 11.06 | 18.08 | 57.77 | 24.87 | 63.0 | False |  | mild_accumulation | 0.06 | -0.01 | 2 | 2 | 5.97 | 5.71 | -3.11 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 5.48 | 1.76 | 56.08 | 209.65 | 57.68 | 217.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.58 | 0.44 | 2 | 1 | -4.94 | -1.87 | -17.35 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 11.52 | -5.7 | 28.63 | 34.12 | 36.15 | 37.79 | False |  | distribution_warning | -0.75 | -1.18 | 1 | 1 | -2.06 | 1.31 | -12.64 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 0.74 | 1.88 | 52.59 | 128.11 | 58.67 | 134.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.32 | 0.63 | 1 | 2 | 0.84 | 1.6 | -10.86 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 1.62 | 18.99 | 33.57 | 37.73 | 35.25 | 44.62 | False |  | mild_accumulation | 0.31 | 0.26 | 1 | 1 | 5.74 | 5.23 | -14.16 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 9.91 | 11.89 | 108.57 | 274.58 | 115.8 | 280.95 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -0.49 | 1 | 1 | 9.94 | 12.2 | -0.62 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | 23.9 | -7.5 | 54.46 | 38.91 | 63.78 | 90.19 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.38 | -3.51 | 0 | 0 | 7.65 | 9.63 | -10.84 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 5.86 | 9.52 | 35.29 | 33.86 | 54.08 | 54.08 | True | 距60日低點反彈>50% | mild_accumulation | 1.21 | 1.08 | 1 | 2 | 4.24 | 5.99 | -11.54 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | -11.55 | 9.76 | 2.5 | 29.07 | 23.8 | 50.87 | False |  | strong_accumulation | 4.5 | 4.21 | 2 | 2 | -1.76 | -1.45 | -19.52 | 20 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 35.15 | 47.99 | 112.24 | 190.82 | 131.49 | 189.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.76 | 0.63 | 2 | 2 | 26.13 | 25.83 | 0.0 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -0.32 | 25.1 | 44.87 | 53.55 | 47.42 | 57.79 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | 0.64 | 0.02 | 3 | 1 | 15.74 | 14.47 | -3.38 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 8.09 | 13.54 | 33.79 | 35.86 | 51.54 | 56.97 | True | 距60日低點反彈>50% | mild_accumulation | 0.8 | 0.79 | 1 | 1 | 8.17 | 8.5 | -9.32 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.35 | 8.57 | 4.97 | 9.83 | 13.1 | 23.11 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 4.54 | 3.54 | -5.32 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | 6.68 | -1.58 | 23.12 | 83.24 | 49.4 | 81.1 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.73 | 1 | 0 | -4.41 | -2.43 | -18.67 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 13.36 | 6.91 | 42.04 | 74.0 | 44.4 | 83.16 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -0.17 | 1 | 0 | 5.13 | 4.32 | -15.53 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 6.59 | -5.82 | 48.71 | 28.41 | 60.2 | 68.72 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.29 | -0.07 | 1 | 1 | -2.97 | -0.63 | -13.75 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 10.52 | -0.66 | 62.77 | 148.03 | 57.63 | 168.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.97 | -3.65 | 1 | 0 | -1.25 | 1.44 | -13.44 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 4.93 | 17.87 | 43.72 | 83.45 | 65.4 | 85.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.83 | -0.01 | 1 | 1 | 4.76 | 7.55 | -4.05 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -1.32 | 3.34 | -0.33 | -4.58 | 6.54 | 6.54 | False |  | distribution_warning | -0.06 | -0.17 | 2 | 1 | 1.62 | 1.08 | -2.08 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_降級_TDCC轉弱 | 57.09899455038421 | 42.50276733448348 | 5.12 | 0.0 | -2.55 | 1.14 | 10.33 | 10.33 | False |  | distribution_warning | -0.61 | -0.82 | 1 | 1 | 2.38 | 2.1 | -7.61 | 12 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 8.98 | 19.54 | 15.56 | 9.97 | 27.72 | 27.72 | False |  | strong_accumulation | 1.26 | 2.12 | 3 | 3 | 14.03 | 11.88 | -2.54 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 1.59 | 1.13 | -17.04 | -24.96 | 12.0 | 12.0 | False |  | mild_accumulation | -0.08 | 0.82 | 1 | 3 | 3.0 | 1.7 | -17.8 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral | D_降級_TDCC轉弱 | 367.4305802571221 | 58.17838010197999 | 3.23 | 12.03 | 0.9 | -14.2 | 17.32 | 17.32 | False |  | distribution_warning | -0.19 | -0.29 | 1 | 1 | 9.83 | 7.58 | -1.97 | 18 | selected |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 6.19 | 25.39 | 16.5 | 14.29 | 27.93 | 27.93 | True | 近20日漲幅>25% | strong_accumulation | 0.25 | 0.31 | 2 | 2 | 16.53 | 13.01 | -3.23 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | 2.7 | 4.58 | -16.42 | -16.6 | 20.69 | 20.69 | False |  | distribution_warning | -0.42 | -0.75 | 0 | 0 | 7.28 | 4.3 | -18.72 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -1.32 | 3.59 | 25.88 | 19.81 | 32.79 | 32.79 | False |  | strong_accumulation | 1.17 | 1.27 | 2 | 3 | 3.19 | 3.17 | -4.99 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 86.14284031322353 | 42.934476141944494 | -5.77 | -3.08 | -30.11 | -26.87 | 19.03 | 19.03 | False |  | strong_accumulation | 0.76 | 0.51 | 2 | 2 | -2.75 | -3.65 | -33.98 | 17 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 69.90066780612314 | 22.241457982263142 | 1.82 | 12.0 | 3.7 | 5.16 | 14.17 | 14.17 | False |  | distribution_warning | -0.49 | -0.3 | 0 | 1 | 8.14 | 6.38 | -1.75 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -0.48 | -16.19 | -13.39 | -0.48 | 4.02 | 4.02 | False |  | distribution_warning | -5.18 | -5.76 | 0 | 1 | -8.03 | -7.48 | -21.89 | 11 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 2.55 | 28.1 | 68.39 | 116.15 | 69.21 | 119.33 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.51 | -1.09 | 1 | 0 | 7.21 | 8.0 | -12.71 |  | fail_already_priced_in |
| 2867 | 三商壽 | 金融保險業 | defensive_or_traditional |  | 154.9374858432906 | 414.2343371404926 | 6.72 | 14.55 | 16.07 | 11.2 | 17.63 | 18.75 | False |  | strong_accumulation | 1.04 | 1.23 | 2 | 3 | 10.5 | 8.72 | -0.46 |  | fail_low_response_condition |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 72.52927583818101 | 37.88073490992248 | 7.57 | 20.03 | 15.17 | 22.33 | 29.56 | 29.56 | False |  | mild_accumulation | 0.26 | 0.2 | 2 | 1 | 13.85 | 10.67 | -2.17 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 9.96 | 45.11 | 58.44 | 43.75 | 60.84 | 65.27 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.75 | 0.76 | 3 | 2 | 20.48 | 19.43 | -2.13 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | 14.93 | 44.92 | 63.14 | 64.53 | 67.15 | 71.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.45 | 0.52 | 3 | 3 | 24.3 | 22.21 | -1.7 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 10.81 | 41.71 | 55.3 | 79.82 | 60.16 | 79.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.1 | 1.32 | 3 | 3 | 23.01 | 19.83 | -1.44 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 10.39 | 23.41 | 50.78 | 75.26 | 54.55 | 75.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 0.01 | 0.02 | 1 | 1 | 11.17 | 11.01 | -0.29 |  | fail_low_response_condition |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 12.87 | 36.34 | 34.37 | 61.85 | 42.01 | 61.04 | True | 近20日漲幅>25% | strong_accumulation | 0.86 | 0.99 | 2 | 2 | 21.33 | 17.59 | -3.28 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 19.7 | 36.77 | 27.16 | 41.89 | 38.92 | 41.39 | True | 近20日漲幅>25% | strong_accumulation | 0.34 | 0.41 | 2 | 2 | 24.34 | 20.92 | -0.25 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 341.3211844301598 | 175.7452659074452 | 6.52 | 24.83 | 38.27 | 54.13 | 40.16 | 53.47 | False |  | strong_accumulation | 0.16 | 0.18 | 2 | 2 | 12.32 | 11.66 | -1.1 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 1.07 | 9.79 | 33.05 | 13.77 | 38.12 | 38.12 | False |  | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -3.58 | -3.34 | -21.11 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | 4.33 | 12.92 | 38.14 | 49.52 | 44.72 | 54.3 | False |  | distribution_warning | -0.47 | -0.09 | 1 | 1 | 9.97 | 10.53 | -1.96 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 1.89 | 3.07 | 31.22 | 38.95 | 36.55 | 39.96 | False |  | distribution_warning | -1.44 | -4.06 | 1 | 0 | 4.16 | 4.75 | -5.61 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 16.14 | 0.0 | 46.6 | 203.32 | 61.56 | 202.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.07 | -4.52 | 1 | 1 | 0.34 | 3.58 | -13.16 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 2.78 | -5.7 | 23.39 | 78.44 | 23.39 | 89.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.07 | -0.86 | 0 | 1 | -6.98 | -4.97 | -20.27 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | -1.97 | 18.02 | 34.77 | 28.03 | 40.13 | 52.53 | False |  | strong_accumulation | 2.59 | 2.62 | 3 | 3 | 8.57 | 8.21 | -5.06 | 19 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | 1.87 | 0.0 | 17.94 | 16.01 | 27.24 | 32.71 | False |  | mild_accumulation | -1.59 | 2.36 | 1 | 1 | -2.75 | 0.68 | -16.47 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 1.08 | -8.87 | 40.98 | 93.55 | 54.64 | 102.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.0 | 0 | 1 | -5.93 | -3.45 | -15.06 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -4.3 | -23.01 | -4.09 | 51.88 | 12.94 | 66.04 | False |  | distribution_warning | -0.98 | -1.16 | 1 | 1 | -17.74 | -13.18 | -27.76 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 97.9444020544591 | 26.69919866889564 | 16.08 | 3.68 | 21.86 | 12.83 | 32.78 | 32.78 | False |  | mild_accumulation | -0.95 | 0.4 | 1 | 1 | 7.64 | 8.71 | -5.54 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -2.0 | -1.34 | 94.19 | 88.46 | 117.13 | 117.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.21 | -5.65 | 1 | 1 | 2.15 | 7.87 | -10.26 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 0.74 | 0.15 | 5.45 | 153.56 | 15.73 | 157.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.07 | -0.03 | 1 | 0 | -3.11 | -2.98 | -19.31 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | 2.59 | -6.38 | 50.0 | 215.29 | 98.0 | 217.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.44 | -1.29 | 1 | 1 | -11.93 | -5.96 | -25.56 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -3.19 | -1.32 | 158.68 | 263.64 | 146.25 | 307.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.06 | 1.34 | 3 | 2 | -1.73 | 0.5 | -13.68 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | 7.52 | 15.53 | 109.38 | 57.76 | 154.17 | 158.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -0.23 | 3.21 | -15.9 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 71.36506452239956 | 62.24907879043217 | 4.29 | 0.0 | 46.0 | 28.63 | 46.0 | 53.52 | True | 近60日漲幅>40% | strong_accumulation | 1.66 | 1.79 | 2 | 2 | -4.82 | -0.31 | -13.86 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 2.92 | -3.83 | 17.33 | 18.52 | 24.82 | 31.84 | False |  | distribution_warning | -0.32 | -0.23 | 1 | 1 | -2.64 | -0.25 | -10.2 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -3.86 | -2.35 | 10.0 | 32.16 | 19.49 | 37.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.7 | -0.54 | -19.91 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 18.39 | -5.45 | 94.01 | 140.59 | 127.1 | 146.7 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -2.98 | 2 | 1 | 1.96 | 3.54 | -18.32 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -5.56 | 17.8 | 78.8 | 64.93 | 78.8 | 81.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 3.72 | 1.72 | 2 | 2 | -5.52 | -2.9 | -22.46 |  | fail_already_priced_in |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | 8.06 | 5.1 | 14.53 | 57.09 | 30.1 | 58.96 | False |  | strong_accumulation | 2.79 | 0.77 | 2 | 2 | 4.08 | 3.86 | -11.26 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 3.23 | -5.08 | 23.48 | 84.21 | 29.48 | 97.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.76 | -0.66 | 0 | 0 | -3.07 | -0.38 | -12.16 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | 7.83 | 2.58 | 7.51 | 56.33 | 12.58 | 60.54 | False |  | distribution_warning | -0.06 | -0.75 | 2 | 2 | 2.86 | 3.02 | -12.04 | 13 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 1.8 | 7.97 | 1.96 | -18.88 | 11.85 | 11.85 | False |  | strong_accumulation | 0.46 | 0.93 | 2 | 3 | 6.25 | 4.84 | -9.58 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 0.0 | 22.28 | 42.12 | 82.42 | 64.89 | 100.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.54 | 6.07 | 3 | 3 | 10.43 | 10.76 | -5.73 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -9.61 | 5.29 | 73.08 | 85.82 | 94.55 | 94.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.49 | -3.45 | 0 | 1 | -4.2 | 1.5 | -18.82 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 1.79 | -1.72 | -3.39 | 14.77 | 14.0 | 30.04 | False |  | mild_accumulation | 0.13 | -0.05 | 2 | 1 | -1.2 | -0.96 | -13.64 | 22 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 0.78 | 1.34 | -22.56 | -35.29 | 6.59 | 6.59 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 0.49 | -0.58 | -22.89 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | 0.36 | 2.96 | 10.96 | 110.98 | 40.3 | 107.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -4.27 | 1 | 1 | -0.13 | 0.24 | -13.78 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -1.05 | 25.58 | 36.96 | 46.51 | 37.96 | 47.08 | True | 近20日漲幅>25% | mild_accumulation | 0.78 | -0.01 | 2 | 0 | 13.53 | 11.17 | -6.44 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -2.21 | -1.06 | 10.64 | 4.47 | 12.42 | 12.42 | False |  | mild_accumulation | 2.03 | 1.42 | 2 | 1 | -2.93 | -1.74 | -10.9 | 17 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -5.43 | 5.15 | 21.45 | 23.68 | 28.77 | 43.51 | False |  | distribution_warning | -0.89 | -0.23 | 0 | 0 | -5.85 | -2.51 | -20.2 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 1.77 | 5.51 | 2.68 | 7.82 | 8.68 | 15.03 | False |  | mild_accumulation | -0.33 | 0.02 | 1 | 1 | 4.74 | 3.76 | -2.27 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 191.64415257562703 | 643.5739953148809 | -7.0 | 7.05 | 6.59 | 13.94 | 9.25 | 17.17 | False |  | strong_accumulation | 0.48 | 0.49 | 2 | 3 | 0.55 | 0.19 | -11.32 | 21 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 2.04 | 3.92 | -10.87 | -20.74 | 10.27 | 10.27 | False |  | mild_accumulation | -0.04 | 0.01 | 1 | 1 | 3.55 | 1.53 | -12.6 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.0 | 1.08 | -2.44 | -1.75 | 2.56 | 2.56 | False |  | strong_accumulation | 0.6 | 0.04 | 3 | 2 | 0.11 | -0.2 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | B_可觀察 | 452.5877921790185 | 13.290185830553815 | 1.46 | 10.2 | 9.91 | 3.74 | 14.44 | 14.44 | False |  | mild_accumulation | 0.57 | 0.69 | 1 | 1 | 7.69 | 5.84 | -4.91 | 20 | selected |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 155.54062108558796 | 134.80726693594198 | 3.52 | 24.29 | 43.92 | 59.88 | 45.24 | 66.25 | True | 近60日漲幅>40% | mild_accumulation | 0.07 | 0.25 | 1 | 1 | 3.62 | 5.02 | -12.95 |  | fail_already_priced_in |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 12.43 | 7.02 | 30.22 | 37.86 | 60.43 | 72.36 | True | 距60日低點反彈>50% | distribution_warning | -2.6 | -2.77 | 0 | 0 | 3.36 | 4.87 | -7.01 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 78.63452035793752 | 28.54441429888791 | -1.36 | -9.94 | -20.33 | 37.44 | 8.21 | 50.26 | False |  | mild_accumulation | 0.94 | 0.62 | 2 | 1 | -4.73 | -4.03 | -25.64 | 17 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | 21.48 | 22.44 | 157.88 | 134.19 | 174.25 | 174.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | 0.24 | 3 | 1 | 16.76 | 20.69 | -0.64 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 6.33 | 13.9 | 5.99 | 5.77 | 21.3 | 21.3 | False |  | distribution_warning | -0.46 | -1.03 | 2 | 1 | 12.87 | 10.3 | -2.51 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 12.5 | 28.28 | 102.14 | 121.48 | 111.17 | 125.45 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | 0.1 | 2 | 1 | 10.88 | 12.98 | -5.03 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | 22.45 | 13.17 | 80.48 | 64.58 | 101.45 | 101.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -8.34 | -6.8 | 0 | 1 | 14.24 | 16.06 | -7.08 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 3.9 | -4.0 | 14.01 | 42.43 | 39.94 | 49.07 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -1.05 | -0.61 | -31.53 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -2.05 | 13.85 | 141.96 | 184.86 | 141.55 | 188.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 0.65 | 2 | 2 | -1.73 | 4.8 | -19.75 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | 7.67 | -21.46 | 45.17 | 111.98 | 54.78 | 142.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -2.77 | 2 | 0 | -13.78 | -9.4 | -28.4 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | 6.87 | 3.73 | 0.52 | 45.69 | 15.09 | 76.02 | False |  | strong_accumulation | 1.66 | 0.37 | 2 | 2 | 0.19 | 0.98 | -20.93 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 13.49 | 30.86 | 70.97 | 107.44 | 83.39 | 126.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.29 | 1 | 2 | 15.21 | 16.65 | -1.4 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 8.37 | 8.62 | 15.38 | 241.16 | 43.95 | 271.32 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.95 | 0.01 | 0 | 2 | 5.45 | 3.04 | -17.75 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | 15.17 | 6.44 | 104.59 | 172.24 | 133.22 | 171.88 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.65 | -1.13 | 2 | 1 | -1.47 | 2.82 | -21.46 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 5.34 | 4.79 | -2.76 | -33.25 | 8.45 | 8.45 | False |  | mild_accumulation | 0.26 | -0.07 | 3 | 0 | 2.05 | 1.33 | -7.22 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional | D_降級_TDCC轉弱 | 56.34771899764404 | 43.25386406944739 | 5.93 | 6.29 | -18.79 | -27.65 | 15.69 | 15.69 | False |  | distribution_warning | -0.07 | -0.25 | 1 | 2 | 6.48 | 4.37 | -22.32 | 7 | fail_score_lt_8 |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -1.43 | -0.62 | 2.11 | 14.45 | 12.59 | 14.73 | False |  | mild_accumulation | 0.18 | 0.89 | 2 | 1 | -1.54 | -0.69 | -6.58 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 2.25 | 3.81 | -3.76 | -15.67 | 6.65 | 6.65 | False |  | distribution_warning | -0.18 | -0.13 | 0 | 0 | 2.94 | 1.94 | -6.19 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 13.03 | 14.65 | 19.01 | 15.76 | 29.73 | 32.6 | False |  | mild_accumulation | -0.8 | 0.2 | 2 | 2 | 8.73 | 7.87 | -7.93 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | 15.22 | 16.3 | 18.34 | 119.53 | 45.49 | 122.82 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.59 | 4.65 | 1 | 1 | -2.43 | 2.19 | -21.48 |  | fail_low_response_condition |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -0.34 | 0.34 | -3.89 | 21.39 | 6.46 | 22.39 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | -0.08 | 0.1 | -6.76 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 32.68 | 43.97 | 230.62 | 271.12 | 241.18 | 288.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.41 | -3.62 | 1 | 1 | 29.04 | 33.81 | 0.0 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | 22.24 | -17.37 | 157.64 | 541.87 | 197.99 | 547.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.75 | 1.15 | 0 | 2 | -4.41 | 1.3 | -24.29 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 2.55 | -12.09 | 7.68 | -16.28 | 11.15 | 11.66 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -8.35 | -6.36 | -20.41 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 3.12 | 18.21 | 19.06 | -1.49 | 37.34 | 37.34 | False |  | distribution_warning | -0.17 | -0.48 | 0 | 1 | 17.44 | 13.66 | -3.78 |  | fail_low_response_condition |