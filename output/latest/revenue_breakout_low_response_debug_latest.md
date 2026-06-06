# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-06 09:04:34 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1957 |
| standardized_revenue_rows | 1957 |
| price_rows | 577184 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 470 |
| tdcc_mild_accumulation_count | 736 |
| tdcc_distribution_warning_count | 618 |
| revenue_condition_pass | 263 |
| price_metrics_pass | 261 |
| low_response_pass | 67 |
| already_priced_in_excluded | 34 |
| overheat_pass | 33 |
| score_pass | 33 |
| theme_priority_pass | 24 |
| final_rows | 24 |

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
| fail_revenue_condition | 1694 |
| fail_low_response_condition | 194 |
| fail_already_priced_in | 34 |
| fail_defensive_or_traditional_excluded | 8 |
| missing_or_insufficient_price_metrics | 2 |
| fail_non_mainstream_score_lt_11 | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 56.2052104978021 | 55.43333917479604 | -11.92 | -2.16 | 16.4 | 31.64 | 26.57 | 36.09 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -6.05 | -5.06 | -17.16 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 115.49336601749948 | 135.29308413677992 | 4.95 | -4.93 | -18.15 | -29.57 | 6.0 | 6.0 | False |  | mild_accumulation | 0.06 | 0.32 | 2 | 1 | 1.95 | 0.13 | -19.7 | 17 | selected |
| 1449 | 佳和 | 紡織纖維 | defensive_or_traditional |  | 75.4889330214084 | 35.36395408045179 | 5.86 | 5.04 | 26.64 | 34.16 | 25.46 | 35.5 | False |  | mild_accumulation | -0.84 | 0.32 | 1 | 2 | 5.88 | 3.37 | -20.53 |  | fail_low_response_condition |
| 1522 | 堤維西 | 汽車工業 | neutral |  | 53.32455951906706 | 40.255746624286246 | -7.09 | 6.47 | -7.76 | -34.42 | 12.43 | 12.43 | False |  | distribution_warning | -0.87 | -0.16 | 1 | 2 | 3.36 | 0.77 | -8.94 |  | fail_low_response_condition |
| 1533 | 車王電 | 汽車工業 | neutral | D_降級_TDCC轉弱 | 72.76557971014493 | 65.36186986942351 | 2.97 | 14.99 | 29.13 | 27.68 | 37.59 | 37.59 | False |  | distribution_warning | -0.06 | -0.03 | 0 | 0 | 4.23 | 6.12 | -4.55 | 11 | selected |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 70.9672402492807 | 42.206256661754686 | -6.94 | -6.94 | 114.74 | 129.77 | 115.02 | 148.15 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.98 | -6.8 | 1 | 0 | -7.79 | -3.62 | -24.21 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 71.71403036691967 | 47.62349772985901 | 21.05 | 15.0 | 22.6 | 39.73 | 27.49 | 44.47 | False |  | mild_accumulation | 0.91 | 1.26 | 1 | 1 | 15.91 | 14.1 | -5.35 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 75.98113638501123 | 84.08413462437495 | 8.32 | 14.32 | 44.86 | 69.54 | 54.38 | 74.79 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.2 | 0.19 | 2 | 2 | 8.99 | 11.24 | -5.47 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 6493.744863214747 | 11655.629597709994 | 7.12 | 7.3 | 1.61 | -0.63 | 12.66 | 12.66 | False |  | strong_accumulation | 0.46 | 0.18 | 3 | 2 | 7.61 | 6.62 | -2.02 | 21 | selected |
| 2022 | 聚亨 | 鋼鐵工業 | cyclical_turnaround |  | 58.72797685088429 | 58.303086049163085 | 4.43 | 1.52 | -8.76 | -2.79 | 7.22 | 7.22 | False |  | strong_accumulation | 0.24 | 0.4 | 2 | 3 | 3.66 | 1.6 | -19.4 |  | fail_low_response_condition |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 112.02365239427697 | 101.64282906158348 | 12.61 | 9.84 | 25.82 | 38.14 | 28.85 | 45.49 | False |  | mild_accumulation | 0.74 | 0.78 | 1 | 1 | 10.79 | 10.72 | -0.37 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 79.13810010482361 | 48.90681620491181 | 10.96 | 12.18 | 69.28 | 58.98 | 78.41 | 95.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.09 | -0.39 | 2 | 1 | 12.2 | 12.76 | -3.19 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 78.33000624034136 | 50.54423965195399 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 150.64504386931364 | 158.89980066771645 | 6.16 | -2.0 | 0.79 | -16.82 | 8.14 | 8.14 | False |  | mild_accumulation | 0.04 | -0.13 | 2 | 2 | 3.39 | 0.83 | -16.82 | 19 | selected |
| 2208 | 台船 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 132.18748539427372 | 40.98484977823417 | 3.38 | -7.09 | -16.97 | -10.49 | 3.67 | 3.67 | False |  | distribution_warning | -1.1 | -1.51 | 0 | 0 | 0.47 | -1.22 | -18.44 | 14 | selected |
| 2241 | 艾姆勒 | 汽車工業 | neutral | B_可觀察 | 65.61372467388287 | 34.04444901386247 | 2.46 | 7.76 | 20.61 | -6.84 | 31.11 | 31.11 | False |  | strong_accumulation | 5.87 | 1.78 | 2 | 2 | 0.45 | 3.63 | -11.39 | 16 | selected |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 58.99419597132127 | 37.279628771534725 | 4.36 | 5.12 | 15.35 | 15.81 | 19.54 | 24.73 | False |  | distribution_warning | -0.8 | 0.0 | 0 | 0 | 4.23 | 3.76 | -7.41 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 81.07437391238557 | 58.26494269000799 | -5.46 | 37.61 | 51.52 | 111.27 | 62.45 | 116.35 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.21 | 0.18 | 2 | 2 | 8.68 | 7.53 | -10.0 |  | fail_already_priced_in |
| 2314 | 台揚 | 通信網路業 | mainstream_growth |  | 89.93139019999026 | 64.86611212397447 | 0.64 | 25.4 | -14.13 | -34.71 | 39.82 | 39.82 | True | 近20日漲幅>25% | distribution_warning | -2.49 | -4.0 | 1 | 0 | 2.4 | 1.68 | -28.83 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.29425507406266 | 29.66893190701796 | -0.89 | 24.63 | 66.17 | 56.07 | 80.35 | 97.17 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.83 | -2.37 | 2 | 1 | 6.15 | 8.31 | -11.17 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 153.71283899759698 | 93.45563776655904 | -9.91 | -11.24 | 26.05 | 302.68 | 29.87 | 318.41 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.28 | -2.49 | 1 | 1 | -4.35 | -4.84 | -16.67 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 182.2232686329836 | 114.45152253341396 | 2.53 | 20.9 | 38.46 | 138.59 | 93.32 | 142.15 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.7 | 5.52 | 2 | 2 | 11.88 | 11.0 | -16.06 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 53.86862868005451 | 61.04008779861957 | 2.47 | -6.92 | 79.14 | 154.86 | 75.35 | 151.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.5 | -0.11 | 1 | 2 | 0.28 | 1.61 | -7.61 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 83.27774880652615 | 49.7322802816284 | 2.79 | 6.0 | 14.38 | 45.47 | 18.05 | 54.1 | False |  | strong_accumulation | 0.2 | 0.05 | 2 | 2 | 3.14 | 2.65 | -6.06 | 22 | selected |
| 2353 | 宏碁 | 電腦及週邊設備業 | mainstream_growth |  | 68.39241034251229 | 29.65214150981726 | 9.09 | 37.14 | 41.44 | 43.82 | 43.82 | 53.6 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 1.48 | 1.55 | 3 | 3 | 15.85 | 12.66 | -13.12 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 128.89343838145112 | 86.02762799824309 | 1.79 | 13.5 | 76.9 | 218.63 | 77.51 | 252.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.55 | 1.24 | 3 | 3 | 6.72 | 6.44 | -8.23 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 87.15138632062427 | 113.29446010652936 | -6.58 | -0.79 | 23.27 | 19.96 | 35.28 | 36.91 | False |  | strong_accumulation | 3.53 | 4.42 | 2 | 3 | -3.79 | -1.88 | -13.19 | 19 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 58.40832442393109 | 60.83836546918864 | -0.38 | -8.04 | 44.66 | 123.64 | 53.98 | 127.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 1.08 | 1 | 3 | -0.74 | -0.86 | -13.49 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 62.53280267892302 | 73.20495684221454 | -4.21 | -0.75 | 11.16 | -4.21 | 20.39 | 22.8 | False |  | mild_accumulation | 1.68 | 1.2 | 3 | 1 | -2.71 | -1.63 | -7.75 | 18 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 73.65790531628242 | 64.15425901107987 | -0.27 | 12.84 | 56.03 | 50.0 | 66.59 | 78.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.58 | 0.18 | 2 | 2 | 6.65 | 6.5 | -8.21 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth |  | 120.71254202479236 | 79.6425126685901 | 15.19 | 16.74 | 35.12 | 31.26 | 41.74 | 50.19 | False |  | distribution_warning | -1.24 | -1.39 | 1 | 0 | 16.62 | 12.23 | -10.84 |  | fail_low_response_condition |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 93.61728577894678 | 62.73574575073765 | -4.59 | -0.71 | 88.97 | 228.96 | 88.25 | 233.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.07 | 1 | 1 | -1.1 | 0.39 | -13.31 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 84.78597634196018 | 22.360190669372724 | -10.4 | -9.1 | 39.19 | 21.09 | 38.63 | 60.98 | False |  | distribution_warning | -0.23 | -0.41 | 1 | 1 | -12.02 | -9.11 | -24.53 |  | fail_low_response_condition |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 102.22569068277646 | 82.88490710977096 | 4.33 | 14.76 | 25.0 | 48.77 | 46.77 | 49.5 | False |  | strong_accumulation | 5.25 | 3.89 | 3 | 3 | 5.19 | 6.22 | -10.41 | 21 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth | D_降級_TDCC轉弱 | 143.2900222907499 | 161.27555347120483 | 0.29 | 8.96 | -0.43 | 50.0 | 23.09 | 54.69 | False |  | distribution_warning | -0.58 | -0.14 | 1 | 2 | 2.9 | 1.01 | -17.11 | 13 | selected |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 717.3347932872048 | 623.5846473576565 | 3.75 | 5.57 | 37.67 | 120.18 | 81.36 | 133.01 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.19 | 0.07 | 2 | 2 | 8.69 | 7.87 | -16.38 |  | fail_already_priced_in |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 150.7809903622466 | -26.41191544789116 | 2.0 | -45.97 | -56.78 | -60.28 | 4.08 | 4.08 | False |  | distribution_warning | -0.88 | -2.35 | 0 | 0 | -13.88 | -17.03 | -58.13 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 87.78233369635424 | 75.58506270870245 | -0.42 | 0.71 | 14.17 | 24.39 | 36.35 | 41.24 | False |  | strong_accumulation | 0.94 | 0.63 | 2 | 2 | 1.22 | 2.24 | -5.59 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 130.07770836507694 | 45.61010923954572 | 7.75 | 8.57 | 2.89 | 6.54 | 13.1 | 23.11 | False |  | mild_accumulation | 0.07 | 0.0 | 3 | 0 | 7.04 | 5.33 | -5.32 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 168.44142686485915 | 550.3124746524734 | 6.7 | 9.34 | -3.63 | -21.81 | 11.17 | 11.17 | False |  | mild_accumulation | -0.74 | 0.18 | 1 | 1 | 6.33 | 5.31 | -9.75 | 20 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 594.4309428523752 | 419.72339242497657 | -4.88 | -6.68 | 23.89 | 77.62 | 54.2 | 91.37 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.76 | -1.84 | 2 | 1 | -2.36 | -1.7 | -16.06 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 57.62140485913217 | 60.96249952274371 | -0.77 | -4.32 | 32.3 | 76.65 | 34.24 | 74.25 | True | 近120日漲幅>70% | distribution_warning | -0.26 | -0.36 | 2 | 1 | -1.15 | -2.52 | -21.97 |  | fail_low_response_condition |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 175.797836656721 | 114.62777854736004 | 0.6 | 0.85 | 45.63 | 50.09 | 64.95 | 73.72 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 2.2 | 1.5 | 2 | 1 | 0.13 | 0.94 | -11.19 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 86.98160791241624 | 76.55198946300291 | -6.3 | -4.92 | 53.24 | 156.07 | 67.15 | 167.28 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.57 | -0.47 | 2 | 2 | -5.02 | -3.8 | -16.18 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 182.9282692118469 | 24.4950641596528 | 3.82 | 4.66 | 2.05 | -5.57 | 6.78 | 6.78 | False |  | strong_accumulation | 0.38 | 0.1 | 3 | 3 | 3.25 | 2.69 | -1.21 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | B_可觀察 | 5302.611940298508 | 306.8870026872911 | 7.41 | 1.6 | 0.5 | -4.69 | 8.21 | 8.21 | False |  | strong_accumulation | 1.2 | 1.2 | 2 | 2 | 4.68 | 3.01 | -7.31 | 24 | selected |
| 2539 | 櫻花建 | 建材營造 | neutral | D_降級_TDCC轉弱 | 559.0995700839725 | -21.92964905658561 | 2.05 | -3.36 | -23.38 | -21.37 | 12.84 | 12.84 | False |  | distribution_warning | -0.54 | -0.69 | 0 | 0 | 1.11 | -0.88 | -25.6 | 12 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 4077.658799321493 | 1725.2218547108523 | 2.5 | -0.35 | 16.85 | 13.31 | 27.6 | 27.6 | False |  | strong_accumulation | 1.04 | 0.94 | 2 | 3 | 0.13 | 2.01 | -4.02 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral |  | 62.14864030788222 | 31.766695479206813 | 7.41 | 23.87 | -33.02 | -18.78 | 33.06 | 33.06 | False |  | distribution_warning | -1.41 | -1.81 | 0 | 0 | 12.39 | 8.45 | -33.91 |  | fail_low_response_condition |
| 2545 | 皇翔 | 建材營造 | neutral |  | 102.09031492521602 | 53.11675313058128 | 5.65 | 1.19 | 5.65 | 0.79 | 8.18 | 8.18 | False |  | mild_accumulation | -0.06 | 0.24 | 2 | 1 | 3.58 | 2.92 | -1.92 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral |  | 28465.962511157395 | 34773.574080324 | -13.39 | -18.18 | -12.29 | -0.48 | 4.02 | 4.02 | False |  | distribution_warning | -0.97 | -0.36 | 0 | 1 | -12.65 | -11.33 | -21.89 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 119.47429042961028 | 112.7116208532482 | 8.85 | 8.02 | -5.35 | -5.35 | 12.3 | 12.3 | False |  | strong_accumulation | 0.45 | 0.74 | 2 | 2 | 7.52 | 5.54 | -7.82 |  | fail_low_response_condition |
| 2816 | 旺旺保 | 金融保險業 | defensive_or_traditional |  | 78.73621403925392 | 29.40789362443229 | 5.06 | 9.6 | 13.41 | 15.32 | 14.36 | 21.67 | False |  | strong_accumulation | 0.45 | 0.05 | 2 | 3 | 6.56 | 5.81 | -4.73 |  | fail_low_response_condition |
| 2850 | 新產 | 金融保險業 | defensive_or_traditional |  | 64.58201026377658 | 21.61586465449111 | 0.34 | 10.61 | 24.26 | 25.32 | 26.96 | 31.53 | False |  | mild_accumulation | 0.44 | -0.36 | 3 | 1 | 4.21 | 4.75 | -1.35 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 1002.1406834015808 | 365.76888748391855 | 24.42 | 47.2 | 92.2 | 138.79 | 92.82 | 148.32 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.61 | -0.49 | 0 | 0 | 30.65 | 28.23 | -1.17 |  | fail_low_response_condition |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 59.58077358578821 | 30.53659326449297 | 14.1 | 6.75 | 3.88 | 13.91 | 17.57 | 17.57 | False |  | distribution_warning | -0.4 | -0.34 | 0 | 1 | 8.08 | 5.73 | -9.84 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 219.78523407605732 | 402.5871994932322 | 7.27 | 24.74 | 32.88 | 23.56 | 38.34 | 41.32 | False |  | strong_accumulation | 0.8 | 0.82 | 3 | 3 | 13.14 | 12.32 | -0.84 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 153.9148431130897 | 577.0666572623264 | 16.69 | 30.38 | 38.12 | 44.93 | 44.72 | 48.59 | True | 近20日漲幅>25% | strong_accumulation | 0.18 | 0.24 | 2 | 2 | 18.79 | 17.39 | 0.0 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 144.30631310157813 | 319.6219559348892 | 22.67 | 24.89 | 34.63 | 70.37 | 43.75 | 71.43 | True | 近120日漲幅>70% | strong_accumulation | 0.03 | 0.04 | 2 | 2 | 21.36 | 19.08 | -3.16 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 324.89668645555184 | 112.85581098417563 | 9.56 | 17.66 | 46.41 | 74.6 | 52.21 | 75.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.07 | -0.02 | 1 | 1 | 12.45 | 11.78 | -2.1 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 87.36017222905045 | 50.078518078805 | 9.0 | 7.21 | 3.81 | 19.34 | 14.14 | 20.22 | False |  | distribution_warning | -0.67 | -0.65 | 0 | 0 | 8.09 | 6.09 | -2.82 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 1120.5725622466316 | 81.69612153552563 | 10.08 | 21.53 | 28.32 | 49.49 | 32.14 | 50.0 | False |  | strong_accumulation | 0.3 | 0.4 | 2 | 2 | 11.06 | 10.06 | -5.53 |  | fail_low_response_condition |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 352.9548403037368 | 50.7749326018759 | 3.65 | 6.37 | -4.38 | -16.96 | 8.81 | 8.81 | False |  | mild_accumulation | -0.01 | 0.07 | 0 | 2 | 3.99 | 2.84 | -5.33 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 160.8459070607583 | 155.54497022876842 | -2.34 | 14.16 | 40.85 | 16.28 | 46.63 | 46.63 | True | 近60日漲幅>40% | distribution_warning | -0.05 | 0.0 | 0 | 0 | 6.75 | 3.26 | -16.25 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 349.21497789414195 | 202.476438292242 | -9.74 | -6.51 | 25.71 | 168.4 | 51.36 | 187.47 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.82 | 1.61 | 2 | 2 | -7.75 | -4.7 | -18.65 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 71.62015931637609 | 99.34392209738031 | -2.44 | 1.76 | 42.08 | 87.73 | 41.69 | 105.53 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.58 | 0 | 1 | 0.1 | -0.91 | -13.62 |  | fail_already_priced_in |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 76.4536478332419 | 47.60130160519188 | -5.23 | 16.12 | 16.69 | 28.6 | 26.52 | 31.96 | False |  | mild_accumulation | -1.19 | 3.15 | 1 | 1 | 0.35 | 0.7 | -16.94 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 106.27092931541586 | 98.74948929988273 | -3.44 | -0.13 | 52.82 | 102.84 | 62.27 | 112.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.61 | -1.69 | 0 | 0 | -3.86 | -1.16 | -10.87 |  | fail_already_priced_in |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 62.50975349591595 | 35.380676159918806 | -9.63 | -9.07 | 46.4 | 115.93 | 56.75 | 124.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.81 | -1.42 | 1 | 0 | -6.91 | -4.98 | -20.0 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 78.6962053513493 | 92.9596666703437 | -2.6 | 3.5 | 19.57 | 84.26 | 42.64 | 109.7 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.14 | 0.41 | 2 | 2 | -1.67 | 1.16 | -8.77 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth |  | 93.60030832533867 | 16.579981523230785 | 3.61 | 17.54 | 26.15 | 19.17 | 31.09 | 38.46 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 8.14 | 7.26 | -5.78 |  | fail_low_response_condition |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 2134.025974025974 | 903.0331796401772 | 25.45 | 24.15 | 5.54 | 253.59 | 43.25 | 251.36 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 20.32 | 17.6 | -12.71 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 336.3079796617205 | 120.32617467953756 | -7.87 | -6.13 | 69.22 | 48.95 | 78.96 | 78.96 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.33 | -3.38 | 1 | 0 | -10.18 | -4.48 | -21.03 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 607.8314481446032 | 296.8515627103815 | -12.67 | 3.17 | 106.82 | 242.11 | 127.5 | 271.13 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.86 | 2.78 | 2 | 2 | 0.19 | 2.61 | -14.47 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 114.23072625004656 | 125.40997222581112 | 19.5 | 24.18 | 158.86 | 334.78 | 212.5 | 372.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.44 | 0.94 | 2 | 1 | 16.08 | 16.71 | 0.0 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 83.84991757028762 | 32.35486967199371 | -3.42 | 15.75 | 75.42 | 121.39 | 82.38 | 134.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.87 | 1.92 | 2 | 2 | -4.08 | 1.08 | -12.19 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 56.26505643863285 | 48.80373503533387 | -10.4 | 9.91 | 135.9 | 116.87 | 150.56 | 150.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.21 | 0.0 | 2 | 0 | 1.21 | -0.0 | -18.47 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 111.98927364274992 | 135.2700931903602 | 7.89 | 23.91 | 26.67 | 14.77 | 39.59 | 39.59 | False |  | strong_accumulation | 0.3 | 0.27 | 2 | 2 | 11.2 | 8.34 | -14.93 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 78.53183930035529 | 96.24488270368444 | 1.17 | 2.36 | 0.0 | -7.8 | 9.24 | 9.24 | False |  | mild_accumulation | -0.17 | 0.13 | 1 | 3 | 2.71 | 0.97 | -8.45 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 60.16717903418358 | 60.03667972061005 | -0.95 | 23.81 | 52.2 | 57.42 | 59.02 | 64.04 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 6.0 | 6.12 | 2 | 3 | 2.5 | 4.85 | -7.96 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 56.33450576009668 | 27.274509505356043 | -1.36 | 7.42 | 20.27 | 23.55 | 28.37 | 35.58 | False |  | mild_accumulation | -0.29 | 0.01 | 1 | 1 | 0.92 | 1.84 | -7.65 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 156.85087929178133 | 81.0355514911027 | -5.57 | -13.1 | 95.13 | 104.64 | 106.07 | 123.86 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.98 | -1.79 | 1 | 1 | -8.16 | -5.5 | -25.88 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 83.23758160377125 | 97.76781501517576 | 17.45 | 66.27 | 120.8 | 99.71 | 125.86 | 126.97 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.17 | 0.02 | 2 | 1 | 29.58 | 26.09 | -3.16 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 96.2350108447434 | 115.45585350897274 | 9.26 | 16.26 | 50.9 | 70.77 | 57.54 | 91.25 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.18 | 2.77 | 2 | 3 | 13.54 | 12.89 | -2.07 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 50.22139699381079 | 30.082092728365648 | 6.67 | 79.37 | 101.01 | 141.94 | 125.56 | 139.04 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.68 | 9.94 | 2 | 2 | 17.14 | 18.68 | -5.88 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 108.38868033496968 | 125.75129312187408 | -4.06 | -4.61 | -13.8 | 25.38 | 10.33 | 26.34 | False |  | mild_accumulation | 0.32 | -0.1 | 3 | 0 | -3.51 | -3.74 | -20.43 | 19 | selected |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 78.61369654620938 | 70.71720149020462 | 1.09 | -2.11 | 33.81 | 97.87 | 40.55 | 114.62 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.57 | -4.64 | 0 | 0 | 0.86 | -0.05 | -13.62 |  | fail_already_priced_in |
| 5215 | 科嘉-KY | 電腦及週邊設備業 | mainstream_growth |  | 72.73453168813967 | 40.2037645186312 | -1.22 | 7.56 | 30.63 | 35.2 | 33.7 | 43.41 | False |  | mild_accumulation | 0.45 | -0.2 | 2 | 0 | 2.83 | 4.26 | -5.47 |  | fail_low_response_condition |
| 5284 | jpp-KY | 其他 | neutral |  | 54.65432151998965 | 47.78147443327516 | -9.97 | 5.31 | 53.69 | 34.6 | 54.86 | 62.6 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.92 | 4.35 | 2 | 3 | -1.97 | -0.76 | -15.31 |  | fail_already_priced_in |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 65.52682741578477 | 51.66798309925093 | 3.34 | 15.32 | 13.71 | 6.29 | 19.63 | 19.63 | False |  | mild_accumulation | 1.28 | -0.16 | 2 | 2 | 4.92 | 4.13 | -5.19 | 19 | selected |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 743.3062171016306 | 795.9274284289337 | 4.68 | 7.94 | 11.75 | 27.26 | 12.08 | 28.55 | False |  | mild_accumulation | 0.02 | -0.14 | 1 | 2 | 5.62 | 5.03 | -0.78 | 21 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 1375.7984438680992 | 1302.5511357042951 | 7.8 | -0.87 | -6.56 | -20.14 | 11.49 | 11.49 | False |  | strong_accumulation | 0.24 | 0.05 | 3 | 3 | 4.64 | 3.09 | -14.93 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 301.60050253861493 | 128.81886706959793 | 17.01 | 42.56 | 62.93 | 80.92 | 66.24 | 88.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.73 | 1.0 | 1 | 2 | 25.9 | 23.03 | -1.1 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 70.59242292002638 | 68.32733199576585 | 3.06 | 12.22 | 41.75 | 68.33 | 57.5 | 69.21 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.05 | -1.03 | 1 | 1 | 4.35 | 5.57 | -5.28 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 116.93180458964852 | 18.057297737695265 | 3.27 | 0.0 | -15.96 | 82.66 | 17.91 | 84.58 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 0.61 | 1 | 2 | 2.56 | 2.65 | -26.34 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 63.164454428616175 | 37.58576900316765 | 0.76 | 19.28 | 121.3 | 98.21 | 134.57 | 134.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.13 | -1.19 | 2 | 0 | 5.14 | 9.87 | -8.28 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 264.8258137419728 | 633.4822945856635 | 7.19 | -0.55 | -2.26 | -5.11 | 9.39 | 9.39 | False |  | distribution_warning | -1.09 | -1.33 | 0 | 0 | 3.87 | 3.06 | -9.46 | 15 | selected |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 66.88098236522453 | 52.50809987028574 | 7.59 | 28.7 | 67.75 | 54.48 | 82.37 | 82.37 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -4.86 | -7.49 | 1 | 1 | 8.41 | 11.21 | -3.3 |  | fail_low_response_condition |
| 6215 | 和椿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 86.85261874392444 | 66.23020669829987 | -7.45 | -0.84 | 4.42 | 6.79 | 26.75 | 26.75 | False |  | strong_accumulation | 4.23 | 2.98 | 3 | 2 | -7.0 | -3.86 | -14.49 | 20 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 76.49244300662184 | 61.90792705834754 | -14.04 | -16.55 | 47.12 | 190.14 | 68.75 | 193.48 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.01 | 2.68 | 3 | 2 | -12.2 | -9.62 | -21.94 |  | fail_low_response_condition |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 68.34595682594261 | 60.268154565481694 | 0.75 | 19.82 | 44.38 | 83.73 | 62.11 | 100.64 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 2.16 | 3 | 2 | 8.14 | 9.75 | -4.19 |  | fail_already_priced_in |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 50.51274485049632 | 34.35824836559721 | -2.77 | -20.07 | 36.77 | 234.33 | 34.58 | 234.33 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.29 | -0.45 | 0 | 1 | -5.84 | -5.57 | -26.68 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 92.87778739857193 | 109.07996893571725 | -15.13 | -3.81 | 91.29 | 147.85 | 129.81 | 171.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.32 | -7.76 | 1 | 0 | -4.82 | -2.23 | -22.61 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 914.8854069223572 | 275.97151367822784 | 7.44 | 8.69 | 1.21 | -27.26 | 12.33 | 12.33 | False |  | mild_accumulation | 0.38 | -0.47 | 3 | 0 | 6.86 | 5.1 | -4.77 |  | fail_low_response_condition |
| 6657 | 華安 | 生技醫療業 | defensive_or_traditional |  | 89.90610328638498 | 34.22818791946309 | 0.26 | -2.76 | -19.12 | -9.05 | 8.71 | 8.71 | False |  | mild_accumulation | 0.67 | 0.0 | 2 | 0 | -1.2 | -2.17 | -22.05 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 66.70054461276516 | 73.74071161548827 | -1.23 | 0.78 | 4.39 | 18.23 | 15.68 | 19.11 | False |  | mild_accumulation | -0.45 | 0.16 | 1 | 1 | 0.62 | 0.08 | -7.76 |  | fail_low_response_condition |
| 6805 | 富世達 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 59.0506505428733 | 78.47048569813265 | 1.04 | 9.55 | 11.43 | 24.2 | 18.54 | 56.0 | False |  | distribution_warning | -3.95 | -6.04 | 0 | 0 | 4.53 | 1.55 | -14.29 | 13 | selected |
| 6885 | 全福生技 | 生技醫療業 | defensive_or_traditional |  | 2152.9411764705883 | 2578.358208955224 | 28.26 | 24.07 | 5.78 | -5.52 | 29.51 | 29.51 | False |  | mild_accumulation | 1.23 | -0.01 | 3 | 1 | 18.66 | 16.3 | 0.0 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 331.0770222733691 | 129.05790884244232 | 15.32 | 0.35 | -0.35 | -9.49 | 18.67 | 18.67 | False |  | distribution_warning | -0.51 | -0.61 | 0 | 0 | 6.68 | 5.87 | -8.92 |  | fail_low_response_condition |
| 6934 | 心誠鎂 | 生技醫療業 | defensive_or_traditional |  | 546.6284074605452 | -8.724233983286908 | -3.11 | -4.15 | -14.76 |  | 2.29 |  | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | -3.37 | -4.65 | -28.4 |  | fail_low_response_condition |
| 6949 | 沛爾生醫-創 | 生技醫療業 | defensive_or_traditional |  | 107.90762771168647 | -29.12783208304917 | 2.02 | -8.1 | 16.46 | 86.93 | 29.27 | 113.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.66 | 2 | 2 | -0.68 | -1.31 | -29.17 |  | fail_low_response_condition |
| 6952 | 大武山 | 其他 | neutral |  | 53.75729646697389 | 41.20225039748869 | 0.0 | -0.82 | -8.86 | -15.31 | 1.96 | 1.96 | False |  | mild_accumulation | 0.06 | 0.06 | 1 | 1 | -0.42 | -0.87 | -14.72 |  | fail_low_response_condition |
| 6957 | 裕慶-KY | 其他 | neutral |  | 53.31255357930569 | 34.466647133509134 | 14.67 | 20.44 | 16.77 | -4.73 | 25.99 | 25.99 | False |  | strong_accumulation | 0.75 | 0.02 | 2 | 2 | 13.99 | 12.11 | -3.77 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 345.323186054649 | 425.22423145865633 | 18.64 | 101.15 | 464.52 | 1483.71 | 485.28 | 1498.17 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.61 | 1.6 | 2 | 1 | 29.4 | 31.85 | -3.31 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 68.76129016183084 | 90.7375655253423 | 1.2 | 0.4 | 7.66 | -1.94 | 17.67 | 19.34 | False |  | strong_accumulation | 0.03 | 0.03 | 2 | 2 | 1.18 | 0.82 | -15.67 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 2905.180718592785 | 1476.0023495403216 | -6.76 | 2.37 | -12.21 | 6.15 | 9.87 | 25.0 | False |  | distribution_warning | -3.55 | -3.9 | 0 | 1 | -1.39 | -2.43 | -16.06 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 94.8739387573844 | 63.768704057004605 | -5.44 | -17.67 | 68.66 | 191.24 | 84.49 | 193.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.72 | -3.23 | 1 | 0 | -5.88 | -4.25 | -26.38 |  | fail_low_response_condition |
| 7765 | 中華資安 | 數位雲端 | neutral |  | 75.03168748308813 | 28.436327862661106 | 4.65 | 5.71 | 14.1 | -4.43 | 19.35 | 19.35 | False |  | distribution_warning | -1.01 | -0.02 | 0 | 0 | 3.48 | 3.73 | -4.78 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 111.83182996542342 | 89.0289902118116 | -11.92 | -3.77 | 78.53 | 145.36 | 110.87 | 149.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -0.19 | 1 | 1 | -3.45 | 0.52 | -14.06 |  | fail_low_response_condition |
| 7786 | 東方風能 | 綠能環保 | neutral |  | 52.31364457664033 | 53.1385367449244 | 5.49 | -4.58 | -12.89 | -23.78 | 10.62 | 10.62 | False |  | mild_accumulation | 0.21 | -0.38 | 1 | 1 | 5.53 | 2.5 | -15.82 |  | fail_low_response_condition |