# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-11 08:32:44 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1953 |
| standardized_revenue_rows | 1953 |
| price_rows | 663489 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 391 |
| tdcc_mild_accumulation_count | 717 |
| tdcc_distribution_warning_count | 674 |
| revenue_condition_pass | 337 |
| price_metrics_pass | 336 |
| low_response_pass | 58 |
| already_priced_in_excluded | 15 |
| overheat_pass | 43 |
| score_pass | 43 |
| theme_priority_pass | 40 |
| final_rows | 40 |

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
| fail_revenue_condition | 1616 |
| fail_low_response_condition | 278 |
| fail_already_priced_in | 15 |
| fail_defensive_or_traditional_excluded | 2 |
| missing_or_insufficient_price_metrics | 1 |
| fail_mainstream_score_lt_10 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | 0.0 | -2.43 | -5.19 | -26.1 | 7.03 | 7.03 | False |  | strong_accumulation | 0.21 | 0.28 | 2 | 2 | -0.49 | -0.84 | -13.36 | 19 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 4.37 | -1.31 | -3.13 | -22.07 | 5.41 | 5.41 | False |  | mild_accumulation | 0.23 | -0.81 | 2 | 0 | 1.47 | 0.73 | -15.3 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 5.5 | -9.61 | 12.5 | 0.98 | 14.62 | 24.85 | False |  | distribution_warning | -1.44 | 0.0 | 0 | 1 | -3.86 | -2.47 | -15.16 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 1.85 | -0.45 | -0.9 | -5.58 | 3.77 | 3.77 | False |  | mild_accumulation | 0.14 | -0.29 | 2 | 2 | 0.57 | 0.7 | -7.56 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.0 | -2.43 | 0.84 | -7.91 | 6.49 | 6.49 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -1.8 | -1.37 | -10.42 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 5.74 | -5.15 | 5.31 | 19.44 | 9.79 | 27.72 | False |  | mild_accumulation | 0.0 | 0.83 | 1 | 2 | 1.92 | 0.71 | -23.21 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -7.28 | -18.84 | -31.22 | -33.86 | 3.17 | 3.17 | False |  | mild_accumulation | 0.08 | 0.0 | 3 | 0 | -7.89 | -9.97 | -34.16 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | 10.95 | 18.94 | 11.74 | 27.64 | 28.16 | 66.49 | False |  | mild_accumulation | 0.13 | -1.66 | 2 | 1 | 11.96 | 10.44 | -1.26 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | D_降級_TDCC轉弱 | 187.03179652280383 | 2.596548930575971 | 5.06 | 4.79 | 5.74 | -11.28 | 12.97 | 12.97 | False |  | distribution_warning | -0.16 | -0.18 | 1 | 2 | 5.85 | 4.18 | -12.9 | 11 | selected |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 18.95 | 1.87 | 50.41 | 63.96 | 49.59 | 66.46 | True | 近60日漲幅>40% | strong_accumulation | 1.52 | 1.11 | 3 | 3 | 4.69 | 7.64 | -4.55 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 16.03 | 0.0 | 74.89 | 83.17 | 79.03 | 85.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.43 | 0.75 | 2 | 3 | 10.74 | 8.06 | -33.4 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 0.76 | 8.28 | 14.21 | 5.87 | 18.89 | 18.89 | False |  | strong_accumulation | 0.27 | 0.39 | 2 | 2 | 3.71 | 4.07 | -1.48 | 22 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -0.45 | 0.0 | 6.25 | -5.15 | 10.5 | 10.5 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | 0.27 | 0.0 | -11.95 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | 7.98 | 8.44 | 10.3 | 5.76 | 14.73 | 24.15 | False |  | mild_accumulation | 0.27 | 0.0 | 2 | 0 | 8.05 | 5.37 | -18.93 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 37.87 | 47.34 | 164.56 | 305.62 | 158.52 | 307.71 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.2 | 1 | 1 | 38.91 | 36.5 | -2.58 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -3.14 | 6.57 | -11.75 |  | 11.59 |  | False |  | distribution_warning | -0.32 | -0.12 | 1 | 2 | 3.22 | 0.58 | -25.6 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 0.0 | -21.26 | 4.98 | 21.24 | 15.13 | 35.64 | False |  | mild_accumulation | -2.08 | 1.97 | 0 | 2 | -5.58 | -4.39 | -27.7 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | 4.38 | 10.91 | 12.32 | 32.62 | 16.98 | 34.49 | False |  | distribution_warning | -0.15 | 0.0 | 0 | 0 | 1.23 | 3.94 | -12.43 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -3.82 | -4.13 | 12.9 | -22.76 | 9.62 | 17.05 | False |  | mild_accumulation | 0.02 | 0.15 | 1 | 2 | -4.16 | -3.41 | -13.71 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 6.25 | -2.41 | 70.34 | 129.73 | 68.32 | 155.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.69 | 0.76 | 1 | 1 | 3.95 | 2.35 | -26.85 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | -9.08 | -26.64 | 75.0 | 129.64 | 72.92 | 147.23 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.49 | -3.58 | 0 | 1 | -7.27 | -6.19 | -31.89 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 9.73 | -11.86 | 18.91 | 70.14 | 28.74 | 93.03 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -0.03 | 1 | 1 | 4.06 | 0.24 | -34.21 |  | fail_low_response_condition |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | 4.55 | 11.84 | 10.21 | 19.68 | 16.78 | 41.07 | False |  | strong_accumulation | 0.93 | 1.0 | 2 | 2 | 6.84 | 5.38 | -15.76 | 18 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 3.8 | -29.78 | 10.19 | 125.59 | 25.52 | 138.75 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.47 | -2.42 | 0 | 0 | -7.76 | -11.73 | -53.03 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 180.47957329305424 | 137.8339123232017 | 20.81 | -3.26 | -5.32 | 49.0 | 45.42 | 50.34 | False |  | distribution_warning | -1.24 | -1.5 | 2 | 1 | 9.28 | 6.3 | -30.47 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 25.52 | 7.49 | 55.41 | 73.43 | 58.15 | 114.2 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.15 | 0.42 | 1 | 1 | 14.68 | 11.44 | -23.13 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -7.28 | -9.98 | -8.07 | 55.76 | 17.66 | 67.83 | False |  | distribution_warning | -0.03 | -0.14 | 2 | 2 | -2.15 | -4.43 | -23.36 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | 0.22 | 11.39 | 9.8 | 35.15 | 14.45 | 39.03 | False |  | strong_accumulation | 0.35 | 0.31 | 3 | 2 | 3.3 | 1.59 | -6.51 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | -4.44 | -7.54 | 2.89 | -5.07 | 6.44 | 6.44 | False |  | strong_accumulation | 0.11 | 0.05 | 2 | 2 | -5.73 | -3.81 | -13.61 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 7.67 | -19.95 | -6.39 | 98.24 | 35.89 | 124.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.69 | 1.32 | 2 | 2 | 2.53 | -0.49 | -27.68 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 3.29 | 2.01 | 28.4 | 46.5 | 27.17 | 71.21 | False |  | strong_accumulation | 1.09 | 0.95 | 3 | 3 | 6.13 | 3.74 | -25.51 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 53.325092938625424 | 40.87924777938564 | 2.38 | 16.19 | 27.81 | 55.51 | 28.82 | 63.6 | False |  | strong_accumulation | 1.5 | 1.94 | 3 | 3 | 7.28 | 6.09 | -15.15 | 18 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 3.57 | 9.73 | -1.69 | 95.19 | 17.34 | 95.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.58 | 2 | 1 | 2.88 | 1.1 | -27.37 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 72.07351671395091 | 95.02794974786696 | 8.32 | -17.56 | -10.15 | -0.74 | 21.9 | 21.9 | False |  | distribution_warning | -0.88 | -0.09 | 1 | 1 | -0.94 | -2.56 | -29.04 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 77.38084589596791 | 70.28827013710922 | 6.19 | -11.39 | -25.02 | 9.46 | 31.35 | 32.86 | False |  | distribution_warning | -0.2 | -0.52 | 1 | 2 | 1.7 | -3.54 | -41.39 | 11 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | 7.58 | -4.11 | -8.12 | -6.7 | 22.71 | 22.71 | False |  | strong_accumulation | 0.04 | 0.12 | 2 | 2 | 6.9 | 4.61 | -16.2 | 19 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 7.7 | 4.17 | 15.73 | 54.3 | 14.59 | 69.25 | False |  | strong_accumulation | 1.46 | 1.22 | 3 | 2 | 3.43 | 3.32 | -13.06 | 18 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 5.73 | -17.06 | 8.1 | 10.0 | 12.37 | 15.26 | False |  | distribution_warning | -0.42 | -0.36 | 1 | 1 | -2.05 | -2.54 | -28.42 | 16 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 6.22 | 3.22 | 20.36 | 151.31 | 34.61 | 156.17 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | -0.5 | 2 | 2 | 8.71 | 5.69 | -15.36 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 15.8 | 24.44 | 43.44 | 124.2 | 48.55 | 122.7 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | 0.32 | 2 | 1 | 16.34 | 16.15 | -4.03 |  | fail_low_response_condition |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | 22.97 | 14.86 | 12.96 | 12.58 | 29.52 | 29.52 | False |  | distribution_warning | -1.16 | -1.45 | 1 | 2 | 16.79 | 14.44 | -2.44 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 63.77094494612451 | 73.90317152093164 | 4.07 | -6.5 | 12.2 | 26.65 | 17.95 | 40.07 | False |  | mild_accumulation | -0.84 | 0.51 | 0 | 2 | 1.43 | 0.19 | -20.69 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 3.4 | -14.0 | 6.32 | 14.11 | 14.93 | 14.93 | False |  | distribution_warning | -4.84 | -5.29 | 0 | 0 | -0.43 | -2.64 | -30.47 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 26.61 | 18.68 | 82.55 | 85.24 | 79.29 | 152.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | 0.13 | 1 | 1 | 19.69 | 18.87 | -0.59 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | 2.59 | 12.49 | 51.76 | 73.86 | 55.09 | 97.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.02 | 0.13 | 2 | 2 | 8.26 | 8.21 | -6.33 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 0.18 | 1.07 | 9.9 | 16.22 | 9.9 | 22.25 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 0 | -0.04 | 0.06 | -11.42 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -2.78 | -12.06 | -19.17 | -18.41 | 9.38 | 9.38 | False |  | strong_accumulation | 0.1 | 0.09 | 2 | 2 | -2.67 | -5.05 | -39.97 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | 2.34 | 2.08 | 6.5 | -5.07 | 7.67 | 9.78 | False |  | distribution_warning | -0.72 | -0.6 | 1 | 2 | 2.1 | 1.99 | -3.91 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 307.65627206955537 | 402.6798478136839 | 5.16 | 17.03 | -4.52 | 38.73 | 36.81 | 54.31 | False |  | distribution_warning | -1.84 | -1.29 | 0 | 1 | 12.13 | 7.62 | -22.85 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 4.61 | -4.93 | 2.58 | 27.2 | 17.78 | 40.71 | False |  | distribution_warning | -0.49 | -0.14 | 0 | 0 | 2.37 | 0.35 | -24.29 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 22.03 | 8.43 | 44.58 | 150.0 | 52.54 | 190.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.05 | 5.15 | 2 | 2 | 19.84 | 15.14 | -12.83 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 23.97 | 8.96 | 23.81 | 80.0 | 38.87 | 95.2 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.74 | 0.0 | 2 | 0 | 17.46 | 16.61 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 10.55 | -7.56 | -0.72 | 101.83 | 27.91 | 107.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.48 | -0.18 | 1 | 1 | 5.13 | 3.91 | -20.52 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 5.88 | -0.4 | 10.53 | 53.28 | 25.37 | 74.52 | False |  | strong_accumulation | 0.8 | 1.47 | 2 | 3 | 5.51 | 3.98 | -10.0 | 19 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 133.3640235641089 | 87.69992405929172 | 14.88 | -11.2 | -37.68 | 16.87 | 36.22 | 36.22 | False |  | strong_accumulation | 1.74 | 1.94 | 2 | 2 | 7.24 | 1.89 | -44.02 |  | fail_low_response_condition |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -2.26 | 1.02 | -4.7 | 6.09 | 5.41 | 8.64 | False |  | strong_accumulation | 0.13 | 0.12 | 2 | 2 | 0.84 | -0.5 | -10.38 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | 10.48 | -17.72 | 4.0 | 29.78 | 24.8 | 38.05 | False |  | mild_accumulation | -0.01 | 0.56 | 1 | 2 | 2.71 | -1.51 | -29.86 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -1.99 | -5.53 | -0.45 | -0.89 | 3.26 | 4.47 | False |  | mild_accumulation | 0.09 | -0.06 | 2 | 2 | -0.55 | -1.91 | -21.83 | 17 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 4.6 | 3.41 | 6.64 | -6.19 | 12.81 | 12.81 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 3.49 | 3.4 | -9.0 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -3.79 | -3.39 | -0.15 | -16.26 | 5.38 | 5.38 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -4.45 | -3.5 | -15.01 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 1.14 | 2.54 | 1.49 | 15.8 | 7.65 | 31.6 | False |  | strong_accumulation | 1.41 | 1.45 | 3 | 3 | 1.06 | 1.05 | -5.84 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 93.8248443457034 | 60.82046311316634 | 3.87 | -2.14 | -8.36 | -35.6 | 9.73 | 9.73 | False |  | strong_accumulation | 0.63 | 0.48 | 3 | 2 | 1.62 | 0.79 | -24.32 | 19 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 1.22 | -4.74 | -11.24 | -10.65 | 4.74 | 4.74 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 2 | -0.45 | -1.69 | -16.92 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | 4.37 | -4.87 | 7.5 | 0.47 | 9.58 | 9.58 | False |  | strong_accumulation | 0.75 | 0.64 | 2 | 2 | 3.09 | 2.11 | -8.9 | 24 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 6.14 | 4.01 | 22.7 | 26.22 | 24.61 | 33.08 | False |  | mild_accumulation | 0.57 | 0.32 | 3 | 1 | 6.57 | 6.99 | -0.68 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -16.52 | -4.17 | 34.06 | 32.13 | 35.71 | 61.58 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 1 | -17.05 | -11.44 | -37.6 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 3.43 | 3.7 | -14.6 | -17.82 | 8.29 | 8.29 | False |  | strong_accumulation | 0.09 | 0.09 | 2 | 2 | 3.09 | 2.22 | -15.7 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 20.32 | 7.18 | 16.44 | 43.57 | 29.87 | 45.09 | False |  | mild_accumulation | -0.73 | 0.04 | 1 | 2 | 14.66 | 12.69 | -3.65 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 1.61 | -18.12 | 2.85 | 10.96 | 7.2 | 28.43 | False |  | distribution_warning | -0.45 | -0.41 | 1 | 0 | -6.56 | -4.94 | -22.39 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 39.14 | 20.83 | 23.82 | 77.74 | 71.12 | 108.71 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.07 | 2.78 | 1 | 1 | 29.28 | 24.68 | -2.13 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 21.87 | -19.85 | 1.9 | 87.72 | 47.18 | 109.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.16 | -0.49 | 2 | 1 | 8.14 | 5.05 | -30.07 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 8.43 | 24.27 | 18.16 | 70.68 | 37.22 | 83.11 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.22 | 1.02 | 3 | 2 | 15.73 | 11.09 | -6.75 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 73.91966377290892 | 26.75099850600647 | 22.83 | 27.97 | 65.93 | 86.78 | 64.48 | 103.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.89 | 2.49 | 3 | 2 | 24.6 | 22.59 | 0.0 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 117.5894936306649 | 96.80997008021892 | 7.2 | -3.79 | -18.84 | 48.27 | 21.24 | 54.63 | False |  | distribution_warning | -0.52 | -1.29 | 1 | 1 | 2.61 | 0.02 | -20.81 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | 5.67 | -3.05 | -3.99 | 59.97 | 17.92 | 73.46 | False |  | distribution_warning | -1.91 | -2.05 | 1 | 1 | 1.88 | 2.6 | -16.92 | 14 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 94.8509470404764 | 111.03077976261774 | 11.98 | 8.53 | -17.92 | 35.91 | 27.22 | 37.13 | False |  | mild_accumulation | 0.17 | 0.03 | 2 | 1 | 12.92 | 8.8 | -25.65 |  | fail_low_response_condition |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 12.87 | -4.84 | 4.03 | -2.58 | 23.37 | 23.37 | False |  | distribution_warning | -0.96 | -2.25 | 1 | 1 | 5.83 | 3.93 | -24.46 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 56.54703093190022 | 34.71282457960092 | 7.35 | -8.54 | -13.19 | 7.07 | 22.78 | 22.78 | False |  | distribution_warning | -0.33 | -0.22 | 0 | 2 | 2.5 | -1.49 | -32.86 | 13 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | 13.22 | 8.84 | 15.2 | 19.15 | 19.15 | 35.71 | False |  | mild_accumulation | 0.08 | 0.0 | 3 | 0 | 9.28 | 8.47 | -7.66 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 54.59950544814572 | 34.30071340658413 | 12.8 | -0.17 | -7.13 | 49.02 | 36.1 | 69.28 | False |  | distribution_warning | -1.25 | -1.93 | 2 | 0 | 10.36 | 4.7 | -30.04 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -0.21 | -19.82 | -27.4 | 55.47 | 7.44 | 56.73 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -7.92 | -9.35 | -42.37 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 21.91 | -30.37 | 1.34 | 71.19 | 44.96 | 104.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.65 | -0.5 | 1 | 0 | -14.52 | -6.54 | -43.53 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 17.09 | -37.6 | -9.8 | 75.57 | 41.23 | 90.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.32 | -2.67 | 0 | 1 | -2.05 | -9.48 | -55.89 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth | A_優先追蹤 | 204.3244857198993 | 247.3095962162866 | 1.88 | -1.21 | -14.44 | 44.25 | 21.64 | 63.0 | False |  | mild_accumulation | -0.54 | 1.15 | 2 | 1 | 4.3 | -0.98 | -38.72 | 21 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 22.66 | -20.7 | -16.03 | 137.75 | 50.75 | 150.0 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.61 | -0.44 | 0 | 1 | -0.81 | -1.59 | -35.47 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 7.27 | 32.9 | 34.66 | 138.97 | 44.81 | 187.57 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 21.09 | 17.4 | -6.43 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 60.760461865560174 | 88.15608743643294 | 3.76 | 34.49 | 45.66 | 49.03 | 44.03 | 57.55 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 7.78 | 7.93 | 3 | 3 | 14.35 | 11.73 | -4.69 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -0.72 | 1.84 | 13.99 | 3.36 | 14.46 | 16.39 | False |  | distribution_warning | -0.01 | -0.01 | 1 | 0 | 0.38 | 0.8 | -2.46 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 59.23071292224356 | 63.75000065335939 | 12.2 | -6.88 | -14.81 | 3.14 | 27.92 | 27.92 | False |  | distribution_warning | -1.83 | -2.16 | 0 | 1 | 5.67 | 1.58 | -32.15 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 8.24 | 6.09 | -1.63 | 80.84 | 42.68 | 111.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.86 | -0.48 | 1 | 1 | 11.32 | 7.26 | -19.4 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 28.12 | 1.75 | 26.72 | 111.29 | 58.79 | 121.1 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.4 | -2.78 | 0 | 1 | 19.49 | 15.04 | -14.38 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 9.11 | 1.41 | -1.6 | -2.27 | 14.93 | 14.93 | False |  | distribution_warning | -1.26 | -1.28 | 1 | 0 | 5.74 | 3.29 | -21.21 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 3.33 | -2.91 | 8.69 | 27.62 | 19.5 | 48.19 | False |  | mild_accumulation | 0.85 | 0.0 | 2 | 2 | 5.19 | 1.0 | -36.77 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 12.75 | -9.8 | -26.07 | -12.0 | 31.3 | 31.3 | False |  | strong_accumulation | 0.94 | 1.28 | 2 | 2 | 4.07 | -0.34 | -38.01 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 9.68 | 29.42 | 36.47 | 23.43 | 38.29 | 47.68 | True | 近20日漲幅>25% | strong_accumulation | 2.18 | 3.33 | 3 | 3 | 14.35 | 10.65 | -10.11 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 16.92 | -8.1 | -17.39 | 15.15 | 44.49 | 53.23 | False |  | distribution_warning | -1.1 | -0.18 | 1 | 2 | 10.59 | 5.96 | -24.75 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 59.590900789853706 | 37.93424741228517 | 4.53 | 17.43 | 10.05 | 74.5 | 29.97 | 70.43 | True | 近120日漲幅>70% | strong_accumulation | 1.16 | 1.54 | 2 | 2 | 4.77 | 3.07 | -14.29 |  | fail_already_priced_in |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | 12.07 | 11.11 | 9.24 | 101.55 | 27.45 | 102.18 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.95 | 1.03 | 3 | 3 | 11.85 | 11.44 | -0.38 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | 11.48 | -2.86 | -14.29 | -2.86 | 19.16 | 19.16 | False |  | mild_accumulation | -0.28 | 0.35 | 2 | 2 | 5.37 | 3.02 | -27.4 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 20.1 | -12.85 | -22.05 | -11.93 | 40.22 | 40.22 | False |  | mild_accumulation | -0.31 | 0.22 | 1 | 2 | 7.62 | 2.23 | -36.13 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 7.69 | 15.38 | 23.53 | -1.13 | 32.58 | 32.58 | False |  | mild_accumulation | 0.0 | 0.32 | 2 | 3 | 7.73 | 8.5 | -2.05 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 14.97 | 8.11 | -4.23 | 97.82 | 39.81 | 112.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.1 | -1.0 | 2 | 1 | 14.47 | 10.73 | -22.16 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 3.36 | -10.9 | -5.77 | -18.91 | 7.84 | 7.84 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.45 | -0.43 | -21.94 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | 9.85 | -8.32 | -4.92 | 26.82 | 26.64 | 34.88 | False |  | distribution_warning | -1.53 | -1.16 | 1 | 1 | 5.41 | -0.18 | -35.32 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 3.7 | 2.98 | -12.82 | 1.47 | 19.73 | 19.73 | False |  | distribution_warning | -0.28 | 0.0 | 2 | 1 | 5.49 | 3.7 | -23.25 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 9.47 | -11.86 | 15.68 | 64.3 | 19.54 | 95.49 | True | 距120日低點反彈>80% | distribution_warning | -0.87 | -1.02 | 1 | 1 | 1.61 | 1.18 | -18.43 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 0.7 | -15.59 | -12.5 | -10.31 | 9.13 | 9.13 | False |  | distribution_warning | -0.76 | -0.19 | 0 | 0 | -3.79 | -4.86 | -24.87 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | 0.0 | 1.51 | -3.0 | -22.74 | 9.81 | 9.81 | False |  | strong_accumulation | 0.03 | 0.02 | 2 | 2 | 0.69 | 0.18 | -9.53 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 18.66 | -10.16 | -16.95 | 62.92 | 34.26 | 66.48 | False |  | strong_accumulation | 0.18 | 0.04 | 2 | 2 | 7.78 | 5.01 | -34.98 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 98.74936839745938 | 71.28591290526819 | 16.87 | 22.22 | 7.47 | 39.55 | 43.48 | 64.52 | False |  | strong_accumulation | 4.71 | 2.93 | 2 | 3 | 20.22 | 13.81 | -11.09 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 18.93 | -4.62 | -28.11 | 9.89 | 37.62 | 37.62 | False |  | distribution_warning | -3.43 | -1.67 | 0 | 0 | 9.32 | 4.31 | -40.66 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 105.41523454519049 | 68.91539282131619 | 10.47 | -18.38 | -27.26 | 47.86 | 34.73 | 38.89 | False |  | distribution_warning | -6.91 | -7.91 | 1 | 1 | 1.24 | -3.64 | -42.55 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 4.22 | 6.47 | 34.81 | 33.0 | 33.9 | 51.92 | False |  | distribution_warning | -0.18 | 0.0 | 0 | 0 | 4.03 | 4.62 | -2.23 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 51.30291899664847 | 56.85528675042054 | 7.09 | 9.6 | 14.43 | 13.59 | 22.83 | 24.97 | False |  | strong_accumulation | 3.61 | 4.59 | 3 | 3 | 7.39 | 7.4 | -1.47 | 22 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 0.0 | -1.51 | -8.05 | -2.84 | 3.01 | 3.01 | False |  | distribution_warning | 0.0 | -0.14 | 2 | 2 | -1.5 | -1.21 | -22.41 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -4.34 | -0.68 | -1.56 | -15.52 | 7.82 | 7.82 | False |  | mild_accumulation | 0.11 | 0.04 | 2 | 1 | -2.62 | -1.97 | -7.74 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 0.9 | -1.39 | 3.57 | 1.16 | 7.7 | 7.7 | False |  | distribution_warning | -0.41 | -0.8 | 0 | 0 | -1.04 | -0.56 | -10.51 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 6.52 | -2.66 | 11.29 | 17.61 | 11.89 | 21.76 | False |  | mild_accumulation | 0.1 | -0.1 | 1 | 1 | -0.66 | 0.77 | -5.05 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 10.65 | 3.03 | -1.58 | 32.62 | 16.15 | 33.1 | False |  | mild_accumulation | 0.25 | 1.22 | 1 | 1 | 9.4 | 6.58 | -12.62 |  | fail_low_response_condition |