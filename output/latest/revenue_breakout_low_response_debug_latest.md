# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-31 19:36:04 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 706147 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 437 |
| tdcc_mild_accumulation_count | 765 |
| tdcc_distribution_warning_count | 580 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 83 |
| already_priced_in_excluded | 28 |
| overheat_pass | 55 |
| score_pass | 55 |
| theme_priority_pass | 50 |
| final_rows | 50 |

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
| fail_low_response_condition | 254 |
| fail_already_priced_in | 28 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | -3.1 | 8.96 | 2.82 | -14.45 | 16.61 | 16.61 | False |  | mild_accumulation | -0.39 | 0.25 | 0 | 2 | 3.3 | 2.07 | -12.4 | 17 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 1.74 | 4.17 | -11.47 | -29.05 | 5.21 | 5.21 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | 1.55 | 0.74 | -15.46 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.49 | 5.5 | 2.99 | 16.29 | 9.06 | 24.85 | False |  | mild_accumulation | 0.36 | 0.0 | 2 | 0 | 0.68 | -0.44 | -15.16 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -2.07 | 9.26 | 0.0 | 0.85 | 11.32 | 11.32 | False |  | strong_accumulation | 1.99 | 1.33 | 3 | 2 | 2.32 | 2.06 | -4.45 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -0.56 | -1.66 | -5.59 | -4.05 | 4.11 | 4.72 | False |  | mild_accumulation | 0.03 | -0.01 | 3 | 0 | -0.95 | -1.18 | -11.91 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -0.8 | 2.05 | -8.46 | 15.81 | 5.96 | 17.45 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | 0.18 | -0.52 | -25.89 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 0.0 | -4.58 | -32.56 | -40.41 | 4.29 | 4.29 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.15 | -4.58 | -34.23 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -0.7 | 0.71 | 8.78 | 39.71 | 16.33 | 50.63 | False |  | mild_accumulation | -0.61 | 0.79 | 1 | 2 | -3.83 | -1.59 | -11.76 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 1.78 | 4.02 | -9.38 | -3.26 | 11.85 | 11.85 | False |  | mild_accumulation | 0.93 | -0.73 | 2 | 1 | 1.05 | 1.27 | -13.76 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -3.46 | 45.75 | 61.59 | 95.61 | 73.32 | 94.48 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.82 | 2 | 2 | 7.66 | 7.52 | -11.27 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 1.5 | 17.77 | 39.67 | 83.1 | 55.05 | 87.36 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.63 | 1 | 2 | 2.52 | 3.09 | -32.4 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -4.48 | 3.02 | 7.57 | 8.6 | 15.2 | 21.57 | False |  | strong_accumulation | 0.63 | 0.7 | 3 | 3 | 0.71 | 0.5 | -9.79 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -1.73 | 2.25 | -0.87 | 0.89 | 6.07 | 13.5 | False |  | mild_accumulation | 0.03 | -0.01 | 2 | 1 | -0.2 | -0.14 | -9.56 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -1.16 | 7.56 | 4.92 | 20.75 | 14.29 | 23.08 | False |  | mild_accumulation | 0.7 | 0.28 | 2 | 1 | 0.93 | 0.65 | -19.24 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -1.6 | 64.22 | 165.05 | 321.4 | 186.75 | 350.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | -1.97 | 3 | 0 | 10.47 | 13.59 | -6.0 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -5.98 | -11.01 | -21.82 |  | 2.54 |  | False |  | distribution_warning | -0.26 | -0.7 | 0 | 0 | -6.72 | -5.76 | -31.64 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -0.41 | -11.31 | -10.66 | 7.52 | 6.11 | 20.3 | False |  | mild_accumulation | 1.06 | -0.99 | 2 | 1 | -4.48 | -5.55 | -35.88 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -1.42 | 5.39 | 8.49 | 28.41 | 15.93 | 30.15 | False |  | distribution_warning | -0.41 | -2.1 | 0 | 0 | 2.98 | 1.84 | -11.58 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -1.11 | -0.96 | -3.42 | -3.57 | 5.96 | 20.54 | False |  | mild_accumulation | 0.04 | 0.02 | 2 | 1 | -0.08 | -0.98 | -11.14 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 3.52 | 10.38 | 27.05 | 138.65 | 47.17 | 157.43 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.14 | -0.76 | 2 | 1 | 1.28 | 2.24 | -24.01 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 12.76 | -5.95 | 33.26 | 108.68 | 48.4 | 116.97 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.43 | 2 | 2 | 5.67 | 3.02 | -29.54 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 2.57 | 7.05 | -0.31 | 74.51 | 25.59 | 72.25 | True | 近120日漲幅>70% | distribution_warning | -1.0 | -1.51 | 0 | 1 | -0.53 | -0.88 | -35.81 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 2.67 | -1.19 | -14.68 | 16.55 | 10.38 | 33.33 | False |  | distribution_warning | -0.39 | -0.34 | 0 | 0 | -1.59 | -0.29 | -14.53 | 11 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -1.09 | -1.27 | -26.65 | 111.24 | 19.39 | 124.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.21 | -2.24 | 1 | 1 | -5.5 | -8.05 | -55.33 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 1.61 | 14.03 | -19.49 | 16.13 | 37.25 | 37.25 | False |  | distribution_warning | -1.54 | -1.3 | 1 | 1 | -0.41 | -0.07 | -34.38 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 3.11 | 27.62 | 1.67 | 67.43 | 55.98 | 117.78 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.68 | 0.62 | 2 | 2 | 3.5 | 4.47 | -21.84 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -1.69 | -12.85 | -18.92 | 43.31 | 10.6 | 47.46 | False |  | distribution_warning | -0.19 | -0.04 | 1 | 1 | -6.65 | -5.65 | -27.96 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | -1.47 | -5.13 | -3.23 | 23.93 | 8.34 | 21.85 | False |  | distribution_warning | -0.46 | -0.37 | 0 | 0 | -3.0 | -1.63 | -11.5 | 18 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | -1.4 | -5.11 | -4.98 | -1.81 | 5.69 | 5.69 | False |  | distribution_warning | -0.18 | -0.07 | 1 | 1 | 0.11 | -1.61 | -14.22 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 15.96 | 48.56 | 10.19 | 161.53 | 87.5 | 165.11 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.73 | 3.55 | 2 | 1 | 23.72 | 19.83 | -5.87 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 0.91 | 4.38 | -14.27 | 56.39 | 17.43 | 66.96 | False |  | strong_accumulation | 0.84 | 0.76 | 2 | 2 | 0.87 | 1.9 | -15.78 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 8.23 | 25.03 | 12.0 | 69.61 | 57.32 | 83.3 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.83 | 1.54 | 3 | 3 | 10.51 | 11.49 | -2.54 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -5.31 | 0.0 | -25.19 | 28.1 | 13.29 | 35.64 | False |  | distribution_warning | -0.15 | -0.86 | 1 | 1 | -6.04 | -5.1 | -26.32 | 16 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 0.99 | 2.51 | -19.02 | 0.99 | 15.35 | 15.35 | False |  | distribution_warning | -1.07 | -0.33 | 0 | 1 | -2.46 | -3.06 | -32.85 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 22.89 | 33.6 | -13.7 | 24.6 | 65.25 | 65.25 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.22 | -1.32 | 0 | 2 | 15.85 | 14.56 | -26.27 |  | fail_low_response_condition |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | 2.38 | 2.08 | -15.08 | -2.69 | 16.44 | 16.44 | False |  | distribution_warning | -0.67 | -0.54 | 1 | 2 | -0.89 | -0.41 | -17.53 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 4.99 | 10.32 | -4.28 | 53.65 | 14.74 | 61.63 | False |  | mild_accumulation | 0.66 | 0.25 | 1 | 1 | 1.44 | 2.47 | -10.95 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 4.15 | 14.17 | -16.21 | 17.13 | 21.33 | 22.87 | False |  | distribution_warning | -0.06 | -0.01 | 1 | 2 | 5.09 | 3.37 | -14.41 | 17 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 1.01 | 10.14 | 13.56 | 102.77 | 39.57 | 113.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.59 | -1.21 | 1 | 0 | -2.78 | -0.78 | -15.22 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 2.89 | 17.53 | 29.69 | 97.66 | 50.78 | 115.95 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.75 | 1 | 1 | 2.07 | 4.57 | -4.51 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | 0.48 | 13.92 | -3.67 | 14.55 | 20.0 | 20.0 | False |  | mild_accumulation | 0.93 | -0.05 | 2 | 0 | -1.62 | 0.54 | -7.49 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | -0.47 | -4.07 | -13.82 | 4.95 | 8.72 | 29.11 | False |  | distribution_warning | -0.12 | -1.22 | 2 | 1 | -4.33 | -3.99 | -26.9 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -0.88 | -9.22 | -27.14 | -17.38 | 3.7 | 3.7 | False |  | distribution_warning | -1.76 | -2.67 | 1 | 0 | -6.25 | -6.44 | -38.96 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 8.38 | 36.95 | 37.47 | 128.15 | 68.63 | 173.55 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.83 | 2.98 | 3 | 3 | 8.45 | 10.14 | -4.57 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -1.32 | -22.57 | 4.62 | 22.02 | 17.06 | 43.85 | False |  | distribution_warning | -4.47 | -0.95 | 2 | 2 | -11.04 | -8.07 | -29.3 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -0.72 | -2.83 | -1.96 | -3.0 | 1.67 | 8.93 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -1.71 | -1.55 | -14.08 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -0.27 | 0.83 | -31.51 | -13.98 | 13.44 | 13.44 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.33 | -0.58 | -31.51 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 233.9341638249008 | 396.6930034235488 | -1.53 | 0.52 | -1.53 | -2.03 | 2.93 | 7.82 | False |  | strong_accumulation | 0.46 | 0.98 | 2 | 2 | -0.68 | -0.74 | -5.62 | 21 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -6.8 | 4.8 | -17.51 | 24.79 | 36.34 | 41.25 | False |  | strong_accumulation | 1.28 | 0.02 | 2 | 2 | 0.2 | 1.46 | -15.62 | 22 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -1.9 | -6.74 | -15.37 | 19.37 | 5.0 | 20.64 | False |  | distribution_warning | -0.12 | -0.08 | 1 | 1 | -4.56 | -4.77 | -32.5 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -4.0 | 22.03 | 5.88 | 153.88 | 52.54 | 173.97 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.41 | 10.78 | 2 | 2 | -2.54 | -0.06 | -16.86 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 2.51 | 24.5 | 10.33 | 71.53 | 39.47 | 86.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.38 | 3.25 | 2 | 2 | 4.16 | 5.9 | -11.74 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 15.01 | 23.22 | -2.08 | 68.64 | 42.56 | 76.66 | False |  | mild_accumulation | 1.42 | -0.27 | 3 | 2 | 11.24 | 9.87 | -8.78 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 54.39975818511566 | 39.61008944759205 | 8.66 | 5.46 | 3.72 | 52.49 | 24.88 | 56.48 | False |  | distribution_warning | -0.13 | -0.85 | 1 | 1 | 2.41 | 2.92 | -10.36 |  | fail_low_response_condition |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | 1.54 | 11.62 | -35.03 | -31.05 | 32.35 | 32.35 | False |  | mild_accumulation | 0.62 | 0.52 | 2 | 1 | 1.54 | 0.44 | -38.67 | 22 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.82 | -4.53 | -10.19 | 1.89 | 2.97 | 3.63 | False |  | distribution_warning | -0.11 | -0.27 | 2 | 2 | -1.1 | -1.36 | -12.45 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | 2.27 | 8.64 | -24.8 | 15.86 | 22.72 | 22.72 | False |  | strong_accumulation | 0.95 | 0.53 | 3 | 2 | 0.11 | -0.73 | -31.03 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -3.25 | -1.32 | -4.89 | -2.19 | 3.95 | 3.95 | False |  | strong_accumulation | 0.25 | 0.36 | 2 | 2 | -1.48 | -1.88 | -21.3 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 5.12 | 18.01 | 18.46 | 11.19 | 22.22 | 27.27 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 8.58 | 7.45 | -1.91 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -1.0 | -2.39 | -4.14 | -12.58 | 3.73 | 6.92 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.27 | -1.14 | -13.77 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -3.42 | 6.39 | 8.24 | 27.63 | 13.23 | 38.43 | False |  | strong_accumulation | 1.8 | 1.95 | 3 | 3 | 0.55 | 0.54 | -4.8 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 93.8248443457034 | 60.82046311316634 | 2.98 | 6.28 | -13.67 | -45.85 | 12.27 | 12.27 | False |  | mild_accumulation | -0.46 | 0.04 | 0 | 2 | 2.81 | 2.58 | -22.57 | 18 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -1.3 | 4.58 | -10.1 | -6.29 | 8.21 | 8.21 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 2 | 1.17 | -0.03 | -14.16 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -1.87 | -3.3 | -3.77 | -10.27 | 1.43 | 1.53 | False |  | strong_accumulation | 0.23 | 0.17 | 2 | 2 | -2.67 | -2.68 | -15.59 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | -3.09 | 13.37 | 20.49 | 40.66 | 32.91 | 41.29 | False |  | strong_accumulation | 0.68 | 0.42 | 3 | 2 | 4.22 | 4.72 | -12.87 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -1.43 | -26.67 | -6.56 | 32.24 | 14.42 | 41.94 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -7.81 | -10.37 | -45.19 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 0.76 | 4.49 | -5.04 | -22.81 | 9.39 | 9.39 | False |  | mild_accumulation | 0.1 | -2.07 | 1 | 0 | 2.19 | 1.6 | -12.58 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 92.98747396520872 | 39.79375890103884 | 7.98 | 20.84 | 10.4 | 37.18 | 30.43 | 42.86 | False |  | strong_accumulation | 2.93 | 2.89 | 3 | 2 | 4.75 | 5.27 | -6.76 | 21 | selected |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -1.25 | -4.82 | -6.69 | 11.27 | 1.28 | 20.3 | False |  | mild_accumulation | 0.36 | -0.03 | 2 | 2 | -4.05 | -4.87 | -27.3 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 3.72 | 47.73 | 19.39 | 81.68 | 81.68 | 98.98 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.26 | 2.16 | 2 | 2 | 10.92 | 13.92 | -0.34 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 3.0 | 17.31 | -6.79 | 72.24 | 41.68 | 101.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.79 | 0.21 | 0 | 1 | 1.2 | 1.42 | -32.68 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 19.96 | 34.31 | 26.38 | 83.65 | 69.98 | 87.16 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.27 | 1 | 2 | 13.9 | 15.88 | -0.72 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 73.91966377290892 | 26.75099850600647 | -3.73 | -1.85 | 18.82 | 48.03 | 20.4 | 49.75 | False |  | mild_accumulation | -0.42 | 1.72 | 1 | 2 | -6.24 | -2.96 | -22.49 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -3.0 | 1.25 | -22.7 | 27.87 | 14.51 | 33.4 | False |  | distribution_warning | -1.06 | -1.12 | 0 | 0 | -4.06 | -3.28 | -24.15 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -4.81 | -4.6 | -10.9 | 46.55 | 6.45 | 43.25 | False |  | distribution_warning | -2.09 | -0.79 | 1 | 2 | -5.1 | -4.41 | -25.0 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -2.24 | -4.16 | -30.5 | -16.77 | 8.89 | 8.89 | False |  | distribution_warning | -1.93 | -2.31 | 0 | 0 | -6.07 | -3.91 | -31.11 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 1.35 | 3.91 | -10.67 | -4.03 | 13.57 | 13.57 | False |  | strong_accumulation | 0.08 | 0.92 | 2 | 2 | -1.0 | -1.55 | -30.46 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 10.33 | 32.75 | -3.03 | 30.66 | 51.83 | 51.83 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.14 | -0.01 | 1 | 1 | 8.51 | 8.04 | -16.97 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -0.88 | 8.24 | -5.99 | 19.07 | 13.91 | 22.83 | False |  | mild_accumulation | 2.7 | 0.0 | 1 | 1 | -2.8 | -1.25 | -10.32 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -1.44 | 8.07 | -19.03 | 44.85 | 30.4 | 62.19 | False |  | distribution_warning | -0.29 | -0.7 | 1 | 1 | -3.84 | -1.97 | -29.53 | 12 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 11.56 | 19.5 | -30.74 | -19.81 | 28.67 | 28.67 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 12.51 | 8.91 | -30.99 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 10.05 | 29.43 | 16.43 | 108.84 | 53.9 | 116.73 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.31 | -5.15 | 0 | 1 | 5.36 | 1.47 | -40.05 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 7.36 | 27.27 | -20.81 | 89.39 | 53.51 | 94.01 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.21 | -3.49 | 1 | 1 | 5.87 | 1.77 | -52.05 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | 3.11 | 14.06 | -24.12 | 65.91 | 36.19 | 82.5 | True | 距120日低點反彈>80% | distribution_warning | -1.43 | -1.72 | 0 | 1 | 6.45 | 6.43 | -22.51 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 19.4 | 48.69 | -11.88 | 103.33 | 82.74 | 161.18 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.83 | -7.13 | 1 | 0 | 13.73 | 12.16 | -21.77 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -10.55 | 12.54 | 14.84 | 183.29 | 51.92 | 201.69 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.43 | -1.57 | 1 | 0 | 0.37 | 2.14 | -14.56 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 1.42 | -4.3 | 1.14 | 32.84 | 28.06 | 45.31 | False |  | distribution_warning | -0.27 | -0.36 | 1 | 1 | -3.94 | -0.66 | -13.59 | 12 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -1.43 | -1.08 | 8.24 | 5.34 | 12.2 | 15.97 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | -0.83 | -0.75 | -2.82 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | 4.19 | 9.27 | -30.0 | 9.8 | 24.58 | 24.58 | False |  | distribution_warning | -0.78 | -0.53 | 1 | 1 | 0.34 | 0.34 | -29.34 | 13 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 13.7 | 45.76 | 38.64 | 166.96 | 92.13 | 185.05 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.42 | 2 | 1 | 14.89 | 15.05 | -4.24 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 27.42 | 57.95 | 24.23 | 129.89 | 95.76 | 172.57 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.94 | 4.34 | 2 | 3 | 20.86 | 20.51 | 0.0 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 0.68 | 12.66 | -10.64 | 5.7 | 18.67 | 18.67 | False |  | mild_accumulation | 0.14 | -1.25 | 2 | 0 | 1.85 | 2.32 | -12.75 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -1.44 | -5.73 | -41.29 | 32.37 | 9.02 | 34.53 | False |  | distribution_warning | -0.42 | -0.14 | 1 | 2 | -5.14 | -4.46 | -40.86 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 2.69 | 9.75 | -35.91 | -30.32 | 27.8 | 27.8 | False |  | strong_accumulation | 0.48 | 0.37 | 2 | 3 | -0.66 | -1.53 | -36.15 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 16.2 | 58.89 | 60.59 | 84.59 | 100.33 | 113.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.15 | -0.41 | 2 | 2 | 19.89 | 21.18 | -0.91 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 9.1 | 25.38 | -6.11 | 27.74 | 54.94 | 64.31 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -1.41 | -4.39 | 1 | 1 | 5.83 | 6.47 | -16.75 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.590900789853706 | 37.93424741228517 | 5.85 | 3.58 | -5.86 | 32.72 | 28.78 | 39.1 | False |  | distribution_warning | -0.16 | -0.27 | 2 | 1 | -1.12 | 1.04 | -15.07 | 12 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | -10.27 | -14.14 | -14.51 | 33.69 | 2.47 | 28.68 | False |  | distribution_warning | -2.05 | -2.31 | 0 | 0 | -12.65 | -9.73 | -23.68 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -0.49 | 12.02 | -17.34 | -21.15 | 19.74 | 19.74 | False |  | mild_accumulation | 0.51 | -0.01 | 3 | 1 | 1.15 | 0.91 | -17.34 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 11.57 | 15.31 | -28.7 | -27.41 | 34.64 | 34.64 | False |  | mild_accumulation | 0.01 | -0.77 | 1 | 2 | 5.4 | 3.1 | -38.68 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 6.74 | 13.64 | 35.45 | 2.4 | 39.9 | 39.9 | False |  | strong_accumulation | 0.27 | 0.26 | 2 | 2 | 5.84 | 6.75 | -1.25 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 9.34 | 9.9 | -5.46 | 78.19 | 33.64 | 89.08 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.85 | 2 | 1 | 1.33 | 3.34 | -11.45 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 0.77 | 2.96 | -17.04 | -12.44 | 7.42 | 7.42 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 0.34 | -0.37 | -19.1 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 128.9172485640275 | 121.34662298357856 | 3.92 | 10.35 | -26.24 | 12.2 | 27.22 | 27.22 | False |  | mild_accumulation | -0.71 | 0.58 | 1 | 1 | 1.25 | 0.74 | -35.02 | 18 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 9.45 | 13.63 | 3.25 | 12.46 | 31.2 | 31.2 | False |  | mild_accumulation | 1.43 | 1.47 | 2 | 1 | 7.11 | 7.57 | -3.05 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 1.32 | 5.16 | -18.45 | 64.58 | 14.3 | 87.78 | True | 距120日低點反彈>80% | distribution_warning | -3.78 | -3.03 | 0 | 0 | -2.66 | -1.93 | -20.08 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -0.35 | -0.7 | -17.25 | -24.13 | 7.6 | 7.6 | False |  | mild_accumulation | 0.21 | 0.38 | 3 | 1 | -1.38 | -2.66 | -25.92 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -3.97 | -8.59 | -10.84 | -32.37 | 2.05 | 2.05 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -5.11 | -5.07 | -17.31 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 9.57 | 25.53 | -22.05 | 12.13 | 42.04 | 42.04 | True | 近20日漲幅>25% | strong_accumulation | 0.22 | 0.19 | 2 | 2 | 7.97 | 6.88 | -22.21 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | -0.72 | 15.0 | -8.61 | 40.1 | 41.18 | 41.18 | False |  | distribution_warning | -4.56 | -1.03 | 2 | 1 | 1.52 | 4.1 | -6.44 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 20.69 | 44.03 | -16.27 | 2.94 | 66.67 | 66.67 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.69 | -0.67 | 2 | 1 | 15.28 | 13.78 | -15.05 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 105.41523454519049 | 68.91539282131619 | 6.59 | 5.89 | -29.98 | -8.87 | 29.14 | 29.14 | False |  | mild_accumulation | -1.03 | 0.38 | 1 | 2 | -0.99 | -2.13 | -44.94 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -1.84 | -1.58 | 12.01 | 33.21 | 18.04 | 37.64 | False |  | mild_accumulation | 0.22 | 0.0 | 2 | 0 | -2.24 | -1.53 | -7.67 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -0.52 | -11.67 | -13.16 | -1.03 | 1.31 | 3.07 | False |  | distribution_warning | -8.96 | -8.86 | 0 | 1 | -6.27 | -4.51 | -18.74 | 14 | selected |
| 5522 | 遠雄 | 建材營造 | neutral | D_降級_TDCC轉弱 | 189.242108725136 | 453.301755044666 | -2.83 | -5.22 | -17.07 | -7.77 | 0.49 | 0.49 | False |  | distribution_warning | -0.45 | -0.52 | 1 | 0 | -2.83 | -3.49 | -26.46 | 12 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -1.79 | -4.77 | -0.9 | -10.59 | 3.29 | 7.33 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -0.88 | -1.11 | -8.16 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | -5.99 | -2.84 | 1.62 | 0.13 | 0.67 | 3.71 | False |  | distribution_warning | -0.32 | -0.29 | 1 | 1 | -3.42 | -3.26 | -13.83 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 1.28 | 8.92 | 5.66 | 13.39 | 11.4 | 18.47 | False |  | strong_accumulation | 0.46 | 0.23 | 2 | 2 | 3.55 | 2.56 | -2.91 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 1.92 | 41.12 | 22.94 | 51.43 | 48.14 | 53.38 | True | 近20日漲幅>25% | strong_accumulation | 3.39 | 6.39 | 3 | 3 | 8.72 | 8.45 | -10.34 |  | fail_already_priced_in |