# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-10 19:38:03 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 786498 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 58 |
| already_priced_in_excluded | 10 |
| overheat_pass | 48 |
| score_pass | 47 |
| theme_priority_pass | 38 |
| final_rows | 38 |

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
| fail_low_response_condition | 278 |
| fail_already_priced_in | 10 |
| fail_defensive_or_traditional_excluded | 4 |
| fail_non_mainstream_score_lt_11 | 3 |
| fail_mainstream_score_lt_10 | 2 |
| missing_or_insufficient_price_metrics | 2 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | 6.64 | -6.77 | 52.11 | 231.04 | 66.09 | 234.49 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -2.48 | 2.81 | -17.55 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround |  | 96.8052734253821 | 30.286775373992953 | -5.24 | -16.5 | 6.75 | 19.34 | 9.52 | 26.75 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -14.45 | -10.63 | -33.77 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral |  | 74.66249568827091 | 115.02921243693271 | -7.12 | -10.96 | -7.86 | -13.86 | 4.28 | 4.28 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -8.82 | -8.1 | -25.92 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -3.24 | -7.0 | -8.43 | -13.09 | 6.22 | 6.22 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -4.19 | -4.05 | -13.25 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 6.28 | 6.95 | -0.59 | -3.79 | 9.72 | 9.72 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 5.13 | 3.68 | -7.3 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 34.93 | 52.92 | 67.58 | 65.32 | 65.32 | 73.11 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 31.31 | 29.94 | -6.85 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | 1.42 | -4.02 | -0.56 | 0.0 | 4.37 | 5.6 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -0.82 | -0.46 | -8.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.23 | 0.0 | -3.79 | 5.37 | 3.1 | 10.77 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.17 | -0.18 | -8.47 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 0.17 | 3.03 | -1.2 | 13.33 | 4.9 | 24.03 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 0.21 | 0.16 | -5.25 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -1.57 | -6.37 | -10.71 | -19.61 | 2.04 | 2.04 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -4.98 | -4.37 | -11.66 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -3.51 | -16.67 | -13.04 | -11.65 | 9.45 | 9.45 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -7.41 | -6.19 | -17.6 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | -5.63 | 34.67 | 20.59 | -14.58 | 43.58 | 43.58 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 2.93 | 2.58 | -29.98 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -2.81 | -0.95 | -9.9 | -6.65 | 2.77 | 2.77 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -3.37 | -2.97 | -14.36 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -8.47 | -20.35 | -23.31 | -31.83 | 9.66 | 11.27 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -16.03 | -13.55 | -30.79 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -4.24 | -20.8 | -5.11 | 61.22 | 8.22 | 69.89 | False |  | distribution_warning | -0.26 | -0.27 | 1 | 1 | -12.25 | -8.59 | -24.4 |  | fail_low_response_condition |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -9.69 | -17.08 | -17.96 | -14.13 | 4.8 | 4.8 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -11.98 | -10.11 | -23.1 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -1.43 | -12.16 | -13.99 | -17.75 | 6.15 | 6.15 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -6.33 | -5.21 | -14.81 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.779802186364 | 14769.518174623092 | -10.69 | -5.07 | -4.78 | 4.92 | 0.32 | 10.16 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | -10.16 | -8.19 | -18.25 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -5.65 | -20.22 | -14.57 | -6.87 | 5.34 | 5.34 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -14.42 | -12.22 | -27.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -7.31 | -19.31 | -30.45 | 74.97 | 18.96 | 85.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -9.39 | -11.34 | -43.22 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -5.91 | -20.99 | -32.13 | -38.76 | 0.98 | 0.98 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -13.03 | -12.19 | -34.49 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -1.78 | -7.83 | -18.2 | -11.09 | 5.74 | 5.74 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -4.67 | -4.07 | -20.55 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | 6.74 | -17.2 | 21.84 | 123.18 | 25.74 | 121.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -6.99 | -3.35 | -20.81 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -4.56 | -7.53 | -9.31 | 0.89 | 4.82 | 4.82 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -5.46 | -5.16 | -12.94 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -0.96 | -28.36 | 70.09 | 161.86 | 80.35 | 159.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -12.81 | -8.62 | -37.95 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -0.44 | -10.39 | -4.59 | 2.47 | 13.12 | 13.12 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -3.59 | -2.95 | -11.78 | 11 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -7.02 | -29.22 | -38.04 | -41.77 | 14.35 | 14.35 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -15.47 | -15.5 | -43.18 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -7.53 | -23.73 | -24.16 | 18.42 | 17.39 | 17.39 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -12.17 | -11.75 | -30.05 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | 3.34 | -25.36 | -27.63 | -37.7 | 24.1 | 24.1 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -11.36 | -8.61 | -35.22 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth |  | 158.6674544463884 | 97.96095815091336 | -13.46 | -17.95 | -13.08 | -6.28 | 0.64 | 0.64 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -17.62 | -14.68 | -23.94 |  | fail_low_response_condition |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -6.39 | -11.64 | -10.64 | -9.22 | 3.11 | 3.11 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -8.23 | -7.59 | -20.25 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -10.19 | -32.64 | -14.16 | -24.22 | 10.23 | 17.34 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -21.2 | -19.68 | -43.39 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -4.02 | -4.52 | -15.67 | 1.48 | 10.91 | 10.91 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | -6.17 | -5.81 | -25.31 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -15.21 | -43.78 | -37.02 | -42.29 | 10.08 | 10.08 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -27.93 | -25.48 | -48.83 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 125.4495058048851 | 63.1715973040828 | -6.88 | -16.12 | -13.12 | -3.79 | 7.98 | 7.98 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -10.46 | -9.58 | -24.25 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -4.17 | -8.29 | -5.39 | -3.08 | 9.74 | 9.74 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -5.28 | -5.19 | -15.08 | 11 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -0.68 | -27.25 | -21.14 | -6.93 | 18.29 | 18.29 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -10.09 | -8.17 | -32.53 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -4.35 | -18.43 | -10.29 | 27.94 | 10.43 | 32.07 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -10.21 | -8.86 | -21.35 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | 7.82 | -3.66 | -8.82 | -6.31 | 11.99 | 11.99 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -0.92 | -1.09 | -11.33 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -6.81 | -28.01 | -21.68 | 30.72 | 18.21 | 32.99 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -11.59 | -11.49 | -32.69 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -5.43 | -22.1 | -39.39 | -18.21 | 7.74 | 7.74 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -13.25 | -12.98 | -34.47 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -1.96 | -4.51 | -3.17 | 4.76 | 3.38 | 6.8 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -2.25 | -1.57 | -8.03 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -6.23 | -10.36 | -10.13 | -19.53 | 5.49 | 8.13 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -6.96 | -6.48 | -24.78 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 290.42308535778307 | 369.98990000276115 | -14.65 | -18.1 | -18.53 | -25.68 | 1.53 | 7.87 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -14.07 | -13.39 | -29.29 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -1.6 | -9.05 | -11.8 | -12.36 | 10.6 | 10.6 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -7.28 | -5.03 | -17.83 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | -0.95 | -16.58 | -16.8 | 14.71 | 19.54 | 32.2 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -6.99 | -6.42 | -30.36 | 11 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 5.56 | 81.86 | 292.39 | 656.81 | 313.04 | 799.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 27.76 | 31.72 | -10.2 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -17.3 | -42.84 | -40.7 | -46.07 | 11.48 | 11.48 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -28.96 | -26.85 | -50.93 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -5.91 | -26.82 | -23.29 | -20.42 | 11.57 | 11.57 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -14.98 | -13.13 | -29.0 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -1.45 | 3.03 | 11.11 | 15.65 | 10.75 | 17.65 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | -5.75 | -2.47 | -13.71 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -4.56 | -29.77 | -27.33 | -39.86 | 16.72 | 16.72 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -14.43 | -13.97 | -45.53 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -9.98 | -31.31 | -3.99 | 8.46 | 14.94 | 45.34 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -20.07 | -14.88 | -33.14 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | 0.87 | 1.76 | -4.68 | -3.62 | 6.13 | 6.13 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -1.55 | -0.46 | -5.98 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -6.64 | -16.14 | -8.34 | 28.49 | 13.21 | 29.65 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -9.4 | -7.08 | -19.61 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -3.25 | -10.51 | -12.61 | -16.76 | 2.41 | 2.41 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -6.22 | -5.89 | -15.82 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -2.02 | -11.72 | -0.68 | -21.54 | 2.94 | 2.94 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.82 | -5.13 | -19.07 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -3.26 | -8.78 | -8.11 | -16.49 | 3.83 | 3.83 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -6.02 | -5.24 | -13.95 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -1.27 | -4.41 | -11.75 | -7.36 | 3.91 | 3.91 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -3.62 | -3.01 | -9.61 | 17 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -1.94 | -0.33 | 7.83 | 16.09 | 10.58 | 19.76 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | -5.59 | -2.89 | -17.89 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -3.46 | 0.0 | 28.01 | 37.32 | 29.65 | 45.56 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -4.7 | -2.74 | -17.1 | 16 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | 0.29 | -1.14 | 1.76 | 5.8 | 9.48 | 11.41 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -1.77 | -0.82 | -12.17 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | 2.04 | -0.25 | -3.37 | -1.23 | 7.22 | 7.22 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | 0.53 | 0.62 | -8.45 | 15 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | -12.2 | 7.92 | -0.38 | 21.6 | 15.11 | 26.34 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | -4.17 | -5.35 | -25.57 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -3.71 | -17.33 | -31.99 | -20.74 | 9.98 | 9.98 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -9.58 | -9.24 | -34.49 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | -2.39 | 1.66 | -3.54 | -2.78 | 7.46 | 7.46 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 0.35 | 0.49 | -5.77 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 470.2347504677583 | 343.911329000345 | -7.01 | -15.54 | -15.7 | 1.58 | 16.84 | 40.06 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -7.37 | -8.49 | -29.31 | 13 | selected |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | 1.29 | -35.97 | 15.76 | 1.73 | 25.13 | 61.62 | False |  | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -14.7 | -10.54 | -39.9 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -12.02 | -18.94 | -32.22 | 4.72 | 2.95 | 4.72 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -14.88 | -13.52 | -31.91 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -4.25 | -28.07 | -25.45 | -40.89 | 14.76 | 14.76 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -14.22 | -11.63 | -29.97 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -3.46 | -9.27 | -25.2 | -28.19 | 7.41 | 7.41 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -8.07 | -7.1 | -28.6 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | B_可觀察 | 60.01219345400749 | 101.25914660378932 | -5.71 | -11.83 | -13.64 | -34.82 | 7.95 | 7.95 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -7.68 | -6.16 | -14.99 | 14 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -8.2 | -34.8 | -16.53 | -8.51 | 15.0 | 26.8 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -18.15 | -15.54 | -41.69 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.500059681732026 | 40.60068600026104 | -3.07 | -18.64 | 7.25 | -2.97 | 19.87 | 44.8 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -10.57 | -6.99 | -21.61 | 15 | selected |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.48 | 0.0 | -3.24 | -0.48 | 3.47 | 3.47 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -1.48 | -0.82 | -8.33 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 0.7 | -1.55 | 19.17 | -14.37 | 19.17 | 27.11 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | 1.21 | 0.86 | -7.89 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 77.30413360834295 | 27.56110296294079 | -0.41 | -16.35 | -16.49 | -12.7 | 16.18 | 16.18 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -7.72 | -6.25 | -19.7 | 14 | selected |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -3.57 | -35.64 | 18.62 | 24.06 | 25.99 | 57.6 | False |  | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -15.96 | -12.29 | -39.32 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -10.31 | -25.4 | -29.64 | -39.9 | 6.82 | 6.82 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -15.28 | -15.21 | -37.33 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -2.44 | -24.08 | 26.14 | 5.95 | 26.14 | 84.35 | True | 距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -12.99 | -9.13 | -26.51 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 90.47990444398276 | 46.685682375869504 | 8.96 | 0.54 | -17.61 | -40.83 | 23.16 | 23.16 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | 3.63 | 4.27 | -17.75 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -3.12 | -9.28 | -10.47 | 22.14 | 12.5 | 23.02 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -5.91 | -4.84 | -16.99 | 19 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -3.52 | -21.11 | 14.37 | 13.15 | 18.21 | 19.35 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -15.69 | -9.77 | -37.71 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -8.72 | -19.51 | -21.24 | -15.56 | 6.93 | 6.93 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -13.67 | -10.94 | -23.7 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | -7.82 | -7.82 | -14.78 | -30.33 | 8.4 | 8.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -5.05 | -5.2 | -18.37 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | 5.52 | -14.23 | 44.7 | 41.56 | 44.99 | 125.83 | True | 近60日漲幅>40%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -3.95 | -1.41 | -18.06 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -1.47 | -29.21 | -21.96 | -16.02 | 19.97 | 19.97 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -12.1 | -12.09 | -43.42 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -2.34 | -18.92 | -15.73 | -39.76 | 19.05 | 19.05 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -12.76 | -9.47 | -32.13 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -4.06 | -19.19 | 42.44 | 73.87 | 40.36 | 93.65 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -8.64 | -6.09 | -22.18 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | 8.92 | -21.29 | -13.53 | -30.28 | 28.33 | 30.04 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -3.36 | -1.59 | -24.5 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 146.48689155577668 | 72.46425018776883 | -8.42 | -21.28 | -26.29 | -25.1 | 11.58 | 11.58 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -14.5 | -12.26 | -26.29 |  | fail_low_response_condition |
| 3703 | 欣陸 | 建材營造 | neutral |  | 89.3174912383306 | 3.4475931972039313 | 14.32 | 22.82 | 18.86 | 17.98 | 25.07 | 25.07 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 14.52 | 14.3 | -1.84 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -3.92 | -11.79 | -21.0 | -14.85 | 11.62 | 11.62 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -8.73 | -7.5 | -25.78 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 0.96 | 0.11 | -8.1 | -25.53 | 14.74 | 14.74 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -1.45 | -1.37 | -11.13 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | 5.78 | -13.45 | -2.46 | -27.44 | 27.68 | 32.96 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -4.79 | -1.9 | -17.93 | 19 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -0.88 | -12.5 | -3.45 | -4.55 | 7.35 | 7.35 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -4.27 | -3.28 | -13.85 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 8.56 | 80.61 | 94.45 | 56.64 | 105.87 | 136.98 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 31.28 | 27.82 | -2.3 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -3.41 | -19.47 | -15.79 | -25.81 | 15.0 | 15.0 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -10.19 | -9.65 | -28.68 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -2.95 | -20.87 | -21.05 | -27.06 | 10.58 | 10.58 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -11.98 | -10.19 | -25.32 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | 0.93 | -4.41 | -6.7 | -1.32 | 21.42 | 21.42 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -1.27 | -0.41 | -14.1 | 16 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -5.22 | 7.25 | 8.09 | 21.62 | 10.19 | 21.62 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | -4.94 | -2.29 | -15.61 | 12 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -1.5 | -15.59 | -3.23 | -25.0 | 14.65 | 33.33 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -7.07 | -5.04 | -18.09 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 109.68927823663151 | 90.15073758650963 | 0.96 | -2.41 | -4.19 | -1.31 | 10.27 | 34.53 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -0.32 | -1.15 | -9.78 | 22 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | 11.98 | 8.41 | 27.65 | -8.56 | 31.69 | 78.1 | False |  | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 4.91 | 6.0 | -5.56 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | 0.0 | -19.54 | -13.38 | -38.84 | 20.08 | 20.08 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -7.46 | -4.59 | -22.4 | 17 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | 1.19 | -9.55 | -11.89 | 12.54 | 5.9 | 14.05 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -4.0 | -3.77 | -13.01 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -6.34 | -7.73 | -13.82 | -20.31 | 1.08 | 1.08 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -7.78 | -6.76 | -13.96 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -1.18 | -4.33 | -4.76 | -5.83 | 2.19 | 2.69 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -2.47 | -2.3 | -8.1 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -5.02 | -18.81 | 20.2 | 22.5 | 20.55 | 50.36 | False |  | distribution_warning | -2.68 | -0.93 | 0 | 2 | -15.65 | -12.21 | -35.12 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth | A_優先追蹤 | 76.79527413697619 | 57.94089889392686 | -0.85 | -16.43 | 18.58 | 13.96 | 31.95 | 59.55 | False |  | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -3.69 | -1.01 | -17.41 | 18 | selected |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -5.31 | -27.28 | -33.16 | -23.29 | 10.99 | 10.99 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -12.7 | -13.11 | -36.66 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -2.4 | -6.96 | -11.4 | -4.26 | 5.04 | 5.04 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -4.5 | -4.12 | -15.18 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -13.67 | -37.69 | -17.65 | -2.21 | 6.73 | 6.73 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -23.88 | -20.0 | -38.6 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -2.87 | -17.31 | -0.67 | -14.07 | 18.44 | 31.39 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -16.45 | -11.16 | -37.92 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -12.0 | -34.49 | 16.81 | 114.2 | 17.86 | 130.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -25.01 | -18.5 | -40.34 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | A_優先追蹤 | 55.69095387442037 | 42.29598437707936 | -8.66 | -3.91 | 29.02 | 44.71 | 29.93 | 45.28 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | -5.25 | -3.69 | -9.56 | 18 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 64.04751148579548 | 40.914406890913945 | -5.9 | -25.34 | -24.61 | -31.73 | 16.41 | 16.41 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -14.46 | -11.44 | -29.07 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -9.64 | -18.72 | -19.93 | -43.35 | 10.41 | 10.41 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -14.13 | -12.88 | -35.43 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 50.70369959160158 | 35.171695901726686 | -6.77 | -4.76 | -5.57 | -20.92 | 18.73 | 21.69 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | -5.51 | -3.2 | -20.05 | 15 | selected |
| 6416 | 瑞祺電通 | 通信網路業 | mainstream_growth |  | 59.150827678561384 | 30.6291038143077 | -4.13 | -13.28 | 4.81 | 14.96 | 14.58 | 32.78 | False |  | strong_accumulation | 1.01 | 0.62 | 2 | 2 | -9.52 | -7.14 | -18.99 |  | fail_low_response_condition |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 52.96265560165975 | 66.44893470632094 | 0.19 | -21.99 | 22.02 | 1.33 | 26.07 | 96.31 | True | 距120日低點反彈>80% | distribution_warning | -1.43 | -0.35 | 1 | 1 | -11.27 | -9.01 | -35.44 |  | fail_low_response_condition |