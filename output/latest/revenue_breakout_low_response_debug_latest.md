# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-08 19:37:40 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 717880 |
| tdcc_rows | 1966 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 373 |
| tdcc_mild_accumulation_count | 730 |
| tdcc_distribution_warning_count | 658 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 106 |
| already_priced_in_excluded | 44 |
| overheat_pass | 62 |
| score_pass | 61 |
| theme_priority_pass | 53 |
| final_rows | 53 |

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
| fail_low_response_condition | 231 |
| fail_already_priced_in | 44 |
| fail_defensive_or_traditional_excluded | 5 |
| fail_mainstream_score_lt_10 | 3 |
| missing_or_insufficient_price_metrics | 1 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 102.03987961747174 | 127.0977623123372 | -1.37 | 7.46 | -4.42 | -12.2 | 15.02 | 15.02 | False |  | distribution_warning | -1.06 | -0.62 | 0 | 1 | -0.18 | 0.52 | -13.6 | 12 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | 0.38 | 0.19 | -7.27 | -24.2 | 4.81 | 4.81 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | 0.73 | 0.5 | -15.78 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | -0.49 | 0.0 | -12.77 | 20.87 | 8.01 | 23.64 | False |  | distribution_warning | -0.41 | 0.0 | 1 | 0 | -0.41 | -0.91 | -15.98 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -1.71 | 5.02 | 4.07 | 0.0 | 8.49 | 8.49 | False |  | mild_accumulation | 0.93 | 0.29 | 2 | 1 | -2.25 | -0.84 | -6.88 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.85 | -1.11 | -3.78 | -5.82 | 4.4 | 5.01 | False |  | mild_accumulation | 0.05 | 0.0 | 3 | 0 | 0.06 | -0.26 | -11.66 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -1.61 | -3.56 | -14.98 | 0.41 | 3.83 | 10.91 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | -1.09 | -1.61 | -22.29 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 2.54 | -3.41 | -33.57 | -36.4 | 2.54 | 2.54 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.1 | -5.1 | -34.19 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -7.61 | -14.42 | 3.49 | 38.63 | 7.66 | 40.23 | False |  | mild_accumulation | -0.02 | 0.05 | 2 | 1 | -7.23 | -6.05 | -17.34 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -1.0 | -3.19 | -5.84 | -1.0 | 10.18 | 10.18 | False |  | distribution_warning | -0.02 | -0.37 | 1 | 2 | -0.7 | -0.23 | -8.46 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | -7.69 | 22.63 | 57.38 | 84.62 | 62.71 | 88.76 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.74 | 1.27 | 2 | 2 | 0.83 | 3.64 | -10.88 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -12.4 | -2.4 | 6.91 | 71.41 | 30.52 | 80.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.16 | -0.42 | 1 | 2 | -3.55 | -2.03 | -35.0 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 0.0 | 7.4 | 9.25 | 14.83 | 17.74 | 24.24 | False |  | strong_accumulation | 0.35 | 0.49 | 2 | 2 | 0.79 | 1.47 | -7.8 | 20 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -1.77 | 0.0 | -0.89 | 0.91 | 3.74 | 11.0 | False |  | distribution_warning | -0.05 | -0.09 | 2 | 1 | -2.8 | -1.73 | -9.02 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -1.95 | -1.18 | -10.99 | -1.57 | 12.05 | 17.29 | False |  | mild_accumulation | 0.96 | 0.0 | 3 | 0 | -1.93 | -1.1 | -16.33 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -11.52 | 1.66 | 81.19 | 268.24 | 93.21 | 297.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -1.68 | 2 | 0 | -8.64 | -3.13 | -17.0 |  | fail_already_priced_in |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -7.42 | -14.1 | -28.02 |  | 1.16 |  | False |  | distribution_warning | -0.12 | -0.05 | 0 | 1 | -10.1 | -9.2 | -29.19 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | 1.67 | -10.29 | -7.58 | 17.31 | 6.55 | 17.87 | False |  | strong_accumulation | 0.82 | 0.74 | 2 | 2 | -0.63 | -2.84 | -35.62 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -2.58 | 5.98 | 6.35 | 23.19 | 11.46 | 25.36 | False |  | distribution_warning | -0.62 | -2.1 | 0 | 0 | -2.12 | -1.75 | -14.83 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 1.11 | 2.25 | 3.92 | 5.46 | 8.52 | 23.45 | False |  | distribution_warning | -0.02 | -0.04 | 1 | 0 | 1.5 | 1.85 | -9.0 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -5.0 | -9.23 | 20.63 | 128.42 | 27.25 | 143.73 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -1.5 | 1 | 0 | -3.94 | -2.87 | -28.06 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 12.35 | 21.83 | 32.27 | 137.14 | 29.18 | 139.71 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.53 | -1.44 | 1 | 1 | 13.56 | 10.38 | -22.16 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | -5.11 | -8.14 | 1.28 | 54.9 | 24.41 | 70.63 | False |  | distribution_warning | -0.58 | -2.3 | 1 | 0 | -0.96 | -1.22 | -36.42 | 13 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | -1.76 | -4.37 | -3.45 | 28.32 | 11.04 | 34.13 | False |  | distribution_warning | -0.39 | -0.33 | 0 | 0 | -0.17 | -0.06 | -8.71 | 14 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | -0.18 | -8.1 | -33.68 | 124.11 | 24.21 | 133.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.13 | -3.89 | 0 | 0 | -0.77 | -1.98 | -53.52 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | 2.86 | -4.91 | -13.99 | -15.15 | 37.25 | 37.25 | False |  | distribution_warning | -2.88 | -2.48 | 1 | 1 | 0.36 | 1.06 | -34.38 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | 6.82 | 5.62 | 9.3 | 74.88 | 60.68 | 124.34 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.99 | -1.5 | 2 | 2 | 5.19 | 6.75 | -19.49 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 71.68985948774075 | 62.35657344241515 | -11.34 | -8.43 | -16.27 | 24.92 | 6.25 | 30.77 | False |  | mild_accumulation | 0.11 | -0.1 | 2 | 1 | -8.13 | -8.17 | -30.8 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 3.37 | -2.31 | -0.22 | 15.45 | 10.71 | 18.85 | False |  | distribution_warning | -0.37 | -0.53 | 0 | 0 | 1.14 | 0.8 | -9.56 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 1.7 | 1.99 | -1.24 | -8.87 | 7.63 | 7.63 | False |  | mild_accumulation | 0.11 | -0.05 | 2 | 1 | 1.32 | 0.4 | -12.64 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 0.66 | 34.22 | 24.32 | 138.72 | 83.47 | 141.25 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.6 | 6.42 | 3 | 2 | 10.36 | 9.03 | -7.89 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -3.9 | -1.69 | -3.32 | 52.56 | 12.68 | 60.2 | False |  | strong_accumulation | 0.06 | 0.03 | 2 | 2 | -3.47 | -2.48 | -12.93 | 18 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | -4.16 | 15.38 | 23.31 | 71.94 | 52.44 | 77.61 | True | 距60日低點反彈>50%；近120日漲幅>70% | strong_accumulation | 0.45 | 1.39 | 3 | 3 | 1.22 | 3.35 | -6.02 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 11.58 | 8.89 | -1.31 | 49.01 | 30.92 | 54.61 | False |  | mild_accumulation | 0.16 | -0.21 | 2 | 2 | 6.99 | 8.81 | -6.98 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 0.58 | -9.12 | -11.45 | 5.5 | 16.93 | 16.93 | False |  | distribution_warning | -1.0 | -0.73 | 0 | 0 | 0.19 | -0.72 | -31.93 | 11 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | -12.24 | 11.51 | -18.56 | 11.75 | 52.48 | 52.48 | True | 距60日低點反彈>50% | mild_accumulation | -0.02 | 0.87 | 1 | 3 | 1.61 | 1.66 | -23.21 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -1.89 | -5.2 | -6.52 | -3.44 | 14.24 | 14.24 | False |  | distribution_warning | -1.53 | -1.01 | 0 | 1 | -2.06 | -1.85 | -17.6 | 10 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 59.67101651519066 | 49.96169077295545 | -0.56 | 1.85 | 4.39 | 53.55 | 14.42 | 61.17 | False |  | distribution_warning | -1.4 | -0.73 | 1 | 1 | -0.14 | 1.05 | -11.19 | 12 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 131.31830412017854 | 92.66781063949252 | -4.09 | 3.96 | -11.83 | 17.14 | 17.56 | 17.99 | False |  | strong_accumulation | 0.21 | 0.12 | 2 | 2 | -1.25 | -1.24 | -16.54 | 20 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | -5.32 | -3.52 | 10.56 | 91.06 | 35.88 | 105.78 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.47 | 0 | 0 | -6.07 | -2.69 | -17.47 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | -7.59 | -0.61 | 38.9 | 99.09 | 45.03 | 109.57 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.49 | 0 | 1 | -3.37 | -0.89 | -9.63 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -4.17 | -11.67 | -3.86 | 11.78 | 13.9 | 13.9 | False |  | mild_accumulation | 0.28 | 0.7 | 2 | 1 | -5.7 | -3.94 | -12.19 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | -4.09 | -8.26 | -19.47 | 15.3 | 8.21 | 28.5 | False |  | mild_accumulation | 0.1 | -1.29 | 2 | 1 | -2.68 | -2.89 | -27.24 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -5.28 | -15.28 | -31.03 | -24.76 | 0.56 | 0.56 | False |  | distribution_warning | -2.62 | -2.47 | 0 | 0 | -5.91 | -7.01 | -41.46 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | 2.51 | 8.59 | 41.98 | 138.12 | 64.91 | 167.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | -2.37 | 2 | 2 | 3.28 | 6.19 | -6.68 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -0.67 | -19.04 | 3.48 | 26.96 | 2.76 | 43.08 | False |  | strong_accumulation | 0.71 | 1.49 | 2 | 3 | -3.23 | -5.37 | -29.68 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 2.0 | -1.41 | 0.0 | 3.51 | 4.09 | 11.11 | False |  | mild_accumulation | 0.07 | 0.04 | 1 | 1 | 1.19 | 0.96 | -12.36 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 9.59 | 3.9 | -10.11 | -13.04 | 25.0 | 25.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.78 | 4.15 | -14.89 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 233.9341638249008 | 396.6930034235488 | -17.57 | -18.21 | -19.65 | -21.62 | 1.59 | 1.59 | False |  | distribution_warning | -2.21 | -0.56 | 1 | 1 | -17.28 | -16.57 | -22.0 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | -3.05 | 0.0 | -6.38 | 5.15 | 32.41 | 37.17 | False |  | distribution_warning | -0.62 | -1.36 | 1 | 1 | -2.67 | -1.31 | -13.2 | 15 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | -3.44 | -10.37 | -10.94 | 13.54 | 4.07 | 17.33 | False |  | distribution_warning | -0.04 | -0.05 | 2 | 2 | -2.83 | -3.86 | -33.1 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 5.42 | 3.73 | 30.54 | 168.28 | 64.83 | 196.04 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.83 | 2.95 | 1 | 1 | 0.78 | 2.67 | -13.17 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 1.15 | 11.51 | 26.67 | 71.2 | 43.77 | 91.88 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.74 | -2.85 | 2 | 2 | 2.77 | 4.15 | -9.86 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 132.72536273917663 | 87.04889933877817 | -2.24 | 14.66 | 10.51 | 71.59 | 41.86 | 70.87 | True | 近120日漲幅>70% | mild_accumulation | 1.04 | -0.92 | 3 | 1 | 5.54 | 5.35 | -9.23 |  | fail_already_priced_in |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | -6.27 | -4.02 | -2.85 | 44.15 | 18.91 | 47.53 | False |  | mild_accumulation | 0.32 | -1.79 | 1 | 0 | -2.13 | -2.22 | -14.64 | 16 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -6.99 | -7.1 | -38.43 | -48.85 | 23.53 | 23.53 | False |  | mild_accumulation | 0.69 | 0.51 | 3 | 1 | -4.94 | -4.99 | -40.09 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | 0.21 | -3.88 | -9.12 | 2.11 | 2.65 | 2.65 | False |  | mild_accumulation | -0.29 | 0.2 | 2 | 3 | -1.03 | -1.07 | -12.73 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | -5.01 | -7.21 | -28.33 | -1.5 | 15.36 | 15.36 | False |  | strong_accumulation | 0.19 | 0.01 | 2 | 2 | -5.19 | -5.28 | -35.16 | 16 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -0.44 | -0.22 | -15.47 | -3.86 | 4.19 | 4.19 | False |  | mild_accumulation | -0.2 | 0.12 | 1 | 2 | -1.59 | -1.08 | -21.13 | 17 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -1.97 | 10.74 | 8.33 | 5.28 | 16.34 | 23.55 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 1.68 | 2.47 | -4.78 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 2.29 | 3.18 | -2.99 | -5.8 | 5.15 | 9.85 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 2.13 | 1.8 | -11.41 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | -0.42 | 7.07 | 6.12 | 33.8 | 13.71 | 41.54 | False |  | strong_accumulation | 1.25 | 1.5 | 3 | 3 | 0.3 | 1.28 | -2.65 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | 1.03 | -0.64 | -16.65 | -39.92 | 10.16 | 10.16 | False |  | mild_accumulation | -0.6 | 0.27 | 0 | 2 | 0.59 | 0.86 | -17.62 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 0.72 | 2.65 | -9.73 | -3.06 | 9.95 | 9.95 | False |  | mild_accumulation | -0.01 | 0.06 | 1 | 2 | 1.01 | 1.15 | -12.01 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 152.2529369970754 | 60.15647368497227 | -0.2 | -5.59 | -10.27 | -6.92 | 1.43 | 1.53 | False |  | mild_accumulation | -0.14 | 0.13 | 1 | 2 | -1.2 | -1.66 | -15.59 |  | fail_low_response_condition |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 2.62 | 12.37 | 24.97 | 44.05 | 38.56 | 47.3 | False |  | mild_accumulation | 0.42 | -0.02 | 2 | 1 | 4.56 | 5.16 | -9.17 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 7.88 | 2.69 | 13.62 | 52.57 | 16.59 | 56.6 | False |  | distribution_warning | -0.02 | -0.01 | 1 | 0 | 4.94 | 1.24 | -39.52 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | 1.52 | -2.2 | -5.66 | -23.66 | 10.5 | 10.5 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.86 | 1.88 | -10.31 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -13.68 | -16.74 | -8.14 | 20.16 | 10.96 | 21.53 | False |  | mild_accumulation | 1.21 | -0.89 | 3 | 1 | -11.21 | -9.33 | -20.68 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 0.83 | -4.72 | -9.36 | 19.8 | 3.42 | 22.84 | False |  | mild_accumulation | 0.13 | -0.31 | 1 | 1 | -0.62 | -1.7 | -25.77 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 7.18 | 11.59 | 37.56 | 65.83 | 85.4 | 103.06 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.08 | 1 | 1 | 9.12 | 11.06 | -3.55 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -2.4 | 0.0 | -10.96 | 66.12 | 39.61 | 99.02 | True | 距120日低點反彈>80% | distribution_warning | -0.98 | -0.63 | 0 | 1 | -0.1 | 0.24 | -33.66 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | -3.67 | 19.02 | 36.59 | 64.66 | 63.03 | 71.54 | True | 距60日低點反彈>50% | mild_accumulation | -0.28 | 0.56 | 1 | 2 | 2.89 | 4.99 | -8.62 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 73.91966377290892 | 26.75099850600647 | -6.59 | -20.0 | -0.8 | 35.0 | 11.92 | 43.28 | False |  | distribution_warning | -2.54 | -1.49 | 0 | 2 | -6.95 | -6.11 | -25.84 | 11 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -3.56 | -11.51 | -16.93 | 15.8 | 10.27 | 28.45 | False |  | distribution_warning | -0.58 | -0.48 | 0 | 0 | -5.35 | -5.16 | -26.96 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -2.15 | -14.09 | -12.7 | 30.03 | 3.46 | 37.46 | False |  | distribution_warning | -3.17 | -2.2 | 0 | 1 | -5.02 | -4.81 | -27.1 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -3.32 | -13.86 | -17.07 | -21.37 | 5.28 | 5.28 | False |  | distribution_warning | -1.79 | -1.73 | 0 | 0 | -5.01 | -4.67 | -19.87 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | -3.02 | -4.05 | -8.35 | -5.46 | 13.07 | 13.07 | False |  | strong_accumulation | 0.36 | 0.12 | 2 | 2 | -1.5 | -2.17 | -30.77 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.54703093190022 | 34.71282457960092 | -3.78 | 9.63 | -2.62 | 36.34 | 48.01 | 48.01 | False |  | mild_accumulation | 0.06 | -0.76 | 1 | 0 | -0.05 | 2.37 | -19.06 | 18 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -4.59 | -10.45 | -4.59 | 14.53 | 8.87 | 17.39 | False |  | distribution_warning | -0.53 | -1.28 | 0 | 1 | -6.37 | -4.21 | -14.29 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 54.59950544814572 | 34.30071340658413 | -5.11 | -11.56 | -28.77 | 34.72 | 23.52 | 53.62 | False |  | distribution_warning | -0.99 | -1.53 | 0 | 1 | -6.8 | -5.25 | -32.2 | 11 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -2.4 | 18.75 | -16.18 | -20.06 | 26.67 | 26.67 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 6.16 | 4.39 | -17.51 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 12.74 | 37.09 | 82.73 | 151.29 | 76.33 | 162.59 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.16 | 0.76 | 0 | 1 | 18.94 | 15.95 | -27.36 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -3.18 | -4.01 | -34.57 | 80.11 | 46.93 | 85.7 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.23 | 0.11 | 1 | 1 | -1.28 | -2.11 | -54.11 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | -1.16 | 2.4 | -11.17 | 16.72 | 27.61 | 71.0 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 1 | -0.61 | -0.62 | -17.79 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 17.25 | 47.72 | 16.38 | 188.62 | 115.88 | 208.55 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.65 | -6.2 | 0 | 0 | 25.29 | 23.85 | -3.4 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | 8.45 | 8.24 | 32.06 | 157.34 | 57.04 | 206.67 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.14 | -1.57 | 2 | 0 | 1.85 | 6.46 | -11.68 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 60.760461865560174 | 88.15608743643294 | 2.47 | -2.36 | 19.55 | 48.61 | 34.17 | 52.24 | False |  | distribution_warning | -0.81 | -1.08 | 1 | 1 | 0.85 | 1.58 | -9.47 | 14 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 0.0 | 1.08 | 6.06 | 5.66 | 5.66 | 17.65 | False |  | mild_accumulation | 0.14 | 0.01 | 2 | 1 | 0.38 | 0.61 | -1.41 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | -0.58 | 20.28 | 36.07 | 130.12 | 87.72 | 178.5 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -2.6 | 1 | 0 | 4.07 | 7.48 | -8.17 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -15.68 | 11.3 | 14.32 | 101.53 | 59.7 | 122.36 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.4 | 1.95 | 2 | 2 | -6.64 | -4.52 | -19.3 |  | fail_already_priced_in |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | -1.34 | 2.55 | -11.4 | 2.55 | 18.13 | 18.13 | False |  | mild_accumulation | 0.29 | 0.02 | 2 | 1 | -0.56 | 0.37 | -13.14 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | -3.21 | -10.66 | -31.97 | 31.13 | 7.82 | 31.98 | False |  | mild_accumulation | 0.61 | -0.25 | 2 | 1 | -4.1 | -4.21 | -37.7 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | B_可觀察 | 1057.5663716814158 | 435.6709565602183 | 0.56 | 0.22 | -28.92 | -22.43 | 29.84 | 29.84 | False |  | mild_accumulation | -0.09 | 0.16 | 1 | 2 | 0.43 | 0.41 | -35.13 | 21 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | -5.69 | 36.53 | 50.41 | 44.16 | 85.62 | 98.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.45 | 2.36 | 1 | 3 | 2.06 | 5.6 | -8.94 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | -5.73 | 1.9 | -1.83 | 26.33 | 53.23 | 62.5 | True | 距60日低點反彈>50% | mild_accumulation | 0.9 | -0.42 | 1 | 2 | 1.14 | 2.07 | -17.67 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 59.590900789853706 | 37.93424741228517 | -16.41 | -12.05 | -16.23 | 6.03 | 14.84 | 14.84 | False |  | mild_accumulation | -0.62 | 0.28 | 1 | 1 | -10.02 | -9.2 | -24.27 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 3.98 | -16.73 | -0.48 | 15.21 | 7.51 | 20.81 | False |  | distribution_warning | -2.68 | -2.84 | 0 | 0 | -2.73 | -2.74 | -19.92 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -0.9 | -2.83 | -14.87 | -15.59 | 16.36 | 16.36 | False |  | mild_accumulation | 0.15 | -0.68 | 2 | 0 | -2.27 | -1.38 | -17.69 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | -4.53 | 3.69 | -24.02 | -25.81 | 41.34 | 41.34 | False |  | distribution_warning | -0.9 | -0.14 | 1 | 2 | 8.44 | 6.02 | -35.62 | 10 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | -4.44 | 1.7 | 29.33 | 3.86 | 31.06 | 35.86 | False |  | strong_accumulation | 0.25 | 0.25 | 2 | 2 | -0.13 | 0.94 | -4.95 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 2.17 | 7.78 | 16.58 | 96.25 | 45.37 | 97.9 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.87 | 0.28 | 2 | 2 | 7.13 | 6.59 | -8.72 |  | fail_already_priced_in |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | -2.65 | -1.34 | -11.99 | -11.84 | 5.98 | 5.98 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -1.51 | -1.64 | -17.1 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -4.2 | -6.06 | -32.43 | -4.09 | 19.51 | 19.51 | False |  | mild_accumulation | -0.86 | 0.91 | 1 | 2 | -4.17 | -3.87 | -37.33 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 1.82 | 12.67 | 10.68 | 13.69 | 34.0 | 34.0 | False |  | mild_accumulation | 0.12 | 1.75 | 1 | 2 | 5.36 | 5.26 | -4.74 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 128.94577120992216 | 58.42418198682172 | -4.41 | -8.8 | -11.35 | 55.46 | 9.04 | 79.14 | False |  | distribution_warning | -0.42 | -0.86 | 1 | 0 | -5.11 | -4.8 | -20.25 | 16 | selected |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -2.14 | -3.52 | -22.6 | -25.14 | 4.18 | 4.18 | False |  | mild_accumulation | 0.08 | 0.3 | 2 | 1 | -3.4 | -3.81 | -28.27 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -16.37 | -18.6 | -22.74 | -38.05 | 7.2 | 7.2 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -13.29 | -12.47 | -27.23 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | -6.36 | 2.82 | -14.43 | 20.85 | 41.67 | 41.67 | False |  | mild_accumulation | -0.44 | 0.22 | 2 | 2 | 3.17 | 2.66 | -16.39 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 1.63 | 2.19 | 3.12 | 9.57 | 43.48 | 43.48 | False |  | distribution_warning | -6.9 | -5.13 | 1 | 1 | 2.73 | 3.91 | -3.77 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | -3.08 | 18.09 | -4.16 | -13.72 | 64.76 | 64.76 | True | 距60日低點反彈>50% | distribution_warning | -0.95 | -2.3 | 1 | 1 | 5.99 | 5.86 | -11.05 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -6.8 | -11.32 | -24.34 | -12.1 | 20.36 | 20.36 | False |  | distribution_warning | -0.86 | -0.05 | 1 | 2 | -5.49 | -6.33 | -48.68 | 15 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | -1.85 | -3.88 | -2.36 | 34.78 | 7.83 | 36.26 | False |  | mild_accumulation | 0.78 | 0.0 | 3 | 0 | -1.91 | -1.68 | -7.0 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -4.67 | -19.32 | -13.83 | -4.3 | 0.27 | 0.27 | False |  | distribution_warning | -6.07 | -4.62 | 0 | 1 | -5.28 | -6.53 | -22.63 | 11 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 1.92 | -2.3 | -20.5 | -7.29 | 3.58 | 3.58 | False |  | distribution_warning | -0.12 | -0.35 | 1 | 0 | 0.66 | -0.2 | -21.48 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 1.6 | 0.68 | -0.45 | -11.73 | 4.47 | 8.56 | False |  | distribution_warning | 0.0 | -0.02 | 1 | 0 | 0.63 | 0.21 | -7.11 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 0.0 | -2.44 | -8.99 | -0.26 | 1.34 | 4.4 | False |  | mild_accumulation | 0.25 | -0.18 | 2 | 1 | -2.09 | -1.69 | -13.26 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 63.192573671422345 | 28.70134038166515 | -6.9 | 13.81 | 18.04 | 34.44 | 38.2 | 40.38 | False |  | strong_accumulation | 1.71 | 4.54 | 2 | 3 | -4.98 | -0.83 | -16.35 | 18 | selected |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28027764281582 | 68.36543520376344 | -3.64 | -8.62 | -7.83 | 24.08 | 17.22 | 44.64 | False |  | distribution_warning | -1.46 | -0.26 | 1 | 1 | -3.37 | -2.93 | -24.82 | 12 | selected |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 79.49201833634949 | 23.814868308479223 | -14.83 | 42.57 | 54.13 | 111.11 | 78.34 | 158.64 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.38 | -0.77 | 2 | 2 | 3.49 | 3.65 | -17.53 |  | fail_already_priced_in |