# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-03 02:34:40 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 710050 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 437 |
| tdcc_mild_accumulation_count | 765 |
| tdcc_distribution_warning_count | 580 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 98 |
| already_priced_in_excluded | 36 |
| overheat_pass | 62 |
| score_pass | 62 |
| theme_priority_pass | 55 |
| final_rows | 55 |

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
| fail_low_response_condition | 239 |
| fail_already_priced_in | 36 |
| fail_defensive_or_traditional_excluded | 4 |
| fail_mainstream_score_lt_10 | 3 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | -6.9 | 8.43 | 3.35 | -16.92 | 15.02 | 15.02 | False |  | mild_accumulation | -0.39 | 0.25 | 0 | 2 | 1.05 | 0.46 | -13.6 | 17 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -2.06 | 3.16 | -6.12 | -26.06 | 4.61 | 4.61 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | 0.66 | 0.15 | -15.94 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -0.97 | 0.49 | -8.48 | 16.21 | 8.01 | 23.64 | False |  | mild_accumulation | 0.36 | 0.0 | 2 | 0 | -0.46 | -1.22 | -15.98 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -1.68 | 7.83 | 0.43 | 0.0 | 10.38 | 10.38 | False |  | strong_accumulation | 1.99 | 1.33 | 3 | 2 | 0.67 | 1.0 | -5.26 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -1.67 | -3.55 | -6.37 | -7.11 | 3.52 | 4.13 | False |  | mild_accumulation | 0.03 | -0.01 | 3 | 0 | -1.23 | -1.46 | -12.41 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -1.99 | -1.6 | -17.45 | 13.36 | 4.68 | 11.82 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -1.01 | -1.51 | -26.79 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -3.0 | -9.35 | -30.71 | -35.33 | 5.43 | 5.43 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.35 | -3.79 | -34.46 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -5.1 | -7.62 | 8.98 | 36.1 | 12.96 | 47.46 | False |  | mild_accumulation | -0.61 | 0.79 | 1 | 2 | -5.55 | -3.35 | -13.62 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 0.51 | 3.38 | -2.57 | -5.24 | 11.02 | 11.02 | False |  | mild_accumulation | 0.93 | -0.73 | 2 | 1 | -0.0 | 0.41 | -14.41 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -5.66 | 33.59 | 75.0 | 93.91 | 74.13 | 96.63 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.82 | 2 | 2 | 9.14 | 9.93 | -7.16 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 4.83 | 17.63 | 37.15 | 76.32 | 39.36 | 92.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.51 | -1.63 | 1 | 2 | 3.18 | 4.28 | -30.6 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -0.42 | 9.41 | 15.66 | 10.78 | 19.76 | 26.38 | False |  | strong_accumulation | 0.63 | 0.7 | 3 | 3 | 3.86 | 3.88 | -6.22 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -3.86 | 1.82 | -3.03 | -1.75 | 4.67 | 12.0 | False |  | mild_accumulation | 0.03 | -0.01 | 2 | 1 | -1.67 | -1.3 | -8.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -4.46 | 7.98 | -12.59 | 17.89 | 14.73 | 23.56 | False |  | mild_accumulation | 0.7 | 0.28 | 2 | 1 | 0.65 | 0.91 | -18.93 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -4.45 | 46.41 | 124.35 | 313.88 | 127.67 | 340.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.87 | -1.97 | 3 | 0 | 4.34 | 8.95 | -8.09 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -6.71 | -13.66 | -28.72 |  | 0.72 |  | False |  | distribution_warning | -0.26 | -0.7 | 0 | 0 | -7.02 | -6.43 | -27.23 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -1.26 | -14.49 | -12.59 | 5.36 | 3.06 | 16.83 | False |  | mild_accumulation | 1.06 | -0.99 | 2 | 1 | -5.86 | -7.16 | -37.73 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.81 | 7.43 | 12.07 | 18.03 | 14.97 | 29.31 | False |  | distribution_warning | -0.41 | -2.1 | 0 | 0 | 1.64 | 1.03 | -12.15 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -1.74 | 3.33 | 2.31 | -3.28 | 5.62 | 20.16 | False |  | mild_accumulation | 0.04 | 0.02 | 2 | 1 | -0.8 | -1.22 | -11.43 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -4.79 | 0.83 | 35.28 | 122.66 | 42.5 | 149.27 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.14 | -0.76 | 2 | 1 | -2.2 | -1.06 | -26.42 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | -3.06 | 2.39 | 32.96 | 103.04 | 39.12 | 116.97 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.84 | -0.43 | 2 | 2 | 6.11 | 2.66 | -29.54 |  | fail_already_priced_in |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | 0.31 | 1.25 | -3.0 | 57.56 | 27.17 | 74.41 | False |  | distribution_warning | -1.0 | -1.51 | 0 | 1 | 0.22 | 0.06 | -35.01 | 14 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 1.83 | -2.9 | -6.86 | 18.4 | 10.82 | 33.87 | False |  | distribution_warning | -0.39 | -0.34 | 0 | 0 | -1.17 | -0.06 | -9.55 | 14 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 0.56 | -6.57 | -28.1 | 88.81 | 18.29 | 122.22 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.21 | -2.24 | 1 | 1 | -6.08 | -7.92 | -55.74 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -1.99 | 4.68 | -14.29 | -5.75 | 33.99 | 33.99 | False |  | distribution_warning | -1.54 | -1.3 | 1 | 1 | -3.09 | -2.03 | -35.94 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -1.38 | 5.92 | 16.23 | 44.94 | 52.99 | 113.6 | True | 距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.68 | 0.62 | 2 | 2 | 0.69 | 2.2 | -23.34 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | 4.14 | -10.27 | -11.57 | 47.08 | 16.3 | 46.08 | False |  | distribution_warning | -0.19 | -0.04 | 1 | 1 | -1.02 | -0.88 | -24.25 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 0.34 | -9.99 | 2.46 | 11.2 | 8.84 | 16.84 | False |  | distribution_warning | -0.46 | -0.37 | 0 | 0 | -1.6 | -0.88 | -11.09 | 18 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.0 | 3.34 | 0.28 | -11.24 | 6.44 | 6.44 | False |  | distribution_warning | -0.18 | -0.07 | 1 | 1 | 0.45 | -0.73 | -13.61 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 4.57 | 35.5 | 25.14 | 144.14 | 84.68 | 161.12 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.73 | 3.55 | 2 | 1 | 18.07 | 14.85 | -7.29 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -0.3 | 1.37 | -3.76 | 51.36 | 17.25 | 66.71 | False |  | strong_accumulation | 0.84 | 0.76 | 2 | 2 | 0.6 | 1.47 | -9.39 | 20 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 4.02 | 20.53 | 19.67 | 70.32 | 59.06 | 85.32 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.83 | 1.54 | 3 | 3 | 9.46 | 10.48 | -1.46 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -0.25 | 4.77 | -19.39 | 34.35 | 14.16 | 34.81 | False |  | distribution_warning | -0.15 | -0.86 | 1 | 1 | -5.76 | -3.9 | -20.36 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | -0.58 | -3.23 | -10.68 | -0.2 | 15.12 | 15.12 | False |  | distribution_warning | -1.07 | -0.33 | 0 | 1 | -2.5 | -2.82 | -32.98 | 12 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 12.98 | 25.0 | -13.6 | 28.14 | 66.67 | 66.67 | True | 距60日低點反彈>50% | distribution_warning | -1.22 | -1.32 | 0 | 2 | 13.66 | 12.33 | -25.63 |  | fail_low_response_condition |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | 0.0 | 1.15 | -3.44 | -2.37 | 18.81 | 18.81 | False |  | distribution_warning | -0.67 | -0.54 | 1 | 2 | 0.98 | 1.51 | -14.3 | 13 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 2.84 | 5.7 | 4.78 | 45.77 | 15.87 | 63.21 | False |  | mild_accumulation | 0.66 | 0.25 | 1 | 1 | 1.76 | 2.96 | -10.07 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 131.31830412017854 | 92.66781063949252 | 1.35 | 10.86 | -10.49 | 16.61 | 20.79 | 22.32 | False |  | distribution_warning | -0.06 | -0.01 | 1 | 2 | 3.43 | 2.31 | -14.25 | 17 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -7.63 | 3.81 | 14.15 | 101.67 | 38.55 | 109.83 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.59 | -1.21 | 1 | 0 | -4.08 | -1.53 | -15.84 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 0.58 | 9.32 | 46.92 | 98.85 | 54.12 | 120.73 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.75 | 1 | 1 | 2.82 | 5.49 | -3.22 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | 0.0 | 1.29 | 3.8 | 12.32 | 19.81 | 19.81 | False |  | mild_accumulation | 0.93 | -0.05 | 2 | 0 | -2.23 | 0.38 | -7.64 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -3.29 | -15.07 | -12.81 | -27.06 | 3.14 | 3.14 | False |  | distribution_warning | -1.76 | -2.67 | 1 | 0 | -5.51 | -6.02 | -39.28 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 0.19 | 16.4 | 52.58 | 90.79 | 60.87 | 160.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.83 | 2.98 | 3 | 3 | 1.88 | 4.23 | -8.96 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -0.92 | -23.32 | 13.4 | 21.06 | 13.92 | 44.81 | False |  | distribution_warning | -4.47 | -0.95 | 2 | 2 | -7.79 | -6.31 | -28.83 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -0.9 | -3.51 | -0.9 | -1.79 | 1.85 | 9.13 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -1.19 | -1.14 | -13.93 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 11.08 | 14.25 | -16.98 | -1.96 | 25.31 | 25.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 9.88 | 8.94 | -15.76 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 233.9341638249008 | 396.6930034235488 | -2.28 | 1.58 | -1.53 | -10.67 | 2.67 | 7.54 | False |  | strong_accumulation | 0.46 | 0.98 | 2 | 2 | -1.08 | -0.88 | -5.87 | 21 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | -1.5 | 4.96 | 0.68 | 4.04 | 37.27 | 42.21 | False |  | strong_accumulation | 1.28 | 0.02 | 2 | 2 | 0.47 | 1.84 | -10.02 | 22 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -2.57 | -10.11 | -4.69 | 10.92 | 5.37 | 18.79 | False |  | distribution_warning | -0.12 | -0.08 | 1 | 1 | -3.48 | -3.91 | -32.26 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 5.21 | 18.82 | 36.03 | 155.37 | 71.19 | 207.46 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.41 | 10.78 | 2 | 2 | 7.78 | 10.83 | -6.7 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 12.18 | 22.38 | 32.24 | 81.03 | 55.79 | 107.92 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.38 | 3.25 | 2 | 2 | 14.01 | 15.82 | -1.41 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 6.84 | 17.79 | 7.22 | 61.75 | 41.63 | 75.5 | False |  | mild_accumulation | 1.42 | -0.27 | 3 | 2 | 8.42 | 7.37 | -9.38 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 54.39975818511566 | 39.61008944759205 | 0.0 | 0.8 | 6.36 | 51.2 | 24.88 | 56.48 | False |  | distribution_warning | -0.13 | -0.85 | 1 | 1 | 2.01 | 2.32 | -10.36 |  | fail_low_response_condition |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -1.74 | 3.05 | -33.07 | -43.6 | 30.96 | 30.96 | False |  | mild_accumulation | 0.62 | 0.52 | 2 | 1 | 0.08 | -0.63 | -39.31 | 22 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.31 | -0.41 | -7.47 | 0.94 | 2.55 | 3.21 | False |  | distribution_warning | -0.11 | -0.27 | 2 | 2 | -1.49 | -1.48 | -12.82 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | -1.42 | -0.65 | -18.17 | 16.36 | 21.76 | 21.76 | False |  | strong_accumulation | 0.95 | 0.53 | 3 | 2 | -0.7 | -1.25 | -31.56 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -2.17 | 1.12 | -6.05 | -4.05 | 4.65 | 4.65 | False |  | strong_accumulation | 0.25 | 0.36 | 2 | 2 | -0.92 | -1.03 | -20.77 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -4.19 | 13.36 | 13.36 | 3.85 | 15.56 | 22.73 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 3.34 | 2.8 | -5.41 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -4.19 | -1.86 | 0.59 | -12.28 | 2.39 | 5.54 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.44 | -2.17 | -14.89 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -0.1 | 8.85 | 14.44 | 30.48 | 14.85 | 42.28 | False |  | strong_accumulation | 1.8 | 1.95 | 3 | 3 | 2.51 | 2.8 | -2.14 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | -0.78 | 2.27 | -19.37 | -46.51 | 8.04 | 8.04 | False |  | mild_accumulation | -0.46 | 0.04 | 0 | 2 | -1.43 | -1.15 | -25.49 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -1.86 | 6.86 | -8.91 | -6.16 | 8.21 | 8.21 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 2 | 0.54 | -0.09 | -14.16 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -2.06 | -3.01 | -6.2 | -11.59 | 1.73 | 1.83 | False |  | strong_accumulation | 0.23 | 0.17 | 2 | 2 | -2.07 | -2.01 | -15.34 | 22 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 5.59 | 12.76 | 22.68 | 34.87 | 36.02 | 44.59 | False |  | strong_accumulation | 0.68 | 0.42 | 3 | 2 | 5.34 | 6.02 | -10.83 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -11.25 | -17.92 | 6.18 | 28.95 | 13.71 | 41.06 | False |  | mild_accumulation | 0.02 | -0.01 | 1 | 0 | -6.56 | -9.52 | -45.53 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 1.28 | 8.79 | -10.0 | -24.14 | 9.39 | 9.39 | False |  | mild_accumulation | 0.1 | -2.07 | 1 | 0 | 1.43 | 1.38 | -11.21 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 4.45 | 14.29 | 11.48 | 33.33 | 28.54 | 40.79 | False |  | strong_accumulation | 2.93 | 2.89 | 3 | 2 | 1.79 | 3.13 | -8.11 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 0.42 | -6.61 | -5.88 | 11.63 | 2.56 | 21.83 | False |  | mild_accumulation | 0.36 | -0.03 | 2 | 2 | -2.28 | -3.1 | -26.38 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 2.93 | 17.78 | 35.99 | 44.73 | 74.84 | 91.5 | True | 距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 2.26 | 2.16 | 2 | 2 | 4.7 | 8.07 | -5.85 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -1.96 | -3.85 | -3.85 | 56.25 | 37.55 | 96.08 | True | 距120日低點反彈>80% | mild_accumulation | -0.79 | 0.21 | 0 | 1 | -1.99 | -1.59 | -34.64 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 4.91 | 21.25 | 28.79 | 73.75 | 64.27 | 80.38 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.03 | 1.27 | 1 | 2 | 7.59 | 9.61 | -5.16 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 73.91966377290892 | 26.75099850600647 | -2.27 | -7.38 | 14.43 | 45.81 | 17.1 | 49.92 | False |  | mild_accumulation | -0.42 | 1.72 | 1 | 2 | -5.86 | -2.58 | -22.4 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -0.45 | -7.95 | -11.65 | 16.61 | 16.81 | 36.08 | False |  | distribution_warning | -1.06 | -1.12 | 0 | 0 | -1.49 | -0.97 | -22.63 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -1.65 | -6.59 | -6.78 | 33.88 | 6.69 | 41.75 | False |  | distribution_warning | -2.09 | -0.79 | 1 | 2 | -4.16 | -3.49 | -24.83 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -4.83 | -16.89 | -25.2 | -25.05 | 3.89 | 3.89 | False |  | distribution_warning | -1.93 | -2.31 | 0 | 0 | -9.2 | -7.4 | -26.81 | 12 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth | A_優先追蹤 | 270.5877639328499 | 61.05386791096055 | 3.48 | 3.93 | 2.15 | 0.42 | 19.6 | 19.6 | False |  | strong_accumulation | 0.08 | 0.92 | 2 | 2 | 3.84 | 3.28 | -26.77 | 24 | selected |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 4.37 | 25.97 | 5.02 | 37.35 | 53.52 | 53.52 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.14 | -0.01 | 1 | 1 | 7.2 | 7.63 | -16.05 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -2.26 | 1.26 | -1.06 | 16.96 | 13.31 | 22.17 | False |  | mild_accumulation | 2.7 | 0.0 | 1 | 1 | -3.65 | -1.55 | -10.79 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -3.91 | -7.38 | -18.92 | 36.19 | 28.27 | 59.53 | False |  | distribution_warning | -0.29 | -0.7 | 1 | 1 | -4.98 | -3.13 | -30.68 | 12 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 3.12 | 13.54 | -25.56 | -35.62 | 24.89 | 24.89 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 7.55 | 4.43 | -26.05 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 11.81 | 26.79 | 56.04 | 137.86 | 81.35 | 155.4 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.31 | -5.15 | 0 | 1 | 21.11 | 16.86 | -29.35 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 1.81 | 14.63 | -19.57 | 68.5 | 47.81 | 86.81 | True | 距120日低點反彈>80% | distribution_warning | -4.21 | -3.49 | 1 | 1 | 0.4 | -1.89 | -53.84 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 204.3244857198993 | 247.3095962162866 | -5.12 | -0.28 | -16.59 | 48.52 | 31.34 | 76.0 | False |  | distribution_warning | -1.43 | -1.72 | 0 | 1 | 2.44 | 2.35 | -20.72 | 16 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 8.1 | 20.0 | -10.52 | 133.84 | 78.14 | 154.61 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.83 | -7.13 | 1 | 0 | 8.21 | 7.43 | -23.74 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -11.88 | 15.71 | 24.57 | 176.76 | 45.66 | 189.27 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.43 | -1.57 | 1 | 0 | -4.67 | -1.7 | -18.08 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 1.92 | -3.89 | 13.46 | 38.43 | 33.45 | 51.43 | False |  | distribution_warning | -0.27 | -0.36 | 1 | 1 | 0.66 | 3.1 | -9.95 | 12 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -1.77 | 0.0 | 11.2 | 5.3 | 11.65 | 16.81 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | -0.23 | -0.08 | -2.11 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | 3.7 | 0.45 | -22.76 | 3.7 | 24.58 | 24.58 | False |  | distribution_warning | -0.78 | -0.53 | 1 | 1 | 0.09 | 0.11 | -25.08 | 13 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | -3.76 | 34.28 | 38.54 | 157.42 | 85.67 | 175.47 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.42 | 2 | 1 | 7.63 | 9.08 | -9.17 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 4.88 | 26.74 | 30.59 | 115.0 | 82.42 | 154.01 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.94 | 4.34 | 2 | 3 | 9.36 | 9.79 | -7.81 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.34606716091966 | 18.855891461759168 | 4.34 | 9.07 | -6.16 | 5.79 | 21.87 | 21.87 | False |  | mild_accumulation | 0.14 | -1.25 | 2 | 0 | 3.53 | 4.38 | -10.39 | 19 | selected |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 3.12 | -3.15 | -30.92 | 35.22 | 14.06 | 40.75 | False |  | distribution_warning | -0.42 | -0.14 | 1 | 2 | -0.36 | 0.14 | -37.68 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 0.23 | 4.0 | -28.05 | -28.92 | 28.82 | 28.82 | False |  | strong_accumulation | 0.48 | 0.37 | 2 | 3 | -0.32 | -0.65 | -35.64 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 0.79 | 32.95 | 51.05 | 54.9 | 92.98 | 106.07 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.15 | -0.41 | 2 | 2 | 11.94 | 13.5 | -5.33 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 6.06 | 16.34 | 0.72 | 31.66 | 59.7 | 69.35 | True | 距60日低點反彈>50% | distribution_warning | -1.41 | -4.39 | 1 | 1 | 7.03 | 7.89 | -14.2 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 59.590900789853706 | 37.93424741228517 | 8.23 | -7.86 | -1.36 | 31.91 | 28.78 | 29.94 | False |  | distribution_warning | -0.16 | -0.27 | 2 | 1 | -0.73 | 0.35 | -15.07 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | -5.56 | -20.93 | -5.56 | 13.33 | 4.94 | 17.92 | False |  | distribution_warning | -2.05 | -2.31 | 0 | 0 | -8.79 | -6.33 | -21.84 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -1.46 | 3.91 | -13.68 | -20.47 | 17.99 | 17.99 | False |  | mild_accumulation | 0.51 | -0.01 | 3 | 1 | -0.81 | -0.44 | -18.22 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 9.21 | 13.7 | -25.0 | -21.2 | 39.11 | 39.11 | False |  | mild_accumulation | 0.01 | -0.77 | 1 | 2 | 6.89 | 4.88 | -36.64 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 7.09 | 15.02 | 36.01 | 2.01 | 41.16 | 41.16 | False |  | strong_accumulation | 0.27 | 0.26 | 2 | 2 | 5.23 | 6.34 | -1.06 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 19.21 | 11.01 | 15.24 | 101.67 | 49.38 | 111.35 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.85 | 2 | 1 | 11.87 | 13.19 | -3.97 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 0.76 | 3.33 | -8.82 | -12.46 | 8.66 | 8.66 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 1.11 | 0.64 | -15.0 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 128.9172485640275 | 121.34662298357856 | -3.83 | -0.58 | -27.93 | 9.21 | 24.31 | 24.31 | False |  | mild_accumulation | -0.71 | 0.58 | 1 | 1 | -1.22 | -1.35 | -36.51 | 17 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 15.34 | 14.96 | 15.08 | 13.94 | 37.33 | 37.33 | False |  | mild_accumulation | 1.43 | 1.47 | 2 | 1 | 10.72 | 10.77 | -0.96 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -1.95 | -3.83 | -13.36 | 61.06 | 14.99 | 88.91 | True | 距120日低點反彈>80% | distribution_warning | -3.78 | -3.03 | 0 | 0 | -1.79 | -1.07 | -19.6 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -2.41 | -4.71 | -7.21 | -28.54 | 7.6 | 7.6 | False |  | mild_accumulation | 0.21 | 0.38 | 3 | 1 | -1.01 | -2.17 | -25.92 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -3.54 | -6.62 | -10.73 | -33.89 | 1.28 | 1.28 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -5.78 | -5.52 | -18.13 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 12.43 | 24.13 | -10.35 | 23.95 | 52.41 | 52.41 | True | 距60日低點反彈>50% | strong_accumulation | 0.22 | 0.19 | 2 | 2 | 13.11 | 12.13 | -16.53 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 2.02 | 4.71 | 0.18 | 23.83 | 42.2 | 42.2 | False |  | distribution_warning | -4.56 | -1.03 | 2 | 1 | 1.65 | 4.11 | -5.44 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 3.52 | 23.86 | -2.22 | -5.11 | 68.1 | 68.1 | True | 距60日低點反彈>50% | mild_accumulation | 1.69 | -0.67 | 2 | 1 | 13.23 | 12.01 | -10.86 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 105.41523454519049 | 68.91539282131619 | -4.63 | -4.63 | -23.23 | -7.13 | 27.35 | 27.35 | False |  | mild_accumulation | -1.03 | 0.38 | 1 | 2 | -1.94 | -3.05 | -45.7 | 21 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 1.06 | 0.0 | 11.66 | 39.78 | 11.34 | 41.33 | False |  | mild_accumulation | 0.22 | 0.0 | 2 | 0 | 0.49 | 1.01 | -5.2 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -0.78 | -16.16 | -8.9 | -4.24 | 0.79 | 2.54 | False |  | distribution_warning | -8.96 | -8.86 | 0 | 1 | -5.21 | -4.27 | -19.16 | 14 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | -1.25 | -1.86 | -14.82 | -9.2 | 2.93 | 2.93 | False |  | distribution_warning | -0.45 | -0.52 | 1 | 0 | -0.24 | -0.87 | -24.67 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -0.45 | -5.38 | 0.23 | -12.0 | 3.53 | 7.58 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -0.11 | -0.69 | -7.95 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | -0.78 | -2.3 | -0.65 | -3.78 | 1.87 | 4.95 | False |  | distribution_warning | -0.32 | -0.29 | 1 | 1 | -2.05 | -1.74 | -12.8 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 0.32 | 5.36 | 3.8 | 13.33 | 10.35 | 17.35 | False |  | strong_accumulation | 0.46 | 0.23 | 2 | 2 | 1.9 | 1.31 | -3.82 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 5.05 | 37.36 | 26.46 | 45.29 | 48.45 | 50.79 | True | 近20日漲幅>25% | strong_accumulation | 3.39 | 6.39 | 3 | 3 | 5.69 | 7.2 | -10.15 |  | fail_already_priced_in |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 79.49201833634949 | 23.814868308479223 | 8.73 | 54.58 | 54.37 | 126.45 | 97.83 | 186.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.37 | 0.16 | 2 | 2 | 23.56 | 18.75 | -8.51 |  | fail_low_response_condition |