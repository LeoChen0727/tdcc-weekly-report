# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-24 19:39:40 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 731490 |
| tdcc_rows | 1963 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 374 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 652 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 81 |
| already_priced_in_excluded | 27 |
| overheat_pass | 54 |
| score_pass | 54 |
| theme_priority_pass | 42 |
| final_rows | 42 |

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
| fail_low_response_condition | 279 |
| fail_already_priced_in | 27 |
| fail_defensive_or_traditional_excluded | 11 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | -2.34 | 2.1 | 5.8 | 15.87 | 35.19 | 46.29 | False |  | mild_accumulation | 0.28 | 0.78 | 1 | 2 | -0.61 | 2.53 | -11.52 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 93.04522686147229 | 122.05590293593936 | -1.88 | -11.06 | 0.48 | -13.99 | 11.29 | 11.29 | False |  | mild_accumulation | -0.81 | 0.13 | 1 | 2 | -2.88 | -2.26 | -16.4 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 1.17 | -0.76 | -1.7 | -19.6 | 4.41 | 4.41 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.26 | 0.22 | -16.1 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 0.5 | -2.88 | -6.05 | 14.64 | 6.43 | 16.49 | False |  | mild_accumulation | 0.11 | -0.33 | 1 | 0 | -0.52 | -0.61 | -15.13 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 3.98 | 1.95 | 3.1 | -2.4 | 6.09 | 7.96 | False |  | strong_accumulation | 0.07 | 0.02 | 2 | 2 | 3.48 | 2.95 | -9.18 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -1.29 | -1.85 | -5.34 | -13.84 | 1.32 | 1.32 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -1.94 | -1.94 | -12.09 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 0.47 | -3.8 | -6.11 | -25.09 | 5.13 | 12.57 | False |  | strong_accumulation | 0.14 | 0.15 | 3 | 3 | -2.11 | -1.89 | -12.07 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 1.22 | 0.0 | -11.39 | -20.95 | 5.96 | 5.96 | False |  | strong_accumulation | 0.39 | 0.11 | 2 | 2 | 1.26 | 0.86 | -19.68 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 5.76 | 5.76 | 5.0 | 1.03 | 11.36 | 21.49 | False |  | distribution_warning | -0.18 | -0.2 | 2 | 2 | 4.18 | 4.23 | -4.85 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 1.28 | 27.38 | 87.5 | 136.41 | 92.9 | 143.7 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.14 | 2.68 | 3 | 3 | 14.93 | 14.11 | -13.86 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 10.0 | 19.2 | 26.37 | 107.36 | 87.2 | 116.29 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.09 | 7.42 | 2 | 2 | 18.46 | 18.03 | -7.6 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | -2.5 | -9.54 | -7.14 | -18.56 | 2.93 | 2.93 | False |  | distribution_warning | -0.81 | -1.37 | 1 | 1 | -2.53 | -2.87 | -19.12 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 33032.925531914894 | 13849.620888036585 | -6.59 | -11.27 | 6.51 | 3.24 | 7.59 | 13.73 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | -7.18 | -6.36 | -15.61 | 13 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 102.5304395876603 | 136.2137376977922 | 6.07 | -0.76 | -0.76 | 14.91 | 16.96 | 22.43 | False |  | mild_accumulation | -0.55 | 0.01 | 1 | 1 | 4.42 | 4.47 | -5.07 | 20 | selected |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 29.36 | 32.17 | 66.12 | 90.6 | 83.13 | 99.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.4 | -0.41 | 3 | 1 | 26.19 | 25.72 | 0.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | 0.45 | -13.88 | 61.33 | 268.11 | 80.56 | 273.68 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.87 | -0.02 | 0 | 1 | -4.29 | -1.62 | -18.13 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | -1.55 | -15.05 | -14.19 | -33.16 | 0.79 | 0.79 | False |  | mild_accumulation | -0.56 | 0.09 | 0 | 2 | -4.01 | -5.19 | -23.95 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 84.20319969775788 | 156.5212859256626 | -1.65 | -9.27 | -4.33 | -16.39 | 0.34 | 1.19 | False |  | distribution_warning | -0.93 | -0.97 | 0 | 0 | -2.67 | -3.41 | -17.66 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 2.34 | 17.7 | -19.03 | 123.61 | 28.55 | 140.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | -1.49 | 0 | 1 | 5.61 | 5.17 | -25.96 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 0.33 | -1.93 | 10.31 | 25.77 | 9.32 | 19.14 | False |  | mild_accumulation | 0.44 | 0.01 | 1 | 1 | 0.07 | 0.14 | -13.84 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | -1.29 | -3.48 | -7.99 | 9.91 | 3.92 | 18.22 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -1.36 | -1.51 | -8.96 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 4.19 | 4.66 | -8.63 | 155.83 | 40.18 | 168.51 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.68 | 0.66 | 1 | 1 | 6.5 | 5.89 | -20.74 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 15.84 | 113.58 | 65.53 | 247.51 | 144.75 | 316.56 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 3.2 | 2 | 2 | 46.53 | 38.46 | -4.12 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 61.18890785808584 | 40.59833569613409 | 3.22 | 0.0 | -26.38 | 36.02 | 26.38 | 47.25 | False |  | mild_accumulation | 0.32 | -0.71 | 2 | 1 | 1.17 | 1.1 | -29.14 |  | fail_low_response_condition |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 0.0 | -0.6 | 1.01 | 24.94 | 10.6 | 26.2 | False |  | mild_accumulation | 0.07 | 0.06 | 1 | 1 | -0.31 | -0.22 | -8.74 | 19 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 9.64 | 4.5 | -49.12 | 103.51 | 27.05 | 100.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -0.78 | 1 | 1 | 4.15 | 2.73 | -48.44 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 53.32005371471296 | 39.26370665798065 | 2.06 | 2.7 | -1.2 | 23.75 | 13.53 | 25.32 | False |  | distribution_warning | -0.03 | -0.05 | 1 | 1 | 1.75 | 1.77 | -1.39 | 15 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 218.53271706735816 | 149.1423915250992 | 0.43 | -8.24 | -18.47 | -19.86 | 27.45 | 27.45 | False |  | distribution_warning | -1.14 | -1.2 | 1 | 1 | -3.15 | -3.18 | -23.03 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 0.88 | -7.8 | -9.74 | 83.42 | 46.58 | 104.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.1 | -3.77 | 1 | 1 | -1.75 | -0.99 | -14.25 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | 5.28 | -9.33 | -28.76 | 3.27 | 5.87 | 6.16 | False |  | distribution_warning | -0.62 | -0.71 | 1 | 0 | -3.72 | -3.67 | -32.92 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 5.59 | 8.87 | 0.96 | 19.17 | 17.68 | 19.47 | False |  | distribution_warning | -0.05 | -0.42 | 1 | 0 | 6.08 | 5.22 | -3.87 | 19 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -2.57 | 0.42 | 0.98 | -6.25 | 7.78 | 7.78 | False |  | mild_accumulation | 1.06 | -0.22 | 3 | 0 | 0.48 | 0.11 | -12.52 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -7.77 | -8.54 | 6.81 | 78.46 | 77.02 | 86.02 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.96 | 3.36 | 3 | 3 | -6.64 | -3.05 | -14.59 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 0.53 | -1.55 | 45.05 | 64.88 | 48.44 | 68.67 | True | 近60日漲幅>40% | mild_accumulation | -0.02 | 0.53 | 2 | 2 | -1.54 | 0.78 | -7.48 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 156.29654201767283 | 108.41049971158722 | 10.07 | 15.33 | 1.1 | 28.57 | 32.66 | 32.66 | False |  | distribution_warning | -0.74 | -0.06 | 1 | 2 | 5.98 | 4.71 | -9.65 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 10.96 | 15.78 | -20.14 | 24.36 | 32.51 | 32.51 | False |  | mild_accumulation | 0.38 | 0.11 | 1 | 1 | 10.31 | 8.23 | -19.48 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | 16.32 | 7.28 | -9.43 | 1.38 | 56.74 | 56.74 | True | 距60日低點反彈>50% | distribution_warning | -0.82 | -0.53 | 1 | 1 | 2.82 | 5.35 | -17.23 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 1.83 | 4.78 | 7.11 | 37.71 | 15.87 | 39.58 | False |  | strong_accumulation | 0.89 | 1.38 | 3 | 2 | 1.55 | 1.65 | -10.07 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -1.6 | 1.5 | -9.01 | 5.29 | 21.33 | 21.33 | False |  | strong_accumulation | 0.37 | 0.36 | 3 | 3 | -0.14 | 0.38 | -13.87 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 129.84671742960728 | 95.18081273476336 | 7.56 | -8.18 | -8.76 | 47.66 | 28.5 | 52.11 | False |  | distribution_warning | -0.63 | -0.7 | 1 | 1 | -3.51 | -2.9 | -21.95 | 16 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | 0.57 | -3.31 | -1.41 | 31.03 | 11.98 | 30.06 | False |  | strong_accumulation | 0.15 | 0.61 | 2 | 2 | -4.68 | -3.67 | -17.24 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 5.25 | 6.96 | 43.54 | 108.67 | 46.45 | 112.67 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.36 | -0.63 | 1 | 0 | 5.29 | 5.86 | -0.82 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 24.76 | 19.53 | -1.15 | 38.77 | 31.79 | 44.38 | False |  | mild_accumulation | 0.1 | -0.56 | 2 | 1 | 18.57 | 15.9 | -7.89 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 14.66 | 6.27 | -24.13 | -6.15 | 17.99 | 17.99 | False |  | distribution_warning | -0.36 | -0.54 | 1 | 1 | 9.7 | 6.91 | -30.84 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 3.07 | -7.02 | 19.48 | 133.95 | 56.21 | 152.76 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.57 | -3.29 | 1 | 1 | -0.85 | 0.4 | -11.6 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.57 | 1.54 | -10.49 | 18.34 | 3.12 | 19.14 | False |  | strong_accumulation | 0.26 | 0.17 | 3 | 3 | 0.69 | -0.06 | -21.86 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | 2.69 | 12.57 | 3.24 | -20.08 | 30.23 | 30.23 | False |  | distribution_warning | -0.2 | -0.67 | 1 | 1 | 4.81 | 4.81 | -6.53 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 0.96 | -2.64 | -15.15 | 37.87 | 4.82 | 30.11 | False |  | strong_accumulation | 0.68 | 1.24 | 2 | 3 | -0.45 | -2.18 | -30.15 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 0.2 | 0.79 | -16.12 | 50.89 | 30.1 | 52.69 | False |  | distribution_warning | -0.49 | -0.05 | 2 | 0 | 0.21 | 0.37 | -29.85 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | -0.73 | -2.68 | -3.88 | -2.68 | 1.3 | 8.13 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.58 | -0.78 | -7.16 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 8.67 | 27.1 | 36.54 | 122.53 | 36.12 | 127.18 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 3.81 | 6.23 | -28.19 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | 1.56 | 7.73 | -10.96 | -6.25 | 21.88 | 21.88 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.7 | -0.49 | -15.22 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | 2.71 | -4.53 | 13.57 | 18.3 | 31.71 | 31.71 | False |  | distribution_warning | -1.2 | -1.15 | 0 | 1 | -0.21 | -0.06 | -13.66 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 3.75 | 27.94 | 54.53 | 85.28 | 117.25 | 117.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.84 | 3.37 | 2 | 1 | 5.42 | 8.91 | -6.1 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 3.78 | 2.72 | -16.23 | -2.58 | 11.85 | 11.85 | False |  | strong_accumulation | 0.36 | 0.12 | 3 | 3 | 2.83 | 1.67 | -26.07 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 8.91 | -7.35 | 2.89 | 183.74 | 65.68 | 186.66 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.62 | -8.2 | 0 | 0 | 1.53 | 3.22 | -12.72 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 383.2629286702524 | 200.70869091113056 | -0.34 | -6.81 | 24.51 | 48.66 | 31.9 | 52.23 | False |  | distribution_warning | -0.68 | -0.45 | 1 | 2 | -5.07 | -2.7 | -17.3 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | 1.93 | -9.57 | -18.11 | -2.4 | 23.02 | 23.02 | False |  | distribution_warning | -0.34 | -0.83 | 1 | 1 | -6.5 | -3.57 | -21.28 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 4.8 | -4.59 | -48.59 | 47.64 | 10.08 | 36.56 | False |  | distribution_warning | -1.04 | -0.07 | 1 | 1 | 0.8 | -0.78 | -51.82 | 12 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.41 | 0.72 | -10.2 | -2.2 | 3.72 | 3.72 | False |  | strong_accumulation | 0.26 | 0.26 | 3 | 3 | 0.62 | 0.19 | -10.53 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 106.21354266385858 | 53.00526357886879 | 4.13 | 1.69 | -21.59 | 5.97 | 24.96 | 24.96 | False |  | strong_accumulation | 0.29 | 1.52 | 2 | 2 | 3.62 | 2.73 | -29.77 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -1.4 | -7.86 | -12.08 | -10.21 | 1.2 | 1.2 | False |  | distribution_warning | -0.52 | -0.45 | 1 | 1 | -3.95 | -3.81 | -15.26 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | 0.0 | -6.51 | 8.71 | 0.35 | 11.67 | 18.6 | False |  | distribution_warning | -0.2 | 0.0 | 0 | 0 | -2.63 | -1.27 | -8.6 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | 0.0 | 0.0 | 2.44 | 2.44 | 3.33 | 11.27 | False |  | strong_accumulation | 0.17 | 0.14 | 3 | 2 | -0.05 | -0.0 | -3.89 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | -1.51 | 2.08 | -9.09 | 1.24 | 15.43 | 15.43 | False |  | strong_accumulation | 0.16 | 0.04 | 3 | 2 | 0.84 | 0.16 | -20.71 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | -2.18 | -1.17 | -0.39 | -34.11 | 7.62 | 7.62 | False |  | mild_accumulation | -0.01 | 0.14 | 2 | 2 | -1.04 | -0.99 | -8.62 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | -0.51 | -2.77 | -12.71 | -7.79 | 2.29 | 2.29 | False |  | distribution_warning | -0.45 | -0.29 | 0 | 0 | -1.04 | -1.56 | -16.78 | 12 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | -0.43 | -2.82 | -8.63 | -26.9 | 1.86 | 1.86 | False |  | mild_accumulation | -0.47 | 0.05 | 1 | 1 | -0.65 | -1.11 | -10.38 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | -1.75 | 6.1 | 26.3 | -7.83 | 26.74 | 27.4 | False |  | strong_accumulation | 1.57 | 1.26 | 3 | 2 | 1.03 | 1.53 | -6.89 | 18 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround | B_可觀察 | 85.48459503786516 | 17.912643295520123 | 1.41 | 3.45 | 3.01 | 5.58 | 15.59 | 15.59 | False |  | strong_accumulation | 1.43 | 1.44 | 3 | 3 | 2.7 | 2.46 | -8.87 | 18 | selected |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | 10.1 | 20.92 | 14.91 | 82.62 | 45.59 | 87.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.08 | 1.23 | 3 | 3 | 10.05 | 10.18 | -3.18 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -1.62 | -10.66 | -10.5 | 22.11 | 8.0 | 24.3 | False |  | distribution_warning | -0.04 | -0.02 | 1 | 0 | -4.31 | -5.7 | -44.96 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 3.09 | -12.77 | -8.8 | 20.56 | 13.61 | 19.72 | False |  | distribution_warning | -0.71 | -1.56 | 1 | 0 | -1.93 | -0.94 | -18.78 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 0.0 | -3.7 | -14.91 | 0.86 | 2.63 | 5.88 | False |  | distribution_warning | -0.88 | -1.69 | 0 | 0 | -1.58 | -2.16 | -28.22 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | -1.26 | 0.36 | 29.11 | 76.28 | 70.81 | 87.07 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.19 | -3.17 | 1 | 1 | -3.16 | -0.81 | -13.79 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 38.53 | 60.16 | 31.15 | 187.77 | 120.08 | 187.25 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.99 | 1 | 1 | 41.85 | 37.02 | 0.0 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 11.62 | 6.44 | 35.69 | 56.95 | 76.43 | 76.43 | True | 距60日低點反彈>50% | mild_accumulation | -0.77 | 0.44 | 1 | 2 | 5.59 | 8.19 | -1.25 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 3.0 | 0.0 | 1.69 | 5.26 | 9.59 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.32 | -0.26 | -36.51 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 84.97614765538744 | 32.40539437293427 | 4.72 | 1.75 | 12.3 | 39.79 | 20.6 | 41.7 | False |  | mild_accumulation | -0.61 | 0.45 | 1 | 2 | 4.42 | 3.28 | -20.09 | 20 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 2.29 | -4.58 | -22.65 | 5.22 | 10.62 | 10.62 | False |  | distribution_warning | -0.54 | -0.14 | 1 | 1 | -0.38 | -1.1 | -25.42 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 0.0 | -7.52 | -16.06 | 24.59 | 3.85 | 26.28 | False |  | distribution_warning | -2.0 | -2.72 | 0 | 1 | -1.93 | -2.74 | -29.63 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 1.47 | 7.25 | -1.9 | -8.2 | 15.0 | 15.0 | False |  | mild_accumulation | -0.33 | 0.14 | 1 | 1 | 5.49 | 3.54 | -12.1 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 26.06 | 0.42 | 13.94 | 85.74 | 81.47 | 100.17 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.2 | 0.71 | 2 | 2 | 18.3 | 15.5 | -3.66 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | 3.34 | 1.98 | -17.14 | 8.41 | 16.58 | 16.58 | False |  | mild_accumulation | 0.59 | 1.31 | 1 | 3 | 1.12 | 0.88 | -22.28 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 7.17 | 11.85 | 6.32 | 43.47 | 64.53 | 64.53 | True | 距60日低點反彈>50% | mild_accumulation | 0.33 | -0.32 | 2 | 1 | 6.19 | 6.92 | -1.65 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 50.31333751338634 | 36.26105158634005 | 2.98 | -7.65 | -21.0 | 36.94 | 23.28 | 42.58 | False |  | distribution_warning | -1.08 | -0.92 | 0 | 1 | -0.11 | -0.58 | -22.31 | 11 | selected |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 2.28 | 7.55 | -3.63 | -22.34 | 29.78 | 29.78 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 2.56 | 3.65 | -10.43 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 23.6 | 59.84 | 56.08 | 235.58 | 126.65 | 231.11 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.75 | -2.07 | 0 | 0 | 26.85 | 24.49 | -11.95 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -3.1 | -14.25 | -6.29 | 35.5 | 16.79 | 38.5 | False |  | distribution_warning | -0.14 | -0.09 | 1 | 0 | -6.37 | -5.1 | -17.85 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 16.16 | 27.9 | 12.71 | 49.92 | 118.41 | 118.41 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.57 | 1 | 1 | 13.88 | 15.84 | -2.27 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -3.75 | 2.36 | 36.56 | 173.79 | 60.46 | 149.01 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.0 | 0.0 | 2 | 1 | -1.68 | -1.66 | -22.63 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | -1.07 | 2.79 | 15.67 | 36.67 | 32.73 | 40.3 | False |  | strong_accumulation | 2.28 | 2.23 | 2 | 2 | -0.38 | 0.38 | -10.44 | 24 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 0.72 | -0.71 | 2.94 | 2.19 | 5.66 | 17.65 | False |  | mild_accumulation | 0.02 | 0.01 | 2 | 1 | 0.52 | 0.55 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 2.84 | 16.9 | 0.0 | 19.28 | 22.74 | 25.37 | False |  | distribution_warning | -1.24 | -0.21 | 0 | 2 | 10.21 | 8.4 | -3.91 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 3.18 | 0.69 | -19.78 | -10.15 | 3.55 | 3.55 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.22 | -1.25 | -21.93 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 31.15 | 44.0 | 68.98 | 219.89 | 168.5 | 231.07 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.15 | 1 | 2 | 30.22 | 28.51 | -0.23 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -2.29 | -11.25 | 0.2 | 67.37 | 55.45 | 75.09 | True | 距60日低點反彈>50% | distribution_warning | -2.72 | -5.07 | 1 | 0 | -6.88 | -3.78 | -21.44 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 29.23 | 22.59 | 103.53 | 67.76 | 131.44 | 147.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.94 | 1.54 | 0 | 2 | 19.68 | 22.31 | 0.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | 14.42 | -2.58 | -15.28 | 24.63 | 43.35 | 43.35 | False |  | distribution_warning | -1.44 | -1.22 | 1 | 1 | -1.57 | 0.68 | -22.98 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 16.42 | 13.87 | 16.42 | 9.86 | 38.87 | 38.87 | False |  | distribution_warning | -0.14 | -0.43 | 1 | 1 | 10.59 | 9.41 | -8.41 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 5.86 | 15.76 | 6.82 | 28.42 | 20.88 | 28.0 | False |  | mild_accumulation | -0.01 | 0.11 | 2 | 2 | 9.76 | 6.82 | -9.96 | 20 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | -2.48 | -14.11 | -14.02 | -5.42 | 1.16 | 1.16 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 1 | -7.61 | -6.36 | -18.06 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 3.32 | -3.2 | -5.5 | -14.05 | 16.47 | 16.47 | False |  | distribution_warning | -0.56 | -2.63 | 1 | 1 | 1.11 | 0.99 | -16.92 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 83.96056599949932 | 46.4979804114173 | 3.8 | 5.58 | -28.49 | -34.05 | 37.43 | 37.43 | False |  | distribution_warning | -0.86 | -0.99 | 1 | 1 | -0.22 | 1.01 | -31.28 | 15 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -4.22 | 6.38 | 28.86 | 12.28 | 30.34 | 43.18 | False |  | strong_accumulation | 0.49 | 0.49 | 3 | 3 | -0.47 | 0.73 | -6.59 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -0.31 | -3.86 | 7.11 | -20.59 | 10.77 | 10.77 | False |  | distribution_warning | -0.31 | -0.31 | 0 | 0 | 0.02 | 0.0 | -9.37 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 14.84 | 11.39 | 19.84 | 11.06 | 22.81 | 26.79 | False |  | distribution_warning | -0.87 | -0.41 | 0 | 0 | 14.36 | 12.17 | -7.13 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | -2.81 | 4.41 | 5.14 | 36.36 | 38.89 | 38.89 | False |  | mild_accumulation | 0.58 | 1.75 | 1 | 2 | -3.38 | -1.41 | -12.79 |  | fail_low_response_condition |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | 0.67 | -4.47 | -11.26 |  | 2.05 |  | False |  | mild_accumulation | 0.09 | 0.02 | 3 | 1 | -1.84 | -2.87 | -23.64 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -0.47 | 0.24 | 8.44 | 11.58 | 20.45 | 20.45 | False |  | distribution_warning | -0.2 | -0.45 | 1 | 0 | 0.57 | 1.12 | -4.29 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | -2.01 | 5.97 | -21.97 | 105.61 | 9.12 | 102.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | 0.0 | 3 | 0 | 0.94 | -2.04 | -34.38 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | -0.49 | -0.97 | -8.89 | 81.1 | 17.28 | 83.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.56 | 2.31 | 3 | 1 | 3.63 | 2.29 | -14.23 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 2.91 | -2.41 | -20.06 | -10.73 | 7.6 | 7.6 | False |  | distribution_warning | -0.14 | -0.75 | 1 | 0 | 1.85 | 0.75 | -24.33 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | 1.36 | -2.1 | -1.97 | -11.92 | 38.15 | 38.15 | False |  | distribution_warning | -0.7 | -0.14 | 1 | 1 | -1.8 | 0.09 | -13.05 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | 0.55 | -1.09 | 8.78 | 24.15 | 39.39 | 39.39 | False |  | mild_accumulation | 0.93 | -0.98 | 1 | 2 | -0.98 | -0.02 | -6.52 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | -2.6 | -1.75 | 7.32 | -10.85 | 60.48 | 60.48 | True | 距60日低點反彈>50% | distribution_warning | -4.15 | -1.63 | 1 | 0 | -2.66 | 0.23 | -11.08 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -0.83 | -10.41 | -35.29 | -26.39 | 18.56 | 18.56 | False |  | distribution_warning | -1.38 | -1.22 | 1 | 1 | -3.44 | -3.82 | -49.45 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | -0.53 | -1.57 | 5.04 | 32.04 | 6.23 | 29.31 | False |  | mild_accumulation | 0.21 | -0.58 | 2 | 0 | 0.33 | -0.0 | -6.25 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | 0.46 | -0.68 | 1.85 | -13.04 | 3.53 | 7.58 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | -0.35 | -0.57 | -7.95 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 0.0 | 0.0 | -0.71 | -3.81 | 3.35 | 3.35 | False |  | strong_accumulation | 0.11 | 0.34 | 2 | 3 | -0.38 | -0.52 | -3.14 |  | fail_low_response_condition |