# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-21 04:26:30 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 692440 |
| tdcc_rows | 1971 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 434 |
| tdcc_mild_accumulation_count | 738 |
| tdcc_distribution_warning_count | 608 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 86 |
| already_priced_in_excluded | 25 |
| overheat_pass | 61 |
| score_pass | 61 |
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
| fail_low_response_condition | 251 |
| fail_already_priced_in | 25 |
| fail_defensive_or_traditional_excluded | 6 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 102.03987961747174 | 127.0977623123372 | 6.5 | 4.41 | 4.41 | -16.14 | 13.42 | 13.42 | False |  | mild_accumulation | -0.14 | 0.47 | 1 | 2 | 5.09 | 3.75 | -8.19 | 20 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -1.73 | -4.49 | -5.9 | -23.54 | 2.2 | 2.2 | False |  | mild_accumulation | 0.26 | -0.69 | 2 | 0 | -0.76 | -1.57 | -17.87 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.0 | -7.96 | 13.79 | 8.22 | 14.29 | 25.45 | False |  | distribution_warning | -0.76 | 0.0 | 1 | 1 | 1.02 | -0.35 | -14.75 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 0.0 | 6.82 | 6.33 | 1.73 | 10.85 | 10.85 | False |  | strong_accumulation | 0.48 | 0.69 | 2 | 2 | 5.36 | 4.02 | -2.08 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -1.94 | -8.31 | -1.94 | -7.59 | 3.52 | 4.13 | False |  | distribution_warning | -0.01 | -0.02 | 1 | 0 | -2.57 | -2.35 | -12.41 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -2.4 | -4.31 | 0.41 | 20.2 | 3.83 | 20.79 | False |  | strong_accumulation | 0.13 | 0.91 | 2 | 3 | -1.11 | -2.75 | -27.38 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -2.91 | -7.12 | -27.18 | -33.18 | 5.63 | 5.63 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | -2.12 | -4.35 | -32.43 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround | B_可觀察 | 50.77907738303081 | 32.86722140693869 | -3.4 | 1.07 | 2.16 | 28.51 | 15.92 | 50.58 | False |  | mild_accumulation | -0.61 | 0.3 | 1 | 2 | -2.57 | -2.11 | -12.07 | 14 | selected |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -4.64 | 1.43 | -5.22 | -8.87 | 8.93 | 8.93 | False |  | strong_accumulation | 0.97 | 0.25 | 2 | 2 | 0.15 | -0.7 | -16.02 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -1.14 | 11.4 | 54.59 | 84.76 | 58.22 | 83.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.84 | 2.58 | 3 | 3 | 10.54 | 7.78 | -10.49 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 1.8 | 10.03 | 81.43 | 76.72 | 81.04 | 88.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.73 | -2.12 | 1 | 2 | 10.01 | 5.32 | -32.0 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 4.23 | 7.64 | 22.56 | 18.15 | 21.69 | 22.99 | False |  | strong_accumulation | 0.29 | 0.23 | 2 | 2 | 5.56 | 5.8 | 0.0 | 22 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | 0.44 | 5.02 | 14.43 | -0.86 | 14.43 | 15.0 | False |  | distribution_warning | -0.04 | 0.0 | 0 | 1 | 2.77 | 2.16 | -8.37 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -1.18 | 2.87 | 4.58 | 12.56 | 12.05 | 21.26 | False |  | mild_accumulation | -0.01 | 0.28 | 1 | 1 | 2.09 | 1.08 | -20.82 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 13.81 | 69.82 | 196.28 | 339.27 | 188.6 | 376.07 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.4 | 2 | 1 | 31.65 | 26.33 | -7.69 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -0.33 | 6.34 | -8.76 |  | 9.42 |  | False |  | distribution_warning | -0.49 | -0.76 | 0 | 1 | -1.1 | -0.78 | -27.05 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -3.15 | -18.0 | -10.55 | 12.33 | 7.42 | 21.78 | False |  | mild_accumulation | -0.42 | 0.82 | 1 | 2 | -7.2 | -8.75 | -35.09 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | 10.75 | 1.91 | 16.82 | 35.96 | 18.33 | 36.39 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | 7.56 | 6.89 | -9.75 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 0.63 | 1.42 | 10.1 | -8.4 | 9.54 | 24.61 | False |  | strong_accumulation | 0.03 | 0.14 | 2 | 2 | 2.88 | 2.34 | -8.14 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -4.31 | 1.88 | 21.15 | 157.44 | 44.17 | 159.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.25 | 1.5 | 2 | 2 | 3.6 | 0.76 | -25.56 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | -13.09 | -22.71 | 14.44 | 119.42 | 31.11 | 125.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.92 | -3.88 | 1 | 1 | -8.46 | -9.84 | -37.75 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | -5.18 | -6.04 | -7.72 | 72.59 | 22.44 | 83.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.11 | 0.46 | 1 | 2 | 0.24 | -4.04 | -37.42 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | -5.92 | -4.27 | -6.27 | 13.59 | 8.83 | 31.47 | False |  | mild_accumulation | 0.48 | 0.49 | 1 | 1 | -2.59 | -2.52 | -21.5 | 16 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -15.11 | -19.25 | -24.26 | 116.99 | 23.11 | 134.17 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.61 | -1.72 | 1 | 1 | -2.26 | -9.91 | -53.93 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -10.62 | -5.79 | -23.75 | 24.49 | 32.9 | 37.39 | False |  | distribution_warning | -1.42 | -1.8 | 1 | 1 | 0.67 | -3.86 | -36.46 | 18 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -0.28 | 9.63 | 22.57 | 69.71 | 50.85 | 110.62 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.43 | -0.32 | 1 | 1 | 9.02 | 4.43 | -24.41 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -7.27 | -9.46 | -13.55 | 61.3 | 14.4 | 58.27 | False |  | distribution_warning | -0.35 | -0.51 | 1 | 1 | -4.24 | -5.77 | -25.49 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | -4.92 | -0.91 | 1.52 | 28.89 | 8.34 | 29.85 | False |  | mild_accumulation | 0.15 | 0.21 | 2 | 1 | -3.55 | -2.9 | -11.5 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 2.87 | -9.34 | 6.21 | 3.31 | 7.49 | 7.49 | False |  | distribution_warning | -0.48 | -0.04 | 1 | 1 | -0.69 | -0.42 | -12.76 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 6.07 | 11.89 | -16.59 | 132.57 | 47.98 | 144.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.71 | 0.92 | 2 | 2 | 12.01 | 6.28 | -21.24 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -6.25 | 2.38 | 0.94 | 60.25 | 13.56 | 67.32 | False |  | strong_accumulation | 1.53 | 1.51 | 3 | 3 | -0.15 | -0.9 | -27.2 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | -2.56 | 18.73 | 31.94 | 82.6 | 43.78 | 82.6 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.62 | 1.39 | 3 | 3 | 8.82 | 8.13 | -10.93 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -6.96 | -0.7 | -16.73 | 59.7 | 23.7 | 72.58 | False |  | distribution_warning | -0.54 | -0.88 | 1 | 1 | 2.96 | 1.12 | -21.03 | 18 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | -6.25 | -10.68 | -21.17 | 5.37 | 15.12 | 15.12 | False |  | mild_accumulation | -0.24 | 0.94 | 1 | 2 | -1.89 | -5.83 | -32.98 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 1.49 | 8.93 | -21.46 | 44.57 | 45.39 | 45.39 | False |  | distribution_warning | -1.0 | -2.73 | 1 | 1 | 10.31 | 3.48 | -35.13 |  | fail_low_response_condition |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -5.36 | -1.47 | -14.63 | -4.14 | 13.73 | 13.73 | False |  | distribution_warning | -0.11 | -0.03 | 2 | 2 | -1.31 | -3.23 | -22.34 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | -12.58 | -2.96 | 1.93 | 60.75 | 10.26 | 66.59 | False |  | strong_accumulation | 2.61 | 2.18 | 3 | 2 | -1.14 | -1.81 | -14.43 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 0.62 | -2.68 | 6.0 | 16.37 | 17.2 | 20.22 | False |  | mild_accumulation | -0.22 | 0.07 | 1 | 2 | 4.31 | 0.8 | -25.34 | 22 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 5.18 | 17.47 | 18.4 | 173.29 | 52.29 | 181.65 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.05 | -0.95 | 2 | 1 | 13.05 | 9.03 | -7.5 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -3.58 | 12.17 | 37.21 | 116.05 | 49.89 | 114.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | -0.2 | 2 | 1 | 7.42 | 7.18 | -5.08 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -2.58 | 7.0 | 3.22 | 12.83 | 22.29 | 22.29 | False |  | distribution_warning | -0.1 | -1.62 | 2 | 1 | 4.51 | 2.85 | -7.89 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | -4.87 | -7.73 | -7.33 | 7.5 | 10.26 | 30.94 | False |  | distribution_warning | -1.32 | -0.83 | 0 | 1 | -2.93 | -5.12 | -25.86 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -9.21 | -14.24 | -14.11 | -9.64 | 2.88 | 2.88 | False |  | distribution_warning | -2.48 | -3.79 | 1 | 0 | -7.1 | -8.49 | -37.76 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 0.58 | 21.36 | 59.57 | 120.47 | 60.56 | 160.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.91 | 2 | 2 | 14.87 | 11.44 | -6.51 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -7.99 | -15.72 | 11.56 | 48.46 | 20.81 | 53.78 | False |  | distribution_warning | -4.06 | -0.62 | 1 | 2 | -13.67 | -10.38 | -27.03 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -2.84 | -4.04 | 4.19 | 16.63 | 4.39 | 16.38 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.71 | -2.51 | -14.4 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -4.24 | 1.12 | -28.66 | -16.82 | 12.81 | 12.81 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 1.11 | -2.06 | -38.08 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | -0.26 | 0.78 | 4.28 | 3.17 | 5.69 | 8.94 | False |  | distribution_warning | -0.17 | -0.68 | 1 | 2 | 1.06 | 0.84 | -4.65 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | -5.79 | 16.36 | -11.65 | 42.96 | 31.71 | 43.32 | False |  | distribution_warning | -0.39 | -0.79 | 1 | 2 | 0.36 | 1.14 | -25.72 | 16 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -6.09 | -9.51 | -9.79 | 13.75 | 5.74 | 26.33 | False |  | distribution_warning | -0.49 | -0.13 | 0 | 0 | -5.22 | -6.54 | -32.02 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -7.91 | 21.55 | 7.44 | 169.81 | 52.97 | 191.6 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.63 | 11.23 | 3 | 2 | 9.1 | 5.35 | -13.22 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | -18.1 | 3.99 | 5.01 | 74.62 | 27.6 | 79.35 | True | 近120日漲幅>70% | mild_accumulation | 8.09 | 6.27 | 2 | 1 | 2.19 | 0.51 | -19.25 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | 2.19 | 4.09 | -9.24 | 53.42 | 30.23 | 75.27 | False |  | strong_accumulation | 0.42 | 1.23 | 2 | 2 | 7.18 | 3.32 | -16.67 | 23 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | -2.85 | -0.83 | -2.05 | 57.44 | 18.91 | 65.51 | False |  | strong_accumulation | 0.53 | 1.49 | 2 | 3 | 0.08 | -1.37 | -14.64 | 18 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -5.84 | -1.08 | -42.76 | -17.47 | 27.24 | 27.24 | False |  | mild_accumulation | 0.28 | 0.88 | 1 | 1 | 2.13 | -3.48 | -45.13 | 22 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -2.79 | -2.01 | -8.11 | 5.41 | 3.4 | 6.56 | False |  | distribution_warning | -0.06 | -0.16 | 2 | 2 | -1.35 | -1.98 | -12.09 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | -6.3 | -4.12 | -21.44 | 29.39 | 19.04 | 31.68 | False |  | mild_accumulation | 0.44 | 0.48 | 1 | 2 | 0.35 | -4.57 | -33.09 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | 0.0 | 1.55 | 3.37 | 2.0 | 6.98 | 8.24 | False |  | strong_accumulation | 0.22 | 0.13 | 2 | 2 | 2.11 | 1.05 | -19.01 | 19 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 8.03 | 13.41 | 19.84 | 4.59 | 22.31 | 22.31 | False |  | mild_accumulation | 0.2 | 0.01 | 3 | 1 | 9.77 | 8.58 | -1.33 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | -0.71 | -2.09 | 2.94 | -14.51 | 4.63 | 7.85 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.16 | -0.15 | -13.03 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 4.09 | 7.45 | 15.0 | 31.07 | 17.23 | 43.32 | False |  | strong_accumulation | 1.13 | 1.16 | 3 | 3 | 7.33 | 6.42 | -0.62 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | B_可觀察 | 93.8248443457034 | 60.82046311316634 | -1.77 | -0.26 | -6.82 | -44.36 | 9.87 | 9.87 | False |  | mild_accumulation | 0.05 | -0.05 | 2 | 2 | 1.74 | 0.39 | -24.22 | 18 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -1.02 | 1.49 | -6.19 | -5.54 | 7.74 | 7.74 | False |  | mild_accumulation | 0.09 | -0.05 | 2 | 2 | 2.65 | 0.77 | -14.54 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | 0.49 | 0.99 | 3.13 | -5.99 | 3.98 | 3.98 | False |  | strong_accumulation | 1.0 | 1.03 | 3 | 2 | -0.87 | -1.52 | -13.56 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround |  | 56.21501385482998 | 35.673950917357274 | 11.15 | 16.48 | 23.47 | 32.08 | 33.76 | 43.05 | False |  | strong_accumulation | 0.48 | 0.69 | 3 | 2 | 10.95 | 10.51 | -1.35 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -7.88 | -16.72 | 5.67 | 6.34 | 18.91 | 47.51 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 1 | -15.82 | -10.84 | -43.04 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 1.03 | 3.16 | -11.91 | -10.71 | 8.29 | 8.29 | False |  | mild_accumulation | 0.18 | -1.99 | 2 | 1 | 1.86 | 1.3 | -13.47 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -7.65 | 5.26 | 2.89 | 33.06 | 20.98 | 35.16 | False |  | strong_accumulation | 2.01 | 3.61 | 2 | 2 | 2.84 | 0.05 | -13.51 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -5.08 | -11.96 | 2.97 | 15.71 | 2.53 | 23.35 | False |  | mild_accumulation | 0.21 | -0.02 | 2 | 1 | -4.78 | -5.6 | -25.46 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | -9.73 | 17.88 | 3.3 | 70.99 | 55.59 | 89.77 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.27 | 5.3 | 2 | 2 | 7.07 | 3.77 | -12.26 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -0.96 | 0.0 | -23.42 | 90.39 | 41.68 | 101.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | -0.08 | 2 | 1 | 6.76 | 0.27 | -32.68 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | -6.72 | 22.34 | 15.7 | 70.57 | 48.14 | 79.28 | True | 近120日漲幅>70% | strong_accumulation | 3.13 | 1.64 | 3 | 2 | 9.98 | 7.66 | -10.09 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | -5.71 | 0.33 | 26.54 | 64.59 | 25.68 | 66.97 | False |  | strong_accumulation | 4.1 | 4.24 | 3 | 2 | -3.03 | -1.93 | -20.6 | 18 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -4.91 | -3.51 | -18.84 | 27.22 | 16.64 | 38.88 | False |  | distribution_warning | -0.9 | -1.45 | 1 | 1 | -0.21 | -2.98 | -23.37 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | -6.69 | -10.2 | -9.48 | 55.31 | 8.36 | 59.4 | False |  | strong_accumulation | 0.17 | 0.59 | 2 | 2 | -3.71 | -4.76 | -23.65 | 19 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -4.42 | -0.96 | -29.02 | 5.12 | 14.17 | 14.17 | False |  | distribution_warning | -0.8 | -1.02 | 1 | 1 | -1.09 | -1.84 | -31.73 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | -3.66 | -7.44 | -11.81 | 0.45 | 12.56 | 12.56 | False |  | distribution_warning | -0.7 | -2.0 | 1 | 1 | -0.7 | -3.58 | -31.08 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | -1.92 | 19.58 | -1.62 | 38.71 | 48.47 | 48.47 | False |  | mild_accumulation | 0.14 | -0.16 | 1 | 2 | 15.62 | 9.11 | -18.81 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -4.26 | 4.47 | 7.35 | 25.73 | 17.74 | 34.1 | False |  | mild_accumulation | 2.91 | 2.62 | 3 | 1 | 3.32 | 2.01 | -8.75 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -7.74 | 10.24 | -22.44 | 63.27 | 33.02 | 65.44 | False |  | distribution_warning | -1.64 | -2.03 | 2 | 0 | 3.47 | -0.45 | -28.11 | 13 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 8.64 | -4.17 | -21.78 | 27.23 | 17.33 | 31.02 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 5.85 | 1.64 | -37.07 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | -8.44 | -27.91 | 2.84 | 75.85 | 38.57 | 95.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.63 | -6.3 | 0 | 0 | -1.84 | -7.85 | -46.02 |  | fail_already_priced_in |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -1.71 | 0.29 | -17.51 | 92.83 | 50.88 | 103.79 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.23 | -7.0 | 0 | 1 | 11.24 | -1.47 | -52.88 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 204.3244857198993 | 247.3095962162866 | -0.59 | 12.0 | -32.8 | 55.56 | 25.37 | 68.0 | False |  | distribution_warning | -1.8 | -0.52 | 1 | 1 | 3.96 | 2.45 | -36.84 | 16 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 13.06 | 10.76 | -4.15 | 186.47 | 75.37 | 190.84 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.71 | -0.12 | 1 | 1 | 21.34 | 11.21 | -24.93 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 7.36 | 30.36 | 26.44 | 187.37 | 61.88 | 221.47 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 1 | 0 | 19.92 | 17.39 | -0.87 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | -8.63 | 3.75 | 24.57 | 44.0 | 29.5 | 46.94 | False |  | strong_accumulation | 5.6 | 5.59 | 3 | 3 | -2.08 | 0.04 | -12.62 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | -0.36 | 2.95 | 9.41 | 2.95 | 13.41 | 17.23 | False |  | distribution_warning | -0.13 | 0.0 | 0 | 0 | 0.87 | 1.02 | -1.76 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | -6.84 | -3.54 | -31.01 | 4.81 | 21.25 | 21.25 | False |  | distribution_warning | -0.49 | -0.42 | 1 | 2 | 0.62 | -3.17 | -35.12 | 13 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 1.62 | 28.54 | 22.66 | 146.93 | 77.32 | 163.08 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 1.16 | 2 | 1 | 22.37 | 16.3 | -6.01 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 4.93 | 16.67 | 14.97 | 83.72 | 67.58 | 133.33 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.62 | 0.17 | 1 | 2 | 17.41 | 11.21 | -9.64 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | -8.05 | 3.33 | -7.07 | 2.12 | 15.73 | 15.73 | False |  | distribution_warning | -1.29 | -2.53 | 1 | 0 | 3.09 | 0.81 | -20.66 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -6.11 | -1.05 | -25.55 | 27.45 | 12.07 | 38.98 | False |  | distribution_warning | -0.49 | -0.05 | 1 | 2 | -2.14 | -4.3 | -40.7 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | -4.66 | -1.68 | -26.97 | -31.25 | 28.09 | 28.09 | False |  | strong_accumulation | 0.58 | 0.91 | 2 | 2 | 2.89 | -2.51 | -39.52 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 20.82 | 50.94 | 60.0 | 94.44 | 87.29 | 100.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.26 | -1.51 | 3 | 2 | 31.75 | 27.53 | -0.36 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 181.7841084291265 | -13.777157023400417 | -10.5 | 6.84 | -12.79 | 20.19 | 42.59 | 51.21 | False |  | mild_accumulation | 0.41 | -3.57 | 2 | 1 | 4.72 | -0.05 | -23.39 | 20 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | 2.04 | -1.53 | 6.38 | 36.78 | 33.53 | 51.01 | False |  | mild_accumulation | 1.5 | 0.64 | 3 | 1 | 2.82 | 4.01 | -11.94 | 17 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | -15.38 | -13.99 | -13.99 | 54.81 | 2.45 | 55.04 | False |  | strong_accumulation | 0.29 | 0.49 | 2 | 2 | -10.03 | -8.94 | -19.92 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | 0.49 | 2.48 | -16.53 | -8.0 | 20.91 | 20.91 | False |  | strong_accumulation | 0.45 | 1.02 | 3 | 3 | 5.69 | 2.55 | -18.18 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | -6.81 | -10.61 | -35.96 | -24.48 | 22.35 | 22.35 | False |  | distribution_warning | -0.17 | -0.41 | 1 | 2 | -1.08 | -7.32 | -44.27 | 12 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | -4.9 | 6.61 | 28.75 | 5.01 | 32.32 | 32.32 | False |  | strong_accumulation | 0.31 | 0.28 | 3 | 3 | 2.45 | 3.23 | -6.6 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | -7.14 | 4.52 | -18.59 | 71.9 | 28.4 | 95.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.33 | 0.03 | 3 | 1 | 1.19 | -1.25 | -23.81 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -2.09 | -0.58 | -6.7 | -16.4 | 6.19 | 6.19 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.55 | -1.38 | -23.13 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -4.8 | -1.65 | -15.17 | 23.04 | 21.25 | 29.15 | False |  | distribution_warning | -1.34 | -2.13 | 1 | 0 | 0.55 | -4.11 | -38.07 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -1.51 | 7.77 | -13.68 | 5.17 | 22.0 | 22.0 | False |  | mild_accumulation | 0.6 | 0.0 | 3 | 1 | 4.13 | 2.65 | -21.79 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -2.17 | -4.06 | -3.12 | 73.6 | 13.62 | 86.65 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.4 | -2.14 | 1 | 1 | -1.49 | -3.07 | -22.12 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -2.73 | -6.25 | -15.68 | -22.55 | 8.37 | 8.37 | False |  | distribution_warning | -0.36 | -0.17 | 1 | 0 | -0.31 | -2.89 | -25.39 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -2.66 | -6.03 | -5.18 | -29.83 | 5.91 | 5.91 | False |  | strong_accumulation | 0.04 | 0.03 | 3 | 3 | -1.7 | -1.76 | -12.75 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 2.91 | -0.28 | -25.86 | 48.58 | 31.11 | 54.25 | False |  | distribution_warning | -0.05 | -0.03 | 1 | 1 | 5.73 | 0.68 | -32.57 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 98.74936839745938 | 71.28591290526819 | -5.17 | 22.58 | -1.66 | 47.78 | 36.06 | 56.01 | False |  | strong_accumulation | 6.22 | 7.02 | 2 | 3 | 4.93 | 3.49 | -15.69 | 21 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 3.3 | 16.36 | -25.65 | -9.01 | 49.05 | 49.05 | False |  | distribution_warning | -1.94 | 0.0 | 1 | 0 | 13.82 | 8.08 | -32.69 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -10.53 | -11.81 | -39.51 | -8.28 | 23.75 | 23.75 | False |  | distribution_warning | -4.2 | -2.48 | 1 | 1 | -2.4 | -8.01 | -47.23 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.0 | -4.05 | 23.05 | 36.33 | 21.47 | 45.77 | False |  | distribution_warning | -0.56 | 0.0 | 0 | 0 | -0.45 | -0.18 | -6.19 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -4.32 | -12.91 | -8.38 | -0.13 | 1.84 | 3.6 | False |  | distribution_warning | -1.25 | -1.76 | 2 | 2 | -8.8 | -7.33 | -18.32 | 13 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 3.22 | -2.73 | -10.97 | -3.17 | 4.4 | 4.4 | False |  | distribution_warning | -0.45 | -0.63 | 1 | 1 | -0.28 | -0.6 | -23.6 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 2.06 | -3.04 | 5.69 | -11.51 | 7.47 | 9.05 | False |  | mild_accumulation | 0.03 | -0.02 | 1 | 0 | -0.45 | 0.38 | -6.69 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | 3.19 | 1.51 | 8.45 | 9.03 | 11.28 | 11.28 | False |  | distribution_warning | -0.59 | -0.97 | 0 | 0 | 3.0 | 2.47 | -7.54 | 18 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | -0.16 | -4.35 | 8.85 | 19.65 | 8.47 | 20.35 | False |  | strong_accumulation | 0.54 | 0.12 | 2 | 2 | 0.43 | 0.18 | -5.96 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 19.82 | 55.22 | 29.03 | 69.93 | 61.49 | 75.08 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.92 | 1.08 | 2 | 1 | 34.44 | 28.27 | -2.26 |  | fail_low_response_condition |