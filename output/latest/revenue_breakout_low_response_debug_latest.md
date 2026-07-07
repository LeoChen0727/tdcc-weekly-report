# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-07 23:38:38 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1966 |
| standardized_revenue_rows | 1966 |
| price_rows | 618429 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 296 |
| low_response_pass | 104 |
| already_priced_in_excluded | 43 |
| overheat_pass | 61 |
| score_pass | 61 |
| theme_priority_pass | 46 |
| final_rows | 46 |

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
| fail_low_response_condition | 192 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 14 |
| missing_or_insufficient_price_metrics | 4 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 152.96178992534956 | 138.94580810199872 | -0.96 | -0.96 | -15.16 | -30.3 | 3.5 | 3.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | -2.7 | -2.15 | -16.87 | 19 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 61.12127236580517 | 34.7376913251014 | 2.3 | -4.72 | -4.31 | -5.13 | 3.74 | 3.74 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | 0.89 | 0.26 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 206.4139941690962 | -36.19371282922685 | 2.81 | -2.92 | -2.4 | -8.04 | 7.96 | 7.96 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 0.18 | 0.25 | -9.18 |  | fail_low_response_condition |
| 1444 | 力麗 | 紡織纖維 | defensive_or_traditional |  | 81.0245545323328 | 24.0040319779792 | -0.33 | 25.77 | 33.08 | 43.57 | 55.3 | 55.3 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.67 | -0.3 | 2 | 2 | 14.46 | 12.35 | -12.88 |  | fail_low_response_condition |
| 1529 | 樂事綠能 | 電機機械 | cyclical_turnaround |  | 158.34377836365994 | -8.228649642919668 | -0.22 | 2.04 | -5.05 | 19.31 | 14.18 | 20.27 | False |  | mild_accumulation | -0.2 | 0.64 | 1 | 1 | -0.53 | -0.21 | -12.6 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 54.89389005630324 | 62.99606584097181 | 4.86 | -0.13 | 20.41 | 17.97 | 25.42 | 30.17 | False |  | distribution_warning | -0.06 | -0.06 | 0 | 0 | 1.15 | 1.62 | -9.69 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 51.38068037992098 | 44.12593065109306 | -1.42 | -10.61 | 18.8 | 91.72 | 35.61 | 105.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | -4.24 | 3 | 0 | -7.07 | -9.04 | -37.1 |  | fail_already_priced_in |
| 1618 | 合機 | 電器電纜 | neutral |  | 153.16268341919277 | -7.777041541987246 | -0.49 | 0.24 | 4.46 | 0.0 | 8.05 | 8.33 | False |  | distribution_warning | -0.34 | -0.57 | 1 | 1 | -1.97 | -1.19 | -11.94 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 84.84705467169664 | 55.43173027911526 | -4.07 | 49.01 | 91.18 | 110.14 | 108.98 | 114.45 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | 3.51 | 7.45 | -24.6 |  | fail_already_priced_in |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 105.7915926237789 | 66.66869452589481 | 8.09 | 5.88 | -12.29 | -27.87 | 13.74 | 13.74 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 0 | 6.48 | 5.64 | -14.46 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 87447.70459081836 | 13923.213699202772 | 0.83 | -1.31 | -0.33 | -13.32 | 7.84 | 7.84 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -2.4 | -1.02 | -8.75 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | D_僅留完整清單 | 562.3794928949568 | 152.7873314363479 | -7.69 | -14.29 | 2.86 | -2.7 | 17.76 | 21.74 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -8.71 | -5.51 | -20.5 | 17 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 172.0525806692346 | 74.15584946766846 | 12.23 | 33.66 | 139.77 | 161.81 | 140.12 | 187.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 14.36 | 17.44 | -3.5 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 81.08636484255565 | 56.24608174520713 | -6.21 | -26.41 | -18.0 |  | 0.0 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -14.11 | -12.03 | -30.68 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 158.74753164663522 | 158.86577952131768 | 8.6 | 7.91 | -6.45 | -8.33 | 15.59 | 15.59 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 4.87 | 5.26 | -6.96 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 97.83153907836146 | 66.25506463438163 | -0.26 | 69.91 | 116.34 | 233.91 | 154.3 | 241.33 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 14.32 | 14.96 | -9.96 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 175.7952036483169 | 110.8517314780429 | -10.61 | -3.14 | 0.0 | 119.59 | 17.8 | 143.86 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -10.48 | -9.73 | -27.6 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 181.967983155321 | 128.57705349708792 | -16.14 | 12.99 | 94.2 | 60.37 | 107.64 | 107.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -9.08 | -5.74 | -25.48 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 56.57862562229947 | 60.005270747875855 | -1.6 | 1.45 | 20.64 | 94.07 | 23.06 | 125.23 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | -0.96 | -1.96 | -13.1 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 129.27243852167018 | 65.0605772744456 | 0.22 | 7.03 | 11.07 | 44.69 | 15.42 | 46.08 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | -1.06 | -0.12 | -7.12 | 25 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 133.09060784010344 | 94.4223296894021 | -9.03 | -19.8 | -4.15 | 112.43 | 6.22 | 114.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -11.29 | -11.78 | -29.7 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.80451818624007 | 107.89432287557707 | -4.78 | 15.06 | 23.26 | 36.31 | 28.32 | 43.92 | False |  | mild_accumulation | 2.17 | 2.99 | 1 | 2 | 0.59 | -1.33 | -13.67 | 19 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 87.29863200632951 | 66.67303602415384 | -5.42 | -16.54 | -2.58 | 79.59 | 0.44 | 91.4 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -11.98 | -10.54 | -28.16 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 94.38123673778152 | 82.59499806151248 | 1.36 | -0.93 | 17.11 | 36.63 | 29.29 | 38.92 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 0.31 | 1.34 | -14.84 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 114.62781738634057 | 73.18092844435232 | -3.15 | 9.43 | 36.11 | 237.86 | 40.32 | 238.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | -3.03 | -2.56 | -16.48 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 88.0613471994038 | 34.31162647538102 | -5.18 | 7.25 | 13.19 | 37.35 | 13.75 | 62.38 | False |  | strong_accumulation | 2.08 | 2.37 | 2 | 2 | -3.85 | -4.66 | -23.88 | 20 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 85.01370770897306 | 83.4020606995027 | -4.55 | 13.51 | 34.76 | 24.75 | 37.11 | 53.47 | False |  | strong_accumulation | 1.5 | 0.92 | 2 | 2 | -2.36 | -1.2 | -13.1 | 19 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 121.1993165447746 | 152.01807699959255 | -6.46 | 22.19 | 19.21 | 57.66 | 38.9 | 61.24 | False |  | distribution_warning | -3.53 | -3.16 | 1 | 1 | 4.13 | 3.98 | -14.91 | 15 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 730.1397699033429 | 649.6230795561926 | -10.94 | 18.7 | 88.76 | 66.87 | 102.51 | 103.02 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | -4.3 | -1.76 | -20.2 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 73.47528640006362 | 36.21680049385616 | 1.66 | 18.34 | 34.28 | 51.17 | 37.91 | 52.68 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 1.25 | 4.11 | -5.69 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 95.17088148345744 | 80.48460599503228 | -11.73 | 20.18 | 28.5 | 34.57 | 40.49 | 58.96 | False |  | mild_accumulation | 1.29 | -0.26 | 2 | 2 | 0.61 | 0.81 | -14.19 | 19 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 94.03136606450563 | 55.29984809570999 | -1.57 | 1.44 | 0.72 | 14.2 | 11.71 | 21.6 | False |  | distribution_warning | -0.1 | 0.0 | 2 | 0 | -1.18 | -0.34 | -11.89 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 469.8305876051363 | 430.4543077358013 | -3.94 | -13.07 | 3.64 | -0.58 | 6.67 | 33.68 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -10.98 | -10.75 | -33.16 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 71.83340834565679 | 63.183650278464505 | -1.48 | 22.45 | -2.01 | 50.41 | 25.82 | 79.61 | False |  | distribution_warning | -0.06 | -1.16 | 1 | 0 | 2.77 | 2.05 | -12.98 | 13 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 135.34394044691544 | 118.9555563155988 | 3.93 | -6.8 | 25.85 | 25.85 | 25.85 | 54.33 | False |  | distribution_warning | -0.29 | 0.0 | 2 | 1 | -3.0 | -3.03 | -21.11 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 74.55363851208284 | 76.05855108375845 | -1.13 | 7.92 | 19.03 | 134.87 | 26.39 | 165.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | 3.45 | 1.45 | -11.42 |  | fail_already_priced_in |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 87.19923905471303 | 44.102711379154506 | 0.8 | 9.03 | 16.28 | 53.64 | 46.32 | 79.47 | False |  | distribution_warning | -3.39 | -1.69 | 0 | 1 | -0.69 | 0.68 | -6.63 | 16 | selected |
| 2506 | 太設 | 建材營造 | neutral |  | 131.02269543289438 | 40.6738369557123 | 1.95 | 0.0 | -0.89 | -1.98 | 5.83 | 5.83 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.15 | 0.45 | -2.73 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | B_可觀察 | 57.09899455038421 | 42.50276733448348 | 7.28 | 8.11 | 2.56 | 8.11 | 15.7 | 15.7 | False |  | strong_accumulation | 0.69 | 0.7 | 3 | 2 | 5.48 | 4.64 | -3.45 | 18 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.32956422871683 | 25.42926777280069 | 2.21 | 10.33 | 12.48 | 6.44 | 21.75 | 21.75 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 0.43 | 2.29 | -7.1 | 16 | selected |
| 2528 | 皇普 | 建材營造 | neutral |  | 506.2302328794015 | -80.54983396731191 | 6.9 | 3.7 | -8.18 | -25.04 | 12.25 | 12.25 | False |  | strong_accumulation | 0.15 | 0.52 | 2 | 3 | 2.06 | 2.02 | -8.74 |  | fail_low_response_condition |
| 2536 | 宏普 | 建材營造 | neutral |  | 367.4305802571221 | 58.17838010197999 | -8.55 | -6.33 | -14.06 | -24.06 | 1.05 | 1.05 | False |  | distribution_warning | -1.6 | -1.07 | 0 | 1 | -9.53 | -8.13 | -14.44 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 128.48525684217282 | 290.35375415914626 | 1.84 | 9.95 | 6.25 | -7.14 | 17.8 | 17.8 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | -0.96 | 1.5 | -10.89 | 12 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 418.92924119579374 | 17.34399183311113 | 2.31 | 8.74 | -15.23 | -16.56 | 20.24 | 20.24 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 2.05 | 2.41 | -15.59 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2114.205326762877 | 1780.7414522786555 | 2.21 | 5.01 | 24.65 | 11.82 | 30.56 | 30.56 | False |  | distribution_warning | -0.74 | -0.81 | 1 | 1 | 0.16 | 1.26 | -6.58 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 86.14284031322353 | 42.934476141944494 | -0.13 | -18.95 | -33.28 | -38.4 | 3.91 | 3.91 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -9.26 | -7.52 | -33.96 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 69.90066780612314 | 22.241457982263142 | 2.27 | 5.63 | 3.69 | 4.65 | 14.68 | 14.68 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 1.24 | 2.33 | -4.66 | 19 | selected |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 9203.558823529413 | 30000.69173757892 | -0.49 | 0.0 | -21.01 | -11.35 | 2.01 | 2.01 | False |  | distribution_warning | -1.46 | -1.04 | 1 | 1 | -1.5 | -3.29 | -23.4 | 12 | selected |
| 2838 | 聯邦銀 | 金融保險業 | defensive_or_traditional |  | 61.12684035593818 | 32.1840567542641 | 8.17 | 18.07 | 15.29 | 28.95 | 23.43 | 34.25 | False |  | distribution_warning | -0.02 | -0.08 | 1 | 1 | 8.83 | 9.34 | -1.21 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 428.43428527421696 | 383.3438851601268 | 2.2 | -3.95 | 52.54 | 90.67 | 57.72 | 96.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | -0.02 | 1.77 | -14.55 |  | fail_already_priced_in |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 126.09044237541612 | 179.36123729648395 | 4.88 | 12.52 | 42.32 | 71.02 | 50.12 | 73.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.33 | -0.55 | 1 | 1 | 2.97 | 6.62 | -3.53 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 317.18131813619806 | 335.3574814056247 | 4.96 | 25.77 | 39.88 | 68.19 | 52.74 | 69.83 | True | 近20日漲幅>25%；距60日低點反彈>50% | strong_accumulation | 0.69 | 0.78 | 3 | 3 | 8.75 | 10.99 | -1.69 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 82.69197880820118 | 56.17182732754353 | 3.01 | 28.84 | 23.42 | 40.75 | 43.46 | 46.0 | True | 近20日漲幅>25% | strong_accumulation | 0.59 | 0.62 | 3 | 3 | 8.12 | 9.23 | -1.67 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 133.58068386512642 | 149.57727987056475 | -1.1 | 19.43 | 0.0 | 35.25 | 36.62 | 58.65 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 7.49 | 6.04 | -9.38 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 52.80006873442736 | 30.333657817463656 | -0.45 | 8.36 | 21.28 | 42.76 | 26.87 | 45.92 | False |  | strong_accumulation | 0.61 | 0.58 | 3 | 3 | -0.57 | 0.91 | -7.29 | 20 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.16201695665634 | 32.12627399775476 | 9.33 | 14.9 | 26.84 | 32.58 | 32.58 | 48.73 | False |  | strong_accumulation | 1.66 | 2.35 | 2 | 3 | 7.74 | 7.77 | -10.12 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | A_優先追蹤 | 296.8056658653291 | 223.4596397756601 | -3.1 | 5.8 | 39.49 | 49.49 | 48.98 | 65.91 | False |  | strong_accumulation | 0.2 | 1.06 | 2 | 2 | -2.45 | -2.82 | -19.93 | 23 | selected |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 60.64003400775296 | 90.30830564253388 | -2.97 | -4.67 | 0.41 | 80.81 | 10.36 | 93.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | -0.79 | -3.1 | -18.6 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 92.4008479108611 | 7.500180953989433 | 4.53 | 10.89 | 28.07 | 35.81 | 32.53 | 58.12 | False |  | distribution_warning | -1.06 | -0.7 | 2 | 2 | 3.63 | 5.73 | -4.37 | 14 | selected |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 134.58787189074948 | 63.49927946398063 | -10.07 | -13.6 | -2.53 | -12.99 | 7.69 | 15.14 | False |  | mild_accumulation | 1.34 | -0.37 | 2 | 0 | -10.9 | -10.08 | -27.53 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 102.54268456763282 | 99.53000030399198 | -6.62 | 3.88 | 22.78 | 94.97 | 31.08 | 101.56 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | -1.13 | -2.25 | -12.12 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 152.69225498874076 | 103.50094623545084 | 0.0 | -14.4 | -8.94 | 47.08 | 8.63 | 49.65 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -3.72 | -6.57 | -30.52 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 97.9444020544591 | 26.69919866889564 | -6.47 | 14.81 | 19.42 | 7.86 | 20.5 | 26.18 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | -3.07 | -2.68 | -17.69 | 18 | selected |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 61.74280101762106 | 26.294131791809715 | -3.82 | -9.16 | 53.94 | 45.61 | 66.21 | 78.73 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -11.57 | -8.59 | -26.13 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 786.0188851660067 | 876.2513943112102 | -2.87 | -19.21 | -16.67 | 92.73 | 2.69 | 114.04 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -6.58 | -6.8 | -27.29 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 234.4685935945025 | 283.2136137681272 | -3.34 | -17.77 | 42.21 | 87.37 | 53.54 | 100.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.8 | -1.3 | 0 | 0 | -8.96 | -9.78 | -34.77 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 120.27058178079602 | 124.08296555919723 | -0.95 | -3.58 | 24.48 | 289.72 | 36.27 | 314.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | 0.92 | 0.99 | -17.83 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 59.79938659560561 | 50.93818472845104 | -6.9 | -4.87 | 39.89 | 67.09 | 27.36 | 120.9 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -10.45 | -9.57 | -28.12 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 71.36506452239956 | 62.24907879043217 | -6.12 | -10.0 | 7.85 | 20.28 | 28.57 | 37.22 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -5.78 | -6.11 | -23.01 | 11 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 52.42017987518027 | 32.00359768097935 | 2.54 | 4.3 | 14.47 | 23.39 | 21.33 | 36.33 | False |  | strong_accumulation | 0.5 | 0.46 | 2 | 2 | 3.73 | 2.82 | -7.14 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 217.9663937957777 | 219.79473374274417 | 1.1 | 2.51 | 12.54 | 30.96 | 14.29 | 31.43 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.1 | -0.29 | -21.2 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 132.1328905238472 | 90.64292104800928 | -7.53 | 5.29 | 33.93 | 82.86 | 37.85 | 109.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -4.56 | -5.31 | -24.71 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 66.83049346499516 | 91.43865586931268 | -2.8 | -22.01 | 37.93 | 48.02 | 37.93 | 59.7 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -11.27 | -8.19 | -31.86 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 2229.0254683224584 | 499.8539070006186 | -9.48 | -14.63 | -16.67 | 11.58 | 0.48 | 24.56 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -13.63 | -12.49 | -30.46 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 82.90674676519687 | 39.84386199206386 | 1.87 | 0.93 | 11.0 | 71.65 | 17.2 | 75.81 | True | 近120日漲幅>70% | distribution_warning | -0.54 | -1.12 | 1 | 0 | 0.58 | -0.47 | -14.51 |  | fail_already_priced_in |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.11391792521879 | 34.318355180717255 | -11.65 | -6.33 | -16.62 | 22.44 | 1.63 | 20.54 | False |  | strong_accumulation | 4.42 | 4.81 | 2 | 2 | -9.75 | -9.5 | -22.64 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 51.88340807174888 | 38.88405941085888 | 0.57 | 0.28 | -5.35 | -9.69 | 5.36 | 5.36 | False |  | strong_accumulation | 0.23 | 0.11 | 2 | 2 | 1.24 | 1.14 | -6.6 |  | fail_low_response_condition |
| 4164 | 承業醫 | 生技醫療業 | defensive_or_traditional |  | 80.21161108919033 | 29.048752999112 | 2.08 | -1.83 | -6.36 | -20.51 | 5.75 | 5.75 | False |  | distribution_warning | -0.24 | -0.56 | 2 | 0 | -1.98 | -0.62 | -14.51 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 117.07702184512344 | 150.12393017540887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 140.95338036510228 | 121.41758390187826 | -6.11 | -9.28 | 20.25 | 59.26 | 30.62 | 74.23 | False |  | distribution_warning | -3.16 | -5.47 | 1 | 0 | -8.69 | -5.29 | -20.07 | 11 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 104.34962097326624 | 42.11962076414818 | 4.88 | -7.33 | 64.88 | 83.45 | 77.98 | 102.07 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 1.58 | 1.74 | -15.69 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 281.10296953335904 | 153.94170544805627 | -8.42 | 10.49 | 2.74 | 18.66 | 13.09 | 22.55 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | -2.92 | -3.13 | -14.9 | 23 | selected |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 56.132933831142346 | 46.31185674454288 | -7.9 | -2.49 | -15.39 | -30.96 | 1.53 | 1.53 | False |  | distribution_warning | -0.35 | 0.0 | 0 | 0 | -4.43 | -4.59 | -22.6 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 112.585794273422 | 77.27049729091536 | -5.31 | -10.09 | 17.14 | 18.81 | 16.86 | 46.33 | False |  | mild_accumulation | -1.13 | 0.33 | 1 | 2 | -7.42 | -6.81 | -22.76 | 20 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 68.50112005035051 | 21.799077088765674 | 4.47 | 9.04 | 16.15 | 27.21 | 28.97 | 43.85 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 1.85 | 4.47 | -7.43 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 69.95652184172461 | 55.27975193155594 | 3.22 | -1.07 | -0.12 | 5.84 | 9.45 | 11.35 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | 1.34 | 1.28 | -11.75 | 13 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 152.31709598952162 | 92.03264339471772 | -0.44 | -14.15 | 17.27 | 17.42 | 24.66 | 38.93 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | -4.12 | -3.67 | -22.75 |  | fail_low_response_condition |
| 5519 | 隆大 | 建材營造 | neutral | B_可觀察 | 88.65151498619764 | -2.528158661804875 | -1.01 | 6.22 | 2.09 | 3.64 | 8.76 | 14.02 | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | -0.03 | 0.69 | -3.53 | 18 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 191.64415257562703 | 643.5739953148809 | -0.77 | -13.61 | -9.08 | -13.96 | 1.42 | 1.42 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -9.66 | -7.06 | -23.6 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 406.8044054988343 | 1055.9616865699388 | 0.7 | -1.14 | -13.89 | -22.5 | 6.11 | 6.11 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.92 | -0.73 | -14.06 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 144.78729359082004 | 7.616376207983096 | 1.07 | 3.27 | -3.73 | 0.0 | 4.03 | 4.03 | False |  | strong_accumulation | 0.31 | 0.42 | 3 | 3 | 1.21 | 1.13 | -3.73 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 452.5877921790185 | 13.290185830553815 | 1.28 | 3.26 | -0.38 | -7.14 | 9.08 | 9.08 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | -1.42 | 0.15 | -9.37 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 103.2633463252738 | 75.2296518472431 | -4.33 | 21.29 | 31.99 | 49.66 | 35.43 | 84.92 | True | 距120日低點反彈>80% | strong_accumulation | 1.8 | 1.98 | 2 | 2 | 3.8 | 2.93 | -10.54 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 78.63452035793752 | 28.54441429888791 | -2.56 | -12.5 | -24.86 | 25.47 | 2.31 | 31.03 | False |  | strong_accumulation | 0.68 | 0.05 | 2 | 2 | -5.3 | -5.38 | -26.92 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 79.45933891237368 | 45.21784190906647 | -7.89 | 2.8 | 82.27 | 111.7 | 82.79 | 126.63 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.49 | 0.47 | 0 | 2 | -7.9 | -5.13 | -22.12 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 149.18224366317995 | 540.6620723440313 | 0.55 | 1.57 | -1.52 | -18.44 | 9.15 | 9.15 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -2.19 | -0.87 | -12.28 | 13 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 64.89222551092452 | 26.75489089581158 | 1.44 | 15.28 | 65.29 | 95.82 | 68.01 | 123.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | 2.26 | 3.69 | -6.02 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 70.65666417439758 | 55.92683953560652 | -6.94 | -6.13 | 23.52 | 25.17 | 27.5 | 55.81 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -12.08 | -9.33 | -28.13 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 87.32134624250807 | -38.09779112159554 | 13.76 | -2.11 | 25.14 | 27.9 | 34.99 | 43.79 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.81 | 1.76 | -33.95 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 230.0 | -37.789203084832906 | -8.65 | -22.22 | 55.77 | 89.19 | 62.79 | 94.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.95 | 0.74 | 1 | 2 | -13.48 | -12.68 | -37.15 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 70.173840431185 | 63.74381080306411 | -4.69 | -14.88 | -11.38 | 106.08 | 3.1 | 110.83 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -9.17 | -11.68 | -37.76 |  | fail_low_response_condition |
| 6442 | 光聖 | 通信網路業 | mainstream_growth |  | 116.02033931403636 | 34.238557659078786 | -6.1 | -21.83 | -25.78 | 15.79 | 3.7 | 28.33 | False |  | mild_accumulation | -2.38 | 0.82 | 0 | 2 | -14.47 | -13.12 | -37.4 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 108.47280556481272 | 70.30680982975338 | 11.57 | 61.45 | 126.52 | 188.61 | 158.65 | 193.14 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 28.48 | 26.47 | -2.92 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 119.79410445881784 | 46.47712328703467 | -0.74 | -4.24 | -18.28 | 152.76 | 6.93 | 148.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -11.16 | -10.24 | -30.16 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 89.34296229779807 | 104.70798649866197 | -10.32 | -1.54 | 52.73 | 96.7 | 51.44 | 128.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -8.45 | -9.26 | -31.42 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 208.2009226037929 | 264.65772960638907 | 2.99 | -1.08 | 1.47 | -23.52 | 10.72 | 10.72 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | 1.23 | 1.31 | -9.43 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 134.89522474098308 | 80.2225548530062 | 0.44 | -6.33 | 0.22 | -0.43 | 6.99 | 6.99 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | -3.01 | -2.28 | -11.22 |  | fail_low_response_condition |
| 6614 | 資拓宏宇 | 數位雲端 | neutral |  | 83.31453463498114 | 52.60336124593389 | 0.5 | 0.0 | -4.31 | -20.48 | 4.3 | 4.3 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | -0.26 | -0.07 | -8.26 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth | A_優先追蹤 | 82.35699071961052 | 76.07474411222435 | -4.34 | 17.99 | 10.64 | 24.44 | 23.39 | 31.17 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | -0.16 | 0.38 | -12.71 | 20 | selected |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 58.86220189113607 | 31.41858931023004 | -12.05 | 3.85 | 29.81 | 41.19 | 37.45 | 56.82 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -5.74 | -6.24 | -25.82 | 17 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 52.059623862982896 | 31.13396556292189 | 2.97 | -7.65 | -9.02 | -2.63 | 4.72 | 11.0 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -2.71 | -1.89 | -10.77 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 58.66754639450782 | 30.20218719888066 | -0.42 | 73.75 | 220.27 | 336.46 | 252.68 | 354.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 11.27 | 11.52 | -15.36 |  | fail_low_response_condition |
| 6861 | 睿生光電 | 生技醫療業 | mainstream_growth |  | 66.38490773960466 | 49.1809916775815 | -7.66 | -9.96 | 107.77 | 365.91 | 105.69 | 402.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.0 | 3 | 0 | -7.21 | -9.33 | -37.24 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 73.79305305207775 | 20.43579481993756 | -0.44 | -7.68 | -10.39 | -22.21 | 1.56 | 5.54 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -3.14 | -4.45 | -24.77 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 407.4601758520748 | 190.75235418047765 | 1.86 | 21.97 | 29.39 | 14.33 | 58.92 | 58.92 | True | 距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 10.18 | 11.53 | -7.04 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 462.17814001937097 | 435.1662155750742 | 7.62 | 34.83 | 270.94 | 1468.63 | 353.69 | 1500.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 11.19 | 13.56 | -7.34 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 140.81698992306858 | 101.0361337726689 | -3.44 | 25.1 | 23.6 | 13.19 | 29.83 | 45.75 | True | 近20日漲幅>25% | distribution_warning | -0.22 | -0.19 | 1 | 1 | 6.39 | 5.35 | -13.45 |  | fail_low_response_condition |
| 7721 | 微程式 | 數位雲端 | neutral |  | 72.32514177693761 | 35.98132967883204 | -1.54 | -8.08 | -23.29 | 47.18 | 4.14 | 52.1 | False |  | distribution_warning | -0.79 | 0.0 | 1 | 0 | -5.91 | -4.83 | -21.67 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 1254.6047846317863 | 1420.9203745156804 | -4.29 | -14.96 | -19.67 | -5.23 | 2.84 | 5.07 | False |  | mild_accumulation | 0.4 | -2.35 | 1 | 0 | -7.48 | -7.68 | -29.44 |  | fail_low_response_condition |
| 7749 | 意騰-KY | 半導體業 | mainstream_growth |  | 73.6849472054308 | 64.05199366520502 | -3.78 | -8.23 | -1.21 | -10.55 | 0.74 | 17.12 | False |  | mild_accumulation | 0.02 | 0.5 | 1 | 1 | -12.04 | -10.42 | -27.32 |  | fail_low_response_condition |