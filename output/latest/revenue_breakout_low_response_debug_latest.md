# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-25 19:48:46 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 698308 |
| tdcc_rows | 1969 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 435 |
| tdcc_mild_accumulation_count | 756 |
| tdcc_distribution_warning_count | 592 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 88 |
| already_priced_in_excluded | 38 |
| overheat_pass | 50 |
| score_pass | 50 |
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
| fail_low_response_condition | 249 |
| fail_already_priced_in | 38 |
| fail_defensive_or_traditional_excluded | 3 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1229 | 聯華 | 食品工業 | defensive_or_traditional |  | 114.98296171902771 | -4.952739530778521 | 1.83 | 1.96 | 4.51 | -4.36 | 5.04 | 9.74 | False |  | mild_accumulation | 0.1 | -0.16 | 2 | 2 | 1.56 | 0.9 | -7.13 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | 5.74 | 10.61 | 9.41 | -11.95 | 17.68 | 17.68 | False |  | mild_accumulation | 0.03 | 0.41 | 1 | 2 | 7.36 | 5.49 | -7.53 | 18 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 5.13 | 2.5 | -2.74 | -24.61 | 6.81 | 6.81 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 3.85 | 2.69 | -14.17 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 1.48 | -2.37 | 12.45 | 8.76 | 13.19 | 24.25 | False |  | distribution_warning | -0.47 | -1.3 | 1 | 0 | 0.91 | -1.01 | -15.57 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 1.71 | 10.19 | 7.21 | 3.93 | 12.26 | 12.26 | False |  | strong_accumulation | 1.61 | 1.98 | 3 | 3 | 5.15 | 3.9 | -3.64 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.0 | -4.3 | -3.78 | -6.32 | 4.4 | 5.01 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -1.03 | -1.17 | -11.66 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 3.28 | 2.86 | -1.56 | 22.33 | 7.23 | 20.57 | False |  | mild_accumulation | 0.04 | 0.09 | 1 | 3 | 2.21 | 0.54 | -25.0 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 1.69 | -6.25 | -27.54 | -33.63 | 5.63 | 5.63 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -1.07 | -3.28 | -32.43 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -1.35 | 6.96 | 4.29 | 50.67 | 19.18 | 54.33 | False |  | distribution_warning | -0.85 | -0.35 | 1 | 1 | -0.17 | 0.75 | -9.6 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 3.25 | 4.47 | -5.92 | -5.02 | 10.74 | 10.74 | False |  | mild_accumulation | 0.95 | -0.73 | 2 | 1 | 1.44 | 0.9 | -14.62 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 3.21 | 37.47 | 73.97 | 98.53 | 76.24 | 100.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.57 | 3.71 | 3 | 3 | 17.77 | 14.62 | -7.02 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -2.37 | 20.88 | 73.68 | 69.06 | 73.5 | 83.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.5 | -1.66 | 1 | 2 | 4.36 | 1.41 | -34.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral |  | 3460.154507547597 | 13488.270126747157 | 10.65 | 15.03 | 23.22 | 27.54 | 27.54 | 29.59 | False |  | strong_accumulation | 0.23 | 0.35 | 2 | 2 | 9.04 | 8.62 | -3.84 |  | fail_low_response_condition |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | 1.75 | 6.42 | 14.85 | 4.04 | 14.85 | 16.0 | False |  | mild_accumulation | 0.02 | -0.02 | 1 | 0 | 2.81 | 2.43 | -7.57 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | 1.97 | 10.21 | 8.82 | 21.03 | 15.62 | 24.52 | False |  | mild_accumulation | 0.3 | 0.28 | 2 | 1 | 3.83 | 3.31 | -18.3 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -0.59 | 91.74 | 182.03 | 376.17 | 188.88 | 373.01 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | -0.39 | 3 | 1 | 24.13 | 21.9 | -5.3 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -1.65 | -2.61 | -12.61 |  | 7.97 |  | False |  | distribution_warning | -0.36 | -0.83 | 0 | 0 | -2.6 | -1.97 | -28.02 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -1.21 | -6.84 | -10.26 | 12.39 | 6.99 | 21.29 | False |  | strong_accumulation | 0.25 | 0.75 | 2 | 2 | -5.44 | -7.12 | -35.36 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | 6.0 | 6.71 | 15.43 | 30.86 | 17.78 | 32.5 | False |  | distribution_warning | -0.21 | -2.1 | 0 | 0 | 6.1 | 4.47 | -10.17 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -0.48 | -1.43 | 2.82 | -7.88 | 5.62 | 20.16 | False |  | mild_accumulation | 0.02 | 0.02 | 2 | 1 | -0.63 | -1.35 | -11.43 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -8.17 | 9.76 | 10.93 | 146.15 | 38.67 | 142.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 0.0 | 2 | 2 | -0.86 | -2.71 | -28.4 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 2.17 | -7.54 | 18.49 | 133.06 | 39.26 | 127.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.58 | -1.96 | 1 | 1 | -0.41 | -2.38 | -33.88 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | -1.89 | 9.47 | -7.42 | 79.52 | 22.83 | 77.27 | True | 近120日漲幅>70% | distribution_warning | -0.61 | -0.46 | 1 | 2 | 0.03 | -2.98 | -37.22 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | -2.41 | 2.1 | -15.92 | 15.44 | 7.28 | 29.6 | False |  | mild_accumulation | 0.54 | 0.51 | 1 | 1 | -3.75 | -3.11 | -22.61 | 16 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -5.56 | -3.37 | -26.29 | 118.91 | 19.17 | 123.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.42 | -2.7 | 1 | 1 | -3.87 | -10.34 | -55.41 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 0.0 | 7.96 | -26.73 | 32.18 | 32.9 | 37.39 | False |  | distribution_warning | -1.43 | -1.66 | 1 | 1 | 0.42 | -3.14 | -36.46 | 18 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 1.42 | 24.31 | 13.29 | 77.23 | 52.99 | 113.6 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.11 | 1.16 | 2 | 2 | 7.95 | 4.5 | -23.34 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -8.76 | -0.49 | -16.46 | 47.1 | 10.33 | 47.1 | False |  | distribution_warning | -0.16 | -0.42 | 1 | 1 | -6.88 | -7.33 | -28.14 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | 0.81 | 0.81 | 0.93 | 26.57 | 7.97 | 27.13 | False |  | mild_accumulation | -0.19 | 0.08 | 1 | 1 | -3.85 | -2.71 | -11.8 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 1.01 | -8.25 | 2.94 | 2.19 | 4.94 | 4.94 | False |  | distribution_warning | -1.0 | -0.05 | 0 | 1 | -1.8 | -2.53 | -14.82 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 13.35 | 38.06 | -3.86 | 150.0 | 60.89 | 147.21 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | -0.92 | 2 | 1 | 17.58 | 12.24 | -14.38 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 0.77 | 11.22 | -6.84 | 63.3 | 15.14 | 63.7 | False |  | strong_accumulation | 1.21 | 1.25 | 2 | 2 | 0.46 | 0.26 | -26.19 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 1.65 | 25.85 | 21.55 | 78.92 | 45.67 | 77.54 | True | 近20日漲幅>25%；近120日漲幅>70% | strong_accumulation | 1.68 | 2.45 | 3 | 3 | 7.04 | 7.25 | -9.76 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -14.75 | 1.29 | -22.02 | 58.47 | 13.58 | 49.43 | False |  | distribution_warning | -0.72 | -0.96 | 0 | 1 | -5.49 | -6.39 | -27.49 | 16 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | -1.75 | 2.44 | -24.66 | 7.23 | 13.77 | 13.77 | False |  | mild_accumulation | 0.18 | 0.56 | 1 | 2 | -2.35 | -5.5 | -33.77 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 77.38084589596791 | 70.28827013710922 | -9.25 | 20.02 | -26.44 | 27.6 | 37.73 | 37.73 | False |  | distribution_warning | -1.31 | -2.95 | 0 | 1 | 2.95 | -1.31 | -38.54 | 13 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | -3.46 | 4.69 | -19.59 | -1.91 | 13.39 | 13.39 | False |  | mild_accumulation | -0.31 | 0.16 | 2 | 2 | -1.82 | -2.91 | -22.57 | 17 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | -0.14 | 6.27 | -6.08 | 61.63 | 11.38 | 60.51 | False |  | mild_accumulation | 1.25 | 0.54 | 2 | 1 | -0.09 | -0.32 | -13.56 | 16 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 0.46 | 4.78 | -3.1 | 16.49 | 17.74 | 19.24 | False |  | strong_accumulation | 0.77 | 1.19 | 2 | 3 | 4.59 | 1.21 | -25.0 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -9.83 | 26.87 | 9.28 | 157.24 | 42.37 | 141.68 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -1.89 | 1 | 0 | 3.03 | 1.6 | -13.52 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -1.33 | 20.5 | 35.35 | 93.08 | 49.22 | 113.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.69 | 2 | 1 | 4.74 | 5.48 | -5.5 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -2.19 | 11.81 | -1.57 | 14.68 | 19.05 | 19.05 | False |  | mild_accumulation | 1.27 | 0.17 | 3 | 1 | 0.48 | 0.04 | -10.33 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | -4.04 | 5.94 | -7.36 | 0.0 | 9.74 | 30.33 | False |  | distribution_warning | -0.98 | -1.71 | 1 | 1 | -3.17 | -4.25 | -26.21 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -1.57 | -8.27 | -18.09 | -11.7 | 4.62 | 4.62 | False |  | distribution_warning | -2.15 | -2.84 | 1 | 0 | -6.18 | -7.47 | -38.41 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | -0.97 | 29.94 | 46.97 | 142.86 | 58.39 | 156.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.09 | 4.36 | 3 | 3 | 9.55 | 7.35 | -7.78 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -4.55 | -12.82 | 6.04 | 49.8 | 18.15 | 48.33 | False |  | distribution_warning | -2.98 | -1.29 | 2 | 2 | -13.35 | -9.79 | -28.64 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 0.18 | -2.13 | 4.16 | 12.22 | 5.15 | 12.45 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -1.6 | -1.37 | -13.77 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -1.94 | 5.36 | -37.23 | -18.24 | 10.62 | 10.62 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.24 | -3.36 | -39.28 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | 1.81 | 3.42 | 5.36 | 5.65 | 5.93 | 9.78 | False |  | distribution_warning | -0.03 | 0.0 | 2 | 2 | 1.42 | 1.17 | -3.91 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | 6.79 | 16.12 | -11.54 | 40.71 | 38.43 | 43.41 | False |  | mild_accumulation | 0.25 | -0.27 | 1 | 2 | 3.04 | 3.96 | -21.93 | 20 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -0.7 | -4.85 | -12.19 | 18.54 | 5.37 | 25.88 | False |  | distribution_warning | -0.42 | -0.15 | 0 | 0 | -4.57 | -5.56 | -32.26 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 8.43 | 47.33 | 4.61 | 203.94 | 63.56 | 193.76 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.46 | 11.69 | 2 | 2 | 11.93 | 10.35 | -7.21 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 3.71 | 19.84 | 7.97 | 81.34 | 32.64 | 82.08 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.11 | -0.16 | 2 | 1 | 4.19 | 3.5 | -16.06 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | -5.14 | 5.31 | -13.57 | 51.13 | 24.42 | 67.45 | False |  | strong_accumulation | 1.51 | 1.74 | 3 | 2 | 1.68 | -1.29 | -20.39 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 0.84 | 8.56 | -1.23 | 65.07 | 19.9 | 62.84 | False |  | mild_accumulation | -0.01 | 0.67 | 1 | 2 | 0.75 | 0.12 | -13.93 | 17 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 133.3640235641089 | 87.69992405929172 | 1.35 | 11.22 | -44.54 | -19.94 | 27.4 | 27.4 | False |  | distribution_warning | -0.35 | -0.44 | 1 | 1 | 1.45 | -2.74 | -44.99 | 17 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -1.63 | -0.41 | -8.95 | 5.11 | 2.65 | 4.77 | False |  | mild_accumulation | 0.53 | -0.21 | 3 | 2 | -1.87 | -2.23 | -12.73 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | 3.2 | 14.16 | -24.85 | 32.53 | 23.84 | 30.08 | False |  | strong_accumulation | 0.56 | 1.09 | 2 | 2 | 3.67 | -0.05 | -30.4 | 18 | selected |
| 2501 | 國建 | 建材營造 | neutral |  | 119.67349677675224 | 35.30940543476948 | 0.0 | 2.23 | 1.1 | 4.81 | 6.51 | 6.51 | False |  | mild_accumulation | -0.01 | 0.12 | 1 | 2 | 1.29 | 0.32 | -19.37 |  | fail_low_response_condition |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 4.24 | 12.17 | 19.43 | 7.27 | 21.9 | 21.9 | False |  | mild_accumulation | 0.16 | 0.0 | 2 | 0 | 7.59 | 6.24 | -1.67 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 1.31 | -1.83 | 1.02 | -9.96 | 3.88 | 7.08 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.37 | -0.85 | -13.65 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -0.52 | 10.59 | 13.23 | 33.24 | 15.29 | 40.95 | False |  | strong_accumulation | 1.58 | 1.93 | 3 | 3 | 3.94 | 3.21 | -3.06 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 0.65 | -0.65 | -16.12 | -46.9 | 8.6 | 8.6 | False |  | distribution_warning | -0.37 | -0.27 | 1 | 1 | 0.59 | -0.7 | -25.1 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 2.67 | 5.49 | -4.68 | -5.08 | 9.32 | 9.32 | False |  | mild_accumulation | -0.03 | 0.36 | 1 | 3 | 3.44 | 1.67 | -13.28 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | -0.99 | -1.47 | 1.93 | -9.46 | 2.34 | 2.45 | False |  | strong_accumulation | 0.44 | 0.39 | 2 | 2 | -2.33 | -2.51 | -14.83 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_僅留完整清單 | 56.21501385482998 | 35.673950917357274 | 7.67 | 16.61 | 26.83 | 42.96 | 34.89 | 43.61 | False |  | strong_accumulation | 0.87 | 1.19 | 3 | 3 | 8.92 | 7.88 | -11.57 | 15 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 3.14 | -34.53 | -3.71 | 28.39 | 16.55 | 44.57 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 1 | -13.0 | -10.12 | -44.17 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 2.86 | 2.86 | -7.49 | -5.5 | 9.12 | 9.12 | False |  | mild_accumulation | 0.08 | -2.09 | 1 | 0 | 2.33 | 1.7 | -12.8 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -3.83 | 13.96 | 4.15 | 37.76 | 23.44 | 35.2 | False |  | strong_accumulation | 2.81 | 3.85 | 3 | 3 | 3.45 | 1.81 | -11.76 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -3.27 | -10.57 | -4.05 | 11.27 | 1.28 | 20.3 | False |  | strong_accumulation | 1.41 | 0.19 | 3 | 2 | -5.52 | -6.44 | -27.3 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 8.87 | 41.36 | 9.53 | 104.55 | 67.7 | 99.26 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.48 | 7.23 | 2 | 2 | 10.69 | 8.9 | -5.43 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -7.81 | 14.15 | -29.86 | 78.93 | 33.15 | 89.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.24 | -0.57 | 1 | 0 | -0.74 | -4.83 | -36.73 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | -2.8 | 31.7 | 10.69 | 77.18 | 46.4 | 77.18 | True | 近20日漲幅>25%；近120日漲幅>70% | strong_accumulation | 2.41 | 2.28 | 2 | 3 | 5.48 | 5.35 | -11.14 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 73.91966377290892 | 26.75099850600647 | 0.22 | 4.26 | 24.33 | 58.43 | 24.0 | 55.52 | False |  | mild_accumulation | 1.32 | 0.87 | 2 | 1 | -2.62 | -0.94 | -20.17 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | 0.61 | 9.09 | -19.02 | 27.17 | 16.81 | 39.09 | False |  | mild_accumulation | -0.14 | 0.19 | 1 | 1 | -0.65 | -2.39 | -23.26 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | 0.77 | 0.0 | -8.65 | 57.36 | 9.8 | 58.45 | False |  | mild_accumulation | -0.82 | 0.47 | 2 | 2 | -1.73 | -2.78 | -22.64 | 18 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.73 | 4.2 | -31.2 | -7.89 | 10.28 | 10.28 | False |  | distribution_warning | -0.99 | -1.75 | 1 | 1 | -4.59 | -4.36 | -34.05 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | -0.22 | 1.14 | -13.26 | 0.23 | 11.81 | 11.81 | False |  | mild_accumulation | 0.72 | -0.01 | 2 | 1 | -0.96 | -3.35 | -31.54 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | -5.22 | 28.79 | -11.13 | 29.51 | 41.59 | 41.59 | True | 近20日漲幅>25% | mild_accumulation | 0.15 | -0.71 | 1 | 1 | 7.33 | 3.38 | -22.58 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -3.05 | 8.13 | -1.72 | 30.0 | 15.32 | 28.83 | False |  | mild_accumulation | 2.89 | 1.28 | 2 | 1 | 0.33 | -0.15 | -10.62 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | 0.36 | 19.7 | -22.78 | 57.73 | 32.07 | 64.25 | False |  | distribution_warning | -2.06 | -1.76 | 1 | 1 | 0.82 | -0.96 | -28.63 | 13 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -4.28 | 1.58 | -23.05 | 3.84 | 14.22 | 14.22 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 3.18 | -1.13 | -38.74 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | -1.7 | 0.87 | 6.94 | 95.43 | 47.51 | 107.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.92 | -5.4 | 0 | 1 | 6.54 | -0.67 | -42.54 |  | fail_already_priced_in |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 2.79 | 18.15 | -27.51 | 88.42 | 45.61 | 87.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.89 | -5.49 | 1 | 1 | 6.21 | -3.66 | -54.52 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | 14.29 | 23.71 | -30.9 | 58.59 | 34.33 | 80.0 | False |  | distribution_warning | -0.87 | -1.54 | 1 | 1 | 9.16 | 7.93 | -32.33 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | -12.47 | 25.75 | -15.22 | 142.45 | 55.12 | 134.03 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.9 | -4.11 | 1 | 0 | 4.72 | -1.68 | -33.6 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 12.33 | 45.69 | 15.96 | 202.11 | 63.3 | 224.29 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 13.65 | 12.54 | -7.12 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | -1.38 | 5.0 | 12.62 | 40.0 | 28.42 | 45.71 | False |  | strong_accumulation | 3.25 | 3.26 | 2 | 2 | -2.99 | -0.37 | -13.35 | 18 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 1.45 | 2.56 | 8.95 | 6.87 | 13.82 | 17.65 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | 0.81 | 1.06 | -1.41 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.23071292224356 | 63.75000065335939 | -2.28 | 5.94 | -32.06 | 9.07 | 19.02 | 19.02 | False |  | mild_accumulation | -0.89 | 0.33 | 1 | 2 | -1.41 | -3.95 | -36.31 | 17 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 0.63 | 52.19 | 19.27 | 154.34 | 75.43 | 160.28 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.11 | 0.31 | 3 | 1 | 15.12 | 11.52 | -7.01 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -7.94 | 31.6 | 8.66 | 109.43 | 61.52 | 124.89 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.39 | 4.76 | 2 | 3 | 9.43 | 5.6 | -12.91 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 2.08 | 12.18 | -8.68 | 4.49 | 17.87 | 17.87 | False |  | mild_accumulation | 0.39 | -1.47 | 2 | 0 | 3.72 | 2.13 | -19.2 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -3.14 | 3.22 | -29.02 | 28.31 | 10.61 | 37.17 | False |  | mild_accumulation | -1.45 | 0.25 | 0 | 3 | -3.41 | -4.34 | -41.47 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | -3.93 | 6.88 | -30.2 | -41.84 | 24.45 | 24.45 | False |  | mild_accumulation | 1.69 | -0.95 | 3 | 2 | -0.2 | -4.21 | -41.24 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 1.07 | 54.45 | 46.83 | 63.68 | 74.08 | 85.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.23 | -0.47 | 3 | 2 | 15.1 | 13.46 | -7.38 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 181.7841084291265 | -13.777157023400417 | 4.04 | 24.08 | -12.46 | 29.05 | 46.96 | 55.85 | False |  | mild_accumulation | 0.42 | -1.35 | 2 | 2 | 5.98 | 2.89 | -21.04 | 20 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -7.37 | -6.32 | -0.48 | 17.23 | 23.15 | 39.26 | False |  | strong_accumulation | 2.23 | 2.17 | 3 | 2 | -4.81 | -3.72 | -18.79 | 18 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 3.29 | 0.0 | -6.38 | 57.37 | 7.84 | 55.59 | False |  | distribution_warning | -0.91 | -0.69 | 1 | 1 | -4.82 | -3.35 | -15.71 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -2.4 | 11.17 | -18.47 | -15.06 | 18.57 | 18.57 | False |  | strong_accumulation | 0.49 | 0.21 | 3 | 2 | 2.69 | 0.19 | -18.8 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | -0.45 | 5.29 | -36.89 | -21.22 | 22.35 | 22.35 | False |  | distribution_warning | -0.55 | -0.64 | 0 | 2 | -0.63 | -5.5 | -44.27 | 12 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | -0.96 | 3.39 | 26.96 | -0.38 | 30.81 | 30.81 | False |  | strong_accumulation | 0.29 | 0.28 | 3 | 3 | 1.05 | 1.48 | -7.66 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | -6.41 | 9.14 | -26.08 | 81.57 | 21.6 | 77.48 | True | 近120日漲幅>70% | mild_accumulation | 0.57 | -1.74 | 2 | 0 | -4.83 | -5.27 | -27.84 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -0.19 | 4.63 | -7.8 | -11.86 | 7.22 | 7.22 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 1.25 | -0.26 | -22.39 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -4.25 | 10.48 | -22.87 | 26.98 | 21.25 | 23.22 | False |  | distribution_warning | -1.02 | -1.25 | 1 | 0 | -0.2 | -3.32 | -38.07 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -1.76 | 10.1 | -22.26 | 6.81 | 19.2 | 19.2 | False |  | mild_accumulation | 0.5 | -0.01 | 2 | 0 | 0.53 | 0.05 | -23.59 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 1.0 | 4.53 | -9.78 | 80.93 | 16.13 | 90.79 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.13 | 1 | 1 | 0.85 | -0.31 | -20.39 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 1.78 | 0.0 | -17.1 | -23.12 | 8.75 | 8.75 | False |  | distribution_warning | -0.08 | -0.21 | 2 | 0 | 0.53 | -1.97 | -25.13 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -0.48 | -4.99 | -8.91 | -32.15 | 7.16 | 7.16 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -1.41 | -1.8 | -13.16 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | -2.74 | 14.7 | -24.95 | 45.79 | 31.48 | 45.64 | False |  | mild_accumulation | 0.07 | 0.11 | 1 | 2 | 4.84 | 0.97 | -32.38 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 98.74936839745938 | 71.28591290526819 | 8.13 | 29.76 | -1.27 | 49.73 | 39.39 | 49.32 | True | 近20日漲幅>25% | mild_accumulation | -0.45 | 0.38 | 2 | 2 | 3.92 | 4.31 | -13.63 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 2.65 | 25.0 | -26.37 | -7.19 | 47.62 | 47.62 | False |  | mild_accumulation | 1.31 | -1.02 | 2 | 0 | 10.56 | 6.12 | -33.33 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -2.87 | 2.35 | -41.72 | -0.81 | 21.56 | 21.56 | False |  | distribution_warning | -18.41 | -18.98 | 0 | 1 | -3.64 | -7.67 | -48.17 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -1.57 | 1.62 | 20.83 | 40.67 | 20.83 | 41.2 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -0.85 | -0.69 | -6.68 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -1.28 | -10.76 | -11.07 | 1.58 | 1.18 | 2.94 | False |  | distribution_warning | -5.63 | -6.23 | 1 | 1 | -7.58 | -6.3 | -18.84 | 13 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 0.95 | -3.34 | -12.38 | -1.24 | 3.75 | 3.75 | False |  | distribution_warning | -0.45 | -0.34 | 1 | 1 | -0.37 | -0.97 | -24.08 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 1.84 | -2.64 | 4.73 | -9.03 | 6.24 | 8.31 | False |  | distribution_warning | -0.03 | -0.02 | 0 | 0 | -0.75 | -0.42 | -7.32 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | -4.44 | -3.34 | 1.62 | 1.76 | 3.58 | 3.58 | False |  | distribution_warning | 0.0 | -0.2 | 1 | 1 | -4.06 | -4.49 | -13.94 | 16 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 2.3 | -2.51 | 7.8 | 17.8 | 9.12 | 17.36 | False |  | mild_accumulation | 0.16 | 0.83 | 1 | 2 | 2.03 | 0.86 | -4.89 |  | fail_low_response_condition |