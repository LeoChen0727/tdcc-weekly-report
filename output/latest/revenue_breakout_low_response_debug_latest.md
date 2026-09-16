# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-16 19:38:50 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 719730 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 367 |
| tdcc_mild_accumulation_count | 755 |
| tdcc_distribution_warning_count | 643 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 109 |
| already_priced_in_excluded | 52 |
| overheat_pass | 57 |
| score_pass | 57 |
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
| fail_low_response_condition | 251 |
| fail_already_priced_in | 52 |
| fail_defensive_or_traditional_excluded | 12 |
| fail_non_mainstream_score_lt_11 | 3 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround |  | 89.22674829328686 | 20.162313431356427 | 1.02 | 25.96 | 7.25 | 10.86 | 37.04 | 48.3 | True | 近20日漲幅>25% | strong_accumulation | 1.06 | 1.17 | 2 | 3 | 5.58 | 6.17 | -10.3 |  | fail_already_priced_in |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | -0.77 | 0.19 | -5.67 | -22.05 | 3.41 | 3.41 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | -0.77 | -0.55 | -16.91 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | -1.58 | -2.06 | -14.62 | 20.22 | 5.27 | 20.07 | False |  | distribution_warning | -0.3 | 0.0 | 1 | 0 | -2.35 | -2.2 | -16.05 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 1.99 | 0.85 | -0.56 | -3.5 | 3.77 | 5.6 | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | 1.14 | 0.88 | -11.17 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -0.98 | -0.7 | -11.1 | -12.2 | 3.37 | 3.37 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 1 | -0.25 | -0.53 | -11.21 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | -1.85 | -5.35 | -0.23 | -24.11 | 3.91 | 11.26 | False |  | mild_accumulation | -0.26 | 0.13 | 2 | 3 | -4.04 | -3.5 | -13.09 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | -2.03 | 0.0 | -19.67 | 8.56 | 2.55 | 7.11 | False |  | strong_accumulation | 0.08 | 0.16 | 2 | 2 | -2.15 | -2.19 | -22.26 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | -1.07 | 2.96 | -7.33 | 2.21 | 5.3 | 14.88 | False |  | distribution_warning | -0.34 | -0.36 | 1 | 1 | -0.54 | -0.77 | -10.03 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 9.69 | 19.97 | 84.63 | 119.38 | 87.29 | 119.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 0.74 | 2 | 2 | 12.02 | 14.7 | 0.0 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 4.94 | 3.13 | -0.93 | 97.11 | 54.94 | 104.71 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.75 | 0.76 | 2 | 2 | 3.22 | 6.21 | -9.81 |  | fail_already_priced_in |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | -0.56 | -4.56 | -6.56 | -14.01 | 4.4 | 4.4 | False |  | distribution_warning | -0.82 | -1.08 | 1 | 2 | -3.9 | -2.59 | -17.97 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 33032.925531914894 | 13849.620888036585 | -4.13 | 1.05 | 12.17 | 10.33 | 13.68 | 19.96 | False |  | mild_accumulation | 0.19 | 0.45 | 1 | 2 | -3.54 | -1.48 | -10.98 | 19 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | -4.38 | -4.38 | -13.04 | 6.19 | 7.14 | 12.15 | False |  | mild_accumulation | 0.73 | 0.0 | 2 | 0 | -5.31 | -3.93 | -16.08 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 57.69192058134775 | 20.405940800672543 | -4.22 | 5.58 | 12.66 | 44.13 | 36.75 | 48.85 | False |  | strong_accumulation | 1.79 | 2.01 | 3 | 2 | -1.42 | 1.26 | -6.2 | 18 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -2.86 | -14.54 | 61.14 | 279.37 | 76.1 | 279.97 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.17 | -1.49 | 1 | 0 | -10.08 | -4.34 | -20.15 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | -4.89 | -15.38 | -27.92 | -31.44 | 0.4 | 0.4 | False |  | distribution_warning | -0.49 | -0.03 | 0 | 1 | -8.98 | -8.23 | -27.92 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | -3.24 | -7.59 | -4.78 | -15.2 | 0.0 | 1.19 | False |  | distribution_warning | -0.6 | -0.75 | 1 | 1 | -5.34 | -4.93 | -17.66 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | -4.2 | 19.63 | 2.79 | 119.5 | 22.54 | 157.95 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.3 | -0.83 | 1 | 1 | 7.59 | 5.35 | -29.42 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | -0.17 | -4.29 | 8.86 | 24.9 | 11.28 | 25.16 | False |  | distribution_warning | -0.62 | 0.0 | 0 | 0 | -2.6 | -0.84 | -14.97 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | -5.19 | -2.9 | -11.32 | 13.35 | 2.73 | 16.86 | False |  | mild_accumulation | -0.02 | 0.01 | 1 | 1 | -3.08 | -2.66 | -13.86 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 5.24 | -1.12 | -3.18 | 156.98 | 34.55 | 157.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.17 | 0.0 | 1 | 0 | 3.34 | 3.8 | -23.92 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 41.14 | 84.33 | 33.15 | 211.67 | 92.22 | 227.15 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.67 | 2.0 | 2 | 2 | 47.88 | 39.77 | 0.0 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | -1.55 | 1.93 | -27.13 | 62.9 | 24.8 | 71.17 | False |  | mild_accumulation | 0.18 | -0.66 | 2 | 1 | -0.06 | -0.37 | -33.4 | 17 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | -1.59 | 1.22 | -4.43 | 32.27 | 9.49 | 30.87 | False |  | mild_accumulation | -0.01 | 0.04 | 1 | 1 | -0.64 | -0.99 | -9.65 | 19 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | -5.13 | -6.94 | -47.45 | 120.12 | 17.42 | 118.78 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.98 | -0.65 | 1 | 1 | -3.26 | -5.32 | -56.07 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | -3.45 | 1.28 | -4.42 | 35.23 | 9.17 | 31.86 | False |  | strong_accumulation | 0.1 | 0.11 | 2 | 2 | -1.32 | -1.09 | -4.99 | 20 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | -5.93 | 0.0 | -30.81 | 3.03 | 29.63 | 29.63 | False |  | mild_accumulation | -0.05 | 0.28 | 2 | 2 | -2.78 | -2.8 | -33.7 | 22 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | -7.65 | 0.6 | -20.09 | 87.36 | 44.44 | 101.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | -0.7 | 2 | 2 | -4.34 | -2.54 | -24.89 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 59.42279854814421 | 61.86168160125982 | -8.68 | -13.41 | -24.44 | 21.85 | 0.55 | 16.83 | False |  | distribution_warning | -0.64 | -0.49 | 1 | 0 | -9.26 | -9.52 | -34.87 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 0.11 | 2.78 | -1.66 | 17.02 | 10.46 | 16.25 | False |  | distribution_warning | -0.19 | -0.45 | 0 | 0 | 1.02 | 0.26 | -9.77 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -1.4 | 0.29 | -1.54 | -7.75 | 5.09 | 5.09 | False |  | mild_accumulation | 0.56 | -0.25 | 3 | 0 | -1.35 | -1.38 | -14.7 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -0.63 | 27.57 | 19.19 | 150.0 | 90.32 | 140.08 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.4 | 6.75 | 3 | 3 | 4.25 | 6.14 | -8.17 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | -4.09 | 1.51 | 19.62 | 71.04 | 47.87 | 72.29 | True | 近120日漲幅>70% | strong_accumulation | 0.42 | 0.16 | 3 | 2 | -2.5 | -0.16 | -8.83 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | -10.49 | -1.42 | -7.73 | 42.66 | 20.81 | 38.87 | False |  | distribution_warning | -0.12 | -0.04 | 2 | 2 | 0.13 | -0.98 | -16.06 | 18 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 81.06426064737752 | 92.59516265483826 | -1.14 | 2.36 | -21.09 | 12.31 | 17.38 | 17.38 | False |  | distribution_warning | -0.75 | -0.35 | 0 | 0 | 1.44 | 0.16 | -31.67 | 14 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 76.38825024031777 | 71.24826737205954 | -9.82 | -4.62 | -21.58 | 15.35 | 40.71 | 40.71 | False |  | mild_accumulation | -0.41 | 0.01 | 1 | 2 | -6.3 | -4.86 | -25.69 | 17 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 0.14 | 0.43 | 5.9 | 57.3 | 12.18 | 57.66 | False |  | mild_accumulation | 0.2 | 0.27 | 2 | 1 | -0.23 | -0.28 | -12.94 | 20 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -0.44 | 2.87 | -8.59 | 22.26 | 22.04 | 22.04 | False |  | strong_accumulation | 0.09 | 0.01 | 2 | 2 | 1.73 | 1.96 | -13.36 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.84671742960728 | 95.18081273476336 | -5.4 | -13.52 | -10.79 | 95.58 | 29.39 | 85.25 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.1 | -0.4 | 0 | 1 | -6.99 | -5.75 | -21.41 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -8.47 | -0.97 | -10.43 | 36.59 | 13.9 | 43.46 | False |  | strong_accumulation | 0.83 | 1.11 | 2 | 3 | -4.13 | -4.32 | -15.82 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 6.43 | 0.14 | 42.56 | 118.21 | 53.42 | 119.24 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.63 | -0.1 | 0 | 1 | 2.81 | 4.09 | -4.4 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | -2.82 | -5.48 | -17.86 | 26.07 | 6.15 | 25.61 | False |  | distribution_warning | -0.04 | -0.41 | 2 | 1 | -2.08 | -2.84 | -28.62 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 86.10504037359958 | 114.852843965949 | -3.29 | -7.36 | -21.75 | -19.11 | 2.32 | 2.32 | False |  | distribution_warning | -0.68 | -1.27 | 1 | 0 | -4.18 | -5.37 | -42.44 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | -5.83 | 2.39 | 8.36 | 148.11 | 52.95 | 147.49 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -1.87 | 2 | 2 | -3.59 | -0.81 | -13.44 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | -1.33 | 0.39 | -14.87 | 22.16 | 1.56 | 22.3 | False |  | strong_accumulation | 0.3 | 0.27 | 3 | 3 | -0.37 | -1.5 | -23.04 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | 0.55 | 13.96 | -4.04 | -15.72 | 24.32 | 24.32 | False |  | distribution_warning | -0.3 | -1.04 | 1 | 0 | 4.78 | 4.22 | -10.03 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | -3.47 | -7.18 | -8.01 | 37.9 | 2.7 | 39.23 | False |  | strong_accumulation | 0.94 | 1.68 | 2 | 3 | -3.1 | -5.21 | -31.57 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 2.21 | -0.97 | -15.75 | 69.9 | 29.59 | 74.57 | False |  | distribution_warning | -2.46 | -0.99 | 1 | 0 | 0.05 | 0.53 | -30.12 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | -1.99 | -0.91 | -6.71 | 1.88 | 0.74 | 7.54 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -1.4 | -1.62 | -15.18 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 0.99 | 22.27 | 30.99 | 113.54 | 57.49 | 115.03 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 4.09 | 3.24 | -32.27 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -5.64 | 6.65 | -17.74 | -17.38 | 20.31 | 20.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.08 | -0.41 | -18.09 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | -1.74 | 0.53 | -5.99 | 33.89 | 30.79 | 30.79 | False |  | distribution_warning | -0.28 | -0.25 | 1 | 2 | -2.8 | -1.01 | -14.26 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | -3.38 | 29.89 | 29.4 | 108.92 | 101.96 | 101.96 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.41 | 4.4 | 3 | 2 | 6.46 | 7.66 | -7.21 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | -6.31 | 1.94 | -21.33 | 17.44 | 7.22 | 16.97 | False |  | strong_accumulation | 0.32 | 0.06 | 3 | 3 | -0.24 | -1.63 | -31.07 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | -7.34 | 0.83 | 6.4 | 171.51 | 55.08 | 178.54 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | -1.38 | 1 | 1 | -4.79 | -2.4 | -18.3 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 383.2629286702524 | 200.70869091113056 | -5.93 | 5.24 | 17.4 | 73.85 | 34.12 | 75.53 | True | 近120日漲幅>70% | strong_accumulation | 1.36 | 2.41 | 2 | 2 | -3.47 | -1.87 | -15.91 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | -10.67 | -5.12 | -10.52 | 28.15 | 20.7 | 33.08 | False |  | distribution_warning | -0.18 | -1.02 | 2 | 1 | -9.79 | -8.04 | -22.77 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | -2.09 | -10.04 | -42.01 | 67.06 | 6.05 | 64.45 | False |  | distribution_warning | -0.96 | -0.99 | 1 | 1 | -3.72 | -5.83 | -56.86 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.73 | 0.0 | -10.83 | 0.93 | 3.18 | 3.18 | False |  | mild_accumulation | -0.33 | 0.27 | 2 | 3 | 0.26 | -0.15 | -11.96 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 106.21354266385858 | 53.00526357886879 | 0.27 | -0.67 | -29.43 | 11.76 | 18.56 | 18.56 | False |  | strong_accumulation | 0.34 | 1.6 | 2 | 3 | -1.23 | -1.55 | -33.36 |  | fail_low_response_condition |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -2.7 | 1.77 | 7.06 | 2.86 | 12.06 | 19.01 | False |  | distribution_warning | -0.15 | 0.0 | 1 | 0 | -3.1 | -0.84 | -8.28 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | -2.24 | 1.22 | 2.72 | 3.11 | 3.23 | 10.08 | False |  | strong_accumulation | 0.16 | 0.29 | 3 | 2 | -0.92 | -0.96 | -4.93 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | -1.22 | 4.75 | -8.14 | 1.04 | 14.25 | 14.25 | False |  | strong_accumulation | 0.1 | 0.06 | 2 | 2 | 1.24 | 0.02 | -21.52 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | -1.78 | 1.57 | -7.53 | -33.04 | 9.17 | 9.17 | False |  | mild_accumulation | -0.11 | 0.39 | 1 | 3 | 0.28 | 0.41 | -7.31 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | -3.58 | -4.06 | -11.51 | -7.71 | 0.94 | 0.94 | False |  | distribution_warning | -0.14 | -0.16 | 1 | 1 | -2.97 | -3.09 | -17.88 | 12 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | -3.87 | -2.13 | -9.46 | -23.42 | 0.44 | 0.44 | False |  | mild_accumulation | 0.08 | -0.29 | 2 | 0 | -2.73 | -2.63 | -12.06 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 58.75071504262123 | 38.71801301175803 | -2.44 | -1.9 | 13.36 | -14.17 | 25.83 | 25.83 | False |  | distribution_warning | -0.98 | -1.66 | 2 | 1 | 0.4 | 2.06 | -8.04 | 12 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 1.45 | -1.54 | 0.29 | 3.24 | 12.86 | 12.86 | False |  | strong_accumulation | 1.33 | 0.5 | 2 | 3 | -0.21 | 0.89 | -11.03 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -14.75 | 3.49 | -7.42 | 34.28 | 5.33 | 37.79 | False |  | distribution_warning | 0.0 | -0.01 | 2 | 0 | -6.57 | -8.21 | -46.32 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | -2.85 | -10.23 | -15.47 | 19.88 | 9.45 | 18.89 | False |  | distribution_warning | -0.15 | -1.77 | 2 | 0 | -8.44 | -6.44 | -21.76 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | -5.31 | -4.53 | -11.45 | 17.65 | 1.75 | 15.42 | False |  | distribution_warning | -1.05 | -1.93 | 0 | 0 | -3.05 | -4.02 | -28.83 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | -8.32 | 14.46 | 14.69 | 87.33 | 74.53 | 91.16 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.06 | 1.68 | 2 | 2 | 0.29 | 1.99 | -11.91 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 15.5 | 13.24 | -24.26 | 122.97 | 58.87 | 126.47 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.46 | 1.07 | 1 | 2 | 11.84 | 10.13 | -24.51 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | -6.07 | 2.58 | 30.93 | 59.55 | 57.57 | 57.57 | True | 距60日低點反彈>50% | mild_accumulation | -0.15 | 0.05 | 1 | 1 | -2.37 | -0.56 | -11.68 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 4.39 | -11.19 | -0.83 | 0.85 | 8.68 | 28.65 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.0 | -1.62 | -37.04 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 84.97614765538744 | 32.40539437293427 | 0.35 | -6.42 | 5.01 | 41.68 | 11.4 | 41.91 | False |  | distribution_warning | -1.69 | -0.08 | 0 | 2 | -3.84 | -3.62 | -26.18 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | -1.29 | -6.71 | -22.43 | 25.93 | 8.32 | 22.4 | False |  | distribution_warning | -0.95 | -0.55 | 0 | 0 | -4.38 | -4.32 | -28.25 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | -0.84 | -7.78 | -17.33 | 30.5 | 3.11 | 30.91 | False |  | distribution_warning | -2.89 | -2.99 | 0 | 1 | -5.3 | -5.38 | -30.13 | 11 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 98.21291582397656 | 109.2004683088644 | -0.26 | -5.21 | -13.38 | -11.98 | 6.11 | 6.11 | False |  | distribution_warning | -0.99 | -0.27 | 1 | 1 | -1.81 | -2.51 | -18.9 | 13 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | -3.22 | -14.96 | -1.33 | 116.2 | 47.17 | 101.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.62 | 3 | 2 | -5.61 | -2.75 | -21.87 |  | fail_already_priced_in |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | -2.83 | 0.0 | -28.53 | 3.72 | 12.06 | 12.06 | False |  | mild_accumulation | -0.34 | 0.99 | 1 | 3 | -1.82 | -2.1 | -30.31 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | -0.98 | 4.89 | -5.08 | 48.89 | 54.13 | 54.13 | True | 距60日低點反彈>50% | distribution_warning | -0.02 | -0.69 | 1 | 0 | 2.98 | 3.84 | -6.49 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | -2.33 | -11.58 | -27.27 | 46.3 | 19.71 | 48.89 | False |  | distribution_warning | -0.73 | -1.66 | 0 | 0 | -5.75 | -5.05 | -28.1 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | -2.28 | 7.96 | -15.89 | -17.75 | 23.56 | 23.56 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 0.32 | 0.91 | -17.75 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 9.7 | 42.61 | 80.42 | 193.38 | 86.79 | 192.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.92 | -1.18 | 0 | 0 | 21.39 | 18.01 | -18.41 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -4.71 | 5.88 | -16.49 | 58.82 | 20.9 | 55.77 | False |  | mild_accumulation | -0.46 | 0.91 | 1 | 1 | -5.94 | -3.72 | -18.8 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | -8.44 | 18.9 | 5.64 | 123.61 | 89.64 | 119.15 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 1.87 | 1 | 1 | 4.36 | 4.73 | -15.14 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | 0.66 | 17.95 | 23.43 | 210.15 | 73.83 | 239.44 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.36 | 0.43 | 2 | 1 | 7.01 | 8.4 | -16.19 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 166.4840985505344 | 98.8701912579111 | -3.17 | 0.55 | 15.46 | 49.39 | 31.65 | 48.78 | False |  | distribution_warning | -0.65 | -0.91 | 1 | 1 | -0.29 | -0.42 | -11.17 | 17 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | -2.5 | 0.37 | 0.74 | 4.2 | 3.02 | 14.71 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -2.13 | -1.75 | -3.87 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 17.96 | 21.34 | -3.18 | 20.95 | 22.9 | 25.54 | False |  | mild_accumulation | -0.44 | 1.2 | 1 | 3 | 15.7 | 13.82 | -3.79 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 0.71 | -2.74 | -25.07 | -16.22 | 0.71 | 0.71 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.15 | -3.73 | -26.42 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 4.14 | 16.53 | 30.58 | 184.99 | 94.33 | 173.61 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -1.19 | 0 | 1 | 4.05 | 6.53 | -6.16 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | 4.04 | -4.59 | -11.6 | 123.55 | 63.94 | 124.48 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.09 | -1.86 | 1 | 1 | -2.94 | 0.65 | -17.15 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | -9.03 | -4.03 | 36.46 | 38.08 | 75.25 | 87.14 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -1.06 | 2.51 | 0 | 3 | -6.87 | -2.77 | -14.03 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | -14.34 | -7.85 | -23.54 | 34.61 | 27.19 | 27.19 | False |  | distribution_warning | -0.07 | -1.69 | 1 | 1 | -13.94 | -12.26 | -31.66 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 53.99150153319462 | 40.00683620722877 | 1.01 | -9.32 | -0.25 | 6.12 | 18.4 | 18.4 | False |  | distribution_warning | -1.83 | -1.94 | 0 | 0 | -4.05 | -3.12 | -21.92 | 10 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 80.45926827221638 | 62.39086469044157 | 0.95 | -0.47 | -1.85 | 20.45 | 9.05 | 21.28 | False |  | distribution_warning | -1.05 | -1.36 | 1 | 1 | 0.8 | -1.03 | -18.77 | 14 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth |  | 119.89332334202707 | 52.56887075398791 | -3.42 | -12.9 | -7.6 | 7.05 | 1.8 | 6.04 | False |  | distribution_warning | -0.57 | -0.39 | 2 | 2 | -10.66 | -9.05 | -17.54 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | -5.65 | -7.88 | -18.34 | -21.43 | 9.23 | 9.23 | False |  | mild_accumulation | 0.53 | -0.04 | 2 | 1 | -6.52 | -5.6 | -22.08 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | -8.52 | 14.88 | -31.39 | -29.43 | 37.99 | 37.99 | False |  | strong_accumulation | 0.01 | 0.48 | 2 | 2 | 3.02 | 1.81 | -33.78 | 21 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | 3.47 | 14.81 | 38.19 | 17.29 | 37.72 | 50.76 | False |  | strong_accumulation | 0.45 | 0.45 | 2 | 2 | 7.79 | 7.62 | -1.32 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | 5.62 | 3.13 | 10.4 | -24.37 | 12.48 | 12.48 | False |  | distribution_warning | -0.17 | -0.17 | 0 | 0 | 1.79 | 1.85 | -7.97 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 0.31 | -8.43 | 0.47 | 13.65 | 8.64 | 15.91 | False |  | distribution_warning | -2.65 | -1.56 | 0 | 0 | -1.14 | -2.02 | -19.88 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | -4.51 | 12.02 | 2.87 | 77.86 | 43.83 | 79.92 | True | 近120日漲幅>70% | strong_accumulation | 1.41 | 1.84 | 2 | 3 | 3.65 | 2.75 | -9.69 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -3.46 | -5.11 | -12.55 |  | 1.36 |  | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | -3.83 | -5.39 | -24.15 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -2.83 | 3.26 | 7.57 | 14.13 | 17.05 | 17.05 | False |  | distribution_warning | -0.09 | -0.48 | 1 | 0 | -0.64 | 0.16 | -7.0 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 6.9 | 1.31 | -28.82 | 116.03 | 15.46 | 117.54 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 8.26 | 4.06 | -30.57 |  | fail_already_priced_in |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | -2.19 | -6.57 | -6.1 | 67.38 | 7.44 | 76.5 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | -4.1 | -3.84 | -21.42 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | -3.6 | -4.63 | -25.35 | -17.79 | 1.9 | 1.9 | False |  | distribution_warning | -0.15 | -0.21 | 1 | 1 | -3.91 | -3.83 | -29.84 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | -6.37 | 2.86 | -18.0 | 7.46 | 33.33 | 33.33 | False |  | mild_accumulation | -0.56 | 0.11 | 2 | 2 | -4.08 | -3.13 | -21.31 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | -2.31 | 5.77 | 1.1 | 38.19 | 40.66 | 40.66 | False |  | mild_accumulation | 2.62 | -1.07 | 2 | 1 | -0.06 | 1.11 | -5.66 | 24 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 3.52 | 21.72 | -4.85 | -7.11 | 68.1 | 68.1 | True | 距60日低點反彈>50% | distribution_warning | -4.27 | -1.28 | 0 | 1 | 4.33 | 6.18 | -6.86 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -0.33 | -0.65 | -34.79 | -5.26 | 22.36 | 22.36 | False |  | distribution_warning | -1.43 | -0.61 | 1 | 1 | -1.7 | -2.37 | -47.83 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 1.64 | -1.59 | 0.82 | 33.45 | 7.54 | 33.94 | False |  | mild_accumulation | 0.89 | 0.0 | 3 | 0 | -0.89 | -0.6 | -7.25 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | -2.03 | -0.46 | 0.23 | -12.12 | 2.35 | 6.36 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 0 | -1.53 | -1.38 | -9.0 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | -0.36 | 0.36 | -0.36 | -3.81 | 3.35 | 3.35 | False |  | mild_accumulation | 0.15 | -0.1 | 2 | 2 | -0.18 | -0.16 | -3.14 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 88.58141426234812 | 67.0501740981801 | -3.83 | -7.95 | -7.6 | -6.54 | 0.28 | 0.28 | False |  | distribution_warning | -1.12 | -1.0 | 1 | 0 | -4.14 | -3.88 | -11.74 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 98.63848944446872 | 32.20453750927072 | -1.19 | 12.13 | 41.56 | 152.02 | 80.14 | 161.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.27 | -4.27 | 1 | 1 | -2.72 | 2.25 | -16.69 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 118.48334266517357 | 55.91323881362982 | 2.71 | 8.99 | 9.78 | -3.5 | 37.73 | 37.73 | False |  | distribution_warning | -0.21 | 0.0 | 2 | 0 | 6.65 | 6.33 | -8.18 | 18 | selected |