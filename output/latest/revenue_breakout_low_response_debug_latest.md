# 營收爆發低反應股 Debug Report

- 產生時間：`2026-09-07 19:36:07 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1968 |
| standardized_revenue_rows | 1968 |
| price_rows | 715922 |
| tdcc_rows | 1966 |
| tdcc_trend_rows | 1971 |
| tdcc_strong_accumulation_count | 373 |
| tdcc_mild_accumulation_count | 730 |
| tdcc_distribution_warning_count | 658 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 337 |
| low_response_pass | 99 |
| already_priced_in_excluded | 35 |
| overheat_pass | 64 |
| score_pass | 64 |
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
| fail_low_response_condition | 238 |
| fail_already_priced_in | 35 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1316 | 上曜 | 建材營造 | neutral | D_降級_TDCC轉弱 | 102.03987961747174 | 127.0977623123372 | -1.83 | 6.97 | -0.46 | -15.35 | 14.48 | 14.48 | False |  | distribution_warning | -1.06 | -0.62 | 0 | 1 | -0.3 | 0.1 | -14.0 | 12 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 138.88341543513957 | 35.55748013706368 | -2.67 | -2.85 | -9.24 | -27.0 | 2.4 | 2.4 | False |  | distribution_warning | -0.06 | 0.0 | 1 | 0 | -1.57 | -1.76 | -17.71 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 76.92275445022611 | 34.13578403052163 | 0.0 | 0.0 | -3.27 | 20.35 | 9.06 | 24.85 | False |  | distribution_warning | -0.41 | 0.0 | 1 | 0 | 0.56 | -0.02 | -15.16 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 74.24763542562339 | 44.20247547874825 | -1.69 | 5.45 | 4.98 | -0.85 | 9.43 | 9.43 | False |  | mild_accumulation | 0.93 | 0.29 | 2 | 1 | -1.17 | -0.05 | -6.07 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 4533.333333333333 | 19.461581604038138 | 0.56 | -1.11 | -4.55 | -4.29 | 4.69 | 5.31 | False |  | mild_accumulation | 0.05 | 0.0 | 3 | 0 | 0.28 | -0.0 | -11.41 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 133.64130708423545 | 46.4144468904606 | -2.41 | -5.81 | -14.74 | -10.0 | 3.4 | 10.45 | False |  | strong_accumulation | 0.11 | 0.2 | 2 | 3 | -1.68 | -2.16 | -22.61 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 59.83901715738191 | 37.77158897509007 | 1.03 | 1.72 | -32.8 | -33.86 | 6.88 | 6.88 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.2 | -1.53 | -31.4 |  | fail_low_response_condition |
| 1590 | 亞德客-KY | 電機機械 | cyclical_turnaround |  | 50.77907738303081 | 32.86722140693869 | -3.86 | -12.74 | 8.3 | 39.65 | 10.48 | 44.82 | False |  | mild_accumulation | -0.02 | 0.05 | 2 | 1 | -5.53 | -4.11 | -15.17 |  | fail_low_response_condition |
| 1618 | 合機 | 電器電纜 | neutral |  | 187.03179652280383 | 2.596548930575971 | -2.0 | -2.96 | -6.76 | -3.68 | 9.62 | 9.62 | False |  | distribution_warning | -0.02 | -0.37 | 1 | 2 | -1.37 | -0.76 | -8.92 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 83.29046508535268 | 14.900753417875832 | 2.24 | 25.27 | 64.03 | 87.91 | 65.62 | 92.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.74 | 1.27 | 2 | 2 | 3.59 | 5.84 | -9.28 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 77.38272254543362 | 61.22417624717493 | -2.66 | -1.2 | 14.24 | 69.94 | 32.13 | 82.37 | True | 距120日低點反彈>80% | distribution_warning | -0.16 | -0.42 | 1 | 2 | -2.48 | -1.01 | -34.2 |  | fail_already_priced_in |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 3460.154507547597 | 13488.270126747157 | 0.44 | 2.7 | 9.78 | 11.56 | 15.71 | 22.1 | False |  | strong_accumulation | 0.35 | 0.49 | 2 | 2 | -0.6 | -0.14 | -9.39 | 19 | selected |
| 1906 | 寶隆 | 造紙工業 | cyclical_turnaround |  | 102.2043908305958 | 8.652108071387124 | -1.32 | 1.36 | 1.36 | 0.0 | 4.67 | 12.0 | False |  | distribution_warning | -0.05 | -0.09 | 2 | 1 | -1.93 | -1.0 | -8.2 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 200.77620698853028 | 144.7342420065355 | -2.73 | -3.11 | -10.43 | 7.33 | 11.16 | 16.36 | False |  | mild_accumulation | 0.96 | 0.0 | 3 | 0 | -2.77 | -1.99 | -17.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 355.5224648845101 | 136.58175926893418 | -1.94 | 16.8 | 117.27 | 308.37 | 114.58 | 341.43 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.17 | -1.68 | 2 | 0 | 1.54 | 7.28 | -7.82 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 105.65363257145547 | 68.55793117306851 | -6.71 | -14.29 | -27.47 |  | 0.0 |  | False |  | distribution_warning | -0.12 | -0.05 | 0 | 1 | -10.08 | -9.26 | -28.65 |  | fail_low_response_condition |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 64.73928453588496 | 29.88903942819763 | -1.23 | -12.41 | -10.45 | 11.11 | 4.8 | 18.81 | False |  | strong_accumulation | 0.82 | 0.74 | 2 | 2 | -2.81 | -4.68 | -36.68 |  | fail_low_response_condition |
| 2237 | 華德動能-創 | 汽車工業 | neutral |  | 73.35258797598237 | 131.59608434402784 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 59.3766932093304 | 49.48723608161035 | -3.51 | -2.58 | 9.03 | 21.29 | 11.65 | 25.57 | False |  | distribution_warning | -0.62 | -2.1 | 0 | 0 | -1.68 | -1.74 | -14.69 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 113.29418903483725 | -9.863285617040727 | 1.29 | 4.3 | 1.45 | 1.94 | 7.33 | 22.09 | False |  | distribution_warning | -0.02 | -0.04 | 1 | 0 | 0.49 | 0.9 | -10.0 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth |  | 81.16244941521768 | 30.46615999681673 | -1.93 | 1.88 | 37.46 | 129.71 | 31.81 | 152.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.78 | -1.5 | 1 | 0 | -0.98 | 0.35 | -25.47 |  | fail_already_priced_in |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 197.79519679786523 | 96.81655256765252 | 11.15 | 14.97 | 46.17 | 124.92 | 46.17 | 141.16 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.53 | -1.44 | 1 | 1 | 15.42 | 12.1 | -21.69 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 74.43152295785818 | 37.52324493334001 | -0.31 | -2.75 | 3.58 | 40.71 | 25.2 | 71.71 | False |  | distribution_warning | -0.58 | -2.3 | 1 | 0 | -0.76 | -0.7 | -36.02 | 13 | selected |
| 2317 | 鴻海 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 54.18913901503827 | 37.89396256372083 | 2.4 | -3.21 | -0.97 | 26.11 | 13.02 | 36.53 | False |  | distribution_warning | -0.39 | -0.33 | 0 | 0 | 1.39 | 1.72 | -7.08 | 15 | selected |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 51.51220682363353 | 32.51567318341994 | 8.07 | 2.79 | -30.05 | 117.34 | 29.03 | 142.39 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.13 | -3.89 | 0 | 0 | 2.63 | 1.64 | -51.72 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 180.47957329305424 | 137.8339123232017 | -1.19 | -6.74 | -11.07 | -22.19 | 35.62 | 35.62 | False |  | distribution_warning | -2.88 | -2.48 | 1 | 1 | -1.09 | -0.04 | -35.16 | 17 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 291.54754061439485 | 160.96925915473923 | -1.37 | 0.28 | 15.02 | 63.64 | 53.85 | 114.8 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.99 | -1.5 | 2 | 2 | 1.0 | 2.84 | -22.91 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 71.68985948774075 | 62.35657344241515 | 3.19 | -3.0 | -7.69 | 30.43 | 14.13 | 40.47 | False |  | mild_accumulation | 0.11 | -0.1 | 2 | 1 | -1.73 | -2.09 | -25.66 | 17 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 126.87926937028048 | 84.53540417540658 | 2.64 | -2.83 | -1.65 | 15.52 | 11.21 | 19.39 | False |  | distribution_warning | -0.37 | -0.53 | 0 | 0 | 1.47 | 1.33 | -9.16 | 20 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 982.241841810558 | 50.88044442559491 | 0.85 | 0.14 | -1.93 | -13.06 | 6.59 | 6.59 | False |  | mild_accumulation | 0.11 | -0.05 | 2 | 1 | 0.43 | -0.54 | -13.49 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 54.00455967585946 | 28.507334791082425 | 0.43 | 38.58 | 29.72 | 154.08 | 88.31 | 166.25 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 4.6 | 6.42 | 3 | 2 | 14.88 | 12.83 | -5.47 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 65.7284615063187 | 40.78203539212061 | -0.9 | 0.15 | 1.07 | 54.44 | 16.37 | 65.46 | False |  | strong_accumulation | 0.06 | 0.03 | 2 | 2 | -0.38 | 0.5 | -10.07 | 19 | selected |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth |  | 53.325092938625424 | 40.87924777938564 | 0.0 | 22.13 | 27.42 | 71.65 | 57.32 | 83.3 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.45 | 1.39 | 3 | 3 | 5.17 | 6.99 | -3.01 |  | fail_already_priced_in |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 175.25829018155406 | 101.53000922739209 | 13.78 | 9.85 | 1.83 | 40.69 | 28.9 | 52.22 | False |  | mild_accumulation | 0.16 | -0.21 | 2 | 2 | 5.8 | 7.99 | -8.42 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 72.07351671395091 | 95.02794974786696 | 2.74 | -2.78 | -6.91 | 3.75 | 18.51 | 18.51 | False |  | distribution_warning | -1.0 | -0.73 | 0 | 0 | 1.04 | 0.56 | -31.01 | 13 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 77.38084589596791 | 70.28827013710922 | -3.86 | 20.95 | -16.73 | 13.36 | 58.87 | 58.87 | True | 距60日低點反彈>50% | mild_accumulation | -0.02 | 0.87 | 1 | 3 | 6.42 | 6.07 | -22.76 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 64.11079364944591 | 53.35864647704091 | -1.75 | -6.77 | -5.86 | -3.98 | 14.41 | 14.41 | False |  | distribution_warning | -1.53 | -1.01 | 0 | 1 | -2.18 | -1.87 | -17.48 | 12 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 59.67101651519066 | 49.96169077295545 | 1.82 | 4.29 | 7.21 | 46.68 | 16.83 | 64.56 | False |  | distribution_warning | -1.4 | -0.73 | 1 | 1 | 2.05 | 3.27 | -9.33 | 13 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 131.31830412017854 | 92.66781063949252 | 2.66 | 10.85 | -6.08 | 22.57 | 24.55 | 26.13 | False |  | strong_accumulation | 0.21 | 0.12 | 2 | 2 | 4.82 | 4.52 | -11.58 | 23 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 129.40232272458806 | 89.40002899909717 | 0.18 | 3.88 | 7.85 | 95.55 | 39.82 | 111.75 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -1.47 | 0 | 0 | -3.51 | -0.11 | -15.07 |  | fail_already_priced_in |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 87.57814496890177 | 40.26417268738088 | 0.44 | 1.95 | 46.55 | 97.67 | 50.11 | 116.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.49 | 0 | 1 | -0.01 | 2.49 | -6.46 |  | fail_already_priced_in |
| 2397 | 友通 | 電腦及週邊設備業 | mainstream_growth |  | 51.27260225910742 | 29.156178289401137 | -1.75 | -8.97 | -0.48 | 13.16 | 17.9 | 17.9 | False |  | mild_accumulation | 0.28 | 0.7 | 2 | 1 | -2.99 | -0.92 | -9.1 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 63.77094494612451 | 73.90317152093164 | 1.89 | -6.09 | -9.62 | 16.13 | 10.77 | 31.55 | False |  | mild_accumulation | 0.1 | -1.29 | 2 | 1 | -0.8 | -0.85 | -25.52 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 66.12807071299159 | 119.8943795149513 | -2.85 | -14.71 | -30.84 | -26.45 | 1.87 | 1.87 | False |  | distribution_warning | -2.62 | -2.47 | 0 | 0 | -5.49 | -6.4 | -40.7 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 719.6141344528174 | 660.8671990662033 | -4.79 | 2.99 | 52.06 | 120.94 | 60.56 | 160.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.92 | -2.37 | 2 | 2 | 0.97 | 3.98 | -9.14 |  | fail_already_priced_in |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 143.60115573754808 | 120.8168984897956 | -0.27 | -24.72 | 2.33 | 21.7 | 3.9 | 43.46 | False |  | strong_accumulation | 0.71 | 1.49 | 2 | 3 | -4.06 | -5.57 | -29.49 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 87.10340000229498 | 57.86622628978438 | 1.64 | -1.41 | -1.76 | -1.41 | 3.72 | 10.71 | False |  | mild_accumulation | 0.07 | 0.04 | 1 | 1 | 0.76 | 0.69 | -12.68 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 185.56636984883 | 60.8421170876004 | 14.88 | 19.14 | -7.33 | -10.13 | 30.31 | 30.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 10.49 | 8.98 | -11.28 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 233.9341638249008 | 396.6930034235488 | 0.78 | -1.02 | -1.52 | -6.04 | 3.73 | 8.66 | False |  | distribution_warning | -2.21 | -0.56 | 1 | 1 | -0.05 | 0.23 | -4.89 | 16 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 307.65627206955537 | 402.6798478136839 | -1.7 | -2.03 | -0.86 | -4.14 | 34.03 | 38.85 | False |  | distribution_warning | -0.62 | -1.36 | 1 | 1 | -1.48 | -0.22 | -12.14 | 15 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 71.21615201900238 | 63.75066762905661 | 0.35 | -10.53 | -7.33 | 10.06 | 5.37 | 18.79 | False |  | distribution_warning | -0.04 | -0.05 | 2 | 2 | -2.17 | -3.01 | -32.26 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 62.10044461308143 | 25.64051311355484 | 12.78 | 12.78 | 42.96 | 172.48 | 72.03 | 208.98 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.83 | 2.95 | 1 | 1 | 5.37 | 7.42 | -9.38 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 280.87664000910723 | 176.72380227122633 | 9.04 | 9.51 | 35.05 | 63.22 | 52.08 | 102.97 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.74 | -2.85 | 2 | 2 | 9.29 | 10.59 | -4.65 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 132.72536273917663 | 87.04889933877817 | 0.98 | 12.55 | 14.21 | 68.44 | 43.95 | 78.39 | False |  | mild_accumulation | 1.04 | -0.92 | 3 | 1 | 7.82 | 7.43 | -7.89 | 23 | selected |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 54.39975818511566 | 39.61008944759205 | -2.79 | -3.17 | 2.52 | 45.24 | 21.39 | 52.12 | False |  | mild_accumulation | 0.32 | -1.79 | 1 | 0 | -0.29 | -0.38 | -12.86 | 16 | selected |
| 2485 | 兆赫 | 通信網路業 | mainstream_growth | A_優先追蹤 | 133.3640235641089 | 87.69992405929172 | -4.8 | -7.5 | -37.19 | -44.93 | 26.01 | 26.01 | False |  | mild_accumulation | 0.69 | 0.51 | 3 | 1 | -3.39 | -3.52 | -40.93 | 21 | selected |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 58.17656481955196 | 24.989635542053016 | 0.41 | -1.91 | -7.94 | 1.14 | 3.4 | 4.06 | False |  | mild_accumulation | -0.29 | 0.2 | 2 | 3 | -0.51 | -0.45 | -12.09 |  | fail_low_response_condition |
| 2495 | 普安 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 64.23716177695917 | 46.433166006608985 | -2.48 | -4.1 | -24.67 | -4.83 | 19.68 | 19.68 | False |  | strong_accumulation | 0.19 | 0.01 | 2 | 2 | -2.0 | -2.2 | -32.73 | 17 | selected |
| 2501 | 國建 | 建材營造 | neutral | B_可觀察 | 119.67349677675224 | 35.30940543476948 | -0.22 | 0.45 | -13.4 | -6.5 | 3.72 | 3.72 | False |  | mild_accumulation | -0.2 | 0.12 | 1 | 2 | -2.04 | -1.62 | -21.48 | 17 | selected |
| 2509 | 全坤建 | 建材營造 | neutral |  | 5220.181215031936 | 686.3996752630304 | -3.25 | 9.16 | 8.36 | 2.05 | 15.95 | 23.14 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 1.85 | 2.35 | -5.1 |  | fail_low_response_condition |
| 2524 | 京城 | 建材營造 | neutral |  | 226.1951960114829 | -38.34673100470893 | 2.73 | 4.23 | -0.56 | -8.93 | 5.15 | 9.85 | False |  | mild_accumulation | 0.04 | 0.04 | 1 | 1 | 2.29 | 1.97 | -11.41 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 196.58747366830235 | 404.2807368960456 | 2.89 | 8.23 | 5.84 | 31.51 | 14.42 | 42.43 | False |  | strong_accumulation | 1.25 | 1.5 | 3 | 3 | 1.27 | 2.04 | -2.04 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 93.8248443457034 | 60.82046311316634 | -2.89 | -0.64 | -17.41 | -40.9 | 9.03 | 9.03 | False |  | mild_accumulation | -0.6 | 0.27 | 0 | 2 | -0.48 | -0.1 | -18.8 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 456.7784314365824 | -10.633771552003529 | 0.73 | 4.07 | -9.33 | -5.87 | 9.0 | 9.0 | False |  | mild_accumulation | -0.01 | 0.06 | 1 | 2 | 0.27 | 0.38 | -12.77 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | B_可觀察 | 152.2529369970754 | 60.15647368497227 | -0.1 | -7.44 | -9.55 | -9.13 | 1.32 | 1.43 | False |  | mild_accumulation | -0.14 | 0.13 | 1 | 2 | -1.58 | -1.91 | -15.68 | 21 | selected |
| 2637 | 慧洋-KY | 航運業 | cyclical_turnaround | B_可觀察 | 56.21501385482998 | 35.673950917357274 | 5.42 | 12.6 | 26.69 | 41.11 | 40.11 | 48.95 | False |  | mild_accumulation | 0.42 | -0.02 | 2 | 1 | 6.34 | 6.85 | -8.15 | 17 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 75.30202631326227 | 151.74496933087312 | 11.98 | -1.63 | 16.31 | 47.28 | 18.34 | 58.94 | False |  | distribution_warning | -0.02 | -0.01 | 1 | 0 | 6.66 | 2.87 | -38.62 |  | fail_low_response_condition |
| 2939 | 永邑-KY | 貿易百貨 | defensive_or_traditional |  | 105.39537539252068 | -2.7456603682258485 | -0.25 | 0.77 | -8.78 | -25.33 | 9.12 | 9.12 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.47 | 0.78 | -11.43 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 92.98747396520872 | 39.79375890103884 | -14.49 | -14.12 | -11.94 | 16.37 | 11.53 | 22.15 | False |  | mild_accumulation | 1.21 | -0.89 | 3 | 1 | -11.54 | -9.63 | -20.27 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 53.03493307821629 | 37.31355708857018 | 1.27 | -5.14 | -9.09 | 15.94 | 2.56 | 21.83 | False |  | mild_accumulation | 0.13 | -0.31 | 1 | 1 | -1.68 | -2.66 | -26.38 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 491.0617601014743 | 281.4805917941651 | 1.54 | 7.8 | 45.23 | 51.92 | 84.47 | 102.04 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.49 | -1.08 | 1 | 1 | 9.19 | 11.63 | -4.04 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 51.43199102826286 | 31.32232745558509 | -2.43 | -6.07 | -3.37 | 60.8 | 38.24 | 97.06 | True | 距120日低點反彈>80% | distribution_warning | -0.98 | -0.63 | 0 | 1 | -1.08 | -0.73 | -34.31 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 57.39113833331852 | 80.33836073352812 | -0.15 | 23.69 | 46.47 | 66.83 | 69.73 | 78.59 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.28 | 0.56 | 1 | 2 | 8.01 | 9.8 | -4.87 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 73.91966377290892 | 26.75099850600647 | 1.33 | -19.03 | 6.15 | 33.58 | 18.52 | 51.74 | False |  | distribution_warning | -2.54 | -1.49 | 0 | 2 | -2.59 | -1.11 | -21.46 | 10 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 117.5894936306649 | 96.80997008021892 | -2.01 | -7.45 | -14.56 | 16.97 | 12.21 | 30.72 | False |  | distribution_warning | -0.58 | -0.48 | 0 | 0 | -4.27 | -3.93 | -25.67 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 78.71068980000454 | 32.99031345898157 | -2.92 | -12.36 | -12.98 | 20.98 | 3.35 | 37.3 | False |  | distribution_warning | -3.17 | -2.2 | 0 | 1 | -5.86 | -5.33 | -27.19 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 94.8509470404764 | 111.03077976261774 | -1.79 | -15.94 | -17.2 | -24.21 | 6.94 | 6.94 | False |  | distribution_warning | -1.79 | -1.73 | 0 | 0 | -4.24 | -3.58 | -19.79 | 13 | selected |
| 3041 | 揚智 | 半導體業 | mainstream_growth |  | 270.5877639328499 | 61.05386791096055 | 1.33 | -6.72 | -5.57 | -2.35 | 15.08 | 15.08 | False |  | strong_accumulation | 0.36 | 0.12 | 2 | 2 | 0.04 | -0.63 | -29.54 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 56.54703093190022 | 34.71282457960092 | -0.7 | 22.79 | 1.86 | 35.81 | 50.76 | 50.76 | True | 距60日低點反彈>50% | mild_accumulation | 0.06 | -0.76 | 1 | 0 | 2.26 | 4.49 | -17.56 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 51.65320953731184 | 24.998384730686325 | -3.72 | -7.95 | -2.16 | 12.51 | 9.68 | 18.26 | False |  | distribution_warning | -0.53 | -1.28 | 0 | 1 | -6.19 | -3.86 | -13.65 |  | fail_low_response_condition |
| 3048 | 益登 | 電子通路業 | mainstream_growth |  | 54.59950544814572 | 34.30071340658413 | -2.55 | -6.63 | -28.67 | 33.08 | 27.08 | 58.05 | False |  | distribution_warning | -0.99 | -1.53 | 0 | 1 | -4.69 | -2.98 | -31.32 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 92.36088424262223 | 446.47665446270986 | -0.17 | 19.54 | -13.99 | -27.02 | 28.44 | 28.44 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 8.55 | 6.28 | -16.35 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 173.49468713105077 | 0.1393314176711153 | 11.62 | 18.5 | 69.18 | 124.54 | 68.34 | 141.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -2.16 | 0.76 | 0 | 1 | 11.36 | 8.38 | -33.08 |  | fail_low_response_condition |
| 3090 | 日電貿 | 電子零組件業 | mainstream_growth |  | 66.62056943729836 | 28.751184145266706 | -2.0 | 6.52 | -26.39 | 79.96 | 50.44 | 90.13 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.23 | 0.11 | 1 | 1 | 0.87 | 0.03 | -53.01 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 204.3244857198993 | 247.3095962162866 | -5.21 | 6.13 | -10.36 | 10.19 | 29.1 | 73.0 | False |  | distribution_warning | -0.82 | -0.04 | 0 | 1 | 0.67 | 0.48 | -16.83 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 152.87141417726988 | 131.80340994633235 | 11.21 | 34.81 | 4.25 | 155.94 | 103.22 | 190.46 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.65 | -6.2 | 0 | 0 | 20.38 | 19.17 | -8.4 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 76.76510854684139 | 60.63179487179488 | -5.24 | -0.59 | 18.92 | 159.49 | 43.95 | 181.11 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.14 | -1.57 | 2 | 0 | -6.27 | -1.83 | -19.04 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 60.760461865560174 | 88.15608743643294 | 10.67 | 2.07 | 29.18 | 51.54 | 41.73 | 60.82 | False |  | distribution_warning | -0.81 | -1.08 | 1 | 1 | 6.4 | 7.46 | -4.37 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 163.0981490537797 | 66.06004491276559 | 1.81 | 1.44 | 5.64 | 4.85 | 7.25 | 18.07 | False |  | mild_accumulation | 0.14 | 0.01 | 2 | 1 | 0.79 | 1.03 | -1.06 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 59.23071292224356 | 63.75000065335939 | -2.23 | -4.78 | -21.79 | 5.29 | 21.8 | 21.8 | False |  | distribution_warning | -1.8 | -2.54 | 0 | 0 | -1.57 | -1.68 | -26.76 | 12 | selected |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 158.38135946958366 | 102.54848095176932 | -2.7 | 31.02 | 44.58 | 124.39 | 86.93 | 177.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.03 | -2.6 | 1 | 0 | 4.55 | 7.76 | -8.55 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 98.00183615933965 | 20.292463997787955 | -9.44 | 11.64 | 29.28 | 104.9 | 77.27 | 146.84 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.4 | 1.95 | 2 | 2 | 4.12 | 5.56 | -10.41 |  | fail_low_response_condition |
| 3515 | 華擎 | 電腦及週邊設備業 | mainstream_growth |  | 131.34606716091966 | 18.855891461759168 | 3.82 | 7.19 | -5.13 | 6.7 | 23.2 | 23.2 | False |  | mild_accumulation | 0.29 | 0.02 | 2 | 1 | 3.83 | 4.71 | -9.41 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 62.596694973543904 | 81.12682822174246 | 0.97 | -7.88 | -29.06 | 33.01 | 10.08 | 35.84 | False |  | mild_accumulation | 0.61 | -0.25 | 2 | 1 | -2.66 | -2.58 | -36.4 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | A_優先追蹤 | 1057.5663716814158 | 435.6709565602183 | 3.53 | 0.78 | -26.69 | -26.69 | 32.31 | 32.31 | False |  | mild_accumulation | -0.09 | 0.16 | 1 | 2 | 2.35 | 2.36 | -33.89 | 23 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 90.95964446430736 | 35.954090570618135 | -5.59 | 36.76 | 56.22 | 46.88 | 89.13 | 101.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.45 | 2.36 | 1 | 3 | 5.43 | 8.15 | -7.22 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 181.7841084291265 | -13.777157023400417 | -0.86 | 6.32 | -0.49 | 19.7 | 53.61 | 62.9 | True | 距60日低點反彈>50% | mild_accumulation | 0.9 | -0.42 | 1 | 2 | 1.48 | 2.51 | -17.47 |  | fail_already_priced_in |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth | A_優先追蹤 | 59.590900789853706 | 37.93424741228517 | -4.61 | -5.48 | -4.17 | 20.35 | 22.85 | 22.85 | False |  | mild_accumulation | -0.62 | 0.28 | 1 | 1 | -4.33 | -3.67 | -18.98 | 17 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.83318057075236 | 59.917707856465086 | 5.42 | -19.23 | -3.23 | 14.88 | 8.02 | 21.39 | False |  | distribution_warning | -2.68 | -2.84 | 0 | 0 | -3.21 | -2.52 | -19.54 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 100.18023971882604 | 8.191084809072704 | -2.83 | -2.35 | -15.95 | -18.36 | 16.36 | 16.36 | False |  | mild_accumulation | 0.15 | -0.68 | 2 | 0 | -2.41 | -1.5 | -17.69 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 69.6507119471058 | 40.90376378051168 | -0.83 | -4.78 | -28.01 | -33.05 | 33.52 | 33.52 | False |  | distribution_warning | -0.9 | -0.14 | 1 | 2 | 2.64 | 0.7 | -39.19 | 13 | selected |
| 4119 | 旭富 | 生技醫療業 | defensive_or_traditional |  | 133.15573369830872 | 3.17390085984396 | -1.44 | 4.0 | 29.08 | 4.4 | 33.01 | 37.88 | False |  | strong_accumulation | 0.25 | 0.25 | 2 | 2 | 1.44 | 2.53 | -3.53 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 60.139921179772095 | 49.66910611953541 | 14.09 | 9.05 | 25.7 | 108.44 | 52.47 | 115.72 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.87 | 0.28 | 2 | 2 | 12.8 | 12.46 | -4.26 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 83.88246111409087 | 32.050889025137955 | 0.0 | -0.38 | -8.6 | -11.84 | 7.42 | 7.42 | False |  | distribution_warning | -0.03 | -0.03 | 0 | 0 | -0.24 | -0.45 | -15.97 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 128.9172485640275 | 121.34662298357856 | -5.61 | -5.17 | -33.2 | -0.36 | 20.09 | 20.09 | False |  | mild_accumulation | -0.86 | 0.91 | 1 | 2 | -4.0 | -3.74 | -37.02 |  | fail_low_response_condition |
| 4912 | 聯德控股-KY | 電子零組件業 | mainstream_growth |  | 66.35391853670312 | 30.54000053488904 | 3.66 | 13.59 | 11.96 | 12.21 | 36.0 | 36.0 | False |  | mild_accumulation | 0.12 | 1.75 | 1 | 2 | 7.57 | 7.34 | -3.32 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 128.94577120992216 | 58.42418198682172 | -2.8 | -6.63 | -15.2 | 57.89 | 11.1 | 82.52 | True | 距120日低點反彈>80% | distribution_warning | -0.42 | -0.86 | 1 | 0 | -3.76 | -3.43 | -19.42 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 163.87219234419487 | 157.8817851681957 | -3.89 | -5.23 | -19.05 | -28.04 | 3.42 | 3.42 | False |  | mild_accumulation | 0.08 | 0.3 | 2 | 1 | -4.28 | -4.84 | -28.8 |  | fail_low_response_condition |
| 4943 | 康控-KY | 電子零組件業 | mainstream_growth |  | 62.11924102043407 | 47.22036969390274 | -17.17 | -24.28 | -26.47 | -41.5 | 1.23 | 1.23 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -18.92 | -18.27 | -31.5 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 98.63908131175776 | 47.622431626136766 | 0.65 | 6.48 | -14.22 | 16.97 | 42.96 | 42.96 | False |  | mild_accumulation | -0.44 | 0.22 | 2 | 2 | 4.26 | 3.85 | -17.61 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 98.74936839745938 | 71.28591290526819 | 0.54 | -1.07 | 0.0 | 6.12 | 41.94 | 41.94 | False |  | distribution_warning | -6.9 | -5.13 | 1 | 1 | 1.74 | 3.17 | -4.8 | 16 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 136.6326290773289 | -1.350919909057194 | 2.57 | 24.22 | 3.46 | -6.51 | 70.95 | 70.95 | True | 距60日低點反彈>50% | distribution_warning | -0.95 | -2.3 | 1 | 1 | 10.87 | 10.43 | -7.71 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 105.41523454519049 | 68.91539282131619 | -4.48 | -8.44 | -21.37 | -16.94 | 23.35 | 23.35 | False |  | distribution_warning | -0.86 | -0.05 | 1 | 2 | -3.72 | -4.55 | -47.4 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 52.80833066831479 | 32.26889490668114 | 2.41 | -3.29 | 0.0 | 34.51 | 10.72 | 40.44 | False |  | mild_accumulation | 0.78 | 0.0 | 3 | 0 | 0.53 | 0.81 | -5.45 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 51.30291899664847 | 56.85528675042054 | -2.46 | -19.55 | -12.54 | -4.8 | 1.21 | 1.21 | False |  | distribution_warning | -6.07 | -4.62 | 0 | 1 | -4.05 | -4.8 | -20.74 | 12 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 189.242108725136 | 453.301755044666 | 2.59 | -2.76 | -20.88 | -10.85 | 3.09 | 3.09 | False |  | distribution_warning | -0.12 | -0.35 | 1 | 0 | 0.06 | -0.69 | -23.09 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1384.2565409555764 | 1413.0648908269566 | 1.37 | 0.91 | 0.68 | -14.09 | 4.71 | 8.8 | False |  | distribution_warning | 0.0 | -0.02 | 1 | 0 | 0.9 | 0.45 | -6.9 |  | fail_low_response_condition |
| 5534 | 長虹 | 建材營造 | neutral |  | 269.79263095650754 | 63.44502485811813 | 0.27 | -3.45 | -7.8 | -1.82 | 0.93 | 3.99 | False |  | mild_accumulation | 0.25 | -0.18 | 2 | 1 | -2.6 | -2.23 | -13.6 |  | fail_low_response_condition |
| 6024 | 群益期 | 金融保險業 | defensive_or_traditional |  | 81.00240598588135 | -15.228327071752355 | -0.94 | 1.29 | 4.14 | 13.54 | 10.35 | 17.35 | False |  | strong_accumulation | 0.17 | 0.37 | 2 | 2 | 1.24 | 0.93 | -3.82 |  | fail_low_response_condition |
| 6108 | 競國 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 63.192573671422345 | 28.70134038166515 | -3.77 | 22.73 | 25.75 | 35.4 | 42.55 | 44.79 | False |  | strong_accumulation | 1.71 | 4.54 | 2 | 3 | -1.42 | 2.21 | -13.72 | 19 | selected |