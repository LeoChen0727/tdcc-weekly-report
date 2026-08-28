# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-28 20:54:29 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 704196 |
| tdcc_rows | 1969 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 435 |
| tdcc_mild_accumulation_count | 756 |
| tdcc_distribution_warning_count | 592 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 82 |
| already_priced_in_excluded | 31 |
| overheat_pass | 51 |
| score_pass | 51 |
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
| fail_revenue_condition | 1630 |
| fail_low_response_condition | 255 |
| fail_already_priced_in | 31 |
| fail_defensive_or_traditional_excluded | 4 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_僅留完整清單 | 102.03987961747174 | 127.0977623123372 | -0.45 | 12.06 | 4.69 | -13.9 | 18.74 | 18.74 | False |  | mild_accumulation | 0.03 | 0.41 | 1 | 2 | 5.63 | 4.14 | -10.8 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 1.36 | 2.75 | -13.27 | -29.13 | 4.81 | 4.81 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 1.37 | 0.42 | -15.78 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.97 | 7.33 | 9.24 | 17.25 | 9.59 | 25.45 | False |  | distribution_warning | -0.47 | -1.3 | 1 | 0 | 1.43 | -0.0 | -14.75 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -1.67 | 9.77 | 0.85 | 0.85 | 11.32 | 11.32 | False |  | strong_accumulation | 1.61 | 1.98 | 3 | 3 | 2.77 | 2.25 | -4.45 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.0 | -2.74 | -4.83 | -6.58 | 4.11 | 4.72 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -1.03 | -1.28 | -11.91 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 1.22 | 2.89 | -10.43 | 14.75 | 5.96 | 17.45 | False |  | mild_accumulation | 0.04 | 0.09 | 1 | 3 | 0.28 | -0.56 | -25.89 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -2.96 | -1.01 | -29.76 | -42.16 | 5.36 | 5.36 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -2.38 | -4.0 | -33.56 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -1.39 | 6.79 | 3.28 | 37.38 | 15.51 | 49.58 | False |  | distribution_warning | -0.85 | -0.35 | 1 | 1 | -4.47 | -2.42 | -12.38 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 3.32 | 6.04 | -10.62 | -2.06 | 12.69 | 12.69 | False |  | mild_accumulation | 0.95 | -0.73 | 2 | 1 | 2.01 | 2.14 | -13.12 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 8.56 | 56.49 | 79.4 | 107.76 | 87.31 | 111.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.57 | 3.71 | 3 | 3 | 18.35 | 16.99 | -4.11 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -1.76 | 27.97 | 51.82 | 82.12 | 53.21 | 85.56 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.5 | -1.66 | 1 | 2 | 2.09 | 2.16 | -33.2 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -5.95 | 5.45 | 12.99 | 13.17 | 17.57 | 24.06 | False |  | strong_accumulation | 0.23 | 0.35 | 2 | 2 | 2.93 | 2.61 | -7.94 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -0.87 | 3.64 | 6.54 | -0.44 | 6.54 | 14.0 | False |  | mild_accumulation | 0.02 | -0.02 | 1 | 0 | 0.35 | 0.29 | -9.16 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | 2.71 | 9.05 | 8.16 | 24.41 | 18.3 | 27.4 | False |  | mild_accumulation | 0.3 | 0.28 | 2 | 1 | 4.85 | 4.25 | -16.4 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 6.84 | 82.17 | 167.29 | 334.65 | 189.18 | 353.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | -0.39 | 3 | 1 | 13.86 | 15.98 | -5.2 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -7.1 | -6.49 | -17.71 |  | 4.35 |  | False |  | distribution_warning | -0.36 | -0.83 | 0 | 0 | -5.62 | -4.59 | -30.43 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -0.41 | -6.9 | -12.27 | 7.05 | 6.11 | 20.3 | False |  | strong_accumulation | 0.25 | 0.75 | 2 | 2 | -5.06 | -6.03 | -35.88 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -5.98 | 5.89 | 10.74 | 28.63 | 16.48 | 31.04 | False |  | distribution_warning | -0.21 | -2.1 | 0 | 0 | 3.74 | 2.5 | -11.16 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -2.19 | -2.19 | -2.34 | -5.44 | 6.64 | 21.32 | False |  | mild_accumulation | 0.02 | 0.02 | 2 | 1 | 0.51 | -0.44 | -10.57 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 3.3 | 19.32 | 23.52 | 135.75 | 46.17 | 155.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 0.0 | 2 | 2 | 1.08 | 1.75 | -24.53 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 11.54 | -3.65 | 23.14 | 100.0 | 43.21 | 109.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.58 | -1.96 | 1 | 1 | 1.64 | -0.3 | -32.0 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 3.47 | 15.49 | -1.5 | 80.62 | 29.13 | 86.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.61 | -0.46 | 1 | 2 | 2.61 | 1.83 | -34.0 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | 3.05 | 1.0 | -18.12 | 17.95 | 11.7 | 34.93 | False |  | mild_accumulation | 0.54 | 0.51 | 1 | 1 | -0.47 | 0.88 | -18.12 | 17 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 7.76 | 18.92 | -27.2 | 137.38 | 30.78 | 145.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.42 | -2.7 | 1 | 1 | 3.45 | -0.01 | -51.07 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 180.47957329305424 | 137.8339123232017 | 3.27 | 25.87 | -21.91 | 27.78 | 37.8 | 37.8 | True | 近20日漲幅>25% | distribution_warning | -1.43 | -1.66 | 1 | 1 | 0.6 | 0.33 | -34.11 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 0.28 | 39.62 | 2.25 | 66.51 | 55.13 | 116.59 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.11 | 1.16 | 2 | 2 | 4.1 | 4.32 | -22.27 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | 4.42 | 0.0 | -17.79 | 41.2 | 15.49 | 53.99 | False |  | distribution_warning | -0.16 | -0.42 | 1 | 1 | -3.19 | -1.98 | -24.78 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | -1.14 | -7.68 | -5.05 | 23.75 | 7.72 | 25.18 | False |  | mild_accumulation | -0.19 | 0.08 | 1 | 1 | -3.81 | -2.34 | -12.0 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | -0.41 | -6.24 | -3.61 | 0.7 | 7.93 | 7.93 | False |  | distribution_warning | -1.0 | -0.05 | 0 | 1 | 1.97 | 0.34 | -12.39 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 30.87 | 64.6 | 15.42 | 173.4 | 93.15 | 181.43 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | -0.92 | 2 | 1 | 30.07 | 25.7 | -3.04 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -1.22 | 5.02 | -24.0 | 51.11 | 14.26 | 62.45 | False |  | strong_accumulation | 1.21 | 1.25 | 2 | 2 | -1.64 | -0.68 | -24.36 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 4.78 | 19.14 | 3.65 | 66.09 | 51.97 | 77.06 | True | 距60日低點反彈>50% | strong_accumulation | 1.68 | 2.45 | 3 | 3 | 7.95 | 8.84 | -5.85 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -4.29 | -4.29 | -21.02 | 34.45 | 16.18 | 42.05 | False |  | distribution_warning | -0.72 | -0.96 | 0 | 1 | -3.64 | -3.13 | -24.72 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | 2.17 | 5.28 | -20.8 | 1.57 | 16.93 | 16.93 | False |  | mild_accumulation | 0.18 | 0.56 | 1 | 2 | -1.01 | -2.01 | -31.93 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 17.1 | 42.5 | -18.41 | 24.04 | 60.28 | 60.28 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.31 | -2.95 | 0 | 1 | 14.03 | 12.61 | -28.48 |  | fail_low_response_condition |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | 0.73 | 7.98 | -15.44 | -2.68 | 16.95 | 16.95 | False |  | mild_accumulation | -0.31 | 0.16 | 2 | 2 | -0.35 | -0.02 | -17.46 | 17 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 2.8 | 3.71 | -12.53 | 53.07 | 11.86 | 57.56 | False |  | mild_accumulation | 1.25 | 0.54 | 2 | 1 | -0.64 | 0.12 | -13.18 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 3.42 | 14.07 | -20.26 | 15.25 | 19.18 | 20.69 | False |  | strong_accumulation | 0.77 | 1.19 | 2 | 3 | 3.91 | 1.85 | -19.3 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -3.35 | 15.7 | 13.66 | 111.15 | 39.69 | 116.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -1.89 | 1 | 0 | -2.25 | -0.76 | -15.15 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 3.08 | 18.83 | 30.41 | 93.91 | 49.0 | 113.4 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.69 | 2 | 1 | 1.63 | 3.76 | -5.64 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | 0.0 | 16.95 | -6.41 | 13.97 | 19.62 | 19.62 | False |  | mild_accumulation | 1.27 | 0.17 | 3 | 1 | -1.34 | 0.27 | -8.05 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | 1.42 | -2.27 | -6.93 | 0.94 | 10.26 | 30.94 | False |  | distribution_warning | -0.98 | -1.71 | 1 | 1 | -3.17 | -2.98 | -25.86 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 0.7 | -8.03 | -24.61 | -17.32 | 5.91 | 5.91 | False |  | distribution_warning | -2.15 | -2.84 | 1 | 0 | -4.7 | -5.0 | -37.65 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 2.27 | 49.79 | 34.5 | 125.47 | 67.7 | 172.04 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.09 | 4.36 | 3 | 3 | 9.46 | 10.55 | -5.1 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | 2.0 | -18.42 | 5.08 | 23.35 | 19.87 | 47.31 | False |  | distribution_warning | -2.98 | -1.29 | 2 | 2 | -10.07 | -6.55 | -27.6 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 2.01 | -2.28 | 0.54 | 0.36 | 3.33 | 10.71 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -0.24 | -0.08 | -12.68 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 1.4 | 0.55 | -30.99 | -14.39 | 13.44 | 13.44 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.37 | -0.64 | -33.03 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | -2.51 | 0.0 | 0.0 | -2.76 | 3.47 | 8.38 | False |  | distribution_warning | -0.03 | 0.0 | 2 | 2 | -0.14 | -0.3 | -5.13 | 15 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -5.92 | 0.34 | -17.88 | 30.38 | 36.11 | 41.01 | False |  | mild_accumulation | 0.25 | -0.27 | 1 | 2 | 0.26 | 1.42 | -23.24 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 0.17 | -4.79 | -16.62 | 24.89 | 6.85 | 27.65 | False |  | distribution_warning | -0.42 | -0.15 | 0 | 0 | -3.21 | -3.51 | -31.31 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 6.15 | 41.26 | 8.26 | 177.78 | 61.02 | 189.19 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.46 | 11.69 | 2 | 2 | 3.78 | 5.49 | -12.24 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 10.59 | 29.43 | 14.73 | 68.14 | 40.95 | 88.12 | True | 近20日漲幅>25%；距120日低點反彈>80% | mild_accumulation | 4.11 | -0.16 | 2 | 1 | 6.35 | 7.6 | -10.8 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 8.93 | 27.48 | -0.81 | 67.12 | 41.86 | 75.79 | True | 近20日漲幅>25% | strong_accumulation | 1.51 | 1.74 | 3 | 2 | 11.87 | 10.33 | -9.23 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 7.73 | 10.57 | 2.03 | 62.99 | 24.88 | 65.79 | False |  | mild_accumulation | -0.01 | 0.67 | 1 | 2 | 2.68 | 3.2 | -10.36 | 17 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 133.3640235641089 | 87.69992405929172 | 5.13 | 20.28 | -37.86 | -29.28 | 33.13 | 33.13 | False |  | distribution_warning | -0.35 | -0.44 | 1 | 1 | 2.68 | 1.06 | -38.31 | 17 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.72 | -4.15 | -10.52 | 1.68 | 2.97 | 3.63 | False |  | mild_accumulation | 0.53 | -0.21 | 3 | 2 | -1.33 | -1.48 | -12.45 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | 3.36 | 11.14 | -27.27 | 26.32 | 22.88 | 28.64 | False |  | strong_accumulation | 0.56 | 1.09 | 2 | 2 | 0.64 | -0.67 | -30.94 | 18 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -2.81 | 2.27 | -2.81 | -1.53 | 4.65 | 4.65 | False |  | mild_accumulation | -0.01 | 0.12 | 1 | 2 | -0.88 | -1.39 | -20.77 | 17 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 4.05 | 18.46 | 23.2 | 9.61 | 23.2 | 27.27 | False |  | mild_accumulation | 0.16 | 0.0 | 2 | 0 | 9.49 | 8.18 | -1.91 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -0.56 | -1.68 | -1.54 | -12.98 | 5.07 | 8.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.9 | 0.04 | -12.66 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -3.69 | 6.82 | 9.3 | 28.77 | 14.08 | 39.47 | False |  | strong_accumulation | 1.58 | 1.93 | 3 | 3 | 1.61 | 1.35 | -4.08 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | -1.67 | 3.51 | -16.38 | -48.66 | 8.04 | 8.04 | False |  | distribution_warning | -0.37 | -0.27 | 1 | 1 | -0.76 | -1.05 | -25.49 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 0.72 | 6.55 | -8.51 | -6.55 | 10.43 | 10.43 | False |  | mild_accumulation | -0.03 | 0.36 | 1 | 3 | 3.46 | 2.01 | -12.41 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -2.44 | -4.76 | -2.91 | -9.91 | 1.83 | 1.94 | False |  | strong_accumulation | 0.44 | 0.39 | 2 | 2 | -2.44 | -2.53 | -15.25 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | -9.71 | 17.62 | 19.61 | 33.09 | 30.08 | 38.5 | False |  | strong_accumulation | 0.87 | 1.19 | 3 | 3 | 2.64 | 2.93 | -14.72 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 2.38 | -26.35 | 1.37 | 39.73 | 22.22 | 51.61 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 1 | -3.15 | -5.15 | -41.45 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 2.3 | 2.83 | -5.21 | -26.34 | 10.5 | 10.5 | False |  | mild_accumulation | 0.08 | -2.09 | 1 | 0 | 3.45 | 2.77 | -11.7 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 11.09 | 30.62 | 15.18 | 40.0 | 36.29 | 49.28 | True | 近20日漲幅>25% | strong_accumulation | 2.81 | 3.85 | 3 | 3 | 10.46 | 10.53 | -2.57 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -1.65 | -11.85 | -5.56 | 10.19 | 1.71 | 20.81 | False |  | strong_accumulation | 1.41 | 0.19 | 3 | 2 | -3.88 | -4.89 | -26.99 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 5.07 | 49.72 | 3.85 | 64.83 | 67.39 | 83.33 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 7.48 | 7.23 | 2 | 2 | 4.06 | 6.3 | -5.6 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 1.22 | 24.66 | -13.77 | 66.83 | 37.0 | 95.29 | True | 距120日低點反彈>80% | distribution_warning | -0.24 | -0.57 | 1 | 0 | -1.4 | -1.8 | -34.9 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 17.28 | 44.83 | 17.69 | 79.2 | 66.75 | 85.12 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.41 | 2.28 | 2 | 3 | 13.39 | 15.35 | -2.61 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | 0.11 | 6.24 | 17.12 | 49.01 | 20.4 | 51.0 | False |  | mild_accumulation | 1.32 | 0.87 | 2 | 1 | -6.32 | -3.22 | -22.49 | 17 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 117.5894936306649 | 96.80997008021892 | -4.02 | 4.72 | -22.78 | 29.58 | 13.98 | 32.78 | False |  | mild_accumulation | -0.14 | 0.19 | 1 | 1 | -4.45 | -4.01 | -25.12 | 20 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | -0.88 | 1.69 | -9.26 | 48.43 | 7.65 | 50.67 | False |  | mild_accumulation | -0.82 | 0.47 | 2 | 2 | -4.25 | -3.72 | -24.16 | 18 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -4.85 | -0.25 | -32.99 | -15.33 | 8.89 | 8.89 | False |  | distribution_warning | -0.99 | -1.75 | 1 | 1 | -6.26 | -4.25 | -32.76 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 2.23 | 6.26 | -13.58 | -4.58 | 15.08 | 15.08 | False |  | mild_accumulation | 0.72 | -0.01 | 2 | 1 | 0.5 | -0.38 | -29.54 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 6.75 | 32.79 | -3.92 | 36.49 | 49.85 | 49.85 | True | 近20日漲幅>25% | mild_accumulation | 0.15 | -0.71 | 1 | 1 | 8.54 | 7.41 | -18.06 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -2.41 | 9.46 | -9.13 | 19.87 | 14.31 | 23.26 | False |  | mild_accumulation | 2.89 | 1.28 | 2 | 1 | -2.09 | -1.02 | -10.0 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -0.71 | 20.22 | -19.65 | 49.06 | 32.07 | 64.25 | False |  | distribution_warning | -2.06 | -1.76 | 1 | 1 | -2.27 | -0.9 | -28.63 | 12 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 6.58 | 17.03 | -25.39 | -13.7 | 26.0 | 26.0 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 11.2 | 7.52 | -32.42 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 17.51 | 41.04 | 26.87 | 116.47 | 62.84 | 129.32 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.92 | -5.4 | 0 | 1 | 12.83 | 7.51 | -36.57 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 5.45 | 39.2 | -18.69 | 93.33 | 52.63 | 96.61 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.89 | -5.49 | 1 | 1 | 6.47 | 1.35 | -52.33 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | 6.16 | 18.3 | -24.11 | 62.33 | 35.07 | 81.0 | True | 距120日低點反彈>80% | distribution_warning | -0.87 | -1.54 | 1 | 1 | 6.27 | 6.18 | -27.31 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 8.0 | 61.11 | -14.89 | 120.56 | 80.21 | 157.57 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.9 | -4.11 | 1 | 0 | 14.28 | 11.85 | -22.86 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -10.36 | 28.39 | 18.63 | 193.12 | 57.61 | 212.99 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 4.72 | 6.17 | -11.36 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | 1.42 | 1.14 | -8.25 | 34.34 | 28.06 | 45.31 | False |  | strong_accumulation | 3.25 | 3.26 | 2 | 2 | -4.15 | -0.72 | -13.59 | 18 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 0.71 | 1.08 | 8.46 | 4.44 | 14.63 | 18.49 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | 1.27 | 1.34 | -0.7 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.23071292224356 | 63.75000065335939 | 7.87 | 18.39 | -28.53 | 11.48 | 29.59 | 29.59 | False |  | mild_accumulation | -0.89 | 0.33 | 1 | 2 | 4.81 | 4.4 | -28.09 | 17 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 7.41 | 58.08 | 30.62 | 162.66 | 89.45 | 181.07 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.11 | 0.31 | 3 | 1 | 15.37 | 15.02 | -5.57 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 15.25 | 70.7 | 15.88 | 131.33 | 92.42 | 167.93 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.39 | 4.76 | 2 | 3 | 21.5 | 20.71 | 0.0 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 0.69 | 13.11 | -15.06 | 5.52 | 17.33 | 17.33 | False |  | mild_accumulation | 0.39 | -1.47 | 2 | 0 | 1.29 | 1.38 | -14.73 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 0.0 | 0.36 | -40.07 | 34.19 | 10.88 | 37.5 | False |  | mild_accumulation | -1.45 | 0.25 | 0 | 3 | -3.8 | -3.23 | -41.33 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 3.92 | 16.99 | -33.43 | -27.26 | 31.3 | 31.3 | False |  | mild_accumulation | 1.69 | -0.95 | 3 | 2 | 2.51 | 1.02 | -36.03 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 7.23 | 67.92 | 48.14 | 68.17 | 93.48 | 106.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.23 | -0.47 | 3 | 2 | 18.42 | 19.33 | -3.26 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 9.86 | 32.84 | -11.53 | 22.62 | 54.56 | 63.91 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.42 | -1.35 | 2 | 2 | 6.71 | 6.83 | -16.96 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -0.66 | 7.62 | 2.96 | 36.56 | 34.12 | 44.87 | False |  | strong_accumulation | 2.23 | 2.17 | 3 | 2 | 3.16 | 5.33 | -11.55 | 18 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | -9.91 | -11.11 | -15.25 | 36.05 | 0.1 | 38.5 | False |  | distribution_warning | -0.91 | -0.69 | 1 | 1 | -12.93 | -10.16 | -23.37 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -2.42 | 9.9 | -17.21 | -21.4 | 17.99 | 17.99 | False |  | strong_accumulation | 0.49 | 0.21 | 3 | 2 | 0.22 | -0.49 | -18.55 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 16.82 | 25.13 | -28.16 | -17.49 | 39.66 | 39.66 | True | 近20日漲幅>25% | distribution_warning | -0.55 | -0.64 | 0 | 2 | 10.11 | 7.25 | -36.39 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 4.02 | 14.89 | 32.52 | 1.87 | 37.37 | 37.37 | False |  | strong_accumulation | 0.29 | 0.28 | 3 | 3 | 4.6 | 5.47 | -3.03 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 6.67 | 19.67 | -7.3 | 76.33 | 33.33 | 88.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | -1.74 | 2 | 0 | 1.56 | 3.42 | -11.66 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 2.9 | 5.54 | -16.19 | -10.57 | 9.9 | 9.9 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 2.8 | 1.9 | -20.45 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 128.9172485640275 | 121.34662298357856 | 5.48 | 16.58 | -22.62 | 16.73 | 28.97 | 28.97 | False |  | distribution_warning | -1.02 | -1.25 | 1 | 0 | 3.13 | 2.19 | -34.13 | 12 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 8.89 | 20.53 | -1.29 | 15.62 | 32.27 | 32.27 | False |  | mild_accumulation | 0.5 | -0.01 | 2 | 0 | 8.68 | 9.19 | -2.27 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 3.85 | 7.89 | -17.67 | 67.76 | 17.28 | 92.67 | True | 距120日低點反彈>80% | distribution_warning | -2.79 | -2.13 | 1 | 1 | 0.12 | 0.44 | -19.61 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 1.04 | 3.56 | -17.09 | -23.82 | 10.65 | 10.65 | False |  | distribution_warning | -0.08 | -0.21 | 2 | 0 | 1.38 | -0.15 | -23.82 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -6.43 | -9.5 | -10.11 | -34.43 | 2.3 | 2.3 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -5.3 | -5.27 | -17.1 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 6.59 | 23.38 | -26.34 | 19.61 | 37.78 | 37.78 | False |  | mild_accumulation | 0.07 | 0.11 | 1 | 2 | 5.9 | 4.33 | -26.7 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 98.74936839745938 | 71.28591290526819 | -0.91 | 17.13 | -8.53 | 45.09 | 39.9 | 45.87 | False |  | mild_accumulation | -0.45 | 0.38 | 2 | 2 | 1.27 | 3.54 | -12.34 | 20 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 14.29 | 47.01 | -21.64 | 3.61 | 63.81 | 63.81 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.31 | -1.02 | 2 | 0 | 15.34 | 13.25 | -19.63 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 105.41523454519049 | 68.91539282131619 | 10.18 | 22.66 | -29.33 | -5.15 | 36.13 | 36.13 | False |  | distribution_warning | -18.41 | -18.98 | 0 | 1 | 4.66 | 2.96 | -41.96 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -1.83 | 2.46 | 12.61 | 34.41 | 18.67 | 38.38 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -1.79 | -1.14 | -7.18 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -0.13 | -5.83 | -15.85 | -1.65 | 1.71 | 3.47 | False |  | distribution_warning | -5.63 | -6.23 | 1 | 1 | -6.49 | -4.53 | -18.42 | 14 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | -2.18 | -3.24 | -17.59 | -3.68 | 2.28 | 2.28 | False |  | distribution_warning | -0.45 | -0.34 | 1 | 1 | -1.37 | -2.08 | -25.15 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -1.77 | -3.7 | 1.14 | -11.04 | 4.24 | 8.31 | False |  | distribution_warning | -0.03 | -0.02 | 0 | 0 | -0.23 | -0.31 | -7.32 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | -6.34 | -2.96 | 2.31 | -0.13 | 2.45 | 3.58 | False |  | distribution_warning | 0.0 | -0.2 | 1 | 1 | -3.68 | -3.67 | -13.94 | 16 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | -2.06 | 5.83 | 2.83 | 11.37 | 8.25 | 15.11 | False |  | mild_accumulation | 0.16 | 0.83 | 1 | 2 | 1.04 | -0.12 | -5.66 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | -0.96 | 54.35 | 30.13 | 57.67 | 59.63 | 65.27 | True | 近20日漲幅>25%；距60日低點反彈>50% | strong_accumulation | 2.88 | 4.45 | 2 | 2 | 19.04 | 17.77 | -3.38 |  | fail_low_response_condition |