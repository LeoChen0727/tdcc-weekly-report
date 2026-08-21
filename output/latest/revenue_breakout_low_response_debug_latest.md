# 營收爆發低反應股 Debug Report

- 產生時間：`2026-08-21 19:51:19 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 694405 |
| tdcc_rows | 1971 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 434 |
| tdcc_mild_accumulation_count | 738 |
| tdcc_distribution_warning_count | 608 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 84 |
| already_priced_in_excluded | 28 |
| overheat_pass | 56 |
| score_pass | 56 |
| theme_priority_pass | 51 |
| final_rows | 51 |

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
| fail_low_response_condition | 253 |
| fail_already_priced_in | 28 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral |  | 102.03987961747174 | 127.0977623123372 | 12.0 | 9.27 | 10.89 | -13.85 | 19.28 | 19.28 | False |  | mild_accumulation | -0.14 | 0.47 | 1 | 2 | 10.0 | 8.29 | -3.45 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 0.39 | -2.64 | -5.84 | -23.89 | 3.41 | 3.41 | False |  | mild_accumulation | 0.26 | -0.69 | 2 | 0 | 0.55 | -0.38 | -16.91 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.0 | -7.21 | 12.45 | 5.75 | 13.19 | 24.25 | False |  | distribution_warning | -0.76 | 0.0 | 1 | 1 | 0.44 | -1.2 | -15.57 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | 0.84 | 10.09 | 8.11 | 3.0 | 13.21 | 13.21 | False |  | strong_accumulation | 0.48 | 0.69 | 2 | 2 | 7.07 | 5.68 | -0.41 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -0.84 | -5.08 | -4.05 | -8.97 | 4.11 | 4.72 | False |  | distribution_warning | -0.01 | -0.02 | 1 | 0 | -1.76 | -1.65 | -11.91 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 1.23 | -3.15 | -3.91 | 17.7 | 4.68 | 21.78 | False |  | strong_accumulation | 0.13 | 0.91 | 2 | 3 | -0.14 | -1.79 | -26.79 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 1.33 | -5.3 | -27.62 | -31.22 | 7.04 | 7.04 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | -0.54 | -2.83 | -31.53 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -1.71 | 0.7 | 2.5 | 31.65 | 17.14 | 52.17 | False |  | mild_accumulation | -0.61 | 0.3 | 1 | 2 | -1.58 | -0.99 | -11.15 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -6.24 | 1.56 | -7.35 | -9.7 | 9.07 | 9.07 | False |  | strong_accumulation | 0.97 | 0.25 | 2 | 2 | 0.2 | -0.53 | -15.91 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 9.72 | 26.86 | 71.65 | 100.0 | 73.89 | 101.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.84 | 2.58 | 3 | 3 | 19.95 | 16.66 | -1.62 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | 3.66 | 14.09 | 78.95 | 74.36 | 81.04 | 88.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.73 | -2.12 | 1 | 2 | 9.27 | 4.85 | -32.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral |  | 3460.154507547597 | 13488.270126747157 | 13.32 | 14.73 | 25.42 | 25.64 | 30.51 | 31.91 | False |  | strong_accumulation | 0.29 | 0.23 | 2 | 2 | 12.39 | 12.21 | -2.12 |  | fail_low_response_condition |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | 1.77 | 5.5 | 13.86 | -1.29 | 14.43 | 15.0 | False |  | distribution_warning | -0.04 | 0.0 | 0 | 1 | 2.5 | 1.97 | -8.37 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | 2.38 | 10.26 | 8.4 | 14.16 | 15.18 | 24.64 | False |  | mild_accumulation | -0.01 | 0.28 | 1 | 1 | 4.43 | 3.56 | -18.61 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | 7.08 | 73.04 | 164.26 | 303.16 | 177.41 | 357.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.4 | 2 | 1 | 23.25 | 19.3 | -11.27 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | 1.64 | 8.39 | -6.91 |  | 12.32 |  | False |  | distribution_warning | -0.49 | -0.76 | 0 | 1 | 1.13 | 1.69 | -25.12 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -4.31 | -18.12 | -10.62 | 8.93 | 6.55 | 20.79 | False |  | mild_accumulation | -0.42 | 0.82 | 1 | 2 | -7.01 | -8.77 | -35.62 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | 15.34 | 7.56 | 21.42 | 37.65 | 23.89 | 39.38 | False |  | distribution_warning | -0.01 | 0.0 | 0 | 0 | 12.16 | 10.81 | -5.51 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 1.59 | -0.16 | 6.14 | -10.49 | 9.03 | 24.03 | False |  | strong_accumulation | 0.03 | 0.14 | 2 | 2 | 2.41 | 1.7 | -8.57 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | 0.59 | -1.28 | 13.2 | 143.27 | 41.5 | 154.95 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.25 | 1.5 | 2 | 2 | 1.75 | -1.02 | -26.94 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | -11.41 | -19.5 | 9.24 | 105.53 | 28.4 | 121.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.92 | -3.88 | 1 | 1 | -9.38 | -10.83 | -39.04 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.43152295785818 | 37.52324493334001 | -0.94 | 1.6 | -5.93 | 69.16 | 24.8 | 87.13 | True | 距120日低點反彈>80% | mild_accumulation | -0.11 | 0.46 | 1 | 2 | 2.09 | -2.01 | -36.22 |  | fail_already_priced_in |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.18913901503827 | 37.89396256372083 | -5.39 | -2.77 | -15.05 | 9.6 | 8.39 | 30.93 | False |  | mild_accumulation | 0.48 | 0.49 | 1 | 1 | -2.85 | -2.68 | -21.82 | 16 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -10.93 | -13.71 | -24.93 | 107.1 | 21.36 | 130.83 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.61 | -1.72 | 1 | 1 | -2.9 | -10.36 | -54.59 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -10.58 | -1.21 | -26.43 | 13.95 | 33.44 | 37.95 | False |  | distribution_warning | -1.42 | -1.8 | 1 | 1 | 1.14 | -3.18 | -36.2 | 18 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -1.36 | 17.15 | 14.56 | 61.61 | 54.7 | 115.99 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.43 | -0.32 | 1 | 1 | 10.89 | 6.47 | -22.48 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 71.68985948774075 | 62.35657344241515 | -11.52 | -8.33 | -16.26 | 43.31 | 10.6 | 53.01 | False |  | distribution_warning | -0.35 | -0.51 | 1 | 1 | -7.04 | -8.22 | -27.96 | 11 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 126.87926937028048 | 84.53540417540658 | -3.74 | -1.24 | 1.86 | 24.82 | 8.97 | 30.6 | False |  | mild_accumulation | 0.15 | 0.21 | 2 | 1 | -2.94 | -2.15 | -10.99 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 4.02 | -7.42 | 6.31 | 3.58 | 8.38 | 8.38 | False |  | distribution_warning | -0.48 | -0.04 | 1 | 1 | 0.54 | 0.38 | -12.03 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 7.02 | 13.66 | -11.81 | 125.93 | 47.58 | 144.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.71 | 0.92 | 2 | 2 | 10.96 | 5.47 | -21.46 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -6.01 | 1.86 | -6.41 | 56.8 | 15.67 | 70.43 | False |  | strong_accumulation | 1.53 | 1.51 | 3 | 3 | 1.62 | 0.87 | -25.85 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | -7.53 | 19.46 | 21.02 | 77.8 | 45.04 | 84.2 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.62 | 1.39 | 3 | 3 | 8.8 | 8.26 | -10.15 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 175.25829018155406 | 101.53000922739209 | -8.7 | 0.96 | -16.67 | 49.47 | 21.39 | 69.35 | False |  | distribution_warning | -0.54 | -0.88 | 1 | 1 | 0.99 | -0.71 | -22.51 | 18 | selected |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 72.07351671395091 | 95.02794974786696 | -5.06 | -8.32 | -24.22 | 0.8 | 14.45 | 14.45 | False |  | mild_accumulation | -0.24 | 0.94 | 1 | 2 | -2.03 | -5.89 | -33.38 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 77.38084589596791 | 70.28827013710922 | -4.93 | 7.1 | -26.89 | 31.11 | 36.88 | 36.88 | False |  | distribution_warning | -1.0 | -2.73 | 1 | 1 | 3.5 | -2.37 | -38.92 | 13 | selected |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -2.84 | 1.48 | -17.67 | -5.91 | 16.1 | 16.1 | False |  | distribution_warning | -0.11 | -0.03 | 2 | 2 | 0.68 | -1.11 | -20.72 | 13 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 59.67101651519066 | 49.96169077295545 | -14.59 | -4.23 | -8.24 | 55.73 | 8.81 | 64.41 | False |  | strong_accumulation | 2.61 | 2.18 | 3 | 2 | -2.22 | -2.84 | -15.55 | 17 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | -1.83 | -1.98 | -5.16 | 11.05 | 15.23 | 18.2 | False |  | mild_accumulation | -0.22 | 0.07 | 1 | 2 | 2.66 | -0.82 | -26.6 | 22 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -7.87 | 19.45 | 10.94 | 140.17 | 44.53 | 167.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.05 | -0.95 | 2 | 1 | 6.36 | 3.18 | -12.21 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -4.98 | 11.7 | 31.11 | 89.49 | 44.54 | 107.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.09 | -0.2 | 2 | 1 | 3.03 | 3.07 | -8.46 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -4.56 | 6.08 | -1.1 | 7.9 | 19.62 | 19.62 | False |  | distribution_warning | -0.1 | -1.62 | 2 | 1 | 1.93 | 0.56 | -9.9 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | -5.78 | -5.36 | -8.23 | -3.64 | 8.72 | 29.11 | False |  | distribution_warning | -1.32 | -0.83 | 0 | 1 | -4.03 | -5.94 | -26.9 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -2.57 | -14.69 | -17.66 | -10.39 | 2.34 | 2.34 | False |  | distribution_warning | -2.48 | -3.79 | 1 | 0 | -6.84 | -8.28 | -38.08 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 3.12 | 31.67 | 52.16 | 105.05 | 63.98 | 165.99 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.63 | 2.91 | 2 | 2 | 15.68 | 12.52 | -4.52 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -8.64 | -19.85 | 5.48 | 40.64 | 17.53 | 49.6 | False |  | distribution_warning | -4.06 | -0.62 | 1 | 2 | -15.14 | -11.88 | -29.02 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | -2.32 | -3.53 | 3.4 | 16.38 | 4.39 | 14.2 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.54 | -2.3 | -14.4 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | -2.98 | -0.28 | -35.61 | -13.53 | 11.87 | 11.87 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 0.28 | -2.64 | -38.59 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | 2.58 | 2.84 | 6.7 | 3.11 | 7.86 | 11.17 | False |  | distribution_warning | -0.17 | -0.68 | 1 | 2 | 2.99 | 2.66 | -2.69 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 307.65627206955537 | 402.6798478136839 | 6.84 | 18.37 | -7.54 | 46.37 | 44.68 | 57.43 | False |  | distribution_warning | -0.39 | -0.79 | 1 | 2 | 9.3 | 10.08 | -18.41 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -3.03 | -7.84 | -11.11 | 10.77 | 6.67 | 27.43 | False |  | distribution_warning | -0.49 | -0.13 | 0 | 0 | -4.0 | -5.27 | -31.43 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -6.77 | 22.18 | -2.98 | 162.08 | 51.69 | 189.18 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 11.63 | 11.23 | 3 | 2 | 7.14 | 4.09 | -13.94 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 280.87664000910723 | 176.72380227122633 | -10.43 | 6.71 | 3.74 | 69.43 | 27.45 | 79.14 | False |  | mild_accumulation | 8.09 | 6.27 | 2 | 1 | 1.74 | 0.36 | -19.34 | 23 | selected |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | 4.67 | 8.74 | -9.53 | 40.0 | 30.23 | 75.27 | False |  | strong_accumulation | 0.42 | 1.23 | 2 | 2 | 6.72 | 3.03 | -16.67 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | -2.92 | -2.1 | -4.51 | 48.22 | 15.92 | 61.36 | False |  | strong_accumulation | 0.53 | 1.49 | 2 | 3 | -2.33 | -3.54 | -16.79 | 17 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -4.88 | 1.74 | -44.88 | -19.96 | 26.63 | 26.63 | False |  | mild_accumulation | 0.28 | 0.88 | 1 | 1 | 1.55 | -3.64 | -45.39 | 22 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -2.01 | -1.81 | -8.0 | 4.49 | 3.72 | 6.89 | False |  | distribution_warning | -0.06 | -0.16 | 2 | 2 | -0.96 | -1.54 | -11.82 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | -5.95 | -1.2 | -27.86 | 22.61 | 18.88 | 31.5 | False |  | mild_accumulation | 0.44 | 0.48 | 1 | 2 | 0.28 | -4.33 | -33.18 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | 1.31 | 1.76 | 2.21 | 1.76 | 7.67 | 8.94 | False |  | strong_accumulation | 0.22 | 0.13 | 2 | 2 | 2.68 | 1.56 | -18.49 | 19 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | 8.03 | 12.12 | 19.84 | 4.23 | 22.31 | 22.31 | False |  | mild_accumulation | 0.2 | 0.01 | 3 | 1 | 9.12 | 7.81 | -1.33 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 1.43 | 1.0 | 2.76 | -13.97 | 5.67 | 8.92 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.11 | 0.77 | -12.16 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 5.63 | 10.41 | 16.33 | 32.97 | 18.45 | 44.81 | False |  | strong_accumulation | 1.13 | 1.16 | 3 | 3 | 7.89 | 6.85 | -0.41 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 0.13 | 0.91 | -15.14 | -45.37 | 9.87 | 9.87 | False |  | mild_accumulation | 0.05 | -0.05 | 2 | 2 | 1.69 | 0.36 | -24.22 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 3.43 | 4.2 | -4.41 | -6.85 | 9.64 | 9.64 | False |  | mild_accumulation | 0.09 | -0.05 | 2 | 2 | 4.24 | 2.32 | -13.03 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | 1.49 | 1.49 | 3.96 | -7.24 | 4.49 | 4.49 | False |  | strong_accumulation | 1.0 | 1.03 | 3 | 2 | -0.46 | -0.95 | -13.14 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround |  | 56.21501385482998 | 35.673950917357274 | 19.02 | 21.72 | 35.46 | 42.26 | 44.07 | 54.08 | False |  | strong_accumulation | 0.48 | 0.69 | 3 | 2 | 18.25 | 17.17 | -1.92 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | -1.75 | -23.95 | -1.37 | 11.97 | 19.39 | 48.09 | False |  | mild_accumulation | 0.04 | 0.0 | 1 | 1 | -14.34 | -9.69 | -42.81 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | -2.25 | 6.25 | -8.43 | -10.32 | 8.01 | 8.01 | False |  | mild_accumulation | 0.18 | -1.99 | 2 | 1 | 1.3 | 0.95 | -13.69 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -2.84 | 9.81 | 3.51 | 30.06 | 22.68 | 37.06 | False |  | strong_accumulation | 2.01 | 3.61 | 2 | 2 | 3.8 | 1.34 | -12.3 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | -4.72 | -10.7 | -2.02 | 11.01 | 2.11 | 22.84 | False |  | mild_accumulation | 0.21 | -0.02 | 2 | 1 | -4.63 | -5.52 | -25.77 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | -6.22 | 24.51 | 4.06 | 73.31 | 59.32 | 94.32 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.27 | 5.3 | 2 | 2 | 8.47 | 5.7 | -10.16 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -4.0 | 3.25 | -28.7 | 73.85 | 35.35 | 92.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | -0.08 | 2 | 1 | 1.83 | -3.87 | -35.69 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 57.39113833331852 | 80.33836073352812 | -11.44 | 20.38 | 7.5 | 57.42 | 42.18 | 72.07 | False |  | strong_accumulation | 3.13 | 1.64 | 3 | 2 | 4.62 | 3.05 | -13.7 | 19 | selected |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.91966377290892 | 26.75099850600647 | -4.25 | -4.04 | 20.59 | 52.36 | 22.55 | 62.82 | False |  | strong_accumulation | 4.1 | 4.24 | 3 | 2 | -5.26 | -4.02 | -22.58 | 18 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -1.47 | -0.3 | -17.67 | 24.72 | 18.76 | 41.41 | False |  | distribution_warning | -0.9 | -1.45 | 1 | 1 | 1.62 | -1.12 | -21.98 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | A_優先追蹤 | 78.71068980000454 | 32.99031345898157 | -5.8 | -9.1 | -9.64 | 50.25 | 8.6 | 59.75 | False |  | strong_accumulation | 0.17 | 0.59 | 2 | 2 | -3.02 | -4.19 | -23.48 | 19 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.9 | 0.24 | -28.6 | -2.37 | 14.44 | 14.44 | False |  | distribution_warning | -0.8 | -1.02 | 1 | 1 | -0.87 | -1.47 | -31.56 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | -3.86 | -5.49 | -12.67 | -3.24 | 12.56 | 12.56 | False |  | distribution_warning | -0.7 | -2.0 | 1 | 1 | -0.41 | -3.29 | -31.08 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | B_可觀察 | 56.54703093190022 | 34.71282457960092 | -5.94 | 16.79 | -11.9 | 24.9 | 40.37 | 40.37 | False |  | mild_accumulation | 0.14 | -0.16 | 1 | 2 | 8.45 | 2.88 | -23.24 | 16 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -2.84 | 5.64 | -0.17 | 21.55 | 17.14 | 33.41 | False |  | mild_accumulation | 2.91 | 2.62 | 3 | 1 | 2.51 | 1.36 | -9.22 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -4.76 | 11.11 | -22.22 | 55.56 | 33.02 | 65.44 | False |  | distribution_warning | -1.64 | -2.03 | 2 | 0 | 2.94 | -0.42 | -28.11 | 13 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 9.58 | -1.85 | -20.36 | 29.91 | 18.22 | 22.86 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 6.76 | 2.2 | -36.59 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | -6.47 | -19.93 | 0.46 | 71.14 | 38.57 | 95.14 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.63 | -6.3 | 0 | 0 | -0.63 | -7.24 | -46.02 |  | fail_already_priced_in |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -5.44 | 0.61 | -27.95 | 77.23 | 44.74 | 95.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -6.23 | -7.0 | 0 | 1 | 6.68 | -5.05 | -54.79 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 204.3244857198993 | 247.3095962162866 | 3.96 | 9.29 | -34.55 | 51.56 | 27.24 | 70.5 | False |  | distribution_warning | -1.8 | -0.52 | 1 | 1 | 5.04 | 3.63 | -35.9 | 15 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 7.41 | 16.94 | -8.81 | 162.68 | 66.86 | 176.72 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.71 | -0.12 | 1 | 1 | 14.49 | 5.3 | -28.57 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 14.87 | 56.46 | 24.85 | 209.0 | 75.82 | 249.15 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 1 | 0 | 27.26 | 24.65 | 0.0 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 60.760461865560174 | 88.15608743643294 | -9.3 | -1.96 | 10.73 | 36.58 | 26.26 | 43.27 | False |  | strong_accumulation | 5.6 | 5.59 | 3 | 3 | -4.44 | -2.26 | -14.81 | 18 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 0.36 | 2.94 | 8.95 | 0.72 | 13.82 | 17.65 | False |  | distribution_warning | -0.13 | 0.0 | 0 | 0 | 1.08 | 1.26 | -1.41 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 59.23071292224356 | 63.75000065335939 | -4.85 | -1.37 | -31.43 | 0.93 | 20.13 | 20.13 | False |  | distribution_warning | -0.49 | -0.42 | 1 | 2 | -0.24 | -3.73 | -35.71 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 2.47 | 37.59 | 19.91 | 137.79 | 76.38 | 161.68 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.37 | 1.16 | 2 | 1 | 19.73 | 14.19 | -6.51 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | 8.04 | 29.04 | 12.33 | 91.99 | 66.97 | 132.49 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.62 | 0.17 | 1 | 2 | 15.47 | 9.82 | -9.97 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | -4.17 | 5.81 | -9.71 | -2.46 | 16.53 | 16.53 | False |  | distribution_warning | -1.29 | -2.53 | 1 | 0 | 3.51 | 1.38 | -20.11 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -7.11 | -1.76 | -28.85 | 23.67 | 10.88 | 37.5 | False |  | distribution_warning | -0.49 | -0.05 | 1 | 2 | -3.1 | -4.9 | -41.33 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | -5.65 | -0.34 | -29.14 | -35.7 | 26.35 | 26.35 | False |  | strong_accumulation | 0.58 | 0.91 | 2 | 2 | 1.51 | -3.53 | -40.34 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | 11.12 | 57.29 | 52.19 | 71.82 | 80.43 | 92.68 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.26 | -1.51 | 3 | 2 | 24.06 | 20.57 | -4.0 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 181.7841084291265 | -13.777157023400417 | -12.11 | 8.66 | -16.19 | 13.15 | 40.68 | 49.19 | False |  | mild_accumulation | 0.41 | -3.57 | 2 | 1 | 2.9 | -1.27 | -24.41 | 20 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | 3.41 | 3.17 | 7.57 | 41.3 | 35.01 | 52.68 | False |  | mild_accumulation | 1.5 | 0.64 | 3 | 1 | 3.8 | 4.71 | -10.96 | 18 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 90.83318057075236 | 59.917707856465086 | -3.48 | -5.53 | -5.53 | 57.0 | 8.82 | 64.69 | False |  | strong_accumulation | 0.29 | 0.49 | 2 | 2 | -4.17 | -3.01 | -14.94 | 21 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | 2.99 | 3.5 | -16.87 | -10.78 | 20.91 | 20.91 | False |  | strong_accumulation | 0.45 | 1.02 | 3 | 3 | 5.5 | 2.34 | -18.18 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | -7.76 | -8.15 | -38.33 | -28.43 | 19.55 | 19.55 | False |  | distribution_warning | -0.17 | -0.41 | 1 | 2 | -2.92 | -8.72 | -45.55 | 12 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | -1.32 | 0.77 | 28.19 | 2.55 | 32.07 | 32.07 | False |  | strong_accumulation | 0.31 | 0.28 | 3 | 3 | 2.22 | 2.77 | -6.77 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | -8.37 | 5.74 | -24.02 | 65.98 | 25.0 | 90.14 | True | 距120日低點反彈>80% | mild_accumulation | 1.33 | 0.03 | 3 | 1 | -1.75 | -3.55 | -25.82 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -0.77 | 0.39 | -8.16 | -14.94 | 6.8 | 6.8 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.11 | -0.74 | -22.69 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -5.83 | 2.69 | -22.22 | 17.81 | 22.27 | 30.23 | False |  | distribution_warning | -1.34 | -2.13 | 1 | 0 | 1.26 | -3.03 | -37.55 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -0.22 | 7.94 | -20.78 | 0.66 | 21.47 | 21.47 | False |  | mild_accumulation | 0.6 | 0.0 | 3 | 1 | 3.28 | 2.01 | -22.14 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -6.89 | -4.17 | -12.27 | 62.07 | 12.93 | 85.53 | True | 距120日低點反彈>80% | distribution_warning | -3.4 | -2.14 | 1 | 1 | -1.88 | -3.36 | -22.59 |  | fail_already_priced_in |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | 0.7 | -5.57 | -16.52 | -23.61 | 9.51 | 9.51 | False |  | distribution_warning | -0.36 | -0.17 | 1 | 0 | 1.03 | -1.72 | -24.61 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -0.35 | -3.82 | -7.07 | -29.63 | 7.55 | 7.55 | False |  | strong_accumulation | 0.04 | 0.03 | 3 | 3 | 0.01 | -0.23 | -11.4 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | -0.14 | 3.71 | -26.22 | 45.87 | 29.26 | 52.07 | False |  | distribution_warning | -0.05 | -0.03 | 1 | 1 | 4.04 | -0.68 | -33.52 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 98.74936839745938 | 71.28591290526819 | 0.36 | 26.32 | 0.0 | 45.65 | 41.18 | 61.88 | True | 近20日漲幅>25% | strong_accumulation | 6.22 | 7.02 | 2 | 3 | 7.65 | 6.73 | -12.52 |  | fail_already_priced_in |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 136.6326290773289 | -1.350919909057194 | 4.51 | 8.27 | -28.5 | -5.64 | 43.33 | 43.33 | False |  | distribution_warning | -1.94 | 0.0 | 1 | 0 | 9.0 | 3.6 | -35.27 | 12 | selected |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -4.48 | -5.06 | -40.77 | -7.34 | 23.55 | 23.55 | False |  | distribution_warning | -4.2 | -2.48 | 1 | 1 | -2.3 | -7.53 | -47.32 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 1.33 | -1.55 | 22.44 | 34.51 | 22.44 | 46.92 | False |  | distribution_warning | -0.56 | 0.0 | 0 | 0 | 0.42 | 0.56 | -5.45 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -2.76 | -12.51 | -10.5 | -1.27 | 1.84 | 3.6 | False |  | distribution_warning | -1.25 | -1.76 | 2 | 2 | -8.2 | -6.76 | -18.32 | 13 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 3.38 | -2.58 | -11.69 | -3.89 | 4.56 | 4.56 | False |  | distribution_warning | -0.45 | -0.63 | 1 | 1 | 0.01 | -0.41 | -23.48 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 3.2 | -2.38 | 6.62 | -11.22 | 8.67 | 10.27 | False |  | mild_accumulation | 0.03 | -0.02 | 1 | 0 | 0.79 | 1.38 | -5.65 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral | D_降級_TDCC轉弱 | 269.79263095650754 | 63.44502485811813 | 1.39 | 0.63 | 8.5 | 7.2 | 10.59 | 10.59 | False |  | distribution_warning | -0.59 | -0.97 | 0 | 0 | 2.33 | 1.68 | -8.11 | 18 | selected |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | 3.79 | -2.93 | 9.19 | 20.92 | 11.11 | 23.29 | False |  | strong_accumulation | 0.54 | 0.12 | 2 | 2 | 3.04 | 2.4 | -3.67 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth |  | 63.192573671422345 | 28.70134038166515 | 17.42 | 54.01 | 30.4 | 70.16 | 61.18 | 74.75 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 1.92 | 1.08 | 2 | 1 | 31.09 | 25.1 | -2.44 |  | fail_low_response_condition |