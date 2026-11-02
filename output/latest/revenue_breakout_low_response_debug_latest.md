# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-02 19:40:17 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1974 |
| standardized_revenue_rows | 1974 |
| price_rows | 774652 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 338 |
| price_metrics_pass | 336 |
| low_response_pass | 76 |
| already_priced_in_excluded | 21 |
| overheat_pass | 55 |
| score_pass | 55 |
| theme_priority_pass | 49 |
| final_rows | 49 |

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
| fail_low_response_condition | 260 |
| fail_already_priced_in | 21 |
| fail_defensive_or_traditional_excluded | 5 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 55.25857165202359 | 26.808140706895525 | 0.0 | 17.81 | 82.42 | 247.98 | 82.98 | 274.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -0.59 | 3.06 | -14.12 |  | fail_already_priced_in |
| 1312 | 國喬 | 塑膠工業 | cyclical_turnaround | B_可觀察 | 96.8052734253821 | 30.286775373992953 | -6.08 | -7.33 | 21.4 | 27.52 | 24.11 | 39.28 | False |  | strong_accumulation | 0.39 | 0.48 | 2 | 2 | -9.3 | -7.08 | -27.23 | 17 | selected |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 74.66249568827091 | 115.02921243693271 | 0.49 | -4.21 | 1.99 | -8.07 | 3.43 | 9.16 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -1.42 | -1.72 | -18.0 | 14 | selected |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 123.50472193074502 | 51.2203317347344 | 1.2 | -3.82 | 0.0 | -7.69 | 2.44 | 2.44 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -1.08 | -1.03 | -8.53 |  | fail_low_response_condition |
| 1410 | 南染 | 紡織纖維 | defensive_or_traditional |  | 109.17440660474716 | 15.717231056005874 | 1.06 | -1.45 | -7.59 | -11.55 | 2.59 | 2.59 | False |  | strong_accumulation | 0.06 | 0.05 | 3 | 3 | 0.15 | -0.28 | -10.71 |  | fail_low_response_condition |
| 1416 | 廣豐 | 其他 | neutral | B_可觀察 | 70.45469720237698 | 47.58022431497226 | 2.26 | 18.34 | 25.46 | 20.44 | 27.23 | 27.83 | False |  | mild_accumulation | 0.27 | -0.2 | 2 | 2 | 6.21 | 6.43 | -0.73 | 16 | selected |
| 1418 | 東華 | 紡織纖維 | defensive_or_traditional |  | 83.33333333333333 | 20.27214662593724 | 0.0 | -2.45 | -0.83 | -2.72 | 3.77 | 5.6 | False |  | mild_accumulation | 0.16 | 0.01 | 2 | 1 | -2.17 | -1.17 | -8.67 |  | fail_low_response_condition |
| 1438 | 三地開發 | 建材營造 | neutral |  | 1566.053201360965 | 5529.984963864772 | -0.23 | 1.65 | -6.11 | 2.38 | 2.63 | 10.26 | False |  | strong_accumulation | 0.21 | 0.21 | 3 | 3 | -0.7 | -0.72 | -8.9 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 11850.939663699308 | 120.98616118153274 | 2.83 | 3.37 | 4.68 | 9.81 | 9.19 | 24.89 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | 0.81 | 0.72 | -4.59 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 654.35225360843 | -47.62586374099816 | -1.13 | -1.87 | -4.36 | -12.91 | 0.38 | 0.38 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -1.79 | -1.83 | -7.07 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 152.15907502886859 | 59.11214720338166 | -4.96 | -8.0 | -5.74 | -14.18 | 1.77 | 1.77 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -6.83 | -5.84 | -13.86 |  | fail_low_response_condition |
| 1516 | 川飛 | 其他 | neutral |  | 1473.25746799431 | 48.70117100205596 | 6.74 | 45.59 | 23.36 | -9.17 | 54.09 | 54.09 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | 0.0 | -0.36 | 0 | 0 | 22.81 | 15.54 | -24.86 |  | fail_low_response_condition |
| 1530 | 亞崴 | 電機機械 | cyclical_turnaround |  | 267.4255691768827 | 5.35072235712996 | 2.26 | 1.12 | -1.99 | 2.46 | 5.65 | 5.65 | False |  | distribution_warning | -0.27 | -0.13 | 1 | 0 | 0.76 | 0.39 | -10.56 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 62.31587090838761 | 46.95702744919681 | -0.74 | -8.53 | 7.2 | -29.1 | 8.5 | 31.37 | False |  | mild_accumulation | 0.19 | 0.97 | 1 | 2 | -7.25 | -5.95 | -18.29 |  | fail_low_response_condition |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 57.38899555820582 | 60.12128130883619 | -5.19 | 5.15 | 20.91 | 75.43 | 27.11 | 86.56 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.27 | 1 | 1 | -7.02 | -4.04 | -16.99 |  | fail_already_priced_in |
| 1723 | 中碳 | 化學工業 | cyclical_turnaround |  | 61.873094432402574 | 20.40781330899844 | -1.49 | -1.61 | -4.91 | -1.0 | 0.63 | 2.19 | False |  | distribution_warning | -0.5 | -0.05 | 1 | 1 | -3.32 | -2.98 | -12.65 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 90.53815615350683 | 27.89987013024577 | -3.72 | -5.82 | 0.78 | -14.76 | 2.37 | 4.35 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -4.93 | -4.52 | -12.92 |  | fail_low_response_condition |
| 1795 | 美時 | 生技醫療業 | defensive_or_traditional |  | 127.96520572576107 | 74.19480655845219 | -4.35 | -7.82 | -11.76 | -19.71 | 0.0 | 0.0 | False |  | mild_accumulation | 0.68 | 0.6 | 3 | 1 | -6.36 | -5.96 | -18.52 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | D_降級_TDCC轉弱 | 63462.779802186364 | 14769.518174623092 | 4.72 | 12.16 | 7.25 | 22.84 | 13.96 | 26.56 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | 3.61 | 2.17 | -6.08 | 18 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 163.02984286280207 | 139.012352909764 | -7.84 | -15.7 | 3.78 | -4.26 | 5.11 | 10.27 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -8.52 | -6.68 | -17.67 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 196.22466238072266 | 167.83532632168345 | -3.43 | -21.86 | 9.09 | 79.43 | 8.03 | 111.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -11.1 | -11.12 | -37.55 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 64.80785695673214 | 69.66548699152172 | -8.06 | -13.31 | -28.3 | -36.13 | 1.33 | 1.33 | False |  | mild_accumulation | -0.11 | 0.1 | 0 | 1 | -9.51 | -8.88 | -31.74 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround |  | 270.34068105049295 | 167.43229879771584 | -2.39 | -4.35 | -14.24 | -11.86 | 0.7 | 0.7 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -3.13 | -3.44 | -21.1 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 62.49950646855218 | 37.99668163097385 | -15.04 | -8.75 | 11.11 | 121.2 | 22.92 | 129.67 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -13.44 | -9.96 | -22.58 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 341.0996081666323 | 36.73292733062783 | 0.83 | -5.16 | -3.34 | 4.48 | 3.41 | 17.64 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -0.64 | -0.61 | -6.47 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 212.8023551877785 | 125.06233304493848 | -5.45 | -26.78 | 57.43 | 199.4 | 95.72 | 220.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -12.67 | -7.49 | -32.66 |  | fail_already_priced_in |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 54.64861207105231 | 41.106694993093484 | -2.31 | -6.05 | -1.69 | 4.95 | 0.87 | 6.88 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -5.39 | -4.22 | -10.04 | 13 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 188.23580475843863 | 154.50791645548554 | -3.32 | -21.47 | -12.94 | -42.74 | 3.22 | 4.79 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -11.09 | -10.32 | -33.43 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 256.6686868151223 | 187.3908590670214 | 4.85 | -9.75 | 13.29 | 32.79 | 12.5 | 44.64 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -3.14 | -2.7 | -16.06 | 17 | selected |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 66.12554142816796 | 62.44981435880206 | -9.01 | -9.01 | -30.84 | -33.68 | 3.86 | 3.86 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -15.78 | -13.56 | -37.76 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 158.6674544463884 | 97.96095815091336 | -4.83 | -0.42 | 3.05 | 13.72 | 11.05 | 17.68 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -4.81 | -3.62 | -9.13 | 25 | selected |
| 2348 | 海悅 | 其他 | neutral |  | 96.29795511644917 | 83.289853268924 | -0.86 | -2.41 | -7.39 | -1.99 | 3.14 | 3.14 | False |  | mild_accumulation | 0.47 | -0.02 | 2 | 1 | -1.95 | -2.12 | -12.78 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 57.361477996258444 | 35.28859580878607 | -8.42 | -14.11 | 14.7 | -1.37 | 15.81 | 44.76 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -12.47 | -12.23 | -30.16 |  | fail_low_response_condition |
| 2356 | 英業達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.87088005015264 | 42.7707850787262 | -1.49 | 0.17 | -6.73 | 12.88 | 5.86 | 18.96 | False |  | distribution_warning | -0.46 | -0.54 | 0 | 0 | 0.19 | -1.35 | -18.91 | 13 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 206.46824005093208 | 119.5343671101157 | -13.38 | -19.67 | -12.5 | -28.69 | 4.26 | 4.26 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -18.17 | -16.15 | -33.01 |  | fail_low_response_condition |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 55.462822673426 | 69.0679079756067 | -4.93 | -5.36 | 21.56 | -21.48 | 23.54 | 50.35 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -9.83 | -6.8 | -19.08 | 11 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 125.4495058048851 | 63.1715973040828 | -2.72 | -5.3 | 4.62 | 8.29 | 6.09 | 13.17 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -5.22 | -4.1 | -15.55 | 22 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 76.68901002964485 | 99.41108069855139 | -1.24 | -4.65 | 7.25 | -6.61 | 9.28 | 13.98 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -2.07 | -2.3 | -9.53 | 15 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 168.87284393304373 | 103.69258923500948 | -7.2 | -4.66 | -5.52 | -4.56 | 4.56 | 19.72 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -10.89 | -8.26 | -27.28 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.13984715432697 | 49.07547452931974 | -2.24 | -9.78 | 13.72 | 41.01 | 16.13 | 49.2 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -6.52 | -5.06 | -13.13 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 62.28854584713688 | 107.88805150926841 | -6.72 | -9.54 | -7.93 | -13.92 | 10.06 | 10.06 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | -4.84 | -3.55 | -14.56 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 576.622775031737 | 626.9495065095125 | 10.27 | -12.04 | 15.13 | 42.21 | 14.13 | 71.94 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -4.33 | -3.17 | -19.77 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 288.57555652794366 | 133.8893219091609 | -5.88 | -16.8 | -35.4 | -7.14 | 1.63 | 1.63 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -9.79 | -9.2 | -41.02 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 98.87686452859533 | 66.26826344206586 | -0.88 | 1.45 | -0.71 | 5.85 | 4.28 | 11.31 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.51 | -0.13 | -6.19 |  | fail_low_response_condition |
| 2438 | 翔耀 | 光電業 | mainstream_growth |  | 147.79194078947367 | 73.54054213996717 | 0.0 | -6.78 | 3.06 | -13.11 | 8.8 | 15.94 | False |  | distribution_warning | -0.15 | -0.15 | 0 | 0 | -3.54 | -3.14 | -19.35 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth | A_優先追蹤 | 290.42308535778307 | 369.98990000276115 | 3.64 | -1.38 | 1.42 | -12.84 | 7.34 | 31.94 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | 1.19 | 0.93 | -13.51 | 24 | selected |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 97.546581301814 | 68.79855492084776 | -3.75 | -3.44 | -2.96 | -16.31 | 5.55 | 9.26 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -4.24 | -3.17 | -12.33 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth |  | 77.97383382912092 | 36.66345172530179 | 1.55 | -15.06 | 10.85 | 45.33 | 11.22 | 45.33 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -9.05 | -8.25 | -27.01 |  | fail_low_response_condition |
| 2466 | 冠西電 | 光電業 | mainstream_growth |  | 308.1627628894985 | 11.879848782904388 | 45.59 | 205.22 | 290.14 | 670.01 | 334.78 | 846.45 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.57 | 0 | 1 | 62.86 | 59.93 | -2.31 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 90.64998093808812 | 84.20298673328344 | -7.63 | -22.54 | -16.08 | -33.31 | 1.71 | 1.71 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -18.36 | -16.24 | -35.07 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 53.76058739003543 | 41.538820604314346 | -4.39 | -11.74 | -8.4 | -8.02 | 2.83 | 8.46 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -10.53 | -8.53 | -18.96 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 50.45285710544276 | 20.005024578212605 | -2.95 | 13.13 | 18.69 | 21.89 | 21.89 | 25.26 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 1.03 | 1.58 | -8.12 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 56.830680809905594 | 32.980802133096326 | -3.73 | -19.37 | -6.3 | -24.12 | 4.88 | 16.22 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -11.89 | -10.55 | -37.07 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 53.92880329001265 | 25.752444157967194 | -3.26 | 18.86 | 48.64 | 78.0 | 50.53 | 79.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.68 | -1.19 | 1 | 1 | -8.37 | -4.59 | -17.5 |  | fail_already_priced_in |
| 2505 | 國揚 | 建材營造 | neutral |  | 9237.193239256227 | 122.99025793829806 | -0.28 | 3.53 | -1.12 | -2.22 | 5.39 | 5.39 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | 0.28 | 0.13 | -4.35 |  | fail_low_response_condition |
| 2527 | 宏璟 | 建材營造 | neutral |  | 89.28166516468502 | 1013.5105380416137 | -0.83 | -4.5 | 5.99 | 40.03 | 15.9 | 46.02 | False |  | mild_accumulation | 0.41 | 0.42 | 1 | 2 | -3.54 | -1.33 | -10.41 |  | fail_low_response_condition |
| 2534 | 宏盛 | 建材營造 | neutral | B_可觀察 | 85.85523299528691 | -80.47361399939216 | -2.49 | -7.67 | -8.75 | -15.18 | 1.95 | 1.95 | False |  | mild_accumulation | -0.02 | 0.12 | 1 | 1 | -4.19 | -4.05 | -11.58 | 16 | selected |
| 2540 | 愛山林 | 建材營造 | neutral |  | 238.7027963385682 | 1.7315084840889938 | -0.44 | -6.5 | -24.5 | -14.85 | 6.71 | 6.71 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -4.87 | -4.26 | -22.96 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral | D_降級_TDCC轉弱 | 103.72653033246353 | 228.35972704120363 | -2.62 | 0.78 | -11.17 | -8.78 | 2.64 | 2.64 | False |  | distribution_warning | -1.65 | -1.77 | 1 | 0 | -0.96 | -3.39 | -20.51 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 719.4781016963254 | -1.300527989199485 | -0.45 | -3.92 | 1.07 | -13.91 | 4.58 | 4.58 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -2.17 | -1.95 | -8.56 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral |  | 157.1373893517917 | 73.07026244678458 | -3.14 | -2.35 | -7.18 | -4.88 | 0.21 | 0.21 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -2.17 | -2.31 | -11.07 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 51.324855309264144 | 62.70887823307178 | -0.91 | 12.07 | 20.82 | 22.64 | 22.64 | 28.97 | False |  | mild_accumulation | 0.05 | 0.05 | 1 | 1 | 2.1 | 2.79 | -11.92 |  | fail_low_response_condition |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 97.6272252761016 | 27.282730439694276 | 0.0 | 4.82 | 38.79 | 60.83 | 42.6 | 62.59 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | 2.11 | 2.21 | -11.15 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 99.17417457345871 | 25.531630157122002 | 0.57 | -1.39 | 6.96 | 4.59 | 10.12 | 13.67 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.65 | -0.4 | -10.39 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 68.88604770696023 | 37.12374134942713 | -0.99 | -0.99 | -6.56 | -1.48 | 1.27 | 1.27 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.64 | -0.79 | -8.9 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 131.25623973463013 | 156.50340708874322 | 19.84 | 15.13 | -11.21 | 20.82 | 30.22 | 47.98 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | 15.62 | 13.31 | -8.44 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 54.79190368647162 | 43.51844934663569 | -4.24 | -13.91 | -8.93 | -10.19 | 0.78 | 0.78 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -7.74 | -7.48 | -29.73 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 56.756646300345345 | 42.38105078727345 | 4.94 | 7.14 | 2.41 | 11.35 | 11.84 | 11.84 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 4.98 | 5.11 | -3.04 | 18 | selected |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 470.2347504677583 | 343.911329000345 | 11.54 | -8.74 | 31.82 | 20.55 | 25.78 | 62.11 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | 0.78 | -0.26 | -18.18 |  | fail_low_response_condition |
| 3016 | 嘉晶 | 半導體業 | mainstream_growth |  | 52.71443419630173 | 36.869539071067244 | -12.07 | -24.56 | 45.22 | 5.37 | 48.08 | 75.38 | True | 近60日漲幅>40% | strong_accumulation | 5.97 | 6.93 | 2 | 2 | -20.05 | -12.59 | -34.78 |  | fail_low_response_condition |
| 3022 | 威強電 | 電腦及週邊設備業 | mainstream_growth |  | 75.87160196530029 | 36.836131048328085 | -3.03 | -6.39 | -6.09 | 27.81 | 5.24 | 30.71 | False |  | strong_accumulation | 1.44 | 2.24 | 3 | 3 | -4.02 | -3.67 | -25.84 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 54.01687411836724 | 29.7636013582763 | -3.23 | -8.78 | -11.17 | -38.53 | 4.3 | 4.3 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -11.51 | -8.48 | -20.96 |  | fail_low_response_condition |
| 3033 | 威健 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 79.8677079320342 | 41.40595239529184 | -2.88 | -5.16 | -13.49 | -5.94 | 0.37 | 0.37 | False |  | distribution_warning | -0.72 | -0.74 | 0 | 1 | -3.96 | -3.92 | -23.48 | 13 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 60.01219345400749 | 101.25914660378932 | -3.99 | -0.49 | 0.0 | -27.99 | 12.67 | 13.61 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -3.62 | -2.44 | -13.16 | 17 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 64.66643811385126 | 37.73807717195555 | -8.11 | -15.15 | 15.26 | 11.77 | 14.2 | 52.68 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -13.53 | -9.05 | -29.79 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 53.500059681732026 | 40.60068600026104 | -5.22 | 0.38 | 40.91 | -0.38 | 42.05 | 61.16 | True | 近60日漲幅>40% | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -6.05 | -3.45 | -12.75 |  | fail_already_priced_in |
| 3052 | 夆典 | 建材營造 | neutral |  | 145.4349942521465 | 12.893819518972387 | 0.95 | 2.4 | 0.95 | 0.0 | 4.93 | 4.93 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | 0.28 | 0.27 | -6.58 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 214.57877921641165 | 342.02003108951027 | 4.18 | -3.54 | 18.27 | -15.49 | 21.91 | 27.33 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | -0.39 | 0.26 | -7.73 |  | fail_low_response_condition |
| 3060 | 銘異 | 電腦及週邊設備業 | mainstream_growth |  | 77.30413360834295 | 27.56110296294079 | -3.36 | -8.01 | -6.85 | -7.84 | 1.97 | 3.61 | False |  | mild_accumulation | -0.08 | 0.7 | 2 | 1 | -6.48 | -4.77 | -16.07 |  | fail_low_response_condition |
| 3094 | 聯傑 | 半導體業 | mainstream_growth |  | 88.78116343490305 | 24.213905654929675 | -2.11 | -17.21 | 45.09 | 66.67 | 46.97 | 80.21 | True | 近60日漲幅>40%；距120日低點反彈>80% | strong_accumulation | 9.38 | 8.82 | 3 | 2 | -15.77 | -8.48 | -30.61 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 132.5343403041849 | 228.6135135135135 | -3.15 | -12.34 | -13.44 | -34.36 | 1.84 | 3.36 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -6.97 | -7.26 | -26.72 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 172.33254972044645 | 140.1978427713856 | -1.3 | 2.82 | 70.79 | 21.12 | 55.37 | 109.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -7.71 | -4.11 | -16.33 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 90.47990444398276 | 46.685682375869504 | -2.31 | -2.21 | -20.09 | -29.27 | 0.57 | 0.57 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | -3.85 | -3.69 | -26.33 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 87.1863428539576 | 97.24836000846553 | -4.47 | -1.63 | -2.42 | 29.18 | 5.22 | 37.5 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -3.04 | -2.7 | -11.89 | 21 | selected |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 446.4684953621241 | 68.26830170354926 | -7.84 | -1.22 | 27.32 | 26.92 | 29.55 | 32.52 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -14.08 | -7.74 | -31.73 | 21 | selected |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 95.90539119217506 | 34.23834809782526 | -6.2 | 2.46 | -4.03 | -0.3 | 5.38 | 6.73 | False |  | mild_accumulation | 0.17 | -0.05 | 2 | 1 | -4.91 | -4.01 | -16.75 |  | fail_low_response_condition |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 103.43107101360125 | 126.26534387085925 | 17.69 | 10.14 | 9.76 | -18.3 | 30.4 | 30.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 11.97 | 11.18 | -1.81 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 97.77847715325761 | 102.83428395752624 | -3.96 | -9.39 | 74.07 | 36.68 | 78.34 | 129.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | -8.08 | -4.63 | -16.74 |  | fail_already_priced_in |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 99.78446338976643 | 36.46696724530479 | -2.12 | -20.65 | 1.47 | -5.9 | 5.87 | 25.76 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -12.51 | -11.26 | -36.45 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 71.39293333177902 | 252.79681111256323 | -8.58 | -9.67 | 3.87 | -33.52 | 4.79 | 20.96 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -9.62 | -7.88 | -24.8 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 79.96854552825599 | 47.12157912350618 | 4.12 | -7.06 | 67.64 | 79.04 | 70.35 | 125.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -5.48 | -1.56 | -15.05 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 495.99846620911757 | 44.59053152341543 | -2.86 | -9.22 | 4.46 | -28.97 | 6.09 | 29.09 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | -11.1 | -8.78 | -25.06 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth | A_優先追蹤 | 146.48689155577668 | 72.46425018776883 | -7.86 | -7.46 | -9.05 | -4.52 | 8.54 | 8.54 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -8.72 | -6.97 | -19.16 | 21 | selected |
| 3703 | 欣陸 | 建材營造 | neutral |  | 89.3174912383306 | 3.4475931972039313 | 1.2 | 7.14 | 2.44 | 3.45 | 9.66 | 9.66 | False |  | distribution_warning | -0.07 | -0.24 | 2 | 2 | 3.64 | 2.91 | -3.45 |  | fail_low_response_condition |
| 3706 | 神達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 88.6477682411653 | 57.38834553320375 | -4.35 | -2.9 | -13.97 | -6.21 | 2.39 | 2.39 | False |  | distribution_warning | -0.88 | -0.93 | 1 | 0 | -4.67 | -4.62 | -19.62 | 15 | selected |
| 3708 | 上緯投控 | 綠能環保 | neutral |  | 165.79440372884912 | 35.87837963467142 | 5.98 | 2.12 | 10.38 | -14.41 | 11.6 | 17.99 | False |  | distribution_warning | -0.23 | -1.4 | 1 | 2 | 4.1 | 3.1 | -4.72 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 84.69522628124143 | 51.25937713911443 | -8.55 | -2.77 | 17.7 | -30.31 | 23.37 | 37.43 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | -6.94 | -4.88 | -15.17 | 21 | selected |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 90.13513513513513 | 31.81289526994584 | -3.09 | -5.48 | 2.68 | -3.09 | 3.92 | 5.18 | False |  | strong_accumulation | 0.47 | 0.22 | 2 | 3 | -4.3 | -3.17 | -11.54 |  | fail_low_response_condition |
| 4526 | 東台 | 電機機械 | cyclical_turnaround |  | 81.03484942822955 | 11.010961782504076 | 35.2 | 63.0 | 97.51 | 55.03 | 99.64 | 120.68 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.47 | 0.2 | 2 | 2 | 42.77 | 36.87 | -9.02 |  | fail_low_response_condition |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 74.69789847753101 | 58.1164628294914 | 0.98 | -12.92 | 4.31 | -17.3 | 7.87 | 26.85 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | -6.7 | -6.15 | -20.35 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 59.95235064320792 | 98.25227077937534 | -6.11 | -14.82 | -4.92 | -25.45 | 2.87 | 9.61 | False |  | strong_accumulation | 0.15 | 0.25 | 2 | 2 | -9.97 | -7.85 | -18.51 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 70.3115141167771 | 63.02464404154338 | 2.91 | -1.44 | 7.89 | 57.21 | 11.05 | 56.01 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 0.38 | 0.83 | -9.69 | 21 | selected |
| 4938 | 和碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 86.87811970952995 | 13.790026773850077 | -0.97 | 14.14 | 18.36 | 25.31 | 21.02 | 35.22 | False |  | distribution_warning | -0.08 | -0.07 | 1 | 1 | 3.69 | 3.14 | -10.09 | 13 | selected |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 93.2880896492796 | 57.86977179214104 | -5.31 | 0.52 | 25.53 | -13.82 | 26.36 | 42.04 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -4.66 | -2.81 | -12.74 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 109.68927823663151 | 90.15073758650963 | 9.4 | -0.55 | 13.96 | -4.2 | 10.28 | 39.9 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | 2.99 | 2.18 | -6.17 |  | fail_low_response_condition |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth |  | 125.76660822131308 | 27.66392696281368 | 10.91 | 8.28 | 50.62 | -24.85 | 46.4 | 74.29 | True | 近60日漲幅>40% | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 3.07 | 3.79 | -7.58 |  | fail_low_response_condition |
| 4989 | 榮科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.623935956655565 | 70.86506389755786 | -13.38 | 0.82 | 0.65 | -33.51 | 5.49 | 22.75 | False |  | strong_accumulation | 0.66 | 0.04 | 3 | 2 | -8.58 | -6.19 | -18.97 | 17 | selected |
| 5288 | 豐祥-KY | 電機機械 | cyclical_turnaround |  | 60.156228400562306 | 37.709946899313486 | -4.16 | -5.72 | -8.71 | 9.49 | 0.0 | 19.31 | False |  | distribution_warning | -0.15 | -0.73 | 0 | 0 | -5.7 | -5.31 | -13.5 |  | fail_low_response_condition |
| 5522 | 遠雄 | 建材營造 | neutral |  | 262.471963434005 | 110.54580308622074 | -2.42 | -0.66 | -6.91 | -13.92 | 1.34 | 1.34 | False |  | mild_accumulation | -0.13 | 0.02 | 2 | 2 | -1.67 | -2.03 | -7.34 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 906.4982187623697 | 1394.3019910297419 | 1.17 | -1.59 | -6.07 | -5.87 | 1.88 | 5.87 | False |  | mild_accumulation | 0.02 | -0.02 | 2 | 0 | -0.53 | -0.56 | -7.08 |  | fail_low_response_condition |
| 6141 | 柏承 | 電子零組件業 | mainstream_growth |  | 74.23882672403616 | 36.85944974599527 | -8.04 | -9.46 | 54.28 | 64.27 | 55.56 | 102.59 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.68 | -0.93 | 0 | 2 | -10.61 | -9.24 | -26.95 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 76.79527413697619 | 57.94089889392686 | 0.55 | 19.61 | 53.78 | 18.06 | 58.44 | 66.36 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.03 | 1.99 | 2 | 2 | -0.05 | 3.13 | -13.88 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 50.50424657170375 | 42.64176748510076 | -0.48 | -22.56 | -16.94 | -7.62 | 1.98 | 1.98 | False |  | mild_accumulation | 0.2 | 0.36 | 1 | 2 | -10.49 | -8.79 | -30.64 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 249.504576436222 | 315.5434384267611 | -1.1 | -3.66 | -5.49 | -3.87 | 0.56 | 7.7 | False |  | mild_accumulation | -0.23 | 0.19 | 1 | 1 | -1.97 | -2.3 | -11.21 |  | fail_low_response_condition |
| 6196 | 帆宣 | 其他電子業 | mainstream_growth |  | 88.49473702740245 | 55.51042227955082 | -10.72 | -8.89 | 7.89 | 27.06 | 15.24 | 35.8 | False |  | mild_accumulation | 0.65 | -0.85 | 2 | 2 | -13.31 | -8.97 | -22.08 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth | A_優先追蹤 | 81.57256696034645 | 71.39362622544883 | -13.94 | 4.28 | 22.06 | 37.2 | 29.88 | 50.26 | False |  | mild_accumulation | 0.36 | -0.69 | 1 | 1 | -8.91 | -7.12 | -29.0 | 17 | selected |
| 6213 | 聯茂 | 電子零組件業 | mainstream_growth |  | 110.7353905337519 | 50.07486064712765 | -15.57 | 5.3 | 126.99 | 139.85 | 126.99 | 185.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.46 | -0.78 | 2 | 2 | -13.85 | -8.38 | -25.88 |  | fail_low_response_condition |
| 6214 | 精誠 | 資訊服務業 | mainstream_growth | A_優先追蹤 | 55.69095387442037 | 42.29598437707936 | 0.5 | 7.45 | 36.03 | 65.57 | 44.29 | 66.94 | False |  | strong_accumulation | 3.24 | 3.17 | 3 | 2 | 3.21 | 3.19 | -0.98 | 19 | selected |
| 6285 | 啟碁 | 通信網路業 | mainstream_growth | A_優先追蹤 | 64.04751148579548 | 40.914406890913945 | -4.57 | -6.99 | -8.16 | -18.85 | 6.04 | 10.03 | False |  | mild_accumulation | 0.25 | 0.68 | 2 | 1 | -9.43 | -7.28 | -18.7 | 16 | selected |
| 6405 | 悅城 | 光電業 | mainstream_growth |  | 176.36363636363637 | -41.03299856527977 | -5.81 | -23.95 | 5.54 | -36.61 | 6.87 | 20.38 | False |  | distribution_warning | -2.09 | -0.91 | 0 | 0 | -5.31 | -4.72 | -23.95 |  | fail_low_response_condition |