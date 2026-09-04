# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-04 19:36:34 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 713952 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 437 |
| tdcc_mild_accumulation_count | 765 |
| tdcc_distribution_warning_count | 580 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 104 |
| already_priced_in_excluded | 38 |
| overheat_pass | 66 |
| score_pass | 66 |
| theme_priority_pass | 63 |
| final_rows | 63 |

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
| fail_revenue_condition | 1630 |
| fail_low_response_condition | 233 |
| fail_already_priced_in | 38 |
| fail_defensive_or_traditional_excluded | 3 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | -4.93 | 5.47 | -3.64 | -16.21 | 12.89 | 12.89 | False |  | mild_accumulation | -0.39 | 0.25 | 0 | 2 | -1.37 | -1.28 | -15.2 | 16 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 0.0 | 3.16 | -6.94 | -25.6 | 4.81 | 4.81 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | 0.6 | 0.39 | -15.78 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -1.44 | -1.44 | -5.09 | 18.22 | 8.01 | 23.64 | False |  | mild_accumulation | 0.36 | 0.0 | 2 | 0 | -0.41 | -0.99 | -15.98 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -0.42 | 6.82 | 7.8 | 0.86 | 10.85 | 10.85 | False |  | strong_accumulation | 1.99 | 1.33 | 3 | 2 | 0.36 | 1.24 | -4.86 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -0.85 | -2.49 | -4.61 | -4.61 | 3.23 | 3.83 | False |  | mild_accumulation | 0.03 | -0.01 | 3 | 0 | -1.18 | -1.4 | -12.66 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -1.61 | -2.39 | -16.95 | -6.13 | 4.26 | 11.36 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -1.17 | -1.55 | -21.97 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -2.71 | -7.72 | -30.34 | -36.36 | 3.99 | 3.99 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.83 | -4.33 | -35.36 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -1.41 | -9.71 | 8.56 | 42.64 | 12.96 | 47.46 | False |  | mild_accumulation | -0.61 | 0.79 | 1 | 2 | -4.47 | -2.73 | -13.62 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -1.86 | 3.12 | -8.64 | -3.76 | 10.6 | 10.6 | False |  | mild_accumulation | 0.93 | -0.73 | 2 | 1 | -0.64 | 0.05 | -9.06 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -5.95 | 22.3 | 60.76 | 81.33 | 65.45 | 91.01 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.82 | 2 | 2 | 4.07 | 5.78 | -9.81 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -0.3 | 5.71 | 27.1 | 68.35 | 33.73 | 84.59 | True | 距120日低點反彈>80% | distribution_warning | -1.51 | -1.63 | 1 | 2 | -1.35 | 0.11 | -33.4 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -0.29 | 4.99 | 10.16 | 14.33 | 17.23 | 23.71 | False |  | strong_accumulation | 0.63 | 0.7 | 3 | 3 | 0.84 | 1.16 | -8.2 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -1.75 | 2.28 | 0.45 | -0.88 | 4.67 | 12.0 | False |  | mild_accumulation | 0.03 | -0.01 | 2 | 1 | -1.86 | -1.09 | -8.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -4.15 | 4.53 | -12.11 | 20.38 | 13.39 | 19.81 | False |  | mild_accumulation | 0.7 | 0.28 | 2 | 1 | -0.97 | -0.2 | -16.99 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -3.08 | 24.75 | 117.58 | 287.69 | 127.59 | 340.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | -1.97 | 3 | 0 | 1.96 | 7.64 | -8.12 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -5.56 | -11.69 | -25.68 |  | 0.74 |  | False |  | distribution_warning | -0.26 | -0.7 | 0 | 0 | -8.05 | -7.29 | -27.27 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 0.0 | -7.25 | -9.33 | 12.5 | 6.11 | 20.3 | False |  | mild_accumulation | 1.06 | -0.99 | 2 | 1 | -2.27 | -3.9 | -35.88 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.23 | 5.13 | 9.04 | 23.62 | 13.68 | 27.86 | False |  | distribution_warning | -0.41 | -2.1 | 0 | 0 | -0.02 | -0.11 | -13.14 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -3.19 | 1.51 | 0.83 | -1.3 | 3.24 | 17.44 | False |  | mild_accumulation | 0.04 | 0.02 | 2 | 1 | -3.13 | -2.86 | -13.43 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -1.71 | 0.47 | 34.69 | 125.07 | 43.67 | 151.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.14 | -0.76 | 2 | 1 | -1.34 | -0.08 | -25.82 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 6.38 | 16.42 | 36.2 | 108.45 | 42.82 | 122.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.43 | 2 | 2 | 7.42 | 4.7 | -27.67 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | -5.49 | -2.82 | -1.27 | 43.52 | 22.05 | 67.39 | False |  | distribution_warning | -1.0 | -1.51 | 0 | 1 | -3.4 | -3.26 | -37.63 | 13 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 1.19 | -1.54 | -2.66 | 24.88 | 13.02 | 36.53 | False |  | distribution_warning | -0.39 | -0.34 | 0 | 0 | 1.22 | 1.88 | -7.08 | 15 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -5.86 | 4.07 | -31.38 | 104.36 | 23.11 | 131.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.21 | -2.24 | 1 | 1 | -1.94 | -2.88 | -53.93 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -3.95 | 0.0 | -10.0 | -22.61 | 32.35 | 32.35 | False |  | distribution_warning | -1.54 | -1.3 | 1 | 1 | -3.82 | -2.46 | -36.72 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -4.13 | 6.42 | 16.78 | 42.62 | 48.72 | 107.64 | True | 距120日低點反彈>80% | strong_accumulation | 0.68 | 0.62 | 2 | 2 | -2.36 | -0.33 | -25.48 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -1.18 | -5.19 | -11.21 | 32.08 | 14.13 | 40.47 | False |  | distribution_warning | -0.19 | -0.04 | 1 | 1 | -1.88 | -2.27 | -25.66 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 1.73 | -5.78 | -4.56 | 12.24 | 9.59 | 17.65 | False |  | distribution_warning | -0.46 | -0.37 | 0 | 0 | -0.15 | -0.03 | -10.48 | 18 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.0 | 0.98 | -7.68 | -13.03 | 7.93 | 7.93 | False |  | distribution_warning | -0.18 | -0.07 | 1 | 1 | 1.71 | 0.67 | -12.39 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 0.0 | 40.88 | 36.86 | 154.25 | 93.15 | 173.09 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.73 | 3.55 | 2 | 1 | 19.75 | 17.1 | -3.04 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 4.01 | 5.47 | 1.96 | 55.35 | 18.84 | 68.96 | False |  | strong_accumulation | 0.84 | 0.76 | 2 | 2 | 1.73 | 2.67 | -8.16 | 20 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 6.22 | 25.46 | 28.77 | 77.34 | 61.42 | 88.07 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.83 | 1.54 | 3 | 3 | 8.95 | 10.48 | -0.49 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | 1.0 | 0.0 | -8.14 | 27.27 | 17.34 | 38.57 | False |  | distribution_warning | -0.15 | -0.86 | 1 | 1 | -3.23 | -0.97 | -16.63 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | -1.35 | -4.84 | -7.26 | 0.2 | 15.35 | 15.35 | False |  | distribution_warning | -1.07 | -0.33 | 0 | 1 | -1.8 | -2.07 | -32.85 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 77.38084589596791 | 70.28827013710922 | -7.52 | 6.42 | -26.41 | 3.98 | 48.23 | 48.23 | False |  | distribution_warning | -1.22 | -1.32 | 0 | 2 | 0.22 | -0.48 | -27.93 | 13 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -1.01 | -2.43 | -4.61 | -3.8 | 15.76 | 15.76 | False |  | distribution_warning | -0.67 | -0.54 | 1 | 2 | -1.37 | -0.88 | -16.5 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 3.44 | 4.94 | 4.79 | 45.86 | 15.71 | 62.98 | False |  | mild_accumulation | 0.66 | 0.25 | 1 | 1 | 1.28 | 2.59 | -10.2 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 3.76 | 15.77 | -9.33 | 20.42 | 23.66 | 25.23 | False |  | distribution_warning | -0.06 | -0.01 | 1 | 2 | 4.6 | 4.19 | -12.21 | 17 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -1.37 | 3.34 | 9.62 | 87.37 | 37.79 | 108.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.59 | -1.21 | 1 | 0 | -4.75 | -1.58 | -16.31 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 6.28 | 12.15 | 52.74 | 107.89 | 58.35 | 126.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.75 | 1 | 1 | 4.64 | 7.41 | -2.2 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -0.96 | -6.04 | 0.0 | 13.5 | 18.48 | 18.48 | False |  | mild_accumulation | 0.93 | -0.05 | 2 | 0 | -2.99 | -0.52 | -8.66 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | -0.47 | -6.96 | -6.96 | 16.94 | 9.74 | 30.33 | False |  | distribution_warning | -0.12 | -1.22 | 2 | 1 | -2.04 | -1.85 | -26.21 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -4.89 | -13.08 | -23.99 | -25.24 | 1.87 | 1.87 | False |  | distribution_warning | -1.76 | -2.67 | 1 | 0 | -6.25 | -6.94 | -40.7 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | -8.15 | 8.53 | 48.95 | 90.77 | 54.04 | 149.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.83 | 2.98 | 3 | 3 | -2.99 | 0.12 | -12.83 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -1.04 | -28.36 | 14.33 | 22.26 | 8.6 | 45.77 | False |  | distribution_warning | -4.47 | -0.95 | 2 | 2 | -4.03 | -4.54 | -28.36 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -2.69 | -3.38 | -2.86 | -2.51 | 0.93 | 7.74 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -2.02 | -1.96 | -15.02 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 20.66 | 26.59 | -3.95 | -3.52 | 36.87 | 36.87 | True | 近20日漲幅>25% | neutral | 0.0 | 0.0 | 0 | 0 | 17.1 | 15.42 | -6.81 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 233.9341638249008 | 396.6930034235488 | -0.52 | -0.52 | -3.5 | -5.62 | 2.93 | 7.82 | False |  | strong_accumulation | 0.46 | 0.98 | 2 | 2 | -0.87 | -0.53 | -5.62 | 21 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -3.23 | -4.21 | -2.9 | -7.93 | 31.71 | 36.45 | False |  | strong_accumulation | 1.28 | 0.02 | 2 | 2 | -3.28 | -1.96 | -13.66 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -1.21 | -5.79 | -8.21 | 13.1 | 5.56 | 19.0 | False |  | distribution_warning | -0.12 | -0.08 | 1 | 1 | -2.56 | -3.1 | -32.14 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 11.05 | 21.61 | 44.52 | 174.03 | 78.81 | 221.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.41 | 10.78 | 2 | 2 | 10.18 | 12.42 | -5.8 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 4.42 | 16.57 | 28.66 | 50.76 | 47.18 | 96.44 | True | 距120日低點反彈>80% | strong_accumulation | 2.38 | 3.25 | 2 | 2 | 6.28 | 8.07 | -7.72 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | -1.15 | 20.6 | 11.67 | 62.31 | 40.23 | 73.78 | False |  | mild_accumulation | 1.42 | -0.27 | 3 | 2 | 5.67 | 5.36 | -10.27 | 22 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 54.39975818511566 | 39.61008944759205 | -3.59 | -3.59 | 2.11 | 40.7 | 20.4 | 50.87 | False |  | distribution_warning | -0.13 | -0.85 | 1 | 1 | -1.26 | -1.23 | -13.57 | 11 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -3.95 | 1.98 | -34.86 | -48.44 | 27.86 | 27.86 | False |  | mild_accumulation | 0.62 | 0.52 | 2 | 1 | -2.35 | -2.41 | -40.06 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | 0.1 | -0.92 | -7.87 | 0.41 | 3.08 | 3.74 | False |  | distribution_warning | -0.11 | -0.27 | 2 | 2 | -0.91 | -0.8 | -12.36 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | -2.47 | 1.63 | -22.14 | -5.19 | 19.84 | 19.84 | False |  | strong_accumulation | 0.95 | 0.53 | 3 | 2 | -2.07 | -2.26 | -32.64 | 17 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | 0.22 | 2.27 | -15.23 | -3.01 | 4.88 | 4.88 | False |  | strong_accumulation | 0.25 | 0.36 | 2 | 2 | -0.92 | -0.66 | -20.6 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -2.92 | 15.0 | 4.55 | 6.79 | 16.34 | 23.55 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 2.63 | 2.92 | -4.78 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -1.42 | 1.61 | -7.47 | -10.8 | 2.21 | 6.77 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.37 | -0.71 | -13.9 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 3.3 | 9.59 | 6.82 | 35.43 | 15.73 | 44.07 | False |  | strong_accumulation | 1.8 | 1.95 | 3 | 3 | 2.82 | 3.4 | -0.92 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 0.39 | -2.04 | -21.37 | -44.76 | 8.46 | 8.46 | False |  | mild_accumulation | -0.46 | 0.04 | 0 | 2 | -1.02 | -0.62 | -22.32 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -0.29 | 8.4 | -11.1 | -4.52 | 10.11 | 10.11 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 2 | 1.49 | 1.44 | -11.88 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -0.2 | -6.29 | -10.49 | -8.44 | 1.63 | 1.73 | False |  | strong_accumulation | 0.23 | 0.17 | 2 | 2 | -1.67 | -1.78 | -15.42 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround |  | 56.21501385482998 | 35.673950917357274 | 8.36 | 13.54 | 31.32 | 39.19 | 40.96 | 49.85 | False |  | strong_accumulation | 0.68 | 0.42 | 3 | 2 | 7.62 | 8.16 | -7.59 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 78.98535443204022 | 130.25483155637795 | 9.06 | 3.1 | 12.04 | 57.74 | 16.53 | 62.7 | False |  | distribution_warning | -0.43 | -0.47 | 1 | 1 | 5.97 | 5.95 | -3.46 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -0.97 | -5.88 | 16.36 | 43.82 | 19.35 | 50.15 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | 0.67 | -2.57 | -42.02 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 0.0 | 5.82 | -2.68 | -23.08 | 10.5 | 10.5 | False |  | mild_accumulation | 0.1 | -2.07 | 1 | 0 | 1.78 | 2.13 | -10.31 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -9.15 | 4.8 | 2.18 | 31.13 | 23.82 | 35.61 | False |  | strong_accumulation | 2.93 | 2.89 | 3 | 2 | -2.51 | -0.55 | -11.49 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 2.1 | -2.02 | -7.6 | 16.27 | 3.85 | 23.35 | False |  | mild_accumulation | 0.36 | -0.03 | 2 | 2 | -0.72 | -1.68 | -25.46 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 3.34 | 8.58 | 37.87 | 28.34 | 72.98 | 89.46 | True | 距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 2.26 | 2.16 | 2 | 2 | 2.8 | 5.79 | -10.02 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 1.41 | 3.06 | -1.94 | 57.32 | 38.93 | 98.04 | True | 距120日低點反彈>80% | mild_accumulation | -0.79 | 0.21 | 0 | 1 | -0.91 | -0.3 | -33.99 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 6.25 | 28.19 | 51.27 | 77.17 | 77.17 | 86.42 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.27 | 1 | 2 | 13.92 | 15.64 | 0.0 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | 6.2 | -6.89 | 12.82 | 40.0 | 24.22 | 59.04 | False |  | mild_accumulation | -0.42 | 1.72 | 1 | 2 | 0.94 | 3.54 | -17.68 | 18 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -0.47 | -2.73 | -15.32 | 13.45 | 13.45 | 32.16 | False |  | distribution_warning | -1.06 | -1.12 | 0 | 0 | -3.58 | -3.22 | -24.85 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -2.44 | -6.59 | -12.45 | 24.86 | 5.02 | 39.52 | False |  | distribution_warning | -2.09 | -0.79 | 1 | 2 | -4.97 | -4.27 | -26.01 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.79 | -8.98 | -19.62 | -23.0 | 6.94 | 6.94 | False |  | distribution_warning | -1.93 | -2.31 | 0 | 0 | -5.1 | -3.89 | -19.79 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 1.75 | 3.56 | -1.89 | -2.71 | 17.09 | 17.09 | False |  | strong_accumulation | 0.08 | 0.92 | 2 | 2 | 1.43 | 1.05 | -28.31 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.54703093190022 | 34.71282457960092 | -0.31 | 23.98 | 1.98 | 33.47 | 49.39 | 49.39 | False |  | mild_accumulation | 0.14 | -0.01 | 1 | 1 | 2.3 | 3.96 | -18.31 | 18 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -2.29 | -2.29 | -0.72 | 14.7 | 11.69 | 20.43 | False |  | mild_accumulation | 2.7 | 0.0 | 1 | 1 | -4.85 | -2.44 | -12.06 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -3.96 | -7.13 | -27.15 | 25.5 | 26.84 | 57.75 | False |  | distribution_warning | -0.29 | -0.7 | 1 | 1 | -5.19 | -3.43 | -31.45 | 12 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -2.65 | 9.96 | -18.58 | -35.81 | 22.67 | 22.67 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 4.6 | 2.08 | -20.12 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 3.92 | 28.02 | 61.59 | 123.06 | 69.22 | 138.31 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.31 | -5.15 | 0 | 1 | 10.67 | 7.59 | -34.08 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 1.44 | 17.28 | -16.75 | 77.57 | 54.82 | 95.68 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.21 | -3.49 | 1 | 1 | 4.13 | 2.95 | -51.64 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | -4.42 | 2.98 | -17.03 | 20.98 | 29.1 | 73.0 | False |  | distribution_warning | -1.43 | -1.72 | 0 | 1 | 0.96 | 0.53 | -16.83 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 2.55 | 16.21 | -6.41 | 124.93 | 84.81 | 164.14 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.83 | -7.13 | 1 | 0 | 11.2 | 10.29 | -16.7 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -10.11 | 6.98 | 15.81 | 180.56 | 41.68 | 181.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.43 | -1.57 | 1 | 0 | -7.78 | -3.54 | -20.32 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 60.760461865560174 | 88.15608743643294 | 11.24 | 7.9 | 25.32 | 55.29 | 42.45 | 61.63 | False |  | distribution_warning | -0.27 | -0.36 | 1 | 1 | 7.06 | 8.74 | -3.88 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -1.42 | 0.0 | 5.7 | 4.91 | 6.11 | 16.81 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | -0.22 | 0.04 | -2.11 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 59.23071292224356 | 63.75000065335939 | -4.72 | -1.33 | -18.68 | 2.3 | 23.47 | 23.47 | False |  | distribution_warning | -0.78 | -0.53 | 1 | 1 | -0.47 | -0.49 | -25.75 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | -3.41 | 27.83 | 44.35 | 122.61 | 82.99 | 171.5 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.42 | 2 | 1 | 3.63 | 6.25 | -10.48 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -8.66 | 21.59 | 22.88 | 107.89 | 75.76 | 144.73 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.94 | 4.34 | 2 | 3 | 3.8 | 5.19 | -11.18 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 3.18 | 6.82 | -6.58 | 3.18 | 21.07 | 21.07 | False |  | mild_accumulation | 0.14 | -1.25 | 2 | 0 | 2.39 | 3.34 | -10.98 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -0.36 | -6.61 | -32.28 | 32.22 | 10.48 | 36.33 | False |  | distribution_warning | -0.42 | -0.14 | 1 | 2 | -2.71 | -2.46 | -36.17 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | -3.77 | 1.88 | -29.43 | -30.28 | 26.35 | 26.35 | False |  | strong_accumulation | 0.48 | 0.37 | 2 | 3 | -2.22 | -2.04 | -36.87 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 1.56 | 34.13 | 54.61 | 50.64 | 96.49 | 109.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.15 | -0.41 | 2 | 2 | 11.11 | 13.19 | -3.61 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 3.81 | 13.59 | 4.46 | 31.06 | 60.46 | 70.16 | True | 距60日低點反彈>50% | distribution_warning | -1.41 | -4.39 | 1 | 1 | 6.32 | 7.32 | -13.79 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.590900789853706 | 37.93424741228517 | -5.09 | -2.5 | -0.46 | 26.92 | 27.3 | 27.3 | False |  | distribution_warning | -0.16 | -0.27 | 2 | 1 | -1.14 | -0.52 | -16.05 | 12 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 4.0 | -15.1 | -4.59 | 11.83 | 7.0 | 20.23 | False |  | distribution_warning | -2.05 | -2.31 | 0 | 0 | -5.22 | -3.66 | -20.31 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -0.5 | 4.69 | -15.55 | -15.55 | 17.41 | 17.41 | False |  | mild_accumulation | 0.51 | -0.01 | 3 | 1 | -1.64 | -0.75 | -16.94 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.6507119471058 | 40.90376378051168 | -5.6 | 3.06 | -27.38 | -38.06 | 31.84 | 31.84 | False |  | mild_accumulation | 0.01 | -0.77 | 1 | 2 | 1.09 | -0.5 | -39.95 | 18 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 3.12 | 8.72 | 30.62 | 6.25 | 36.66 | 41.67 | False |  | strong_accumulation | 0.27 | 0.26 | 2 | 2 | 4.43 | 5.59 | -0.88 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 10.19 | 9.17 | 18.41 | 100.0 | 46.91 | 107.86 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.85 | 2 | 1 | 9.2 | 9.61 | -5.56 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -2.63 | 1.17 | -10.21 | -13.21 | 7.01 | 7.01 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -0.64 | -0.88 | -16.29 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -5.64 | -0.71 | -33.12 | 0.48 | 21.69 | 21.69 | False |  | mild_accumulation | -0.71 | 0.58 | 1 | 1 | -2.98 | -2.78 | -36.18 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth | A_優先追蹤 | 66.35391853670312 | 30.54000053488904 | 2.82 | 14.61 | 9.68 | 12.83 | 36.0 | 36.0 | False |  | mild_accumulation | 1.43 | 1.47 | 2 | 1 | 8.27 | 8.06 | -3.32 | 19 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -5.07 | -9.91 | -12.74 | 52.27 | 11.33 | 82.89 | True | 距120日低點反彈>80% | distribution_warning | -3.78 | -3.03 | 0 | 0 | -3.89 | -3.53 | -19.59 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -4.47 | -1.77 | -14.46 | -30.5 | 5.7 | 5.7 | False |  | mild_accumulation | 0.21 | 0.38 | 3 | 1 | -2.42 | -3.17 | -27.23 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -11.12 | -18.74 | -21.44 | -39.23 | 0.0 | 0.0 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -13.91 | -13.52 | -26.32 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 4.57 | 16.47 | -15.43 | 7.91 | 44.07 | 44.07 | False |  | strong_accumulation | 0.22 | 0.19 | 2 | 2 | 5.41 | 5.03 | -17.15 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 0.91 | -1.43 | 2.6 | 1.85 | 41.18 | 41.18 | False |  | distribution_warning | -4.56 | -1.03 | 2 | 1 | 1.14 | 2.91 | -5.32 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 7.56 | 38.58 | 5.11 | -1.33 | 76.19 | 76.19 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.69 | -0.67 | 2 | 1 | 15.52 | 14.9 | -4.88 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 105.41523454519049 | 68.91539282131619 | -10.41 | -7.0 | -25.58 | -17.32 | 21.96 | 21.96 | False |  | mild_accumulation | -1.03 | 0.38 | 1 | 2 | -5.23 | -6.02 | -48.0 | 20 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.8 | -1.82 | 2.44 | 37.96 | 9.57 | 38.97 | False |  | mild_accumulation | 0.22 | 0.0 | 2 | 0 | -0.7 | -0.18 | -6.44 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -2.45 | -17.29 | -10.0 | -4.91 | 1.61 | 1.61 | False |  | distribution_warning | -8.96 | -8.86 | 0 | 1 | -4.78 | -4.84 | -20.42 | 12 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 1.91 | -0.16 | -22.14 | -6.98 | 4.23 | 4.23 | False |  | distribution_warning | -0.45 | -0.52 | 1 | 0 | 1.03 | 0.35 | -23.72 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 0.0 | 0.45 | -0.67 | -12.97 | 4.24 | 8.31 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 0.49 | 0.04 | -7.32 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 1.73 | -2.3 | -8.26 | -0.26 | 2.27 | 5.36 | False |  | distribution_warning | -0.32 | -0.29 | 1 | 1 | -1.48 | -1.14 | -12.46 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 2.76 | 5.84 | 4.62 | 15.27 | 11.23 | 18.28 | False |  | strong_accumulation | 0.46 | 0.23 | 2 | 2 | 2.11 | 1.82 | -3.06 |  | fail_low_response_condition |