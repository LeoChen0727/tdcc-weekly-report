# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-15 14:05:14 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1952 |
| standardized_revenue_rows | 1952 |
| price_rows | 626280 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 221 |
| tdcc_mild_accumulation_count | 850 |
| tdcc_distribution_warning_count | 707 |
| revenue_condition_pass | 301 |
| price_metrics_pass | 300 |
| low_response_pass | 105 |
| already_priced_in_excluded | 42 |
| overheat_pass | 63 |
| score_pass | 63 |
| theme_priority_pass | 52 |
| final_rows | 52 |

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
| fail_low_response_condition | 195 |
| fail_already_priced_in | 42 |
| fail_defensive_or_traditional_excluded | 8 |
| fail_non_mainstream_score_lt_11 | 3 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | -6.53 | 4.49 | 13.76 | 11.04 | 18.85 | 30.07 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | 0.39 | -1.01 | -14.87 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 101.96587437597796 | 132.1329440999445 | -5.12 | -9.73 | -12.82 | -31.54 | 2.0 | 2.0 | False |  | mild_accumulation | 0.55 | -0.38 | 2 | 0 | -3.04 | -2.81 | -13.92 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 68.32688588007737 | 39.48200784911037 | 0.0 | 1.36 | -2.61 | -5.49 | 4.67 | 4.67 | False |  | mild_accumulation | -0.85 | 0.07 | 0 | 1 | 1.63 | 1.14 | -5.88 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | 0.54 | 0.81 | 2.75 | -6.52 | 10.03 | 10.03 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 2.04 | 1.5 | -7.44 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -6.17 | -18.6 | -14.63 | -20.45 | 1.45 | 1.45 | False |  | mild_accumulation | 1.02 | 0.0 | 2 | 0 | -9.48 | -9.17 | -21.52 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral | D_降級_TDCC轉弱 | 70.01963312430405 | 44.542976125957246 | -2.29 | -3.86 | -7.44 | -37.42 | 4.55 | 4.55 | False |  | distribution_warning | -0.03 | 0.0 | 1 | 1 | -2.21 | -2.25 | -13.6 | 11 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -18.42 | 12.17 | 74.69 | 86.75 | 89.02 | 89.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.62 | 1 | 1 | -9.38 | -2.16 | -31.8 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 162537.27465535526 | 17993.11726781669 | -2.54 | -3.76 | 3.37 | -9.71 | 9.45 | 9.45 | False |  | distribution_warning | -0.04 | -0.1 | 1 | 0 | -0.32 | 0.57 | -7.39 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -13.75 | -17.73 | -2.11 | -4.53 | 8.41 | 12.08 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | -12.75 | -10.13 | -26.81 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | 2.7 | 15.7 | 103.18 | 139.01 | 128.76 | 178.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.1 | -2.21 | 1 | 1 | 6.32 | 8.82 | -6.6 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | -4.41 | -22.53 | -22.53 |  | 1.81 |  | False |  | mild_accumulation | -0.67 | 0.12 | 0 | 1 | -11.49 | -10.62 | -31.88 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 0.15 | 2.55 | -2.15 | -8.56 | 15.93 | 15.93 | False |  | mild_accumulation | 0.11 | 0.24 | 1 | 1 | 4.39 | 3.93 | -2.56 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | 0.58 | -1.7 | -0.95 | 4.84 | 5.69 | 6.12 | False |  | strong_accumulation | 0.95 | 0.58 | 3 | 3 | 1.47 | 1.23 | -2.07 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | -8.7 | 27.27 | 29.23 | 50.67 | 33.33 | 66.34 | True | 近20日漲幅>25% | distribution_warning | -0.29 | -0.74 | 0 | 1 | 8.72 | 6.28 | -11.35 |  | fail_already_priced_in |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 125.11209715086407 | 47.06150242210431 | -15.21 | -8.82 | 23.0 | 9.62 | 33.22 | 45.56 | False |  | mild_accumulation | 0.43 | -0.92 | 1 | 0 | -13.41 | -8.68 | -28.55 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral | D_降級_TDCC轉弱 | 106.58847855421364 | 47.886498368081 | 4.24 | 8.29 | 6.78 | 24.67 | 15.85 | 33.19 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | 8.47 | 7.84 | -1.13 | 15 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | -13.36 | 47.21 | 106.42 | 147.16 | 144.7 | 214.47 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.29 | 2 | 2 | 1.8 | 7.21 | -13.36 |  | fail_already_priced_in |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth |  | 55.42638489110967 | 41.01765691988111 | -7.02 | -16.25 | -7.94 | 75.0 | 4.21 | 80.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -1.0 | 0 | 0 | -7.37 | -7.8 | -28.24 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | -2.69 | -9.6 | 6.56 | 0.43 | 8.03 | 25.6 | False |  | distribution_warning | -1.42 | -1.44 | 0 | 0 | -6.14 | -5.56 | -25.0 | 10 | selected |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 67.86685548491262 | 35.613194655616326 | -1.63 | 4.76 | 18.05 | 41.52 | 17.76 | 44.05 | False |  | distribution_warning | -0.11 | -0.13 | 0 | 0 | -0.26 | 0.51 | -4.54 | 17 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | -3.46 | -4.78 | 3.72 | 132.11 | 12.5 | 133.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -2.01 | 1 | 1 | -9.94 | -6.89 | -27.34 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | -10.11 | -4.36 | 81.57 | 64.83 | 95.83 | 96.3 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.28 | -3.23 | 0 | 0 | -14.99 | -8.6 | -29.55 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -13.8 | -2.36 | 3.64 | 87.65 | 13.43 | 109.17 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.3 | 0.29 | 2 | 2 | -8.24 | -7.68 | -19.29 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 135.4532611228886 | 77.39100370968649 | -11.41 | -6.73 | -1.07 | 25.72 | 5.06 | 30.66 | False |  | strong_accumulation | 0.33 | 0.31 | 2 | 2 | -8.96 | -7.34 | -15.46 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 247.66387451562755 | -4.129081203674164 | -0.39 | 4.4 | -1.04 | -7.32 | 12.76 | 12.76 | False |  | distribution_warning | -0.89 | -0.77 | 0 | 1 | 3.0 | 2.94 | -4.88 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | -14.69 | 6.28 | 17.17 | 157.28 | 40.43 | 161.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.86 | -2.6 | 0 | 0 | -4.1 | -3.94 | -16.52 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 61.61746792060725 | 36.83107001078034 | -5.21 | -3.78 | 33.4 | 44.28 | 41.09 | 65.24 | False |  | distribution_warning | -0.18 | -0.33 | 1 | 1 | -4.12 | -3.94 | -28.1 | 12 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 3.38 | -10.45 | 15.44 | 33.14 | 21.0 | 43.47 | False |  | distribution_warning | -1.53 | -1.29 | 0 | 0 | -2.97 | -2.16 | -27.07 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | -16.51 | -20.7 | -10.34 | 84.02 | 5.2 | 96.12 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -1.49 | 1 | 0 | -14.47 | -13.83 | -34.88 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 74.79882516895688 | 99.90714739063372 | -9.08 | 6.15 | 4.02 | 25.58 | 21.29 | 36.04 | False |  | mild_accumulation | 2.17 | 2.57 | 1 | 1 | -7.19 | -6.03 | -18.4 | 16 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -17.14 | -23.11 | -18.8 | 49.71 | 6.28 | 71.16 | False |  | distribution_warning | -0.59 | -0.4 | 1 | 1 | -17.13 | -16.07 | -35.76 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | -0.74 | -2.34 | 17.19 | 35.22 | 23.48 | 61.74 | False |  | distribution_warning | -0.53 | -1.27 | 1 | 0 | -0.88 | -1.04 | -16.92 | 12 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 102.87247195164616 | 86.48475082849643 | 0.53 | 2.15 | 13.43 | 32.87 | 31.72 | 41.53 | False |  | mild_accumulation | 0.06 | 0.08 | 1 | 1 | 2.04 | 2.49 | -13.24 | 20 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -9.22 | 2.9 | 22.26 | 197.6 | 25.03 | 221.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.11 | 1.44 | 1 | 2 | -8.34 | -6.23 | -20.48 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | 2.72 | 11.84 | 46.54 | 80.85 | 52.01 | 92.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.44 | 0.17 | 2 | 1 | 5.75 | 4.95 | -10.79 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 50.90083303173535 | 76.24247572692803 | -10.23 | -9.54 | 18.5 | 3.04 | 25.4 | 44.34 | False |  | mild_accumulation | 0.44 | -0.21 | 1 | 1 | -8.12 | -5.6 | -18.28 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.99850390624209 | 133.4952742541738 | -15.92 | -10.64 | 7.07 | 9.42 | 23.8 | 31.51 | False |  | distribution_warning | -0.63 | -0.39 | 1 | 1 | -7.22 | -7.05 | -24.16 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | 6.54 | 19.79 | 104.57 | 89.43 | 125.13 | 125.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.21 | 0 | 0 | 2.81 | 7.9 | -11.29 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth | A_優先追蹤 | 87.26211992785133 | 46.19747329391832 | 3.08 | 3.92 | 36.63 | 54.37 | 41.96 | 58.41 | False |  | mild_accumulation | 0.56 | -0.01 | 2 | 0 | 4.06 | 6.03 | -6.06 | 21 | selected |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | -8.1 | -6.03 | -63.46 | -73.97 | 1.88 | 1.88 | False |  | distribution_warning | -1.13 | -0.04 | 0 | 0 | -10.62 | -14.43 | -66.76 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 375.5658851662359 | 116.51091844759344 | 6.37 | 23.09 | 43.9 | 41.15 | 55.81 | 76.29 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.13 | -0.87 | 1 | 1 | 7.75 | 9.67 | -7.91 |  | fail_already_priced_in |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 38.31 | 131.08 | 148.68 | 150.33 | 161.67 | 163.51 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 54.25 | 49.78 | 0.0 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 55.96076128364229 | 23.255026779465105 | -11.94 | -9.17 | -3.06 | 4.28 | 2.26 | 14.86 | False |  | strong_accumulation | 0.42 | 0.47 | 2 | 2 | -6.0 | -6.49 | -29.71 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 220.09287723199685 | 399.98004177172845 | -3.54 | -3.78 | 2.69 | -22.67 | 6.7 | 6.7 | False |  | distribution_warning | -0.15 | -0.44 | 1 | 0 | -1.74 | -1.26 | -6.6 | 15 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 381.5468504599107 | 422.1697253819397 | -11.65 | -21.77 | -11.15 | -0.62 | 3.69 | 24.8 | False |  | distribution_warning | -2.89 | -1.7 | 0 | 0 | -13.87 | -13.26 | -37.6 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 59.07699165913917 | 62.47100752006232 | -19.37 | 0.95 | -19.16 | 40.0 | 9.64 | 56.51 | False |  | mild_accumulation | 0.33 | -0.77 | 1 | 0 | -11.93 | -9.69 | -24.17 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 543.886650237175 | 158.17460116324747 | 12.45 | 10.98 | 19.07 | 46.38 | 31.02 | 77.06 | False |  | distribution_warning | -0.61 | -1.14 | 1 | 0 | 9.03 | 7.45 | -9.49 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | -18.17 | -2.9 | -10.22 | 111.02 | 10.52 | 132.54 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.84 | 1 | 1 | -9.78 | -9.33 | -22.54 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.76248321707817 | 36.92164743994052 | -10.29 | -0.81 | 0.41 | 30.9 | 12.96 | 68.98 | False |  | mild_accumulation | 1.78 | 1.08 | 2 | 1 | -4.74 | -4.07 | -12.86 | 16 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -10.92 | -27.01 | -33.38 | 42.26 | 4.53 | 38.71 | False |  | distribution_warning | -0.19 | -0.65 | 1 | 1 | -14.18 | -15.13 | -39.82 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | -11.23 | -7.2 | -2.95 | 12.95 | 12.74 | 48.44 | False |  | mild_accumulation | -0.4 | 0.5 | 0 | 2 | -1.14 | -1.9 | -16.24 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | -1.78 | -2.43 | -0.45 | -2.64 | 5.23 | 5.23 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.39 | -0.19 | -3.28 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | -2.55 | 2.81 | 4.34 | -1.64 | 11.67 | 11.67 | False |  | strong_accumulation | 0.08 | 0.04 | 2 | 2 | 1.86 | 1.89 | -3.55 | 19 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.3105385295913 | 31.38789796597349 | -0.71 | 0.0 | 12.54 | 5.42 | 22.81 | 22.81 | False |  | mild_accumulation | 0.16 | 0.35 | 1 | 2 | 0.71 | 2.13 | -6.29 | 16 | selected |
| 2527 | 宏璟 | 建材營造 | neutral | B_可觀察 | 365.123018807587 | 2533.2289075556096 | -2.0 | 14.38 | 19.8 | 35.99 | 27.68 | 51.54 | False |  | strong_accumulation | 0.75 | 0.49 | 2 | 2 | 2.27 | 3.3 | -10.22 | 19 | selected |
| 2537 | 聯上發 | 建材營造 | neutral |  | 57.67979274611399 | 238.4760412839904 | -2.68 | -4.39 | 1.87 | -8.4 | 16.2 | 16.2 | False |  | distribution_warning | -0.41 | -0.2 | 1 | 0 | -2.4 | -0.24 | -12.1 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 79.55310359840207 | 22.58855338149928 | 2.14 | 4.51 | -9.49 | -17.75 | 22.51 | 22.51 | False |  | mild_accumulation | 0.02 | 0.06 | 1 | 1 | 3.18 | 3.41 | -9.89 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | D_降級_TDCC轉弱 | 105.33076260323196 | 54.8064697471788 | -1.9 | -17.4 | -25.0 | -38.57 | 4.45 | 4.45 | False |  | distribution_warning | -0.68 | -0.84 | 0 | 0 | -4.8 | -5.28 | -25.15 | 13 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | -3.88 | 0.45 | 5.19 | 1.36 | 13.66 | 13.66 | False |  | mild_accumulation | 0.46 | 0.41 | 1 | 1 | -0.04 | 0.64 | -5.51 | 21 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | -1.72 | 3.26 | -1.04 | -5.63 | 13.1 | 13.1 | False |  | mild_accumulation | 0.17 | 0.0 | 2 | 1 | 1.91 | 1.79 | -4.04 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 57.91908933878501 | 32.316290442538865 | 6.89 | 6.75 | 10.55 | 17.04 | 19.2 | 26.59 | False |  | distribution_warning | -0.52 | -0.76 | 0 | 0 | 8.74 | 7.73 | -4.77 | 12 | selected |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 329.50067645662165 | 334.2834434453442 | 3.35 | 17.38 | 48.02 | 66.82 | 55.14 | 66.82 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.25 | 0.26 | 2 | 2 | 6.08 | 8.19 | -6.09 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 294.84268843595487 | 170.38806261042123 | 15.99 | 32.77 | 23.81 | 51.46 | 57.58 | 82.99 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.06 | 2 | 1 | 18.09 | 17.54 | -0.95 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | A_優先追蹤 | 328.3542479788894 | 242.62430701861496 | -0.68 | 0.23 | 29.85 | 46.46 | 44.52 | 64.77 | False |  | mild_accumulation | 0.03 | 0.24 | 1 | 1 | -4.4 | -3.37 | -20.48 | 22 | selected |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 66.11083679678092 | 85.45932489486553 | -20.6 | -11.85 | -21.34 | 49.3 | 5.21 | 67.59 | False |  | mild_accumulation | 0.42 | 0.73 | 1 | 2 | -13.05 | -13.31 | -29.57 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | -2.9 | -1.27 | 7.34 | 2.63 | 26.49 | 26.49 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.85 | -0.14 | -7.14 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -12.61 | -6.67 | 10.76 | 71.57 | 18.24 | 75.22 | True | 近120日漲幅>70% | strong_accumulation | 2.1 | 1.88 | 2 | 2 | -10.11 | -9.5 | -20.72 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth |  | 54.44557676970354 | 26.196636563481785 | 0.4 | 2.02 | 43.95 | 63.75 | 48.82 | 77.86 | True | 近60日漲幅>40% | strong_accumulation | 1.39 | 1.85 | 3 | 3 | 1.63 | 1.71 | -8.5 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 188.0864822148371 | 114.02783651203414 | -7.08 | -10.94 | -4.68 | 31.72 | 3.3 | 41.32 | False |  | distribution_warning | -1.26 | -1.2 | 0 | 0 | -6.04 | -8.8 | -33.93 | 16 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 167.50830564784053 | 42.89095493442987 | -9.68 | 4.48 | 2.19 | -3.57 | 15.28 | 20.99 | False |  | distribution_warning | -0.97 | -3.02 | 1 | 0 | -8.44 | -5.28 | -21.08 | 15 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | 0.38 | -5.83 | 8.0 | -2.56 | 14.38 | 22.39 | False |  | distribution_warning | -0.97 | 0.0 | 0 | 0 | -1.8 | -2.06 | -16.72 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -13.93 | -23.84 | 37.11 | 34.62 | 52.75 | 64.25 | True | 距60日低點反彈>50% | mild_accumulation | -0.82 | 0.36 | 1 | 1 | -14.98 | -12.81 | -32.11 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | -7.23 | -13.24 | -18.06 | 96.99 | 3.51 | 107.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -7.55 | -7.96 | -29.68 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 150.02313750823012 | 256.0946243793828 | -15.3 | -19.48 | 16.54 | 37.17 | 25.0 | 55.0 | False |  | distribution_warning | -2.07 | -1.23 | 0 | 0 | -15.4 | -15.92 | -41.73 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | -3.87 | 7.94 | 27.94 | 277.44 | 42.16 | 332.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | -0.28 | 1 | 0 | 6.44 | 5.46 | -14.29 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 170.41456580742187 | 44.354447130404274 | -2.98 | -4.25 | 17.2 | 74.93 | 22.21 | 78.66 | True | 近120日漲幅>70% | mild_accumulation | -0.94 | 0.23 | 0 | 1 | -2.25 | -4.48 | -29.99 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | -12.59 | -12.8 | -8.53 | 39.92 | 4.89 | 105.93 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -14.43 | -12.42 | -33.0 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 53.84760848458394 | 94.00659331121736 | -9.81 | -8.65 | -1.04 | -2.4 | 7.95 | 16.33 | False |  | distribution_warning | -1.56 | -1.54 | 0 | 0 | -8.52 | -7.49 | -29.1 | 11 | selected |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 76.00142700075368 | 64.57714379703859 | -12.45 | -17.3 | 3.91 | -1.24 | 17.73 | 25.66 | False |  | mild_accumulation | -0.04 | 0.14 | 1 | 1 | -11.76 | -11.39 | -29.5 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -4.89 | -6.42 | -4.11 | 20.69 | 6.06 | 23.24 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.25 | -4.39 | -25.05 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -12.7 | -8.22 | 9.39 | 66.12 | 8.5 | 87.85 | True | 距120日低點反彈>80% | distribution_warning | -0.91 | -0.37 | 0 | 1 | -14.55 | -12.38 | -32.44 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | -8.46 | 3.25 | 30.95 | 85.94 | 62.46 | 100.84 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | 0.87 | 1 | 1 | -9.76 | -6.79 | -22.22 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -10.65 | -24.85 | 19.1 | 26.48 | 22.18 | 47.7 | False |  | distribution_warning | -1.65 | -2.07 | 0 | 0 | -13.41 | -12.28 | -36.98 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -11.59 | -20.4 | -21.65 | 12.37 | 9.18 | 10.02 | False |  | distribution_warning | -4.18 | -0.18 | 0 | 0 | -14.39 | -12.94 | -33.84 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 57.64322627738095 | 26.63684630892036 | -7.53 | -16.8 | -43.25 | 25.31 | 9.64 | 33.48 | False |  | mild_accumulation | 0.47 | 0.89 | 1 | 1 | -12.19 | -10.85 | -46.0 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 63.789881691302135 | 33.96537207102099 | -8.74 | -23.16 | -26.8 | 25.0 | 2.9 | 42.57 | False |  | distribution_warning | -0.61 | -2.82 | 0 | 1 | -10.16 | -10.65 | -41.03 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 131.85418997881953 | 55.17736411171146 | 8.64 | 13.81 | 17.73 | 82.16 | 28.49 | 92.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.15 | -0.55 | 1 | 0 | 9.48 | 8.2 | -6.27 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 80.93046018498126 | 44.798488379235415 | -0.33 | 4.91 | 5.16 | 4.55 | 15.3 | 21.71 | False |  | mild_accumulation | 0.72 | 0.49 | 1 | 1 | 2.14 | 1.34 | -13.33 | 20 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -15.09 | 0.25 | 2.27 | 73.82 | 19.47 | 91.04 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.83 | 1.33 | 2 | 2 | -6.76 | -7.75 | -30.41 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -10.0 | -7.53 | -11.91 | -19.16 | 1.5 | 1.5 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -7.98 | -7.32 | -19.4 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -20.95 | -24.86 | -4.2 | 26.28 | 10.94 | 47.97 | False |  | distribution_warning | -1.54 | -3.03 | 1 | 0 | -18.83 | -16.24 | -32.12 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | -5.56 | -6.5 | -6.39 | -7.01 | 7.47 | 7.47 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -2.94 | -4.8 | -27.44 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 80.52350065869514 | 48.63403792846589 | -2.22 | 2.33 | 58.27 | 73.5 | 82.12 | 106.77 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.76 | -7.06 | 0 | 0 | 4.24 | 2.35 | -13.73 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 168.6655162496405 | 156.81600720436765 | -5.92 | -5.65 | -4.02 | 10.23 | 12.08 | 15.17 | False |  | strong_accumulation | 0.74 | 1.51 | 2 | 2 | -4.12 | -3.38 | -15.66 | 21 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | 0.13 | -11.97 | -14.36 | 94.8 | 11.63 | 100.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.74 | 0.0 | 1 | 0 | -3.79 | -4.58 | -30.04 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -27.93 | 0.38 | -31.33 | 32.23 | 7.24 | 76.02 | False |  | mild_accumulation | 6.3 | 6.47 | 1 | 2 | -11.82 | -13.03 | -36.0 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | -2.68 | -4.72 | 3.12 | 19.41 | 25.17 | 39.62 | False |  | mild_accumulation | 0.75 | 0.0 | 2 | 0 | -1.17 | 0.32 | -10.15 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | 5.28 | 0.47 | 1.66 | 8.62 | 12.47 | 14.42 | False |  | distribution_warning | -2.12 | -2.1 | 0 | 0 | 4.23 | 3.18 | -9.31 | 16 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 224.3279602768877 | 118.4530613441191 | 0.21 | -3.33 | 22.07 | 19.18 | 31.1 | 46.11 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 0 | 2.2 | 0.9 | -18.76 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2513.497664900037 | 792.7361428535551 | 4.17 | -15.62 | -4.12 | -5.2 | 6.8 | 6.8 | False |  | distribution_warning | -0.84 | -0.59 | 1 | 1 | -0.97 | -0.75 | -19.55 | 13 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | 0.92 | -1.12 | -11.09 | -19.67 | 7.82 | 7.82 | False |  | mild_accumulation | 0.06 | 0.0 | 1 | 0 | 0.75 | 0.7 | -10.73 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 124.2066375411972 | 34.20005594741868 | -1.12 | -4.8 | 4.06 | -4.22 | 9.22 | 9.22 | False |  | distribution_warning | -0.12 | -0.01 | 1 | 1 | -0.71 | 0.23 | -9.26 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 101.2009801216322 | 127.59657279483612 | -11.31 | -12.56 | 20.92 | 24.68 | 22.66 | 25.83 | False |  | distribution_warning | -1.44 | -1.63 | 0 | 0 | -10.4 | -8.81 | -25.14 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 1.76 | 3.41 | 14.39 | 22.78 | 15.85 | 26.44 | False |  | strong_accumulation | 0.17 | 0.31 | 2 | 2 | 2.27 | 2.72 | -2.75 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 1322.1624507927131 | 667.7676077743706 | -0.43 | -2.44 | 1.43 | -12.21 | 10.71 | 10.71 | False |  | distribution_warning | -0.3 | -0.98 | 0 | 0 | -0.41 | 0.59 | -11.03 | 17 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | -5.44 | -1.64 | 38.03 | 81.48 | 48.69 | 114.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.0 | 0.37 | 1 | 1 | -2.93 | -0.77 | -9.87 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 73.30676173690114 | 58.7802399797441 | -3.21 | -4.73 | 20.77 | 36.52 | 33.28 | 62.86 | False |  | distribution_warning | -5.14 | -3.6 | 0 | 1 | -7.53 | -4.3 | -24.88 | 12 | selected |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | D_降級_TDCC轉弱 | 76.89914529735076 | 37.00041684126828 | 2.93 | -3.44 | 11.51 | 18.57 | 19.07 | 34.45 | False |  | distribution_warning | -1.45 | -1.85 | 0 | 0 | 3.48 | 3.04 | -13.27 | 14 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 4.89 | 5.79 | 36.94 | 45.0 | 36.94 | 53.11 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 9.16 | 6.84 | -29.67 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | -4.26 | -8.33 | 2.48 | 131.31 | 23.75 | 131.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.13 | 0 | 0 | -3.6 | -4.83 | -26.45 |  | fail_already_priced_in |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 56.96595858063789 | 23.32960784964402 | -1.69 | 0.53 | 18.52 | 27.1 | 22.96 | 47.46 | False |  | mild_accumulation | 0.48 | -3.47 | 1 | 0 | -0.18 | -0.38 | -9.69 | 18 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -7.18 | -9.82 | -29.07 | 98.97 | 6.4 | 100.34 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.85 | 0.0 | 2 | 0 | -11.3 | -12.75 | -40.65 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -16.96 | 26.45 | 85.47 | 127.7 | 107.61 | 128.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.38 | 0.26 | 2 | 1 | -2.75 | -1.5 | -23.57 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -21.03 | -26.59 | -34.39 | 101.43 | 5.63 | 107.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.44 | -0.5 | 1 | 1 | -19.77 | -17.19 | -38.73 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | -10.06 | -7.94 | 8.33 | 83.14 | 20.85 | 119.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -2.44 | 0 | 0 | -11.88 | -10.63 | -34.25 |  | fail_low_response_condition |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | 12.5 | 11.94 | -11.24 | -7.41 | 19.05 | 32.35 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 11.94 | 10.01 | -18.92 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | -4.8 | 0.51 | -3.76 | -22.71 | 6.3 | 6.3 | False |  | distribution_warning | -0.34 | -0.87 | 0 | 0 | -3.1 | -2.36 | -13.05 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | -2.71 | -7.72 | 39.29 | 36.41 | 52.12 | 60.49 | True | 距60日低點反彈>50% | mild_accumulation | 0.15 | 1.59 | 1 | 1 | -5.25 | -0.37 | -17.16 |  | fail_low_response_condition |
| 6598 | ABC-KY | 生技醫療業 | defensive_or_traditional |  | 83.5074318744839 | 81.11545407527365 | 2.37 | -3.25 | 7.45 | 0.21 | 10.96 | 10.96 | False |  | mild_accumulation | 0.02 | 0.04 | 1 | 1 | 1.6 | 1.18 | -7.93 |  | fail_low_response_condition |