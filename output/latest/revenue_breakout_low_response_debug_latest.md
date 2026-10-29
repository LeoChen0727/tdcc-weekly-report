# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-29 19:38:10 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 770725 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 91 |
| already_priced_in_excluded | 43 |
| overheat_pass | 48 |
| score_pass | 48 |
| theme_priority_pass | 43 |
| final_rows | 43 |

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
| fail_low_response_condition | 245 |
| fail_already_priced_in | 43 |
| fail_defensive_or_traditional_excluded | 3 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |
| fail_mainstream_score_lt_10 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | 5.41 | 31.09 | 115.17 | 240.98 | 95.61 | 288.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 4.67 | 7.28 | -10.98 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -4.01 | -1.71 | 31.65 | 21.61 | 28.7 | 43.79 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -6.88 | -5.37 | -24.87 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | 1.94 | 0.48 | 8.47 | -8.3 | 7.14 | 11.82 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | 0.62 | 0.26 | -16.0 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | 0.2 | -3.07 | 0.6 | -8.68 | 1.41 | 1.41 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -1.28 | -1.1 | -8.35 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 0.85 | -1.25 | -6.32 | -13.82 | 1.94 | 1.94 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -0.23 | -0.58 | -10.9 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 2.7 | 16.16 | 24.3 | 17.7 | 24.88 | 25.47 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 5.79 | 5.3 | -1.48 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -0.56 | -2.19 | -0.28 | -4.79 | 3.77 | 5.6 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -2.45 | -1.49 | -8.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -0.46 | 0.23 | -7.11 | -0.69 | 2.86 | 10.51 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.3 | -0.61 | -9.83 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 1.91 | 4.63 | 7.1 | 9.5 | 10.73 | 26.18 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 2.23 | 2.0 | -3.61 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -0.74 | -1.84 | -1.84 | -14.42 | 0.75 | 0.75 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -0.45 | -0.65 | -5.65 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -2.04 | -3.61 | 1.69 | -15.49 | 1.27 | 2.13 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -3.48 | -2.79 | -10.11 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 42.86 | 51.72 | 39.68 | 6.54 | 71.21 | 71.21 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 42.53 | 33.09 | -16.51 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 1.13 | 0.94 | -0.19 | 1.32 | 5.07 | 5.07 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | 0.36 | -0.13 | -11.06 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | 4.33 | 8.24 | 38.94 | -20.6 | 31.96 | 41.67 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -0.74 | 0.47 | -11.89 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -6.54 | 13.33 | 41.67 | 81.96 | 40.0 | 91.94 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | -3.68 | -1.97 | -14.59 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -1.23 | 0.0 | -4.39 | -0.37 | 1.26 | 3.6 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -2.09 | -2.18 | -11.44 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -2.91 | -0.89 | 3.73 | -11.05 | 5.7 | 7.74 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -2.33 | -2.27 | -10.09 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576107 | 74.19480655845219 | -1.43 | -1.71 | -0.29 | -25.97 | 1.17 | 1.17 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -2.76 | -2.66 | -14.81 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.779802186364 | 14769.518174623092 | 7.1 | 15.83 | 13.87 | 27.85 | 18.62 | 31.73 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 9.15 | 6.91 | -2.25 | 17 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 163.02984286280207 | 139.012352909764 | -4.07 | -1.15 | 7.92 | 10.68 | 10.21 | 15.62 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -5.25 | -3.4 | -13.67 | 19 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -2.18 | -20.0 | 38.38 | 78.99 | 27.32 | 122.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -8.95 | -8.53 | -34.5 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | 0.0 | -5.12 | -18.03 | -33.24 | 0.0 | 0.0 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -5.66 | -5.29 | -27.84 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -2.85 | -3.02 | -10.79 | -13.84 | 1.05 | 1.05 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -2.36 | -2.89 | -20.14 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -11.83 | -1.99 | 23.46 | 127.25 | 25.99 | 135.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -11.76 | -9.27 | -20.65 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | 1.66 | 0.16 | -2.55 | 8.72 | 4.09 | 18.41 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -0.4 | -0.16 | -5.86 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -6.76 | -18.92 | 85.12 | 190.6 | 98.44 | 224.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -14.29 | -7.65 | -31.73 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | 0.42 | -2.42 | 9.52 | 8.05 | 4.55 | 10.78 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -2.44 | -1.37 | -6.76 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | 0.0 | -14.53 | 8.93 | -37.3 | 0.81 | 8.93 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -9.65 | -8.63 | -30.8 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | 11.8 | -0.58 | 43.88 | 45.11 | 31.15 | 52.23 | True | 近60日漲幅>40% | distribution_warning | -1.13 | -1.08 | 2 | 2 | 1.13 | 2.02 | -11.66 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -10.91 | -7.39 | -9.3 | -32.24 | 0.86 | 0.86 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -9.31 | -8.43 | -32.37 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | 3.03 | 7.94 | 18.47 | 18.06 | 19.86 | 27.02 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 2.99 | 3.79 | -1.92 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -0.29 | -3.06 | -8.52 | -1.69 | 4.49 | 4.49 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -0.94 | -1.31 | -11.65 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | 0.77 | -10.25 | 47.57 | 3.41 | 39.72 | 58.87 | True | 近60日漲幅>40% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -5.36 | -5.69 | -23.35 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 2.33 | 2.5 | 6.78 | 22.31 | 9.06 | 28.59 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 3.25 | 1.35 | -16.46 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 206.46824005093208 | 119.5343671101157 | -2.75 | -15.25 | 1.83 | -17.58 | 5.42 | 12.43 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -9.04 | -7.58 | -24.02 | 16 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -5.91 | 0.9 | 54.65 | -20.36 | 42.22 | 58.16 | True | 近60日漲幅>40% | distribution_warning | -0.79 | -0.57 | 1 | 1 | -5.79 | -3.52 | -14.89 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -3.38 | -5.12 | 7.69 | 5.7 | 9.24 | 14.33 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -4.84 | -3.95 | -14.68 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -0.78 | -6.06 | 13.98 | -7.42 | 11.97 | 13.98 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -2.58 | -2.73 | -9.53 | 15 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 168.87284393304373 | 103.69258923500948 | 1.31 | -0.79 | 16.11 | 3.3 | 8.09 | 27.48 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -5.54 | -3.87 | -22.57 | 22 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | -1.61 | -6.79 | 23.03 | 40.65 | 24.63 | 53.3 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -4.77 | -3.07 | -10.74 | 17 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | 6.38 | -1.64 | 5.82 | -14.89 | 16.05 | 16.05 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -0.44 | 1.06 | -9.91 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | 13.03 | -5.17 | 45.43 | 58.47 | 32.32 | 79.66 | True | 近60日漲幅>40% | distribution_warning | -0.15 | -0.24 | 1 | 1 | -1.21 | 0.53 | -16.17 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -4.85 | -12.45 | -24.24 | -1.67 | 0.47 | 1.25 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -8.17 | -7.53 | -38.85 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | 1.79 | 4.22 | 1.07 | 3.27 | 5.58 | 12.7 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 0.87 | 1.07 | -5.02 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | 1.06 | -2.56 | 15.5 | -15.93 | 13.43 | 18.75 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -1.87 | -1.45 | -17.39 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 290.42308535778307 | 369.98990000276115 | 9.09 | 3.34 | 9.09 | -14.41 | 10.73 | 36.11 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | 4.27 | 4.27 | -10.77 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -5.21 | -0.66 | 6.19 | -9.09 | 7.33 | 11.11 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -2.92 | -2.27 | -10.85 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | 2.34 | -10.49 | 42.86 | 45.83 | 33.08 | 59.09 | True | 近60日漲幅>40% | distribution_warning | -3.44 | -5.05 | 0 | 0 | -4.1 | -3.14 | -21.88 |  | fail_already_priced_in |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 42.48 | 169.46 | 247.36 | 524.03 | 268.42 | 701.99 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 54.42 | 51.24 | -6.26 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -3.62 | -12.0 | 5.08 | -21.1 | 3.79 | 8.26 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -11.02 | -9.21 | -27.6 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -6.17 | -6.94 | 8.06 | -4.6 | 5.56 | 13.43 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -7.51 | -5.76 | -15.24 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | 0.83 | 13.66 | 15.46 | 22.41 | 23.23 | 26.64 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 3.48 | 3.2 | -7.11 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -3.37 | -14.1 | 17.54 | -28.6 | 11.05 | 20.72 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -10.33 | -8.94 | -34.63 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | 14.63 | 35.79 | 113.1 | 146.65 | 94.04 | 152.54 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 10.81 | 13.07 | -1.97 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -0.84 | 3.79 | 1.14 | 0.85 | 6.59 | 6.59 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 1.76 | 1.25 | -3.26 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | 2.0 | 0.94 | 19.36 | 40.9 | 17.48 | 48.01 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -2.5 | -0.22 | -9.19 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -2.43 | -3.89 | -6.69 | -14.4 | 4.56 | 4.56 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -2.42 | -2.19 | -9.32 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -1.6 | -6.02 | -21.82 | -10.58 | 8.48 | 8.48 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -3.77 | -3.32 | -25.49 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -1.74 | -0.13 | -11.05 | -5.28 | 3.95 | 3.95 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | 0.44 | -2.7 | -19.49 | 12 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | 1.35 | -1.32 | 3.21 | -13.35 | 6.64 | 6.64 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -0.57 | -0.4 | -6.77 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 157.1373893517917 | 73.07026244678458 | -1.52 | -1.32 | -6.38 | -5.46 | 0.94 | 0.94 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -1.08 | -1.37 | -9.86 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | 0.0 | 16.01 | 24.43 | 18.98 | 23.48 | 29.37 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 3.64 | 3.54 | -11.65 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -1.71 | -0.43 | 36.26 | 46.5 | 37.23 | 56.46 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -1.12 | -1.19 | -14.5 | 16 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | -0.42 | -1.95 | 8.13 | 2.92 | 9.81 | 13.34 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.96 | -0.7 | -10.65 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.5 | -1.49 | -7.66 | -2.93 | 0.0 | 1.02 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -1.01 | -1.28 | -9.55 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 7.94 | 9.05 | -28.18 | -4.85 | 17.78 | 33.84 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 6.02 | 4.28 | -26.8 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -2.7 | -10.15 | 0.93 | -8.63 | 1.31 | 2.08 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -5.52 | -5.22 | -27.03 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | -1.23 | 2.99 | -3.98 | 5.24 | 5.7 | 7.59 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | -0.39 | -0.36 | -10.74 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | 22.03 | 2.73 | 72.26 | 27.25 | 56.94 | 75.47 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -5.51 | -6.04 | 0 | 0 | 8.39 | 8.51 | -11.44 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -10.26 | -15.31 | 82.12 | 5.45 | 76.2 | 86.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -17.33 | -9.39 | -30.69 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -1.34 | -4.94 | 5.99 | 28.26 | 7.8 | 33.89 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -2.31 | -1.92 | -24.03 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -3.93 | -0.37 | 8.03 | -32.24 | 4.26 | 9.8 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -7.25 | -4.87 | -16.46 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | 0.84 | 0.72 | 0.0 | -4.32 | 4.6 | 4.6 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -0.31 | -0.51 | -20.27 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | 3.13 | 3.38 | 16.62 | -19.09 | 17.91 | 18.89 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | 0.82 | 1.73 | -9.13 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -1.42 | -12.24 | 45.25 | 20.79 | 32.15 | 59.26 | True | 近60日漲幅>40% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -11.17 | -6.8 | -26.76 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -5.47 | -0.37 | 56.73 | 9.5 | 50.56 | 63.91 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -4.51 | -2.68 | -11.26 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.47 | 2.4 | 1.91 | -0.47 | 4.93 | 4.93 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 0.54 | 0.33 | -6.58 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 3.79 | -1.54 | 26.23 | -17.39 | 22.34 | 27.78 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -0.38 | 0.61 | -7.41 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -2.55 | 0.94 | 5.51 | -6.13 | 5.1 | 7.41 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -3.78 | -2.29 | -12.99 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -2.34 | 0.0 | 71.29 | 75.73 | 59.71 | 91.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -11.79 | -4.24 | -26.12 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth | A_優先追蹤 | 132.5343403041849 | 228.6135135135135 | 7.22 | -5.11 | 6.45 | -23.65 | 7.61 | 10.82 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -1.41 | -1.77 | -21.43 | 19 | selected |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -2.57 | -0.32 | 114.03 | 29.95 | 105.43 | 117.72 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -3.95 | -1.03 | -13.21 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 90.47990444398276 | 46.685682375869504 | 0.44 | -0.55 | -12.91 | -24.71 | 3.17 | 3.17 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -1.46 | -1.74 | -24.34 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -0.26 | 2.17 | 17.81 | 35.61 | 13.9 | 42.8 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | 0.56 | 0.63 | -8.5 | 23 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 446.4684953621241 | 68.26830170354926 | -9.63 | 11.04 | 33.91 | 28.81 | 34.98 | 38.07 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -10.38 | -5.44 | -28.87 | 21 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -3.63 | 7.14 | 8.15 | 0.58 | 9.18 | 10.58 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -1.15 | -1.12 | -13.75 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | 8.24 | 2.72 | -2.27 | -27.4 | 20.8 | 20.8 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 4.99 | 5.44 | -8.48 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -1.36 | -10.38 | 120.81 | 33.33 | 100.79 | 140.63 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -4.23 | -0.45 | -12.69 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | 0.58 | -15.59 | 27.92 | 1.17 | 18.79 | 31.21 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -10.82 | -9.46 | -33.69 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -7.24 | -1.47 | 24.25 | -30.87 | 13.56 | 26.78 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -6.13 | -4.97 | -21.18 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -3.68 | -7.44 | 104.31 | 59.53 | 92.34 | 128.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -4.97 | -0.54 | -13.91 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.99846620911757 | 44.59053152341543 | 1.1 | -2.39 | 32.14 | -31.53 | 24.96 | 39.92 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -4.39 | -2.68 | -18.76 | 15 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | B_可觀察 | 146.48689155577668 | 72.46425018776883 | -3.08 | -6.38 | 4.27 | -3.51 | 13.17 | 13.17 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -5.44 | -4.04 | -15.71 | 20 | selected |
| 3703 | 欣陸 | 建材營造 | neutral |  | 89.3174912383306 | 3.4475931972039313 | 0.97 | 5.32 | 0.97 | 0.24 | 8.62 | 8.62 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.33 | 2.39 | -4.37 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -1.49 | 1.27 | -5.47 | -8.41 | 2.45 | 2.45 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -1.85 | -2.4 | -17.01 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 9.82 | 4.31 | 18.45 | -14.4 | 15.56 | 21.5 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | 7.47 | 6.74 | -1.89 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 84.69522628124143 | 51.25937713911443 | 1.93 | 7.32 | 45.21 | -27.27 | 35.25 | 47.49 | True | 近60日漲幅>40% | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -0.43 | 0.93 | -8.97 |  | fail_already_priced_in |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -1.69 | -2.23 | 5.74 | -0.85 | 6.38 | 6.71 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -3.42 | -2.39 | -10.26 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 52.6 | 66.3 | 109.52 | 49.79 | 99.25 | 109.94 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 44.22 | 40.19 | -3.3 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | 10.1 | -0.67 | 35.87 | -10.78 | 28.45 | 37.96 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | 0.04 | 1.02 | -13.37 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -3.68 | -1.26 | 13.6 | -17.8 | 6.66 | 14.26 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -7.35 | -5.43 | -15.04 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 70.3115141167771 | 63.02464404154338 | 2.97 | 1.46 | 17.51 | 55.22 | 12.68 | 60.74 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 1.7 | 2.24 | -8.37 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -0.48 | 14.46 | 29.81 | 25.3 | 26.21 | 37.86 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 7.04 | 5.79 | -8.33 | 14 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -1.64 | 4.29 | 41.45 | -18.45 | 33.91 | 44.07 | True | 近60日漲幅>40% | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -3.35 | -2.17 | -11.49 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663151 | 90.15073758650963 | 15.29 | 5.14 | 34.82 | 0.7 | 29.05 | 46.55 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | 8.0 | 7.69 | -1.72 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | 7.31 | 8.9 | 72.3 | -25.41 | 63.84 | 74.76 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 3.89 | 4.29 | -7.32 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -6.98 | 7.74 | 25.49 | -32.35 | 17.86 | 27.74 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -4.77 | -3.66 | -15.68 | 18 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -0.82 | -3.2 | -2.16 | 17.48 | 1.97 | 25.17 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -1.53 | -1.34 | -9.25 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 262.471963434005 | 110.54580308622074 | -1.61 | 0.66 | -6.57 | -15.96 | 2.17 | 2.17 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -0.88 | -1.58 | -8.53 | 22 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | 0.46 | -1.36 | -4.41 | -7.26 | 2.12 | 6.11 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -0.49 | -0.52 | -6.87 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -16.08 | -3.28 | 71.28 | 50.68 | 72.46 | 116.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -5.3 | -4.38 | -21.96 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | -0.53 | 26.0 | 71.82 | 27.27 | 67.26 | 71.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 5.2 | 7.53 | -11.06 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | 0.0 | -19.32 | -15.14 | 14.89 | 3.9 | 14.27 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -9.86 | -7.21 | -28.28 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -0.88 | -2.71 | -5.27 | -4.46 | 0.45 | 8.18 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.86 | -2.27 | -10.81 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -4.38 | 0.35 | 30.05 | 33.41 | 23.26 | 44.46 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -8.23 | -4.75 | -17.11 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -16.43 | 17.15 | 61.66 | 42.25 | 52.44 | 65.08 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 0.55 | 0.86 | -22.0 |  | fail_already_priced_in |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -0.53 | 25.21 | 211.06 | 147.92 | 183.27 | 224.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -1.51 | 2.82 | -15.82 |  | fail_already_priced_in |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 2.8 | 6.04 | 40.77 | 59.06 | 44.29 | 66.94 | True | 近60日漲幅>40% | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 3.9 | 3.77 | -0.98 |  | fail_already_priced_in |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | -8.08 | -4.41 | 11.52 | -12.16 | 5.32 | 14.04 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -6.82 | -5.45 | -15.74 | 18 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -1.12 | -4.46 | 23.36 | -31.72 | 14.78 | 25.12 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -4.01 | -2.06 | -20.96 |  | fail_low_response_condition |