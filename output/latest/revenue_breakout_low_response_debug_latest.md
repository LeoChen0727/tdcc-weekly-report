# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-27 19:35:59 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 766797 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 103 |
| already_priced_in_excluded | 38 |
| overheat_pass | 65 |
| score_pass | 65 |
| theme_priority_pass | 58 |
| final_rows | 58 |

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
| fail_low_response_condition | 233 |
| fail_already_priced_in | 38 |
| fail_defensive_or_traditional_excluded | 5 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -3.09 | 28.51 | 89.49 | 229.46 | 119.56 | 270.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 2.66 | 3.96 | -15.12 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -8.67 | 0.34 | 27.71 | 21.9 | 36.57 | 47.8 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -4.35 | -3.54 | -22.77 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | -1.9 | -1.9 | 3.6 | -8.81 | 10.22 | 10.22 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -0.74 | -0.95 | -17.2 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | 0.59 | -3.05 | -2.31 | -12.41 | 2.01 | 2.01 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -0.99 | -0.63 | -7.8 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 0.85 | -2.68 | -4.84 | -15.71 | 1.51 | 1.51 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -0.81 | -1.05 | -11.28 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 0.76 | 16.67 | 23.15 | 17.7 | 25.47 | 25.47 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 7.41 | 6.48 | -1.48 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -0.27 | 4.9 | -2.15 | -3.7 | 5.51 | 7.37 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -0.97 | -0.02 | -7.14 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -0.23 | 0.23 | -0.68 | 8.21 | 3.82 | 13.87 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | 0.62 | 0.24 | -11.04 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | -1.02 | -1.19 | 8.41 | 9.02 | 12.84 | 24.46 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 1.25 | 0.96 | -4.92 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -1.48 | -2.56 | -2.92 | -15.56 | 0.38 | 0.38 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -1.0 | -1.11 | -6.01 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -4.78 | -3.24 | -2.45 | -8.78 | 1.7 | 1.7 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -4.15 | -3.67 | -10.49 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 83.82 | 78.57 | 52.44 | 24.38 | 94.55 | 94.55 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 70.59 | 61.86 | -5.12 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -2.23 | -1.68 | -6.89 | 1.54 | 2.73 | 2.73 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -1.83 | -2.49 | -13.04 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround | B_可觀察 | 62.31587090838761 | 46.95702744919681 | 0.0 | 6.67 | 22.55 | -20.22 | 41.18 | 41.18 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -0.17 | 0.5 | -12.2 | 15 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -4.94 | 13.66 | 34.07 | 100.22 | 46.99 | 100.0 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | 0.01 | 0.4 | -12.44 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 61.873094432402574 | 20.40781330899844 | -7.59 | -0.37 | -4.06 | 2.16 | 1.13 | 3.47 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -2.18 | -2.63 | -11.55 | 12 | selected |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -2.88 | 0.3 | 3.21 | -4.26 | 8.87 | 8.87 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -1.35 | -1.62 | -9.15 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576107 | 74.19480655845219 | -4.14 | -1.7 | -1.7 | -25.54 | 1.76 | 1.76 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -2.38 | -2.51 | -14.32 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.779802186364 | 14769.518174623092 | 6.51 | 5.14 | 16.46 | 29.58 | 19.87 | 31.19 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 10.4 | 7.98 | -2.65 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | 2.56 | 11.55 | 19.15 | 17.15 | 19.15 | 26.7 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | 2.85 | 4.43 | -6.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -1.46 | -22.57 | 31.68 | 102.69 | 43.42 | 120.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -11.52 | -10.42 | -34.97 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -5.45 | -5.08 | -20.59 | -30.97 | 0.83 | 0.83 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -5.3 | -5.32 | -27.25 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -4.58 | -2.67 | -10.86 | -15.99 | 1.75 | 1.75 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -2.03 | -2.77 | -19.59 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -7.07 | 2.47 | 13.95 | 104.17 | 38.03 | 157.89 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -3.18 | -1.54 | -13.06 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -2.26 | -1.94 | -3.66 | 7.07 | 3.24 | 17.44 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -1.25 | -1.08 | -6.91 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -10.78 | -15.83 | 65.57 | 211.73 | 96.5 | 221.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -16.64 | -9.43 | -32.4 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -0.83 | -2.44 | 5.26 | 3.9 | 10.09 | 10.09 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -3.31 | -2.2 | -7.34 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 188.23580475843863 | 154.50791645548554 | -3.74 | -12.71 | -8.85 | -37.39 | 12.2 | 12.2 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -8.28 | -7.14 | -28.72 | 16 | selected |
| 2344 | 華邦電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 256.6686868151223 | 187.3908590670214 | 0.93 | -4.68 | 13.19 | 42.98 | 39.32 | 57.49 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -3.36 | -2.01 | -15.54 | 16 | selected |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -11.11 | -8.09 | -13.73 | -31.25 | 1.15 | 1.15 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -9.56 | -9.36 | -32.18 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -0.97 | 13.46 | 18.6 | 21.57 | 22.3 | 27.02 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 3.8 | 4.6 | -1.92 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral | B_可觀察 | 96.29795511644917 | 83.289853268924 | 3.69 | 0.83 | -4.32 | 2.52 | 9.43 | 9.43 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | 3.4 | 3.2 | -7.47 | 19 | selected |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -3.87 | -16.77 | 37.37 | 19.22 | 60.08 | 60.08 | True | 距60日低點反彈>50% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -5.61 | -5.65 | -22.76 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 6.78 | 2.94 | 7.14 | 26.13 | 11.9 | 31.94 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 6.33 | 4.64 | -14.29 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -2.25 | -19.88 | 0.77 | -15.91 | 10.76 | 13.01 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -9.92 | -8.07 | -23.63 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -13.25 | 3.85 | 33.5 | -25.52 | 53.19 | 53.19 | True | 距60日低點反彈>50% | distribution_warning | -0.79 | -0.57 | 1 | 1 | -8.53 | -6.66 | -17.56 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | 0.0 | -2.46 | 9.33 | 15.7 | 14.58 | 19.17 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -1.11 | -0.14 | -11.07 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | 1.71 | -4.24 | 4.47 | -4.8 | 17.38 | 17.38 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -0.16 | -0.01 | -6.83 | 13 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -8.03 | -2.26 | 7.71 | -4.23 | 20.87 | 20.87 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -10.47 | -9.5 | -26.58 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | 0.29 | -2.28 | 23.56 | 54.73 | 29.87 | 56.49 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -3.21 | -1.42 | -8.89 | 18 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | 5.72 | 1.33 | -1.13 | -12.61 | 17.99 | 17.99 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | 1.19 | 3.04 | -8.41 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 576.622775031737 | 626.9495065095125 | -1.45 | -11.27 | 12.36 | 53.66 | 36.96 | 69.62 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -9.27 | -6.96 | -22.5 | 14 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -7.26 | -12.5 | -24.83 | 5.0 | 1.09 | 6.72 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -8.73 | -8.12 | -38.47 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -0.53 | 3.85 | 0.71 | 4.04 | 5.39 | 12.5 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 1.09 | 1.07 | -5.18 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | 0.78 | -2.75 | 15.77 | -16.7 | 21.56 | 21.56 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | 0.15 | 0.65 | -15.43 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.98990000276115 | 1.44 | -1.23 | 9.32 | -6.94 | 12.6 | 30.32 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | 0.17 | 0.64 | -14.57 | 22 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -5.18 | -0.17 | 1.0 | -10.25 | 11.85 | 11.85 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -2.36 | -1.91 | -10.25 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | 0.57 | -7.09 | 35.11 | 59.46 | 50.0 | 62.39 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -3.95 | -2.4 | -20.98 | 13 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 35.7 | 148.48 | 203.38 | 439.47 | 232.18 | 614.82 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 52.42 | 48.89 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -10.63 | -14.02 | -10.63 | -18.05 | 5.58 | 5.58 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -14.1 | -12.77 | -29.39 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -10.93 | -10.93 | -0.9 | -3.93 | 9.45 | 9.45 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -11.34 | -10.05 | -18.22 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | 1.07 | 16.31 | 21.54 | 28.57 | 27.27 | 30.8 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 8.4 | 7.57 | -4.06 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -7.41 | -14.35 | -2.44 | -28.06 | 20.12 | 20.12 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -11.91 | -10.69 | -34.96 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -5.7 | 19.77 | 52.04 | 132.81 | 87.66 | 145.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 0.26 | 1.48 | -13.67 |  | fail_already_priced_in |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -2.48 | 3.21 | -1.12 | -0.84 | 5.99 | 5.99 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 1.58 | 0.94 | -3.8 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -4.35 | -1.87 | 9.5 | 36.56 | 17.54 | 44.5 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -4.7 | -2.49 | -11.35 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral | D_僅留完整清單 | 85.85523299528691 | -80.47361399939216 | -6.97 | -9.71 | -10.76 | -18.78 | 0.0 | 0.0 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -7.14 | -6.9 | -13.28 | 13 | selected |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -7.04 | -7.98 | -18.52 | -12.4 | 7.3 | 7.3 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.53 | -5.1 | -26.29 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | 1.26 | -11.66 | -6.52 | 1.9 | 5.8 | 5.8 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | 2.12 | -1.62 | -18.06 | 12 | selected |
| 2545 | 皇翔 | 建材營造 | neutral | B_可觀察 | 719.4781016963254 | -1.300527989199485 | -4.8 | -4.52 | -0.15 | -16.03 | 3.48 | 3.48 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -3.6 | -3.39 | -9.53 | 19 | selected |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -3.61 | -3.52 | -5.88 | -6.34 | 0.0 | 0.0 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -2.18 | -2.52 | -10.7 | 16 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -1.52 | 13.33 | 18.32 | 19.63 | 23.28 | 28.17 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 4.18 | 3.34 | -12.47 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -4.9 | 0.0 | 39.35 | 48.98 | 39.19 | 58.5 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 0.37 | 0.15 | -13.38 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | -1.8 | 0.57 | 7.89 | 4.41 | 10.75 | 14.31 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.18 | 0.1 | -9.89 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -1.23 | -0.99 | -7.8 | -2.43 | 0.5 | 2.03 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.17 | -0.49 | -8.64 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 2.72 | 0.19 | -29.75 | -2.04 | 17.56 | 33.59 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 6.73 | 5.41 | -40.09 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -4.59 | -7.38 | -5.76 | -3.05 | 2.08 | 2.08 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -6.35 | -6.07 | -27.03 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | -0.41 | 3.4 | -8.3 | 1.25 | 6.58 | 8.48 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 0.73 | 0.47 | -10.0 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | 2.45 | -10.05 | 31.15 | 27.48 | 55.59 | 55.59 | True | 距60日低點反彈>50% | distribution_warning | -5.51 | -6.04 | 0 | 0 | -3.72 | -2.44 | -21.47 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -10.39 | 4.15 | 62.74 | 16.46 | 89.82 | 89.82 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -16.58 | -9.12 | -29.41 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | 0.55 | -0.55 | 2.02 | 20.85 | 10.98 | 37.67 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | 0.23 | 0.77 | -21.89 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -10.54 | -3.36 | -5.3 | -37.96 | 5.71 | 5.71 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -10.53 | -9.03 | -19.57 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -4.29 | -0.36 | -10.12 | -3.73 | 2.61 | 2.61 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -2.08 | -2.44 | -21.78 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | 2.38 | 4.88 | 12.86 | -1.83 | 19.44 | 19.44 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | 1.73 | 2.68 | -8.7 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -2.75 | -5.36 | 38.74 | 18.3 | 62.33 | 62.33 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -10.25 | -5.76 | -25.35 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -10.62 | -3.15 | 45.2 | 4.4 | 59.63 | 59.63 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -7.01 | -5.57 | -13.58 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.93 | 3.38 | 0.47 | -0.47 | 5.42 | 5.42 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 1.25 | 0.86 | -6.14 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 1.76 | -1.37 | 14.03 | -23.58 | 28.22 | 28.22 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | 0.02 | 1.48 | -7.09 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -4.68 | -0.94 | -1.31 | -8.48 | 6.01 | 6.01 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -4.86 | -3.89 | -14.12 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -11.67 | -3.61 | 54.57 | 52.02 | 71.28 | 79.15 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -17.55 | -11.11 | -31.02 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | 0.69 | -8.75 | 0.34 | -13.86 | 8.15 | 8.96 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -3.66 | -3.75 | -22.75 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -9.0 | 11.11 | 79.1 | 27.15 | 120.94 | 120.94 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -1.85 | 1.05 | -11.93 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -3.18 | -0.44 | -17.0 | -16.54 | 3.4 | 3.4 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -1.19 | -1.66 | -24.17 | 14 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | 4.38 | 5.54 | 12.06 | 30.48 | 20.95 | 44.32 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | 2.13 | 2.12 | -7.52 | 21 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 446.4684953621241 | 68.26830170354926 | -13.22 | 14.29 | 25.0 | 33.12 | 35.48 | 37.25 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -9.72 | -6.45 | -29.29 | 21 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -2.2 | 9.88 | 5.01 | 3.79 | 13.02 | 14.1 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | 2.83 | 2.05 | -11.0 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | -11.97 | -17.22 | -28.57 | -44.69 | 0.0 | 0.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -13.33 | -12.56 | -27.11 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -0.67 | -11.28 | 103.01 | 36.33 | 134.02 | 134.02 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -7.5 | -2.66 | -15.09 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -6.13 | -18.44 | 5.93 | 13.64 | 30.0 | 30.0 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -13.06 | -11.74 | -34.3 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -14.49 | 2.55 | 10.62 | -32.95 | 28.82 | 28.82 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -4.45 | -4.02 | -19.91 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -12.93 | 0.51 | 73.89 | 51.23 | 89.03 | 109.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -13.41 | -9.13 | -21.24 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.99846620911757 | 44.59053152341543 | -5.16 | -5.92 | 12.2 | -27.11 | 32.89 | 32.89 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -9.26 | -7.77 | -22.85 | 15 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | 0.0 | 3.1 | 5.91 | 12.56 | 19.86 | 19.86 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -0.09 | 1.34 | -10.73 | 23 | selected |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | 6.36 | 10.13 | 5.58 | 4.07 | 13.58 | 13.58 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 8.6 | 7.6 | 0.0 | 12 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -1.23 | 1.39 | -8.84 | -8.01 | 3.61 | 3.61 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -0.53 | -1.58 | -16.08 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral | D_降級_TDCC轉弱 | 165.79440372884912 | 35.87837963467142 | 3.08 | -1.62 | 6.24 | -19.5 | 13.32 | 13.32 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | 0.77 | 0.8 | -8.49 | 15 | selected |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -4.56 | -2.33 | 20.67 | -33.6 | 40.22 | 40.22 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -4.73 | -3.76 | -13.45 | 21 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -4.62 | -1.68 | 4.78 | -2.23 | 7.01 | 7.01 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -3.35 | -2.55 | -10.0 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 32.4 | 41.31 | 55.96 | 24.72 | 79.52 | 79.52 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 30.36 | 28.74 | 0.0 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -5.44 | 0.13 | 6.1 | -14.07 | 16.45 | 16.45 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -5.6 | -4.37 | -13.42 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -1.47 | -2.9 | 3.5 | 59.27 | 14.99 | 62.88 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -1.7 | -0.82 | -11.45 | 17 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | 2.94 | 16.67 | 26.2 | 24.56 | 32.74 | 38.52 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 9.22 | 7.82 | -7.89 | 14 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -0.76 | 4.1 | 27.14 | -19.78 | 45.74 | 45.74 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -1.58 | -1.08 | -10.47 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 109.68927823663151 | 90.15073758650963 | 1.73 | -2.94 | 25.71 | -11.11 | 33.33 | 35.04 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -0.08 | 0.46 | -9.43 | 20 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | -7.61 | -0.29 | 37.1 | -23.77 | 61.9 | 61.9 | True | 距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | -2.77 | -2.41 | -13.04 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | B_可觀察 | 56.623935956655565 | 70.86506389755786 | -1.07 | 7.08 | 9.24 | -36.89 | 29.74 | 29.74 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -2.46 | -2.49 | -14.36 | 16 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -1.63 | -4.23 | -2.43 | 17.92 | 2.55 | 24.83 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -2.15 | -1.84 | -9.5 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 262.471963434005 | 110.54580308622074 | 5.5 | 5.33 | -1.06 | -6.46 | 9.03 | 9.03 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 6.08 | 5.18 | -2.4 | 23 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -1.83 | -4.66 | -5.49 | -7.13 | 1.18 | 5.13 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -1.58 | -1.51 | -7.92 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -3.39 | 0.98 | 57.85 | 40.55 | 85.2 | 121.6 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -3.09 | -2.42 | -20.09 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | -3.93 | 11.4 | 44.92 | 22.58 | 55.45 | 55.45 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -2.83 | -1.5 | -19.53 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -1.38 | -15.35 | -21.53 | 24.28 | 4.88 | 27.82 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -10.47 | -7.09 | -27.61 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | 2.5 | 0.0 | -0.63 | 2.5 | 4.9 | 13.36 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | 2.54 | 2.01 | -6.55 | 21 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -4.11 | 9.16 | 23.08 | 48.6 | 36.77 | 48.79 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -5.13 | -2.4 | -14.62 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -5.87 | 22.7 | 48.51 | 31.02 | 66.84 | 66.84 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 3.67 | 2.85 | -21.17 |  | fail_already_priced_in |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -3.62 | 37.38 | 169.8 | 149.08 | 214.77 | 225.05 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | 1.21 | 3.94 | -15.71 |  | fail_already_priced_in |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 2.78 | 6.56 | 41.96 | 62.4 | 45.0 | 67.77 | True | 近60日漲幅>40% | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 5.0 | 4.96 | -0.49 |  | fail_already_priced_in |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | -10.59 | -2.36 | -0.87 | -10.94 | 14.29 | 14.29 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -6.69 | -5.89 | -15.56 | 16 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -3.38 | -8.1 | 7.23 | -36.91 | 21.8 | 21.8 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -6.91 | -4.88 | -23.05 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth | A_優先追蹤 | 50.70369959160158 | 35.171695901726686 | -2.25 | 11.16 | 18.17 | 12.6 | 32.04 | 32.04 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | 6.33 | 5.21 | -6.82 | 18 | selected |