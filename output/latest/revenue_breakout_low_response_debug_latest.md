# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-04 19:37:44 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 778600 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 65 |
| already_priced_in_excluded | 17 |
| overheat_pass | 48 |
| score_pass | 48 |
| theme_priority_pass | 39 |
| final_rows | 39 |

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
| fail_low_response_condition | 271 |
| fail_already_priced_in | 17 |
| fail_defensive_or_traditional_excluded | 7 |
| fail_non_mainstream_score_lt_11 | 2 |
| missing_or_insufficient_price_metrics | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -13.32 | 6.35 | 56.21 | 224.15 | 63.13 | 243.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -9.19 | -4.38 | -21.11 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -7.17 | -7.8 | 12.4 | 30.77 | 17.75 | 36.27 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -10.56 | -7.62 | -28.8 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | -6.82 | -5.5 | 0.1 | -5.94 | 1.94 | 6.18 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -3.6 | -3.73 | -20.24 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -3.33 | -5.37 | -2.57 | -9.38 | 0.82 | 0.82 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.69 | -2.71 | -10.53 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 10.06 | 9.6 | 1.35 | -2.78 | 13.39 | 13.39 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 10.21 | 9.26 | -1.32 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral | B_可觀察 | 70.45469720237698 | 47.58022431497226 | 5.2 | 19.41 | 30.41 | 27.48 | 32.24 | 33.49 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 9.1 | 9.55 | -1.74 | 14 | selected |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -3.87 | -5.43 | -4.92 | -4.92 | 1.46 | 2.65 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -4.42 | -3.43 | -11.22 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.0 | 1.17 | -3.99 | 5.61 | 3.34 | 11.03 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.01 | 0.01 | -8.26 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | -1.02 | 0.17 | 1.75 | 13.28 | 5.84 | 24.46 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 0.46 | 0.35 | -4.92 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -5.6 | -5.6 | -8.33 | -16.23 | 0.4 | 0.4 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -4.99 | -4.74 | -10.6 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -7.05 | -9.31 | -10.4 | -9.68 | 3.7 | 3.7 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -8.5 | -7.18 | -16.1 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | -8.89 | 56.49 | 28.12 | -5.96 | 59.53 | 59.53 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 22.04 | 16.47 | -22.2 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 0.94 | 0.75 | -3.76 | -0.37 | 4.68 | 4.68 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -0.18 | -0.41 | -11.39 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -14.77 | -14.19 | -7.64 | -29.25 | 5.83 | 24.51 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -10.5 | -9.14 | -22.56 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -7.34 | 1.19 | 15.59 | 73.27 | 16.38 | 83.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | -8.75 | -4.61 | -18.42 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -10.59 | -9.7 | -13.26 | -8.45 | 0.55 | 0.55 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -11.05 | -10.07 | -20.13 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -7.29 | -7.7 | -3.71 | -13.11 | 2.13 | 2.13 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -7.77 | -6.93 | -16.15 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576107 | 74.19480655845219 | -8.62 | -9.66 | -16.32 | -17.62 | 2.25 | 2.25 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -8.91 | -8.08 | -21.48 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.779802186364 | 14769.518174623092 | -11.01 | 4.91 | 2.31 | 14.11 | 6.42 | 18.18 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | -3.87 | -4.19 | -12.3 | 16 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -16.55 | -18.88 | -2.52 | 0.0 | 2.2 | 3.57 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -12.37 | -10.53 | -22.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -15.27 | -29.19 | -9.19 | 76.95 | 3.37 | 93.26 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -16.42 | -16.73 | -42.99 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -8.98 | -16.17 | -30.75 | -34.99 | 3.72 | 3.72 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -9.86 | -9.22 | -29.43 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -4.67 | -5.97 | -20.03 | -11.56 | 2.04 | 2.04 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -6.17 | -6.08 | -24.0 | 14 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -9.63 | -7.58 | 12.44 | 130.19 | 24.97 | 133.49 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -11.18 | -6.83 | -21.29 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -4.29 | -6.45 | -3.33 | 5.84 | 2.11 | 12.4 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -4.39 | -4.4 | -10.63 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -9.63 | -18.94 | 66.27 | 197.56 | 89.88 | 210.83 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -13.28 | -8.49 | -34.67 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -6.8 | -9.6 | -6.03 | -0.22 | 1.12 | 3.67 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -7.38 | -6.14 | -12.74 | 12 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -15.75 | -28.52 | -25.79 | -46.34 | 5.83 | 5.83 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -16.82 | -16.27 | -39.65 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -17.73 | -20.95 | -16.27 | 9.27 | 6.79 | 26.34 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -13.55 | -13.11 | -26.68 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -18.46 | -24.68 | -37.95 | -40.92 | 5.71 | 5.71 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -20.98 | -18.12 | -42.97 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -11.9 | -7.0 | -7.0 | 9.59 | 6.11 | 12.45 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -8.54 | -6.81 | -13.17 | 23 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -5.67 | -5.67 | -3.2 | -4.17 | 2.46 | 2.46 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -4.74 | -4.64 | -15.7 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -20.19 | -22.46 | -2.96 | -8.89 | 7.19 | 32.26 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -18.07 | -17.12 | -36.19 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -11.6 | -4.41 | -14.16 | 8.05 | 3.49 | 12.57 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | -4.78 | -5.74 | -23.27 | 12 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -27.76 | -32.88 | -22.02 | -34.38 | 5.38 | 5.38 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -27.69 | -24.97 | -42.58 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -18.65 | -12.76 | 2.55 | -25.27 | 6.99 | 36.74 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -17.05 | -13.16 | -26.41 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -10.48 | -13.12 | -5.12 | -0.61 | 2.37 | 8.17 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -8.25 | -7.15 | -19.28 | 21 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -8.33 | -8.89 | -0.49 | -1.14 | 2.54 | 8.42 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -6.09 | -6.2 | -13.94 | 11 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -9.35 | -12.15 | -13.16 | -1.3 | 5.93 | 15.9 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -12.73 | -9.35 | -29.6 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | -8.71 | -12.15 | -0.63 | 36.89 | 4.83 | 43.28 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -8.99 | -7.43 | -16.58 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | -5.45 | -8.33 | -12.94 | -7.29 | 10.64 | 10.64 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -3.18 | -2.13 | -12.94 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -16.25 | -24.05 | -10.22 | 28.25 | 6.39 | 50.47 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -14.16 | -13.31 | -29.79 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -6.67 | -18.95 | -37.27 | -10.98 | 5.3 | 5.3 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -8.91 | -8.58 | -41.78 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -1.41 | 1.27 | -2.11 | 6.49 | 3.72 | 10.71 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -1.18 | -0.6 | -6.69 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -4.71 | -9.0 | 3.7 | -14.15 | 6.12 | 13.75 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -4.54 | -4.31 | -20.87 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.98990000276115 | -10.39 | -9.31 | -6.9 | -21.73 | 5.2 | 21.76 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -5.89 | -6.08 | -20.18 | 20 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -9.03 | -10.06 | -12.48 | -13.44 | 3.75 | 3.75 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -9.26 | -7.84 | -17.68 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | -11.14 | -18.41 | -6.18 | 26.09 | 7.41 | 35.17 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -9.47 | -8.89 | -28.79 |  | fail_low_response_condition |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 4.75 | 134.4 | 243.2 | 609.99 | 278.15 | 723.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 30.39 | 30.47 | -17.79 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -21.61 | -31.97 | -27.37 | -36.03 | 6.22 | 6.22 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -24.06 | -21.65 | -41.6 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -10.53 | -19.05 | -18.07 | -11.3 | 5.59 | 5.59 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -14.68 | -12.36 | -24.16 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -8.99 | 6.5 | 12.42 | 15.82 | 13.53 | 19.03 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | -4.6 | -2.95 | -12.69 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -14.73 | -27.96 | -19.22 | -29.12 | 7.95 | 7.95 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -16.95 | -15.9 | -42.6 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -21.61 | -13.69 | 20.23 | 51.46 | 31.92 | 57.18 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -19.09 | -14.29 | -27.69 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -4.48 | 0.29 | -3.67 | -3.4 | 2.1 | 2.1 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -2.89 | -2.57 | -7.34 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -5.6 | -6.36 | 8.54 | 39.34 | 12.62 | 41.9 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -5.66 | -3.41 | -12.95 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -3.13 | -7.49 | -9.12 | -12.96 | 2.32 | 2.32 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -4.63 | -4.45 | -12.71 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -1.65 | -7.37 | -22.84 | -23.37 | 5.06 | 5.06 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.57 | -4.87 | -21.75 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -1.54 | -1.29 | -13.17 | -12.57 | 0.79 | 0.79 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -2.7 | -4.4 | -21.94 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -5.01 | -5.15 | 0.47 | -14.48 | 1.74 | 1.74 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -4.3 | -3.91 | -11.05 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 157.1373893517917 | 73.07026244678458 | -3.6 | -4.0 | -9.03 | -5.83 | 0.97 | 0.97 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -3.75 | -3.64 | -12.84 | 16 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -4.57 | 9.44 | 16.79 | 23.23 | 17.67 | 24.21 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | -2.42 | -0.75 | -15.18 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | -2.53 | 2.21 | 35.25 | 55.66 | 37.83 | 55.24 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -1.53 | -1.02 | -14.13 | 16 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | -3.23 | -2.68 | 6.82 | 5.51 | 7.32 | 10.77 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -2.94 | -2.5 | -12.67 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -2.5 | -2.99 | -8.45 | -2.99 | 0.78 | 0.78 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -2.61 | -2.62 | -10.96 | 13 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 14.77 | 32.99 | 8.7 | 47.11 | 41.56 | 60.86 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.01 | 1 | 0 | 22.77 | 19.58 | -0.16 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -9.43 | -17.58 | -16.89 | -15.61 | 3.78 | 3.78 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -10.64 | -10.34 | -33.18 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.756646300345345 | 42.38105078727345 | 4.12 | 4.12 | -1.56 | 4.55 | 10.96 | 10.96 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 3.75 | 3.64 | -3.07 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | -15.97 | -18.91 | -3.14 | -7.77 | 5.95 | 43.79 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -8.98 | -10.17 | -27.43 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -16.13 | -35.18 | 12.5 | 5.41 | 24.6 | 60.94 | False |  | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -23.88 | -17.13 | -40.15 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -9.3 | -9.4 | -15.06 | 23.18 | 3.88 | 25.42 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -6.97 | -6.46 | -28.84 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -15.37 | -22.0 | -21.34 | -40.76 | 6.61 | 6.61 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -16.91 | -13.7 | -27.33 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -6.49 | -6.49 | -17.05 | -17.22 | 3.52 | 3.52 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -5.06 | -4.73 | -24.91 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -5.76 | -4.22 | -9.11 | -24.26 | 12.67 | 13.61 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -3.16 | -1.95 | -13.16 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -19.27 | -31.95 | -8.36 | 8.16 | 8.42 | 35.99 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -20.47 | -16.55 | -37.46 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -11.03 | -10.7 | 21.46 | 1.36 | 26.21 | 48.01 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -12.95 | -9.75 | -19.87 |  | fail_low_response_condition |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -1.88 | 0.0 | -0.95 | -0.95 | 2.96 | 2.96 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -1.62 | -1.39 | -8.33 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -5.17 | -4.69 | 14.95 | -14.56 | 21.06 | 26.44 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -0.6 | -0.36 | -8.37 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -10.7 | -16.26 | -16.7 | -9.87 | 4.31 | 4.31 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -11.02 | -9.26 | -21.43 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -15.35 | -32.93 | 30.79 | 44.41 | 35.88 | 66.61 | False |  | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -19.15 | -13.15 | -35.85 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -11.45 | -17.3 | -25.5 | -39.12 | 6.48 | 6.48 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -10.05 | -10.21 | -30.42 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -16.21 | -12.03 | 33.8 | 17.41 | 35.91 | 98.62 | True | 距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -11.45 | -7.58 | -20.83 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 90.47990444398276 | 46.685682375869504 | -6.77 | -5.86 | -26.06 | -36.18 | 3.09 | 3.09 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -5.38 | -4.81 | -26.81 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -9.51 | -5.63 | -8.81 | 29.89 | 3.83 | 33.33 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -5.36 | -4.81 | -14.56 | 21 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -12.46 | -20.75 | 20.34 | 26.94 | 25.72 | 28.59 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -15.08 | -8.78 | -33.75 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -12.15 | -6.33 | -15.95 | -4.6 | 3.67 | 3.67 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -10.77 | -9.05 | -22.25 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | 6.18 | -1.02 | -8.75 | -26.26 | 16.8 | 16.8 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.41 | -0.4 | -12.05 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -12.91 | -9.94 | 62.07 | 46.85 | 67.41 | 124.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -9.14 | -5.52 | -18.69 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -14.04 | -30.11 | -20.11 | -4.05 | 8.74 | 15.0 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -17.35 | -16.27 | -41.88 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -16.0 | -18.08 | -10.58 | -37.88 | 7.03 | 10.77 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -15.8 | -13.53 | -31.13 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | 1.18 | -5.15 | 48.62 | 86.15 | 65.6 | 130.36 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -2.67 | 0.89 | -13.31 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | -16.32 | -16.54 | -11.91 | -30.94 | 7.61 | 20.91 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -15.34 | -12.45 | -29.8 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 146.48689155577668 | 72.46425018776883 | -14.14 | -16.3 | -22.79 | -9.45 | 2.89 | 2.89 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -12.4 | -10.51 | -23.68 |  | fail_low_response_condition |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.4475931972039313 | 0.48 | 7.42 | 3.19 | 4.48 | 9.66 | 9.66 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 2.92 | 2.46 | -3.45 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth |  | 88.6477682411653 | 57.38834553320375 | -10.25 | -10.58 | -20.89 | -9.01 | 2.11 | 2.11 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -9.06 | -8.61 | -24.11 |  | fail_low_response_condition |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | -10.05 | -6.24 | -4.22 | -17.97 | 2.42 | 8.76 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -3.45 | -4.22 | -12.17 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 84.69522628124143 | 51.25937713911443 | -13.86 | -11.2 | 5.02 | -34.29 | 10.58 | 28.49 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -11.96 | -9.33 | -20.69 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -2.86 | -5.56 | -0.87 | -1.16 | 1.49 | 3.66 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -5.12 | -3.85 | -12.82 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 21.45 | 75.8 | 96.42 | 62.75 | 108.29 | 139.76 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 46.36 | 39.29 | -1.15 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -14.73 | -17.09 | -11.01 | -26.93 | 7.48 | 19.75 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -10.14 | -9.65 | -24.81 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -11.14 | -19.05 | -16.41 | -25.44 | 3.91 | 4.51 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -12.41 | -10.34 | -22.29 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -5.6 | -6.51 | -6.51 | 44.31 | 7.24 | 32.93 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -3.7 | -3.21 | -13.92 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -6.02 | 13.79 | 13.41 | 32.68 | 19.83 | 33.91 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 1.47 | 1.79 | -10.96 | 13 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -9.37 | -5.41 | 10.86 | -14.24 | 14.66 | 36.11 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -8.23 | -5.79 | -16.38 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 109.68927823663151 | 90.15073758650963 | -4.83 | -2.56 | 0.19 | -3.62 | 7.26 | 36.06 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | 0.52 | -0.37 | -8.75 | 23 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth | A_優先追蹤 | 125.76660822131308 | 27.66392696281368 | -1.87 | 4.56 | 28.77 | -18.98 | 39.54 | 74.76 | False |  | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 3.22 | 4.14 | -7.32 | 20 | selected |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -9.16 | -5.32 | -9.57 | -31.01 | 7.08 | 20.76 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -9.69 | -6.39 | -20.29 | 17 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -7.42 | -10.61 | -12.01 | 12.71 | 0.0 | 16.21 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -7.1 | -6.62 | -15.75 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -7.49 | -1.98 | -7.92 | -16.12 | 0.68 | 0.68 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -3.62 | -3.57 | -9.33 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | -2.3 | -2.52 | -8.6 | -6.18 | 0.95 | 3.91 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -2.1 | -2.02 | -7.0 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -16.35 | -13.24 | 24.82 | 56.64 | 31.5 | 59.75 | False |  | distribution_warning | -2.68 | -0.93 | 0 | 2 | -14.43 | -12.31 | -31.07 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 0.0 | 17.83 | 55.46 | 25.0 | 60.17 | 68.18 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -0.34 | 3.9 | -12.94 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -15.42 | -26.15 | -30.94 | -14.29 | 5.38 | 5.38 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -14.04 | -12.91 | -35.35 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | -4.32 | -6.09 | -9.53 | -5.26 | 0.58 | 3.97 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -4.77 | -4.91 | -14.29 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -18.58 | -22.01 | -5.3 | 19.45 | 5.24 | 22.8 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -19.97 | -15.34 | -29.53 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | -23.37 | -7.75 | 7.65 | 15.52 | 17.99 | 36.51 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -16.69 | -13.41 | -35.5 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -21.34 | -10.4 | 79.47 | 141.9 | 81.87 | 166.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -19.03 | -12.38 | -30.85 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | A_優先追蹤 | 55.69095387442037 | 42.29598437707936 | -9.23 | -3.45 | 18.95 | 49.18 | 30.0 | 50.41 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | -7.17 | -6.71 | -10.78 | 16 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth |  | 64.04751148579548 | 40.914406890913945 | -15.01 | -15.55 | -22.69 | -22.69 | 6.35 | 6.35 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -15.86 | -13.07 | -25.56 |  | fail_low_response_condition |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -12.9 | -17.41 | -9.88 | -40.0 | 3.39 | 10.9 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -10.91 | -10.6 | -29.94 |  | fail_low_response_condition |