# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-27 17:06:15 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 700273 |
| tdcc_rows | 1969 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 435 |
| tdcc_mild_accumulation_count | 756 |
| tdcc_distribution_warning_count | 592 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 83 |
| already_priced_in_excluded | 38 |
| overheat_pass | 45 |
| score_pass | 45 |
| theme_priority_pass | 41 |
| final_rows | 41 |

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
| fail_already_priced_in | 38 |
| fail_defensive_or_traditional_excluded | 4 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 102.03987961747174 | 127.0977623123372 | 9.43 | 20.83 | 12.08 | -9.73 | 23.54 | 23.54 | False |  | mild_accumulation | 0.03 | 0.41 | 1 | 2 | 11.62 | 9.76 | -2.93 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 3.5 | 3.29 | -2.56 | -26.38 | 6.81 | 6.81 | False |  | mild_accumulation | 0.2 | 0.0 | 2 | 0 | 3.68 | 2.46 | -14.17 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 1.47 | 0.49 | 11.53 | 9.06 | 11.41 | 24.85 | False |  | distribution_warning | -0.47 | -1.3 | 1 | 0 | 1.37 | -0.48 | -15.16 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 1.28 | 10.7 | 5.78 | 4.39 | 12.26 | 12.26 | False |  | strong_accumulation | 1.61 | 1.98 | 3 | 3 | 4.62 | 3.56 | -3.64 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 1.13 | -2.71 | -6.02 | -3.75 | 5.28 | 5.9 | False |  | mild_accumulation | 0.02 | -0.01 | 2 | 0 | -0.06 | -0.31 | -10.92 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 4.15 | 6.36 | -10.68 | 18.96 | 6.81 | 18.4 | False |  | mild_accumulation | 0.04 | 0.09 | 1 | 3 | 1.5 | 0.13 | -25.3 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 2.04 | -2.91 | -27.54 | -37.11 | 5.63 | 5.63 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -0.92 | -3.02 | -32.43 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | 1.03 | 10.94 | 8.89 | 51.55 | 20.0 | 55.39 | False |  | distribution_warning | -0.85 | -0.35 | 1 | 1 | 0.02 | 1.32 | -8.98 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | 2.86 | 7.9 | -7.04 | -3.65 | 10.46 | 10.46 | False |  | mild_accumulation | 0.95 | -0.73 | 2 | 1 | 0.81 | 0.59 | -14.84 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 13.98 | 54.58 | 90.26 | 120.18 | 92.23 | 120.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.57 | 3.71 | 3 | 3 | 26.57 | 23.33 | 0.0 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -1.19 | 25.38 | 68.71 | 71.5 | 69.4 | 83.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.5 | -1.66 | 1 | 2 | 3.58 | 1.57 | -33.8 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 6.91 | 13.38 | 22.34 | 21.92 | 23.83 | 26.92 | False |  | strong_accumulation | 0.23 | 0.35 | 2 | 2 | 6.13 | 5.82 | -5.82 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | 2.64 | 5.43 | 13.11 | 2.64 | 13.66 | 16.5 | False |  | mild_accumulation | 0.02 | -0.02 | 1 | 0 | 2.98 | 2.62 | -7.17 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 200.77620698853028 | 144.7342420065355 | 7.17 | 8.03 | 13.03 | 23.39 | 20.09 | 29.33 | False |  | mild_accumulation | 0.3 | 0.28 | 2 | 1 | 7.41 | 6.65 | -15.14 | 21 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 2.94 | 103.08 | 178.24 | 374.18 | 193.43 | 374.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | -0.39 | 3 | 1 | 22.17 | 21.41 | -3.81 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -0.33 | -0.33 | -12.61 |  | 7.97 |  | False |  | distribution_warning | -0.36 | -0.83 | 0 | 0 | -2.58 | -1.81 | -28.02 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -5.16 | -8.78 | -14.95 | 8.14 | 4.37 | 18.32 | False |  | strong_accumulation | 0.25 | 0.75 | 2 | 2 | -7.35 | -8.68 | -36.94 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | 1.75 | 9.4 | 16.15 | 31.69 | 18.52 | 33.33 | False |  | distribution_warning | -0.21 | -2.1 | 0 | 0 | 6.28 | 4.68 | -9.6 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 1.61 | -2.17 | -4.25 | -6.52 | 7.5 | 22.29 | False |  | mild_accumulation | 0.02 | 0.02 | 2 | 1 | 1.24 | 0.36 | -9.86 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 0.45 | 31.48 | 17.39 | 161.05 | 49.67 | 161.81 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 0.0 | 2 | 2 | 5.65 | 4.57 | -22.72 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 15.67 | 12.93 | 34.49 | 133.08 | 53.09 | 128.78 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.58 | -1.96 | 1 | 1 | 8.8 | 6.66 | -27.32 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | 3.54 | 17.95 | -3.01 | 74.43 | 26.77 | 82.95 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.61 | -0.46 | 1 | 2 | 2.43 | 0.12 | -35.21 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | 0.61 | 4.01 | -16.01 | 17.66 | 8.83 | 31.47 | False |  | mild_accumulation | 0.54 | 0.51 | 1 | 1 | -2.55 | -1.58 | -21.5 | 16 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -6.77 | 5.92 | -32.03 | 107.74 | 17.63 | 120.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.42 | -2.7 | 1 | 1 | -5.36 | -10.64 | -55.98 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 5.46 | 23.04 | -25.07 | 38.37 | 36.71 | 36.71 | False |  | distribution_warning | -1.43 | -1.66 | 1 | 1 | 2.31 | -0.33 | -34.64 | 18 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 8.04 | 39.62 | 8.04 | 72.04 | 55.13 | 116.59 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.11 | 1.16 | 2 | 2 | 7.78 | 5.44 | -22.27 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -3.29 | 7.59 | -18.13 | 43.21 | 11.68 | 48.91 | False |  | distribution_warning | -0.16 | -0.42 | 1 | 1 | -6.05 | -5.7 | -27.26 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | 0.93 | 1.99 | 0.69 | 26.23 | 8.47 | 27.34 | False |  | mild_accumulation | -0.19 | 0.08 | 1 | 1 | -3.5 | -2.07 | -11.39 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 1.57 | -5.45 | 1.72 | 2.3 | 6.44 | 6.44 | False |  | distribution_warning | -1.0 | -0.05 | 0 | 1 | -0.11 | -1.04 | -13.61 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 18.38 | 67.82 | 8.42 | 168.71 | 76.61 | 166.75 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.22 | -0.92 | 2 | 1 | 25.79 | 20.87 | -6.01 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | 2.45 | 10.78 | -13.47 | 63.33 | 17.61 | 67.21 | False |  | strong_accumulation | 1.21 | 1.25 | 2 | 2 | 2.1 | 2.2 | -24.6 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 4.97 | 27.6 | 16.01 | 82.86 | 52.91 | 78.17 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 1.68 | 2.45 | 3 | 3 | 11.02 | 11.42 | -5.27 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -6.6 | 7.9 | -23.26 | 45.59 | 14.45 | 39.93 | False |  | distribution_warning | -0.72 | -0.96 | 0 | 1 | -5.1 | -5.22 | -25.84 | 16 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | 0.98 | 12.75 | -23.55 | 3.22 | 15.8 | 15.8 | False |  | mild_accumulation | 0.18 | 0.56 | 1 | 2 | -1.16 | -3.5 | -32.59 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | 0.0 | 42.66 | -21.51 | 27.29 | 47.52 | 47.52 | True | 近20日漲幅>25% | distribution_warning | -1.31 | -2.95 | 0 | 1 | 8.48 | 5.21 | -34.18 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 64.11079364944591 | 53.35864647704091 | 4.78 | 11.98 | -17.24 | -0.85 | 18.81 | 18.81 | False |  | mild_accumulation | -0.31 | 0.16 | 2 | 2 | 2.31 | 1.59 | -17.92 | 18 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | 0.86 | 9.33 | -9.17 | 59.05 | 12.66 | 58.69 | False |  | mild_accumulation | 1.25 | 0.54 | 2 | 1 | 0.63 | 0.75 | -12.56 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 0.45 | 7.43 | -10.74 | 17.7 | 19.18 | 20.69 | False |  | strong_accumulation | 0.77 | 1.19 | 2 | 3 | 5.48 | 2.23 | -24.09 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 0.26 | 43.78 | 16.27 | 148.21 | 50.0 | 148.21 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.72 | -1.89 | 1 | 0 | 6.79 | 6.42 | -8.89 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -0.86 | 25.09 | 33.08 | 99.13 | 53.23 | 119.46 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.13 | -0.69 | 2 | 1 | 6.41 | 7.57 | -2.96 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -3.08 | 16.48 | -2.93 | 14.16 | 19.81 | 19.81 | False |  | mild_accumulation | 1.27 | 0.17 | 3 | 1 | 0.41 | 0.62 | -9.76 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | -1.37 | 6.4 | -8.09 | 3.85 | 10.77 | 31.55 | False |  | distribution_warning | -0.98 | -1.71 | 1 | 1 | -2.55 | -3.08 | -25.52 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | 1.05 | 0.35 | -19.64 | -9.84 | 6.65 | 6.65 | False |  | distribution_warning | -2.15 | -2.84 | 1 | 0 | -4.38 | -5.22 | -37.21 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 7.48 | 46.25 | 35.52 | 123.81 | 60.56 | 160.45 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.09 | 4.36 | 3 | 3 | 9.14 | 8.03 | -6.51 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -2.56 | -13.93 | 3.54 | 47.86 | 18.94 | 46.15 | False |  | distribution_warning | -2.98 | -1.29 | 2 | 2 | -12.15 | -8.49 | -28.17 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 1.46 | 0.54 | 4.13 | 2.78 | 3.54 | 10.12 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | -0.91 | -0.6 | -13.15 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 0.0 | 8.73 | -35.99 | -13.22 | 12.81 | 12.81 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.31 | -1.33 | -37.54 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | 1.81 | 3.14 | 4.23 | 9.14 | 5.35 | 10.06 | False |  | distribution_warning | -0.03 | 0.0 | 2 | 2 | 1.52 | 1.31 | -3.67 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 307.65627206955537 | 402.6798478136839 | 7.12 | 11.69 | -15.8 | 36.82 | 39.35 | 44.36 | False |  | mild_accumulation | 0.25 | -0.27 | 1 | 2 | 3.17 | 4.25 | -21.41 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 2.82 | 0.69 | -10.98 | 19.67 | 8.15 | 29.2 | False |  | distribution_warning | -0.42 | -0.15 | 0 | 0 | -2.09 | -2.82 | -30.48 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 5.79 | 56.1 | -3.52 | 185.29 | 62.71 | 192.24 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.46 | 11.69 | 2 | 2 | 9.17 | 8.89 | -7.69 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 8.96 | 28.93 | 5.76 | 87.2 | 38.87 | 85.35 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.11 | -0.16 | 2 | 1 | 7.77 | 7.61 | -12.11 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | 4.2 | 23.64 | -10.52 | 60.56 | 32.56 | 64.27 | False |  | strong_accumulation | 1.51 | 1.74 | 3 | 2 | 7.22 | 4.72 | -15.18 | 23 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | 5.46 | 18.4 | 2.87 | 67.33 | 24.88 | 65.79 | False |  | mild_accumulation | -0.01 | 0.67 | 1 | 2 | 4.08 | 3.91 | -10.36 | 16 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 133.3640235641089 | 87.69992405929172 | 6.69 | 21.44 | -40.7 | -14.41 | 33.28 | 33.28 | False |  | distribution_warning | -0.35 | -0.44 | 1 | 1 | 5.15 | 1.6 | -41.67 | 16 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.31 | -0.1 | -10.44 | 4.42 | 2.87 | 4.53 | False |  | mild_accumulation | 0.53 | -0.21 | 3 | 2 | -1.66 | -1.86 | -12.55 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | 3.49 | 18.77 | -24.17 | 28.03 | 23.52 | 29.31 | False |  | strong_accumulation | 0.56 | 1.09 | 2 | 2 | 2.56 | -0.28 | -30.58 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | 0.88 | 3.84 | 0.22 | 4.55 | 6.98 | 6.98 | False |  | mild_accumulation | -0.01 | 0.12 | 1 | 2 | 1.55 | 0.7 | -19.01 | 18 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 9.54 | 18.32 | 26.02 | 11.51 | 28.1 | 28.1 | False |  | mild_accumulation | 0.16 | 0.0 | 2 | 0 | 12.08 | 10.57 | -0.32 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 5.29 | -1.24 | 0.99 | -10.16 | 6.87 | 10.15 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.56 | 1.83 | -11.17 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -0.31 | 10.98 | 12.68 | 33.33 | 16.5 | 42.43 | False |  | strong_accumulation | 1.58 | 1.93 | 3 | 3 | 4.5 | 3.92 | -2.04 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 1.31 | 5.75 | -17.87 | -49.14 | 8.89 | 8.89 | False |  | distribution_warning | -0.37 | -0.27 | 1 | 1 | 0.58 | -0.41 | -24.9 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 4.02 | 5.76 | -5.55 | -4.9 | 10.27 | 10.27 | False |  | mild_accumulation | -0.03 | 0.36 | 1 | 3 | 4.04 | 2.34 | -12.53 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | 0.99 | -0.49 | 2.82 | -10.53 | 3.87 | 3.98 | False |  | strong_accumulation | 0.44 | 0.39 | 2 | 2 | -0.85 | -0.97 | -13.56 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | D_僅留完整清單 | 56.21501385482998 | 35.673950917357274 | -0.65 | 13.43 | 15.74 | 33.72 | 28.81 | 37.14 | False |  | strong_accumulation | 0.87 | 1.19 | 3 | 3 | 3.38 | 2.76 | -15.56 | 15 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 18.34 | -33.9 | 5.45 | 45.31 | 28.13 | 58.94 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 1 | -1.94 | -1.08 | -38.62 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 3.99 | 0.0 | -6.9 | -13.11 | 8.01 | 8.01 | False |  | mild_accumulation | 0.08 | -2.09 | 1 | 0 | 1.3 | 0.62 | -13.69 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | 0.93 | 19.89 | 4.83 | 31.78 | 23.06 | 34.78 | False |  | strong_accumulation | 2.81 | 3.85 | 3 | 3 | 2.26 | 1.37 | -12.03 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -1.65 | -9.47 | -3.24 | 9.63 | 2.14 | 21.32 | False |  | strong_accumulation | 1.41 | 0.19 | 3 | 2 | -4.25 | -5.2 | -26.69 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 11.41 | 59.01 | 9.4 | 88.62 | 69.88 | 86.05 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 7.48 | 7.23 | 2 | 2 | 9.84 | 9.37 | -4.2 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 0.0 | 31.95 | -19.05 | 83.12 | 40.3 | 100.0 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.24 | -0.57 | 1 | 0 | 3.29 | 0.25 | -33.33 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 1.94 | 50.6 | 13.29 | 86.14 | 56.58 | 81.32 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.41 | 2.28 | 2 | 3 | 10.71 | 11.5 | -4.97 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | 0.65 | 5.11 | 21.87 | 51.14 | 23.33 | 54.68 | False |  | mild_accumulation | 1.32 | 0.87 | 2 | 1 | -3.37 | -1.35 | -20.6 | 17 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | 1.07 | 13.72 | -18.25 | 35.72 | 17.35 | 36.7 | False |  | mild_accumulation | -0.14 | 0.19 | 1 | 1 | -0.8 | -1.79 | -22.91 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | 0.89 | 4.49 | -7.06 | 54.42 | 8.48 | 54.95 | False |  | mild_accumulation | -0.82 | 0.47 | 2 | 2 | -3.11 | -3.63 | -23.57 | 18 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -2.48 | 6.5 | -31.65 | -11.49 | 9.17 | 9.17 | False |  | distribution_warning | -0.99 | -1.75 | 1 | 1 | -5.82 | -4.9 | -34.72 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 3.14 | 11.92 | -10.33 | 2.91 | 15.58 | 15.58 | False |  | mild_accumulation | 0.72 | -0.01 | 2 | 1 | 1.83 | -0.08 | -29.23 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 0.1 | 41.68 | -7.14 | 33.06 | 47.09 | 47.09 | True | 近20日漲幅>25% | mild_accumulation | 0.15 | -0.71 | 1 | 1 | 9.7 | 6.74 | -19.57 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -2.04 | 12.3 | -10.16 | 28.35 | 15.93 | 26.79 | False |  | mild_accumulation | 2.89 | 1.28 | 2 | 1 | 0.31 | 0.35 | -9.73 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 54.59950544814572 | 34.30071340658413 | -1.4 | 27.15 | -17.84 | 54.82 | 33.49 | 66.03 | True | 近20日漲幅>25% | distribution_warning | -2.06 | -1.76 | 1 | 1 | 0.81 | 0.1 | -27.86 |  | fail_already_priced_in |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 5.83 | 13.54 | -20.44 | 0.18 | 21.11 | 21.11 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 8.7 | 4.41 | -35.04 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 10.43 | 22.71 | 17.05 | 115.25 | 62.2 | 128.42 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.92 | -5.4 | 0 | 1 | 15.89 | 8.39 | -36.82 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -6.76 | 30.83 | -29.12 | 81.87 | 45.18 | 87.01 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.89 | -5.49 | 1 | 1 | 4.58 | -3.63 | -54.66 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | 21.24 | 25.34 | -25.95 | 67.12 | 38.43 | 85.5 | True | 近20日漲幅>25%；距120日低點反彈>80% | distribution_warning | -0.87 | -1.54 | 1 | 1 | 11.23 | 10.2 | -27.68 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 3.32 | 48.39 | -8.91 | 143.54 | 64.79 | 135.53 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.9 | -4.11 | 1 | 0 | 9.26 | 4.07 | -29.46 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 12.16 | 51.9 | 6.8 | 197.19 | 65.29 | 228.25 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.11 | 0.0 | 2 | 0 | 12.82 | 12.6 | -7.04 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | 0.0 | 7.37 | 4.6 | 41.09 | 30.94 | 48.57 | False |  | strong_accumulation | 3.25 | 3.26 | 2 | 2 | -1.42 | 1.45 | -11.65 | 19 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 4.04 | 2.54 | 8.85 | 4.43 | 15.04 | 18.91 | False |  | mild_accumulation | 0.13 | 0.0 | 1 | 0 | 1.76 | 1.96 | -0.35 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 59.23071292224356 | 63.75000065335939 | -1.37 | 14.04 | -35.52 | 5.37 | 20.13 | 20.13 | False |  | mild_accumulation | -0.89 | 0.33 | 1 | 2 | -1.09 | -2.8 | -35.71 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 15.68 | 85.89 | 31.58 | 172.83 | 92.91 | 186.21 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.11 | 0.31 | 3 | 1 | 22.99 | 20.36 | 0.0 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 1.23 | 57.48 | 6.49 | 131.45 | 73.94 | 142.19 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.39 | 4.76 | 2 | 3 | 15.37 | 12.43 | -6.21 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | -0.45 | 14.96 | -13.61 | 2.58 | 16.8 | 16.8 | False |  | mild_accumulation | 0.39 | -1.47 | 2 | 0 | 2.1 | 1.1 | -19.93 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -0.71 | 6.24 | -35.35 | 24.48 | 10.61 | 37.17 | False |  | mild_accumulation | -1.45 | 0.25 | 0 | 3 | -3.68 | -3.99 | -41.47 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 1.38 | 18.68 | -34.35 | -33.36 | 28.53 | 28.53 | False |  | mild_accumulation | 1.69 | -0.95 | 3 | 2 | 2.23 | -0.99 | -39.31 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 4.85 | 72.96 | 49.09 | 63.81 | 91.47 | 104.46 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.23 | -0.47 | 3 | 2 | 23.31 | 22.27 | 0.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | 9.09 | 41.18 | -18.43 | 29.41 | 50.57 | 59.68 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.42 | -1.35 | 2 | 2 | 6.89 | 4.95 | -19.1 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -8.86 | -4.07 | -3.84 | 25.71 | 18.99 | 34.56 | False |  | strong_accumulation | 2.23 | 2.17 | 3 | 2 | -7.84 | -6.42 | -21.53 | 17 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 1.41 | 1.89 | -8.86 | 49.79 | 5.88 | 52.33 | False |  | distribution_warning | -0.91 | -0.69 | 1 | 1 | -6.63 | -4.7 | -17.24 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | 0.99 | 16.35 | -13.87 | -17.0 | 19.74 | 19.74 | False |  | strong_accumulation | 0.49 | 0.21 | 3 | 2 | 2.95 | 1.08 | -17.34 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | 6.05 | 16.33 | -37.36 | -22.18 | 27.37 | 27.37 | False |  | distribution_warning | -0.55 | -0.64 | 0 | 2 | 2.71 | -1.48 | -41.98 | 12 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 0.38 | 5.35 | 24.58 | -2.61 | 31.82 | 31.82 | False |  | strong_accumulation | 0.29 | 0.28 | 3 | 3 | 1.57 | 2.07 | -6.95 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | -2.4 | 15.34 | -22.81 | 76.52 | 25.31 | 77.29 | True | 近120日漲幅>70% | mild_accumulation | 0.57 | -1.74 | 2 | 0 | -2.57 | -2.19 | -23.4 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 1.95 | 6.09 | -9.83 | -14.54 | 7.84 | 7.84 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | 1.53 | 0.29 | -21.94 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 128.9172485640275 | 121.34662298357856 | 6.6 | 24.2 | -18.53 | 23.68 | 29.26 | 29.26 | False |  | distribution_warning | -1.02 | -1.25 | 1 | 0 | 5.3 | 2.8 | -33.98 | 12 | selected |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -1.65 | 13.9 | -21.32 | 3.48 | 19.07 | 19.07 | False |  | mild_accumulation | 0.5 | -0.01 | 2 | 0 | -0.2 | -0.06 | -20.62 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | 1.99 | 13.64 | -13.87 | 77.34 | 17.28 | 92.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.79 | -2.13 | 1 | 1 | 1.23 | 0.62 | -19.61 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 3.2 | 6.62 | -16.18 | -20.55 | 10.27 | 10.27 | False |  | distribution_warning | -0.08 | -0.21 | 2 | 0 | 1.61 | -0.55 | -24.08 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -2.73 | -1.21 | -11.84 | -32.87 | 4.73 | 4.73 | False |  | strong_accumulation | 0.03 | 0.03 | 3 | 3 | -3.58 | -3.7 | -15.13 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 4.57 | 26.64 | -29.28 | 42.14 | 35.56 | 38.9 | True | 近20日漲幅>25% | mild_accumulation | 0.07 | 0.11 | 1 | 2 | 6.88 | 3.74 | -30.29 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 98.74936839745938 | 71.28591290526819 | 4.81 | 24.71 | -5.71 | 47.3 | 39.39 | 48.5 | False |  | mild_accumulation | -0.45 | 0.38 | 2 | 2 | 2.86 | 3.94 | -13.63 | 20 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 17.59 | 52.23 | -21.43 | 13.29 | 62.38 | 62.38 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.31 | -1.02 | 2 | 0 | 19.13 | 15.13 | -26.67 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 105.41523454519049 | 68.91539282131619 | 8.43 | 20.54 | -37.48 | 4.04 | 33.53 | 33.53 | False |  | distribution_warning | -18.41 | -18.98 | 0 | 1 | 4.91 | 1.31 | -43.06 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 0.53 | 3.55 | 17.7 | 38.83 | 19.94 | 41.95 | False |  | distribution_warning | -0.52 | 0.0 | 1 | 0 | -0.5 | -0.15 | -6.19 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -1.28 | -5.49 | -14.1 | 0.52 | 1.57 | 3.34 | False |  | distribution_warning | -5.63 | -6.23 | 1 | 1 | -6.97 | -5.47 | -18.53 | 13 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 2.24 | -2.44 | -13.75 | -1.69 | 4.23 | 4.23 | False |  | distribution_warning | -0.45 | -0.34 | 1 | 1 | 0.23 | -0.46 | -23.72 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 1.14 | -4.12 | 1.38 | -10.89 | 4.0 | 8.07 | False |  | distribution_warning | -0.03 | -0.02 | 0 | 0 | -0.76 | -0.59 | -7.53 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | -2.9 | -1.41 | 2.95 | 3.08 | 5.78 | 5.78 | False |  | distribution_warning | 0.0 | -0.2 | 1 | 1 | -1.95 | -2.26 | -12.11 | 16 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 3.12 | -0.63 | 7.73 | 15.47 | 10.0 | 16.98 | False |  | mild_accumulation | 0.16 | 0.83 | 1 | 2 | 2.89 | 1.53 | -4.13 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | -8.08 | 39.14 | 14.04 | 44.44 | 41.3 | 46.3 | True | 近20日漲幅>25% | strong_accumulation | 2.88 | 4.45 | 2 | 2 | 9.59 | 7.02 | -14.47 |  | fail_already_priced_in |