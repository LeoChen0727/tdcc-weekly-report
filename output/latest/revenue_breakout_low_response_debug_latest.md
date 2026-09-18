# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-18 19:37:12 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 723643 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 367 |
| tdcc_mild_accumulation_count | 755 |
| tdcc_distribution_warning_count | 643 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 119 |
| already_priced_in_excluded | 43 |
| overheat_pass | 76 |
| score_pass | 76 |
| theme_priority_pass | 61 |
| final_rows | 61 |

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
| fail_revenue_condition | 1611 |
| fail_low_response_condition | 241 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 13 |
| fail_non_mainstream_score_lt_11 | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | 2.44 | 22.5 | 3.89 | 11.36 | 36.11 | 47.29 | False |  | strong_accumulation | 1.06 | 1.17 | 2 | 3 | 2.71 | 4.4 | -10.91 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 93.04522686147229 | 122.05590293593936 | 0.47 | -4.02 | 4.37 | -10.79 | 14.48 | 14.48 | False |  | distribution_warning | -0.91 | -0.42 | 0 | 2 | -1.65 | 0.07 | -14.0 | 11 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | -0.38 | 0.78 | -3.17 | -21.92 | 4.21 | 4.21 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | -0.09 | 0.26 | -16.26 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 2.72 | -0.97 | -9.73 | 22.01 | 7.48 | 22.6 | False |  | distribution_warning | -0.3 | 0.0 | 1 | 0 | -0.07 | -0.01 | -14.29 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 0.86 | -0.56 | -1.12 | -5.61 | 2.32 | 4.13 | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | -0.23 | -0.42 | -12.41 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | 0.28 | 2.01 | -8.03 | -10.47 | 4.11 | 4.11 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 1 | 0.41 | 0.25 | -9.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 4.92 | -0.22 | -6.28 | -20.0 | 9.54 | 17.28 | False |  | mild_accumulation | -0.26 | 0.13 | 2 | 3 | 1.38 | 1.79 | -8.38 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 0.82 | 0.0 | -16.61 | -0.81 | 4.68 | 4.68 | False |  | strong_accumulation | 0.08 | 0.16 | 2 | 2 | -0.16 | -0.13 | -20.65 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | -2.09 | 0.72 | -3.1 | -1.75 | 6.44 | 16.12 | False |  | distribution_warning | -0.34 | -0.36 | 1 | 1 | 0.34 | 0.33 | -9.06 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 8.29 | 17.72 | 83.18 | 120.22 | 86.67 | 119.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 0.74 | 2 | 2 | 9.54 | 11.5 | -8.73 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 18.3 | 17.52 | 13.25 | 120.37 | 71.8 | 126.98 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.75 | 0.76 | 2 | 2 | 12.67 | 14.61 | -3.2 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | 3.75 | -8.4 | -4.76 | -16.67 | 5.57 | 5.57 | False |  | distribution_warning | -0.82 | -1.08 | 1 | 2 | -1.99 | -1.26 | -17.05 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_僅留完整清單 | 33032.925531914894 | 13849.620888036585 | 4.21 | -2.97 | 15.62 | 18.09 | 21.28 | 27.99 | False |  | mild_accumulation | 0.19 | 0.45 | 1 | 2 | 3.12 | 4.67 | -5.03 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 0.81 | -3.88 | -7.12 | 9.73 | 10.71 | 15.89 | False |  | mild_accumulation | 0.73 | 0.0 | 2 | 0 | -1.88 | -0.58 | -13.29 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 6.17 | 11.88 | 31.66 | 54.49 | 50.3 | 63.61 | True | 距60日低點反彈>50% | strong_accumulation | 1.79 | 2.01 | 3 | 2 | 7.35 | 9.86 | 0.0 |  | fail_already_priced_in |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | 3.44 | -6.65 | 70.81 | 273.54 | 82.68 | 294.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.17 | -1.49 | 1 | 0 | -5.84 | -0.53 | -17.17 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 2.36 | -16.13 | -25.5 | -28.96 | 3.17 | 3.17 | False |  | distribution_warning | -0.49 | -0.03 | 0 | 1 | -4.85 | -4.77 | -25.93 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | 1.16 | -7.97 | -3.16 | -18.94 | 2.51 | 3.73 | False |  | distribution_warning | -0.6 | -0.75 | 1 | 1 | -2.17 | -2.09 | -15.59 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | -1.8 | 22.44 | -11.53 | 146.73 | 25.74 | 164.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.3 | -0.83 | 1 | 1 | 8.22 | 6.73 | -27.58 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 3.2 | -8.52 | 11.88 | 27.23 | 13.12 | 27.1 | False |  | distribution_warning | -0.62 | 0.0 | 0 | 0 | -0.28 | 0.73 | -13.56 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 3.93 | -0.78 | -4.65 | 16.3 | 8.18 | 23.06 | False |  | mild_accumulation | -0.02 | 0.01 | 1 | 1 | 2.31 | 2.31 | -5.37 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 8.29 | 4.59 | -7.5 | 155.17 | 35.16 | 158.89 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.17 | 0.0 | 1 | 0 | 3.46 | 3.6 | -23.58 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 43.0 | 125.77 | 55.29 | 262.35 | 128.4 | 288.74 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.67 | 2.0 | 2 | 2 | 61.14 | 51.53 | -0.51 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | -0.95 | -1.26 | -33.26 | 57.13 | 23.23 | 69.01 | False |  | mild_accumulation | 0.18 | -0.66 | 2 | 1 | -1.26 | -1.33 | -34.24 | 17 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 1.01 | 2.04 | -2.72 | 29.79 | 10.6 | 32.19 | False |  | mild_accumulation | -0.01 | 0.04 | 1 | 1 | 0.18 | 0.01 | -8.74 | 20 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 1.1 | -0.72 | -51.11 | 123.58 | 20.48 | 120.44 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.98 | -0.65 | 1 | 1 | -0.4 | -2.12 | -54.92 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | 2.07 | 2.07 | 2.93 | 35.91 | 12.84 | 34.06 | False |  | strong_accumulation | 0.1 | 0.11 | 2 | 2 | 1.79 | 1.98 | -1.8 | 21 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | 1.68 | -1.22 | -25.08 | -6.2 | 31.81 | 31.81 | False |  | mild_accumulation | -0.05 | 0.28 | 2 | 2 | -0.86 | -0.7 | -30.66 | 21 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 4.66 | -0.83 | -18.22 | 95.53 | 53.42 | 114.2 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | -0.7 | 2 | 2 | 1.83 | 3.37 | -20.22 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | -1.59 | -8.85 | -22.06 | 16.67 | 3.63 | 15.94 | False |  | distribution_warning | -0.64 | -0.49 | 1 | 0 | -7.41 | -7.29 | -34.34 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 2.02 | 3.77 | -4.42 | 17.31 | 13.08 | 17.31 | False |  | distribution_warning | -0.19 | -0.45 | 0 | 0 | 3.07 | 2.32 | -7.63 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral | D_僅留完整清單 | 540.5590508718318 | 80.61133112104658 | 5.55 | 2.49 | 4.36 | -7.25 | 11.08 | 11.08 | False |  | mild_accumulation | 0.56 | -0.25 | 3 | 0 | 3.99 | 3.57 | -9.84 | 20 | selected |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | 3.21 | 31.97 | 15.55 | 142.47 | 94.76 | 140.3 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.4 | 6.75 | 3 | 3 | 4.08 | 7.26 | -6.03 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 3.9 | 4.23 | 28.34 | 72.97 | 51.18 | 76.15 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.42 | 0.16 | 3 | 2 | -0.7 | 1.83 | -6.8 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | 6.02 | 9.05 | 4.81 | 49.19 | 32.37 | 47.27 | False |  | distribution_warning | -0.12 | -0.04 | 2 | 2 | 9.36 | 7.83 | -8.03 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 81.06426064737752 | 92.59516265483826 | 5.92 | 5.92 | -29.43 | 15.98 | 21.22 | 21.22 | False |  | distribution_warning | -0.75 | -0.35 | 0 | 0 | 4.26 | 2.99 | -29.25 | 13 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 76.38825024031777 | 71.24826737205954 | -0.97 | 5.7 | -17.74 | 12.71 | 44.68 | 44.68 | False |  | mild_accumulation | -0.41 | 0.01 | 1 | 2 | -3.56 | -1.32 | -23.6 | 17 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 2.01 | 4.86 | 6.59 | 56.14 | 14.1 | 60.36 | False |  | mild_accumulation | 0.2 | 0.27 | 2 | 1 | 1.09 | 1.22 | -11.44 | 21 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | 1.93 | 6.69 | -6.41 | 20.56 | 22.94 | 22.94 | False |  | strong_accumulation | 0.09 | 0.01 | 2 | 2 | 1.89 | 2.25 | -12.72 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.84671742960728 | 95.18081273476336 | -8.85 | -13.91 | -13.3 | 75.58 | 24.43 | 71.58 | True | 近120日漲幅>70% | distribution_warning | -1.1 | -0.4 | 0 | 1 | -8.82 | -7.73 | -24.42 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -7.05 | -5.41 | -7.78 | 35.99 | 11.66 | 40.64 | False |  | strong_accumulation | 0.83 | 1.11 | 2 | 3 | -5.53 | -5.24 | -17.47 | 18 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 2.37 | 6.32 | 43.75 | 113.29 | 52.32 | 116.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.63 | -0.1 | 0 | 1 | 1.66 | 2.84 | -5.09 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 11.94 | 6.13 | -17.58 | 35.71 | 15.38 | 35.71 | False |  | distribution_warning | -0.04 | -0.41 | 2 | 1 | 6.33 | 5.38 | -22.41 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 86.10504037359958 | 114.852843965949 | 4.73 | -2.81 | -22.11 | -10.23 | 6.96 | 6.96 | False |  | distribution_warning | -0.68 | -1.27 | 1 | 0 | 0.67 | -0.62 | -39.83 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 6.49 | -0.57 | 10.06 | 161.85 | 63.04 | 163.82 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -1.87 | 2 | 2 | 3.1 | 5.37 | -7.73 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.57 | 1.91 | -11.31 | 24.24 | 3.9 | 25.12 | False |  | strong_accumulation | 0.3 | 0.27 | 3 | 3 | 1.8 | 0.74 | -21.27 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 245.59047432473767 | 22.17724035271652 | 3.14 | 13.18 | -0.53 | -15.07 | 26.82 | 26.82 | False |  | distribution_warning | -0.3 | -1.04 | 1 | 0 | 5.54 | 5.25 | -8.22 | 17 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 0.14 | -1.46 | -12.63 | 42.31 | 4.96 | 42.31 | False |  | strong_accumulation | 0.94 | 1.68 | 2 | 3 | -0.62 | -2.55 | -30.06 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 1.96 | 2.56 | -15.58 | 73.33 | 32.65 | 78.69 | True | 近120日漲幅>70% | distribution_warning | -2.46 | -0.99 | 1 | 0 | 2.53 | 2.6 | -28.47 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.92 | 0.37 | -3.68 | 3.39 | 2.04 | 8.93 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.16 | -0.29 | -6.47 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 2.99 | 27.44 | 51.4 | 111.97 | 58.77 | 116.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 2.82 | 3.67 | -31.72 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | 9.71 | 16.76 | -6.07 | -11.06 | 30.62 | 30.62 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 7.5 | 7.46 | -9.13 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | 2.35 | -9.44 | -1.74 | 21.46 | 31.02 | 31.02 | False |  | distribution_warning | -0.28 | -0.25 | 1 | 2 | -2.01 | -0.54 | -14.11 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 7.96 | 36.95 | 43.11 | 114.67 | 118.04 | 118.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.41 | 4.4 | 3 | 2 | 11.79 | 13.68 | -1.77 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | -1.0 | 3.3 | -23.52 | 18.53 | 10.19 | 18.29 | False |  | strong_accumulation | 0.32 | 0.06 | 3 | 3 | 2.25 | 1.08 | -27.17 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 4.51 | 10.06 | 16.22 | 196.24 | 66.95 | 199.85 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | -1.38 | 1 | 1 | 2.05 | 4.96 | -12.05 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 383.2629286702524 | 200.70869091113056 | 1.78 | 6.64 | 18.04 | 75.48 | 35.91 | 75.48 | True | 近120日漲幅>70% | strong_accumulation | 1.36 | 2.41 | 2 | 2 | -2.65 | -0.28 | -14.79 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | -4.35 | -5.71 | -9.74 | 34.69 | 22.79 | 34.35 | False |  | distribution_warning | -0.18 | -1.02 | 2 | 1 | -7.64 | -5.36 | -21.43 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 1.17 | -0.92 | -45.59 | 64.26 | 8.82 | 68.75 | False |  | distribution_warning | -0.96 | -0.99 | 1 | 1 | -0.82 | -2.6 | -55.74 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.41 | -0.2 | -11.2 | -0.91 | 3.5 | 3.5 | False |  | mild_accumulation | -0.33 | 0.27 | 2 | 3 | 0.58 | 0.15 | -10.88 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 106.21354266385858 | 53.00526357886879 | 1.6 | 2.42 | -28.88 | 18.91 | 21.76 | 21.76 | False |  | strong_accumulation | 0.34 | 1.6 | 2 | 3 | 1.27 | 1.04 | -31.56 | 23 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | 3.11 | 0.68 | 11.19 | 4.56 | 15.95 | 23.14 | False |  | distribution_warning | -0.15 | 0.0 | 1 | 0 | 0.39 | 2.47 | -5.1 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 87.88742117627663 | 23.60389010735311 | -0.71 | 0.36 | 3.2 | 4.22 | 4.35 | 11.27 | False |  | strong_accumulation | 0.16 | 0.29 | 3 | 2 | 0.08 | 0.1 | -3.89 | 20 | selected |
| 2540 | 愛山林 | 建材營造 | neutral | D_僅留完整清單 | 98.38295459889332 | -25.14735482235493 | 3.05 | 6.41 | -6.64 | 4.87 | 19.2 | 19.2 | False |  | strong_accumulation | 0.1 | 0.06 | 2 | 2 | 5.13 | 3.77 | -18.12 | 13 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 51.50921763610771 | 59.40841445991509 | 4.09 | 1.28 | -0.88 | -31.27 | 11.28 | 11.28 | False |  | mild_accumulation | -0.11 | 0.39 | 1 | 3 | 2.15 | 2.07 | -5.51 | 17 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | 2.85 | -1.46 | -7.76 | -4.27 | 5.21 | 5.21 | False |  | distribution_warning | -0.14 | -0.16 | 1 | 1 | 1.38 | 1.02 | -14.41 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | B_可觀察 | 139.52959372288657 | 105.3349499169469 | 1.69 | -1.03 | -6.31 | -20.9 | 5.46 | 5.46 | False |  | mild_accumulation | 0.08 | -0.29 | 2 | 0 | 2.31 | 2.11 | -7.21 | 21 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 58.75071504262123 | 38.71801301175803 | -1.1 | -4.5 | 16.64 | -12.59 | 26.0 | 26.0 | False |  | distribution_warning | -0.98 | -1.66 | 2 | 1 | 0.68 | 1.61 | -7.91 | 12 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 0.0 | -2.86 | 1.86 | 3.34 | 14.47 | 14.47 | False |  | strong_accumulation | 1.33 | 0.5 | 2 | 3 | 1.38 | 1.98 | -9.76 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | 6.69 | 7.33 | 7.11 | 57.56 | 20.44 | 57.1 | False |  | distribution_warning | 0.0 | -0.01 | 2 | 0 | 6.54 | 4.87 | -38.62 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 3.33 | -9.24 | -14.14 | 19.23 | 11.34 | 20.94 | False |  | distribution_warning | -0.15 | -1.77 | 2 | 0 | -5.99 | -4.01 | -20.41 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 0.84 | -1.24 | -7.72 | 16.02 | 4.82 | 10.65 | False |  | distribution_warning | -1.05 | -1.93 | 0 | 0 | 0.13 | -0.79 | -26.69 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 0.17 | 13.45 | 21.25 | 93.36 | 80.75 | 97.96 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.06 | 1.68 | 2 | 2 | 2.71 | 5.04 | -8.78 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 6.39 | 18.39 | -12.73 | 128.43 | 60.25 | 127.54 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.46 | 1.07 | 1 | 2 | 11.16 | 9.23 | -18.53 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 1.78 | 19.72 | 36.93 | 65.7 | 70.22 | 70.22 | True | 距60日低點反彈>50% | mild_accumulation | -0.15 | 0.05 | 1 | 1 | 4.25 | 6.78 | -4.59 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 8.6 | -13.98 | -2.83 | 1.27 | 9.59 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.88 | -0.45 | -36.51 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 84.97614765538744 | 32.40539437293427 | 9.38 | 0.89 | 10.17 | 46.54 | 17.88 | 50.17 | False |  | distribution_warning | -1.69 | -0.08 | 0 | 2 | 1.91 | 1.84 | -21.89 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 0.16 | -7.9 | -20.57 | 23.11 | 9.38 | 21.18 | False |  | distribution_warning | -0.95 | -0.55 | 0 | 0 | -2.68 | -2.78 | -27.55 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 0.12 | -8.47 | -15.53 | 30.61 | 3.35 | 30.0 | False |  | distribution_warning | -2.89 | -2.99 | 0 | 1 | -4.26 | -4.4 | -29.97 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 98.21291582397656 | 109.2004683088644 | 7.59 | -0.24 | -5.52 | -8.26 | 14.17 | 14.17 | False |  | distribution_warning | -0.99 | -0.27 | 1 | 1 | 5.7 | 4.14 | -12.74 | 13 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 0.41 | -9.59 | -3.82 | 89.02 | 50.23 | 80.0 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.47 | 0.62 | 3 | 2 | -2.18 | -0.3 | -20.24 |  | fail_already_priced_in |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 143.33455025414924 | 69.46103918462916 | 2.22 | 2.68 | -21.37 | 5.75 | 15.58 | 15.58 | False |  | mild_accumulation | -0.34 | 0.99 | 1 | 3 | 1.12 | 1.0 | -22.95 | 22 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 1.97 | 12.85 | -2.63 | 49.49 | 58.41 | 58.41 | True | 距60日低點反彈>50% | distribution_warning | -0.02 | -0.69 | 1 | 0 | 5.03 | 5.86 | -3.18 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | 1.59 | -8.93 | -23.88 | 49.34 | 21.14 | 50.66 | False |  | distribution_warning | -0.73 | -1.66 | 0 | 0 | -3.67 | -3.23 | -25.87 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 3.21 | 8.65 | -11.89 | -14.24 | 28.44 | 28.44 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 3.46 | 4.19 | -11.35 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 10.68 | 57.6 | 67.65 | 198.43 | 94.76 | 203.73 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.92 | -1.18 | 0 | 0 | 21.41 | 19.31 | -14.93 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | 0.62 | -4.11 | -14.4 | 56.46 | 22.01 | 57.21 | False |  | mild_accumulation | -0.46 | 0.91 | 1 | 1 | -4.69 | -2.3 | -17.01 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 0.72 | 15.03 | 6.24 | 87.21 | 91.94 | 91.94 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 1.87 | 1 | 1 | 4.54 | 5.16 | -14.11 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -4.59 | 4.21 | 42.79 | 247.17 | 83.21 | 257.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.36 | 0.43 | 2 | 1 | 12.36 | 12.58 | -11.66 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 166.4840985505344 | 98.8701912579111 | 0.54 | 6.27 | 16.56 | 49.2 | 34.17 | 51.63 | False |  | distribution_warning | -0.65 | -0.91 | 1 | 1 | 1.14 | 1.24 | -9.47 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 0.0 | 0.0 | 2.94 | 6.46 | 5.66 | 17.65 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | 0.39 | 0.7 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 10.57 | 21.13 | 2.52 | 23.05 | 24.84 | 27.51 | False |  | mild_accumulation | -0.44 | 1.2 | 1 | 3 | 15.41 | 13.23 | -2.27 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 8.36 | 4.36 | -17.29 | -6.61 | 10.28 | 10.28 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 7.0 | 5.27 | -17.29 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 16.83 | 27.68 | 47.42 | 208.19 | 125.2 | 207.53 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -1.19 | 0 | 1 | 18.17 | 19.98 | 0.0 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | 5.08 | -2.36 | -8.19 | 123.24 | 63.03 | 118.26 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.09 | -1.86 | 1 | 1 | -3.12 | 0.26 | -17.61 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | -4.16 | 2.41 | 62.98 | 48.92 | 84.78 | 97.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -1.06 | 2.51 | 0 | 3 | -1.71 | 2.35 | -9.35 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 273.61017160561573 | 13.583391933925409 | -3.01 | -4.32 | -16.31 | 30.87 | 34.6 | 34.6 | False |  | distribution_warning | -0.07 | -1.69 | 1 | 1 | -8.2 | -5.61 | -27.68 | 12 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 17.87 | -2.86 | 15.1 | 15.71 | 31.16 | 31.16 | False |  | distribution_warning | -1.83 | -1.94 | 0 | 0 | 7.07 | 6.87 | -13.5 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 80.45926827221638 | 62.39086469044157 | 7.51 | 3.15 | 7.01 | 30.11 | 17.8 | 29.52 | False |  | distribution_warning | -1.05 | -1.36 | 1 | 1 | 8.37 | 6.01 | -12.26 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | 0.5 | -10.56 | -5.85 | 7.76 | 3.74 | 7.91 | False |  | distribution_warning | -0.57 | -0.39 | 2 | 2 | -7.97 | -6.23 | -15.97 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral | B_可觀察 | 534.5730588954555 | 23.246721642333693 | 1.04 | -6.57 | -15.91 | -16.64 | 12.97 | 12.97 | False |  | mild_accumulation | 0.53 | -0.04 | 2 | 1 | -2.65 | -1.99 | -19.42 | 17 | selected |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | -3.66 | 10.75 | -33.05 | -31.1 | 32.4 | 32.4 | False |  | strong_accumulation | 0.01 | 0.48 | 2 | 2 | -1.99 | -1.95 | -36.46 | 20 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -0.17 | 11.28 | 30.35 | 12.79 | 33.79 | 46.97 | False |  | strong_accumulation | 0.45 | 0.45 | 2 | 2 | 3.89 | 3.96 | -4.12 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -1.78 | 4.08 | 9.03 | -23.24 | 13.5 | 13.5 | False |  | distribution_warning | -0.17 | -0.17 | 0 | 0 | 2.43 | 2.49 | -7.13 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | -0.62 | -3.73 | 2.71 | 14.16 | 9.32 | 16.64 | False |  | distribution_warning | -2.65 | -1.56 | 0 | 0 | -0.05 | -1.21 | -19.37 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | -0.83 | 18.52 | 9.59 | 83.91 | 48.15 | 83.21 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.41 | 1.84 | 2 | 3 | 5.33 | 5.15 | -6.98 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -1.1 | -5.27 | -10.74 |  | 2.05 |  | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | -2.63 | -3.98 | -23.64 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | 6.7 | 8.04 | 13.46 | 19.78 | 22.16 | 22.16 | False |  | distribution_warning | -0.09 | -0.48 | 1 | 0 | 3.01 | 3.86 | -2.93 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 9.6 | 1.78 | -25.24 | 120.35 | 16.95 | 120.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 9.85 | 4.9 | -29.68 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | 11.88 | 6.89 | 6.03 | 93.22 | 20.71 | 98.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 7.18 | 6.88 | -11.72 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 3.73 | -3.47 | -20.34 | -12.85 | 5.7 | 5.7 | False |  | distribution_warning | -0.15 | -0.21 | 1 | 1 | 0.04 | -0.12 | -27.23 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | -2.48 | 6.88 | -15.03 | 16.38 | 38.15 | 38.15 | False |  | mild_accumulation | -0.56 | 0.11 | 2 | 2 | -1.12 | 0.41 | -14.94 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | -1.25 | 0.36 | 0.36 | 32.54 | 41.69 | 41.69 | False |  | mild_accumulation | 2.62 | -1.07 | 2 | 1 | 0.55 | 1.71 | -4.97 | 24 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 0.0 | 16.28 | -1.13 | -4.11 | 66.67 | 66.67 | True | 距60日低點反彈>50% | distribution_warning | -4.27 | -1.28 | 0 | 1 | 2.2 | 4.49 | -7.65 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | 1.5 | -1.45 | -33.26 | -3.79 | 21.76 | 21.76 | False |  | distribution_warning | -1.43 | -0.61 | 1 | 1 | -1.95 | -2.27 | -48.09 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 4.71 | -1.05 | 3.56 | 34.52 | 9.57 | 35.97 | False |  | mild_accumulation | 0.89 | 0.0 | 3 | 0 | 1.06 | 1.09 | -5.5 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | 1.37 | -1.33 | 1.6 | -9.55 | 4.71 | 8.8 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 0 | 0.9 | 0.87 | -6.9 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 1.8 | 1.07 | 1.43 | -1.74 | 5.2 | 5.2 | False |  | mild_accumulation | 0.15 | -0.1 | 2 | 2 | 1.58 | 1.51 | -1.39 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 88.58141426234812 | 67.0501740981801 | 3.24 | -4.98 | -3.05 | -1.67 | 5.09 | 5.09 | False |  | distribution_warning | -1.12 | -1.0 | 1 | 0 | 1.17 | 0.82 | -7.51 | 15 | selected |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 98.63848944446872 | 32.20453750927072 | -2.25 | 9.8 | 17.85 | 137.95 | 79.96 | 160.99 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.27 | -4.27 | 1 | 1 | -3.76 | 1.85 | -16.78 |  | fail_already_priced_in |