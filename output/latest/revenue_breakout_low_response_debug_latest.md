# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-11 19:36:58 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1954 |
| standardized_revenue_rows | 1954 |
| price_rows | 723743 |
| tdcc_rows | 1966 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 373 |
| tdcc_mild_accumulation_count | 730 |
| tdcc_distribution_warning_count | 658 |
| revenue_condition_pass | 358 |
| price_metrics_pass | 358 |
| low_response_pass | 120 |
| already_priced_in_excluded | 44 |
| overheat_pass | 76 |
| score_pass | 75 |
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
| fail_revenue_condition | 1596 |
| fail_low_response_condition | 238 |
| fail_already_priced_in | 44 |
| fail_defensive_or_traditional_excluded | 12 |
| fail_non_mainstream_score_lt_11 | 2 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | -1.71 | 20.59 | 8.3 | 3.99 | 32.87 | 43.79 | False |  | strong_accumulation | 0.5 | 0.92 | 2 | 3 | 5.48 | 4.29 | -13.03 | 18 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | -0.19 | 1.56 | -9.69 | -23.46 | 4.61 | 4.61 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | 0.43 | 0.27 | -15.94 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | -3.12 | -3.59 | -14.76 | 16.82 | 4.64 | 19.78 | False |  | distribution_warning | -0.41 | 0.0 | 1 | 0 | -3.14 | -3.38 | -17.93 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | -0.57 | -2.23 | -5.41 | -7.89 | 2.64 | 3.24 | False |  | mild_accumulation | 0.05 | 0.0 | 3 | 0 | -1.27 | -1.56 | -13.15 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -1.69 | -1.83 | -22.21 | -13.31 | 2.2 | 2.2 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 1 | -1.51 | -1.88 | -23.41 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | -4.69 | -3.83 | -5.32 | -27.38 | 4.4 | 11.78 | False |  | mild_accumulation | -0.28 | 0.11 | 2 | 3 | -4.34 | -4.03 | -12.68 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | -0.41 | 0.41 | -13.78 | 3.39 | 3.83 | 10.91 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | -0.91 | -1.39 | -22.29 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 2.5 | 3.61 | -5.28 | -2.71 | 8.71 | 18.6 | False |  | strong_accumulation | 0.07 | 0.06 | 2 | 2 | 3.02 | 2.47 | -9.18 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 6.47 | 19.28 | 72.79 | 100.55 | 73.62 | 103.37 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.74 | 1.27 | 2 | 2 | 5.76 | 9.11 | -3.98 |  | fail_already_priced_in |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | -5.39 | 19.31 | -4.58 | 84.55 | 45.22 | 91.86 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.89 | 2.48 | 3 | 3 | -2.76 | 0.05 | -15.47 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 33032.925531914894 | 13849.620888036585 | -0.72 | 5.51 | 6.33 | 10.77 | 16.39 | 22.82 | False |  | strong_accumulation | 0.35 | 0.49 | 2 | 2 | -1.15 | 0.12 | -8.86 | 22 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | -3.15 | -2.38 | -13.07 | 6.03 | 9.82 | 14.95 | False |  | mild_accumulation | 0.96 | 0.0 | 3 | 0 | -3.62 | -2.58 | -14.29 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 57.69192058134775 | 20.405940800672543 | 0.21 | 14.36 | 27.37 | 44.62 | 41.57 | 54.1 | False |  | strong_accumulation | 1.91 | 2.64 | 3 | 2 | 3.22 | 5.21 | -2.89 | 18 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -12.84 | -3.36 | 82.48 | 234.16 | 82.48 | 283.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -1.68 | 2 | 0 | -11.95 | -5.57 | -19.92 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | -6.62 | -16.72 | -27.64 |  | 0.4 | 0.4 | False |  | distribution_warning | -0.12 | -0.05 | 0 | 1 | -10.88 | -9.92 | -28.05 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 84.20319969775788 | 156.5212859256626 | -3.51 | -4.12 | -9.16 | -11.81 | 0.0 | 2.54 | False |  | distribution_warning | -1.08 | -0.94 | 1 | 1 | -5.01 | -4.93 | -16.55 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 8.7 | 25.94 | 6.38 | 142.13 | 28.04 | 169.54 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | 0.41 | 1 | 1 | 15.43 | 11.71 | -26.25 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | -3.58 | 2.24 | 5.33 | 18.72 | 9.61 | 23.28 | False |  | distribution_warning | -0.62 | -2.1 | 0 | 0 | -4.35 | -2.86 | -16.24 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 0.83 | -3.02 | -4.08 | 1.83 | 4.09 | 18.41 | False |  | distribution_warning | -0.02 | -0.04 | 1 | 0 | -2.34 | -2.19 | -12.71 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | -4.87 | -2.84 | -8.89 | 119.84 | 24.81 | 139.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -1.5 | 1 | 0 | -4.94 | -4.06 | -29.43 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 33.06 | 39.86 | 34.15 | 154.18 | 59.73 | 171.85 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.53 | -1.44 | 1 | 1 | 34.25 | 28.36 | -3.75 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 61.18890785808584 | 40.59833569613409 | 1.94 | -1.25 | -15.51 | 54.15 | 24.41 | 70.63 | False |  | distribution_warning | -0.58 | -2.3 | 1 | 0 | -0.78 | -1.21 | -36.42 | 12 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 51.978131522564816 | 39.72709766894786 | -3.12 | -4.43 | -8.82 | 23.69 | 9.49 | 32.27 | False |  | distribution_warning | -0.39 | -0.33 | 0 | 0 | -0.76 | -1.32 | -9.98 | 14 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | -3.2 | -12.54 | -44.72 | 107.63 | 19.17 | 123.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.13 | -3.89 | 0 | 0 | -3.06 | -5.25 | -55.41 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | B_可觀察_TDCC未確認 | 53.32005371471296 | 39.26370665798065 | 0.0 | 0.63 | 1.05 | 30.98 | 10.55 | 36.93 | False |  | neutral | 0.0 | 0.0 | 1 | 1 | -0.04 | -0.15 | -4.93 | 17 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 218.53271706735816 | 149.1423915250992 | -2.06 | -13.14 | -26.32 | -7.03 | 29.63 | 29.63 | False |  | distribution_warning | -2.88 | -2.48 | 1 | 1 | -3.6 | -4.16 | -38.02 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | -1.44 | -6.54 | -13.82 | 78.65 | 46.58 | 104.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.99 | -1.5 | 2 | 2 | -3.95 | -2.82 | -26.55 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 59.42279854814421 | 61.86168160125982 | -10.24 | -18.04 | -24.45 | 12.54 | 2.45 | 26.09 | False |  | mild_accumulation | 0.11 | -0.1 | 2 | 1 | -9.46 | -9.73 | -33.27 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 1.14 | -2.09 | -3.68 | 9.74 | 10.83 | 18.98 | False |  | distribution_warning | -0.37 | -0.53 | 0 | 0 | 1.69 | 0.75 | -9.46 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -2.5 | 1.01 | -9.41 | -11.13 | 5.24 | 5.24 | False |  | mild_accumulation | 0.11 | -0.05 | 2 | 1 | -1.13 | -1.61 | -14.58 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -2.3 | 36.84 | 30.0 | 135.89 | 88.71 | 148.14 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.6 | 6.42 | 3 | 2 | 8.48 | 8.92 | -5.65 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 51.16688342643828 | 42.30457002299758 | -9.85 | -7.23 | 15.07 | 60.98 | 45.51 | 69.54 | False |  | strong_accumulation | 0.45 | 1.39 | 3 | 3 | -3.92 | -1.96 | -10.29 | 17 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | A_優先追蹤 | 156.29654201767283 | 108.41049971158722 | 6.4 | -6.09 | -3.14 | 31.71 | 24.86 | 47.44 | False |  | mild_accumulation | 0.16 | -0.21 | 2 | 2 | 2.32 | 2.2 | -13.25 | 23 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 81.06426064737752 | 92.59516265483826 | -0.78 | -5.06 | -14.07 | 4.21 | 14.45 | 14.45 | False |  | distribution_warning | -1.0 | -0.73 | 0 | 0 | -1.24 | -2.71 | -33.38 | 13 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 76.38825024031777 | 71.24826737205954 | -1.44 | 1.48 | -24.82 | 12.2 | 46.1 | 46.1 | False |  | mild_accumulation | -0.02 | 0.87 | 1 | 3 | -3.33 | -2.57 | -26.43 | 17 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 98.42707910183296 | 55.23396713556208 | -3.32 | -12.2 | 0.43 | 49.46 | 11.86 | 57.56 | False |  | distribution_warning | -1.4 | -0.73 | 1 | 1 | -0.76 | -1.0 | -13.18 | 15 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -2.46 | 2.75 | -10.03 | 17.25 | 20.61 | 21.04 | False |  | strong_accumulation | 0.21 | 0.12 | 2 | 2 | 0.76 | 0.91 | -14.38 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.84671742960728 | 95.18081273476336 | -0.92 | -12.98 | 3.17 | 82.17 | 36.51 | 106.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.47 | 0 | 0 | -4.4 | -1.76 | -17.08 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -7.62 | -1.18 | 0.0 | 43.51 | 20.13 | 51.31 | False |  | mild_accumulation | 0.16 | 0.33 | 1 | 2 | 0.39 | -0.5 | -16.26 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | -5.2 | -1.32 | 37.97 | 98.82 | 48.79 | 114.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.49 | 0 | 1 | -0.27 | 1.68 | -7.29 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.050412994601615 | 71.61194957406076 | -6.07 | -10.67 | -21.48 | 11.05 | 3.08 | 22.41 | False |  | mild_accumulation | 0.1 | -1.29 | 2 | 1 | -6.16 | -6.61 | -30.69 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 86.10504037359958 | 114.852843965949 | -3.12 | -9.59 | -27.07 | -27.87 | 0.38 | 0.38 | False |  | distribution_warning | -2.62 | -2.47 | 0 | 0 | -5.73 | -7.22 | -42.55 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | -0.6 | -3.71 | 12.81 | 118.63 | 53.11 | 148.36 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | -2.37 | 2 | 2 | -4.32 | -1.83 | -13.36 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.95 | -0.56 | -12.69 | 22.26 | 3.31 | 24.41 | False |  | strong_accumulation | 0.44 | 0.49 | 3 | 3 | 1.38 | -0.07 | -21.71 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | -0.18 | 9.07 | -8.77 | -18.65 | 22.95 | 22.95 | False |  | distribution_warning | -0.35 | -0.75 | 1 | 0 | 5.1 | 3.88 | -11.02 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | -2.51 | -10.1 | -10.42 | 29.65 | 2.07 | 42.12 | False |  | strong_accumulation | 0.71 | 1.49 | 2 | 3 | -2.2 | -4.85 | -30.15 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 51.21457814625632 | 27.60777173513282 | -1.92 | 0.0 | -14.72 | 61.9 | 30.1 | 75.26 | False |  | mild_accumulation | -3.46 | 0.87 | 0 | 1 | 0.38 | 1.02 | -29.85 | 17 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.18 | -2.86 | -2.86 | -0.55 | 1.12 | 7.94 | False |  | mild_accumulation | 0.07 | 0.04 | 1 | 1 | -1.29 | -1.68 | -14.87 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | -10.55 | 17.12 | 64.93 | 107.23 | 62.7 | 111.23 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 4.53 | 1.64 | -33.7 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -13.01 | 3.25 | -12.61 | -15.33 | 19.06 | 19.06 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.08 | -1.4 | -18.94 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | -2.81 | -5.47 | -11.09 | 14.26 | 28.01 | 32.61 | False |  | distribution_warning | -0.62 | -1.36 | 1 | 1 | -5.22 | -3.98 | -16.08 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | -2.46 | 35.7 | 20.33 | 89.34 | 101.96 | 108.92 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.33 | 3.53 | 2 | 2 | 10.33 | 10.73 | -7.21 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 5.44 | 1.18 | -15.35 | 21.66 | 11.3 | 24.69 | False |  | distribution_warning | -0.04 | -0.05 | 2 | 2 | 3.75 | 1.72 | -28.45 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | -10.66 | -1.82 | 13.55 | 160.72 | 59.75 | 186.91 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.83 | 2.95 | 1 | 1 | -2.2 | -0.91 | -15.85 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | -9.27 | -6.15 | 10.02 | 66.05 | 33.53 | 78.22 | False |  | distribution_warning | -0.74 | -2.85 | 2 | 2 | -3.59 | -3.12 | -16.28 | 17 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 60.72584163286522 | 83.37487145378931 | -8.46 | 3.18 | -5.64 | 33.33 | 28.37 | 43.56 | False |  | mild_accumulation | 1.04 | -0.92 | 3 | 1 | -5.1 | -4.27 | -17.86 | 17 | selected |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | -5.11 | -12.86 | -41.59 | 68.77 | 7.56 | 73.58 | False |  | distribution_warning | -1.48 | -3.01 | 1 | 0 | -3.98 | -6.22 | -56.25 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.0 | -2.61 | -10.09 | 0.94 | 3.08 | 3.08 | False |  | mild_accumulation | -0.29 | 0.2 | 2 | 3 | -0.07 | -0.4 | -12.36 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 106.21354266385858 | 53.00526357886879 | 0.0 | -5.19 | -30.39 | 7.93 | 19.84 | 19.84 | False |  | strong_accumulation | 0.19 | 0.01 | 2 | 2 | -0.48 | -1.04 | -32.64 | 20 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 60.17783541872381 | 37.18142647157366 | -1.77 | -3.06 | -17.96 | -7.32 | 3.02 | 3.02 | False |  | mild_accumulation | -0.2 | 0.12 | 1 | 2 | -2.22 | -1.8 | -22.01 | 14 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -3.34 | 5.47 | 3.21 | 1.76 | 12.45 | 19.42 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -2.69 | -1.01 | -7.96 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | 0.24 | 2.42 | 3.17 | 4.06 | 5.1 | 12.07 | False |  | strong_accumulation | 0.01 | 0.16 | 2 | 2 | 1.09 | 0.74 | -3.21 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | 4.14 | 7.91 | -10.4 | 2.72 | 15.67 | 15.67 | False |  | strong_accumulation | 0.2 | 0.04 | 2 | 2 | 3.16 | 0.98 | -20.55 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 51.50921763610771 | 59.40841445991509 | -1.43 | -2.57 | -18.41 | -39.46 | 6.91 | 6.91 | False |  | mild_accumulation | -0.6 | 0.27 | 0 | 2 | -1.98 | -2.13 | -18.67 | 14 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 81.22955024989892 | 63.44944538479019 | -1.6 | -2.77 | -12.32 | -9.07 | 0.2 | 0.2 | False |  | mild_accumulation | -0.14 | 0.13 | 1 | 2 | -2.34 | -2.63 | -16.78 | 17 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | 0.32 | 1.71 | -12.13 | -22.53 | 2.26 | 2.26 | False |  | distribution_warning | -0.19 | -1.27 | 1 | 0 | 0.22 | -0.18 | -11.72 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 58.75071504262123 | 38.71801301175803 | 1.81 | 12.83 | 12.48 | -14.62 | 27.4 | 27.4 | False |  | distribution_warning | -1.19 | -1.52 | 1 | 1 | 2.0 | 3.7 | -6.89 | 12 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 2.59 | 5.48 | 0.99 | 4.25 | 14.47 | 14.47 | False |  | strong_accumulation | 1.53 | 1.55 | 2 | 3 | 1.11 | 2.39 | -9.76 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -0.78 | -1.17 | -0.39 | 38.04 | 10.92 | 48.97 | False |  | distribution_warning | -0.02 | -0.01 | 1 | 0 | -0.22 | -4.02 | -42.47 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | -12.98 | -14.67 | -14.93 | 12.43 | 7.75 | 18.01 | False |  | mild_accumulation | 1.21 | -0.89 | 3 | 1 | -11.74 | -9.91 | -22.97 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | -2.47 | -6.69 | -11.57 | 16.75 | 1.28 | 20.3 | False |  | mild_accumulation | 0.13 | -0.31 | 1 | 1 | -1.92 | -3.3 | -27.3 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 4.31 | 6.22 | 29.11 | 72.4 | 80.43 | 97.62 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.08 | 1 | 1 | 4.59 | 5.05 | -8.93 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 8.42 | 6.83 | -10.61 | 83.11 | 50.62 | 114.71 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.98 | -0.63 | 0 | 1 | 7.3 | 6.8 | -28.43 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | -5.6 | 4.17 | 42.49 | 48.13 | 67.25 | 73.26 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.28 | 0.56 | 1 | 2 | 4.14 | 5.58 | -6.26 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | -6.36 | -19.34 | -4.33 | -7.14 | 0.91 | 19.46 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -11.3 | -9.94 | -41.53 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 84.97614765538744 | 32.40539437293427 | -13.24 | -11.68 | -0.6 | 32.91 | 7.77 | 37.98 | False |  | distribution_warning | -2.54 | -1.49 | 0 | 2 | -8.19 | -7.82 | -28.58 | 13 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | -3.74 | -9.4 | -16.96 | 14.68 | 9.2 | 27.22 | False |  | distribution_warning | -0.58 | -0.48 | 0 | 0 | -4.73 | -4.84 | -27.67 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | -5.46 | -13.89 | -15.03 | 25.53 | 0.61 | 31.9 | False |  | distribution_warning | -3.17 | -2.2 | 0 | 1 | -6.63 | -6.93 | -30.05 | 11 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 98.21291582397656 | 109.2004683088644 | -0.78 | -9.05 | -14.73 | -15.86 | 6.11 | 6.11 | False |  | distribution_warning | -1.79 | -1.73 | 0 | 0 | -2.61 | -3.12 | -18.9 | 13 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 8.31 | -4.22 | -1.11 | 94.62 | 49.62 | 119.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.0 | 1.51 | 3 | 2 | -6.4 | -1.96 | -20.57 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | -3.43 | -3.43 | -22.41 | -2.17 | 13.07 | 13.07 | False |  | strong_accumulation | 0.36 | 0.12 | 2 | 2 | -1.15 | -1.97 | -30.77 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 3.99 | 4.1 | -11.03 | 42.7 | 55.35 | 55.35 | True | 距60日低點反彈>50% | mild_accumulation | 0.06 | -0.76 | 1 | 0 | 4.35 | 5.7 | -15.05 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 50.31333751338634 | 36.26105158634005 | -5.99 | -14.63 | -30.85 | 35.31 | 19.24 | 48.3 | False |  | distribution_warning | -0.99 | -1.53 | 0 | 1 | -7.88 | -7.03 | -33.51 | 10 | selected |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 1.45 | 15.35 | -17.4 | -13.85 | 24.44 | 24.44 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 2.03 | 1.78 | -18.37 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 16.6 | 33.19 | 78.0 | 165.01 | 78.0 | 177.88 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.16 | 0.76 | 0 | 1 | 20.35 | 16.55 | -23.13 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -6.07 | -0.91 | -15.58 | 43.17 | 21.27 | 62.5 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 1 | -5.58 | -4.83 | -21.88 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 3.11 | 22.67 | 2.6 | 136.91 | 90.56 | 148.65 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.65 | -6.2 | 0 | 0 | 6.65 | 6.13 | -14.73 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | 35.54 | 25.46 | 52.89 | 225.3 | 92.03 | 275.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.14 | -1.57 | 2 | 0 | 21.53 | 23.85 | 0.0 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 166.4840985505344 | 98.8701912579111 | -6.31 | -4.13 | 14.15 | 46.06 | 33.45 | 51.43 | False |  | distribution_warning | -0.81 | -1.08 | 1 | 1 | 0.98 | 0.68 | -9.95 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 0.72 | 0.36 | 3.32 | 4.09 | 5.66 | 17.65 | False |  | mild_accumulation | 0.14 | 0.01 | 2 | 1 | 0.32 | 0.44 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 9.55 | 8.53 | -11.17 | 7.69 | 12.9 | 15.32 | False |  | strong_accumulation | 0.58 | 1.29 | 2 | 3 | 8.76 | 7.67 | -15.05 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | -0.69 | -6.17 | -21.47 | -15.74 | 2.48 | 2.48 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.89 | -2.67 | -25.32 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 5.34 | 11.99 | 20.59 | 140.94 | 92.76 | 185.98 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -2.6 | 1 | 0 | 4.91 | 7.91 | -5.7 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -11.72 | 0.39 | -0.39 | 83.51 | 55.15 | 116.03 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.4 | 1.95 | 2 | 2 | -9.39 | -5.91 | -21.59 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | -1.87 | 18.74 | 44.49 | 46.32 | 92.81 | 105.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.45 | 2.36 | 1 | 3 | 2.84 | 7.27 | -5.41 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | B_可觀察 | 273.61017160561573 | 13.583391933925409 | -13.51 | -13.3 | -15.51 | 19.09 | 38.78 | 47.18 | False |  | mild_accumulation | 0.9 | -0.42 | 1 | 2 | -7.42 | -7.09 | -25.43 | 16 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | -12.59 | -14.77 | -10.29 | 3.88 | 11.28 | 11.28 | False |  | mild_accumulation | -0.62 | 0.28 | 1 | 1 | -11.2 | -10.01 | -26.61 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 80.45926827221638 | 62.39086469044157 | 2.4 | -7.39 | -0.47 | 11.99 | 9.57 | 23.12 | False |  | distribution_warning | -2.68 | -2.84 | 0 | 0 | 1.09 | -0.69 | -18.39 | 14 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth |  | 119.89332334202707 | 52.56887075398791 | -13.41 | -13.59 | -7.18 | 1.39 | 0.63 | 8.68 | False |  | strong_accumulation | 1.44 | 1.89 | 3 | 3 | -11.33 | -10.38 | -16.39 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | -4.78 | -4.78 | -16.42 | -20.25 | 11.8 | 11.8 | False |  | mild_accumulation | 0.15 | -0.68 | 2 | 0 | -5.42 | -4.5 | -20.58 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 83.96056599949932 | 46.4979804114173 | 4.24 | 6.03 | -30.11 | -33.51 | 37.43 | 37.43 | False |  | distribution_warning | -0.9 | -0.14 | 1 | 2 | 3.95 | 1.39 | -37.4 | 15 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | 3.92 | 10.0 | 34.49 | 10.63 | 36.21 | 47.22 | False |  | strong_accumulation | 0.25 | 0.25 | 2 | 2 | 7.16 | 7.22 | -0.68 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | 6.29 | 5.96 | 8.51 | -19.33 | 15.56 | 15.56 | False |  | distribution_warning | -0.1 | -0.1 | 0 | 0 | 5.51 | 5.91 | -3.57 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 1.56 | -14.15 | 2.69 | 9.26 | 10.0 | 17.36 | False |  | distribution_warning | -4.31 | -0.38 | 0 | 1 | -2.05 | -1.75 | -18.87 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | 1.68 | 9.5 | 20.4 | 76.0 | 49.38 | 89.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.87 | 0.28 | 2 | 2 | 8.8 | 7.26 | -6.2 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -3.4 | -10.98 | -12.69 |  | 2.71 |  | False |  | mild_accumulation | -0.15 | 0.01 | 2 | 1 | -3.2 | -5.26 | -22.79 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -3.36 | 1.77 | 8.04 | 5.5 | 14.49 | 14.49 | False |  | mild_accumulation | 0.07 | -0.49 | 1 | 0 | -2.26 | -1.85 | -9.03 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 0.35 | -9.19 | -28.38 | 82.48 | 6.7 | 101.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -0.64 | -3.61 | -37.17 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 82.95982513400992 | 61.84717333927541 | -3.08 | -11.04 | -4.46 | 63.15 | 7.89 | 77.26 | False |  | distribution_warning | -0.42 | -0.86 | 1 | 0 | -4.9 | -4.67 | -21.09 | 14 | selected |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | -3.6 | -6.29 | -22.99 | -24.93 | 1.9 | 1.9 | False |  | mild_accumulation | 0.08 | 0.3 | 2 | 1 | -4.76 | -4.98 | -29.84 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth | A_優先追蹤 | 107.5919947488982 | 53.29791219386038 | -1.67 | 9.44 | -11.66 | 19.53 | 41.67 | 41.67 | False |  | mild_accumulation | -0.44 | 0.22 | 2 | 2 | 1.7 | 1.98 | -16.39 | 22 | selected |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.0567709273065 | 87.01658569617017 | 1.63 | 2.0 | 2.0 | 22.22 | 43.48 | 43.48 | False |  | distribution_warning | -6.9 | -5.13 | 1 | 1 | 2.66 | 3.08 | -3.77 | 19 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | -5.41 | 21.53 | -2.23 | -12.28 | 66.67 | 66.67 | True | 距60日低點反彈>50% | distribution_warning | -0.95 | -2.3 | 1 | 1 | 4.99 | 5.67 | -10.03 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -1.64 | -7.25 | -25.43 | -8.8 | 19.96 | 19.96 | False |  | distribution_warning | -0.86 | -0.05 | 1 | 2 | -4.36 | -5.58 | -48.85 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | -4.5 | -4.24 | -5.5 | 28.01 | 4.64 | 31.75 | False |  | mild_accumulation | 0.78 | 0.0 | 3 | 0 | -4.19 | -3.72 | -9.75 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | -0.9 | 0.46 | -2.44 | -14.42 | 3.29 | 7.33 | False |  | distribution_warning | 0.0 | -0.02 | 1 | 0 | -0.69 | -0.86 | -8.16 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | -0.36 | 0.36 | -1.42 | -3.81 | 3.35 | 3.35 | False |  | mild_accumulation | 0.23 | -0.2 | 2 | 2 | -0.23 | -0.31 | -3.14 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | B_可觀察 | 88.58141426234812 | 67.0501740981801 | -3.39 | -6.68 | -13.15 | -3.9 | 0.54 | 1.79 | False |  | mild_accumulation | 0.25 | -0.18 | 2 | 1 | -3.81 | -3.44 | -15.43 | 18 | selected |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 98.63848944446872 | 32.20453750927072 | -2.86 | 45.71 | 45.3 | 138.32 | 84.12 | 167.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.38 | -0.77 | 2 | 2 | 1.68 | 4.66 | -14.86 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 118.48334266517357 | 55.91323881362982 | 8.7 | 6.38 | 3.09 | -18.92 | 36.36 | 36.36 | False |  | distribution_warning | -0.94 | -0.76 | 1 | 0 | 6.91 | 7.26 | -9.09 |  | fail_low_response_condition |