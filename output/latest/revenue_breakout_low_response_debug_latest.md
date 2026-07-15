# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-15 21:29:03 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1952 |
| standardized_revenue_rows | 1952 |
| price_rows | 628242 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 221 |
| tdcc_mild_accumulation_count | 850 |
| tdcc_distribution_warning_count | 707 |
| revenue_condition_pass | 301 |
| price_metrics_pass | 300 |
| low_response_pass | 85 |
| already_priced_in_excluded | 35 |
| overheat_pass | 50 |
| score_pass | 50 |
| theme_priority_pass | 41 |
| final_rows | 41 |

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
| fail_revenue_condition | 1651 |
| fail_low_response_condition | 215 |
| fail_already_priced_in | 35 |
| fail_defensive_or_traditional_excluded | 7 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | -5.75 | 5.31 | 18.55 | 12.87 | 20.45 | 31.82 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | 1.48 | 0.3 | -13.73 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 101.96587437597796 | 132.1329440999445 | 0.97 | -4.57 | -8.73 | -28.91 | 4.5 | 4.5 | False |  | mild_accumulation | 0.55 | -0.38 | 2 | 0 | -0.43 | -0.39 | -11.81 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 68.32688588007737 | 39.48200784911037 | 1.35 | -0.88 | -2.17 | -5.46 | 5.14 | 5.14 | False |  | mild_accumulation | -0.85 | 0.07 | 0 | 1 | 2.13 | 1.45 | -5.46 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | 2.46 | 0.81 | 3.02 | -6.25 | 10.62 | 10.62 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 2.54 | 1.87 | -6.95 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -4.04 | -15.84 | -11.22 | -19.82 | 3.19 | 3.19 | False |  | mild_accumulation | 1.02 | 0.0 | 2 | 0 | -7.12 | -7.03 | -20.18 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 70.01963312430405 | 44.542976125957246 | 0.17 | -3.53 | -4.9 | -38.07 | 5.43 | 5.43 | False |  | distribution_warning | -0.03 | 0.0 | 1 | 1 | -1.21 | -1.32 | -12.88 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -11.41 | 0.0 | 67.84 | 81.92 | 85.14 | 85.97 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.62 | 1 | 1 | -11.24 | -3.83 | -33.2 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 162537.27465535526 | 17993.11726781669 | 3.14 | -4.29 | 1.13 | -7.0 | 11.23 | 11.23 | False |  | distribution_warning | -0.04 | -0.1 | 1 | 0 | 1.54 | 2.02 | -5.88 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -5.95 | -21.0 | 3.04 | -11.24 | 10.75 | 14.49 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | -9.8 | -7.56 | -25.24 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | 2.91 | 22.13 | 137.1 | 150.0 | 143.2 | 195.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.1 | -2.21 | 1 | 1 | 11.89 | 14.2 | -1.85 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | 1.74 | -19.34 | -21.08 |  | 5.42 |  | False |  | mild_accumulation | -0.67 | 0.12 | 0 | 1 | -7.33 | -6.88 | -29.47 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 0.0 | 1.34 | -0.15 | -9.19 | 15.59 | 15.59 | False |  | mild_accumulation | 0.11 | 0.24 | 1 | 1 | 4.01 | 3.32 | -2.85 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | 1.36 | 3.17 | -0.76 | 4.0 | 5.69 | 6.12 | False |  | strong_accumulation | 0.95 | 0.58 | 3 | 3 | 1.32 | 1.13 | -2.07 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | -10.3 | 23.97 | 23.51 | 44.54 | 31.35 | 63.86 | False |  | distribution_warning | -0.29 | -0.74 | 0 | 1 | 6.0 | 4.29 | -12.66 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 125.11209715086407 | 47.06150242210431 | -6.5 | -9.54 | 19.94 | 11.02 | 36.61 | 49.26 | False |  | mild_accumulation | 0.43 | -0.92 | 1 | 0 | -10.79 | -5.86 | -26.73 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 106.58847855421364 | 47.886498368081 | 12.24 | 16.61 | 11.11 | 33.74 | 24.53 | 43.17 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | 15.64 | 14.4 | 0.0 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | -8.72 | 26.99 | 114.37 | 120.44 | 132.12 | 198.3 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.29 | 2 | 2 | -4.41 | 1.55 | -17.82 |  | fail_already_priced_in |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth |  | 55.42638489110967 | 41.01765691988111 | 0.0 | -14.48 | -4.55 | 80.86 | 6.18 | 78.3 | True | 近120日漲幅>70% | distribution_warning | -1.03 | -1.0 | 0 | 0 | -4.86 | -5.59 | -26.89 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | 0.84 | -10.65 | 6.22 | 2.36 | 9.63 | 27.47 | False |  | distribution_warning | -1.42 | -1.44 | 0 | 0 | -4.2 | -3.83 | -23.89 | 11 | selected |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 67.86685548491262 | 35.613194655616326 | 0.0 | 2.74 | 17.31 | 44.38 | 15.91 | 42.69 | False |  | distribution_warning | -0.11 | -0.13 | 0 | 0 | 0.43 | 1.23 | -3.75 | 17 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | 6.83 | -6.6 | 17.86 | 139.9 | 19.76 | 135.71 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -2.01 | 1 | 1 | -3.81 | -0.81 | -22.66 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | 3.74 | -4.5 | 105.58 | 81.96 | 114.88 | 115.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.28 | -3.23 | 0 | 0 | -6.51 | 0.27 | -22.7 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -4.68 | -3.7 | 12.5 | 88.71 | 14.15 | 114.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.3 | 0.29 | 2 | 2 | -5.65 | -4.83 | -17.17 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 135.4532611228886 | 77.39100370968649 | -4.49 | -3.86 | 5.95 | 32.12 | 10.24 | 37.11 | False |  | strong_accumulation | 0.33 | 0.31 | 2 | 2 | -4.29 | -2.55 | -11.29 | 24 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 247.66387451562755 | -4.129081203674164 | 2.01 | 4.96 | 2.14 | -6.04 | 13.06 | 13.06 | False |  | distribution_warning | -0.89 | -0.77 | 0 | 1 | 3.02 | 2.93 | -4.63 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | -6.09 | 8.97 | 32.78 | 163.82 | 44.77 | 167.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.86 | -2.6 | 0 | 0 | -1.55 | -0.89 | -13.95 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 61.61746792060725 | 36.83107001078034 | -6.57 | -8.94 | 31.97 | 38.39 | 35.33 | 58.5 | False |  | distribution_warning | -0.18 | -0.33 | 1 | 1 | -7.62 | -7.25 | -31.04 | 11 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 7.39 | -10.1 | 19.06 | 36.66 | 22.55 | 45.31 | False |  | distribution_warning | -1.53 | -1.29 | 0 | 0 | -1.19 | -0.83 | -26.14 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | -3.05 | -15.89 | -1.8 | 97.2 | 10.12 | 105.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -1.49 | 1 | 0 | -9.72 | -9.06 | -31.84 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 74.79882516895688 | 99.90714739063372 | -1.07 | 6.04 | 20.15 | 33.2 | 26.95 | 42.39 | False |  | mild_accumulation | 2.17 | 2.57 | 1 | 1 | -3.12 | -1.51 | -14.59 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -9.69 | -22.35 | -18.97 | 53.44 | 7.33 | 72.85 | False |  | distribution_warning | -0.59 | -0.4 | 1 | 1 | -15.29 | -14.15 | -35.13 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | 5.2 | -1.57 | 25.09 | 40.41 | 27.17 | 66.59 | False |  | distribution_warning | -0.53 | -1.27 | 1 | 0 | 2.17 | 1.76 | -14.43 | 13 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 102.87247195164616 | 86.48475082849643 | 2.14 | 2.97 | 18.32 | 34.63 | 32.06 | 41.9 | False |  | mild_accumulation | 0.06 | 0.08 | 1 | 1 | 2.16 | 2.52 | -13.01 | 20 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -2.68 | 0.99 | 23.9 | 223.57 | 22.12 | 228.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.11 | 1.44 | 1 | 2 | -6.35 | -3.82 | -18.72 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | 7.35 | 9.9 | 49.51 | 85.39 | 52.72 | 94.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.44 | 0.17 | 2 | 1 | 6.04 | 5.24 | -10.12 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 50.90083303173535 | 76.24247572692803 | 1.98 | -6.88 | 31.79 | 11.74 | 35.98 | 56.52 | False |  | mild_accumulation | 0.44 | -0.21 | 1 | 1 | 0.0 | 2.17 | -11.38 | 17 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.99850390624209 | 133.4952742541738 | -10.49 | -8.5 | 18.04 | 7.86 | 24.33 | 32.08 | False |  | distribution_warning | -0.63 | -0.39 | 1 | 1 | -6.42 | -6.13 | -23.83 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | 19.35 | 21.62 | 131.25 | 102.53 | 141.71 | 142.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.21 | 0 | 0 | 9.31 | 14.33 | -4.75 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 87.26211992785133 | 46.19747329391832 | 5.38 | 6.25 | 40.43 | 57.18 | 43.56 | 60.9 | True | 近60日漲幅>40% | mild_accumulation | 0.56 | -0.01 | 2 | 0 | 5.37 | 7.01 | -4.58 |  | fail_low_response_condition |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | 0.63 | -10.6 | -60.78 | -75.01 | 6.9 | 6.9 | False |  | distribution_warning | -1.13 | -0.04 | 0 | 0 | -6.01 | -9.72 | -65.24 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 375.5658851662359 | 116.51091844759344 | 11.15 | 15.65 | 49.33 | 40.79 | 56.16 | 76.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.13 | -0.87 | 1 | 1 | 7.21 | 9.02 | -7.7 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 60.7 | 139.07 | 170.82 | 173.06 | 187.8 | 189.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 61.68 | 56.31 | 0.0 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 55.96076128364229 | 23.255026779465105 | 0.89 | -1.45 | 6.94 | 10.42 | 9.35 | 22.83 | False |  | strong_accumulation | 0.42 | 0.47 | 2 | 2 | 0.59 | 0.0 | -24.83 | 19 | selected |
| 2442 | 新美齊 | 建材營造 | neutral |  | 220.09287723199685 | 399.98004177172845 | -0.26 | -2.53 | 1.05 | -21.86 | 7.82 | 7.82 | False |  | distribution_warning | -0.15 | -0.44 | 1 | 0 | -0.58 | -0.2 | -5.62 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 381.5468504599107 | 422.1697253819397 | -1.17 | -18.39 | 0.6 | 6.3 | 9.76 | 32.11 | False |  | distribution_warning | -2.89 | -1.7 | 0 | 0 | -7.88 | -7.55 | -33.94 | 14 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 59.07699165913917 | 62.47100752006232 | -8.62 | -3.75 | -15.87 | 46.49 | 14.97 | 64.13 | False |  | mild_accumulation | 0.33 | -0.77 | 1 | 0 | -7.48 | -4.88 | -20.48 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 543.886650237175 | 158.17460116324747 | 12.57 | 0.36 | 21.96 | 42.39 | 28.55 | 73.72 | False |  | distribution_warning | -0.61 | -1.14 | 1 | 0 | 6.95 | 4.95 | -11.19 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | -3.92 | 2.26 | 9.48 | 130.08 | 21.44 | 155.53 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.84 | 1 | 1 | -0.97 | -0.33 | -14.88 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.76248321707817 | 36.92164743994052 | -1.15 | 1.17 | 10.21 | 39.55 | 19.91 | 79.36 | False |  | mild_accumulation | 1.78 | 1.08 | 2 | 1 | 1.05 | 1.67 | -7.5 | 18 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -1.2 | -22.45 | -22.69 | 35.16 | 9.17 | 44.87 | False |  | distribution_warning | -0.19 | -0.65 | 1 | 1 | -9.2 | -10.52 | -37.15 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | -8.06 | -4.82 | -3.26 | 14.7 | 12.74 | 48.44 | False |  | mild_accumulation | -0.4 | 0.5 | 0 | 2 | -0.89 | -1.75 | -16.24 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | 0.56 | -1.43 | 1.7 | -1.54 | 6.42 | 6.42 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | 0.81 | 0.86 | -2.19 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | -0.23 | 5.04 | 6.48 | 0.23 | 13.26 | 13.26 | False |  | strong_accumulation | 0.08 | 0.04 | 2 | 2 | 3.05 | 3.06 | -2.18 | 19 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.3105385295913 | 31.38789796597349 | 4.76 | 4.6 | 17.26 | 10.15 | 27.54 | 27.54 | False |  | mild_accumulation | 0.16 | 0.35 | 1 | 2 | 4.36 | 5.53 | -2.68 | 16 | selected |
| 2527 | 宏璟 | 建材營造 | neutral |  | 365.123018807587 | 2533.2289075556096 | 5.75 | 15.07 | 31.92 | 49.17 | 37.77 | 63.52 | False |  | strong_accumulation | 0.75 | 0.49 | 2 | 2 | 9.56 | 10.41 | -3.12 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 57.67979274611399 | 238.4760412839904 | 1.36 | -7.44 | 5.66 | -3.45 | 19.4 | 19.4 | False |  | distribution_warning | -0.41 | -0.2 | 1 | 0 | 0.7 | 2.29 | -9.68 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 79.55310359840207 | 22.58855338149928 | 0.75 | 2.82 | -9.58 | -17.49 | 21.15 | 21.15 | False |  | mild_accumulation | 0.02 | 0.06 | 1 | 1 | 1.89 | 2.07 | -9.68 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 105.33076260323196 | 54.8064697471788 | 2.73 | -15.49 | -20.9 | -36.62 | 6.75 | 6.75 | False |  | distribution_warning | -0.68 | -0.84 | 0 | 0 | -1.84 | -2.94 | -23.05 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | -1.78 | 0.45 | 5.24 | 0.0 | 12.64 | 12.64 | False |  | mild_accumulation | 0.46 | 0.41 | 1 | 1 | -0.96 | -0.24 | -6.36 | 20 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | 1.06 | 2.87 | 2.87 | -4.33 | 13.89 | 13.89 | False |  | mild_accumulation | 0.17 | 0.0 | 2 | 1 | 2.48 | 2.29 | -3.37 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 57.91908933878501 | 32.316290442538865 | 6.2 | 5.93 | 14.62 | 17.02 | 19.35 | 26.74 | False |  | distribution_warning | -0.52 | -0.76 | 0 | 0 | 8.54 | 7.16 | -4.66 | 12 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 199.0184261973224 | 334.18209408719963 | -8.22 | -8.75 | 37.94 | 72.11 | 36.93 | 72.43 | True | 近120日漲幅>70% | distribution_warning | -0.33 | -0.34 | 1 | 1 | -6.95 | -5.54 | -21.57 |  | fail_already_priced_in |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 329.50067645662165 | 334.2834434453442 | 3.58 | 14.4 | 52.53 | 67.36 | 58.21 | 66.97 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.25 | 0.26 | 2 | 2 | 7.45 | 9.38 | -4.24 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 294.84268843595487 | 170.38806261042123 | 25.32 | 32.16 | 31.4 | 61.43 | 71.21 | 98.83 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.06 | 2 | 1 | 26.34 | 24.83 | -0.29 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 328.3542479788894 | 242.62430701861496 | 9.13 | 7.42 | 53.7 | 57.76 | 58.8 | 81.06 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.03 | 0.24 | 1 | 1 | 4.68 | 5.64 | -12.61 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 66.11083679678092 | 85.45932489486553 | -11.63 | -10.17 | -19.22 | 56.88 | 7.44 | 71.15 | False |  | mild_accumulation | 0.42 | 0.73 | 1 | 2 | -10.76 | -10.62 | -28.07 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | -1.66 | -0.42 | 9.22 | 3.95 | 28.11 | 28.11 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.57 | 1.05 | -5.95 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -0.77 | 1.72 | 26.02 | 90.83 | 27.06 | 92.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.1 | 1.88 | 2 | 2 | -1.21 | -0.41 | -12.8 |  | fail_already_priced_in |
| 3033 | 威健 | 電子通路業 | mainstream_growth |  | 54.44557676970354 | 26.196636563481785 | 12.55 | 12.1 | 58.86 | 81.11 | 63.53 | 95.43 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.39 | 1.85 | 3 | 3 | 11.01 | 10.68 | 0.0 |  | fail_low_response_condition |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 188.0864822148371 | 114.02783651203414 | -6.54 | -11.5 | -2.91 | 31.58 | 1.52 | 38.89 | False |  | distribution_warning | -1.26 | -1.2 | 0 | 0 | -7.1 | -9.58 | -35.06 | 16 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 167.50830564784053 | 42.89095493442987 | -1.31 | -2.22 | 11.86 | -1.12 | 18.65 | 24.53 | False |  | distribution_warning | -0.97 | -3.02 | 1 | 0 | -5.66 | -2.3 | -18.77 | 16 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | -6.34 | -5.03 | 13.72 | 1.67 | 17.38 | 25.6 | False |  | distribution_warning | -0.97 | 0.0 | 0 | 0 | 1.05 | 0.47 | -14.53 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -5.62 | -22.31 | 49.09 | 38.93 | 56.87 | 68.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.82 | 0.36 | 1 | 1 | -11.58 | -9.67 | -30.28 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | -1.31 | -10.42 | -12.88 | 100.0 | 5.61 | 111.23 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -5.15 | -5.61 | -28.25 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 150.02313750823012 | 256.0946243793828 | -7.2 | -17.65 | 24.32 | 45.05 | 25.78 | 61.0 | False |  | distribution_warning | -2.07 | -1.23 | 0 | 0 | -11.29 | -11.74 | -39.47 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | 6.95 | 6.32 | 39.59 | 292.95 | 42.95 | 343.78 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | -0.28 | 1 | 0 | 8.78 | 7.4 | -12.12 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 170.41456580742187 | 44.354447130404274 | 3.08 | -1.63 | 21.7 | 79.46 | 20.36 | 83.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.94 | 0.23 | 0 | 1 | 0.67 | -1.57 | -27.96 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | -5.88 | -19.91 | -4.54 | 44.88 | 5.9 | 107.91 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -12.67 | -10.72 | -32.35 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 53.84760848458394 | 94.00659331121736 | -6.43 | -9.91 | 4.3 | 1.39 | 10.23 | 18.78 | False |  | distribution_warning | -1.56 | -1.54 | 0 | 0 | -6.11 | -5.1 | -27.61 | 11 | selected |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 76.00142700075368 | 64.57714379703859 | -8.81 | -17.36 | 9.68 | -5.18 | 17.24 | 25.13 | False |  | mild_accumulation | -0.04 | 0.14 | 1 | 1 | -11.31 | -10.89 | -29.79 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -2.45 | -2.97 | 5.59 | 12.54 | 7.16 | 16.56 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.64 | -1.78 | -23.13 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -8.04 | -14.43 | 5.37 | 64.47 | 11.2 | 92.52 | True | 距120日低點反彈>80% | distribution_warning | -0.91 | -0.37 | 0 | 1 | -11.78 | -9.43 | -30.76 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | -3.03 | -5.33 | 43.93 | 88.98 | 63.82 | 102.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | 0.87 | 1 | 1 | -8.77 | -5.54 | -21.57 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -6.39 | -30.08 | 21.04 | 29.49 | 21.69 | 49.51 | False |  | distribution_warning | -1.65 | -2.07 | 0 | 0 | -10.67 | -10.37 | -36.21 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -4.29 | -22.09 | -14.47 | 2.87 | 9.84 | 10.32 | False |  | distribution_warning | -4.18 | -0.18 | 0 | 0 | -12.81 | -11.5 | -33.44 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 57.64322627738095 | 26.63684630892036 | 2.66 | -14.47 | -38.23 | 37.82 | 17.14 | 42.61 | False |  | mild_accumulation | 0.47 | 0.89 | 1 | 1 | -5.43 | -4.37 | -41.17 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.789881691302135 | 33.96537207102099 | -3.54 | -15.67 | -25.24 | 27.76 | 10.72 | 53.41 | False |  | distribution_warning | -0.61 | -2.82 | 0 | 1 | -2.45 | -3.55 | -36.54 | 12 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 131.85418997881953 | 55.17736411171146 | 6.88 | 8.37 | 21.1 | 78.68 | 22.63 | 87.9 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.15 | -0.55 | 1 | 0 | 6.3 | 5.0 | -8.63 |  | fail_already_priced_in |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 80.93046018498126 | 44.798488379235415 | 3.3 | 6.19 | 10.18 | 7.83 | 16.84 | 23.34 | False |  | mild_accumulation | 0.72 | 0.49 | 1 | 1 | 3.2 | 2.46 | -12.17 | 20 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -7.62 | -4.19 | 8.42 | 69.55 | 21.53 | 94.34 | True | 距120日低點反彈>80% | strong_accumulation | 0.83 | 1.33 | 2 | 2 | -4.95 | -5.67 | -29.21 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -4.82 | -6.59 | -7.99 | -14.4 | 3.95 | 3.95 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -5.45 | -4.68 | -17.46 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -14.42 | -24.9 | -8.46 | 26.55 | 11.79 | 49.11 | False |  | distribution_warning | -1.54 | -3.03 | 1 | 0 | -17.09 | -14.48 | -31.6 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | 1.28 | -4.61 | 0.69 | -3.87 | 10.13 | 10.13 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -0.3 | -2.25 | -25.64 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 80.52350065869514 | 48.63403792846589 | 5.12 | 13.57 | 70.95 | 80.8 | 87.09 | 112.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.76 | -7.06 | 0 | 0 | 6.4 | 4.69 | -11.37 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 168.6655162496405 | 156.81600720436765 | -0.3 | -6.41 | 3.7 | 13.13 | 12.75 | 15.86 | False |  | strong_accumulation | 0.74 | 1.51 | 2 | 2 | -3.23 | -2.57 | -15.15 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | 8.98 | -10.44 | -11.15 | 97.25 | 11.91 | 100.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.74 | 0.0 | 1 | 0 | -3.0 | -3.99 | -29.87 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -19.92 | -0.99 | -26.94 | 20.3 | 7.24 | 76.02 | False |  | mild_accumulation | 6.3 | 6.47 | 1 | 2 | -11.78 | -12.08 | -33.88 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | 1.6 | 4.11 | 10.47 | 18.75 | 31.03 | 46.15 | False |  | mild_accumulation | 0.75 | 0.0 | 2 | 0 | 3.25 | 4.58 | -5.94 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | 7.19 | 3.35 | 9.83 | 13.89 | 17.32 | 19.36 | False |  | distribution_warning | -2.12 | -2.1 | 0 | 0 | 8.53 | 6.95 | -5.4 | 15 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 224.3279602768877 | 118.4530613441191 | 5.05 | -1.75 | 26.62 | 18.17 | 30.96 | 45.95 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 0 | 2.19 | 0.73 | -18.85 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2513.497664900037 | 792.7361428535551 | 6.55 | -12.1 | -0.87 | -2.98 | 8.07 | 8.07 | False |  | distribution_warning | -0.84 | -0.59 | 1 | 1 | 0.9 | 0.39 | -18.59 | 14 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | 1.84 | -0.9 | -8.68 | -19.64 | 8.07 | 8.07 | False |  | mild_accumulation | 0.06 | 0.0 | 1 | 0 | 1.03 | 0.85 | -9.05 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 124.2066375411972 | 34.20005594741868 | 1.13 | -2.67 | 3.89 | -3.61 | 10.32 | 10.32 | False |  | distribution_warning | -0.12 | -0.01 | 1 | 1 | 0.43 | 1.13 | -8.34 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 4.01 | 4.85 | 17.39 | 25.34 | 18.03 | 28.83 | False |  | strong_accumulation | 0.17 | 0.31 | 2 | 2 | 3.95 | 4.25 | -0.92 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 1322.1624507927131 | 667.7676077743706 | 3.42 | -0.64 | 1.41 | -10.84 | 12.88 | 12.88 | False |  | distribution_warning | -0.3 | -0.98 | 0 | 0 | 1.57 | 2.34 | -9.28 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | 4.09 | 2.09 | 55.59 | 91.49 | 61.38 | 132.6 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.0 | 0.37 | 1 | 1 | 5.24 | 7.01 | -2.17 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 73.30676173690114 | 58.7802399797441 | 4.26 | -9.69 | 28.78 | 31.6 | 31.16 | 62.45 | False |  | distribution_warning | -5.14 | -3.6 | 0 | 1 | -7.31 | -4.18 | -25.07 | 12 | selected |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 76.89914529735076 | 37.00041684126828 | 6.02 | -1.4 | 16.53 | 18.99 | 19.49 | 34.93 | False |  | distribution_warning | -1.45 | -1.85 | 0 | 0 | 3.92 | 3.11 | -12.96 |  | fail_low_response_condition |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 13.61 | 11.91 | 46.11 | 49.01 | 44.11 | 63.35 | True | 近60日漲幅>40% | neutral | 0.0 | 0.0 | 0 | 0 | 15.74 | 12.67 | -24.96 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | 9.65 | -2.73 | 22.76 | 146.08 | 33.5 | 149.53 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.13 | 0 | 0 | 4.14 | 2.44 | -20.65 |  | fail_low_response_condition |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 56.96595858063789 | 23.32960784964402 | -1.38 | 3.41 | 24.25 | 32.83 | 28.5 | 54.1 | False |  | mild_accumulation | 0.48 | -3.47 | 1 | 0 | 4.14 | 3.75 | -5.62 | 19 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -1.64 | -13.88 | -24.84 | 95.23 | 9.76 | 106.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.85 | 0.0 | 2 | 0 | -7.82 | -9.24 | -38.78 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -11.71 | 38.66 | 109.86 | 147.19 | 128.37 | 145.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.38 | 0.26 | 2 | 1 | 5.41 | 7.6 | -15.92 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -9.6 | -26.9 | -32.39 | 110.29 | 8.85 | 113.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.44 | -0.5 | 1 | 1 | -16.04 | -13.6 | -35.22 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | 5.36 | 1.29 | 20.13 | 100.64 | 32.82 | 140.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -2.44 | 0 | 0 | -3.21 | -1.63 | -27.74 |  | fail_already_priced_in |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | 18.23 | 9.93 | -4.02 | -5.22 | 20.11 | 33.53 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 12.36 | 9.98 | -12.69 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | -2.66 | 0.12 | -1.59 | -22.84 | 7.77 | 7.77 | False |  | distribution_warning | -0.34 | -0.87 | 0 | 0 | -1.77 | -0.92 | -11.84 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | 4.53 | -6.62 | 44.98 | 35.39 | 53.94 | 62.4 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.15 | 1.59 | 1 | 1 | -3.79 | 0.75 | -16.17 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 94.32153392330385 | 50.47184104059554 | -6.71 | 4.76 | 0.64 | -29.4 | 17.81 | 17.81 | False |  | mild_accumulation | 0.08 | 0.49 | 1 | 1 | -1.15 | -0.62 | -11.75 |  | fail_low_response_condition |