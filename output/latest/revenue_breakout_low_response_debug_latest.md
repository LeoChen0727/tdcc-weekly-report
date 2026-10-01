# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-01 19:37:22 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 737379 |
| tdcc_rows | 1967 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 402 |
| tdcc_mild_accumulation_count | 763 |
| tdcc_distribution_warning_count | 615 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 107 |
| already_priced_in_excluded | 44 |
| overheat_pass | 63 |
| score_pass | 63 |
| theme_priority_pass | 54 |
| final_rows | 54 |

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
| fail_low_response_condition | 253 |
| fail_already_priced_in | 44 |
| fail_defensive_or_traditional_excluded | 9 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | -0.68 | -6.71 | 3.18 | 1.04 | 35.19 | 46.29 | False |  | strong_accumulation | 0.79 | 0.88 | 2 | 2 | -0.17 | 1.79 | -11.52 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 93.04522686147229 | 122.05590293593936 | -0.47 | -4.11 | -2.33 | -13.93 | 11.82 | 11.82 | False |  | mild_accumulation | -0.06 | 0.76 | 1 | 3 | -1.78 | -1.49 | -16.0 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | -0.19 | 0.38 | -10.29 | -19.04 | 4.81 | 4.81 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 0.65 | 0.48 | -11.36 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | -0.5 | -2.91 | -14.16 | 13.38 | 5.37 | 12.61 | False |  | distribution_warning | -0.85 | -0.33 | 1 | 0 | -1.04 | -1.3 | -15.97 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 6.63 | 4.82 | -0.27 | 0.27 | 7.25 | 9.14 | False |  | strong_accumulation | 0.15 | 0.02 | 2 | 2 | 4.02 | 3.26 | -4.88 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | 0.42 | 1.57 | -3.66 | -11.25 | 4.11 | 4.11 | False |  | distribution_warning | -0.04 | -0.03 | 0 | 0 | 0.77 | 0.7 | -9.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | 0.46 | -2.68 | -1.8 | -25.21 | 6.6 | 14.14 | False |  | strong_accumulation | 0.12 | 0.13 | 3 | 3 | -0.05 | 0.03 | -10.84 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | -0.4 | -0.81 | -16.61 | -16.33 | 4.68 | 4.68 | False |  | mild_accumulation | 1.27 | -0.25 | 2 | 1 | 0.1 | -0.42 | -16.61 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 4.23 | 3.86 | 3.5 | 1.37 | 12.12 | 22.31 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 1 | 4.06 | 3.95 | -4.21 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 15.78 | 46.15 | 114.08 | 178.53 | 135.92 | 198.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.03 | 0.34 | 2 | 2 | 33.58 | 31.12 | 0.0 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 56.10735951141534 | 60.53884698622307 | 0.62 | -12.67 | -22.49 | 63.31 | 30.12 | 79.6 | False |  | distribution_warning | -0.83 | -1.0 | 0 | 0 | 0.81 | 0.65 | -23.94 | 11 | selected |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 5.66 | 17.52 | 10.34 | 96.15 | 81.52 | 109.74 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.85 | 11.08 | 2 | 2 | 12.21 | 10.53 | -10.4 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | 0.28 | -5.09 | -13.45 | -24.68 | 3.81 | 3.81 | False |  | mild_accumulation | 0.24 | -0.23 | 2 | 1 | -0.81 | -1.68 | -18.43 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 33032.925531914894 | 13849.620888036585 | -9.43 | -9.04 | 0.63 | 6.02 | 5.84 | 13.01 | False |  | distribution_warning | -0.06 | -0.19 | 1 | 1 | -6.57 | -5.41 | -16.14 | 13 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 11.95 | 9.77 | 4.46 | 21.65 | 25.45 | 31.31 | False |  | mild_accumulation | -0.27 | 0.01 | 1 | 1 | 10.59 | 9.06 | -6.33 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 38.17 | 65.49 | 96.09 | 128.18 | 126.81 | 146.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.97 | -0.99 | 3 | 1 | 44.43 | 39.94 | -5.88 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -6.59 | -16.36 | 52.02 | 244.04 | 73.03 | 244.04 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.55 | 0.42 | 1 | 2 | -5.86 | -4.75 | -21.54 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 4.69 | -5.3 | -9.15 | -22.77 | 6.35 | 6.35 | False |  | mild_accumulation | -0.54 | 0.07 | 0 | 1 | 2.45 | 0.3 | -19.76 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | -1.0 | -5.57 | -13.18 | -18.77 | 0.0 | 0.51 | False |  | distribution_warning | -0.45 | -0.69 | 0 | 0 | -2.52 | -3.25 | -18.21 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | -0.76 | 12.99 | -20.91 | 126.46 | 33.67 | 149.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.91 | -1.46 | 1 | 2 | 6.92 | 7.25 | -18.44 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | -0.49 | -0.81 | 4.24 | 15.41 | 10.04 | 16.29 | False |  | mild_accumulation | 0.64 | 0.01 | 1 | 1 | 0.99 | 0.61 | -13.28 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 3.24 | 1.27 | -1.09 | 13.73 | 8.69 | 23.64 | False |  | mild_accumulation | 0.03 | 0.02 | 1 | 2 | 3.01 | 2.5 | -3.19 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 6.41 | 5.68 | -10.92 | 157.62 | 41.55 | 171.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.99 | 0.0 | 1 | 1 | 6.95 | 5.73 | -11.6 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 3.17 | 109.48 | 45.13 | 251.7 | 140.86 | 309.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.85 | 5.23 | 2 | 3 | 27.67 | 23.22 | -14.62 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | 4.05 | 0.3 | -22.69 | 44.59 | 31.5 | 53.21 | False |  | mild_accumulation | 0.22 | -0.12 | 2 | 2 | 5.1 | 4.23 | -25.28 | 18 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 0.4 | -0.78 | 4.96 | 22.41 | 12.14 | 24.82 | False |  | strong_accumulation | 0.16 | 0.15 | 2 | 2 | 1.14 | 1.08 | -7.47 | 21 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | 5.43 | 5.99 | -40.1 | 86.96 | 31.87 | 107.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.27 | 1.25 | 2 | 2 | 8.21 | 6.5 | -41.27 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | 2.03 | 2.87 | 2.03 | 20.67 | 15.14 | 23.95 | False |  | strong_accumulation | 0.04 | 0.03 | 2 | 2 | 2.76 | 2.66 | 0.0 | 21 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | 2.54 | -1.22 | -16.26 | -14.79 | 31.81 | 31.81 | False |  | mild_accumulation | 0.28 | 0.18 | 1 | 1 | 0.71 | 0.15 | -19.6 | 23 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 5.26 | 2.27 | -1.64 | 99.56 | 53.85 | 114.8 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.27 | 2 | 2 | 3.31 | 3.26 | -6.74 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 59.42279854814421 | 61.86168160125982 | -0.78 | -13.83 | -28.17 | -3.55 | 7.34 | 7.34 | False |  | distribution_warning | -0.82 | -0.22 | 1 | 1 | -1.26 | -1.86 | -29.63 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 122.01643193808464 | 89.65916297833103 | 6.12 | 10.93 | 1.71 | 16.06 | 18.8 | 20.61 | False |  | mild_accumulation | 0.06 | -0.07 | 2 | 1 | 5.59 | 4.84 | -4.6 | 25 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -2.9 | -0.42 | -7.73 | -10.89 | 5.39 | 5.39 | False |  | mild_accumulation | 0.77 | -0.15 | 2 | 1 | -1.62 | -1.67 | -14.46 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -10.9 | -5.97 | -6.8 | 75.62 | 71.37 | 77.82 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.09 | 0.78 | 2 | 2 | -8.42 | -4.77 | -17.32 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 1.26 | -4.46 | 41.91 | 65.24 | 45.99 | 66.09 | True | 近60日漲幅>40% | distribution_warning | -0.41 | -0.36 | 1 | 1 | 0.14 | 1.62 | -6.31 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | -14.75 | 2.46 | -4.59 | 2.97 | 20.23 | 20.23 | False |  | distribution_warning | -0.73 | -0.48 | 1 | 1 | -4.83 | -4.48 | -18.11 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 81.06426064737752 | 92.59516265483826 | 0.5 | 17.67 | -11.27 | 24.95 | 36.79 | 36.79 | False |  | strong_accumulation | 0.87 | 0.73 | 2 | 2 | 11.32 | 9.22 | -13.3 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | 5.29 | -10.61 | -10.61 | -6.01 | 55.32 | 55.32 | True | 距60日低點反彈>50% | distribution_warning | -0.36 | -0.12 | 1 | 1 | 2.77 | 2.99 | -12.05 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | 0.55 | 2.65 | 9.51 | 32.08 | 18.11 | 36.23 | False |  | strong_accumulation | 1.77 | 1.44 | 3 | 2 | 3.19 | 3.12 | -8.33 | 23 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -2.34 | -2.34 | -11.64 | 8.27 | 19.71 | 19.71 | False |  | strong_accumulation | 0.16 | 0.13 | 2 | 2 | -1.34 | -0.78 | -13.25 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 129.84671742960728 | 95.18081273476336 | 2.37 | -11.79 | -9.13 | 30.58 | 26.59 | 33.74 | False |  | mild_accumulation | -0.11 | 0.06 | 2 | 2 | -3.29 | -3.25 | -23.11 | 21 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | 3.39 | 0.0 | 2.95 | 17.47 | 17.09 | 20.96 | False |  | mild_accumulation | -0.71 | 0.02 | 1 | 1 | -0.2 | 0.79 | -13.46 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 2.84 | 1.69 | 40.39 | 107.76 | 46.65 | 107.76 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.2 | 2 | 1 | 4.5 | 4.46 | -4.11 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 14.47 | 18.64 | -1.14 | 43.41 | 33.85 | 43.72 | False |  | strong_accumulation | 2.35 | 1.85 | 3 | 2 | 17.28 | 13.8 | -1.14 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 4.32 | 10.56 | -24.25 | -4.99 | 21.47 | 21.47 | False |  | distribution_warning | -0.5 | -0.44 | 1 | 1 | 11.33 | 7.85 | -25.94 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 4.43 | 0.19 | 23.42 | 145.39 | 61.18 | 160.8 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 0.85 | 2 | 2 | 2.88 | 2.93 | -8.79 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.19 | 1.72 | -13.78 | 18.09 | 3.7 | 19.69 | False |  | strong_accumulation | 0.19 | 0.12 | 3 | 3 | 0.92 | 0.39 | -21.42 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 245.59047432473767 | 22.17724035271652 | -0.68 | 14.37 | -0.17 | -17.0 | 32.05 | 32.05 | False |  | mild_accumulation | 0.08 | 0.37 | 1 | 2 | 3.96 | 4.59 | -5.22 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | 1.48 | 0.8 | -9.25 | 20.61 | 7.09 | 32.92 | False |  | strong_accumulation | 0.98 | 1.08 | 3 | 3 | 1.77 | 0.06 | -28.64 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 51.21457814625632 | 27.60777173513282 | 2.35 | 1.95 | -24.02 | 43.01 | 33.16 | 56.29 | False |  | mild_accumulation | 0.35 | 0.77 | 2 | 1 | 2.69 | 2.65 | -24.78 | 17 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 1.1 | 0.55 | -3.66 | -1.43 | 2.6 | 9.52 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 0.67 | 0.35 | -5.96 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | -5.7 | -7.77 | 15.84 | 113.95 | 31.32 | 119.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.01 | 0.0 | 0 | 0 | -0.37 | 1.37 | -30.73 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -0.25 | 9.32 | -8.9 | -4.55 | 24.69 | 24.69 | False |  | distribution_warning | -0.1 | -0.1 | 0 | 0 | -0.68 | 1.5 | -13.26 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.4659980905217 | 384.0048979178835 | 1.58 | -1.86 | 7.02 | 16.73 | 34.03 | 34.03 | False |  | mild_accumulation | -0.51 | 0.72 | 1 | 2 | 1.88 | 1.4 | -12.14 | 21 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | -0.18 | 4.2 | 61.54 | 98.55 | 114.12 | 114.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.84 | -2.52 | 1 | 0 | 1.9 | 5.51 | -7.46 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 1.16 | 5.15 | -22.53 | -13.31 | 13.33 | 13.33 | False |  | strong_accumulation | 0.41 | 0.15 | 3 | 3 | 3.37 | 2.5 | -23.5 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 1.57 | 4.88 | 14.5 | 160.43 | 63.98 | 165.8 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.76 | -8.56 | 0 | 0 | -0.12 | 1.75 | -13.62 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | 2.31 | -2.71 | 23.44 | 56.9 | 38.28 | 59.59 | False |  | distribution_warning | -3.54 | -0.68 | 1 | 1 | -0.02 | 1.81 | -13.3 | 18 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 60.72584163286522 | 83.37487145378931 | 2.84 | -12.98 | -17.1 | 6.47 | 26.28 | 26.28 | False |  | distribution_warning | -0.71 | 0.0 | 0 | 2 | -2.11 | -0.75 | -19.08 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 3.91 | 0.89 | -44.2 | 24.52 | 13.85 | 38.23 | False |  | distribution_warning | -1.68 | -0.62 | 1 | 1 | 4.93 | 2.87 | -45.48 | 12 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | -0.31 | 1.45 | -9.85 | -2.88 | 3.93 | 3.93 | False |  | strong_accumulation | 0.2 | 0.2 | 2 | 2 | 0.7 | 0.35 | -10.02 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 106.21354266385858 | 53.00526357886879 | 0.39 | 1.71 | -26.62 | -14.6 | 23.52 | 23.52 | False |  | strong_accumulation | 0.51 | 1.64 | 2 | 2 | 2.17 | 1.03 | -30.58 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -1.86 | -6.44 | -14.95 | -15.63 | 0.96 | 0.96 | False |  | distribution_warning | -0.55 | -1.0 | 1 | 0 | -3.29 | -3.19 | -14.6 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -1.72 | -6.23 | 5.54 | -0.35 | 11.28 | 18.18 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -1.84 | -1.13 | -8.92 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | -1.19 | 0.24 | -3.7 | 1.22 | 2.46 | 10.34 | False |  | strong_accumulation | 0.16 | 0.14 | 3 | 2 | -0.92 | -0.67 | -4.7 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | -1.31 | 1.56 | -9.2 | -4.96 | 15.08 | 15.08 | False |  | strong_accumulation | 0.22 | 0.2 | 3 | 3 | 0.67 | 0.13 | -20.95 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | 0.13 | -1.16 | -3.17 | -33.91 | 7.76 | 7.76 | False |  | distribution_warning | -0.04 | -0.13 | 2 | 1 | -0.67 | -0.71 | -8.5 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 81.22955024989892 | 63.44944538479019 | -1.71 | -2.0 | -15.69 | -10.28 | 1.88 | 1.88 | False |  | mild_accumulation | -0.12 | 0.01 | 1 | 1 | -1.19 | -1.57 | -17.12 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral |  | 139.52959372288657 | 105.3349499169469 | -2.65 | -1.5 | -10.87 | -29.11 | 0.33 | 0.33 | False |  | strong_accumulation | 0.19 | 0.44 | 2 | 2 | -1.92 | -2.02 | -11.3 |  | fail_low_response_condition |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | -4.58 | 1.87 | 14.94 | -0.84 | 19.59 | 23.56 | False |  | strong_accumulation | 1.41 | 1.0 | 3 | 2 | -2.18 | -1.21 | -9.69 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 0.0 | 1.58 | -1.39 | 3.51 | 13.67 | 13.67 | False |  | strong_accumulation | 0.75 | 1.39 | 3 | 3 | 0.59 | 0.5 | -10.39 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | -0.88 | 12.8 | 8.05 | 71.69 | 42.07 | 74.07 | True | 近120日漲幅>70% | strong_accumulation | 1.26 | 1.22 | 3 | 3 | 5.34 | 5.78 | -5.53 |  | fail_already_priced_in |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -3.79 | 2.63 | -5.58 | 3.25 | 12.89 | 28.28 | False |  | mild_accumulation | 0.01 | -0.02 | 2 | 0 | 0.03 | -0.71 | -42.47 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 2.57 | -12.06 | -9.8 | 11.78 | 13.04 | 14.78 | False |  | distribution_warning | -1.17 | -0.66 | 1 | 1 | -0.04 | -1.18 | -19.19 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 2.98 | 0.83 | -24.14 | 4.76 | 6.14 | 9.5 | False |  | distribution_warning | -0.17 | -1.65 | 1 | 0 | 1.79 | 1.25 | -24.61 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 0.9 | 0.9 | 28.31 | 80.13 | 74.53 | 91.16 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.05 | -3.62 | 1 | 1 | -1.25 | 0.8 | -11.91 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 26.79 | 61.54 | 30.74 | 168.37 | 131.09 | 175.41 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.24 | 5.29 | 2 | 2 | 36.65 | 30.3 | -4.55 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 3.54 | 2.93 | 31.46 | 50.97 | 74.19 | 74.19 | True | 距60日低點反彈>50% | distribution_warning | -1.07 | -0.58 | 0 | 1 | 4.02 | 5.6 | -2.5 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 2.94 | -4.3 | 1.66 | 12.39 | 11.87 | 32.43 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 4.68 | 1.73 | -35.19 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 84.97614765538744 | 32.40539437293427 | 1.2 | 0.11 | 6.68 | 37.39 | 19.95 | 40.09 | False |  | strong_accumulation | 0.02 | 0.98 | 2 | 2 | 3.58 | 2.08 | -20.52 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | -0.32 | -3.87 | -22.47 | -1.27 | 9.91 | 9.91 | False |  | distribution_warning | -0.85 | -0.78 | 1 | 1 | -0.54 | -1.5 | -23.24 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 2.29 | -4.18 | -15.87 | 25.07 | 5.34 | 24.89 | False |  | distribution_warning | -1.72 | -2.42 | 0 | 1 | 0.28 | -1.01 | -28.62 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | 3.66 | 8.42 | -2.97 | -7.41 | 18.06 | 18.06 | False |  | mild_accumulation | 0.2 | -0.1 | 1 | 1 | 7.27 | 5.23 | -9.77 | 20 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 8.48 | 25.13 | 32.5 | 96.6 | 86.06 | 100.5 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 0.91 | 2 | 2 | 18.49 | 14.32 | -1.22 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 143.33455025414924 | 69.46103918462916 | 4.01 | 6.25 | -13.2 | 12.05 | 23.87 | 23.87 | False |  | strong_accumulation | 1.56 | 2.16 | 2 | 3 | 6.54 | 5.88 | -13.66 | 22 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | -1.86 | 5.17 | 4.55 | 31.59 | 61.77 | 61.77 | True | 距60日低點反彈>50% | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 3.54 | 4.08 | -3.29 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth | A_優先追蹤 | 50.31333751338634 | 36.26105158634005 | 4.55 | -3.65 | -18.27 | 32.5 | 25.42 | 45.05 | False |  | mild_accumulation | -0.65 | 0.44 | 0 | 2 | 2.58 | 1.27 | -18.27 | 17 | selected |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 1.88 | 2.05 | -6.29 | -10.51 | 32.44 | 32.44 | False |  | mild_accumulation | 0.49 | 0.0 | 1 | 0 | 4.22 | 4.52 | -7.6 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 1.69 | 62.16 | 30.84 | 235.46 | 139.18 | 242.02 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.44 | -2.03 | 1 | 0 | 24.15 | 22.89 | -7.08 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -1.88 | -9.25 | -14.21 | 25.6 | 17.16 | 38.94 | False |  | mild_accumulation | 0.57 | 0.82 | 2 | 1 | -4.21 | -3.76 | -16.93 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 12.85 | 21.88 | 7.73 | 39.09 | 124.4 | 124.4 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.41 | 1.02 | 1 | 1 | 14.34 | 15.62 | 0.0 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | 2.97 | 15.91 | 41.49 | 131.83 | 67.85 | 111.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | 0.0 | 1 | 1 | 1.52 | 2.49 | -19.07 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | 5.54 | 4.67 | 20.57 | 43.23 | 37.05 | 44.87 | False |  | mild_accumulation | 0.05 | -0.17 | 1 | 1 | 2.24 | 3.23 | -7.52 | 24 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 0.0 | 0.0 | 3.32 | 1.82 | 5.66 | 17.65 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 0.57 | 0.55 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 22.86 | 40.44 | 16.97 | 36.82 | 45.65 | 48.76 | True | 近20日漲幅>25% | distribution_warning | -0.64 | -1.36 | 1 | 1 | 25.82 | 23.34 | 0.0 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | -1.34 | 2.43 | -20.05 | -9.23 | 4.61 | 4.61 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.96 | -0.28 | -20.91 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | -5.67 | 31.78 | 71.55 | 157.33 | 148.82 | 151.59 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | -0.31 | 2 | 2 | 15.59 | 13.88 | -7.55 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -2.09 | -17.6 | -0.96 | 49.06 | 56.06 | 75.77 | True | 距60日低點反彈>50% | distribution_warning | -5.69 | -4.98 | 0 | 0 | -3.52 | -2.88 | -21.13 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 17.92 | 16.82 | 107.08 | 65.46 | 129.93 | 145.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.72 | 1.35 | 1 | 2 | 15.98 | 15.88 | -3.98 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 273.61017160561573 | 13.583391933925409 | 1.35 | -11.93 | -10.68 | 17.29 | 43.16 | 43.16 | False |  | distribution_warning | -2.2 | -3.47 | 1 | 0 | -0.1 | 0.62 | -16.89 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 13.81 | 10.37 | 31.36 | 11.33 | 51.63 | 51.63 | True | 距60日低點反彈>50% | strong_accumulation | 0.91 | 0.27 | 2 | 2 | 18.37 | 14.59 | -4.84 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 5.31 | 18.41 | 8.18 | 22.05 | 22.43 | 27.96 | False |  | strong_accumulation | 0.97 | 1.03 | 3 | 3 | 8.73 | 6.82 | -8.81 | 21 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | 3.53 | -14.21 | -8.78 | 0.12 | 5.8 | 5.8 | False |  | distribution_warning | -2.41 | -2.45 | 0 | 0 | -1.04 | -1.08 | -14.3 | 18 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | 0.3 | -1.59 | -16.54 | -12.86 | 15.54 | 15.54 | False |  | distribution_warning | -0.67 | -2.29 | 1 | 2 | 0.73 | 0.23 | -15.47 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | 0.39 | -2.64 | -21.82 | -30.46 | 44.13 | 44.13 | False |  | mild_accumulation | 1.33 | -0.08 | 2 | 2 | 4.56 | 4.94 | -22.52 | 20 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -2.96 | -1.07 | 22.82 | 11.4 | 26.3 | 40.66 | False |  | strong_accumulation | 0.38 | 0.38 | 2 | 2 | -2.27 | -0.74 | -8.24 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -1.09 | 2.42 | 3.08 | -18.15 | 8.72 | 8.72 | False |  | distribution_warning | -0.28 | -0.28 | 0 | 0 | -1.68 | -1.51 | -11.05 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 15.69 | 15.16 | 8.67 | 6.82 | 24.3 | 28.33 | False |  | distribution_warning | -0.29 | -1.22 | 1 | 0 | 13.42 | 10.47 | -6.0 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround | D_降級_TDCC轉弱 | 98.0452097433352 | 55.75153262414533 | 2.37 | 3.04 | -0.42 | 22.74 | 46.6 | 46.6 | False |  | distribution_warning | -1.16 | -0.26 | 0 | 1 | 0.87 | 3.05 | -7.95 | 14 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | -1.1 | -5.68 | -19.13 |  | 1.82 |  | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | -1.28 | -2.37 | -23.81 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -1.16 | -0.7 | -0.23 | 11.49 | 21.31 | 21.31 | False |  | distribution_warning | -0.54 | -0.37 | 1 | 0 | 1.2 | 1.44 | -3.61 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | 1.02 | 6.81 | -21.78 | 98.01 | 10.99 | 101.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 1.9 | -0.01 | -33.26 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | -0.48 | 3.31 | -8.44 | 70.81 | 17.85 | 70.53 | True | 近120日漲幅>70% | mild_accumulation | 0.3 | 1.67 | 2 | 1 | 3.8 | 2.16 | -13.08 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 0.69 | 3.57 | -18.31 | -12.65 | 10.27 | 10.27 | False |  | distribution_warning | -0.33 | -0.82 | 1 | 0 | 4.04 | 2.41 | -18.77 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | 0.4 | -7.1 | -3.44 | -14.72 | 40.56 | 40.56 | False |  | mild_accumulation | 0.67 | -0.15 | 2 | 1 | 0.22 | 1.36 | -11.54 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | 0.0 | -1.45 | 4.21 | 25.93 | 39.13 | 39.13 | False |  | mild_accumulation | 0.75 | 1.26 | 1 | 2 | -1.05 | -0.24 | -6.69 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | 0.0 | -4.48 | 7.23 | -9.55 | 62.38 | 62.38 | True | 距60日低點反彈>50% | distribution_warning | -3.04 | 0.0 | 1 | 0 | -1.0 | 1.24 | -10.03 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | 0.66 | -5.56 | -44.95 | -37.84 | 21.96 | 21.96 | False |  | distribution_warning | -0.81 | -0.61 | 2 | 1 | 0.63 | -0.63 | -47.1 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | 0.53 | 0.26 | 1.88 | 14.8 | 7.65 | 31.03 | False |  | mild_accumulation | 0.14 | -0.58 | 1 | 0 | 1.77 | 1.42 | -5.0 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1699.2086400934063 | 1440.8138488925792 | -2.88 | 0.23 | 0.23 | -13.44 | 3.06 | 7.09 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 0 | -0.78 | -0.84 | -8.37 |  | fail_low_response_condition |