# 營收爆發低反應股 Debug Report

- 產生時間：`2026-05-22 01:00:47 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1958 |
| standardized_revenue_rows | 1958 |
| price_rows | 253173 |
| tdcc_rows | 1968 |
| tdcc_trend_rows | 1968 |
| tdcc_strong_accumulation_count | 231 |
| tdcc_mild_accumulation_count | 860 |
| tdcc_distribution_warning_count | 675 |
| revenue_condition_pass | 263 |
| price_metrics_pass | 257 |
| low_response_pass | 86 |
| already_priced_in_excluded | 40 |
| overheat_pass | 46 |
| score_pass | 45 |
| theme_priority_pass | 26 |
| final_rows | 26 |

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
| fail_low_response_condition | 171 |
| fail_already_priced_in | 40 |
| fail_defensive_or_traditional_excluded | 17 |
| missing_or_insufficient_price_metrics | 6 |
| fail_non_mainstream_score_lt_11 | 2 |
| fail_score_lt_8 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 56.2052104978021 | 55.43333917479604 | 1.62 | 14.98 | 17.87 | 28.77 | 31.47 | 42.42 | False |  | distribution_warning | -1.35 | -0.22 | 0 | 0 | 8.69 | 8.07 | -5.53 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 115.49336601749948 | 135.29308413677992 | -3.59 | -8.12 | -22.66 | -28.09 | 4.88 | 4.88 | False |  | mild_accumulation | 0.28 | -0.45 | 2 | 0 | -2.93 | -4.01 | -24.56 | 16 | selected |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 75.4889330214084 | 35.36395408045179 | -3.49 | -12.63 | 15.28 | 22.66 | 23.27 | 25.76 | False |  | mild_accumulation | -0.14 | 1.02 | 1 | 2 | -5.18 | -4.65 | -26.98 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 53.32455951906706 | 40.255746624286246 | -1.66 | -8.06 | -33.22 | -38.16 | 2.77 | 2.77 | False |  | mild_accumulation | -1.43 | 0.22 | 0 | 2 | -4.18 | -4.59 | -34.26 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral |  | 72.76557971014493 | 65.36186986942351 | 14.84 | 26.51 | 29.38 | 20.39 | 37.41 | 37.41 | True | 近20日漲幅>25% | distribution_warning | -0.53 | -0.03 | 0 | 0 | 18.03 | 17.27 | -0.13 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 70.9672402492807 | 42.206256661754686 | -7.5 | 44.16 | 115.39 | 128.71 | 146.67 | 146.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.76 | 7.45 | 2 | 1 | 3.8 | 5.69 | -16.33 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround | B_可觀察 | 71.71403036691967 | 47.62349772985901 | -2.0 | 0.41 | 5.95 | 18.5 | 8.89 | 23.12 | False |  | mild_accumulation | 0.89 | 1.08 | 1 | 1 | 1.87 | 1.26 | -7.98 | 19 | selected |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 75.98113638501123 | 84.08413462437495 | 2.03 | 34.1 | 40.33 | 51.61 | 45.19 | 55.99 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 0.36 | 0.35 | 2 | 2 | 13.59 | 11.27 | -7.59 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 6493.744863214747 | 11655.629597709994 | 0.0 | -0.84 | -7.24 | -19.86 | 4.99 | 4.99 | False |  | mild_accumulation | -0.16 | 0.01 | 1 | 1 | 1.11 | 0.53 | -9.24 | 21 | selected |
| 2022 | 聚亨 | 鋼鐵工業 | cyclical_turnaround |  | 58.72797685088429 | 58.303086049163085 | -4.3 | -11.16 | -16.0 | -6.67 | 1.07 | 1.07 | False |  | strong_accumulation | 0.38 | 0.53 | 2 | 2 | -5.26 | -6.25 | -24.02 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 112.02365239427697 | 101.64282906158348 | -4.51 | -1.69 | -4.12 | 27.74 | 12.56 | 33.3 | False |  | mild_accumulation | 0.84 | 0.84 | 1 | 1 | 0.73 | -0.23 | -13.38 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 79.13810010482361 | 48.90681620491181 | -2.3 | 24.4 | 61.55 | 31.76 | 67.35 | 70.26 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.91 | -0.94 | 1 | 0 | 7.77 | 9.04 | -12.82 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 78.33000624034136 | 50.54423965195399 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 150.64504386931364 | 158.89980066771645 | -4.45 | -11.02 | -11.52 | -14.21 | 4.19 | 4.19 | False |  | strong_accumulation | 0.48 | 0.41 | 2 | 2 | -5.19 | -5.28 | -18.9 | 18 | selected |
| 2208 | 台船 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 132.18748539427372 | 40.98484977823417 | -5.57 | -9.9 | -20.64 | -3.62 | 2.47 | 2.47 | False |  | distribution_warning | -0.35 | -0.55 | 1 | 1 | -6.18 | -5.72 | -25.1 | 12 | selected |
| 2241 | 艾姆勒 | 汽車工業 | neutral |  | 65.61372467388287 | 34.04444901386247 | 12.33 | 15.49 | 23.83 | -3.66 | 36.67 | 36.67 | False |  | distribution_warning | -0.2 | -0.02 | 0 | 1 | 14.75 | 14.72 | -1.99 |  | fail_low_response_condition |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 58.99419597132127 | 37.279628771534725 | 0.55 | -4.35 | 14.11 | 11.56 | 17.4 | 19.31 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.72 | 0.36 | -11.43 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 81.07437391238557 | 58.26494269000799 | 8.26 | -1.12 | 38.82 | 63.89 | 50.64 | 74.38 | True | 距60日低點反彈>50% | distribution_warning | -2.2 | -1.38 | 0 | 0 | 6.63 | 5.7 | -12.38 |  | fail_low_response_condition |
| 2314 | 台揚 | 通信網路業 | mainstream_growth |  | 89.93139019999026 | 64.86611212397447 | 27.38 | 0.94 | -21.71 | -28.51 | 42.04 | 42.04 | False |  | distribution_warning | -0.29 | -1.02 | 1 | 0 | 16.01 | 13.7 | -27.7 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.29425507406266 | 29.66893190701796 | 12.69 | 33.04 | 57.62 | 64.49 | 78.28 | 78.28 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.54 | 1.22 | 2 | 1 | 21.33 | 20.26 | 0.0 |  | fail_low_response_condition |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 153.71283899759698 | 93.45563776655904 | -16.57 | 4.83 | 43.15 | 263.87 | 58.78 | 342.7 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.39 | -3.87 | 0 | 0 | -8.62 | -6.32 | -21.01 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 182.2232686329836 | 114.45152253341396 | -14.93 | 25.83 | 8.06 | 72.21 | 36.04 | 118.39 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.89 | 6.95 | 2 | 2 | 4.9 | 2.83 | -16.48 |  | fail_already_priced_in |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 53.86862868005451 | 61.04008779861957 | -7.29 | 12.73 | 71.03 | 148.5 | 92.25 | 179.28 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.47 | 0.47 | 1 | 2 | 3.23 | 6.35 | -7.98 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 83.27774880652615 | 49.7322802816284 | 1.32 | 0.48 | 22.85 | 44.03 | 27.69 | 47.29 | False |  | mild_accumulation | 0.01 | 0.13 | 1 | 1 | 1.67 | 2.12 | -3.54 | 21 | selected |
| 2353 | 宏碁 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 68.39241034251229 | 29.65214150981726 | 1.43 | 0.35 | 4.8 | -0.87 | 10.94 | 13.6 | False |  | strong_accumulation | 0.69 | 0.84 | 2 | 2 | 2.08 | 2.0 | -3.57 | 22 | selected |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 128.89343838145112 | 86.02762799824309 | 0.44 | 11.82 | 116.19 | 193.28 | 110.19 | 211.81 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.21 | -0.52 | 1 | 1 | 3.77 | 6.18 | -10.28 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 87.15138632062427 | 113.29446010652936 | -0.32 | 5.19 | 14.18 | 28.16 | 37.57 | 37.57 | False |  | mild_accumulation | 3.75 | 2.96 | 2 | 1 | 8.69 | 8.43 | -5.56 | 19 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 58.40832442393109 | 60.83836546918864 | -10.14 | 2.8 | 55.01 | 139.29 | 84.36 | 157.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.54 | 0.13 | 2 | 1 | -5.77 | -0.6 | -15.46 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 62.53280267892302 | 73.20495684221454 | 0.12 | 5.79 | 3.74 | -1.71 | 23.88 | 23.88 | False |  | mild_accumulation | 1.35 | 0.56 | 2 | 1 | 2.62 | 2.85 | -5.96 | 19 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 73.65790531628242 | 64.15425901107987 | -3.21 | 11.05 | 37.91 | 23.63 | 53.27 | 53.27 | True | 距60日低點反彈>50% | strong_accumulation | 2.57 | 2.79 | 2 | 2 | 5.2 | 5.78 | -9.83 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 120.71254202479236 | 79.6425126685901 | -7.92 | -8.06 | 7.69 | 11.59 | 13.24 | 18.46 | False |  | mild_accumulation | 0.24 | 0.06 | 2 | 1 | -4.47 | -2.78 | -12.62 | 21 | selected |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 93.61728577894678 | 62.73574575073765 | -4.67 | 15.38 | 113.67 | 223.45 | 120.71 | 262.16 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.03 | 0.52 | 1 | 1 | 0.65 | 5.74 | -10.07 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 84.78597634196018 | 22.360190669372724 | 13.46 | 7.5 | 74.8 | 68.3 | 100.93 | 100.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.32 | -2.42 | 0 | 0 | 11.79 | 15.82 | -2.93 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | D_降級_TDCC轉弱 | 102.22569068277646 | 82.88490710977096 | 4.76 | 10.0 | 19.18 | 38.89 | 33.98 | 47.06 | False |  | distribution_warning | -0.33 | -1.25 | 1 | 1 | 9.92 | 9.72 | -3.08 | 14 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | A_優先追蹤 | 143.2900222907499 | 161.27555347120483 | -2.83 | -5.07 | 4.57 | 48.2 | 9.77 | 59.28 | False |  | mild_accumulation | 2.67 | 3.73 | 1 | 2 | -2.57 | -3.69 | -22.46 | 19 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 717.3347932872048 | 623.5846473576565 | -14.08 | 33.79 | 5.4 | 75.98 | 47.61 | 120.3 | True | 近20日漲幅>25%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.67 | 2.54 | 2 | 2 | 8.36 | 7.39 | -17.0 |  | fail_already_priced_in |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 150.7809903622466 | -26.41191544789116 | -31.36 | -35.59 | -50.76 | -58.99 | 0.0 | 0.0 | False |  | distribution_warning | -1.01 | 0.0 | 0 | 0 | -23.17 | -24.61 | -54.87 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 87.78233369635424 | 75.58506270870245 | -3.27 | 10.73 | 25.18 | 19.06 | 35.66 | 35.66 | False |  | mild_accumulation | 0.74 | -1.27 | 2 | 0 | 6.52 | 6.15 | -5.29 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 130.07770836507694 | 45.61010923954572 | 0.0 | -11.32 | 8.02 | -4.55 | 13.39 | 13.39 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 0 | -3.89 | -2.85 | -12.79 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | D_降級_TDCC轉弱 | 168.44142686485915 | 550.3124746524734 | 2.75 | 0.54 | -9.66 | -20.59 | 4.47 | 4.47 | False |  | distribution_warning | -0.52 | -0.49 | 0 | 0 | 1.08 | -0.16 | -15.19 | 15 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 594.4309428523752 | 419.72339242497657 | -9.0 | 16.54 | 43.15 | 57.54 | 63.71 | 86.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.82 | -0.33 | 2 | 1 | 4.95 | 4.81 | -12.92 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 57.62140485913217 | 60.96249952274371 | -6.1 | -19.92 | 19.73 | 106.21 | 39.6 | 125.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.89 | -0.97 | 0 | 0 | -8.24 | -4.23 | -23.42 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 175.797836656721 | 114.62777854736004 | 0.61 | 16.55 | 60.74 | 53.89 | 73.31 | 73.31 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.87 | 0.0 | 1 | 0 | 6.09 | 9.32 | -11.41 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 86.98160791241624 | 76.55198946300291 | -4.1 | -2.01 | 114.29 | 238.15 | 116.67 | 248.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.24 | -1.21 | 1 | 1 | 2.1 | 4.03 | -10.41 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 182.9282692118469 | 24.4950641596528 | 1.17 | -2.36 | -3.77 | -10.05 | 3.21 | 3.21 | False |  | strong_accumulation | 0.14 | 0.06 | 2 | 2 | -0.34 | -0.53 | -5.14 |  | fail_low_response_condition |
| 2515 | 中工 | 建材營造 | neutral | D_降級_TDCC轉弱 | 52.62693153616593 | 39.29483572172644 | 7.36 | 1.47 | -12.34 | -18.77 | 14.46 | 14.46 | False |  | distribution_warning | -0.15 | -0.17 | 1 | 0 | 6.25 | 5.69 | -25.74 | 7 | fail_score_lt_8 |
| 2537 | 聯上發 | 建材營造 | neutral |  | 5302.611940298508 | 306.8870026872911 | -1.6 | -8.13 | -6.82 | -6.38 | 3.47 | 3.47 | False |  | strong_accumulation | 1.54 | 2.2 | 2 | 2 | -3.14 | -2.54 | -10.23 |  | fail_low_response_condition |
| 2539 | 櫻花建 | 建材營造 | neutral |  | 559.0995700839725 | -21.92964905658561 | -0.65 | -14.29 | -20.91 | -16.79 | 2.4 | 2.4 | False |  | distribution_warning | -0.21 | -0.29 | 1 | 0 | -3.82 | -5.51 | -23.96 |  | fail_low_response_condition |
| 2542 | 興富發 | 建材營造 | neutral |  | 4077.658799321493 | 1725.2218547108523 | 1.16 | 28.38 | 12.36 | 15.63 | 29.53 | 29.53 | True | 近20日漲幅>25% | strong_accumulation | 0.81 | 0.83 | 2 | 2 | 6.2 | 6.79 | -2.57 |  | fail_already_priced_in |
| 2543 | 皇昌 | 建材營造 | neutral |  | 62.14864030788222 | 31.766695479206813 | 16.71 | -9.98 | -24.1 | -23.6 | 25.37 | 25.37 | False |  | distribution_warning | -1.15 | -1.24 | 0 | 0 | 6.51 | 2.21 | -43.08 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 102.09031492521602 | 53.11675313058128 | -1.58 | -1.84 | -0.93 | -4.24 | 5.22 | 5.22 | False |  | mild_accumulation | 0.33 | 0.28 | 2 | 1 | -1.6 | -0.92 | -4.6 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral | D_降級_TDCC轉弱 | 28465.962511157395 | 34773.574080324 | -2.37 | -5.36 | 13.82 | 25.64 | 14.88 | 27.98 | False |  | distribution_warning | -0.53 | -1.2 | 0 | 0 | -1.96 | -1.39 | -6.79 | 15 | selected |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 119.47429042961028 | 112.7116208532482 | -0.38 | -9.38 | -9.38 | -15.26 | 3.57 | 3.57 | False |  | distribution_warning | -0.13 | 0.0 | 0 | 0 | -2.08 | -2.95 | -18.44 |  | fail_low_response_condition |
| 2816 | 旺旺保 | 金融保險業 | defensive_or_traditional |  | 78.73621403925392 | 29.40789362443229 | -0.96 | 1.14 | 7.28 | 10.14 | 5.99 | 10.73 | False |  | strong_accumulation | 0.22 | 0.51 | 2 | 2 | 1.14 | 0.51 | -4.18 |  | fail_low_response_condition |
| 2838 | 聯邦銀 | 金融保險業 | defensive_or_traditional |  | 62.81295828670586 | 25.276502670699795 | -0.25 | -1.23 | 3.34 | 7.2 | 6.63 | 10.14 | False |  | distribution_warning | -0.03 | -0.1 | 1 | 0 | -0.9 | -1.21 | -6.73 |  | fail_low_response_condition |
| 2850 | 新產 | 金融保險業 | defensive_or_traditional |  | 64.58201026377658 | 21.61586465449111 | 4.92 | 12.15 | 21.49 | 18.88 | 22.57 | 24.77 | False |  | mild_accumulation | -0.23 | 0.47 | 1 | 2 | 5.36 | 5.56 | -0.72 |  | fail_low_response_condition |
| 2851 | 中再保 | 金融保險業 | defensive_or_traditional |  | 605.1368833163822 | 139.31094434143236 | 7.4 | 17.72 | 29.51 | 36.73 | 34.15 | 39.69 | False |  | mild_accumulation | 0.27 | 0.71 | 1 | 2 | 10.74 | 9.4 | -0.28 |  | fail_low_response_condition |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 352.9548403037368 | 50.7749326018759 | 0.0 | -6.32 | -14.42 | -7.29 | 2.3 | 2.3 | False |  | mild_accumulation | 0.06 | -0.01 | 1 | 1 | -1.17 | -2.02 | -19.58 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 160.8459070607583 | 155.54497022876842 | -2.74 | -15.48 | -6.17 | 5.97 | 24.93 | 24.93 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -9.09 | -6.93 | -28.88 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 349.21497789414195 | 202.476438292242 | -6.72 | 32.54 | 44.16 | 141.83 | 68.18 | 191.72 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.75 | 9.27 | 2 | 2 | 9.89 | 8.18 | -14.94 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 71.62015931637609 | 99.34392209738031 | -2.35 | -7.42 | 55.45 | 75.7 | 65.23 | 107.05 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.72 | -0.94 | 0 | 0 | -4.22 | 0.45 | -17.11 |  | fail_already_priced_in |
| 3025 | 星通 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 76.4536478332419 | 47.60130160519188 | 6.25 | 0.47 | 19.41 | 46.15 | 20.75 | 51.64 | False |  | distribution_warning | -2.05 | -1.93 | 0 | 0 | 5.1 | 4.81 | -4.86 | 13 | selected |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 106.27092931541586 | 98.74948929988273 | 5.71 | 31.8 | 73.72 | 128.85 | 75.55 | 139.37 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.28 | 0.13 | 1 | 1 | 12.2 | 13.09 | -5.66 |  | fail_low_response_condition |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 62.50975349591595 | 35.380676159918806 | -5.22 | 6.56 | 106.22 | 150.16 | 103.47 | 173.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.93 | 1.65 | 1 | 1 | 2.16 | 4.63 | -12.4 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 78.6962053513493 | 92.9596666703437 | 7.37 | 36.53 | 66.57 | 103.85 | 68.5 | 124.23 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.07 | 0.58 | 1 | 2 | 22.03 | 17.44 | -0.51 |  | fail_low_response_condition |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 93.60030832533867 | 16.579981523230785 | 1.56 | 5.57 | 6.98 | 7.42 | 19.63 | 19.63 | False |  | mild_accumulation | 0.09 | 0.0 | 2 | 0 | 4.45 | 3.95 | -1.14 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 2134.025974025974 | 903.0331796401772 | -1.04 | -7.22 | 116.53 | 192.98 | 116.53 | 203.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -3.34 | -2.35 | -30.42 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 336.3079796617205 | 120.32617467953756 | 9.91 | 38.03 | 80.34 | 100.52 | 109.53 | 109.53 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.04 | -0.86 | 1 | 1 | 23.67 | 22.44 | -6.05 |  | fail_low_response_condition |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 607.8314481446032 | 296.8515627103815 | -11.34 | 46.99 | 70.74 | 291.0 | 95.5 | 335.41 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.35 | -2.23 | 1 | 0 | 11.67 | 11.82 | -18.71 |  | fail_low_response_condition |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 114.23072625004656 | 125.40997222581112 | -1.18 | 11.18 | 178.45 | 235.25 | 188.55 | 305.36 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.26 | -0.31 | 1 | 1 | 0.37 | 5.32 | -15.44 |  | fail_already_priced_in |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 83.84991757028762 | 32.35486967199371 | 24.57 | 58.2 | 111.5 | 137.89 | 136.12 | 152.31 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.13 | 1.58 | 2 | 1 | 30.38 | 28.58 | -1.86 |  | fail_low_response_condition |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 56.26505643863285 | 48.80373503533387 | -6.69 | -5.52 | 80.58 | 148.51 | 112.71 | 163.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.97 | 0.0 | 2 | 0 | -6.51 | 0.49 | -23.55 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth | D_降級_TDCC轉弱 | 111.98927364274992 | 135.2700931903602 | 1.45 | -2.78 | 6.46 | 1.45 | 14.29 | 14.29 | False |  | distribution_warning | -0.15 | -0.13 | 1 | 1 | 0.07 | 1.45 | -6.04 | 18 | selected |
| 3266 | 昇陽 | 建材營造 | neutral |  | 78.53183930035529 | 96.24488270368444 | -3.54 | -11.55 | -12.81 | -9.26 | 2.94 | 2.94 | False |  | mild_accumulation | -0.09 | 0.06 | 1 | 2 | -7.13 | -6.33 | -14.63 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 60.16717903418358 | 60.03667972061005 | 10.32 | 20.87 | 27.52 | 37.62 | 46.16 | 53.25 | False |  | strong_accumulation | 5.2 | 3.73 | 2 | 2 | 16.0 | 12.64 | -7.33 |  | fail_low_response_condition |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 56.33450576009668 | 27.274509505356043 | 2.97 | 8.44 | 21.75 | 18.84 | 29.96 | 29.96 | False |  | distribution_warning | -0.18 | -0.16 | 1 | 0 | 6.1 | 6.07 | -3.07 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 156.85087929178133 | 81.0355514911027 | -0.2 | 37.82 | 104.65 | 161.08 | 136.68 | 176.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.75 | -0.44 | 0 | 0 | 6.6 | 12.0 | -14.87 |  | fail_low_response_condition |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 83.23758160377125 | 97.76781501517576 | 2.77 | 13.13 | 18.31 | 29.24 | 40.3 | 40.3 | False |  | mild_accumulation | -1.11 | 0.13 | 1 | 2 | 4.07 | 6.08 | -7.88 |  | fail_low_response_condition |
| 4142 | 國光生 | 生技醫療業 | defensive_or_traditional |  | 474.3686868686869 | 38.12184476230543 | -0.56 | -3.03 | -2.49 | -14.36 | 3.53 | 3.53 | False |  | mild_accumulation | 0.21 | 0.1 | 2 | 1 | -0.76 | -0.9 | -8.33 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround | B_可觀察 | 96.2350108447434 | 115.45585350897274 | -6.8 | -0.73 | 39.12 | 33.24 | 46.67 | 53.32 | False |  | mild_accumulation | 2.25 | 0.56 | 2 | 1 | 2.39 | 2.64 | -12.81 | 17 | selected |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 50.22139699381079 | 30.082092728365648 | 47.68 | 42.16 | 64.12 | 111.11 | 85.71 | 127.13 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.59 | 1.23 | 2 | 2 | 43.47 | 39.25 | 0.0 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth |  | 108.38868033496968 | 125.75129312187408 | -2.31 | -2.59 | 4.31 | 30.89 | 13.0 | 45.49 | False |  | mild_accumulation | 0.08 | -0.5 | 1 | 0 | -0.31 | -0.99 | -25.33 |  | fail_low_response_condition |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 78.61369654620938 | 70.71720149020462 | -6.49 | 1.72 | 33.58 | 81.91 | 56.3 | 117.55 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.93 | -0.52 | 0 | 1 | -4.97 | -0.85 | -17.49 |  | fail_already_priced_in |
| 5215 | 科嘉-KY | 電腦及週邊設備業 | mainstream_growth |  | 72.73453168813967 | 40.2037645186312 | -0.56 | 17.3 | 18.07 | 15.34 | 24.13 | 32.59 | False |  | distribution_warning | -0.98 | -0.2 | 0 | 0 | 10.28 | 8.39 | -12.08 |  | fail_low_response_condition |
| 5284 | jpp-KY | 其他 | neutral |  | 54.65432151998965 | 47.78147443327516 | 1.3 | 8.01 | 53.94 | 36.95 | 55.78 | 56.4 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.31 | 0.93 | 2 | 1 | 8.48 | 9.26 | -3.46 |  | fail_already_priced_in |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | D_降級_TDCC轉弱 | 65.52682741578477 | 51.66798309925093 | 6.82 | -1.54 | 0.97 | 1.84 | 10.81 | 10.81 | False |  | distribution_warning | -3.18 | -3.81 | 0 | 0 | 3.68 | 2.92 | -6.95 | 15 | selected |
| 5522 | 遠雄 | 建材營造 | neutral |  | 743.3062171016306 | 795.9274284289337 | -0.14 | 0.0 | 3.99 | 24.82 | 10.87 | 27.08 | False |  | mild_accumulation | 0.12 | -0.15 | 1 | 1 | 0.61 | 0.05 | -5.63 |  | fail_low_response_condition |
| 5525 | 順天 | 建材營造 | neutral |  | 1375.7984438680992 | 1302.5511357042951 | -3.04 | -10.08 | -14.56 | -20.78 | 0.68 | 0.68 | False |  | mild_accumulation | 0.16 | 0.0 | 1 | 1 | -3.48 | -4.36 | -16.79 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 70.59242292002638 | 68.32733199576585 | 8.89 | 8.74 | 51.06 | 86.89 | 64.19 | 91.92 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.82 | -2.35 | 0 | 0 | 11.51 | 12.4 | -0.76 |  | fail_low_response_condition |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 116.93180458964852 | 18.057297737695265 | -2.53 | -2.22 | 1.32 | 79.07 | 14.93 | 92.26 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.38 | -0.09 | 1 | 0 | 5.73 | 0.99 | -30.63 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 63.164454428616175 | 37.58576900316765 | 6.28 | 46.3 | 90.82 | 112.37 | 108.99 | 121.08 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 0.02 | 1 | 1 | 27.69 | 24.99 | -3.66 |  | fail_low_response_condition |
| 6177 | 達麗 | 建材營造 | neutral |  | 264.8258137419728 | 633.4822945856635 | -2.3 | -1.54 | -7.75 | -0.45 | 1.94 | 1.94 | False |  | distribution_warning | -0.43 | -0.59 | 0 | 0 | -2.27 | -2.4 | -11.06 |  | fail_low_response_condition |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 66.88098236522453 | 52.50809987028574 | 26.94 | 33.38 | 48.71 | 61.45 | 79.88 | 79.88 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.86 | 3.28 | 1 | 1 | 28.51 | 27.74 | 0.0 |  | fail_low_response_condition |
| 6215 | 和椿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 86.85261874392444 | 66.23020669829987 | 5.88 | 14.03 | 12.0 | 23.53 | 35.34 | 35.34 | False |  | mild_accumulation | 1.21 | 1.28 | 2 | 1 | 8.97 | 8.04 | -4.55 | 20 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 76.49244300662184 | 61.90792705834754 | -4.55 | 6.71 | 69.9 | 276.61 | 116.94 | 307.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.04 | 2.69 | 1 | 1 | 7.81 | 9.1 | -10.71 |  | fail_already_priced_in |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 68.34595682594261 | 60.268154565481694 | 2.05 | 23.34 | 10.07 | 70.88 | 38.06 | 76.35 | True | 近120日漲幅>70% | strong_accumulation | 1.32 | 1.81 | 2 | 2 | 13.1 | 10.38 | -7.1 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 50.51274485049632 | 34.35824836559721 | -9.77 | -11.37 | 90.01 | 331.29 | 112.99 | 351.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.23 | -3.59 | 1 | 0 | -4.9 | -1.4 | -17.23 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 92.87778739857193 | 109.07996893571725 | -16.57 | 10.61 | 121.21 | 109.07 | 123.75 | 135.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.04 | -0.52 | 0 | 1 | -5.84 | -2.34 | -23.83 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 914.8854069223572 | 275.97151367822784 | 1.04 | -5.46 | -19.02 | -29.57 | 2.91 | 2.91 | False |  | mild_accumulation | 0.14 | -0.44 | 1 | 0 | -1.38 | -1.74 | -22.1 |  | fail_low_response_condition |
| 6657 | 華安 | 生技醫療業 | defensive_or_traditional |  | 89.90610328638498 | 34.22818791946309 | 0.13 | -9.43 | -15.21 | -4.44 | 3.24 | 3.24 | False |  | distribution_warning | -0.04 | 0.0 | 1 | 0 | -2.23 | -2.72 | -22.92 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 66.70054461276516 | 73.74071161548827 | -2.51 | -9.21 | 3.67 | 39.39 | 11.89 | 44.25 | False |  | mild_accumulation | -0.55 | 0.82 | 0 | 1 | -3.16 | -2.04 | -11.91 |  | fail_low_response_condition |
| 6805 | 富世達 | 電子零組件業 | mainstream_growth |  | 59.0506505428733 | 78.47048569813265 | 1.69 | -8.82 | 17.15 | 21.07 | 23.97 | 44.8 | False |  | distribution_warning | -5.12 | -2.91 | 0 | 0 | -5.57 | -2.79 | -20.44 |  | fail_low_response_condition |
| 6885 | 全福生技 | 生技醫療業 | defensive_or_traditional |  | 2152.9411764705883 | 2578.358208955224 | 4.91 | -6.07 | -19.68 | -22.32 | 5.9 | 5.9 | False |  | mild_accumulation | 0.1 | 0.0 | 2 | 1 | -0.8 | -1.4 | -23.77 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral | D_降級_TDCC轉弱 | 331.0770222733691 | 129.05790884244232 | -1.05 | -1.74 | -12.15 | -18.73 | 8.46 | 8.46 | False |  | distribution_warning | -0.47 | -0.31 | 0 | 0 | 2.88 | 1.77 | -22.1 | 15 | selected |
| 6934 | 心誠鎂 | 生技醫療業 | defensive_or_traditional |  | 546.6284074605452 | -8.724233983286908 | 1.74 | -10.59 | -35.86 |  | 8.57 |  | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -3.61 | -3.45 | -43.49 |  | fail_low_response_condition |
| 6949 | 沛爾生醫-創 | 生技醫療業 | defensive_or_traditional |  | 107.90762771168647 | -29.12783208304917 | -5.87 | -21.63 | -0.59 | 77.37 | 32.68 | 118.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.38 | 3.35 | 2 | 2 | -7.34 | -4.08 | -27.45 |  | fail_low_response_condition |
| 6952 | 大武山 | 其他 | neutral |  | 53.75729646697389 | 41.20225039748869 | 0.54 | -6.57 | -14.65 | -16.57 | 1.09 | 1.09 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | -0.94 | -1.61 | -16.85 |  | fail_low_response_condition |
| 6957 | 裕慶-KY | 其他 | neutral |  | 53.31255357930569 | 34.466647133509134 | 0.63 | -1.23 | -8.05 | -23.81 | 5.26 | 5.26 | False |  | mild_accumulation | -0.01 | 0.01 | 1 | 1 | 0.05 | -0.14 | -13.04 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 345.323186054649 | 425.22423145865633 | 41.38 | 83.58 | 348.91 | 1105.88 | 369.47 | 1181.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.15 | 2.6 | 0 | 1 | 53.33 | 49.71 | 0.0 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 68.76129016183084 | 90.7375655253423 | 3.25 | -9.61 | 4.96 | -1.17 | 19.81 | 19.81 | False |  | strong_accumulation | 0.03 | 0.03 | 2 | 2 | 0.16 | 1.42 | -15.33 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 2905.180718592785 | 1476.0023495403216 | 4.45 | -12.0 | 10.0 | 8.31 | 12.1 | 29.89 | False |  | distribution_warning | -1.99 | -3.5 | 0 | 0 | 0.01 | 1.49 | -14.36 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 94.8739387573844 | 63.768704057004605 | -12.39 | 17.89 | 95.53 | 205.98 | 107.33 | 244.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.8 | 0.12 | 0 | 1 | -5.14 | 0.74 | -21.66 |  | fail_low_response_condition |
| 7765 | 中華資安 | 數位雲端 | neutral |  | 75.03168748308813 | 28.436327862661106 | 2.04 | 9.65 | -5.12 | -9.09 | 15.21 | 15.21 | False |  | distribution_warning | -1.12 | -0.01 | 0 | 0 | 5.8 | 4.68 | -7.06 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 111.83182996542342 | 89.0289902118116 | 1.52 | 61.75 | 76.64 |  | 122.46 |  | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -0.4 | 0.55 | 0 | 1 | 26.7 | 26.36 | -4.0 |  | fail_low_response_condition |
| 7786 | 東方風能 | 綠能環保 | neutral |  | 52.31364457664033 | 53.1385367449244 | -10.69 | -14.91 | -24.52 |  | 2.63 | 2.63 | False |  | mild_accumulation | 0.23 | 0.0 | 1 | 0 | -10.67 | -9.88 | -29.09 |  | fail_low_response_condition |
| 7822 | 倍利科 | 半導體業 | mainstream_growth |  | 77.97234335979724 | 110.5923011120616 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 8021 | 尖點 | 其他電子業 | mainstream_growth |  | 63.17741148386335 | 54.210191135482056 | -21.71 | -13.8 | 89.16 | 188.72 | 82.42 | 229.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.97 | 0.87 | 2 | 1 | -8.91 | -4.18 | -22.74 |  | fail_already_priced_in |
| 8045 | 達運光電 | 通信網路業 | mainstream_growth |  | 95.94130842373109 | 60.08779268099978 | 0.0 | -10.42 | -12.38 | -6.36 | 7.28 | 7.28 | False |  | distribution_warning | -0.01 | -0.05 | 1 | 0 | -1.73 | -1.68 | -17.49 |  | fail_low_response_condition |
| 8112 | 至上 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 55.95920366319202 | 111.08875431756188 | 1.18 | -2.84 | 18.26 | 13.4 | 35.71 | 35.71 | False |  | distribution_warning | -4.85 | -5.49 | 1 | 0 | 1.05 | 1.62 | -12.67 | 13 | selected |
| 8271 | 宇瞻 | 半導體業 | mainstream_growth |  | 360.8214661098714 | 276.8939909009716 | -12.7 | -7.56 | 86.44 | 101.83 | 109.52 | 146.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.52 | -3.18 | 0 | 0 | -5.21 | -1.1 | -18.82 |  | fail_already_priced_in |