# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-21 19:37:09 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 762871 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 92 |
| already_priced_in_excluded | 40 |
| overheat_pass | 52 |
| score_pass | 52 |
| theme_priority_pass | 46 |
| final_rows | 46 |

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
| fail_low_response_condition | 244 |
| fail_already_priced_in | 40 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -8.17 | 34.66 | 80.56 | 240.96 | 136.53 | 298.63 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 13.08 | 12.97 | -8.56 |  | fail_low_response_condition |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.28677537399296 | -18.78 | 4.42 | 16.29 | 27.39 | 42.13 | 53.81 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -0.37 | -0.26 | -19.63 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693272 | -3.77 | -5.12 | -0.49 | -9.33 | 8.63 | 8.63 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -2.51 | -2.69 | -18.4 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -2.14 | -3.27 | -5.09 | -10.34 | 0.8 | 0.8 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.34 | -1.9 | -8.71 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | -0.21 | -2.87 | -10.42 | -18.17 | 1.72 | 1.72 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -0.93 | -1.07 | -13.84 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 1.15 | 14.78 | 21.1 | 16.3 | 24.53 | 24.53 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 8.26 | 6.96 | -2.22 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -2.7 | 1.98 | -3.74 | -6.25 | 4.35 | 6.19 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -1.73 | -1.27 | -8.16 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -1.38 | -4.02 | -2.27 | 2.63 | 2.63 | 12.57 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.61 | -0.95 | -12.07 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 0.0 | -0.18 | 8.16 | 7.34 | 13.1 | 22.32 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | -0.7 | -0.82 | -6.56 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -1.11 | -2.55 | -4.63 | -13.83 | 1.13 | 1.13 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -0.59 | -0.58 | -6.62 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.1590750288686 | 59.11214720338166 | -3.91 | 0.0 | -3.15 | -7.52 | 4.68 | 4.68 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -1.68 | -1.42 | -7.87 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 37.92 | 32.97 | 6.61 | -8.85 | 44.36 | 44.36 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 31.51 | 27.26 | 0.0 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -2.37 | -0.74 | -13.83 | 2.68 | 4.48 | 4.69 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -0.33 | -1.24 | -11.55 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround | B_可觀察 | 62.31587090838761 | 46.95702744919681 | -11.53 | 2.53 | 12.7 | -17.92 | 39.22 | 39.22 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -1.35 | -1.36 | -13.41 | 14 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -7.58 | 20.38 | 26.85 | 104.1 | 51.81 | 109.53 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | 4.59 | 3.77 | -9.57 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -7.13 | 0.25 | -8.29 | 3.59 | 1.64 | 4.39 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -1.72 | -2.61 | -11.11 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350685 | 27.89987013024577 | -1.01 | 0.73 | -1.15 | 17.84 | 10.81 | 10.81 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | 0.37 | -0.21 | -7.54 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576108 | 74.19480655845219 | -2.22 | -2.22 | -4.86 | -21.6 | 3.23 | 3.23 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -1.21 | -1.63 | -13.09 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.77980218637 | 14769.518174623092 | -1.72 | -4.32 | 6.51 | 21.38 | 11.89 | 22.46 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 3.02 | 1.55 | -9.13 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -2.18 | 8.47 | 14.96 | 22.83 | 16.96 | 23.39 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -0.3 | 0.77 | -10.33 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072263 | 167.83532632168345 | 0.75 | -19.33 | 30.32 | 143.48 | 47.37 | 146.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -11.44 | -9.79 | -33.18 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -6.15 | -6.15 | -14.69 | -32.6 | 1.24 | 1.24 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -5.33 | -5.71 | -26.95 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -1.83 | -3.43 | -10.45 | -11.79 | 3.14 | 3.14 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -1.01 | -1.9 | -18.48 | 15 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | 0.0 | 18.13 | 15.08 | 123.08 | 48.53 | 177.51 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | 4.54 | 6.09 | -6.45 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -0.82 | -4.72 | -5.62 | 8.04 | 3.07 | 17.25 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -1.71 | -1.5 | -7.07 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -11.48 | -4.09 | 74.3 | 236.12 | 119.07 | 258.6 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -8.21 | -0.37 | -24.63 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.10669499309349 | -2.81 | -1.63 | 2.98 | 7.56 | 11.01 | 11.01 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -2.81 | -1.85 | -6.56 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -6.36 | -14.88 | -16.94 | -35.83 | 12.2 | 12.2 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -9.71 | -8.65 | -28.72 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 256.6686868151223 | 187.3908590670214 | -3.33 | -11.14 | 3.24 | 61.44 | 36.32 | 54.11 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -6.2 | -4.92 | -17.36 | 17 | selected |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | B_可觀察 | 66.12554142816796 | 62.44981435880206 | -11.46 | -2.16 | -18.24 | -27.25 | 2.54 | 2.54 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -7.26 | -8.1 | -30.06 | 14 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -2.73 | 9.8 | 12.53 | 21.29 | 19.54 | 24.16 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 2.59 | 2.88 | -4.13 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644916 | 83.289853268924 | 0.43 | -5.26 | -10.1 | -2.36 | 5.24 | 5.24 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -0.76 | -0.61 | -11.01 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.36147799625845 | 35.28859580878607 | -0.48 | -14.7 | 27.95 | 29.15 | 66.13 | 66.13 | True | 距60日低點反彈>50% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -3.88 | -3.23 | -19.84 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 5.15 | -0.65 | -4.96 | 30.56 | 8.88 | 30.01 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 3.5 | 2.33 | -16.6 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 206.46824005093208 | 119.5343671101157 | -10.67 | -12.23 | -3.37 | -10.07 | 13.88 | 16.18 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -9.22 | -6.81 | -21.48 | 16 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | -5.16 | 17.16 | 32.63 | -19.26 | 69.5 | 69.5 | True | 距60日低點反彈>50% | distribution_warning | -0.79 | -0.57 | 1 | 1 | 1.68 | 2.27 | -8.78 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | 0.7 | 0.7 | 1.13 | 28.26 | 14.9 | 26.68 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -1.21 | -0.11 | -10.82 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.4110806985514 | 1.7 | -4.23 | 0.15 | 2.34 | 17.74 | 17.74 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -0.42 | 0.15 | -6.54 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 168.87284393304373 | 103.69258923500948 | -9.6 | 2.04 | 4.94 | 5.5 | 26.97 | 26.97 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -5.89 | -6.11 | -22.87 | 21 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -4.34 | -1.01 | 17.56 | 72.26 | 29.11 | 71.18 | True | 近120日漲幅>70% | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -4.12 | -2.47 | -9.42 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.8880515092684 | 0.0 | 8.14 | -10.34 | -8.56 | 15.67 | 15.67 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -0.71 | 1.59 | -12.06 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -9.16 | -16.86 | 8.85 | 70.18 | 35.56 | 67.88 | True | 近120日漲幅>70% | distribution_warning | -0.15 | -0.24 | 1 | 1 | -11.63 | -9.58 | -23.29 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -3.74 | -9.59 | -28.6 | 3.72 | 0.45 | 9.67 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -7.45 | -6.87 | -36.77 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859532 | 66.26826344206586 | -2.11 | 1.64 | -1.59 | -0.36 | 3.72 | 10.71 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.18 | -0.35 | -6.69 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -2.83 | -9.57 | 5.29 | -17.11 | 18.12 | 18.12 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -3.35 | -2.49 | -17.83 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.9899000027612 | -1.62 | -3.18 | 3.79 | -3.18 | 9.6 | 26.85 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -2.75 | -2.13 | -16.84 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -1.56 | 5.71 | 0.64 | -7.5 | 16.48 | 16.48 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | 1.76 | 1.92 | -6.54 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | -10.05 | -13.71 | 16.04 | 50.44 | 44.07 | 61.9 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -8.86 | -7.42 | -24.11 | 12 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 16.39 | 134.43 | 161.58 | 355.96 | 187.62 | 518.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 44.33 | 40.23 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -12.25 | -9.09 | -6.8 | -15.94 | 11.63 | 11.63 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -10.43 | -9.99 | -25.35 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -4.35 | -2.42 | 1.68 | 4.31 | 20.4 | 20.4 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -3.41 | -2.63 | -10.04 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -3.42 | 11.21 | 15.41 | 22.33 | 23.57 | 26.99 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 6.73 | 5.83 | -6.85 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 56.8306808099056 | 32.980802133096326 | -4.72 | -10.74 | -3.2 | -30.94 | 27.33 | 27.33 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -7.99 | -7.19 | -31.06 | 11 | selected |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.7524441579672 | -4.81 | 31.02 | 47.99 | 173.06 | 104.28 | 180.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 10.94 | 10.66 | -6.03 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256228 | 122.99025793829806 | 1.69 | 7.78 | 1.41 | -0.28 | 7.78 | 7.78 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 3.66 | 2.81 | -2.17 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416136 | -4.86 | 6.77 | 5.96 | 44.25 | 21.64 | 49.54 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -1.34 | 0.6 | -8.26 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -2.71 | -4.44 | -6.38 | -13.87 | 0.94 | 0.94 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -3.06 | -2.94 | -8.76 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -7.64 | -9.19 | -13.95 | -9.9 | 8.24 | 8.24 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -5.44 | -5.19 | -25.65 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | 1.01 | -16.11 | -9.28 | 1.01 | 5.67 | 5.67 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | 0.49 | -2.07 | -18.16 | 12 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -3.74 | -4.97 | 0.45 | -12.09 | 5.69 | 5.69 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -1.93 | -1.83 | -7.6 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 157.1373893517917 | 73.07026244678458 | 0.1 | -2.08 | -2.08 | -3.51 | 3.02 | 3.02 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | 0.53 | 0.2 | -8.0 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -0.91 | 13.89 | 15.49 | 22.39 | 25.19 | 30.16 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 7.1 | 5.77 | -11.11 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.28273043969428 | -6.8 | -3.32 | 33.91 | 51.3 | 42.07 | 58.5 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 0.47 | 0.41 | -13.38 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122 | -4.08 | -0.84 | 7.46 | 4.28 | 9.97 | 13.5 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.87 | -0.69 | -10.52 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.99 | -2.67 | -5.2 | -2.67 | 0.25 | 1.78 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.5 | -0.8 | -8.86 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | -5.54 | -11.99 | -28.16 | 6.71 | 6.0 | 20.45 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | -4.1 | -4.66 | -45.98 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -2.28 | -5.26 | -5.58 | 0.54 | 5.48 | 5.48 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -3.97 | -4.0 | -24.59 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.75664630034535 | 42.38105078727345 | 1.23 | 2.93 | -9.23 | -1.99 | 7.89 | 9.82 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 2.31 | 1.8 | -9.56 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | -0.4 | -15.46 | 19.42 | 35.16 | 52.8 | 52.8 | True | 距60日低點反彈>50% | distribution_warning | -5.51 | -6.04 | 0 | 0 | -6.86 | -5.19 | -22.88 |  | fail_already_priced_in |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.86953907106725 | -8.85 | 32.62 | 62.12 | 43.06 | 112.52 | 112.52 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -5.75 | 0.42 | -20.97 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | 0.11 | -0.11 | -3.3 | 21.2 | 10.85 | 37.52 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -0.11 | 0.62 | -21.97 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.01687411836724 | 29.7636013582763 | -9.77 | 3.75 | -5.3 | -33.09 | 13.06 | 13.06 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -4.55 | -4.23 | -13.98 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -4.0 | 1.08 | -15.9 | 9.08 | 4.47 | 4.47 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -0.36 | -1.06 | -20.36 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -1.62 | 3.41 | 3.41 | 1.67 | 18.06 | 18.06 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | 0.94 | 1.92 | -9.77 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -7.17 | 12.13 | 31.11 | 21.82 | 68.45 | 68.45 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -6.84 | -3.07 | -22.54 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -3.32 | 12.55 | 48.35 | 20.33 | 78.29 | 78.29 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | 4.0 | 4.93 | -3.48 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | -0.47 | 3.38 | 0.0 | -2.73 | 5.42 | 5.42 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 1.52 | 0.89 | -6.14 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -3.0 | -4.84 | 1.48 | -18.03 | 22.22 | 22.22 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -5.0 | -3.41 | -11.43 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -1.95 | 3.37 | -4.5 | -3.33 | 10.62 | 10.62 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -0.83 | -0.35 | -10.39 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -14.24 | 8.32 | 54.7 | 102.9 | 89.19 | 98.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -9.41 | -3.63 | -23.81 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -4.98 | -12.54 | -8.33 | -12.27 | 5.93 | 6.72 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -6.64 | -6.56 | -24.34 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | 4.17 | 19.9 | 61.29 | 29.87 | 130.15 | 130.15 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | 3.37 | 5.11 | -8.26 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 90.47990444398276 | 46.685682375869504 | -3.88 | 0.11 | -20.81 | -15.25 | 3.85 | 3.85 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -0.82 | -1.59 | -23.84 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | 4.28 | 4.56 | 8.94 | 37.32 | 23.81 | 47.73 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | 4.92 | 4.92 | -5.34 | 20 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 446.4684953621241 | 68.26830170354926 | -17.59 | 19.25 | 35.14 | 50.08 | 48.87 | 52.06 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | 0.45 | 1.96 | -22.31 | 23 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -1.39 | 9.54 | -3.0 | 13.02 | 13.02 | 14.1 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | 3.73 | 2.42 | -11.0 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360124 | 126.26534387085924 | -4.47 | -1.77 | -22.35 | -28.35 | 0.0 | 0.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -5.04 | -4.24 | -22.78 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.7784771532576 | 102.83428395752624 | -2.97 | 11.89 | 96.56 | 65.46 | 151.97 | 151.97 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -1.01 | 4.48 | -8.57 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976644 | 36.46696724530479 | -10.0 | -16.36 | 5.39 | 23.29 | 36.36 | 36.36 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -10.78 | -9.52 | -31.09 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 71.39293333177902 | 252.79681111256323 | 4.2 | 9.38 | 11.14 | -33.47 | 40.9 | 40.9 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | 4.73 | 4.43 | -12.4 | 13 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -7.57 | 18.28 | 90.52 | 36.72 | 110.81 | 133.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -3.21 | -0.1 | -12.16 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.9984662091176 | 44.59053152341543 | -5.84 | 4.8 | 8.96 | -10.6 | 41.06 | 41.06 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -4.16 | -3.53 | -18.1 | 16 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | -2.95 | 0.44 | -2.13 | 12.2 | 18.31 | 18.31 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -1.2 | 0.13 | -11.88 | 23 | selected |
| 3703 | 欣陸 | 建材營造 | neutral |  | 89.3174912383306 | 3.447593197203932 | 0.98 | 2.49 | -1.2 | 0.49 | 7.31 | 7.31 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.37 | 2.68 | -2.14 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -3.44 | 0.99 | -10.95 | -3.33 | 4.77 | 4.77 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | 0.7 | -0.77 | -15.14 | 18 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | -1.76 | -1.96 | -5.2 | -24.76 | 10.75 | 10.75 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -1.82 | -1.49 | -10.57 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 84.69522628124143 | 51.25937713911443 | -3.91 | 13.92 | 15.88 | -31.3 | 50.84 | 50.84 | True | 距60日低點反彈>50% | strong_accumulation | 0.51 | 0.17 | 2 | 2 | 2.99 | 3.43 | -6.25 |  | fail_already_priced_in |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513512 | 31.81289526994584 | -2.98 | 0.56 | 4.99 | -1.1 | 9.15 | 9.15 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -1.47 | -0.96 | -8.21 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 11.91 | 21.76 | 23.74 | -5.58 | 51.29 | 51.29 | True | 距60日低點反彈>50% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 13.4 | 13.49 | 0.0 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -4.02 | -10.42 | 12.27 | -9.09 | 32.72 | 32.72 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -4.62 | -3.22 | -16.67 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -6.12 | 4.15 | 1.22 | -9.71 | 20.52 | 20.52 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -2.4 | -1.82 | -10.39 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | 1.97 | -1.9 | 0.49 | 58.99 | 18.42 | 67.75 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 0.82 | 1.9 | -8.81 | 19 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth |  | 86.87811970952995 | 13.790026773850077 | 5.0 | 16.28 | 18.78 | 28.83 | 32.74 | 38.52 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 10.82 | 9.3 | -7.89 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | 5.02 | 15.01 | 27.49 | -15.47 | 58.89 | 58.89 | True | 距60日低點反彈>50% | mild_accumulation | 0.38 | -0.18 | 1 | 0 | 7.78 | 7.91 | -2.39 |  | fail_already_priced_in |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663152 | 90.15073758650963 | -6.04 | -10.11 | 13.96 | -13.84 | 25.76 | 27.37 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -6.36 | -5.63 | -14.58 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | -5.5 | 3.14 | 29.86 | -17.77 | 71.9 | 71.9 | True | 距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 2.95 | 2.88 | -7.67 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -1.15 | 12.95 | 5.67 | -34.38 | 37.52 | 37.52 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | 4.52 | 3.72 | -9.22 | 20 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.15622840056231 | 37.709946899313486 | -0.82 | -3.7 | -6.19 | 6.43 | 3.12 | 25.52 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -2.07 | -1.66 | -9.0 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | 0.32 | -0.64 | -6.22 | -10.56 | 3.34 | 3.34 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 0.87 | 0.22 | -7.9 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623696 | 1394.301991029742 | -1.59 | -2.92 | -6.49 | -6.49 | 1.65 | 5.62 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -1.61 | -1.38 | -7.49 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -0.92 | 7.92 | 39.2 | 46.59 | 94.22 | 132.4 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | 1.87 | 1.81 | -16.2 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | -1.34 | 21.93 | 50.41 | 31.07 | 66.82 | 66.82 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 5.52 | 6.0 | -13.65 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -6.14 | -6.55 | -35.74 | 36.13 | 4.39 | 38.78 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -12.4 | -9.04 | -35.35 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -0.44 | -5.89 | -6.28 | 0.22 | 1.34 | 9.51 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.2 | -1.44 | -9.72 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth | A_優先追蹤 | 88.49473702740245 | 55.51042227955082 | -6.25 | 13.89 | 16.92 | 64.44 | 44.03 | 63.13 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | 0.81 | 2.52 | -10.09 | 21 | selected |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | 22.49 | 36.82 | 62.48 | 60.12 | 94.0 | 94.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 23.07 | 20.77 | -8.33 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -3.86 | 62.97 | 165.91 | 189.79 | 247.26 | 258.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | 15.07 | 15.99 | -4.08 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 1.53 | 2.31 | 42.65 | 59.2 | 42.14 | 64.46 | True | 近60日漲幅>40% | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 3.52 | 3.78 | -1.73 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | B_可觀察 | 64.04751148579548 | 40.914406890913945 | -2.57 | 8.35 | -1.2 | 5.79 | 23.56 | 23.56 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | 0.68 | 0.69 | -8.7 | 17 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | 0.12 | 0.12 | 4.63 | -33.79 | 28.44 | 28.44 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -2.37 | -0.2 | -18.86 |  | fail_low_response_condition |