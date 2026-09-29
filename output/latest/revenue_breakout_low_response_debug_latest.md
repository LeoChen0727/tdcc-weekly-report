# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-29 19:37:26 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 733450 |
| tdcc_rows | 1967 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 402 |
| tdcc_mild_accumulation_count | 763 |
| tdcc_distribution_warning_count | 615 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 93 |
| already_priced_in_excluded | 35 |
| overheat_pass | 58 |
| score_pass | 58 |
| theme_priority_pass | 47 |
| final_rows | 47 |

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
| fail_low_response_condition | 267 |
| fail_already_priced_in | 35 |
| fail_defensive_or_traditional_excluded | 10 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | -1.7 | 2.12 | 0.0 | 7.04 | 33.8 | 44.79 | False |  | strong_accumulation | 0.79 | 0.88 | 2 | 2 | -1.73 | 1.35 | -12.42 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral |  | 93.04522686147229 | 122.05590293593936 | -2.79 | -6.28 | -0.95 | -13.28 | 11.29 | 11.29 | False |  | mild_accumulation | -0.06 | 0.76 | 1 | 3 | -2.56 | -2.07 | -16.4 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 0.19 | -0.38 | -1.88 | -19.1 | 4.41 | 4.41 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 0.28 | 0.2 | -16.1 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | -0.98 | -2.88 | -11.01 | 13.74 | 6.43 | 14.51 | False |  | distribution_warning | -0.85 | -0.33 | 1 | 0 | -0.37 | -0.56 | -15.13 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 3.68 | 3.1 | 1.1 | -2.14 | 6.09 | 7.96 | False |  | strong_accumulation | 0.15 | 0.02 | 2 | 2 | 3.32 | 2.7 | -9.18 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -3.24 | -3.24 | -7.66 | -14.02 | 0.73 | 0.73 | False |  | distribution_warning | -0.04 | -0.03 | 0 | 0 | -2.35 | -2.31 | -12.6 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | -5.58 | -5.37 | -6.83 | -26.31 | 3.42 | 10.73 | False |  | strong_accumulation | 0.12 | 0.13 | 3 | 3 | -3.44 | -3.21 | -13.5 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 0.41 | -0.8 | -13.64 | -17.67 | 5.11 | 5.11 | False |  | mild_accumulation | 1.27 | -0.25 | 2 | 1 | 0.49 | 0.05 | -20.32 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 3.91 | 6.96 | 3.55 | -1.02 | 10.61 | 20.66 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 1 | 3.13 | 3.22 | -5.5 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 12.24 | 21.72 | 88.03 | 129.17 | 95.12 | 146.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.03 | 0.34 | 2 | 2 | 15.06 | 13.96 | -12.87 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 11.79 | 20.8 | 28.39 | 102.91 | 92.06 | 121.91 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.85 | 11.08 | 2 | 2 | 20.28 | 19.0 | -5.2 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | -1.39 | -8.03 | -7.55 | -25.11 | 4.11 | 4.11 | False |  | mild_accumulation | 0.24 | -0.23 | 2 | 1 | -0.99 | -1.62 | -18.2 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 33032.925531914894 | 13849.620888036585 | -11.98 | -9.2 | 6.58 | 5.16 | 6.58 | 12.66 | False |  | distribution_warning | -0.06 | -0.19 | 1 | 1 | -7.62 | -6.68 | -16.4 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | D_僅留完整清單 | 102.5304395876603 | 136.2137376977922 | 7.66 | 0.75 | 1.14 | 15.09 | 19.2 | 24.77 | False |  | mild_accumulation | -0.27 | 0.01 | 1 | 1 | 6.37 | 5.89 | -4.98 | 16 | selected |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 33.87 | 46.49 | 81.03 | 106.17 | 101.2 | 119.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.97 | -0.99 | 3 | 1 | 35.66 | 33.87 | 0.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -3.04 | -15.28 | 53.74 | 263.27 | 77.12 | 256.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.55 | 0.42 | 1 | 2 | -5.31 | -3.21 | -19.69 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 1.15 | -8.68 | -10.54 | -27.95 | 4.37 | 4.37 | False |  | mild_accumulation | -0.54 | 0.07 | 0 | 1 | -0.13 | -1.68 | -21.26 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | -2.61 | -6.14 | -7.74 | -19.68 | 0.17 | 1.02 | False |  | distribution_warning | -0.45 | -0.69 | 0 | 0 | -2.52 | -3.28 | -17.79 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 2.85 | 22.13 | -19.46 | 120.04 | 29.32 | 141.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.91 | -1.46 | 1 | 2 | 5.23 | 5.29 | -25.52 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 0.49 | -2.23 | 8.47 | 15.38 | 10.22 | 20.12 | False |  | mild_accumulation | 0.64 | 0.01 | 1 | 1 | 1.0 | 0.88 | -13.14 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | -2.52 | -1.12 | -5.06 | 12.75 | 5.45 | 19.96 | False |  | mild_accumulation | 0.03 | 0.02 | 1 | 2 | 0.15 | -0.05 | -6.64 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 2.03 | 3.31 | -18.23 | 151.67 | 37.9 | 164.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.99 | 0.0 | 1 | 1 | 4.59 | 3.81 | -22.03 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 17.72 | 138.28 | 83.78 | 248.99 | 168.87 | 357.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.85 | 5.23 | 2 | 3 | 53.79 | 45.78 | 0.0 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | 3.51 | -1.22 | -24.3 | 43.36 | 27.56 | 48.62 | False |  | mild_accumulation | 0.22 | -0.12 | 2 | 2 | 2.18 | 1.87 | -28.48 | 18 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 0.0 | -0.99 | 4.81 | 25.25 | 10.6 | 23.1 | False |  | strong_accumulation | 0.16 | 0.15 | 2 | 2 | -0.26 | -0.2 | -8.74 | 20 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | -0.36 | -8.21 | -48.06 | 80.56 | 20.04 | 89.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.27 | 1.25 | 2 | 2 | -1.16 | -2.7 | -49.02 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | 0.61 | 2.27 | 0.41 | 24.37 | 13.53 | 23.13 | False |  | strong_accumulation | 0.04 | 0.03 | 2 | 2 | 1.63 | 1.62 | -1.39 | 21 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | -2.07 | -6.32 | -18.56 | -19.66 | 29.08 | 29.08 | False |  | mild_accumulation | 0.28 | 0.18 | 1 | 1 | -1.58 | -1.78 | -22.04 | 22 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | -3.06 | -4.13 | -5.18 | 84.32 | 48.72 | 107.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.27 | 2 | 2 | -0.1 | 0.41 | -13.0 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | -2.43 | -14.82 | -34.18 | -0.55 | 1.12 | 1.12 | False |  | distribution_warning | -0.82 | -0.22 | 1 | 1 | -7.3 | -7.38 | -35.93 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 122.01643193808464 | 89.65916297833103 | 4.07 | 9.25 | 1.61 | 15.24 | 17.68 | 19.47 | False |  | mild_accumulation | 0.06 | -0.07 | 2 | 1 | 5.6 | 4.77 | -5.5 | 24 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -4.99 | -2.22 | -1.81 | -9.73 | 5.54 | 5.54 | False |  | mild_accumulation | 0.77 | -0.15 | 2 | 1 | -1.5 | -1.82 | -14.34 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -10.77 | -10.02 | 1.17 | 75.2 | 73.79 | 82.63 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.09 | 0.78 | 2 | 2 | -7.87 | -4.43 | -16.15 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 0.31 | -0.21 | 44.38 | 66.61 | 46.58 | 66.61 | True | 近60日漲幅>40% | distribution_warning | -0.41 | -0.36 | 1 | 1 | -0.5 | 1.68 | -6.5 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | -4.59 | 8.71 | -1.13 | 16.22 | 26.3 | 26.3 | False |  | distribution_warning | -0.73 | -0.48 | 1 | 1 | 0.49 | -0.28 | -13.98 | 18 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 10.24 | 14.29 | -16.74 | 26.63 | 33.63 | 33.63 | False |  | strong_accumulation | 0.87 | 0.73 | 2 | 2 | 10.48 | 8.32 | -18.01 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | 9.8 | -0.88 | -9.31 | 6.16 | 58.87 | 58.87 | True | 距60日低點反彈>50% | distribution_warning | -0.36 | -0.12 | 1 | 1 | 4.26 | 6.18 | -16.1 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 1.69 | 3.72 | 6.94 | 37.12 | 16.03 | 37.38 | False |  | strong_accumulation | 1.77 | 1.44 | 3 | 2 | 1.51 | 1.64 | -9.95 | 23 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -1.9 | 1.2 | -8.81 | 5.49 | 20.61 | 20.61 | False |  | strong_accumulation | 0.16 | 0.13 | 2 | 2 | -0.79 | -0.2 | -14.38 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 129.84671742960728 | 95.18081273476336 | 0.61 | -10.38 | -13.0 | 47.97 | 25.19 | 40.97 | False |  | mild_accumulation | -0.11 | 0.06 | 2 | 2 | -5.48 | -4.97 | -23.96 | 21 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | 1.86 | -2.86 | -0.56 | 28.52 | 13.74 | 28.06 | False |  | mild_accumulation | -0.71 | 0.02 | 1 | 1 | -3.04 | -1.99 | -15.94 | 18 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 5.8 | 9.12 | 43.14 | 113.14 | 48.07 | 113.14 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.2 | 2 | 1 | 5.98 | 6.41 | -3.18 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 8.44 | 13.49 | -11.91 | 30.9 | 25.13 | 34.51 | False |  | strong_accumulation | 2.35 | 1.85 | 3 | 2 | 11.82 | 9.13 | -12.54 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 9.58 | 5.76 | -27.43 | -3.81 | 17.21 | 17.21 | False |  | distribution_warning | -0.5 | -0.44 | 1 | 1 | 8.66 | 5.66 | -29.29 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | -3.62 | -6.3 | 24.32 | 124.39 | 57.14 | 154.27 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 0.85 | 2 | 2 | 0.07 | 0.92 | -11.07 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | -0.38 | 2.31 | -12.95 | 18.79 | 3.51 | 19.46 | False |  | strong_accumulation | 0.19 | 0.12 | 3 | 3 | 0.96 | 0.29 | -21.57 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 245.59047432473767 | 22.17724035271652 | 3.94 | 15.54 | 3.57 | -17.96 | 31.82 | 31.82 | False |  | mild_accumulation | 0.08 | 0.37 | 1 | 2 | 5.34 | 5.56 | -5.38 | 22 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 1.22 | -2.22 | -11.15 | 27.16 | 6.24 | 31.87 | False |  | strong_accumulation | 0.98 | 1.08 | 3 | 3 | 1.01 | -0.78 | -29.21 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | -3.27 | -4.01 | -19.13 | 42.09 | 28.32 | 50.6 | False |  | mild_accumulation | 0.35 | 0.77 | 2 | 1 | -0.96 | -0.92 | -30.81 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.73 | -0.9 | -1.6 | 0.73 | 2.79 | 9.72 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 0.92 | 0.62 | -5.79 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 4.52 | 14.89 | 23.43 | 121.92 | 35.28 | 125.78 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.01 | 0.0 | 0 | 0 | 2.48 | 5.09 | -28.63 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -5.74 | 8.54 | -7.29 | -5.06 | 23.12 | 23.12 | False |  | distribution_warning | -0.1 | -0.1 | 0 | 0 | -1.08 | 0.49 | -14.35 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.4659980905217 | 384.0048979178835 | 1.06 | -2.72 | 10.85 | 16.73 | 32.41 | 32.41 | False |  | mild_accumulation | -0.51 | 0.72 | 1 | 2 | 0.46 | 0.43 | -13.2 | 21 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | -2.34 | 25.12 | 56.03 | 85.32 | 112.94 | 112.94 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.84 | -2.52 | 1 | 0 | 2.27 | 6.15 | -7.97 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 0.34 | 3.47 | -18.22 | -11.42 | 10.56 | 10.56 | False |  | strong_accumulation | 0.41 | 0.15 | 3 | 3 | 1.47 | 0.45 | -26.93 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | -2.54 | 1.05 | 4.63 | 173.89 | 62.71 | 171.19 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.76 | -8.56 | 0 | 0 | -0.34 | 1.26 | -14.29 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | 0.33 | -3.26 | 29.99 | 48.95 | 36.35 | 57.36 | False |  | distribution_warning | -3.54 | -0.68 | 1 | 1 | -1.7 | 0.54 | -14.51 | 18 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | 3.03 | -10.82 | -17.33 | -0.91 | 26.51 | 26.51 | False |  | distribution_warning | -0.71 | 0.0 | 0 | 2 | -3.28 | -0.77 | -18.93 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | -1.39 | -8.39 | -50.23 | 31.08 | 7.3 | 30.28 | False |  | distribution_warning | -1.68 | -0.62 | 1 | 1 | -1.3 | -3.02 | -53.03 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | -0.1 | 0.41 | -9.98 | -1.72 | 3.4 | 3.4 | False |  | strong_accumulation | 0.2 | 0.2 | 2 | 2 | 0.29 | -0.11 | -10.81 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 106.21354266385858 | 53.00526357886879 | 2.37 | 1.43 | -22.26 | -1.14 | 24.64 | 24.64 | False |  | strong_accumulation | 0.51 | 1.64 | 2 | 2 | 3.28 | 2.25 | -29.95 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -2.98 | -6.0 | -12.24 | -12.06 | 1.44 | 1.44 | False |  | distribution_warning | -0.55 | -1.0 | 1 | 0 | -3.42 | -3.3 | -15.06 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -5.7 | -8.77 | 5.24 | -1.06 | 9.34 | 16.12 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -4.23 | -3.07 | -10.51 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | -0.83 | 0.0 | 1.59 | 1.22 | 2.46 | 10.34 | False |  | strong_accumulation | 0.16 | 0.14 | 3 | 2 | -0.89 | -0.77 | -4.7 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | -5.93 | -1.24 | -11.19 | -3.74 | 12.13 | 12.13 | False |  | strong_accumulation | 0.22 | 0.2 | 3 | 3 | -1.98 | -2.48 | -22.98 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | -3.3 | -0.39 | -0.39 | -33.77 | 7.62 | 7.62 | False |  | distribution_warning | -0.04 | -0.13 | 2 | 1 | -1.02 | -0.91 | -8.62 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 81.22955024989892 | 63.44944538479019 | -2.48 | -1.5 | -12.44 | -10.05 | 2.6 | 2.6 | False |  | mild_accumulation | -0.12 | 0.01 | 1 | 1 | -0.67 | -1.15 | -16.53 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral | B_可觀察 | 139.52959372288657 | 105.3349499169469 | -4.46 | -1.71 | -9.61 | -26.83 | 0.77 | 0.77 | False |  | strong_accumulation | 0.19 | 0.44 | 2 | 2 | -1.63 | -1.99 | -11.35 | 21 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | -1.94 | 1.0 | 21.86 | -11.72 | 20.41 | 23.56 | False |  | strong_accumulation | 1.41 | 1.0 | 3 | 2 | -2.06 | -1.4 | -9.69 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | -1.12 | 2.18 | 0.28 | 3.83 | 13.18 | 13.18 | False |  | strong_accumulation | 0.75 | 1.39 | 3 | 3 | 0.45 | 0.3 | -10.77 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | 4.13 | 14.32 | 11.56 | 79.03 | 39.8 | 77.88 | True | 近120日漲幅>70% | strong_accumulation | 1.26 | 1.22 | 3 | 3 | 4.98 | 5.29 | -7.04 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -11.81 | -7.54 | -9.47 | 15.74 | 6.22 | 20.71 | False |  | mild_accumulation | 0.01 | -0.02 | 2 | 0 | -5.52 | -6.68 | -45.87 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 1.36 | -17.2 | -8.85 | 10.97 | 12.85 | 14.59 | False |  | distribution_warning | -1.17 | -0.66 | 1 | 1 | -1.59 | -1.47 | -19.32 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | -1.67 | -1.26 | -13.92 | -1.26 | 3.07 | 6.33 | False |  | distribution_warning | -0.17 | -1.65 | 1 | 0 | -1.09 | -1.59 | -27.91 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | -2.06 | 5.75 | 30.73 | 78.68 | 77.02 | 93.88 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.05 | -3.62 | 1 | 1 | 0.09 | 2.56 | -10.66 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 48.07 | 73.19 | 28.73 | 204.23 | 137.28 | 200.0 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.24 | 5.29 | 2 | 2 | 48.14 | 42.08 | -1.99 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | -0.87 | 1.19 | 24.09 | 54.55 | 68.73 | 68.73 | True | 距60日低點反彈>50% | distribution_warning | -1.07 | -0.58 | 0 | 1 | 0.93 | 3.18 | -5.56 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | -0.42 | 0.0 | 0.0 | 6.22 | 9.13 | 29.19 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.9 | -0.62 | -36.77 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 84.97614765538744 | 32.40539437293427 | 2.2 | 2.99 | 6.9 | 36.97 | 20.47 | 40.7 | False |  | strong_accumulation | 0.02 | 0.98 | 2 | 2 | 4.15 | 2.9 | -20.17 | 21 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 1.46 | -2.64 | -24.18 | 4.85 | 10.97 | 10.97 | False |  | distribution_warning | -0.85 | -0.78 | 1 | 1 | 0.07 | -0.72 | -25.18 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 0.96 | -6.77 | -16.67 | 22.45 | 4.35 | 26.89 | False |  | distribution_warning | -1.72 | -2.42 | 0 | 1 | -1.11 | -2.09 | -29.29 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 0.97 | 5.87 | -4.6 | -8.99 | 15.28 | 15.28 | False |  | mild_accumulation | 0.2 | -0.1 | 1 | 1 | 5.44 | 3.46 | -11.89 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 18.76 | 4.95 | 19.0 | 86.1 | 78.41 | 96.79 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 0.91 | 2 | 2 | 15.99 | 12.28 | -5.28 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | 2.61 | 3.06 | -16.61 | 7.27 | 18.59 | 18.59 | False |  | strong_accumulation | 1.56 | 2.16 | 2 | 3 | 2.71 | 2.39 | -20.94 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 0.58 | 6.33 | 2.96 | 39.49 | 59.33 | 59.33 | True | 距60日低點反彈>50% | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 2.52 | 3.23 | -4.75 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth | A_優先追蹤 | 50.31333751338634 | 36.26105158634005 | 0.2 | -8.09 | -20.53 | 29.53 | 21.38 | 40.38 | False |  | mild_accumulation | -0.65 | 0.44 | 0 | 2 | -1.22 | -1.94 | -23.5 | 16 | selected |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 1.73 | 3.7 | -4.08 | -18.56 | 30.67 | 30.67 | False |  | mild_accumulation | 0.49 | 0.0 | 1 | 0 | 3.07 | 3.98 | -9.82 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 19.01 | 59.61 | 45.36 | 224.56 | 131.78 | 233.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.44 | -2.03 | 1 | 0 | 26.65 | 24.47 | -9.96 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -4.28 | -13.54 | -14.71 | 34.91 | 16.79 | 38.5 | False |  | mild_accumulation | 0.57 | 0.82 | 2 | 1 | -5.68 | -4.7 | -17.85 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 8.27 | 15.33 | 13.16 | 47.07 | 107.83 | 107.83 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.41 | 1.02 | 1 | 1 | 7.58 | 9.29 | -7.0 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -11.34 | 3.07 | 33.88 | 152.1 | 62.45 | 144.02 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | 0.0 | 1 | 1 | -0.61 | -0.4 | -21.67 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | -0.54 | 4.21 | 17.03 | 37.92 | 33.45 | 41.06 | False |  | mild_accumulation | 0.05 | -0.17 | 1 | 1 | -0.04 | 0.85 | -9.95 | 24 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | -1.79 | -2.48 | 2.61 | 0.36 | 3.77 | 15.55 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -1.15 | -1.15 | -3.17 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | -1.42 | 17.02 | 0.66 | 14.56 | 23.06 | 25.7 | False |  | distribution_warning | -0.64 | -1.36 | 1 | 1 | 9.62 | 7.91 | -3.66 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | -4.82 | 1.37 | -18.68 | -8.07 | 4.96 | 4.96 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.53 | 0.09 | -20.86 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 10.84 | 31.75 | 48.69 | 185.59 | 149.61 | 178.56 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | -0.31 | 2 | 2 | 19.31 | 17.56 | -7.26 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -2.42 | -17.32 | 4.79 | 69.63 | 59.09 | 79.18 | True | 距60日低點反彈>50% | distribution_warning | -5.69 | -4.98 | 0 | 0 | -3.74 | -1.4 | -19.6 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 24.8 | 19.19 | 98.42 | 70.46 | 130.6 | 146.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.72 | 1.35 | 1 | 2 | 18.12 | 19.69 | -3.7 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 273.61017160561573 | 13.583391933925409 | 4.1 | -9.35 | -24.72 | 19.26 | 40.11 | 40.11 | False |  | distribution_warning | -2.2 | -3.47 | 1 | 0 | -3.31 | -1.46 | -24.64 | 14 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 10.63 | 8.19 | 19.85 | 11.14 | 45.1 | 45.1 | False |  | strong_accumulation | 0.91 | 0.27 | 2 | 2 | 15.05 | 12.97 | -4.31 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 0.44 | 15.0 | 6.48 | 19.05 | 18.31 | 23.66 | False |  | strong_accumulation | 0.97 | 1.03 | 3 | 3 | 6.67 | 4.16 | -11.88 | 20 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | -1.99 | -14.33 | -15.43 | -4.25 | 1.68 | 1.68 | False |  | distribution_warning | -2.41 | -2.45 | 0 | 0 | -6.41 | -5.42 | -17.64 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 0.93 | -3.37 | -7.49 | -16.22 | 14.02 | 14.02 | False |  | distribution_warning | -0.67 | -2.29 | 1 | 2 | -0.85 | -1.04 | -18.67 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | 5.06 | -0.4 | -29.06 | -33.24 | 39.11 | 39.11 | False |  | mild_accumulation | 1.33 | -0.08 | 2 | 2 | 1.01 | 2.05 | -29.46 | 20 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -4.81 | 1.84 | 22.84 | 9.06 | 25.62 | 39.9 | False |  | strong_accumulation | 0.38 | 0.38 | 2 | 2 | -2.84 | -1.45 | -8.73 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -3.77 | -4.05 | 4.75 | -20.13 | 9.23 | 9.23 | False |  | distribution_warning | -0.28 | -0.28 | 0 | 0 | -1.16 | -1.27 | -10.63 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 13.49 | 11.42 | 11.42 | 2.81 | 20.99 | 24.91 | False |  | distribution_warning | -0.29 | -1.22 | 1 | 0 | 12.02 | 9.55 | -8.5 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround | D_降級_TDCC轉弱 | 98.0452097433352 | 55.75153262414533 | 0.42 | 11.57 | 2.55 | 32.78 | 48.77 | 48.77 | False |  | distribution_warning | -1.16 | -0.26 | 0 | 1 | 2.94 | 5.11 | -6.59 | 15 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -1.11 | -5.13 | -17.16 |  | 0.91 |  | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | -2.67 | -3.64 | -24.49 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -1.63 | 2.67 | 4.96 | 10.44 | 20.17 | 20.17 | False |  | distribution_warning | -0.54 | -0.37 | 1 | 0 | 0.2 | 0.8 | -4.51 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | -7.17 | 4.11 | -22.99 | 86.26 | 8.57 | 96.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 0.22 | -2.33 | -34.71 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | -3.79 | -0.98 | -11.74 | 75.0 | 16.13 | 75.61 | True | 近120日漲幅>70% | mild_accumulation | 0.3 | 1.67 | 2 | 1 | 2.68 | 1.18 | -15.06 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 1.8 | -2.75 | -21.82 | -9.58 | 7.6 | 7.6 | False |  | distribution_warning | -0.33 | -0.82 | 1 | 0 | 2.0 | 0.69 | -24.33 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | 1.88 | 2.15 | -3.8 | -18.37 | 40.74 | 40.74 | False |  | mild_accumulation | 0.67 | -0.15 | 2 | 1 | -0.06 | 1.8 | -11.42 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 275.0567709273065 | 87.01658569617017 | -1.81 | -0.55 | 6.25 | 23.92 | 39.13 | 39.13 | False |  | mild_accumulation | 0.75 | 1.26 | 1 | 2 | -1.14 | -0.19 | -6.69 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | -3.71 | -2.03 | 4.98 | -17.0 | 60.48 | 60.48 | True | 距60日低點反彈>50% | distribution_warning | -3.04 | 0.0 | 1 | 0 | -2.56 | 0.21 | -11.08 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -2.46 | -12.76 | -40.8 | -26.81 | 18.76 | 18.76 | False |  | distribution_warning | -0.81 | -0.61 | 2 | 1 | -2.59 | -3.36 | -49.36 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | -1.32 | -0.53 | 1.91 | 19.55 | 5.67 | 28.62 | False |  | mild_accumulation | 0.14 | -0.58 | 1 | 0 | -0.17 | -0.49 | -6.75 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | -1.35 | -0.9 | 2.33 | -13.41 | 3.29 | 7.33 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | -0.53 | -0.73 | -8.16 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | -2.12 | -0.72 | -1.07 | -4.81 | 2.97 | 2.97 | False |  | mild_accumulation | -0.08 | 0.29 | 1 | 3 | -0.7 | -0.8 | -3.48 |  | fail_low_response_condition |