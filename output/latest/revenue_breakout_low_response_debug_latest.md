# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-04 19:25:05 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1957 |
| standardized_revenue_rows | 1957 |
| price_rows | 575219 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 470 |
| tdcc_mild_accumulation_count | 736 |
| tdcc_distribution_warning_count | 618 |
| revenue_condition_pass | 263 |
| price_metrics_pass | 261 |
| low_response_pass | 66 |
| already_priced_in_excluded | 32 |
| overheat_pass | 34 |
| score_pass | 34 |
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
| fail_revenue_condition | 1694 |
| fail_low_response_condition | 195 |
| fail_already_priced_in | 32 |
| fail_defensive_or_traditional_excluded | 9 |
| fail_non_mainstream_score_lt_11 | 3 |
| missing_or_insufficient_price_metrics | 2 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1256 | 鮮活果汁-KY | 食品工業 | defensive_or_traditional |  | 56.2052104978021 | 55.43333917479604 | -2.68 | 4.71 | 24.22 | 44.4 | 39.86 | 50.38 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 3.71 | 4.42 | -8.47 |  | fail_low_response_condition |
| 1316 | 上曜 | 建材營造 | neutral | B_可觀察 | 115.49336601749948 | 135.29308413677992 | 5.45 | -4.48 | -16.8 | -29.7 | 6.5 | 6.5 | False |  | mild_accumulation | 0.06 | 0.32 | 2 | 1 | 2.16 | 0.61 | -19.32 | 17 | selected |
| 1533 | 車王電 | 汽車工業 | neutral |  | 72.76557971014493 | 65.36186986942351 | -1.16 | 13.82 | 25.37 | 21.59 | 32.07 | 32.07 | False |  | distribution_warning | -0.06 | -0.03 | 0 | 0 | 0.74 | 2.43 | -8.37 |  | fail_low_response_condition |
| 1597 | 直得 | 電機機械 | cyclical_turnaround |  | 70.9672402492807 | 42.206256661754686 | -4.17 | -8.73 | 128.17 | 135.01 | 127.57 | 155.56 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.98 | -6.8 | 1 | 0 | -5.36 | -1.07 | -21.95 |  | fail_already_priced_in |
| 1714 | 和桐 | 化學工業 | cyclical_turnaround |  | 71.71403036691967 | 47.62349772985901 | 27.37 | 22.35 | 31.09 | 47.38 | 34.15 | 52.01 | False |  | mild_accumulation | 0.91 | 1.26 | 1 | 1 | 22.89 | 21.62 | 0.0 |  | fail_low_response_condition |
| 1762 | 中化生 | 生技醫療業 | defensive_or_traditional |  | 75.98113638501123 | 84.08413462437495 | 4.23 | 7.25 | 42.31 | 63.13 | 48.54 | 68.18 | True | 近60日漲幅>40% | strong_accumulation | 0.2 | 0.19 | 2 | 2 | 5.58 | 8.14 | -0.37 |  | fail_low_response_condition |
| 1808 | 潤隆 | 建材營造 | neutral | B_可觀察 | 6493.744863214747 | 11655.629597709994 | 7.46 | 9.69 | 0.96 | -2.76 | 13.01 | 13.01 | False |  | strong_accumulation | 0.46 | 0.18 | 3 | 2 | 8.35 | 7.61 | -1.71 | 21 | selected |
| 2022 | 聚亨 | 鋼鐵工業 | cyclical_turnaround | B_可觀察 | 58.72797685088429 | 58.303086049163085 | 5.21 | -2.42 | -10.72 | -3.12 | 8.02 | 8.02 | False |  | strong_accumulation | 0.24 | 0.4 | 2 | 3 | 4.51 | 2.51 | -18.79 | 17 | selected |
| 2025 | 千興 | 鋼鐵工業 | cyclical_turnaround |  | 112.02365239427697 | 101.64282906158348 | 2.52 | -5.43 | 15.09 | 26.03 | 17.31 | 32.46 | False |  | mild_accumulation | 0.74 | 0.78 | 1 | 1 | 1.37 | 1.79 | -9.29 |  | fail_low_response_condition |
| 2059 | 川湖 | 電子零組件業 | mainstream_growth |  | 79.13810010482361 | 48.90681620491181 | 5.63 | 1.9 | 58.99 | 54.62 | 69.84 | 86.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.09 | -0.39 | 2 | 1 | 7.46 | 8.61 | -4.72 |  | fail_low_response_condition |
| 2072 | 世紀風電 | 綠能環保 | neutral |  | 78.33000624034136 | 50.54423965195399 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 2101 | 南港 | 橡膠工業 | cyclical_turnaround | B_可觀察 | 150.64504386931364 | 158.89980066771645 | 7.99 | 0.0 | 1.72 | -15.6 | 10.0 | 10.0 | False |  | mild_accumulation | 0.04 | -0.13 | 2 | 2 | 5.06 | 2.65 | -15.38 | 19 | selected |
| 2208 | 台船 | 航運業 | cyclical_turnaround | D_降級_TDCC轉弱 | 132.18748539427372 | 40.98484977823417 | 2.25 | -9.02 | -15.58 | -13.57 | 2.54 | 2.54 | False |  | distribution_warning | -1.1 | -1.51 | 0 | 0 | -1.01 | -2.4 | -19.33 | 13 | selected |
| 2241 | 艾姆勒 | 汽車工業 | neutral | B_可觀察 | 65.61372467388287 | 34.04444901386247 | -6.8 | -3.3 | 11.42 | -17.65 | 19.26 | 19.26 | False |  | strong_accumulation | 5.87 | 1.78 | 2 | 2 | -8.3 | -5.42 | -19.4 | 15 | selected |
| 2248 | 華勝-KY | 汽車工業 | neutral |  | 58.99419597132127 | 37.279628771534725 | 4.72 | 6.26 | 18.36 | 15.98 | 19.96 | 25.16 | False |  | distribution_warning | -0.8 | 0.0 | 0 | 0 | 4.86 | 4.47 | -7.09 |  | fail_low_response_condition |
| 2305 | 全友 | 電腦及週邊設備業 | mainstream_growth |  | 81.07437391238557 | 58.26494269000799 | -5.25 | 34.23 | 56.6 | 116.83 | 62.82 | 116.83 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.21 | 0.18 | 2 | 2 | 10.57 | 8.51 | -9.8 |  | fail_low_response_condition |
| 2314 | 台揚 | 通信網路業 | mainstream_growth |  | 89.93139019999026 | 64.86611212397447 | 6.69 | 28.35 | 0.0 | -30.64 | 48.23 | 48.23 | True | 近20日漲幅>25% | distribution_warning | -2.49 | -4.0 | 1 | 0 | 9.69 | 7.96 | -24.55 |  | fail_low_response_condition |
| 2316 | 楠梓電 | 電子零組件業 | mainstream_growth |  | 74.29425507406266 | 29.66893190701796 | -5.04 | 12.28 | 75.05 | 53.85 | 72.79 | 88.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.83 | -2.37 | 2 | 1 | 2.78 | 4.56 | -14.89 |  | fail_already_priced_in |
| 2337 | 旺宏 | 半導體業 | mainstream_growth |  | 153.71283899759698 | 93.45563776655904 | -6.01 | -6.85 | 44.24 | 361.65 | 35.5 | 358.94 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.28 | -2.49 | 1 | 1 | -0.81 | -1.15 | -13.06 |  | fail_already_priced_in |
| 2344 | 華邦電 | 半導體業 | mainstream_growth |  | 182.2232686329836 | 114.45152253341396 | 13.61 | 47.13 | 64.68 | 190.45 | 114.2 | 182.68 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.7 | 5.52 | 2 | 2 | 25.17 | 24.23 | -6.99 |  | fail_low_response_condition |
| 2345 | 智邦 | 通信網路業 | mainstream_growth |  | 53.86862868005451 | 61.04008779861957 | 3.29 | 3.08 | 76.76 | 153.54 | 81.88 | 156.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.5 | -0.11 | 1 | 2 | 0.71 | 2.57 | -6.86 |  | fail_already_priced_in |
| 2347 | 聯強 | 電子通路業 | mainstream_growth | A_優先追蹤 | 83.27774880652615 | 49.7322802816284 | 4.66 | 8.18 | 28.06 | 47.62 | 25.91 | 56.89 | False |  | strong_accumulation | 0.2 | 0.05 | 2 | 2 | 5.31 | 4.76 | -4.36 | 22 | selected |
| 2353 | 宏碁 | 電腦及週邊設備業 | mainstream_growth |  | 68.39241034251229 | 29.65214150981726 | 11.08 | 38.16 | 42.96 | 44.55 | 46.44 | 56.4 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 1.48 | 1.55 | 3 | 3 | 19.85 | 16.05 | -11.54 |  | fail_low_response_condition |
| 2360 | 致茂 | 其他電子業 | mainstream_growth |  | 128.89343838145112 | 86.02762799824309 | 3.97 | 8.94 | 71.24 | 229.15 | 81.31 | 259.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.55 | 1.24 | 3 | 3 | 9.7 | 9.36 | -6.26 |  | fail_already_priced_in |
| 2363 | 矽統 | 半導體業 | mainstream_growth | A_優先追蹤 | 87.15138632062427 | 113.29446010652936 | -5.68 | 5.34 | 24.7 | 27.35 | 36.58 | 38.23 | False |  | strong_accumulation | 3.53 | 4.42 | 2 | 3 | -2.91 | -1.1 | -12.36 | 19 | selected |
| 2368 | 金像電 | 電子零組件業 | mainstream_growth |  | 58.40832442393109 | 60.83836546918864 | 2.27 | 0.0 | 44.39 | 126.51 | 58.08 | 133.97 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 1.08 | 1 | 3 | 1.47 | 1.7 | -11.18 |  | fail_already_priced_in |
| 2374 | 佳能 | 光電業 | mainstream_growth | A_優先追蹤 | 62.53280267892302 | 73.20495684221454 | -2.76 | 1.25 | 14.59 | -0.74 | 22.21 | 24.65 | False |  | mild_accumulation | 1.68 | 1.2 | 3 | 1 | -1.28 | -0.3 | -6.37 | 18 | selected |
| 2376 | 技嘉 | 電腦及週邊設備業 | mainstream_growth |  | 73.65790531628242 | 64.15425901107987 | 1.08 | 19.3 | 60.52 | 53.28 | 68.85 | 81.11 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 0.58 | 0.18 | 2 | 2 | 8.75 | 8.58 | -6.97 |  | fail_already_priced_in |
| 2382 | 廣達 | 電腦及週邊設備業 | mainstream_growth |  | 120.71254202479236 | 79.6425126685901 | 19.17 | 18.65 | 39.79 | 35.8 | 46.64 | 55.38 | False |  | distribution_warning | -1.24 | -1.39 | 1 | 0 | 21.67 | 17.41 | -7.76 |  | fail_low_response_condition |
| 2383 | 台光電 | 電子零組件業 | mainstream_growth |  | 93.61728577894678 | 62.73574575073765 | -5.66 | -2.03 | 78.56 | 223.08 | 87.57 | 229.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.25 | 0.07 | 1 | 1 | -2.25 | -0.7 | -14.29 |  | fail_already_priced_in |
| 2388 | 威盛 | 半導體業 | mainstream_growth |  | 84.78597634196018 | 22.360190669372724 | -4.68 | -2.01 | 51.92 | 41.51 | 53.03 | 71.26 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.23 | -0.41 | 1 | 1 | -6.81 | -4.1 | -19.72 |  | fail_already_priced_in |
| 2404 | 漢唐 | 其他電子業 | mainstream_growth | A_優先追蹤 | 102.22569068277646 | 82.88490710977096 | 6.49 | 20.0 | 21.78 | 55.11 | 49.82 | 54.52 | False |  | strong_accumulation | 5.25 | 3.89 | 3 | 3 | 8.11 | 9.04 | -8.55 | 21 | selected |
| 2406 | 國碩 | 光電業 | mainstream_growth |  | 143.2900222907499 | 161.27555347120483 | 11.43 | 16.49 | 13.4 | 64.88 | 36.77 | 73.03 | False |  | distribution_warning | -0.58 | -0.14 | 1 | 2 | 14.81 | 12.33 | -7.89 |  | fail_low_response_condition |
| 2408 | 南亞科 | 半導體業 | mainstream_growth |  | 717.3347932872048 | 623.5846473576565 | 13.83 | 23.05 | 65.97 | 158.17 | 98.99 | 155.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.19 | 0.07 | 2 | 2 | 19.6 | 19.2 | -8.25 |  | fail_low_response_condition |
| 2424 | 隴華 | 通信網路業 | mainstream_growth |  | 150.7809903622466 | -26.41191544789116 | 6.8 | -47.75 | -55.72 | -58.54 | 8.98 | 8.98 | False |  | distribution_warning | -0.88 | -2.35 | 0 | 0 | -13.02 | -14.45 | -56.23 |  | fail_low_response_condition |
| 2425 | 承啟 | 電腦及週邊設備業 | mainstream_growth |  | 87.78233369635424 | 75.58506270870245 | 0.42 | 6.4 | 16.64 | 25.44 | 37.5 | 42.43 | False |  | strong_accumulation | 0.94 | 0.63 | 2 | 2 | 2.11 | 3.32 | -4.79 |  | fail_low_response_condition |
| 2432 | 倚天酷碁-創 | 電腦及週邊設備業 | mainstream_growth |  | 130.07770836507694 | 45.61010923954572 | 5.86 | 5.66 | -1.06 | 4.67 | 11.11 | 20.95 | False |  | mild_accumulation | 0.07 | 0.0 | 3 | 0 | 5.61 | 3.99 | -6.98 |  | fail_low_response_condition |
| 2442 | 新美齊 | 建材營造 | neutral | B_可觀察 | 168.44142686485915 | 550.3124746524734 | 5.09 | 7.1 | -0.51 | -22.83 | 9.5 | 9.5 | False |  | mild_accumulation | -0.74 | 0.18 | 1 | 1 | 5.21 | 4.23 | -11.11 | 20 | selected |
| 2451 | 創見 | 半導體業 | mainstream_growth |  | 594.4309428523752 | 419.72339242497657 | 5.62 | 9.17 | 51.27 | 102.27 | 71.22 | 112.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.76 | -1.84 | 2 | 1 | 8.04 | 8.99 | -6.79 |  | fail_already_priced_in |
| 2460 | 建通 | 電子零組件業 | mainstream_growth |  | 57.62140485913217 | 60.96249952274371 | 3.4 | -4.96 | 41.05 | 83.56 | 42.55 | 88.2 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.36 | 2 | 1 | 2.78 | 1.34 | -18.69 |  | fail_already_priced_in |
| 2465 | 麗臺 | 電腦及週邊設備業 | mainstream_growth |  | 175.797836656721 | 114.62777854736004 | 2.9 | 2.53 | 55.47 | 53.24 | 68.71 | 77.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 2.2 | 1.5 | 2 | 1 | 2.45 | 3.33 | -9.17 |  | fail_already_priced_in |
| 2467 | 志聖 | 電子零組件業 | mainstream_growth |  | 86.98160791241624 | 76.55198946300291 | 1.13 | 0.0 | 72.21 | 203.88 | 80.4 | 198.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.57 | -0.47 | 2 | 2 | 2.26 | 3.47 | -9.54 |  | fail_already_priced_in |
| 2506 | 太設 | 建材營造 | neutral |  | 182.9282692118469 | 24.4950641596528 | 2.77 | 3.37 | -0.34 | -6.52 | 5.71 | 5.71 | False |  | strong_accumulation | 0.38 | 0.1 | 3 | 3 | 2.45 | 1.91 | -2.2 |  | fail_low_response_condition |
| 2537 | 聯上發 | 建材營造 | neutral | B_可觀察 | 5302.611940298508 | 306.8870026872911 | 6.35 | 0.5 | -0.5 | -4.74 | 7.14 | 7.14 | False |  | strong_accumulation | 1.2 | 1.2 | 2 | 2 | 3.74 | 2.27 | -8.22 | 24 | selected |
| 2542 | 興富發 | 建材營造 | neutral | B_可觀察 | 4077.658799321493 | 1725.2218547108523 | 2.74 | 0.94 | 17.92 | 13.42 | 27.89 | 27.89 | False |  | strong_accumulation | 1.04 | 0.94 | 2 | 3 | 0.34 | 2.43 | -3.79 | 22 | selected |
| 2543 | 皇昌 | 建材營造 | neutral | D_降級_TDCC轉弱 | 62.14864030788222 | 31.766695479206813 | 0.44 | 9.76 | -37.28 | -23.55 | 24.43 | 24.43 | False |  | distribution_warning | -1.41 | -1.81 | 0 | 0 | 6.25 | 2.2 | -38.2 | 11 | selected |
| 2545 | 皇翔 | 建材營造 | neutral |  | 102.09031492521602 | 53.11675313058128 | 4.96 | -0.91 | 4.24 | -0.13 | 7.48 | 7.48 | False |  | mild_accumulation | -0.06 | 0.24 | 2 | 1 | 2.97 | 2.52 | -2.56 |  | fail_low_response_condition |
| 2548 | 華固 | 建材營造 | neutral |  | 28465.962511157395 | 34773.574080324 | -16.49 | -19.84 | -14.33 | -4.5 | 0.3 | 0.3 | False |  | distribution_warning | -0.97 | -0.36 | 0 | 1 | -16.58 | -15.38 | -24.68 |  | fail_low_response_condition |
| 2611 | 志信 | 航運業 | cyclical_turnaround |  | 119.47429042961028 | 112.7116208532482 | 6.92 | 4.91 | -6.4 | -8.55 | 10.32 | 10.32 | False |  | strong_accumulation | 0.45 | 0.74 | 2 | 2 | 6.05 | 4.2 | -9.45 |  | fail_low_response_condition |
| 2816 | 旺旺保 | 金融保險業 | defensive_or_traditional |  | 78.73621403925392 | 29.40789362443229 | 5.21 | 8.89 | 14.52 | 14.72 | 14.52 | 21.85 | False |  | strong_accumulation | 0.45 | 0.05 | 2 | 3 | 7.21 | 6.53 | -4.59 |  | fail_low_response_condition |
| 2850 | 新產 | 金融保險業 | defensive_or_traditional |  | 64.58201026377658 | 21.61586465449111 | -0.34 | 9.02 | 20.83 | 24.46 | 26.09 | 30.63 | False |  | mild_accumulation | 0.44 | -0.36 | 3 | 1 | 4.02 | 4.48 | -1.36 |  | fail_low_response_condition |
| 2855 | 統一證 | 金融保險業 | defensive_or_traditional |  | 1002.1406834015808 | 365.76888748391855 | 16.84 | 33.25 | 83.47 | 126.53 | 83.47 | 133.19 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.61 | -0.49 | 0 | 0 | 25.32 | 23.6 | -4.64 |  | fail_low_response_condition |
| 2880 | 華南金 | 金融保險業 | defensive_or_traditional |  | 59.58077358578821 | 30.53659326449297 | 23.61 | 15.11 | 11.37 | 22.4 | 27.36 | 27.36 | False |  | distribution_warning | -0.4 | -0.34 | 0 | 1 | 17.49 | 15.14 | -2.33 |  | fail_low_response_condition |
| 2881 | 富邦金 | 金融保險業 | defensive_or_traditional |  | 219.78523407605732 | 402.5871994932322 | 3.64 | 20.38 | 29.4 | 20.13 | 33.65 | 36.53 | False |  | strong_accumulation | 0.8 | 0.82 | 3 | 3 | 10.55 | 9.75 | -1.72 |  | fail_low_response_condition |
| 2882 | 國泰金 | 金融保險業 | defensive_or_traditional |  | 153.9148431130897 | 577.0666572623264 | 10.15 | 22.12 | 31.66 | 37.41 | 36.61 | 40.27 | False |  | strong_accumulation | 0.18 | 0.24 | 2 | 2 | 13.71 | 12.6 | -1.97 |  | fail_low_response_condition |
| 2883 | 凱基金 | 金融保險業 | defensive_or_traditional |  | 144.30631310157813 | 319.6219559348892 | 21.78 | 24.83 | 36.32 | 70.72 | 42.71 | 71.25 | True | 近120日漲幅>70% | strong_accumulation | 0.03 | 0.04 | 2 | 2 | 21.95 | 20.31 | -2.66 |  | fail_low_response_condition |
| 2885 | 元大金 | 金融保險業 | defensive_or_traditional |  | 324.89668645555184 | 112.85581098417563 | 7.21 | 14.52 | 47.58 | 69.27 | 48.95 | 72.47 | True | 近60日漲幅>40% | distribution_warning | -0.07 | -0.02 | 1 | 1 | 10.98 | 10.57 | -1.99 |  | fail_low_response_condition |
| 2890 | 永豐金 | 金融保險業 | defensive_or_traditional |  | 87.36017222905045 | 50.078518078805 | 10.5 | 8.51 | 4.41 | 20.55 | 15.71 | 22.1 | False |  | distribution_warning | -0.67 | -0.65 | 0 | 0 | 9.98 | 8.14 | -1.49 |  | fail_low_response_condition |
| 2891 | 中信金 | 金融保險業 | defensive_or_traditional |  | 1120.5725622466316 | 81.69612153552563 | 12.4 | 23.86 | 32.55 | 52.64 | 34.92 | 53.5 | False |  | strong_accumulation | 0.3 | 0.4 | 2 | 2 | 14.53 | 13.41 | -3.55 |  | fail_low_response_condition |
| 2905 | 三商 | 貿易百貨 | defensive_or_traditional |  | 352.9548403037368 | 50.7749326018759 | 4.74 | 7.49 | -8.31 | -15.09 | 9.96 | 9.96 | False |  | mild_accumulation | -0.01 | 0.07 | 0 | 2 | 5.42 | 4.2 | -7.42 |  | fail_low_response_condition |
| 2923 | 鼎固-KY | 建材營造 | neutral |  | 160.8459070607583 | 155.54497022876842 | 1.17 | 6.8 | 41.53 | 19.08 | 51.91 | 51.91 | True | 近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.05 | 0.0 | 0 | 0 | 11.33 | 7.29 | -13.23 |  | fail_low_response_condition |
| 3006 | 晶豪科 | 半導體業 | mainstream_growth |  | 349.21497789414195 | 202.476438292242 | -0.61 | 13.16 | 52.17 | 206.25 | 66.67 | 216.54 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.82 | 1.61 | 2 | 2 | 1.25 | 4.49 | -10.42 |  | fail_already_priced_in |
| 3017 | 奇鋐 | 電腦及週邊設備業 | mainstream_growth |  | 71.62015931637609 | 99.34392209738031 | 1.69 | 4.84 | 45.31 | 95.67 | 48.09 | 114.23 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.27 | -0.58 | 0 | 1 | 4.42 | 3.2 | -9.97 |  | fail_already_priced_in |
| 3025 | 星通 | 通信網路業 | mainstream_growth |  | 76.4536478332419 | 47.60130160519188 | -5.91 | 13.43 | 13.43 | 29.57 | 25.63 | 31.03 | False |  | mild_accumulation | -1.19 | 3.15 | 1 | 1 | 0.34 | 0.05 | -17.53 |  | fail_low_response_condition |
| 3028 | 增你強 | 電子通路業 | mainstream_growth |  | 106.27092931541586 | 98.74948929988273 | 2.7 | 14.19 | 65.42 | 128.38 | 72.58 | 127.76 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.61 | -1.69 | 0 | 0 | 2.24 | 5.01 | -5.21 |  | fail_already_priced_in |
| 3030 | 德律 | 其他電子業 | mainstream_growth |  | 62.50975349591595 | 35.380676159918806 | -9.88 | -11.84 | 31.53 | 117.91 | 56.32 | 123.93 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.81 | -1.42 | 1 | 0 | -7.59 | -5.66 | -20.22 |  | fail_already_priced_in |
| 3036 | 文曄 | 電子通路業 | mainstream_growth |  | 78.6962053513493 | 92.9596666703437 | -2.25 | -0.7 | 19.75 | 89.9 | 43.15 | 110.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.14 | 0.41 | 2 | 2 | -1.16 | 1.63 | -8.44 |  | fail_already_priced_in |
| 3046 | 建碁 | 電腦及週邊設備業 | mainstream_growth | A_優先追蹤 | 93.60030832533867 | 16.579981523230785 | 3.26 | 16.7 | 26.66 | 19.48 | 30.65 | 38.0 | False |  | mild_accumulation | 0.52 | 0.0 | 2 | 0 | 8.66 | 7.62 | -6.09 | 19 | selected |
| 3054 | 立萬利 | 食品工業 | defensive_or_traditional |  | 2134.025974025974 | 903.0331796401772 | 25.15 | 23.3 | 15.79 | 254.24 | 42.91 | 255.74 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 21.46 | 19.22 | -12.92 |  | fail_low_response_condition |
| 3055 | 蔚華科 | 電子通路業 | mainstream_growth |  | 336.3079796617205 | 120.32617467953756 | -4.17 | -8.81 | 79.38 | 58.26 | 86.15 | 86.15 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.33 | -3.38 | 1 | 0 | -6.84 | -1.04 | -17.86 |  | fail_already_priced_in |
| 3135 | 凌航 | 半導體業 | mainstream_growth |  | 607.8314481446032 | 296.8515627103815 | -7.68 | 13.98 | 118.64 | 257.36 | 140.5 | 292.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.86 | 2.78 | 2 | 2 | 6.08 | 8.74 | -9.59 |  | fail_already_priced_in |
| 3167 | 大量 | 電機機械 | cyclical_turnaround |  | 114.23072625004656 | 125.40997222581112 | 13.33 | 19.65 | 130.73 | 307.69 | 196.38 | 348.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.44 | 0.94 | 2 | 1 | 11.35 | 12.4 | -5.16 |  | fail_low_response_condition |
| 3209 | 全科 | 電子通路業 | mainstream_growth |  | 83.84991757028762 | 32.35486967199371 | 1.18 | 22.81 | 93.22 | 130.19 | 91.07 | 145.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.87 | 1.92 | 2 | 2 | 1.15 | 6.0 | -8.0 |  | fail_already_priced_in |
| 3229 | 晟鈦 | 電子零組件業 | mainstream_growth |  | 56.26505643863285 | 48.80373503533387 | -6.06 | 3.79 | 146.68 | 148.0 | 162.71 | 162.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.21 | 0.0 | 2 | 0 | 6.6 | 4.84 | -14.52 |  | fail_low_response_condition |
| 3231 | 緯創 | 電腦及週邊設備業 | mainstream_growth |  | 111.98927364274992 | 135.2700931903602 | 11.04 | 25.27 | 31.34 | 16.56 | 43.67 | 43.67 | True | 近20日漲幅>25% | strong_accumulation | 0.3 | 0.27 | 2 | 2 | 15.69 | 12.36 | -12.44 |  | fail_low_response_condition |
| 3266 | 昇陽 | 建材營造 | neutral |  | 78.53183930035529 | 96.24488270368444 | -0.78 | -2.67 | -2.67 | -9.57 | 7.14 | 7.14 | False |  | mild_accumulation | -0.17 | 0.13 | 1 | 3 | 0.85 | -0.89 | -10.21 |  | fail_low_response_condition |
| 3305 | 昇貿 | 其他電子業 | mainstream_growth |  | 60.16717903418358 | 60.03667972061005 | 1.59 | 22.61 | 56.86 | 63.27 | 63.1 | 68.24 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 6.0 | 6.12 | 2 | 3 | 6.17 | 8.01 | -5.6 |  | fail_already_priced_in |
| 3416 | 融程電 | 電腦及週邊設備業 | mainstream_growth |  | 56.33450576009668 | 27.274509505356043 | -1.91 | 7.78 | 21.62 | 22.87 | 27.66 | 34.83 | False |  | mild_accumulation | -0.29 | 0.01 | 1 | 1 | 0.71 | 1.45 | -8.16 |  | fail_low_response_condition |
| 3443 | 創意 | 半導體業 | mainstream_growth |  | 156.85087929178133 | 81.0355514911027 | -5.78 | -17.45 | 92.56 | 98.2 | 105.61 | 123.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.98 | -1.79 | 1 | 1 | -9.0 | -6.18 | -26.05 |  | fail_already_priced_in |
| 3528 | 安馳 | 電子通路業 | mainstream_growth |  | 83.23758160377125 | 97.76781501517576 | 19.15 | 71.36 | 125.44 | 100.0 | 129.13 | 130.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 4.17 | 0.02 | 2 | 1 | 34.94 | 31.02 | -1.75 |  | fail_low_response_condition |
| 4739 | 康普 | 化學工業 | cyclical_turnaround |  | 96.2350108447434 | 115.45585350897274 | 9.72 | 17.33 | 52.12 | 73.75 | 58.21 | 92.06 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.18 | 2.77 | 2 | 3 | 14.93 | 14.71 | -1.25 |  | fail_low_response_condition |
| 4916 | 事欣科 | 電腦及週邊設備業 | mainstream_growth |  | 50.22139699381079 | 30.082092728365648 | 8.89 | 87.88 | 101.81 | 156.54 | 130.26 | 155.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.68 | 9.94 | 2 | 2 | 22.76 | 23.25 | -3.92 |  | fail_low_response_condition |
| 4934 | 太極 | 光電業 | mainstream_growth | A_優先追蹤 | 108.38868033496968 | 125.75129312187408 | -0.87 | -3.93 | -8.31 | 31.54 | 14.0 | 33.59 | False |  | mild_accumulation | 0.32 | -0.1 | 3 | 0 | -0.54 | -0.87 | -17.79 | 19 | selected |
| 4967 | 十銓 | 半導體業 | mainstream_growth |  | 78.61369654620938 | 70.71720149020462 | 9.42 | 5.78 | 53.3 | 127.92 | 52.14 | 132.31 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.57 | -4.64 | 0 | 0 | 9.05 | 8.18 | -6.5 |  | fail_low_response_condition |
| 5215 | 科嘉-KY | 電腦及週邊設備業 | mainstream_growth |  | 72.73453168813967 | 40.2037645186312 | -0.51 | 5.29 | 31.4 | 35.79 | 34.67 | 44.44 | False |  | mild_accumulation | 0.45 | -0.2 | 2 | 0 | 3.95 | 5.42 | -4.79 |  | fail_low_response_condition |
| 5284 | jpp-KY | 其他 | neutral |  | 54.65432151998965 | 47.78147443327516 | -7.75 | 5.71 | 55.12 | 28.55 | 58.67 | 66.6 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.92 | 4.35 | 2 | 3 | 0.69 | 1.61 | -13.23 |  | fail_low_response_condition |
| 5388 | 中磊 | 通信網路業 | mainstream_growth | A_優先追蹤 | 65.52682741578477 | 51.66798309925093 | 2.54 | 11.96 | 13.97 | 6.47 | 18.69 | 18.69 | False |  | mild_accumulation | 1.28 | -0.16 | 2 | 2 | 4.83 | 3.71 | -5.93 | 19 | selected |
| 5522 | 遠雄 | 建材營造 | neutral | B_可觀察 | 743.3062171016306 | 795.9274284289337 | 2.34 | 5.68 | 11.21 | 25.89 | 11.21 | 25.89 | False |  | mild_accumulation | 0.02 | -0.14 | 1 | 2 | 3.66 | 3.16 | -3.0 | 21 | selected |
| 5525 | 順天 | 建材營造 | neutral |  | 1375.7984438680992 | 1302.5511357042951 | 4.73 | -3.7 | -9.78 | -22.28 | 8.31 | 8.31 | False |  | strong_accumulation | 0.24 | 0.05 | 3 | 3 | 1.61 | 0.43 | -17.35 |  | fail_low_response_condition |
| 6005 | 群益證 | 金融保險業 | defensive_or_traditional |  | 301.60050253861493 | 128.81886706959793 | 10.26 | 32.66 | 52.7 | 70.48 | 56.64 | 77.99 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | mild_accumulation | 0.73 | 1.0 | 1 | 2 | 20.91 | 18.41 | -6.39 |  | fail_low_response_condition |
| 6139 | 亞翔 | 其他電子業 | mainstream_growth |  | 70.59242292002638 | 68.32733199576585 | 5.23 | 20.26 | 57.44 | 77.04 | 60.82 | 75.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -0.05 | -1.03 | 1 | 1 | 7.15 | 8.34 | -3.28 |  | fail_already_priced_in |
| 6152 | 百一 | 通信網路業 | mainstream_growth |  | 116.93180458964852 | 18.057297737695265 | -0.33 | -1.61 | -20.16 | 78.99 | 13.81 | 82.85 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.52 | 0.61 | 1 | 2 | -1.01 | -0.69 | -28.9 |  | fail_already_priced_in |
| 6166 | 凌華 | 電腦及週邊設備業 | mainstream_growth |  | 63.164454428616175 | 37.58576900316765 | -1.89 | 16.14 | 116.56 | 97.41 | 128.4 | 128.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.13 | -1.19 | 2 | 0 | 3.25 | 7.95 | -10.69 |  | fail_already_priced_in |
| 6177 | 達麗 | 建材營造 | neutral | D_降級_TDCC轉弱 | 264.8258137419728 | 633.4822945856635 | 5.31 | -4.08 | -2.72 | -7.56 | 7.46 | 7.46 | False |  | distribution_warning | -1.09 | -1.33 | 0 | 0 | 2.01 | 1.53 | -11.06 | 15 | selected |
| 6209 | 今國光 | 光電業 | mainstream_growth |  | 66.88098236522453 | 52.50809987028574 | 3.67 | 36.39 | 64.47 | 50.44 | 75.73 | 75.73 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -4.86 | -7.49 | 1 | 1 | 5.74 | 8.26 | -6.82 |  | fail_already_priced_in |
| 6215 | 和椿 | 其他電子業 | mainstream_growth | A_優先追蹤 | 86.85261874392444 | 66.23020669829987 | -8.24 | -2.9 | 4.93 | 3.08 | 25.67 | 25.67 | False |  | strong_accumulation | 4.23 | 2.98 | 3 | 2 | -7.82 | -5.01 | -15.22 | 19 | selected |
| 6426 | 統新 | 通信網路業 | mainstream_growth |  | 76.49244300662184 | 61.90792705834754 | -9.18 | -12.14 | 70.77 | 212.5 | 78.31 | 213.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.01 | 2.68 | 3 | 2 | -8.02 | -5.32 | -17.52 |  | fail_already_priced_in |
| 6446 | 藥華藥 | 生技醫療業 | defensive_or_traditional |  | 68.34595682594261 | 60.268154565481694 | 0.86 | 19.95 | 42.77 | 82.85 | 62.28 | 100.86 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.58 | 2.16 | 3 | 2 | 9.23 | 10.85 | -4.09 |  | fail_low_response_condition |
| 6515 | 穎崴 | 半導體業 | mainstream_growth |  | 50.51274485049632 | 34.35824836559721 | -0.17 | -12.41 | 37.63 | 237.89 | 43.09 | 243.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.29 | -0.45 | 0 | 1 | -4.45 | -3.54 | -24.72 |  | fail_low_response_condition |
| 6531 | 愛普* | 半導體業 | mainstream_growth |  | 92.87778739857193 | 109.07996893571725 | -11.34 | 1.44 | 98.68 | 166.08 | 140.05 | 183.22 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.32 | -7.76 | 1 | 0 | -0.77 | 1.92 | -19.16 |  | fail_already_priced_in |
| 6541 | 泰福-KY | 生技醫療業 | defensive_or_traditional |  | 914.8854069223572 | 275.97151367822784 | 5.51 | 0.73 | -2.14 | -27.17 | 10.32 | 10.32 | False |  | mild_accumulation | 0.38 | -0.47 | 3 | 0 | 5.4 | 3.7 | -6.48 |  | fail_low_response_condition |
| 6657 | 華安 | 生技醫療業 | defensive_or_traditional |  | 89.90610328638498 | 34.22818791946309 | 2.46 | -1.49 | -17.52 | -10.62 | 11.1 | 11.1 | False |  | mild_accumulation | 0.67 | 0.0 | 2 | 0 | 0.83 | -0.21 | -20.34 |  | fail_low_response_condition |
| 6691 | 洋基工程 | 其他電子業 | mainstream_growth |  | 66.70054461276516 | 73.74071161548827 | -2.31 | 0.47 | 2.75 | 28.41 | 14.41 | 26.49 | False |  | mild_accumulation | -0.45 | 0.16 | 1 | 1 | -0.44 | -1.0 | -8.76 |  | fail_low_response_condition |
| 6805 | 富世達 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 59.0506505428733 | 78.47048569813265 | 2.85 | 8.47 | 13.11 | 28.06 | 20.67 | 58.8 | False |  | distribution_warning | -3.95 | -6.04 | 0 | 0 | 6.89 | 3.52 | -12.75 | 13 | selected |
| 6885 | 全福生技 | 生技醫療業 | defensive_or_traditional |  | 2152.9411764705883 | 2578.358208955224 | 16.67 | 11.29 | -3.01 | -14.81 | 17.8 | 17.8 | False |  | mild_accumulation | 1.23 | -0.01 | 3 | 1 | 9.19 | 7.38 | -8.17 |  | fail_low_response_condition |
| 6901 | 鑽石投資 | 其他 | neutral |  | 331.0770222733691 | 129.05790884244232 | 16.94 | -1.69 | -2.68 | -13.17 | 20.33 | 20.33 | False |  | distribution_warning | -0.51 | -0.61 | 0 | 0 | 8.19 | 7.92 | -7.64 |  | fail_low_response_condition |
| 6934 | 心誠鎂 | 生技醫療業 | defensive_or_traditional |  | 546.6284074605452 | -8.724233983286908 | -0.68 | -3.42 | -7.44 |  | 4.86 |  | False |  | mild_accumulation | 0.25 | 0.0 | 2 | 0 | -1.15 | -2.67 | -26.6 |  | fail_low_response_condition |
| 6949 | 沛爾生醫-創 | 生技醫療業 | defensive_or_traditional |  | 107.90762771168647 | -29.12783208304917 | 0.0 | -4.87 | 12.37 | 75.75 | 26.72 | 109.08 | True | 近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.38 | 1.66 | 2 | 2 | -3.07 | -3.38 | -30.57 |  | fail_low_response_condition |
| 6952 | 大武山 | 其他 | neutral |  | 53.75729646697389 | 41.20225039748869 | -0.96 | -2.56 | -9.63 | -15.64 | 0.98 | 0.98 | False |  | mild_accumulation | 0.06 | 0.06 | 1 | 1 | -1.42 | -1.9 | -15.54 |  | fail_low_response_condition |
| 6957 | 裕慶-KY | 其他 | neutral |  | 53.31255357930569 | 34.466647133509134 | 16.17 | 22.01 | 17.58 | -8.49 | 27.63 | 27.63 | False |  | strong_accumulation | 0.75 | 0.02 | 2 | 2 | 16.6 | 14.83 | -2.51 |  | fail_low_response_condition |
| 7610 | 聯友金屬-創 | 綠能環保 | neutral |  | 345.323186054649 | 425.22423145865633 | 17.29 | 101.63 | 438.94 | 1524.41 | 478.6 | 1539.81 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.61 | 1.6 | 2 | 1 | 32.22 | 34.23 | -4.42 |  | fail_low_response_condition |
| 7631 | 聚賢研發-創 | 其他電子業 | mainstream_growth |  | 68.76129016183084 | 90.7375655253423 | 1.6 | -0.39 | 5.83 | -1.55 | 18.14 | 19.81 | False |  | strong_accumulation | 0.03 | 0.03 | 2 | 2 | 1.6 | 1.29 | -15.33 |  | fail_low_response_condition |
| 7740 | 熙特爾-創 | 綠能環保 | neutral |  | 2905.180718592785 | 1476.0023495403216 | -1.89 | 7.4 | -11.03 | 17.1 | 15.61 | 31.52 | False |  | distribution_warning | -3.55 | -3.9 | 0 | 1 | 3.88 | 2.44 | -11.68 |  | fail_low_response_condition |
| 7750 | 新代 | 電機機械 | cyclical_turnaround |  | 94.8739387573844 | 63.768704057004605 | -4.39 | -17.36 | 73.11 | 192.95 | 86.53 | 197.53 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.72 | -3.23 | 1 | 0 | -5.79 | -3.56 | -25.57 |  | fail_low_response_condition |
| 7765 | 中華資安 | 數位雲端 | neutral |  | 75.03168748308813 | 28.436327862661106 | 2.63 | 3.67 | 10.43 | -6.79 | 17.05 | 17.05 | False |  | distribution_warning | -1.01 | -0.02 | 0 | 0 | 1.76 | 2.07 | -6.62 |  | fail_low_response_condition |
| 7769 | 鴻勁 | 半導體業 | mainstream_growth |  | 111.83182996542342 | 89.0289902118116 | -10.59 | -0.74 | 86.96 | 149.49 | 114.06 | 159.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.25 | -0.19 | 1 | 1 | -2.17 | 2.09 | -12.76 |  | fail_low_response_condition |
| 7786 | 東方風能 | 綠能環保 | neutral |  | 52.31364457664033 | 53.1385367449244 | 2.53 | -11.96 | -16.21 | -27.03 | 7.52 | 7.52 | False |  | mild_accumulation | 0.21 | -0.38 | 1 | 1 | 2.32 | -0.15 | -18.18 |  | fail_low_response_condition |
| 7822 | 倍利科 | 半導體業 | mainstream_growth |  | 77.97234335979724 | 110.5923011120616 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 8021 | 尖點 | 其他電子業 | mainstream_growth |  | 63.17741148386335 | 54.210191135482056 | -2.0 | -1.12 | 81.11 | 226.67 | 98.2 | 230.34 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.32 | -0.64 | 2 | 2 | 1.52 | 1.78 | -11.27 |  | fail_low_response_condition |
| 8045 | 達運光電 | 通信網路業 | mainstream_growth |  | 95.94130842373109 | 60.08779268099978 | 2.27 | -8.54 | -11.18 | -23.99 | 5.47 | 5.47 | False |  | distribution_warning | -2.09 | -0.09 | 0 | 0 | -2.77 | -3.38 | -22.86 |  | fail_low_response_condition |