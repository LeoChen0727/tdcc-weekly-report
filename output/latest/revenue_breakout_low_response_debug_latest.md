# 營收爆發低反應股 Debug Report

- 產生時間：`2026-11-12 19:37:08 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1963 |
| standardized_revenue_rows | 1963 |
| price_rows | 790431 |
| tdcc_rows | 1965 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 356 |
| tdcc_mild_accumulation_count | 777 |
| tdcc_distribution_warning_count | 647 |
| revenue_condition_pass | 391 |
| price_metrics_pass | 389 |
| low_response_pass | 50 |
| already_priced_in_excluded | 7 |
| overheat_pass | 43 |
| score_pass | 43 |
| theme_priority_pass | 41 |
| final_rows | 41 |

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
| fail_low_response_condition | 339 |
| fail_already_priced_in | 7 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |
| fail_defensive_or_traditional_excluded | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | 塑膠工業 | cyclical_turnaround |  | 64.59509485803973 | 30.5104354576266 | 17.67 | -8.15 | 55.03 | 237.95 | 68.39 | 239.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.21 | -0.23 | 1 | 1 | -0.86 | 2.98 | -16.41 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 57.767666472529605 | 107.76286474027243 | -4.53 | -11.2 | -7.2 | -10.77 | 4.5 | 4.5 | False |  | mild_accumulation | -0.43 | 0.45 | 1 | 2 | -7.51 | -6.66 | -25.76 | 13 | selected |
| 1326 | 台化 | 塑膠工業 | cyclical_turnaround |  | 61.79229277055931 | 22.844253687340956 | 9.54 | -8.48 | 19.66 | 56.31 | 26.92 | 61.09 | False |  | distribution_warning | -0.35 | -0.39 | 0 | 1 | -2.5 | -0.29 | -17.31 |  | fail_low_response_condition |
| 1340 | 勝悅-KY | 塑膠工業 | cyclical_turnaround |  | 181.42576847612818 | 62.34390277971784 | -1.04 | -6.3 | -8.29 | -12.66 | 5.78 | 5.78 | False |  | mild_accumulation | 0.55 | 0.0 | 2 | 0 | -3.98 | -3.87 | -13.61 |  | fail_low_response_condition |
| 1342 | 八貫 | 其他 | neutral |  | 53.879220578105055 | 37.498354687053826 | -0.53 | -6.57 | -9.71 | -0.32 | 4.33 | 4.33 | False |  | distribution_warning | -0.63 | -0.33 | 2 | 0 | -3.09 | -2.94 | -10.57 |  | fail_low_response_condition |
| 1439 | 雋揚 | 建材營造 | neutral |  | 1155.988737275287 | 130.16595685006638 | -3.47 | -1.94 | -3.47 | 7.53 | 1.09 | 19.53 | False |  | strong_accumulation | 0.18 | 0.18 | 3 | 3 | -3.46 | -3.12 | -8.69 |  | fail_low_response_condition |
| 1446 | 宏和 | 紡織纖維 | defensive_or_traditional |  | 856.4496783338785 | -39.30994709260049 | 1.57 | -4.09 | -7.86 | -17.83 | 5.31 | 5.31 | False |  | strong_accumulation | 0.2 | 0.1 | 3 | 3 | -1.55 | -1.14 | -8.83 |  | fail_low_response_condition |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 124.76319164843305 | 64.01741613513904 | 0.91 | -12.99 | -11.6 | -12.65 | 9.95 | 9.95 | False |  | mild_accumulation | 1.38 | -0.17 | 3 | 2 | -5.62 | -4.85 | -17.23 |  | fail_low_response_condition |
| 1506 | 正道 | 電機機械 | cyclical_turnaround |  | 53.737533894020864 | 21.55768900021609 | -0.32 | -3.64 | -10.1 | -15.43 | 3.81 | 3.81 | False |  | distribution_warning | -0.13 | 0.0 | 1 | 0 | -1.53 | -1.5 | -10.96 |  | fail_low_response_condition |
| 1608 | 華榮 | 電器電纜 | neutral |  | 62.711222688855365 | 23.068823783594734 | -2.9 | -17.4 | -18.07 | -9.46 | 6.91 | 12.92 | False |  | distribution_warning | -0.28 | -0.06 | 1 | 1 | -10.12 | -9.02 | -22.89 |  | fail_low_response_condition |
| 1709 | 和益 | 化學工業 | cyclical_turnaround |  | 78.22384391674278 | 25.3647155945427 | 13.76 | -13.02 | 69.98 | 183.15 | 76.61 | 185.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.67 | -0.86 | 1 | 1 | 2.08 | 5.52 | -21.42 |  | fail_low_response_condition |
| 1710 | 東聯 | 化學工業 | cyclical_turnaround | B_可觀察 | 88.62963468018916 | 12.793107452165357 | 4.73 | -14.87 | 12.16 | 28.19 | 14.48 | 32.8 | False |  | strong_accumulation | 0.6 | 0.55 | 2 | 2 | -2.02 | -0.53 | -17.0 | 15 | selected |
| 1727 | 中華化 | 化學工業 | cyclical_turnaround |  | 69.9705645533864 | 31.944739742565208 | 1.9 | -19.5 | 5.37 | -21.08 | 13.22 | 30.47 | False |  | strong_accumulation | 3.41 | 6.37 | 2 | 2 | -10.42 | -10.37 | -38.08 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 598.516057585825 | 38.86287653881451 | 0.98 | -11.17 | -11.68 | -18.31 | 5.98 | 5.98 | False |  | distribution_warning | -0.15 | 0.0 | 2 | 0 | -5.6 | -4.94 | -14.95 |  | fail_low_response_condition |
| 1802 | 台玻 | 玻璃陶瓷 | cyclical_turnaround |  | 56.48543728626003 | 22.616700054087328 | 35.94 | 32.2 | 43.59 | 15.89 | 51.02 | 94.29 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.03 | 0.05 | 2 | 2 | 23.13 | 23.45 | -3.08 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 41625.77535624476 | 15374.082949656578 | -6.49 | -10.79 | -5.34 | 8.2 | 0.65 | 10.52 | False |  | distribution_warning | -0.16 | -0.51 | 1 | 0 | -9.38 | -7.29 | -17.99 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 129.55096222380612 | 138.17831679575767 | -4.98 | -21.05 | -17.32 | -15.32 | 1.94 | 1.94 | False |  | mild_accumulation | 0.04 | -0.32 | 2 | 1 | -15.41 | -13.15 | -30.0 |  | fail_low_response_condition |
| 2034 | 允強 | 鋼鐵工業 | cyclical_turnaround |  | 99.84279561575912 | 11.448430856809212 | 9.77 | 1.9 | 20.45 | 21.97 | 23.21 | 34.54 | False |  | strong_accumulation | 0.89 | 1.3 | 3 | 3 | 3.19 | 4.09 | -4.17 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 191.0633435081773 | 170.4137539237435 | 2.13 | -18.84 | -33.27 | 60.41 | 13.4 | 77.31 | False |  | mild_accumulation | -0.08 | 0.26 | 2 | 2 | -11.88 | -13.73 | -45.87 |  | fail_low_response_condition |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | D_降級_TDCC轉弱 | 481.8567713692403 | 190.67882142816143 | 5.22 | -1.02 | -14.6 | -4.72 | 11.85 | 11.85 | False |  | distribution_warning | -0.5 | -0.45 | 0 | 0 | 1.38 | 1.66 | -13.2 | 15 | selected |
| 2236 | 百達-KY | 汽車工業 | neutral |  | 57.68901943927019 | 33.061727972521304 | 0.55 | 13.56 | -27.48 | -37.13 | 19.92 | 19.92 | False |  | distribution_warning | -1.12 | -0.1 | 1 | 2 | 0.46 | -2.78 | -28.6 |  | fail_low_response_condition |
| 2243 | 宏旭-KY | 汽車工業 | neutral |  | 263.8520349677535 | 56.78006708193579 | -2.53 | -20.48 | 16.37 | 102.63 | 18.31 | 108.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.29 | -1.48 | 2 | 2 | -10.51 | -7.99 | -25.48 |  | fail_low_response_condition |
| 2258 | 鴻華先進-創 | 汽車工業 | neutral |  | 1346.1385633785483 | 77.13169968570347 | -3.28 | -7.27 | -12.21 | -7.73 | 4.08 | 4.08 | False |  | mild_accumulation | 0.05 | 0.02 | 1 | 2 | -5.46 | -4.96 | -13.56 |  | fail_low_response_condition |
| 2302 | 麗正 | 半導體業 | mainstream_growth | A_優先追蹤 | 52.37377746088548 | 39.70456693802114 | 4.86 | -16.27 | -14.05 | 38.26 | 16.49 | 47.44 | False |  | strong_accumulation | 2.08 | 1.69 | 2 | 2 | -6.96 | -6.47 | -23.67 | 16 | selected |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 165.33752633346563 | 129.50597675323428 | -8.53 | -39.18 | 31.59 | 113.83 | 56.42 | 125.21 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.12 | 1.22 | 1 | 2 | -20.29 | -18.32 | -46.18 |  | fail_low_response_condition |
| 2327 | 國巨* | 電子零組件業 | mainstream_growth |  | 55.00975999915437 | 38.25598095571042 | 0.62 | -32.05 | -38.52 | -35.29 | 11.66 | 11.66 | False |  | strong_accumulation | 1.16 | 1.13 | 2 | 2 | -17.14 | -16.04 | -40.67 |  | fail_low_response_condition |
| 2330 | 台積電 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 59.709757600700904 | 43.29045540365918 | 4.46 | -6.02 | -3.9 | 3.77 | 15.84 | 15.84 | False |  | distribution_warning | -0.04 | -0.05 | 1 | 1 | -0.65 | -0.69 | -9.65 | 12 | selected |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 217.1919858274479 | 161.49292298628288 | -1.63 | -26.38 | -42.56 | -47.56 | 9.19 | 9.19 | False |  | distribution_warning | -0.16 | -0.48 | 1 | 1 | -16.67 | -17.03 | -45.74 |  | fail_low_response_condition |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 256.9590857564141 | 195.44947989897403 | 0.0 | -21.05 | -27.97 | 2.0 | 10.87 | 10.87 | False |  | distribution_warning | -1.13 | -1.08 | 2 | 2 | -15.07 | -14.77 | -33.59 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 91.15506140307477 | 65.80885180817718 | 10.51 | -25.25 | -32.82 | -38.26 | 22.49 | 22.49 | False |  | mild_accumulation | -0.71 | 0.73 | 1 | 2 | -9.74 | -8.57 | -36.06 |  | fail_low_response_condition |
| 2347 | 聯強 | 電子通路業 | mainstream_growth |  | 59.51432168340272 | 93.4995691798238 | -12.16 | -23.78 | -16.28 | -8.92 | 0.0 | 0.0 | False |  | mild_accumulation | 0.21 | 0.04 | 3 | 1 | -18.37 | -15.2 | -26.35 |  | fail_low_response_condition |
| 2351 | 順德 | 半導體業 | mainstream_growth |  | 80.94065846345056 | 39.55623508502928 | 0.34 | -28.95 | -14.16 | -20.38 | 12.5 | 19.76 | False |  | mild_accumulation | -0.47 | 0.58 | 1 | 2 | -16.97 | -15.91 | -42.22 |  | fail_low_response_condition |
| 2357 | 華碩 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 62.248039849071496 | 41.131638760290016 | 2.65 | -7.87 | -5.02 | 30.5 | 12.66 | 40.16 | False |  | distribution_warning | -0.64 | -0.62 | 0 | 1 | -4.24 | -3.21 | -13.59 | 12 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 163.2560218675471 | 124.23311647079436 | 6.37 | -35.45 | -38.26 | -37.44 | 19.33 | 19.33 | False |  | distribution_warning | -0.28 | -0.63 | 1 | 1 | -17.87 | -16.48 | -44.53 |  | fail_low_response_condition |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 76.37330730453692 | 76.325234320535 | 6.81 | -14.92 | -13.51 | -29.46 | 18.66 | 18.66 | False |  | strong_accumulation | 1.11 | 0.56 | 3 | 2 | -6.83 | -6.42 | -25.91 | 17 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 76.17971022116946 | 69.88407899868652 | 12.33 | -16.67 | -3.47 | -26.69 | 24.68 | 38.3 | False |  | distribution_warning | -0.79 | -0.57 | 1 | 1 | -8.95 | -6.33 | -25.57 |  | fail_low_response_condition |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 136.72416140195128 | 70.72100883311214 | -7.51 | -18.57 | -26.43 | -10.23 | 2.66 | 2.66 | False |  | strong_accumulation | 1.47 | 1.49 | 3 | 3 | -13.38 | -12.37 | -27.99 |  | fail_low_response_condition |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth |  | 103.9601585472691 | 99.88620940840123 | -7.17 | -13.78 | -14.31 | -11.87 | 2.39 | 2.39 | False |  | distribution_warning | -0.01 | -0.07 | 1 | 1 | -10.66 | -10.31 | -20.77 |  | fail_low_response_condition |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 203.07515404377685 | 114.05965443168765 | 0.12 | -25.97 | -27.86 | -17.98 | 11.25 | 11.25 | False |  | mild_accumulation | 0.34 | -0.11 | 2 | 2 | -12.67 | -12.28 | -36.55 |  | fail_low_response_condition |
| 2395 | 研華 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 88.41712908981661 | 53.088745989386965 | 1.17 | -16.02 | -13.61 | 28.57 | 12.29 | 34.3 | False |  | mild_accumulation | 0.17 | 0.01 | 2 | 1 | -7.12 | -6.33 | -20.03 | 19 | selected |
| 2399 | 映泰 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 150.9505086438245 | 17.64304361923672 | 4.08 | -16.74 | -10.92 | -15.04 | 15.64 | 31.83 | False |  | strong_accumulation | 3.62 | 0.69 | 2 | 3 | -6.59 | -7.09 | -23.8 | 17 | selected |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth |  | 55.99925704609442 | 61.535849801128656 | 1.46 | -14.91 | -14.16 | -16.02 | 12.66 | 12.66 | False |  | strong_accumulation | 2.74 | 3.1 | 3 | 3 | -6.99 | -7.21 | -28.41 |  | fail_low_response_condition |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 51.38776767063092 | 100.55791451054965 | 1.02 | 2.07 | -6.03 | -6.77 | 14.51 | 14.51 | False |  | distribution_warning | -1.21 | -0.7 | 0 | 1 | 1.33 | 1.03 | -9.34 | 12 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 487.72943534104417 | 602.154485146844 | 5.42 | -22.23 | -26.17 | 22.22 | 17.13 | 31.77 | False |  | distribution_warning | -0.15 | -0.24 | 1 | 1 | -9.88 | -10.78 | -33.3 |  | fail_low_response_condition |
| 2414 | 精技 | 電子通路業 | mainstream_growth |  | 52.59912440445534 | 46.21659350926994 | -0.52 | -7.6 | -9.0 | -4.28 | 6.78 | 6.78 | False |  | strong_accumulation | 0.12 | 0.1 | 3 | 3 | -3.92 | -3.7 | -11.35 |  | fail_low_response_condition |
| 2419 | 仲琦 | 通信網路業 | mainstream_growth | B_可觀察 | 61.442637721350245 | 22.76545439044366 | 1.84 | -8.29 | 0.0 | -21.2 | 12.67 | 13.18 | False |  | strong_accumulation | 0.28 | 0.42 | 2 | 2 | -5.01 | -4.25 | -18.76 | 16 | selected |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth | B_可觀察 | 423.8346822457185 | 152.7650841754859 | 3.66 | -14.66 | -29.2 | -14.41 | 14.89 | 14.89 | False |  | strong_accumulation | 0.45 | 0.5 | 2 | 3 | -5.99 | -6.33 | -29.62 | 19 | selected |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 104.48808464352813 | 70.02572263494662 | -0.18 | -2.45 | -0.89 | 6.29 | 4.89 | 8.35 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | -0.56 | -0.13 | -6.69 |  | fail_low_response_condition |
| 2440 | 太空梭 | 電子零組件業 | mainstream_growth |  | 59.7408763811429 | 33.33503048242509 | -1.47 | -6.6 | -6.27 | -25.28 | 8.47 | 8.47 | False |  | mild_accumulation | 0.05 | 0.04 | 1 | 1 | -6.06 | -4.91 | -12.09 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 6975.206313416009 | 531.5739549159281 | 1.24 | -12.23 | -37.6 | -34.05 | 8.44 | 8.44 | False |  | distribution_warning | -0.12 | -0.22 | 1 | 1 | -5.37 | -6.14 | -39.15 | 13 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 191.62415264540607 | 344.4727836796557 | -9.23 | -16.3 | -23.51 | -27.01 | 0.65 | 6.94 | False |  | strong_accumulation | 0.16 | 0.43 | 2 | 2 | -13.26 | -12.25 | -29.89 |  | fail_low_response_condition |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 95.20056675819117 | 71.4699607489928 | -4.76 | -18.62 | -14.47 | -20.12 | 4.0 | 4.0 | False |  | strong_accumulation | 0.29 | 0.04 | 2 | 2 | -11.32 | -9.59 | -22.73 |  | fail_low_response_condition |
| 2464 | 盟立 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 95.9988149893207 | 42.68355260588374 | 6.55 | -16.03 | -21.17 | 7.29 | 18.39 | 30.93 | False |  | distribution_warning | -3.44 | -5.05 | 0 | 0 | -6.26 | -6.59 | -31.03 | 13 | selected |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 340.57609557459455 | 125.19243597077654 | 37.24 | 83.45 | 56.19 | 90.92 | 99.51 | 143.32 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.98 | 0.34 | 1 | 1 | 50.92 | 43.67 | 0.0 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 80.67875061959084 | 83.80094521811333 | -9.91 | -45.23 | -44.43 | -49.5 | 7.6 | 7.6 | False |  | distribution_warning | -0.11 | -0.12 | 1 | 2 | -27.18 | -26.16 | -52.64 |  | fail_low_response_condition |
| 2472 | 立隆電 | 電子零組件業 | mainstream_growth |  | 60.61793461300194 | 29.30528362005905 | 2.8 | -29.94 | -34.78 | -36.54 | 14.19 | 14.19 | False |  | distribution_warning | -0.79 | -2.74 | 2 | 0 | -14.99 | -13.64 | -35.04 |  | fail_low_response_condition |
| 2476 | 鉅祥 | 電子零組件業 | mainstream_growth |  | 62.519073558552414 | 43.69792273832236 | 2.0 | -23.62 | -21.14 | -19.83 | 13.32 | 13.32 | False |  | strong_accumulation | 0.65 | 0.77 | 2 | 2 | -11.3 | -10.22 | -27.88 |  | fail_low_response_condition |
| 2480 | 敦陽科 | 資訊服務業 | mainstream_growth |  | 69.84202715674517 | 25.070841829961658 | 13.55 | -2.08 | 17.08 | 26.09 | 22.8 | 30.45 | False |  | strong_accumulation | 0.16 | 0.19 | 2 | 2 | 4.49 | 7.11 | -4.31 |  | fail_low_response_condition |
| 2486 | 一詮 | 光電業 | mainstream_growth |  | 67.86469051765079 | 36.482902038810515 | 4.09 | -24.6 | -28.51 | -38.93 | 15.33 | 15.33 | False |  | distribution_warning | -1.9 | -2.14 | 1 | 0 | -12.97 | -13.27 | -46.18 |  | fail_low_response_condition |
| 2488 | 漢平 | 其他電子業 | mainstream_growth |  | 68.0349249896575 | 30.961077135272443 | -0.2 | -1.4 | -1.6 | -9.38 | 4.89 | 4.89 | False |  | mild_accumulation | -0.06 | 0.05 | 1 | 2 | -0.62 | -0.07 | -3.33 |  | fail_low_response_condition |
| 2492 | 華新科 | 電子零組件業 | mainstream_growth |  | 57.111134230197685 | 28.67364384164082 | -3.37 | -30.61 | -14.06 | -7.01 | 8.37 | 37.03 | False |  | distribution_warning | -0.68 | -1.19 | 1 | 1 | -21.93 | -17.44 | -36.96 |  | fail_low_response_condition |
| 2505 | 國揚 | 建材營造 | neutral |  | 110081.106870229 | 145.48970757927498 | -2.9 | -5.1 | -6.69 | -7.46 | 2.76 | 2.76 | False |  | distribution_warning | -0.22 | -0.32 | 1 | 1 | -4.42 | -3.32 | -8.97 |  | fail_low_response_condition |
| 2506 | 太設 | 建材營造 | neutral |  | 421.495501003469 | 48.86875327214938 | -1.09 | -2.86 | -4.9 | -5.88 | 0.87 | 0.87 | False |  | mild_accumulation | -0.44 | 0.53 | 0 | 2 | -2.14 | -1.97 | -6.64 |  | fail_low_response_condition |
| 2511 | 太子 | 建材營造 | neutral | B_可觀察 | 78.24940336075872 | 31.742780171246356 | -1.85 | -3.16 | -5.24 | 2.84 | 2.05 | 5.01 | False |  | mild_accumulation | 0.07 | 0.0 | 2 | 2 | -1.43 | -1.56 | -7.66 | 18 | selected |
| 2530 | 華建 | 建材營造 | neutral | B_可觀察 | 2703.9144493217 | -71.49138124020595 | -4.17 | -10.68 | -5.64 | -10.02 | 6.36 | 6.36 | False |  | mild_accumulation | 0.08 | -0.12 | 2 | 1 | -5.37 | -4.24 | -13.62 | 18 | selected |
| 2535 | 達欣工 | 建材營造 | neutral |  | 64.23038581980985 | 27.535286720968383 | 1.57 | 2.02 | 3.77 | 17.16 | 7.71 | 20.26 | False |  | mild_accumulation | -0.19 | 0.13 | 0 | 3 | 0.56 | 0.73 | -3.61 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 157.62161407365198 | 10.827675767842882 | 1.64 | -7.35 | -26.08 | -19.11 | 7.67 | 7.67 | False |  | mild_accumulation | 0.47 | 0.39 | 2 | 1 | -2.55 | -2.4 | -26.43 |  | fail_low_response_condition |
| 2540 | 愛山林 | 建材營造 | neutral |  | 360.4307813599472 | 21.214141620507657 | 0.56 | -8.4 | 1.0 | -18.91 | 6.47 | 6.6 | False |  | strong_accumulation | 0.03 | 0.18 | 2 | 3 | -1.5 | -1.42 | -16.2 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 1174.2550655542311 | 12.761197533160972 | 0.0 | -7.41 | -7.55 | -13.8 | 6.17 | 6.17 | False |  | mild_accumulation | 0.02 | -0.1 | 1 | 0 | -3.05 | -2.49 | -12.02 |  | fail_low_response_condition |
| 2547 | 日勝生 | 建材營造 | neutral | D_降級_TDCC轉弱 | 193.20885592758208 | 84.89840613579092 | 0.53 | -4.15 | -6.8 | -5.4 | 5.58 | 5.58 | False |  | distribution_warning | -0.18 | -0.04 | 1 | 1 | -1.6 | -1.22 | -8.16 | 17 | selected |
| 2603 | 長榮 | 航運業 | cyclical_turnaround | B_可觀察 | 96.13406373417418 | 22.24689137162106 | -2.9 | -4.73 | 16.71 | 14.84 | 19.19 | 39.34 | False |  | strong_accumulation | 0.16 | 0.27 | 2 | 2 | -3.38 | -1.54 | -8.38 | 18 | selected |
| 2605 | 新興 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 91.6858998835063 | 48.18745924840134 | -0.61 | -13.0 | 0.46 | 3.67 | 8.35 | 13.26 | False |  | distribution_warning | -0.18 | -0.54 | 2 | 2 | -5.13 | -4.42 | -17.22 | 12 | selected |
| 2607 | 榮運 | 航運業 | cyclical_turnaround |  | 75.98733589278142 | 23.469572484789072 | 0.17 | -1.36 | 16.03 | 20.88 | 17.09 | 27.81 | False |  | strong_accumulation | 0.08 | 0.3 | 2 | 3 | 1.07 | 2.0 | -3.18 |  | fail_low_response_condition |
| 2609 | 陽明 | 航運業 | cyclical_turnaround | B_可觀察 | 82.44651696845074 | 23.20381282773115 | -3.0 | -9.77 | 13.23 | 9.81 | 14.79 | 23.17 | False |  | mild_accumulation | 1.51 | 1.16 | 1 | 1 | -5.57 | -3.81 | -13.52 | 16 | selected |
| 2615 | 萬海 | 航運業 | cyclical_turnaround | B_可觀察 | 124.36480644917681 | 35.92088925621068 | -5.31 | -11.93 | 22.29 | 26.93 | 22.99 | 39.69 | False |  | mild_accumulation | 0.22 | 0.26 | 1 | 1 | -7.58 | -5.91 | -20.45 | 17 | selected |
| 2636 | 台驊控股 | 航運業 | cyclical_turnaround |  | 125.54297999754175 | 34.02484327434486 | 2.92 | -3.29 | 4.59 | 5.06 | 11.53 | 13.5 | False |  | strong_accumulation | 0.11 | 2.12 | 2 | 3 | 0.42 | 0.94 | -10.52 |  | fail_low_response_condition |
| 2646 | 星宇航空 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 59.47228116872314 | 39.3938941812916 | 0.51 | -1.74 | -2.94 | -3.18 | 5.88 | 5.88 | False |  | distribution_warning | -0.17 | -0.09 | 0 | 0 | -0.61 | -0.63 | -9.59 | 13 | selected |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 80.13292543760198 | 149.1882762948346 | -20.0 | 2.42 | -6.96 | 18.41 | 12.89 | 23.9 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 0 | -6.19 | -5.9 | -27.01 |  | fail_low_response_condition |
| 2929 | 淘帝-KY | 貿易百貨 | defensive_or_traditional |  | 53.441498418876186 | 20.955681131352456 | 1.41 | 0.35 | -2.04 | 0.35 | 9.32 | 9.32 | False |  | mild_accumulation | 0.62 | 0.04 | 3 | 1 | 1.63 | 1.6 | -6.5 |  | fail_low_response_condition |
| 3002 | 歐格 | 電腦及週邊設備業 | mainstream_growth |  | 85.5625401962615 | 31.473709686555406 | 3.06 | -9.41 | -0.88 | -3.99 | 13.85 | 13.85 | False |  | distribution_warning | -0.07 | -0.02 | 1 | 0 | -5.31 | -4.47 | -21.08 |  | fail_low_response_condition |
| 3003 | 健和興 | 電子零組件業 | mainstream_growth |  | 52.466111556875724 | 44.45331513053742 | -0.73 | -16.28 | -31.75 | -23.59 | 8.49 | 8.49 | False |  | strong_accumulation | 0.2 | 0.31 | 2 | 2 | -9.26 | -9.11 | -35.38 |  | fail_low_response_condition |
| 3004 | 豐達科 | 鋼鐵工業 | cyclical_turnaround |  | 51.08502105140537 | 43.33967286547871 | -0.4 | 3.33 | -3.12 | -4.98 | 8.77 | 8.77 | False |  | mild_accumulation | 0.43 | 1.43 | 1 | 1 | 1.37 | 1.53 | -4.25 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 430.0611365734368 | 353.58017683428835 | 5.37 | -6.82 | -18.74 | -5.05 | 16.84 | 40.06 | False |  | distribution_warning | -5.51 | -6.04 | 0 | 0 | -6.57 | -7.51 | -29.31 | 16 | selected |
| 3029 | 零壹 | 資訊服務業 | mainstream_growth |  | 91.12753663059947 | 28.65475028715983 | 15.93 | 9.17 | 17.49 | 35.05 | 25.96 | 39.21 | False |  | distribution_warning | -0.38 | -0.97 | 1 | 1 | 7.58 | 7.84 | -4.73 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 71.92792324679422 | 33.04466992687986 | 2.06 | -27.29 | -26.69 | -46.96 | 13.23 | 13.23 | False |  | mild_accumulation | -0.28 | 0.06 | 1 | 1 | -12.6 | -11.29 | -30.9 |  | fail_low_response_condition |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 112.86439423180833 | 102.78865814569586 | -6.15 | -13.48 | -14.88 | -36.68 | 3.98 | 3.98 | False |  | mild_accumulation | 0.06 | -0.51 | 1 | 1 | -9.96 | -8.59 | -18.12 |  | fail_low_response_condition |
| 3037 | 欣興 | 電子零組件業 | mainstream_growth |  | 67.61651572185568 | 40.87531408660304 | -1.0 | -32.88 | -20.8 | -18.35 | 10.0 | 21.29 | False |  | strong_accumulation | 0.87 | 0.93 | 2 | 2 | -18.58 | -17.14 | -44.23 |  | fail_low_response_condition |
| 3044 | 健鼎 | 電子零組件業 | mainstream_growth |  | 70.32634159542289 | 43.660674974825135 | 21.78 | -6.64 | 7.88 | 8.87 | 35.19 | 63.3 | False |  | strong_accumulation | 0.87 | 0.98 | 3 | 3 | 1.79 | 4.3 | -11.59 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 58.677185968760504 | 27.483848231923762 | 4.47 | -2.52 | -17.7 | -5.99 | 10.57 | 10.57 | False |  | distribution_warning | -1.01 | 0.0 | 1 | 0 | -0.61 | -1.05 | -19.55 |  | fail_low_response_condition |
| 3052 | 夆典 | 建材營造 | neutral |  | 98.45561279438057 | 18.586711689848357 | 0.48 | -1.87 | -6.67 | -0.47 | 3.96 | 3.96 | False |  | mild_accumulation | 0.44 | 0.02 | 2 | 1 | -0.83 | -0.29 | -7.89 |  | fail_low_response_condition |
| 3054 | 立萬利 | 電子通路業 | mainstream_growth |  | 516.8037075796083 | 352.8122144169259 | 4.29 | 3.55 | 19.96 | -13.76 | 21.46 | 29.56 | False |  | distribution_warning | -0.59 | -0.5 | 0 | 0 | 2.8 | 2.26 | -6.12 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 191.80768622489325 | 3.8670389284699467 | 10.42 | -26.8 | 11.81 | 12.29 | 23.83 | 69.22 | False |  | mild_accumulation | 1.53 | -0.97 | 2 | 0 | -4.3 | -7.99 | -41.76 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 237.29689096505317 | 229.5654302580979 | -1.64 | -19.73 | -28.99 | -43.26 | 9.09 | 9.09 | False |  | mild_accumulation | 0.17 | -0.09 | 1 | 1 | -11.49 | -11.68 | -36.0 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 174.90740647903988 | 144.49531376078457 | 13.13 | -10.03 | 30.42 | 5.78 | 38.43 | 102.3 | True | 距120日低點反彈>80% | distribution_warning | -0.35 | -5.88 | 1 | 0 | -2.93 | -0.25 | -19.36 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 169.43498384084424 | 62.374885498074185 | 13.4 | 1.27 | -14.64 | -38.72 | 25.79 | 25.79 | False |  | distribution_warning | -0.52 | -0.29 | 1 | 1 | 5.65 | 5.44 | -15.25 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 117.5572069759596 | 99.52528249578863 | 0.89 | -9.09 | -13.71 | 17.65 | 11.84 | 22.3 | False |  | strong_accumulation | 1.63 | 1.59 | 2 | 2 | -5.63 | -4.76 | -17.48 | 20 | selected |
| 3296 | 勝德 | 電子零組件業 | mainstream_growth |  | 61.238735177865614 | 21.280770602925436 | 5.88 | -18.77 | -5.06 | 14.5 | 17.49 | 18.11 | False |  | mild_accumulation | 0.3 | 0.12 | 1 | 1 | -6.98 | -6.44 | -27.3 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 53.132988411628745 | 58.859591226050156 | 13.68 | 0.47 | -7.69 | -26.03 | 26.32 | 26.32 | False |  | distribution_warning | -0.36 | -0.02 | 2 | 0 | 2.42 | 3.26 | -10.74 |  | fail_low_response_condition |
| 3308 | 聯德 | 電子零組件業 | mainstream_growth |  | 572.6775956284152 | 52.505046797577535 | -9.9 | -20.09 | -11.28 | -15.61 | 1.17 | 1.17 | False |  | strong_accumulation | 0.17 | 0.17 | 2 | 2 | -15.16 | -14.22 | -27.62 |  | fail_low_response_condition |
| 3311 | 閎暉 | 通信網路業 | mainstream_growth | B_可觀察 | 629.1409179812659 | 118.75339188355494 | 7.55 | -30.83 | 19.72 | 15.66 | 25.08 | 26.29 | False |  | mild_accumulation | 3.37 | -0.24 | 2 | 1 | -7.82 | -4.11 | -34.09 | 19 | selected |
| 3432 | 台端 | 電子零組件業 | mainstream_growth |  | 87.20206934778592 | 120.85975318742756 | -4.41 | -10.34 | -19.0 | -31.58 | 4.0 | 4.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -8.03 | -7.86 | -21.69 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 126.95750136110938 | 106.35531661015841 | 22.72 | -2.9 | 41.88 | 52.92 | 51.01 | 147.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.9 | -0.49 | 3 | 2 | 5.61 | 6.67 | -10.17 |  | fail_low_response_condition |
| 3450 | 聯鈞 | 半導體業 | mainstream_growth |  | 74.58783464735932 | 40.187058133074316 | 3.36 | -25.26 | -32.92 | -23.07 | 14.77 | 14.77 | False |  | distribution_warning | -5.48 | -3.91 | 0 | 0 | -13.15 | -14.01 | -45.87 |  | fail_low_response_condition |
| 3535 | 晶彩科 | 光電業 | mainstream_growth |  | 72.80840016689073 | 222.62788185837613 | 4.29 | -19.96 | -20.91 | -42.75 | 15.87 | 15.87 | False |  | distribution_warning | -0.12 | -0.18 | 2 | 0 | -13.27 | -10.36 | -33.94 |  | fail_low_response_condition |
| 3563 | 牧德 | 光電業 | mainstream_growth |  | 95.58715133646274 | 24.59024723903795 | 6.34 | -13.75 | -11.66 | -30.69 | 18.06 | 18.06 | False |  | mild_accumulation | 0.65 | -0.1 | 2 | 1 | -4.59 | -4.58 | -24.73 |  | fail_low_response_condition |
| 3653 | 健策 | 電子零組件業 | mainstream_growth |  | 80.6841558493479 | 50.53909493401264 | -3.45 | -19.81 | 20.93 | 53.14 | 23.73 | 87.46 | True | 距120日低點反彈>80% | mild_accumulation | -0.66 | 0.16 | 1 | 2 | -9.91 | -8.46 | -24.66 |  | fail_low_response_condition |
| 3661 | 世芯-KY | 半導體業 | mainstream_growth |  | 515.8077034803464 | 72.61924772874468 | 24.16 | -9.37 | -12.29 | -24.92 | 37.9 | 39.73 | False |  | distribution_warning | -0.91 | -2.97 | 1 | 1 | 5.53 | 4.84 | -18.87 |  | fail_low_response_condition |
| 3665 | 貿聯-KY | 其他電子業 | mainstream_growth |  | 79.99209905355778 | 44.44448312639371 | 3.06 | -32.96 | -31.29 | -31.91 | 16.99 | 16.99 | False |  | mild_accumulation | 0.73 | -0.01 | 2 | 2 | -12.11 | -13.09 | -43.58 |  | fail_low_response_condition |
| 3701 | 大眾控 | 電腦及週邊設備業 | mainstream_growth |  | 93.95223113106867 | -3.906795594950309 | 32.63 | 14.31 | 69.93 | 21.93 | 81.94 | 110.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.83 | 1.15 | 3 | 2 | 21.15 | 24.01 | 0.0 |  | fail_low_response_condition |
| 3702 | 大聯大 | 電子通路業 | mainstream_growth |  | 79.04019204347462 | 73.12719508837236 | -5.65 | -26.04 | -29.64 | -26.36 | 4.83 | 4.83 | False |  | strong_accumulation | 0.76 | 0.79 | 3 | 3 | -17.59 | -15.5 | -30.2 |  | fail_low_response_condition |
| 3715 | 定穎投控 | 電子零組件業 | mainstream_growth |  | 121.47129190100547 | 58.89467218155531 | 38.65 | 7.89 | 22.13 | -17.77 | 53.97 | 60.34 | True | 距60日低點反彈>50% | strong_accumulation | 0.51 | 0.17 | 2 | 2 | 14.72 | 15.86 | -1.03 |  | fail_low_response_condition |
| 4545 | 銘鈺 | 電子零組件業 | mainstream_growth |  | 103.77090658167121 | 10.600762729063572 | 22.27 | 7.83 | 20.4 | 18.22 | 32.15 | 32.15 | False |  | distribution_warning | -0.29 | -0.25 | 0 | 0 | 8.6 | 9.19 | -6.55 |  | fail_low_response_condition |
| 4566 | 時碩工業 | 電機機械 | cyclical_turnaround | B_可觀察 | 61.70032883785875 | 27.24080387252237 | 0.93 | -0.91 | 0.66 | 20.25 | 21.41 | 28.81 | False |  | mild_accumulation | 3.36 | 2.38 | 2 | 1 | -5.78 | -2.68 | -16.11 | 15 | selected |
| 4576 | 大銀微系統 | 電機機械 | cyclical_turnaround |  | 68.74796921849358 | 59.29022306198356 | 20.28 | -5.11 | -4.69 | -18.36 | 33.44 | 33.44 | False |  | distribution_warning | -1.18 | -1.06 | 0 | 0 | 5.51 | 4.77 | -17.25 |  | fail_low_response_condition |
| 4588 | 玖鼎電力 | 其他電子業 | mainstream_growth |  | 369.96502869440457 | 38.23538108392017 | -0.91 | -3.54 | 3.61 | -3.02 | 9.22 | 12.37 | False |  | distribution_warning | -0.02 | -0.02 | 0 | 0 | -1.82 | -1.32 | -6.03 |  | fail_low_response_condition |
| 4807 | 日成-KY | 貿易百貨 | defensive_or_traditional |  | 124.78894381077127 | 49.032732768125726 | 8.49 | -6.29 | -0.63 | 36.38 | 17.67 | 36.98 | False |  | mild_accumulation | 0.03 | 0.0 | 2 | 0 | 2.78 | 3.19 | -13.77 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 112.42760478951273 | 68.75398284152372 | 14.91 | 2.5 | 0.99 | 4.27 | 27.65 | 27.65 | False |  | mild_accumulation | 0.38 | 0.81 | 2 | 1 | 3.64 | 3.83 | -9.69 |  | fail_low_response_condition |
| 4927 | 泰鼎-KY | 電子零組件業 | mainstream_growth |  | 87.0002088072709 | 16.83446331292745 | 27.43 | 2.28 | 68.74 | 3.55 | 83.33 | 121.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 1.07 | 0.95 | 3 | 3 | 8.99 | 12.08 | -10.86 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 251.47616691406895 | 146.12933323763727 | 4.03 | -22.05 | -11.95 | -25.86 | 15.18 | 15.18 | False |  | distribution_warning | -0.14 | -0.25 | 1 | 0 | -9.35 | -7.13 | -28.93 |  | fail_low_response_condition |
| 4949 | 有成精密 | 光電業 | mainstream_growth |  | 68.40745433475969 | 59.03652713624137 | -8.03 | -21.54 | -6.83 | -34.73 | 2.07 | 18.7 | False |  | mild_accumulation | 0.38 | -0.18 | 1 | 0 | -15.28 | -13.55 | -27.08 |  | fail_low_response_condition |