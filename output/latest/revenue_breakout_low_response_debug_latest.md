# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-27 22:26:29 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 702233 |
| tdcc_rows | 1969 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 435 |
| tdcc_mild_accumulation_count | 756 |
| tdcc_distribution_warning_count | 592 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 89 |
| already_priced_in_excluded | 45 |
| overheat_pass | 44 |
| score_pass | 44 |
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
| fail_revenue_condition | 1630 |
| fail_low_response_condition | 248 |
| fail_already_priced_in | 45 |
| fail_defensive_or_traditional_excluded | 4 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 102.03987961747174 | 127.0977623123372 | 10.33 | 21.38 | 14.08 | -9.96 | 25.13 | 25.13 | False |  | mild_accumulation | 0.03 | 0.41 | 1 | 2 | 11.95 | 10.15 | -6.0 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 2.94 | 4.58 | -4.37 | -26.47 | 5.21 | 5.21 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 1.89 | 0.84 | -15.46 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.0 | 1.46 | 10.17 | 8.45 | 10.99 | 25.45 | False |  | distribution_warning | -0.47 | -1.3 | 1 | 0 | 1.79 | -0.0 | -14.75 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 0.43 | 10.28 | 2.61 | 1.72 | 11.32 | 11.32 | False |  | strong_accumulation | 1.61 | 1.98 | 3 | 3 | 3.24 | 2.46 | -4.45 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 1.7 | 0.0 | -6.02 | -5.53 | 5.28 | 5.9 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -0.06 | -0.29 | -10.92 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 2.05 | 5.51 | -9.78 | 16.36 | 5.96 | 17.45 | False |  | mild_accumulation | 0.04 | 0.09 | 1 | 3 | 0.42 | -0.61 | -25.89 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -0.67 | -2.93 | -29.05 | -40.4 | 6.43 | 6.43 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -1.44 | -3.37 | -32.88 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | 4.23 | 10.45 | 15.62 | 43.0 | 20.82 | 56.45 | False |  | distribution_warning | -0.85 | -0.35 | 1 | 1 | 0.22 | 1.84 | -8.36 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral | B_可觀察 | 187.03179652280383 | 2.596548930575971 | 4.1 | 11.37 | -4.35 | -3.21 | 13.39 | 13.39 | False |  | mild_accumulation | 0.95 | -0.73 | 2 | 1 | 2.94 | 2.98 | -12.58 | 17 | selected |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 12.71 | 51.44 | 72.91 | 102.07 | 76.94 | 99.71 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.57 | 3.71 | 3 | 3 | 14.24 | 12.26 | -9.42 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -2.65 | 31.35 | 65.5 | 67.51 | 64.68 | 83.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.5 | -1.66 | 1 | 2 | 2.32 | 1.44 | -33.8 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 4.2 | 10.79 | 22.91 | 16.16 | 23.33 | 28.16 | False |  | strong_accumulation | 0.23 | 0.35 | 2 | 2 | 6.61 | 6.25 | -4.89 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | 0.0 | 5.02 | 10.05 | 0.88 | 10.05 | 15.0 | False |  | mild_accumulation | 0.02 | -0.02 | 1 | 0 | 1.41 | 1.19 | -8.37 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | 5.18 | 10.0 | 9.09 | 20.0 | 17.86 | 26.92 | False |  | mild_accumulation | 0.3 | 0.28 | 2 | 1 | 4.91 | 4.26 | -16.72 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 2.98 | 100.84 | 182.56 | 327.42 | 189.99 | 355.24 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | -0.39 | 3 | 1 | 17.19 | 18.02 | -4.94 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -0.99 | 1.7 | -14.08 |  | 8.33 |  | False |  | distribution_warning | -0.36 | -0.83 | 0 | 0 | -2.34 | -1.36 | -27.78 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -2.03 | -8.37 | -13.31 | 6.17 | 5.24 | 19.31 | False |  | strong_accumulation | 0.25 | 0.75 | 2 | 2 | -6.17 | -7.31 | -36.41 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.66 | 8.17 | 12.27 | 27.85 | 15.19 | 29.58 | False |  | distribution_warning | -0.21 | -2.1 | 0 | 0 | 2.89 | 1.59 | -12.15 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | -1.71 | 0.8 | -3.81 | -8.41 | 7.67 | 22.48 | False |  | mild_accumulation | 0.02 | 0.02 | 2 | 1 | 1.36 | 0.48 | -9.71 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 1.73 | 31.54 | 18.92 | 132.8 | 46.67 | 156.56 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 0.0 | 2 | 2 | 2.26 | 2.26 | -24.27 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 10.92 | 6.9 | 25.85 | 101.71 | 45.43 | 112.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.58 | -1.96 | 1 | 1 | 3.02 | 1.22 | -30.95 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 3.22 | 23.94 | -0.31 | 69.13 | 26.38 | 82.39 | True | 距120日低點反彈>80% | distribution_warning | -0.61 | -0.46 | 1 | 2 | 1.12 | -0.18 | -35.41 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | 2.23 | 9.8 | -16.42 | 15.07 | 11.26 | 34.4 | False |  | mild_accumulation | 0.54 | 0.51 | 1 | 1 | -0.82 | 0.57 | -19.75 | 17 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -1.25 | 21.58 | -34.4 | 109.83 | 21.58 | 128.4 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.42 | -2.7 | 1 | 1 | -3.03 | -7.05 | -54.51 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 180.47957329305424 | 137.8339123232017 | 4.51 | 38.89 | -27.35 | 27.88 | 38.89 | 38.89 | True | 近20日漲幅>25% | distribution_warning | -1.43 | -1.66 | 1 | 1 | 2.45 | 1.15 | -33.59 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 5.38 | 56.96 | 0.81 | 63.16 | 58.97 | 121.96 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.11 | 1.16 | 2 | 2 | 8.28 | 7.33 | -20.34 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -0.71 | 8.01 | -13.81 | 40.74 | 13.59 | 51.45 | False |  | distribution_warning | -0.16 | -0.42 | 1 | 1 | -4.78 | -3.76 | -26.02 | 12 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | -0.23 | 0.81 | -5.14 | 26.53 | 8.09 | 26.72 | False |  | mild_accumulation | -0.19 | 0.08 | 1 | 1 | -3.87 | -2.21 | -11.7 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | -0.14 | -6.03 | 1.41 | -1.1 | 7.34 | 7.34 | False |  | distribution_warning | -1.0 | -0.05 | 0 | 1 | 1.06 | -0.19 | -12.88 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 30.79 | 79.78 | 20.0 | 182.69 | 93.55 | 187.08 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | -0.92 | 2 | 1 | 33.76 | 28.98 | -0.21 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 1.71 | 14.09 | -18.61 | 52.56 | 15.49 | 64.21 | False |  | strong_accumulation | 1.21 | 1.25 | 2 | 2 | -0.35 | 0.33 | -25.96 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 6.02 | 31.34 | 5.22 | 65.75 | 52.44 | 77.61 | True | 近20日漲幅>25%；距60日低點反彈>50% | strong_accumulation | 1.68 | 2.45 | 3 | 3 | 9.23 | 10.06 | -5.56 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -7.01 | 4.19 | -17.77 | 33.11 | 15.03 | 40.64 | False |  | distribution_warning | -0.72 | -0.96 | 0 | 1 | -4.81 | -4.37 | -25.47 | 17 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | -0.59 | 13.17 | -24.1 | -1.55 | 14.45 | 14.45 | False |  | mild_accumulation | 0.18 | 0.56 | 1 | 2 | -2.87 | -4.26 | -33.38 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 0.49 | 42.86 | -19.22 | 14.7 | 46.1 | 46.1 | True | 近20日漲幅>25% | distribution_warning | -1.31 | -2.95 | 0 | 1 | 5.73 | 3.83 | -34.81 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | 2.98 | 15.94 | -16.24 | -4.56 | 17.12 | 17.12 | False |  | mild_accumulation | -0.31 | 0.16 | 2 | 2 | 0.16 | 0.13 | -17.34 | 18 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 0.29 | 8.32 | -11.65 | 48.71 | 10.58 | 55.76 | False |  | mild_accumulation | 1.25 | 0.54 | 2 | 1 | -1.6 | -1.02 | -14.18 | 16 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 1.99 | 19.53 | -16.73 | 15.4 | 19.53 | 21.05 | False |  | strong_accumulation | 0.77 | 1.19 | 2 | 3 | 4.89 | 2.32 | -23.86 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -8.1 | 27.46 | 13.17 | 124.49 | 39.95 | 125.41 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -1.89 | 1 | 0 | -1.42 | -0.65 | -14.99 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 0.3 | 23.4 | 31.07 | 95.09 | 50.33 | 115.31 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.69 | 2 | 1 | 3.38 | 5.05 | -4.8 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -0.62 | 21.06 | -1.09 | 14.54 | 21.52 | 21.52 | False |  | mild_accumulation | 1.27 | 0.17 | 3 | 1 | 0.95 | 1.89 | -8.46 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 63.77094494612451 | 73.90317152093164 | 0.0 | 6.44 | -6.52 | -0.92 | 10.26 | 30.94 | False |  | distribution_warning | -0.98 | -1.71 | 1 | 1 | -3.28 | -3.25 | -25.86 | 12 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 0.35 | 1.23 | -19.83 | -15.96 | 6.1 | 6.1 | False |  | distribution_warning | -2.15 | -2.84 | 1 | 0 | -4.93 | -5.26 | -37.54 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 4.64 | 64.94 | 28.96 | 112.99 | 68.01 | 172.54 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.09 | 4.36 | 3 | 3 | 11.69 | 11.83 | -2.52 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -1.68 | -11.12 | 5.27 | 34.34 | 18.78 | 45.96 | False |  | distribution_warning | -2.98 | -1.29 | 2 | 2 | -11.79 | -7.95 | -28.26 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 2.38 | -0.36 | 0.18 | 0.72 | 3.7 | 11.11 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | 0.0 | 0.28 | -12.36 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 0.28 | 10.03 | -32.84 | -14.22 | 13.13 | 13.13 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.12 | -0.97 | -33.82 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | 0.77 | 2.34 | 3.97 | -0.25 | 4.8 | 9.78 | False |  | distribution_warning | -0.03 | 0.0 | 2 | 2 | 1.15 | 0.96 | -3.91 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | 4.75 | 10.58 | -18.02 | 30.13 | 37.96 | 42.93 | False |  | mild_accumulation | 0.25 | -0.27 | 1 | 2 | 1.65 | 2.94 | -22.19 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 2.98 | 4.07 | -17.65 | 23.27 | 8.89 | 30.09 | False |  | distribution_warning | -0.42 | -0.15 | 0 | 0 | -1.61 | -1.98 | -30.0 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 16.9 | 72.24 | 14.05 | 204.91 | 78.81 | 221.16 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.46 | 11.69 | 2 | 2 | 17.03 | 17.73 | 0.0 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 10.93 | 41.12 | 7.07 | 73.45 | 41.54 | 88.91 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.11 | -0.16 | 2 | 1 | 8.11 | 8.81 | -10.42 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 4.46 | 32.05 | -0.51 | 58.97 | 36.05 | 68.59 | True | 近20日漲幅>25% | strong_accumulation | 1.51 | 1.74 | 3 | 2 | 8.59 | 6.81 | -12.95 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 5.86 | 19.91 | 6.3 | 58.72 | 25.87 | 67.11 | False |  | mild_accumulation | -0.01 | 0.67 | 1 | 2 | 4.01 | 4.32 | -9.64 | 17 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth |  | 133.3640235641089 | 87.69992405929172 | 7.06 | 35.38 | -37.05 | -20.43 | 36.22 | 36.22 | True | 近20日漲幅>25% | distribution_warning | -0.35 | -0.44 | 1 | 1 | 5.99 | 3.51 | -38.03 |  | fail_already_priced_in |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.41 | -0.41 | -9.68 | 2.11 | 2.97 | 3.63 | False |  | mild_accumulation | 0.53 | -0.21 | 3 | 2 | -1.54 | -1.62 | -12.45 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | 3.23 | 20.57 | -25.58 | 27.57 | 22.88 | 28.64 | False |  | strong_accumulation | 0.56 | 1.09 | 2 | 2 | 1.15 | -0.73 | -30.94 | 18 | selected |
| 2501 | 國建 | 建材營造 | neutral |  | 119.67349677675224 | 35.30940543476948 | -0.43 | 2.23 | 0.88 | 0.44 | 6.51 | 6.51 | False |  | mild_accumulation | -0.01 | 0.12 | 1 | 2 | 0.99 | 0.24 | -19.37 |  | fail_low_response_condition |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 3.72 | 17.62 | 24.29 | 8.48 | 26.86 | 26.86 | False |  | mild_accumulation | 0.16 | 0.0 | 2 | 0 | 10.08 | 8.64 | -2.23 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 1.28 | 0.57 | 4.57 | -11.8 | 5.97 | 9.23 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.68 | 0.89 | -11.91 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -1.14 | 7.67 | 12.49 | 29.05 | 15.9 | 41.69 | False |  | strong_accumulation | 1.58 | 1.93 | 3 | 3 | 3.57 | 3.09 | -2.55 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | -0.9 | 8.58 | -15.63 | -47.84 | 8.89 | 8.89 | False |  | distribution_warning | -0.37 | -0.27 | 1 | 1 | 0.18 | -0.37 | -24.9 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 3.37 | 7.8 | -6.0 | -6.87 | 11.37 | 11.37 | False |  | mild_accumulation | -0.03 | 0.36 | 1 | 3 | 4.68 | 3.08 | -11.65 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | -0.98 | -2.42 | -1.46 | -9.01 | 2.85 | 2.96 | False |  | strong_accumulation | 0.44 | 0.39 | 2 | 2 | -1.7 | -1.78 | -14.41 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | -0.11 | 21.13 | 22.86 | 38.1 | 33.62 | 42.26 | False |  | strong_accumulation | 0.87 | 1.19 | 3 | 3 | 6.24 | 6.01 | -12.41 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 8.15 | -26.29 | 3.82 | 39.49 | 28.61 | 59.53 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 1 | 0.17 | -0.66 | -38.39 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | -2.04 | 0.52 | -8.79 | -22.42 | 6.08 | 6.08 | False |  | mild_accumulation | 0.08 | -2.09 | 1 | 0 | -0.54 | -1.09 | -15.23 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 7.66 | 28.79 | 11.49 | 36.44 | 30.25 | 42.65 | True | 近20日漲幅>25% | strong_accumulation | 2.81 | 3.85 | 3 | 3 | 6.94 | 6.64 | -6.89 |  | fail_already_priced_in |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 0.0 | -3.19 | 1.67 | 8.0 | 3.85 | 23.35 | False |  | strong_accumulation | 1.41 | 0.19 | 3 | 2 | -2.49 | -3.32 | -25.46 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 9.38 | 67.07 | 2.43 | 71.79 | 70.19 | 86.39 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.48 | 7.23 | 2 | 2 | 7.66 | 8.7 | -4.03 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -3.01 | 34.27 | -15.7 | 69.32 | 37.41 | 95.88 | True | 近20日漲幅>25%；距120日低點反彈>80% | distribution_warning | -0.24 | -0.57 | 1 | 0 | -0.13 | -1.66 | -34.71 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 11.89 | 58.29 | 23.7 | 79.57 | 65.76 | 84.02 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.41 | 2.28 | 2 | 3 | 14.73 | 16.29 | -2.91 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | -1.08 | 9.58 | 17.76 | 47.58 | 22.0 | 53.01 | False |  | mild_accumulation | 1.32 | 0.87 | 2 | 1 | -4.81 | -2.22 | -21.46 | 17 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -0.61 | 14.71 | -22.02 | 30.74 | 15.93 | 35.05 | False |  | mild_accumulation | -0.14 | 0.19 | 1 | 1 | -2.61 | -2.73 | -23.84 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | -0.33 | 7.36 | -9.05 | 50.67 | 8.0 | 52.19 | False |  | mild_accumulation | -0.82 | 0.47 | 2 | 2 | -3.86 | -3.73 | -23.91 | 18 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -6.08 | 5.18 | -33.56 | -16.63 | 7.22 | 7.22 | False |  | distribution_warning | -0.99 | -1.75 | 1 | 1 | -7.71 | -6.08 | -35.34 | 12 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 1.56 | 12.9 | -11.31 | -4.01 | 14.32 | 14.32 | False |  | mild_accumulation | 0.72 | -0.01 | 2 | 1 | 0.14 | -1.07 | -30.0 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | -0.93 | 40.64 | -5.31 | 34.55 | 47.09 | 47.09 | True | 近20日漲幅>25% | mild_accumulation | 0.15 | -0.71 | 1 | 1 | 7.99 | 6.15 | -19.57 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -1.2 | 13.36 | -7.09 | 21.22 | 16.33 | 25.43 | False |  | mild_accumulation | 2.89 | 1.28 | 2 | 1 | 0.06 | 0.64 | -8.7 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 54.59950544814572 | 34.30071340658413 | 0.36 | 31.46 | -25.27 | 50.87 | 33.49 | 66.03 | True | 近20日漲幅>25% | distribution_warning | -2.06 | -1.76 | 1 | 1 | -0.39 | 0.09 | -27.86 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 2.84 | 19.21 | -24.58 | -9.2 | 20.67 | 20.67 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 7.36 | 3.68 | -35.28 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 14.75 | 33.58 | 22.06 | 107.5 | 59.0 | 123.92 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.92 | -5.4 | 0 | 1 | 12.01 | 5.7 | -38.06 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -2.03 | 47.81 | -23.41 | 82.16 | 47.81 | 90.4 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.89 | -5.49 | 1 | 1 | 4.67 | -1.73 | -53.84 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | 8.63 | 30.82 | -23.96 | 58.01 | 36.19 | 82.5 | True | 近20日漲幅>25%；距120日低點反彈>80% | distribution_warning | -0.87 | -1.54 | 1 | 1 | 8.04 | 7.66 | -26.71 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | -2.62 | 67.87 | -11.67 | 129.72 | 70.77 | 144.08 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.9 | -4.11 | 1 | 0 | 10.7 | 7.14 | -26.9 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -3.16 | 40.38 | 9.54 | 164.27 | 56.76 | 211.3 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 5.37 | 6.19 | -11.84 |  | fail_already_priced_in |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | -0.28 | 12.19 | -6.02 | 34.96 | 29.14 | 46.53 | False |  | strong_accumulation | 3.25 | 3.26 | 2 | 2 | -3.29 | 0.05 | -12.86 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 1.08 | 1.44 | 10.59 | 4.06 | 14.63 | 18.49 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | 1.33 | 1.47 | -0.7 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.23071292224356 | 63.75000065335939 | 2.29 | 23.2 | -29.21 | 5.19 | 24.03 | 24.03 | False |  | mild_accumulation | -0.89 | 0.33 | 1 | 2 | 1.14 | 0.32 | -33.23 | 18 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 5.15 | 71.1 | 30.54 | 149.26 | 86.46 | 176.64 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.11 | 0.31 | 3 | 1 | 16.01 | 14.77 | -7.06 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 4.52 | 70.75 | 5.47 | 112.11 | 75.15 | 143.88 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.39 | 4.76 | 2 | 3 | 13.44 | 11.98 | -5.56 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 0.46 | 15.04 | -20.29 | 3.81 | 16.27 | 16.27 | False |  | mild_accumulation | 0.39 | -1.47 | 2 | 0 | 0.96 | 0.59 | -20.29 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -0.47 | 7.82 | -33.78 | 29.78 | 11.54 | 38.32 | False |  | mild_accumulation | -1.45 | 0.25 | 0 | 3 | -3.21 | -2.93 | -40.98 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 1.7 | 27.67 | -34.91 | -30.62 | 30.28 | 30.28 | True | 近20日漲幅>25% | mild_accumulation | 1.69 | -0.95 | 3 | 2 | 2.47 | 0.33 | -38.49 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 0.8 | 80.06 | 41.48 | 61.98 | 88.8 | 101.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.23 | -0.47 | 3 | 2 | 18.39 | 18.53 | -5.6 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 3.2 | 38.96 | -15.41 | 15.01 | 47.15 | 56.05 | True | 近20日漲幅>25% | mild_accumulation | 0.42 | -1.35 | 2 | 2 | 2.95 | 2.34 | -20.94 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -8.67 | 7.59 | -3.07 | 31.31 | 21.96 | 31.73 | False |  | strong_accumulation | 2.23 | 2.17 | 3 | 2 | -5.85 | -3.76 | -19.57 | 18 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 90.83318057075236 | 59.917707856465086 | -2.87 | -3.79 | -14.71 | 39.42 | 0.5 | 40.58 | False |  | distribution_warning | -0.91 | -0.69 | 1 | 1 | -12.1 | -9.65 | -22.22 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -0.48 | 17.31 | -13.81 | -20.77 | 20.33 | 20.33 | False |  | strong_accumulation | 0.49 | 0.21 | 3 | 2 | 2.67 | 1.44 | -16.94 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 6.39 | 28.16 | -32.85 | -23.36 | 30.17 | 30.17 | True | 近20日漲幅>25% | distribution_warning | -0.55 | -0.64 | 0 | 2 | 3.77 | 0.62 | -40.71 |  | fail_already_priced_in |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 1.72 | 11.04 | 30.0 | -3.09 | 34.6 | 34.6 | False |  | strong_accumulation | 0.29 | 0.28 | 3 | 3 | 3.18 | 3.86 | -4.99 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 3.61 | 31.0 | -9.45 | 78.1 | 33.02 | 88.21 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.57 | -1.74 | 2 | 0 | 2.18 | 3.5 | -11.86 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 2.91 | 8.16 | -8.46 | -11.67 | 9.28 | 9.28 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 2.49 | 1.5 | -20.9 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | 5.88 | 27.64 | -17.95 | 15.29 | 28.38 | 28.38 | True | 近20日漲幅>25% | distribution_warning | -1.02 | -1.25 | 1 | 0 | 3.42 | 1.93 | -34.42 |  | fail_already_priced_in |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth | A_優先追蹤 | 66.35391853670312 | 30.54000053488904 | 7.32 | 24.3 | -4.2 | 10.96 | 30.93 | 30.93 | False |  | mild_accumulation | 0.5 | -0.01 | 2 | 0 | 8.59 | 9.0 | -4.2 | 18 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 4.23 | 16.95 | -9.21 | 72.5 | 18.42 | 94.55 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.13 | 1 | 1 | 1.47 | 1.47 | -18.82 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 1.75 | 8.61 | -14.96 | -25.45 | 10.27 | 10.27 | False |  | distribution_warning | -0.08 | -0.21 | 2 | 0 | 1.2 | -0.51 | -24.08 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -1.78 | -1.19 | -8.11 | -29.92 | 5.75 | 5.75 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -2.59 | -2.54 | -14.3 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 7.63 | 38.55 | -27.08 | 34.63 | 41.11 | 41.11 | True | 近20日漲幅>25% | mild_accumulation | 0.07 | 0.11 | 1 | 2 | 9.56 | 7.28 | -27.43 |  | fail_already_priced_in |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 98.74936839745938 | 71.28591290526819 | 3.57 | 29.65 | -9.52 | 44.24 | 40.92 | 46.93 | True | 近20日漲幅>25% | mild_accumulation | -0.45 | 0.38 | 2 | 2 | 2.77 | 4.64 | -12.68 |  | fail_already_priced_in |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 9.58 | 61.03 | -19.29 | 13.58 | 63.33 | 63.33 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.31 | -1.02 | 2 | 0 | 17.16 | 14.3 | -26.24 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 105.41523454519049 | 68.91539282131619 | 6.94 | 30.0 | -33.7 | -6.22 | 32.34 | 32.34 | True | 近20日漲幅>25% | distribution_warning | -18.41 | -18.98 | 0 | 1 | 2.73 | 0.37 | -43.57 |  | fail_already_priced_in |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.53 | 2.7 | 19.06 | 36.07 | 20.57 | 40.59 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -0.1 | 0.34 | -5.69 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -0.13 | -2.02 | -16.93 | 0.26 | 1.71 | 3.47 | False |  | distribution_warning | -5.63 | -6.23 | 1 | 1 | -6.76 | -4.92 | -18.42 | 14 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | -0.47 | -2.45 | -15.05 | -2.74 | 3.91 | 3.91 | False |  | distribution_warning | -0.45 | -0.34 | 1 | 1 | 0.04 | -0.71 | -23.96 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | -0.67 | -2.42 | 1.61 | -12.45 | 4.24 | 8.31 | False |  | distribution_warning | -0.03 | -0.02 | 0 | 0 | -0.42 | -0.34 | -7.32 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | -6.43 | -3.44 | 2.71 | -0.39 | 4.13 | 4.13 | False |  | distribution_warning | 0.0 | -0.2 | 1 | 1 | -3.31 | -3.48 | -13.49 | 16 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 0.81 | -1.43 | 5.98 | 12.52 | 8.77 | 15.67 | False |  | mild_accumulation | 0.16 | 0.83 | 1 | 2 | 1.81 | 0.36 | -5.2 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | -8.46 | 46.46 | 21.74 | 52.08 | 47.83 | 53.05 | True | 近20日漲幅>25% | strong_accumulation | 2.88 | 4.45 | 2 | 2 | 12.6 | 10.86 | -10.53 |  | fail_low_response_condition |