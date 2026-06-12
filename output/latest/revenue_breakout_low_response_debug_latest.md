# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-12 00:31:43 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1947 |
| standardized_revenue_rows | 1947 |
| price_rows | 579151 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 440 |
| tdcc_mild_accumulation_count | 742 |
| tdcc_distribution_warning_count | 638 |
| revenue_condition_pass | 290 |
| price_metrics_pass | 285 |
| low_response_pass | 49 |
| already_priced_in_excluded | 16 |
| overheat_pass | 33 |
| score_pass | 32 |
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
| fail_revenue_condition | 1657 |
| fail_low_response_condition | 236 |
| fail_already_priced_in | 16 |
| fail_defensive_or_traditional_excluded | 6 |
| missing_or_insufficient_price_metrics | 5 |
| fail_non_mainstream_score_lt_11 | 1 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_僅留完整清單 | 152.96178992534956 | 138.94580810199872 | 4.35 | 1.89 | -16.92 | -29.18 | 8.0 | 8.0 | False |  | strong_accumulation | 0.11 | 1.35 | 2 | 2 | 3.77 | 1.85 | -17.87 | 17 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | -1.78 | -0.45 | -5.56 | -5.56 | 0.91 | 0.91 | False |  | mild_accumulation | -0.07 | 0.54 | 1 | 1 | -1.56 | -2.31 | -7.14 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | -2.09 | 2.19 | -1.58 | -6.5 | 10.32 | 10.32 | False |  | strong_accumulation | 0.09 | 0.03 | 2 | 2 | 2.37 | 1.15 | -6.5 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | 4.6 | 21.34 | 15.01 | 15.76 | 22.61 | 22.61 | False |  | strong_accumulation | 0.21 | 0.27 | 2 | 3 | 11.9 | 9.39 | -10.76 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | 1.42 | 14.92 | 31.34 | 41.09 | 29.55 | 41.79 | False |  | distribution_warning | -0.48 | -0.75 | 1 | 1 | 10.55 | 7.92 | -16.42 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround | B_可觀察 | 158.34377836365994 | -8.228649642919668 | 2.43 | 15.75 | -20.58 | 19.64 | 17.22 | 26.16 | False |  | mild_accumulation | -0.65 | 0.01 | 0 | 2 | 5.65 | 3.11 | -21.66 | 18 | selected |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | -4.39 | 10.76 | 23.5 | 18.69 | 31.38 | 31.38 | False |  | distribution_warning | -0.04 | -0.02 | 0 | 0 | -0.95 | 1.22 | -8.85 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -20.5 | -20.06 | 79.38 | 97.93 | 84.21 | 112.59 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -9.14 | -7.78 | 0 | 0 | -20.21 | -16.22 | -35.07 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | B_可觀察 | 153.16268341919277 | -7.777041541987246 | -1.06 | 10.63 | 0.36 | -1.17 | 11.51 | 11.51 | False |  | mild_accumulation | 0.34 | 0.58 | 2 | 1 | 2.57 | 1.85 | -8.47 | 20 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | 46.79 | 46.34 | 46.34 | 74.76 | 59.65 | 80.9 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.19 | 1.64 | 1 | 1 | 41.88 | 37.95 | 0.0 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 87447.70459081836 | 13923.213699202772 | 7.22 | 7.4 | -2.5 | 0.97 | 11.23 | 11.23 | False |  | strong_accumulation | 0.78 | 0.54 | 3 | 2 | 5.86 | 4.81 | -3.26 | 24 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | 16.81 | 19.83 | 27.52 | 43.3 | 33.65 | 50.92 | False |  | distribution_warning | -0.13 | -0.1 | 0 | 0 | 13.84 | 13.44 | -9.15 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 22.72 | 31.69 | 91.04 | 82.86 | 103.17 | 122.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.91 | -0.09 | 1 | 2 | 25.84 | 25.44 | -2.14 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 158.74753164663522 | 158.86577952131768 | 3.12 | 5.94 | 3.12 | -12.35 | 11.86 | 11.86 | False |  | mild_accumulation | -0.19 | 0.1 | 2 | 2 | 6.63 | 3.94 | -13.95 | 19 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -0.87 | 39.33 | 54.39 | 116.59 | 64.98 | 119.71 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.06 | -0.09 | 2 | 2 | 8.68 | 8.37 | -8.6 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -16.42 | -13.85 | 7.28 | 261.29 | 21.21 | 290.52 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.75 | -0.5 | 2 | 2 | -10.08 | -10.35 | -22.22 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -6.85 | 20.85 | 26.72 | 119.5 | 86.75 | 132.54 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.81 | 1.63 | 1 | 1 | 7.08 | 6.59 | -18.91 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -9.36 | -9.18 | 56.36 | 128.64 | 55.29 | 117.7 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.7 | -0.4 | 2 | 1 | -7.95 | -6.61 | -15.58 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | B_可觀察 | 129.27243852167018 | 65.0605772744456 | 4.97 | 10.19 | 15.52 | 48.61 | 21.39 | 58.46 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | 5.54 | 5.07 | -5.81 | 22 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -15.12 | -2.23 | 48.98 | 171.04 | 49.49 | 200.82 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.83 | 2 | 2 | -8.79 | -8.43 | -21.65 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 88.80451818624007 | 107.89432287557707 | -15.95 | -6.78 | 10.37 | 14.4 | 22.08 | 23.55 | False |  | strong_accumulation | 0.18 | 0.79 | 2 | 2 | -12.91 | -10.6 | -21.67 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | 1.51 | 4.26 | 46.67 | 125.67 | 57.49 | 133.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.88 | 0.8 | 0 | 2 | 1.32 | 1.28 | -11.51 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 94.38123673778152 | 82.59499806151248 | -0.67 | 20.92 | 28.03 | 25.0 | 34.3 | 42.31 | False |  | distribution_warning | -0.38 | -0.25 | 1 | 1 | 9.45 | 5.78 | -15.53 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | 0.49 | 10.4 | 88.7 | 239.67 | 96.34 | 247.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.13 | -0.92 | 0 | 0 | 2.65 | 4.3 | -9.58 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 88.0613471994038 | 34.31162647538102 | -12.17 | -12.86 | 29.84 | 5.12 | 32.19 | 53.5 | False |  | distribution_warning | -0.89 | -0.74 | 1 | 1 | -15.58 | -12.35 | -28.04 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 85.01370770897306 | 83.4020606995027 | 1.7 | 19.5 | 28.63 | 43.98 | 45.55 | 45.55 | False |  | strong_accumulation | 3.33 | 1.13 | 2 | 2 | 3.44 | 4.88 | -11.15 | 20 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 121.1993165447746 | 152.01807699959255 | 9.75 | 27.71 | 3.01 | 71.3 | 39.96 | 75.89 | True | 近20日漲幅>25%；近120日漲幅>70% | strong_accumulation | 4.03 | 3.79 | 2 | 2 | 15.53 | 13.45 | -5.74 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -10.88 | 9.15 | 25.23 | 109.88 | 71.28 | 120.06 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.33 | 2 | 2 | 2.21 | 1.71 | -21.02 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 22.33 | 30.43 | 42.86 | 51.99 | 47.89 | 58.29 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | 0.5 | 0.13 | 3 | 1 | 22.78 | 22.55 | 0.0 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | -0.68 | 5.35 | 17.2 | 27.0 | 40.19 | 45.22 | False |  | mild_accumulation | 0.03 | 0.94 | 1 | 2 | 3.8 | 4.68 | -2.93 | 20 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 6.57 | 8.4 | 1.43 | 6.17 | 12.7 | 22.68 | False |  | mild_accumulation | 0.07 | 0.0 | 3 | 0 | 6.23 | 4.53 | -5.65 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -18.32 | -13.1 | 2.46 | 61.33 | 40.05 | 73.81 | False |  | distribution_warning | -1.75 | -2.3 | 1 | 0 | -10.72 | -9.91 | -23.76 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | -6.4 | -4.06 | 19.69 | 53.5 | 28.18 | 61.58 | False |  | distribution_warning | -0.1 | -0.13 | 2 | 1 | -5.41 | -6.38 | -25.49 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | -14.24 | -1.81 | 30.86 | 37.5 | 50.3 | 58.29 | True | 距60日低點反彈>50% | mild_accumulation | 0.37 | 1.15 | 2 | 1 | -8.69 | -7.41 | -19.08 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -14.91 | -7.67 | 43.96 | 140.89 | 56.2 | 149.77 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.0 | -1.72 | 1 | 1 | -10.91 | -9.34 | -21.68 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | -2.46 | 41.25 | 51.83 | 80.22 | 57.62 | 81.54 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.03 | 3.24 | 2 | 2 | 6.4 | 5.97 | -7.71 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 4.13 | 5.58 | 3.06 | -4.42 | 7.97 | 7.97 | False |  | strong_accumulation | 0.32 | 0.05 | 3 | 2 | 4.11 | 3.51 | -0.44 |  | fail_low_response_condition |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.32956422871683 | 25.42926777280069 | 8.09 | 8.09 | 2.14 | 1.52 | 17.19 | 17.19 | False |  | strong_accumulation | 1.1 | 0.93 | 3 | 2 | 8.64 | 7.91 | -5.11 |  | fail_low_response_condition |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 9.43 | -1.56 | -18.93 | -26.25 | 10.25 | 10.25 | False |  | mild_accumulation | -0.06 | 0.96 | 1 | 3 | 1.69 | 1.05 | -20.4 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | 9.62 | 7.98 | -5.66 | -19.67 | 13.65 | 13.65 | False |  | mild_accumulation | -0.1 | 0.08 | 1 | 2 | 8.66 | 7.01 | -6.28 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 12.44 | 16.98 | 12.44 | 7.62 | 20.47 | 20.47 | False |  | strong_accumulation | 0.71 | 0.91 | 2 | 2 | 15.57 | 13.29 | -3.42 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 418.92924119579374 | 17.34399183311113 | 5.99 | 2.1 | -21.65 | -18.28 | 17.52 | 17.52 | False |  | distribution_warning | -0.42 | -0.78 | 0 | 0 | 5.19 | 2.96 | -22.51 | 11 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 2114.205326762877 | 1780.7414522786555 | 6.46 | 3.66 | 23.4 | 20.13 | 34.57 | 34.57 | False |  | strong_accumulation | 0.48 | 0.32 | 2 | 3 | 5.4 | 6.9 | -1.41 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | D_降級_TDCC轉弱 | 86.14284031322353 | 42.934476141944494 | -0.43 | 24.97 | -34.64 | -21.74 | 26.32 | 26.32 | False |  | distribution_warning | -0.14 | -0.33 | 1 | 1 | 5.57 | 2.7 | -36.76 | 12 | selected |
| 2547 | 日勝生 | 建材營造 | neutral |  | 69.90066780612314 | 22.241457982263142 | 10.89 | 10.55 | -2.65 | 0.92 | 12.13 | 12.13 | False |  | distribution_warning | -0.42 | -0.1 | 0 | 1 | 9.15 | 7.77 | -3.51 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral |  | 9203.558823529413 | 30000.69173757892 | -15.1 | -17.79 | -11.86 | 0.0 | 4.52 | 4.52 | False |  | distribution_warning | -5.18 | -5.03 | 0 | 1 | -11.39 | -10.09 | -21.51 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 5.6 | 24.75 | 58.07 | 105.66 | 66.07 | 113.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.1 | -0.36 | 1 | 0 | 11.28 | 9.49 | -14.88 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 9.2 | 10.1 | 4.89 | 21.13 | 16.06 | 22.24 | False |  | distribution_warning | -0.13 | -0.13 | 1 | 1 | 9.36 | 7.17 | -1.19 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | -9.34 | 7.62 | 24.93 | 7.37 | 36.66 | 36.66 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -0.86 | -3.46 | -21.94 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 52.80006873442736 | 30.333657817463656 | 7.89 | 14.33 | 31.37 | 40.9 | 38.72 | 47.9 | False |  | mild_accumulation | -0.25 | 0.18 | 2 | 2 | 8.21 | 9.12 | 0.0 | 17 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 6.88 | 9.09 | 22.79 | 32.0 | 34.01 | 37.5 | False |  | distribution_warning | -0.01 | -2.16 | 2 | 0 | 3.67 | 5.56 | -7.04 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | -18.2 | -18.53 | 5.14 | 148.48 | 39.12 | 164.21 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.73 | -8.07 | 1 | 1 | -14.39 | -11.49 | -25.23 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -16.16 | -4.89 | 22.57 | 65.6 | 27.25 | 84.58 | True | 距120日低點反彈>80% | distribution_warning | -0.52 | -1.21 | 0 | 1 | -9.9 | -10.18 | -22.43 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 92.4008479108611 | 7.500180953989433 | 13.57 | 28.08 | 39.03 | 30.41 | 42.95 | 55.6 | True | 近20日漲幅>25% | strong_accumulation | 2.25 | 2.76 | 3 | 3 | 16.62 | 15.58 | -1.26 |  | fail_low_response_condition |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -3.86 | 15.59 | 14.26 | 25.36 | 24.91 | 30.28 | False |  | mild_accumulation | -2.29 | 2.4 | 1 | 1 | -1.59 | -0.53 | -18.0 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -8.51 | -5.72 | 31.1 | 85.5 | 52.99 | 100.0 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.18 | 0.07 | 0 | 1 | -9.11 | -6.28 | -15.97 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 152.69225498874076 | 103.50094623545084 | -19.13 | -13.89 | -6.81 | 53.97 | 18.02 | 73.51 | False |  | distribution_warning | -0.34 | -0.37 | 1 | 1 | -18.1 | -15.14 | -24.51 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -5.46 | 4.75 | 2.32 | -6.19 | 14.39 | 14.39 | False |  | strong_accumulation | 2.3 | 1.22 | 2 | 2 | -4.88 | -3.75 | -12.14 | 19 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | 9.65 | 33.69 | 89.16 | 78.78 | 121.57 | 121.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.48 | -2.59 | 1 | 1 | 7.7 | 14.28 | -8.42 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -1.9 | 0.9 | -23.02 | 181.76 | 14.87 | 181.17 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.58 | -0.03 | 0 | 0 | -3.55 | -5.25 | -30.0 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -22.95 | -10.65 | 62.87 | 187.2 | 93.0 | 214.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.74 | 0.67 | 1 | 2 | -14.57 | -12.0 | -27.44 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | 7.76 | 15.24 | 155.89 | 261.19 | 178.62 | 321.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.2 | 2.05 | 2 | 2 | 2.79 | 3.7 | -10.84 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -21.78 | 17.06 | 130.0 | 104.57 | 140.4 | 140.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -3.58 | -3.74 | -21.78 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 71.36506452239956 | 62.24907879043217 | -16.42 | 1.08 | 29.63 | 42.28 | 42.71 | 47.21 | False |  | strong_accumulation | 2.72 | 4.71 | 2 | 3 | -8.06 | -5.44 | -17.4 | 17 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | -7.07 | 4.91 | 12.13 | 14.77 | 21.28 | 28.09 | False |  | strong_accumulation | 0.03 | 0.14 | 2 | 2 | -4.87 | -3.48 | -12.76 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | 3.46 | 2.1 | 16.47 | 36.01 | 24.28 | 43.01 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.26 | 2.44 | -16.7 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -11.82 | -15.27 | 79.26 | 94.09 | 91.82 | 108.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.13 | -3.21 | 1 | 1 | -13.85 | -11.14 | -31.01 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -9.3 | 35.1 | 83.96 | 67.62 | 91.49 | 92.43 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 4.9 | 0.13 | 2 | 1 | 8.31 | 6.29 | -17.89 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -7.81 | 1.22 | -0.4 | 37.78 | 20.39 | 47.44 | False |  | strong_accumulation | 2.33 | 0.82 | 2 | 3 | -2.75 | -3.25 | -17.88 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | -8.44 | -1.36 | 20.56 | 65.4 | 25.43 | 91.7 | True | 距120日低點反彈>80% | distribution_warning | -0.48 | -0.52 | 1 | 0 | -7.66 | -5.37 | -14.9 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.11391792521879 | 34.318355180717255 | -8.79 | -5.14 | 5.06 | 43.1 | 4.4 | 50.91 | False |  | distribution_warning | -3.31 | -3.83 | 1 | 1 | -3.88 | -4.73 | -18.43 | 13 | selected |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 7.18 | 9.09 | -7.69 | -18.07 | 9.87 | 9.87 | False |  | mild_accumulation | 0.06 | 1.24 | 1 | 3 | 6.49 | 5.24 | -11.18 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 140.95338036510228 | 121.41758390187826 | 13.3 | 28.25 | 57.93 | 62.93 | 64.89 | 100.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 3.38 | 6.0 | 2 | 3 | 17.3 | 16.39 | -4.26 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -3.78 | 69.13 | 83.49 | 125.84 | 115.23 | 125.39 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 8.74 | 9.29 | 1 | 2 | 9.27 | 12.01 | -10.2 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | -2.89 | 1.2 | -15.15 | 21.74 | 12.0 | 28.24 | False |  | mild_accumulation | 0.4 | -0.01 | 3 | 1 | -2.11 | -2.1 | -19.23 | 22 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -3.23 | -3.75 | -24.77 | -36.24 | 5.76 | 5.76 | False |  | distribution_warning | -0.12 | 0.0 | 0 | 0 | -0.18 | -1.71 | -25.08 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -3.98 | 0.54 | 23.61 | 95.42 | 39.8 | 113.46 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.1 | 4.09 | 1 | 1 | 0.29 | -0.54 | -14.09 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 18.63 | 27.76 | 39.42 | 40.96 | 40.96 | 48.64 | True | 近20日漲幅>25% | mild_accumulation | 0.92 | 0.0 | 3 | 1 | 21.83 | 18.94 | -0.52 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 69.95652184172461 | 55.27975193155594 | -4.44 | 10.95 | 7.36 | 3.86 | 14.95 | 14.95 | False |  | strong_accumulation | 2.51 | 2.65 | 2 | 2 | 0.33 | 0.06 | -8.89 | 20 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -7.28 | 22.41 | 24.56 | 23.33 | 36.16 | 51.76 | False |  | distribution_warning | -0.21 | -0.23 | 1 | 0 | 2.83 | 2.57 | -15.62 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | 5.95 | 5.95 | -0.44 | 6.61 | 6.78 | 13.02 | False |  | mild_accumulation | -0.05 | 0.02 | 1 | 1 | 4.55 | 4.27 | -2.87 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | 7.82 | 13.15 | 14.94 | 33.33 | 17.47 | 34.45 | False |  | strong_accumulation | 0.28 | 0.39 | 2 | 3 | 10.32 | 9.46 | -4.65 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 1.38 | -2.43 | -11.6 | -22.05 | 8.07 | 8.07 | False |  | strong_accumulation | 0.05 | 0.03 | 2 | 2 | 1.55 | -0.07 | -17.54 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.36 | 0.72 | -2.1 | -2.44 | 2.56 | 2.56 | False |  | mild_accumulation | 0.49 | 0.0 | 3 | 1 | 0.52 | -0.03 | -5.72 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 9.77 | 7.47 | 3.4 | 6.36 | 12.79 | 12.79 | False |  | distribution_warning | -1.0 | -1.19 | 0 | 0 | 8.8 | 7.86 | -3.76 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth | A_優先追蹤 | 103.2633463252738 | 75.2296518472431 | -5.79 | 5.63 | 26.21 | 48.93 | 42.69 | 53.3 | False |  | mild_accumulation | 0.13 | -0.61 | 1 | 1 | -5.71 | -4.01 | -14.19 | 20 | selected |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 78.63452035793752 | 28.54441429888791 | -2.65 | -0.68 | -23.64 | 62.79 | 9.7 | 68.0 | False |  | strong_accumulation | 1.13 | 0.67 | 2 | 2 | -4.55 | -4.14 | -31.47 | 18 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -4.12 | 14.29 | 106.12 | 95.72 | 125.75 | 125.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.47 | -0.26 | 3 | 1 | 0.55 | 5.24 | -11.72 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | 8.72 | 3.95 | -1.46 | 0.42 | 14.08 | 14.08 | False |  | distribution_warning | -0.66 | -1.27 | 1 | 0 | 8.1 | 6.81 | -5.58 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -1.75 | 24.91 | 79.04 | 112.66 | 87.71 | 115.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.06 | -0.55 | 2 | 1 | 5.57 | 6.47 | -4.73 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -6.15 | 18.36 | 51.05 | 39.37 | 64.52 | 64.52 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -2.94 | -3.8 | 1 | 2 | -2.93 | 0.3 | -12.76 |  | fail_already_priced_in |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | -5.52 | -34.09 | 4.29 | 36.69 | 34.69 | 43.48 | False |  | mild_accumulation | 1.07 | 4.5 | 1 | 1 | -8.65 | -5.52 | -34.09 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -8.41 | 24.79 | 135.48 | 182.4 | 152.6 | 194.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.02 | 1.16 | 2 | 2 | 3.61 | 4.82 | -18.07 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -26.78 | -23.63 | 13.99 | 146.53 | 43.75 | 148.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.18 | -2.69 | 2 | 1 | -24.33 | -21.5 | -33.5 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth | A_優先追蹤 | 116.02033931403636 | 34.238557659078786 | -3.45 | 4.6 | 8.01 | 51.67 | 7.69 | 64.71 | False |  | mild_accumulation | 2.01 | -0.06 | 2 | 1 | -5.16 | -6.52 | -26.02 | 19 | selected |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | -2.91 | 13.08 | 42.16 | 82.42 | 61.59 | 100.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.36 | 0.85 | 2 | 2 | 7.12 | 8.55 | -5.47 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | 0.17 | -10.84 | 31.72 | 225.98 | 32.83 | 242.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.18 | -0.41 | 0 | 1 | -1.96 | -2.08 | -24.11 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -20.89 | -17.59 | 53.45 | 118.14 | 102.5 | 138.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.9 | -6.45 | 1 | 0 | -15.37 | -12.84 | -31.8 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -7.25 | 0.13 | -8.79 | -39.34 | 2.95 | 2.95 | False |  | mild_accumulation | 0.39 | -0.06 | 3 | 0 | -2.07 | -3.38 | -12.73 |  | fail_low_response_condition |
| 6550 | 北極星藥業-KY | 生技醫療業 | defensive_or_traditional |  | 248.65366759517173 | 233.5268264366863 | 2.67 | -20.41 | -43.61 | -53.86 | 5.08 | 5.08 | False |  | strong_accumulation | 0.44 | 1.52 | 2 | 3 | -8.47 | -9.22 | -42.52 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional | D_降級_TDCC轉弱 | 56.34771899764404 | 43.25386406944739 | -0.34 | -1.68 | -23.61 | -41.92 | 9.22 | 9.22 | False |  | distribution_warning | -0.66 | -0.84 | 1 | 1 | 1.41 | -0.32 | -28.11 | 7 | fail_score_lt_8 |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 1.24 | 0.62 | -0.41 | 15.02 | 14.22 | 19.51 | False |  | mild_accumulation | -0.74 | 0.99 | 1 | 1 | 0.01 | 1.13 | -5.22 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.0 | 0.25 | -7.94 | -19.52 | 4.3 | 4.3 | False |  | distribution_warning | -0.18 | -0.16 | 0 | 0 | 1.41 | 0.41 | -9.19 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 82.35699071961052 | 76.07474411222435 | -1.7 | 1.43 | 4.77 | 14.98 | 14.77 | 17.31 | False |  | mild_accumulation | -1.21 | 0.08 | 1 | 1 | -0.23 | -0.64 | -8.48 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth |  | 58.86220189113607 | 31.41858931023004 | -25.98 | 2.55 | -10.18 | 82.44 | 26.27 | 94.56 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 8.05 | 8.26 | 2 | 2 | -12.16 | -12.12 | -31.85 |  | fail_low_response_condition |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | -0.83 | 4.94 | -6.3 | 21.18 | 6.82 | 22.81 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.92 | 0.48 | -21.19 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | -0.65 | 52.39 | 123.36 | 173.21 | 157.14 | 193.1 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.59 | -0.09 | 2 | 1 | 7.32 | 13.37 | -10.0 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -23.36 | -32.71 | 92.7 | 417.04 | 143.78 | 437.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.11 | 0.74 | 0 | 2 | -26.38 | -20.71 | -38.06 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -14.66 | -11.87 | 3.17 | -15.05 | 8.39 | 8.89 | False |  | mild_accumulation | 0.04 | 0.01 | 2 | 1 | -13.3 | -11.86 | -22.39 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 22.05 | 15.47 | 11.07 | 0.0 | 33.2 | 33.2 | False |  | distribution_warning | -0.22 | -0.31 | 0 | 1 | 18.78 | 16.99 | -2.73 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | -3.72 | 64.03 | 395.22 | 1258.08 | 409.84 | 1307.24 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.59 | 4.37 | 2 | 2 | 12.46 | 15.51 | -14.09 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | 1.6 | 3.25 | 7.17 | 0.79 | 18.14 | 19.81 | False |  | mild_accumulation | 2.05 | 0.01 | 2 | 1 | 1.42 | 1.12 | -15.33 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -5.25 | 3.84 | 48.92 | 54.38 | 61.79 | 63.54 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.83 | 0.0 | 0 | 0 | -0.27 | -0.45 | -18.49 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -1.74 | 2.42 | -15.5 | 0.3 | 7.64 | 22.46 | False |  | distribution_warning | -1.38 | -0.96 | 1 | 1 | -3.5 | -4.05 | -17.76 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 73.6849472054308 | 64.05199366520502 | 1.8 | 4.1 | 28.45 | 18.97 | 46.19 | 46.19 | False |  | distribution_warning | -1.96 | -0.01 | 0 | 0 | 0.9 | 3.21 | -9.29 | 11 | selected |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 88.25510096241669 | 69.4277284799705 | -7.11 | -18.2 | 52.55 | 166.92 | 70.61 | 171.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.86 | -3.23 | 1 | 0 | -12.11 | -10.6 | -31.92 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 83.64462145795709 | 87.84549623036372 | -6.12 | 2.32 | 66.78 | 137.14 | 104.49 | 137.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.49 | -1.86 | 1 | 0 | -6.47 | -2.32 | -16.66 |  | fail_low_response_condition |
| 7803 | 雲象科技-創 | 生技醫療業 | defensive_or_traditional |  | 1440.6307977736549 | 2.7893555626803463 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |