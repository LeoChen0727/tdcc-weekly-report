# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-09 19:41:01 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 784533 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 48 |
| already_priced_in_excluded | 10 |
| overheat_pass | 38 |
| score_pass | 38 |
| theme_priority_pass | 32 |
| final_rows | 32 |

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
| fail_revenue_condition | 1636 |
| fail_low_response_condition | 288 |
| fail_already_priced_in | 10 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -12.62 | -16.24 | 42.16 | 225.5 | 52.46 | 216.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -11.57 | -6.2 | -24.96 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround |  | 96.8052734253821 | 30.286775373992953 | -6.83 | -13.95 | 8.82 | 24.52 | 12.12 | 29.76 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -13.16 | -9.39 | -32.2 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | -8.68 | -9.57 | -6.87 | -11.7 | 5.41 | 5.41 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -8.35 | -7.79 | -25.12 | 13 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -5.56 | -8.11 | -9.51 | -12.34 | 5.78 | 5.78 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -4.93 | -4.8 | -13.61 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 7.37 | 6.69 | -1.16 | -2.3 | 10.15 | 10.15 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 5.91 | 4.44 | -6.93 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 32.47 | 51.48 | 63.18 | 61.71 | 63.93 | 69.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 31.43 | 30.67 | 0.0 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | 0.0 | -3.76 | -0.83 | 0.0 | 4.37 | 5.6 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -1.02 | -0.51 | -8.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.23 | -0.92 | -4.01 | 4.36 | 2.86 | 10.51 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.4 | -0.43 | -8.69 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | -0.69 | -0.86 | 5.47 | 13.56 | 5.28 | 24.03 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 0.36 | 0.18 | -5.25 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -3.42 | -5.58 | -8.96 | -17.8 | 3.67 | 3.67 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -3.77 | -3.23 | -10.25 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -4.35 | -14.06 | -14.73 | -10.2 | 9.45 | 9.45 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -8.26 | -6.71 | -17.6 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | -5.05 | 39.26 | 26.17 | -13.56 | 46.3 | 46.3 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 6.29 | 4.77 | -28.65 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -4.24 | -1.52 | -4.42 | -5.12 | 2.77 | 2.77 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -3.41 | -3.23 | -14.36 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -17.54 | -23.79 | -25.84 | -35.38 | 6.76 | 8.33 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -19.12 | -16.86 | -32.62 |  | fail_low_response_condition |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -10.45 | -12.65 | -17.61 | -10.79 | 6.6 | 6.6 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -11.27 | -9.4 | -21.78 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -2.94 | -7.37 | -14.21 | -18.97 | 7.35 | 7.35 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -5.88 | -4.59 | -14.21 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.779802186364 | 14769.518174623092 | -12.54 | -4.02 | -6.9 | 6.34 | 0.49 | 10.7 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | -9.94 | -8.43 | -17.86 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -10.93 | -18.52 | -14.4 | -5.58 | 6.8 | 6.8 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -14.16 | -11.98 | -26.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -14.97 | -32.06 | -32.72 | 78.0 | 11.25 | 73.94 | True | 近120日漲幅>70% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -16.17 | -17.93 | -46.9 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -9.21 | -20.69 | -32.79 | -40.69 | 0.98 | 0.98 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -14.02 | -13.15 | -34.49 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -3.67 | -7.39 | -19.68 | -10.41 | 5.35 | 5.35 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -5.4 | -4.77 | -20.83 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -2.29 | -21.44 | 15.52 | 124.4 | 20.1 | 123.87 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -12.01 | -7.96 | -24.35 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -6.43 | -8.09 | -5.96 | 6.17 | 5.38 | 5.38 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -5.33 | -5.1 | -12.48 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -10.83 | -23.85 | 54.39 | 170.18 | 74.51 | 166.96 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -17.06 | -12.26 | -39.96 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -4.08 | -13.54 | -6.09 | 2.29 | 10.64 | 10.64 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -6.22 | -5.33 | -13.71 | 10 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -13.41 | -29.41 | -37.6 | -40.92 | 16.02 | 16.02 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -15.71 | -15.46 | -42.35 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -18.21 | -26.18 | -26.18 | 14.72 | 15.22 | 16.74 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -14.96 | -14.3 | -31.35 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -13.0 | -30.27 | -35.1 | -40.34 | 12.85 | 12.85 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -20.59 | -17.53 | -41.09 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth |  | 158.6674544463884 | 97.96095815091336 | -14.18 | -16.22 | -11.75 | -3.11 | 0.87 | 1.0 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -16.29 | -13.68 | -22.02 |  | fail_low_response_condition |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -6.82 | -9.07 | -9.7 | -7.09 | 5.07 | 5.07 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -7.04 | -6.48 | -18.73 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -23.68 | -37.16 | -18.69 | -23.89 | 3.79 | 10.48 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -27.2 | -25.7 | -46.69 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -6.71 | -4.3 | -15.76 | 8.17 | 12.32 | 12.32 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | -5.18 | -5.11 | -24.35 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -27.11 | -47.92 | -38.42 | -39.47 | 5.04 | 5.04 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -33.11 | -30.51 | -51.17 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -15.66 | -28.19 | -3.46 | -27.61 | 14.32 | 26.81 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -19.09 | -15.05 | -31.76 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 125.4495058048851 | 63.1715973040828 | -8.84 | -15.32 | -11.44 | 2.48 | 9.75 | 9.75 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -9.77 | -8.88 | -23.01 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -6.76 | -11.49 | -5.42 | 2.24 | 9.01 | 9.01 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -6.32 | -6.27 | -15.65 | 11 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -13.5 | -31.6 | -23.06 | -7.39 | 10.3 | 10.3 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -17.56 | -15.0 | -37.09 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -10.99 | -20.46 | -12.59 | 25.38 | 8.57 | 29.84 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -12.61 | -11.11 | -22.68 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | 5.8 | -2.59 | -5.79 | 0.17 | 16.44 | 16.44 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | 2.82 | 2.74 | -7.81 | 11 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -18.95 | -28.02 | -26.29 | 34.55 | 14.2 | 32.14 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -16.03 | -15.38 | -34.97 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -9.46 | -22.81 | -42.99 | -13.48 | 9.28 | 9.28 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -13.07 | -12.76 | -42.17 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -1.78 | -2.65 | -2.65 | 6.99 | 3.57 | 6.99 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -2.3 | -1.53 | -7.86 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -8.09 | -11.66 | -2.57 | -21.25 | 3.96 | 6.56 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -8.8 | -8.37 | -25.87 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 290.42308535778307 | 369.98990000276115 | -16.14 | -16.72 | -19.12 | -22.78 | 4.14 | 10.65 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -12.69 | -12.23 | -27.47 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -10.17 | -12.97 | -16.67 | -14.52 | 6.0 | 6.0 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -11.55 | -9.4 | -21.25 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | -9.17 | -23.06 | -17.5 | 19.28 | 13.79 | 25.85 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -12.27 | -11.44 | -33.71 |  | fail_low_response_condition |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | -13.55 | 81.99 | 238.31 | 601.92 | 275.86 | 718.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 19.7 | 23.42 | -18.28 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -26.11 | -45.78 | -43.91 | -44.31 | 9.01 | 9.01 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -32.34 | -30.17 | -52.02 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -11.56 | -26.69 | -23.49 | -15.44 | 12.62 | 12.62 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -15.49 | -13.35 | -28.33 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -8.01 | -0.6 | 7.77 | 13.65 | 9.18 | 15.22 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | -7.56 | -4.69 | -15.48 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -17.57 | -33.54 | -31.55 | -38.18 | 11.15 | 11.15 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -19.97 | -19.1 | -48.13 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -20.22 | -33.64 | 3.84 | 17.36 | 13.15 | 43.07 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -22.72 | -17.32 | -34.18 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -3.41 | 0.0 | -6.08 | -4.76 | 4.29 | 4.29 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -3.18 | -2.23 | -7.61 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -12.25 | -17.36 | -11.97 | 26.97 | 10.7 | 26.78 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -12.17 | -9.72 | -21.39 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -4.15 | -9.64 | -12.54 | -15.73 | 2.39 | 2.39 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -6.1 | -5.77 | -15.25 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -2.76 | -9.64 | -2.54 | -20.77 | 3.77 | 3.77 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.66 | -4.82 | -18.43 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -2.82 | -2.45 | -14.66 | -13.39 | 3.7 | 3.7 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -3.62 | -4.33 | -22.76 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -5.74 | -7.83 | -5.88 | -16.47 | 4.0 | 4.0 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -6.29 | -5.53 | -13.81 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -3.35 | -4.55 | -14.05 | -7.6 | 3.12 | 3.12 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -4.56 | -4.0 | -13.64 | 16 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround |  | 60.11419447583549 | 41.76866714526904 | -9.44 | -13.52 | -4.38 | 5.15 | 5.68 | 10.47 | False |  | distribution_warning | -0.18 | -0.54 | 2 | 2 | -9.37 | -8.08 | -19.26 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -5.23 | 2.33 | 8.07 | 18.92 | 12.41 | 21.74 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | -4.05 | -1.54 | -16.53 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -10.46 | -4.04 | 22.29 | 31.94 | 24.42 | 39.69 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -8.55 | -6.9 | -20.45 | 15 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | -4.67 | -3.85 | 2.43 | 4.01 | 6.48 | 8.36 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -4.52 | -3.61 | -14.58 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -1.75 | -2.49 | -5.54 | -2.97 | 4.81 | 4.81 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -1.74 | -1.58 | -10.5 | 13 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | -3.41 | 19.41 | 2.72 | 37.71 | 25.78 | 39.41 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 5.08 | 2.92 | -18.68 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -8.46 | -18.63 | -30.71 | -19.32 | 9.17 | 9.17 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -11.08 | -10.65 | -35.68 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | -6.67 | -1.65 | -5.93 | -3.25 | 4.39 | 4.39 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | -2.44 | -2.34 | -8.46 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 470.2347504677583 | 343.911329000345 | -12.64 | -15.71 | -17.24 | 2.47 | 18.13 | 41.61 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -7.14 | -8.19 | -28.53 | 16 | selected |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -16.08 | -45.13 | 0.0 | 1.9 | 13.95 | 47.18 | False |  | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -24.14 | -19.31 | -45.27 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -16.55 | -20.51 | -36.19 | 5.87 | 1.41 | 4.95 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -16.98 | -15.86 | -38.11 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -13.16 | -29.51 | -25.46 | -36.31 | 12.47 | 12.47 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -17.31 | -14.3 | -31.37 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -4.46 | -7.43 | -21.78 | -24.9 | 9.97 | 9.97 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -6.32 | -5.49 | -26.89 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 60.01219345400749 | 101.25914660378932 | -11.25 | -15.78 | -20.74 | -34.95 | 3.12 | 3.12 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -12.35 | -10.85 | -19.51 |  | fail_low_response_condition |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -24.07 | -41.99 | -23.69 | -8.02 | 5.14 | 15.93 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -26.77 | -23.86 | -46.69 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -15.84 | -23.8 | 10.46 | -4.11 | 12.28 | 35.63 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -17.09 | -13.43 | -26.57 |  | fail_low_response_condition |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -2.35 | -0.95 | -2.8 | -0.48 | 2.97 | 2.97 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -1.96 | -1.37 | -8.77 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -2.62 | -5.26 | 15.41 | -16.22 | 18.72 | 24.0 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -1.34 | -1.53 | -10.14 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -7.74 | -18.18 | -19.29 | -10.34 | 15.22 | 15.22 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -9.31 | -7.56 | -20.37 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -17.06 | -37.33 | 14.48 | 16.53 | 19.49 | 49.47 | False |  | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -22.11 | -17.73 | -42.45 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -12.27 | -22.61 | -25.46 | -36.22 | 10.45 | 10.45 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -13.65 | -13.52 | -35.2 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -18.97 | -27.9 | 12.82 | -5.26 | 16.38 | 70.08 | False |  | distribution_warning | -0.35 | -5.88 | 1 | 0 | -20.82 | -16.85 | -32.2 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -4.06 | -8.49 | -23.75 | -45.45 | 11.97 | 11.97 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -5.76 | -4.83 | -25.35 | 14 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -7.16 | -8.92 | -12.69 | 27.17 | 10.86 | 25.75 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -7.73 | -6.64 | -18.2 | 18 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -11.84 | -24.5 | 10.68 | 13.49 | 14.22 | 15.32 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -19.45 | -13.58 | -39.81 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -8.71 | -10.06 | -22.45 | -8.71 | 10.95 | 10.95 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -11.36 | -8.5 | -23.23 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | -18.1 | -9.49 | -16.56 | -32.06 | 6.8 | 6.8 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -6.82 | -7.03 | -19.58 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -7.96 | -20.74 | 48.01 | 45.6 | 45.29 | 111.18 | True | 近60日漲幅>40%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -10.89 | -7.92 | -23.37 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -18.19 | -36.54 | -35.21 | -17.9 | 10.23 | 10.23 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -20.67 | -20.11 | -48.01 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -14.44 | -22.63 | -21.18 | -41.72 | 12.86 | 12.86 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -18.13 | -14.91 | -35.66 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -10.84 | -17.19 | 36.28 | 85.97 | 44.67 | 88.46 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -12.04 | -9.11 | -24.26 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | -8.39 | -25.78 | -18.16 | -32.39 | 16.7 | 18.25 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -13.25 | -10.64 | -31.35 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 146.48689155577668 | 72.46425018776883 | -14.31 | -24.67 | -30.46 | -24.03 | 9.05 | 9.05 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -17.4 | -15.2 | -29.37 |  | fail_low_response_condition |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | 6.9 | 16.02 | 11.14 | 11.69 | 17.23 | 17.23 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 8.51 | 8.56 | 0.0 | 11 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -6.88 | -11.37 | -22.82 | -10.71 | 12.56 | 12.56 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -8.52 | -7.35 | -25.16 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | -7.72 | -3.12 | -8.63 | -21.68 | 13.52 | 13.52 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -2.49 | -2.54 | -12.08 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 84.69522628124143 | 51.25937713911443 | -11.79 | -21.94 | -13.55 | -32.61 | 16.42 | 21.23 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -13.83 | -10.71 | -25.17 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -3.19 | -9.97 | -4.84 | -3.75 | 6.71 | 6.71 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -5.49 | -4.15 | -14.36 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | -2.34 | 62.03 | 78.29 | 46.09 | 87.22 | 115.51 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 22.99 | 19.26 | -11.15 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -13.14 | -23.06 | -21.19 | -24.52 | 11.56 | 11.56 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -13.81 | -13.11 | -30.81 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -5.44 | -18.54 | -18.16 | -22.19 | 14.1 | 14.1 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -10.22 | -8.18 | -22.94 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -10.93 | -10.93 | -12.21 | 1.56 | 13.7 | 13.7 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -7.75 | -6.78 | -19.56 | 16 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -6.93 | 6.0 | 6.59 | 23.58 | 12.63 | 22.78 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | -5.42 | -3.3 | -16.32 | 12 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -5.74 | -13.83 | -0.28 | -17.18 | 15.13 | 33.89 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -7.48 | -5.08 | -17.75 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | B_可觀察 | 109.68927823663151 | 90.15073758650963 | -3.84 | -0.75 | -6.24 | 0.77 | 10.27 | 34.53 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -0.44 | -1.25 | -9.78 | 20 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth | A_優先追蹤 | 125.76660822131308 | 27.66392696281368 | -2.73 | 1.71 | 23.18 | -11.44 | 25.35 | 69.52 | False |  | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 0.27 | 1.46 | -10.1 | 20 | selected |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 56.623935956655565 | 70.86506389755786 | -10.73 | -25.51 | -18.67 | -40.84 | 11.93 | 11.93 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -14.7 | -11.43 | -27.67 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -3.47 | -11.64 | -15.44 | 13.99 | 3.73 | 13.22 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -6.44 | -6.07 | -16.5 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -6.77 | -7.68 | -13.21 | -20.2 | 1.8 | 1.8 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -7.48 | -6.67 | -13.61 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -3.23 | -4.56 | -4.99 | -6.47 | 1.95 | 2.44 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -2.92 | -2.74 | -8.32 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -13.01 | -23.6 | 17.58 | 18.26 | 20.35 | 47.29 | False |  | distribution_warning | -2.68 | -0.93 | 0 | 2 | -18.17 | -14.95 | -36.45 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth | B_可觀察 | 76.79527413697619 | 57.94089889392686 | -7.38 | -14.39 | 18.12 | 13.38 | 27.44 | 54.09 | False |  | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -7.86 | -4.48 | -20.24 | 16 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -10.1 | -29.31 | -35.24 | -19.83 | 13.06 | 13.06 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -12.5 | -12.53 | -35.47 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -5.47 | -7.84 | -12.78 | -5.26 | 3.93 | 3.93 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -5.84 | -5.48 | -16.07 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -22.05 | -37.99 | -18.05 | 2.85 | 5.59 | 5.59 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -26.39 | -22.27 | -39.25 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -15.73 | -21.01 | -2.97 | -9.0 | 14.15 | 26.63 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -20.18 | -15.24 | -40.17 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -19.05 | -33.29 | 24.21 | 124.52 | 34.26 | 131.37 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -26.04 | -19.39 | -40.0 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | B_可觀察 | 55.69095387442037 | 42.29598437707936 | -11.39 | -5.54 | 23.88 | 44.35 | 27.4 | 43.2 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | -8.25 | -6.87 | -12.25 | 14 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 64.04751148579548 | 40.914406890913945 | -17.77 | -29.9 | -29.49 | -35.3 | 9.73 | 9.73 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -20.53 | -17.39 | -33.15 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -14.44 | -19.01 | -18.4 | -39.07 | 11.26 | 11.26 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -14.31 | -13.22 | -34.93 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 50.70369959160158 | 35.171695901726686 | -14.67 | -6.35 | -8.06 | -15.68 | 15.23 | 18.09 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | -8.52 | -6.33 | -22.41 | 15 | selected |