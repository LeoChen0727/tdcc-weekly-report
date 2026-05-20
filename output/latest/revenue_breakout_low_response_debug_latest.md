# 營收爆發低反應股 Debug Report

- 產生時間：`2026-05-21 03:52:01 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1958 |
| standardized_revenue_rows | 1958 |
| price_rows | 251211 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1968 |
| tdcc_strong_accumulation_count | 231 |
| tdcc_mild_accumulation_count | 860 |
| tdcc_distribution_warning_count | 675 |
| revenue_condition_pass | 263 |
| price_metrics_pass | 257 |
| low_response_pass | 87 |
| already_priced_in_excluded | 42 |
| overheat_pass | 45 |
| score_pass | 45 |
| theme_priority_pass | 22 |
| final_rows | 22 |

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
| fail_revenue_condition | 1695 |
| fail_low_response_condition | 170 |
| fail_already_priced_in | 42 |
| fail_defensive_or_traditional_excluded | 19 |
| missing_or_insufficient_price_metrics | 6 |
| fail_non_mainstream_score_lt_11 | 4 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 56.2052104978021 | 55.43333917479604 | -4.19 | 10.57 | 18.06 | 18.45 | 27.97 | 38.64 | False |  | distribution_warning | -1.35 | -0.22 | 0 | 0 | 6.55 | 5.98 | -8.04 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 115.49336601749948 | 135.29308413677992 | -4.93 | -10.92 | -22.06 | -29.8 | 3.41 | 3.41 | False |  | mild_accumulation | 0.28 | -0.45 | 2 | 0 | -4.7 | -5.69 | -25.61 | 16 | selected |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 75.4889330214084 | 35.36395408045179 | -8.58 | -18.87 | 13.43 | 15.57 | 21.29 | 23.74 | False |  | mild_accumulation | -0.14 | 1.02 | 1 | 2 | -7.34 | -6.58 | -28.15 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 53.32455951906706 | 40.255746624286246 | -6.43 | -10.32 | -39.06 | -38.61 | 0.87 | 0.87 | False |  | mild_accumulation | -1.43 | 0.22 | 0 | 2 | -6.36 | -6.75 | -36.6 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 72.76557971014493 | 65.36186986942351 | 12.93 | 22.38 | 23.58 | 15.85 | 31.03 | 31.03 | False |  | distribution_warning | -0.53 | -0.03 | 0 | 0 | 13.96 | 13.61 | 0.0 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 70.9672402492807 | 42.206256661754686 | -9.52 | 50.0 | 117.56 | 134.57 | 153.33 | 153.33 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.76 | 7.45 | 2 | 1 | 8.33 | 9.11 | -14.07 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround | B_可觀察 | 71.71403036691967 | 47.62349772985901 | -3.74 | -4.03 | 4.73 | 13.74 | 5.78 | 19.6 | False |  | mild_accumulation | 0.89 | 1.08 | 1 | 1 | -1.02 | -1.52 | -10.61 | 17 | selected |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 75.98113638501123 | 84.08413462437495 | 2.11 | 35.25 | 50.49 | 53.77 | 50.19 | 60.12 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.36 | 0.35 | 2 | 2 | 18.3 | 15.4 | -5.14 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral |  | 6493.744863214747 | 11655.629597709994 | 1.04 | -2.5 | -7.3 | -24.25 | 4.1 | 4.1 | False |  | mild_accumulation | -0.16 | 0.01 | 1 | 1 | 0.21 | -0.28 | -10.02 |  | fail_low_response_condition |
| 2022 | 聚亨 | 鋼鐵工業 | cyclical_turnaround |  | 58.72797685088429 | 58.303086049163085 | -9.18 | -12.76 | -12.25 | -6.23 | 0.53 | 0.53 | False |  | strong_accumulation | 0.38 | 0.53 | 2 | 2 | -6.32 | -7.27 | -24.42 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 112.02365239427697 | 101.64282906158348 | -9.69 | -4.12 | -4.12 | 27.46 | 12.56 | 33.3 | False |  | mild_accumulation | 0.84 | 0.84 | 1 | 1 | 0.65 | -0.25 | -13.38 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 79.13810010482361 | 48.90681620491181 | -14.29 | 16.73 | 53.32 | 21.13 | 54.11 | 56.52 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.91 | -0.94 | 1 | 0 | 0.13 | 1.07 | -19.86 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 78.33000624034136 | 50.54423965195399 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 150.64504386931364 | 158.89980066771645 | -5.24 | -12.77 | -12.27 | -15.87 | 3.02 | 3.02 | False |  | strong_accumulation | 0.48 | 0.41 | 2 | 2 | -6.8 | -6.79 | -19.82 | 18 | selected |
| 2208 | 台船 | 航運業 | cyclical_turnaround |  | 132.18748539427372 | 40.98484977823417 | -8.52 | -11.84 | -19.96 | -6.89 | 0.27 | 0.27 | False |  | distribution_warning | -0.35 | -0.55 | 1 | 1 | -8.66 | -8.22 | -26.71 |  | fail_low_response_condition |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 65.61372467388287 | 34.04444901386247 | 0.75 | 15.49 | 11.09 | -7.06 | 24.26 | 24.26 | False |  | distribution_warning | -0.2 | -0.02 | 0 | 1 | 5.14 | 5.72 | -10.89 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 58.99419597132127 | 37.279628771534725 | 1.66 | -0.72 | 18.07 | 11.29 | 19.74 | 19.74 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.59 | 0.76 | -11.11 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 81.07437391238557 | 58.26494269000799 | -1.19 | -10.75 | 31.23 | 50.91 | 41.28 | 63.55 | False |  | distribution_warning | -2.2 | -1.38 | 0 | 0 | -0.06 | -0.35 | -17.82 | 14 | selected |
| 2314 | 台揚 | 通信網路業 | mainstream_growth |  | 89.93139019999026 | 64.86611212397447 | 11.88 | -7.01 | -29.13 | -39.04 | 29.2 | 29.2 | False |  | distribution_warning | -0.29 | -1.02 | 1 | 0 | 5.59 | 4.73 | -34.23 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.29425507406266 | 29.66893190701796 | -3.51 | 19.05 | 43.08 | 43.23 | 62.34 | 62.34 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.54 | 1.22 | 2 | 1 | 12.18 | 11.57 | -8.03 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 153.71283899759698 | 93.45563776655904 | -16.07 | 6.42 | 57.37 | 270.57 | 58.78 | 342.7 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.39 | -3.87 | 0 | 0 | -8.43 | -6.85 | -21.01 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 182.2232686329836 | 114.45152253341396 | -5.33 | 26.78 | 11.59 | 91.54 | 37.83 | 121.26 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.89 | 6.95 | 2 | 2 | 7.43 | 4.45 | -15.38 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 53.86862868005451 | 61.04008779861957 | -3.29 | 7.53 | 69.42 | 139.57 | 82.56 | 165.2 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.47 | 0.47 | 1 | 2 | -1.4 | 1.57 | -12.62 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 83.27774880652615 | 49.7322802816284 | 0.72 | -1.3 | 23.09 | 40.67 | 26.63 | 46.07 | False |  | mild_accumulation | 0.01 | 0.13 | 1 | 1 | 0.85 | 1.46 | -4.34 | 21 | selected |
| 2353 | 宏碁 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 68.39241034251229 | 29.65214150981726 | -3.0 | -3.35 | 1.48 | -5.51 | 7.23 | 9.8 | False |  | strong_accumulation | 0.69 | 0.84 | 2 | 2 | -1.31 | -1.23 | -6.79 | 21 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 128.89343838145112 | 86.02762799824309 | -14.14 | 1.98 | 98.56 | 163.06 | 98.56 | 183.65 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.21 | -0.52 | 1 | 1 | -5.08 | -2.87 | -18.38 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 87.15138632062427 | 113.29446010652936 | 0.33 | 5.07 | 10.48 | 19.72 | 31.65 | 31.65 | False |  | mild_accumulation | 3.75 | 2.96 | 2 | 1 | 4.3 | 4.57 | -9.62 | 20 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 58.40832442393109 | 60.83836546918864 | -8.52 | 0.82 | 45.98 | 127.02 | 77.19 | 147.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.54 | 0.13 | 2 | 1 | -9.32 | -4.52 | -18.75 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 62.53280267892302 | 73.20495684221454 | -1.38 | 5.21 | 1.55 | -5.85 | 21.42 | 21.42 | False |  | mild_accumulation | 1.35 | 0.56 | 2 | 1 | 0.86 | 1.07 | -7.84 | 19 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 73.65790531628242 | 64.15425901107987 | -3.67 | 4.68 | 33.33 | 11.65 | 46.25 | 46.25 | False |  | strong_accumulation | 2.57 | 2.79 | 2 | 2 | 0.91 | 1.47 | -13.96 | 19 | selected |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth |  | 120.71254202479236 | 79.6425126685901 | -14.83 | -14.71 | 1.75 | 3.76 | 6.62 | 11.54 | False |  | mild_accumulation | 0.24 | 0.06 | 2 | 1 | -10.43 | -8.69 | -17.73 |  | fail_low_response_condition |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 93.61728577894678 | 62.73574575073765 | -10.85 | 11.27 | 108.79 | 218.48 | 112.83 | 239.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.03 | 0.52 | 1 | 1 | -5.04 | -0.39 | -15.72 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 84.78597634196018 | 22.360190669372724 | 9.22 | 12.23 | 60.2 | 62.1 | 90.89 | 90.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.32 | -2.42 | 0 | 0 | 6.62 | 11.64 | -4.33 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 102.22569068277646 | 82.88490710977096 | 0.0 | 2.5 | 12.89 | 31.24 | 24.85 | 37.03 | False |  | distribution_warning | -0.33 | -1.25 | 1 | 1 | 2.94 | 3.15 | -9.69 | 16 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 143.2900222907499 | 161.27555347120483 | -9.08 | -10.83 | 7.32 | 48.03 | 6.75 | 54.9 | False |  | mild_accumulation | 2.67 | 3.73 | 1 | 2 | -5.5 | -6.65 | -24.59 | 18 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 717.3347932872048 | 623.5846473576565 | -14.33 | 25.0 | 1.48 | 73.5 | 38.54 | 106.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.67 | 2.54 | 2 | 2 | 3.11 | 1.48 | -22.1 |  | fail_already_priced_in |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 150.7809903622466 | -26.41191544789116 | -29.55 | -21.4 | -44.27 | -54.77 | 4.65 | 4.65 | False |  | distribution_warning | -1.01 | 0.0 | 0 | 0 | -16.41 | -18.07 | -49.86 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 87.78233369635424 | 75.58506270870245 | -2.83 | 4.65 | 14.56 | 12.59 | 30.08 | 30.08 | False |  | mild_accumulation | 0.74 | -1.27 | 2 | 0 | 2.67 | 2.36 | -9.18 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 130.07770836507694 | 45.61010923954572 | -2.83 | -12.12 | 5.75 | -8.2 | 11.23 | 11.23 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 0 | -6.3 | -4.95 | -14.45 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral |  | 168.44142686485915 | 550.3124746524734 | 0.82 | -2.89 | -10.87 | -20.47 | 3.07 | 3.07 | False |  | distribution_warning | -0.52 | -0.49 | 0 | 0 | -0.24 | -1.51 | -16.33 |  | fail_low_response_condition |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 594.4309428523752 | 419.72339242497657 | -5.35 | 16.57 | 45.31 | 57.91 | 61.62 | 84.23 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.82 | -0.33 | 2 | 1 | 4.39 | 3.93 | -14.03 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 57.62140485913217 | 60.96249952274371 | -12.06 | -19.38 | 24.0 | 100.65 | 37.17 | 121.43 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.89 | -0.97 | 0 | 0 | -10.86 | -6.26 | -24.76 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 175.797836656721 | 114.62777854736004 | -9.03 | 11.83 | 45.38 | 28.79 | 57.66 | 57.66 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.87 | 0.0 | 1 | 0 | -2.75 | 0.3 | -19.4 |  | fail_low_response_condition |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 86.98160791241624 | 76.55198946300291 | -11.5 | -1.07 | 103.3 | 223.03 | 108.66 | 229.76 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -1.21 | 1 | 1 | -3.41 | -1.12 | -15.16 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 182.9282692118469 | 24.4950641596528 | 0.47 | -2.81 | -4.0 | -10.37 | 2.73 | 2.73 | False |  | strong_accumulation | 0.14 | 0.06 | 2 | 2 | -0.92 | -1.04 | -5.57 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral |  | 5302.611940298508 | 306.8870026872911 | -3.3 | -7.46 | -7.46 | -9.2 | 1.79 | 1.79 | False |  | strong_accumulation | 1.54 | 2.2 | 2 | 2 | -5.13 | -4.34 | -11.69 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 559.0995700839725 | -21.92964905658561 | -2.42 | -15.44 | -20.93 | -18.49 | 2.27 | 2.27 | False |  | distribution_warning | -0.21 | -0.29 | 1 | 0 | -4.71 | -6.1 | -24.06 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral |  | 4077.658799321493 | 1725.2218547108523 | 2.34 | 28.91 | 14.1 | 15.92 | 29.67 | 29.67 | True | 近20日漲幅>25% | strong_accumulation | 0.81 | 0.83 | 2 | 2 | 7.58 | 7.58 | -2.46 |  | fail_already_priced_in |
| 2545 | 皇翔 | 建材營造 | neutral |  | 102.09031492521602 | 53.11675313058128 | -2.86 | -1.58 | 0.67 | -5.44 | 5.36 | 5.36 | False |  | mild_accumulation | 0.33 | 0.28 | 2 | 1 | -1.56 | -0.87 | -4.48 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 28465.962511157395 | 34773.574080324 | -0.8 | -4.63 | 14.88 | 24.87 | 15.96 | 27.98 | False |  | distribution_warning | -0.53 | -1.2 | 0 | 0 | -2.24 | -1.51 | -6.79 | 15 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 119.47429042961028 | 112.7116208532482 | -2.26 | -10.69 | -10.69 | -15.64 | 2.78 | 2.78 | False |  | distribution_warning | -0.13 | 0.0 | 0 | 0 | -3.32 | -3.95 | -19.06 |  | fail_low_response_condition |
| 2816 | 旺旺保 | 金融保險業 | defensive_or_traditional |  | 78.73621403925392 | 29.40789362443229 | -0.63 | 2.79 | 8.68 | 11.79 | 9.82 | 11.99 | False |  | strong_accumulation | 0.22 | 0.51 | 2 | 2 | 2.34 | 1.7 | -3.1 |  | fail_low_response_condition |
| 2850 | 新產 | 金融保險業 | defensive_or_traditional |  | 64.58201026377658 | 21.61586465449111 | 4.14 | 13.06 | 21.49 | 19.4 | 22.57 | 24.77 | False |  | mild_accumulation | -0.23 | 0.47 | 1 | 2 | 5.97 | 6.1 | 0.0 |  | fail_low_response_condition |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 352.9548403037368 | 50.7749326018759 | 0.0 | -8.56 | -13.87 | -7.93 | 2.3 | 2.3 | False |  | mild_accumulation | 0.06 | -0.01 | 1 | 1 | -1.49 | -2.2 | -19.58 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 160.8459070607583 | 155.54497022876842 | -15.26 | -23.61 | -1.44 | 3.79 | 20.53 | 20.53 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -13.02 | -10.77 | -31.39 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 349.21497789414195 | 202.476438292242 | 2.77 | 38.2 | 43.55 | 138.22 | 68.56 | 192.38 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.75 | 9.27 | 2 | 2 | 11.64 | 9.24 | -14.75 |  | fail_low_response_condition |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 71.62015931637609 | 99.34392209738031 | -9.48 | -8.77 | 44.44 | 64.79 | 54.97 | 94.19 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.72 | -0.94 | 0 | 0 | -10.52 | -5.75 | -22.26 |  | fail_already_priced_in |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 76.4536478332419 | 47.60130160519188 | -4.21 | -8.07 | 5.9 | 31.26 | 10.65 | 38.97 | False |  | distribution_warning | -2.05 | -1.93 | 0 | 0 | -3.66 | -3.53 | -12.81 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 106.27092931541586 | 98.74948929988273 | 15.14 | 37.68 | 82.68 | 115.86 | 90.52 | 142.53 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.28 | 0.13 | 1 | 1 | 15.24 | 15.96 | -4.42 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 62.50975349591595 | 35.380676159918806 | -16.18 | 1.76 | 88.59 | 130.56 | 90.66 | 148.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.93 | 1.65 | 1 | 1 | -6.79 | -4.43 | -20.32 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 78.6962053513493 | 92.9596666703437 | -1.76 | 28.28 | 65.58 | 89.8 | 67.07 | 114.62 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.07 | 0.58 | 1 | 2 | 18.74 | 14.21 | -4.29 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 93.60030832533867 | 16.579981523230785 | -0.39 | 4.37 | 3.43 | 5.12 | 17.8 | 17.8 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 3.13 | 2.72 | -2.66 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 2134.025974025974 | 903.0331796401772 | -1.77 | -11.2 | 114.15 | 193.39 | 115.88 | 202.73 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -3.99 | -2.85 | -30.63 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 336.3079796617205 | 120.32617467953756 | -1.32 | 35.76 | 68.93 | 90.48 | 101.44 | 101.44 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -0.86 | 1 | 1 | 20.96 | 20.16 | -9.68 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 607.8314481446032 | 296.8515627103815 | -9.72 | 53.63 | 68.58 | 287.2 | 90.5 | 324.28 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.35 | -2.23 | 1 | 0 | 10.79 | 10.15 | -20.79 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 114.23072625004656 | 125.40997222581112 | 3.59 | 24.6 | 183.12 | 280.49 | 197.71 | 318.23 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.26 | -0.31 | 1 | 1 | 4.08 | 9.2 | -12.75 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 83.84991757028762 | 32.35486967199371 | 24.4 | 60.49 | 109.12 | 132.49 | 132.84 | 148.8 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.13 | 1.58 | 2 | 1 | 31.73 | 30.17 | -2.26 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 56.26505643863285 | 48.80373503533387 | -15.62 | 1.89 | 77.46 | 150.33 | 113.56 | 164.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.97 | 0.0 | 2 | 0 | -6.4 | 0.94 | -23.25 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 111.98927364274992 | 135.2700931903602 | -5.69 | -8.3 | 2.32 | -5.69 | 8.16 | 8.16 | False |  | distribution_warning | -0.15 | -0.13 | 1 | 1 | -5.42 | -3.86 | -11.07 | 16 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 78.53183930035529 | 96.24488270368444 | -7.25 | -11.96 | -9.33 | -10.0 | 2.1 | 2.1 | False |  | mild_accumulation | -0.09 | 0.06 | 1 | 2 | -8.44 | -7.62 | -15.33 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 60.16717903418358 | 60.03667972061005 | 3.45 | 14.89 | 21.08 | 29.81 | 41.96 | 48.84 | False |  | strong_accumulation | 5.2 | 3.73 | 2 | 2 | 13.8 | 10.67 | -10.0 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 56.33450576009668 | 27.274509505356043 | -0.3 | 6.73 | 16.03 | 13.27 | 24.72 | 24.72 | False |  | distribution_warning | -0.18 | -0.16 | 1 | 0 | 2.24 | 2.35 | -6.98 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 156.85087929178133 | 81.0355514911027 | -13.6 | 23.29 | 83.83 | 144.95 | 115.19 | 153.72 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -0.44 | 0 | 0 | -1.64 | 2.95 | -22.61 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 83.23758160377125 | 97.76781501517576 | 1.47 | 13.1 | 17.42 | 21.55 | 36.35 | 36.35 | False |  | mild_accumulation | -1.11 | 0.13 | 1 | 2 | 1.76 | 3.67 | -10.48 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 474.3686868686869 | 38.12184476230543 | -2.53 | -4.14 | -4.93 | -19.49 | 2.06 | 2.06 | False |  | mild_accumulation | 0.21 | 0.1 | 2 | 1 | -2.32 | -2.39 | -9.64 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 96.2350108447434 | 115.45585350897274 | -9.41 | -0.97 | 33.38 | 27.26 | 41.86 | 48.3 | False |  | mild_accumulation | 2.25 | 0.56 | 2 | 1 | -1.01 | -0.49 | -15.67 | 16 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 50.22139699381079 | 30.082092728365648 | 37.88 | 33.78 | 42.02 | 89.26 | 68.98 | 106.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.59 | 1.23 | 2 | 2 | 33.38 | 31.4 | 0.0 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 108.38868033496968 | 125.75129312187408 | -7.87 | -7.61 | 2.5 | 25.19 | 9.33 | 40.77 | False |  | mild_accumulation | 0.08 | -0.5 | 1 | 0 | -3.67 | -4.29 | -27.75 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 78.61369654620938 | 70.71720149020462 | -8.58 | 9.43 | 29.85 | 83.16 | 53.08 | 113.06 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.93 | -0.52 | 0 | 1 | -6.85 | -2.97 | -19.2 |  | fail_already_priced_in |
| 5215 | 科嘉-KY | 電腦及週邊設備業 | mainstream_growth |  | 72.73453168813967 | 40.2037645186312 | -3.67 | 16.6 | 19.25 | 19.57 | 23.72 | 32.15 | False |  | distribution_warning | -0.98 | -0.2 | 0 | 0 | 10.81 | 8.86 | -12.38 |  | fail_low_response_condition |
| 5284 | jpp-KY | 其他 | neutral |  | 54.65432151998965 | 47.78147443327516 | -7.87 | -4.47 | 42.07 | 23.89 | 44.62 | 45.2 | True | 近60日漲幅>40% | mild_accumulation | 1.31 | 0.93 | 2 | 1 | 1.12 | 2.3 | -10.37 |  | fail_already_priced_in |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 65.52682741578477 | 51.66798309925093 | 3.02 | -2.15 | -0.73 | 0.12 | 9.21 | 9.21 | False |  | distribution_warning | -3.18 | -3.81 | 0 | 0 | 2.1 | 1.71 | -8.3 | 15 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 743.3062171016306 | 795.9274284289337 | 0.57 | 1.43 | 5.67 | 28.49 | 11.5 | 29.91 | False |  | mild_accumulation | 0.12 | -0.15 | 1 | 1 | 1.18 | 0.62 | -5.09 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1375.7984438680992 | 1302.5511357042951 | -2.61 | -10.4 | -14.18 | -20.71 | 1.13 | 1.13 | False |  | mild_accumulation | 0.16 | 0.0 | 1 | 1 | -3.57 | -4.31 | -16.42 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 70.59242292002638 | 68.32733199576585 | 4.96 | -0.69 | 37.4 | 72.04 | 50.79 | 76.25 | True | 距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.82 | -2.35 | 0 | 0 | 2.86 | 4.41 | -6.74 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 116.93180458964852 | 18.057297737695265 | -3.55 | -7.72 | 0.67 | 66.11 | 11.57 | 86.64 | True | 距120日低點反彈>80% | distribution_warning | -0.38 | -0.09 | 1 | 0 | 2.52 | -1.88 | -32.66 |  | fail_low_response_condition |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 63.164454428616175 | 37.58576900316765 | 3.59 | 46.57 | 93.47 | 103.35 | 103.7 | 115.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 0.02 | 1 | 1 | 27.03 | 24.65 | -4.15 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 264.8258137419728 | 633.4822945856635 | -4.08 | -0.56 | -6.69 | -1.11 | 1.94 | 1.94 | False |  | distribution_warning | -0.43 | -0.59 | 0 | 0 | -2.34 | -2.62 | -11.06 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 66.88098236522453 | 52.50809987028574 | 27.05 | 15.69 | 34.64 | 47.48 | 63.69 | 63.69 | True | 距60日低點反彈>50% | mild_accumulation | 1.86 | 3.28 | 1 | 1 | 18.86 | 19.26 | 0.0 |  | fail_low_response_condition |
| 6215 | 和椿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 86.85261874392444 | 66.23020669829987 | 1.24 | 14.02 | 9.42 | 13.49 | 31.04 | 31.04 | False |  | mild_accumulation | 1.21 | 1.28 | 2 | 1 | 6.23 | 5.38 | -7.58 | 21 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 76.49244300662184 | 61.90792705834754 | -13.41 | -5.16 | 69.5 | 236.62 | 97.52 | 271.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.04 | 2.69 | 1 | 1 | -1.5 | 0.16 | -18.71 |  | fail_already_priced_in |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 68.34595682594261 | 60.268154565481694 | 0.9 | 21.38 | 8.38 | 64.2 | 36.51 | 74.36 | False |  | strong_accumulation | 1.32 | 1.81 | 2 | 2 | 13.03 | 10.18 | -8.15 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 50.51274485049632 | 34.35824836559721 | -8.05 | -15.26 | 85.5 | 313.67 | 103.36 | 331.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -3.59 | 1 | 0 | -9.75 | -5.98 | -20.97 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 92.87778739857193 | 109.07996893571725 | -6.44 | 35.14 | 137.32 | 137.03 | 148.53 | 161.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -0.52 | 0 | 1 | 5.06 | 8.25 | -15.39 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 914.8854069223572 | 275.97151367822784 | -7.1 | -5.83 | -22.55 | -31.62 | 0.26 | 0.26 | False |  | mild_accumulation | 0.14 | -0.44 | 1 | 0 | -4.18 | -4.42 | -24.1 |  | fail_low_response_condition |
| 6657 | 華安 | 生技醫療業 | defensive_or_traditional |  | 89.90610328638498 | 34.22818791946309 | -2.86 | -13.33 | -13.81 | -6.14 | 1.04 | 1.04 | False |  | distribution_warning | -0.04 | 0.0 | 1 | 0 | -4.8 | -5.03 | -24.56 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 66.70054461276516 | 73.74071161548827 | -3.01 | -9.45 | 2.85 | 40.27 | 10.45 | 42.39 | False |  | mild_accumulation | -0.55 | 0.82 | 0 | 1 | -4.87 | -3.48 | -13.05 |  | fail_low_response_condition |
| 6805 | 富世達 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 59.0506505428733 | 78.47048569813265 | -6.01 | -10.18 | 8.86 | 17.41 | 17.81 | 37.6 | False |  | distribution_warning | -5.12 | -2.91 | 0 | 0 | -10.67 | -7.86 | -24.4 | 11 | selected |
| 6885 | 全福生技 | 生技醫療業 | defensive_or_traditional |  | 2152.9411764705883 | 2578.358208955224 | 2.3 | -5.33 | -21.83 | -24.87 | 4.72 | 4.72 | False |  | mild_accumulation | 0.1 | 0.0 | 2 | 1 | -2.21 | -2.63 | -24.62 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 331.0770222733691 | 129.05790884244232 | -8.81 | -5.61 | -16.46 | -26.1 | 3.46 | 3.46 | False |  | distribution_warning | -0.47 | -0.31 | 0 | 0 | -1.95 | -2.77 | -25.69 |  | fail_low_response_condition |
| 6934 | 心誠鎂 | 生技醫療業 | defensive_or_traditional |  | 546.6284074605452 | -8.724233983286908 | -1.32 | -14.19 | -39.02 |  | 7.14 |  | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -5.42 | -5.02 | -44.24 |  | fail_low_response_condition |
| 6949 | 沛爾生醫-創 | 生技醫療業 | defensive_or_traditional |  | 107.90762771168647 | -29.12783208304917 | 1.33 | -13.91 | -0.15 | 80.79 | 35.24 | 122.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.38 | 3.35 | 2 | 2 | -6.75 | -2.59 | -26.05 |  | fail_low_response_condition |
| 6952 | 大武山 | 其他 | neutral |  | 53.75729646697389 | 41.20225039748869 | -0.67 | -7.87 | -15.09 | -17.56 | 0.68 | 0.68 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -1.69 | -2.16 | -17.19 |  | fail_low_response_condition |
| 6957 | 裕慶-KY | 其他 | neutral |  | 53.31255357930569 | 34.466647133509134 | 0.63 | -1.23 | -11.11 | -23.08 | 5.26 | 5.26 | False |  | mild_accumulation | -0.01 | 0.01 | 1 | 1 | -0.02 | -0.15 | -13.04 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 345.323186054649 | 425.22423145865633 | 30.54 | 78.34 | 322.64 | 998.04 | 334.95 | 1066.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.15 | 2.6 | 0 | 1 | 44.67 | 42.77 | 0.0 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 68.76129016183084 | 90.7375655253423 | -3.17 | -8.96 | 1.24 | -5.06 | 15.09 | 15.09 | False |  | strong_accumulation | 0.03 | 0.03 | 2 | 2 | -4.29 | -2.44 | -18.67 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 2905.180718592785 | 1476.0023495403216 | -5.33 | -14.89 | 9.97 | -4.19 | 9.22 | 18.08 | False |  | distribution_warning | -1.99 | -3.5 | 0 | 0 | -9.69 | -7.61 | -22.14 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 94.8739387573844 | 63.768704057004605 | -9.76 | 28.61 | 116.96 | 229.16 | 115.09 | 257.45 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.8 | 0.12 | 0 | 1 | -0.87 | 4.58 | -18.73 |  | fail_already_priced_in |
| 7765 | 中華資安 | 數位雲端 | neutral |  | 75.03168748308813 | 28.436327862661106 | -0.61 | 5.64 | -6.7 | -10.97 | 12.21 | 12.21 | False |  | distribution_warning | -1.12 | -0.01 | 0 | 0 | 3.53 | 2.39 | -9.48 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 111.83182996542342 | 89.0289902118116 | -6.18 | 56.33 | 74.5 |  | 102.32 |  | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.4 | 0.55 | 0 | 1 | 18.08 | 17.74 | -12.7 |  | fail_low_response_condition |
| 7786 | 東方風能 | 綠能環保 | neutral |  | 52.31364457664033 | 53.1385367449244 | -17.03 | -17.33 | -23.41 |  | 0.44 |  | False |  | mild_accumulation | 0.23 | 0.0 | 1 | 0 | -13.26 | -12.59 | -30.61 |  | fail_low_response_condition |
| 7822 | 倍利科 | 半導體業 | mainstream_growth |  | 77.97234335979724 | 110.5923011120616 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 8021 | 尖點 | 其他電子業 | mainstream_growth |  | 63.17741148386335 | 54.210191135482056 | -19.06 | -10.86 | 84.65 | 185.38 | 82.32 | 209.87 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.97 | 0.87 | 2 | 1 | -14.99 | -10.26 | -27.36 |  | fail_low_response_condition |
| 8045 | 達運光電 | 通信網路業 | mainstream_growth |  | 95.94130842373109 | 60.08779268099978 | -3.25 | -9.16 | -13.45 | -10.75 | 6.09 | 6.09 | False |  | distribution_warning | -0.01 | -0.05 | 1 | 0 | -3.37 | -2.92 | -21.19 |  | fail_low_response_condition |
| 8112 | 至上 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 55.95920366319202 | 111.08875431756188 | 2.19 | -3.23 | 18.14 | 9.8 | 33.33 | 33.33 | False |  | distribution_warning | -4.85 | -5.49 | 1 | 0 | -0.87 | -0.01 | -14.2 | 12 | selected |
| 8271 | 宇瞻 | 半導體業 | mainstream_growth |  | 360.8214661098714 | 276.8939909009716 | -13.31 | -0.69 | 83.76 | 88.6 | 104.76 | 141.03 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.52 | -3.18 | 0 | 0 | -7.73 | -3.44 | -20.66 |  | fail_already_priced_in |
| 8374 | 羅昇 | 電機機械 | cyclical_turnaround |  | 62.72965373270798 | 37.07159439027231 | 7.31 | 19.33 | 13.33 | 22.35 | 50.47 | 50.47 | True | 距60日低點反彈>50% | mild_accumulation | 0.48 | 0.0 | 2 | 0 | 8.49 | 7.38 | -14.25 |  | fail_already_priced_in |
| 8488 | 吉源-KY | 其他 | neutral |  | 67.98570321422744 | 58.45035507875949 | -1.11 | -6.67 | 0.62 |  | 2.94 |  | False |  | strong_accumulation | 0.05 | 0.05 | 2 | 2 | -3.4 | -2.87 | -14.41 |  | fail_low_response_condition |
| 8499 | 鼎炫-KY | 其他電子業 | mainstream_growth |  | 95.50083046241792 | 80.38349880973118 | -10.45 | 0.91 | -2.28 | 12.3 | 16.77 | 18.51 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.84 | 0.58 | -15.09 |  | fail_low_response_condition |
| 8926 | 台汽電 | 油電燃氣業 | defensive_or_traditional |  | 532.8072071332866 | 574.6994590229478 | 5.64 | 30.22 | 37.54 | 39.63 | 39.79 | 50.13 | True | 近20日漲幅>25% | strong_accumulation | 0.72 | 0.76 | 2 | 2 | 19.03 | 16.35 | -4.47 |  | fail_low_response_condition |