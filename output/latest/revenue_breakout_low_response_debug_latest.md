# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-03 19:36:46 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 712000 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 437 |
| tdcc_mild_accumulation_count | 765 |
| tdcc_distribution_warning_count | 580 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 119 |
| already_priced_in_excluded | 49 |
| overheat_pass | 70 |
| score_pass | 70 |
| theme_priority_pass | 67 |
| final_rows | 67 |

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
| fail_low_response_condition | 218 |
| fail_already_priced_in | 49 |
| fail_defensive_or_traditional_excluded | 2 |
| missing_or_insufficient_price_metrics | 1 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | -8.51 | 6.44 | 2.87 | -16.67 | 14.48 | 14.48 | False |  | mild_accumulation | -0.39 | 0.25 | 0 | 2 | 0.28 | -0.0 | -14.0 | 17 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -1.71 | 1.98 | -6.01 | -26.07 | 3.41 | 3.41 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | -0.6 | -0.92 | -16.91 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -1.92 | 0.49 | -8.52 | 15.25 | 7.48 | 23.04 | False |  | mild_accumulation | 0.36 | 0.0 | 2 | 0 | -0.97 | -1.56 | -16.39 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -0.85 | 8.84 | 6.85 | -0.43 | 10.38 | 10.38 | False |  | strong_accumulation | 1.99 | 1.33 | 3 | 2 | 0.26 | 0.92 | -5.26 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -2.79 | -4.12 | -7.18 | -7.67 | 2.35 | 2.95 | False |  | mild_accumulation | 0.03 | -0.01 | 3 | 0 | -2.14 | -2.37 | -13.4 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -2.41 | -2.41 | -25.69 | 2.1 | 3.4 | 10.45 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -2.1 | -2.49 | -27.68 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -3.69 | -9.18 | -30.34 | -37.34 | 3.99 | 3.99 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.22 | -4.71 | -35.36 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -7.09 | -11.86 | 5.36 | 34.15 | 11.34 | 45.35 | False |  | mild_accumulation | -0.61 | 0.79 | 1 | 2 | -6.32 | -4.36 | -14.86 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -2.83 | 2.33 | -12.03 | -6.06 | 10.18 | 10.18 | False |  | mild_accumulation | 0.93 | -0.73 | 2 | 1 | -0.87 | -0.32 | -15.05 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -2.05 | 20.98 | 65.19 | 82.79 | 63.17 | 87.92 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.82 | 2 | 2 | 3.37 | 4.62 | -11.27 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 0.0 | 2.16 | 19.06 | 71.86 | 32.93 | 83.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.63 | 1 | 2 | -1.68 | -0.48 | -33.8 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -0.42 | 12.4 | 15.67 | 14.19 | 20.95 | 27.63 | False |  | strong_accumulation | 0.63 | 0.7 | 3 | 3 | 4.28 | 4.47 | -5.29 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -2.61 | 1.82 | 0.45 | -0.88 | 4.67 | 12.0 | False |  | mild_accumulation | 0.03 | -0.01 | 2 | 1 | -1.75 | -1.19 | -8.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -4.17 | 4.98 | -17.32 | 18.22 | 12.95 | 21.63 | False |  | mild_accumulation | 0.7 | 0.28 | 2 | 1 | -1.15 | -0.61 | -17.32 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -6.21 | 33.17 | 97.94 | 294.43 | 120.85 | 326.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | -1.97 | 3 | 0 | -0.05 | 5.19 | -10.84 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -7.69 | -9.21 | -26.98 |  | 0.0 |  | False |  | distribution_warning | -0.26 | -0.7 | 0 | 0 | -7.26 | -6.55 | -27.18 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 3.32 | -8.12 | -7.09 | 13.7 | 8.73 | 23.27 | False |  | mild_accumulation | 1.06 | -0.99 | 2 | 1 | -0.24 | -1.88 | -34.3 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -0.8 | 5.83 | 9.4 | 18.65 | 14.05 | 28.27 | False |  | distribution_warning | -0.41 | -2.1 | 0 | 0 | 0.55 | 0.2 | -12.85 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -4.75 | 0.5 | -1.15 | -5.79 | 2.56 | 16.67 | False |  | mild_accumulation | 0.04 | 0.02 | 2 | 1 | -3.7 | -3.76 | -14.0 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -3.75 | -1.63 | 24.74 | 122.31 | 41.17 | 146.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.14 | -0.76 | 2 | 1 | -3.04 | -1.83 | -27.11 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 2.21 | 13.8 | 30.87 | 100.0 | 39.35 | 117.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.43 | 2 | 2 | 5.6 | 2.59 | -29.43 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | -4.67 | -5.85 | -9.2 | 36.0 | 20.47 | 65.23 | False |  | distribution_warning | -1.0 | -1.51 | 0 | 1 | -4.78 | -4.79 | -38.43 | 13 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | -1.79 | -6.43 | -10.81 | 17.86 | 9.27 | 32.0 | False |  | distribution_warning | -0.39 | -0.34 | 0 | 0 | -2.22 | -1.33 | -10.16 | 13 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -7.93 | -10.35 | -38.14 | 82.17 | 11.94 | 110.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.21 | -2.24 | 1 | 1 | -10.66 | -11.92 | -58.11 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -8.24 | -9.3 | -19.59 | -18.47 | 27.45 | 27.45 | False |  | distribution_warning | -1.54 | -1.3 | 1 | 1 | -7.38 | -6.28 | -39.06 | 16 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -9.14 | -1.17 | 7.99 | 32.03 | 44.44 | 101.67 | True | 距120日低點反彈>80% | strong_accumulation | 0.68 | 0.62 | 2 | 2 | -4.88 | -3.23 | -27.62 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | 0.0 | -13.28 | -15.56 | 30.62 | 13.59 | 39.8 | False |  | distribution_warning | -0.19 | -0.04 | 1 | 1 | -2.61 | -2.94 | -26.02 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | -0.46 | -8.76 | -5.05 | 8.0 | 7.6 | 15.51 | False |  | distribution_warning | -0.46 | -0.37 | 0 | 0 | -2.27 | -1.85 | -12.11 | 18 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | -0.84 | 2.16 | 0.14 | -12.0 | 6.44 | 6.44 | False |  | distribution_warning | -0.18 | -0.07 | 1 | 1 | 0.35 | -0.67 | -13.61 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | -7.08 | 30.03 | 15.84 | 128.72 | 79.84 | 154.28 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.73 | 3.55 | 2 | 1 | 13.47 | 10.75 | -9.72 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -0.91 | -0.76 | -7.93 | 46.56 | 14.44 | 62.7 | False |  | strong_accumulation | 0.84 | 0.76 | 2 | 2 | -1.78 | -0.89 | -11.56 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 0.31 | 18.7 | 14.24 | 63.47 | 52.91 | 78.17 | True | 距60日低點反彈>50% | strong_accumulation | 0.83 | 1.54 | 3 | 3 | 4.36 | 5.66 | -5.27 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | 1.26 | 2.03 | -15.69 | 28.75 | 16.47 | 37.54 | False |  | distribution_warning | -0.15 | -0.86 | 1 | 1 | -3.94 | -1.79 | -17.25 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | -1.18 | -5.47 | -14.07 | -5.11 | 13.09 | 13.09 | False |  | distribution_warning | -1.07 | -0.33 | 0 | 1 | -3.96 | -4.17 | -34.17 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 6.8 | 11.68 | -26.42 | 19.96 | 56.03 | 56.03 | True | 距60日低點反彈>50% | distribution_warning | -1.22 | -1.32 | 0 | 2 | 5.82 | 4.71 | -30.38 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -1.74 | -2.44 | -9.1 | -6.99 | 15.08 | 15.08 | False |  | distribution_warning | -0.67 | -0.54 | 1 | 2 | -2.07 | -1.54 | -16.99 | 10 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 1.59 | 1.89 | -2.37 | 40.48 | 12.34 | 58.24 | False |  | mild_accumulation | 0.66 | 0.25 | 1 | 1 | -1.43 | -0.16 | -12.81 | 16 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 0.45 | 10.93 | -10.67 | 14.33 | 20.07 | 21.6 | False |  | distribution_warning | -0.06 | -0.01 | 1 | 2 | 2.3 | 1.56 | -14.76 | 17 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -3.82 | -0.28 | 4.44 | 95.93 | 34.61 | 103.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.59 | -1.21 | 1 | 0 | -6.8 | -3.99 | -18.24 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -0.15 | 8.36 | 37.69 | 93.12 | 50.11 | 114.99 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.75 | 1 | 1 | -0.24 | 2.51 | -5.73 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -3.76 | -0.65 | -0.49 | 10.04 | 16.95 | 16.95 | False |  | mild_accumulation | 0.93 | -0.05 | 2 | 0 | -4.53 | -1.85 | -9.84 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | -3.72 | -11.54 | -13.03 | 10.34 | 6.15 | 26.07 | False |  | distribution_warning | -0.12 | -1.22 | 2 | 1 | -5.59 | -5.22 | -28.62 | 11 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -5.75 | -15.86 | -22.71 | -26.69 | 0.19 | 0.19 | False |  | distribution_warning | -1.76 | -2.67 | 1 | 0 | -7.59 | -8.21 | -41.13 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | -11.74 | 4.03 | 31.54 | 73.01 | 48.29 | 140.55 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.83 | 2.98 | 3 | 3 | -6.25 | -3.61 | -16.08 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -4.22 | -24.51 | 5.98 | 17.45 | 9.98 | 39.81 | False |  | distribution_warning | -4.47 | -0.95 | 2 | 2 | -9.67 | -8.82 | -31.29 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -3.93 | -5.28 | -5.78 | -5.45 | 0.0 | 6.75 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -3.09 | -3.03 | -15.81 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 21.82 | 25.64 | -1.56 | 6.78 | 37.81 | 37.81 | True | 近20日漲幅>25% | neutral | 0.0 | 0.0 | 0 | 0 | 19.37 | 17.86 | -7.35 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 233.9341638249008 | 396.6930034235488 | -1.78 | 1.58 | -1.03 | -9.18 | 2.93 | 7.82 | False |  | strong_accumulation | 0.46 | 0.98 | 2 | 2 | -0.9 | -0.57 | -5.62 | 21 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -4.03 | -2.39 | -6.54 | -8.77 | 32.41 | 37.17 | False |  | strong_accumulation | 1.28 | 0.02 | 2 | 2 | -2.98 | -1.62 | -13.2 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -3.91 | -9.02 | -9.46 | 7.62 | 4.63 | 17.95 | False |  | distribution_warning | -0.12 | -0.08 | 1 | 1 | -3.7 | -4.22 | -32.74 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 5.21 | 24.72 | 48.0 | 178.89 | 88.14 | 237.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.41 | 10.78 | 2 | 2 | 17.07 | 19.63 | 0.0 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 0.84 | 12.51 | 19.35 | 50.78 | 42.73 | 90.5 | True | 距120日低點反彈>80% | strong_accumulation | 2.38 | 3.25 | 2 | 2 | 3.85 | 5.58 | -10.51 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | 1.71 | 14.64 | 3.66 | 48.38 | 38.37 | 71.47 | False |  | mild_accumulation | 1.42 | -0.27 | 3 | 2 | 5.22 | 4.47 | -11.46 | 22 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 54.39975818511566 | 39.61008944759205 | -3.16 | -3.92 | -2.39 | 42.94 | 21.89 | 52.74 | False |  | distribution_warning | -0.13 | -0.85 | 1 | 1 | -0.22 | -0.12 | -12.5 | 11 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -7.5 | -0.73 | -40.15 | -49.12 | 26.01 | 26.01 | False |  | mild_accumulation | 0.62 | 0.52 | 2 | 1 | -3.67 | -4.04 | -41.61 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.21 | -0.41 | -8.85 | 0.0 | 2.76 | 3.42 | False |  | distribution_warning | -0.11 | -0.27 | 2 | 2 | -1.26 | -1.17 | -12.64 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | -3.91 | -5.38 | -26.79 | 2.64 | 18.08 | 18.08 | False |  | strong_accumulation | 0.95 | 0.53 | 3 | 2 | -3.43 | -3.9 | -33.63 | 17 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -1.75 | 2.27 | -7.02 | -4.05 | 4.65 | 4.65 | False |  | strong_accumulation | 0.25 | 0.36 | 2 | 2 | -1.03 | -0.94 | -20.77 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -2.61 | 15.44 | 15.0 | 5.28 | 16.34 | 23.55 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 3.32 | 3.19 | -4.78 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -4.23 | -0.15 | -0.29 | -13.71 | 0.89 | 4.62 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.3 | -2.78 | -15.63 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 1.88 | 10.32 | 12.62 | 33.29 | 15.97 | 44.36 | False |  | strong_accumulation | 1.8 | 1.95 | 3 | 3 | 3.5 | 3.93 | -0.71 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | -0.65 | 1.72 | -21.57 | -44.98 | 8.18 | 8.18 | False |  | mild_accumulation | -0.46 | 0.04 | 0 | 2 | -1.38 | -0.94 | -25.39 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -1.7 | 8.62 | -7.35 | -5.46 | 9.48 | 9.48 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 2 | 1.3 | 0.99 | -13.16 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -1.09 | -3.48 | -9.59 | -10.4 | 1.73 | 1.83 | False |  | strong_accumulation | 0.23 | 0.17 | 2 | 2 | -1.9 | -1.84 | -15.34 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 5.5 | 16.73 | 23.36 | 39.19 | 40.96 | 49.85 | False |  | strong_accumulation | 0.68 | 0.42 | 3 | 2 | 8.32 | 8.97 | -7.59 | 16 | selected |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 78.98535443204022 | 130.25483155637795 | 8.39 | 2.09 | 5.71 | 53.42 | 14.36 | 59.67 | False |  | distribution_warning | -0.43 | -0.47 | 1 | 1 | 4.16 | 4.54 | -5.26 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 51.29772013409098 | 54.61796290315564 | 8.26 | 10.08 | 24.38 | 32.92 | 31.08 | 48.69 | False |  | mild_accumulation | 0.01 | 0.08 | 1 | 2 | 6.67 | 6.16 | -1.27 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -13.05 | -16.13 | 8.49 | 25.8 | 11.82 | 38.71 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -7.29 | -10.2 | -46.43 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 2.6 | 8.24 | -7.29 | -24.23 | 8.84 | 8.84 | False |  | mild_accumulation | 0.1 | -2.07 | 1 | 0 | 0.54 | 0.79 | -11.66 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -5.08 | 7.57 | 1.87 | 28.74 | 23.63 | 35.4 | False |  | strong_accumulation | 2.93 | 2.89 | 3 | 2 | -2.44 | -0.75 | -11.62 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 53.03493307821629 | 37.31355708857018 | 1.23 | -4.65 | -8.55 | 15.49 | 5.13 | 24.87 | False |  | mild_accumulation | 0.36 | -0.03 | 2 | 2 | 0.41 | -0.62 | -24.54 | 15 | selected |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 1.09 | 7.36 | 29.14 | 29.74 | 72.05 | 88.44 | True | 距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 2.26 | 2.16 | 2 | 2 | 2.66 | 5.78 | -10.5 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -1.6 | -5.02 | -12.23 | 50.08 | 35.21 | 92.75 | True | 距120日低點反彈>80% | mild_accumulation | -0.79 | 0.21 | 0 | 1 | -3.41 | -3.0 | -35.75 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | -1.2 | 12.24 | 29.67 | 78.38 | 63.77 | 79.84 | True | 距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 1.03 | 1.27 | 1 | 2 | 6.64 | 8.44 | -6.38 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | -4.7 | -13.23 | 0.35 | 39.97 | 12.95 | 44.61 | False |  | mild_accumulation | -0.42 | 1.72 | 1 | 2 | -8.56 | -5.55 | -25.15 | 16 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -2.29 | -11.85 | -17.74 | 8.66 | 13.27 | 31.96 | False |  | distribution_warning | -1.06 | -1.12 | 0 | 0 | -3.86 | -3.65 | -24.97 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -2.32 | -7.73 | -13.43 | 27.42 | 5.5 | 40.16 | False |  | distribution_warning | -2.09 | -0.79 | 1 | 2 | -4.85 | -4.2 | -25.67 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.3 | -18.42 | -23.8 | -25.59 | 5.83 | 5.83 | False |  | distribution_warning | -1.93 | -2.31 | 0 | 0 | -6.53 | -5.22 | -24.1 | 12 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 0.88 | 1.1 | -2.96 | -3.77 | 15.33 | 15.33 | False |  | strong_accumulation | 0.08 | 0.92 | 2 | 2 | 0.08 | -0.38 | -29.38 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.54703093190022 | 34.71282457960092 | 1.35 | 22.64 | -2.5 | 30.52 | 49.08 | 49.08 | False |  | mild_accumulation | 0.14 | -0.01 | 1 | 1 | 3.11 | 4.13 | -18.48 | 18 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -4.68 | -1.43 | -5.5 | 13.29 | 10.89 | 19.57 | False |  | mild_accumulation | 2.7 | 0.0 | 1 | 1 | -5.64 | -3.36 | -12.7 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -6.76 | -10.27 | -26.82 | 26.72 | 24.47 | 54.8 | False |  | distribution_warning | -0.29 | -0.7 | 1 | 1 | -7.31 | -5.53 | -32.73 | 11 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 2.58 | 10.74 | -20.99 | -38.32 | 23.78 | 23.78 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 6.05 | 3.2 | -22.64 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 5.22 | 18.55 | 49.2 | 117.97 | 67.31 | 135.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.31 | -5.15 | 0 | 1 | 10.76 | 7.11 | -34.83 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -3.56 | 4.84 | -29.35 | 63.32 | 42.54 | 80.16 | True | 距120日低點反彈>80% | distribution_warning | -4.21 | -3.49 | 1 | 1 | -3.39 | -4.96 | -55.48 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 204.3244857198993 | 247.3095962162866 | -5.48 | -7.51 | -20.32 | 32.69 | 28.73 | 72.5 | False |  | distribution_warning | -1.43 | -1.72 | 0 | 1 | 0.82 | 0.29 | -22.3 | 16 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | -1.62 | 3.55 | -23.24 | 109.17 | 68.01 | 140.13 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.83 | -7.13 | 1 | 0 | 1.88 | 1.22 | -28.08 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -11.8 | 5.65 | 7.52 | 157.82 | 38.26 | 174.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.43 | -1.57 | 1 | 0 | -9.73 | -6.17 | -22.24 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 5.01 | -0.53 | 13.9 | 44.44 | 35.61 | 53.88 | False |  | distribution_warning | -0.27 | -0.36 | 1 | 1 | 2.32 | 4.35 | -8.5 | 11 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -2.84 | -0.36 | 8.3 | 2.62 | 9.6 | 15.13 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | -1.65 | -1.39 | -3.52 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | -2.69 | -5.24 | -23.59 | -3.56 | 20.69 | 20.69 | False |  | distribution_warning | -0.78 | -0.53 | 1 | 1 | -2.78 | -2.77 | -27.42 | 12 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | -2.03 | 29.46 | 34.57 | 130.62 | 82.68 | 171.03 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.42 | 2 | 1 | 4.64 | 6.67 | -10.63 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -4.15 | 12.72 | 9.27 | 97.5 | 67.88 | 133.76 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.94 | 4.34 | 2 | 3 | 0.07 | 0.95 | -15.16 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 0.92 | 2.56 | -12.7 | -1.12 | 17.33 | 17.33 | False |  | mild_accumulation | 0.14 | -1.25 | 2 | 0 | -0.44 | 0.45 | -13.73 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -2.02 | -8.75 | -38.05 | 28.95 | 9.28 | 34.86 | False |  | distribution_warning | -0.42 | -0.14 | 1 | 2 | -4.09 | -3.73 | -40.29 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | B_可觀察 | 1057.5663716814158 | 435.6709565602183 | -4.47 | -2.06 | -36.43 | -30.49 | 24.45 | 24.45 | False |  | strong_accumulation | 0.48 | 0.37 | 2 | 3 | -3.6 | -3.69 | -37.82 | 21 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | -0.53 | 26.18 | 42.69 | 41.08 | 87.79 | 100.54 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.15 | -0.41 | 2 | 2 | 7.71 | 9.5 | -7.88 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 4.65 | 10.66 | -4.71 | 22.73 | 53.99 | 63.31 | True | 距60日低點反彈>50% | distribution_warning | -1.41 | -4.39 | 1 | 1 | 2.69 | 3.69 | -17.26 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.590900789853706 | 37.93424741228517 | 2.19 | -11.39 | 0.24 | 20.69 | 24.63 | 25.37 | False |  | distribution_warning | -0.16 | -0.27 | 2 | 1 | -3.34 | -2.65 | -17.81 | 12 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 0.49 | -18.73 | -7.69 | 9.56 | 4.94 | 17.92 | False |  | distribution_warning | -2.05 | -2.31 | 0 | 0 | -7.82 | -5.83 | -21.84 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -2.91 | 2.56 | -17.01 | -19.35 | 16.82 | 16.82 | False |  | mild_accumulation | 0.51 | -0.01 | 3 | 1 | -1.91 | -1.31 | -19.03 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 69.6507119471058 | 40.90376378051168 | 1.29 | 1.29 | -32.38 | -31.99 | 31.84 | 31.84 | False |  | mild_accumulation | 0.01 | -0.77 | 1 | 2 | 1.24 | -0.55 | -39.95 | 18 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 5.25 | 15.31 | 31.23 | 3.51 | 37.16 | 41.67 | False |  | strong_accumulation | 0.27 | 0.26 | 2 | 2 | 4.87 | 6.13 | -0.71 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 7.19 | 5.72 | 7.94 | 90.91 | 42.59 | 101.75 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.85 | 2 | 1 | 6.48 | 7.32 | -8.33 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -0.38 | 3.33 | -10.81 | -13.01 | 8.87 | 8.87 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 1.14 | 0.76 | -14.84 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 128.9172485640275 | 121.34662298357856 | -6.69 | -5.94 | -36.69 | -0.72 | 19.8 | 19.8 | False |  | mild_accumulation | -0.71 | 0.58 | 1 | 1 | -4.52 | -4.54 | -38.81 | 17 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 3.36 | 11.66 | 6.06 | 9.73 | 35.33 | 35.33 | False |  | mild_accumulation | 1.43 | 1.47 | 2 | 1 | 8.49 | 8.33 | -3.79 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -6.57 | -10.46 | -19.08 | 56.47 | 10.64 | 81.77 | True | 距120日低點反彈>80% | distribution_warning | -3.78 | -3.03 | 0 | 0 | -4.98 | -4.43 | -21.06 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -5.86 | -5.21 | -15.74 | -28.91 | 3.8 | 3.8 | False |  | mild_accumulation | 0.21 | 0.38 | 3 | 1 | -4.26 | -5.18 | -28.53 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -4.47 | -10.02 | -14.59 | -31.9 | 8.07 | 8.07 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -5.28 | -5.08 | -18.13 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth | B_可觀察 | 98.63908131175776 | 47.622431626136766 | 1.71 | 14.81 | -17.9 | 14.31 | 43.52 | 43.52 | False |  | strong_accumulation | 0.22 | 0.19 | 2 | 2 | 5.79 | 5.1 | -21.4 | 19 | selected |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | -1.09 | -2.68 | -4.72 | 10.55 | 39.39 | 39.39 | False |  | distribution_warning | -4.56 | -1.03 | 2 | 1 | -0.22 | 1.87 | -6.52 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 0.58 | 24.55 | -10.39 | -3.63 | 64.29 | 64.29 | True | 距60日低點反彈>50% | mild_accumulation | 1.69 | -0.67 | 2 | 1 | 9.47 | 8.61 | -11.31 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 105.41523454519049 | 68.91539282131619 | -8.75 | -10.64 | -30.7 | -19.87 | 20.76 | 20.76 | False |  | mild_accumulation | -1.03 | 0.38 | 1 | 2 | -6.5 | -7.44 | -48.51 | 20 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -1.84 | -0.8 | 6.25 | 35.02 | 8.41 | 38.01 | False |  | mild_accumulation | 0.22 | 0.0 | 2 | 0 | -1.84 | -1.25 | -7.43 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -3.1 | -18.19 | -11.54 | -5.53 | 0.13 | 0.27 | False |  | distribution_warning | -8.96 | -8.86 | 0 | 1 | -6.34 | -5.88 | -20.95 | 11 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 0.0 | 0.0 | -16.05 | -9.12 | 3.91 | 3.91 | False |  | distribution_warning | -0.45 | -0.52 | 1 | 0 | 0.7 | 0.07 | -23.96 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -0.68 | 1.15 | 2.09 | -14.56 | 3.53 | 7.58 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -0.17 | -0.63 | -7.95 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 1.19 | -1.54 | -1.42 | -1.79 | 2.27 | 5.36 | False |  | distribution_warning | -0.32 | -0.29 | 1 | 1 | -1.59 | -1.24 | -12.46 |  | fail_low_response_condition |