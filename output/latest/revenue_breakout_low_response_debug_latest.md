# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-11 19:38:57 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1963 |
| standardized_revenue_rows | 1963 |
| price_rows | 788466 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 391 |
| price_metrics_pass | 389 |
| low_response_pass | 85 |
| already_priced_in_excluded | 19 |
| overheat_pass | 66 |
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
| fail_revenue_condition | 1572 |
| fail_low_response_condition | 304 |
| fail_already_priced_in | 19 |
| fail_non_mainstream_score_lt_11 | 3 |
| fail_defensive_or_traditional_excluded | 3 |
| missing_or_insufficient_price_metrics | 2 |
| fail_score_lt_8 | 1 |
| fail_mainstream_score_lt_10 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 64.59509485803973 | 30.5104354576266 | 13.2 | 3.3 | 65.61 | 261.01 | 79.89 | 262.27 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | 5.44 | 10.31 | -10.7 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral |  | 57.767666472529605 | 107.76286474027243 | -7.82 | -12.06 | -10.34 | -11.63 | 3.49 | 3.49 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -8.94 | -8.12 | -26.48 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 181.42576847612818 | 62.34390277971784 | -2.03 | -6.03 | -7.12 | -11.38 | 7.33 | 7.33 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -2.89 | -2.8 | -12.34 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 53.879220578105055 | 37.498354687053826 | -1.26 | -7.19 | -8.54 | 0.0 | 4.67 | 4.67 | False |  | distribution_warning | -0.63 | -0.33 | 2 | 0 | -3.11 | -2.89 | -10.29 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 1155.988737275287 | 130.16595685006638 | -1.55 | 2.51 | -1.04 | 11.31 | 3.63 | 22.53 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | -1.13 | -0.96 | -6.39 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 856.4496783338785 | -39.30994709260049 | 2.37 | -3.72 | -7.5 | -17.52 | 5.71 | 5.71 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -1.37 | -0.85 | -8.48 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 124.76319164843305 | 64.01741613513904 | -1.79 | -14.06 | -13.04 | -13.04 | 9.45 | 9.45 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -6.7 | -5.7 | -17.6 |  | fail_low_response_condition |
| 1506 | 正道 | 電機機械 | cyclical_turnaround |  | 53.737533894020864 | 21.55768900021609 | -1.59 | -3.63 | -11.62 | -15.25 | 4.04 | 4.04 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | -1.5 | -1.42 | -10.77 |  | fail_low_response_condition |
| 1608 | 華榮 | 電器電纜 | neutral | D_降級_TDCC轉弱 | 62.711222688855365 | 23.068823783594734 | -2.21 | -16.55 | -18.31 | -6.91 | 9.93 | 16.1 | False |  | distribution_warning | -0.28 | -0.06 | 1 | 1 | -8.45 | -7.21 | -20.72 | 7 | fail_score_lt_8 |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 78.22384391674278 | 25.3647155945427 | 3.51 | -14.51 | 78.93 | 172.28 | 77.98 | 174.52 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.86 | 1 | 1 | -2.58 | 1.98 | -24.43 |  | fail_already_priced_in |
| 1710 | 東聯 | 化學工業 | cyclical_turnaround | B_可觀察 | 88.62963468018916 | 12.793107452165357 | 1.19 | -6.09 | 11.15 | 30.89 | 16.9 | 35.6 | False |  | strong_accumulation | 0.6 | 0.55 | 2 | 2 | -0.8 | 1.52 | -15.25 | 15 | selected |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround | B_可觀察 | 69.9705645533864 | 31.944739742565208 | -1.52 | -18.74 | 6.05 | -17.55 | 18.28 | 36.3 | False |  | strong_accumulation | 3.41 | 6.37 | 2 | 2 | -7.42 | -7.23 | -35.31 | 15 | selected |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 598.516057585825 | 38.86287653881451 | 5.14 | -6.56 | -7.62 | -13.7 | 11.97 | 11.97 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -0.86 | -0.02 | -10.15 |  | fail_low_response_condition |
| 1802 | 台玻 | 玻璃陶瓷 | cyclical_turnaround |  | 56.48543728626003 | 22.616700054087328 | 14.99 | 20.79 | 33.16 | 8.79 | 41.77 | 82.4 | True | 距120日低點反彈>80% | mild_accumulation | -0.03 | 0.05 | 2 | 2 | 17.35 | 18.42 | 0.0 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 41625.77535624476 | 15374.082949656578 | -6.49 | -10.79 | -5.34 | 8.2 | 0.65 | 10.52 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | -9.38 | -7.29 | -17.99 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 129.55096222380612 | 138.17831679575767 | -6.47 | -18.73 | -14.23 | -12.5 | 5.34 | 5.34 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -13.56 | -11.32 | -27.67 |  | fail_low_response_condition |
| 2034 | 允強 | 鋼鐵工業 | cyclical_turnaround |  | 99.84279561575912 | 11.448430856809212 | 8.65 | 4.03 | 21.29 | 23.74 | 25.0 | 36.49 | False |  | strong_accumulation | 0.89 | 1.3 | 3 | 3 | 4.79 | 5.99 | -2.0 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 191.0633435081773 | 170.4137539237435 | 1.51 | -17.49 | -27.52 | 71.51 | 21.25 | 89.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -6.74 | -8.9 | -42.13 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 481.8567713692403 | 190.67882142816143 | 0.54 | -9.03 | -19.24 | -9.77 | 5.93 | 5.93 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | -4.04 | -3.58 | -20.4 | 15 | selected |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 57.68901943927019 | 33.061727972521304 | -2.01 | 13.19 | -28.69 | -36.72 | 20.7 | 20.7 | False |  | distribution_warning | -1.12 | -0.1 | 1 | 2 | 1.73 | -2.39 | -29.77 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 263.8520349677535 | 56.78006708193579 | -1.43 | -19.16 | 17.32 | 110.96 | 23.18 | 117.16 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -7.89 | -4.9 | -22.42 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 1346.1385633785483 | 77.13169968570347 | -3.1 | -6.8 | -12.05 | -7.57 | 4.27 | 4.27 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -5.64 | -5.21 | -13.41 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth | A_優先追蹤 | 52.37377746088548 | 39.70456693802114 | -0.74 | -18.76 | -12.07 | 42.53 | 20.09 | 51.99 | False |  | strong_accumulation | 2.08 | 1.69 | 2 | 2 | -4.94 | -4.14 | -21.32 | 15 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 165.33752633346563 | 129.50597675323428 | -12.91 | -40.23 | 52.88 | 126.06 | 65.37 | 138.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -17.84 | -15.06 | -43.11 |  | fail_low_response_condition |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 55.00975999915437 | 38.25598095571042 | -5.46 | -33.25 | -29.49 | -32.51 | 16.46 | 16.46 | False |  | strong_accumulation | 1.16 | 1.13 | 2 | 2 | -15.24 | -13.69 | -38.12 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 59.709757600700904 | 43.29045540365918 | 5.97 | -5.71 | -0.83 | 6.21 | 18.56 | 18.56 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | 1.36 | 1.58 | -7.53 | 11 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 217.1919858274479 | 161.49292298628288 | -5.16 | -28.4 | -39.41 | -44.68 | 15.18 | 15.18 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -13.39 | -13.82 | -42.77 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.9590857564141 | 195.44947989897403 | -3.53 | -21.55 | -22.88 | 9.2 | 18.7 | 18.7 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -10.09 | -9.96 | -28.91 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth | A_優先追蹤 | 91.15506140307477 | 65.80885180817718 | 6.42 | -26.06 | -28.89 | -36.23 | 26.51 | 26.51 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -8.18 | -6.3 | -33.96 | 16 | selected |
| 2347 | 聯強 | 電子通路業 | mainstream_growth |  | 59.51432168340272 | 93.4995691798238 | -12.4 | -20.02 | -13.65 | -5.95 | 3.13 | 3.13 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -16.76 | -13.62 | -23.94 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 80.94065846345056 | 39.55623508502928 | -4.27 | -26.12 | -8.72 | -15.82 | 18.94 | 26.61 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -13.68 | -12.36 | -38.91 |  | fail_low_response_condition |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.248039849071496 | 41.131638760290016 | 2.85 | -7.68 | 5.87 | 32.26 | 14.18 | 42.05 | False |  | distribution_warning | -0.64 | -0.62 | 0 | 1 | -3.35 | -2.19 | -12.43 | 11 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 163.2560218675471 | 124.23311647079436 | -6.8 | -42.07 | -37.59 | -39.65 | 15.13 | 15.13 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -22.51 | -20.61 | -46.48 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 76.37330730453692 | 76.325234320535 | -0.42 | -17.04 | -13.9 | -28.49 | 20.3 | 20.3 | False |  | strong_accumulation | 1.11 | 0.56 | 3 | 2 | -6.31 | -5.68 | -24.88 | 15 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.17971022116946 | 69.88407899868652 | 8.92 | -14.98 | 5.0 | -21.05 | 34.27 | 48.94 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -2.83 | 0.29 | -19.85 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 136.72416140195128 | 70.72100883311214 | -6.01 | -14.33 | -18.77 | -5.43 | 8.16 | 8.16 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -9.64 | -8.71 | -24.13 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 103.9601585472691 | 99.88620940840123 | -1.49 | -7.45 | -8.45 | -5.7 | 9.56 | 9.56 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -5.08 | -4.92 | -15.22 | 14 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 203.07515404377685 | 114.05965443168765 | -1.21 | -26.83 | -21.47 | -10.09 | 21.95 | 21.95 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -5.71 | -4.9 | -30.45 | 20 | selected |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 88.41712908981661 | 53.088745989386965 | -2.7 | -15.12 | -10.79 | 30.49 | 13.97 | 36.3 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -6.56 | -5.47 | -18.83 | 17 | selected |
| 2399 | 映泰 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 150.9505086438245 | 17.64304361923672 | 6.44 | -11.81 | -4.77 | -7.73 | 25.58 | 43.17 | False |  | strong_accumulation | 3.62 | 0.69 | 2 | 3 | 0.5 | 0.26 | -17.24 | 19 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 55.99925704609442 | 61.535849801128656 | -0.1 | -19.51 | -12.42 | -13.94 | 15.45 | 15.45 | False |  | strong_accumulation | 2.74 | 3.1 | 3 | 3 | -5.46 | -5.53 | -26.64 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 51.38776767063092 | 100.55791451054965 | 2.45 | -2.5 | -7.42 | -7.72 | 13.35 | 13.35 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | 0.4 | 0.1 | -10.26 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 487.72943534104417 | 602.154485146844 | -1.38 | -25.24 | -18.34 | 26.89 | 21.6 | 36.81 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -7.63 | -8.27 | -30.76 | 12 | selected |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 52.59912440445534 | 46.21659350926994 | -1.34 | -8.05 | -9.09 | -4.38 | 6.67 | 6.67 | False |  | strong_accumulation | 0.12 | 0.1 | 3 | 3 | -4.4 | -4.13 | -11.44 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth |  | 61.442637721350245 | 22.76545439044366 | -2.55 | -9.64 | -0.4 | -21.36 | 12.44 | 12.95 | False |  | strong_accumulation | 0.28 | 0.42 | 2 | 2 | -5.6 | -4.81 | -18.92 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 423.8346822457185 | 152.7650841754859 | -0.65 | -14.29 | -26.97 | -11.82 | 18.38 | 18.38 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -3.92 | -4.04 | -28.0 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 104.48808464352813 | 70.02572263494662 | 0.18 | -2.78 | -1.93 | 6.48 | 5.08 | 8.54 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.51 | 0.04 | -6.52 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 59.7408763811429 | 33.33503048242509 | 1.81 | -1.4 | -9.9 | -21.67 | 13.71 | 13.71 | False |  | mild_accumulation | 0.05 | 0.04 | 1 | 1 | -1.84 | -0.75 | -7.84 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 6975.206313416009 | 531.5739549159281 | 3.24 | -8.27 | -34.95 | -31.08 | 13.33 | 13.33 | False |  | distribution_warning | -0.12 | -0.22 | 1 | 1 | -1.75 | -2.46 | -36.41 | 13 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 191.62415264540607 | 344.4727836796557 | -10.65 | -17.98 | -20.2 | -25.75 | 2.4 | 8.8 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -12.5 | -11.72 | -28.68 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 95.20056675819117 | 71.4699607489928 | 0.54 | -12.97 | -9.58 | -14.44 | 11.4 | 11.4 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -5.96 | -4.0 | -17.24 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 95.9988149893207 | 42.68355260588374 | 2.19 | -14.88 | -17.05 | 13.19 | 24.9 | 38.14 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -1.98 | -2.04 | -27.23 | 12 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 340.57609557459455 | 125.19243597077654 | 19.6 | 78.19 | 56.54 | 74.04 | 81.87 | 121.81 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.98 | 0.34 | 1 | 1 | 42.47 | 36.38 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 80.67875061959084 | 83.80094521811333 | -14.11 | -45.34 | -41.58 | -46.52 | 13.96 | 13.96 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -25.13 | -23.62 | -49.84 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth |  | 60.61793461300194 | 29.30528362005905 | -0.28 | -27.72 | -29.6 | -32.31 | 21.8 | 21.8 | False |  | distribution_warning | -0.79 | -2.74 | 2 | 0 | -10.94 | -9.01 | -34.21 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 62.519073558552414 | 43.69792273832236 | -2.65 | -22.72 | -22.42 | -17.93 | 16.0 | 16.0 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -10.43 | -8.94 | -26.17 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 69.84202715674517 | 25.070841829961658 | 5.23 | 2.55 | 17.53 | 21.07 | 17.92 | 25.26 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 0.22 | 3.51 | -8.12 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 67.86469051765079 | 36.482902038810515 | -0.28 | -24.63 | -23.48 | -35.06 | 22.65 | 22.65 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -8.75 | -8.87 | -42.76 |  | fail_low_response_condition |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 68.0349249896575 | 30.961077135272443 | -0.5 | -1.89 | -2.08 | -9.28 | 5.0 | 5.0 | False |  | mild_accumulation | -0.06 | 0.05 | 1 | 2 | -0.59 | 0.02 | -3.24 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 57.111134230197685 | 28.67364384164082 | -7.69 | -31.1 | 0.0 | -1.54 | 14.74 | 45.09 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -18.74 | -13.95 | -33.26 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 110081.106870229 | 145.48970757927498 | 1.76 | -0.29 | -4.41 | -4.14 | 6.44 | 6.44 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -1.25 | -0.16 | -5.71 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 421.495501003469 | 48.86875327214938 | -0.6 | -2.14 | -4.42 | -5.19 | 1.61 | 1.61 | False |  | mild_accumulation | -0.44 | 0.53 | 0 | 2 | -1.56 | -1.43 | -5.95 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral |  | 78.24940336075872 | 31.742780171246356 | -1.38 | -4.13 | -4.83 | 1.94 | 1.15 | 4.09 | False |  | mild_accumulation | 0.07 | 0.0 | 2 | 2 | -2.45 | -2.56 | -8.47 |  | fail_low_response_condition |
| 2530 | 華建 | 建材營造 | neutral |  | 2703.9144493217 | -71.49138124020595 | -4.75 | -12.17 | -6.96 | -11.74 | 4.34 | 4.34 | False |  | mild_accumulation | 0.08 | -0.12 | 2 | 1 | -7.7 | -6.42 | -15.26 |  | fail_low_response_condition |
| 2535 | 達欣工 | 建材營造 | neutral |  | 64.23038581980985 | 27.535286720968383 | -0.33 | -1.21 | 1.13 | 15.87 | 6.52 | 18.94 | False |  | mild_accumulation | -0.19 | 0.13 | 0 | 3 | -0.45 | -0.31 | -4.67 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 157.62161407365198 | 10.827675767842882 | 0.17 | -10.83 | -28.71 | -21.34 | 4.7 | 4.7 | False |  | mild_accumulation | 0.47 | 0.39 | 2 | 1 | -5.59 | -5.29 | -28.71 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 360.4307813599472 | 21.214141620507657 | 0.45 | -10.31 | 0.67 | -19.71 | 5.41 | 5.54 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -2.91 | -2.52 | -17.04 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 1174.2550655542311 | 12.761197533160972 | -2.95 | -9.55 | -10.59 | -15.43 | 4.17 | 4.17 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -5.25 | -4.54 | -13.67 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 193.20885592758208 | 84.89840613579092 | 0.96 | -5.02 | -6.34 | -5.4 | 5.58 | 5.58 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -1.81 | -1.33 | -8.16 | 17 | selected |
| 2603 | 長榮 | 航運業 | cyclical_turnaround | B_可觀察 | 96.13406373417418 | 22.24689137162106 | -3.92 | 0.78 | 20.05 | 17.58 | 22.04 | 42.66 | False |  | strong_accumulation | 0.16 | 0.27 | 2 | 2 | -1.31 | 0.66 | -6.19 | 19 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 91.6858998835063 | 48.18745924840134 | -1.21 | -12.33 | 0.46 | 4.47 | 9.18 | 14.14 | False |  | distribution_warning | -0.18 | -0.54 | 2 | 2 | -5.07 | -4.07 | -16.58 | 11 | selected |
| 2607 | 榮運 | 航運業 | cyclical_turnaround |  | 75.98733589278142 | 23.469572484789072 | -1.03 | 0.87 | 14.46 | 20.67 | 16.89 | 27.59 | False |  | strong_accumulation | 0.08 | 0.3 | 2 | 3 | 0.83 | 2.01 | -3.34 |  | fail_low_response_condition |
| 2609 | 陽明 | 航運業 | cyclical_turnaround | B_可觀察 | 82.44651696845074 | 23.20381282773115 | -5.14 | -7.08 | 14.31 | 11.51 | 16.57 | 25.08 | False |  | mild_accumulation | 1.51 | 1.16 | 1 | 1 | -4.59 | -2.66 | -12.18 | 16 | selected |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 124.36480644917681 | 35.92088925621068 | -3.9 | -8.26 | 27.44 | 31.67 | 28.32 | 44.91 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -4.72 | -2.92 | -17.47 | 18 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 125.54297999754175 | 34.02484327434486 | 1.6 | -3.45 | 3.55 | 4.17 | 10.58 | 12.54 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | -0.6 | 0.17 | -11.28 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 59.47228116872314 | 39.3938941812916 | 2.82 | -0.5 | -2.43 | -1.96 | 7.22 | 7.22 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | 0.55 | 0.57 | -8.45 | 14 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 80.13292543760198 | 149.1882762948346 | -22.61 | 1.44 | -9.54 | 14.92 | 9.56 | 20.24 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | -8.86 | -9.16 | -29.17 |  | fail_low_response_condition |
| 2929 | 淘帝-KY | 貿易百貨 | defensive_or_traditional |  | 53.441498418876186 | 20.955681131352456 | 1.06 | -1.38 | -3.06 | -0.35 | 8.56 | 8.56 | False |  | mild_accumulation | 0.62 | 0.04 | 3 | 1 | 0.95 | 1.04 | -7.15 |  | fail_low_response_condition |
| 3002 | 歐格 | 電腦及週邊設備業 | mainstream_growth |  | 85.5625401962615 | 31.473709686555406 | -2.6 | -12.47 | -2.03 | -3.99 | 13.85 | 13.85 | False |  | distribution_warning | -0.07 | -0.02 | 1 | 0 | -5.77 | -4.85 | -21.08 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.466111556875724 | 44.45331513053742 | -1.92 | -15.36 | -30.42 | -21.65 | 11.24 | 11.24 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -7.77 | -7.57 | -33.74 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 51.08502105140537 | 43.33967286547871 | -3.16 | 0.82 | -2.78 | -6.13 | 7.46 | 7.46 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 0.31 | 0.45 | -5.77 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 430.0611365734368 | 353.58017683428835 | 1.51 | -9.79 | -14.23 | -1.05 | 21.76 | 45.96 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -2.96 | -4.27 | -26.33 | 15 | selected |
| 3029 | 零壹 | 資訊服務業 | mainstream_growth |  | 91.12753663059947 | 28.65475028715983 | 15.88 | 12.97 | 24.42 | 39.18 | 29.81 | 43.46 | False |  | distribution_warning | -0.38 | -0.97 | 1 | 1 | 11.36 | 11.93 | -1.46 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth | A_優先追蹤 | 71.92792324679422 | 33.04466992687986 | -0.21 | -26.11 | -24.07 | -44.34 | 18.83 | 18.83 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -9.76 | -7.85 | -27.48 | 15 | selected |
| 3036 | 文曄 | 電子通路業 | mainstream_growth | A_優先追蹤 | 112.86439423180833 | 102.78865814569586 | -5.13 | -10.39 | -10.8 | -32.87 | 10.23 | 10.23 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -5.22 | -3.85 | -13.2 | 19 | selected |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 67.61651572185568 | 40.87531408660304 | -2.7 | -31.16 | -13.6 | -10.93 | 20.0 | 32.31 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -12.91 | -10.99 | -39.15 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 70.32634159542289 | 43.660674974825135 | 7.44 | -10.19 | 7.11 | 6.01 | 31.65 | 59.02 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | -1.24 | 1.96 | -13.91 | 17 | selected |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 58.677185968760504 | 27.483848231923762 | 3.07 | -3.45 | -19.26 | -5.81 | 10.79 | 10.79 | False |  | distribution_warning | -1.01 | 0.0 | 1 | 0 | -0.54 | -0.95 | -20.16 |  | fail_low_response_condition |
| 3052 | 夆典 | 建材營造 | neutral |  | 98.45561279438057 | 18.586711689848357 | 0.48 | -1.87 | -3.23 | -0.47 | 3.96 | 3.96 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -0.92 | -0.32 | -7.89 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 516.8037075796083 | 352.8122144169259 | 3.51 | 3.33 | 21.82 | -12.87 | 22.71 | 30.89 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | 4.05 | 3.53 | -5.15 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth | A_優先追蹤 | 191.80768622489325 | 3.8670389284699467 | 5.36 | -31.59 | 17.52 | 16.53 | 28.5 | 75.61 | False |  | mild_accumulation | 1.53 | -0.97 | 2 | 0 | -2.4 | -5.2 | -39.56 | 17 | selected |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.29689096505317 | 229.5654302580979 | -6.08 | -21.09 | -25.38 | -41.61 | 12.27 | 12.27 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -9.89 | -10.06 | -34.13 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 174.90740647903988 | 144.49531376078457 | 2.09 | -18.8 | 31.1 | 6.02 | 38.74 | 102.76 | True | 距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -3.23 | -0.05 | -19.17 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 169.43498384084424 | 62.374885498074185 | 9.68 | 2.15 | -14.23 | -38.97 | 25.26 | 25.26 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | 5.28 | 5.52 | -16.2 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 117.5572069759596 | 99.52528249578863 | -0.85 | -7.92 | -9.82 | 20.76 | 14.8 | 25.54 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -3.59 | -2.66 | -15.29 | 19 | selected |
| 3296 | 勝德 | 電子零組件業 | mainstream_growth |  | 61.238735177865614 | 21.280770602925436 | 1.32 | -20.17 | -1.71 | 16.79 | 19.84 | 20.47 | False |  | mild_accumulation | 0.3 | 0.12 | 1 | 1 | -6.13 | -5.13 | -25.85 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 53.132988411628745 | 58.859591226050156 | 2.43 | -4.52 | -9.05 | -27.74 | 23.39 | 23.39 | False |  | distribution_warning | -0.36 | -0.02 | 2 | 0 | 0.08 | 1.17 | -12.81 | 11 | selected |
| 3308 | 聯德 | 電子零組件業 | mainstream_growth |  | 572.6775956284152 | 52.505046797577535 | -2.31 | -13.24 | -2.56 | -7.32 | 2.98 | 4.11 | False |  | strong_accumulation | 0.17 | 0.17 | 2 | 2 | -7.81 | -7.0 | -20.5 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | A_優先追蹤 | 629.1409179812659 | 118.75339188355494 | 3.43 | -20.97 | 27.19 | 20.24 | 30.03 | 31.29 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -6.1 | -0.68 | -31.48 | 20 | selected |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 87.20206934778592 | 120.85975318742756 | -8.9 | -8.28 | -18.4 | -29.26 | 6.4 | 6.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -6.4 | -6.4 | -19.88 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 126.95750136110938 | 106.35531661015841 | 10.82 | -2.65 | 53.7 | 53.4 | 51.49 | 148.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | 5.78 | 7.67 | -9.89 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 74.58783464735932 | 40.187058133074316 | -1.98 | -28.32 | -26.63 | -19.04 | 20.78 | 20.78 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -9.93 | -10.64 | -43.03 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 72.80840016689073 | 222.62788185837613 | -1.18 | -19.14 | -18.7 | -41.02 | 19.37 | 19.37 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -11.61 | -8.52 | -31.95 |  | fail_low_response_condition |
| 3563 | 牧德 | 光電業 | mainstream_growth |  | 95.58715133646274 | 24.59024723903795 | -3.71 | -14.66 | -13.11 | -30.47 | 18.44 | 18.44 | False |  | mild_accumulation | 0.65 | -0.1 | 2 | 1 | -5.0 | -4.67 | -24.48 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 80.6841558493479 | 50.53909493401264 | -3.49 | -13.06 | 39.26 | 70.08 | 41.0 | 108.19 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -1.04 | 0.88 | -16.33 |  | fail_already_priced_in |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 515.8077034803464 | 72.61924772874468 | 14.78 | -16.95 | -9.99 | -25.43 | 36.96 | 38.78 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | 4.24 | 4.59 | -19.43 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 79.99209905355778 | 44.44448312639371 | 0.64 | -32.91 | -26.68 | -26.68 | 22.01 | 22.01 | False |  | mild_accumulation | 0.73 | -0.01 | 2 | 2 | -10.28 | -10.42 | -41.15 |  | fail_low_response_condition |
| 3701 | 大眾控 | 電腦及週邊設備業 | mainstream_growth |  | 93.95223113106867 | -3.906795594950309 | 12.26 | 1.77 | 52.29 | 10.88 | 65.45 | 91.52 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.83 | 1.15 | 3 | 2 | 11.01 | 15.29 | -8.93 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 79.04019204347462 | 73.12719508837236 | -7.93 | -20.95 | -25.14 | -22.29 | 10.62 | 10.62 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -14.28 | -12.07 | -26.64 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 121.47129190100547 | 58.89467218155531 | 13.48 | -6.12 | 10.59 | -25.21 | 40.02 | 45.81 | False |  | strong_accumulation | 0.51 | 0.17 | 2 | 2 | 4.77 | 6.9 | -10.0 |  | fail_low_response_condition |
| 4545 | 銘鈺 | 電子零組件業 | mainstream_growth |  | 103.77090658167121 | 10.600762729063572 | 12.19 | 0.79 | 15.41 | 15.06 | 28.62 | 28.62 | False |  | distribution_warning | -0.29 | -0.25 | 0 | 0 | 6.11 | 7.16 | -9.05 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround | B_可觀察 | 61.70032883785875 | 27.24080387252237 | -5.22 | -1.17 | 5.25 | 20.57 | 21.73 | 29.15 | False |  | mild_accumulation | 3.36 | 2.38 | 2 | 1 | -5.57 | -2.67 | -15.89 | 14 | selected |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 369.96502869440457 | 38.23538108392017 | -1.27 | -4.39 | 3.02 | -3.02 | 9.22 | 12.37 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | -2.0 | -1.44 | -6.03 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 124.78894381077127 | 49.032732768125726 | 5.72 | -5.56 | 0.8 | 36.82 | 18.05 | 37.42 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | 2.76 | 3.82 | -13.5 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 112.42760478951273 | 68.75398284152372 | 5.94 | 0.49 | 0.49 | 5.29 | 28.89 | 28.89 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 4.78 | 5.21 | -8.81 | 21 | selected |
| 4927 | 泰鼎-KY | 電子零組件業 | mainstream_growth |  | 87.0002088072709 | 16.83446331292745 | 18.29 | 2.76 | 72.46 | 5.68 | 87.11 | 125.81 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.07 | 0.95 | 3 | 3 | 11.37 | 15.65 | -1.65 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 251.47616691406895 | 146.12933323763727 | -0.76 | -22.85 | -8.77 | -25.29 | 16.07 | 16.07 | False |  | distribution_warning | -0.14 | -0.25 | 1 | 0 | -9.8 | -7.02 | -28.37 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.40745433475969 | 59.03652713624137 | -9.39 | -21.92 | -4.86 | -32.18 | 6.05 | 23.33 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -12.99 | -11.27 | -24.23 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth | A_優先追蹤 | 159.3995435550978 | 95.1773725066357 | -1.69 | -2.97 | -6.44 | -3.33 | 9.64 | 33.76 | False |  | mild_accumulation | -1.03 | 3.42 | 1 | 3 | -0.74 | -1.57 | -10.29 | 24 | selected |
| 4977 | 眾達-KY | 通信網路業 | mainstream_growth | A_優先追蹤 | 117.36150511767242 | 36.33309790571782 | 1.36 | 1.09 | 20.78 | -15.26 | 30.99 | 77.14 | False |  | mild_accumulation | 1.97 | 1.86 | 2 | 1 | 4.29 | 4.96 | -6.06 | 20 | selected |