# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-03 19:35:38 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 776619 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 55 |
| already_priced_in_excluded | 10 |
| overheat_pass | 45 |
| score_pass | 45 |
| theme_priority_pass | 36 |
| final_rows | 36 |

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
| fail_low_response_condition | 281 |
| fail_already_priced_in | 10 |
| fail_defensive_or_traditional_excluded | 7 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -8.91 | 6.69 | 58.94 | 217.7 | 59.88 | 237.06 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -10.75 | -6.65 | -22.68 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround |  | 96.8052734253821 | 30.286775373992953 | -9.49 | -8.56 | 15.09 | 25.35 | 15.58 | 33.77 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -12.53 | -9.95 | -30.1 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | -3.67 | -5.05 | -0.8 | -10.58 | 0.2 | 6.18 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -3.87 | -4.05 | -20.24 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -2.76 | -5.54 | -2.18 | -10.99 | 0.61 | 0.61 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.77 | -2.75 | -10.34 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 1.27 | -1.04 | -7.0 | -11.81 | 3.24 | 3.24 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 0.83 | 0.32 | -10.15 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral | B_可觀察 | 70.45469720237698 | 47.58022431497226 | 2.26 | 16.74 | 26.51 | 20.89 | 27.1 | 28.3 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 5.8 | 6.22 | -1.09 | 16 | selected |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -3.02 | -4.59 | -1.94 | -3.81 | 2.92 | 4.13 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -3.31 | -2.34 | -9.95 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -0.92 | -1.15 | -5.07 | 3.36 | 2.86 | 10.51 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.42 | -0.45 | -8.69 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | -0.52 | -0.17 | 2.85 | 9.9 | 6.26 | 23.82 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | -0.05 | -0.13 | -5.41 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -4.51 | -5.58 | -6.62 | -16.45 | 0.0 | 0.0 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -4.89 | -4.78 | -10.25 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -4.6 | -7.32 | -6.94 | -11.63 | 2.7 | 2.7 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -7.3 | -6.14 | -14.61 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | -21.8 | 45.35 | 22.19 | -10.32 | 52.14 | 52.14 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 19.01 | 12.76 | -25.81 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 1.33 | -0.56 | -2.91 | 1.14 | 4.09 | 4.09 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -0.7 | -1.0 | -11.88 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -13.89 | -19.74 | -5.34 | -31.11 | 0.81 | 21.57 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -13.26 | -12.02 | -24.39 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -9.84 | 1.85 | 13.4 | 65.0 | 13.01 | 77.42 | False |  | distribution_warning | -0.26 | -0.27 | 1 | 1 | -11.65 | -8.07 | -21.05 |  | fail_low_response_condition |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -3.73 | -2.89 | -7.08 | -4.09 | 0.26 | 0.26 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -5.62 | -5.0 | -14.85 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -6.67 | -7.22 | -2.02 | -14.86 | 0.0 | 1.61 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -7.09 | -6.48 | -15.21 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.779802186364 | 14769.518174623092 | -5.98 | 9.15 | 6.63 | 17.49 | 11.08 | 23.35 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 0.56 | -0.38 | -8.47 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -17.86 | -18.15 | -4.56 | -5.74 | 0.0 | 2.68 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -14.0 | -12.14 | -23.33 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -5.81 | -21.93 | -2.69 | 84.43 | 1.26 | 107.64 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -11.72 | -11.87 | -38.75 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -9.47 | -17.91 | -32.72 | -37.14 | 0.0 | 0.0 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -11.84 | -11.18 | -34.13 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -3.43 | -5.06 | -16.47 | -13.52 | 0.0 | 0.0 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -4.41 | -4.56 | -22.34 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -14.66 | -11.88 | 6.24 | 119.05 | 17.8 | 120.1 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -16.58 | -12.72 | -25.81 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -2.31 | -7.21 | -1.33 | 4.96 | 0.34 | 14.73 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -2.73 | -2.81 | -8.78 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -7.33 | -24.39 | 43.56 | 186.24 | 82.1 | 198.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -17.67 | -12.91 | -37.35 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -4.37 | -8.57 | -1.08 | 1.1 | 0.66 | 5.28 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -6.4 | -5.21 | -11.39 | 12 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -14.27 | -27.02 | -26.42 | -47.75 | 0.68 | 0.68 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -17.14 | -16.45 | -38.89 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -10.43 | -18.89 | -7.01 | 8.96 | 0.0 | 30.36 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -11.81 | -11.4 | -24.35 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -15.06 | -21.32 | -35.56 | -44.11 | 1.01 | 1.01 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -21.2 | -18.63 | -42.39 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -10.39 | -4.19 | -2.56 | 9.72 | 7.4 | 13.82 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -7.74 | -6.25 | -12.12 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -7.93 | -4.4 | -0.74 | -3.44 | 0.0 | 0.75 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -4.01 | -4.04 | -14.81 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -18.39 | -23.76 | -2.11 | -10.99 | 0.0 | 30.65 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -20.02 | -19.39 | -36.96 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -9.21 | -4.19 | -13.33 | 7.52 | 1.6 | 14.17 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | -3.64 | -4.9 | -22.18 | 12 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -20.97 | -25.72 | -19.74 | -31.64 | 0.0 | 0.0 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -25.33 | -22.89 | -39.65 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -10.19 | -11.42 | 8.14 | -32.17 | 7.06 | 37.59 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -17.04 | -13.65 | -25.95 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -8.53 | -11.26 | -1.51 | 0.0 | 0.31 | 9.0 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -8.18 | -7.04 | -18.66 | 23 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -4.89 | -6.74 | 3.66 | -6.88 | 5.59 | 11.65 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -3.74 | -3.95 | -11.38 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -7.47 | -11.66 | -14.49 | -10.67 | 0.92 | 11.83 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -16.3 | -13.27 | -32.07 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -9.75 | -14.25 | 7.64 | 33.33 | 5.08 | 41.23 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -10.86 | -9.37 | -17.77 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 62.28854584713688 | 107.88805150926841 | -11.97 | -14.49 | -14.22 | -15.57 | 3.87 | 3.87 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -9.5 | -8.29 | -19.37 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -6.8 | -20.81 | -5.73 | 20.53 | 0.0 | 54.8 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -12.88 | -11.88 | -27.77 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -9.52 | -21.99 | -41.33 | -16.34 | 0.68 | 0.68 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -13.82 | -13.26 | -44.33 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -1.06 | 1.63 | -1.06 | 6.86 | 4.28 | 11.31 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.58 | -0.12 | -6.19 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -5.14 | -7.52 | 4.83 | -13.38 | 8.21 | 15.31 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -3.68 | -3.37 | -19.78 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.98990000276115 | -3.02 | -5.7 | -4.04 | -20.75 | 2.82 | 26.39 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -2.79 | -3.05 | -17.15 | 23 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -6.95 | -8.17 | -7.87 | -16.37 | 1.26 | 4.07 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -8.42 | -7.17 | -16.49 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | -11.02 | -18.6 | -2.78 | 36.96 | 0.32 | 35.19 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -11.5 | -10.75 | -29.69 |  | fail_low_response_condition |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 19.16 | 166.15 | 259.62 | 606.61 | 291.3 | 751.81 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 40.16 | 38.85 | -14.93 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -15.97 | -29.74 | -24.16 | -37.46 | 1.19 | 1.19 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -24.2 | -21.94 | -40.67 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -7.73 | -17.48 | -14.71 | -14.71 | 1.0 | 1.0 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -15.94 | -13.76 | -24.54 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -8.73 | 7.81 | 14.24 | 15.0 | 13.86 | 19.38 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | -4.05 | -2.93 | -12.44 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -12.25 | -29.38 | -20.59 | -32.24 | 0.57 | 5.41 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -18.73 | -17.57 | -42.93 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -13.96 | -2.58 | 23.51 | 45.68 | 35.52 | 61.46 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -17.41 | -13.08 | -25.72 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -3.11 | 0.59 | -3.65 | -2.83 | 2.69 | 2.69 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -2.31 | -2.23 | -6.79 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -2.86 | -6.52 | 7.87 | 37.63 | 11.41 | 40.37 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -6.98 | -4.74 | -13.88 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | 0.33 | -8.61 | -8.88 | -13.48 | 0.33 | 0.33 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -5.3 | -5.14 | -12.99 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -2.09 | -8.7 | -20.07 | -18.76 | 5.06 | 5.06 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.92 | -5.29 | -23.76 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -3.99 | 0.39 | -12.68 | -10.66 | 1.58 | 1.58 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -2.0 | -4.03 | -21.33 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -1.68 | -5.85 | -0.92 | -15.04 | 1.74 | 1.74 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -4.55 | -4.25 | -11.05 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -1.77 | -3.58 | -8.45 | -5.7 | 0.0 | 0.0 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -3.33 | -3.34 | -12.28 | 16 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -4.33 | 7.67 | 15.73 | 17.94 | 16.17 | 22.62 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | -3.26 | -2.08 | -16.26 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -0.86 | 2.67 | 34.15 | 54.41 | 37.83 | 56.08 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -1.43 | -1.11 | -14.13 | 16 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | -2.81 | -2.26 | 5.34 | 2.07 | 7.63 | 11.09 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -2.79 | -2.44 | -12.42 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -2.24 | -2.48 | -7.09 | -2.72 | 0.0 | 0.0 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -2.01 | -2.1 | -10.27 | 13 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 11.53 | 16.14 | -0.84 | 34.7 | 31.11 | 48.99 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 15.47 | 12.76 | -2.96 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -7.78 | -16.72 | -13.84 | -18.36 | 0.4 | 0.4 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -10.86 | -10.55 | -32.7 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | 3.29 | 3.72 | 0.0 | 7.26 | 10.09 | 10.09 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 3.14 | 3.16 | -4.56 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 470.2347504677583 | 343.911329000345 | -3.19 | -13.7 | 11.49 | 1.89 | 7.06 | 50.62 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -5.66 | -6.76 | -23.98 | 16 | selected |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -15.94 | -30.95 | 22.36 | -5.69 | 23.54 | 59.56 | False |  | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -26.06 | -19.1 | -40.66 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -8.57 | -10.15 | -8.47 | 21.99 | 1.34 | 25.87 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -7.09 | -6.67 | -28.58 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -9.07 | -18.51 | -20.57 | -41.49 | 0.0 | 0.0 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -17.35 | -14.21 | -26.86 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -5.45 | -7.9 | -18.98 | -15.84 | 0.51 | 0.51 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -6.8 | -6.58 | -26.04 | 12 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -6.28 | -5.18 | -5.18 | -25.78 | 11.02 | 11.94 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -4.78 | -3.56 | -14.44 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -14.91 | -25.76 | -2.38 | 2.38 | 3.32 | 38.13 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -20.7 | -16.49 | -36.48 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -6.42 | -7.66 | 24.62 | -4.59 | 27.38 | 49.39 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -12.6 | -9.71 | -19.12 |  | fail_low_response_condition |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -1.87 | 0.48 | -0.47 | -0.47 | 3.45 | 3.45 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -1.15 | -1.05 | -7.89 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -1.56 | -4.7 | 15.21 | -15.85 | 20.85 | 26.22 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -1.02 | -0.57 | -8.53 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -8.7 | -14.66 | -16.15 | -13.13 | 0.84 | 0.84 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -11.97 | -10.21 | -21.59 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -8.78 | -31.68 | 30.65 | 41.01 | 33.29 | 63.43 | False |  | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -22.24 | -15.81 | -37.07 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -10.27 | -16.56 | -20.85 | -40.59 | 0.0 | 0.0 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -11.23 | -11.38 | -30.69 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -14.48 | -15.79 | 39.86 | 7.32 | 29.29 | 88.95 | True | 距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -16.26 | -12.68 | -24.68 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -5.91 | -5.29 | -26.08 | -32.36 | 0.35 | 0.35 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -6.64 | -6.2 | -28.65 | 13 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -7.35 | -7.35 | -9.49 | 27.9 | 2.32 | 33.71 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -5.36 | -4.96 | -14.32 | 21 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -8.69 | -15.06 | 20.03 | 21.94 | 22.52 | 25.33 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -18.15 | -11.81 | -35.44 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -9.83 | -3.6 | -9.83 | -4.75 | 1.58 | 2.88 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -8.18 | -6.89 | -19.75 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | 17.6 | -1.34 | -6.96 | -23.83 | 17.6 | 17.6 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.05 | 0.25 | -11.45 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -8.55 | -13.99 | 63.93 | 33.89 | 59.88 | 114.02 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -13.66 | -10.22 | -22.34 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -12.59 | -27.18 | -13.19 | -11.14 | 0.4 | 13.64 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -19.76 | -18.47 | -42.57 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -13.22 | -15.88 | -8.68 | -37.05 | 0.66 | 11.79 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -15.81 | -13.8 | -30.5 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | 2.99 | -12.22 | 45.6 | 79.35 | 54.94 | 115.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -9.18 | -5.53 | -18.88 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | -10.16 | -16.6 | -7.37 | -34.99 | 0.8 | 19.39 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -17.1 | -14.52 | -30.68 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 146.48689155577668 | 72.46425018776883 | -13.3 | -15.13 | -14.04 | -9.01 | 3.91 | 3.91 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -11.93 | -10.12 | -22.61 |  | fail_low_response_condition |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | -3.68 | 7.16 | 2.7 | 3.97 | 9.4 | 9.4 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.04 | 2.44 | -3.68 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -7.96 | -9.87 | -18.95 | -8.87 | 0.0 | 0.0 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -7.93 | -7.69 | -22.76 | 14 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | -3.81 | -5.66 | -1.17 | -19.91 | 2.19 | 9.0 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -3.56 | -4.38 | -11.98 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 84.69522628124143 | 51.25937713911443 | -10.36 | -12.79 | 7.66 | -37.85 | 8.17 | 25.7 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -14.35 | -12.04 | -22.41 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -3.42 | -6.35 | 0.3 | -4.24 | 0.0 | 3.35 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -5.66 | -4.47 | -13.08 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 21.59 | 59.59 | 84.54 | 54.43 | 89.64 | 118.29 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 37.59 | 31.51 | -10.0 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -13.01 | -19.79 | -5.22 | -21.12 | 0.79 | 17.59 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -12.57 | -12.05 | -26.16 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -11.13 | -18.74 | -13.92 | -29.95 | 0.28 | 3.49 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -14.15 | -12.04 | -23.05 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -3.88 | -6.21 | -4.83 | 44.39 | 4.66 | 43.75 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -5.1 | -4.57 | -14.89 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -3.33 | 12.53 | 14.82 | 31.82 | 19.83 | 33.91 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 2.1 | 1.95 | -10.96 | 13 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -7.12 | -3.69 | 15.66 | -13.29 | 14.04 | 35.37 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -8.97 | -6.8 | -16.84 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | B_可觀察 | 109.68927823663151 | 90.15073758650963 | -1.33 | -4.23 | 1.56 | -8.6 | 5.04 | 33.25 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -1.69 | -2.46 | -10.63 | 19 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth | A_優先追蹤 | 125.76660822131308 | 27.66392696281368 | -1.76 | -2.05 | 27.48 | -29.09 | 27.0 | 59.05 | False |  | mild_accumulation | 1.97 | 1.86 | 2 | 1 | -5.85 | -4.86 | -15.66 | 19 | selected |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth |  | 56.623935956655565 | 70.86506389755786 | -9.38 | -3.6 | -12.35 | -35.06 | 1.38 | 17.56 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -12.31 | -9.39 | -22.4 |  | fail_low_response_condition |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -6.91 | -11.32 | -12.92 | 10.49 | 0.0 | 16.21 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -7.61 | -7.18 | -15.75 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -8.13 | -1.48 | -6.55 | -15.04 | 0.17 | 0.17 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -2.74 | -2.91 | -8.41 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -1.16 | -2.97 | -7.61 | -7.61 | 0.0 | 3.91 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -2.22 | -2.2 | -8.8 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -14.52 | -16.0 | 31.29 | 70.62 | 30.31 | 89.42 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -15.75 | -14.06 | -31.7 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 3.51 | 14.56 | 50.0 | 12.03 | 53.25 | 60.91 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -3.92 | -0.23 | -16.71 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -10.7 | -26.15 | -24.11 | -13.9 | 0.52 | 0.52 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -15.33 | -13.92 | -35.35 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | -7.01 | -6.11 | -7.4 | -4.16 | 0.69 | 5.42 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -3.75 | -4.02 | -13.1 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -16.7 | -19.19 | -1.12 | 11.71 | 5.19 | 23.95 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -20.12 | -15.73 | -28.87 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -18.92 | -7.26 | 11.0 | 12.3 | 16.92 | 35.27 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -17.73 | -15.23 | -36.08 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -19.57 | -6.54 | 93.55 | 123.88 | 87.21 | 161.44 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -20.99 | -15.06 | -32.2 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | A_優先追蹤 | 55.69095387442037 | 42.29598437707936 | -0.49 | 6.88 | 34.67 | 65.57 | 44.29 | 66.94 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 2.86 | 2.92 | -0.98 | 19 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 64.04751148579548 | 40.914406890913945 | -10.75 | -13.59 | -19.41 | -22.33 | 0.0 | 2.01 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -15.47 | -13.02 | -24.63 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -7.13 | -20.62 | -7.37 | -38.28 | 0.42 | 13.11 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -9.98 | -9.69 | -28.54 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth | B_可觀察 | 50.70369959160158 | 35.171695901726686 | -1.15 | 14.41 | 11.44 | -6.06 | 22.73 | 30.52 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | 0.18 | 0.24 | -14.25 | 15 | selected |