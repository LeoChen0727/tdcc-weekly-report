# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-19 18:35:37 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 758945 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 100 |
| already_priced_in_excluded | 40 |
| overheat_pass | 60 |
| score_pass | 60 |
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
| fail_low_response_condition | 236 |
| fail_already_priced_in | 40 |
| fail_defensive_or_traditional_excluded | 8 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | 0.17 | 35.49 | 45.91 | 238.73 | 123.99 | 277.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 9.84 | 8.81 | -13.41 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.28677537399296 | -5.3 | 2.7 | 10.14 | 23.58 | 40.74 | 52.3 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -1.14 | -1.52 | -20.42 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693272 | -0.48 | -2.8 | 0.0 | -5.45 | 10.76 | 10.76 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -1.02 | -1.2 | -16.8 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -1.75 | -2.13 | -2.13 | -12.48 | 1.2 | 1.2 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.22 | -1.85 | -8.35 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | -1.47 | -5.26 | -11.2 | -15.06 | 0.65 | 0.65 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -2.28 | -2.37 | -14.75 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 3.95 | 16.89 | 19.0 | 15.35 | 24.06 | 24.06 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 9.36 | 7.79 | -2.59 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | 0.27 | 2.79 | 1.38 | -4.17 | 6.67 | 8.55 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | 0.66 | 0.68 | -6.12 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -1.59 | 1.65 | -1.37 | -2.48 | 3.1 | 13.09 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.3 | -0.61 | -11.66 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 4.67 | 5.23 | 11.05 | 10.63 | 15.67 | 25.11 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 1.69 | 1.4 | -4.43 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | 0.0 | 0.75 | -3.93 | -14.87 | 1.51 | 1.51 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -0.39 | -0.28 | -6.27 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.1590750288686 | 59.11214720338166 | -4.3 | 1.66 | -4.3 | -5.41 | 4.26 | 4.26 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -2.1 | -2.12 | -8.24 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 37.92 | 32.97 | 6.61 | -8.85 | 44.36 | 44.36 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 31.51 | 27.26 | 0.0 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -7.81 | -2.03 | -13.38 | 0.38 | 3.51 | 3.71 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -1.39 | -2.44 | -15.58 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround | B_可觀察 | 62.31587090838761 | 46.95702744919681 | -3.39 | 2.89 | 10.47 | -0.7 | 39.71 | 39.71 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -0.87 | -1.49 | -13.11 | 14 | selected |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -7.43 | 19.87 | 19.11 | 98.94 | 50.2 | 107.32 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | 5.31 | 3.52 | -10.53 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | 0.0 | 4.12 | -2.68 | 6.51 | 4.91 | 8.59 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | 1.49 | 0.1 | -8.25 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350685 | 27.89987013024577 | -2.0 | 2.08 | -1.58 | 21.59 | 10.81 | 24.46 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | 0.5 | -0.24 | -7.54 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.77980218637 | 14769.518174623092 | 0.14 | 3.42 | 8.92 | 21.25 | 13.36 | 24.06 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 4.18 | 3.23 | -7.94 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -0.37 | 10.83 | 15.15 | 20.36 | 17.18 | 24.3 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -0.6 | -0.18 | -11.33 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072263 | 167.83532632168345 | -6.24 | -17.64 | 22.09 | 153.71 | 45.03 | 154.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -14.57 | -12.83 | -34.24 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -6.39 | -1.58 | -13.24 | -31.22 | 0.81 | 0.81 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -4.01 | -4.91 | -25.45 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 270.34068105049295 | 167.43229879771584 | -0.66 | 1.34 | -9.97 | -9.57 | 5.58 | 5.58 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | 1.06 | 0.13 | -16.55 | 16 | selected |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -3.87 | 19.54 | 9.58 | 109.91 | 46.48 | 173.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | 4.58 | 5.47 | -7.74 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | 0.66 | 0.66 | -4.56 | 6.68 | 3.41 | 17.64 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -1.76 | -1.51 | -6.76 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -21.8 | 12.55 | 64.74 | 254.14 | 116.34 | 254.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -9.5 | -1.93 | -25.57 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.10669499309349 | -4.72 | 1.68 | 0.83 | 13.35 | 11.01 | 11.01 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -2.93 | -2.24 | -6.56 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -11.69 | -14.29 | -24.44 | -33.77 | 11.11 | 11.11 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -11.92 | -11.21 | -29.41 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -10.63 | -7.99 | -9.06 | 73.16 | 32.91 | 70.69 | True | 近120日漲幅>70% | distribution_warning | -1.13 | -1.08 | 2 | 2 | -9.55 | -8.51 | -19.43 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 66.12554142816796 | 62.44981435880206 | -5.87 | 8.97 | -12.25 | -12.06 | 13.28 | 13.28 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | 2.79 | 0.69 | -22.74 | 18 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | 2.12 | 13.87 | 14.51 | 22.42 | 21.1 | 25.78 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 4.92 | 4.72 | -2.88 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644916 | 83.289853268924 | -1.41 | -0.14 | -11.04 | -1.41 | 4.94 | 4.94 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -1.59 | -1.04 | -11.6 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.36147799625845 | 35.28859580878607 | -5.18 | -14.62 | 19.94 | 30.84 | 62.5 | 62.5 | True | 距60日低點反彈>50% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -7.66 | -6.34 | -21.6 |  | fail_already_priced_in |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 1.72 | -4.21 | -4.21 | 28.76 | 4.97 | 28.9 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | -0.37 | -1.1 | -19.59 | 12 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -15.22 | -4.07 | -5.65 | -5.42 | 13.6 | 15.9 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -10.19 | -8.27 | -21.68 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | 1.21 | 26.01 | 32.98 | -10.07 | 77.3 | 77.3 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.79 | -0.57 | 1 | 1 | 8.25 | 7.36 | -4.58 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -1.12 | 0.57 | 1.15 | 28.94 | 12.82 | 30.13 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -2.97 | -2.02 | -12.44 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.4110806985514 | -2.33 | -7.64 | -4.41 | 0.64 | 12.72 | 12.72 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -5.21 | -4.31 | -10.53 | 12 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 168.87284393304373 | 103.69258923500948 | -16.67 | 0.79 | 0.0 | 12.76 | 30.41 | 30.41 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -3.02 | -4.75 | -20.79 | 22 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -5.83 | -2.3 | 13.93 | 88.87 | 28.36 | 86.28 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -4.74 | -3.49 | -9.95 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.8880515092684 | -5.82 | 6.99 | -19.83 | -7.36 | 9.48 | 9.48 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -5.42 | -4.05 | -21.28 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -17.27 | -11.47 | -2.13 | 102.32 | 35.4 | 100.92 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.15 | -0.24 | 1 | 1 | -13.09 | -11.53 | -23.37 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -4.48 | -5.8 | -24.47 | 12.54 | 1.34 | 11.99 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -6.45 | -6.16 | -35.54 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859532 | 66.26826344206586 | -1.57 | 4.43 | -0.7 | 2.35 | 5.2 | 12.3 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 1.42 | 1.01 | -5.35 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -1.55 | -0.78 | 4.37 | -14.92 | 19.38 | 19.38 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -2.92 | -1.97 | -16.96 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.9899000027612 | -5.93 | -4.6 | 11.59 | 6.73 | 13.71 | 24.77 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -4.63 | -4.26 | -18.21 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -2.19 | 8.12 | -2.34 | -12.57 | 15.93 | 15.93 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | 1.97 | 1.87 | -6.98 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | -9.92 | -5.74 | 14.24 | 51.98 | 46.19 | 64.29 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -8.39 | -7.32 | -22.99 | 12 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 3.67 | 117.31 | 95.67 | 291.68 | 161.57 | 462.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 42.25 | 36.39 | -7.76 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -16.78 | -5.39 | -10.07 | -19.38 | 14.19 | 14.19 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -9.09 | -9.6 | -23.64 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -3.5 | 5.53 | 2.48 | 5.98 | 23.38 | 23.38 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -1.06 | -0.67 | -7.81 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | 2.27 | 12.81 | 13.52 | 26.22 | 21.55 | 26.67 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 6.18 | 5.15 | -8.38 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 56.8306808099056 | 32.980802133096326 | -8.57 | -6.97 | -8.17 | -21.07 | 28.23 | 28.23 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -8.26 | -7.93 | -30.57 | 11 | selected |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.7524441579672 | -12.92 | 18.37 | 21.33 | 176.81 | 83.38 | 176.81 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 1.93 | 0.46 | -15.64 |  | fail_already_priced_in |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256228 | 122.99025793829806 | 2.87 | 4.07 | 1.13 | 1.13 | 7.19 | 7.19 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 3.68 | 2.76 | -2.72 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416136 | -9.39 | 10.92 | -2.65 | 40.23 | 18.78 | 46.02 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -2.99 | -1.92 | -10.41 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral |  | 85.85523299528691 | -80.47361399939216 | -1.2 | -2.08 | -4.08 | -13.65 | 1.54 | 1.54 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -1.66 | -1.53 | -7.06 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -3.1 | -0.21 | -9.87 | -10.54 | 14.02 | 14.02 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -1.17 | -0.96 | -21.68 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -0.37 | -12.96 | -10.83 | -0.5 | 5.27 | 5.27 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -1.66 | -2.81 | -18.47 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -2.6 | 1.05 | -0.44 | -10.27 | 6.32 | 6.32 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -1.68 | -1.62 | -7.04 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 157.1373893517917 | 73.07026244678458 | -0.8 | 1.96 | -2.66 | -4.54 | 2.92 | 2.92 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | 0.31 | 0.09 | -8.09 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround | B_可觀察 | 51.324855309264144 | 62.70887823307178 | -0.9 | 16.25 | 15.03 | 23.68 | 25.57 | 30.56 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 8.85 | 7.2 | -10.84 | 16 | selected |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.28273043969428 | -2.07 | 3.04 | 39.25 | 58.85 | 44.51 | 61.22 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 1.87 | 2.25 | -11.9 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122 | -2.07 | 1.14 | 7.9 | 5.81 | 10.59 | 14.15 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.36 | -0.23 | -10.01 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.5 | -0.5 | -6.31 | -0.99 | 0.25 | 1.78 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.69 | -0.98 | -8.86 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 9.47 | 12.24 | -17.65 | 23.72 | 18.22 | 34.34 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 6.23 | 5.66 | -39.75 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -1.92 | -2.94 | -8.02 | 2.74 | 6.24 | 6.24 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -3.77 | -4.08 | -24.05 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.75664630034535 | 42.38105078727345 | 0.0 | 4.74 | -11.96 | 4.29 | 6.58 | 8.48 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 1.42 | 0.83 | -16.21 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | -8.25 | -14.95 | 9.89 | 41.0 | 48.45 | 48.45 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -11.06 | -9.25 | -25.08 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.86953907106725 | -16.48 | 29.44 | 42.38 | 66.67 | 105.64 | 105.64 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -6.71 | -2.95 | -23.53 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -1.22 | 3.49 | -2.09 | 28.99 | 8.54 | 34.64 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -2.16 | -1.49 | -23.61 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.01687411836724 | 29.7636013582763 | -8.86 | 9.71 | -3.52 | -15.91 | 17.55 | 17.55 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -0.31 | -1.13 | -10.56 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -0.12 | 1.2 | -16.33 | 17.48 | 4.35 | 15.23 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -0.43 | -1.44 | -20.45 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -5.08 | 7.59 | 4.05 | 0.74 | 14.17 | 14.17 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -2.14 | -1.29 | -12.74 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -10.76 | 16.55 | 23.48 | 26.84 | 71.52 | 71.52 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -4.2 | -2.23 | -21.13 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -0.35 | 14.48 | 38.2 | 28.65 | 76.45 | 76.45 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | 4.13 | 4.56 | -4.47 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | 0.47 | 4.37 | 0.47 | 0.94 | 5.91 | 5.91 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 2.33 | 1.54 | -5.7 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -1.58 | 0.9 | 1.81 | -15.0 | 24.67 | 24.67 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -3.48 | -2.05 | -9.66 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -3.86 | 4.98 | -9.12 | -2.32 | 9.82 | 9.82 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -1.23 | -1.17 | -11.04 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -17.53 | 25.7 | 46.79 | 113.74 | 89.19 | 110.92 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -8.46 | -4.36 | -23.81 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -9.9 | -12.96 | -7.84 | -0.35 | 4.44 | 5.22 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -9.24 | -9.24 | -25.4 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -8.85 | 20.02 | 41.49 | 14.87 | 127.62 | 127.62 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | 3.95 | 4.67 | -9.27 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -2.04 | 0.66 | -20.19 | -12.55 | 3.4 | 3.4 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -1.25 | -2.41 | -24.17 | 14 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -5.01 | -1.64 | 9.76 | 31.39 | 14.29 | 36.36 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -2.86 | -2.52 | -12.62 | 19 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -8.45 | 23.75 | 37.87 | 53.83 | 52.1 | 55.35 | True | 距60日低點反彈>50% | mild_accumulation | 3.37 | -0.24 | 2 | 1 | 4.59 | 4.69 | -20.62 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | 0.0 | 10.25 | -1.11 | 12.7 | 12.7 | 13.78 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | 4.46 | 2.66 | -11.25 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360124 | 126.26534387085924 | -1.38 | 0.0 | -14.63 | -36.44 | 1.42 | 1.42 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -2.47 | -2.24 | -20.56 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.7784771532576 | 102.83428395752624 | -3.33 | 26.9 | 79.18 | 83.8 | 146.61 | 146.61 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -1.84 | 2.82 | -10.51 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976644 | 36.46696724530479 | -14.45 | -17.93 | -3.16 | 47.02 | 34.55 | 45.34 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -13.53 | -12.62 | -32.01 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 71.39293333177902 | 252.79681111256323 | 5.05 | 14.4 | 8.56 | -23.97 | 42.21 | 42.21 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | 6.61 | 5.99 | -11.58 | 10 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -8.38 | 25.19 | 87.43 | 21.93 | 111.61 | 134.29 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -1.15 | 0.42 | -11.83 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.9984662091176 | 44.59053152341543 | -15.47 | 11.06 | 3.48 | -10.16 | 41.25 | 41.25 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -3.39 | -4.2 | -17.99 | 16 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | -1.29 | 8.02 | -2.97 | 13.37 | 17.8 | 17.8 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -1.51 | -0.4 | -12.26 | 22 | selected |
| 3703 | 欣陸 | 建材營造 | neutral | D_降級_TDCC轉弱 | 89.3174912383306 | 3.447593197203932 | 5.1 | 5.1 | 0.24 | -0.72 | 7.57 | 7.57 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.92 | 3.49 | -1.9 | 13 | selected |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -2.43 | 1.65 | -11.95 | -1.35 | 3.48 | 3.48 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -0.48 | -2.2 | -16.18 | 17 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | -4.61 | -0.43 | -9.61 | -20.09 | 8.76 | 8.76 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -3.76 | -3.54 | -12.17 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -3.6 | 8.5 | 6.77 | -22.99 | 49.72 | 49.72 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | 3.32 | 2.94 | -6.94 | 23 | selected |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 9.36 | 16.31 | 11.41 | -2.99 | 41.75 | 41.75 | False |  | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 7.9 | 8.09 | -3.39 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -12.42 | -12.23 | 3.28 | -7.88 | 26.23 | 26.23 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -10.35 | -8.95 | -20.74 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -7.33 | 5.38 | -0.96 | -3.07 | 19.65 | 19.65 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -2.81 | -3.0 | -11.04 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | -1.94 | 7.56 | -5.16 | 63.96 | 15.56 | 63.7 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -1.8 | -0.42 | -11.01 | 17 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | 3.45 | 14.61 | 20.85 | 23.94 | 28.95 | 34.56 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 9.34 | 8.08 | -2.86 | 13 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -5.98 | 11.39 | 16.74 | -23.98 | 48.52 | 48.52 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | 1.82 | 1.62 | -8.76 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 109.68927823663152 | 90.15073758650963 | -5.94 | -7.82 | 16.02 | -9.79 | 28.03 | 29.67 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -5.57 | -4.95 | -13.04 | 19 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | -4.89 | -0.85 | 30.6 | -16.86 | 66.67 | 66.67 | True | 距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | -0.09 | -0.2 | -10.49 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -3.23 | 12.23 | -5.1 | -39.12 | 37.33 | 37.33 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | 5.72 | 4.3 | -9.35 | 20 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.15622840056231 | 37.709946899313486 | -1.64 | -2.96 | -7.22 | 8.43 | 1.98 | 24.14 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -3.47 | -3.0 | -10.0 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -0.64 | 3.33 | -6.2 | -9.88 | 3.68 | 3.68 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 1.27 | 0.63 | -7.6 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623696 | 1394.301991029742 | -1.81 | -0.23 | -6.47 | -5.65 | 2.12 | 6.11 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -1.36 | -1.18 | -7.26 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | 6.76 | 17.03 | 39.05 | 79.69 | 110.83 | 152.27 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | 12.09 | 12.04 | -2.5 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | -13.61 | 15.18 | 42.45 | 29.26 | 58.64 | 58.64 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 2.57 | 2.32 | -17.88 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -11.62 | -2.74 | -26.55 | 42.0 | 3.9 | 38.13 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -13.27 | -11.03 | -38.79 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | -3.0 | -3.21 | -6.42 | -0.66 | 0.67 | 8.78 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -2.4 | -2.38 | -10.32 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -8.98 | 14.78 | 9.12 | 58.2 | 40.05 | 61.19 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -0.74 | -0.17 | -12.57 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | 14.48 | 27.5 | 45.71 | 63.72 | 79.89 | 79.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 18.33 | 16.83 | -2.39 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -5.54 | 39.45 | 108.99 | 184.07 | 223.63 | 234.2 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | 11.71 | 10.41 | -10.61 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 1.81 | 2.88 | 38.87 | 63.75 | 41.37 | 63.07 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 2.44 | 3.09 | -2.96 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | -6.45 | 12.56 | -2.57 | 14.12 | 23.56 | 23.56 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | 1.51 | 0.86 | -8.7 | 19 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -3.55 | 4.79 | -6.08 | -22.59 | 24.49 | 24.49 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -5.52 | -3.44 | -21.36 |  | fail_low_response_condition |
| 6415 | 矽力*-KY | 半導體業 | mainstream_growth |  | 50.70369959160158 | 35.171695901726686 | 8.07 | 13.62 | -1.65 | 11.36 | 31.35 | 31.35 | False |  | mild_accumulation | 0.19 | 0.5 | 1 | 2 | 8.14 | 6.78 | -7.31 |  | fail_low_response_condition |
| 6416 | 瑞祺電通 | 通信網路業 | mainstream_growth |  | 59.15082767856138 | 30.6291038143077 | 0.83 | 2.54 | 14.15 | 49.38 | 41.52 | 53.75 | False |  | strong_accumulation | 1.01 | 0.62 | 2 | 2 | 1.66 | 3.27 | -6.2 |  | fail_low_response_condition |