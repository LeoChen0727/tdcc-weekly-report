# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-23 20:58:11 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 729533 |
| tdcc_rows | 1963 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 374 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 652 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 99 |
| already_priced_in_excluded | 39 |
| overheat_pass | 60 |
| score_pass | 60 |
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
| fail_low_response_condition | 261 |
| fail_already_priced_in | 39 |
| fail_defensive_or_traditional_excluded | 12 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | -1.35 | 12.31 | 3.55 | 14.06 | 35.19 | 46.29 | False |  | mild_accumulation | 0.28 | 0.78 | 1 | 2 | -0.51 | 2.76 | -11.52 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral |  | 93.04522686147229 | 122.05590293593936 | -0.93 | -8.62 | 1.44 | -12.03 | 12.89 | 12.89 | False |  | mild_accumulation | -0.81 | 0.13 | 1 | 2 | -2.08 | -1.06 | -15.2 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 1.74 | -1.5 | -0.94 | -20.21 | 5.21 | 5.21 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.99 | 1.01 | -15.46 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 1.1 | -2.42 | -10.22 | 15.03 | 6.43 | 16.49 | False |  | mild_accumulation | 0.11 | -0.33 | 1 | 0 | -0.66 | -0.66 | -15.13 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 1.96 | 1.67 | 2.53 | -3.18 | 5.8 | 7.67 | False |  | strong_accumulation | 0.07 | 0.02 | 2 | 2 | 3.3 | 2.94 | -9.43 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -1.7 | -1.0 | -6.98 | -13.05 | 1.61 | 1.61 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -1.74 | -1.83 | -11.83 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 2.12 | -3.12 | -5.65 | -23.59 | 6.11 | 13.61 | False |  | strong_accumulation | 0.14 | 0.15 | 3 | 3 | -1.39 | -1.15 | -11.25 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 2.07 | -1.99 | -13.68 | -25.0 | 4.68 | 4.68 | False |  | strong_accumulation | 0.39 | 0.11 | 2 | 2 | 0.04 | -0.28 | -20.65 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 0.36 | -1.41 | -3.13 | -0.36 | 5.68 | 15.29 | False |  | distribution_warning | -0.18 | -0.2 | 2 | 2 | -0.85 | -0.7 | -9.71 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 23.69 | 30.19 | 120.05 | 163.93 | 118.55 | 170.59 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.14 | 2.68 | 3 | 3 | 29.21 | 28.35 | -4.36 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 21.86 | 23.41 | 29.73 | 129.78 | 88.82 | 124.47 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.09 | 7.42 | 2 | 2 | 20.64 | 21.03 | 0.0 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | -0.28 | -9.21 | -7.31 | -16.67 | 4.11 | 4.11 | False |  | distribution_warning | -0.81 | -1.37 | 1 | 1 | -1.92 | -2.02 | -18.2 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 33032.925531914894 | 13849.620888036585 | -5.2 | -10.39 | 6.33 | 4.93 | 7.59 | 13.73 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | -7.72 | -6.9 | -15.61 | 13 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 5.42 | -5.95 | -7.33 | 10.96 | 12.95 | 18.22 | False |  | mild_accumulation | -0.55 | 0.01 | 1 | 1 | 0.8 | 1.29 | -11.54 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 21.81 | 17.66 | 52.34 | 71.74 | 66.57 | 81.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.4 | -0.41 | 3 | 1 | 16.57 | 17.08 | -7.68 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | 2.86 | -14.61 | 68.34 | 278.32 | 81.14 | 279.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.87 | -0.02 | 0 | 1 | -4.71 | -1.45 | -17.87 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 0.79 | -14.43 | -16.67 | -31.08 | 1.19 | 1.19 | False |  | mild_accumulation | -0.56 | 0.09 | 0 | 2 | -4.44 | -5.26 | -23.65 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | 0.67 | -8.94 | -4.3 | -17.9 | 0.67 | 1.86 | False |  | distribution_warning | -0.93 | -0.97 | 0 | 0 | -2.5 | -3.06 | -17.1 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 7.21 | 23.91 | -10.0 | 126.49 | 31.37 | 145.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | -1.49 | 0 | 1 | 8.79 | 7.98 | -24.34 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 2.82 | -3.28 | 12.55 | 26.07 | 12.55 | 27.89 | False |  | mild_accumulation | 0.44 | 0.01 | 1 | 1 | 1.44 | 1.63 | -12.57 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 1.49 | -3.01 | -7.13 | 13.33 | 4.26 | 18.6 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -1.21 | -1.32 | -8.79 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 3.51 | 1.89 | -4.39 | 152.07 | 39.27 | 166.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.68 | 0.66 | 1 | 1 | 6.06 | 5.77 | -21.26 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 28.74 | 105.16 | 65.19 | 260.34 | 147.47 | 321.19 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 3.2 | 2 | 2 | 54.16 | 45.07 | -3.05 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | 0.32 | -1.24 | -26.73 | 47.91 | 25.2 | 45.87 | False |  | mild_accumulation | 0.32 | -0.71 | 2 | 1 | 0.22 | 0.25 | -29.96 | 18 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 3.23 | 3.85 | 1.99 | 28.0 | 13.02 | 28.97 | False |  | mild_accumulation | 0.07 | 0.06 | 1 | 1 | 1.85 | 1.95 | -6.74 | 20 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 6.9 | 6.7 | -49.74 | 103.55 | 25.52 | 102.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -0.78 | 1 | 1 | 3.12 | 1.74 | -53.03 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 53.32005371471296 | 39.26370665798065 | 5.04 | 3.52 | 3.73 | 27.88 | 14.68 | 26.9 | False |  | distribution_warning | -0.03 | -0.05 | 1 | 1 | 2.91 | 2.97 | -0.4 | 15 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 218.53271706735816 | 149.1423915250992 | 0.0 | -5.18 | -23.47 | -16.2 | 29.63 | 29.63 | False |  | distribution_warning | -1.14 | -1.2 | 1 | 1 | -1.92 | -1.81 | -23.96 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 2.07 | -4.96 | -16.87 | 89.56 | 47.44 | 105.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.1 | -3.77 | 1 | 1 | -1.58 | -0.5 | -16.87 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | 2.72 | -8.03 | -24.25 | 11.83 | 5.59 | 9.88 | False |  | distribution_warning | -0.62 | -0.71 | 1 | 0 | -4.45 | -4.25 | -33.1 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 6.54 | 8.5 | 3.73 | 16.52 | 17.68 | 19.47 | False |  | distribution_warning | -0.05 | -0.42 | 1 | 0 | 6.54 | 5.73 | -3.87 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | 3.99 | 2.67 | 1.39 | -5.07 | 9.28 | 9.28 | False |  | mild_accumulation | 1.06 | -0.22 | 3 | 0 | 1.9 | 1.51 | -11.3 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -4.24 | 3.2 | 6.35 | 93.16 | 82.26 | 91.53 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.96 | 3.36 | 3 | 3 | -4.29 | -0.46 | -12.06 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 2.02 | -1.34 | 36.86 | 68.66 | 50.87 | 69.56 | True | 距60日低點反彈>50% | mild_accumulation | -0.02 | 0.53 | 2 | 2 | -1.1 | 1.38 | -6.99 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 156.29654201767283 | 108.41049971158722 | 11.24 | 17.42 | 7.64 | 26.36 | 34.39 | 34.39 | False |  | distribution_warning | -0.74 | -0.06 | 1 | 2 | 8.13 | 6.54 | -8.46 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 13.85 | 15.4 | -14.2 | 25.56 | 33.63 | 33.63 | False |  | mild_accumulation | 0.38 | 0.11 | 1 | 1 | 12.09 | 9.97 | -22.0 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | 14.92 | 9.62 | -5.0 | 4.11 | 61.7 | 61.7 | True | 距60日低點反彈>50% | distribution_warning | -0.82 | -0.53 | 1 | 1 | 6.45 | 9.21 | -14.61 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 4.29 | 3.84 | 6.1 | 45.42 | 16.99 | 45.13 | False |  | strong_accumulation | 0.89 | 1.38 | 3 | 2 | 2.77 | 2.79 | -9.2 | 23 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | 0.29 | 2.71 | -7.2 | 9.11 | 22.4 | 22.4 | False |  | strong_accumulation | 0.37 | 0.36 | 3 | 3 | 0.82 | 1.3 | -13.1 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 129.84671742960728 | 95.18081273476336 | -1.28 | -14.84 | -6.86 | 55.9 | 27.74 | 53.99 | False |  | distribution_warning | -0.63 | -0.7 | 1 | 1 | -4.49 | -3.73 | -22.41 | 16 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -0.7 | -4.32 | -3.41 | 30.63 | 13.1 | 33.08 | False |  | strong_accumulation | 0.15 | 0.61 | 2 | 2 | -3.88 | -3.04 | -16.41 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 0.86 | 1.89 | 42.48 | 101.44 | 42.19 | 106.48 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.36 | -0.63 | 1 | 0 | 2.58 | 3.33 | -3.58 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 20.77 | 15.74 | -5.3 | 37.82 | 28.21 | 40.45 | False |  | mild_accumulation | 0.1 | -0.56 | 2 | 1 | 16.47 | 14.4 | -10.39 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 13.04 | 3.64 | -28.47 | -5.38 | 15.67 | 15.67 | False |  | distribution_warning | -0.36 | -0.54 | 1 | 1 | 7.89 | 5.47 | -34.93 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 4.57 | -0.39 | 13.81 | 151.22 | 59.94 | 158.79 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.57 | -3.29 | 1 | 1 | 1.13 | 2.83 | -9.49 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 1.92 | 1.72 | -11.94 | 22.77 | 3.51 | 23.06 | False |  | strong_accumulation | 0.26 | 0.17 | 3 | 3 | 1.15 | 0.31 | -21.57 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 245.59047432473767 | 22.17724035271652 | 6.03 | 16.0 | 2.65 | -21.52 | 31.82 | 31.82 | False |  | distribution_warning | -0.2 | -0.67 | 1 | 1 | 6.72 | 6.56 | -5.38 | 17 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 2.49 | -2.37 | -17.92 | 38.95 | 5.25 | 41.87 | False |  | strong_accumulation | 0.68 | 1.24 | 2 | 3 | -0.18 | -1.97 | -29.87 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 0.2 | 0.99 | -19.21 | 57.1 | 29.85 | 52.4 | False |  | distribution_warning | -0.49 | -0.05 | 2 | 0 | 0.05 | 0.21 | -29.99 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.55 | -1.8 | -4.72 | -0.73 | 1.3 | 8.13 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.72 | -0.85 | -7.16 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 9.59 | 27.65 | 55.12 | 130.82 | 53.01 | 134.84 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 8.51 | 10.44 | -25.77 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | 2.6 | 9.42 | -7.06 | -4.13 | 23.44 | 23.44 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.09 | 0.74 | -14.13 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | 0.71 | -5.48 | 6.75 | 22.1 | 31.71 | 31.71 | False |  | distribution_warning | -1.2 | -1.15 | 0 | 1 | -0.45 | -0.06 | -13.66 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 7.18 | 28.97 | 59.08 | 91.67 | 116.47 | 116.47 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.84 | 3.37 | 2 | 1 | 6.27 | 9.4 | -6.44 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 6.39 | 5.48 | -16.98 | 6.21 | 14.07 | 14.07 | False |  | strong_accumulation | 0.36 | 0.12 | 3 | 3 | 5.02 | 3.85 | -24.6 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 6.56 | 1.56 | 12.72 | 188.04 | 65.25 | 186.34 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.62 | -8.2 | 0 | 0 | 0.87 | 3.26 | -12.95 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | -1.33 | -4.7 | 25.28 | 51.44 | 32.34 | 53.79 | False |  | distribution_warning | -0.68 | -0.45 | 1 | 2 | -5.08 | -2.61 | -17.02 | 17 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | 0.58 | -8.42 | -15.81 | 5.78 | 21.4 | 21.4 | False |  | distribution_warning | -0.34 | -0.83 | 1 | 1 | -8.19 | -5.16 | -22.32 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 2.85 | -0.92 | -52.26 | 48.8 | 9.07 | 49.31 | False |  | distribution_warning | -1.04 | -0.07 | 1 | 1 | -0.37 | -1.76 | -55.64 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 1.03 | 1.34 | -9.58 | -1.31 | 4.25 | 4.25 | False |  | strong_accumulation | 0.26 | 0.26 | 3 | 3 | 1.17 | 0.72 | -10.07 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 106.21354266385858 | 53.00526357886879 | 4.86 | 0.65 | -22.76 | 7.47 | 24.32 | 24.32 | False |  | strong_accumulation | 0.29 | 1.52 | 2 | 2 | 3.18 | 2.45 | -30.13 | 23 | selected |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | 0.24 | -7.83 | -14.17 | -9.01 | 1.68 | 1.68 | False |  | distribution_warning | -0.52 | -0.45 | 1 | 1 | -3.89 | -3.69 | -14.86 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | 0.35 | -6.77 | 9.89 | 1.05 | 12.45 | 19.42 | False |  | distribution_warning | -0.2 | 0.0 | 0 | 0 | -2.28 | -0.7 | -7.96 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | 1.2 | 0.24 | 3.32 | 2.94 | 3.96 | 11.41 | False |  | strong_accumulation | 0.17 | 0.14 | 3 | 2 | 0.07 | 0.11 | -3.78 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | 2.37 | 5.19 | -8.23 | 4.53 | 16.96 | 16.96 | False |  | strong_accumulation | 0.16 | 0.04 | 3 | 2 | 2.29 | 1.5 | -19.66 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | -1.03 | -0.78 | -0.65 | -33.39 | 8.04 | 8.04 | False |  | mild_accumulation | -0.01 | 0.14 | 2 | 2 | -0.71 | -0.69 | -8.26 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | 2.58 | -2.55 | -9.64 | -6.67 | 3.54 | 3.54 | False |  | distribution_warning | -0.45 | -0.29 | 0 | 0 | 0.03 | -0.49 | -15.76 | 13 | selected |
| 2548 | 華固 | 建材營造 | neutral | B_可觀察 | 139.52959372288657 | 105.3349499169469 | 1.63 | -2.71 | -8.43 | -27.6 | 2.08 | 2.08 | False |  | mild_accumulation | -0.47 | 0.05 | 1 | 1 | -0.58 | -1.0 | -10.19 | 20 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | 2.77 | 6.31 | 25.59 | -5.0 | 28.65 | 29.32 | False |  | strong_accumulation | 1.57 | 1.26 | 3 | 2 | 2.85 | 3.21 | -5.48 | 18 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 0.85 | 1.29 | 1.0 | 4.12 | 13.83 | 13.83 | False |  | strong_accumulation | 1.43 | 1.44 | 3 | 3 | 1.3 | 1.12 | -10.27 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | 11.82 | 21.73 | 15.4 | 83.76 | 45.34 | 87.03 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.08 | 1.23 | 3 | 3 | 10.92 | 11.02 | -3.35 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | 8.44 | -5.17 | -6.03 | 34.91 | 14.22 | 36.34 | False |  | distribution_warning | -0.04 | -0.02 | 1 | 0 | 0.63 | -0.78 | -41.79 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 1.21 | -9.98 | -11.75 | 16.5 | 10.78 | 17.55 | False |  | distribution_warning | -0.71 | -1.56 | 1 | 0 | -5.06 | -3.5 | -20.81 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 1.72 | -1.26 | -11.94 | 5.36 | 3.51 | 6.79 | False |  | distribution_warning | -0.88 | -1.69 | 0 | 0 | -0.92 | -1.51 | -27.61 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | -2.49 | 0.18 | 21.24 | 76.77 | 70.19 | 86.39 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.19 | -3.17 | 1 | 1 | -3.5 | -1.24 | -14.11 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 25.97 | 42.65 | 8.99 | 168.45 | 100.14 | 167.46 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.99 | 1 | 1 | 32.53 | 28.95 | 0.0 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 9.29 | 9.98 | 37.43 | 55.26 | 72.21 | 72.21 | True | 距60日低點反彈>50% | mild_accumulation | -0.77 | 0.44 | 1 | 2 | 3.4 | 6.4 | -3.48 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 0.84 | -6.98 | 0.0 | 4.8 | 9.59 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.32 | -0.28 | -36.51 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 84.97614765538744 | 32.40539437293427 | 5.47 | -1.95 | 8.23 | 45.12 | 17.49 | 38.05 | False |  | mild_accumulation | -0.61 | 0.45 | 1 | 2 | 1.82 | 0.92 | -22.15 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 0.82 | -6.94 | -25.75 | 2.49 | 9.2 | 9.2 | False |  | distribution_warning | -0.54 | -0.14 | 1 | 1 | -1.89 | -2.46 | -26.55 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 0.24 | -8.37 | -15.79 | 26.06 | 3.35 | 25.68 | False |  | distribution_warning | -2.0 | -2.72 | 0 | 1 | -2.79 | -3.44 | -29.97 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 7.85 | 4.83 | -3.74 | -8.04 | 14.44 | 14.44 | False |  | mild_accumulation | -0.33 | 0.14 | 1 | 1 | 5.36 | 3.37 | -12.53 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 20.71 | 0.0 | 8.41 | 85.6 | 77.64 | 95.95 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.2 | 0.71 | 2 | 2 | 15.84 | 14.68 | -5.69 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | 5.83 | 2.61 | -17.48 | 9.01 | 18.59 | 18.59 | False |  | mild_accumulation | 0.59 | 1.31 | 1 | 3 | 2.97 | 2.7 | -20.94 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 7.74 | 12.89 | 4.83 | 43.65 | 66.06 | 66.06 | True | 距60日低點反彈>50% | mild_accumulation | 0.33 | -0.32 | 2 | 1 | 7.78 | 8.59 | -0.73 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | 0.0 | -10.32 | -19.87 | 43.79 | 19.71 | 41.57 | False |  | distribution_warning | -1.08 | -0.92 | 0 | 1 | -3.39 | -3.5 | -26.74 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 5.22 | 7.34 | -6.85 | -14.47 | 30.0 | 30.0 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 3.1 | 4.17 | -10.28 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 24.09 | 60.24 | 75.43 | 238.6 | 131.78 | 244.33 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.75 | -2.07 | 0 | 0 | 32.88 | 30.21 | -9.96 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -1.85 | -14.29 | -11.42 | 40.71 | 18.66 | 40.71 | False |  | distribution_warning | -0.14 | -0.09 | 1 | 0 | -5.61 | -4.03 | -16.54 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 8.01 | 24.3 | 5.7 | 54.51 | 104.83 | 104.83 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.57 | 1 | 1 | 8.14 | 10.22 | -8.34 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -6.06 | -1.2 | 36.67 | 206.13 | 63.3 | 210.27 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.0 | 0.0 | 2 | 1 | 0.17 | -0.06 | -21.26 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | -1.64 | -1.1 | 13.56 | 35.85 | 29.5 | 36.88 | False |  | strong_accumulation | 2.28 | 2.23 | 2 | 2 | -2.68 | -2.03 | -12.62 | 23 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 1.83 | -1.77 | 1.83 | 2.58 | 4.91 | 16.81 | False |  | mild_accumulation | 0.02 | 0.01 | 2 | 1 | -0.23 | -0.12 | -2.11 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | -3.67 | 11.89 | -3.17 | 13.98 | 18.39 | 20.92 | False |  | distribution_warning | -1.24 | -0.21 | 0 | 2 | 7.15 | 5.36 | -7.32 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 3.52 | 1.73 | -16.71 | -8.7 | 4.26 | 4.26 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.94 | -0.69 | -21.39 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 35.9 | 36.9 | 73.07 | 215.82 | 164.09 | 225.63 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.15 | 1 | 2 | 30.68 | 29.76 | -1.81 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -3.88 | -9.41 | -2.26 | 79.62 | 57.58 | 84.07 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.72 | -5.07 | 1 | 0 | -6.17 | -2.8 | -20.37 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 22.33 | 11.97 | 86.88 | 51.18 | 114.38 | 128.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.94 | 1.54 | 0 | 2 | 12.1 | 15.64 | 0.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | 12.41 | -5.05 | -10.05 | 29.88 | 42.97 | 42.97 | False |  | distribution_warning | -1.44 | -1.22 | 1 | 1 | -1.96 | 0.47 | -23.19 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 17.29 | 16.71 | 22.19 | 16.13 | 38.87 | 38.87 | False |  | distribution_warning | -0.14 | -0.43 | 1 | 1 | 11.34 | 10.35 | -8.41 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 7.55 | 5.56 | 6.54 | 24.86 | 17.28 | 25.55 | False |  | mild_accumulation | -0.01 | 0.11 | 2 | 2 | 7.29 | 4.29 | -12.64 | 19 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | -0.51 | -14.1 | -9.97 | 0.51 | 1.29 | 1.29 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 1 | -8.19 | -6.78 | -17.95 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 4.28 | -4.88 | -10.14 | -14.47 | 13.9 | 13.9 | False |  | distribution_warning | -0.56 | -2.63 | 1 | 1 | -1.29 | -1.15 | -18.75 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 83.96056599949932 | 46.4979804114173 | 1.62 | 10.09 | -28.69 | -32.89 | 40.22 | 40.22 | False |  | distribution_warning | -0.86 | -0.99 | 1 | 1 | 2.07 | 3.16 | -32.71 | 14 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -4.86 | 8.81 | 26.79 | 11.37 | 30.57 | 43.43 | False |  | strong_accumulation | 0.49 | 0.49 | 3 | 3 | 0.0 | 0.97 | -6.43 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -1.52 | -1.52 | 6.93 | -22.3 | 10.77 | 10.77 | False |  | distribution_warning | -0.31 | -0.31 | 0 | 0 | -0.18 | 0.0 | -9.37 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround | D_降級_TDCC轉弱 | 53.94780686006835 | 20.455252439317967 | 5.46 | 1.2 | 6.62 | 11.0 | 11.74 | 15.36 | False |  | distribution_warning | -0.87 | -0.41 | 0 | 0 | 4.66 | 3.2 | -15.5 | 11 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround | B_可觀察 | 98.0452097433352 | 55.75153262414533 | -4.08 | 10.1 | 5.92 | 36.7 | 37.96 | 44.19 | False |  | mild_accumulation | 0.58 | 1.75 | 1 | 2 | -3.83 | -2.19 | -13.37 | 18 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | 0.45 | -3.45 | -12.33 |  | 1.82 |  | False |  | mild_accumulation | 0.09 | 0.02 | 3 | 1 | -2.28 | -3.34 | -23.81 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | 5.83 | 5.06 | 11.22 | 13.25 | 23.86 | 23.86 | False |  | distribution_warning | -0.2 | -0.45 | 1 | 0 | 3.43 | 4.08 | -1.58 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | -3.71 | 8.74 | -17.77 | 108.74 | 11.17 | 109.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | 0.0 | 3 | 0 | 3.13 | -0.38 | -33.15 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | 11.29 | 1.95 | 1.95 | 87.61 | 19.57 | 86.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.56 | 2.31 | 3 | 1 | 5.6 | 4.5 | -12.55 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 7.84 | -0.34 | -21.47 | -10.53 | 9.89 | 9.89 | False |  | distribution_warning | -0.14 | -0.75 | 1 | 0 | 3.88 | 2.96 | -24.35 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | 2.22 | 0.55 | -5.03 | -4.42 | 36.3 | 36.3 | False |  | distribution_warning | -0.7 | -0.14 | 1 | 1 | -3.22 | -1.24 | -14.22 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | -1.09 | -0.18 | 3.23 | 23.64 | 39.13 | 39.13 | False |  | mild_accumulation | 0.93 | -0.98 | 1 | 2 | -1.22 | -0.21 | -6.69 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | -5.67 | -2.35 | -1.77 | -10.72 | 58.57 | 58.57 | True | 距60日低點反彈>50% | distribution_warning | -4.15 | -1.63 | 1 | 0 | -3.9 | -0.94 | -12.14 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -2.28 | -10.46 | -31.39 | -18.39 | 19.56 | 19.56 | False |  | distribution_warning | -1.38 | -1.22 | 1 | 1 | -3.17 | -3.34 | -49.02 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 1.89 | -0.26 | 5.59 | 31.71 | 9.57 | 35.0 | False |  | mild_accumulation | 0.21 | -0.58 | 2 | 0 | 1.06 | 0.8 | -5.5 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | 2.07 | 0.45 | 3.02 | -11.73 | 4.47 | 8.56 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | 0.52 | 0.28 | -7.11 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 1.08 | 0.36 | 0.0 | -2.77 | 4.46 | 4.46 | False |  | strong_accumulation | 0.11 | 0.34 | 2 | 3 | 0.7 | 0.51 | -2.09 |  | fail_low_response_condition |