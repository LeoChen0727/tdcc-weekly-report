# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-01 14:16:07 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 610565 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 363 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 709 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 92 |
| already_priced_in_excluded | 35 |
| overheat_pass | 57 |
| score_pass | 57 |
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
| fail_already_priced_in | 35 |
| fail_defensive_or_traditional_excluded | 18 |
| missing_or_insufficient_price_metrics | 4 |
| fail_mainstream_score_lt_10 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 152.96178992534956 | 138.94580810199872 | 0.48 | 0.97 | -14.4 | -30.2 | 4.0 | 4.0 | False |  | distribution_warning | -0.86 | -1.1 | 1 | 0 | -2.12 | -1.44 | -16.47 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 0.93 | -5.22 | -5.63 | -8.79 | 1.87 | 1.87 | False |  | distribution_warning | -0.65 | -0.61 | 1 | 0 | -1.91 | -1.21 | -8.4 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -2.47 | -7.07 | -5.33 | -11.03 | 4.72 | 4.72 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | -3.24 | -2.53 | -11.25 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 35.12 | 37.5 | 49.6 | 56.62 | 62.61 | 62.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.56 | 0.56 | 3 | 3 | 27.56 | 27.78 | -4.59 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | -6.02 | 1.81 | -10.79 | 26.01 | 16.6 | 39.11 | False |  | distribution_warning | -0.79 | -0.23 | 0 | 1 | -2.33 | -0.56 | -16.37 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -1.98 | -0.67 | -5.91 | 18.62 | 12.91 | 19.89 | False |  | mild_accumulation | 0.28 | 0.63 | 1 | 1 | -2.24 | -0.94 | -13.57 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -2.85 | -6.53 | 17.38 | 10.15 | 18.94 | 23.45 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -4.79 | -3.56 | -14.35 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -4.98 | -15.63 | 44.3 | 95.89 | 39.51 | 111.85 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.12 | 0.76 | 3 | 1 | -6.23 | -7.07 | -35.29 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -3.09 | -4.12 | 7.24 | -3.89 | 7.8 | 7.8 | False |  | mild_accumulation | 0.7 | 0.01 | 1 | 1 | -3.23 | -1.7 | -12.37 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 1.31 | 93.0 | 89.22 | 139.75 | 113.97 | 142.46 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.62 | -1.38 | 1 | 1 | 17.59 | 18.98 | -6.76 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | -2.33 | -3.57 | -12.3 | -32.98 | 3.85 | 3.85 | False |  | distribution_warning | -0.31 | -0.47 | 1 | 0 | -2.48 | -2.45 | -21.9 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | -4.16 | 2.39 | -3.07 | -10.6 | 6.77 | 6.77 | False |  | mild_accumulation | 0.07 | -0.05 | 2 | 1 | -3.82 | -2.11 | -9.65 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -4.0 | 9.09 | 15.79 | 16.81 | 23.36 | 27.54 | False |  | distribution_warning | -0.38 | -1.45 | 1 | 0 | -4.24 | -1.42 | -16.72 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 2.0 | 50.84 | 128.17 | 121.24 | 131.62 | 166.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -1.39 | 0 | 1 | 13.38 | 15.38 | -2.79 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -13.45 | -14.94 | -22.11 |  | 0.0 |  | False |  | distribution_warning | -0.05 | 0.0 | 2 | 0 | -15.59 | -13.04 | -28.5 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | -0.64 | -3.11 | -12.61 | -16.69 | 5.76 | 5.76 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | -3.29 | -2.23 | -16.47 | 18 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -2.31 | 62.39 | 109.94 | 247.03 | 151.66 | 255.14 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 1.92 | 3 | 3 | 25.51 | 23.0 | -7.32 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -16.57 | -18.23 | -1.71 | 231.03 | 21.61 | 201.15 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.3 | -1.24 | 2 | 1 | -8.77 | -9.57 | -25.26 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -7.32 | 2.98 | 103.21 | 109.25 | 126.73 | 126.73 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.57 | -0.72 | 1 | 1 | 0.65 | 2.08 | -18.63 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 12.0 | 9.69 | 44.96 | 132.31 | 49.02 | 144.04 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.33 | -0.27 | 2 | 2 | 8.58 | 8.61 | -2.21 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 1.41 | 2.3 | 18.03 | 61.1 | 18.33 | 61.1 | False |  | strong_accumulation | 0.41 | 0.18 | 3 | 2 | 2.45 | 3.22 | -3.6 | 26 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | 5.09 | -6.2 | 27.17 | 185.18 | 27.17 | 186.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.19 | -0.02 | 2 | 1 | -1.0 | 0.39 | -18.78 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | 6.21 | 10.03 | 55.72 | 57.39 | 58.06 | 61.01 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 4.16 | 4.43 | 1 | 2 | 14.96 | 11.89 | -3.42 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -2.79 | -4.31 | 11.93 | 89.74 | 16.19 | 105.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.62 | -0.66 | 2 | 2 | -7.22 | -5.33 | -22.78 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 94.38123673778152 | 82.59499806151248 | 0.0 | -7.12 | 15.71 | 34.3 | 28.94 | 38.55 | False |  | distribution_warning | -0.46 | -0.5 | 0 | 0 | -1.17 | 1.79 | -15.07 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -0.45 | 13.89 | 61.84 | 248.11 | 66.72 | 261.76 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.52 | 1.68 | 3 | 3 | 5.88 | 5.19 | -8.44 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | -9.54 | -5.7 | 32.9 | 38.06 | 31.91 | 66.12 | False |  | strong_accumulation | 2.18 | 2.19 | 2 | 2 | -1.43 | -3.62 | -22.12 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 3.59 | 13.04 | 40.39 | 35.42 | 46.07 | 58.34 | True | 近60日漲幅>40% | mild_accumulation | 0.77 | 2.78 | 1 | 3 | 3.2 | 3.6 | -10.34 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 17.2 | 12.29 | 23.69 | 61.77 | 42.81 | 74.03 | False |  | distribution_warning | -5.7 | -7.4 | 0 | 0 | 10.04 | 10.8 | -12.51 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -5.07 | 0.36 | 95.81 | 103.38 | 111.56 | 112.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.8 | 0.86 | 1 | 1 | 1.71 | 2.6 | -16.63 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | -2.31 | 14.09 | 32.21 | 45.39 | 33.11 | 47.2 | False |  | mild_accumulation | 0.91 | 0.0 | 2 | 1 | 0.55 | 2.19 | -9.08 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 13.12 | 20.8 | 62.5 | 37.38 | 53.35 | 73.51 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 4.55 | 4.6 | 3 | 2 | 13.4 | 12.19 | -6.34 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -11.27 | 1.43 | 1.25 | 9.88 | 12.5 | 22.46 | False |  | distribution_warning | -0.19 | 0.0 | 1 | 0 | -0.21 | 0.56 | -11.27 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -14.8 | -31.09 | 4.16 | 23.4 | 4.81 | 30.81 | False |  | distribution_warning | -3.87 | -2.31 | 1 | 0 | -16.98 | -15.72 | -34.6 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 71.83340834565679 | 63.183650278464505 | -10.88 | 0.98 | 16.29 | 63.12 | 24.1 | 77.15 | False |  | distribution_warning | -0.58 | -0.87 | 0 | 0 | 4.48 | 3.07 | -14.17 | 13 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -9.04 | -19.87 | 19.4 | 13.69 | 22.26 | 48.91 | False |  | distribution_warning | -0.96 | -1.22 | 1 | 1 | -8.63 | -7.84 | -23.88 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | 9.86 | 9.86 | 19.19 | 139.26 | 33.2 | 180.26 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.41 | 0.87 | 1 | 1 | 10.44 | 9.16 | -6.65 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 87.19923905471303 | 44.102711379154506 | -6.39 | -3.49 | 35.14 | 52.53 | 43.72 | 76.28 | False |  | distribution_warning | -3.02 | -2.08 | 0 | 1 | -1.93 | -0.31 | -8.29 | 15 | selected |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | -1.69 | -0.11 | -2.79 | -6.03 | 3.69 | 3.69 | False |  | distribution_warning | -0.09 | -0.32 | 1 | 0 | -2.24 | -1.42 | -4.7 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | 0.76 | 4.31 | 1.14 | 3.1 | 9.92 | 9.92 | False |  | mild_accumulation | 0.18 | 0.02 | 2 | 1 | 1.57 | 1.55 | -7.96 | 17 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 1.03 | 9.94 | 11.54 | 5.05 | 20.35 | 20.35 | False |  | strong_accumulation | 0.73 | 1.61 | 2 | 3 | 1.09 | 2.28 | -8.17 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral | B_可觀察 | 506.2302328794015 | -80.54983396731191 | 4.67 | 10.89 | -6.28 | -25.58 | 12.0 | 12.0 | False |  | mild_accumulation | -0.2 | 0.28 | 1 | 3 | 2.66 | 3.1 | -9.13 | 19 | selected |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -2.11 | 6.11 | -6.08 | -19.34 | 9.45 | 9.45 | False |  | distribution_warning | -0.94 | -1.17 | 1 | 1 | -1.53 | -0.77 | -7.33 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | -2.7 | 8.22 | 4.85 | -6.9 | 15.14 | 15.14 | False |  | distribution_warning | -1.12 | -1.16 | 1 | 0 | -1.46 | -0.1 | -12.9 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 418.92924119579374 | 17.34399183311113 | 0.38 | 9.03 | -17.8 | -18.23 | 18.58 | 18.58 | False |  | mild_accumulation | -0.15 | 0.07 | 1 | 1 | 1.86 | 1.69 | -18.57 | 17 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | -1.74 | -0.24 | 15.4 | 7.9 | 25.67 | 25.67 | False |  | strong_accumulation | 0.68 | 0.84 | 2 | 2 | -3.07 | -2.04 | -10.08 | 20 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -1.54 | -16.28 | -33.85 | -36.69 | 3.37 | 3.37 | False |  | strong_accumulation | 0.12 | 0.04 | 2 | 2 | -13.13 | -10.47 | -34.53 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 3.69 | 9.76 | 5.63 | 4.65 | 14.68 | 14.68 | False |  | mild_accumulation | -0.03 | 0.06 | 1 | 1 | 3.02 | 3.98 | -2.17 | 18 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | 0.49 | -2.39 | -20.0 | -11.3 | 2.51 | 2.51 | False |  | distribution_warning | -1.57 | -0.84 | 1 | 2 | -0.82 | -3.77 | -23.02 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 2.34 | 1.72 | 58.93 | 111.34 | 63.05 | 110.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.6 | -1.34 | 0 | 0 | -3.21 | 1.07 | -15.89 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 5.54 | 27.78 | 35.85 | 63.48 | 45.95 | 63.48 | True | 近20日漲幅>25% | strong_accumulation | 0.71 | 0.81 | 3 | 3 | 7.81 | 10.0 | -2.2 |  | fail_already_priced_in |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 1.14 | 29.03 | 22.32 | 38.89 | 39.62 | 42.1 | True | 近20日漲幅>25% | strong_accumulation | 0.75 | 0.81 | 3 | 3 | 9.63 | 9.66 | -2.2 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 6.89 | 3.63 | 36.43 | 35.75 | 38.87 | 59.24 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 9.77 | 8.98 | -9.05 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | -6.13 | 6.63 | 32.2 | 38.16 | 31.27 | 45.47 | False |  | strong_accumulation | 0.54 | 0.24 | 2 | 2 | 0.2 | 0.81 | -7.57 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 4.17 | 15.06 | 18.53 | 25.0 | 24.43 | 39.59 | False |  | mild_accumulation | 0.83 | 0.2 | 1 | 2 | 4.27 | 5.21 | -3.51 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | A_優先追蹤 | 296.8056658653291 | 223.4596397756601 | -13.59 | -20.37 | 36.54 | 64.48 | 44.9 | 61.36 | False |  | mild_accumulation | -0.04 | 0.49 | 2 | 2 | -6.51 | -6.92 | -22.12 | 21 | selected |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | 3.56 | -2.96 | 15.67 | 80.07 | 19.91 | 107.11 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.12 | 0.22 | 2 | 2 | 5.85 | 5.64 | -12.96 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 92.4008479108611 | 7.500180953989433 | 0.12 | 6.69 | 24.47 | 27.34 | 26.18 | 49.64 | False |  | strong_accumulation | 0.8 | 0.19 | 3 | 3 | 0.39 | 2.26 | -6.85 | 20 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -4.86 | -7.77 | 2.47 | 2.47 | 16.26 | 24.3 | False |  | mild_accumulation | 1.68 | -0.21 | 2 | 0 | -5.2 | -4.36 | -21.76 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | 1.76 | -3.81 | 36.03 | 112.07 | 37.41 | 110.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.96 | 1 | 1 | 3.07 | 2.33 | -8.49 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -3.65 | -27.37 | -6.43 | 50.18 | 7.11 | 51.8 | False |  | distribution_warning | -2.02 | -2.52 | 0 | 0 | -9.81 | -9.72 | -31.49 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -9.24 | 9.16 | 30.84 | 6.87 | 32.08 | 32.08 | False |  | mild_accumulation | 2.13 | 1.43 | 1 | 1 | 3.81 | 2.67 | -13.85 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -4.78 | -12.63 | 73.35 | 43.76 | 80.49 | 94.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.21 | 0.15 | 2 | 2 | -5.09 | -2.49 | -19.78 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -8.18 | -15.83 | -19.41 | 89.97 | 0.5 | 112.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | 0.0 | 3 | 0 | -11.84 | -9.1 | -27.77 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -13.02 | -30.42 | 44.59 | 87.64 | 47.79 | 92.84 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.33 | -1.23 | 0 | 0 | -16.59 | -15.27 | -37.22 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 6.18 | 0.24 | 33.02 | 263.71 | 37.58 | 318.91 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.37 | -0.58 | 2 | 1 | 0.54 | 3.47 | -17.04 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -11.47 | -17.89 | 100.49 | 45.94 | 82.34 | 133.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -6.75 | -6.12 | -24.08 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | -1.81 | -13.97 | 16.31 | 24.88 | 33.5 | 42.48 | False |  | distribution_warning | -1.91 | -1.78 | 0 | 1 | -5.13 | -3.88 | -20.06 | 12 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 52.42017987518027 | 32.00359768097935 | 4.97 | -1.64 | 20.47 | 19.67 | 20.88 | 34.46 | False |  | distribution_warning | -0.13 | -0.22 | 1 | 1 | 2.79 | 3.04 | -8.42 | 11 | selected |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -3.19 | -3.19 | 13.04 | 26.39 | 13.75 | 32.85 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.19 | -1.47 | -22.06 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 3.38 | 11.25 | 89.31 | 130.89 | 95.92 | 135.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.11 | 0.49 | 1 | 2 | 9.55 | 7.59 | -15.21 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -5.77 | -22.83 | 41.62 | 45.4 | 40.4 | 61.18 | True | 近60日漲幅>40% | mild_accumulation | -0.95 | 1.71 | 2 | 2 | -16.03 | -9.74 | -31.23 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -5.71 | -16.0 | -13.81 | 20.56 | 3.59 | 37.01 | False |  | distribution_warning | -2.43 | -0.16 | 2 | 0 | -7.88 | -6.31 | -23.51 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 3.29 | -7.56 | 20.22 | 85.81 | 19.83 | 87.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.79 | -1.09 | 0 | 0 | 0.57 | 0.36 | -13.73 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.11391792521879 | 34.318355180717255 | -4.18 | -0.86 | -7.77 | 35.43 | 12.42 | 49.57 | False |  | strong_accumulation | 6.24 | 7.1 | 3 | 3 | -0.49 | -1.23 | -14.43 | 19 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 1.45 | 1.74 | -4.63 | -8.62 | 4.17 | 4.17 | False |  | strong_accumulation | 0.03 | 0.09 | 2 | 2 | 0.17 | 0.53 | -8.85 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | -7.04 | -1.22 | -9.84 | -23.04 | 1.97 | 1.97 | False |  | mild_accumulation | 0.77 | -0.13 | 3 | 1 | -5.76 | -4.41 | -17.56 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -7.85 | 3.72 | 31.8 | 63.49 | 35.48 | 80.71 | True | 距120日低點反彈>80% | distribution_warning | -3.49 | -4.13 | 1 | 1 | -6.14 | -2.35 | -17.1 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 10.84 | -1.32 | 98.76 | 92.97 | 101.25 | 111.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -9.23 | -9.01 | 0 | 0 | 4.67 | 9.3 | -11.76 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | B_可觀察 | 281.10296953335904 | 153.94170544805627 | 0.85 | 3.81 | 11.67 | 26.88 | 18.79 | 34.6 | False |  | strong_accumulation | 1.11 | 2.31 | 2 | 2 | 3.31 | 2.49 | -10.61 | 21 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 6.48 | 4.11 | -14.82 | -27.36 | 10.24 | 10.24 | False |  | mild_accumulation | 0.27 | 0.01 | 1 | 1 | 3.91 | 3.09 | -15.96 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -9.89 | -17.73 | 14.12 | 29.46 | 18.72 | 46.92 | False |  | distribution_warning | -4.96 | -9.67 | 1 | 1 | -9.26 | -8.06 | -22.45 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | -1.11 | 11.56 | 25.7 | 21.43 | 23.1 | 37.31 | False |  | distribution_warning | -0.05 | 0.0 | 1 | 0 | -0.87 | 1.26 | -11.63 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | -2.57 | -14.68 | -5.35 | 0.0 | 4.46 | 6.28 | False |  | distribution_warning | -1.75 | -2.16 | 1 | 0 | -4.9 | -3.59 | -15.77 | 14 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -4.77 | -21.69 | 11.4 | 18.45 | 23.15 | 37.25 | False |  | mild_accumulation | 0.56 | -0.04 | 1 | 0 | -8.12 | -4.68 | -23.68 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 2.07 | 8.49 | 3.6 | 5.34 | 9.87 | 15.19 | False |  | mild_accumulation | 0.49 | 0.0 | 3 | 0 | 2.26 | 2.37 | -2.54 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -9.65 | -13.98 | -11.87 | -12.82 | 1.89 | 1.89 | False |  | distribution_warning | -0.58 | -0.43 | 2 | 2 | -11.69 | -8.93 | -23.0 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | -1.37 | -0.92 | -14.62 | -23.13 | 5.62 | 5.62 | False |  | distribution_warning | -0.17 | -0.01 | 0 | 0 | -1.83 | -1.47 | -15.13 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.36 | 0.0 | -3.11 | -3.11 | 2.56 | 2.56 | False |  | strong_accumulation | 0.57 | 0.1 | 3 | 3 | 0.05 | 0.05 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | -0.25 | 7.19 | -5.73 | -6.18 | 8.67 | 8.67 | False |  | mild_accumulation | 1.08 | 0.7 | 1 | 1 | -0.75 | 0.05 | -9.71 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | 11.49 | 19.69 | 43.4 | 61.42 | 54.84 | 90.99 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.48 | 2 | 2 | 10.84 | 9.81 | -6.17 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -5.71 | -13.73 | -26.26 | 25.71 | 1.54 | 30.69 | False |  | mild_accumulation | 0.06 | 0.05 | 1 | 2 | -8.7 | -7.73 | -28.84 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -15.91 | -1.89 | 109.55 | 103.94 | 112.3 | 128.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.34 | 1 | 1 | -6.73 | -5.46 | -21.52 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 149.18224366317995 | 540.6620723440313 | -0.11 | 7.09 | -2.54 | -12.45 | 10.83 | 10.83 | False |  | mild_accumulation | 0.11 | -0.67 | 2 | 2 | -0.3 | 0.55 | -10.93 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 5.74 | 10.44 | 75.42 | 106.88 | 81.56 | 127.04 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.14 | 0.02 | 1 | 1 | 6.83 | 8.17 | -4.52 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -11.01 | 0.0 | 44.0 | 19.28 | 44.53 | 64.32 | True | 近60日漲幅>40% | distribution_warning | -4.67 | -3.73 | 1 | 1 | -8.17 | -6.2 | -24.21 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 8.85 | -8.09 | 17.82 | 23.06 | 29.15 | 37.58 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.01 | -1.94 | -36.8 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -14.08 | -21.9 | 61.31 | 105.2 | 72.09 | 105.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.12 | -3.04 | 1 | 1 | -12.81 | -10.18 | -33.56 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -10.4 | -26.83 | -3.81 | 88.56 | 1.88 | 118.32 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.2 | 0.0 | 2 | 0 | -9.64 | -11.48 | -35.54 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -18.6 | -16.22 | -32.26 | 14.13 | 0.32 | 31.25 | False |  | mild_accumulation | -1.99 | 2.47 | 0 | 3 | -16.74 | -14.63 | -35.98 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 17.24 | 50.78 | 110.53 | 174.75 | 135.29 | 178.69 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.04 | 2 | 2 | 28.05 | 26.36 | -3.2 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -6.42 | 10.02 | 12.11 | 207.08 | 18.45 | 203.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.83 | 0.65 | 0 | 2 | -0.21 | -0.37 | -22.63 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -10.19 | -10.6 | 86.24 | 109.6 | 91.43 | 145.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 1.84 | 1 | 2 | -3.08 | -4.17 | -26.36 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -10.39 | -3.11 | -0.61 | -26.67 | 8.71 | 8.71 | False |  | mild_accumulation | -0.21 | 0.23 | 1 | 1 | -0.76 | -0.04 | -11.07 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -3.02 | -7.41 | 2.27 | 2.27 | 4.9 | 4.9 | False |  | mild_accumulation | 1.08 | -0.03 | 3 | 1 | -6.02 | -4.99 | -12.96 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.0 | -0.75 | -2.34 | -21.23 | 3.52 | 3.52 | False |  | distribution_warning | -0.05 | -0.02 | 0 | 0 | -0.92 | -0.66 | -8.94 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | -1.06 | 16.46 | 19.05 | 35.38 | 27.12 | 35.14 | False |  | strong_accumulation | 1.74 | 2.63 | 3 | 3 | 6.25 | 4.88 | -10.07 | 20 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -13.3 | -13.5 | 34.12 | 76.48 | 45.69 | 74.41 | True | 近120日漲幅>70% | distribution_warning | -1.2 | -1.04 | 2 | 2 | -1.21 | -1.84 | -21.38 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -7.44 | -12.58 | -9.78 | -0.74 | 0.94 | 7.0 | False |  | distribution_warning | -1.33 | 0.0 | 0 | 0 | -8.11 | -6.62 | -13.99 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 3.67 | 73.97 | 279.1 | 326.89 | 277.98 | 386.59 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.18 | -3.65 | 0 | 1 | 33.05 | 29.92 | -3.05 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -8.36 | -12.57 | 137.87 | 436.48 | 151.75 | 428.59 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.05 | 0.0 | 2 | 0 | -4.02 | -6.68 | -33.98 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -2.14 | -17.0 | 0.22 | -21.63 | 1.44 | 5.43 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -5.75 | -6.11 | -24.86 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 6.96 | 39.77 | 34.67 | 14.24 | 53.11 | 53.11 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.15 | -0.78 | 1 | 0 | 11.3 | 11.77 | -10.44 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 2.97 | 44.21 | 388.44 | 1553.06 | 386.0 | 1673.72 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.48 | 0.23 | 2 | 2 | 21.2 | 24.3 | -4.52 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 6.33 | 27.6 | 45.0 | 24.61 | 47.69 | 50.47 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | -0.03 | 0.02 | 2 | 2 | 14.73 | 11.85 | -10.64 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -2.88 | -6.61 | -15.83 | 42.83 | 4.43 | 52.54 | False |  | mild_accumulation | 1.47 | 0.0 | 2 | 0 | -6.69 | -5.25 | -23.98 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -1.95 | -10.65 | -14.2 | -5.92 | 7.09 | 9.42 | False |  | mild_accumulation | -1.27 | 1.37 | 0 | 1 | -7.23 | -6.34 | -26.52 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -9.25 | -13.03 | 17.15 | -2.95 | 19.44 | 22.88 | False |  | mild_accumulation | 1.16 | 0.49 | 1 | 1 | -9.37 | -8.46 | -23.75 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -5.31 | -6.82 | 36.67 | 132.95 | 36.67 | 145.51 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.12 | 0.0 | 1 | 0 | -5.92 | -6.31 | -33.22 |  | fail_low_response_condition |