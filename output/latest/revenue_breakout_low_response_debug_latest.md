# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-20 19:37:45 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 760907 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 88 |
| already_priced_in_excluded | 37 |
| overheat_pass | 51 |
| score_pass | 51 |
| theme_priority_pass | 45 |
| final_rows | 45 |

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
| fail_low_response_condition | 248 |
| fail_already_priced_in | 37 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | -7.21 | 25.42 | 50.25 | 234.84 | 118.45 | 268.16 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 5.98 | 5.58 | -15.55 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.28677537399296 | -15.3 | 0.0 | 7.17 | 27.78 | 38.43 | 49.8 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -2.76 | -2.88 | -21.73 | 18 | selected |
| 1316 | 上曜 | 建材營造 | neutral |  | 74.66249568827091 | 115.02921243693272 | -1.44 | -3.29 | 0.98 | -6.36 | 9.69 | 9.69 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -1.81 | -1.98 | -17.6 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | -0.79 | -2.14 | -5.62 | -11.89 | 1.0 | 1.0 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.31 | -1.88 | -8.53 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | -0.42 | -3.09 | -11.82 | -13.92 | 1.08 | 1.08 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | -1.7 | -1.79 | -14.39 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral |  | 70.45469720237698 | 47.58022431497226 | 0.0 | 14.6 | 17.73 | 14.1 | 22.17 | 22.17 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 6.96 | 5.61 | -4.07 |  | fail_low_response_condition |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | -2.7 | 2.27 | -6.49 | -6.98 | 4.35 | 6.19 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -1.64 | -1.39 | -8.16 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | 0.23 | 1.17 | -1.59 | 0.7 | 3.34 | 13.35 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.13 | -0.35 | -11.45 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 1.58 | 2.67 | 8.46 | 8.26 | 14.48 | 23.82 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 0.51 | 0.32 | -5.41 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | 0.0 | -0.74 | -3.93 | -14.06 | 1.51 | 1.51 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -0.35 | -0.26 | -6.27 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.1590750288686 | 59.11214720338166 | -3.54 | -0.41 | -3.92 | -6.49 | 4.26 | 4.26 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -2.08 | -1.95 | -8.24 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 37.92 | 32.97 | 6.61 | -8.85 | 44.36 | 44.36 | True | 近20日漲幅>25% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 31.51 | 27.26 | 0.0 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | -3.62 | -2.02 | -12.62 | 2.3 | 3.9 | 4.1 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | -0.92 | -1.9 | -14.99 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -5.14 | 0.36 | 2.97 | -12.06 | 35.78 | 35.78 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -3.67 | -3.91 | -15.55 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -4.02 | 19.0 | 23.62 | 106.26 | 53.41 | 111.75 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | 6.64 | 5.23 | -8.61 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -3.55 | 0.62 | -8.84 | 5.71 | 2.52 | 5.98 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -0.85 | -2.0 | -10.34 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350685 | 27.89987013024577 | -1.43 | 1.78 | -0.29 | 24.19 | 10.97 | 24.64 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | 0.56 | -0.09 | -7.4 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576108 | 74.19480655845219 | -1.69 | -2.78 | -7.16 | -22.74 | 2.64 | 2.64 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -1.88 | -2.33 | -13.58 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 63462.77980218637 | 14769.518174623092 | -2.82 | 1.02 | 7.64 | 21.48 | 12.38 | 22.99 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 3.23 | 2.14 | -8.73 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | 1.5 | 9.31 | 10.66 | 21.62 | 18.94 | 23.85 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | 0.47 | 1.21 | -10.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072263 | 167.83532632168345 | 0.4 | -17.85 | 23.17 | 149.08 | 47.66 | 152.5 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -12.19 | -10.4 | -33.05 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -8.02 | -6.59 | -15.14 | -34.86 | 0.0 | 0.0 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -6.79 | -7.35 | -27.84 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 270.34068105049295 | 167.43229879771584 | 0.85 | -1.81 | -10.91 | -9.97 | 4.01 | 4.01 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -0.35 | -1.24 | -17.79 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -3.96 | 13.76 | 2.57 | 125.45 | 42.89 | 166.99 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | 1.39 | 2.64 | -10.0 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | -0.66 | -2.75 | -5.21 | 6.0 | 2.39 | 16.47 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -2.6 | -2.28 | -7.68 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -17.25 | 0.74 | 59.24 | 237.65 | 112.84 | 248.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -10.99 | -3.23 | -26.77 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.10669499309349 | -3.41 | -0.82 | 0.0 | 5.71 | 10.32 | 10.32 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -3.49 | -2.62 | -7.14 | 14 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -6.1 | -14.16 | -22.78 | -35.28 | 8.93 | 8.93 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -13.02 | -12.0 | -30.8 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.6686868151223 | 187.3908590670214 | -5.57 | -10.29 | -5.28 | 59.85 | 30.34 | 57.87 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -10.84 | -9.5 | -20.98 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 66.12554142816796 | 62.44981435880206 | -3.43 | 9.44 | -15.27 | -21.36 | 11.3 | 11.3 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | 0.56 | -0.98 | -24.08 | 18 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -1.49 | 10.61 | 12.76 | 21.18 | 18.71 | 23.29 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | 2.34 | 2.42 | -4.81 | 26 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644916 | 83.289853268924 | 0.0 | -5.28 | -11.62 | -2.78 | 4.79 | 4.79 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -1.46 | -1.09 | -11.39 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.36147799625845 | 35.28859580878607 | -6.46 | -17.86 | 19.21 | 23.73 | 57.66 | 57.66 | True | 距60日低點反彈>50% | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -9.53 | -8.43 | -23.93 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | 4.71 | -2.44 | -4.76 | 29.03 | 6.57 | 29.59 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 1.27 | 0.37 | -18.37 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 206.46824005093208 | 119.5343671101157 | -9.09 | -4.08 | -7.19 | -13.42 | 13.31 | 15.61 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -10.24 | -7.85 | -21.88 | 16 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 55.462822673426 | 69.0679079756067 | 1.28 | 24.74 | 25.93 | -17.71 | 68.09 | 68.09 | True | 距60日低點反彈>50% | distribution_warning | -0.79 | -0.57 | 1 | 1 | 1.59 | 1.63 | -9.54 |  | fail_already_priced_in |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -0.14 | 0.0 | 0.14 | 27.24 | 13.78 | 28.86 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -2.14 | -1.09 | -11.69 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.4110806985514 | -0.77 | -6.83 | -4.61 | 0.79 | 14.87 | 14.87 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -3.06 | -2.28 | -8.82 | 13 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 168.87284393304373 | 103.69258923500948 | -10.82 | 5.32 | -2.94 | 4.0 | 25.83 | 25.83 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -6.65 | -7.47 | -23.57 | 21 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth |  | 73.13984715432697 | 49.07547452931974 | -4.74 | -0.29 | 14.0 | 73.16 | 29.3 | 76.29 | True | 近120日漲幅>70% | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -4.03 | -2.55 | -9.28 |  | fail_already_priced_in |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.8880515092684 | -2.76 | 6.02 | -15.44 | -13.63 | 9.09 | 9.09 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -6.01 | -4.04 | -17.66 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | -13.52 | -13.52 | -0.94 | 78.06 | 31.06 | 74.02 | True | 近120日漲幅>70% | distribution_warning | -0.15 | -0.24 | 1 | 1 | -15.32 | -13.34 | -25.83 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -2.3 | -7.1 | -25.76 | 10.21 | 1.04 | 11.48 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -6.39 | -5.93 | -35.73 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859532 | 66.26826344206586 | -2.45 | 1.64 | -2.11 | 0.18 | 3.72 | 10.71 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.1 | -0.38 | -6.69 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | -1.31 | -2.08 | 5.32 | -16.44 | 17.5 | 17.5 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -4.35 | -3.22 | -18.26 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.9899000027612 | -2.36 | -2.71 | 10.22 | 1.51 | 7.8 | 24.77 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -4.5 | -3.92 | -18.21 | 21 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -0.94 | 8.76 | 0.32 | -9.83 | 17.22 | 17.22 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | 2.68 | 2.75 | -5.94 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 77.97383382912092 | 36.66345172530179 | -7.07 | -4.74 | 15.15 | 47.41 | 44.92 | 62.86 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -8.98 | -7.5 | -23.66 | 12 | selected |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | -4.64 | 120.49 | 117.31 | 298.59 | 161.57 | 462.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 36.93 | 32.38 | -8.13 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -13.13 | -6.94 | -10.22 | -16.72 | 12.33 | 12.33 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -10.27 | -10.24 | -24.88 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -4.33 | 1.67 | 0.83 | 6.58 | 20.9 | 20.9 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -3.13 | -2.46 | -9.67 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -5.71 | 12.38 | 14.15 | 23.89 | 22.22 | 25.61 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 6.14 | 5.23 | -7.87 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.8306808099056 | 32.980802133096326 | -5.24 | -9.17 | -12.97 | -30.08 | 24.92 | 24.92 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -10.22 | -9.53 | -32.36 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.7524441579672 | -5.87 | 24.24 | 23.0 | 166.43 | 85.89 | 169.34 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -1.19 | 1 | 1 | 2.3 | 1.68 | -14.48 |  | fail_already_priced_in |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256228 | 122.99025793829806 | 1.7 | 4.06 | 1.41 | -1.37 | 7.49 | 7.49 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 3.76 | 2.79 | -2.45 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416136 | -8.75 | 8.46 | -2.57 | 36.15 | 18.03 | 45.11 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -3.96 | -2.33 | -10.98 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral | B_可觀察 | 85.85523299528691 | -80.47361399939216 | -0.6 | -3.52 | -4.36 | -12.96 | 2.81 | 2.81 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -1.48 | -1.4 | -7.06 | 17 | selected |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -5.26 | -5.93 | -12.52 | -12.69 | 10.25 | 10.25 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -4.15 | -3.89 | -24.27 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | 1.39 | -14.3 | -10.68 | 0.5 | 5.8 | 5.8 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -0.34 | -2.13 | -18.06 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -3.2 | -1.62 | -0.89 | -11.9 | 5.21 | 5.21 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -2.62 | -2.43 | -8.01 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 157.1373893517917 | 73.07026244678458 | -0.3 | -0.3 | -2.57 | -4.93 | 2.5 | 2.5 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -0.08 | -0.29 | -8.47 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -0.61 | 13.99 | 14.39 | 22.1 | 24.43 | 29.37 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 7.15 | 5.68 | -11.65 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.28273043969428 | -3.7 | -2.9 | 38.46 | 54.76 | 42.68 | 59.18 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 0.73 | 0.88 | -13.01 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122 | -3.01 | -0.14 | 7.93 | 4.73 | 10.28 | 13.83 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.63 | -0.47 | -10.27 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.74 | -1.23 | -5.88 | -1.23 | 0.0 | 1.52 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.88 | -1.12 | -9.09 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | -1.01 | -0.61 | -18.71 | 13.92 | 9.11 | 23.99 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | -1.93 | -2.28 | -44.39 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -1.77 | -4.8 | -8.72 | 0.0 | 4.91 | 4.91 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -4.74 | -4.86 | -25.0 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 56.75664630034535 | 42.38105078727345 | 1.67 | 4.27 | -11.59 | 5.63 | 7.02 | 8.93 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 1.62 | 1.14 | -12.54 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | -4.34 | -16.88 | 8.94 | 33.82 | 43.79 | 43.79 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -13.09 | -11.2 | -27.43 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.86953907106725 | -10.12 | 30.74 | 46.6 | 53.14 | 107.7 | 107.7 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -6.8 | -1.81 | -22.76 |  | fail_already_priced_in |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | 0.79 | 0.9 | -2.71 | 26.34 | 9.39 | 35.7 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -1.43 | -0.65 | -23.0 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth | A_優先追蹤 | 54.01687411836724 | 29.7636013582763 | -8.5 | 6.06 | -5.56 | -25.63 | 14.29 | 14.29 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -3.35 | -3.56 | -13.04 | 16 | selected |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -2.68 | -0.12 | -17.33 | 10.16 | 3.73 | 11.19 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -1.01 | -1.86 | -20.93 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -1.89 | 1.72 | 0.0 | -1.43 | 15.28 | 15.28 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -1.27 | -0.31 | -11.89 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -10.59 | 12.23 | 17.75 | 15.81 | 61.56 | 61.56 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -10.2 | -7.29 | -25.7 |  | fail_already_priced_in |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -0.87 | 12.95 | 39.66 | 21.8 | 73.39 | 73.39 | True | 距60日低點反彈>50% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | 1.73 | 2.51 | -6.13 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | 0.0 | 3.38 | 0.47 | 0.47 | 5.42 | 5.42 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 1.69 | 0.98 | -6.14 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | -1.6 | -2.98 | 0.54 | -16.94 | 23.11 | 23.11 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -4.54 | -3.01 | -10.79 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -0.54 | 3.19 | -8.03 | -1.26 | 10.22 | 10.22 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -1.03 | -0.74 | -10.71 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -17.14 | 18.3 | 50.88 | 98.57 | 87.84 | 102.55 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -9.75 | -4.64 | -24.35 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -7.36 | -14.24 | -7.67 | -10.93 | 2.59 | 3.36 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -10.18 | -10.04 | -26.72 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -0.61 | 18.85 | 41.13 | 13.7 | 123.48 | 123.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | 1.24 | 2.53 | -10.92 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 90.47990444398276 | 46.685682375869504 | -3.92 | 0.0 | -21.81 | -12.45 | 2.72 | 2.72 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -1.9 | -2.8 | -24.67 | 14 | selected |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | 1.07 | 1.34 | 8.93 | 34.52 | 20.0 | 43.18 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | 1.93 | 2.15 | -8.25 | 20 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth |  | 446.4684953621241 | 68.26830170354926 | -17.4 | 26.35 | 36.7 | 53.28 | 50.81 | 54.04 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 3.37 | -0.24 | 2 | 1 | 2.59 | 3.47 | -21.3 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -2.19 | 11.18 | 0.28 | 11.53 | 13.65 | 14.74 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | 4.79 | 3.22 | -10.5 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360124 | 126.26534387085924 | -3.79 | -1.76 | -18.42 | -34.51 | 0.0 | 0.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.78 | -4.26 | -22.5 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.7784771532576 | 102.83428395752624 | -4.32 | 19.15 | 76.83 | 65.31 | 143.94 | 143.94 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -3.65 | 1.56 | -11.49 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976644 | 36.46696724530479 | -8.99 | -18.0 | -9.18 | 29.67 | 30.45 | 30.45 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -15.38 | -14.19 | -34.07 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 71.39293333177902 | 252.79681111256323 | 2.96 | 8.55 | 4.92 | -33.4 | 36.68 | 36.68 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | 2.05 | 1.71 | -15.02 | 11 | selected |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | -4.86 | 24.18 | 79.25 | 25.47 | 114.52 | 137.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -0.76 | 1.65 | -10.62 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 495.9984662091176 | 44.59053152341543 | -10.23 | 10.47 | 3.7 | -14.35 | 38.4 | 38.4 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -5.76 | -5.65 | -19.65 | 15 | selected |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | -3.4 | 2.25 | -6.58 | 8.61 | 16.77 | 16.77 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -2.47 | -1.17 | -13.03 | 22 | selected |
| 3703 | 欣陸 | 建材營造 | neutral |  | 89.3174912383306 | 3.447593197203932 | 2.49 | 3.26 | 0.0 | 0.24 | 7.57 | 7.57 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.75 | 3.19 | -1.9 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -2.77 | 0.25 | -12.28 | -2.65 | 3.99 | 3.99 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | 0.01 | -1.57 | -15.76 | 18 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 0.42 | -1.87 | -6.24 | -21.41 | 10.63 | 10.63 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | -2.02 | -1.73 | -10.66 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -2.63 | 9.28 | 5.71 | -27.65 | 44.69 | 44.69 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -0.58 | -0.47 | -10.07 | 21 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513512 | 31.81289526994584 | -2.73 | 0.28 | 4.4 | 1.71 | 8.54 | 8.54 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -2.0 | -1.6 | -8.72 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround | B_可觀察 | 81.03484942822955 | 11.010961782504076 | 4.69 | 11.08 | 9.84 | -7.73 | 37.57 | 37.57 | False |  | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 4.18 | 4.48 | -6.23 | 17 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | -9.78 | -12.31 | 2.01 | -12.88 | 25.31 | 25.31 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -10.44 | -8.89 | -21.32 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -6.64 | 2.26 | -3.78 | -6.43 | 18.63 | 18.63 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -3.74 | -3.52 | -11.8 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | 1.0 | -1.94 | -2.42 | 59.56 | 15.56 | 63.7 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | -1.71 | -0.39 | -11.01 | 17 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth |  | 86.87811970952995 | 13.790026773850077 | 2.44 | 16.15 | 20.41 | 29.15 | 32.74 | 38.52 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 11.68 | 10.23 | -1.41 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -3.18 | 7.47 | 11.41 | -24.67 | 46.48 | 46.48 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | 0.07 | 0.2 | -10.01 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663152 | 90.15073758650963 | -5.51 | -8.3 | 14.52 | -12.65 | 25.51 | 27.11 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -7.04 | -6.29 | -14.75 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | -1.72 | -1.16 | 27.14 | -21.38 | 62.86 | 62.86 | True | 距60日低點反彈>50% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | -2.31 | -2.28 | -12.53 |  | fail_already_priced_in |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | B_可觀察 | 56.623935956655565 | 70.86506389755786 | 0.29 | 14.86 | -2.13 | -33.2 | 37.33 | 37.33 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | 5.0 | 3.92 | -9.35 | 17 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.15622840056231 | 37.709946899313486 | 1.67 | -2.92 | -7.34 | 10.24 | 3.68 | 26.21 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -1.72 | -1.27 | -8.5 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | 0.0 | 2.31 | -5.77 | -10.52 | 3.85 | 3.85 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | 1.32 | 0.73 | -7.45 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623696 | 1394.301991029742 | -1.14 | -1.37 | -6.09 | -6.49 | 1.65 | 5.62 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -1.75 | -1.5 | -7.49 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | 15.47 | 20.61 | 39.16 | 70.57 | 115.52 | 157.88 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | 13.47 | 13.16 | -7.01 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 0.26 | 28.81 | 55.74 | 35.23 | 72.73 | 72.73 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | 10.3 | 10.36 | -10.59 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -7.39 | -4.91 | -33.23 | 29.4 | 3.9 | 38.13 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -13.08 | -10.2 | -38.79 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral | B_可觀察 | 249.504576436222 | 315.5434384267611 | -1.41 | -4.83 | -6.49 | 0.44 | 1.0 | 9.15 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.83 | -1.89 | -10.02 | 19 | selected |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -7.49 | 14.92 | 9.21 | 54.83 | 38.88 | 59.84 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -2.19 | -0.92 | -13.3 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 81.57256696034645 | 71.39362622544883 | 22.94 | 43.59 | 55.99 | 79.2 | 97.53 | 97.53 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.36 | -0.69 | 1 | 1 | 27.42 | 25.33 | 0.0 |  | fail_low_response_condition |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -5.79 | 51.31 | 118.05 | 158.28 | 216.03 | 226.36 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | 7.11 | 7.12 | -12.7 |  | fail_already_priced_in |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth |  | 55.69095387442037 | 42.29598437707936 | 1.55 | 1.81 | 39.36 | 61.73 | 41.37 | 62.4 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 2.34 | 2.83 | -2.96 |  | fail_low_response_condition |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | 0.41 | 9.27 | -4.26 | 9.27 | 24.06 | 24.06 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | 1.49 | 1.16 | -8.33 | 19 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | 0.25 | -3.14 | -1.96 | -28.35 | 26.54 | 26.54 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -3.81 | -1.7 | -20.06 |  | fail_low_response_condition |