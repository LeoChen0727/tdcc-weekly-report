# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-20 00:44:53 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 594855 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 76 |
| already_priced_in_excluded | 30 |
| overheat_pass | 46 |
| score_pass | 45 |
| theme_priority_pass | 33 |
| final_rows | 33 |

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
| fail_low_response_condition | 220 |
| fail_already_priced_in | 30 |
| fail_defensive_or_traditional_excluded | 12 |
| missing_or_insufficient_price_metrics | 4 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | 1.39 | 6.83 | -9.88 | -33.23 | 9.5 | 9.5 | False |  | mild_accumulation | -0.56 | 0.51 | 2 | 2 | 3.67 | 1.77 | -12.05 | 20 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 0.45 | -0.45 | -2.63 | -4.72 | 2.3 | 2.3 | False |  | mild_accumulation | -0.35 | 0.51 | 1 | 1 | -1.27 | -1.14 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -1.07 | 4.23 | 0.0 | -4.88 | 9.14 | 9.14 | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | -0.34 | -0.21 | -7.5 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -1.08 | 9.31 | -5.76 | 22.79 | 15.95 | 23.12 | False |  | mild_accumulation | 0.24 | -0.01 | 1 | 1 | 0.86 | 1.29 | -11.24 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 0.26 | -1.67 | 27.33 | 17.0 | 31.72 | 31.72 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -1.14 | 0.69 | -8.61 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | 10.1 | -21.39 | 85.01 | 118.84 | 91.75 | 134.07 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.05 | -0.88 | 1 | 1 | -6.05 | -2.37 | -28.51 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.83 | 5.16 | 5.03 | 1.46 | 10.58 | 10.58 | False |  | strong_accumulation | 1.82 | 1.2 | 2 | 2 | -1.64 | -0.13 | -10.11 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 41.32 | 110.88 | 109.79 | 144.89 | 125.61 | 155.65 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.76 | 2.47 | 2 | 2 | 59.8 | 49.91 | -1.69 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | -0.52 | -2.28 | -10.23 | -31.8 | 6.04 | 6.04 | False |  | strong_accumulation | 0.11 | 0.02 | 2 | 2 | -1.29 | -2.44 | -20.25 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 3.37 | 11.4 | 3.86 | -4.3 | 14.97 | 14.97 | False |  | strong_accumulation | 0.36 | 0.4 | 2 | 2 | 5.42 | 4.62 | -2.71 | 24 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 1.44 | 12.8 | 22.08 | 47.64 | 31.78 | 53.09 | False |  | distribution_warning | -0.5 | -1.49 | 0 | 0 | 6.9 | 5.6 | -11.04 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 7.27 | 37.85 | 90.69 | 87.57 | 117.94 | 138.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.13 | 0.18 | 1 | 2 | 18.15 | 16.37 | -4.59 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -4.4 | 3.88 | -5.43 |  | 7.08 |  | False |  | mild_accumulation | 0.96 | 0.7 | 3 | 1 | -2.03 | -2.25 | -15.94 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -1.67 | 7.45 | -6.21 | -13.93 | 10.0 | 10.0 | False |  | strong_accumulation | 0.17 | 0.42 | 2 | 3 | 1.81 | 0.3 | -15.38 | 20 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 47.26 | 62.95 | 94.51 | 207.31 | 122.85 | 214.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.49 | 2 | 2 | 36.87 | 37.85 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | 20.71 | 10.82 | 35.2 | 354.91 | 46.32 | 344.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.27 | 3.81 | 2 | 2 | 7.18 | 8.53 | -6.11 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | 39.62 | 70.04 | 136.47 | 206.45 | 160.74 | 201.8 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.98 | 1.71 | 1 | 1 | 29.4 | 32.06 | 0.0 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 7.03 | -4.13 | 47.13 | 107.23 | 62.88 | 123.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.34 | -1.03 | 1 | 0 | -1.09 | -0.02 | -9.65 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 2.86 | 10.93 | 17.04 | 58.57 | 24.87 | 62.72 | False |  | mild_accumulation | 0.06 | -0.01 | 2 | 2 | 5.01 | 5.12 | -3.81 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 5.48 | -6.1 | 43.03 | 211.74 | 57.68 | 209.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.58 | 0.44 | 2 | 1 | -5.04 | -1.49 | -17.35 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 11.52 | -9.1 | 28.63 | 30.77 | 36.15 | 37.79 | False |  | distribution_warning | -0.75 | -1.18 | 1 | 1 | 0.46 | 2.87 | -12.64 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 0.74 | -4.91 | 46.65 | 122.86 | 58.67 | 128.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.32 | 0.63 | 1 | 2 | 0.13 | 0.57 | -14.24 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 1.62 | 18.8 | 30.1 | 41.89 | 35.25 | 44.34 | False |  | mild_accumulation | 0.31 | 0.26 | 1 | 1 | 3.08 | 4.06 | -14.16 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 9.91 | 1.73 | 92.44 | 261.29 | 115.8 | 266.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -0.49 | 1 | 1 | 10.74 | 12.0 | -0.62 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | 23.9 | -3.33 | 49.36 | 44.58 | 63.78 | 90.19 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.38 | -3.51 | 0 | 0 | 12.48 | 11.83 | -10.84 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 5.86 | 1.61 | 43.75 | 28.69 | 54.08 | 54.08 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.21 | 1.08 | 1 | 2 | 4.7 | 5.79 | -11.54 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | -11.55 | 2.8 | -2.38 | 41.67 | 23.8 | 50.87 | False |  | strong_accumulation | 4.5 | 4.21 | 2 | 2 | -2.51 | -1.48 | -19.52 | 20 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 35.15 | 55.24 | 109.34 | 163.32 | 131.49 | 162.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.76 | 0.63 | 2 | 2 | 24.11 | 25.31 | 0.0 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -0.32 | 25.6 | 44.7 | 52.24 | 47.42 | 57.79 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | 0.64 | 0.02 | 3 | 1 | 14.08 | 13.01 | -3.38 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 8.09 | 12.57 | 40.21 | 31.99 | 51.54 | 56.97 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.8 | 0.79 | 1 | 1 | 8.73 | 8.96 | -9.32 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.35 | 6.94 | 4.78 | 12.43 | 13.1 | 23.11 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 3.57 | 3.01 | -5.32 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | 6.68 | 0.16 | 31.99 | 77.49 | 49.4 | 78.0 | True | 近120日漲幅>70% | distribution_warning | -2.79 | -2.73 | 1 | 0 | -3.66 | -1.2 | -18.67 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 13.36 | 6.26 | 39.76 | 77.55 | 44.4 | 81.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -0.17 | 1 | 0 | 6.05 | 5.29 | -15.53 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 6.59 | -6.15 | 48.17 | 29.65 | 60.2 | 68.72 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.29 | -0.07 | 1 | 1 | -1.74 | -0.03 | -13.75 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 10.52 | -9.65 | 44.51 | 168.01 | 55.79 | 166.82 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.97 | -3.65 | 1 | 0 | 0.29 | 2.46 | -13.44 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 4.93 | 12.89 | 49.5 | 76.91 | 65.4 | 84.42 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.83 | -0.01 | 1 | 1 | 3.67 | 7.01 | -4.05 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -1.32 | 3.58 | -0.55 | -3.76 | 6.54 | 6.54 | False |  | distribution_warning | -0.06 | -0.17 | 2 | 1 | 1.12 | 0.76 | -2.08 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_降級_TDCC轉弱 | 57.09899455038421 | 42.50276733448348 | 5.12 | 1.52 | -1.84 | 0.38 | 10.33 | 10.33 | False |  | distribution_warning | -0.61 | -0.82 | 1 | 1 | 2.93 | 2.36 | -7.61 | 12 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 8.98 | 21.13 | 13.04 | 2.82 | 27.72 | 27.72 | False |  | strong_accumulation | 1.26 | 2.12 | 3 | 3 | 12.53 | 10.7 | -2.54 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 1.59 | 1.13 | -13.01 | -26.92 | 12.0 | 12.0 | False |  | mild_accumulation | -0.08 | 0.82 | 1 | 3 | 3.24 | 1.67 | -12.33 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral | D_降級_TDCC轉弱 | 367.4305802571221 | 58.17838010197999 | 3.23 | 13.74 | 0.22 | -15.98 | 17.32 | 17.32 | False |  | distribution_warning | -0.19 | -0.29 | 1 | 1 | 8.92 | 6.94 | -1.97 | 18 | selected |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 6.19 | 25.65 | 17.65 | 1.27 | 27.93 | 27.93 | True | 近20日漲幅>25% | strong_accumulation | 0.25 | 0.31 | 2 | 2 | 15.1 | 12.16 | -3.23 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | 2.7 | 9.15 | -17.63 | -17.63 | 20.69 | 20.69 | False |  | distribution_warning | -0.42 | -0.75 | 0 | 0 | 7.3 | 4.29 | -17.54 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -1.32 | 5.54 | 25.0 | 12.86 | 32.79 | 32.79 | False |  | strong_accumulation | 1.17 | 1.27 | 2 | 3 | 2.99 | 2.7 | -4.99 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 86.14284031322353 | 42.934476141944494 | -5.77 | 4.5 | -30.11 | -29.67 | 19.03 | 19.03 | False |  | strong_accumulation | 0.76 | 0.51 | 2 | 2 | -4.03 | -4.5 | -28.64 | 17 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 69.90066780612314 | 22.241457982263142 | 1.82 | 13.02 | 4.67 | 4.19 | 14.17 | 14.17 | False |  | distribution_warning | -0.49 | -0.3 | 0 | 1 | 6.63 | 5.25 | -2.61 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -0.48 | -15.16 | -15.51 | -9.61 | 4.02 | 4.02 | False |  | distribution_warning | -5.18 | -5.76 | 0 | 1 | -5.49 | -5.9 | -21.89 | 11 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 2.55 | 24.14 | 58.66 | 114.81 | 69.21 | 119.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.51 | -1.09 | 1 | 0 | 3.49 | 6.0 | -12.71 |  | fail_already_priced_in |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 72.52927583818101 | 37.88073490992248 | 7.57 | 25.53 | 14.48 | 20.22 | 29.56 | 29.56 | True | 近20日漲幅>25% | mild_accumulation | 0.26 | 0.2 | 2 | 1 | 12.21 | 9.84 | -2.17 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 9.96 | 41.25 | 57.35 | 41.83 | 60.84 | 65.27 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.75 | 0.76 | 3 | 2 | 16.63 | 17.17 | -2.13 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | 14.93 | 41.72 | 63.6 | 52.98 | 67.15 | 71.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.45 | 0.52 | 3 | 3 | 20.54 | 19.69 | -1.7 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 10.81 | 42.03 | 54.91 | 75.21 | 60.16 | 79.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.1 | 1.32 | 3 | 3 | 18.52 | 16.82 | -1.44 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 10.39 | 21.21 | 50.11 | 69.15 | 54.55 | 74.36 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.01 | 0.02 | 1 | 1 | 9.14 | 9.88 | -0.29 |  | fail_low_response_condition |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 12.87 | 39.27 | 34.93 | 51.64 | 42.01 | 60.64 | True | 近20日漲幅>25% | strong_accumulation | 0.86 | 0.99 | 2 | 2 | 17.96 | 15.4 | -3.28 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 19.7 | 37.48 | 25.55 | 36.77 | 38.92 | 41.39 | True | 近20日漲幅>25% | strong_accumulation | 0.34 | 0.41 | 2 | 2 | 22.05 | 19.8 | -0.25 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 341.3211844301598 | 175.7452659074452 | 6.52 | 25.48 | 35.66 | 45.25 | 40.16 | 46.44 | True | 近20日漲幅>25% | strong_accumulation | 0.16 | 0.18 | 2 | 2 | 9.72 | 9.99 | -1.1 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 1.07 | 4.67 | 29.04 | 14.32 | 38.12 | 38.12 | False |  | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -3.79 | -2.2 | -21.11 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 52.80006873442736 | 30.333657817463656 | 4.33 | 14.59 | 38.97 | 46.39 | 44.72 | 54.3 | False |  | distribution_warning | -0.47 | -0.09 | 1 | 1 | 9.58 | 9.99 | -1.96 | 11 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 1.89 | -4.27 | 33.83 | 34.5 | 36.55 | 36.55 | False |  | distribution_warning | -1.44 | -4.06 | 1 | 0 | 4.49 | 3.99 | -5.61 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 16.14 | 3.71 | 38.08 | 194.67 | 61.56 | 187.18 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.07 | -4.52 | 1 | 1 | 2.07 | 5.19 | -13.16 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 2.78 | -6.8 | 9.34 | 65.52 | 23.39 | 89.72 | True | 距120日低點反彈>80% | distribution_warning | -1.07 | -0.86 | 0 | 1 | -6.63 | -4.25 | -20.27 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | -1.97 | 14.97 | 34.98 | 23.18 | 40.13 | 52.53 | False |  | strong_accumulation | 2.59 | 2.62 | 3 | 3 | 6.24 | 6.3 | -5.06 | 20 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | 1.87 | -9.09 | 18.93 | 11.46 | 27.24 | 32.71 | False |  | mild_accumulation | -1.59 | 2.36 | 1 | 1 | -2.24 | 0.56 | -16.47 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 1.08 | -7.75 | 40.71 | 94.81 | 54.64 | 102.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.0 | 0 | 1 | -4.87 | -2.85 | -15.06 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -4.3 | -26.2 | -2.84 | 46.38 | 12.94 | 66.04 | False |  | distribution_warning | -0.98 | -1.16 | 1 | 1 | -15.56 | -11.7 | -27.76 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 97.9444020544591 | 26.69919866889564 | 16.08 | 4.26 | 23.46 | 13.74 | 32.78 | 32.78 | False |  | mild_accumulation | -0.95 | 0.4 | 1 | 1 | 9.86 | 9.69 | -5.54 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -2.0 | 0.27 | 98.38 | 89.43 | 117.13 | 117.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.21 | -5.65 | 1 | 1 | 2.92 | 6.61 | -10.26 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 0.74 | -1.88 | 9.02 | 151.21 | 14.36 | 157.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.07 | -0.03 | 1 | 0 | -3.77 | -2.94 | -19.31 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | 2.59 | -7.26 | 80.82 | 215.79 | 98.0 | 217.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.44 | -1.29 | 1 | 1 | -11.92 | -5.36 | -25.56 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -3.19 | -6.71 | 120.43 | 277.88 | 122.52 | 307.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.06 | 1.34 | 3 | 2 | -2.5 | -0.77 | -19.21 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | 7.52 | 5.05 | 122.63 | 77.33 | 154.17 | 158.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -0.94 | 3.59 | -15.9 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 71.36506452239956 | 62.24907879043217 | 4.29 | -9.03 | 37.09 | 43.14 | 46.0 | 53.52 | False |  | strong_accumulation | 1.66 | 1.79 | 2 | 2 | -3.92 | 0.42 | -13.86 | 19 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 2.92 | -7.61 | 16.56 | 14.66 | 24.82 | 31.84 | False |  | distribution_warning | -0.32 | -0.23 | 1 | 1 | -1.8 | -0.05 | -10.2 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -3.86 | -6.03 | 9.36 | 32.62 | 19.49 | 37.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.29 | 0.04 | -19.91 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 18.39 | -8.47 | 97.56 | 137.65 | 127.1 | 143.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -2.98 | 2 | 1 | 5.27 | 4.99 | -18.32 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -5.56 | 20.63 | 71.85 | 62.5 | 78.8 | 81.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 3.72 | 1.72 | 2 | 2 | -9.44 | -4.87 | -22.46 |  | fail_already_priced_in |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | 8.06 | 3.08 | 15.02 | 47.25 | 30.1 | 58.96 | False |  | strong_accumulation | 2.79 | 0.77 | 2 | 2 | 4.26 | 4.05 | -11.26 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 3.23 | -9.31 | 21.61 | 89.19 | 29.48 | 97.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.76 | -0.66 | 0 | 0 | -1.71 | 0.36 | -12.16 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | 7.83 | 0.0 | -12.04 | 51.05 | 16.99 | 55.65 | False |  | distribution_warning | -0.06 | -0.75 | 2 | 2 | 3.6 | 3.63 | -11.82 | 13 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 1.8 | 10.07 | 2.81 | -20.54 | 11.85 | 11.85 | False |  | strong_accumulation | 0.46 | 0.93 | 2 | 3 | 5.36 | 4.17 | -9.58 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 0.0 | 16.51 | 44.95 | 83.51 | 64.89 | 100.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.54 | 6.07 | 3 | 3 | 7.29 | 8.1 | -8.18 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -9.61 | 1.97 | 76.02 | 84.16 | 94.55 | 94.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.49 | -3.45 | 0 | 1 | -6.32 | -0.42 | -18.82 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 1.79 | -4.2 | -2.84 | 26.2 | 14.77 | 30.04 | False |  | mild_accumulation | 0.13 | -0.05 | 2 | 1 | 0.23 | 0.04 | -13.64 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 0.78 | 1.8 | -18.01 | -28.1 | 6.59 | 6.59 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 0.28 | -0.42 | -22.89 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | 0.36 | 2.58 | 21.88 | 104.78 | 40.3 | 97.52 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -4.27 | 1 | 1 | -0.49 | 0.33 | -13.78 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -1.05 | 24.34 | 33.57 | 43.73 | 37.96 | 47.08 | False |  | mild_accumulation | 0.78 | -0.01 | 2 | 0 | 10.9 | 9.42 | -6.44 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -2.21 | -2.55 | 7.95 | 3.31 | 12.27 | 12.42 | False |  | mild_accumulation | 2.03 | 1.42 | 2 | 1 | -2.74 | -1.48 | -10.9 | 17 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -5.43 | -4.37 | 17.5 | 23.68 | 28.77 | 43.51 | False |  | distribution_warning | -0.89 | -0.23 | 0 | 0 | -7.62 | -3.64 | -20.2 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 1.77 | 6.66 | 2.68 | 3.77 | 9.71 | 15.03 | False |  | mild_accumulation | -0.33 | 0.02 | 1 | 1 | 4.62 | 3.54 | -2.68 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 191.64415257562703 | 643.5739953148809 | -7.0 | 7.51 | 3.48 | -2.62 | 9.25 | 17.17 | False |  | strong_accumulation | 0.48 | 0.49 | 2 | 3 | -1.07 | -0.77 | -11.32 | 20 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 2.04 | 7.38 | -12.26 | -20.6 | 10.27 | 10.27 | False |  | mild_accumulation | -0.04 | 0.01 | 1 | 1 | 3.22 | 1.64 | -11.39 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.0 | 1.08 | -4.11 | -2.1 | 2.56 | 2.56 | False |  | strong_accumulation | 0.6 | 0.04 | 3 | 2 | 0.09 | -0.08 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | B_可觀察 | 452.5877921790185 | 13.290185830553815 | 1.46 | 10.93 | 5.05 | -2.12 | 14.44 | 14.44 | False |  | mild_accumulation | 0.57 | 0.69 | 1 | 1 | 6.86 | 5.11 | -4.91 | 20 | selected |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 12.43 | 1.98 | 43.38 | 36.26 | 60.43 | 72.36 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -2.6 | -2.77 | 0 | 0 | 4.22 | 5.37 | -7.01 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 78.63452035793752 | 28.54441429888791 | -1.36 | -7.35 | -19.44 | 40.1 | 8.21 | 43.56 | False |  | mild_accumulation | 0.94 | 0.62 | 2 | 1 | -3.86 | -3.7 | -22.46 | 17 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | 21.48 | 22.92 | 155.76 | 138.86 | 174.25 | 174.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | 0.24 | 3 | 1 | 16.44 | 19.64 | -0.64 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 6.33 | 18.17 | 4.13 | 1.31 | 21.3 | 21.3 | False |  | distribution_warning | -0.46 | -1.03 | 2 | 1 | 12.23 | 9.85 | -2.51 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 12.5 | 16.67 | 93.52 | 108.46 | 111.17 | 125.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | 0.1 | 2 | 1 | 9.41 | 12.0 | -5.03 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | 22.45 | 12.65 | 90.39 | 54.62 | 101.45 | 101.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -8.34 | -6.8 | 0 | 1 | 14.84 | 15.32 | -7.08 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 3.9 | -4.0 | 17.07 | 39.53 | 39.94 | 49.07 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -0.25 | -0.11 | -31.53 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -2.05 | 3.62 | 133.28 | 182.61 | 139.53 | 184.86 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 0.65 | 2 | 2 | -3.0 | 4.42 | -19.75 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | 7.67 | -23.18 | 35.37 | 117.68 | 54.78 | 142.51 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -2.77 | 2 | 0 | -10.94 | -7.43 | -28.4 |  | fail_already_priced_in |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | 6.87 | -5.58 | -8.04 | 68.4 | 15.09 | 65.53 | False |  | strong_accumulation | 1.66 | 0.37 | 2 | 2 | -0.19 | 0.8 | -20.93 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 13.49 | 26.19 | 65.62 | 114.36 | 83.39 | 126.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.29 | 1 | 2 | 12.51 | 14.67 | -1.4 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 8.37 | 6.78 | 19.39 | 260.0 | 43.95 | 269.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.95 | 0.01 | 0 | 2 | 6.13 | 3.9 | -17.75 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | 15.17 | -2.84 | 102.17 | 167.97 | 133.22 | 163.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.65 | -1.13 | 2 | 1 | -0.44 | 4.41 | -21.46 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 5.34 | 6.45 | -2.76 | -33.25 | 8.45 | 8.45 | False |  | mild_accumulation | 0.26 | -0.07 | 3 | 0 | 1.11 | 1.01 | -7.22 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional | D_降級_TDCC轉弱 | 56.34771899764404 | 43.25386406944739 | 5.93 | 10.73 | -18.37 | -26.85 | 15.69 | 15.69 | False |  | distribution_warning | -0.07 | -0.25 | 1 | 2 | 5.92 | 4.15 | -20.46 | 7 | fail_score_lt_8 |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -1.43 | -1.43 | 3.43 | 12.33 | 12.59 | 12.59 | False |  | mild_accumulation | 0.18 | 0.89 | 2 | 1 | -1.8 | -1.02 | -6.58 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 2.25 | 5.01 | -3.2 | -15.15 | 6.65 | 6.65 | False |  | distribution_warning | -0.18 | -0.13 | 0 | 0 | 2.68 | 1.9 | -6.19 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 13.03 | 11.46 | 21.62 | 19.4 | 29.73 | 32.6 | False |  | mild_accumulation | -0.8 | 0.2 | 2 | 2 | 8.86 | 8.14 | -7.93 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | 15.22 | 9.76 | 25.34 | 101.63 | 45.49 | 92.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.59 | 4.65 | 1 | 1 | -2.96 | 3.43 | -21.48 |  | fail_low_response_condition |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -0.34 | 1.02 | -1.0 | 20.28 | 6.46 | 22.39 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | -0.44 | -0.17 | -4.66 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 32.68 | 30.97 | 234.98 | 262.5 | 238.9 | 288.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.41 | -3.62 | 1 | 1 | 29.48 | 32.74 | 0.0 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | 22.24 | -12.09 | 168.84 | 540.76 | 197.99 | 546.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.75 | 1.15 | 0 | 2 | -0.44 | 3.38 | -24.29 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 2.55 | -13.66 | 7.09 | -14.04 | 11.15 | 11.66 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -7.08 | -5.48 | -20.41 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 3.12 | 24.44 | 18.21 | -1.49 | 37.34 | 37.34 | False |  | distribution_warning | -0.17 | -0.48 | 0 | 1 | 14.79 | 11.12 | -4.06 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 48.87 | 85.2 | 529.08 | 1976.23 | 572.97 | 1948.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.29 | 3.07 | 2 | 2 | 38.85 | 42.04 | 0.0 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 3.54 | 4.37 | 12.88 | -1.87 | 22.33 | 24.06 | False |  | strong_accumulation | 2.17 | 0.13 | 3 | 2 | 3.85 | 3.37 | -12.33 |  | fail_low_response_condition |