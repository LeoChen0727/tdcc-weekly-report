# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-30 19:34:07 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1971 |
| standardized_revenue_rows | 1971 |
| price_rows | 735422 |
| tdcc_rows | 1967 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 402 |
| tdcc_mild_accumulation_count | 763 |
| tdcc_distribution_warning_count | 615 |
| revenue_condition_pass | 360 |
| price_metrics_pass | 360 |
| low_response_pass | 101 |
| already_priced_in_excluded | 43 |
| overheat_pass | 58 |
| score_pass | 58 |
| theme_priority_pass | 49 |
| final_rows | 49 |

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
| fail_low_response_condition | 259 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 9 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 89.22674829328686 | 20.162313431356427 | 2.74 | -3.54 | -0.66 | 1.01 | 38.89 | 50.3 | False |  | strong_accumulation | 0.79 | 0.88 | 2 | 2 | 2.2 | 4.75 | -9.09 | 19 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 93.04522686147229 | 122.05590293593936 | 0.0 | -2.28 | -2.28 | -11.2 | 13.95 | 13.95 | False |  | mild_accumulation | -0.06 | 0.76 | 1 | 3 | -0.12 | 0.25 | -14.4 | 16 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 114.24269798253538 | 44.303500903674944 | 0.58 | -0.19 | -10.27 | -19.14 | 5.01 | 5.01 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 0.87 | 0.71 | -15.62 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 62.82977561740993 | 37.03689610523247 | 0.0 | -3.38 | -13.42 | 12.11 | 5.37 | 13.38 | False |  | distribution_warning | -0.85 | -0.33 | 1 | 0 | -1.19 | -1.41 | -15.97 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 123.52941176470588 | 19.955344683226347 | 4.56 | 3.38 | -0.54 | -1.61 | 6.38 | 8.26 | False |  | strong_accumulation | 0.15 | 0.02 | 2 | 2 | 3.42 | 2.72 | -8.93 |  | fail_low_response_condition |
| 1423 | 利華 | 紡織纖維 | defensive_or_traditional |  | 140.2441731409545 | 15.816278233211534 | 3.6 | 1.41 | -3.36 | -10.34 | 5.57 | 5.57 | False |  | distribution_warning | -0.04 | -0.03 | 0 | 0 | 2.27 | 2.18 | -8.4 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 41420.55214723927 | 68608.20344544708 | -3.64 | -5.58 | -6.0 | -26.31 | 3.42 | 10.73 | False |  | strong_accumulation | 0.12 | 0.13 | 3 | 3 | -3.16 | -2.95 | -13.5 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 100.43731041456016 | 51.53476314747586 | -0.4 | 0.4 | -14.09 | -13.79 | 6.38 | 6.38 | False |  | mild_accumulation | 1.27 | -0.25 | 2 | 1 | 1.69 | 1.16 | -19.35 |  | fail_low_response_condition |
| 1456 | 怡華 | 建材營造 | neutral |  | 6526.080375163244 | 344.8356865720742 | 1.03 | 5.4 | 3.9 | 1.03 | 10.98 | 21.07 | False |  | distribution_warning | -0.28 | -0.27 | 1 | 1 | 3.21 | 3.27 | -5.18 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 82.66667069773207 | 22.25561662215326 | 12.3 | 44.69 | 104.22 | 150.13 | 114.63 | 171.15 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.03 | 0.34 | 2 | 2 | 24.14 | 22.76 | -4.16 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 56.10735951141534 | 60.53884698622307 | 3.45 | -2.37 | -27.47 | 63.37 | 32.53 | 82.93 | True | 距120日低點反彈>80% | distribution_warning | -0.83 | -1.0 | 0 | 0 | 1.93 | 2.57 | -34.0 |  | fail_already_priced_in |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 62.67146732929334 | 26.36720246395244 | 5.83 | 9.11 | 17.58 | 87.61 | 76.66 | 104.12 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.85 | 11.08 | 2 | 2 | 10.13 | 8.6 | -12.8 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 81.67977762526685 | 69.18849391685958 | 0.56 | -3.76 | -10.28 | -23.67 | 4.99 | 4.99 | False |  | mild_accumulation | 0.24 | -0.23 | 2 | 1 | 0.04 | -0.72 | -17.51 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 33032.925531914894 | 13849.620888036585 | -11.84 | -7.18 | 4.11 | 5.85 | 5.68 | 12.83 | False |  | distribution_warning | -0.06 | -0.19 | 1 | 1 | -7.14 | -6.02 | -16.27 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 102.5304395876603 | 136.2137376977922 | 18.15 | 14.45 | 7.33 | 27.39 | 30.8 | 36.92 | False |  | mild_accumulation | -0.27 | 0.01 | 1 | 1 | 15.88 | 14.66 | 0.0 |  | fail_low_response_condition |
| 2030 | 彰源 | 鋼鐵工業 | cyclical_turnaround |  | 57.69192058134775 | 20.405940800672543 | 47.98 | 62.03 | 90.65 | 125.15 | 121.08 | 140.66 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.97 | -0.99 | 3 | 1 | 44.93 | 41.54 | 0.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 344.4151275890319 | 163.96140518937497 | -5.82 | -14.99 | 50.69 | 249.93 | 76.24 | 250.95 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.55 | 0.42 | 1 | 2 | -4.99 | -3.39 | -20.09 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 84.83502788539076 | 70.23367509463723 | 1.94 | -7.07 | -10.54 | -26.74 | 4.37 | 4.37 | False |  | mild_accumulation | -0.54 | 0.07 | 0 | 1 | 0.25 | -1.54 | -21.26 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 84.20319969775788 | 156.5212859256626 | -1.97 | -4.32 | -10.48 | -18.19 | 0.67 | 1.36 | False |  | distribution_warning | -0.45 | -0.69 | 0 | 0 | -1.98 | -2.72 | -17.52 | 13 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 106.4393510172547 | 34.09353678567797 | -2.59 | 25.24 | -20.18 | 128.7 | 34.7 | 151.67 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.91 | -1.46 | 1 | 2 | 8.41 | 8.79 | -22.42 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 62.42324416919225 | 51.12566058865302 | 1.32 | -2.08 | 6.98 | 15.23 | 9.86 | 16.54 | False |  | mild_accumulation | 0.64 | 0.01 | 1 | 1 | 0.78 | 0.5 | -13.42 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 726.0737499660993 | 14.577719626235568 | 2.07 | 2.89 | -2.74 | 14.08 | 9.03 | 24.03 | False |  | mild_accumulation | 0.03 | 0.02 | 1 | 2 | 3.4 | 3.05 | -3.32 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 87.72217512750316 | 37.96464139075741 | 1.93 | 1.93 | -13.46 | 147.93 | 36.99 | 162.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.99 | 0.0 | 1 | 1 | 3.79 | 2.85 | -20.91 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 239.98536640276163 | 113.21461801444438 | 16.84 | 128.62 | 77.06 | 283.8 | 167.32 | 354.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.85 | 5.23 | 2 | 3 | 46.59 | 39.7 | -5.24 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 61.18890785808584 | 40.59833569613409 | 6.41 | 4.08 | -25.06 | 40.08 | 30.71 | 52.29 | False |  | mild_accumulation | 0.22 | -0.12 | 2 | 2 | 4.48 | 4.0 | -26.39 | 18 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 51.978131522564816 | 39.72709766894786 | 0.6 | 0.6 | 4.57 | 21.2 | 11.04 | 23.59 | False |  | strong_accumulation | 0.16 | 0.15 | 2 | 2 | 0.11 | 0.18 | -8.38 | 21 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.799610560411935 | 34.94853667392253 | -1.62 | 0.55 | -47.56 | 75.64 | 20.04 | 89.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.27 | 1.25 | 2 | 2 | -1.19 | -2.48 | -48.06 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | A_優先追蹤 | 53.32005371471296 | 39.26370665798065 | 0.0 | 3.12 | 1.43 | 20.68 | 13.76 | 22.47 | False |  | strong_accumulation | 0.04 | 0.03 | 2 | 2 | 1.68 | 1.67 | -1.2 | 21 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | A_優先追蹤 | 218.53271706735816 | 149.1423915250992 | 2.08 | -2.78 | -14.04 | -21.22 | 33.44 | 33.44 | False |  | mild_accumulation | 0.28 | 0.18 | 1 | 1 | 1.89 | 1.41 | -19.41 | 23 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 289.42756449599915 | 177.3892901148317 | 3.16 | -1.64 | -2.71 | 91.98 | 53.42 | 114.2 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.27 | 2 | 2 | 3.15 | 3.28 | -10.25 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 59.42279854814421 | 61.86168160125982 | -3.53 | -12.78 | -35.1 | -6.08 | 0.28 | 0.28 | False |  | distribution_warning | -0.82 | -0.22 | 1 | 1 | -8.48 | -8.47 | -37.17 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 122.01643193808464 | 89.65916297833103 | 5.68 | 9.08 | 0.11 | 15.45 | 18.18 | 19.97 | False |  | mild_accumulation | 0.06 | -0.07 | 2 | 1 | 5.59 | 4.76 | -5.1 | 25 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 540.5590508718318 | 80.61133112104658 | -3.29 | 0.0 | -7.11 | -9.25 | 5.69 | 5.69 | False |  | mild_accumulation | 0.77 | -0.15 | 2 | 1 | -1.36 | -1.54 | -14.22 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 61.221187315428 | 32.46100185315033 | -11.63 | -10.11 | 0.72 | 69.92 | 68.55 | 77.12 | True | 距60日低點反彈>50% | strong_accumulation | 1.09 | 0.78 | 2 | 2 | -10.19 | -6.75 | -18.68 |  | fail_already_priced_in |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 51.16688342643828 | 42.30457002299758 | 1.59 | -3.8 | 42.37 | 65.69 | 45.39 | 65.69 | True | 近60日漲幅>40% | distribution_warning | -0.41 | -0.36 | 1 | 1 | -0.51 | 1.34 | -6.7 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 156.29654201767283 | 108.41049971158722 | -10.11 | 8.93 | -5.74 | 16.03 | 23.41 | 23.41 | False |  | distribution_warning | -0.73 | -0.48 | 1 | 1 | -2.2 | -2.35 | -15.94 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 81.06426064737752 | 92.59516265483826 | 0.17 | 15.66 | -16.29 | 22.74 | 33.41 | 33.41 | False |  | strong_accumulation | 0.87 | 0.73 | 2 | 2 | 9.47 | 7.41 | -18.14 | 20 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.38825024031777 | 71.24826737205954 | 7.18 | -3.86 | -14.18 | -2.61 | 58.87 | 58.87 | True | 距60日低點反彈>50% | distribution_warning | -0.36 | -0.12 | 1 | 1 | 4.48 | 5.63 | -16.1 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 98.42707910183296 | 55.23396713556208 | -2.58 | 0.14 | 5.91 | 36.05 | 14.9 | 33.77 | False |  | strong_accumulation | 1.77 | 1.44 | 3 | 2 | 0.52 | 0.6 | -10.82 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 177.453640698528 | 102.62669045483766 | -3.19 | -1.48 | -11.54 | 3.25 | 19.53 | 19.53 | False |  | strong_accumulation | 0.16 | 0.13 | 2 | 2 | -1.6 | -1.0 | -15.14 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 129.84671742960728 | 95.18081273476336 | 0.82 | -10.03 | -18.83 | 36.89 | 25.57 | 33.38 | False |  | mild_accumulation | -0.11 | 0.06 | 2 | 2 | -4.68 | -4.31 | -23.72 | 21 | selected |
| 2388 | 威盛 | 半導體業 | mainstream_growth | A_優先追蹤 | 77.39127929312332 | 39.64236861805114 | 4.73 | 0.41 | 2.53 | 28.52 | 16.61 | 26.08 | False |  | mild_accumulation | -0.71 | 0.02 | 1 | 1 | -0.61 | 0.45 | -13.81 | 19 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.51710391930136 | 45.88007993778177 | 2.83 | 7.24 | 39.35 | 111.05 | 47.26 | 110.13 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.2 | 2 | 1 | 5.03 | 5.32 | -3.71 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 59.050412994601615 | 71.61194957406076 | 14.16 | 21.7 | -4.44 | 40.98 | 32.31 | 42.23 | False |  | strong_accumulation | 2.35 | 1.85 | 3 | 2 | 17.01 | 13.93 | -4.44 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 86.10504037359958 | 114.852843965949 | 3.45 | 12.12 | -23.57 | -1.56 | 21.66 | 21.66 | False |  | distribution_warning | -0.5 | -0.44 | 1 | 1 | 12.1 | 8.79 | -25.83 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 560.8541425724004 | 638.1931640340957 | 0.58 | -4.42 | 26.74 | 135.91 | 61.18 | 160.8 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.13 | 0.85 | 2 | 2 | 2.89 | 3.21 | -8.79 |  | fail_already_priced_in |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 79.51753158995898 | 47.82374330893988 | 0.76 | 2.9 | -13.33 | 19.37 | 3.9 | 19.91 | False |  | strong_accumulation | 0.19 | 0.12 | 3 | 3 | 1.2 | 0.61 | -21.27 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 245.59047432473767 | 22.17724035271652 | -3.1 | 18.33 | 0.0 | -13.54 | 35.0 | 35.0 | False |  | mild_accumulation | 0.08 | 0.37 | 1 | 2 | 6.99 | 7.38 | -3.1 | 22 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 118.45737918391718 | 120.45013392296772 | -1.57 | 0.27 | -11.45 | 23.76 | 6.38 | 32.04 | False |  | strong_accumulation | 0.98 | 1.08 | 3 | 3 | 1.13 | -0.6 | -29.11 |  | fail_low_response_condition |
| 2428 | 興勤 | 電子零組件業 | mainstream_growth |  | 51.21457814625632 | 27.60777173513282 | -2.71 | -0.2 | -26.46 | 35.95 | 28.32 | 50.6 | False |  | mild_accumulation | 0.35 | 0.77 | 2 | 1 | -0.96 | -0.85 | -30.81 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 80.44201183191694 | 60.67525402355528 | 0.73 | 0.73 | -3.32 | -1.25 | 2.79 | 9.72 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 0.88 | 0.57 | -5.79 |  | fail_low_response_condition |
| 2434 | 統懋 | 半導體業 | mainstream_growth |  | 84.26308539944904 | 19.85682116089134 | 7.74 | 5.48 | 13.34 | 121.69 | 36.53 | 127.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.01 | 0.0 | 0 | 0 | 3.15 | 5.53 | -27.97 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 126.96455047850117 | 67.45512079557594 | -3.86 | 9.64 | -6.79 | -6.35 | 24.37 | 24.37 | False |  | distribution_warning | -0.1 | -0.1 | 0 | 0 | -0.51 | 1.38 | -13.48 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.4659980905217 | 384.0048979178835 | 1.05 | -1.87 | 9.89 | 15.83 | 33.8 | 33.8 | False |  | mild_accumulation | -0.51 | 0.72 | 1 | 2 | 1.61 | 1.36 | -12.29 | 21 | selected |
| 2455 | 全新 | 通信網路業 | mainstream_growth |  | 71.15939605853318 | 35.87422019326332 | -3.5 | 15.72 | 54.19 | 96.79 | 116.47 | 116.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.84 | -2.52 | 1 | 0 | 3.24 | 7.2 | -6.44 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 75.64976190094438 | 65.25316667122193 | 1.33 | 7.76 | -21.16 | -11.45 | 13.15 | 13.15 | False |  | strong_accumulation | 0.41 | 0.15 | 3 | 3 | 3.46 | 2.57 | -25.21 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 73.70780965783624 | 31.436497637078872 | 0.0 | 6.94 | 11.59 | 156.32 | 63.14 | 164.42 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -7.76 | -8.56 | 0 | 0 | -0.4 | 1.39 | -14.06 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 383.2629286702524 | 200.70869091113056 | -0.87 | -2.98 | 24.25 | 50.5 | 35.31 | 56.16 | False |  | distribution_warning | -3.54 | -0.68 | 1 | 1 | -2.3 | -0.21 | -15.16 | 17 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 60.72584163286522 | 83.37487145378931 | 2.47 | -12.07 | -12.36 | -1.64 | 25.35 | 25.35 | False |  | distribution_warning | -0.71 | 0.0 | 0 | 2 | -3.53 | -1.54 | -19.67 | 12 | selected |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 51.18935687397397 | 24.37989170066266 | 0.23 | -4.69 | -49.76 | 19.61 | 7.56 | 30.58 | False |  | distribution_warning | -1.68 | -0.62 | 1 | 1 | -0.82 | -2.56 | -50.92 | 11 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 50.050599201065246 | 28.65055233803744 | 0.21 | 0.72 | -10.2 | -2.3 | 3.72 | 3.72 | False |  | strong_accumulation | 0.2 | 0.2 | 2 | 2 | 0.57 | 0.18 | -10.53 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 106.21354266385858 | 53.00526357886879 | -0.13 | 1.83 | -24.61 | -4.99 | 24.96 | 24.96 | False |  | strong_accumulation | 0.51 | 1.64 | 2 | 2 | 3.45 | 2.3 | -29.77 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 60.17783541872381 | 37.18142647157366 | -2.76 | -5.59 | -12.99 | -13.88 | 1.2 | 1.2 | False |  | distribution_warning | -0.55 | -1.0 | 1 | 0 | -3.38 | -3.24 | -15.26 | 11 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 510.3268226648617 | 665.3996298068884 | -3.38 | -7.14 | 5.15 | 0.0 | 11.28 | 18.18 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -2.16 | -1.23 | -8.92 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 87.88742117627663 | 23.60389010735311 | -1.18 | 0.48 | -0.71 | 1.21 | 2.71 | 10.61 | False |  | strong_accumulation | 0.16 | 0.14 | 3 | 2 | -0.67 | -0.49 | -4.47 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 98.38295459889332 | -25.14735482235493 | -1.32 | -2.91 | -9.78 | -3.29 | 14.13 | 14.13 | False |  | strong_accumulation | 0.22 | 0.2 | 3 | 3 | -0.08 | -0.68 | -21.6 |  | fail_low_response_condition |
| 2543 | 皇昌 | 建材營造 | neutral |  | 51.50921763610771 | 59.40841445991509 | 0.26 | -3.27 | -1.79 | -33.04 | 8.6 | 8.6 | False |  | distribution_warning | -0.04 | -0.13 | 2 | 1 | 0.05 | 0.0 | -7.78 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 81.22955024989892 | 63.44944538479019 | -2.1 | -1.71 | -15.24 | -10.18 | 1.98 | 1.98 | False |  | mild_accumulation | -0.12 | 0.01 | 1 | 1 | -1.19 | -1.61 | -17.03 | 17 | selected |
| 2548 | 華固 | 建材營造 | neutral | B_可觀察 | 139.52959372288657 | 105.3349499169469 | -2.24 | -1.4 | -11.5 | -28.99 | 0.11 | 0.11 | False |  | strong_accumulation | 0.19 | 0.44 | 2 | 2 | -2.2 | -2.42 | -11.92 | 21 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | B_可觀察 | 58.75071504262123 | 38.71801301175803 | -4.69 | 0.57 | 15.42 | -1.93 | 20.1 | 24.08 | False |  | strong_accumulation | 1.41 | 1.0 | 3 | 2 | -1.67 | -0.9 | -9.31 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 85.48459503786516 | 17.912643295520123 | 1.7 | 4.22 | 0.56 | 5.6 | 15.27 | 15.27 | False |  | strong_accumulation | 0.75 | 1.39 | 3 | 3 | 2.09 | 1.97 | -9.13 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 109.8769286098819 | 217.3997425446664 | -1.22 | 14.23 | 9.06 | 78.83 | 42.57 | 78.55 | True | 近120日漲幅>70% | strong_accumulation | 1.26 | 1.22 | 3 | 3 | 6.35 | 6.72 | -5.19 |  | fail_already_priced_in |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 7187.402448021923 | 49.90881573724763 | -2.4 | 4.57 | 21.59 | 24.91 | 22.0 | 40.23 | False |  | distribution_warning | -0.08 | -0.2 | 1 | 1 | -0.04 | 0.9 | -3.68 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 218.9867410565063 | 159.2156506984672 | -3.05 | 5.17 | -6.95 | 13.36 | 13.11 | 28.54 | False |  | mild_accumulation | 0.01 | -0.02 | 2 | 0 | 0.35 | -0.58 | -42.36 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 59.309258699644346 | 42.13177453980629 | 2.55 | -12.46 | -7.5 | 11.03 | 14.18 | 15.93 | False |  | distribution_warning | -1.17 | -0.66 | 1 | 1 | 0.27 | -0.29 | -18.38 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 62.29746815925001 | 40.46530427736193 | 1.28 | 0.42 | -20.67 | 2.15 | 4.39 | 7.69 | False |  | distribution_warning | -0.17 | -1.65 | 1 | 0 | 0.15 | -0.31 | -26.99 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 605.2432014317565 | 324.37526455062414 | 0.35 | -2.22 | 35.22 | 78.19 | 77.64 | 94.56 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.05 | -3.62 | 1 | 1 | 0.55 | 2.67 | -10.34 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 57.78643473495075 | 34.73380056609053 | 40.25 | 64.08 | 24.72 | 177.96 | 132.46 | 181.2 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.24 | 5.29 | 2 | 2 | 41.14 | 34.79 | -3.98 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 54.340256925995845 | 76.09653467608655 | 0.59 | 0.29 | 24.46 | 48.7 | 70.47 | 70.47 | True | 距60日低點反彈>50% | distribution_warning | -1.07 | -0.58 | 0 | 1 | 1.95 | 3.87 | -4.58 |  | fail_already_priced_in |
| 3018 | 隆銘綠能 | 其他電子業 | mainstream_growth |  | 130.49163179916317 | -38.15147028595431 | 0.0 | 0.42 | 0.42 | 7.14 | 9.59 | 29.73 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.3 | -0.19 | -36.51 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 84.97614765538744 | 32.40539437293427 | -0.54 | 2.21 | 5.97 | 36.54 | 19.56 | 39.64 | False |  | strong_accumulation | 0.02 | 0.98 | 2 | 2 | 3.25 | 1.94 | -20.77 | 21 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 87.95350944559226 | 95.60013434168664 | 0.16 | -2.78 | -23.29 | -1.87 | 11.33 | 11.33 | False |  | distribution_warning | -0.85 | -0.78 | 1 | 1 | 0.54 | -0.37 | -24.49 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 56.83746008784256 | 35.66932938520228 | 1.67 | -4.38 | -15.48 | 23.66 | 5.84 | 28.7 | False |  | distribution_warning | -1.72 | -2.42 | 0 | 1 | 0.54 | -0.63 | -28.28 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 98.21291582397656 | 109.2004683088644 | -0.48 | 4.85 | -7.22 | -9.67 | 14.17 | 14.17 | False |  | mild_accumulation | 0.2 | -0.1 | 1 | 1 | 4.17 | 2.25 | -12.74 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 56.25723917867715 | 34.15926167073539 | 15.2 | 17.62 | 21.26 | 96.82 | 79.94 | 95.83 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.05 | 0.91 | 2 | 2 | 15.97 | 12.01 | -4.47 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 143.33455025414924 | 69.46103918462916 | 2.53 | 7.74 | -15.45 | 9.44 | 22.36 | 22.36 | False |  | strong_accumulation | 1.56 | 2.16 | 2 | 3 | 5.57 | 5.15 | -18.43 | 23 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 65.47995924001005 | 38.71624949635544 | 0.19 | 5.74 | 0.96 | 37.61 | 60.55 | 60.55 | True | 距60日低點反彈>50% | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 3.02 | 3.68 | -4.02 |  | fail_already_priced_in |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 50.31333751338634 | 36.26105158634005 | 1.17 | -5.83 | -19.72 | 32.56 | 22.8 | 42.03 | False |  | mild_accumulation | -0.65 | 0.44 | 0 | 2 | 0.25 | -0.72 | -22.6 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 75.61228823557171 | 358.9093907385123 | 1.89 | 2.59 | -7.62 | -16.1 | 32.0 | 32.0 | False |  | mild_accumulation | 0.49 | 0.0 | 1 | 0 | 3.98 | 4.6 | -8.9 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 108.2355516637478 | 8.08709676380926 | 11.44 | 73.86 | 37.38 | 243.44 | 138.61 | 241.21 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.44 | -2.03 | 1 | 0 | 26.87 | 25.21 | -7.3 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.786227791755 | 246.1253200193925 | -2.17 | -13.42 | -14.36 | 27.94 | 17.91 | 39.82 | False |  | mild_accumulation | 0.57 | 0.82 | 2 | 1 | -4.07 | -3.48 | -17.06 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.9786603130761 | 135.15148912145784 | 10.05 | 11.71 | 1.14 | 31.99 | 104.14 | 104.14 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.41 | 1.02 | 1 | 1 | 5.09 | 6.7 | -8.65 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 80.40598372488151 | 63.05454340558206 | -2.66 | 9.74 | 37.08 | 139.18 | 66.71 | 144.17 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | 0.0 | 1 | 1 | 1.54 | 2.03 | -19.62 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 166.4840985505344 | 98.8701912579111 | -1.07 | 3.65 | 16.04 | 35.16 | 32.73 | 40.3 | False |  | mild_accumulation | 0.05 | -0.17 | 1 | 1 | -0.75 | 0.28 | -10.44 | 23 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 307.0065719737121 | 83.54021703884372 | 0.0 | 1.45 | 2.94 | 0.72 | 5.66 | 17.65 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 0.57 | 0.6 | -1.41 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 104.3828563949176 | 15.60311433090802 | 8.89 | 26.7 | 6.35 | 25.15 | 32.42 | 35.26 | True | 近20日漲幅>25% | distribution_warning | -0.64 | -1.36 | 1 | 1 | 16.5 | 14.57 | -2.15 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 86.54643709940933 | 130.1290650876625 | -1.32 | 2.05 | -19.02 | -7.74 | 5.67 | 5.67 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.11 | 0.7 | -20.32 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 111.0204372171911 | 103.84182833494644 | 5.58 | 31.8 | 59.52 | 163.61 | 153.23 | 161.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.31 | -0.31 | 2 | 2 | 19.3 | 17.38 | -5.91 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 109.75810219812358 | 29.44255734638869 | -4.04 | -19.04 | -1.32 | 66.3 | 58.48 | 78.5 | True | 距60日低點反彈>50% | distribution_warning | -5.69 | -4.98 | 0 | 0 | -3.02 | -1.63 | -19.91 |  | fail_already_priced_in |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.90319995881175 | 42.93230357414348 | 17.44 | 13.52 | 98.83 | 70.0 | 127.42 | 142.86 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.72 | 1.35 | 1 | 2 | 15.69 | 16.29 | -5.03 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 273.61017160561573 | 13.583391933925409 | 2.05 | -8.22 | -19.57 | 16.87 | 42.21 | 42.21 | False |  | distribution_warning | -2.2 | -3.47 | 1 | 0 | -1.43 | 0.01 | -20.43 | 15 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 53.99150153319462 | 40.00683620722877 | 12.83 | 19.59 | 30.08 | 16.63 | 54.01 | 54.01 | True | 距60日低點反彈>50% | strong_accumulation | 0.91 | 0.27 | 2 | 2 | 20.89 | 17.95 | -3.35 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 80.45926827221638 | 62.39086469044157 | 0.0 | 14.46 | 3.64 | 18.13 | 17.28 | 22.58 | False |  | strong_accumulation | 0.97 | 1.03 | 3 | 3 | 5.04 | 2.97 | -12.64 | 20 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 119.89332334202707 | 52.56887075398791 | -0.63 | -14.27 | -12.86 | -3.76 | 2.19 | 2.19 | False |  | distribution_warning | -2.41 | -2.45 | 0 | 0 | -5.19 | -4.55 | -17.22 | 18 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 534.5730588954555 | 23.246721642333693 | -0.8 | -3.51 | -10.5 | -15.11 | 15.54 | 15.54 | False |  | distribution_warning | -0.67 | -2.29 | 1 | 2 | 0.65 | 0.25 | -17.58 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 83.96056599949932 | 46.4979804114173 | 6.75 | 4.98 | -26.45 | -32.17 | 41.34 | 41.34 | False |  | mild_accumulation | 1.33 | -0.08 | 2 | 2 | 2.39 | 3.37 | -27.51 | 20 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 187.52268077056712 | 14.20904000499167 | -3.14 | 0.18 | 23.06 | 10.12 | 25.85 | 40.15 | False |  | strong_accumulation | 0.38 | 0.38 | 2 | 2 | -2.67 | -1.17 | -8.57 |  | fail_low_response_condition |
| 4148 | 全宇生技-KY | 生技醫療業 | defensive_or_traditional |  | 51.949525200273904 | 26.60381039079264 | -2.29 | -1.23 | 3.9 | -19.29 | 9.4 | 9.4 | False |  | distribution_warning | -0.28 | -0.28 | 0 | 0 | -0.94 | -1.03 | -10.49 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround |  | 53.94780686006835 | 20.455252439317967 | 12.44 | 14.18 | 8.49 | 2.07 | 22.48 | 26.45 | False |  | distribution_warning | -0.29 | -1.22 | 1 | 0 | 12.61 | 9.9 | -7.38 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround | D_降級_TDCC轉弱 | 98.0452097433352 | 55.75153262414533 | 1.07 | 9.01 | 6.07 | 22.6 | 45.68 | 45.68 | False |  | distribution_warning | -1.16 | -0.26 | 0 | 1 | 0.38 | 2.68 | -8.53 | 14 | selected |
| 4582 | 聚恆-創 | 綠能環保 | neutral |  | 66.87285868493922 | 134.67269589515453 | 0.45 | -4.46 | -17.58 |  | 2.27 |  | False |  | mild_accumulation | 0.06 | 0.02 | 2 | 1 | -1.13 | -2.14 | -23.47 |  | fail_low_response_condition |
| 4771 | 望隼 | 生技醫療業 | defensive_or_traditional |  | 70.6377909701609 | 34.11983247770873 | -2.05 | -0.23 | -0.23 | 13.19 | 21.88 | 21.88 | False |  | distribution_warning | -0.54 | -0.37 | 1 | 0 | 1.63 | 2.04 | -3.16 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 105.4337738232811 | 38.99935957688426 | -5.17 | 4.63 | -22.66 | 94.37 | 9.31 | 98.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 0.69 | -1.52 | -34.27 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 82.95982513400992 | 61.84717333927541 | -0.95 | 4.1 | -9.57 | 78.08 | 18.99 | 77.17 | True | 近120日漲幅>70% | mild_accumulation | 0.3 | 1.67 | 2 | 1 | 4.99 | 3.36 | -12.24 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 192.98288508557457 | 163.62546217647647 | 3.46 | 5.65 | -18.08 | -7.14 | 13.69 | 13.69 | False |  | distribution_warning | -0.33 | -0.82 | 1 | 0 | 7.46 | 5.82 | -18.97 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 107.5919947488982 | 53.29791219386038 | -0.91 | -0.52 | -3.9 | -17.33 | 41.3 | 41.3 | False |  | mild_accumulation | 0.67 | -0.15 | 2 | 1 | 0.36 | 2.02 | -11.07 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 275.0567709273065 | 87.01658569617017 | -0.54 | -0.36 | 5.77 | 24.43 | 40.66 | 40.66 | False |  | mild_accumulation | 0.75 | 1.26 | 1 | 2 | -0.03 | 0.83 | -5.66 | 24 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 106.21752924846322 | 13.696101410482228 | -2.87 | -3.43 | 4.32 | -13.11 | 60.95 | 60.95 | True | 距60日低點反彈>50% | distribution_warning | -3.04 | 0.0 | 1 | 0 | -2.1 | 0.46 | -10.82 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 101.82935261463086 | 73.03671866545044 | 0.16 | -5.72 | -44.8 | -31.77 | 21.76 | 21.76 | False |  | distribution_warning | -0.81 | -0.61 | 2 | 1 | 0.17 | -0.85 | -48.09 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.09646994248528 | 35.380100629058546 | -3.42 | -1.61 | -0.81 | 7.0 | 3.97 | 26.55 | False |  | mild_accumulation | 0.14 | -0.58 | 1 | 0 | -1.7 | -1.92 | -8.25 |  | fail_low_response_condition |