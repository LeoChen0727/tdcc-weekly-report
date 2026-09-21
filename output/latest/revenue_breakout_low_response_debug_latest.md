# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-21 19:38:51 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 725611 |
| tdcc_rows | 1963 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 374 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 652 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 105 |
| already_priced_in_excluded | 40 |
| overheat_pass | 65 |
| score_pass | 65 |
| theme_priority_pass | 53 |
| final_rows | 53 |

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
| fail_low_response_condition | 255 |
| fail_already_priced_in | 40 |
| fail_defensive_or_traditional_excluded | 11 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | 1.04 | 23.73 | 4.29 | 8.15 | 35.19 | 46.29 | False |  | mild_accumulation | 0.28 | 0.78 | 1 | 2 | 1.02 | 3.37 | -11.52 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 93.04522686147229 | 122.05590293593936 | 0.0 | -5.31 | 5.94 | -11.57 | 13.95 | 13.95 | False |  | mild_accumulation | -0.81 | 0.13 | 1 | 2 | -1.83 | -0.37 | -14.4 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 0.97 | 0.97 | -1.51 | -22.47 | 4.41 | 4.41 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.06 | 0.41 | -16.1 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 0.2 | -2.91 | -9.91 | 14.94 | 5.37 | 15.34 | False |  | mild_accumulation | 0.11 | -0.33 | 1 | 0 | -1.89 | -1.81 | -15.97 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 0.86 | -1.68 | -1.4 | -7.87 | 1.74 | 3.54 | False |  | strong_accumulation | 0.07 | 0.02 | 2 | 2 | -0.71 | -0.91 | -12.9 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -0.29 | -2.8 | -9.03 | -12.8 | 1.91 | 1.91 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -1.57 | -1.71 | -11.58 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 2.81 | -2.23 | -3.73 | -21.75 | 7.33 | 14.92 | False |  | strong_accumulation | 0.14 | 0.15 | 3 | 3 | -0.54 | -0.23 | -10.22 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 2.03 | 0.0 | -10.36 | -7.72 | 6.81 | 6.81 | False |  | strong_accumulation | 0.39 | 0.11 | 2 | 2 | 1.87 | 1.74 | -19.03 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 1.4 | 7.01 | 1.4 | 0.35 | 9.85 | 19.83 | False |  | distribution_warning | -0.18 | -0.2 | 2 | 2 | 3.2 | 3.24 | -6.15 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 19.56 | 24.39 | 104.75 | 139.44 | 104.27 | 141.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.14 | 2.68 | 3 | 3 | 19.03 | 20.33 | 0.0 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 16.78 | 14.44 | 17.05 | 118.68 | 66.94 | 115.48 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.09 | 7.42 | 2 | 2 | 8.73 | 10.32 | -5.94 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | 2.59 | -9.18 | -2.73 | -16.24 | 4.4 | 4.4 | False |  | distribution_warning | -0.81 | -1.37 | 1 | 1 | -2.6 | -2.17 | -17.97 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 33032.925531914894 | 13849.620888036585 | 8.13 | 0.56 | 17.32 | 17.32 | 21.28 | 27.99 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | 3.09 | 4.26 | -5.03 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 0.81 | -4.25 | -3.88 | 12.22 | 10.71 | 15.89 | False |  | mild_accumulation | -0.55 | 0.01 | 1 | 1 | -1.67 | -0.53 | -13.29 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 57.69192058134775 | 20.405940800672543 | 6.9 | 7.83 | 32.27 | 53.56 | 49.4 | 62.62 | False |  | mild_accumulation | 0.4 | -0.41 | 3 | 1 | 6.29 | 8.37 | -0.6 | 16 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | 6.76 | -11.17 | 83.12 | 303.15 | 87.13 | 293.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.87 | -0.02 | 0 | 1 | -2.95 | 1.74 | -15.15 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 0.78 | -14.29 | -21.58 | -24.34 | 2.38 | 2.38 | False |  | mild_accumulation | -0.56 | 0.09 | 0 | 2 | -4.83 | -5.07 | -22.75 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | 1.16 | -8.96 | -2.09 | -14.08 | 2.18 | 3.39 | False |  | distribution_warning | -0.93 | -0.97 | 0 | 0 | -2.02 | -2.21 | -15.86 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 13.45 | 35.85 | 1.89 | 158.37 | 38.28 | 166.67 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | -1.49 | 0 | 1 | 17.18 | 15.7 | -20.35 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 2.2 | -4.72 | 10.6 | 23.72 | 10.6 | 25.65 | False |  | mild_accumulation | 0.44 | 0.01 | 1 | 1 | -1.18 | -0.39 | -14.55 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 4.15 | -0.32 | -0.63 | 17.2 | 6.81 | 21.51 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | 1.04 | 0.93 | -6.56 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 6.13 | 3.52 | -6.26 | 149.44 | 34.4 | 157.43 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.68 | 0.66 | 1 | 1 | 2.7 | 2.76 | -24.01 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 30.23 | 120.64 | 67.52 | 265.22 | 128.79 | 289.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 3.2 | 2 | 2 | 54.59 | 45.51 | -5.01 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 61.18890785808584 | 40.59833569613409 | 0.65 | 0.32 | -32.17 | 68.47 | 22.83 | 65.78 | False |  | mild_accumulation | 0.32 | -0.71 | 2 | 1 | -1.59 | -1.51 | -33.62 |  | fail_low_response_condition |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 0.6 | 2.67 | 0.6 | 30.21 | 10.38 | 27.23 | False |  | mild_accumulation | 0.07 | 0.06 | 1 | 1 | -0.15 | -0.18 | -8.93 | 19 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 2.2 | 1.09 | -45.12 | 117.58 | 22.02 | 110.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -0.78 | 1 | 1 | 0.81 | -0.8 | -54.34 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 53.32005371471296 | 39.26370665798065 | 4.2 | 4.42 | 5.98 | 33.33 | 13.76 | 28.83 | False |  | distribution_warning | -0.03 | -0.05 | 1 | 1 | 2.39 | 2.57 | -1.0 | 15 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 218.53271706735816 | 149.1423915250992 | 3.45 | -3.23 | -26.15 | -12.09 | 30.72 | 30.72 | False |  | distribution_warning | -1.14 | -1.2 | 1 | 1 | -1.52 | -1.4 | -28.36 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 8.75 | -1.69 | -15.74 | 94.63 | 48.72 | 107.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.1 | -3.77 | 1 | 1 | -1.21 | 0.19 | -18.12 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | -1.87 | -11.11 | -22.69 | 13.93 | 2.79 | 10.18 | False |  | distribution_warning | -0.62 | -0.71 | 1 | 0 | -7.63 | -7.42 | -34.87 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 0.22 | 1.7 | -3.23 | 13.96 | 11.83 | 13.96 | False |  | distribution_warning | -0.05 | -0.42 | 1 | 0 | 1.85 | 1.09 | -8.65 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | 3.55 | 1.96 | 3.99 | -9.2 | 9.28 | 9.28 | False |  | mild_accumulation | 1.06 | -0.22 | 3 | 0 | 2.21 | 1.73 | -11.3 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -7.98 | 17.96 | 20.36 | 116.97 | 90.73 | 116.97 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.96 | 3.36 | 3 | 3 | 1.14 | 4.6 | -7.98 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 1.28 | 2.49 | 34.95 | 72.0 | 48.98 | 68.93 | True | 近120日漲幅>70% | mild_accumulation | -0.02 | 0.53 | 2 | 2 | -2.26 | 0.32 | -8.16 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 156.29654201767283 | 108.41049971158722 | 10.98 | 14.73 | 16.71 | 51.27 | 37.28 | 38.08 | False |  | distribution_warning | -0.74 | -0.06 | 1 | 2 | 12.6 | 10.74 | -5.57 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 14.79 | 16.6 | -13.99 | 24.6 | 33.18 | 33.18 | False |  | mild_accumulation | 0.38 | 0.11 | 1 | 1 | 13.63 | 11.93 | -22.27 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 76.38825024031777 | 71.24826737205954 | 2.45 | 10.23 | -12.18 | 12.73 | 48.23 | 48.23 | False |  | distribution_warning | -0.82 | -0.53 | 1 | 1 | -1.65 | 1.0 | -21.72 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 6.98 | 7.92 | 15.18 | 65.39 | 17.95 | 60.7 | False |  | strong_accumulation | 0.89 | 1.38 | 3 | 2 | 4.09 | 4.23 | -8.46 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | 3.61 | 6.0 | -4.83 | 19.2 | 23.48 | 23.48 | False |  | strong_accumulation | 0.37 | 0.36 | 3 | 3 | 2.04 | 2.46 | -12.34 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 129.84671742960728 | 95.18081273476336 | -8.42 | -9.85 | -6.85 | 69.67 | 24.55 | 56.14 | False |  | distribution_warning | -0.63 | -0.7 | 1 | 1 | -8.27 | -7.04 | -24.34 | 15 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -3.6 | -3.33 | -1.69 | 40.24 | 11.34 | 38.29 | False |  | strong_accumulation | 0.15 | 0.61 | 2 | 2 | -5.65 | -5.08 | -17.71 | 18 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 5.37 | 7.29 | 54.99 | 118.91 | 54.32 | 110.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.36 | -0.63 | 1 | 0 | 3.66 | 4.76 | -2.89 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 11.33 | 6.1 | -15.67 | 32.16 | 15.9 | 29.59 | False |  | mild_accumulation | 0.1 | -0.56 | 2 | 1 | 6.48 | 5.33 | -22.07 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 14.72 | 7.42 | -12.01 | -0.98 | 17.6 | 17.6 | False |  | distribution_warning | -0.36 | -0.54 | 1 | 1 | 10.26 | 8.43 | -33.84 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 9.09 | 2.99 | 14.92 | 150.49 | 60.25 | 159.3 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.57 | -3.29 | 1 | 1 | 1.18 | 3.25 | -9.31 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.38 | 0.76 | -9.88 | 24.03 | 3.12 | 23.02 | False |  | strong_accumulation | 0.26 | 0.17 | 3 | 3 | 0.99 | -0.01 | -21.86 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | 14.58 | 25.1 | 13.94 | -8.78 | 39.32 | 39.32 | True | 近20日漲幅>25% | distribution_warning | -0.2 | -0.67 | 1 | 1 | 14.61 | 14.14 | 0.0 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 4.96 | 0.53 | -3.42 | 45.42 | 8.09 | 45.7 | False |  | strong_accumulation | 0.68 | 1.24 | 2 | 3 | 2.31 | 0.32 | -27.98 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 2.17 | 3.19 | -12.82 | 74.66 | 31.89 | 71.19 | True | 近120日漲幅>70% | distribution_warning | -0.49 | -0.05 | 2 | 0 | 1.78 | 1.84 | -28.89 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.55 | -0.72 | -0.54 | 4.57 | 2.04 | 8.93 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.13 | -0.27 | -6.47 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | -0.98 | 13.46 | 44.18 | 107.88 | 55.44 | 111.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 0.07 | 1.37 | -33.15 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | 8.95 | 13.74 | -5.05 | -8.0 | 29.37 | 29.37 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.79 | 5.86 | -10.0 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | 4.38 | -9.49 | 2.69 | 22.48 | 32.41 | 32.41 | False |  | distribution_warning | -1.2 | -1.15 | 0 | 1 | -0.45 | 0.47 | -13.2 | 16 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 6.92 | 49.93 | 64.37 | 101.05 | 124.31 | 124.31 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.84 | 3.37 | 2 | 1 | 12.85 | 15.33 | -3.05 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 2.38 | 4.33 | -16.25 | 13.56 | 11.67 | 14.86 | False |  | strong_accumulation | 0.36 | 0.12 | 3 | 3 | 3.4 | 2.23 | -26.19 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 9.69 | 2.67 | 23.79 | 192.55 | 63.14 | 187.31 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.62 | -8.2 | 0 | 0 | -0.41 | 2.34 | -14.06 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | 3.84 | 0.33 | 28.13 | 69.43 | 36.5 | 64.87 | False |  | distribution_warning | -0.68 | -0.45 | 1 | 2 | -2.24 | 0.14 | -14.42 | 18 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | -2.05 | -1.31 | -6.07 | 28.76 | 22.33 | 23.76 | False |  | distribution_warning | -0.34 | -0.83 | 1 | 1 | -7.93 | -5.27 | -21.73 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 1.19 | -3.18 | -43.35 | 66.41 | 7.3 | 60.15 | False |  | distribution_warning | -1.04 | -0.07 | 1 | 1 | -2.04 | -3.63 | -56.35 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.83 | -0.31 | -9.89 | -1.61 | 3.5 | 3.5 | False |  | strong_accumulation | 0.26 | 0.26 | 3 | 3 | 0.6 | 0.14 | -10.71 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 106.21354266385858 | 53.00526357886879 | 4.83 | 4.27 | -22.27 | 21.81 | 25.12 | 25.12 | False |  | strong_accumulation | 0.29 | 1.52 | 2 | 2 | 3.84 | 3.5 | -29.68 | 22 | selected |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -0.69 | -6.06 | -10.14 | -3.77 | 4.08 | 4.08 | False |  | distribution_warning | -0.52 | -0.45 | 1 | 1 | -2.34 | -2.0 | -12.85 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | 3.14 | 1.02 | 12.12 | 4.96 | 15.18 | 22.31 | False |  | distribution_warning | -0.2 | 0.0 | 0 | 0 | -0.34 | 1.63 | -5.73 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | 0.48 | 1.56 | 4.71 | 4.71 | 4.71 | 11.94 | False |  | strong_accumulation | 0.17 | 0.14 | 3 | 2 | 0.6 | 0.64 | -3.32 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | 2.19 | 6.05 | -7.18 | 3.48 | 15.67 | 15.67 | False |  | strong_accumulation | 0.16 | 0.04 | 3 | 2 | 1.71 | 0.64 | -20.55 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | 2.13 | -0.65 | 0.26 | -32.98 | 8.32 | 8.32 | False |  | mild_accumulation | -0.01 | 0.14 | 2 | 2 | -0.54 | -0.6 | -8.02 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | 2.56 | -1.48 | -8.26 | -6.54 | 4.17 | 4.17 | False |  | distribution_warning | -0.45 | -0.29 | 0 | 0 | 0.45 | 0.02 | -15.25 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | B_可觀察 | 139.52959372288657 | 105.3349499169469 | 0.86 | -3.0 | -8.59 | -23.2 | 2.4 | 2.4 | False |  | mild_accumulation | -0.47 | 0.05 | 1 | 1 | -0.51 | -0.78 | -9.9 | 21 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | 3.18 | 1.91 | 27.3 | -10.34 | 30.19 | 30.19 | False |  | strong_accumulation | 1.57 | 1.26 | 3 | 2 | 3.92 | 4.55 | -4.85 | 18 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 1.15 | -5.5 | 3.37 | 2.62 | 13.34 | 13.34 | False |  | strong_accumulation | 1.43 | 1.44 | 3 | 3 | 0.68 | 0.9 | -10.65 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | 8.32 | 24.03 | 14.6 | 77.13 | 44.33 | 85.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.08 | 1.23 | 3 | 3 | 12.42 | 12.45 | -1.21 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | 7.8 | 6.92 | 10.76 | 46.24 | 16.67 | 46.24 | False |  | distribution_warning | -0.04 | -0.02 | 1 | 0 | 2.85 | 1.45 | -40.54 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 3.15 | -7.82 | -10.35 | 20.33 | 11.34 | 19.11 | False |  | distribution_warning | -0.71 | -1.56 | 1 | 0 | -5.61 | -3.69 | -20.41 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 1.73 | -2.08 | -7.84 | 3.98 | 3.07 | 8.8 | False |  | distribution_warning | -0.88 | -1.69 | 0 | 0 | -1.45 | -2.25 | -27.91 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 5.36 | 1.06 | 25.55 | 81.53 | 77.02 | 93.88 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.19 | -3.17 | 1 | 1 | 0.54 | 2.63 | -10.66 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 7.11 | 20.5 | -3.21 | 133.98 | 65.75 | 127.36 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.99 | 1 | 1 | 13.86 | 11.77 | -15.73 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 3.17 | 19.61 | 51.44 | 68.23 | 69.48 | 69.48 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.77 | 0.44 | 1 | 2 | 2.92 | 5.76 | -5.01 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 5.73 | -11.11 | -0.41 | 0.0 | 9.59 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.52 | -0.41 | -36.51 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 84.97614765538744 | 32.40539437293427 | 7.66 | -1.07 | 14.15 | 52.63 | 20.21 | 51.39 | False |  | mild_accumulation | -0.61 | 0.45 | 1 | 2 | 3.98 | 3.52 | -20.34 | 19 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 2.61 | -5.85 | -22.37 | 18.94 | 11.15 | 16.08 | False |  | distribution_warning | -0.54 | -0.14 | 1 | 1 | -0.8 | -1.1 | -26.38 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 1.21 | -10.47 | -14.49 | 29.12 | 4.1 | 28.13 | False |  | distribution_warning | -2.0 | -2.72 | 0 | 1 | -3.03 | -3.41 | -29.46 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 7.55 | 2.99 | -4.18 | -9.23 | 14.72 | 14.72 | False |  | mild_accumulation | -0.33 | 0.14 | 1 | 1 | 6.05 | 4.24 | -12.31 | 18 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 5.15 | -5.12 | 4.62 | 80.85 | 56.2 | 72.3 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.2 | 0.71 | 2 | 2 | 1.98 | 3.35 | -17.07 |  | fail_already_priced_in |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 143.33455025414924 | 69.46103918462916 | 6.26 | 6.5 | -13.0 | 8.94 | 19.35 | 19.35 | False |  | mild_accumulation | 0.59 | 1.31 | 1 | 3 | 4.09 | 3.92 | -20.44 | 21 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 2.75 | 16.44 | 3.15 | 46.78 | 60.24 | 60.24 | True | 距60日低點反彈>50% | mild_accumulation | 0.33 | -0.32 | 2 | 1 | 5.45 | 6.45 | -2.06 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | 1.79 | -8.26 | -18.89 | 50.07 | 21.38 | 46.84 | False |  | distribution_warning | -1.08 | -0.92 | 0 | 1 | -3.06 | -2.79 | -25.73 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 4.48 | 12.33 | -5.36 | -3.95 | 29.56 | 29.56 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 3.76 | 4.65 | -10.58 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 17.87 | 71.69 | 95.83 | 232.74 | 114.12 | 229.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.75 | -2.07 | 0 | 0 | 29.86 | 27.85 | -6.47 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | 1.57 | -8.76 | -13.17 | 55.29 | 20.52 | 50.23 | False |  | distribution_warning | -0.14 | -0.09 | 1 | 0 | -5.43 | -3.21 | -15.22 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | -0.49 | 21.2 | 5.36 | 64.49 | 85.5 | 85.5 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.57 | 1 | 1 | 0.15 | 1.49 | -16.99 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -10.01 | 0.84 | 41.48 | 221.07 | 71.27 | 225.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.0 | 0.0 | 2 | 1 | 4.99 | 4.78 | -17.42 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | 3.04 | 6.27 | 21.9 | 51.01 | 34.17 | 47.43 | False |  | strong_accumulation | 2.28 | 2.23 | 2 | 2 | 0.84 | 1.14 | -9.47 | 25 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 1.08 | 0.0 | 2.94 | 6.06 | 5.66 | 17.65 | False |  | mild_accumulation | 0.02 | 0.01 | 2 | 1 | 0.39 | 0.64 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 7.71 | 18.0 | 2.03 | 18.74 | 21.61 | 24.22 | False |  | distribution_warning | -1.24 | -0.21 | 0 | 2 | 11.47 | 9.36 | -4.8 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 4.5 | 0.0 | -16.8 | -7.65 | 7.09 | 7.09 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 3.91 | 2.04 | -19.25 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 18.98 | 41.94 | 72.29 | 221.99 | 139.84 | 222.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.15 | 1 | 2 | 23.55 | 24.9 | -1.81 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | 7.07 | 7.5 | 2.83 | 111.24 | 65.15 | 106.83 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.72 | -5.07 | 1 | 0 | -2.19 | 1.44 | -16.54 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | -0.52 | 12.32 | 70.04 | 53.99 | 93.65 | 106.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.94 | 1.54 | 0 | 2 | 2.43 | 6.62 | -5.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 273.61017160561573 | 13.583391933925409 | 2.09 | -1.87 | -5.3 | 35.49 | 39.35 | 39.35 | False |  | distribution_warning | -1.44 | -1.22 | 1 | 1 | -4.87 | -2.09 | -25.13 | 13 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 17.65 | 12.2 | 23.99 | 20.1 | 36.5 | 36.5 | False |  | distribution_warning | -0.14 | -0.43 | 1 | 1 | 10.76 | 10.19 | -9.98 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 6.54 | 2.7 | 7.04 | 27.95 | 17.28 | 27.37 | False |  | mild_accumulation | -0.01 | 0.11 | 2 | 2 | 7.75 | 5.06 | -12.64 | 18 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | 1.4 | -13.36 | -4.43 | 6.54 | 2.84 | 4.31 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 1 | -8.13 | -6.5 | -16.7 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 2.89 | -3.2 | -8.11 | -11.77 | 16.47 | 16.47 | False |  | distribution_warning | -0.56 | -2.63 | 1 | 1 | 0.53 | 0.97 | -16.92 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 83.96056599949932 | 46.4979804114173 | -1.66 | 9.72 | -29.67 | -34.71 | 32.4 | 32.4 | False |  | distribution_warning | -0.86 | -0.99 | 1 | 1 | -2.41 | -1.79 | -36.46 | 14 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -1.21 | 10.4 | 28.76 | 9.98 | 31.72 | 44.7 | False |  | strong_accumulation | 0.49 | 0.49 | 3 | 3 | 1.79 | 2.15 | -5.6 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -5.07 | 2.66 | 11.02 | -24.45 | 11.97 | 11.97 | False |  | distribution_warning | -0.31 | -0.31 | 0 | 0 | 0.91 | 1.01 | -8.39 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 4.77 | 0.61 | 11.32 | 18.95 | 10.76 | 17.26 | False |  | distribution_warning | -0.87 | -0.41 | 0 | 0 | 2.08 | 0.86 | -17.62 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | 2.41 | 17.93 | 16.46 | 72.32 | 44.14 | 65.02 | True | 近120日漲幅>70% | mild_accumulation | 0.58 | 1.75 | 1 | 2 | 1.69 | 2.11 | -9.5 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | 0.22 | -5.08 | -8.2 |  | 1.82 |  | False |  | mild_accumulation | 0.09 | 0.02 | 3 | 1 | -2.6 | -3.86 | -23.81 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | 7.35 | 9.23 | 16.8 | 17.74 | 24.43 | 24.43 | False |  | distribution_warning | -0.2 | -0.45 | 1 | 0 | 4.46 | 5.29 | -1.13 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 10.54 | 11.33 | -18.34 | 116.43 | 15.27 | 117.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | 0.0 | 3 | 0 | 7.68 | 3.1 | -30.68 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | 11.82 | 6.49 | 9.72 | 93.37 | 20.14 | 89.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.56 | 2.31 | 3 | 1 | 6.32 | 5.81 | -12.13 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 7.04 | 1.76 | -11.35 | -9.12 | 9.89 | 9.89 | False |  | distribution_warning | -0.14 | -0.75 | 1 | 0 | 3.9 | 3.5 | -24.35 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 107.5919947488982 | 53.29791219386038 | 6.06 | 10.0 | -6.1 | 17.92 | 42.59 | 42.59 | False |  | distribution_warning | -0.7 | -0.14 | 1 | 1 | 1.59 | 3.33 | -10.26 | 14 | selected |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | 1.1 | -0.54 | 4.34 | 30.12 | 41.43 | 41.43 | False |  | mild_accumulation | 0.93 | -0.98 | 1 | 2 | 0.4 | 1.4 | -5.15 | 24 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 4.19 | 20.0 | 5.78 | -2.25 | 65.71 | 65.71 | True | 距60日低點反彈>50% | distribution_warning | -4.15 | -1.63 | 1 | 0 | 0.77 | 3.56 | -8.18 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | 1.5 | 0.33 | -26.09 | -3.33 | 21.56 | 21.56 | False |  | distribution_warning | -1.38 | -1.22 | 1 | 1 | -2.12 | -2.24 | -48.17 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 4.11 | 0.0 | 8.26 | 35.71 | 10.14 | 36.69 | False |  | mild_accumulation | 0.21 | -0.58 | 2 | 0 | 1.59 | 1.49 | -5.0 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | 2.97 | 0.67 | 4.17 | -8.35 | 5.88 | 10.02 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | 1.99 | 1.83 | -5.86 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 2.9 | 1.79 | 2.16 | -1.05 | 5.58 | 5.58 | False |  | strong_accumulation | 0.11 | 0.34 | 2 | 3 | 1.85 | 1.71 | -1.05 |  | fail_low_response_condition |