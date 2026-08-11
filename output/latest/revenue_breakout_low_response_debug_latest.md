# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-11 19:52:59 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1953 |
| standardized_revenue_rows | 1953 |
| price_rows | 665456 |
| tdcc_rows | 1970 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 391 |
| tdcc_mild_accumulation_count | 717 |
| tdcc_distribution_warning_count | 674 |
| revenue_condition_pass | 337 |
| price_metrics_pass | 336 |
| low_response_pass | 66 |
| already_priced_in_excluded | 15 |
| overheat_pass | 51 |
| score_pass | 51 |
| theme_priority_pass | 48 |
| final_rows | 48 |

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
| fail_low_response_condition | 270 |
| fail_already_priced_in | 15 |
| fail_defensive_or_traditional_excluded | 3 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | 0.0 | -1.47 | -6.51 | -27.7 | 7.03 | 7.03 | False |  | strong_accumulation | 0.21 | 0.28 | 2 | 2 | -0.41 | -0.77 | -13.36 | 19 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 3.37 | -1.32 | -5.09 | -27.6 | 4.61 | 4.61 | False |  | mild_accumulation | 0.23 | -0.81 | 2 | 0 | 0.76 | -0.03 | -15.94 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 2.5 | -12.77 | 9.98 | 1.99 | 13.51 | 23.64 | False |  | distribution_warning | -1.44 | 0.0 | 0 | 1 | -4.12 | -3.14 | -15.98 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 1.86 | -2.23 | -1.35 | -6.81 | 3.3 | 3.3 | False |  | mild_accumulation | 0.14 | -0.29 | 2 | 2 | 0.23 | 0.22 | -7.98 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.0 | -3.49 | 0.56 | -8.63 | 6.19 | 6.19 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -1.89 | -1.5 | -10.67 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 3.27 | -6.3 | 1.61 | 17.13 | 7.66 | 25.25 | False |  | mild_accumulation | 0.0 | 0.83 | 1 | 2 | 0.28 | -1.14 | -24.7 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -4.05 | -12.0 | -26.67 | -27.19 | 8.45 | 8.45 | False |  | mild_accumulation | 0.08 | 0.0 | 3 | 0 | -2.53 | -4.94 | -30.63 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | 9.47 | 20.93 | 9.86 | 30.0 | 27.35 | 65.43 | False |  | mild_accumulation | 0.13 | -1.66 | 2 | 1 | 10.19 | 8.85 | -1.89 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 5.02 | 7.65 | 4.62 | -8.83 | 13.81 | 13.81 | False |  | distribution_warning | -0.16 | -0.18 | 1 | 2 | 6.23 | 4.52 | -12.26 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 8.73 | -2.32 | 48.91 | 64.56 | 50.14 | 67.07 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.52 | 1.11 | 3 | 3 | 5.2 | 7.32 | -4.2 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 14.43 | -2.35 | 69.9 | 80.0 | 79.03 | 85.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.43 | 0.75 | 2 | 3 | 10.89 | 7.34 | -33.4 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 0.0 | 5.7 | 10.19 | 2.2 | 15.69 | 15.69 | False |  | strong_accumulation | 0.27 | 0.39 | 2 | 2 | 0.64 | 1.16 | -4.14 | 22 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -0.45 | 1.37 | 6.22 | -7.11 | 11.0 | 11.0 | False |  | mild_accumulation | -0.01 | 0.03 | 1 | 2 | 0.66 | 0.42 | -11.55 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 200.77620698853028 | 144.7342420065355 | 5.39 | 9.48 | 9.01 | 4.53 | 13.39 | 22.71 | False |  | mild_accumulation | 0.27 | 0.0 | 2 | 0 | 6.3 | 3.79 | -19.87 | 20 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 29.7 | 54.03 | 151.58 | 306.44 | 167.43 | 321.03 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.56 | -0.2 | 1 | 1 | 40.17 | 36.51 | -1.79 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -6.73 | 8.16 | -9.76 |  | 10.51 |  | False |  | distribution_warning | -0.32 | -0.12 | 1 | 2 | 1.82 | -0.37 | -26.33 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -0.73 | -19.05 | -1.45 | 20.89 | 14.29 | 34.65 | False |  | mild_accumulation | -2.08 | 1.97 | 0 | 2 | -5.23 | -4.68 | -28.23 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.07 | -7.33 | 3.45 | 18.05 | 7.36 | 21.45 | False |  | distribution_warning | -0.15 | 0.0 | 0 | 0 | -6.75 | -4.24 | -19.63 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 3.83 | -2.96 | 11.25 | -21.14 | 11.05 | 20.74 | False |  | mild_accumulation | 0.02 | 0.15 | 1 | 2 | -0.99 | -0.34 | -11.0 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 9.9 | 7.72 | 74.43 | 155.12 | 74.76 | 176.58 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.69 | 0.76 | 1 | 1 | 12.18 | 9.9 | -20.74 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | -16.41 | -26.25 | 53.95 | 113.73 | 52.66 | 131.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.49 | -3.58 | 0 | 1 | -11.65 | -11.11 | -36.11 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 12.79 | -6.52 | 13.91 | 79.54 | 35.43 | 103.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -0.03 | 1 | 1 | 9.89 | 4.97 | -30.78 |  | fail_low_response_condition |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | 5.2 | 11.68 | 6.26 | 15.86 | 16.11 | 40.27 | False |  | strong_accumulation | 0.93 | 1.0 | 2 | 2 | 5.64 | 4.36 | -16.24 | 18 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 9.01 | -20.69 | 7.87 | 141.02 | 35.16 | 157.08 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.47 | -2.42 | 0 | 0 | 0.62 | -4.56 | -49.43 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 180.47957329305424 | 137.8339123232017 | 10.42 | -5.02 | -6.03 | 34.52 | 44.34 | 49.21 | False |  | distribution_warning | -1.24 | -1.5 | 2 | 1 | 8.77 | 5.03 | -30.99 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 13.38 | 8.21 | 56.14 | 68.72 | 54.11 | 112.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.15 | 0.42 | 1 | 1 | 13.23 | 9.55 | -23.77 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -7.97 | -6.36 | -13.91 | 47.24 | 16.03 | 65.5 | False |  | distribution_warning | -0.03 | -0.14 | 2 | 2 | -3.19 | -5.3 | -24.42 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | -2.99 | 9.51 | 7.82 | 32.46 | 13.33 | 37.67 | False |  | strong_accumulation | 0.35 | 0.31 | 3 | 2 | 1.84 | 0.54 | -7.43 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 3.98 | -7.24 | 1.59 | -4.86 | 5.54 | 5.54 | False |  | strong_accumulation | 0.11 | 0.05 | 2 | 2 | -6.18 | -4.25 | -14.34 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 2.42 | -12.85 | -11.72 | 97.09 | 36.69 | 126.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.69 | 1.32 | 2 | 2 | 3.92 | 0.09 | -27.25 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -1.36 | 2.2 | 20.33 | 43.55 | 18.8 | 68.87 | False |  | strong_accumulation | 1.09 | 0.95 | 3 | 3 | 4.56 | 2.13 | -26.52 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 53.325092938625424 | 40.87924777938564 | 4.09 | 19.35 | 27.9 | 60.42 | 32.13 | 67.8 | False |  | strong_accumulation | 1.5 | 1.94 | 3 | 3 | 9.06 | 8.02 | -12.97 | 17 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 8.05 | 14.29 | -8.37 | 98.1 | 20.23 | 92.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.28 | -0.58 | 2 | 1 | 4.72 | 3.28 | -25.58 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth |  | 72.07351671395091 | 95.02794974786696 | 10.89 | -8.21 | -9.24 | 3.64 | 28.67 | 28.67 | False |  | distribution_warning | -0.88 | -0.09 | 1 | 1 | 5.05 | 2.61 | -25.1 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 77.38084589596791 | 70.28827013710922 | 7.47 | -5.02 | -24.98 | 16.28 | 36.74 | 38.31 | False |  | distribution_warning | -0.2 | -0.52 | 1 | 2 | 6.17 | 0.39 | -38.99 | 13 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | 5.49 | -1.66 | -11.57 | -8.26 | 20.51 | 20.51 | False |  | strong_accumulation | 0.04 | 0.12 | 2 | 2 | 5.07 | 2.5 | -17.71 | 19 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 5.57 | 4.94 | 10.74 | 52.72 | 12.52 | 69.73 | False |  | strong_accumulation | 1.46 | 1.22 | 3 | 2 | 3.48 | 3.3 | -12.81 | 18 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 4.99 | -16.97 | 2.44 | 10.31 | 13.08 | 15.99 | False |  | distribution_warning | -0.42 | -0.36 | 1 | 1 | -0.43 | -1.76 | -27.97 | 16 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 7.68 | 11.37 | 18.02 | 152.16 | 40.84 | 160.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | -0.5 | 2 | 2 | 13.09 | 9.61 | -11.44 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 14.76 | 24.95 | 42.61 | 116.72 | 47.22 | 113.23 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | 0.32 | 2 | 1 | 13.99 | 13.67 | -4.89 |  | fail_low_response_condition |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | 18.15 | 17.94 | 11.53 | 11.9 | 28.95 | 28.95 | False |  | distribution_warning | -1.16 | -1.45 | 1 | 2 | 15.25 | 12.62 | -2.87 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 63.77094494612451 | 73.90317152093164 | 3.6 | -2.95 | 4.55 | 24.59 | 17.95 | 40.07 | False |  | mild_accumulation | -0.84 | 0.51 | 0 | 2 | 1.59 | 0.17 | -20.69 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 1.44 | -8.9 | 2.75 | 7.45 | 14.21 | 14.21 | False |  | distribution_warning | -4.84 | -5.29 | 0 | 0 | -0.57 | -2.99 | -30.9 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 12.16 | 9.15 | 66.89 | 75.9 | 69.79 | 146.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | 0.13 | 1 | 1 | 16.03 | 14.29 | -3.17 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -8.47 | 3.84 | 34.95 | 68.93 | 43.82 | 83.07 | True | 距120日低點反彈>80% | strong_accumulation | 2.02 | 0.13 | 2 | 2 | 0.21 | 0.32 | -13.14 |  | fail_already_priced_in |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 0.18 | 1.07 | 8.19 | 16.87 | 10.29 | 22.68 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 0 | 0.26 | 0.38 | -11.11 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 9.38 | -0.77 | -10.47 | -7.23 | 20.31 | 20.31 | False |  | strong_accumulation | 0.1 | 0.09 | 2 | 2 | 7.11 | 4.06 | -33.96 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | 2.09 | 2.09 | 4.28 | -5.8 | 6.85 | 8.94 | False |  | distribution_warning | -0.72 | -0.6 | 1 | 2 | 1.22 | 1.11 | -4.65 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | 0.53 | 19.67 | -8.77 | 30.59 | 32.41 | 49.35 | False |  | distribution_warning | -1.84 | -1.29 | 0 | 1 | 7.57 | 3.8 | -25.33 | 16 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 2.79 | -1.57 | -0.63 | 18.98 | 16.11 | 38.72 | False |  | distribution_warning | -0.49 | -0.14 | 0 | 0 | 1.01 | -0.98 | -25.36 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 15.74 | 17.92 | 37.87 | 163.71 | 58.9 | 202.91 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.05 | 5.15 | 2 | 2 | 23.66 | 17.98 | -9.2 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 11.41 | 2.36 | 4.57 | 68.09 | 28.93 | 81.23 | True | 距120日低點反彈>80% | mild_accumulation | 2.74 | 0.0 | 2 | 0 | 8.91 | 7.52 | -9.29 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 5.77 | -0.75 | -9.06 | 94.87 | 23.72 | 97.04 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.48 | -0.18 | 1 | 1 | 1.73 | 0.46 | -23.12 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 4.62 | 2.05 | 3.75 | 50.18 | 23.88 | 72.44 | False |  | strong_accumulation | 0.8 | 1.47 | 2 | 3 | 4.14 | 2.5 | -11.07 | 18 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | 5.27 | -9.2 | -38.64 | 16.71 | 32.97 | 32.97 | False |  | strong_accumulation | 1.74 | 1.94 | 2 | 2 | 5.24 | -0.49 | -45.36 | 23 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | 4.25 | 3.07 | -4.01 | 6.34 | 6.79 | 10.07 | False |  | strong_accumulation | 0.13 | 0.12 | 2 | 2 | 2.01 | 0.74 | -9.21 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | 3.6 | -13.18 | -4.43 | 22.94 | 24.32 | 37.52 | False |  | mild_accumulation | -0.01 | 0.56 | 1 | 2 | 3.11 | -1.74 | -30.13 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | 0.9 | 3.94 | 0.45 | -0.44 | 4.42 | 5.65 | False |  | mild_accumulation | 0.09 | -0.06 | 2 | 2 | 0.38 | -0.74 | -20.95 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 1.89 | 2.27 | 5.88 | -6.9 | 11.57 | 11.57 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 2.23 | 2.08 | -10.0 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -1.28 | -3.35 | 1.17 | -16.43 | 6.46 | 6.46 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -3.31 | -2.31 | -14.14 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 0.91 | 2.65 | 2.06 | 14.67 | 8.13 | 32.2 | False |  | strong_accumulation | 1.41 | 1.45 | 3 | 3 | 1.38 | 1.38 | -5.41 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 7.23 | 1.55 | -15.39 | -35.78 | 10.86 | 10.86 | False |  | strong_accumulation | 0.63 | 0.48 | 3 | 2 | 2.58 | 1.67 | -23.54 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 4.31 | -0.73 | -9.12 | -9.96 | 7.11 | 7.11 | False |  | distribution_warning | 0.0 | -0.02 | 2 | 2 | 1.84 | 0.49 | -15.04 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | 2.43 | -5.38 | 4.98 | -2.31 | 7.54 | 7.54 | False |  | strong_accumulation | 0.75 | 0.64 | 2 | 2 | 1.47 | 0.2 | -10.59 | 23 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 4.05 | 4.18 | 21.42 | 24.36 | 23.48 | 31.87 | False |  | mild_accumulation | 0.57 | 0.32 | 3 | 1 | 5.38 | 5.49 | -1.58 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -12.61 | -16.67 | 22.07 | 14.54 | 26.83 | 52.49 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 1 | -21.1 | -15.27 | -41.11 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 11.14 | 8.49 | -8.91 | -13.89 | 12.98 | 12.98 | False |  | strong_accumulation | 0.09 | 0.09 | 2 | 2 | 7.11 | 6.06 | -12.04 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 21.97 | 13.71 | 16.53 | 43.58 | 33.27 | 48.89 | False |  | mild_accumulation | -0.73 | 0.04 | 1 | 2 | 16.84 | 14.16 | -4.73 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 1.2 | -17.26 | 0.79 | 12.89 | 7.63 | 28.93 | False |  | distribution_warning | -0.45 | -0.41 | 1 | 0 | -5.26 | -4.2 | -22.09 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 22.99 | 22.99 | 20.5 | 73.7 | 66.15 | 102.65 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.07 | 2.78 | 1 | 1 | 24.07 | 18.97 | -4.97 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 7.07 | -18.15 | -12.12 | 82.88 | 39.61 | 99.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.16 | -0.49 | 2 | 1 | 3.76 | -0.32 | -33.66 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 6.15 | 30.19 | 10.62 | 71.96 | 36.97 | 82.78 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.22 | 1.02 | 3 | 2 | 13.99 | 9.89 | -6.91 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 73.91966377290892 | 26.75099850600647 | 18.81 | 25.14 | 54.51 | 77.92 | 54.51 | 94.95 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.89 | 2.49 | 3 | 2 | 17.68 | 15.51 | -7.3 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 117.5894936306649 | 96.80997008021892 | 3.99 | 0.57 | -15.49 | 46.82 | 24.6 | 48.37 | False |  | distribution_warning | -0.52 | -1.29 | 1 | 1 | 5.43 | 2.56 | -18.33 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | 4.56 | -0.4 | -4.0 | 59.75 | 20.43 | 77.15 | False |  | distribution_warning | -1.91 | -2.05 | 1 | 1 | 4.07 | 4.36 | -15.15 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 94.8509470404764 | 111.03077976261774 | 3.53 | 8.11 | -24.53 | 25.71 | 22.22 | 27.17 | False |  | mild_accumulation | 0.17 | 0.03 | 2 | 1 | 8.04 | 4.14 | -28.57 | 19 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 270.5877639328499 | 61.05386791096055 | 5.39 | -8.58 | -5.63 | -4.48 | 17.84 | 17.84 | False |  | distribution_warning | -0.96 | -2.25 | 1 | 1 | 1.57 | -0.67 | -27.85 | 18 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 12.63 | 4.74 | -9.53 | 13.79 | 35.02 | 35.02 | False |  | distribution_warning | -0.33 | -0.22 | 0 | 2 | 12.43 | 7.58 | -26.17 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | 13.35 | 13.13 | 15.74 | 23.82 | 21.57 | 38.46 | False |  | mild_accumulation | 0.08 | 0.0 | 3 | 0 | 10.78 | 9.69 | -5.78 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 54.59950544814572 | 34.30071340658413 | 5.38 | 5.76 | -13.27 | 54.13 | 39.67 | 73.71 | False |  | distribution_warning | -1.25 | -1.93 | 2 | 0 | 12.9 | 6.78 | -28.21 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -2.64 | -18.64 | -28.14 | 55.59 | 6.67 | 55.59 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -7.62 | -9.25 | -42.79 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 4.41 | -39.32 | -8.58 | 64.86 | 36.02 | 91.55 | True | 距120日低點反彈>80% | distribution_warning | -1.65 | -0.5 | 1 | 0 | -17.66 | -11.39 | -47.01 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 21.18 | -24.95 | -10.97 | 87.84 | 53.07 | 106.75 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.32 | -2.67 | 0 | 1 | 8.07 | -1.74 | -52.19 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth | A_優先追蹤 | 204.3244857198993 | 247.3095962162866 | 0.91 | 7.74 | -14.58 | 45.85 | 24.63 | 67.0 | False |  | mild_accumulation | -0.54 | 1.15 | 2 | 1 | 6.45 | 1.33 | -37.22 | 21 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 8.18 | -27.01 | -16.01 | 133.89 | 46.14 | 142.37 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.61 | -0.44 | 0 | 1 | -2.09 | -4.23 | -37.44 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 6.81 | 39.92 | 35.46 | 144.6 | 45.09 | 188.14 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 19.26 | 15.92 | -6.25 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 60.760461865560174 | 88.15608743643294 | -2.05 | 34.04 | 36.43 | 45.25 | 37.41 | 55.92 | True | 近20日漲幅>25% | strong_accumulation | 7.78 | 7.93 | 3 | 3 | 11.57 | 9.6 | -5.68 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 1.47 | 2.59 | 13.06 | -1.42 | 13.06 | 16.39 | False |  | distribution_warning | -0.01 | -0.01 | 1 | 0 | 0.25 | 0.74 | -2.46 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | 2.74 | -5.86 | -19.06 | 3.21 | 25.14 | 25.14 | False |  | distribution_warning | -1.83 | -2.16 | 0 | 1 | 3.71 | -0.58 | -33.63 | 13 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 19.54 | 23.26 | -2.17 | 100.2 | 56.06 | 131.54 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.86 | -0.48 | 1 | 1 | 20.38 | 15.65 | -11.83 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 9.61 | -0.53 | 7.61 | 94.86 | 43.48 | 99.79 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.4 | -2.78 | 0 | 1 | 8.01 | 3.62 | -22.63 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 8.82 | 6.4 | -3.79 | -2.48 | 15.2 | 15.2 | False |  | distribution_warning | -1.26 | -1.28 | 1 | 0 | 5.65 | 3.22 | -21.02 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 3.29 | 1.34 | 6.68 | 26.21 | 20.69 | 49.67 | False |  | mild_accumulation | 0.85 | 0.0 | 2 | 2 | 6.17 | 1.84 | -36.14 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 5.83 | -10.91 | -28.51 | -14.01 | 29.55 | 29.55 | False |  | strong_accumulation | 0.94 | 1.28 | 2 | 2 | 3.33 | -1.53 | -38.83 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | -1.93 | 32.41 | 22.07 | 26.83 | 35.95 | 45.18 | True | 近20日漲幅>25% | strong_accumulation | 2.18 | 3.33 | 3 | 3 | 10.89 | 7.99 | -11.63 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 16.67 | 6.17 | -19.37 | 17.01 | 50.38 | 59.48 | True | 距60日低點反彈>50% | distribution_warning | -1.1 | -0.18 | 1 | 2 | 14.72 | 9.34 | -21.68 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -4.35 | 23.94 | 11.96 | 59.42 | 30.56 | 71.21 | False |  | strong_accumulation | 1.16 | 1.54 | 2 | 2 | 4.19 | 3.24 | -13.89 | 19 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | 6.81 | 5.02 | 1.62 | 94.57 | 23.04 | 93.97 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.95 | 1.03 | 3 | 3 | 7.7 | 6.9 | -3.83 |  | fail_already_priced_in |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | 8.58 | 1.49 | -18.97 | -0.49 | 19.74 | 19.74 | False |  | mild_accumulation | -0.28 | 0.35 | 2 | 2 | 5.8 | 3.22 | -27.05 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 16.75 | -13.48 | -25.61 | -13.48 | 36.31 | 36.31 | False |  | mild_accumulation | -0.31 | 0.22 | 1 | 2 | 5.48 | -0.57 | -37.91 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 10.21 | 18.61 | 22.88 | 1.73 | 33.59 | 33.59 | False |  | mild_accumulation | 0.0 | 0.32 | 2 | 3 | 7.63 | 8.49 | -1.31 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 8.71 | 7.9 | -11.9 | 92.51 | 34.88 | 105.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.1 | -1.0 | 2 | 1 | 9.98 | 6.21 | -24.91 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 2.96 | -3.52 | -5.79 | -19.85 | 7.42 | 7.42 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.24 | -0.74 | -22.24 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 128.9172485640275 | 121.34662298357856 | 5.81 | -4.27 | -7.61 | 28.53 | 27.22 | 35.5 | False |  | distribution_warning | -1.53 | -1.16 | 1 | 1 | 6.15 | 0.26 | -35.02 | 13 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 0.34 | 5.06 | -12.12 | 1.59 | 18.93 | 18.93 | False |  | distribution_warning | -0.28 | 0.0 | 2 | 1 | 4.52 | 2.75 | -23.76 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 2.96 | -5.0 | 5.77 | 73.59 | 19.57 | 96.43 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.87 | -1.02 | 1 | 1 | 2.38 | 1.53 | -18.04 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -1.05 | -14.97 | -16.22 | -12.62 | 7.98 | 7.98 | False |  | distribution_warning | -0.76 | -0.19 | 0 | 0 | -3.99 | -5.4 | -25.65 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | 3.37 | 1.18 | -3.91 | -23.89 | 8.18 | 8.18 | False |  | strong_accumulation | 0.03 | 0.02 | 2 | 2 | -0.87 | -1.2 | -10.88 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 17.72 | -5.46 | -22.5 | 69.28 | 37.78 | 68.71 | False |  | strong_accumulation | 0.18 | 0.04 | 2 | 2 | 10.96 | 7.07 | -33.27 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 98.74936839745938 | 71.28591290526819 | 7.02 | 22.27 | 3.0 | 37.59 | 40.41 | 61.0 | False |  | strong_accumulation | 4.71 | 2.93 | 2 | 3 | 16.4 | 10.33 | -13.0 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 11.83 | -0.34 | -28.36 | 5.4 | 39.52 | 39.52 | False |  | distribution_warning | -3.43 | -1.67 | 0 | 0 | 10.86 | 5.25 | -39.84 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | 1.19 | -15.0 | -29.39 | 35.46 | 35.73 | 35.73 | False |  | distribution_warning | -6.91 | -7.91 | 1 | 1 | 2.91 | -2.69 | -42.13 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.0 | 6.61 | 27.72 | 28.15 | 29.43 | 48.85 | False |  | distribution_warning | -0.18 | 0.0 | 0 | 0 | 1.6 | 2.29 | -4.21 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 51.30291899664847 | 56.85528675042054 | 2.13 | 6.3 | 9.76 | 10.83 | 19.55 | 21.63 | False |  | strong_accumulation | 3.61 | 4.59 | 3 | 3 | 4.2 | 4.14 | -4.11 | 22 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 1.56 | -3.56 | -7.53 | -3.84 | 3.01 | 3.01 | False |  | distribution_warning | 0.0 | -0.14 | 2 | 2 | -1.32 | -1.11 | -22.41 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -4.13 | 0.0 | -1.12 | -15.52 | 7.82 | 7.82 | False |  | mild_accumulation | 0.11 | 0.04 | 2 | 1 | -2.62 | -1.81 | -7.74 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 0.39 | -2.02 | 2.64 | 1.3 | 7.02 | 7.02 | False |  | distribution_warning | -0.41 | -0.8 | 0 | 0 | -1.57 | -1.09 | -11.09 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 5.84 | -3.14 | 8.83 | 17.78 | 10.99 | 20.78 | False |  | mild_accumulation | 0.1 | -0.1 | 1 | 1 | -1.3 | -0.04 | -5.81 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 15.68 | 12.03 | 1.56 | 36.24 | 21.43 | 36.24 | False |  | mild_accumulation | 0.25 | 1.22 | 1 | 1 | 13.68 | 10.37 | -8.64 |  | fail_low_response_condition |