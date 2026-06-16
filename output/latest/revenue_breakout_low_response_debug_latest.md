# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-17 02:48:57 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1965 |
| standardized_revenue_rows | 1965 |
| price_rows | 585045 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 299 |
| price_metrics_pass | 294 |
| low_response_pass | 60 |
| already_priced_in_excluded | 27 |
| overheat_pass | 33 |
| score_pass | 33 |
| theme_priority_pass | 25 |
| final_rows | 25 |

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
| fail_low_response_condition | 234 |
| fail_already_priced_in | 27 |
| fail_defensive_or_traditional_excluded | 8 |
| missing_or_insufficient_price_metrics | 5 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | 1.88 | 2.36 | -14.57 | -28.38 | 8.5 | 8.5 | False |  | mild_accumulation | -0.56 | 0.51 | 2 | 2 | 3.58 | 1.4 | -14.23 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -5.93 | 0.0 | -5.13 | -5.53 | 2.3 | 2.3 | False |  | mild_accumulation | -0.35 | 0.51 | 1 | 1 | -1.25 | -1.58 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -0.8 | 4.19 | 0.0 | -6.28 | 10.03 | 10.03 | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | 1.62 | 0.75 | -6.75 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -5.99 | 11.79 | -14.31 | 21.01 | 15.19 | 23.31 | False |  | mild_accumulation | 0.24 | -0.01 | 1 | 1 | 1.95 | 0.75 | -14.31 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -0.39 | 0.39 | 24.07 | 17.75 | 31.55 | 31.55 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -1.86 | 0.86 | -8.73 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -13.04 | -12.28 | 86.8 | 107.18 | 92.55 | 122.22 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.05 | -0.88 | 1 | 1 | -14.58 | -10.05 | -32.13 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -4.97 | 9.79 | 3.06 | -0.71 | 11.24 | 11.24 | False |  | strong_accumulation | 1.82 | 1.2 | 2 | 2 | 0.88 | 1.18 | -8.69 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 48.35 | 88.55 | 85.43 | 114.97 | 99.0 | 125.5 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.76 | 2.47 | 2 | 2 | 60.34 | 51.14 | -1.37 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 0.63 | 9.25 | 3.91 | -1.39 | 13.73 | 13.73 | False |  | strong_accumulation | 0.36 | 0.4 | 2 | 2 | 6.61 | 5.24 | -3.04 | 24 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 17.62 | 23.18 | 23.71 | 49.48 | 34.11 | 55.81 | False |  | distribution_warning | -0.5 | -1.49 | 0 | 0 | 13.69 | 12.4 | -6.21 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 24.3 | 47.78 | 95.3 | 77.81 | 111.11 | 131.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.13 | 0.18 | 1 | 2 | 22.55 | 20.92 | -7.57 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 3.08 | 8.78 | -5.37 | -13.0 | 13.39 | 13.39 | False |  | strong_accumulation | 0.17 | 0.42 | 2 | 3 | 6.48 | 4.05 | -12.78 | 20 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | 34.59 | 82.83 | 104.38 | 183.64 | 119.13 | 186.32 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.49 | 2 | 2 | 33.72 | 34.08 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | 6.39 | 18.09 | 4.06 | 337.01 | 44.16 | 364.44 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.27 | 3.81 | 2 | 2 | 6.02 | 6.35 | -7.5 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | 9.75 | 70.56 | 79.09 | 164.08 | 135.08 | 186.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.98 | 1.71 | 1 | 1 | 26.38 | 26.29 | -1.99 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | 0.4 | 7.01 | 56.52 | 118.18 | 68.56 | 131.19 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.34 | -1.03 | 1 | 0 | 1.87 | 3.47 | -6.49 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 3.45 | 11.11 | 20.31 | 55.0 | 24.33 | 62.3 | False |  | mild_accumulation | 0.06 | -0.01 | 2 | 2 | 6.56 | 6.31 | -3.53 | 23 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -11.26 | 12.59 | 46.69 | 188.82 | 58.7 | 219.37 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.58 | 0.44 | 2 | 1 | -4.32 | -1.88 | -16.82 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 88.80451818624007 | 107.89432287557707 | -6.5 | -1.83 | 16.6 | 23.04 | 27.71 | 29.24 | False |  | distribution_warning | -0.75 | -1.18 | 1 | 1 | -8.67 | -5.28 | -18.06 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -0.37 | 8.91 | 36.13 | 117.64 | 57.49 | 133.1 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.32 | 0.63 | 1 | 2 | 0.5 | 1.26 | -11.51 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | -10.27 | 25.0 | 27.87 | 26.53 | 31.58 | 39.42 | False |  | mild_accumulation | 0.31 | 0.26 | 1 | 1 | 3.79 | 2.42 | -17.24 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 6.0 | 16.5 | 82.21 | 219.0 | 97.3 | 249.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -0.49 | 1 | 1 | 1.62 | 4.24 | -9.14 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 88.0613471994038 | 34.31162647538102 | -6.68 | -16.28 | 23.69 | 6.71 | 37.63 | 59.81 | False |  | distribution_warning | -3.38 | -3.51 | 0 | 0 | -10.57 | -6.88 | -25.08 | 13 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 85.01370770897306 | 83.4020606995027 | 1.22 | 21.46 | 33.87 | 31.61 | 51.64 | 51.64 | True | 距60日低點反彈>50% | mild_accumulation | 1.21 | 1.08 | 1 | 2 | 3.84 | 5.64 | -12.94 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 121.1993165447746 | 152.01807699959255 | -8.57 | 17.14 | -4.99 | 30.37 | 25.04 | 52.38 | False |  | strong_accumulation | 4.5 | 4.21 | 2 | 2 | 0.41 | -0.39 | -18.71 | 21 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | 7.59 | 54.55 | 81.62 | 162.35 | 114.11 | 175.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.76 | 0.63 | 2 | 2 | 21.55 | 21.68 | -1.73 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 12.95 | 22.11 | 36.97 | 45.94 | 41.31 | 51.26 | False |  | mild_accumulation | 0.64 | 0.02 | 3 | 1 | 13.37 | 12.43 | -7.38 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 95.17088148345744 | 80.48460599503228 | 10.49 | 20.98 | 28.87 | 27.83 | 51.92 | 57.37 | True | 距60日低點反彈>50% | mild_accumulation | 0.8 | 0.79 | 1 | 1 | 10.24 | 11.08 | -6.29 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.0 | 8.74 | -1.06 | 6.06 | 11.11 | 20.95 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 3.46 | 2.24 | -6.98 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -12.46 | 0.97 | 3.48 | 72.18 | 49.88 | 86.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.73 | 1 | 0 | -4.21 | -2.58 | -18.41 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 4.03 | 12.42 | 34.82 | 73.82 | 45.51 | 83.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -0.17 | 1 | 0 | 6.27 | 5.54 | -15.41 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -7.16 | 4.63 | 25.96 | 32.5 | 56.63 | 64.96 | True | 距60日低點反彈>50% | distribution_warning | -0.29 | -0.07 | 1 | 1 | -5.49 | -2.86 | -15.67 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -9.9 | 1.81 | 53.47 | 130.67 | 62.54 | 152.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.97 | -3.65 | 1 | 0 | -7.05 | -4.43 | -18.5 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -2.94 | 32.0 | 25.95 | 70.98 | 57.14 | 78.7 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 0.83 | -0.01 | 1 | 1 | 1.68 | 4.01 | -7.99 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 1.8 | 4.75 | 0.0 | -4.13 | 7.61 | 7.61 | False |  | distribution_warning | -0.06 | -0.17 | 2 | 1 | 3.01 | 2.38 | -1.09 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_降級_TDCC轉弱 | 57.09899455038421 | 42.50276733448348 | -1.13 | 3.97 | -8.07 | 2.34 | 8.26 | 8.26 | False |  | distribution_warning | -0.61 | -0.82 | 1 | 1 | 0.25 | 0.56 | -9.34 | 12 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 8.49 | 12.2 | 4.39 | 6.15 | 21.05 | 21.05 | False |  | strong_accumulation | 1.26 | 2.12 | 3 | 3 | 10.03 | 8.42 | -4.7 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 5.65 | 1.13 | -17.31 | -25.54 | 12.25 | 12.25 | False |  | mild_accumulation | -0.08 | 0.82 | 1 | 3 | 3.33 | 2.19 | -17.61 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | 6.47 | 6.73 | -5.1 | -20.0 | 12.34 | 12.34 | False |  | distribution_warning | -0.19 | -0.29 | 1 | 1 | 6.14 | 4.08 | -6.14 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 13.43 | 17.89 | 9.62 | 8.06 | 21.54 | 21.54 | False |  | strong_accumulation | 0.25 | 0.31 | 2 | 2 | 13.23 | 10.09 | -6.17 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | 1.97 | 1.43 | -19.21 | -18.62 | 17.52 | 17.52 | False |  | distribution_warning | -0.42 | -0.75 | 0 | 0 | 4.84 | 2.26 | -20.85 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 4.52 | 3.09 | 23.42 | 20.62 | 33.68 | 33.68 | False |  | strong_accumulation | 1.17 | 1.27 | 2 | 3 | 4.29 | 4.65 | -4.35 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 86.14284031322353 | 42.934476141944494 | 1.95 | 10.72 | -28.13 | -24.56 | 26.86 | 26.86 | False |  | strong_accumulation | 0.76 | 0.51 | 2 | 2 | 3.48 | 2.46 | -31.49 | 18 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 69.90066780612314 | 22.241457982263142 | 6.76 | 10.5 | 0.91 | 3.76 | 12.64 | 12.64 | False |  | distribution_warning | -0.49 | -0.3 | 0 | 1 | 7.92 | 6.24 | -3.07 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 9203.558823529413 | 30000.69173757892 | 4.21 | -15.79 | -13.69 | 0.48 | 4.52 | 4.52 | False |  | distribution_warning | -5.18 | -5.76 | 0 | 1 | -9.02 | -8.01 | -21.51 |  | fail_low_response_condition |
| 2851 | 中再保 | 金融保險業 | defensive_or_traditional |  | 1113.1485058158516 | 203.7258536468597 | 7.87 | 13.9 | 30.33 | 52.59 | 36.83 | 54.07 | False |  | mild_accumulation | 0.15 | -0.02 | 2 | 1 | 10.76 | 11.32 | -1.12 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | -5.23 | 34.18 | 62.6 | 116.02 | 71.62 | 121.01 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.51 | -1.09 | 1 | 0 | 10.63 | 10.38 | -12.04 |  | fail_low_response_condition |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 72.52927583818101 | 37.88073490992248 | -0.66 | 16.85 | 11.62 | 21.0 | 26.52 | 26.52 | False |  | mild_accumulation | 0.26 | 0.2 | 2 | 1 | 13.27 | 10.23 | -2.98 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 15.79 | 37.79 | 48.98 | 36.36 | 54.75 | 58.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.75 | 0.76 | 3 | 2 | 19.53 | 18.37 | -0.38 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 130.63810203221996 | 223.540679705256 | 16.0 | 40.56 | 52.08 | 56.21 | 58.47 | 62.7 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.45 | 0.52 | 3 | 3 | 22.5 | 20.72 | 0.0 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 8.39 | 37.5 | 47.76 | 74.19 | 54.69 | 76.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.1 | 1.32 | 3 | 3 | 23.21 | 20.03 | -1.66 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 2.35 | 18.69 | 47.96 | 71.88 | 52.45 | 73.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 0.01 | 0.02 | 1 | 1 | 9.15 | 8.84 | -1.95 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 13.13 | 35.15 | 31.03 | 66.49 | 41.36 | 68.67 | True | 近20日漲幅>25% | strong_accumulation | 0.86 | 0.99 | 2 | 2 | 24.83 | 21.16 | -0.92 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 6.49 | 18.46 | 9.8 | 27.9 | 23.21 | 28.6 | False |  | strong_accumulation | 0.34 | 0.41 | 2 | 2 | 13.35 | 10.59 | -0.98 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 341.3211844301598 | 175.7452659074452 | 4.12 | 22.49 | 35.89 | 52.26 | 40.48 | 53.41 | False |  | strong_accumulation | 0.16 | 0.18 | 2 | 2 | 13.05 | 12.3 | -2.48 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | -0.58 | 25.3 | 39.95 | 17.31 | 51.03 | 51.03 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.05 | 0.0 | 2 | 0 | 6.8 | 5.79 | -13.74 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 52.80006873442736 | 30.333657817463656 | 7.84 | 14.24 | 32.94 | 41.6 | 39.54 | 48.79 | False |  | distribution_warning | -0.47 | -0.09 | 1 | 1 | 7.26 | 8.3 | -1.17 | 14 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 4.72 | 8.13 | 28.5 | 37.11 | 35.03 | 38.54 | False |  | distribution_warning | -1.44 | -4.06 | 1 | 0 | 3.48 | 4.48 | -6.67 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -8.37 | 0.9 | 14.83 | 171.79 | 52.72 | 190.05 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.07 | -4.52 | 1 | 1 | -5.09 | -1.91 | -17.92 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -12.55 | 1.28 | 15.61 | 66.32 | 23.76 | 87.35 | True | 距120日低點反彈>80% | distribution_warning | -1.07 | -0.86 | 0 | 1 | -8.63 | -7.15 | -21.26 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 92.4008479108611 | 7.500180953989433 | 8.68 | 21.29 | 20.58 | 25.15 | 36.98 | 49.1 | False |  | strong_accumulation | 2.59 | 2.62 | 3 | 3 | 7.98 | 7.35 | -7.19 |  | fail_low_response_condition |
| 3025 | 星通 | 通信網路業 | mainstream_growth | A_優先追蹤 | 134.58787189074948 | 63.49927946398063 | 0.14 | 18.58 | 13.41 | 13.23 | 25.81 | 31.21 | False |  | mild_accumulation | -1.59 | 2.36 | 1 | 1 | -3.46 | -0.38 | -17.41 | 21 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -10.63 | -11.37 | 38.01 | 95.05 | 54.23 | 101.62 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.0 | 0 | 1 | -7.13 | -4.41 | -15.29 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -22.34 | -21.51 | -13.78 | 45.03 | 11.17 | 63.43 | False |  | distribution_warning | -0.98 | -1.16 | 1 | 1 | -21.0 | -16.59 | -28.9 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | B_可觀察 | 97.9444020544591 | 26.69919866889564 | 4.35 | 11.86 | 12.58 | 4.76 | 24.53 | 24.53 | False |  | mild_accumulation | -0.95 | 0.4 | 1 | 1 | 1.95 | 3.98 | -6.71 | 17 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | 4.87 | 15.24 | 76.87 | 75.99 | 110.04 | 110.04 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.21 | -5.65 | 1 | 1 | -0.93 | 5.8 | -13.19 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -19.02 | 1.65 | -14.52 | 169.72 | 15.73 | 167.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.07 | -0.03 | 1 | 0 | -3.04 | -3.51 | -19.31 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -19.75 | 1.31 | 22.93 | 193.31 | 93.0 | 214.85 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.44 | -1.29 | 1 | 1 | -14.47 | -9.57 | -27.44 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -11.21 | 2.56 | 131.88 | 243.35 | 163.16 | 298.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.06 | 1.34 | 3 | 2 | -3.89 | -2.0 | -15.79 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -3.98 | 18.12 | 128.97 | 86.04 | 148.06 | 152.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -1.27 | 1.01 | -17.92 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 71.36506452239956 | 62.24907879043217 | -12.19 | 4.07 | 35.1 | 45.45 | 43.22 | 47.74 | False |  | strong_accumulation | 1.66 | 1.79 | 2 | 2 | -8.3 | -4.33 | -17.11 | 18 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -3.61 | 4.2 | 15.28 | 15.67 | 23.05 | 29.96 | False |  | distribution_warning | -0.32 | -0.23 | 1 | 1 | -4.18 | -1.79 | -11.48 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -2.7 | -4.26 | 11.11 | 26.76 | 15.02 | 32.35 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.69 | -4.49 | -22.91 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | 11.82 | 6.84 | 86.01 | 116.26 | 129.91 | 149.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -2.98 | 2 | 1 | 2.92 | 5.97 | -17.31 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -12.14 | 48.37 | 97.12 | 76.72 | 101.31 | 102.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 1.72 | 2 | 2 | 7.65 | 8.53 | -13.68 |  | fail_already_priced_in |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -6.57 | 4.92 | 3.23 | 47.47 | 24.27 | 52.2 | False |  | strong_accumulation | 2.79 | 0.77 | 2 | 2 | 0.06 | -0.02 | -15.23 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -6.44 | -8.4 | 19.26 | 71.38 | 26.01 | 92.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.76 | -0.66 | 0 | 0 | -6.58 | -3.5 | -14.51 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | 1.18 | 6.21 | -4.2 | 42.5 | 7.55 | 55.45 | False |  | distribution_warning | -0.06 | -0.75 | 2 | 2 | -1.27 | -1.17 | -15.97 | 13 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | -1.97 | 0.58 | -3.86 | -9.35 | 3.87 | 3.87 | False |  | mild_accumulation | 0.32 | -0.07 | 3 | 1 | 0.33 | -0.3 | -9.11 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 1.99 | 8.83 | -0.16 | -20.0 | 10.59 | 10.59 | False |  | strong_accumulation | 0.46 | 0.93 | 2 | 3 | 5.85 | 4.48 | -10.6 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | -2.11 | 26.78 | 40.1 | 69.34 | 54.87 | 88.01 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 3.54 | 6.07 | 3 | 3 | 6.14 | 6.16 | -11.45 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -19.18 | 10.12 | 60.98 | 76.79 | 86.09 | 86.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.49 | -3.45 | 0 | 1 | -8.15 | -3.05 | -22.35 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | 1.17 | 5.49 | -8.47 | 21.83 | 15.33 | 31.56 | False |  | mild_accumulation | 0.13 | -0.05 | 2 | 1 | 0.0 | 0.18 | -12.63 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | 1.34 | 0.78 | -19.73 | -34.98 | 6.71 | 6.71 | False |  | mild_accumulation | 0.2 | 0.01 | 1 | 1 | 0.69 | -0.64 | -23.14 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -8.94 | 5.36 | 5.16 | 101.47 | 38.54 | 111.54 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -4.27 | 1 | 1 | -1.1 | -1.09 | -14.86 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 9.91 | 24.91 | 28.87 | 38.11 | 34.56 | 42.41 | False |  | mild_accumulation | 0.78 | -0.01 | 2 | 0 | 12.56 | 10.09 | -9.41 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -5.29 | 2.93 | 6.45 | 2.43 | 12.42 | 12.42 | False |  | mild_accumulation | 2.03 | 1.42 | 2 | 1 | -2.86 | -1.95 | -10.9 | 17 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 152.31709598952162 | 92.03264339471772 | -13.49 | 18.63 | 16.27 | 20.0 | 28.22 | 42.9 | False |  | distribution_warning | -0.89 | -0.23 | 0 | 0 | -5.52 | -3.32 | -20.54 | 17 | selected |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 6.5 | 5.52 | 0.58 | 6.67 | 8.52 | 14.86 | False |  | mild_accumulation | -0.33 | 0.02 | 1 | 1 | 5.2 | 4.44 | -1.71 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 191.64415257562703 | 643.5739953148809 | 2.42 | 7.63 | 7.32 | 24.1 | 11.89 | 25.33 | False |  | strong_accumulation | 0.48 | 0.49 | 2 | 3 | 3.65 | 2.72 | -9.18 | 22 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 0.23 | -0.89 | -14.29 | -22.78 | 8.56 | 8.56 | False |  | mild_accumulation | -0.04 | 0.01 | 1 | 1 | 2.19 | 0.23 | -14.45 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.0 | 1.44 | -2.77 | -2.09 | 2.93 | 2.93 | False |  | strong_accumulation | 0.6 | 0.04 | 3 | 2 | 0.61 | 0.18 | -5.39 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 10.92 | 8.86 | 6.88 | 3.0 | 13.2 | 13.2 | False |  | mild_accumulation | 0.57 | 0.69 | 1 | 1 | 7.72 | 6.12 | -3.4 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 155.54062108558796 | 134.80726693594198 | -6.36 | 29.9 | 42.73 | 60.28 | 46.68 | 66.67 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | 0.07 | 0.25 | 1 | 1 | 6.04 | 6.24 | -12.73 |  | fail_already_priced_in |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -1.58 | 12.78 | 36.93 | 45.26 | 58.28 | 70.05 | True | 距60日低點反彈>50% | distribution_warning | -2.6 | -2.77 | 0 | 0 | 2.47 | 4.23 | -8.25 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 78.63452035793752 | 28.54441429888791 | -4.92 | -3.01 | -23.88 | 60.58 | 8.21 | 62.74 | False |  | mild_accumulation | 0.94 | 0.62 | 2 | 1 | -5.49 | -4.73 | -27.32 | 17 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | 6.56 | 19.48 | 126.23 | 107.83 | 143.39 | 143.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | 0.24 | 3 | 1 | 5.71 | 10.44 | -7.38 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 5.04 | 5.04 | -3.0 | -1.47 | 12.88 | 12.88 | False |  | distribution_warning | -0.46 | -1.03 | 2 | 1 | 6.19 | 4.23 | -4.19 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 7.34 | 33.91 | 87.85 | 110.51 | 101.49 | 119.47 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | 0.1 | 2 | 1 | 8.3 | 9.99 | -9.38 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | 12.51 | 20.79 | 60.44 | 45.94 | 97.72 | 97.72 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -8.34 | -6.8 | 0 | 1 | 13.48 | 17.32 | 0.0 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 1.31 | -13.73 | 2.88 | 37.57 | 35.57 | 44.41 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -4.79 | -3.91 | -33.67 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -25.19 | 10.47 | 95.37 | 130.86 | 104.5 | 138.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 0.65 | 2 | 2 | -17.84 | -13.33 | -33.67 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -18.14 | -16.95 | 17.46 | 103.59 | 45.96 | 128.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -2.77 | 2 | 0 | -20.73 | -16.56 | -32.48 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -12.59 | 5.93 | -8.31 | 39.93 | 10.95 | 69.68 | False |  | strong_accumulation | 1.66 | 0.37 | 2 | 2 | -3.11 | -2.97 | -23.78 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 5.65 | 25.6 | 54.84 | 97.41 | 71.45 | 112.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.1 | 0.29 | 1 | 2 | 10.49 | 12.04 | -0.6 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 14.97 | 9.53 | 25.41 | 255.18 | 51.49 | 290.77 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.95 | 0.01 | 0 | 2 | 11.41 | 9.07 | -13.45 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -12.42 | -5.04 | 67.09 | 133.33 | 110.24 | 148.05 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.65 | -1.13 | 2 | 1 | -10.67 | -7.59 | -29.2 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -1.58 | 6.72 | -4.93 | -31.59 | 8.58 | 8.58 | False |  | mild_accumulation | 0.26 | -0.07 | 3 | 0 | 2.61 | 1.71 | -7.11 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 0.22 | 3.21 | -20.35 | -33.04 | 12.08 | 12.08 | False |  | distribution_warning | -0.07 | -0.25 | 1 | 2 | 3.7 | 1.75 | -24.75 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | -0.41 | 0.83 | -2.2 | 15.64 | 13.75 | 19.02 | False |  | mild_accumulation | 0.18 | 0.89 | 2 | 1 | -0.53 | 0.3 | -5.61 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.63 | 2.29 | -7.04 | -18.36 | 4.95 | 4.95 | False |  | distribution_warning | -0.18 | -0.13 | 0 | 0 | 1.72 | 0.8 | -7.68 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | 11.81 | 15.82 | 16.2 | 15.82 | 27.93 | 30.76 | False |  | mild_accumulation | -0.8 | 0.2 | 2 | 2 | 8.65 | 7.73 | -9.21 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -12.35 | 22.84 | -5.96 | 102.28 | 39.22 | 114.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.59 | 4.65 | 1 | 1 | -5.3 | -2.29 | -24.87 |  | fail_already_priced_in |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -1.66 | 3.49 | -12.67 | 20.28 | 6.46 | 22.39 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | -0.03 | 0.06 | -11.09 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | 16.67 | 38.61 | 168.37 | 198.93 | 182.35 | 221.84 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.41 | -3.62 | 1 | 1 | 10.8 | 16.98 | -9.19 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -1.87 | -15.97 | 119.23 | 495.82 | 174.7 | 505.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.75 | 1.15 | 0 | 2 | -13.75 | -7.16 | -30.2 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -9.39 | -11.87 | 7.1 | -15.72 | 10.92 | 11.43 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | -9.75 | -7.67 | -20.58 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 7.24 | 15.61 | 10.28 | -9.33 | 29.05 | 29.05 | False |  | distribution_warning | -0.17 | -0.48 | 0 | 1 | 12.17 | 9.35 | -9.06 |  | fail_low_response_condition |