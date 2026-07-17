# 營收爆發低反應股 Debug Report

- 產生時間：`2026-07-17 23:34:59 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1963 |
| standardized_revenue_rows | 1963 |
| price_rows | 632166 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 221 |
| tdcc_mild_accumulation_count | 850 |
| tdcc_distribution_warning_count | 707 |
| revenue_condition_pass | 305 |
| price_metrics_pass | 303 |
| low_response_pass | 78 |
| already_priced_in_excluded | 26 |
| overheat_pass | 52 |
| score_pass | 51 |
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
| fail_revenue_condition | 1658 |
| fail_low_response_condition | 225 |
| fail_already_priced_in | 26 |
| fail_defensive_or_traditional_excluded | 7 |
| fail_non_mainstream_score_lt_11 | 3 |
| missing_or_insufficient_price_metrics | 2 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 52.279239592014925 | 47.491044118474434 | -6.33 | 3.64 | 17.46 | 17.83 | 16.72 | 29.37 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | -0.86 | -1.48 | -15.33 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 101.96587437597796 | 132.1329440999445 | -2.9 | -9.46 | -7.8 | -30.45 | 0.5 | 0.5 | False |  | mild_accumulation | 0.55 | -0.38 | 2 | 0 | -3.53 | -3.77 | -15.19 | 18 | selected |
| 1416 | 廣豐 | 其他 | neutral |  | 68.32688588007737 | 39.48200784911037 | 0.45 | -0.45 | -3.06 | -5.53 | 3.74 | 3.74 | False |  | mild_accumulation | -0.85 | 0.07 | 0 | 1 | 0.79 | 0.08 | -6.72 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 6800.0 | -3.4385569334836528 | -4.43 | -0.81 | 0.82 | -7.56 | 8.26 | 8.26 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 0.44 | -0.32 | -8.93 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.91312876558778 | 35.200631755589555 | -9.89 | -19.8 | -18.41 | -24.25 | 0.31 | 0.31 | False |  | mild_accumulation | 1.02 | 0.0 | 2 | 0 | -12.79 | -12.69 | -26.46 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 70.01963312430405 | 44.542976125957246 | -3.5 | -7.95 | -7.66 | -44.33 | 1.4 | 1.4 | False |  | distribution_warning | -0.03 | 0.0 | 1 | 1 | -4.31 | -4.42 | -16.21 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 73.41431351726915 | 58.39990415923418 | -11.3 | -20.52 | 58.22 | 66.85 | 69.62 | 70.38 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.83 | -0.62 | 1 | 1 | -17.43 | -10.55 | -38.8 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 162537.27465535526 | 17993.11726781669 | 6.98 | -0.62 | 8.78 | -3.74 | 14.8 | 14.8 | False |  | distribution_warning | -0.04 | -0.1 | 1 | 0 | 4.79 | 4.43 | -2.87 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 57.857221996528416 | 139.16826059543175 | -4.55 | -18.37 | 3.59 | -17.5 | 7.94 | 11.59 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | -10.29 | -8.54 | -27.13 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 220.5230581202144 | 98.94781003339511 | -4.36 | 19.18 | 99.24 | 138.37 | 103.09 | 174.43 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.1 | -2.21 | 1 | 1 | 1.67 | 4.19 | -11.35 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 101.11290567980993 | 63.32375134083277 | -5.1 | -20.51 | -20.29 |  | 1.09 |  | False |  | mild_accumulation | -0.67 | 0.12 | 0 | 1 | -9.5 | -9.65 | -32.61 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 328.25458390774605 | 188.7483496965832 | 0.0 | 2.1 | 2.87 | -8.11 | 15.25 | 15.25 | False |  | mild_accumulation | 0.11 | 0.24 | 1 | 1 | 3.42 | 2.39 | -3.68 | 24 | selected |
| 2107 | 厚生 | 橡膠工業 | cyclical_turnaround |  | 107.32742504320058 | 7.380722054614817 | 0.39 | 1.98 | -0.96 | 3.21 | 4.47 | 4.9 | False |  | strong_accumulation | 0.95 | 0.58 | 3 | 3 | -0.09 | -0.14 | -3.2 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 75.65338225299264 | 24.16277764224123 | -8.52 | 20.15 | 19.7 | 45.7 | 27.78 | 59.41 | False |  | distribution_warning | -0.29 | -0.74 | 0 | 1 | 1.37 | 1.22 | -15.04 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 125.11209715086407 | 47.06150242210431 | -14.9 | -20.63 | 15.48 | -2.01 | 23.9 | 35.37 | False |  | mild_accumulation | 0.43 | -0.92 | 1 | 0 | -17.83 | -12.96 | -33.55 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 106.58847855421364 | 47.886498368081 | 5.93 | 11.01 | 6.66 | 25.25 | 17.92 | 35.57 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | 8.06 | 6.51 | -11.72 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 142.3336189198364 | 79.62108324410907 | -10.69 | 5.07 | 102.2 | 108.77 | 104.78 | 173.62 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.03 | 1.29 | 2 | 2 | -12.98 | -6.29 | -24.62 |  | fail_already_priced_in |
| 2308 | 台達電 | 電子零組件業 | mainstream_growth |  | 55.42638489110967 | 41.01765691988111 | -7.45 | -19.26 | -13.86 | 55.36 | 0.29 | 58.18 | False |  | distribution_warning | -1.03 | -1.0 | 0 | 0 | -10.75 | -11.79 | -32.69 |  | fail_low_response_condition |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 52.11164672139997 | 34.98569899471218 | -1.47 | -13.97 | 2.63 | 1.96 | 6.61 | 24.8 | False |  | distribution_warning | -1.42 | -1.44 | 0 | 0 | -4.97 | -5.2 | -25.48 | 11 | selected |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 67.86685548491262 | 35.613194655616326 | -5.18 | -3.98 | 1.1 | 30.11 | 7.26 | 31.61 | False |  | distribution_warning | -0.11 | -0.13 | 0 | 0 | -5.69 | -4.78 | -9.66 | 16 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 216.09461825396 | 128.75502117306723 | -12.89 | -22.6 | -13.79 | 69.61 | 0.81 | 88.25 | True | 距120日低點反彈>80% | distribution_warning | -1.78 | -2.01 | 1 | 1 | -17.25 | -14.76 | -34.9 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 189.876760712048 | 139.19764936720955 | -12.18 | -22.11 | 65.07 | 33.05 | 74.55 | 84.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.28 | -3.23 | 0 | 0 | -18.26 | -12.59 | -33.62 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 61.16410559844036 | 60.28045047959245 | -15.38 | -16.23 | -3.91 | 79.4 | 0.0 | 91.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.3 | 0.29 | 2 | 2 | -14.69 | -13.55 | -26.02 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 135.4532611228886 | 77.39100370968649 | -3.62 | -7.68 | 6.49 | 31.03 | 7.3 | 34.12 | False |  | strong_accumulation | 0.33 | 0.31 | 2 | 2 | -5.71 | -4.12 | -13.22 | 24 | selected |
| 2348 | 海悅 | 其他 | neutral | D_降級_TDCC轉弱 | 247.66387451562755 | -4.129081203674164 | 2.77 | 0.52 | 8.18 | -0.89 | 15.73 | 15.73 | False |  | distribution_warning | -0.89 | -0.77 | 0 | 1 | 5.05 | 4.27 | -5.22 | 15 | selected |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 51.71958184529576 | 24.21365182181492 | -13.75 | -4.17 | 18.15 | 120.31 | 19.38 | 130.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.86 | -2.6 | 0 | 0 | -15.46 | -13.32 | -25.97 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth |  | 61.61746792060725 | 36.83107001078034 | -16.19 | -13.33 | 25.27 | 31.02 | 29.57 | 51.75 | False |  | distribution_warning | -0.18 | -0.33 | 1 | 1 | -10.54 | -9.82 | -33.97 |  | fail_low_response_condition |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 55.63429893699061 | 38.84510089773063 | 2.34 | -12.83 | 19.05 | 37.25 | 20.48 | 42.86 | False |  | distribution_warning | -1.53 | -1.29 | 0 | 0 | -1.63 | -2.27 | -27.39 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 73.02446781174181 | 90.60268702714608 | 1.65 | -17.04 | -3.9 | 94.74 | 6.94 | 99.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -1.49 | 1 | 0 | -10.81 | -10.47 | -33.81 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 74.79882516895688 | 99.90714739063372 | -13.57 | -3.9 | 6.98 | 9.04 | 10.74 | 24.21 | False |  | mild_accumulation | 2.17 | 2.57 | 1 | 1 | -15.6 | -12.76 | -25.49 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 78.22292794927401 | 68.740667371717 | -13.77 | -32.34 | -34.72 | 48.56 | 0.0 | 56.32 | False |  | distribution_warning | -0.59 | -0.4 | 1 | 1 | -20.83 | -19.9 | -41.33 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 68.55140790315762 | 48.36152042575696 | -3.42 | -6.47 | 14.04 | 35.42 | 20.15 | 57.38 | False |  | distribution_warning | -0.53 | -1.27 | 1 | 0 | -2.99 | -3.53 | -19.15 | 12 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth |  | 102.87247195164616 | 86.48475082849643 | -12.85 | -12.97 | 0.0 | 15.43 | 12.82 | 21.23 | False |  | mild_accumulation | 0.06 | 0.08 | 1 | 1 | -12.03 | -11.14 | -25.68 |  | fail_low_response_condition |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 120.69324458952984 | 81.82058149540548 | -15.11 | -13.56 | -4.97 | 184.49 | 8.05 | 188.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.11 | 1.44 | 1 | 2 | -16.49 | -13.46 | -28.08 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.39187977693179 | 32.183756736357665 | -5.0 | 5.02 | 41.32 | 78.75 | 43.5 | 86.89 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.44 | 0.17 | 2 | 1 | 1.31 | 0.82 | -13.49 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 50.90083303173535 | 76.24247572692803 | -4.53 | -9.38 | 19.71 | 5.94 | 22.75 | 41.29 | False |  | mild_accumulation | 0.44 | -0.21 | 1 | 1 | -9.32 | -7.12 | -20.0 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 62.99850390624209 | 133.4952742541738 | -20.13 | -15.06 | 3.89 | -0.16 | 5.67 | 16.04 | False |  | distribution_warning | -0.63 | -0.39 | 1 | 1 | -17.04 | -15.72 | -33.08 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 621.3354284927444 | 643.1170392921229 | -9.18 | -9.5 | 74.61 | 43.82 | 84.38 | 99.24 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.21 | 0 | 0 | -9.84 | -5.83 | -21.68 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 87.26211992785133 | 46.19747329391832 | -2.6 | -1.15 | 32.3 | 46.34 | 33.33 | 49.44 | False |  | mild_accumulation | 0.56 | -0.01 | 2 | 0 | -2.21 | -0.74 | -11.37 |  | fail_low_response_condition |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 94.99032752985124 | -13.789322594792871 | -12.08 | -16.62 | -59.54 | -75.16 | 0.0 | 0.0 | False |  | distribution_warning | -1.13 | -0.04 | 0 | 0 | -11.69 | -14.53 | -67.88 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 375.5658851662359 | 116.51091844759344 | 3.0 | 0.0 | 39.83 | 24.43 | 42.0 | 64.34 | False |  | distribution_warning | -0.13 | -0.87 | 1 | 1 | -0.75 | 0.77 | -14.15 | 18 | selected |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 117.37116386797916 | 18.628753653999468 | 31.72 | 124.11 | 169.97 | 171.31 | 185.02 | 187.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.18 | 0 | 0 | 46.08 | 40.65 | -9.91 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 55.96076128364229 | 23.255026779465105 | -6.61 | -8.26 | -8.53 | -3.72 | 0.32 | 12.68 | False |  | strong_accumulation | 0.42 | 0.47 | 2 | 2 | -7.27 | -7.47 | -31.04 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 220.09287723199685 | 399.98004177172845 | -0.52 | -4.01 | 4.64 | -16.74 | 5.8 | 6.98 | False |  | distribution_warning | -0.15 | -0.44 | 1 | 0 | -1.08 | -0.96 | -6.36 | 15 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 381.5468504599107 | 422.1697253819397 | -9.27 | -26.05 | -12.21 | -10.33 | 0.0 | 20.1 | False |  | distribution_warning | -2.89 | -1.7 | 0 | 0 | -13.97 | -14.18 | -39.95 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 59.07699165913917 | 62.47100752006232 | -7.73 | -10.85 | -15.26 | 36.13 | 8.95 | 55.53 | False |  | mild_accumulation | 0.33 | -0.77 | 1 | 0 | -11.52 | -8.52 | -24.64 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 543.886650237175 | 158.17460116324747 | -14.64 | -6.6 | 11.05 | 30.82 | 12.52 | 59.33 | False |  | distribution_warning | -0.61 | -1.14 | 1 | 0 | -1.67 | -3.57 | -18.55 | 17 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 94.07732107248208 | 78.92076095195968 | 0.36 | -4.62 | 12.61 | 127.76 | 9.84 | 142.08 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.84 | 1 | 1 | -6.41 | -5.49 | -19.36 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.76248321707817 | 36.92164743994052 | -8.14 | -3.27 | -1.66 | 24.08 | 9.72 | 64.13 | False |  | mild_accumulation | 1.78 | 1.08 | 2 | 1 | -7.82 | -6.65 | -15.36 | 15 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 80.9284462655301 | 82.0194649920665 | -13.03 | -31.11 | -30.23 | 16.2 | 0.46 | 27.27 | False |  | distribution_warning | -0.19 | -0.65 | 1 | 1 | -17.74 | -19.06 | -44.78 |  | fail_low_response_condition |
| 2497 | 怡利電 | 汽車工業 | neutral |  | 52.51953851879419 | 21.202127284894164 | -8.22 | -9.12 | -3.63 | 4.3 | 6.08 | 39.67 | False |  | mild_accumulation | -0.4 | 0.5 | 0 | 2 | -6.08 | -6.87 | -21.19 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 126.52159812203672 | 51.06891870158917 | -1.57 | -2.99 | 0.46 | -3.31 | 4.16 | 4.16 | False |  | mild_accumulation | 0.26 | -0.15 | 2 | 0 | -1.04 | -1.11 | -4.26 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 76.55528600440893 | 21.9113159587622 | 0.47 | 4.15 | 7.43 | 0.95 | 13.13 | 13.13 | False |  | strong_accumulation | 0.08 | 0.04 | 2 | 2 | 2.4 | 2.35 | -2.29 | 19 | selected |
| 2520 | 冠德 | 建材營造 | neutral | B_可觀察 | 52.3105385295913 | 31.38789796597349 | 1.71 | -1.24 | 18.8 | 9.17 | 25.26 | 25.26 | False |  | mild_accumulation | 0.16 | 0.35 | 1 | 2 | 2.35 | 3.0 | -4.42 | 16 | selected |
| 2527 | 宏璟 | 建材營造 | neutral |  | 365.123018807587 | 2533.2289075556096 | 12.91 | 23.65 | 37.63 | 59.01 | 47.09 | 74.59 | False |  | strong_accumulation | 0.75 | 0.49 | 2 | 2 | 14.36 | 14.31 | -3.7 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral | B_可觀察 | 79.55310359840207 | 22.58855338149928 | 3.82 | 3.55 | -0.61 | -15.26 | 23.26 | 23.26 | False |  | mild_accumulation | 0.02 | 0.06 | 1 | 1 | 3.19 | 3.14 | -1.92 | 16 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | D_降級_TDCC轉弱 | 105.33076260323196 | 54.8064697471788 | -1.42 | -17.65 | -17.48 | -39.57 | 3.24 | 3.24 | False |  | distribution_warning | -0.68 | -0.84 | 0 | 0 | -3.21 | -5.47 | -25.58 | 11 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 141.98893188532435 | 43.60561665546948 | -10.04 | -8.04 | -0.96 | -6.36 | 4.99 | 4.99 | False |  | mild_accumulation | 0.46 | 0.41 | 1 | 1 | -7.33 | -6.48 | -12.71 | 18 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 56.41813290679075 | 83.99651912270093 | -4.11 | -0.36 | 4.48 | -7.59 | 11.11 | 11.11 | False |  | mild_accumulation | 0.17 | 0.0 | 2 | 1 | -0.12 | -0.31 | -5.72 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 57.91908933878501 | 32.316290442538865 | -4.34 | 2.58 | 10.28 | 11.83 | 12.78 | 19.94 | False |  | distribution_warning | -0.52 | -0.76 | 0 | 0 | 2.31 | 0.88 | -9.77 | 14 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 199.0184261973224 | 334.18209408719963 | -12.4 | -14.44 | 23.67 | 55.73 | 26.69 | 61.13 | False |  | distribution_warning | -0.33 | -0.34 | 1 | 1 | -11.2 | -9.78 | -26.17 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional | D_降級_TDCC轉弱 | 72.83314528275568 | 142.24828219717486 | -4.83 | -2.55 | 27.95 | 53.3 | 27.95 | 58.54 | False |  | distribution_warning | -0.17 | -0.21 | 0 | 0 | -3.44 | -1.87 | -10.1 | 7 | fail_score_lt_8 |
| 2887 | 台新新光金 | 金融保險業 | defensive_or_traditional |  | 329.50067645662165 | 334.2834434453442 | -3.53 | 9.05 | 49.37 | 55.58 | 55.58 | 61.22 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.25 | 0.26 | 2 | 2 | 4.6 | 6.14 | -5.83 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 294.84268843595487 | 170.38806261042123 | 31.86 | 40.39 | 49.17 | 75.92 | 80.81 | 109.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.06 | 2 | 1 | 28.53 | 25.43 | -1.78 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 328.3542479788894 | 242.62430701861496 | -16.46 | -12.0 | 17.86 | 24.92 | 19.28 | 50.0 | False |  | mild_accumulation | 0.03 | 0.24 | 1 | 1 | -12.68 | -11.38 | -27.61 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 66.11083679678092 | 85.45932489486553 | -6.38 | -6.98 | -22.4 | 71.88 | 9.18 | 73.91 | True | 近120日漲幅>70% | mild_accumulation | 0.42 | 0.73 | 1 | 2 | -8.73 | -7.9 | -26.42 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 84.09046597777345 | -41.885171958756736 | -3.32 | 0.87 | 8.88 | -1.27 | 25.95 | 25.95 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.37 | -0.62 | -7.54 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 65.62443152383592 | 93.17531759444776 | -9.57 | -8.48 | -0.87 | 62.29 | 2.56 | 69.36 | False |  | strong_accumulation | 2.1 | 1.88 | 2 | 2 | -12.3 | -10.78 | -22.99 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | B_可觀察 | 54.44557676970354 | 26.196636563481785 | -1.61 | -0.2 | 36.89 | 58.7 | 37.46 | 71.53 | False |  | strong_accumulation | 1.39 | 1.85 | 3 | 3 | -3.08 | -3.21 | -17.85 | 15 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 188.0864822148371 | 114.02783651203414 | -10.87 | -15.85 | -6.22 | 26.94 | 0.8 | 30.9 | False |  | distribution_warning | -1.26 | -1.2 | 0 | 0 | -11.23 | -12.95 | -38.8 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 167.50830564784053 | 42.89095493442987 | -12.1 | -19.83 | -0.64 | -13.57 | 4.49 | 9.67 | False |  | distribution_warning | -0.97 | -3.02 | 1 | 0 | -15.93 | -12.58 | -28.46 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 53.6303119191817 | 20.313044004783457 | -5.76 | -8.07 | 10.78 | -2.96 | 11.73 | 20.32 | False |  | distribution_warning | -0.97 | 0.0 | 0 | 0 | -2.53 | -3.42 | -18.13 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 60.10438064297345 | 31.06060814146213 | -15.5 | -30.17 | 29.83 | 18.32 | 33.07 | 49.78 | False |  | mild_accumulation | -0.82 | 0.36 | 1 | 1 | -19.16 | -17.7 | -38.1 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 175.55224852346186 | 576.0554681118128 | -12.46 | -18.14 | -28.94 | 85.31 | 0.91 | 92.71 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -11.12 | -11.57 | -33.85 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 150.02313750823012 | 256.0946243793828 | -15.99 | -24.94 | 4.33 | 7.84 | 6.64 | 44.5 | False |  | distribution_warning | -2.07 | -1.23 | 0 | 0 | -18.48 | -18.47 | -45.68 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 139.6643774590947 | 127.28400124297455 | -1.16 | -5.08 | 13.48 | 248.18 | 22.76 | 281.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | -0.28 | 1 | 0 | -6.64 | -7.35 | -24.53 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth | A_優先追蹤 | 170.41456580742187 | 44.354447130404274 | -4.93 | -7.3 | 5.08 | 65.38 | 10.69 | 70.43 | False |  | mild_accumulation | -0.94 | 0.23 | 0 | 1 | -6.29 | -7.94 | -33.21 | 20 | selected |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 99.08963077859762 | 57.87534694883431 | 5.55 | -7.36 | 7.92 | 65.59 | 16.69 | 131.07 | True | 距120日低點反彈>80% | distribution_warning | -0.04 | -1.57 | 0 | 0 | -2.07 | -0.57 | -24.82 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 53.84760848458394 | 94.00659331121736 | -3.81 | -14.46 | -2.46 | 0.36 | 5.3 | 13.47 | False |  | distribution_warning | -1.56 | -1.54 | 0 | 0 | -9.28 | -8.32 | -30.85 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 76.00142700075368 | 64.57714379703859 | -14.51 | -23.51 | 4.31 | -8.4 | 6.34 | 14.62 | False |  | mild_accumulation | -0.04 | 0.14 | 1 | 1 | -17.09 | -16.45 | -35.69 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 97.58195188832109 | 181.8689925928791 | -6.08 | -7.61 | -17.27 | -11.69 | 1.8 | 10.39 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -6.43 | -6.22 | -27.19 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 103.71897307865596 | 93.05257734463794 | -11.64 | -24.43 | -3.03 | 42.3 | 1.46 | 79.21 | False |  | distribution_warning | -0.91 | -0.37 | 0 | 1 | -16.11 | -14.04 | -35.55 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 88.17862702906383 | 9.911626096750895 | -13.94 | -15.95 | 43.28 | 76.33 | 44.72 | 82.28 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | 0.87 | 1 | 1 | -17.09 | -13.54 | -29.41 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 57.39755714580272 | 84.92502961789467 | -15.41 | -31.43 | 9.8 | 21.21 | 10.24 | 38.16 | False |  | distribution_warning | -1.65 | -2.07 | 0 | 0 | -14.4 | -15.17 | -41.05 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 160.85153540914453 | 408.6299445898107 | -12.25 | -31.82 | -21.29 | -13.9 | 1.89 | 1.89 | False |  | distribution_warning | -4.18 | -0.18 | 0 | 0 | -17.82 | -17.0 | -39.27 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 57.64322627738095 | 26.63684630892036 | 0.16 | -19.55 | -35.28 | 32.1 | 14.64 | 39.57 | False |  | mild_accumulation | 0.47 | 0.89 | 1 | 1 | -5.86 | -5.84 | -41.05 | 16 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 63.789881691302135 | 33.96537207102099 | -5.36 | -15.55 | -36.17 | 26.07 | 2.32 | 41.77 | False |  | distribution_warning | -0.61 | -2.82 | 0 | 1 | -8.71 | -9.97 | -41.36 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 131.85418997881953 | 55.17736411171146 | 2.82 | 2.34 | 14.66 | 70.83 | 15.26 | 76.61 | True | 近120日漲幅>70% | distribution_warning | -0.15 | -0.55 | 1 | 0 | -0.41 | -1.37 | -14.12 |  | fail_already_priced_in |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 80.93046018498126 | 44.798488379235415 | -0.45 | 2.32 | 8.61 | 4.62 | 13.5 | 19.81 | False |  | mild_accumulation | 0.72 | 0.49 | 1 | 1 | -0.19 | -0.53 | -14.69 | 19 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 62.558818527127386 | 47.779761403199295 | -11.01 | -3.48 | 7.18 | 55.82 | 8.99 | 83.02 | True | 距120日低點反彈>80% | strong_accumulation | 0.83 | 1.33 | 2 | 2 | -10.43 | -10.1 | -33.33 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 300.738900962434 | 178.0335630702673 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 79.3119034787295 | 20.73895703213184 | -10.26 | -11.64 | -12.39 | -24.23 | 0.58 | 0.58 | False |  | distribution_warning | -0.18 | -2.51 | 0 | 0 | -10.97 | -9.78 | -22.99 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 113.78698185062235 | 120.05822763884169 | -15.05 | -31.63 | -0.24 | 11.98 | 1.94 | 36.3 | False |  | distribution_warning | -1.54 | -3.03 | 1 | 0 | -21.94 | -19.38 | -37.47 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 53.33200678435051 | 25.095796515703565 | -4.74 | -7.21 | -1.32 | -8.34 | 4.3 | 4.3 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -5.15 | -6.72 | -29.57 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 80.52350065869514 | 48.63403792846589 | -5.56 | 3.34 | 63.46 | 66.12 | 68.32 | 91.73 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -6.76 | -7.06 | 0 | 0 | -4.62 | -5.24 | -20.0 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 168.6655162496405 | 156.81600720436765 | -11.59 | -12.36 | -3.48 | 2.01 | 2.35 | 4.45 | False |  | strong_accumulation | 0.74 | 1.51 | 2 | 2 | -11.35 | -10.32 | -22.98 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.69247448786183 | 40.94635505649941 | -12.53 | -20.21 | -19.84 | 62.59 | 0.0 | 68.54 | False |  | mild_accumulation | 0.74 | 0.0 | 1 | 0 | -13.67 | -14.34 | -38.58 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 73.41090827325492 | 63.18019609357152 | -23.31 | -12.66 | -30.64 | 11.39 | 0.0 | 54.9 | False |  | mild_accumulation | 6.3 | 6.47 | 1 | 2 | -21.9 | -20.27 | -41.82 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 71.58654077170728 | 28.97151163964546 | -2.89 | -3.4 | 9.5 | 17.14 | 27.24 | 41.92 | False |  | mild_accumulation | 0.75 | 0.0 | 2 | 0 | 0.31 | 1.17 | -8.66 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 70.82679590683092 | 58.0873125778475 | -1.54 | -2.34 | 7.62 | 3.35 | 9.32 | 11.21 | False |  | distribution_warning | -2.12 | -2.1 | 0 | 0 | 1.1 | -0.59 | -11.85 | 15 | selected |
| 5484 | 慧友 | 光電業 | mainstream_growth |  | 224.3279602768877 | 118.4530613441191 | -13.79 | -10.34 | 15.33 | 4.81 | 16.28 | 29.77 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 0 | -8.64 | -9.52 | -27.84 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | D_降級_TDCC轉弱 | 2513.497664900037 | 792.7361428535551 | 5.26 | -9.2 | -1.45 | -0.29 | 7.75 | 7.75 | False |  | distribution_warning | -0.84 | -0.59 | 1 | 1 | 1.63 | -0.06 | -18.83 | 15 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 4115.01490559788 | 1416.5514844835934 | -0.23 | -3.11 | -5.83 | -17.89 | 6.6 | 6.6 | False |  | mild_accumulation | 0.06 | 0.0 | 1 | 0 | -0.17 | -0.56 | -7.63 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 124.2066375411972 | 34.20005594741868 | 2.53 | -4.69 | 4.5 | 0.5 | 11.69 | 11.69 | False |  | distribution_warning | -0.12 | -0.01 | 1 | 1 | 1.97 | 1.96 | -7.2 | 16 | selected |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 101.2009801216322 | 127.59657279483612 | -9.34 | -16.35 | 18.07 | 15.99 | 18.07 | 21.77 | False |  | distribution_warning | -1.44 | -1.63 | 0 | 0 | -11.28 | -9.86 | -27.55 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 124.14887355302106 | -29.03029678678487 | 0.0 | 3.53 | 16.22 | 24.28 | 16.43 | 28.23 | False |  | strong_accumulation | 0.17 | 0.31 | 2 | 2 | 3.0 | 3.06 | -1.38 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 1322.1624507927131 | 667.7676077743706 | 4.86 | -1.55 | 6.62 | -7.59 | 14.32 | 14.32 | False |  | distribution_warning | -0.3 | -0.98 | 0 | 0 | 2.83 | 2.97 | -8.12 | 18 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 120.99485624843622 | 39.47871328861635 | -1.28 | 0.18 | 42.44 | 85.3 | 46.09 | 115.51 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.0 | 0.37 | 1 | 1 | -2.93 | -1.38 | -10.71 |  | fail_already_priced_in |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 73.30676173690114 | 58.7802399797441 | -14.23 | -27.59 | 5.16 | 14.93 | 11.95 | 43.78 | False |  | distribution_warning | -5.14 | -3.6 | 0 | 1 | -15.73 | -13.71 | -33.68 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | D_降級_TDCC轉弱 | 76.89914529735076 | 37.00041684126828 | -4.53 | -2.84 | 15.13 | 16.1 | 14.64 | 31.1 | False |  | distribution_warning | -1.45 | -1.85 | 0 | 0 | 1.16 | -0.01 | -15.43 | 14 | selected |
| 6225 | 天瀚 | 光電業 | mainstream_growth |  | 846.5463596764157 | 32.0746334962239 | 11.59 | 9.47 | 42.08 | 46.07 | 41.69 | 61.49 | True | 近60日漲幅>40% | neutral | 0.0 | 0.0 | 0 | 0 | 13.29 | 9.56 | -25.82 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 84.36983842052487 | 22.802551262295434 | -9.98 | -13.31 | 10.87 | 97.89 | 12.47 | 89.11 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.2 | -1.13 | 0 | 0 | -7.73 | -9.17 | -30.31 |  | fail_already_priced_in |
| 6414 | 樺漢 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 56.96595858063789 | 23.32960784964402 | 0.25 | 6.61 | 26.81 | 34.58 | 27.21 | 54.3 | False |  | mild_accumulation | 0.48 | -3.47 | 1 | 0 | 3.48 | 3.14 | -5.5 | 17 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 103.0427419123346 | 70.16045645961799 | -16.27 | -19.49 | -23.41 | 74.25 | 1.62 | 77.2 | True | 近120日漲幅>70% | mild_accumulation | 3.85 | 0.0 | 2 | 0 | -18.23 | -18.57 | -46.6 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 94.88062647812396 | 74.5949825992632 | -7.0 | 18.32 | 97.19 | 107.11 | 97.85 | 117.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.38 | 0.26 | 2 | 1 | -6.27 | -2.58 | -23.89 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 287.8983328197554 | 70.27062547976278 | -22.02 | -35.93 | -36.8 | 75.0 | 0.41 | 76.53 | True | 近120日漲幅>70% | distribution_warning | -0.44 | -0.5 | 1 | 1 | -27.14 | -25.02 | -45.15 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 59.47776921504176 | 94.67605835240276 | -11.17 | -12.22 | 8.76 | 59.03 | 5.68 | 109.2 | True | 距120日低點反彈>80% | distribution_warning | -1.49 | -2.44 | 0 | 0 | -15.38 | -13.17 | -37.24 |  | fail_low_response_condition |
| 6533 | 晶心科 | 半導體業 | mainstream_growth |  | 247.04308093994777 | 62.06907821274695 | 9.66 | 4.22 | -12.32 | -16.17 | 11.11 | 23.53 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 3.05 | 0.79 | -19.23 |  | fail_low_response_condition |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 267.3506268589285 | 265.39754450202213 | -5.88 | -5.07 | -4.24 | -26.15 | 2.95 | 2.95 | False |  | distribution_warning | -0.34 | -0.87 | 0 | 0 | -5.91 | -4.89 | -15.79 |  | fail_low_response_condition |
| 6585 | 鼎基 | 其他 | neutral |  | 91.43760971759134 | 13.805961179598444 | -0.8 | -9.52 | 48.8 | 31.38 | 48.8 | 57.93 | True | 近60日漲幅>40% | mild_accumulation | 0.15 | 1.59 | 1 | 1 | -5.56 | -1.92 | -18.48 |  | fail_low_response_condition |