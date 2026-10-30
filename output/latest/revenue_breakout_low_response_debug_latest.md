# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-30 19:36:39 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1086 |
| standardized_revenue_rows | 1086 |
| price_rows | 772694 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 169 |
| price_metrics_pass | 168 |
| low_response_pass | 64 |
| already_priced_in_excluded | 15 |
| overheat_pass | 49 |
| score_pass | 49 |
| theme_priority_pass | 42 |
| final_rows | 42 |

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
| fail_revenue_condition | 917 |
| fail_low_response_condition | 104 |
| fail_already_priced_in | 15 |
| fail_defensive_or_traditional_excluded | 5 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -7.64 | 19.84 | 85.58 | 232.21 | 82.72 | 268.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -1.51 | 1.63 | -15.55 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -9.77 | -4.15 | 22.57 | 20.43 | 24.22 | 38.78 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -9.95 | -8.0 | -27.49 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | -0.49 | -2.87 | 2.01 | -11.35 | 2.94 | 8.09 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -2.59 | -2.83 | -18.8 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -0.6 | -4.03 | -1.77 | -8.59 | 1.63 | 1.63 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.06 | -1.91 | -9.26 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 0.0 | -1.87 | -10.42 | -11.75 | 1.72 | 1.72 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -0.35 | -0.72 | -11.09 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | -1.89 | 14.1 | 20.47 | 15.62 | 21.6 | 22.17 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 2.35 | 2.31 | -4.07 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -1.67 | -3.28 | -3.01 | -3.8 | 2.61 | 4.42 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -3.38 | -2.38 | -9.69 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.23 | 1.89 | -7.51 | 1.41 | 2.86 | 10.51 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.39 | -0.56 | -8.69 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 3.16 | 4.44 | 8.69 | 10.32 | 10.32 | 26.18 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 2.01 | 1.83 | -3.61 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -1.49 | -1.12 | -3.65 | -15.11 | 0.76 | 0.76 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -1.51 | -1.62 | -6.71 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -6.1 | -6.48 | -4.55 | -16.0 | 2.21 | 2.21 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -6.8 | -5.93 | -13.48 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 23.67 | 56.55 | 29.41 | -2.56 | 62.65 | 62.65 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 32.17 | 23.71 | -20.68 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 0.75 | 2.08 | -2.7 | 1.5 | 5.26 | 5.26 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | 0.45 | 0.05 | -10.89 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround | B_可觀察 | 62.31587090838761 | 46.95702744919681 | -3.52 | -6.48 | 20.18 | -26.74 | 22.32 | 34.31 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -5.58 | -4.36 | -16.46 | 14 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -7.67 | 10.79 | 33.72 | 70.24 | 34.75 | 87.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | -6.27 | -3.83 | -16.51 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -1.61 | -0.62 | -2.21 | -1.85 | 0.0 | 2.32 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -3.27 | -3.12 | -12.54 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -5.97 | -4.15 | -0.92 | -6.38 | 2.22 | 4.19 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -5.35 | -5.05 | -13.06 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.779802186364 | 14769.518174623092 | 4.66 | 13.77 | 8.94 | 25.04 | 15.41 | 28.16 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 5.52 | 3.67 | -4.89 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -8.55 | -7.87 | 1.23 | 2.5 | 4.68 | 9.82 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -9.66 | -7.61 | -18.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -4.27 | -20.35 | 22.93 | 77.23 | 18.19 | 116.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -10.05 | -9.86 | -36.03 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -6.56 | -13.31 | -25.97 | -36.49 | 0.44 | 0.44 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -10.13 | -9.61 | -31.74 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -3.21 | -4.03 | -13.98 | -14.37 | 0.7 | 0.7 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -3.35 | -3.74 | -21.1 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -15.43 | -2.87 | 18.05 | 120.95 | 25.61 | 134.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -11.91 | -8.82 | -20.89 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -0.66 | -2.91 | -6.09 | 5.07 | 2.39 | 16.47 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -1.89 | -1.64 | -7.4 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -12.26 | -28.51 | 64.12 | 182.29 | 92.22 | 214.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -15.58 | -9.75 | -33.87 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -2.07 | -4.24 | -2.27 | 5.1 | 2.6 | 8.72 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -4.06 | -2.95 | -8.49 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -7.38 | -19.49 | -5.07 | -37.65 | 2.36 | 3.92 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -12.89 | -11.89 | -33.98 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 256.6686868151223 | 187.3908590670214 | 3.13 | -5.46 | 26.54 | 35.39 | 23.22 | 46.88 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -2.16 | -1.44 | -14.77 | 17 | selected |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -11.02 | -10.77 | -24.0 | -36.04 | 2.22 | 2.22 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -16.13 | -14.61 | -37.76 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -0.2 | 5.29 | 6.19 | 17.2 | 16.92 | 23.91 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 0.21 | 1.14 | -4.33 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -2.84 | -3.12 | -11.18 | -3.67 | 2.25 | 2.25 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -2.92 | -3.16 | -13.54 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -10.92 | -14.85 | 26.12 | 0.82 | 28.77 | 47.98 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -11.16 | -11.26 | -28.6 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -2.94 | 0.51 | -3.72 | 22.18 | 5.68 | 22.93 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 0.03 | -1.64 | -19.05 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -12.69 | -19.68 | -16.43 | -28.07 | 0.0 | 1.45 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -17.09 | -15.44 | -31.45 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -14.64 | -8.93 | 28.63 | -26.62 | 21.28 | 44.68 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -13.45 | -10.87 | -22.14 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -6.28 | -7.18 | -0.15 | 4.67 | 7.01 | 12.0 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -6.45 | -5.44 | -16.42 | 21 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -3.2 | -5.5 | 9.09 | -6.47 | 11.97 | 13.98 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -2.3 | -2.51 | -9.53 | 15 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -6.31 | -4.98 | -1.48 | -4.59 | 2.52 | 18.96 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -11.65 | -9.52 | -27.74 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | -0.44 | -6.85 | 20.78 | 37.51 | 25.93 | 54.9 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -3.44 | -1.89 | -9.81 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | -4.35 | -5.61 | -8.19 | -17.58 | 10.64 | 10.64 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -4.82 | -3.36 | -14.11 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 576.622775031737 | 626.9495065095125 | 4.12 | -10.18 | 26.07 | 41.59 | 21.36 | 71.19 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -5.37 | -3.87 | -20.12 | 15 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -7.47 | -17.36 | -34.08 | -8.97 | 0.49 | 0.49 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -11.32 | -10.67 | -41.49 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | 0.36 | 1.27 | -1.93 | 4.28 | 4.09 | 11.11 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.61 | -0.32 | -6.35 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -2.65 | -6.6 | 1.94 | -14.42 | 7.92 | 15.0 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -4.65 | -4.2 | -20.0 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.98990000276115 | 3.65 | -0.7 | -3.07 | -19.09 | 6.97 | 31.48 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | 0.76 | 0.67 | -13.81 | 24 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -7.79 | -2.85 | -4.29 | -9.52 | 3.76 | 7.41 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -6.03 | -5.09 | -13.82 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | -1.76 | -13.02 | 24.16 | 41.53 | 24.63 | 51.82 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -7.85 | -6.98 | -25.45 | 12 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 42.45 | 211.89 | 288.58 | 605.18 | 305.03 | 781.69 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 60.51 | 57.57 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -10.42 | -20.96 | -10.14 | -33.74 | 2.14 | 2.14 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -16.9 | -14.99 | -33.13 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -8.68 | -11.24 | -2.64 | -6.75 | 2.79 | 9.95 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -9.83 | -7.99 | -17.84 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | 0.54 | 15.67 | 11.14 | 24.66 | 24.24 | 27.68 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 3.59 | 3.7 | -6.35 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -9.2 | -18.78 | 2.39 | -28.84 | 4.34 | 15.62 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -13.26 | -11.85 | -37.4 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -6.04 | 26.16 | 74.77 | 102.12 | 68.21 | 109.92 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | -1.21 | 1.69 | -11.7 |  | fail_already_priced_in |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -2.78 | 3.24 | -2.51 | -2.78 | 4.79 | 4.79 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -0.11 | -0.42 | -4.89 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -2.15 | -1.03 | 7.41 | 41.99 | 16.14 | 46.33 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -3.56 | -1.24 | -10.23 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -1.24 | -5.62 | -6.73 | -15.16 | 3.91 | 3.91 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -2.74 | -2.57 | -9.89 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | 0.22 | -3.26 | -24.51 | -7.9 | 8.48 | 8.48 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -3.62 | -3.05 | -24.38 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -2.0 | 1.81 | -10.68 | -4.38 | 3.56 | 3.56 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -0.03 | -2.83 | -19.8 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -1.2 | -2.51 | 0.76 | -13.93 | 4.42 | 4.42 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -2.51 | -2.27 | -8.7 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -2.93 | -2.54 | -8.57 | -5.42 | 0.63 | 0.63 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -1.88 | -2.1 | -10.7 | 16 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -2.13 | 14.23 | 20.22 | 18.45 | 21.59 | 27.38 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 1.41 | 1.79 | -13.01 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround |  | 97.6272252761016 | 27.282730439694276 | 3.0 | 8.11 | 41.68 | 56.05 | 43.2 | 63.27 | True | 近60日漲幅>40% | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 2.78 | 2.84 | -10.78 |  | fail_already_priced_in |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | 0.71 | 0.99 | 7.24 | 4.41 | 10.75 | 14.31 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.16 | 0.13 | -9.89 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -1.5 | -1.5 | -8.78 | -3.42 | 0.25 | 0.25 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -1.68 | -1.86 | -9.82 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 13.21 | 12.97 | -23.08 | 5.68 | 20.0 | 36.36 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 7.36 | 5.7 | -23.62 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -6.27 | -12.4 | -5.25 | -12.54 | 1.36 | 1.36 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -7.9 | -7.58 | -29.32 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | -3.66 | 0.85 | -12.22 | 4.41 | 3.95 | 5.33 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | -2.09 | -1.85 | -9.89 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | 12.6 | -2.81 | 53.89 | 25.91 | 46.95 | 72.05 | True | 近60日漲幅>40% | distribution_warning | -5.51 | -6.04 | 0 | 0 | 6.45 | 5.83 | -13.17 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -18.77 | -27.25 | 57.07 | 3.29 | 61.94 | 72.63 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -22.32 | -14.94 | -35.81 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -3.96 | -6.13 | 2.71 | 25.25 | 6.33 | 32.07 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -3.33 | -2.99 | -25.06 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -9.03 | -8.7 | -6.15 | -38.24 | 2.02 | 2.86 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -12.75 | -10.07 | -21.74 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -2.73 | -2.62 | -7.67 | -7.99 | 1.61 | 1.61 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -3.03 | -3.08 | -22.54 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -2.59 | -0.24 | 5.34 | -24.86 | 14.05 | 15.0 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -2.46 | -1.46 | -12.1 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -10.09 | -15.11 | 25.67 | 13.03 | 17.46 | 51.45 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -14.88 | -10.52 | -30.35 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.500059681732026 | 40.60068600026104 | -12.18 | -1.73 | 38.75 | 6.44 | 43.82 | 56.57 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -8.71 | -6.49 | -15.23 | 16 | selected |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.47 | 2.9 | 0.95 | -0.93 | 4.93 | 4.93 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 0.4 | 0.3 | -6.58 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 3.64 | -3.06 | 17.65 | -16.79 | 21.28 | 26.67 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -1.09 | -0.24 | -8.21 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 77.30413360834295 | 27.56110296294079 | -7.79 | -7.29 | -6.26 | -10.86 | 0.39 | 2.0 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -8.3 | -6.65 | -17.37 | 18 | selected |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -10.54 | -16.08 | 43.76 | 59.55 | 47.35 | 77.03 | True | 近60日漲幅>40% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -17.98 | -10.78 | -31.84 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -1.4 | -9.9 | -7.84 | -33.96 | 2.17 | 5.22 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -5.91 | -6.21 | -25.4 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -5.8 | 4.32 | 93.83 | 23.95 | 83.63 | 116.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -4.55 | -1.33 | -13.58 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -2.94 | -2.2 | -20.25 | -33.08 | 0.79 | 0.79 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -3.63 | -3.69 | -26.08 | 14 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -5.9 | -1.08 | 4.26 | 29.68 | 8.26 | 39.02 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -2.05 | -1.87 | -10.92 | 21 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -14.08 | 3.93 | 21.44 | 19.79 | 26.68 | 29.58 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -16.03 | -10.41 | -33.25 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -4.49 | 4.94 | 2.72 | -0.29 | 7.59 | 8.97 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -2.8 | -2.35 | -15.0 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | 19.42 | 13.7 | 9.57 | -17.82 | 32.8 | 32.8 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 14.62 | 14.39 | 0.0 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -4.56 | -3.66 | 100.66 | 37.07 | 89.45 | 140.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -4.12 | -0.47 | -12.74 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -9.11 | -22.1 | 9.95 | -13.07 | 7.07 | 23.94 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -14.74 | -13.43 | -37.37 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -15.29 | -8.69 | 6.36 | -35.69 | 6.49 | 19.36 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -11.25 | -9.75 | -25.79 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -3.37 | -8.41 | 83.31 | 61.1 | 72.78 | 125.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -5.9 | -1.78 | -15.12 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | -7.68 | -7.06 | 11.93 | -35.5 | 12.3 | 30.23 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -10.71 | -8.7 | -24.39 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | -5.65 | -5.65 | -3.56 | -4.82 | 11.63 | 11.63 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -6.47 | -4.92 | -16.86 | 22 | selected |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | 0.97 | 6.41 | 0.73 | 1.22 | 8.36 | 8.36 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 2.76 | 1.96 | -4.6 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -5.54 | -2.66 | -12.13 | -10.59 | 2.13 | 2.13 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -5.06 | -5.27 | -19.83 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 6.01 | 2.97 | 9.36 | -17.28 | 11.54 | 17.41 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | 3.7 | 2.88 | -5.19 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -11.11 | -3.61 | 20.12 | -33.52 | 20.36 | 34.08 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -9.33 | -7.61 | -17.24 | 20 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -3.91 | -4.97 | 3.93 | -1.99 | 4.56 | 4.88 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -4.84 | -3.73 | -11.79 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 47.17 | 74.18 | 108.18 | 51.56 | 110.13 | 122.66 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 48.14 | 42.89 | 0.0 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -10.02 | -10.46 | -1.97 | -26.24 | 1.78 | 8.44 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -11.62 | -9.48 | -19.37 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -3.38 | -1.48 | 5.26 | 46.2 | 8.34 | 54.56 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -2.14 | -1.55 | -11.89 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -2.38 | 12.89 | 21.45 | 26.39 | 23.79 | 35.22 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 4.36 | 3.44 | -10.09 | 13 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -13.05 | -1.84 | 23.71 | -24.49 | 25.17 | 38.15 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -7.24 | -5.71 | -15.13 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663151 | 90.15073758650963 | 12.05 | 2.57 | 19.49 | -2.28 | 21.3 | 42.71 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | 5.04 | 4.44 | -4.29 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | -4.16 | 2.67 | 47.86 | -36.04 | 49.14 | 64.76 | True | 近60日漲幅>40% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | -2.18 | -1.54 | -12.63 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 56.623935956655565 | 70.86506389755786 | -12.34 | 1.51 | 8.63 | -36.08 | 3.6 | 20.56 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -10.19 | -8.39 | -20.42 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -1.37 | -3.75 | -1.91 | 14.33 | 1.41 | 23.79 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -2.43 | -2.23 | -10.25 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -1.62 | 0.16 | -6.32 | -12.89 | 1.67 | 1.67 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -1.38 | -1.89 | -7.03 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -0.69 | -2.28 | -6.74 | -7.94 | 0.94 | 4.89 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -1.53 | -1.53 | -7.94 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -8.92 | -7.37 | 62.79 | 54.57 | 68.67 | 111.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -7.04 | -5.97 | -23.68 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 3.54 | 25.83 | 65.22 | 18.38 | 66.67 | 72.73 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 4.63 | 7.38 | -10.59 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -3.27 | -23.33 | -8.41 | 1.97 | 1.97 | 1.97 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -11.22 | -9.08 | -30.3 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -1.43 | -3.03 | -5.18 | -5.08 | 0.79 | 7.94 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.93 | -2.28 | -11.01 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -12.85 | -1.47 | 14.53 | 27.77 | 16.52 | 36.56 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -13.19 | -9.2 | -21.64 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth | A_優先追蹤 | 81.57256696034645 | 71.39362622544883 | -20.91 | 6.75 | 37.01 | 31.82 | 38.1 | 53.44 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -6.81 | -5.76 | -27.5 | 17 | selected |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -16.52 | 10.81 | 161.22 | 140.63 | 141.05 | 199.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -9.58 | -4.78 | -22.37 |  | fail_already_priced_in |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | A_優先追蹤 | 55.69095387442037 | 42.29598437707936 | 1.01 | 6.35 | 30.52 | 62.1 | 43.57 | 66.12 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 3.06 | 2.98 | -1.47 | 19 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 64.04751148579548 | 40.914406890913945 | -13.59 | -8.39 | -4.05 | -24.47 | 0.95 | 6.77 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -12.41 | -10.62 | -21.11 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -8.61 | -18.44 | 5.24 | -36.17 | 7.68 | 17.38 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -9.02 | -7.5 | -25.85 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 50.70369959160158 | 35.171695901726686 | 2.45 | 22.74 | 21.55 | 5.35 | 30.39 | 38.67 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | 8.17 | 7.14 | -8.89 | 17 | selected |
| 6416 | 瑞祺電通 | 通信網路業 | mainstream_growth |  | 59.150827678561384 | 30.6291038143077 | -3.28 | 1.72 | 35.48 | 40.64 | 37.21 | 49.94 | False |  | strong_accumulation | 1.01 | 0.62 | 2 | 2 | -1.75 | -0.65 | -8.53 |  | fail_low_response_condition |