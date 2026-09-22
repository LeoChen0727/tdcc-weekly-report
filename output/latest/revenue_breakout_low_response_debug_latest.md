# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-22 19:35:42 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 727575 |
| tdcc_rows | 1963 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 374 |
| tdcc_mild_accumulation_count | 723 |
| tdcc_distribution_warning_count | 652 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 96 |
| already_priced_in_excluded | 32 |
| overheat_pass | 64 |
| score_pass | 64 |
| theme_priority_pass | 51 |
| final_rows | 51 |

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
| fail_low_response_condition | 264 |
| fail_already_priced_in | 32 |
| fail_defensive_or_traditional_excluded | 12 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | 2.44 | 24.05 | 3.89 | 14.4 | 36.11 | 47.29 | False |  | mild_accumulation | 0.28 | 0.78 | 1 | 2 | 0.72 | 3.73 | -10.91 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 93.04522686147229 | 122.05590293593936 | 1.44 | -4.52 | 1.93 | -13.17 | 12.35 | 12.35 | False |  | mild_accumulation | -0.81 | 0.13 | 1 | 2 | -2.99 | -1.62 | -15.6 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 3.35 | -1.69 | -1.13 | -21.79 | 5.01 | 5.01 | False |  | mild_accumulation | 0.51 | 0.0 | 2 | 0 | 0.72 | 0.91 | -15.62 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 0.0 | -2.43 | -10.67 | 13.05 | 5.9 | 15.92 | False |  | mild_accumulation | 0.11 | -0.33 | 1 | 0 | -1.28 | -1.21 | -15.55 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | -1.14 | -2.53 | -2.8 | -8.92 | 0.58 | 2.36 | False |  | strong_accumulation | 0.07 | 0.02 | 2 | 2 | -1.71 | -1.87 | -13.9 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | 1.58 | -1.26 | -5.61 | -11.29 | 3.67 | 3.67 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | 0.19 | -0.02 | -10.05 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 2.36 | -2.69 | -5.24 | -22.64 | 6.11 | 13.61 | False |  | strong_accumulation | 0.14 | 0.15 | 3 | 3 | -1.54 | -1.25 | -11.25 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | 2.07 | -1.98 | -14.53 | -17.39 | 5.11 | 5.11 | False |  | strong_accumulation | 0.39 | 0.11 | 2 | 2 | 0.35 | 0.1 | -20.32 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 2.16 | 4.41 | -0.35 | 1.43 | 7.58 | 17.36 | False |  | distribution_warning | -0.18 | -0.2 | 2 | 2 | 0.85 | 1.01 | -8.09 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 29.44 | 36.15 | 115.73 | 155.99 | 115.22 | 157.42 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.14 | 2.68 | 3 | 3 | 24.8 | 25.33 | -3.06 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 17.65 | 16.1 | 20.45 | 110.32 | 71.8 | 113.28 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.09 | 7.42 | 2 | 2 | 11.04 | 12.27 | -3.2 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | -1.12 | -9.02 | -7.35 | -18.48 | 3.52 | 3.52 | False |  | distribution_warning | -0.81 | -1.37 | 1 | 1 | -2.96 | -2.75 | -18.66 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 33032.925531914894 | 13849.620888036585 | 6.06 | -3.71 | 17.06 | 12.36 | 18.24 | 24.78 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | 0.7 | 1.51 | -7.41 | 16 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 5.91 | -3.09 | -3.83 | 9.13 | 12.05 | 17.29 | False |  | mild_accumulation | -0.55 | 0.01 | 1 | 1 | -0.32 | 0.61 | -12.24 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 22.75 | 15.22 | 48.1 | 67.18 | 64.16 | 78.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.4 | -0.41 | 3 | 1 | 15.9 | 17.21 | 0.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | 8.15 | -11.31 | 78.2 | 282.2 | 85.23 | 289.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.87 | -0.02 | 0 | 1 | -3.35 | 0.65 | -16.01 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 0.39 | -14.09 | -15.79 | -27.68 | 1.59 | 1.59 | False |  | mild_accumulation | -0.56 | 0.09 | 0 | 2 | -4.83 | -5.35 | -23.35 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | -0.17 | -9.65 | -5.97 | -17.72 | 0.34 | 1.53 | False |  | distribution_warning | -0.93 | -0.97 | 0 | 0 | -3.29 | -3.65 | -17.38 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 10.85 | 28.14 | -1.13 | 155.34 | 34.7 | 152.88 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | -1.49 | 0 | 1 | 12.73 | 11.52 | -22.42 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 4.05 | -2.99 | 12.18 | 25.15 | 12.8 | 27.48 | False |  | mild_accumulation | 0.44 | 0.01 | 1 | 1 | 0.94 | 1.45 | -12.85 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 2.83 | -0.32 | -2.83 | 12.16 | 5.28 | 19.77 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 1 | -0.39 | -0.47 | -7.9 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 8.71 | 5.05 | -7.42 | 141.44 | 33.03 | 154.81 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.68 | 0.66 | 1 | 1 | 1.4 | 1.56 | -24.78 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 33.48 | 112.77 | 65.98 | 260.36 | 133.46 | 297.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.72 | 3.2 | 2 | 2 | 51.42 | 42.71 | -3.07 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | 3.55 | 2.88 | -23.57 | 63.61 | 26.38 | 62.12 | False |  | mild_accumulation | 0.32 | -0.71 | 2 | 1 | 1.1 | 1.22 | -29.3 | 18 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 2.64 | 4.12 | 2.64 | 25.56 | 11.7 | 27.78 | False |  | mild_accumulation | 0.07 | 0.06 | 1 | 1 | 0.85 | 0.94 | -7.83 | 20 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 6.33 | 4.96 | -45.1 | 110.31 | 25.08 | 109.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -0.78 | 1 | 1 | 3.1 | 1.55 | -53.2 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 53.32005371471296 | 39.26370665798065 | 3.14 | 2.5 | 3.8 | 26.15 | 12.84 | 27.46 | False |  | distribution_warning | -0.03 | -0.05 | 1 | 1 | 1.44 | 1.59 | -1.99 | 15 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 218.53271706735816 | 149.1423915250992 | 3.06 | -3.28 | -25.55 | -21.33 | 28.54 | 28.54 | False |  | distribution_warning | -1.14 | -1.2 | 1 | 1 | -3.0 | -2.79 | -27.38 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 7.21 | -4.47 | -15.76 | 78.87 | 46.15 | 104.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.1 | -3.77 | 1 | 1 | -2.69 | -1.41 | -18.76 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | 4.08 | -5.67 | -18.16 | 11.99 | 6.98 | 14.67 | False |  | distribution_warning | -0.62 | -0.71 | 1 | 0 | -3.59 | -3.35 | -32.21 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 1.58 | 3.69 | -1.75 | 10.85 | 11.96 | 13.65 | False |  | distribution_warning | -0.05 | -0.42 | 1 | 0 | 1.78 | 1.1 | -8.55 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | 3.28 | 3.42 | 1.54 | -9.03 | 8.53 | 8.53 | False |  | mild_accumulation | 1.06 | -0.22 | 3 | 0 | 1.33 | 0.95 | -11.91 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -5.17 | 19.55 | 20.76 | 102.12 | 92.34 | 109.21 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.96 | 3.36 | 3 | 3 | 1.16 | 5.01 | -7.2 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 2.69 | 3.03 | 35.56 | 69.57 | 50.08 | 70.18 | True | 距60日低點反彈>50% | mild_accumulation | -0.02 | 0.53 | 2 | 2 | -1.68 | 0.97 | -7.48 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 156.29654201767283 | 108.41049971158722 | 17.31 | 24.17 | 17.31 | 41.45 | 41.04 | 41.04 | False |  | distribution_warning | -0.74 | -0.06 | 1 | 2 | 14.39 | 12.48 | -3.94 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 19.88 | 19.64 | -12.23 | 24.46 | 36.12 | 36.12 | False |  | mild_accumulation | 0.38 | 0.11 | 1 | 1 | 15.03 | 13.04 | -20.55 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 76.38825024031777 | 71.24826737205954 | 7.0 | 7.11 | -9.96 | 4.21 | 47.52 | 47.52 | False |  | distribution_warning | -0.82 | -0.53 | 1 | 1 | -2.43 | 0.48 | -22.1 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 6.85 | 5.47 | 12.77 | 49.9 | 17.47 | 48.38 | False |  | strong_accumulation | 0.89 | 1.38 | 3 | 2 | 3.39 | 3.48 | -8.83 | 23 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | 2.7 | 4.11 | -6.81 | 11.22 | 22.58 | 22.58 | False |  | strong_accumulation | 0.37 | 0.36 | 3 | 3 | 1.1 | 1.57 | -12.98 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 129.84671742960728 | 95.18081273476336 | -4.99 | -13.14 | -10.83 | 53.31 | 23.66 | 52.83 | False |  | distribution_warning | -0.63 | -0.7 | 1 | 1 | -8.3 | -7.11 | -24.88 | 15 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | 2.16 | -1.39 | 0.28 | 29.85 | 13.26 | 33.77 | False |  | strong_accumulation | 0.15 | 0.61 | 2 | 2 | -3.96 | -3.17 | -16.29 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 2.63 | 4.93 | 48.78 | 101.72 | 47.38 | 107.07 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.36 | -0.63 | 1 | 0 | 2.97 | 3.94 | -3.3 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 10.14 | 6.54 | -16.18 | 26.11 | 16.92 | 28.09 | False |  | mild_accumulation | 0.1 | -0.56 | 2 | 1 | 7.07 | 5.72 | -18.28 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 16.44 | 6.36 | -20.79 | -7.67 | 16.44 | 16.44 | False |  | distribution_warning | -0.36 | -0.54 | 1 | 1 | 8.82 | 6.7 | -34.49 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 6.77 | -2.55 | 9.71 | 122.87 | 54.35 | 149.75 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.57 | -3.29 | 1 | 1 | -2.42 | -0.5 | -12.65 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 1.14 | 2.71 | -10.15 | 22.63 | 3.51 | 23.2 | False |  | strong_accumulation | 0.26 | 0.17 | 3 | 3 | 1.24 | 0.34 | -21.57 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | 9.96 | 18.9 | 6.56 | -20.84 | 32.95 | 32.95 | False |  | distribution_warning | -0.2 | -0.67 | 1 | 1 | 8.43 | 8.12 | -4.57 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 4.49 | -1.46 | -9.49 | 37.78 | 5.53 | 42.26 | False |  | strong_accumulation | 0.68 | 1.24 | 2 | 3 | -0.03 | -1.88 | -29.68 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.21457814625632 | 27.60777173513282 | 0.79 | 2.2 | -14.43 | 63.46 | 30.1 | 64.52 | False |  | distribution_warning | -0.49 | -0.05 | 2 | 0 | 0.29 | 0.42 | -29.85 | 12 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.92 | -0.91 | -2.15 | 2.25 | 1.49 | 8.33 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.63 | -0.74 | -6.98 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 12.48 | 27.78 | 68.86 | 129.21 | 67.8 | 132.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 8.66 | 10.34 | -26.54 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | 1.01 | 12.99 | -6.1 | -8.47 | 25.0 | 25.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.61 | 2.09 | -13.04 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | 4.4 | -4.68 | 3.64 | 14.92 | 31.94 | 31.94 | False |  | distribution_warning | -1.2 | -1.15 | 0 | 1 | -0.56 | 0.11 | -13.51 | 16 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 5.19 | 30.39 | 62.8 | 88.3 | 114.51 | 114.51 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.84 | 3.37 | 2 | 1 | 6.58 | 9.35 | -7.29 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 5.03 | 6.33 | -14.31 | 12.04 | 12.04 | 12.04 | False |  | strong_accumulation | 0.36 | 0.12 | 3 | 3 | 3.43 | 2.35 | -25.95 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 8.24 | -1.3 | 19.06 | 180.15 | 61.44 | 181.39 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.62 | -8.2 | 0 | 0 | -1.38 | 1.17 | -14.96 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | 1.79 | 1.9 | 29.4 | 52.6 | 35.16 | 58.71 | False |  | distribution_warning | -0.68 | -0.45 | 1 | 2 | -3.28 | -0.77 | -15.26 | 17 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | 2.33 | -1.31 | -7.21 | 17.59 | 22.79 | 22.79 | False |  | distribution_warning | -0.34 | -0.83 | 1 | 1 | -7.52 | -4.52 | -21.43 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 4.57 | -0.23 | -47.27 | 54.8 | 9.57 | 54.8 | False |  | distribution_warning | -1.04 | -0.07 | 1 | 1 | 0.05 | -1.47 | -55.43 | 12 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 1.66 | 1.55 | -9.24 | -0.81 | 4.25 | 4.25 | False |  | strong_accumulation | 0.26 | 0.26 | 3 | 3 | 1.24 | 0.78 | -10.07 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 106.21354266385858 | 53.00526357886879 | 5.49 | -0.65 | -22.79 | 14.09 | 23.04 | 23.04 | False |  | strong_accumulation | 0.29 | 1.52 | 2 | 2 | 2.15 | 1.63 | -30.85 | 23 | selected |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | 0.7 | -6.33 | -11.36 | -7.74 | 2.88 | 2.88 | False |  | distribution_warning | -0.52 | -0.45 | 1 | 1 | -3.15 | -2.88 | -13.86 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | 3.56 | -1.36 | 11.07 | 2.46 | 13.23 | 20.25 | False |  | distribution_warning | -0.2 | 0.0 | 0 | 0 | -1.95 | -0.08 | -7.32 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | 0.6 | 0.96 | 3.69 | 2.93 | 4.21 | 11.67 | False |  | strong_accumulation | 0.17 | 0.14 | 3 | 2 | 0.32 | 0.36 | -3.55 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | 4.21 | 6.22 | -6.6 | 3.45 | 16.61 | 16.61 | False |  | strong_accumulation | 0.16 | 0.04 | 3 | 2 | 2.24 | 1.33 | -19.9 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | 2.14 | -0.91 | -1.29 | -34.79 | 7.62 | 7.62 | False |  | mild_accumulation | -0.01 | 0.14 | 2 | 2 | -1.14 | -1.14 | -8.62 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | 2.68 | -1.0 | -9.55 | -7.44 | 3.65 | 3.65 | False |  | distribution_warning | -0.45 | -0.29 | 0 | 0 | -0.01 | -0.44 | -15.68 | 12 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | 2.95 | -2.18 | -8.0 | -25.75 | 3.06 | 3.06 | False |  | mild_accumulation | -0.47 | 0.05 | 1 | 1 | 0.24 | -0.13 | -9.33 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | 5.85 | 1.09 | 24.08 | -4.26 | 29.49 | 29.49 | False |  | strong_accumulation | 1.57 | 1.26 | 3 | 2 | 3.31 | 3.65 | -5.36 | 18 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 2.17 | -4.85 | 2.61 | 4.28 | 13.67 | 13.67 | False |  | strong_accumulation | 1.43 | 1.44 | 3 | 3 | 1.22 | 1.08 | -10.39 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | 10.49 | 23.16 | 13.12 | 71.9 | 43.32 | 84.44 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.08 | 1.23 | 3 | 3 | 10.47 | 10.59 | -4.69 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | 14.78 | 7.1 | 1.34 | 35.38 | 17.33 | 40.05 | False |  | distribution_warning | -0.04 | -0.02 | 1 | 0 | 3.08 | 1.85 | -40.2 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 3.0 | -10.72 | -11.13 | 16.6 | 10.21 | 16.95 | False |  | distribution_warning | -0.71 | -1.56 | 1 | 0 | -6.04 | -4.3 | -21.22 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 3.07 | -0.84 | -7.11 | 4.91 | 3.07 | 8.8 | False |  | distribution_warning | -0.88 | -1.69 | 0 | 0 | -1.41 | -2.06 | -27.91 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 5.49 | 3.15 | 24.61 | 73.52 | 72.98 | 89.46 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.19 | -3.17 | 1 | 1 | -1.9 | 0.26 | -12.7 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 20.45 | 36.88 | 9.05 | 145.83 | 82.26 | 148.13 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.83 | -0.99 | 1 | 1 | 23.12 | 20.6 | -7.34 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 8.83 | 14.92 | 47.39 | 52.02 | 68.24 | 68.24 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.77 | 0.44 | 1 | 2 | 1.49 | 4.55 | -5.7 |  | fail_low_response_condition |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 5.78 | -7.39 | -0.83 | 3.93 | 8.68 | 28.65 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.08 | -1.14 | -37.04 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 84.97614765538744 | 32.40539437293427 | 7.39 | -1.61 | 11.18 | 47.11 | 18.52 | 48.06 | False |  | mild_accumulation | -0.61 | 0.45 | 1 | 2 | 2.61 | 1.9 | -21.46 | 20 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 2.64 | -5.61 | -23.46 | 13.69 | 10.27 | 10.27 | False |  | distribution_warning | -0.54 | -0.14 | 1 | 1 | -1.3 | -1.74 | -26.96 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 1.59 | -9.79 | -15.06 | 25.23 | 2.98 | 26.76 | False |  | distribution_warning | -2.0 | -2.72 | 0 | 1 | -3.57 | -4.09 | -30.22 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 6.49 | 3.27 | -1.91 | -12.21 | 13.89 | 13.89 | False |  | mild_accumulation | -0.33 | 0.14 | 1 | 1 | 5.1 | 3.18 | -12.95 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 17.77 | 2.28 | 14.75 | 80.65 | 71.52 | 89.19 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.2 | 0.71 | 2 | 2 | 11.84 | 12.22 | -8.94 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | 7.97 | 6.52 | -11.57 | 7.73 | 19.1 | 19.1 | False |  | mild_accumulation | 0.59 | 1.31 | 1 | 3 | 3.54 | 3.39 | -20.6 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 9.89 | 16.41 | 7.91 | 45.68 | 64.83 | 64.83 | True | 距60日低點反彈>50% | mild_accumulation | 0.33 | -0.32 | 2 | 1 | 7.65 | 8.64 | -1.1 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | 2.23 | -9.17 | -18.02 | 41.46 | 19.95 | 44.49 | False |  | distribution_warning | -1.08 | -0.92 | 0 | 1 | -3.74 | -3.62 | -26.6 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 6.95 | 13.81 | -6.7 | -5.95 | 30.0 | 30.0 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 3.47 | 4.57 | -10.28 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 31.11 | 78.79 | 95.73 | 244.17 | 135.19 | 252.99 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.75 | -2.07 | 0 | 0 | 38.29 | 35.86 | 0.0 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | 0.95 | -11.11 | -11.6 | 40.35 | 19.4 | 44.14 | False |  | distribution_warning | -0.14 | -0.09 | 1 | 0 | -5.76 | -3.78 | -16.01 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 9.09 | 28.19 | 11.63 | 60.3 | 98.85 | 98.85 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.52 | 0.57 | 1 | 1 | 6.1 | 8.01 | -11.02 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -4.98 | -0.17 | 36.59 | 204.79 | 63.02 | 209.73 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.0 | 0.0 | 2 | 1 | -0.06 | -0.24 | -21.4 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | -1.1 | 1.12 | 16.83 | 37.79 | 29.86 | 38.85 | False |  | strong_accumulation | 2.28 | 2.23 | 2 | 2 | -2.46 | -1.94 | -12.38 | 23 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 1.82 | 0.0 | 1.45 | 3.7 | 5.66 | 17.65 | False |  | mild_accumulation | 0.02 | 0.01 | 2 | 1 | 0.39 | 0.59 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | -0.14 | 14.66 | 1.38 | 12.04 | 18.55 | 21.09 | False |  | distribution_warning | -1.24 | -0.21 | 0 | 2 | 7.91 | 6.02 | -7.2 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | 4.55 | 2.4 | -16.48 | -9.12 | 6.03 | 6.03 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.75 | 0.94 | -20.05 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 38.77 | 50.36 | 89.48 | 233.67 | 163.78 | 240.45 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.15 | 1 | 2 | 32.86 | 33.21 | 0.0 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | 6.8 | -1.31 | 4.16 | 93.74 | 59.39 | 93.38 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.72 | -5.07 | 1 | 0 | -5.54 | -1.93 | -19.45 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 9.79 | 12.01 | 75.6 | 45.39 | 94.98 | 108.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.94 | 1.54 | 0 | 2 | 2.57 | 6.7 | -4.35 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | 10.73 | -3.88 | -6.78 | 29.9 | 41.25 | 41.25 | False |  | distribution_warning | -1.44 | -1.22 | 1 | 1 | -3.38 | -0.69 | -24.11 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 13.38 | 8.19 | 19.41 | 12.81 | 33.23 | 33.23 | False |  | distribution_warning | -0.14 | -0.43 | 1 | 1 | 7.67 | 6.88 | -12.13 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 5.61 | 2.73 | 8.13 | 22.96 | 16.26 | 24.72 | False |  | mild_accumulation | -0.01 | 0.11 | 2 | 2 | 6.65 | 3.78 | -13.41 | 19 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | 2.19 | -13.24 | -8.22 | 0.0 | 2.19 | 2.19 | False |  | distribution_warning | -1.3 | -1.17 | 1 | 1 | -8.06 | -6.53 | -17.22 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 3.35 | -2.86 | -7.85 | -13.13 | 15.19 | 15.19 | False |  | distribution_warning | -0.56 | -2.63 | 1 | 1 | -0.43 | -0.14 | -17.83 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 83.96056599949932 | 46.4979804114173 | 7.53 | 17.35 | -22.59 | -33.93 | 43.58 | 43.58 | False |  | distribution_warning | -0.86 | -0.99 | 1 | 1 | 5.01 | 5.93 | -31.1 | 14 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -3.69 | 10.81 | 29.72 | 9.75 | 31.95 | 44.95 | False |  | strong_accumulation | 0.49 | 0.49 | 3 | 3 | 1.47 | 2.13 | -5.44 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -4.17 | 1.74 | 5.24 | -22.53 | 9.91 | 9.91 | False |  | distribution_warning | -0.31 | -0.31 | 0 | 0 | -1.02 | -0.77 | -10.07 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 3.5 | -0.15 | 6.56 | 11.88 | 7.44 | 13.84 | False |  | distribution_warning | -0.87 | -0.41 | 0 | 0 | 0.7 | -0.48 | -18.75 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround | B_可觀察 | 98.0452097433352 | 55.75153262414533 | 0.65 | 17.77 | 13.45 | 55.7 | 43.21 | 51.63 | False |  | mild_accumulation | 0.58 | 1.75 | 1 | 2 | 0.27 | 1.33 | -10.08 | 19 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | 2.26 | -3.0 | -7.55 |  | 2.95 |  | False |  | mild_accumulation | 0.09 | 0.02 | 3 | 1 | -1.36 | -2.56 | -22.96 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | 2.61 | 5.88 | 13.09 | 16.44 | 22.73 | 22.73 | False |  | distribution_warning | -0.2 | -0.45 | 1 | 0 | 2.73 | 3.51 | -2.48 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | -4.22 | 5.92 | -19.4 | 107.02 | 9.87 | 107.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | 0.0 | 3 | 0 | 2.34 | -1.58 | -33.93 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | 12.13 | 1.97 | 7.59 | 81.9 | 18.42 | 87.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.56 | 2.31 | 3 | 1 | 4.7 | 3.93 | -13.39 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 9.09 | 0.7 | -14.03 | -12.73 | 9.51 | 9.51 | False |  | distribution_warning | -0.14 | -0.75 | 1 | 0 | 3.5 | 2.88 | -24.61 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | 5.73 | 6.48 | -1.95 | 8.0 | 40.0 | 40.0 | False |  | distribution_warning | -0.7 | -0.14 | 1 | 1 | -0.56 | 1.33 | -11.89 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | 2.26 | -0.18 | 3.03 | 21.16 | 39.13 | 39.13 | False |  | mild_accumulation | 0.93 | -0.98 | 1 | 2 | -1.23 | -0.23 | -6.69 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 6.23 | 10.0 | 2.1 | -9.07 | 62.38 | 62.38 | True | 距60日低點反彈>50% | distribution_warning | -4.15 | -1.63 | 1 | 0 | -1.7 | 1.35 | -10.03 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | 4.12 | -0.33 | -23.55 | -12.41 | 21.16 | 21.16 | False |  | distribution_warning | -1.38 | -1.22 | 1 | 1 | -2.43 | -2.35 | -48.34 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 3.28 | 0.27 | 7.69 | 33.57 | 9.57 | 35.97 | False |  | mild_accumulation | 0.21 | -0.58 | 2 | 0 | 1.04 | 0.87 | -5.5 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | 3.92 | 1.81 | 5.37 | -10.87 | 6.12 | 10.27 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | 2.13 | 1.88 | -5.65 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 1.81 | 1.08 | 0.71 | -2.42 | 4.83 | 4.83 | False |  | strong_accumulation | 0.11 | 0.34 | 2 | 3 | 1.08 | 0.91 | -1.74 |  | fail_low_response_condition |