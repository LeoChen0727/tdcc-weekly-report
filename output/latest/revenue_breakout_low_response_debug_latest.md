# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-28 19:38:02 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 768765 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 91 |
| already_priced_in_excluded | 34 |
| overheat_pass | 57 |
| score_pass | 57 |
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
| fail_revenue_condition | 1636 |
| fail_low_response_condition | 245 |
| fail_already_priced_in | 34 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | 5.11 | 40.22 | 125.44 | 260.05 | 135.42 | 296.77 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 8.37 | 10.42 | -8.99 |  | fail_low_response_condition |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -3.62 | 0.34 | 31.98 | 26.29 | 35.65 | 46.79 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -5.01 | -3.86 | -23.3 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | 2.88 | 0.94 | 11.46 | -4.46 | 11.92 | 13.95 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | 2.56 | 2.19 | -14.4 | 15 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | 0.99 | -2.86 | -1.16 | -9.41 | 2.41 | 2.41 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -0.46 | -0.22 | -7.44 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 1.92 | -1.85 | -3.83 | -13.59 | 2.58 | 2.58 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 0.34 | 0.0 | -10.34 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 2.28 | 16.96 | 25.12 | 19.03 | 26.29 | 26.89 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 7.77 | 7.0 | -0.37 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -1.63 | -0.82 | -1.9 | -5.24 | 4.93 | 6.78 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -1.47 | -0.52 | -7.65 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.23 | -0.23 | -2.7 | 5.87 | 3.34 | 13.35 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | 0.17 | -0.2 | -11.45 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 0.51 | 3.53 | 9.12 | 10.98 | 10.36 | 25.75 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 2.12 | 1.83 | -3.93 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -0.37 | -1.83 | -1.83 | -15.19 | 1.13 | 1.13 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -0.17 | -0.34 | -5.3 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -1.63 | -2.03 | 2.12 | -6.95 | 2.12 | 2.55 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -3.25 | -2.63 | -9.74 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 60.71 | 56.25 | 43.31 | 11.66 | 75.1 | 75.1 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 49.4 | 40.33 | -14.61 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 0.19 | -0.19 | -5.51 | 1.53 | 3.7 | 3.7 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -0.89 | -1.43 | -12.21 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround | B_可觀察 | 62.31587090838761 | 46.95702744919681 | 4.56 | 11.61 | 36.07 | -13.87 | 46.08 | 46.08 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | 2.74 | 3.65 | -9.15 | 16 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -1.6 | 16.46 | 39.39 | 99.35 | 47.79 | 97.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | -0.15 | 0.87 | -11.96 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -2.64 | 0.62 | -1.34 | 1.63 | 2.14 | 4.5 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -1.23 | -1.53 | -10.67 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -2.18 | 0.0 | 3.38 | -13.29 | 8.39 | 8.39 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -1.79 | -1.89 | -9.56 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576107 | 74.19480655845219 | -1.14 | -1.97 | -0.85 | -26.43 | 2.05 | 2.05 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -2.0 | -2.05 | -14.07 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.779802186364 | 14769.518174623092 | 7.04 | 16.77 | 18.63 | 30.93 | 20.16 | 32.8 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 10.86 | 8.46 | -1.46 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 163.02984286280207 | 139.012352909764 | 4.51 | 9.88 | 11.65 | 23.01 | 18.3 | 24.11 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | 1.65 | 3.37 | -7.33 | 21 | selected |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | 2.32 | -18.08 | 42.06 | 90.79 | 48.39 | 128.09 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -7.51 | -6.75 | -32.71 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -1.61 | -3.92 | -18.06 | -31.56 | 1.66 | 1.66 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -4.33 | -4.17 | -26.65 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -4.46 | -3.83 | -10.39 | -16.23 | 0.87 | 0.87 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -2.68 | -3.31 | -20.28 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -5.59 | 5.26 | 22.03 | 126.89 | 38.28 | 158.37 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -3.23 | -1.25 | -12.9 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -0.16 | -0.98 | -6.05 | 5.57 | 3.24 | 17.44 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -1.21 | -0.99 | -6.91 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -2.88 | -15.09 | 96.72 | 203.37 | 110.12 | 243.95 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -10.15 | -2.89 | -27.71 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | 0.21 | -3.0 | 10.23 | 5.9 | 10.73 | 11.24 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -2.16 | -1.08 | -6.37 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 188.23580475843863 | 154.50791645548554 | 1.47 | -13.03 | 1.47 | -32.35 | 12.75 | 12.75 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -7.2 | -6.17 | -28.37 | 14 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | 10.61 | -0.29 | 32.31 | 60.75 | 47.01 | 53.57 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | 1.99 | 3.1 | -10.88 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 66.12554142816796 | 62.44981435880206 | -9.48 | -3.97 | -4.97 | -23.58 | 4.31 | 4.31 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -6.55 | -6.02 | -30.06 | 16 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | 1.49 | 8.47 | 20.02 | 24.7 | 21.16 | 27.65 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 3.89 | 4.66 | -1.44 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | 0.71 | -3.29 | -6.12 | -0.42 | 5.69 | 5.69 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | 0.04 | -0.3 | -10.63 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | 1.99 | -9.07 | 57.47 | 12.3 | 65.73 | 65.73 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -1.8 | -2.13 | -20.04 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 7.95 | 4.59 | 5.8 | 28.76 | 13.32 | 33.61 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 7.43 | 5.44 | -13.2 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 206.46824005093208 | 119.5343671101157 | 1.5 | -12.47 | 10.9 | -8.74 | 15.3 | 17.63 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -5.6 | -3.96 | -20.51 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -5.2 | 3.95 | 62.55 | -10.9 | 68.09 | 68.09 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.79 | -0.57 | 1 | 1 | 0.17 | 2.21 | -9.54 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | 2.98 | -0.68 | 12.75 | 14.35 | 16.19 | 20.83 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | 0.31 | 1.15 | -9.83 | 24 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | 4.93 | -3.37 | 6.62 | -3.08 | 18.28 | 18.28 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | 0.78 | 0.69 | -6.12 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 168.87284393304373 | 103.69258923500948 | -1.95 | 0.1 | 22.56 | 5.79 | 27.86 | 27.86 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -5.29 | -3.92 | -22.33 | 22 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | 1.47 | -1.71 | 25.27 | 44.6 | 28.79 | 56.95 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -2.84 | -1.04 | -8.62 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | 6.89 | 1.17 | 5.22 | -8.33 | 17.02 | 17.02 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | 0.31 | 2.0 | -9.16 | 14 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | 9.4 | -7.38 | 34.94 | 74.09 | 48.14 | 79.66 | True | 近120日漲幅>70% | distribution_warning | -0.15 | -0.24 | 1 | 1 | -1.48 | 0.58 | -16.17 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -3.23 | -11.05 | -25.25 | 6.97 | 2.48 | 3.29 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -6.93 | -6.31 | -37.62 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | 0.0 | 3.85 | 2.54 | 2.54 | 5.2 | 12.3 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 0.72 | 0.81 | -5.35 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | 0.0 | -3.29 | 15.06 | -18.03 | 17.9 | 19.38 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -1.48 | -1.07 | -16.96 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 290.42308535778307 | 369.98990000276115 | 8.91 | 3.16 | 8.91 | -6.08 | 12.88 | 35.88 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | 4.27 | 4.5 | -10.93 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -2.72 | -1.14 | 5.0 | -4.84 | 9.14 | 12.78 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -1.5 | -1.0 | -9.51 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | 4.06 | -7.95 | 45.93 | 47.13 | 51.48 | 63.18 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -3.44 | -5.05 | 0 | 0 | -2.18 | -0.93 | -19.87 |  | fail_already_priced_in |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 39.6 | 177.97 | 251.34 | 525.99 | 260.98 | 685.8 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 59.02 | 55.43 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -2.44 | -8.24 | 3.9 | -10.8 | 11.4 | 11.4 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -9.0 | -7.35 | -25.51 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -8.06 | -6.56 | 7.55 | 1.79 | 11.22 | 13.43 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -7.82 | -6.25 | -15.24 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | 4.71 | 17.39 | 21.15 | 27.7 | 27.27 | 30.8 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 7.54 | 6.9 | -4.06 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 56.830680809905594 | 32.980802133096326 | -3.04 | -10.78 | 12.2 | -26.47 | 24.32 | 24.32 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -8.33 | -6.98 | -32.68 | 11 | selected |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | 9.34 | 30.07 | 80.5 | 155.13 | 100.5 | 162.71 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 5.81 | 7.67 | -7.76 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -0.28 | 4.08 | -0.28 | 0.56 | 6.89 | 6.89 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 2.23 | 1.65 | -2.99 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | 2.93 | 1.55 | 18.01 | 41.85 | 22.26 | 50.31 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -0.94 | 1.31 | -7.79 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -3.04 | -5.9 | -7.27 | -14.93 | 3.91 | 3.91 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -3.22 | -2.99 | -9.89 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -6.3 | -8.66 | -21.54 | -11.6 | 6.83 | 6.83 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.53 | -5.08 | -26.62 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -2.75 | -1.77 | -10.17 | -2.87 | 2.37 | 2.37 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -1.09 | -4.42 | -20.71 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | 0.74 | -0.29 | 2.73 | -12.97 | 7.11 | 7.11 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -0.2 | 0.0 | -6.35 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -1.62 | -2.21 | -5.17 | -5.63 | 1.25 | 1.25 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -0.84 | -1.19 | -9.58 | 17 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -0.3 | 15.9 | 22.39 | 22.39 | 25.19 | 30.16 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 5.03 | 4.51 | -11.11 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | 0.0 | 4.41 | 39.41 | 54.9 | 41.41 | 61.22 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 1.87 | 1.71 | -11.9 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | 0.28 | 0.56 | 8.54 | 5.17 | 10.9 | 14.47 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.07 | 0.22 | -9.76 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.25 | -1.72 | -6.98 | -2.91 | 0.0 | 1.52 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.58 | -0.9 | -9.09 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 4.32 | 7.98 | -32.32 | -1.77 | 23.33 | 40.15 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 11.51 | 9.62 | -37.15 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -2.85 | -6.83 | 0.55 | -2.15 | 2.82 | 3.21 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -4.98 | -4.62 | -26.22 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | 0.0 | 2.97 | -7.95 | 3.85 | 6.58 | 8.48 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 0.58 | 0.43 | -10.0 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | 15.27 | 0.55 | 60.17 | 36.39 | 71.12 | 71.12 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -5.51 | -6.04 | 0 | 0 | 5.86 | 6.64 | -13.64 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -6.69 | -4.12 | 80.47 | 19.23 | 91.88 | 91.88 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -15.52 | -7.51 | -28.64 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | 2.7 | 0.77 | 3.86 | 24.02 | 11.46 | 38.28 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | 0.63 | 1.11 | -21.55 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.01687411836724 | 29.7636013582763 | -3.99 | 4.54 | 8.43 | -29.01 | 12.86 | 12.86 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -4.68 | -2.65 | -14.13 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | 0.95 | 1.92 | -2.42 | -3.31 | 5.34 | 5.34 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | 0.43 | 0.15 | -19.7 | 14 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | 5.6 | 5.34 | 17.62 | -9.77 | 20.22 | 20.56 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | 2.41 | 3.32 | -7.86 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -1.79 | -5.17 | 59.88 | 34.47 | 68.45 | 68.45 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -6.62 | -2.02 | -22.54 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -5.72 | 0.18 | 60.24 | 13.1 | 63.86 | 66.36 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -3.1 | -1.46 | -9.93 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.93 | 2.4 | 1.43 | 0.0 | 4.93 | 4.93 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 0.66 | 0.36 | -6.58 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 6.95 | 2.56 | 25.0 | -14.77 | 33.33 | 33.33 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | 3.87 | 5.04 | -3.38 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -1.09 | 3.04 | 3.63 | -3.21 | 7.75 | 8.62 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -2.66 | -1.4 | -12.01 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -0.54 | 2.58 | 81.14 | 80.26 | 85.98 | 96.82 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -9.52 | -2.15 | -24.22 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | 5.32 | -6.6 | 0.34 | -16.1 | 7.61 | 10.82 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -1.67 | -1.93 | -21.43 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | 4.15 | 15.73 | 113.47 | 50.58 | 137.05 | 137.05 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | 4.56 | 7.66 | -5.5 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | 1.97 | 1.75 | -12.83 | -15.36 | 5.44 | 5.44 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | 0.68 | 0.25 | -22.67 | 15 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 87.1863428539576 | 97.24836000846553 | 8.06 | 8.06 | 14.75 | 32.76 | 23.49 | 47.35 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | 3.87 | 3.89 | -5.58 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 446.4684953621241 | 68.26830170354926 | -4.67 | 22.48 | 39.81 | 38.73 | 43.61 | 46.9 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -4.22 | 0.11 | -24.33 | 23 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -0.28 | 10.28 | 6.95 | 0.85 | 12.03 | 13.46 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | 1.77 | 1.35 | -11.5 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | -3.85 | -8.03 | -19.12 | -34.68 | 10.0 | 10.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.26 | -3.51 | -18.15 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | 4.34 | -2.56 | 147.95 | 56.81 | 157.32 | 157.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | 1.85 | 6.42 | -6.63 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -0.56 | -15.1 | 21.12 | 7.68 | 33.79 | 33.79 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -9.81 | -8.47 | -32.39 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -7.27 | 5.35 | 21.77 | -29.49 | 31.88 | 31.88 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -2.42 | -1.6 | -18.01 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -2.82 | -0.55 | 92.6 | 74.66 | 105.65 | 127.68 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -5.77 | -1.05 | -14.31 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.99846620911757 | 44.59053152341543 | 2.29 | 1.06 | 35.47 | -22.29 | 44.49 | 44.49 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -1.39 | 0.25 | -16.11 | 17 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | 1.31 | 1.75 | 9.43 | 2.2 | 19.34 | 19.34 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -0.6 | 0.83 | -11.11 | 23 | selected |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | 1.46 | 5.03 | 2.2 | 0.97 | 9.14 | 9.14 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 4.1 | 3.1 | -3.91 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | 0.87 | 3.05 | -5.04 | -6.03 | 4.38 | 4.38 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | 0.07 | -0.78 | -15.45 | 18 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 11.17 | 6.15 | 17.48 | -12.66 | 19.79 | 20.91 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | 7.19 | 6.88 | -2.36 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -0.37 | 6.37 | 36.22 | -26.04 | 49.16 | 49.16 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | 1.04 | 2.17 | -7.93 | 23 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -1.69 | -1.96 | 5.42 | -1.69 | 6.38 | 6.71 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -3.53 | -2.6 | -10.26 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 39.27 | 59.13 | 80.22 | 43.91 | 97.42 | 97.42 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 39.63 | 36.83 | 0.0 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | 11.25 | 1.79 | 29.26 | -0.22 | 40.43 | 40.43 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | 1.8 | 2.92 | -11.82 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -1.7 | 0.87 | 13.01 | -7.02 | 17.44 | 17.61 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -4.69 | -3.14 | -12.55 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | 2.48 | -0.96 | 14.75 | 66.94 | 17.61 | 65.34 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 1.29 | 1.96 | -8.81 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth |  | 86.87811970952995 | 13.790026773850077 | 5.88 | 18.29 | 31.71 | 27.96 | 36.54 | 42.48 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 11.37 | 9.91 | -5.26 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | 1.12 | 10.19 | 40.31 | -13.45 | 50.19 | 50.19 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.38 | -0.18 | 1 | 0 | 0.95 | 1.78 | -7.74 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663151 | 90.15073758650963 | 10.26 | 2.76 | 27.92 | -6.21 | 34.05 | 42.97 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | 5.64 | 5.79 | -4.12 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | 6.86 | 12.31 | 66.96 | -17.98 | 78.1 | 78.1 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 6.33 | 6.7 | -4.35 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -3.2 | 11.19 | 20.0 | -29.67 | 32.93 | 32.93 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -0.56 | -0.08 | -12.25 | 18 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | 1.11 | -3.7 | -0.55 | 19.74 | 2.25 | 25.52 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -1.42 | -1.19 | -9.0 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 262.471963434005 | 110.54580308622074 | 3.39 | 5.25 | -2.29 | -8.43 | 7.19 | 7.19 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 4.02 | 3.11 | -4.04 | 23 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | 0.23 | -2.03 | -5.64 | -7.45 | 2.35 | 6.36 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -0.33 | -0.34 | -6.65 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -9.42 | 2.12 | 72.31 | 59.82 | 90.97 | 128.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -0.17 | 0.57 | -17.6 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 6.02 | 22.92 | 63.72 | 37.04 | 68.18 | 68.18 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 4.11 | 5.98 | -12.94 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 50.50424657170375 | 42.64176748510076 | 6.57 | -10.28 | -18.35 | 30.01 | 10.73 | 32.59 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -4.96 | -1.75 | -23.57 | 15 | selected |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | -0.11 | -2.9 | -4.14 | -3.53 | 0.67 | 8.66 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.56 | -2.03 | -10.42 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -1.0 | 7.83 | 32.44 | 44.39 | 38.64 | 50.83 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -4.17 | -0.97 | -13.45 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -0.98 | 29.49 | 60.32 | 53.03 | 78.13 | 78.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 9.31 | 8.92 | -15.83 |  | fail_already_priced_in |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | 1.43 | 43.81 | 212.45 | 170.61 | 228.27 | 239.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | 3.88 | 7.64 | -12.09 |  | fail_already_priced_in |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 2.04 | 5.53 | 39.24 | 59.76 | 43.21 | 65.7 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 3.43 | 3.36 | -1.72 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | -4.06 | 2.83 | 9.49 | -4.44 | 18.55 | 18.55 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -3.34 | -2.19 | -12.41 | 17 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | 2.28 | -3.01 | 19.05 | -37.42 | 27.33 | 27.33 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -2.53 | -0.52 | -19.56 |  | fail_low_response_condition |