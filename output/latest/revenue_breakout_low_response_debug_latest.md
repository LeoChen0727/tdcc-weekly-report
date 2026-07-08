# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-08 19:54:57 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 620392 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 297 |
| low_response_pass | 83 |
| already_priced_in_excluded | 36 |
| overheat_pass | 47 |
| score_pass | 47 |
| theme_priority_pass | 35 |
| final_rows | 35 |

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
| fail_low_response_condition | 214 |
| fail_already_priced_in | 36 |
| fail_defensive_or_traditional_excluded | 10 |
| missing_or_insufficient_price_metrics | 3 |
| fail_mainstream_score_lt_10 | 1 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | -0.48 | -0.96 | -13.75 | -29.11 | 3.5 | 3.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | -2.66 | -1.98 | -14.46 | 19 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 0.92 | 0.46 | -5.98 | -6.78 | 2.8 | 2.8 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | -0.05 | -0.59 | -7.56 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 3.1 | -2.66 | -2.4 | -7.58 | 7.96 | 7.96 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 0.32 | 0.23 | -9.18 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 98.71730241416007 | 44.35003336829059 | -0.71 | -14.68 | -3.13 | 23.45 | 15.77 | 38.12 | False |  | distribution_warning | -0.77 | -1.61 | 0 | 0 | -2.86 | -1.79 | -16.96 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | 0.22 | -1.11 | -7.45 | 15.21 | 13.16 | 13.16 | False |  | mild_accumulation | -0.2 | 0.64 | 1 | 1 | -1.36 | -1.0 | -13.37 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 1.68 | -5.45 | 16.48 | 14.83 | 20.93 | 25.52 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | -2.19 | -1.85 | -12.92 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -1.75 | -12.19 | 19.57 | 92.99 | 37.07 | 108.15 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | -4.24 | 3 | 0 | -5.45 | -7.44 | -36.43 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.61 | -9.8 | 3.71 | -1.22 | 6.86 | 7.14 | False |  | distribution_warning | -0.34 | -0.57 | 1 | 1 | -2.54 | -2.09 | -12.9 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | -8.03 | 27.7 | 84.32 | 98.32 | 96.78 | 101.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | -3.55 | 1.08 | -29.0 |  | fail_already_priced_in |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | 10.85 | 4.23 | -10.66 | -28.38 | 15.11 | 15.11 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 0 | 7.53 | 6.3 | -13.43 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | 0.33 | -2.91 | 0.0 | -16.41 | 7.13 | 7.13 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -2.9 | -1.54 | -9.35 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 562.3794928949568 | 152.7873314363479 | -8.71 | -21.24 | -1.63 | 2.12 | 12.62 | 16.43 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -11.66 | -8.9 | -23.97 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 5.75 | 19.13 | 122.39 | 144.19 | 131.62 | 181.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 11.08 | 13.66 | -5.43 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | 0.0 | -21.69 | -20.0 |  | 3.14 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -10.32 | -8.57 | -28.5 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 158.74753164663522 | 158.86577952131768 | 8.01 | 3.85 | -5.47 | -9.65 | 14.24 | 14.24 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 3.44 | 3.68 | -6.39 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -7.5 | 52.83 | 98.59 | 211.06 | 132.78 | 200.43 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 2.79 | 4.78 | -17.58 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -3.48 | -4.81 | 5.73 | 137.56 | 17.37 | 136.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -10.6 | -9.29 | -27.86 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -11.32 | 7.67 | 91.91 | 72.29 | 101.07 | 101.07 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -12.23 | -8.05 | -27.84 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -9.21 | -2.42 | 16.67 | 98.77 | 21.05 | 121.56 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | -2.45 | -3.27 | -14.51 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | -4.81 | -2.09 | 6.2 | 39.44 | 12.64 | 40.98 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | -3.34 | -2.32 | -9.36 | 25 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -18.28 | -22.38 | -17.74 | 100.98 | 3.63 | 101.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -15.23 | -15.54 | -33.63 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.80451818624007 | 107.89432287557707 | -8.84 | 14.92 | 23.16 | 37.3 | 30.86 | 46.77 | False |  | mild_accumulation | 2.17 | 2.99 | 1 | 2 | 1.9 | 0.57 | -11.96 | 19 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -5.74 | -23.08 | -2.13 | 80.53 | 3.6 | 93.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -9.61 | -8.64 | -27.22 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 1.34 | 0.53 | 16.72 | 33.22 | 30.68 | 40.41 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 1.36 | 2.22 | -13.93 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -3.97 | 4.94 | 39.87 | 239.62 | 42.88 | 244.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | -1.5 | -0.72 | -14.96 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | 4.5 | 11.9 | 13.78 | 48.6 | 19.65 | 73.6 | False |  | strong_accumulation | 2.08 | 2.37 | 2 | 2 | 2.23 | 1.76 | -18.62 | 21 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 85.01370770897306 | 83.4020606995027 | -7.69 | 0.84 | 17.07 | 20.72 | 26.98 | 46.16 | False |  | strong_accumulation | 1.5 | 0.92 | 2 | 2 | -7.05 | -5.44 | -17.24 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 121.1993165447746 | 152.01807699959255 | -2.86 | 11.57 | 15.02 | 53.14 | 38.72 | 47.36 | False |  | distribution_warning | -3.53 | -3.16 | 1 | 1 | 3.44 | 3.52 | -15.02 | 15 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -5.94 | 9.09 | 88.57 | 82.07 | 98.99 | 99.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | -6.33 | -3.19 | -21.58 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 3.38 | 7.38 | 34.88 | 49.75 | 36.38 | 52.18 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 0.57 | 3.45 | -6.0 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | -8.96 | 15.6 | 31.29 | 31.95 | 39.61 | 57.97 | False |  | mild_accumulation | 1.29 | -0.26 | 2 | 2 | -0.7 | 0.16 | -14.73 | 19 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | 0.0 | -0.7 | 0.0 | 14.55 | 12.5 | 22.46 | False |  | distribution_warning | -0.1 | 0.0 | 2 | 0 | -0.44 | 0.33 | -11.27 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -0.2 | -18.3 | 1.42 | 3.52 | 4.17 | 30.55 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -12.21 | -11.9 | -34.73 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.83340834565679 | 63.183650278464505 | 2.36 | 18.27 | 0.27 | 57.36 | 27.02 | 81.33 | True | 距120日低點反彈>80% | distribution_warning | -0.06 | -1.16 | 1 | 0 | 2.93 | 2.77 | -12.14 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 14.01 | 0.99 | 34.77 | 39.38 | 32.36 | 69.76 | False |  | distribution_warning | -0.29 | 0.0 | 2 | 1 | 6.64 | 6.07 | -13.22 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -14.55 | -3.83 | 0.36 | 113.13 | 13.81 | 139.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | -6.67 | -7.99 | -20.23 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 87.19923905471303 | 44.102711379154506 | 2.81 | 1.59 | 19.49 | 60.0 | 47.76 | 81.24 | True | 距120日低點反彈>80% | distribution_warning | -3.39 | -1.69 | 0 | 1 | 0.21 | 1.53 | -5.71 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 2.06 | -0.56 | -0.89 | -1.87 | 5.83 | 5.83 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.12 | 0.42 | -2.73 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_僅留完整清單 | 57.09899455038421 | 42.50276733448348 | 6.77 | 11.81 | 2.53 | 7.17 | 17.36 | 17.36 | False |  | strong_accumulation | 0.69 | 0.7 | 3 | 2 | 6.39 | 5.59 | -7.19 | 14 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 1.9 | 7.87 | 12.56 | 6.72 | 22.63 | 22.63 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 0.78 | 2.76 | -6.43 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | -1.12 | 3.26 | -7.9 | -28.55 | 10.75 | 10.75 | False |  | strong_accumulation | 0.15 | 0.52 | 2 | 3 | 0.53 | 0.6 | -7.71 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -9.11 | -8.89 | -15.21 | -25.25 | 0.53 | 0.53 | False |  | distribution_warning | -1.6 | -1.07 | 0 | 1 | -10.55 | -8.83 | -15.59 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 128.48525684217282 | 290.35375415914626 | 1.85 | 8.91 | 6.28 | -5.98 | 17.27 | 17.27 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | -1.81 | 0.95 | -11.29 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | -0.25 | 6.1 | -16.17 | -18.78 | 18.28 | 18.28 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 0.1 | 0.67 | -16.61 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2114.205326762877 | 1780.7414522786555 | 2.72 | 0.69 | 24.46 | 9.02 | 29.08 | 29.08 | False |  | distribution_warning | -0.74 | -0.81 | 1 | 1 | -1.01 | 0.1 | -7.64 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | 1.04 | -20.86 | -32.81 | -38.96 | 4.45 | 4.45 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -7.68 | -6.49 | -33.51 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 0.0 | 1.81 | 3.69 | 4.17 | 14.68 | 14.68 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 1.15 | 2.13 | -4.66 | 19 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -1.47 | -0.99 | -22.69 | -12.99 | 1.01 | 1.01 | False |  | distribution_warning | -1.46 | -1.04 | 1 | 1 | -2.43 | -3.91 | -24.15 | 12 | selected |
| 2838 | 聯邦銀 | 金融保險業 | defensive_or_traditional |  | 61.12684035593818 | 32.1840567542641 | 9.29 | 13.3 | 18.18 | 30.69 | 24.43 | 35.34 | False |  | distribution_warning | -0.02 | -0.08 | 1 | 1 | 9.01 | 9.3 | -0.8 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 0.2 | -6.67 | 55.32 | 90.19 | 54.6 | 90.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | -1.04 | 0.34 | -15.72 |  | fail_already_priced_in |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 72.52927583818101 | 37.88073490992248 | 8.17 | 11.99 | 9.82 | 24.65 | 34.12 | 34.12 | False |  | strong_accumulation | 0.24 | 0.31 | 3 | 3 | 6.18 | 7.52 | 0.0 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 155.02666088498714 | 258.385032023246 | 2.86 | 0.8 | 43.18 | 31.94 | 44.5 | 50.9 | True | 近60日漲幅>40% | distribution_warning | -0.1 | -0.13 | 0 | 0 | -2.14 | 1.66 | -10.64 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 8.48 | 5.68 | 46.54 | 75.93 | 53.12 | 75.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.33 | -0.55 | 1 | 1 | 4.72 | 7.96 | -1.6 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 928.42236221935 | 167.93120445448935 | 8.33 | 10.34 | 42.43 | 75.25 | 43.57 | 78.3 | True | 近60日漲幅>40%；近120日漲幅>70% | distribution_warning | -0.11 | -0.18 | 1 | 1 | 7.58 | 8.62 | -0.56 |  | fail_low_response_condition |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 7.5 | 21.32 | 47.53 | 71.94 | 56.89 | 72.36 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.69 | 0.78 | 3 | 3 | 10.62 | 12.7 | -0.42 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 4.75 | 22.34 | 28.13 | 43.49 | 46.25 | 48.85 | False |  | strong_accumulation | 0.59 | 0.62 | 3 | 3 | 9.13 | 10.31 | -0.24 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | 5.34 | 31.19 | 2.14 | 44.08 | 44.44 | 67.74 | True | 近20日漲幅>25% | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 12.13 | 10.99 | -4.19 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.80006873442736 | 30.333657817463656 | 1.06 | 3.74 | 21.53 | 44.47 | 27.83 | 45.1 | False |  | strong_accumulation | 0.61 | 0.58 | 3 | 3 | 0.0 | 1.53 | -6.59 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 56.16201695665634 | 32.12627399775476 | 5.82 | 8.18 | 28.76 | 31.08 | 31.67 | 47.72 | False |  | strong_accumulation | 1.66 | 2.35 | 2 | 3 | 6.57 | 6.42 | -10.74 | 17 | selected |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 296.8056658653291 | 223.4596397756601 | 1.17 | 0.47 | 40.85 | 58.46 | 46.6 | 63.26 | True | 近60日漲幅>40% | strong_accumulation | 0.2 | 1.06 | 2 | 2 | -4.03 | -4.02 | -21.21 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -11.26 | -8.64 | -3.12 | 69.09 | 4.73 | 83.79 | True | 距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | -5.43 | -7.42 | -22.76 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 92.4008479108611 | 7.500180953989433 | 13.75 | 8.52 | 36.67 | 44.85 | 42.66 | 70.22 | False |  | distribution_warning | -1.06 | -0.7 | 2 | 2 | 11.07 | 12.52 | -1.46 |  | fail_low_response_condition |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -8.57 | -15.79 | -5.74 | -14.25 | 6.29 | 13.64 | False |  | mild_accumulation | 1.34 | -0.37 | 2 | 0 | -11.33 | -10.41 | -28.47 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -8.29 | -4.76 | 17.99 | 90.73 | 25.17 | 87.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | -5.36 | -6.14 | -16.08 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | -0.24 | -15.8 | -8.48 | 43.69 | 6.85 | 47.2 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -4.45 | -7.48 | -31.66 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -4.82 | 12.68 | 17.92 | 7.68 | 20.05 | 25.71 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | -3.96 | -2.8 | -18.0 | 18 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -9.44 | -16.9 | 51.21 | 41.84 | 63.46 | 75.78 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -12.25 | -9.34 | -27.35 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | 0.99 | -13.19 | -19.15 | 99.67 | 3.03 | 114.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -5.61 | -5.98 | -27.06 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | 2.69 | -20.79 | 44.12 | 81.48 | 51.77 | 71.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -2.8 | -1.3 | 0 | 0 | -8.93 | -10.01 | -35.53 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -3.8 | -14.83 | 18.25 | 267.35 | 32.35 | 302.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | -1.14 | -1.76 | -20.2 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -8.84 | -16.7 | 22.64 | 65.86 | 11.56 | 112.71 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -13.02 | -11.97 | -30.79 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 4.18 | 5.95 | 16.87 | 25.93 | 24.67 | 40.07 | False |  | strong_accumulation | 0.5 | 0.46 | 2 | 2 | 6.27 | 5.15 | -4.59 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | -0.82 | -2.96 | 11.08 | 28.93 | 12.11 | 28.93 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.85 | -2.01 | -22.7 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -12.78 | 2.09 | 35.18 | 86.05 | 27.54 | 105.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -6.36 | -6.45 | -26.05 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -1.84 | -27.67 | 33.06 | 42.94 | 34.73 | 58.22 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -10.59 | -8.35 | -32.49 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -9.09 | -21.93 | -12.86 | 11.11 | 1.45 | 24.56 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -12.57 | -11.57 | -30.46 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 82.90674676519687 | 39.84386199206386 | -4.09 | -4.52 | 6.78 | 64.33 | 13.44 | 70.16 | False |  | distribution_warning | -0.54 | -1.12 | 1 | 0 | -2.43 | -3.37 | -17.25 | 14 | selected |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.11391792521879 | 34.318355180717255 | -11.92 | -13.18 | -23.48 | 8.6 | 3.77 | 17.44 | False |  | strong_accumulation | 4.42 | 4.81 | 2 | 2 | -11.48 | -10.95 | -24.25 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 0.86 | 0.28 | -4.59 | -11.53 | 5.06 | 5.06 | False |  | strong_accumulation | 0.23 | 0.11 | 2 | 2 | 0.94 | 0.79 | -4.59 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 1.94 | -3.5 | -7.06 | -20.25 | 3.95 | 3.95 | False |  | distribution_warning | -0.24 | -0.56 | 2 | 0 | -3.48 | -2.11 | -15.97 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 140.95338036510228 | 121.41758390187826 | -1.35 | -15.38 | 21.68 | 61.53 | 33.66 | 78.28 | False |  | distribution_warning | -3.16 | -5.47 | 1 | 0 | -5.76 | -2.84 | -18.22 | 12 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | -1.33 | -7.11 | 63.72 | 90.72 | 83.77 | 108.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 5.31 | 4.61 | -12.94 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 281.10296953335904 | 153.94170544805627 | -2.82 | 6.17 | 2.38 | 22.42 | 15.44 | 22.42 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | -1.19 | -1.02 | -13.13 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -8.22 | -7.03 | -21.46 | -30.92 | 1.18 | 1.18 | False |  | distribution_warning | -0.35 | 0.0 | 0 | 0 | -4.42 | -4.53 | -22.87 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 112.585794273422 | 77.27049729091536 | -6.99 | -18.53 | 6.15 | 15.63 | 9.13 | 36.66 | False |  | mild_accumulation | -1.13 | 0.33 | 1 | 2 | -12.69 | -12.02 | -27.86 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 4.2 | 5.68 | 16.98 | 27.4 | 28.28 | 43.08 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 1.03 | 3.58 | -7.92 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 4.4 | -2.12 | 1.09 | 5.86 | 9.06 | 10.95 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | 1.08 | 0.84 | -12.06 | 15 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -0.22 | -18.01 | 15.59 | 11.57 | 22.88 | 36.95 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | -4.5 | -4.65 | -23.85 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral |  | 88.65151498619764 | -2.528158661804875 | -0.87 | 5.39 | 3.64 | 2.55 | 8.92 | 14.19 | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | -0.14 | 0.77 | -3.39 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -0.93 | -15.79 | -8.18 | -15.01 | 1.27 | 1.27 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -9.03 | -6.64 | -23.72 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 0.93 | 1.16 | -13.66 | -22.0 | 6.6 | 6.6 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.52 | -0.25 | -13.49 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 0.71 | 2.55 | -3.75 | -1.05 | 3.3 | 3.3 | False |  | strong_accumulation | 0.31 | 0.42 | 3 | 3 | 0.37 | 0.39 | -3.75 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 0.25 | 1.93 | 0.25 | -7.91 | 8.94 | 8.94 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | -1.63 | 0.02 | -9.49 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -5.04 | 15.62 | 19.78 | 44.09 | 32.21 | 81.36 | True | 距120日低點反彈>80% | strong_accumulation | 1.8 | 1.98 | 2 | 2 | 1.11 | 0.87 | -12.26 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | 1.14 | -12.17 | -23.28 | 30.24 | 2.69 | 30.24 | False |  | strong_accumulation | 0.68 | 0.05 | 2 | 2 | -4.32 | -4.62 | -23.05 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | 4.63 | -1.45 | 83.6 | 123.97 | 86.9 | 138.98 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.49 | 0.47 | 0 | 2 | -2.82 | 0.04 | -17.88 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral |  | 149.18224366317995 | 540.6620723440313 | -1.85 | 0.56 | -1.2 | -16.61 | 8.78 | 8.78 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -2.54 | -1.1 | -12.57 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | -4.38 | 5.0 | 52.09 | 97.83 | 50.62 | 117.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | -0.89 | 0.68 | -8.7 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 70.65666417439758 | 55.92683953560652 | -1.26 | -11.14 | 25.93 | 32.54 | 32.77 | 62.24 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -7.92 | -5.15 | -25.17 | 11 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 3.84 | -3.77 | 20.73 | 36.5 | 34.11 | 42.86 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.35 | 1.01 | -34.38 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -8.78 | -25.1 | 47.74 | 80.9 | 56.98 | 87.83 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.95 | 0.74 | 1 | 2 | -15.39 | -14.67 | -39.39 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -0.26 | -18.18 | -16.74 | 112.12 | 6.48 | 117.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -5.2 | -8.11 | -35.71 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -5.71 | -29.29 | -31.09 | 6.07 | 3.12 | 23.75 | False |  | mild_accumulation | -2.38 | 0.82 | 0 | 2 | -16.09 | -15.07 | -39.63 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 12.5 | 54.55 | 134.3 | 198.83 | 164.71 | 200.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 28.51 | 26.33 | -2.55 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -13.33 | -10.51 | -25.23 | 120.77 | 3.49 | 126.62 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -14.27 | -12.82 | -32.94 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -3.64 | -3.84 | 43.79 | 92.92 | 41.16 | 136.53 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -5.1 | -5.63 | -29.04 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | -0.12 | -1.82 | -1.22 | -23.15 | 8.58 | 8.58 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | -0.64 | -0.6 | -11.18 |  | fail_low_response_condition |
| 6550 | 北極星藥業-KY | 生技醫療業 | defensive_or_traditional |  | 248.65366759517173 | 233.5268264366863 | 0.0 | 1.9 | -28.72 | -55.92 | 7.2 | 7.2 | False |  | distribution_warning | -0.04 | -0.13 | 1 | 1 | 0.7 | -1.41 | -33.33 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 56.34771899764404 | 43.25386406944739 | 1.86 | 9.78 | -2.37 | -21.71 | 23.04 | 23.04 | False |  | mild_accumulation | -0.03 | 0.59 | 1 | 2 | 4.7 | 4.26 | -7.84 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 1.11 | -9.0 | -0.22 | -1.73 | 6.06 | 6.06 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | -3.4 | -2.87 | -11.99 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.63 | 0.13 | -2.56 | -19.05 | 4.17 | 4.17 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | -0.39 | -0.18 | -8.37 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | -4.67 | 12.24 | 8.5 | 22.64 | 21.19 | 28.83 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | -2.46 | -1.3 | -14.27 | 19 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 58.86220189113607 | 31.41858931023004 | -4.17 | -0.42 | 35.36 | 49.89 | 39.61 | 48.33 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -4.24 | -4.39 | -24.66 | 18 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | 3.36 | -9.79 | -8.14 | -7.06 | 4.34 | 10.6 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -2.55 | -2.06 | -11.09 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | -0.39 | 68.67 | 239.14 | 323.79 | 276.49 | 384.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 15.98 | 17.19 | -9.64 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -8.04 | -15.48 | 84.21 | 354.89 | 88.89 | 386.11 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.0 | 3 | 0 | -9.49 | -11.37 | -39.29 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | 1.2 | -10.72 | -6.67 | -22.03 | 2.67 | 6.7 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -1.5 | -3.13 | -23.95 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 14.09 | 31.56 | 45.17 | 24.19 | 74.69 | 74.69 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 19.38 | 20.33 | 0.0 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 2.26 | 29.77 | 289.5 | 1388.02 | 369.75 | 1443.48 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 13.63 | 15.88 | -4.05 |  | fail_low_response_condition |