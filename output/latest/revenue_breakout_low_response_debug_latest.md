# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-10 19:37:11 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 721791 |
| tdcc_rows | 1966 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 373 |
| tdcc_mild_accumulation_count | 730 |
| tdcc_distribution_warning_count | 658 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 93 |
| already_priced_in_excluded | 33 |
| overheat_pass | 60 |
| score_pass | 60 |
| theme_priority_pass | 54 |
| final_rows | 54 |

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
| fail_low_response_condition | 244 |
| fail_already_priced_in | 33 |
| fail_defensive_or_traditional_excluded | 4 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1229 | 聯華 | 食品工業 | defensive_or_traditional |  | 114.98296171902771 | -4.952739530778521 | -0.83 | 1.09 | -0.36 | -6.7 | 5.16 | 9.87 | False |  | strong_accumulation | 0.18 | 0.12 | 2 | 2 | 0.0 | 0.19 | -5.54 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 102.03987961747174 | 127.0977623123372 | 2.79 | 10.5 | 1.84 | -11.95 | 17.68 | 17.68 | False |  | distribution_warning | -1.06 | -0.62 | 0 | 1 | 1.19 | 2.27 | -11.6 | 12 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 1.16 | 0.58 | -9.22 | -24.24 | 4.61 | 4.61 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | 0.51 | 0.29 | -15.94 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -0.98 | -2.88 | -13.3 | 17.99 | 6.43 | 21.83 | False |  | distribution_warning | -0.41 | 0.0 | 1 | 0 | -1.66 | -2.02 | -16.53 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -2.14 | -2.55 | 3.15 | -1.29 | 8.02 | 8.02 | False |  | mild_accumulation | 0.93 | 0.29 | 2 | 1 | -2.57 | -1.07 | -7.29 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.86 | -2.22 | -5.63 | -7.61 | 3.23 | 3.83 | False |  | mild_accumulation | 0.05 | 0.0 | 3 | 0 | -0.82 | -1.14 | -12.66 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 1.65 | -1.2 | -10.83 | 5.56 | 5.11 | 12.27 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | 0.32 | -0.31 | -21.34 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 1.05 | -6.15 | -31.44 | -34.68 | 5.07 | 5.07 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.92 | -2.04 | -31.28 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -5.09 | -11.22 | 0.77 | 29.21 | 4.82 | 34.54 | False |  | mild_accumulation | -0.02 | 0.05 | 2 | 1 | -7.94 | -7.07 | -19.2 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -1.01 | -4.52 | -7.02 | -3.46 | 9.07 | 9.07 | False |  | distribution_warning | -0.02 | -0.37 | 1 | 2 | -1.23 | -1.09 | -9.39 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 5.53 | 15.17 | 69.71 | 97.21 | 70.94 | 98.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.74 | 1.27 | 2 | 2 | 4.01 | 7.28 | -6.37 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -0.3 | -1.2 | -8.08 | 71.16 | 32.53 | 82.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.16 | -0.42 | 1 | 2 | -1.83 | -0.58 | -34.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -3.91 | 3.93 | 7.84 | 9.9 | 16.22 | 22.64 | False |  | strong_accumulation | 0.35 | 0.49 | 2 | 2 | -1.04 | -0.02 | -8.99 | 19 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -0.89 | -3.06 | -2.2 | 0.45 | 3.74 | 11.0 | False |  | distribution_warning | -0.05 | -0.09 | 2 | 1 | -2.22 | -1.46 | -9.02 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -1.98 | -2.36 | -13.59 | 7.36 | 10.71 | 15.89 | False |  | mild_accumulation | 0.96 | 0.0 | 3 | 0 | -2.95 | -2.01 | -15.93 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -6.32 | 2.98 | 89.47 | 248.55 | 94.44 | 300.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -1.68 | 2 | 0 | -8.3 | -2.0 | -16.47 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -5.43 | -13.86 | -26.06 |  | 0.77 |  | False |  | distribution_warning | -0.12 | -0.05 | 0 | 1 | -9.23 | -8.27 | -27.09 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 2.01 | 0.0 | -5.22 | 14.41 | 10.92 | 16.51 | False |  | strong_accumulation | 0.82 | 0.74 | 2 | 2 | 3.78 | 1.26 | -32.98 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.27 | 4.51 | 7.1 | 22.31 | 11.46 | 25.36 | False |  | distribution_warning | -0.62 | -2.1 | 0 | 0 | -2.63 | -1.48 | -14.83 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 3.32 | -2.66 | -1.89 | 1.97 | 5.96 | 20.54 | False |  | distribution_warning | -0.02 | -0.04 | 1 | 0 | -0.73 | -0.63 | -11.14 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -0.24 | -6.53 | 1.08 | 125.94 | 28.61 | 146.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -1.5 | 1 | 0 | -2.18 | -1.5 | -27.28 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 27.91 | 26.02 | 26.85 | 161.9 | 49.81 | 162.8 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.53 | -1.44 | 1 | 1 | 28.37 | 23.57 | -9.73 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | 5.23 | -1.83 | -5.29 | 56.31 | 26.77 | 73.87 | False |  | distribution_warning | -0.58 | -2.3 | 1 | 0 | 1.04 | 0.55 | -35.21 | 14 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 1.41 | -4.2 | -6.69 | 25.5 | 10.82 | 33.87 | False |  | distribution_warning | -0.39 | -0.33 | 0 | 0 | 0.21 | -0.25 | -8.89 | 15 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 11.94 | -13.6 | -39.79 | 120.0 | 25.3 | 135.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.13 | -3.89 | 0 | 0 | 1.23 | -0.85 | -53.11 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 4.7 | -10.26 | -26.43 | -13.73 | 33.44 | 33.44 | False |  | distribution_warning | -2.88 | -2.48 | 1 | 1 | -1.49 | -1.71 | -36.2 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 6.21 | 1.41 | -8.88 | 82.79 | 53.42 | 114.2 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.99 | -1.5 | 2 | 2 | 0.2 | 1.46 | -23.13 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 71.68985948774075 | 62.35657344241515 | -5.98 | -13.44 | -22.02 | 16.62 | 6.79 | 31.44 | False |  | mild_accumulation | 0.11 | -0.1 | 2 | 1 | -6.55 | -6.72 | -30.44 | 16 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 2.78 | -2.95 | -4.52 | 11.14 | 10.59 | 18.72 | False |  | distribution_warning | -0.37 | -0.53 | 0 | 0 | 1.35 | 0.6 | -9.66 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.28 | 2.15 | -4.42 | -10.65 | 6.74 | 6.74 | False |  | mild_accumulation | 0.11 | -0.05 | 2 | 1 | 0.32 | -0.35 | -13.37 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 5.61 | 36.13 | 33.81 | 134.33 | 89.92 | 149.73 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.6 | 6.42 | 3 | 2 | 10.8 | 10.51 | -5.04 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -3.69 | -9.01 | -6.01 | 45.92 | 10.21 | 56.7 | False |  | strong_accumulation | 0.06 | 0.03 | 2 | 2 | -4.8 | -4.09 | -14.83 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 1.85 | 5.55 | 25.03 | 75.04 | 55.75 | 81.47 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.45 | 1.39 | 3 | 3 | 2.46 | 4.75 | -3.98 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 8.19 | -5.22 | -6.24 | 34.15 | 26.01 | 48.81 | False |  | mild_accumulation | 0.16 | -0.21 | 2 | 2 | 2.93 | 3.36 | -12.45 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 4.99 | -3.31 | -10.85 | 5.2 | 18.74 | 18.74 | False |  | distribution_warning | -1.0 | -0.73 | 0 | 0 | 2.2 | 0.68 | -30.88 | 13 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 77.38084589596791 | 70.28827013710922 | -5.0 | 3.47 | -22.3 | 13.34 | 48.23 | 48.23 | False |  | mild_accumulation | -0.02 | 0.87 | 1 | 3 | -1.85 | -1.39 | -25.36 | 17 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -0.88 | -5.08 | -9.66 | -6.66 | 14.07 | 14.07 | False |  | distribution_warning | -1.53 | -1.01 | 0 | 1 | -1.68 | -1.73 | -17.73 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 59.67101651519066 | 49.96169077295545 | 0.29 | -10.67 | 1.01 | 50.21 | 12.66 | 58.69 | False |  | distribution_warning | -1.4 | -0.73 | 1 | 1 | -0.73 | -0.38 | -12.56 | 11 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 0.3 | 3.38 | -7.31 | 17.89 | 20.43 | 20.86 | False |  | strong_accumulation | 0.21 | 0.12 | 2 | 2 | 0.74 | 0.84 | -14.5 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 1.61 | -5.54 | 4.98 | 88.93 | 36.77 | 107.13 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.47 | 0 | 0 | -4.9 | -1.73 | -16.92 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -2.23 | -5.59 | 37.29 | 97.6 | 45.47 | 110.21 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.49 | 0 | 1 | -2.56 | -0.43 | -9.35 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -2.61 | -9.26 | -1.81 | 7.17 | 13.9 | 13.9 | False |  | mild_accumulation | 0.28 | 0.7 | 2 | 1 | -4.73 | -3.34 | -12.19 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | 2.42 | -6.19 | -14.86 | 12.41 | 8.72 | 29.11 | False |  | mild_accumulation | 0.1 | -1.29 | 2 | 1 | -1.58 | -2.09 | -26.9 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -0.55 | -14.6 | -23.58 | -26.5 | 1.13 | 1.13 | False |  | distribution_warning | -2.62 | -2.47 | 0 | 0 | -4.42 | -6.07 | -41.46 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 7.85 | 0.19 | 21.18 | 127.37 | 59.94 | 159.45 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | -2.37 | 2 | 2 | -0.24 | 2.38 | -9.49 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | 2.61 | -11.08 | -5.57 | 27.96 | 3.04 | 43.46 | False |  | strong_accumulation | 0.71 | 1.49 | 2 | 3 | -1.82 | -4.37 | -29.49 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 2.23 | -2.31 | -1.79 | 0.92 | 2.23 | 9.13 | False |  | mild_accumulation | 0.07 | 0.04 | 1 | 1 | -0.34 | -0.75 | -13.93 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -10.2 | 5.04 | -10.41 | -7.04 | 23.75 | 23.75 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 4.02 | 2.35 | -15.74 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | -18.91 | -19.95 | -20.76 | -24.21 | 0.0 | 0.0 | False |  | distribution_warning | -2.21 | -0.56 | 1 | 1 | -17.23 | -15.82 | -23.47 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | -1.22 | -6.46 | -9.6 | 10.78 | 30.79 | 35.49 | False |  | distribution_warning | -0.62 | -1.36 | 1 | 1 | -3.43 | -2.25 | -14.26 | 15 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 9.38 | 1.64 | -11.33 | 24.1 | 14.44 | 28.22 | False |  | distribution_warning | -0.04 | -0.05 | 2 | 2 | 6.74 | 4.76 | -26.43 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -12.84 | -1.28 | 7.8 | 160.08 | 63.98 | 194.52 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.83 | 2.95 | 1 | 1 | 0.3 | 1.63 | -13.62 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | -4.68 | -12.67 | 15.93 | 64.93 | 36.05 | 81.58 | True | 距120日低點反彈>80% | distribution_warning | -0.74 | -2.85 | 2 | 2 | -2.08 | -1.56 | -14.7 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | -3.36 | 4.93 | 1.95 | 42.15 | 33.72 | 49.54 | False |  | mild_accumulation | 1.04 | -0.92 | 3 | 1 | -1.0 | -0.66 | -14.43 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 54.39975818511566 | 39.61008944759205 | -2.86 | -3.25 | -0.42 | 40.66 | 18.41 | 46.91 | False |  | mild_accumulation | 0.32 | -1.79 | 1 | 0 | -2.06 | -2.28 | -15.0 |  | fail_low_response_condition |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -2.09 | -8.71 | -34.13 | -50.19 | 23.37 | 23.37 | False |  | mild_accumulation | 0.69 | 0.51 | 3 | 1 | -4.25 | -4.47 | -37.05 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.52 | -3.89 | -10.0 | 0.1 | 2.23 | 2.23 | False |  | mild_accumulation | -0.29 | 0.2 | 2 | 3 | -1.02 | -1.26 | -13.09 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | 0.14 | -6.93 | -25.35 | 0.82 | 18.24 | 18.24 | False |  | strong_accumulation | 0.19 | 0.01 | 2 | 2 | -2.08 | -2.46 | -33.54 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -1.11 | -3.26 | -13.59 | -7.48 | 3.49 | 3.49 | False |  | mild_accumulation | -0.2 | 0.12 | 1 | 2 | -1.93 | -1.52 | -21.65 | 17 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -2.01 | 6.93 | 5.02 | 2.81 | 14.01 | 21.07 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -1.1 | 0.27 | -6.69 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 2.94 | -0.85 | -6.04 | -8.62 | 3.09 | 7.69 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 0.09 | -0.22 | -13.15 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -4.42 | 0.22 | 3.22 | 28.81 | 10.85 | 37.98 | False |  | strong_accumulation | 1.25 | 1.5 | 3 | 3 | -2.58 | -1.34 | -5.1 | 21 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 1.96 | -1.39 | -16.81 | -40.31 | 10.3 | 10.3 | False |  | mild_accumulation | -0.6 | 0.27 | 0 | 2 | 0.99 | 0.77 | -17.25 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | -0.72 | -0.15 | -11.0 | -6.9 | 8.69 | 8.69 | False |  | mild_accumulation | -0.01 | 0.06 | 1 | 2 | -0.09 | -0.06 | -13.02 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -0.1 | -1.67 | -9.68 | -8.44 | 1.63 | 1.73 | False |  | mild_accumulation | -0.14 | 0.13 | 1 | 2 | -0.89 | -1.28 | -15.42 | 21 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 0.7 | 17.96 | 28.19 | 42.76 | 41.95 | 50.9 | False |  | mild_accumulation | 0.42 | -0.02 | 2 | 1 | 5.55 | 6.42 | -6.94 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 15.43 | 0.0 | 6.02 | 47.17 | 19.21 | 60.12 | False |  | distribution_warning | -0.02 | -0.01 | 1 | 0 | 7.18 | 2.79 | -38.17 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 1.52 | 3.09 | -9.09 | -23.37 | 10.5 | 10.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.76 | 1.7 | -10.31 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -10.24 | -15.3 | -12.91 | 16.01 | 10.96 | 21.53 | False |  | mild_accumulation | 1.21 | -0.89 | 3 | 1 | -9.8 | -8.06 | -20.68 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -1.22 | -5.08 | -8.65 | 17.39 | 3.85 | 23.35 | False |  | mild_accumulation | 0.13 | -0.31 | 1 | 1 | 0.21 | -1.15 | -25.46 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 12.64 | 12.43 | 38.98 | 75.77 | 93.79 | 112.24 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.08 | 1 | 1 | 12.68 | 13.35 | -2.19 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 11.9 | 5.77 | -7.95 | 80.92 | 51.31 | 115.69 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.98 | -0.63 | 0 | 1 | 8.16 | 7.96 | -28.1 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 4.85 | 8.13 | 45.99 | 64.76 | 71.71 | 77.89 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.28 | 0.56 | 1 | 2 | 7.15 | 8.95 | -3.76 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 73.91966377290892 | 26.75099850600647 | -3.21 | -13.97 | 2.18 | 32.91 | 9.33 | 39.97 | False |  | distribution_warning | -2.54 | -1.49 | 0 | 2 | -7.43 | -7.15 | -27.55 | 11 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -2.66 | -10.1 | -16.71 | 14.52 | 10.27 | 28.45 | False |  | distribution_warning | -0.58 | -0.48 | 0 | 0 | -4.28 | -4.33 | -26.96 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -4.76 | -13.48 | -13.83 | 25.71 | 1.82 | 33.49 | False |  | distribution_warning | -3.17 | -2.2 | 0 | 1 | -6.22 | -6.4 | -29.21 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | 1.05 | -10.47 | -12.1 | -18.95 | 6.94 | 6.94 | False |  | distribution_warning | -1.79 | -1.73 | 0 | 0 | -2.32 | -2.64 | -18.26 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 0.0 | -1.29 | -13.07 | -2.75 | 15.33 | 15.33 | False |  | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 0.65 | -0.18 | -29.38 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 3.18 | 1.62 | -7.88 | 40.9 | 53.82 | 53.82 | True | 距60日低點反彈>50% | mild_accumulation | 0.06 | -0.76 | 1 | 0 | 3.54 | 5.21 | -15.89 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -3.64 | -13.11 | -7.02 | 12.29 | 6.85 | 15.22 | False |  | distribution_warning | -0.53 | -1.28 | 0 | 1 | -6.82 | -5.25 | -15.87 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -1.91 | -15.32 | -27.71 | 34.2 | 22.09 | 51.85 | False |  | distribution_warning | -0.99 | -1.53 | 0 | 1 | -6.42 | -5.41 | -31.92 | 11 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 1.26 | 16.05 | -16.69 | -13.23 | 25.33 | 25.33 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 3.46 | 2.68 | -18.26 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 22.14 | 35.02 | 88.01 | 164.03 | 92.31 | 187.77 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.16 | 0.76 | 0 | 1 | 26.53 | 22.55 | -20.4 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | 5.23 | -2.29 | -37.82 | 82.69 | 50.0 | 89.37 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.23 | 0.11 | 1 | 1 | 1.03 | 0.17 | -53.15 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | -3.19 | -1.18 | -13.47 | 32.54 | 24.63 | 67.0 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 1 | -3.01 | -2.62 | -19.71 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 16.16 | 25.82 | 6.0 | 143.33 | 95.17 | 154.65 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.65 | -6.2 | 0 | 0 | 10.31 | 9.3 | -12.67 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 26.34 | 15.85 | 37.51 | 200.24 | 74.68 | 241.11 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.14 | -1.57 | 2 | 0 | 11.93 | 15.15 | -6.69 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | -1.86 | -6.09 | 17.09 | 44.53 | 33.09 | 51.02 | False |  | distribution_warning | -0.81 | -1.08 | 1 | 1 | 0.49 | 0.48 | -10.19 | 13 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 2.55 | 0.36 | 4.07 | 4.85 | 6.04 | 18.07 | False |  | mild_accumulation | 0.14 | 0.01 | 2 | 1 | 0.7 | 0.84 | -1.06 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | -6.45 | -13.25 | -27.76 | -0.98 | 12.9 | 12.9 | False |  | distribution_warning | -1.8 | -2.54 | 0 | 0 | -7.26 | -7.29 | -32.11 | 11 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 7.33 | 12.36 | 26.52 | 151.52 | 96.06 | 190.89 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -2.6 | 1 | 0 | 7.31 | 10.55 | -4.08 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -5.6 | -0.76 | 4.7 | 88.13 | 58.48 | 120.68 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.4 | 1.95 | 2 | 2 | -7.43 | -4.4 | -19.91 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 0.68 | -6.14 | -9.03 | 1.61 | 18.13 | 18.13 | False |  | mild_accumulation | 0.29 | 0.02 | 2 | 1 | -0.26 | 0.17 | -12.45 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 2.06 | -6.56 | -31.63 | 33.92 | 11.54 | 36.08 | False |  | mild_accumulation | 0.61 | -0.25 | 2 | 1 | -0.12 | -0.73 | -31.9 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 0.0 | -7.37 | -33.2 | -29.34 | 24.45 | 24.45 | False |  | mild_accumulation | -0.09 | 0.16 | 1 | 2 | -3.21 | -3.52 | -37.82 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 3.12 | 24.92 | 52.97 | 46.77 | 93.65 | 106.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.45 | 2.36 | 1 | 3 | 4.13 | 8.45 | -5.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 0.12 | -3.22 | -6.03 | 28.73 | 54.18 | 63.51 | True | 距60日低點反彈>50% | mild_accumulation | 0.9 | -0.42 | 1 | 2 | 2.13 | 2.55 | -17.16 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 59.590900789853706 | 37.93424741228517 | -8.1 | -12.47 | -8.96 | 11.56 | 14.54 | 14.54 | False |  | mild_accumulation | -0.62 | 0.28 | 1 | 1 | -9.29 | -8.2 | -24.46 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 5.88 | -12.55 | -0.92 | 12.73 | 11.11 | 24.86 | False |  | distribution_warning | -2.68 | -2.84 | 0 | 0 | 2.1 | 0.65 | -17.24 | 16 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -1.8 | -4.66 | -16.07 | -18.51 | 14.72 | 14.72 | False |  | mild_accumulation | 0.15 | -0.68 | 2 | 0 | -3.18 | -2.4 | -18.51 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | 7.63 | 8.09 | -25.73 | -30.6 | 41.9 | 41.9 | False |  | distribution_warning | -0.9 | -0.14 | 1 | 2 | 7.65 | 4.82 | -35.37 | 12 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 3.21 | 5.08 | 37.53 | 10.71 | 38.02 | 46.21 | False |  | strong_accumulation | 0.25 | 0.25 | 2 | 2 | 6.94 | 7.19 | -0.86 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 3.03 | 6.25 | 15.25 | 84.5 | 46.91 | 91.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.87 | 0.28 | 2 | 2 | 7.51 | 6.19 | -7.75 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -3.41 | -3.04 | -12.22 | -15.0 | 5.15 | 5.15 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -1.98 | -2.08 | -17.74 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 128.9172485640275 | 121.34662298357856 | -5.71 | -11.31 | -33.1 | -8.71 | 12.95 | 12.95 | False |  | mild_accumulation | -0.86 | 0.91 | 1 | 2 | -8.39 | -7.79 | -39.38 | 16 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -11.33 | -3.12 | 1.35 | -0.11 | 20.0 | 20.0 | False |  | mild_accumulation | 0.12 | 1.75 | 1 | 2 | -5.64 | -5.44 | -14.69 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 128.94577120992216 | 58.42418198682172 | -2.07 | -6.7 | -4.34 | 57.57 | 8.35 | 78.01 | False |  | distribution_warning | -0.42 | -0.86 | 1 | 0 | -5.05 | -4.67 | -20.75 | 16 | selected |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 0.0 | -6.83 | -21.1 | -24.79 | 3.8 | 3.8 | False |  | mild_accumulation | 0.08 | 0.3 | 2 | 1 | -3.29 | -3.65 | -28.53 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -8.86 | -16.76 | -20.62 | -34.55 | 10.26 | 10.26 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -9.49 | -8.59 | -25.16 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | -1.03 | 11.48 | -9.87 | 17.1 | 42.04 | 42.04 | False |  | mild_accumulation | -0.44 | 0.22 | 2 | 2 | 2.42 | 2.43 | -16.17 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 1.47 | -1.43 | 0.55 | 8.64 | 41.43 | 41.43 | False |  | distribution_warning | -6.9 | -5.13 | 1 | 1 | 1.3 | 1.89 | -5.15 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 0.29 | 14.19 | -4.16 | -4.68 | 64.76 | 64.76 | True | 距60日低點反彈>50% | distribution_warning | -0.95 | -2.3 | 1 | 1 | 4.77 | 5.0 | -11.05 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | 2.81 | -10.25 | -20.97 | -7.16 | 24.15 | 24.15 | False |  | distribution_warning | -0.86 | -0.05 | 1 | 2 | -1.39 | -2.77 | -47.06 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -2.41 | -3.69 | -0.27 | 29.89 | 5.8 | 33.21 | False |  | mild_accumulation | 0.78 | 0.0 | 3 | 0 | -3.34 | -2.98 | -8.75 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -5.33 | -12.33 | -15.56 | -7.06 | 0.14 | 0.14 | False |  | distribution_warning | -6.07 | -4.62 | 0 | 1 | -7.22 | -8.35 | -25.16 | 11 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | -1.72 | 0.97 | -17.72 | -13.99 | 2.12 | 2.12 | False |  | distribution_warning | -0.12 | -0.35 | 1 | 0 | -0.85 | -1.45 | -18.25 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 0.68 | 1.37 | -0.23 | -13.65 | 4.24 | 8.31 | False |  | distribution_warning | 0.0 | -0.02 | 1 | 0 | 0.24 | -0.03 | -7.32 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | B_可觀察 | 269.79263095650754 | 63.44502485811813 | -2.74 | -4.97 | -9.48 | -3.37 | 0.4 | 2.48 | False |  | mild_accumulation | 0.25 | -0.18 | 2 | 1 | -3.5 | -3.09 | -14.86 | 21 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | -3.33 | -1.14 | -1.46 | 10.93 | 6.84 | 13.62 | False |  | strong_accumulation | 0.17 | 0.37 | 2 | 2 | -1.85 | -1.8 | -6.88 |  | fail_low_response_condition |