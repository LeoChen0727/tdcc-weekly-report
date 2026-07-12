# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-12 16:44:24 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1743 |
| standardized_revenue_rows | 1743 |
| price_rows | 622355 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 270 |
| price_metrics_pass | 269 |
| low_response_pass | 87 |
| already_priced_in_excluded | 46 |
| overheat_pass | 41 |
| score_pass | 41 |
| theme_priority_pass | 36 |
| final_rows | 36 |

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
| fail_revenue_condition | 1473 |
| fail_low_response_condition | 182 |
| fail_already_priced_in | 46 |
| fail_defensive_or_traditional_excluded | 4 |
| missing_or_insufficient_price_metrics | 1 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | 7.34 | 10.96 | 21.91 | 24.61 | 26.2 | 38.11 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | 7.32 | 5.22 | -9.61 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral |  | 101.96587437597796 | 132.1329440999445 | -1.9 | -5.91 | -13.03 | -29.11 | 3.5 | 3.5 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | -2.36 | -1.81 | -13.75 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | 6.08 | 4.07 | 4.63 | -4.24 | 13.27 | 13.27 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 5.03 | 4.71 | -4.71 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -1.89 | -17.08 | -11.44 | -14.35 | 1.11 | 1.11 | False |  | mild_accumulation | 1.23 | 0.21 | 3 | 1 | -7.59 | -6.92 | -18.39 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 70.01963312430405 | 44.542976125957246 | -0.5 | -2.76 | -6.98 | -35.9 | 5.08 | 5.08 | False |  | distribution_warning | -0.03 | -0.35 | 1 | 1 | -1.99 | -2.02 | -13.17 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -16.67 | 31.68 | 77.1 | 94.04 | 91.24 | 96.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | -7.31 | -1.62 | -31.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral |  | 162537.27465535526 | 17993.11726781669 | 1.52 | -4.44 | 0.84 | -12.75 | 7.31 | 7.31 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -2.52 | -1.26 | -9.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -8.33 | -16.26 | -0.82 | 3.42 | 13.08 | 16.91 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -10.52 | -7.87 | -23.66 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | 4.7 | 29.51 | 120.29 | 145.17 | 136.05 | 186.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 11.76 | 14.33 | -3.62 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | 0.0 | -19.67 | -18.78 |  | 2.44 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -9.94 | -8.48 | -28.99 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 5.26 | 3.82 | -4.09 | -7.86 | 15.25 | 15.25 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 4.16 | 4.2 | -5.56 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | -0.58 | -0.97 | -1.54 | 4.7 | 4.07 | 5.35 | False |  | strong_accumulation | 1.38 | 0.61 | 3 | 3 | -0.17 | -0.13 | -3.58 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | 5.07 | 31.34 | 40.24 | 53.71 | 41.37 | 74.26 | True | 近20日漲幅>25%；近60日漲幅>40% | mild_accumulation | 0.6 | -0.84 | 1 | 1 | 16.77 | 13.08 | -7.12 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 125.11209715086407 | 47.06150242210431 | -7.53 | 3.37 | 45.59 | 25.4 | 48.87 | 59.07 | True | 近60日漲幅>40% | mild_accumulation | 2.3 | 3.91 | 2 | 1 | -5.72 | -1.57 | -21.91 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | -4.26 | 58.94 | 109.91 | 190.32 | 138.41 | 206.38 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 3.26 | 6.66 | -15.59 |  | fail_already_priced_in |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth |  | 55.42638489110967 | 41.01765691988111 | -4.57 | -14.55 | -1.05 | 78.2 | 5.03 | 83.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.33 | -1.2 | 0 | 0 | -7.57 | -7.78 | -27.27 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | -0.63 | -9.7 | 14.46 | 3.94 | 13.37 | 26.67 | False |  | distribution_warning | -1.47 | -1.46 | 0 | 0 | -6.22 | -5.72 | -24.36 | 10 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | -1.37 | 6.3 | 19.09 | 134.48 | 16.19 | 144.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -7.63 | -5.55 | -25.26 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | -3.81 | 18.46 | 105.95 | 73.04 | 110.12 | 110.62 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -8.71 | -3.39 | -24.41 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -10.18 | 4.44 | 23.19 | 104.98 | 22.89 | 126.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | -0.44 | -0.98 | -12.57 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 135.4532611228886 | 77.39100370968649 | -4.84 | -4.01 | 5.36 | 37.85 | 11.88 | 39.15 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | -3.8 | -2.74 | -9.97 | 25 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 247.66387451562755 | -4.129081203674164 | 5.71 | -2.82 | -1.04 | -7.44 | 12.61 | 12.61 | False |  | distribution_warning | -1.62 | -1.91 | 0 | 1 | 3.39 | 3.49 | -5.01 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | -6.1 | 14.29 | 41.34 | 171.0 | 44.4 | 173.97 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.77 | -2.98 | 1 | 0 | -0.36 | -1.25 | -14.16 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth |  | 61.61746792060725 | 36.83107001078034 | 3.87 | 5.44 | 49.79 | 59.91 | 54.6 | 81.06 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.43 | -0.48 | 1 | 1 | 4.8 | 4.62 | -21.22 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 2.55 | -14.07 | 13.06 | 25.27 | 17.73 | 39.59 | False |  | distribution_warning | -1.56 | -1.68 | 0 | 0 | -6.64 | -5.18 | -29.05 | 10 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | -17.65 | -17.65 | -11.22 | 90.78 | 1.68 | 96.12 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -16.08 | -15.93 | -34.88 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 74.79882516895688 | 99.90714739063372 | -7.74 | 19.06 | 17.99 | 33.6 | 28.12 | 43.7 | False |  | mild_accumulation | 2.17 | 2.99 | 1 | 2 | -1.02 | -1.4 | -13.8 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -12.96 | -24.3 | -11.16 | 61.41 | 0.94 | 81.28 | True | 距120日低點反彈>80% | distribution_warning | -0.56 | -0.29 | 2 | 2 | -14.34 | -13.55 | -31.96 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | -0.59 | -2.32 | 20.61 | 42.89 | 24.4 | 62.95 | False |  | distribution_warning | -0.68 | -1.09 | 1 | 1 | -0.33 | -0.46 | -16.29 | 12 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 102.87247195164616 | 86.48475082849643 | 1.22 | -1.84 | 13.53 | 33.16 | 29.46 | 39.11 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 0.51 | 1.16 | -14.73 | 20 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -6.37 | 7.19 | 37.53 | 228.88 | 38.25 | 242.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | -2.19 | -1.01 | -15.28 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | 5.88 | 16.0 | 48.56 | 87.5 | 55.17 | 96.72 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.37 | 0.03 | 2 | 1 | 9.35 | 8.29 | -3.91 |  | fail_already_priced_in |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | 7.0 | 30.78 | 110.39 | 82.22 | 118.84 | 119.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | 1.78 | 5.9 | -13.76 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 87.26211992785133 | 46.19747329391832 | 0.98 | 7.13 | 35.83 | 50.61 | 37.5 | 53.42 | False |  | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 1.05 | 3.92 | -5.23 |  | fail_low_response_condition |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | 2.02 | -7.76 | -55.21 | -69.02 | 5.76 | 5.76 | False |  | distribution_warning | -1.23 | -0.08 | 0 | 0 | -2.38 | -8.14 | -63.47 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 18.29 | 91.37 | 109.09 | 105.29 | 116.38 | 117.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 38.72 | 34.96 | 0.0 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 55.96076128364229 | 23.255026779465105 | -1.48 | -2.35 | 2.78 | 11.74 | 7.07 | 20.65 | False |  | strong_accumulation | 0.29 | 0.38 | 2 | 2 | -1.87 | -2.5 | -26.16 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 220.09287723199685 | 399.98004177172845 | -0.52 | -3.75 | 3.77 | -16.85 | 7.54 | 7.54 | False |  | mild_accumulation | 0.08 | -0.13 | 2 | 1 | -1.28 | -0.65 | -5.87 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 381.5468504599107 | 422.1697253819397 | -1.74 | -13.48 | 1.2 | 6.96 | 4.97 | 32.38 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -10.36 | -9.86 | -33.81 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 59.07699165913917 | 62.47100752006232 | -6.03 | 10.47 | -2.0 | 45.96 | 18.07 | 68.55 | False |  | distribution_warning | -0.06 | -1.16 | 1 | 0 | -4.76 | -4.12 | -18.33 | 12 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 543.886650237175 | 158.17460116324747 | 26.59 | 16.08 | 34.79 | 53.25 | 38.12 | 86.65 | True | 距120日低點反彈>80% | distribution_warning | -0.29 | 0.0 | 2 | 1 | 16.31 | 15.03 | -4.58 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | -15.5 | 2.96 | -2.46 | 118.9 | 14.64 | 141.21 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | -6.12 | -6.75 | -19.65 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.76248321707817 | 36.92164743994052 | -3.73 | 8.86 | 6.17 | 41.14 | 19.44 | 78.67 | False |  | mild_accumulation | 2.55 | 1.02 | 3 | 1 | 0.98 | 0.98 | -7.86 | 18 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -4.59 | -21.29 | -29.72 | 81.45 | 1.84 | 72.07 | True | 近120日漲幅>70% | mild_accumulation | 0.1 | -0.58 | 2 | 2 | -12.08 | -12.66 | -36.51 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | 6.67 | -4.55 | 7.8 | 17.83 | 15.59 | 52.19 | False |  | mild_accumulation | -0.88 | 0.61 | 0 | 3 | 0.85 | 0.56 | -14.12 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | 2.06 | -1.11 | 0.34 | -2.2 | 5.83 | 5.83 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.06 | 0.38 | -2.73 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | 3.66 | 4.04 | 4.81 | -0.59 | 12.6 | 12.6 | False |  | strong_accumulation | 0.25 | 0.06 | 3 | 3 | 3.11 | 3.2 | -2.75 | 19 | selected |
| 2527 | 宏璟 | 建材營造 | neutral |  | 365.123018807587 | 2533.2289075556096 | 3.9 | 23.12 | 17.68 | 32.3 | 30.28 | 54.63 | False |  | strong_accumulation | 0.36 | 0.45 | 2 | 2 | 6.47 | 7.02 | -1.84 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 57.67979274611399 | 238.4760412839904 | 3.7 | 0.9 | 7.69 | -3.86 | 19.4 | 19.4 | False |  | distribution_warning | -0.16 | -0.53 | 2 | 0 | -0.07 | 2.55 | -9.68 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 79.55310359840207 | 22.58855338149928 | 0.51 | -0.13 | -14.47 | -18.72 | 18.73 | 18.73 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 0.49 | 0.97 | -15.12 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 105.33076260323196 | 54.8064697471788 | 1.31 | -20.65 | -29.71 | -38.51 | 4.72 | 4.72 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -6.31 | -5.76 | -29.84 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | 1.78 | 2.69 | 7.01 | 5.53 | 16.72 | 16.72 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 2.81 | 3.61 | -2.97 | 22 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | 6.18 | 5.8 | 0.69 | -3.31 | 15.87 | 15.87 | False |  | strong_accumulation | 0.48 | 0.06 | 3 | 2 | 4.92 | 4.85 | -1.68 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround |  | 57.91908933878501 | 32.316290442538865 | 15.76 | 9.21 | 14.17 | 15.76 | 18.07 | 25.38 | False |  | distribution_warning | -0.65 | -0.96 | 0 | 0 | 8.53 | 8.41 | -1.19 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 328.3542479788894 | 242.62430701861496 | 8.72 | 17.33 | 57.48 | 62.33 | 57.48 | 79.55 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.2 | 1.06 | 2 | 2 | 4.73 | 5.07 | -13.35 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 66.11083679678092 | 85.45932489486553 | -14.23 | -0.42 | -5.62 | 73.43 | 5.86 | 85.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.82 | 1.09 | 2 | 3 | -4.39 | -5.92 | -21.93 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | 0.84 | -0.41 | 9.55 | 5.7 | 30.27 | 30.27 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.03 | 3.06 | -4.37 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -9.07 | -0.66 | 22.68 | 82.08 | 27.03 | 89.9 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | -3.93 | -4.37 | -14.84 |  | fail_already_priced_in |
| 3033 | 威健 | 電子通路業 | mainstream_growth |  | 54.44557676970354 | 26.196636563481785 | -1.59 | -1.2 | 43.56 | 58.97 | 45.88 | 74.34 | True | 近60日漲幅>40% | strong_accumulation | 1.08 | 1.51 | 2 | 3 | -0.16 | 0.08 | -10.31 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 188.0864822148371 | 114.02783651203414 | -2.76 | -11.69 | -2.53 | 46.88 | 7.36 | 46.88 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -3.38 | -6.49 | -31.33 | 17 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | 7.75 | -0.36 | 13.93 | 4.32 | 19.31 | 27.67 | False |  | distribution_warning | -0.99 | 0.0 | 0 | 0 | 2.01 | 1.94 | -13.12 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -6.69 | -18.14 | 52.48 | 43.71 | 64.84 | 77.25 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -10.64 | -7.92 | -26.74 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | 3.43 | -6.49 | -14.09 | 108.55 | 6.73 | 122.46 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -1.88 | -2.39 | -24.43 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | -2.88 | -9.67 | 15.67 | 234.05 | 26.63 | 285.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | -4.93 | -5.53 | -23.65 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 170.41456580742187 | 44.354447130404274 | -0.34 | -9.4 | 21.24 | 81.76 | 23.92 | 80.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.11 | -0.38 | 0 | 1 | -2.29 | -4.79 | -29.75 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | -9.14 | -9.88 | 14.81 | 55.31 | 11.51 | 118.93 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -10.04 | -8.69 | -28.77 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 53.84760848458394 | 94.00659331121736 | -8.83 | -8.54 | 2.85 | -1.03 | 9.47 | 17.96 | False |  | distribution_warning | -2.07 | -2.1 | 0 | 0 | -7.9 | -7.45 | -28.11 | 11 | selected |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 76.00142700075368 | 64.57714379703859 | -5.2 | -6.59 | 7.59 | 4.94 | 25.62 | 34.07 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -7.27 | -7.22 | -24.78 | 11 | selected |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -1.63 | 1.12 | 8.38 | 25.69 | 10.03 | 29.29 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.63 | -1.59 | -22.48 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -18.57 | 7.83 | 21.23 | 78.23 | 20.39 | 102.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -7.94 | -7.13 | -27.06 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | 0.2 | 6.36 | 31.07 | 95.33 | 71.33 | 111.81 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.79 | 0.99 | 1 | 2 | -4.13 | -2.28 | -17.97 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -0.6 | -19.27 | 37.92 | 42.67 | 37.92 | 63.32 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -6.68 | -4.97 | -30.32 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -9.52 | -15.04 | -16.06 | 22.37 | 0.97 | 23.96 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -12.31 | -11.11 | -30.79 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 57.64322627738095 | 26.63684630892036 | -7.77 | -15.66 | -36.16 | 26.43 | 14.46 | 39.35 | False |  | mild_accumulation | 1.14 | 0.77 | 2 | 1 | -9.67 | -8.51 | -43.62 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.789881691302135 | 33.96537207102099 | -8.58 | -13.46 | -21.14 | 30.88 | 2.47 | 49.8 | False |  | distribution_warning | -1.04 | -2.07 | 0 | 2 | -7.55 | -7.61 | -38.04 | 11 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 131.85418997881953 | 55.17736411171146 | -1.39 | -2.29 | 5.97 | 67.45 | 14.52 | 71.77 | False |  | distribution_warning | -0.54 | -1.12 | 1 | 0 | -1.39 | -2.25 | -16.47 | 16 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 80.93046018498126 | 44.798488379235415 | -4.93 | 3.02 | 5.47 | 0.8 | 14.01 | 20.35 | False |  | distribution_warning | -0.6 | -0.74 | 1 | 1 | 1.49 | 0.57 | -14.3 | 15 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -7.23 | 8.46 | 10.1 | 97.29 | 28.61 | 105.66 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.04 | 1.11 | 2 | 2 | 0.69 | -1.85 | -25.09 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -3.04 | -0.52 | -4.64 | -6.05 | 8.08 | 8.08 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -2.24 | -1.96 | -14.18 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -11.21 | -20.8 | 7.03 | 38.85 | 20.29 | 60.45 | False |  | distribution_warning | -3.16 | -5.47 | 1 | 0 | -14.23 | -11.63 | -26.39 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | 0.58 | -6.99 | -4.0 | -5.26 | 9.49 | 9.49 | False |  | distribution_warning | -1.15 | 0.0 | 1 | 0 | -1.66 | -3.66 | -26.07 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 168.6655162496405 | 156.81600720436765 | -4.7 | 6.15 | 1.17 | 18.97 | 15.77 | 21.91 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | -1.19 | -0.67 | -12.88 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | 0.0 | -14.13 | -11.53 | 107.08 | 12.06 | 105.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.63 | -0.04 | 1 | 0 | -4.59 | -4.83 | -29.78 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -8.66 | 11.81 | -14.21 | 80.0 | 23.06 | 101.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 5.82 | 6.03 | 1 | 2 | 1.44 | -2.37 | -26.56 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | 3.83 | 2.98 | 11.76 | 27.52 | 31.03 | 46.15 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 3.05 | 5.29 | -5.94 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | 5.09 | 0.71 | 1.56 | 5.88 | 11.02 | 12.95 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | 2.87 | 2.44 | -10.48 | 15 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 224.3279602768877 | 118.4530613441191 | -0.2 | -1.3 | 26.25 | 23.87 | 35.07 | 50.53 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | 5.05 | 4.4 | -16.3 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 2513.497664900037 | 792.7361428535551 | 1.41 | -21.29 | -6.37 | -11.25 | 2.37 | 2.37 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -6.88 | -5.18 | -22.88 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | 1.86 | -2.02 | -12.25 | -19.52 | 6.85 | 6.85 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | -0.19 | -0.02 | -12.95 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 4.54 | 6.44 | 14.97 | 24.52 | 17.49 | 28.23 | False |  | strong_accumulation | 0.24 | 0.34 | 3 | 3 | 4.18 | 4.75 | -0.77 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 1322.1624507927131 | 667.7676077743706 | -0.11 | -2.79 | 1.0 | -14.53 | 9.03 | 9.03 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -2.19 | -0.81 | -12.38 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | -6.63 | 9.8 | 39.16 | 101.47 | 51.45 | 118.29 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | -0.79 | 1.13 | -8.19 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 73.30676173690114 | 58.7802399797441 | 0.62 | -0.25 | 22.61 | 35.8 | 37.18 | 67.63 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -4.85 | -1.83 | -22.68 | 12 | selected |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 76.89914529735076 | 37.00041684126828 | 8.71 | 0.0 | 13.44 | 21.1 | 21.61 | 37.32 | False |  | distribution_warning | -2.56 | -2.33 | 0 | 0 | 5.46 | 5.88 | -11.42 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 6.88 | -1.06 | 32.01 | 35.47 | 35.86 | 44.72 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 3.74 | 2.13 | -33.52 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | 0.97 | -3.52 | 3.58 | 134.68 | 30.25 | 144.6 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.44 | -3.36 | 0 | 0 | 0.75 | -0.34 | -22.59 |  | fail_already_priced_in |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 56.96595858063789 | 23.32960784964402 | 5.49 | 1.55 | 27.1 | 34.24 | 28.34 | 53.91 | False |  | distribution_warning | -0.05 | -1.64 | 1 | 1 | 4.12 | 4.17 | -5.74 | 14 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -2.6 | -9.86 | -24.85 | 103.8 | 5.63 | 116.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -5.47 | -8.16 | -36.22 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -7.89 | 30.32 | 95.29 | 148.55 | 122.32 | 151.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 6.59 | 5.57 | -18.15 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -16.6 | -4.43 | -28.07 | 123.78 | 4.3 | 128.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -13.43 | -11.24 | -32.42 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | -4.06 | 3.13 | 35.19 | 95.34 | 30.41 | 135.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -5.65 | -5.56 | -29.35 |  | fail_already_priced_in |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | -5.2 | -4.01 | -18.51 | -22.31 | 1.32 | 12.65 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -3.82 | -5.17 | -30.99 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | 0.62 | 3.16 | 0.99 | -20.0 | 9.38 | 9.38 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | -0.06 | 0.12 | -10.53 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | -3.11 | -1.19 | 38.33 | 39.73 | 50.91 | 59.21 | True | 距60日低點反彈>50% | mild_accumulation | 0.27 | 1.59 | 2 | 1 | -6.39 | -1.34 | -17.82 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 94.32153392330385 | 50.47184104059554 | 2.88 | 6.04 | -1.53 | -24.25 | 20.17 | 20.17 | False |  | mild_accumulation | -0.03 | 0.59 | 1 | 2 | 1.97 | 1.68 | -9.98 |  | fail_low_response_condition |
| 6672 | 騰輝電子-KY | 電子零組件業 | mainstream_growth |  | 68.12346641728693 | 34.54799350529283 | 0.17 | 36.38 | 59.36 | 219.06 | 71.26 | 251.83 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 8.92 | 3.83 | 2 | 1 | 10.17 | 9.72 | -9.7 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 115.18509399137636 | 84.28516773674946 | -7.57 | 12.03 | 6.47 | 19.39 | 20.0 | 27.57 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | -3.92 | -2.08 | -15.11 |  | fail_low_response_condition |
| 6770 | 力積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 68.75001629130628 | 37.81385240017568 | -4.82 | 10.4 | 38.33 | 42.77 | 37.79 | 48.12 | False |  | strong_accumulation | 0.18 | 0.2 | 2 | 2 | -4.8 | -4.16 | -24.76 | 19 | selected |
| 6776 | 展碁國際 | 電子通路業 | mainstream_growth |  | 50.695530560848255 | 34.61390098363236 | 3.53 | -6.86 | -5.43 | -3.97 | 5.09 | 11.4 | False |  | distribution_warning | -1.37 | 0.0 | 0 | 0 | -1.49 | -1.24 | -10.45 |  | fail_low_response_condition |
| 6834 | 天二科技 | 電子零組件業 | mainstream_growth |  | 66.45908716785986 | 36.55631428112642 | 0.0 | 85.71 | 242.11 | 296.34 | 286.9 | 398.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.85 | -4.97 | 1 | 0 | 16.0 | 18.42 | -7.14 |  | fail_low_response_condition |
| 6863 | 永道-KY | 通信網路業 | mainstream_growth |  | 80.80583566568964 | 29.708297590229776 | 1.75 | -7.66 | -7.2 | -28.62 | 3.11 | 7.16 | False |  | mild_accumulation | -0.02 | 0.02 | 1 | 1 | -0.67 | -2.49 | -23.62 |  | fail_low_response_condition |
| 6885 | 全福生技 | 生技醫療業 | defensive_or_traditional |  | 491.5422885572139 | 305.0715990453461 | 2.1 | -9.34 | -7.02 | -22.93 | 6.59 | 6.59 | False |  | strong_accumulation | 0.08 | 0.05 | 2 | 2 | 0.02 | -0.69 | -20.4 |  | fail_low_response_condition |
| 6887 | 寶綠特-KY | 綠能環保 | neutral |  | 183.71076107386315 | -3.233323242858129 | -2.73 | -5.19 | -19.62 | -41.52 | 10.28 | 10.28 | False |  | distribution_warning | -0.13 | -0.03 | 0 | 0 | -3.26 | -3.09 | -20.28 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 4396.6335866973695 | 423.4001874685442 | 15.6 | 28.88 | 44.6 | 22.78 | 72.2 | 72.2 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.12 | -1.21 | 1 | 0 | 16.15 | 16.8 | -7.37 |  | fail_low_response_condition |
| 6934 | 心誠鎂 | 生技醫療業 | defensive_or_traditional |  | 41325.0 | 82.52418240442192 | 20.76 | 14.84 | -8.71 |  | 29.38 |  | False |  | mild_accumulation | 1.56 | 0.0 | 3 | 0 | 15.96 | 13.53 | -11.15 |  | fail_low_response_condition |
| 6937 | 天虹 | 半導體業 | mainstream_growth |  | 64.17155209836051 | 33.627529532614275 | -11.32 | -5.14 | -23.18 | 8.84 | 4.02 | 29.57 | False |  | strong_accumulation | 0.05 | 0.37 | 2 | 2 | -4.87 | -6.04 | -27.89 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 555.4301993309172 | 461.6331304222786 | 6.21 | 53.62 | 314.06 | 1344.14 | 400.95 | 1360.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.98 | -0.02 | 1 | 2 | 18.66 | 21.19 | -2.93 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 190.83258436146744 | 114.11277848375384 | -1.92 | 21.34 | 12.04 | 2.68 | 28.99 | 44.81 | False |  | distribution_warning | -0.22 | -0.19 | 1 | 1 | 3.66 | 3.9 | -14.01 |  | fail_low_response_condition |
| 7711 | 永擎 | 電腦及週邊設備業 | mainstream_growth |  | 140.78849243584202 | 44.46783852433029 | -4.65 | -12.89 | 0.49 | 19.19 | 1.49 | 62.7 | False |  | mild_accumulation | 0.04 | 0.02 | 1 | 1 | -8.67 | -8.89 | -34.71 |  | fail_low_response_condition |