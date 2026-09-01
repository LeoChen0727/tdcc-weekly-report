# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-01 19:37:02 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 708101 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 437 |
| tdcc_mild_accumulation_count | 765 |
| tdcc_distribution_warning_count | 580 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 84 |
| already_priced_in_excluded | 26 |
| overheat_pass | 58 |
| score_pass | 58 |
| theme_priority_pass | 53 |
| final_rows | 53 |

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
| fail_low_response_condition | 253 |
| fail_already_priced_in | 26 |
| fail_defensive_or_traditional_excluded | 4 |
| missing_or_insufficient_price_metrics | 1 |
| fail_mainstream_score_lt_10 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | -0.9 | 8.96 | 3.3 | -15.44 | 16.61 | 16.61 | False |  | mild_accumulation | -0.39 | 0.25 | 0 | 2 | 2.86 | 1.9 | -12.4 | 17 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -2.25 | 3.17 | -12.44 | -30.16 | 4.41 | 4.41 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | 0.62 | -0.03 | -16.1 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.0 | 3.0 | -0.96 | 16.78 | 8.54 | 24.25 | False |  | mild_accumulation | 0.36 | 0.0 | 2 | 0 | 0.05 | -0.85 | -15.57 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -1.68 | 8.84 | 0.0 | 0.86 | 10.38 | 10.38 | False |  | strong_accumulation | 1.99 | 1.33 | 3 | 2 | 1.04 | 1.1 | -5.26 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -0.84 | -1.94 | -5.36 | -6.61 | 3.52 | 4.13 | False |  | mild_accumulation | 0.03 | -0.01 | 3 | 0 | -1.41 | -1.59 | -12.41 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -1.59 | 1.22 | -8.49 | 15.89 | 5.53 | 14.81 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -0.28 | -0.84 | -26.19 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -8.0 | -12.66 | -35.81 | -41.03 | 0.0 | 0.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -7.85 | -9.06 | -37.84 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -1.03 | 1.4 | 9.47 | 42.36 | 17.96 | 52.75 | False |  | mild_accumulation | -0.61 | 0.79 | 1 | 2 | -2.55 | -0.19 | -10.53 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 0.5 | 2.7 | -5.0 | -3.39 | 11.3 | 11.3 | False |  | mild_accumulation | 0.93 | -0.73 | 2 | 1 | 0.42 | 0.7 | -14.19 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 7.85 | 44.44 | 80.2 | 98.91 | 88.6 | 104.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.82 | 2 | 2 | 15.08 | 15.36 | -3.45 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 12.42 | 27.49 | 61.3 | 97.76 | 49.0 | 105.65 | True | 近20日漲幅>25%；近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.63 | 1 | 2 | 11.18 | 11.93 | -25.8 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -4.13 | 7.4 | 10.28 | 12.06 | 17.74 | 24.24 | False |  | strong_accumulation | 0.63 | 0.7 | 3 | 3 | 2.56 | 2.48 | -7.8 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -2.59 | 1.35 | -9.96 | 1.35 | 5.61 | 13.0 | False |  | mild_accumulation | 0.03 | -0.01 | 2 | 1 | -0.7 | -0.53 | -7.38 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -1.16 | 6.22 | -4.48 | 20.19 | 14.29 | 23.08 | False |  | mild_accumulation | 0.7 | 0.28 | 2 | 1 | 0.63 | 0.6 | -19.24 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -0.95 | 49.03 | 151.78 | 326.2 | 135.83 | 349.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | -1.97 | 3 | 0 | 8.27 | 12.1 | -6.2 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -5.03 | -13.46 | -28.89 |  | 2.54 |  | False |  | distribution_warning | -0.26 | -0.7 | 0 | 0 | -6.04 | -5.3 | -31.64 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -2.04 | -12.41 | -14.29 | 7.62 | 4.8 | 18.81 | False |  | mild_accumulation | 1.06 | -0.99 | 2 | 1 | -5.03 | -6.19 | -36.68 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.67 | 6.54 | 7.65 | 24.17 | 14.63 | 28.69 | False |  | distribution_warning | -0.41 | -2.1 | 0 | 0 | 1.51 | 0.64 | -12.57 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 1.61 | 5.0 | 0.64 | -1.25 | 7.33 | 22.09 | False |  | mild_accumulation | 0.04 | 0.02 | 2 | 1 | 0.96 | 0.27 | -10.0 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 5.77 | 5.01 | 30.18 | 134.67 | 46.67 | 156.56 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.14 | -0.76 | 2 | 1 | 0.7 | 1.73 | -24.27 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 4.79 | -9.36 | 31.33 | 98.99 | 45.93 | 113.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.43 | 2 | 2 | 4.47 | 1.2 | -30.72 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | 6.73 | 9.18 | -0.3 | 65.67 | 31.1 | 79.81 | False |  | distribution_warning | -1.0 | -1.51 | 0 | 1 | 3.38 | 3.17 | -33.0 | 14 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 5.35 | 2.4 | -10.02 | 18.24 | 13.02 | 36.53 | False |  | distribution_warning | -0.39 | -0.34 | 0 | 0 | 0.65 | 1.93 | -7.75 | 15 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 4.41 | 0.35 | -26.14 | 118.46 | 24.42 | 133.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.21 | -2.24 | 1 | 1 | -1.53 | -3.84 | -53.44 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 0.41 | 2.08 | -18.33 | 2.94 | 33.44 | 33.44 | False |  | distribution_warning | -1.54 | -1.3 | 1 | 1 | -3.28 | -2.61 | -36.2 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -1.68 | 12.1 | 8.64 | 50.43 | 50.43 | 110.02 | True | 距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.68 | 0.62 | 2 | 2 | -0.72 | 0.69 | -24.63 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 71.68985948774075 | 62.35657344241515 | 8.62 | -4.96 | -11.45 | 58.63 | 19.84 | 55.28 | False |  | distribution_warning | -0.19 | -0.04 | 1 | 1 | 1.41 | 2.05 | -21.95 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | -0.81 | -8.32 | -2.6 | 11.4 | 7.1 | 14.97 | False |  | distribution_warning | -0.46 | -0.37 | 0 | 0 | -3.7 | -2.54 | -12.51 | 18 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.86 | 4.28 | -2.35 | -10.51 | 5.84 | 5.84 | False |  | distribution_warning | -0.18 | -0.07 | 1 | 1 | 0.05 | -1.35 | -14.09 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 13.28 | 36.56 | 12.72 | 152.8 | 82.26 | 157.7 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.73 | 3.55 | 2 | 1 | 18.36 | 14.9 | -8.5 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 1.83 | 0.91 | -13.28 | 54.52 | 17.25 | 66.71 | False |  | strong_accumulation | 0.84 | 0.76 | 2 | 2 | 0.67 | 1.6 | -9.39 | 20 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 9.19 | 25.31 | 12.22 | 71.48 | 59.06 | 85.32 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.83 | 1.54 | 3 | 3 | 10.49 | 11.54 | -1.46 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | 3.31 | 5.45 | -20.86 | 40.0 | 17.34 | 40.48 | False |  | distribution_warning | -0.15 | -0.86 | 1 | 1 | -2.93 | -1.57 | -18.15 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 2.18 | 0.19 | -17.6 | 1.58 | 16.25 | 16.25 | False |  | distribution_warning | -1.07 | -0.33 | 0 | 1 | -1.71 | -2.11 | -32.33 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 26.16 | 36.57 | -6.84 | 34.76 | 73.76 | 73.76 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.22 | -1.32 | 0 | 2 | 19.86 | 18.44 | -22.47 |  | fail_low_response_condition |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | 2.69 | 1.93 | -13.8 | -4.18 | 16.44 | 16.44 | False |  | distribution_warning | -0.67 | -0.54 | 1 | 2 | -0.98 | -0.38 | -16.01 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 3.31 | 8.13 | -2.71 | 51.8 | 15.06 | 62.08 | False |  | mild_accumulation | 0.66 | 0.25 | 1 | 1 | 1.33 | 2.52 | -10.7 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 4.11 | 13.81 | -12.42 | 18.34 | 22.58 | 24.14 | False |  | distribution_warning | -0.06 | -0.01 | 1 | 2 | 5.5 | 4.05 | -12.98 | 17 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 0.8 | 9.73 | 15.46 | 118.18 | 43.51 | 117.34 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.59 | -1.21 | 1 | 0 | -0.47 | 1.85 | -12.83 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 6.12 | 23.44 | 43.35 | 109.12 | 58.35 | 126.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.75 | 1 | 1 | 6.11 | 8.93 | -0.56 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -0.16 | 8.9 | -2.65 | 12.03 | 18.86 | 18.86 | False |  | mild_accumulation | 0.93 | -0.05 | 2 | 0 | -2.95 | -0.39 | -8.37 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | 2.8 | -0.9 | -8.71 | 14.11 | 12.82 | 33.98 | False |  | distribution_warning | -0.12 | -1.22 | 2 | 1 | -0.68 | -0.34 | -24.14 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 0.35 | -9.27 | -18.04 | -18.39 | 4.99 | 4.99 | False |  | distribution_warning | -1.76 | -2.67 | 1 | 0 | -4.62 | -4.86 | -38.19 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 1.57 | 18.81 | 43.89 | 98.09 | 60.87 | 160.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.83 | 2.98 | 3 | 3 | 2.62 | 4.63 | -8.96 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -0.79 | -25.4 | 5.64 | 20.61 | 17.21 | 44.04 | False |  | distribution_warning | -4.47 | -0.95 | 2 | 2 | -9.55 | -7.34 | -29.21 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -0.36 | -3.17 | -3.68 | -0.9 | 1.67 | 8.93 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -1.55 | -1.42 | -14.08 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 3.11 | 3.69 | -29.67 | -11.41 | 14.06 | 14.06 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.7 | -0.03 | -28.57 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 233.9341638249008 | 396.6930034235488 | -1.53 | 1.31 | -2.76 | -6.3 | 3.2 | 8.1 | False |  | strong_accumulation | 0.46 | 0.98 | 2 | 2 | -0.49 | -0.45 | -5.38 | 21 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -1.34 | 3.69 | -8.24 | 13.68 | 36.57 | 41.49 | False |  | strong_accumulation | 1.28 | 0.02 | 2 | 2 | 0.2 | 1.5 | -10.47 | 22 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 2.28 | -4.59 | -9.49 | 19.75 | 7.78 | 21.5 | False |  | distribution_warning | -0.12 | -0.08 | 1 | 1 | -1.81 | -2.06 | -30.71 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -4.4 | 13.89 | 11.82 | 137.45 | 56.36 | 180.82 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.41 | 10.78 | 2 | 2 | -0.71 | 2.23 | -14.78 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 7.16 | 22.82 | 15.01 | 67.48 | 42.14 | 89.7 | True | 距120日低點反彈>80% | strong_accumulation | 2.38 | 3.25 | 2 | 2 | 5.11 | 7.22 | -10.05 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 16.64 | 24.06 | 7.59 | 64.86 | 45.12 | 79.83 | False |  | mild_accumulation | 1.42 | -0.27 | 3 | 2 | 12.01 | 10.75 | -7.14 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 54.39975818511566 | 39.61008944759205 | 5.81 | 7.14 | 6.25 | 58.78 | 26.87 | 58.98 | False |  | distribution_warning | -0.13 | -0.85 | 1 | 1 | 3.68 | 4.17 | -8.93 | 13 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | 4.25 | 5.15 | -36.44 | -37.1 | 32.82 | 32.82 | False |  | mild_accumulation | 0.62 | 0.52 | 2 | 1 | 1.65 | 0.72 | -38.45 | 22 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.21 | 0.0 | -9.81 | 1.37 | 2.44 | 3.1 | False |  | distribution_warning | -0.11 | -0.27 | 2 | 2 | -1.61 | -1.72 | -12.91 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | -1.94 | 1.2 | -23.33 | 18.97 | 21.44 | 21.44 | False |  | strong_accumulation | 0.95 | 0.53 | 3 | 2 | -0.99 | -1.62 | -31.74 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral |  | 119.67349677675224 | 35.30940543476948 | -1.75 | 1.12 | -6.64 | -1.53 | 4.65 | 4.65 | False |  | strong_accumulation | 0.25 | 0.36 | 2 | 2 | -0.87 | -1.12 | -20.77 |  | fail_low_response_condition |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 3.39 | 15.09 | 16.41 | 10.11 | 21.03 | 26.03 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 6.77 | 5.84 | -2.87 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 0.29 | -0.43 | -3.72 | -10.74 | 4.18 | 7.38 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.19 | -0.65 | -13.4 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 0.84 | 8.49 | 11.4 | 30.16 | 16.26 | 42.14 | False |  | strong_accumulation | 1.8 | 1.95 | 3 | 3 | 2.83 | 2.96 | -2.24 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 93.8248443457034 | 60.82046311316634 | 0.39 | 5.46 | -21.6 | -47.49 | 9.03 | 9.03 | False |  | mild_accumulation | -0.46 | 0.04 | 0 | 2 | -0.42 | -0.35 | -24.81 | 17 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -0.14 | 6.31 | -9.91 | -4.82 | 9.16 | 9.16 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 2 | 1.74 | 0.78 | -13.41 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -0.7 | -3.11 | -4.95 | -10.49 | 1.63 | 1.73 | False |  | strong_accumulation | 0.23 | 0.17 | 2 | 2 | -2.32 | -2.28 | -15.42 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 0.1 | 13.95 | 18.61 | 34.84 | 35.03 | 43.54 | False |  | strong_accumulation | 0.68 | 0.42 | 3 | 2 | 5.2 | 5.82 | -11.48 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 0.41 | -16.81 | -1.0 | 39.44 | 17.02 | 45.16 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -4.81 | -7.69 | -43.94 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | -0.25 | 7.07 | -10.45 | -26.9 | 8.84 | 8.84 | False |  | mild_accumulation | 0.1 | -2.07 | 1 | 0 | 1.34 | 0.99 | -13.02 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 4.13 | 17.65 | 8.11 | 36.82 | 28.54 | 40.79 | False |  | strong_accumulation | 2.93 | 2.89 | 3 | 2 | 2.44 | 3.42 | -8.11 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 1.27 | -4.38 | -7.69 | 11.63 | 2.56 | 21.83 | False |  | mild_accumulation | 0.36 | -0.03 | 2 | 2 | -2.62 | -3.37 | -26.38 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 3.15 | 28.05 | 25.17 | 57.34 | 72.98 | 89.46 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 2.26 | 2.16 | 2 | 2 | 4.4 | 7.7 | -6.86 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 7.44 | 9.7 | -3.7 | 66.67 | 43.05 | 103.92 | True | 距120日低點反彈>80% | mild_accumulation | -0.79 | 0.21 | 0 | 1 | 1.73 | 2.2 | -32.03 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 15.59 | 31.15 | 31.15 | 86.34 | 69.23 | 85.83 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.27 | 1 | 2 | 11.89 | 13.92 | -1.59 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | -0.54 | 1.76 | 19.51 | 51.14 | 23.33 | 53.4 | False |  | mild_accumulation | -0.42 | 1.72 | 1 | 2 | -4.03 | -0.55 | -20.6 | 17 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -2.12 | -4.58 | -17.92 | 25.44 | 14.34 | 33.2 | False |  | distribution_warning | -1.06 | -1.12 | 0 | 0 | -3.99 | -3.15 | -24.27 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -3.7 | -8.2 | -14.58 | 38.93 | 5.73 | 40.48 | False |  | distribution_warning | -2.09 | -0.79 | 1 | 2 | -5.34 | -4.65 | -25.51 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.26 | -7.76 | -30.25 | -16.6 | 8.89 | 8.89 | False |  | distribution_warning | -1.93 | -2.31 | 0 | 0 | -5.7 | -3.59 | -23.29 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 270.5877639328499 | 61.05386791096055 | 4.27 | 4.27 | -5.88 | -0.85 | 16.58 | 16.58 | False |  | strong_accumulation | 0.08 | 0.92 | 2 | 2 | 1.42 | 0.97 | -28.62 | 24 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 8.64 | 28.32 | 1.0 | 38.95 | 53.82 | 53.82 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.14 | -0.01 | 1 | 1 | 8.61 | 8.59 | -15.89 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -1.05 | 6.39 | -6.14 | 18.41 | 14.11 | 23.04 | False |  | mild_accumulation | 2.7 | 0.0 | 1 | 1 | -2.91 | -0.99 | -10.16 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -1.44 | -1.79 | -17.35 | 40.33 | 30.17 | 61.89 | False |  | distribution_warning | -0.29 | -0.7 | 1 | 1 | -3.94 | -1.97 | -29.65 | 12 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 13.62 | 18.46 | -30.31 | -26.45 | 29.78 | 29.78 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 12.49 | 8.96 | -23.16 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 12.12 | 26.96 | 30.15 | 120.24 | 65.39 | 132.91 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.31 | -5.15 | 0 | 1 | 11.88 | 8.24 | -35.57 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 4.22 | 20.14 | -21.72 | 83.65 | 51.75 | 91.8 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.21 | -3.49 | 1 | 1 | 3.75 | 0.56 | -52.6 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 204.3244857198993 | 247.3095962162866 | -3.89 | 4.53 | -23.96 | 57.27 | 29.1 | 73.0 | False |  | distribution_warning | -1.43 | -1.72 | 0 | 1 | 0.68 | 0.82 | -22.07 | 16 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 18.69 | 36.29 | -15.79 | 117.98 | 84.12 | 163.16 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.83 | -7.13 | 1 | 0 | 12.87 | 11.8 | -21.18 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -11.32 | 6.6 | 14.77 | 170.74 | 44.81 | 187.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.43 | -1.57 | 1 | 0 | -4.61 | -2.43 | -18.56 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 1.96 | -6.67 | 6.43 | 34.81 | 30.94 | 48.57 | False |  | distribution_warning | -0.27 | -0.36 | 1 | 1 | -1.44 | 1.44 | -11.65 | 13 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 0.0 | 2.56 | 7.69 | 7.69 | 13.82 | 17.65 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | 0.48 | 0.63 | -1.41 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | 7.01 | 4.57 | -26.6 | 11.71 | 27.36 | 27.36 | False |  | distribution_warning | -0.78 | -0.53 | 1 | 1 | 2.35 | 2.36 | -23.41 | 13 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 7.63 | 44.63 | 35.94 | 165.27 | 88.82 | 180.14 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.42 | 2 | 1 | 10.98 | 11.85 | -7.63 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 17.26 | 44.68 | 24.75 | 115.89 | 89.39 | 163.71 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.94 | 4.34 | 2 | 3 | 14.86 | 15.0 | -4.29 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 1.58 | 13.1 | -10.02 | 6.65 | 19.73 | 19.73 | False |  | mild_accumulation | 0.14 | -1.25 | 2 | 0 | 2.16 | 2.96 | -11.96 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 0.72 | -4.65 | -39.13 | 34.4 | 11.41 | 37.48 | False |  | distribution_warning | -0.42 | -0.14 | 1 | 2 | -2.83 | -2.17 | -39.13 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 3.74 | 5.47 | -32.03 | -28.76 | 29.11 | 29.11 | False |  | strong_accumulation | 0.48 | 0.37 | 2 | 3 | 0.1 | -0.48 | -35.49 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 13.06 | 41.98 | 62.57 | 73.6 | 96.82 | 110.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.15 | -0.41 | 2 | 2 | 15.77 | 17.2 | -3.45 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 10.61 | 26.11 | -0.23 | 36.8 | 62.55 | 72.38 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.41 | -4.39 | 1 | 1 | 9.76 | 10.61 | -12.67 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 59.590900789853706 | 37.93424741228517 | 11.57 | 0.65 | 7.42 | 45.6 | 37.39 | 45.6 | False |  | distribution_warning | -0.16 | -0.27 | 2 | 1 | 5.45 | 7.09 | -9.39 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | -8.64 | -14.47 | -12.23 | 22.71 | 3.4 | 22.11 | False |  | distribution_warning | -2.05 | -2.31 | 0 | 0 | -11.2 | -8.23 | -22.99 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -0.99 | 6.46 | -15.9 | -19.92 | 17.41 | 17.41 | False |  | mild_accumulation | 0.51 | -0.01 | 3 | 1 | -1.12 | -0.98 | -18.62 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 21.0 | 26.79 | -22.06 | -17.96 | 48.04 | 48.04 | True | 近20日漲幅>25% | mild_accumulation | 0.01 | -0.77 | 1 | 2 | 14.5 | 12.12 | -32.57 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 8.69 | 17.29 | 36.32 | 2.74 | 42.17 | 42.17 | False |  | strong_accumulation | 0.27 | 0.26 | 2 | 2 | 6.71 | 7.73 | -0.35 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 17.01 | 14.68 | 4.54 | 87.4 | 42.28 | 101.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.85 | 2 | 1 | 7.15 | 9.12 | -5.73 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 1.54 | 4.35 | -12.29 | -11.71 | 8.87 | 8.87 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 1.47 | 0.89 | -14.84 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 128.9172485640275 | 121.34662298357856 | 2.88 | 3.75 | -27.37 | 9.59 | 24.75 | 24.75 | False |  | mild_accumulation | -0.71 | 0.58 | 1 | 1 | -0.9 | -1.12 | -36.28 | 17 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 10.4 | 11.02 | 6.47 | 8.58 | 31.6 | 31.6 | False |  | mild_accumulation | 1.43 | 1.47 | 2 | 1 | 6.86 | 7.19 | -2.76 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -1.77 | -1.77 | -16.92 | 67.0 | 14.07 | 87.41 | True | 距120日低點反彈>80% | distribution_warning | -3.78 | -3.03 | 0 | 0 | -2.76 | -1.95 | -20.24 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -2.1 | -2.44 | -15.41 | -27.08 | 6.46 | 6.46 | False |  | mild_accumulation | 0.21 | 0.38 | 3 | 1 | -2.3 | -3.39 | -26.7 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -0.12 | 0.6 | -5.96 | -30.25 | 7.03 | 7.03 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -0.51 | -0.4 | -13.26 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 15.07 | 29.27 | -12.99 | 23.04 | 51.3 | 51.3 | True | 近20日漲幅>25%；距60日低點反彈>50% | strong_accumulation | 0.22 | 0.19 | 2 | 2 | 13.54 | 12.55 | -17.14 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 1.28 | 7.6 | -1.08 | 32.37 | 41.18 | 41.18 | False |  | distribution_warning | -4.56 | -1.03 | 2 | 1 | 1.15 | 3.75 | -6.12 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 15.16 | 36.26 | -10.97 | -4.55 | 70.0 | 70.0 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.69 | -0.67 | 2 | 1 | 15.78 | 14.52 | -9.85 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 105.41523454519049 | 68.91539282131619 | 6.24 | -3.72 | -28.82 | -4.01 | 29.14 | 29.14 | False |  | mild_accumulation | -1.03 | 0.38 | 1 | 2 | -0.8 | -1.96 | -44.94 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.53 | -2.07 | 13.81 | 37.82 | 19.94 | 39.85 | False |  | mild_accumulation | 0.22 | 0.0 | 2 | 0 | -0.56 | 0.05 | -6.19 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | 0.0 | -13.57 | -13.95 | -2.16 | 1.18 | 2.94 | False |  | distribution_warning | -8.96 | -8.86 | 0 | 1 | -5.7 | -4.26 | -18.84 | 14 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | -2.04 | -2.65 | -18.0 | -8.37 | 1.63 | 1.63 | False |  | distribution_warning | -0.45 | -0.52 | 1 | 0 | -1.6 | -2.2 | -25.63 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -1.35 | -5.0 | -4.17 | -10.45 | 2.82 | 6.85 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -1.08 | -1.43 | -8.58 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 0.8 | -2.06 | -1.94 | 0.8 | 1.34 | 4.4 | False |  | distribution_warning | -0.32 | -0.29 | 1 | 1 | -2.68 | -2.41 | -13.26 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 1.45 | 8.42 | 4.47 | 14.31 | 10.7 | 17.72 | False |  | strong_accumulation | 0.46 | 0.23 | 2 | 2 | 2.48 | 1.75 | -3.52 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 4.6 | 41.42 | 21.94 | 51.27 | 48.45 | 50.79 | True | 近20日漲幅>25% | strong_accumulation | 3.39 | 6.39 | 3 | 3 | 7.23 | 7.9 | -10.15 |  | fail_already_priced_in |