# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-09 19:36:47 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 719842 |
| tdcc_rows | 1966 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 373 |
| tdcc_mild_accumulation_count | 730 |
| tdcc_distribution_warning_count | 658 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 101 |
| already_priced_in_excluded | 36 |
| overheat_pass | 65 |
| score_pass | 65 |
| theme_priority_pass | 59 |
| final_rows | 59 |

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
| fail_low_response_condition | 236 |
| fail_already_priced_in | 36 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 1 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 102.03987961747174 | 127.0977623123372 | 3.7 | 9.27 | 2.28 | -8.94 | 19.28 | 19.28 | False |  | distribution_warning | -1.06 | -0.62 | 0 | 1 | 3.06 | 3.88 | -10.4 | 11 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -0.38 | 0.0 | -9.88 | -24.2 | 4.21 | 4.21 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | 0.15 | -0.07 | -16.26 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -0.98 | -1.46 | -12.12 | 19.69 | 6.95 | 22.44 | False |  | distribution_warning | -0.41 | 0.0 | 1 | 0 | -1.31 | -1.72 | -16.12 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -2.14 | 0.44 | 0.88 | 0.44 | 8.02 | 8.02 | False |  | mild_accumulation | 0.93 | 0.29 | 2 | 1 | -2.7 | -1.16 | -7.29 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | -0.57 | -2.77 | -5.65 | -7.63 | 2.93 | 3.54 | False |  | mild_accumulation | 0.05 | 0.0 | 3 | 0 | -1.21 | -1.52 | -12.9 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | 0.0 | -2.77 | -13.38 | 2.5 | 4.68 | 11.82 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | -0.14 | -0.74 | -21.66 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | -4.12 | -9.42 | -35.12 | -37.3 | 1.09 | 1.09 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.99 | -5.93 | -35.12 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround | B_可觀察 | 50.77907738303081 | 32.86722140693869 | -4.66 | -16.61 | 1.53 | 39.56 | 7.26 | 37.11 | False |  | mild_accumulation | -0.02 | 0.05 | 2 | 1 | -6.72 | -5.9 | -17.65 | 13 | selected |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -1.26 | -4.96 | -7.42 | -2.12 | 9.62 | 9.62 | False |  | distribution_warning | -0.02 | -0.37 | 1 | 2 | -0.95 | -0.68 | -8.92 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 1.71 | 27.14 | 68.32 | 96.69 | 72.4 | 100.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.74 | 1.27 | 2 | 2 | 5.62 | 8.91 | -5.57 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -3.17 | -3.45 | 0.6 | 79.1 | 34.94 | 86.25 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.16 | -0.42 | 1 | 2 | -0.1 | 1.18 | -32.8 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | -0.99 | 7.18 | 7.67 | 15.27 | 18.58 | 25.13 | False |  | strong_accumulation | 0.35 | 0.49 | 2 | 2 | 1.17 | 2.01 | -7.14 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -0.89 | -8.26 | -1.77 | 2.78 | 3.74 | 11.0 | False |  | distribution_warning | -0.05 | -0.09 | 2 | 1 | -2.37 | -1.59 | -9.02 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -2.33 | -0.79 | -16.33 | 5.02 | 12.05 | 17.29 | False |  | mild_accumulation | 0.96 | 0.0 | 3 | 0 | -1.9 | -1.01 | -16.33 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -10.57 | 2.95 | 78.16 | 252.27 | 91.36 | 293.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -1.68 | 2 | 0 | -9.63 | -3.74 | -17.8 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -4.32 | -11.92 | -26.52 |  | 2.7 |  | False |  | distribution_warning | -0.12 | -0.05 | 0 | 1 | -8.17 | -7.21 | -28.11 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 3.39 | -6.15 | -8.61 | 15.64 | 6.55 | 15.64 | False |  | strong_accumulation | 0.82 | 0.74 | 2 | 2 | -0.31 | -2.61 | -35.62 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -3.05 | 6.91 | 6.54 | 23.82 | 11.46 | 25.36 | False |  | distribution_warning | -0.62 | -2.1 | 0 | 0 | -2.43 | -1.61 | -14.83 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 2.58 | -0.47 | -0.47 | 5.65 | 8.35 | 23.26 | False |  | distribution_warning | -0.02 | -0.04 | 1 | 0 | 1.36 | 1.55 | -9.14 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -1.75 | -7.79 | 10.53 | 128.26 | 27.85 | 144.9 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -1.5 | 1 | 0 | -3.09 | -2.21 | -27.71 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 16.47 | 25.9 | 26.81 | 142.21 | 36.19 | 142.21 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.53 | -1.44 | 1 | 1 | 18.26 | 14.8 | -17.94 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | -0.31 | -0.31 | -6.12 | 61.0 | 26.77 | 73.87 | False |  | distribution_warning | -0.58 | -2.3 | 1 | 0 | 0.94 | 0.61 | -35.21 | 14 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 0.4 | -6.67 | -5.79 | 29.23 | 11.26 | 34.4 | False |  | distribution_warning | -0.39 | -0.33 | 0 | 0 | 0.39 | 0.13 | -8.53 | 15 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 4.63 | -6.15 | -39.89 | 125.55 | 23.77 | 132.51 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.13 | -3.89 | 0 | 0 | -0.8 | -2.14 | -53.69 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 2.85 | -7.33 | -20.44 | -7.33 | 37.8 | 37.8 | False |  | distribution_warning | -2.88 | -2.48 | 1 | 1 | 1.16 | 1.34 | -34.11 | 18 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 2.23 | 3.39 | -3.17 | 83.92 | 56.41 | 118.38 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.99 | -1.5 | 2 | 2 | 2.22 | 3.57 | -21.63 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 71.68985948774075 | 62.35657344241515 | -5.84 | -9.03 | -17.08 | 31.27 | 9.51 | 34.78 | False |  | mild_accumulation | 0.11 | -0.1 | 2 | 1 | -4.86 | -4.93 | -28.67 | 17 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 1.37 | -3.28 | -2.32 | 12.01 | 10.34 | 18.45 | False |  | distribution_warning | -0.37 | -0.53 | 0 | 0 | 0.97 | 0.42 | -9.87 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.14 | 0.85 | -1.93 | -9.53 | 6.59 | 6.59 | False |  | mild_accumulation | 0.11 | -0.05 | 2 | 1 | 0.29 | -0.53 | -13.49 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 3.71 | 38.08 | 29.08 | 131.71 | 91.53 | 151.86 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.6 | 6.42 | 3 | 2 | 13.41 | 12.53 | -3.85 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -3.45 | -6.81 | -4.17 | 52.19 | 13.2 | 60.95 | False |  | strong_accumulation | 0.06 | 0.03 | 2 | 2 | -2.67 | -1.86 | -12.52 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | -3.07 | 14.91 | 23.61 | 73.27 | 54.17 | 79.63 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.45 | 1.39 | 3 | 3 | 1.7 | 4.14 | -4.95 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 18.23 | 6.38 | 3.09 | 57.77 | 34.97 | 59.39 | False |  | mild_accumulation | 0.16 | -0.21 | 2 | 2 | 9.93 | 11.04 | -6.22 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 3.14 | -5.05 | -14.19 | 7.57 | 18.74 | 18.74 | False |  | distribution_warning | -1.0 | -0.73 | 0 | 0 | 2.02 | 0.75 | -30.88 | 11 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | -6.38 | 10.0 | -16.67 | 23.87 | 56.03 | 56.03 | True | 距60日低點反彈>50% | mild_accumulation | -0.02 | 0.87 | 1 | 3 | 3.49 | 3.67 | -21.43 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -3.42 | -5.31 | -9.97 | -2.73 | 14.75 | 14.75 | False |  | distribution_warning | -1.53 | -1.01 | 0 | 1 | -1.36 | -1.3 | -17.24 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 59.67101651519066 | 49.96169077295545 | -3.32 | -6.92 | 0.0 | 48.72 | 12.02 | 57.79 | False |  | distribution_warning | -1.4 | -0.73 | 1 | 1 | -1.88 | -0.98 | -13.06 | 11 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 1.48 | 5.07 | -7.57 | 21.49 | 22.58 | 23.02 | False |  | strong_accumulation | 0.21 | 0.12 | 2 | 2 | 2.71 | 2.72 | -12.98 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -1.29 | -6.2 | 6.86 | 100.19 | 36.77 | 107.13 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.47 | 0 | 0 | -5.16 | -1.89 | -16.92 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -5.64 | -4.81 | 34.64 | 97.88 | 44.15 | 108.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.49 | 0 | 1 | -3.72 | -1.37 | -10.18 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -4.77 | -10.19 | -4.62 | 10.11 | 14.1 | 14.1 | False |  | mild_accumulation | 0.28 | 0.7 | 2 | 1 | -5.03 | -3.48 | -12.04 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 63.77094494612451 | 73.90317152093164 | 3.9 | -6.17 | -22.83 | 13.9 | 9.23 | 29.72 | False |  | mild_accumulation | 0.1 | -1.29 | 2 | 1 | -1.43 | -1.81 | -26.55 | 17 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -1.97 | -13.59 | -28.5 | -19.56 | 2.24 | 2.24 | False |  | distribution_warning | -2.62 | -2.47 | 0 | 0 | -3.61 | -5.03 | -40.48 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 0.97 | 8.39 | 32.24 | 141.57 | 62.42 | 163.48 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | -2.37 | 2 | 2 | 1.32 | 4.19 | -8.08 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -0.4 | -10.5 | -2.22 | 27.33 | 3.59 | 44.23 | False |  | strong_accumulation | 0.71 | 1.49 | 2 | 3 | -1.89 | -4.24 | -29.11 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 0.55 | -2.98 | -2.47 | 1.84 | 2.79 | 9.72 | False |  | mild_accumulation | 0.07 | 0.04 | 1 | 1 | 0.08 | -0.27 | -13.46 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 1.75 | 8.51 | -7.69 | -6.64 | 27.5 | 27.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 7.44 | 5.68 | -13.19 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | -16.88 | -18.37 | -19.19 | -21.76 | 1.91 | 1.91 | False |  | distribution_warning | -2.21 | -0.56 | 1 | 1 | -16.24 | -15.16 | -21.76 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | -3.04 | -2.38 | -7.26 | 13.64 | 33.1 | 37.89 | False |  | distribution_warning | -0.62 | -1.36 | 1 | 1 | -2.04 | -0.73 | -12.75 | 15 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 8.61 | 0.32 | -10.95 | 26.12 | 14.44 | 28.22 | False |  | distribution_warning | -0.04 | -0.05 | 2 | 2 | 6.84 | 5.21 | -26.43 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | -2.23 | 0.51 | 20.8 | 174.31 | 67.37 | 200.61 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.83 | 2.95 | 1 | 1 | 2.31 | 3.89 | -11.83 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | -8.48 | 0.63 | 15.78 | 76.65 | 42.58 | 90.3 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -2.85 | 2 | 2 | 1.89 | 3.01 | -10.6 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | -4.6 | 5.25 | 0.87 | 57.88 | 35.12 | 52.89 | False |  | mild_accumulation | 1.04 | -0.92 | 3 | 1 | 0.27 | 0.31 | -13.54 | 22 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 54.39975818511566 | 39.61008944759205 | -4.38 | -6.25 | -6.25 | 43.54 | 19.4 | 48.15 | False |  | mild_accumulation | 0.32 | -1.79 | 1 | 0 | -1.4 | -1.67 | -14.29 |  | fail_low_response_condition |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -3.9 | -7.61 | -36.19 | -45.94 | 25.85 | 25.85 | False |  | mild_accumulation | 0.69 | 0.51 | 3 | 1 | -2.77 | -2.94 | -37.46 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | -0.1 | -4.27 | -9.81 | 1.26 | 2.44 | 2.44 | False |  | mild_accumulation | -0.29 | 0.2 | 2 | 3 | -1.02 | -1.17 | -12.91 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth |  | 64.23716177695917 | 46.433166006608985 | -2.89 | -7.51 | -26.83 | 1.93 | 18.24 | 18.24 | False |  | strong_accumulation | 0.19 | 0.01 | 2 | 2 | -2.44 | -2.68 | -33.54 |  | fail_low_response_condition |
| 2501 | 國建 | 建材營造 | neutral |  | 119.67349677675224 | 35.30940543476948 | -0.44 | -3.24 | -17.04 | -5.08 | 4.19 | 4.19 | False |  | mild_accumulation | -0.2 | 0.12 | 1 | 2 | -1.43 | -0.99 | -21.13 |  | fail_low_response_condition |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -0.34 | 9.23 | 8.42 | 4.23 | 15.18 | 22.31 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 0.24 | 1.32 | -5.73 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 2.77 | 1.73 | -4.73 | -6.0 | 3.83 | 8.46 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 0.76 | 0.47 | -12.53 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 0.52 | 7.59 | 6.05 | 35.58 | 14.9 | 43.03 | False |  | strong_accumulation | 1.25 | 1.5 | 3 | 3 | 0.99 | 2.14 | -1.63 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 2.87 | -3.9 | -15.81 | -37.56 | 11.14 | 11.14 | False |  | mild_accumulation | -0.6 | 0.27 | 0 | 2 | 1.7 | 1.61 | -16.88 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 1.02 | -1.0 | -10.13 | -4.68 | 9.32 | 9.32 | False |  | mild_accumulation | -0.01 | 0.06 | 1 | 2 | 0.48 | 0.52 | -12.52 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | 0.6 | -0.5 | -8.64 | -6.94 | 2.34 | 2.45 | False |  | mild_accumulation | -0.14 | 0.13 | 1 | 2 | -0.28 | -0.71 | -14.83 | 21 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 4.36 | 14.2 | 26.89 | 45.02 | 41.95 | 50.9 | False |  | mild_accumulation | 0.42 | -0.02 | 2 | 1 | 6.41 | 7.05 | -6.94 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 15.59 | 2.02 | 8.38 | 57.06 | 21.4 | 63.05 | False |  | distribution_warning | -0.02 | -0.01 | 1 | 0 | 9.15 | 4.93 | -37.03 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | -0.51 | -1.01 | -8.37 | -25.94 | 8.84 | 8.84 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.38 | 0.33 | -11.66 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -12.35 | -14.49 | -6.14 | 17.79 | 12.67 | 23.4 | False |  | mild_accumulation | 1.21 | -0.89 | 3 | 1 | -9.15 | -7.33 | -19.46 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 2.08 | -2.78 | -11.23 | 19.51 | 4.7 | 24.37 | False |  | mild_accumulation | 0.13 | -0.31 | 1 | 1 | 0.76 | -0.44 | -24.85 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 8.88 | 11.86 | 37.75 | 89.2 | 90.37 | 108.5 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.08 | 1 | 1 | 11.38 | 12.72 | -1.45 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | 0.0 | -3.85 | -20.0 | 64.74 | 37.55 | 96.08 | True | 距120日低點反彈>80% | distribution_warning | -0.98 | -0.63 | 0 | 1 | -1.38 | -1.14 | -34.64 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | 2.11 | 16.15 | 40.25 | 73.78 | 67.74 | 73.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | -0.28 | 0.56 | 1 | 2 | 5.09 | 7.3 | -5.98 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 73.91966377290892 | 26.75099850600647 | -5.2 | -18.77 | 0.47 | 36.68 | 11.01 | 42.12 | False |  | distribution_warning | -2.54 | -1.49 | 0 | 2 | -6.71 | -6.33 | -26.44 | 11 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -6.06 | -11.05 | -18.1 | 16.54 | 9.73 | 27.84 | False |  | distribution_warning | -0.58 | -0.48 | 0 | 0 | -5.25 | -5.17 | -27.32 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -6.27 | -16.8 | -15.62 | 26.24 | 1.33 | 32.86 | False |  | distribution_warning | -3.17 | -2.2 | 0 | 1 | -7.34 | -7.38 | -29.55 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | 2.41 | -11.95 | -15.27 | -17.46 | 6.39 | 6.39 | False |  | distribution_warning | -1.79 | -1.73 | 0 | 0 | -3.38 | -3.37 | -18.68 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | -3.57 | -2.13 | -15.0 | -0.65 | 15.33 | 15.33 | False |  | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 0.58 | -0.2 | -29.38 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | 1.39 | 4.84 | -2.12 | 49.27 | 55.66 | 55.66 | True | 距60日低點反彈>50% | mild_accumulation | 0.06 | -0.76 | 1 | 0 | 4.86 | 6.97 | -14.88 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -3.2 | -12.68 | -5.56 | 15.38 | 9.68 | 18.26 | False |  | distribution_warning | -0.53 | -1.28 | 0 | 1 | -5.03 | -3.21 | -13.65 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -4.44 | -13.57 | -29.8 | 36.33 | 22.57 | 52.44 | False |  | distribution_warning | -0.99 | -1.53 | 0 | 1 | -6.84 | -5.51 | -31.66 | 11 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | 1.25 | 17.68 | -15.33 | -11.37 | 26.44 | 26.44 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 5.13 | 3.84 | -17.54 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 5.28 | 27.78 | 79.9 | 160.45 | 79.69 | 168.88 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.16 | 0.76 | 0 | 1 | 20.2 | 16.9 | -25.62 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -1.48 | -2.64 | -41.03 | 81.82 | 45.61 | 83.83 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.23 | 0.11 | 1 | 1 | -2.04 | -2.75 | -54.52 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | -3.41 | 2.72 | -13.04 | 28.79 | 26.87 | 70.0 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 1 | -1.32 | -1.1 | -18.27 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 16.28 | 33.93 | 7.27 | 183.91 | 107.13 | 170.27 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.65 | -6.2 | 0 | 0 | 18.41 | 16.99 | -7.31 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 18.55 | 8.59 | 32.1 | 177.8 | 72.69 | 237.22 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.14 | -1.57 | 2 | 0 | 11.51 | 15.43 | -2.88 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 1.89 | -2.33 | 17.03 | 46.51 | 35.97 | 54.29 | False |  | distribution_warning | -0.81 | -1.08 | 1 | 1 | 2.33 | 2.69 | -8.25 | 14 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 0.72 | 0.36 | 4.48 | 6.06 | 5.66 | 17.65 | False |  | mild_accumulation | 0.14 | 0.01 | 2 | 1 | 0.36 | 0.56 | -1.41 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 59.23071292224356 | 63.75000065335939 | -6.7 | -9.91 | -27.43 | 4.5 | 16.24 | 16.24 | False |  | distribution_warning | -1.8 | -2.54 | 0 | 0 | -5.19 | -5.17 | -30.1 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | 0.51 | 15.5 | 23.05 | 136.53 | 86.61 | 176.87 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -2.6 | 1 | 0 | 2.75 | 6.24 | -8.71 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -13.62 | 2.56 | 2.56 | 102.33 | 57.58 | 119.41 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.4 | 1.95 | 2 | 2 | -7.99 | -5.33 | -20.37 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | -1.31 | 0.45 | -8.15 | 5.87 | 20.27 | 20.27 | False |  | mild_accumulation | 0.29 | 0.02 | 2 | 1 | 1.21 | 1.99 | -10.87 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -2.67 | -6.27 | -35.62 | 35.44 | 11.01 | 35.44 | False |  | mild_accumulation | 0.61 | -0.25 | 2 | 1 | -0.95 | -1.27 | -35.12 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 1057.5663716814158 | 435.6709565602183 | 1.24 | -3.14 | -30.54 | -23.42 | 30.42 | 30.42 | False |  | mild_accumulation | -0.09 | 0.16 | 1 | 2 | 1.04 | 0.79 | -34.84 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | -0.17 | 28.86 | 50.2 | 45.82 | 92.64 | 105.71 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.45 | 2.36 | 1 | 3 | 4.68 | 8.72 | -5.5 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 181.7841084291265 | -13.777157023400417 | -7.02 | -3.7 | -8.12 | 25.56 | 48.48 | 57.46 | False |  | mild_accumulation | 0.9 | -0.42 | 1 | 2 | -1.82 | -1.01 | -20.22 | 19 | selected |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -8.99 | -8.35 | -12.8 | 11.58 | 17.21 | 17.21 | False |  | mild_accumulation | -0.62 | 0.28 | 1 | 1 | -7.77 | -6.76 | -22.7 | 16 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 2.94 | -14.29 | -2.33 | 15.77 | 8.02 | 21.39 | False |  | distribution_warning | -2.68 | -2.84 | 0 | 0 | -1.46 | -2.09 | -19.54 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -1.88 | -4.71 | -16.72 | -16.02 | 15.77 | 15.77 | False |  | mild_accumulation | 0.15 | -0.68 | 2 | 0 | -2.52 | -1.72 | -18.1 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 69.6507119471058 | 40.90376378051168 | 8.43 | 14.41 | -20.12 | -18.92 | 50.84 | 50.84 | True | 距60日低點反彈>50% | distribution_warning | -0.9 | -0.14 | 1 | 2 | 14.89 | 11.91 | -31.3 |  | fail_low_response_condition |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | 3.22 | 4.72 | 36.89 | 10.54 | 37.71 | 45.71 | False |  | strong_accumulation | 0.25 | 0.25 | 2 | 2 | 6.85 | 7.52 | -1.2 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 0.83 | 7.49 | 13.49 | 105.04 | 50.62 | 102.49 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.87 | 0.28 | 2 | 2 | 10.57 | 9.48 | -5.43 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -2.66 | -3.02 | -13.34 | -12.31 | 5.77 | 5.77 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -1.55 | -1.68 | -17.26 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -9.13 | -10.8 | -36.65 | -10.7 | 12.95 | 12.95 | False |  | mild_accumulation | -0.86 | 0.91 | 1 | 2 | -8.93 | -8.44 | -39.38 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | -5.34 | 2.96 | 6.91 | 8.45 | 30.0 | 30.0 | False |  | mild_accumulation | 0.12 | 1.75 | 1 | 2 | 2.07 | 1.94 | -7.58 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -4.48 | -6.8 | -3.52 | 60.54 | 9.84 | 80.45 | True | 距120日低點反彈>80% | distribution_warning | -0.42 | -0.86 | 1 | 0 | -4.08 | -3.77 | -19.67 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -1.77 | -2.46 | -22.56 | -21.47 | 5.7 | 5.7 | False |  | mild_accumulation | 0.08 | 0.3 | 2 | 1 | -1.87 | -2.21 | -27.23 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -7.72 | -10.99 | -19.63 | -37.69 | 11.64 | 11.64 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -9.19 | -8.16 | -24.22 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | -6.56 | 9.86 | -12.71 | 26.07 | 42.41 | 42.41 | False |  | mild_accumulation | -0.44 | 0.22 | 2 | 2 | 3.23 | 2.92 | -15.96 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 1.26 | 0.72 | 1.62 | 12.15 | 43.99 | 43.99 | False |  | distribution_warning | -6.9 | -5.13 | 1 | 1 | 3.06 | 3.91 | -3.43 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | -3.4 | 10.71 | -5.28 | -7.84 | 62.38 | 62.38 | True | 距60日低點反彈>50% | distribution_warning | -0.95 | -2.3 | 1 | 1 | 3.93 | 3.96 | -12.34 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -3.61 | -10.87 | -23.89 | -7.52 | 22.75 | 22.75 | False |  | distribution_warning | -0.86 | -0.05 | 1 | 2 | -3.04 | -4.11 | -47.66 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -4.7 | -4.95 | 0.0 | 32.25 | 5.8 | 33.21 | False |  | mild_accumulation | 0.78 | 0.0 | 3 | 0 | -3.52 | -3.25 | -8.75 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -4.95 | -11.41 | -15.61 | -4.07 | 0.27 | 0.27 | False |  | distribution_warning | -6.07 | -4.62 | 0 | 1 | -5.35 | -6.61 | -23.16 | 11 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 0.47 | 0.79 | -18.28 | -9.03 | 3.42 | 3.42 | False |  | distribution_warning | -0.12 | -0.35 | 1 | 0 | 0.46 | -0.33 | -18.59 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 0.91 | 2.07 | -0.45 | -12.25 | 4.47 | 8.56 | False |  | distribution_warning | 0.0 | -0.02 | 1 | 0 | 0.53 | 0.19 | -7.11 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | -0.66 | -3.19 | -8.01 | 0.13 | 1.2 | 4.26 | False |  | mild_accumulation | 0.25 | -0.18 | 2 | 1 | -2.06 | -1.67 | -13.37 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | -3.18 | -0.81 | -1.46 | 11.54 | 6.84 | 13.62 | False |  | strong_accumulation | 0.17 | 0.37 | 2 | 2 | -1.91 | -1.96 | -6.88 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 63.192573671422345 | 28.70134038166515 | -2.3 | 17.04 | 19.44 | 42.38 | 45.03 | 47.32 | False |  | strong_accumulation | 1.71 | 4.54 | 2 | 3 | -1.0 | 3.72 | -12.22 | 19 | selected |