# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-14 06:23:09 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1946 |
| standardized_revenue_rows | 1946 |
| price_rows | 624319 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 389 |
| tdcc_mild_accumulation_count | 719 |
| tdcc_distribution_warning_count | 701 |
| revenue_condition_pass | 300 |
| price_metrics_pass | 299 |
| low_response_pass | 104 |
| already_priced_in_excluded | 49 |
| overheat_pass | 55 |
| score_pass | 55 |
| theme_priority_pass | 44 |
| final_rows | 44 |

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
| fail_revenue_condition | 1646 |
| fail_low_response_condition | 195 |
| fail_already_priced_in | 49 |
| fail_defensive_or_traditional_excluded | 7 |
| fail_non_mainstream_score_lt_11 | 4 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | -0.52 | 9.71 | 16.01 | 17.43 | 22.68 | 34.27 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | 3.85 | 2.09 | -12.13 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 101.96587437597796 | 132.1329440999445 | -5.94 | -4.63 | -13.45 | -29.21 | 3.0 | 3.0 | False |  | mild_accumulation | 0.49 | -0.41 | 2 | 0 | -2.6 | -2.1 | -14.17 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 68.32688588007737 | 39.48200784911037 | -1.34 | 0.0 | -4.74 | -6.36 | 3.27 | 3.27 | False |  | mild_accumulation | -0.41 | 0.02 | 1 | 1 | 0.34 | -0.11 | -7.14 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | 0.27 | -1.07 | 0.54 | -7.5 | 9.14 | 9.14 | False |  | mild_accumulation | 0.03 | 0.0 | 3 | 0 | 1.26 | 0.82 | -8.19 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -3.99 | -15.26 | -12.59 | -17.39 | 0.28 | 0.28 | False |  | mild_accumulation | 1.23 | 0.21 | 3 | 1 | -7.59 | -7.09 | -19.06 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 70.01963312430405 | 44.542976125957246 | -0.65 | -1.62 | -6.32 | -34.2 | 6.48 | 6.48 | False |  | distribution_warning | -0.03 | -0.35 | 1 | 1 | -0.6 | -0.65 | -12.01 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -26.81 | 15.62 | 67.84 | 85.0 | 84.59 | 85.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.97 | -2.1 | 1 | 1 | -11.07 | -4.64 | -33.4 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral |  | 162537.27465535526 | 17993.11726781669 | 1.32 | -1.28 | 2.84 | -9.28 | 9.8 | 9.8 | False |  | mild_accumulation | 0.03 | -0.12 | 2 | 0 | -0.19 | 0.95 | -7.09 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -13.19 | -14.75 | -2.47 | -2.47 | 10.75 | 14.49 | False |  | mild_accumulation | 0.29 | 0.0 | 2 | 0 | -11.7 | -9.03 | -25.24 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | 1.0 | 26.25 | 109.6 | 144.48 | 131.19 | 181.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.42 | -1.23 | 1 | 2 | 8.23 | 10.87 | -5.61 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | -1.7 | -20.6 | -21.68 |  | 0.7 |  | False |  | mild_accumulation | -0.66 | 0.12 | 1 | 1 | -10.44 | -9.28 | -30.19 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 3.44 | 4.7 | -1.99 | -6.5 | 17.12 | 17.12 | False |  | mild_accumulation | 0.21 | -0.05 | 2 | 1 | 5.59 | 5.37 | -2.4 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | 0.39 | 0.19 | 0.39 | 5.5 | 5.28 | 5.71 | False |  | strong_accumulation | 1.38 | 0.61 | 3 | 3 | 0.99 | 0.95 | -2.45 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | -5.43 | 29.85 | 34.88 | 55.36 | 38.1 | 72.28 | True | 近20日漲幅>25% | mild_accumulation | 0.6 | -0.84 | 1 | 1 | 13.93 | 10.71 | -8.18 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral | B_可觀察 | 125.11209715086407 | 47.06150242210431 | -14.92 | 1.12 | 39.41 | 15.88 | 37.76 | 50.0 | False |  | mild_accumulation | 2.3 | 3.91 | 2 | 1 | -11.14 | -6.63 | -26.36 | 16 | selected |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 106.58847855421364 | 47.886498368081 | -2.44 | 0.9 | 0.54 | 12.93 | 5.47 | 21.26 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | -0.83 | -1.12 | -9.98 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | 2.06 | 73.3 | 112.9 | 191.18 | 162.25 | 237.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 1.81 | 3 | 3 | 10.92 | 15.66 | -7.15 |  | fail_low_response_condition |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth |  | 55.42638489110967 | 41.01765691988111 | -8.92 | -12.5 | -6.2 | 83.5 | 5.59 | 84.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.33 | -1.2 | 0 | 0 | -6.46 | -6.73 | -26.89 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | -1.66 | -8.51 | 12.09 | 4.42 | 11.29 | 26.13 | False |  | distribution_warning | -1.47 | -1.46 | 0 | 0 | -6.21 | -5.64 | -24.68 | 10 | selected |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 67.86685548491262 | 35.613194655616326 | -0.2 | 8.44 | 19.02 | 42.69 | 19.61 | 45.24 | False |  | distribution_warning | -0.08 | -0.09 | 1 | 1 | 0.8 | 1.39 | -3.75 | 17 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | -3.16 | -1.43 | 4.15 | 126.6 | 11.29 | 133.11 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -2.06 | 2 | 1 | -11.11 | -8.47 | -28.12 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | -9.49 | 6.71 | 83.32 | 67.33 | 98.81 | 99.28 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.41 | -0.45 | 1 | 1 | -13.86 | -7.93 | -28.48 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -12.07 | 5.71 | 9.82 | 103.81 | 19.65 | 120.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.48 | 0.4 | 3 | 3 | -3.32 | -3.29 | -14.87 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth |  | 135.4532611228886 | 77.39100370968649 | -12.97 | -9.14 | -2.71 | 27.51 | 4.3 | 29.72 | False |  | strong_accumulation | 0.42 | 0.36 | 3 | 3 | -9.91 | -8.62 | -16.07 |  | fail_low_response_condition |
| 2348 | 海悅 | 其他 | neutral |  | 247.66387451562755 | -4.129081203674164 | 1.18 | 5.92 | -0.65 | -4.23 | 14.09 | 14.09 | False |  | distribution_warning | -1.62 | -1.91 | 0 | 1 | 4.45 | 4.43 | -3.75 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | 1.45 | 16.94 | 39.4 | 187.57 | 51.99 | 187.57 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.77 | -2.98 | 1 | 0 | 4.08 | 3.6 | -9.66 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 61.61746792060725 | 36.83107001078034 | -4.29 | -1.07 | 36.64 | 49.25 | 43.3 | 67.83 | False |  | distribution_warning | -0.43 | -0.48 | 1 | 1 | -2.8 | -2.78 | -26.98 | 10 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 4.3 | -10.2 | 17.53 | 35.91 | 21.17 | 43.67 | False |  | distribution_warning | -1.56 | -1.68 | 0 | 0 | -3.38 | -2.21 | -26.97 | 10 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | -18.32 | -15.53 | -8.64 | 88.01 | 3.35 | 99.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.87 | 1 | 1 | -14.02 | -13.5 | -33.81 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 74.79882516895688 | 99.90714739063372 | -7.22 | 16.13 | 14.51 | 33.54 | 27.93 | 43.48 | False |  | mild_accumulation | 2.17 | 2.99 | 1 | 2 | -1.84 | -1.42 | -13.93 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -19.92 | -22.3 | -14.69 | 59.54 | 0.48 | 76.22 | False |  | distribution_warning | -0.56 | -0.29 | 2 | 2 | -15.73 | -14.83 | -33.86 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | -0.89 | -1.32 | 16.29 | 42.46 | 24.03 | 62.47 | False |  | distribution_warning | -0.68 | -1.09 | 1 | 1 | -0.56 | -0.69 | -16.54 | 12 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 102.87247195164616 | 86.48475082849643 | 0.27 | 2.16 | 11.18 | 35.48 | 31.02 | 40.78 | False |  | mild_accumulation | -0.08 | 0.04 | 1 | 1 | 1.61 | 2.18 | -13.7 | 20 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -15.71 | 0.59 | 29.75 | 213.46 | 31.58 | 231.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.1 | 1.48 | 2 | 3 | -5.36 | -3.85 | -18.0 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | 2.88 | 15.52 | 47.05 | 86.76 | 54.02 | 95.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.37 | 0.03 | 2 | 1 | 7.75 | 6.82 | -9.61 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 50.90083303173535 | 76.24247572692803 | -8.89 | 2.93 | 23.0 | 13.89 | 30.16 | 49.82 | False |  | strong_accumulation | 1.5 | 0.92 | 2 | 2 | -5.09 | -2.51 | -15.17 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.99850390624209 | 133.4952742541738 | -9.72 | -5.71 | 10.24 | 20.42 | 31.97 | 40.19 | False |  | distribution_warning | -3.53 | -3.16 | 1 | 1 | -1.64 | -1.55 | -19.15 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | 3.3 | 24.41 | 92.27 | 83.91 | 112.56 | 113.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.17 | 1 | 1 | -2.09 | 2.61 | -16.24 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 87.26211992785133 | 46.19747329391832 | 3.74 | 1.27 | 41.15 | 54.85 | 42.41 | 58.9 | True | 近60日漲幅>40% | mild_accumulation | 0.5 | -0.02 | 2 | 0 | 4.59 | 6.95 | -5.76 |  | fail_already_priced_in |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | -5.78 | -6.7 | -58.03 | -70.06 | 0.95 | 0.95 | False |  | distribution_warning | -1.23 | -0.08 | 0 | 0 | -6.8 | -11.67 | -65.24 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 375.5658851662359 | 116.51091844759344 | 4.01 | 20.85 | 41.19 | 41.87 | 55.11 | 75.5 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.29 | -0.26 | 2 | 2 | 8.36 | 10.14 | -5.27 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 18.37 | 110.48 | 125.04 | 126.91 | 137.98 | 139.65 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 46.7 | 42.68 | 0.0 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 55.96076128364229 | 23.255026779465105 | -3.74 | -2.9 | -0.3 | 11.3 | 7.72 | 21.38 | False |  | strong_accumulation | 0.29 | 0.38 | 2 | 2 | -1.14 | -1.76 | -25.72 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 220.09287723199685 | 399.98004177172845 | -2.28 | -2.53 | 1.32 | -20.94 | 7.54 | 7.54 | False |  | mild_accumulation | 0.08 | -0.13 | 2 | 1 | -1.16 | -0.59 | -5.87 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 381.5468504599107 | 422.1697253819397 | -3.99 | -13.53 | -4.9 | 5.43 | 4.55 | 31.85 | False |  | distribution_warning | -2.76 | -1.71 | 1 | 0 | -10.09 | -9.45 | -34.07 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 59.07699165913917 | 62.47100752006232 | -13.68 | 8.96 | -13.0 | 48.01 | 15.15 | 64.37 | False |  | distribution_warning | -0.06 | -1.16 | 1 | 0 | -7.47 | -5.98 | -20.36 | 11 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 543.886650237175 | 158.17460116324747 | 17.03 | 13.18 | 27.07 | 49.39 | 32.56 | 79.14 | False |  | distribution_warning | -0.29 | 0.0 | 2 | 1 | 10.91 | 9.46 | -8.42 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | -3.25 | 9.78 | 6.25 | 131.97 | 22.68 | 158.13 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 4.33 | 2 | 2 | 0.02 | -0.19 | -14.02 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.76248321707817 | 36.92164743994052 | -4.89 | 6.3 | 3.69 | 39.78 | 17.13 | 75.21 | False |  | mild_accumulation | 2.55 | 1.02 | 3 | 1 | -1.27 | -0.9 | -9.64 | 17 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -7.56 | -23.53 | -31.47 | 63.8 | 1.12 | 53.17 | False |  | mild_accumulation | 0.1 | -0.58 | 2 | 2 | -11.51 | -12.3 | -36.96 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | 1.32 | -2.22 | 10.79 | 20.08 | 17.11 | 54.19 | False |  | mild_accumulation | -0.88 | 0.61 | 0 | 3 | 2.3 | 1.72 | -12.99 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | -0.34 | -2.09 | 0.0 | -1.77 | 5.71 | 5.71 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.07 | 0.25 | -2.84 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | 1.19 | 5.2 | 4.55 | -0.58 | 12.73 | 12.73 | False |  | strong_accumulation | 0.25 | 0.06 | 3 | 3 | 2.97 | 3.04 | -2.63 | 19 | selected |
| 2520 | 冠德 | 建材營造 | neutral |  | 52.3105385295913 | 31.38789796597349 | 1.43 | 5.84 | 11.69 | 5.21 | 24.04 | 24.04 | False |  | strong_accumulation | 0.52 | 0.68 | 2 | 3 | 1.72 | 3.35 | -5.35 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 365.123018807587 | 2533.2289075556096 | 10.8 | 31.94 | 25.93 | 42.88 | 39.6 | 65.7 | True | 近20日漲幅>25% | strong_accumulation | 0.36 | 0.45 | 2 | 2 | 12.54 | 13.29 | -1.83 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 79.55310359840207 | 22.58855338149928 | 4.2 | 5.27 | -9.7 | -15.31 | 23.72 | 23.72 | False |  | mild_accumulation | -0.05 | 0.06 | 1 | 1 | 4.43 | 4.75 | -11.56 | 15 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | D_降級_TDCC轉弱 | 105.33076260323196 | 54.8064697471788 | 1.4 | -15.06 | -24.0 | -37.1 | 7.29 | 7.29 | False |  | distribution_warning | -0.56 | -0.76 | 1 | 1 | -3.19 | -3.17 | -24.29 | 13 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | -2.16 | 2.73 | 6.1 | 3.2 | 15.19 | 15.19 | False |  | strong_accumulation | 0.9 | 0.82 | 2 | 2 | 1.32 | 2.06 | -4.24 | 22 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | 1.75 | 6.59 | 0.34 | -3.32 | 15.48 | 15.48 | False |  | strong_accumulation | 0.48 | 0.06 | 3 | 2 | 4.23 | 4.1 | -2.02 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround |  | 57.91908933878501 | 32.316290442538865 | 14.0 | 8.17 | 13.24 | 19.13 | 20.48 | 27.95 | False |  | distribution_warning | -0.65 | -0.96 | 0 | 0 | 10.29 | 9.66 | -3.75 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 199.0184261973224 | 334.18209408719963 | -4.34 | -2.46 | 48.43 | 82.87 | 49.55 | 84.57 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.94 | -0.53 | 1 | 1 | -2.31 | -1.08 | -16.97 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 294.84268843595487 | 170.38806261042123 | 5.12 | 23.39 | 6.88 | 37.23 | 45.2 | 68.62 | False |  | mild_accumulation | 0.05 | 0.06 | 3 | 1 | 10.43 | 10.06 | -3.04 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 328.3542479788894 | 242.62430701861496 | 7.8 | 11.49 | 41.61 | 55.63 | 51.5 | 72.73 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.2 | 1.06 | 2 | 2 | 0.23 | 0.99 | -16.64 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 66.11083679678092 | 85.45932489486553 | -19.38 | -4.71 | -13.26 | 65.43 | 0.68 | 75.89 | False |  | strong_accumulation | 0.82 | 1.09 | 2 | 3 | -9.28 | -10.11 | -26.08 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | 0.42 | 0.0 | 10.09 | 5.26 | 29.73 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.61 | 2.41 | -4.76 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -13.17 | -4.04 | 16.15 | 74.51 | 20.27 | 78.22 | True | 近120日漲幅>70% | strong_accumulation | 0.85 | 0.75 | 2 | 2 | -8.86 | -8.73 | -19.37 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth |  | 54.44557676970354 | 26.196636563481785 | 0.99 | 2.41 | 46.05 | 66.07 | 49.71 | 78.91 | True | 近60日漲幅>40% | strong_accumulation | 1.08 | 1.51 | 2 | 3 | 2.34 | 2.47 | -7.96 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 188.0864822148371 | 114.02783651203414 | -4.74 | -9.25 | -2.99 | 39.27 | 7.11 | 46.53 | False |  | distribution_warning | -1.73 | -1.77 | 0 | 0 | -3.13 | -6.19 | -31.49 | 17 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 167.50830564784053 | 42.89095493442987 | -10.42 | 6.39 | 4.24 | -1.53 | 15.96 | 21.7 | False |  | mild_accumulation | 3.85 | 0.41 | 2 | 1 | -7.73 | -5.18 | -20.62 | 20 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | 3.04 | -2.34 | 10.48 | 1.5 | 16.52 | 24.68 | False |  | distribution_warning | -0.99 | 0.0 | 0 | 0 | -0.26 | -0.4 | -15.16 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -10.87 | -23.47 | 46.43 | 40.17 | 57.69 | 69.57 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -1.72 | -1.32 | 1 | 1 | -13.38 | -11.03 | -29.91 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | -6.22 | -10.27 | -19.6 | 107.57 | 1.52 | 111.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | -6.18 | -6.61 | -28.13 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 150.02313750823012 | 256.0946243793828 | -10.57 | -14.51 | 33.06 | 45.37 | 33.06 | 65.0 | False |  | distribution_warning | -2.8 | -1.3 | 0 | 0 | -10.86 | -11.77 | -37.97 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | -5.82 | -2.48 | 31.95 | 242.03 | 34.97 | 310.95 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.37 | 0.53 | 1 | 1 | 1.46 | 0.63 | -18.62 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 170.41456580742187 | 44.354447130404274 | -0.5 | -3.07 | 23.25 | 80.69 | 24.92 | 82.62 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.11 | -0.38 | 0 | 1 | -0.3 | -2.76 | -28.43 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | -10.41 | -9.99 | 3.23 | 43.71 | 10.22 | 116.38 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -10.64 | -9.01 | -29.6 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 53.84760848458394 | 94.00659331121736 | -9.75 | -5.9 | -0.69 | 0.0 | 8.71 | 17.14 | False |  | distribution_warning | -2.07 | -2.1 | 0 | 0 | -8.28 | -7.47 | -28.61 | 11 | selected |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 76.00142700075368 | 64.57714379703859 | -9.19 | -11.79 | 5.11 | 2.07 | 21.67 | 29.86 | False |  | distribution_warning | -0.15 | -0.69 | 1 | 1 | -9.64 | -9.37 | -27.14 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -1.36 | -6.43 | 9.64 | 26.83 | 10.3 | 30.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.75 | -0.96 | -22.06 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -15.28 | 4.02 | 14.32 | 76.45 | 16.67 | 99.53 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.97 | 0.31 | 0 | 2 | -9.59 | -7.96 | -28.24 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | -2.83 | 13.81 | 35.53 | 106.41 | 75.77 | 117.3 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.79 | 0.99 | 1 | 2 | -2.23 | 0.23 | -15.85 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -6.07 | -20.68 | 26.6 | 33.72 | 27.12 | 52.63 | False |  | distribution_warning | -1.3 | -1.68 | 1 | 1 | -11.78 | -10.36 | -34.88 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -14.16 | -19.35 | -21.88 | 16.96 | 1.42 | 18.48 | False |  | distribution_warning | -3.33 | -0.26 | 1 | 0 | -15.24 | -13.86 | -33.77 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 57.64322627738095 | 26.63684630892036 | -6.58 | -11.74 | -40.5 | 33.68 | 14.11 | 38.91 | False |  | mild_accumulation | 1.14 | 0.77 | 2 | 1 | -9.41 | -8.13 | -43.8 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.789881691302135 | 33.96537207102099 | -6.52 | -13.66 | -24.19 | 33.69 | 2.47 | 49.8 | False |  | distribution_warning | -1.04 | -2.07 | 0 | 2 | -6.87 | -7.02 | -38.04 | 11 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 131.85418997881953 | 55.17736411171146 | 6.36 | 7.83 | 14.15 | 82.24 | 25.81 | 88.71 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.54 | -1.12 | 1 | 0 | 7.91 | 6.73 | -8.24 |  | fail_already_priced_in |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 80.93046018498126 | 44.798488379235415 | -0.22 | 4.97 | 6.82 | 6.45 | 16.71 | 23.2 | False |  | distribution_warning | -0.6 | -0.74 | 1 | 1 | 3.64 | 2.7 | -12.27 | 15 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -5.84 | 6.62 | 7.99 | 91.32 | 23.6 | 97.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.04 | 1.11 | 2 | 2 | -3.52 | -5.23 | -28.01 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -1.51 | 2.98 | -2.98 | -3.45 | 10.34 | 10.34 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -0.35 | 0.08 | -12.39 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -16.39 | -23.16 | 2.71 | 31.44 | 15.31 | 53.81 | False |  | distribution_warning | -3.16 | -5.47 | 1 | 0 | -16.75 | -14.2 | -29.44 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | -1.25 | -4.28 | -3.11 | -3.54 | 10.38 | 10.38 | False |  | distribution_warning | -1.15 | 0.0 | 1 | 0 | -0.64 | -2.65 | -25.47 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 80.52350065869514 | 48.63403792846589 | 2.61 | 3.06 | 75.6 | 90.32 | 95.36 | 121.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.47 | -11.35 | 0 | 0 | 11.95 | 10.03 | -7.45 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 168.6655162496405 | 156.81600720436765 | -6.85 | 1.19 | -4.23 | 16.44 | 14.09 | 17.24 | False |  | strong_accumulation | 1.85 | 2.88 | 3 | 3 | -2.68 | -1.94 | -14.14 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | 1.64 | -10.33 | -9.83 | 108.26 | 14.47 | 107.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.63 | -0.04 | 1 | 0 | -1.99 | -2.56 | -28.27 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -25.16 | 5.22 | -22.35 | 50.36 | 10.86 | 81.96 | True | 距120日低點反彈>80% | mild_accumulation | 5.82 | 6.03 | 1 | 2 | -8.83 | -11.15 | -33.84 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | 0.27 | -2.88 | 7.54 | 21.24 | 27.93 | 42.69 | False |  | mild_accumulation | 0.66 | 0.0 | 2 | 0 | 0.76 | 2.56 | -8.17 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | 4.66 | -0.81 | 2.15 | 10.05 | 12.07 | 14.02 | False |  | distribution_warning | -2.9 | -2.11 | 0 | 0 | 3.89 | 3.11 | -9.63 | 16 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth | B_可觀察 | 224.3279602768877 | 118.4530613441191 | 3.36 | -1.11 | 25.38 | 26.51 | 34.66 | 50.08 | False |  | mild_accumulation | 0.58 | -0.04 | 1 | 0 | 4.79 | 3.73 | -16.55 | 20 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 2513.497664900037 | 792.7361428535551 | 2.96 | -17.38 | -5.3 | -8.58 | 4.59 | 4.59 | False |  | distribution_warning | -0.72 | -0.54 | 2 | 2 | -3.9 | -2.87 | -21.22 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | 1.83 | 0.45 | -11.2 | -18.53 | 8.56 | 8.56 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | 1.38 | 1.45 | -11.55 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 124.2066375411972 | 34.20005594741868 | -1.37 | -3.17 | 2.58 | -4.11 | 9.22 | 9.22 | False |  | distribution_warning | -0.22 | -0.07 | 1 | 1 | -0.96 | 0.25 | -9.26 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 3.07 | 5.63 | 14.34 | 22.69 | 16.21 | 26.84 | False |  | strong_accumulation | 0.24 | 0.34 | 3 | 3 | 2.76 | 3.3 | -2.45 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 1322.1624507927131 | 667.7676077743706 | 1.21 | -2.74 | 2.67 | -12.52 | 10.95 | 10.95 | False |  | distribution_warning | -0.26 | -0.89 | 1 | 1 | -0.32 | 0.87 | -10.83 | 17 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | -6.29 | 9.33 | 38.62 | 88.38 | 52.0 | 119.09 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.14 | 0.06 | 1 | 1 | -0.85 | 1.37 | -7.86 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 73.30676173690114 | 58.7802399797441 | 3.5 | 4.41 | 21.41 | 42.02 | 40.58 | 71.78 | False |  | distribution_warning | -3.88 | -1.82 | 1 | 2 | -2.69 | 0.55 | -20.77 | 11 | selected |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | D_降級_TDCC轉弱 | 76.89914529735076 | 37.00041684126828 | 5.62 | -0.7 | 10.59 | 20.51 | 19.49 | 34.93 | False |  | distribution_warning | -2.56 | -2.33 | 0 | 0 | 3.66 | 3.69 | -12.96 | 13 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 1.04 | 4.76 | 39.88 | 47.11 | 35.2 | 50.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 7.48 | 5.54 | -30.96 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | 0.39 | -4.95 | 3.81 | 142.06 | 29.5 | 142.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.44 | -3.36 | 0 | 0 | 0.44 | -0.84 | -23.03 |  | fail_already_priced_in |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 56.96595858063789 | 23.32960784964402 | 3.46 | -1.65 | 24.32 | 34.66 | 26.55 | 51.76 | False |  | distribution_warning | -0.05 | -1.64 | 1 | 1 | 2.76 | 2.48 | -7.06 | 14 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -9.45 | -6.91 | -27.78 | 108.0 | 2.54 | 108.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.33 | 0.0 | 2 | 0 | -7.93 | -10.04 | -38.1 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -10.39 | 33.83 | 92.31 | 141.31 | 116.26 | 139.92 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.64 | 0.12 | 3 | 1 | 2.35 | 2.46 | -20.38 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -25.51 | -15.42 | -31.17 | 113.77 | 0.2 | 116.91 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.99 | 0.36 | 1 | 2 | -17.16 | -14.58 | -35.81 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | -9.52 | 0.34 | 24.03 | 87.61 | 25.77 | 128.1 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.89 | 0.16 | 0 | 1 | -8.63 | -7.88 | -31.57 |  | fail_already_priced_in |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | 5.25 | 7.12 | -8.68 | -12.66 | 11.38 | 23.82 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 5.36 | 3.87 | -24.14 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | -3.14 | 4.43 | -0.5 | -20.91 | 7.51 | 7.51 | False |  | distribution_warning | -0.35 | -0.52 | 0 | 1 | -1.98 | -1.46 | -12.06 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | -7.81 | -0.4 | 35.96 | 37.93 | 50.3 | 58.57 | True | 距60日低點反彈>50% | mild_accumulation | 0.27 | 1.59 | 2 | 1 | -6.75 | -1.6 | -18.15 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 83.5074318744839 | 81.11545407527365 | 7.81 | 1.43 | 11.69 | 6.2 | 15.85 | 15.85 | False |  | strong_accumulation | 0.07 | 0.12 | 2 | 2 | 5.9 | 5.75 | -3.87 |  | fail_low_response_condition |
| 6672 | 騰輝電子-KY | 電子零組件業 | mainstream_growth |  | 68.12346641728693 | 34.54799350529283 | -12.7 | 28.81 | 46.67 | 199.56 | 58.05 | 224.68 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 8.92 | 3.83 | 2 | 1 | 0.52 | 1.15 | -16.67 |  | fail_already_priced_in |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 115.18509399137636 | 84.28516773674946 | -4.86 | 13.81 | 7.09 | 20.03 | 22.88 | 30.63 | False |  | strong_accumulation | 1.94 | 1.26 | 3 | 2 | -2.19 | 0.25 | -13.07 |  | fail_low_response_condition |