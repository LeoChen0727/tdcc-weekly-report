# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-16 19:37:46 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1963 |
| standardized_revenue_rows | 1963 |
| price_rows | 630201 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 221 |
| tdcc_mild_accumulation_count | 850 |
| tdcc_distribution_warning_count | 707 |
| revenue_condition_pass | 305 |
| price_metrics_pass | 303 |
| low_response_pass | 90 |
| already_priced_in_excluded | 37 |
| overheat_pass | 53 |
| score_pass | 53 |
| theme_priority_pass | 40 |
| final_rows | 40 |

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
| fail_revenue_condition | 1658 |
| fail_low_response_condition | 213 |
| fail_already_priced_in | 37 |
| fail_defensive_or_traditional_excluded | 11 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | -5.26 | 5.88 | 19.62 | 14.55 | 20.77 | 32.17 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | 1.46 | 0.52 | -13.5 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 101.96587437597796 | 132.1329440999445 | 0.0 | -4.61 | -6.76 | -27.37 | 3.5 | 3.5 | False |  | mild_accumulation | 0.55 | -0.38 | 2 | 0 | -1.15 | -1.23 | -12.66 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 68.32688588007737 | 39.48200784911037 | 0.91 | 0.0 | -3.06 | -5.53 | 3.74 | 3.74 | False |  | mild_accumulation | -0.85 | 0.07 | 0 | 1 | 0.77 | 0.09 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | 1.09 | -0.8 | 1.65 | -7.04 | 9.14 | 9.14 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 1.22 | 0.47 | -8.19 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -4.92 | -15.33 | -14.5 | -20.73 | 0.87 | 0.87 | False |  | mild_accumulation | 1.02 | 0.0 | 2 | 0 | -8.46 | -8.42 | -21.97 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 70.01963312430405 | 44.542976125957246 | -1.84 | -5.92 | -6.07 | -42.47 | 2.98 | 2.98 | False |  | distribution_warning | -0.03 | 0.0 | 1 | 1 | -3.22 | -3.32 | -14.91 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -8.73 | -9.75 | 68.22 | 78.41 | 79.6 | 80.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.62 | 1 | 1 | -13.5 | -6.19 | -35.2 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 162537.27465535526 | 17993.11726781669 | 6.82 | 0.63 | 4.22 | -2.73 | 14.44 | 14.44 | False |  | distribution_warning | -0.04 | -0.1 | 1 | 0 | 4.43 | 4.53 | -3.17 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -2.9 | -18.47 | 2.63 | -16.73 | 9.35 | 13.04 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | -10.03 | -8.06 | -26.18 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | 6.92 | 30.15 | 128.06 | 153.81 | 131.11 | 201.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.1 | -2.21 | 1 | 1 | 12.44 | 14.73 | -2.75 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | -2.36 | -18.13 | -18.82 |  | 4.33 |  | False |  | mild_accumulation | -0.67 | 0.12 | 0 | 1 | -7.34 | -7.23 | -30.19 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 2.52 | 3.29 | 3.44 | -6.75 | 17.12 | 17.12 | False |  | mild_accumulation | 0.11 | 0.24 | 1 | 1 | 5.21 | 4.27 | -2.12 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | 1.56 | 2.76 | 0.19 | 4.2 | 5.89 | 6.33 | False |  | strong_accumulation | 0.95 | 0.58 | 3 | 3 | 1.37 | 1.21 | -1.88 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | -8.26 | 20.15 | 20.15 | 40.61 | 27.78 | 59.41 | False |  | distribution_warning | -0.29 | -0.74 | 0 | 1 | 2.24 | 1.33 | -15.04 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 125.11209715086407 | 47.06150242210431 | -10.46 | -10.05 | 20.96 | 4.7 | 32.03 | 44.26 | False |  | mild_accumulation | 0.43 | -0.92 | 1 | 0 | -13.36 | -8.32 | -29.18 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 106.58847855421364 | 47.886498368081 | 12.37 | 16.16 | 9.18 | 32.52 | 23.4 | 41.87 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | 13.68 | 12.11 | -7.63 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | -2.13 | 13.34 | 118.41 | 131.65 | 127.81 | 192.77 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.29 | 2 | 2 | -6.7 | -0.3 | -19.34 |  | fail_already_priced_in |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 55.42638489110967 | 41.01765691988111 | 1.06 | -14.57 | -8.19 | 69.33 | 7.02 | 73.18 | False |  | distribution_warning | -1.03 | -1.0 | 0 | 0 | -3.31 | -4.45 | -26.31 | 11 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | 2.11 | -9.85 | 9.48 | 3.41 | 10.48 | 29.33 | False |  | distribution_warning | -1.42 | -1.44 | 0 | 0 | -2.28 | -2.22 | -22.77 | 11 | selected |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 67.86685548491262 | 35.613194655616326 | 0.2 | 2.92 | 13.04 | 41.95 | 15.69 | 43.19 | False |  | distribution_warning | -0.11 | -0.13 | 0 | 0 | 1.52 | 2.26 | -2.56 | 17 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | -1.44 | -18.02 | 3.41 | 103.73 | 4.6 | 105.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -2.01 | 1 | 1 | -10.71 | -8.15 | -28.91 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | 2.08 | -12.69 | 95.01 | 61.5 | 93.69 | 105.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.28 | -3.23 | 0 | 0 | -10.33 | -4.1 | -26.34 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -3.93 | -7.94 | 8.41 | 88.62 | 10.21 | 112.84 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.3 | 0.29 | 2 | 2 | -6.08 | -5.2 | -17.88 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 135.4532611228886 | 77.39100370968649 | -2.02 | -6.13 | 5.69 | 33.69 | 10.37 | 37.26 | False |  | strong_accumulation | 0.33 | 0.31 | 2 | 2 | -3.88 | -2.24 | -11.19 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral | D_降級_TDCC轉弱 | 247.66387451562755 | -4.129081203674164 | 4.99 | 7.1 | 9.15 | 0.63 | 18.55 | 18.55 | False |  | distribution_warning | -0.89 | -0.77 | 0 | 1 | 7.64 | 7.22 | -2.92 | 15 | selected |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | -5.9 | 8.81 | 30.27 | 147.42 | 38.27 | 155.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.86 | -2.6 | 0 | 0 | -6.32 | -4.92 | -17.81 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 61.61746792060725 | 36.83107001078034 | -8.31 | -8.86 | 26.2 | 36.87 | 34.44 | 57.46 | False |  | distribution_warning | -0.18 | -0.33 | 1 | 1 | -7.81 | -7.25 | -31.49 | 11 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 4.08 | -9.61 | 22.22 | 40.2 | 23.06 | 45.92 | False |  | distribution_warning | -1.53 | -1.29 | 0 | 0 | -0.24 | -0.38 | -25.83 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | 7.28 | -14.41 | 3.65 | 101.21 | 15.03 | 114.44 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -1.49 | 1 | 0 | -4.93 | -4.61 | -28.8 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 74.79882516895688 | 99.90714739063372 | -5.97 | 6.78 | 14.55 | 27.27 | 23.05 | 38.01 | False |  | mild_accumulation | 2.17 | 2.57 | 1 | 1 | -6.38 | -4.17 | -17.21 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -12.61 | -25.28 | -27.7 | 48.45 | 5.24 | 69.48 | False |  | distribution_warning | -0.59 | -0.4 | 1 | 1 | -15.76 | -14.7 | -36.39 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | 0.6 | -3.16 | 21.22 | 36.71 | 24.58 | 63.2 | False |  | distribution_warning | -0.53 | -1.27 | 1 | 0 | 0.25 | -0.29 | -16.17 | 13 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 102.87247195164616 | 86.48475082849643 | -6.63 | -2.9 | 8.98 | 21.59 | 22.01 | 31.1 | False |  | mild_accumulation | 0.06 | 0.08 | 1 | 1 | -5.48 | -4.86 | -19.63 | 19 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -6.11 | -2.54 | 11.51 | 207.08 | 19.95 | 222.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.11 | 1.44 | 1 | 2 | -7.9 | -5.09 | -20.16 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | -2.93 | 10.42 | 49.72 | 84.35 | 48.67 | 93.08 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.44 | 0.17 | 2 | 1 | 4.92 | 4.24 | -10.62 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 50.90083303173535 | 76.24247572692803 | 4.17 | 0.4 | 26.39 | 13.64 | 32.28 | 52.25 | False |  | mild_accumulation | 0.44 | -0.21 | 1 | 1 | -2.74 | -0.56 | -13.79 | 17 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 62.99850390624209 | 133.4952742541738 | -13.06 | -3.55 | 18.29 | 10.95 | 20.6 | 28.11 | False |  | distribution_warning | -0.63 | -0.39 | 1 | 1 | -9.07 | -8.26 | -26.12 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | 10.86 | 3.29 | 113.11 | 75.6 | 104.66 | 121.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.21 | 0 | 0 | -0.39 | 3.97 | -13.07 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 87.26211992785133 | 46.19747329391832 | 1.15 | 2.66 | 34.35 | 50.0 | 37.33 | 53.92 | False |  | mild_accumulation | 0.56 | -0.01 | 2 | 0 | 0.67 | 2.17 | -8.71 |  | fail_low_response_condition |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | -12.1 | -14.93 | -59.69 | -75.22 | 3.59 | 3.59 | False |  | distribution_warning | -1.13 | -0.04 | 0 | 0 | -9.01 | -12.32 | -66.62 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 375.5658851662359 | 116.51091844759344 | 9.33 | 9.75 | 46.45 | 40.06 | 52.64 | 72.71 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.13 | -0.87 | 1 | 1 | 4.31 | 5.98 | -9.78 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 60.71 | 138.95 | 197.7 | 201.16 | 216.38 | 218.6 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 68.99 | 62.12 | 0.0 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 55.96076128364229 | 23.255026779465105 | 1.53 | -1.19 | 2.47 | 5.06 | 7.1 | 20.29 | False |  | strong_accumulation | 0.42 | 0.47 | 2 | 2 | -1.43 | -1.89 | -26.39 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 220.09287723199685 | 399.98004177172845 | 1.3 | -1.27 | 3.72 | -17.89 | 8.94 | 8.94 | False |  | distribution_warning | -0.15 | -0.44 | 1 | 0 | 0.52 | 0.76 | -4.65 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 381.5468504599107 | 422.1697253819397 | -1.0 | -20.8 | -1.98 | -2.56 | 7.38 | 29.24 | False |  | distribution_warning | -2.89 | -1.7 | 0 | 0 | -8.81 | -8.83 | -35.38 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 59.07699165913917 | 62.47100752006232 | -12.87 | -7.75 | -18.5 | 42.26 | 10.67 | 57.99 | False |  | mild_accumulation | 0.33 | -0.77 | 1 | 0 | -10.61 | -7.79 | -23.45 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 543.886650237175 | 158.17460116324747 | -0.74 | 2.15 | 19.53 | 39.07 | 24.69 | 68.51 | False |  | distribution_warning | -0.61 | -1.14 | 1 | 0 | 3.63 | 1.65 | -13.86 | 18 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | 12.32 | 9.93 | 15.24 | 148.0 | 27.84 | 168.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.84 | 1 | 1 | 3.76 | 4.49 | -10.4 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76248321707817 | 36.92164743994052 | -0.38 | 10.04 | 6.48 | 44.66 | 21.76 | 82.13 | True | 距120日低點反彈>80% | mild_accumulation | 1.78 | 1.08 | 2 | 1 | 2.14 | 2.96 | -6.07 |  | fail_already_priced_in |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -5.78 | -21.82 | -21.82 | 33.43 | 4.53 | 38.71 | False |  | distribution_warning | -0.19 | -0.65 | 1 | 1 | -11.99 | -13.29 | -39.82 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | -6.58 | -4.49 | 2.05 | 10.78 | 13.31 | 49.19 | False |  | mild_accumulation | -0.4 | 0.5 | 0 | 2 | -0.16 | -1.15 | -15.82 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | -1.12 | -2.76 | -0.68 | -3.3 | 4.64 | 4.64 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -0.74 | -0.76 | -3.83 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | 1.53 | 6.4 | 7.87 | 2.61 | 14.59 | 14.59 | False |  | strong_accumulation | 0.08 | 0.04 | 2 | 2 | 3.93 | 3.9 | -1.03 | 19 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.3105385295913 | 31.38789796597349 | 2.72 | 4.06 | 15.81 | 10.63 | 25.96 | 25.96 | False |  | mild_accumulation | 0.16 | 0.35 | 1 | 2 | 2.86 | 3.86 | -3.88 | 16 | selected |
| 2527 | 宏璟 | 建材營造 | neutral |  | 365.123018807587 | 2533.2289075556096 | 19.98 | 24.03 | 46.17 | 60.36 | 51.53 | 79.85 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.75 | 0.49 | 2 | 2 | 19.11 | 19.31 | 0.0 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 57.67979274611399 | 238.4760412839904 | 2.73 | -0.88 | 7.62 | 4.15 | 20.47 | 20.47 | False |  | distribution_warning | -0.41 | -0.2 | 1 | 0 | 1.64 | 2.93 | -8.87 | 11 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 79.55310359840207 | 22.58855338149928 | 5.24 | 5.91 | -4.74 | -13.99 | 24.47 | 24.47 | False |  | mild_accumulation | 0.02 | 0.06 | 1 | 1 | 4.38 | 4.45 | -4.3 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 105.33076260323196 | 54.8064697471788 | 2.71 | -15.43 | -16.93 | -36.8 | 7.29 | 7.29 | False |  | distribution_warning | -0.68 | -0.84 | 0 | 0 | -0.44 | -2.25 | -22.67 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | -1.33 | 0.45 | 6.22 | 2.3 | 13.15 | 13.15 | False |  | mild_accumulation | 0.46 | 0.41 | 1 | 1 | -0.54 | 0.2 | -5.93 | 21 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | -0.7 | 2.52 | 4.01 | -5.0 | 13.1 | 13.1 | False |  | mild_accumulation | 0.17 | 0.0 | 2 | 1 | 1.64 | 1.45 | -4.04 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 57.91908933878501 | 32.316290442538865 | 3.12 | 5.23 | 14.58 | 16.36 | 17.35 | 24.62 | False |  | distribution_warning | -0.52 | -0.76 | 0 | 0 | 6.44 | 4.9 | -6.25 | 12 | selected |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 329.50067645662165 | 334.2834434453442 | 0.84 | 11.92 | 50.94 | 65.45 | 58.21 | 66.97 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.25 | 0.26 | 2 | 2 | 6.83 | 8.53 | -4.24 |  | fail_already_priced_in |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 479.1566577311533 | 58.15505184137289 | 0.98 | 1.31 | 11.51 | -1.9 | 18.77 | 18.77 | False |  | mild_accumulation | 0.05 | -0.03 | 1 | 1 | 2.43 | 3.06 | -0.96 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 294.84268843595487 | 170.38806261042123 | 25.35 | 39.22 | 47.53 | 68.71 | 81.06 | 110.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.06 | 2 | 1 | 31.14 | 28.58 | 0.0 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 328.3542479788894 | 242.62430701861496 | 2.09 | -2.0 | 42.39 | 42.39 | 40.58 | 66.67 | True | 近60日漲幅>40% | mild_accumulation | 0.03 | 0.24 | 1 | 1 | -3.55 | -2.54 | -19.56 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 66.11083679678092 | 85.45932489486553 | -4.3 | -6.12 | -24.45 | 63.6 | 10.42 | 75.89 | False |  | mild_accumulation | 0.42 | 0.73 | 1 | 2 | -8.01 | -7.51 | -26.08 | 16 | selected |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | -2.89 | 1.73 | 9.81 | 3.98 | 27.03 | 27.03 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.49 | 0.18 | -6.75 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -1.35 | -2.27 | 17.15 | 80.72 | 16.4 | 82.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.1 | 1.88 | 2 | 2 | -6.11 | -5.02 | -17.21 |  | fail_already_priced_in |
| 3033 | 威健 | 電子通路業 | mainstream_growth |  | 54.44557676970354 | 26.196636563481785 | 9.27 | 11.07 | 56.65 | 77.41 | 59.41 | 90.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.39 | 1.85 | 3 | 3 | 7.63 | 7.19 | -8.75 |  | fail_low_response_condition |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 188.0864822148371 | 114.02783651203414 | -6.89 | -10.5 | -1.51 | 31.54 | 0.0 | 36.11 | False |  | distribution_warning | -1.26 | -1.2 | 0 | 0 | -8.46 | -10.54 | -36.36 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 167.50830564784053 | 42.89095493442987 | -4.13 | -3.22 | 3.02 | -2.67 | 14.83 | 20.52 | False |  | distribution_warning | -0.97 | -3.02 | 1 | 0 | -8.56 | -5.02 | -21.38 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | -1.45 | -4.91 | 13.87 | 0.18 | 16.31 | 24.45 | False |  | distribution_warning | -0.97 | 0.0 | 0 | 0 | 0.39 | -0.41 | -15.31 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -6.22 | -21.52 | 48.8 | 36.43 | 53.3 | 64.84 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.82 | 0.36 | 1 | 1 | -12.55 | -10.86 | -31.87 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | -2.78 | -12.11 | -16.2 | 97.35 | 4.39 | 106.6 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -5.65 | -6.18 | -29.08 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 150.02313750823012 | 256.0946243793828 | -9.04 | -19.17 | 17.74 | 27.87 | 17.29 | 56.0 | False |  | distribution_warning | -2.07 | -1.23 | 0 | 0 | -13.16 | -13.43 | -41.35 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | 5.06 | 6.37 | 21.23 | 277.38 | 36.38 | 323.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | -0.28 | 1 | 0 | 3.46 | 2.25 | -16.16 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 170.41456580742187 | 44.354447130404274 | 4.9 | -0.99 | 10.09 | 78.57 | 18.81 | 82.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.94 | 0.23 | 0 | 1 | 0.22 | -1.89 | -28.32 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | 7.44 | -9.41 | 8.74 | 64.1 | 15.41 | 128.53 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -3.52 | -1.71 | -25.64 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 53.84760848458394 | 94.00659331121736 | 0.0 | -7.28 | 3.53 | 1.03 | 10.98 | 19.59 | False |  | distribution_warning | -1.56 | -1.54 | 0 | 0 | -5.12 | -4.09 | -27.11 | 12 | selected |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 76.00142700075368 | 64.57714379703859 | -8.4 | -14.59 | 14.29 | -4.0 | 18.23 | 26.18 | False |  | mild_accumulation | -0.04 | 0.14 | 1 | 1 | -9.88 | -9.38 | -29.2 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -1.66 | -1.39 | -5.08 | 1.43 | 5.97 | 15.26 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.67 | -2.64 | -23.98 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -4.89 | -14.94 | 3.72 | 66.73 | 12.96 | 95.56 | True | 距120日低點反彈>80% | distribution_warning | -0.91 | -0.37 | 0 | 1 | -9.67 | -7.38 | -29.66 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | -5.88 | -3.9 | 50.94 | 91.62 | 63.82 | 102.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | 0.87 | 1 | 1 | -8.6 | -5.1 | -21.57 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -7.48 | -27.64 | 16.64 | 27.32 | 18.67 | 46.38 | False |  | distribution_warning | -1.65 | -2.07 | 0 | 0 | -11.05 | -11.34 | -37.54 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -7.52 | -24.14 | -14.82 | 0.21 | 6.12 | 6.59 | False |  | distribution_warning | -4.18 | -0.18 | 0 | 0 | -14.62 | -13.45 | -35.7 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 57.64322627738095 | 26.63684630892036 | 6.09 | -10.3 | -36.78 | 40.87 | 21.25 | 47.61 | False |  | mild_accumulation | 0.47 | 0.89 | 1 | 1 | -1.56 | -0.94 | -38.27 | 16 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.789881691302135 | 33.96537207102099 | 2.89 | -7.78 | -29.04 | 32.99 | 13.33 | 57.03 | False |  | distribution_warning | -0.61 | -2.82 | 0 | 1 | 0.27 | -1.17 | -35.05 | 13 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 131.85418997881953 | 55.17736411171146 | 7.58 | 4.13 | 17.01 | 75.97 | 19.47 | 83.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.15 | -0.55 | 1 | 0 | 3.35 | 2.1 | -10.98 |  | fail_already_priced_in |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 80.93046018498126 | 44.798488379235415 | 1.93 | 6.64 | 9.77 | 7.92 | 15.55 | 21.98 | False |  | mild_accumulation | 0.72 | 0.49 | 1 | 1 | 1.74 | 1.22 | -13.14 | 20 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -4.31 | 2.18 | 17.88 | 67.46 | 24.48 | 99.06 | True | 距120日低點反彈>80% | strong_accumulation | 0.83 | 1.33 | 2 | 2 | -2.74 | -3.11 | -27.49 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -5.74 | -6.71 | -9.36 | -20.53 | 1.88 | 1.88 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -7.02 | -6.06 | -19.1 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -17.82 | -22.07 | -0.11 | 22.16 | 9.84 | 46.52 | False |  | distribution_warning | -1.54 | -3.03 | 1 | 0 | -17.58 | -14.84 | -32.79 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | -1.69 | -1.46 | 3.18 | -3.85 | 10.76 | 10.76 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | 0.35 | -1.55 | -25.21 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 80.52350065869514 | 48.63403792846589 | -0.45 | 11.62 | 67.93 | 81.15 | 82.95 | 107.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.76 | -7.06 | 0 | 0 | 3.48 | 2.18 | -13.33 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 168.6655162496405 | 156.81600720436765 | -5.23 | -5.78 | 3.49 | 12.03 | 9.4 | 12.41 | False |  | strong_accumulation | 0.74 | 1.51 | 2 | 2 | -5.83 | -5.04 | -17.68 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | 6.68 | -9.87 | -11.74 | 93.69 | 8.79 | 91.27 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.74 | 0.0 | 1 | 0 | -5.22 | -6.14 | -31.82 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -20.53 | -0.64 | -28.26 | 19.57 | 4.83 | 72.06 | False |  | mild_accumulation | 6.3 | 6.47 | 1 | 2 | -13.74 | -13.04 | -35.37 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | 0.81 | 2.46 | 10.62 | 17.19 | 29.31 | 44.23 | False |  | mild_accumulation | 0.75 | 0.0 | 2 | 0 | 1.76 | 2.93 | -7.18 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | 4.21 | 2.85 | 9.9 | 10.18 | 13.65 | 15.62 | False |  | distribution_warning | -2.12 | -2.1 | 0 | 0 | 4.98 | 3.29 | -8.36 | 16 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 224.3279602768877 | 118.4530613441191 | 3.79 | -0.53 | 25.3 | 16.23 | 27.53 | 42.14 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 0 | -0.46 | -1.75 | -20.97 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 2513.497664900037 | 792.7361428535551 | 8.44 | -8.92 | -0.14 | 1.76 | 9.81 | 9.81 | False |  | distribution_warning | -0.84 | -0.59 | 1 | 1 | 3.04 | 1.84 | -17.28 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | 1.61 | -0.23 | -7.13 | -17.04 | 8.31 | 8.31 | False |  | mild_accumulation | 0.06 | 0.0 | 1 | 0 | 1.27 | 0.99 | -6.14 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 124.2066375411972 | 34.20005594741868 | 3.16 | -0.73 | 5.28 | 1.11 | 12.38 | 12.38 | False |  | distribution_warning | -0.12 | -0.01 | 1 | 1 | 2.34 | 2.77 | -6.63 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 1.24 | 5.5 | 18.33 | 25.63 | 18.76 | 29.62 | False |  | strong_accumulation | 0.17 | 0.31 | 2 | 2 | 4.3 | 4.47 | -0.31 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 1322.1624507927131 | 667.7676077743706 | 6.19 | 2.35 | 4.8 | -3.71 | 15.52 | 15.52 | False |  | distribution_warning | -0.3 | -0.98 | 0 | 0 | 3.83 | 4.33 | -7.16 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | 8.06 | 9.06 | 52.85 | 97.99 | 62.76 | 134.59 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.0 | 0.37 | 1 | 1 | 5.68 | 7.22 | -2.8 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 73.30676173690114 | 58.7802399797441 | -1.66 | -19.31 | 26.27 | 27.32 | 24.23 | 59.54 | False |  | distribution_warning | -5.14 | -3.6 | 0 | 1 | -7.96 | -5.43 | -26.41 | 11 | selected |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | D_降級_TDCC轉弱 | 76.89914529735076 | 37.00041684126828 | 3.7 | -0.71 | 16.67 | 19.15 | 18.64 | 33.97 | False |  | distribution_warning | -1.45 | -1.85 | 0 | 0 | 3.23 | 2.18 | -13.58 | 14 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 11.09 | 9.89 | 39.24 | 49.85 | 40.0 | 58.7 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 11.88 | 8.6 | -27.1 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | 2.19 | -3.2 | 23.26 | 137.96 | 28.5 | 119.66 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.13 | 0 | 0 | 0.41 | -1.28 | -23.63 |  | fail_already_priced_in |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 56.96595858063789 | 23.32960784964402 | -0.99 | 8.99 | 28.0 | 31.58 | 30.29 | 56.25 | False |  | mild_accumulation | 0.48 | -3.47 | 1 | 0 | 5.13 | 4.74 | -4.31 | 19 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -9.52 | -13.85 | -20.83 | 94.1 | 4.27 | 95.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.85 | 0.0 | 2 | 0 | -11.81 | -12.78 | -41.84 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -17.65 | 27.14 | 103.23 | 114.65 | 117.99 | 129.51 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.38 | 0.26 | 2 | 1 | -0.45 | 2.48 | -19.75 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -12.59 | -32.28 | -33.05 | 90.52 | 1.05 | 97.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.44 | -0.5 | 1 | 1 | -20.58 | -18.45 | -38.99 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | -1.84 | -1.62 | 15.36 | 88.79 | 28.03 | 132.18 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -2.44 | 0 | 0 | -6.63 | -4.77 | -30.34 |  | fail_already_priced_in |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | 18.44 | 13.15 | -7.69 | -4.6 | 20.63 | 34.12 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 12.12 | 9.51 | -12.31 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | -0.49 | -0.49 | 0.5 | -23.24 | 8.04 | 8.04 | False |  | distribution_warning | -0.34 | -0.87 | 0 | 0 | -1.5 | -0.62 | -11.62 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | 0.79 | -8.3 | 47.67 | 32.29 | 53.94 | 62.4 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.15 | 1.59 | 1 | 1 | -3.37 | 0.69 | -16.17 |  | fail_low_response_condition |
| 6589 | 台康生技 | 生技醫療業 | defensive_or_traditional |  | 94.32153392330385 | 50.47184104059554 | -6.38 | 2.78 | 1.43 | -29.71 | 15.19 | 15.19 | False |  | mild_accumulation | 0.08 | 0.49 | 1 | 1 | -3.47 | -2.6 | -13.71 |  | fail_low_response_condition |