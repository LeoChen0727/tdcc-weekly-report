# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-17 19:38:27 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 721686 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 367 |
| tdcc_mild_accumulation_count | 755 |
| tdcc_distribution_warning_count | 643 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 115 |
| already_priced_in_excluded | 41 |
| overheat_pass | 74 |
| score_pass | 74 |
| theme_priority_pass | 59 |
| final_rows | 59 |

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
| fail_low_response_condition | 245 |
| fail_already_priced_in | 41 |
| fail_defensive_or_traditional_excluded | 14 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround |  | 89.22674829328686 | 20.162313431356427 | 0.0 | 27.23 | 6.79 | 12.41 | 38.43 | 49.8 | True | 近20日漲幅>25% | strong_accumulation | 1.06 | 1.17 | 2 | 3 | 5.45 | 6.6 | -9.39 |  | fail_already_priced_in |
| 1316 | 上曜 | 建材營造 | neutral |  | 93.04522686147229 | 122.05590293593936 | -3.62 | 0.0 | 2.9 | -12.7 | 13.42 | 13.42 | False |  | distribution_warning | -0.91 | -0.42 | 0 | 2 | -2.76 | -0.86 | -14.8 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | -1.34 | 0.98 | -6.02 | -23.13 | 3.21 | 3.21 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | -1.01 | -0.68 | -17.07 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | -0.5 | -3.37 | -12.61 | 18.79 | 5.9 | 20.79 | False |  | distribution_warning | -0.3 | 0.0 | 1 | 0 | -1.59 | -1.48 | -15.55 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 0.0 | -0.28 | -3.3 | -5.12 | 2.03 | 3.83 | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | -0.54 | -0.75 | -12.66 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | -1.41 | -0.99 | -9.44 | -12.5 | 2.64 | 2.64 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 1 | -0.91 | -1.14 | -10.94 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | -0.7 | -4.25 | -6.14 | -23.71 | 4.65 | 12.04 | False |  | mild_accumulation | -0.26 | 0.13 | 2 | 3 | -3.16 | -2.59 | -12.47 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | -0.4 | 0.82 | -17.73 | 8.85 | 4.68 | 4.68 | False |  | strong_accumulation | 0.08 | 0.16 | 2 | 2 | -0.16 | -0.15 | -20.65 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | -2.46 | 3.35 | -6.71 | -7.02 | 5.3 | 14.88 | False |  | distribution_warning | -0.34 | -0.36 | 1 | 1 | -0.7 | -0.71 | -10.03 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 21.67 | 41.75 | 101.64 | 137.29 | 104.52 | 141.29 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 0.74 | 2 | 2 | 21.01 | 23.46 | 0.0 |  | fail_low_response_condition |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 16.15 | 14.63 | 10.53 | 113.2 | 70.18 | 124.84 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.75 | 0.76 | 2 | 2 | 12.55 | 15.06 | -0.94 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | 1.69 | -7.69 | -6.98 | -15.89 | 5.57 | 5.57 | False |  | distribution_warning | -0.82 | -1.08 | 1 | 2 | -2.43 | -1.38 | -17.05 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 33032.925531914894 | 13849.620888036585 | -0.73 | -1.01 | 9.28 | 10.7 | 15.37 | 21.75 | False |  | mild_accumulation | 0.19 | 0.45 | 1 | 2 | -2.06 | -0.01 | -9.66 | 20 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | -0.4 | -1.59 | -10.18 | 8.33 | 10.27 | 15.42 | False |  | mild_accumulation | 0.73 | 0.0 | 2 | 0 | -2.47 | -1.04 | -13.64 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 57.69192058134775 | 20.405940800672543 | -0.63 | 7.55 | 21.76 | 46.88 | 41.57 | 54.1 | False |  | strong_accumulation | 1.79 | 2.01 | 3 | 2 | 1.69 | 4.41 | -2.89 | 18 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -2.42 | -11.71 | 63.82 | 255.86 | 79.75 | 287.85 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.17 | -1.49 | 1 | 0 | -7.66 | -2.17 | -18.5 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | -1.15 | -14.57 | -24.56 | -30.27 | 2.38 | 2.38 | False |  | distribution_warning | -0.49 | -0.03 | 0 | 1 | -6.44 | -5.91 | -26.5 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 84.20319969775788 | 156.5212859256626 | -0.16 | -7.61 | -3.34 | -15.58 | 1.68 | 2.88 | False |  | distribution_warning | -0.6 | -0.75 | 1 | 1 | -3.37 | -3.07 | -16.28 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | 1.13 | 22.32 | -3.82 | 122.45 | 25.61 | 164.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.3 | -0.83 | 1 | 1 | 9.19 | 7.28 | -27.65 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 0.83 | -4.85 | 11.36 | 24.97 | 12.38 | 26.4 | False |  | distribution_warning | -0.62 | 0.0 | 0 | 0 | -1.39 | 0.13 | -14.12 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | -0.64 | -3.89 | -10.95 | 13.19 | 5.28 | 19.77 | False |  | mild_accumulation | -0.02 | 0.01 | 1 | 1 | -0.47 | -0.22 | -11.59 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 4.62 | 2.2 | -11.95 | 149.72 | 34.55 | 157.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.17 | 0.0 | 1 | 0 | 3.23 | 3.47 | -23.92 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 41.04 | 104.52 | 39.59 | 241.51 | 111.28 | 259.6 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.67 | 2.0 | 2 | 2 | 56.07 | 47.06 | 0.0 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | -3.42 | 0.0 | -29.48 | 56.28 | 22.44 | 67.93 | False |  | mild_accumulation | 0.18 | -0.66 | 2 | 1 | -1.95 | -2.07 | -34.66 | 17 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | -0.2 | 1.62 | -2.15 | 27.16 | 10.6 | 32.19 | False |  | mild_accumulation | -0.01 | 0.04 | 1 | 1 | 0.28 | 0.01 | -8.74 | 20 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | -7.52 | -5.87 | -49.62 | 110.34 | 15.88 | 115.92 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.98 | -0.65 | 1 | 1 | -4.24 | -6.04 | -56.64 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | -1.02 | 2.11 | 1.46 | 30.73 | 11.24 | 34.35 | False |  | strong_accumulation | 0.1 | 0.11 | 2 | 2 | 0.45 | 0.71 | -3.19 | 21 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | -4.9 | -4.51 | -32.27 | -8.27 | 26.91 | 26.91 | False |  | mild_accumulation | -0.05 | 0.28 | 2 | 2 | -4.61 | -4.45 | -35.1 | 22 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | -5.29 | -3.68 | -17.07 | 82.6 | 45.3 | 102.86 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | -0.7 | 2 | 2 | -3.6 | -1.8 | -24.44 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 59.42279854814421 | 61.86168160125982 | -8.4 | -14.49 | -24.21 | 8.43 | 0.56 | 13.92 | False |  | distribution_warning | -0.64 | -0.49 | 1 | 0 | -10.56 | -10.63 | -36.28 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 122.01643193808464 | 89.65916297833103 | 0.79 | 2.87 | -3.03 | 15.48 | 11.46 | 15.78 | False |  | distribution_warning | -0.19 | -0.45 | 0 | 0 | 1.79 | 1.07 | -8.95 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral | B_可觀察 | 540.5590508718318 | 80.61133112104658 | 3.65 | 2.92 | 3.94 | -6.81 | 10.63 | 10.63 | False |  | mild_accumulation | 0.56 | -0.25 | 3 | 0 | 3.7 | 3.49 | -10.21 | 22 | selected |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | 1.06 | 29.7 | 9.43 | 129.95 | 91.94 | 140.89 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.4 | 6.75 | 3 | 3 | 3.88 | 6.41 | -7.39 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 51.16688342643828 | 42.30457002299758 | -4.15 | 3.83 | 22.96 | 67.2 | 49.29 | 73.94 | False |  | strong_accumulation | 0.42 | 0.16 | 3 | 2 | -1.74 | 0.73 | -7.96 | 19 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | -4.36 | -2.57 | -3.47 | 29.5 | 20.52 | 37.17 | False |  | distribution_warning | -0.12 | -0.04 | 2 | 2 | 0.02 | -1.12 | -16.27 | 18 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 81.06426064737752 | 92.59516265483826 | 0.57 | 3.73 | -23.55 | 11.02 | 19.41 | 19.41 | False |  | distribution_warning | -0.75 | -0.35 | 0 | 0 | 3.01 | 1.74 | -30.49 | 14 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | -9.09 | -7.32 | -24.3 | 0.42 | 34.75 | 34.75 | False |  | mild_accumulation | -0.41 | 0.01 | 1 | 2 | -9.94 | -8.21 | -28.84 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 1.0 | 3.2 | 4.72 | 53.02 | 13.78 | 59.91 | False |  | mild_accumulation | 0.2 | 0.27 | 2 | 1 | 1.04 | 1.05 | -11.69 | 21 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | 2.38 | 5.2 | -7.53 | 18.42 | 23.3 | 23.3 | False |  | strong_accumulation | 0.09 | 0.01 | 2 | 2 | 2.52 | 2.75 | -12.47 | 24 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.84671742960728 | 95.18081273476336 | -12.65 | -21.55 | -15.56 | 64.16 | 19.47 | 69.19 | False |  | distribution_warning | -1.1 | -0.4 | 0 | 1 | -13.1 | -12.03 | -27.43 |  | fail_low_response_condition |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | -10.3 | -5.04 | -11.32 | 32.76 | 11.34 | 40.24 | False |  | strong_accumulation | 0.83 | 1.11 | 2 | 3 | -6.05 | -5.96 | -17.71 | 18 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 4.1 | 1.93 | 44.88 | 107.25 | 51.43 | 116.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.63 | -0.1 | 0 | 1 | 1.38 | 2.5 | -5.64 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | -2.83 | -4.19 | -17.93 | 23.5 | 5.64 | 25.0 | False |  | distribution_warning | -0.04 | -0.41 | 2 | 1 | -2.35 | -3.04 | -28.97 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 86.10504037359958 | 114.852843965949 | -1.12 | -6.99 | -22.45 | -18.15 | 2.9 | 2.9 | False |  | distribution_warning | -0.68 | -1.27 | 1 | 0 | -3.29 | -4.45 | -42.11 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | -5.24 | -5.61 | 10.03 | 131.28 | 51.55 | 145.23 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.14 | -1.87 | 2 | 2 | -4.2 | -1.58 | -14.24 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.0 | 0.57 | -13.06 | 22.18 | 2.53 | 23.47 | False |  | strong_accumulation | 0.3 | 0.27 | 3 | 3 | 0.55 | -0.51 | -22.3 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 245.59047432473767 | 22.17724035271652 | 3.91 | 13.88 | -2.45 | -20.63 | 26.82 | 26.82 | False |  | distribution_warning | -0.3 | -1.04 | 1 | 0 | 6.19 | 5.76 | -8.22 | 17 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | -1.88 | -5.18 | -4.94 | 37.34 | 3.83 | 40.77 | False |  | strong_accumulation | 0.94 | 1.68 | 2 | 3 | -1.76 | -3.83 | -30.81 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | 1.6 | -4.68 | -16.28 | 63.67 | 29.85 | 74.91 | False |  | distribution_warning | -2.46 | -0.99 | 1 | 0 | 0.49 | 0.67 | -29.99 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | -0.18 | 0.37 | -14.08 | 1.67 | 2.04 | 8.93 | False |  | mild_accumulation | 0.15 | 0.04 | 2 | 1 | -0.15 | -0.32 | -9.11 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | -2.44 | 22.32 | 34.68 | 105.83 | 53.65 | 109.79 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 0.62 | 0.66 | -33.92 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -3.03 | 6.37 | -14.48 | -18.82 | 20.0 | 20.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.48 | -0.61 | -17.95 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 275.4659980905217 | 384.0048979178835 | -1.95 | -2.64 | -5.78 | 20.43 | 28.24 | 28.24 | False |  | distribution_warning | -0.28 | -0.25 | 1 | 2 | -4.57 | -2.7 | -15.93 | 15 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | 0.38 | 29.61 | 34.51 | 102.66 | 109.41 | 109.41 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.41 | 4.4 | 3 | 2 | 9.01 | 10.56 | -5.65 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | -5.83 | 1.93 | -28.06 | 14.12 | 7.78 | 17.58 | False |  | strong_accumulation | 0.32 | 0.06 | 3 | 3 | 0.18 | -1.03 | -30.71 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | -7.24 | -0.55 | 2.87 | 163.58 | 52.12 | 173.21 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | -1.38 | 1 | 1 | -6.58 | -3.93 | -19.87 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 383.2629286702524 | 200.70869091113056 | -2.73 | 3.72 | 13.63 | 70.55 | 32.34 | 73.2 | True | 近120日漲幅>70% | strong_accumulation | 1.36 | 2.41 | 2 | 2 | -4.91 | -2.92 | -17.02 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | -9.74 | -7.32 | -11.73 | 30.24 | 20.7 | 33.08 | False |  | distribution_warning | -0.18 | -1.02 | 2 | 1 | -9.46 | -7.42 | -22.77 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | -3.92 | -6.71 | -42.24 | 56.77 | 5.04 | 62.89 | False |  | distribution_warning | -0.96 | -0.99 | 1 | 1 | -4.3 | -6.2 | -57.27 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 1.04 | -0.1 | -10.57 | -0.51 | 3.29 | 3.29 | False |  | mild_accumulation | -0.33 | 0.27 | 2 | 3 | 0.37 | -0.04 | -11.87 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 106.21354266385858 | 53.00526357886879 | 1.49 | 0.81 | -29.51 | 9.65 | 20.0 | 20.0 | False |  | strong_accumulation | 0.34 | 1.6 | 2 | 3 | -0.07 | -0.33 | -32.55 | 22 | selected |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -3.82 | -6.96 | -11.93 | -5.31 | 2.64 | 2.64 | False |  | distribution_warning | -0.14 | -0.12 | 2 | 1 | -4.28 | -3.69 | -14.06 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -2.05 | -3.04 | 8.3 | 0.0 | 11.67 | 18.6 | False |  | distribution_warning | -0.15 | 0.0 | 1 | 0 | -3.29 | -1.09 | -8.6 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | -0.59 | 1.08 | 3.07 | 3.45 | 4.35 | 11.27 | False |  | strong_accumulation | 0.16 | 0.29 | 3 | 2 | 0.1 | 0.11 | -3.89 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | 0.61 | 3.0 | -6.84 | 1.95 | 17.2 | 17.2 | False |  | strong_accumulation | 0.1 | 0.06 | 2 | 2 | 3.69 | 2.38 | -19.5 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 51.50921763610771 | 59.40841445991509 | -0.26 | 0.13 | 0.26 | -32.76 | 10.01 | 10.01 | False |  | mild_accumulation | -0.11 | 0.39 | 1 | 3 | 1.05 | 1.09 | -6.59 | 18 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 81.22955024989892 | 63.44944538479019 | -1.1 | -3.24 | -9.03 | -6.45 | 2.81 | 2.81 | False |  | distribution_warning | -0.14 | -0.16 | 1 | 1 | -1.01 | -1.18 | -16.36 | 12 | selected |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | -0.85 | -2.19 | -7.78 | -23.9 | 2.3 | 2.3 | False |  | mild_accumulation | 0.08 | -0.29 | 2 | 0 | -0.82 | -0.76 | -10.43 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 58.75071504262123 | 38.71801301175803 | 2.48 | 2.06 | 17.94 | -9.39 | 29.67 | 29.67 | False |  | distribution_warning | -0.98 | -1.66 | 2 | 1 | 3.36 | 4.72 | -5.23 | 12 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 0.0 | -0.42 | 2.01 | 2.46 | 13.99 | 13.99 | False |  | strong_accumulation | 1.33 | 0.5 | 2 | 3 | 0.8 | 1.74 | -10.14 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -9.52 | -1.79 | -2.76 | 39.94 | 9.78 | 43.6 | False |  | distribution_warning | 0.0 | -0.01 | 2 | 0 | -2.54 | -3.99 | -44.05 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | -0.68 | -8.91 | -16.95 | 16.95 | 10.21 | 19.71 | False |  | distribution_warning | -0.15 | -1.77 | 2 | 0 | -7.39 | -5.33 | -21.22 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | -3.7 | -3.7 | -11.36 | 8.33 | 2.63 | 14.71 | False |  | distribution_warning | -1.05 | -1.93 | 0 | 0 | -2.03 | -2.93 | -28.22 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | -10.74 | 11.18 | 12.98 | 77.96 | 72.98 | 89.46 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.06 | 1.68 | 2 | 2 | -1.1 | 0.99 | -12.7 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 5.0 | 12.14 | -16.0 | 118.75 | 58.87 | 126.47 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.46 | 1.07 | 1 | 2 | 11.16 | 9.21 | -19.23 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | -7.95 | 6.7 | 25.89 | 50.95 | 58.06 | 58.06 | True | 距60日低點反彈>50% | mild_accumulation | -0.15 | 0.05 | 1 | 1 | -2.36 | -0.23 | -11.4 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 5.91 | -20.48 | -2.92 | -0.85 | 6.39 | 25.95 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.86 | -3.39 | -38.36 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 84.97614765538744 | 32.40539437293427 | 5.33 | -3.89 | 7.37 | 44.79 | 15.16 | 46.7 | False |  | distribution_warning | -1.69 | -0.08 | 0 | 2 | -0.4 | -0.34 | -23.69 | 14 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 87.95350944559226 | 95.60013434168664 | -1.93 | -7.28 | -23.05 | 21.23 | 8.14 | 22.2 | False |  | distribution_warning | -0.95 | -0.55 | 0 | 0 | -4.18 | -4.12 | -28.37 | 13 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | -0.59 | -7.83 | -16.4 | 28.22 | 3.85 | 31.86 | False |  | distribution_warning | -2.89 | -2.99 | 0 | 1 | -4.23 | -4.32 | -29.63 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 98.21291582397656 | 109.2004683088644 | 5.97 | -0.73 | -6.85 | -9.33 | 13.33 | 13.33 | False |  | distribution_warning | -0.99 | -0.27 | 1 | 1 | 4.91 | 3.77 | -13.38 | 13 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | -5.43 | -17.54 | 0.97 | 92.43 | 43.95 | 82.52 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.62 | 3 | 2 | -6.76 | -4.49 | -23.58 |  | fail_already_priced_in |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 143.33455025414924 | 69.46103918462916 | -2.18 | 0.22 | -27.23 | 1.13 | 12.81 | 12.81 | False |  | mild_accumulation | -0.34 | 0.99 | 1 | 3 | -1.17 | -1.32 | -27.93 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | -0.2 | 3.4 | -4.56 | 41.41 | 53.52 | 53.52 | True | 距60日低點反彈>50% | distribution_warning | -0.02 | -0.69 | 1 | 0 | 2.4 | 3.13 | -6.86 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 50.31333751338634 | 36.26105158634005 | -1.95 | -10.0 | -26.96 | 45.24 | 19.71 | 48.89 | False |  | distribution_warning | -0.73 | -1.66 | 0 | 0 | -5.25 | -4.65 | -28.1 | 11 | selected |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 1.24 | 8.14 | -13.48 | -23.15 | 26.89 | 26.89 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 2.63 | 3.32 | -15.53 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 0.63 | 48.39 | 61.16 | 175.21 | 83.37 | 185.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.92 | -1.18 | 0 | 0 | 16.9 | 14.34 | -19.9 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -3.29 | -3.87 | -15.89 | 51.64 | 20.52 | 55.29 | False |  | mild_accumulation | -0.46 | 0.91 | 1 | 1 | -6.05 | -3.69 | -19.05 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | -3.66 | 7.22 | 3.03 | 101.73 | 88.03 | 96.39 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 1.87 | 1 | 1 | 3.12 | 3.5 | -15.86 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -4.56 | 2.99 | 25.62 | 198.98 | 66.71 | 225.56 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.36 | 0.43 | 2 | 1 | 2.47 | 3.63 | -19.62 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 166.4840985505344 | 98.8701912579111 | 0.81 | 3.61 | 18.41 | 46.85 | 34.17 | 51.63 | False |  | distribution_warning | -0.65 | -0.91 | 1 | 1 | 1.44 | 1.36 | -9.47 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | -1.07 | -0.36 | 2.21 | 5.7 | 4.91 | 16.81 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -0.32 | 0.04 | -2.11 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 16.17 | 16.72 | -3.65 | 15.09 | 19.35 | 21.91 | False |  | mild_accumulation | -0.44 | 1.2 | 1 | 3 | 11.46 | 9.57 | -6.57 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | -3.08 | -1.74 | -23.92 | -14.24 | 0.35 | 0.35 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.41 | -3.74 | -25.33 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 4.42 | 15.45 | 33.2 | 176.01 | 104.72 | 180.78 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.78 | -1.19 | 0 | 1 | 8.82 | 11.09 | -1.66 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | 0.38 | -5.06 | -9.64 | 112.12 | 59.09 | 117.84 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.09 | -1.86 | 1 | 1 | -5.57 | -2.13 | -19.6 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | -7.51 | -4.37 | 47.12 | 35.57 | 79.1 | 91.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -1.06 | 2.51 | 0 | 3 | -4.62 | -0.59 | -12.14 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | -18.74 | -12.13 | -23.9 | 20.7 | 25.29 | 25.29 | False |  | distribution_warning | -0.07 | -1.69 | 1 | 1 | -14.73 | -12.58 | -32.69 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 53.99150153319462 | 40.00683620722877 | 4.15 | -10.67 | 0.25 | 15.52 | 19.29 | 19.29 | False |  | distribution_warning | -1.83 | -1.94 | 0 | 0 | -2.77 | -2.2 | -21.33 | 11 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 80.45926827221638 | 62.39086469044157 | 2.78 | 6.22 | 4.23 | 23.47 | 14.2 | 27.0 | False |  | distribution_warning | -1.05 | -1.36 | 1 | 1 | 5.23 | 3.33 | -14.94 | 14 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | -1.83 | -10.65 | -7.15 | 5.37 | 3.74 | 8.05 | False |  | distribution_warning | -0.57 | -0.39 | 2 | 2 | -8.47 | -6.76 | -15.97 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | -1.73 | -6.76 | -15.72 | -21.22 | 12.73 | 12.73 | False |  | mild_accumulation | 0.53 | -0.04 | 2 | 1 | -3.19 | -2.36 | -19.58 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | -6.69 | 8.22 | -33.98 | -34.17 | 32.4 | 32.4 | False |  | strong_accumulation | 0.01 | 0.48 | 2 | 2 | -1.52 | -2.12 | -36.46 | 20 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | 2.25 | 12.98 | 33.79 | 14.07 | 36.09 | 49.49 | False |  | strong_accumulation | 0.45 | 0.45 | 2 | 2 | 6.24 | 6.13 | -2.15 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | 0.31 | 1.56 | 5.52 | -25.46 | 11.11 | 11.11 | False |  | distribution_warning | -0.17 | -0.17 | 0 | 0 | 0.47 | 0.56 | -9.09 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 0.78 | -5.27 | 2.05 | 11.94 | 9.66 | 17.0 | False |  | distribution_warning | -2.65 | -1.56 | 0 | 0 | 0.06 | -1.01 | -19.12 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 98.0452097433352 | 55.75153262414533 | -2.73 | 11.3 | 5.71 | 76.05 | 42.9 | 78.76 | True | 近120日漲幅>70% | strong_accumulation | 1.41 | 1.84 | 2 | 3 | 2.44 | 1.91 | -10.27 |  | fail_already_priced_in |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -2.62 | -5.71 | -12.38 |  | 1.36 |  | False |  | mild_accumulation | 0.08 | 0.01 | 3 | 1 | -3.55 | -4.97 | -24.15 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | 4.93 | 5.97 | 11.81 | 16.71 | 21.02 | 21.02 | False |  | distribution_warning | -0.09 | -0.48 | 1 | 0 | 2.44 | 3.26 | -3.84 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 2.22 | -4.93 | -30.38 | 107.64 | 11.36 | 109.82 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 4.7 | 0.34 | -33.03 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | 8.76 | 3.73 | 1.48 | 79.44 | 17.85 | 93.61 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 5.0 | 5.0 | -13.81 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 0.73 | -3.51 | -21.65 | -17.42 | 4.56 | 4.56 | False |  | distribution_warning | -0.15 | -0.21 | 1 | 1 | -1.22 | -1.21 | -28.01 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | -4.04 | 3.95 | -18.67 | 8.39 | 36.3 | 36.3 | False |  | mild_accumulation | -0.56 | 0.11 | 2 | 2 | -2.13 | -0.9 | -19.56 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | -1.99 | 1.88 | -2.52 | 27.23 | 38.62 | 38.62 | False |  | mild_accumulation | 2.62 | -1.07 | 2 | 1 | -1.61 | -0.33 | -7.03 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 0.0 | 10.54 | -5.21 | -2.26 | 64.76 | 64.76 | True | 距60日低點反彈>50% | distribution_warning | -4.27 | -1.28 | 0 | 1 | 1.76 | 3.72 | -8.71 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | -3.7 | -3.39 | -36.07 | -9.52 | 19.56 | 19.56 | False |  | distribution_warning | -1.43 | -0.61 | 1 | 1 | -3.78 | -4.23 | -49.02 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 3.29 | -0.53 | 4.43 | 33.22 | 9.28 | 36.1 | False |  | mild_accumulation | 0.89 | 0.0 | 3 | 0 | 0.73 | 0.92 | -5.75 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | -1.13 | -1.79 | 0.0 | -11.52 | 3.06 | 7.09 | False |  | distribution_warning | -0.02 | -0.02 | 1 | 0 | -0.76 | -0.64 | -8.37 |  | fail_low_response_condition |
| 5533 | 皇鼎 | 建材營造 | neutral |  | 189.42621733966743 | 8.811016014230672 | 0.0 | -0.36 | -0.36 | -3.81 | 3.35 | 3.35 | False |  | mild_accumulation | 0.15 | -0.1 | 2 | 2 | -0.16 | -0.15 | -3.14 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 88.58141426234812 | 67.0501740981801 | -0.13 | -8.03 | -6.06 | -5.46 | 2.34 | 2.34 | False |  | distribution_warning | -1.12 | -1.0 | 1 | 0 | -1.74 | -1.74 | -9.93 |  | fail_low_response_condition |