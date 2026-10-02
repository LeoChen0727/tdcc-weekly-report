# 營收爆發低反應股 Debug Report

- 產生時間：`2026-10-02 19:43:59 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 888 |
| standardized_revenue_rows | 888 |
| price_rows | 739341 |
| tdcc_rows | 1967 |
| tdcc_trend_rows | 1969 |
| tdcc_strong_accumulation_count | 402 |
| tdcc_mild_accumulation_count | 763 |
| tdcc_distribution_warning_count | 615 |
| revenue_condition_pass | 170 |
| price_metrics_pass | 170 |
| low_response_pass | 29 |
| already_priced_in_excluded | 13 |
| overheat_pass | 16 |
| score_pass | 16 |
| theme_priority_pass | 11 |
| final_rows | 11 |

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
| fail_revenue_condition | 718 |
| fail_low_response_condition | 141 |
| fail_already_priced_in | 13 |
| fail_defensive_or_traditional_excluded | 5 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1591 | 駿吉-KY | 電機機械 | cyclical_turnaround |  | 927.8923253150056 | 337.0821504946037 | -0.84 | 13.64 | 2.61 | -10.91 | 32.42 | 32.42 | False |  | distribution_warning | -0.97 | 0.0 | 2 | 0 | 4.82 | 4.1 | -13.88 |  | fail_low_response_condition |
| 1599 | 宏佳騰 | 電機機械 | cyclical_turnaround |  | 98.4969606411519 | 27.25751519828112 | 0.43 | 1.31 | -2.73 | -8.48 | 3.11 | 3.11 | False |  | distribution_warning | -0.08 | -0.09 | 1 | 1 | 0.29 | 0.22 | -6.83 |  | fail_low_response_condition |
| 1799 | 易威 | 生技醫療業 | defensive_or_traditional |  | 82.42065171392298 | 78.14643043397021 | 0.69 | -3.81 | -13.69 | -29.78 | 2.29 | 2.29 | False |  | mild_accumulation | 0.03 | 0.01 | 2 | 1 | -0.57 | -1.05 | -26.21 |  | fail_low_response_condition |
| 1815 | 富喬 | 電子零組件業 | mainstream_growth |  | 79.20696400933353 | 51.19937149056726 | 0.83 | -7.63 | 25.39 | 4.76 | 104.74 | 104.74 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.65 | -3.6 | 2 | 2 | 0.19 | 3.25 | -14.49 |  | fail_already_priced_in |
| 2073 | 雄順 | 鋼鐵工業 | cyclical_turnaround |  | 249.78321391082105 | 80.3361175138126 | -0.97 | -2.66 | 0.39 | -1.54 | 4.07 | 4.07 | False |  | strong_accumulation | 0.02 | 0.02 | 2 | 2 | -0.89 | -0.91 | -14.81 |  | fail_low_response_condition |
| 2221 | 大甲 | 其他 | neutral |  | 81.31871139616996 | 29.091341365027425 | 18.61 | 125.96 | 279.03 | 493.06 | 346.56 | 493.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.0 | 0.0 | 1 | 1 | 48.59 | 44.14 | -5.05 |  | fail_low_response_condition |
| 2596 | 綠意 | 建材營造 | neutral |  | 1287.8783165883854 | 51.48817312985642 | -0.57 | -2.66 | 8.92 | 7.41 | 21.68 | 32.32 | False |  | distribution_warning | -0.16 | -0.08 | 0 | 0 | -1.28 | -0.24 | -5.31 |  | fail_low_response_condition |
| 2724 | 藝舍-KY | 其他 | neutral |  | 227.70419426048565 | 57.3466120946639 | 7.17 | 18.69 | 2.83 | -37.9 | 29.33 | 29.33 | False |  | mild_accumulation | 0.07 | 0.07 | 1 | 1 | 13.49 | 11.05 | -3.79 |  | fail_low_response_condition |
| 2734 | 易飛網 | 觀光餐旅 | defensive_or_traditional |  | 53.64213986231172 | 32.937667797869686 | -0.69 | -3.68 | -4.32 | -16.76 | 2.49 | 2.49 | False |  | mild_accumulation | 0.05 | 0.0 | 2 | 0 | -1.25 | -1.31 | -11.93 |  | fail_low_response_condition |
| 3081 | 聯亞 | 通信網路業 | mainstream_growth |  | 180.9018539007475 | 129.03610801621684 | 9.14 | -13.84 | 53.54 | 23.68 | 119.1 | 119.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -3.66 | -3.38 | 0 | 1 | 3.45 | 4.57 | -18.75 |  | fail_low_response_condition |
| 3088 | 艾訊 | 電腦及週邊設備業 | mainstream_growth |  | 78.52614807235602 | 49.50165318684724 | 3.94 | 7.32 | -5.04 | 38.51 | 15.79 | 39.98 | False |  | mild_accumulation | 0.54 | -0.05 | 2 | 1 | 3.98 | 2.69 | -16.98 |  | fail_low_response_condition |
| 3141 | 晶宏 | 半導體業 | mainstream_growth |  | 79.77072598488336 | 23.93358237328677 | 0.81 | -12.46 | 15.98 | 99.54 | 53.35 | 99.54 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.09 | -7.3 | 0 | 1 | -4.94 | -0.24 | -20.82 |  | fail_already_priced_in |
| 3147 | 大綜 | 資訊服務業 | mainstream_growth |  | 233.4782684238417 | 111.9619364888416 | 12.79 | 19.95 | 17.56 | 60.79 | 35.29 | 63.78 | False |  | distribution_warning | -0.42 | 0.0 | 1 | 1 | 13.13 | 11.45 | -3.11 |  | fail_low_response_condition |
| 3162 | 精確 | 電機機械 | cyclical_turnaround |  | 101.18952622424948 | 33.42354480729761 | 19.95 | 25.84 | 6.54 | 42.22 | 62.91 | 62.91 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | -0.07 | 0.49 | 1 | 2 | 19.12 | 17.81 | -2.61 |  | fail_low_response_condition |
| 3176 | 基亞 | 生技醫療業 | defensive_or_traditional |  | 197.4033952820216 | -10.451573430439558 | -2.59 | 6.98 | -1.83 | 19.59 | 21.13 | 28.16 | False |  | strong_accumulation | 0.62 | 2.7 | 3 | 3 | 1.19 | 1.03 | -7.4 |  | fail_low_response_condition |
| 3226 | 龍鋒 | 電機機械 | cyclical_turnaround |  | 123.95113510044578 | -13.819118890336528 | 8.42 | 16.85 | 29.04 | 28.78 | 41.8 | 68.04 | False |  | strong_accumulation | 0.35 | 0.38 | 3 | 3 | 10.04 | 9.78 | -2.92 |  | fail_low_response_condition |
| 3234 | 光環 | 通信網路業 | mainstream_growth |  | 110.12726780395344 | 26.94082696105297 | 6.76 | -13.98 | 47.56 | 61.33 | 117.63 | 117.63 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.0 | -1.58 | 2 | 1 | -0.6 | 3.54 | -17.5 |  | fail_already_priced_in |
| 3260 | 威剛 | 半導體業 | mainstream_growth | D_降級_TDCC轉弱 | 279.80697041038457 | 218.1360564650288 | -0.26 | -7.39 | -5.45 | 5.96 | 14.37 | 14.37 | False |  | distribution_warning | -0.94 | -0.15 | 1 | 2 | -2.97 | -2.59 | -16.87 | 17 | selected |
| 3290 | 東浦 | 電子零組件業 | mainstream_growth |  | 79.79663584803046 | 84.26047338908913 | 9.95 | 3.29 | -24.36 | 1.82 | 12.65 | 14.06 | False |  | distribution_warning | -0.18 | -1.73 | 1 | 1 | 6.98 | 3.86 | -28.75 |  | fail_low_response_condition |
| 3310 | 佳穎 | 電子零組件業 | mainstream_growth |  | 259.9634084627661 | 18.10698372294364 | -1.31 | -2.31 | -1.31 | -3.43 | 6.46 | 6.46 | False |  | strong_accumulation | 0.16 | 0.39 | 3 | 2 | -0.99 | -1.06 | -7.65 |  | fail_low_response_condition |
| 3324 | 雙鴻 | 其他電子業 | mainstream_growth |  | 67.17939465738924 | 81.01348291098509 | -5.64 | 4.88 | 55.15 | 44.02 | 85.8 | 85.8 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.25 | -0.66 | 3 | 2 | 3.06 | 5.52 | -14.0 |  | fail_already_priced_in |
| 3357 | 臺慶科 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 53.06726585348456 | 32.22016146268528 | 4.61 | 3.11 | -17.9 | 23.14 | 26.76 | 32.21 | False |  | mild_accumulation | 0.69 | 0.27 | 2 | 1 | 4.45 | 3.2 | -23.45 | 17 | selected |
| 3491 | 昇達科 | 通信網路業 | mainstream_growth |  | 93.18632935147426 | 73.39943090565077 | -5.11 | 2.77 | 14.23 | -14.66 | 63.37 | 63.37 | True | 距60日低點反彈>50% | mild_accumulation | -0.29 | 1.15 | 1 | 3 | 0.76 | 1.7 | -8.9 |  | fail_low_response_condition |
| 3498 | 陽程 | 其他電子業 | mainstream_growth |  | 326.0465447130375 | 154.7955799441265 | 8.04 | 6.7 | 74.8 | 164.13 | 155.65 | 182.52 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.57 | -3.63 | 1 | 1 | 7.88 | 7.93 | -8.51 |  | fail_low_response_condition |
| 3512 | 皇龍 | 建材營造 | neutral |  | 27442.5 | -62.79066107443284 | -0.78 | -3.05 | -8.39 | -11.57 | 0.79 | 0.79 | False |  | mild_accumulation | -0.27 | 0.06 | 2 | 3 | -0.65 | -0.96 | -13.18 |  | fail_low_response_condition |
| 3546 | 宇峻 | 文化創意業 | defensive_or_traditional |  | 93.84497509896563 | 49.8742383019689 | 0.97 | 0.83 | -1.75 | 1.67 | 4.29 | 8.63 | False |  | mild_accumulation | 0.08 | 0.0 | 1 | 0 | 0.39 | 0.31 | -5.32 |  | fail_low_response_condition |
| 3594 | 磐儀 | 電腦及週邊設備業 | mainstream_growth |  | 50.512183676505934 | 43.95074303410667 | 1.18 | -3.58 | -8.8 | 8.89 | 4.78 | 10.29 | False |  | distribution_warning | -0.54 | -0.09 | 1 | 0 | 0.42 | -1.25 | -23.83 |  | fail_low_response_condition |
| 3623 | 富晶通 | 光電業 | mainstream_growth |  | 96.26579854461892 | -3.904992748296346 | 10.29 | 31.12 | 28.36 | 36.08 | 60.79 | 60.79 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 1.49 | 0.0 | 1 | 0 | 12.01 | 12.81 | -1.45 |  | fail_low_response_condition |
| 3624 | 光頡 | 電子零組件業 | mainstream_growth |  | 65.7609210971893 | 30.70367519540332 | 10.82 | 66.85 | 11.24 | 165.18 | 164.71 | 205.87 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 3.89 | 3.34 | 2 | 2 | 22.07 | 21.22 | -5.71 |  | fail_low_response_condition |
| 3629 | 地心引力 | 文化創意業 | defensive_or_traditional |  | 381.0 | 3076.410835214447 | -19.78 | -10.7 | -8.18 | -29.47 | 14.06 | 14.06 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -22.67 | -16.89 | -31.62 |  | fail_low_response_condition |
| 3631 | 晟楠 | 電子零組件業 | mainstream_growth |  | 421.939736346516 | 35.275157605346735 | 2.11 | 2.11 | 23.39 | 54.12 | 36.71 | 49.64 | False |  | mild_accumulation | 0.11 | 0.0 | 3 | 0 | 4.74 | 4.17 | -8.15 |  | fail_low_response_condition |
| 3646 | 艾恩特 | 電子零組件業 | mainstream_growth |  | 50.80557194714161 | 20.04391791741236 | 0.81 | 4.84 | 5.96 | 8.03 | 10.42 | 10.42 | False |  | distribution_warning | -0.14 | 0.0 | 0 | 0 | 1.43 | 1.75 | -0.99 |  | fail_low_response_condition |
| 3664 | 安瑞-KY | 通信網路業 | mainstream_growth |  | 269.24933206929245 | -28.55899750094389 | -6.63 | -0.36 | 7.92 | -4.26 | 59.81 | 76.06 | True | 距60日低點反彈>50% | neutral | 0.0 | 0.0 | 0 | 0 | 2.18 | 3.88 | -9.38 |  | fail_low_response_condition |
| 3689 | 湧德 | 電子零組件業 | mainstream_growth |  | 62.06674705146218 | 43.33418890723997 | 3.2 | -4.64 | -8.13 | -16.61 | 18.32 | 18.32 | False |  | mild_accumulation | 0.64 | 0.0 | 2 | 1 | 2.52 | 2.4 | -12.06 |  | fail_low_response_condition |
| 3691 | 碩禾 | 光電業 | mainstream_growth | A_優先追蹤 | 75.83834981581273 | 119.78541950258304 | -7.0 | 11.33 | -23.91 | -8.5 | 24.86 | 24.86 | False |  | strong_accumulation | 1.08 | 0.29 | 3 | 3 | 8.89 | 5.16 | -24.41 | 19 | selected |
| 3693 | 營邦 | 電腦及週邊設備業 | mainstream_growth |  | 171.01452065990162 | 25.272232227252942 | -9.43 | 3.27 | 22.32 | 10.13 | 64.93 | 64.93 | True | 距60日低點反彈>50% | strong_accumulation | 4.13 | 5.28 | 2 | 2 | -3.43 | -0.22 | -11.36 |  | fail_low_response_condition |
| 3709 | 鑫聯大投控 | 電腦及週邊設備業 | mainstream_growth |  | 76.05769307049941 | 44.75713821429095 | 3.48 | -0.76 | -11.84 | -5.07 | 8.26 | 8.26 | False |  | mild_accumulation | 0.41 | 0.01 | 3 | 1 | 2.94 | 0.96 | -22.02 |  | fail_low_response_condition |
| 3713 | 新晶投控 | 綠能環保 | neutral |  | 184.7986446899376 | 97.83756861361584 | -2.13 | -6.12 | -7.69 | -16.62 | 4.94 | 10.4 | False |  | strong_accumulation | 0.21 | 0.18 | 3 | 3 | -2.42 | -2.61 | -10.97 |  | fail_low_response_condition |
| 4113 | 聯上 | 建材營造 | neutral |  | 2252.2927328556807 | 154.7256930801135 | -2.88 | 0.66 | 2.01 | -5.59 | 8.57 | 9.35 | False |  | strong_accumulation | 0.14 | 1.05 | 2 | 2 | -2.27 | -1.42 | -12.39 |  | fail_low_response_condition |
| 4154 | 樂威科-KY | 其他 | neutral |  | 117.02317290552584 | 67.14616163076478 | -5.06 | -2.17 | -12.11 | 9.22 | 4.17 | 5.63 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -6.43 | -6.24 | -14.45 |  | fail_low_response_condition |
| 4157 | 太景*-KY | 生技醫療業 | defensive_or_traditional |  | 172.2115013508298 | 4.858537301383436 | -2.48 | -2.59 | -4.42 | -20.64 | 11.9 | 11.9 | False |  | mild_accumulation | 0.13 | -0.08 | 2 | 1 | -2.38 | -2.17 | -7.39 |  | fail_low_response_condition |
| 4402 | 郡都開發 | 紡織纖維 | defensive_or_traditional |  | 840.3707518022657 | 36.499848346982105 | 1.8 | -5.35 | -16.27 | -13.72 | 5.6 | 24.12 | False |  | strong_accumulation | 0.04 | 0.03 | 2 | 2 | -0.49 | -1.4 | -18.44 |  | fail_low_response_condition |
| 4416 | 三圓 | 建材營造 | neutral |  | 3633.031771674744 | 547.9095220722364 | -9.22 | 1.19 | 19.63 | -6.91 | 28.26 | 38.08 | False |  | distribution_warning | -4.47 | -7.62 | 1 | 0 | 3.16 | 1.06 | -21.47 |  | fail_low_response_condition |
| 4442 | 竣邦-KY | 紡織纖維 | defensive_or_traditional |  | 131.32054817155662 | 32.31463758869362 | -0.92 | 5.93 | 7.2 | -8.38 | 16.52 | 16.52 | False |  | mild_accumulation | -1.36 | 4.36 | 0 | 1 | -0.31 | -0.17 | -26.47 |  | fail_low_response_condition |
| 4502 | 健信 | 電機機械 | cyclical_turnaround |  | 78.28824565554592 | 35.85489775931537 | 0.96 | 1.28 | 0.63 | -0.31 | 5.32 | 5.32 | False |  | mild_accumulation | 0.07 | -0.59 | 2 | 0 | 0.76 | 0.7 | -4.8 |  | fail_low_response_condition |
| 4523 | 永彰 | 電機機械 | cyclical_turnaround |  | 242.5427997252677 | 91.93464113212823 | 0.84 | 0.42 | -9.13 | -21.51 | 2.58 | 2.58 | False |  | strong_accumulation | 0.02 | 0.01 | 2 | 2 | 0.2 | -0.34 | -8.6 |  | fail_low_response_condition |
| 4529 | 淳紳 | 其他 | neutral |  | 327.27272727272725 | 311.48219707424784 | 1.83 | -12.11 | -24.09 | 8.79 | 8.79 | 13.22 | False |  | distribution_warning | -0.01 | -0.01 | 0 | 0 | -4.83 | -4.37 | -32.53 |  | fail_low_response_condition |
| 4542 | 科嶠 | 電子零組件業 | mainstream_growth |  | 194.65100798782808 | 54.126809332335526 | 1.51 | 13.11 | -16.6 | 96.21 | 54.0 | 106.44 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.39 | 0.0 | 1 | 0 | 14.12 | 11.03 | -20.26 |  | fail_low_response_condition |
| 4561 | 健椿 | 電機機械 | cyclical_turnaround |  | 52.37483047016275 | 23.0496196694697 | 3.81 | 0.58 | 4.56 | 16.58 | 36.25 | 37.54 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 4.86 | 3.55 | -14.34 |  | fail_low_response_condition |
| 4726 | 永昕 | 生技醫療業 | defensive_or_traditional |  | 131.44212689667236 | 36.95672300221732 | 3.8 | -4.13 | -12.29 | -23.56 | 4.98 | 4.98 | False |  | strong_accumulation | 0.03 | 0.04 | 2 | 3 | 0.49 | -0.11 | -13.43 |  | fail_low_response_condition |
| 4760 | 勤凱科技 | 其他電子業 | mainstream_growth |  | 91.5371817810842 | 65.53244031575477 | 19.62 | 16.33 | 0.96 | 19.17 | 62.56 | 62.56 | True | 距60日低點反彈>50% | distribution_warning | -0.3 | -0.31 | 0 | 0 | 18.59 | 17.91 | -5.51 |  | fail_low_response_condition |
| 4768 | 晶呈科技 | 化學工業 | cyclical_turnaround |  | 93.11618386508256 | 126.35883305765292 | 13.83 | 25.67 | 11.79 | -21.82 | 48.61 | 48.61 | True | 近20日漲幅>25% | distribution_warning | -0.91 | 0.0 | 0 | 0 | 17.06 | 13.98 | -7.19 |  | fail_low_response_condition |
| 4806 | 桂田文創 | 文化創意業 | defensive_or_traditional |  | 179.11410148584244 | 173.7594875619708 | 48.72 | 44.55 | 31.37 | 27.01 | 62.03 | 62.03 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.07 | 0.0 | 3 | 0 | 42.58 | 38.42 | -2.19 |  | fail_low_response_condition |
| 4905 | 台聯電 | 生技醫療業 | defensive_or_traditional |  | 68.23410881113757 | 37.705899263289325 | 18.44 | 4.05 | 35.63 | 13.78 | 45.67 | 45.67 | False |  | strong_accumulation | 0.03 | 0.03 | 2 | 2 | 14.16 | 13.83 | -7.5 |  | fail_low_response_condition |
| 4931 | 新盛力 | 電腦及週邊設備業 | mainstream_growth |  | 125.86678832116787 | 88.36847369976456 | 5.66 | 0.8 | 1.82 | 79.36 | 57.5 | 80.0 | True | 距60日低點反彈>50%；近120日漲幅>70% | distribution_warning | -5.8 | -7.59 | 1 | 1 | 4.32 | 3.31 | -12.5 |  | fail_already_priced_in |
| 4950 | 金耘國際 | 鋼鐵工業 | cyclical_turnaround |  | 64.87176511546942 | 29.29786327634824 | 2.22 | -1.23 | 0.0 | 1.26 | 8.42 | 8.42 | False |  | mild_accumulation | 0.03 | 0.0 | 1 | 0 | 1.51 | 1.53 | -5.57 |  | fail_low_response_condition |
| 4973 | 廣穎電通 | 半導體業 | mainstream_growth |  | 204.02859571367856 | 135.88675742507232 | 2.59 | -8.58 | -14.77 | 80.34 | 18.88 | 80.1 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.13 | -1.12 | 1 | 0 | -1.32 | -1.88 | -19.01 |  | fail_low_response_condition |
| 5205 | 中茂 | 綠能環保 | neutral |  | 2617.518248175182 | 94.80352846832398 | 31.79 | 10.95 | -2.77 | -21.51 | 38.18 | 38.18 | False |  | mild_accumulation | 1.26 | 1.41 | 1 | 1 | 15.69 | 14.37 | -9.52 |  | fail_low_response_condition |
| 5206 | 坤悅 | 建材營造 | neutral |  | 2630241.1764705884 | -15.3744999515524 | -0.44 | -1.93 | -1.08 | -10.04 | 15.7 | 15.7 | False |  | mild_accumulation | -0.62 | 0.33 | 0 | 2 | 0.91 | 0.92 | -5.97 |  | fail_low_response_condition |
| 5209 | 新鼎 | 其他 | neutral |  | 92.1791254768751 | -11.968626260310954 | 5.07 | 13.55 | 11.04 | 6.67 | 16.56 | 16.56 | False |  | distribution_warning | -1.68 | -1.61 | 0 | 0 | 5.17 | 5.2 | -3.3 |  | fail_low_response_condition |
| 5220 | 萬達光電 | 光電業 | mainstream_growth |  | 72.53576386793023 | 39.74673024792735 | 16.67 | 16.08 | 11.33 | 14.36 | 20.63 | 20.63 | False |  | strong_accumulation | 0.08 | 0.05 | 3 | 2 | 13.24 | 10.95 | -4.94 |  | fail_low_response_condition |
| 5228 | 鈺鎧 | 電子零組件業 | mainstream_growth |  | 70.24885536023534 | 55.60044315952866 | 21.19 | 17.91 | -16.72 | 42.37 | 42.79 | 60.7 | False |  | mild_accumulation | 0.08 | 0.0 | 2 | 0 | 17.92 | 16.26 | -17.86 |  | fail_low_response_condition |
| 5263 | 智崴 | 文化創意業 | defensive_or_traditional |  | 216.5614441898171 | 79.29711524381315 | -0.33 | -7.75 | -10.4 | -5.63 | 4.26 | 4.26 | False |  | distribution_warning | -0.26 | -1.32 | 1 | 1 | -3.43 | -1.91 | -14.62 |  | fail_low_response_condition |
| 5274 | 信驊 | 半導體業 | mainstream_growth |  | 118.41515263458372 | 74.48866403472434 | -7.1 | 6.29 | 30.7 | 30.11 | 58.59 | 58.59 | True | 距60日低點反彈>50% | distribution_warning | -0.37 | -0.29 | 1 | 0 | -0.09 | 1.67 | -13.58 |  | fail_low_response_condition |
| 5289 | 宜鼎 | 電腦及週邊設備業 | mainstream_growth |  | 576.2927682888633 | 553.1525733190747 | -0.77 | -8.8 | -18.55 | 19.35 | 18.81 | 32.14 | False |  | distribution_warning | -0.39 | -2.69 | 1 | 0 | -1.18 | -2.74 | -22.92 |  | fail_low_response_condition |
| 5291 | 邑昇 | 電子零組件業 | mainstream_growth |  | 61.4139456123347 | 45.78003472004 | 7.83 | -12.31 | 12.73 | -14.13 | 49.4 | 49.4 | False |  | mild_accumulation | 0.8 | 0.0 | 2 | 0 | 2.02 | 3.14 | -15.3 |  | fail_low_response_condition |
| 5314 | 世紀* | 其他 | neutral |  | 102.52220805278574 | 151.4041502193621 | 15.0 | -12.57 | -55.9 | -61.62 | 84.57 | 84.57 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 1.47 | 0.9 | 1 | 1 | -8.56 | -7.72 | -57.59 |  | fail_low_response_condition |
| 5351 | 鈺創 | 半導體業 | mainstream_growth |  | 525.3153245373534 | 488.92138522250326 | 5.94 | -0.85 | 24.6 | 74.44 | 76.56 | 94.96 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.12 | -5.59 | 0 | 0 | 4.88 | 4.72 | -17.73 |  | fail_already_priced_in |
| 5355 | 佳總 | 電子零組件業 | mainstream_growth |  | 103.3460896869787 | 36.10493943796871 | 8.82 | 23.33 | 19.55 | 14.02 | 58.8 | 58.8 | True | 距60日低點反彈>50% | strong_accumulation | 0.15 | 0.21 | 3 | 3 | 13.3 | 12.06 | -0.67 |  | fail_low_response_condition |
| 5386 | 青雲 | 電腦及週邊設備業 | mainstream_growth |  | 1846.2079589216944 | 625.4991757344794 | 3.72 | 5.22 | -32.06 | -17.61 | 45.16 | 45.16 | False |  | distribution_warning | -0.24 | 0.0 | 1 | 0 | 2.82 | 3.45 | -32.84 |  | fail_low_response_condition |
| 5455 | 昇益 | 建材營造 | neutral |  | 546.5800865800866 | -98.12440164053912 | 0.66 | 3.54 | 11.64 | 31.2 | 15.41 | 39.55 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.14 | 2.62 | -0.97 |  | fail_low_response_condition |
| 5468 | 凱鈺 | 半導體業 | mainstream_growth |  | 232.888948140248 | 66.108739450808 | 2.44 | 2.44 | -17.78 | 37.33 | 13.51 | 54.13 | False |  | distribution_warning | -0.93 | -0.2 | 1 | 1 | 0.23 | -0.65 | -25.0 |  | fail_low_response_condition |
| 5475 | 德宏 | 電子零組件業 | mainstream_growth |  | 271.8799275827834 | 166.78962235136055 | 1.98 | -5.0 | -12.8 | -46.12 | 80.5 | 80.5 | True | 距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -4.13 | -2.62 | 0 | 1 | -0.39 | 0.74 | -20.48 |  | fail_already_priced_in |
| 5498 | 凱崴 | 電子零組件業 | mainstream_growth |  | 87.52412149123518 | 70.79154446159939 | 10.76 | -0.36 | -8.85 | -19.77 | 47.87 | 47.87 | False |  | mild_accumulation | 0.3 | -0.65 | 1 | 1 | 7.48 | 7.38 | -11.46 |  | fail_low_response_condition |
| 5508 | 永信建 | 建材營造 | neutral |  | 633.6485802383911 | 60.19059588257221 | 0.56 | 0.56 | -6.45 | 5.5 | 9.15 | 18.02 | False |  | mild_accumulation | 0.01 | -0.46 | 1 | 1 | 0.22 | 0.5 | -10.5 |  | fail_low_response_condition |
| 5514 | 三豐 | 建材營造 | neutral |  | 319.29460580912865 | 17470.23871302543 | 3.06 | 1.34 | 10.99 | -3.5 | 15.21 | 16.09 | False |  | mild_accumulation | -0.18 | 0.01 | 0 | 1 | 0.82 | 1.6 | -1.62 |  | fail_low_response_condition |
| 5529 | 鉅陞 | 建材營造 | neutral |  | 3702.282608695652 | 1148.9078262626942 | 0.19 | 15.52 | 21.45 | 5.04 | 27.07 | 27.07 | False |  | strong_accumulation | 0.49 | 0.27 | 3 | 3 | 3.24 | 4.58 | -2.07 |  | fail_low_response_condition |
| 5547 | 久舜 | 建材營造 | neutral |  | 89.50367793179775 | 20.860723558940627 | 1.0 | 2.54 | -1.7 | -9.01 | 6.32 | 6.32 | False |  | mild_accumulation | 1.65 | 4.13 | 3 | 1 | 1.33 | 1.1 | -2.42 |  | fail_low_response_condition |
| 6026 | 福邦證 | 金融業 | defensive_or_traditional |  | 231.77946698415604 | 170.39888033589924 | 0.0 | 5.98 | -0.93 | 7.77 | 21.76 | 21.76 | False |  | strong_accumulation | 1.13 | 1.23 | 3 | 2 | 2.87 | 2.91 | -1.85 |  | fail_low_response_condition |
| 6113 | 亞矽 | 電子通路業 | mainstream_growth |  | 130.4034643008027 | 72.2960954962667 | 9.64 | 4.49 | -3.36 | 6.3 | 23.8 | 23.8 | False |  | mild_accumulation | 0.07 | 0.0 | 2 | 0 | 7.91 | 6.69 | -14.21 |  | fail_low_response_condition |
| 6126 | 信音 | 電子零組件業 | mainstream_growth |  | 57.25232421904718 | 54.322022437339406 | 1.79 | 3.48 | -8.49 | -5.59 | 11.01 | 11.01 | False |  | strong_accumulation | 0.73 | 0.2 | 3 | 2 | 4.28 | 2.94 | -16.56 |  | fail_low_response_condition |
| 6148 | 驊宏資 | 資訊服務業 | mainstream_growth |  | 95.400250775424 | -34.765720711052694 | 2.01 | 36.07 | 14.59 | 14.76 | 54.25 | 54.25 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.05 | 0.0 | 1 | 0 | 9.93 | 8.95 | -9.5 |  | fail_already_priced_in |
| 6156 | 松上 | 電子零組件業 | mainstream_growth |  | 55.15640641987535 | 24.92790459822721 | 7.45 | 6.68 | -21.3 | 10.92 | 15.5 | 25.21 | False |  | distribution_warning | -0.11 | -0.04 | 1 | 1 | 7.25 | 5.58 | -24.49 |  | fail_low_response_condition |
| 6169 | 昱泉 | 文化創意業 | defensive_or_traditional |  | 148.26175869120655 | -93.39853300733496 | -0.41 | -2.83 | -18.64 | -30.43 | 3.45 | 3.45 | False |  | mild_accumulation | 0.08 | 0.0 | 3 | 0 | -0.87 | -1.6 | -20.0 |  | fail_low_response_condition |
| 6173 | 信昌電 | 電子零組件業 | mainstream_growth |  | 54.26510929473646 | 26.13937451549827 | 0.17 | 16.31 | 6.69 | 261.14 | 128.68 | 311.13 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.63 | 2.13 | 1 | 2 | 3.64 | 7.0 | -8.46 |  | fail_already_priced_in |
| 6175 | 立敦 | 電子零組件業 | mainstream_growth |  | 68.93824644185868 | 24.45378133298373 | 10.36 | 7.42 | -28.32 | 20.79 | 16.74 | 27.83 | False |  | strong_accumulation | 0.21 | 1.92 | 2 | 3 | 8.43 | 6.29 | -32.12 |  | fail_low_response_condition |
| 6179 | 亞通 | 其他 | neutral |  | 223.27509730425265 | 131.39675731028802 | 3.99 | 22.69 | 35.44 | 48.68 | 62.95 | 67.05 | True | 距60日低點反彈>50% | strong_accumulation | 1.29 | 1.53 | 2 | 2 | 2.85 | 5.24 | -12.89 |  | fail_already_priced_in |
| 6187 | 萬潤 | 半導體業 | mainstream_growth |  | 103.06092173798378 | 51.11324845299687 | 12.45 | 1.12 | 39.12 | 22.62 | 64.04 | 64.04 | True | 距60日低點反彈>50% | distribution_warning | -2.27 | -1.17 | 0 | 1 | 6.53 | 7.16 | -6.87 |  | fail_low_response_condition |
| 6190 | 萬泰科 | 通信網路業 | mainstream_growth | A_優先追蹤 | 71.82219158754506 | 29.675733762149 | 3.96 | 2.46 | -14.29 | 12.03 | 25.98 | 25.98 | False |  | mild_accumulation | 0.77 | -0.9 | 3 | 1 | 3.47 | 2.71 | -17.1 | 18 | selected |
| 6199 | 天品 | 其他 | neutral |  | 171.69669177857844 | 527.7881911902531 | 8.2 | 38.66 | 27.54 | 17.33 | 46.99 | 51.55 | True | 近20日漲幅>25% | mild_accumulation | 3.29 | -0.33 | 3 | 1 | 20.5 | 17.72 | -1.49 |  | fail_low_response_condition |
| 6212 | 理銘 | 建材營造 | neutral |  | 331.5416800772449 | -43.06817091684851 | 0.31 | 3.22 | 14.64 | -13.94 | 18.01 | 19.78 | False |  | mild_accumulation | 0.02 | 0.0 | 2 | 0 | 0.46 | 1.4 | -8.15 |  | fail_low_response_condition |
| 6219 | 富旺 | 建材營造 | neutral |  | 115059.92366412214 | 31310.13004791239 | 0.83 | 0.41 | -5.08 | -15.92 | 2.53 | 6.58 | False |  | mild_accumulation | -0.02 | 0.01 | 1 | 2 | -0.14 | -0.29 | -18.18 |  | fail_low_response_condition |
| 6220 | 岳豐 | 電子零組件業 | mainstream_growth |  | 68.01226096987067 | 25.581915624751705 | 1.39 | -1.74 | -23.92 | -25.69 | 7.61 | 7.61 | False |  | mild_accumulation | -0.16 | 0.01 | 2 | 2 | 0.19 | -0.26 | -30.94 |  | fail_low_response_condition |
| 6223 | 旺矽 | 半導體業 | mainstream_growth | A_優先追蹤 | 69.87471956008775 | 54.78774916750976 | -5.52 | 0.38 | -15.85 | 8.04 | 14.19 | 15.31 | False |  | mild_accumulation | 0.75 | -0.25 | 3 | 1 | -2.39 | -2.13 | -30.13 | 17 | selected |
| 6227 | 茂綸 | 電子通路業 | mainstream_growth | A_優先追蹤 | 168.85623019694452 | 51.40575719860173 | 4.46 | 21.12 | 16.12 | 50.91 | 40.5 | 60.39 | False |  | mild_accumulation | 1.62 | 0.0 | 2 | 0 | 9.98 | 8.72 | -3.44 | 23 | selected |
| 6234 | 高僑 | 光電業 | mainstream_growth |  | 68.3996984746364 | 33.77040476051723 | 4.58 | 12.38 | -12.49 | 18.2 | 38.72 | 38.72 | False |  | strong_accumulation | 0.02 | 1.07 | 2 | 2 | 9.02 | 6.84 | -17.46 |  | fail_low_response_condition |
| 6259 | 百徽 | 電子零組件業 | mainstream_growth |  | 93.68859091434516 | 58.558352975010784 | 12.39 | 9.02 | -23.36 | 34.64 | 24.14 | 73.21 | False |  | distribution_warning | -0.1 | 0.0 | 0 | 0 | 11.3 | 9.2 | -24.6 |  | fail_low_response_condition |
| 6265 | 方土昶 | 電子通路業 | mainstream_growth | D_降級_TDCC轉弱 | 465.9463049253146 | 680.3753443601282 | 6.14 | -10.22 | -0.4 | 29.62 | 30.64 | 42.94 | False |  | distribution_warning | -5.15 | -2.75 | 0 | 0 | -0.08 | -0.95 | -27.07 | 15 | selected |
| 6274 | 台燿 | 電子零組件業 | mainstream_growth |  | 132.48393122185607 | 97.0098143748561 | 10.96 | 14.89 | 2.86 | 68.75 | 72.71 | 84.09 | True | 距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | -0.65 | 0.09 | 1 | 1 | 14.06 | 11.22 | -6.36 |  | fail_low_response_condition |
| 6419 | 京晨科 | 光電業 | mainstream_growth |  | 365.6956677803241 | 214.59560842862132 | 3.31 | 0.32 | 8.71 | 14.71 | 38.67 | 38.67 | False |  | distribution_warning | -0.1 | 0.0 | 0 | 0 | 2.82 | 2.37 | -14.75 |  | fail_low_response_condition |
| 6425 | 易發 | 電機機械 | cyclical_turnaround |  | 93.96055625174893 | 56.13194851355093 | 9.62 | 22.77 | 13.51 | 2.18 | 64.54 | 64.54 | True | 距60日低點反彈>50% | distribution_warning | -0.43 | 0.0 | 1 | 0 | 17.33 | 15.01 | -5.34 |  | fail_low_response_condition |
| 6441 | 廣錠 | 電腦及週邊設備業 | mainstream_growth |  | 135.5224867724868 | -46.96087581292683 | 1.84 | 16.86 | 9.67 | 19.09 | 38.61 | 38.61 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | 3.6 | 4.54 | -7.25 |  | fail_low_response_condition |
| 6461 | 益得 | 生技醫療業 | defensive_or_traditional |  | 1102.978723404255 | -56.19966460321732 | 10.21 | 63.27 | 75.17 | 44.54 | 79.32 | 79.32 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.45 | 0.94 | 2 | 1 | 14.47 | 17.17 | -10.03 |  | fail_low_response_condition |
| 6465 | 威潤 | 通信網路業 | mainstream_growth |  | 128.67103900586815 | 90.76375974682718 | 0.96 | -10.33 | -26.4 | -5.61 | 4.47 | 4.47 | False |  | distribution_warning | -2.79 | -3.09 | 2 | 0 | -1.53 | -2.59 | -33.91 |  | fail_low_response_condition |
| 6486 | 互動 | 通信網路業 | mainstream_growth |  | 825.8113558796152 | 130.93748048323718 | -0.12 | -3.92 | -2.18 | -8.48 | 10.67 | 10.67 | False |  | strong_accumulation | 0.88 | 0.08 | 3 | 2 | -0.31 | 0.86 | -12.63 |  | fail_low_response_condition |
| 6510 | 精測 | 半導體業 | mainstream_growth |  | 54.27157903895514 | 33.14430578664898 | -11.65 | -10.63 | 8.29 | -16.12 | 37.36 | 37.36 | False |  | mild_accumulation | 0.33 | -4.64 | 1 | 0 | -8.87 | -4.76 | -21.98 |  | fail_low_response_condition |
| 6535 | 順藥 | 生技醫療業 | defensive_or_traditional |  | 5135.838150289017 | 1.269446845289542 | 3.28 | 3.41 | -16.26 | -37.04 | 15.33 | 15.33 | False |  | mild_accumulation | -0.08 | 0.1 | 2 | 3 | 7.93 | 5.87 | -19.05 |  | fail_low_response_condition |
| 6560 | 欣普羅 | 光電業 | mainstream_growth |  | 461.324570273003 | 64.14995833375167 | -3.92 | 2.08 | -18.62 | -16.82 | 8.14 | 8.14 | False |  | mild_accumulation | 1.75 | 2.02 | 1 | 1 | -0.86 | -1.4 | -19.55 |  | fail_low_response_condition |
| 6574 | 霈方 | 生技醫療業 | defensive_or_traditional |  | 82.79946784014737 | 39.79211362908695 | -0.42 | -0.42 | -1.65 | 16.02 | 6.22 | 23.83 | False |  | distribution_warning | -0.34 | 0.0 | 1 | 0 | -0.1 | -0.63 | -22.4 |  | fail_low_response_condition |
| 6578 | 達邦蛋白 | 農業科技 | defensive_or_traditional |  | 97.3592571096924 | 29.5049711051416 | -2.08 | -7.84 | -1.2 | -7.58 | 3.79 | 14.63 | False |  | strong_accumulation | 0.47 | 2.97 | 3 | 3 | -4.22 | -3.69 | -15.21 |  | fail_low_response_condition |
| 6588 | 東典光電 | 通信網路業 | mainstream_growth |  | 189.01808785529715 | 135.2352266207688 | 1.33 | 6.05 | 40.57 | -25.0 | 71.17 | 71.17 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.18 | 0.0 | 1 | 0 | 2.68 | 4.19 | -10.24 |  | fail_already_priced_in |
| 6593 | 台灣銘板 | 資訊服務業 | mainstream_growth |  | 107.70474650432796 | 11.187269900432035 | -1.24 | -0.47 | -5.9 | -14.59 | 2.08 | 2.08 | False |  | mild_accumulation | -0.14 | 0.03 | 2 | 3 | 0.07 | -0.49 | -8.86 |  | fail_low_response_condition |
| 6609 | 瀧澤科 | 電機機械 | cyclical_turnaround |  | 92.46337718051008 | 7.802791285394987 | -1.88 | -3.58 | -1.01 | 0.26 | 12.52 | 12.52 | False |  | strong_accumulation | 0.31 | 0.05 | 3 | 3 | -0.95 | -0.97 | -15.55 |  | fail_low_response_condition |
| 6613 | 朋億* | 其他電子業 | mainstream_growth |  | 186.8173497622356 | 63.62011712507013 | 4.46 | 6.24 | -14.46 | 19.07 | 15.64 | 24.89 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.86 | 4.41 | -25.37 |  | fail_low_response_condition |
| 6642 | 富致 | 電子零組件業 | mainstream_growth |  | 51.855473297015415 | 25.70186147958134 | 6.36 | 4.76 | 4.5 | 45.39 | 28.22 | 49.02 | False |  | distribution_warning | -1.12 | 0.0 | 1 | 0 | 6.02 | 5.11 | -5.96 |  | fail_low_response_condition |
| 6654 | 天正國際 | 其他電子業 | mainstream_growth |  | 848.7643215604583 | 154.779527404262 | 12.6 | 9.5 | 9.77 | 149.43 | 56.43 | 157.65 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.2 | 0.0 | 2 | 0 | 6.13 | 9.07 | -3.1 |  | fail_low_response_condition |
| 6693 | 廣閎科 | 半導體業 | mainstream_growth |  | 114.19594133697134 | 91.03457478012612 | 4.57 | 19.08 | -17.27 | 45.58 | 53.16 | 54.89 | True | 距60日低點反彈>50% | distribution_warning | -0.03 | 0.0 | 1 | 0 | 9.17 | 7.82 | -19.84 |  | fail_already_priced_in |
| 6716 | 應廣 | 半導體業 | mainstream_growth |  | 111.75153616840056 | 66.26539158342996 | 2.98 | -3.59 | 24.49 | 59.42 | 76.13 | 76.13 | True | 距60日低點反彈>50% | mild_accumulation | 2.04 | -0.74 | 2 | 0 | 2.48 | 2.97 | -13.57 |  | fail_low_response_condition |
| 6739 | 竹陞科技 | 其他電子業 | mainstream_growth |  | 96.72751410554264 | 97.06337201665968 | 10.85 | 4.91 | -0.84 | -25.4 | 53.8 | 53.8 | True | 距60日低點反彈>50% | distribution_warning | -0.04 | 0.0 | 0 | 0 | 3.82 | 5.53 | -14.23 |  | fail_low_response_condition |
| 6811 | 宏碁資訊 | 數位雲端 | neutral |  | 77.11195291418402 | 25.85246337318264 | -3.42 | 6.9 | 9.09 | 23.08 | 14.29 | 26.98 | False |  | mild_accumulation | 1.37 | -0.06 | 2 | 0 | 0.33 | 0.11 | -11.93 |  | fail_low_response_condition |