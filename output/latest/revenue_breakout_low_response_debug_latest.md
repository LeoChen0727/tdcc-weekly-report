# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-19 23:49:43 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 889 |
| standardized_revenue_rows | 889 |
| price_rows | 594855 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 152 |
| price_metrics_pass | 151 |
| low_response_pass | 21 |
| already_priced_in_excluded | 10 |
| overheat_pass | 11 |
| score_pass | 11 |
| theme_priority_pass | 9 |
| final_rows | 9 |

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
| fail_revenue_condition | 737 |
| fail_low_response_condition | 130 |
| fail_already_priced_in | 10 |
| fail_defensive_or_traditional_excluded | 2 |
| missing_or_insufficient_price_metrics | 1 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1591 | 駿吉-KY | 電機機械 | cyclical_turnaround |  | 219.71633689371387 | 560.9285277947465 | -27.98 | -26.53 | -29.2 | -37.58 | 0.0 | 0.0 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 0 | -21.55 | -26.11 | -55.31 |  | fail_low_response_condition |
| 1595 | 川寶 | 半導體業 | mainstream_growth |  | 173.84980525803311 | -1.0761190409435573 | 2.8 | -19.79 | 82.46 | 109.52 | 92.02 | 110.38 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.63 | -4.2 | 1 | 0 | -3.52 | -2.24 | -28.04 |  | fail_low_response_condition |
| 1780 | 立弘 | 食品工業 | defensive_or_traditional |  | 57.04726554518831 | 21.571303001130133 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | missing_or_insufficient_price_metrics |
| 1781 | 合世 | 生技醫療業 | defensive_or_traditional |  | 89.11606383983379 | -4.203678293733901 | 0.42 | 10.09 | -1.23 | 5.73 | 18.23 | 18.23 | False |  | mild_accumulation | 0.98 | -2.55 | 2 | 0 | 4.05 | 3.58 | -4.76 |  | fail_low_response_condition |
| 1785 | 光洋科 | 其他電子業 | mainstream_growth |  | 95.4717440249422 | 73.6023469794557 | 2.41 | -1.32 | 54.56 | 139.94 | 71.07 | 163.72 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.24 | -4.2 | 1 | 1 | 2.94 | 3.38 | -19.46 |  | fail_already_priced_in |
| 1799 | 易威 | 生技醫療業 | defensive_or_traditional |  | 64.30326328872445 | 80.10002545416836 | 0.82 | -8.9 | -20.26 | -8.77 | 5.5 | 11.03 | False |  | mild_accumulation | 0.32 | -0.04 | 2 | 0 | -5.54 | -6.1 | -31.63 |  | fail_low_response_condition |
| 2073 | 雄順 | 鋼鐵工業 | cyclical_turnaround |  | 111.44875532630634 | 13.803571208213532 | -1.92 | 1.39 | -1.92 | -1.92 | 2.0 | 2.0 | False |  | mild_accumulation | 0.03 | -0.03 | 2 | 0 | -1.35 | -1.71 | -10.53 |  | fail_low_response_condition |
| 2230 | 泰茂 | 居家生活 | neutral |  | 62.61525358875298 | 65.1480007526132 | 4.23 | -5.41 | -13.56 | -72.4 | 5.24 | 5.24 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -2.15 | -2.52 | -28.59 |  | fail_low_response_condition |
| 2596 | 綠意 | 建材營造 | neutral |  | 157.27477860377417 | -30.48785196903357 | 0.82 | 12.61 | -5.81 | -17.43 | 17.11 | 17.11 | False |  | strong_accumulation | 1.04 | 3.45 | 3 | 3 | 5.86 | 3.92 | -6.38 |  | fail_low_response_condition |
| 2724 | 藝舍-KY | 其他 | neutral |  | 287.3424759080801 | 25.35770947318476 | -2.37 | -11.47 | -39.61 | -34.31 | 5.56 | 5.56 | False |  | mild_accumulation | 0.71 | 0.0 | 1 | 0 | -5.15 | -6.52 | -39.46 |  | fail_low_response_condition |
| 3066 | 李洲 | 光電業 | mainstream_growth |  | 83.9535434937189 | 30.77091697817158 | 5.97 | 0.47 | 7.04 | 54.35 | 24.93 | 63.85 | False |  | distribution_warning | -0.52 | -0.04 | 1 | 0 | 0.85 | 2.65 | -11.06 |  | fail_low_response_condition |
| 3073 | 天方能源 | 綠能環保 | neutral |  | 68.92239794041927 | 253.0646367756413 | 4.95 | 4.69 | -24.01 | -32.05 | 7.07 | 7.07 | False |  | strong_accumulation | 0.19 | 0.15 | 2 | 2 | 1.34 | 0.47 | -26.9 |  | fail_low_response_condition |
| 3081 | 聯亞 | 通信網路業 | mainstream_growth |  | 118.83628392642144 | 107.10735429516782 | 12.7 | -16.58 | 41.86 | 317.09 | 58.44 | 311.47 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.13 | -0.63 | 0 | 1 | -3.85 | -1.64 | -26.17 |  | fail_low_response_condition |
| 3085 | 新零售 | 數位雲端 | neutral |  | 80.85255066387141 | 31.133113311331133 | -2.8 | -1.22 | -6.9 | -13.21 | 9.46 | 11.47 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -3.17 | -2.22 | -14.44 |  | fail_low_response_condition |
| 3115 | 富榮綱 | 電子零組件業 | mainstream_growth |  | 428.3870967741936 | 187.4311926605505 | -1.64 | 10.43 | -6.93 | -13.04 | 19.21 | 19.21 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 3.17 | -0.42 | -19.64 |  | fail_low_response_condition |
| 3147 | 大綜 | 資訊服務業 | mainstream_growth |  | 812.4457522257431 | 75.04351412184546 | 2.83 | 73.94 | 100.0 | 96.4 | 113.03 | 115.84 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.65 | 3.1 | 3 | 2 | 25.3 | 21.1 | -7.1 |  | fail_low_response_condition |
| 3171 | 炎洲流通 | 居家生活 | neutral |  | 109.7805751973872 | 94.6972283019752 | -1.65 | 0.99 | 8.98 | 52.99 | 13.47 | 54.98 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -0.06 | 0.49 | -9.82 |  | fail_low_response_condition |
| 3188 | 鑫龍騰 | 建材營造 | neutral |  | 826.2341553353307 | 880.0626237824936 | 0.0 | 7.78 | -12.76 | -19.9 | 12.39 | 12.39 | False |  | distribution_warning | -0.04 | -0.92 | 1 | 0 | 5.53 | 3.08 | -12.61 |  | fail_low_response_condition |
| 3205 | 佰研 | 生技醫療業 | defensive_or_traditional |  | 129.60145788764757 | 68.47281902811075 | -2.77 | -1.31 | -6.9 | 3.54 | 1.94 | 11.68 | False |  | mild_accumulation | 0.07 | 0.0 | 2 | 0 | -2.08 | -2.39 | -21.49 |  | fail_low_response_condition |
| 3260 | 威剛 | 半導體業 | mainstream_growth |  | 210.4355947810273 | 175.82844223209355 | 7.22 | 3.8 | 8.32 | 124.4 | 26.27 | 117.48 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.48 | -2.25 | 1 | 1 | 0.68 | 1.0 | -14.37 |  | fail_already_priced_in |
| 3276 | 宇環 | 電子零組件業 | mainstream_growth |  | 67.31336658223881 | 20.76774563056572 | 4.11 | 6.67 | 10.55 | 0.0 | 12.59 | 13.01 | False |  | mild_accumulation | -0.02 | 0.02 | 2 | 1 | 4.18 | 3.02 | -13.14 |  | fail_low_response_condition |
| 3285 | 微端 | 其他電子業 | mainstream_growth |  | 216.7536335744519 | 71.32173394156858 | 35.99 | 75.64 | 81.56 | 76.25 | 89.28 | 95.42 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.29 | 2.51 | 3 | 3 | 44.49 | 39.52 | 0.0 |  | fail_low_response_condition |
| 3290 | 東浦 | 電子零組件業 | mainstream_growth |  | 96.15981646915073 | 83.08174943599377 | 9.75 | 48.04 | 62.33 | 60.09 | 71.08 | 73.85 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 4.11 | 2.96 | 3 | 2 | 28.57 | 24.79 | -1.55 |  | fail_low_response_condition |
| 3313 | 斐成 | 建材營造 | neutral |  | 12749.180327868851 | 1540.4202719406676 | 3.85 | 4.74 | -7.25 | -19.54 | 12.5 | 12.5 | False |  | mild_accumulation | -0.06 | 0.47 | 1 | 3 | 6.28 | 4.58 | -7.95 |  | fail_low_response_condition |
| 3324 | 雙鴻 | 其他電子業 | mainstream_growth | A_優先追蹤 | 93.75003472065764 | 80.47253733211849 | 7.21 | 5.94 | 7.75 | 9.86 | 22.29 | 22.29 | False |  | mild_accumulation | 0.71 | 1.6 | 1 | 1 | -1.17 | 0.11 | -18.01 | 19 | selected |
| 3354 | 律勝 | 電子零組件業 | mainstream_growth |  | 72.62221041445271 | 29.48090566391159 | 5.07 | -17.04 | 10.67 | 35.27 | 18.64 | 35.92 | False |  | distribution_warning | -0.07 | 0.0 | 1 | 0 | -7.51 | -6.03 | -25.53 |  | fail_low_response_condition |
| 3360 | 尚立 | 電子通路業 | mainstream_growth |  | 125.62116562772736 | 59.94457164554596 | 9.8 | 10.92 | 7.62 | 26.46 | 24.05 | 30.0 | False |  | distribution_warning | -0.8 | 0.0 | 1 | 0 | 10.36 | 8.8 | -4.13 |  | fail_low_response_condition |
| 3390 | 旭軟 | 電子零組件業 | mainstream_growth |  | 66.10699853377677 | 26.55576804184805 | 4.2 | 0.35 | 31.03 | 31.34 | 38.69 | 38.69 | False |  | distribution_warning | -1.89 | 0.0 | 1 | 0 | 1.27 | 2.03 | -7.77 |  | fail_low_response_condition |
| 3465 | 進泰電子 | 其他電子業 | mainstream_growth |  | 190.50131595438023 | 14.137773080688476 | 11.86 | 32.0 | -9.93 | -21.0 | 36.98 | 36.98 | True | 近20日漲幅>25% | distribution_warning | -0.02 | -4.31 | 1 | 1 | 17.91 | 16.31 | -10.15 |  | fail_low_response_condition |
| 3466 | 德晉 | 通信網路業 | mainstream_growth |  | 1974.037442599788 | 1473.309846750044 | 5.9 | 0.76 | -4.87 | -22.43 | 9.93 | 9.93 | False |  | strong_accumulation | 0.1 | 2.55 | 2 | 3 | 1.39 | -0.43 | -27.51 |  | fail_low_response_condition |
| 3491 | 昇達科 | 通信網路業 | mainstream_growth |  | 57.235965671158574 | 66.84291354319335 | -7.14 | -25.36 | -6.31 | 150.0 | 9.47 | 148.8 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.12 | 4.55 | 1 | 3 | -17.31 | -12.35 | -29.09 |  | fail_low_response_condition |
| 3498 | 陽程 | 其他電子業 | mainstream_growth |  | 67.0910241535703 | 97.67221552663295 | 6.49 | -22.64 | 64.88 | 156.25 | 80.09 | 162.26 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.09 | -1.72 | 1 | 0 | -8.92 | -4.61 | -25.23 |  | fail_low_response_condition |
| 3512 | 皇龍 | 建材營造 | neutral |  | 190.4100879516796 | -64.49088145896657 | 0.73 | 2.21 | -2.8 | -5.02 | 4.52 | 5.05 | False |  | distribution_warning | -0.15 | -0.07 | 0 | 0 | 0.74 | 0.52 | -5.45 |  | fail_low_response_condition |
| 3546 | 宇峻 | 文化創意業 | defensive_or_traditional |  | 61.33511348464619 | 48.46909955811981 | 2.51 | 5.53 | 19.14 | 9.15 | 27.83 | 31.75 | False |  | mild_accumulation | 2.06 | 0.0 | 2 | 0 | 3.86 | 4.79 | -1.15 |  | fail_low_response_condition |
| 3555 | 博士旺 | 半導體業 | mainstream_growth |  | 904.2402826855124 | 2643.99235390497 | -3.4 | -14.78 | 30.07 | 127.43 | 34.46 | 149.69 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.06 | -0.07 | 1 | 0 | -5.36 | -4.74 | -29.31 |  | fail_low_response_condition |
| 3594 | 磐儀 | 電腦及週邊設備業 | mainstream_growth |  | 53.26802954536106 | 40.53142459523748 | 4.01 | -7.79 | 21.7 | 26.68 | 25.85 | 36.03 | False |  | mild_accumulation | 1.13 | -0.12 | 1 | 0 | -1.11 | -0.57 | -19.55 |  | fail_low_response_condition |
| 3629 | 地心引力 | 文化創意業 | defensive_or_traditional |  | 1328.0 | 23153.521126760563 | -4.09 | -15.04 | -24.32 | -7.29 | 5.9 | 5.9 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -6.27 | -6.13 | -29.89 |  | fail_low_response_condition |
| 3631 | 晟楠 | 電子零組件業 | mainstream_growth |  | 83.30658105939006 | 11.21441395229546 | 2.56 | -9.93 | 24.54 | 37.37 | 30.77 | 51.11 | False |  | mild_accumulation | 1.11 | 0.0 | 2 | 0 | -2.73 | -2.8 | -20.56 |  | fail_low_response_condition |
| 3672 | 康聯訊 | 通信網路業 | mainstream_growth |  | 87.63020833333333 | -14.885064690365532 | -2.43 | 10.55 | 10.55 | -12.68 | 16.43 | 16.43 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.47 | 4.05 | -16.32 |  | fail_low_response_condition |
| 3691 | 碩禾 | 光電業 | mainstream_growth |  | 131.16545520789458 | 165.32057110145806 | -7.49 | 6.92 | 39.19 | 98.33 | 51.47 | 107.38 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.1 | -1.13 | 1 | 1 | -3.51 | -0.9 | -13.2 |  | fail_already_priced_in |
| 3713 | 新晶投控 | 綠能環保 | neutral |  | 106.34920634920636 | 29.22878241575371 | -2.19 | 20.85 | -7.67 | -31.96 | 25.2 | 25.2 | False |  | strong_accumulation | 0.22 | 1.28 | 3 | 3 | -2.39 | -0.06 | -15.63 |  | fail_low_response_condition |
| 4131 | 浩泰 | 生技醫療業 | defensive_or_traditional |  | 135.43373240915773 | 15.253021148036254 | 2.79 | 8.24 | 2.79 | -7.07 | 12.88 | 12.88 | False |  | distribution_warning | -0.18 | 0.0 | 0 | 0 | 6.12 | 4.19 | -3.79 |  | fail_low_response_condition |
| 4154 | 樂威科-KY | 其他 | neutral |  | 134.11875589066918 | 17.31054131054131 | -8.6 | -8.27 | 12.83 | -18.27 | 15.38 | 35.78 | False |  | mild_accumulation | -0.37 | 0.39 | 2 | 1 | -4.23 | -4.1 | -17.74 |  | fail_low_response_condition |
| 4161 | 聿新科 | 生技醫療業 | defensive_or_traditional |  | 73.81430977345575 | 24.876432426467964 | 1.75 | -0.43 | -7.39 | -9.2 | 2.65 | 2.65 | False |  | mild_accumulation | 0.22 | 1.69 | 3 | 1 | 1.02 | 0.56 | -8.84 |  | fail_low_response_condition |
| 4162 | 智擎 | 生技醫療業 | defensive_or_traditional |  | 51.88562179660102 | 26.68920238317372 | -0.17 | 2.32 | -2.05 | -21.51 | 8.11 | 8.11 | False |  | strong_accumulation | 0.63 | 0.85 | 2 | 2 | 3.04 | 1.88 | -4.66 |  | fail_low_response_condition |
| 4523 | 永彰 | 電機機械 | cyclical_turnaround |  | 72.14966169589658 | 82.91134358916827 | 4.81 | 5.54 | 0.33 | 2.69 | 11.31 | 11.31 | False |  | mild_accumulation | 0.05 | -0.05 | 3 | 1 | 3.4 | 3.49 | -3.33 |  | fail_low_response_condition |
| 4529 | 淳紳 | 其他 | neutral |  | 689.8419864559819 | 228.2959641255605 | -4.78 | -11.65 | 43.11 | 26.12 | 70.11 | 70.11 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -3.33 | -4.11 | -27.36 |  | fail_low_response_condition |
| 4542 | 科嶠 | 電子零組件業 | mainstream_growth |  | 57.55107393699181 | 20.22830374472784 | 33.44 | 53.58 | 131.91 | 401.23 | 167.76 | 399.39 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.94 | -4.62 | 1 | 1 | 35.07 | 33.18 | -1.21 |  | fail_low_response_condition |
| 4702 | 中美實 | 居家生活 | neutral |  | 107.5968992248062 | 3.9315463650212297 | 1.5 | 4.64 | -0.98 | 0.5 | 6.17 | 8.09 | False |  | distribution_warning | -0.22 | -1.59 | 1 | 1 | 1.91 | 1.67 | -3.79 |  | fail_low_response_condition |
| 4714 | 永捷 | 化學工業 | cyclical_turnaround | B_可觀察 | 80.92069964588475 | 92.56251442285505 | -2.25 | -3.33 | -8.42 | -23.68 | 2.35 | 2.35 | False |  | mild_accumulation | -0.18 | 0.23 | 1 | 1 | -3.57 | -3.64 | -25.21 | 16 | selected |
| 4760 | 勤凱科技 | 其他電子業 | mainstream_growth |  | 64.80898590294036 | 56.92625507265585 | 2.88 | 0.0 | 82.04 | 114.29 | 100.0 | 132.2 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.51 | 0.07 | 1 | 1 | -7.65 | -0.99 | -26.47 |  | fail_low_response_condition |
| 4768 | 晶呈科技 | 化學工業 | cyclical_turnaround |  | 64.24352567014994 | 145.4680749912152 | 2.83 | -17.32 | -21.4 | 27.76 | 6.85 | 27.55 | False |  | distribution_warning | -2.99 | -0.03 | 1 | 0 | -12.74 | -10.12 | -34.7 |  | fail_low_response_condition |
| 4772 | 台特化 | 化學工業 | cyclical_turnaround |  | 241.1891244566664 | 260.78257124863404 | 5.64 | -7.72 | -5.23 | -5.07 | 7.66 | 7.66 | False |  | mild_accumulation | -0.49 | 0.08 | 1 | 2 | -3.09 | -2.59 | -18.67 |  | fail_low_response_condition |
| 4806 | 桂田文創 | 文化創意業 | defensive_or_traditional |  | 863.7059724349158 | 225.76994499141583 | -5.96 | 2.5 | -8.89 | 2.5 | 5.67 | 5.67 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 0.62 | -0.05 | -14.58 |  | fail_low_response_condition |
| 4907 | 富宇 | 建材營造 | neutral |  | 216.6538260804732 | 262.6125344300645 | 10.97 | 13.79 | 3.41 | -3.85 | 21.08 | 21.08 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 11.51 | 9.1 | -0.12 |  | fail_low_response_condition |
| 4924 | 欣厚-KY | 綠能環保 | neutral |  | 159.0667744998066 | 38.19968014621888 | -4.6 | -10.59 | 10.68 | 3.17 | 21.41 | 21.41 | False |  | strong_accumulation | 0.36 | 1.84 | 2 | 2 | -5.55 | -4.1 | -12.98 |  | fail_low_response_condition |
| 4931 | 新盛力 | 電腦及週邊設備業 | mainstream_growth |  | 178.64397014885378 | 57.43901205841665 | 11.75 | 17.0 | 80.34 | 41.73 | 101.15 | 119.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.06 | -0.83 | 1 | 2 | 8.27 | 10.6 | -8.89 |  | fail_low_response_condition |
| 4973 | 廣穎電通 | 半導體業 | mainstream_growth |  | 187.1927568325929 | 98.67266191343712 | 1.04 | 63.98 | 216.18 | 439.0 | 216.69 | 432.32 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.02 | -1.08 | 2 | 2 | 12.94 | 16.01 | -11.64 |  | fail_low_response_condition |
| 4991 | 環宇-KY | 半導體業 | mainstream_growth |  | 54.369695427950326 | 55.05158501826551 | 6.79 | -32.62 | 26.91 | 194.03 | 45.88 | 187.31 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.02 | -5.16 | 0 | 0 | -13.86 | -10.66 | -36.76 |  | fail_low_response_condition |
| 5205 | 中茂 | 綠能環保 | neutral |  | 124.65618860510806 | 69.36197094125079 | 5.06 | 5.06 | -13.39 | -18.23 | 25.76 | 25.76 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.02 | 4.0 | -19.42 |  | fail_low_response_condition |
| 5213 | 亞昕 | 建材營造 | neutral |  | 211.33890576943767 | -57.83231080937989 | -1.29 | -12.4 | -14.68 | -6.13 | 3.85 | 3.85 | False |  | mild_accumulation | -0.33 | 0.04 | 0 | 2 | -8.49 | -7.21 | -16.24 |  | fail_low_response_condition |
| 5228 | 鈺鎧 | 電子零組件業 | mainstream_growth |  | 51.87312361310534 | 51.77659185196097 | 5.59 | 37.52 | 212.63 | 299.47 | 235.56 | 331.43 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.43 | -1.13 | 0 | 0 | 11.74 | 15.37 | -7.81 |  | fail_low_response_condition |
| 5263 | 智崴 | 文化創意業 | defensive_or_traditional |  | 61.21424790731411 | 42.10896004509289 | -0.49 | -7.31 | 7.98 | 8.67 | 14.82 | 14.82 | False |  | mild_accumulation | -0.3 | 0.05 | 1 | 1 | -2.68 | -2.34 | -11.74 |  | fail_low_response_condition |
| 5274 | 信驊 | 半導體業 | mainstream_growth |  | 68.73818861369199 | 61.729958331940246 | 7.73 | 6.97 | 64.08 | 188.15 | 77.86 | 188.15 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.48 | -0.02 | 1 | 1 | 4.7 | 6.17 | -2.82 |  | fail_low_response_condition |
| 5289 | 宜鼎 | 電腦及週邊設備業 | mainstream_growth |  | 640.802244561199 | 493.9247662959244 | 12.87 | 14.54 | 101.04 | 293.08 | 127.86 | 290.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.47 | 0.01 | 1 | 2 | 5.41 | 6.94 | -4.69 |  | fail_low_response_condition |
| 5302 | 太欣 | 半導體業 | mainstream_growth |  | 107.48007357449416 | 102.38460228240504 | 14.09 | 25.5 | 10.09 | 39.6 | 29.65 | 41.01 | True | 近20日漲幅>25% | mild_accumulation | 0.67 | 0.0 | 2 | 0 | 12.37 | 11.11 | -4.92 |  | fail_low_response_condition |
| 5310 | 天剛 | 資訊服務業 | mainstream_growth |  | 1485.7142857142858 | -17.93103448275862 | -2.8 | 1.25 | -10.0 | -16.78 | 10.45 | 10.45 | False |  | mild_accumulation | 0.97 | 0.76 | 3 | 1 | 0.55 | -0.4 | -15.77 |  | fail_low_response_condition |
| 5314 | 世紀* | 其他 | neutral | D_降級_TDCC轉弱 | 157.45570866141733 | 160.58565890325826 | 1.03 | -8.81 | -22.47 | -39.8 | 6.69 | 6.69 | False |  | distribution_warning | -1.37 | -1.34 | 0 | 0 | -2.96 | -4.21 | -30.34 | 12 | selected |
| 5345 | 馥鴻 | 其他 | neutral |  | 1505.660377358491 | 510.6753812636165 | -8.49 | 72.53 | 43.78 | 30.44 | 77.26 | 77.26 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | distribution_warning | -0.59 | -0.59 | 0 | 0 | 23.04 | 18.94 | -14.98 |  | fail_low_response_condition |
| 5348 | 正能量智能 | 運動休閒 | neutral |  | 53.49971639251276 | 32.58138458486699 | 0.31 | -9.89 | -6.73 | -7.0 | 10.0 | 10.0 | False |  | mild_accumulation | 0.26 | 0.0 | 2 | 0 | 0.66 | -0.11 | -9.89 |  | fail_low_response_condition |
| 5351 | 鈺創 | 半導體業 | mainstream_growth |  | 605.4820263517354 | 411.4344351891923 | 11.51 | 14.49 | 32.39 | 138.58 | 57.98 | 136.18 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.4 | -0.27 | 2 | 2 | 7.37 | 8.39 | -2.08 |  | fail_low_response_condition |
| 5386 | 青雲 | 電腦及週邊設備業 | mainstream_growth |  | 412.7919634117528 | 510.9980823759461 | 7.87 | -4.58 | 100.0 | 574.87 | 101.94 | 593.74 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.48 | 0.0 | 1 | 0 | -3.16 | 2.4 | -17.04 |  | fail_already_priced_in |
| 5410 | 國眾 | 資訊服務業 | mainstream_growth |  | 199.22657884057065 | 60.05520451885815 | 1.36 | 15.63 | 47.2 | 48.67 | 50.17 | 53.78 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.01 | -2.35 | 1 | 1 | 7.64 | 7.49 | -10.14 |  | fail_already_priced_in |
| 5439 | 高技 | 電子零組件業 | mainstream_growth | D_降級_TDCC轉弱 | 58.304659282636976 | 59.76338375118807 | -3.9 | -13.64 | 9.38 | 5.72 | 24.07 | 36.55 | False |  | distribution_warning | -1.75 | -1.54 | 0 | 1 | -7.77 | -6.52 | -28.26 | 11 | selected |
| 5475 | 德宏 | 電子零組件業 | mainstream_growth |  | 214.9584342703777 | 123.25387942257557 | 5.88 | -12.35 | 18.03 | 203.61 | 27.92 | 205.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.78 | 0.23 | 2 | 1 | -6.03 | -5.66 | -37.7 |  | fail_already_priced_in |
| 5498 | 凱崴 | 電子零組件業 | mainstream_growth |  | 86.3193558161101 | 57.82371596014622 | 0.6 | -1.9 | 19.4 | 81.84 | 29.29 | 75.65 | True | 近120日漲幅>70% | mild_accumulation | 1.92 | 1.87 | 2 | 1 | 3.06 | 2.02 | -23.05 |  | fail_already_priced_in |
| 5508 | 永信建 | 建材營造 | neutral |  | 116.37225189625435 | 3.136885648699773 | 12.39 | 30.58 | 19.81 | -5.08 | 35.6 | 35.6 | True | 近20日漲幅>25% | mild_accumulation | -0.42 | 0.01 | 1 | 1 | 17.83 | 15.01 | -2.06 |  | fail_low_response_condition |
| 5514 | 三豐 | 建材營造 | neutral |  | 545.4183266932271 | 27801.12126245848 | 1.81 | -7.57 | -11.64 | -15.36 | 7.66 | 7.66 | False |  | mild_accumulation | -0.03 | 0.01 | 1 | 1 | -0.53 | -1.69 | -16.37 |  | fail_low_response_condition |
| 5516 | 雙喜 | 建材營造 | neutral |  | 93.66502038023266 | 40.95635213400519 | 1.83 | 8.78 | -12.2 | -22.03 | 10.95 | 10.95 | False |  | distribution_warning | -0.93 | -2.45 | 0 | 0 | 4.94 | 3.12 | -15.21 |  | fail_low_response_condition |
| 5864 | 致和證 | 金融業 | defensive_or_traditional |  | 350.19622607796714 | 2479.527079224786 | 14.07 | 45.33 | 99.39 | 245.42 | 112.8 | 243.01 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.64 | 1 | 2 | 7.6 | 11.15 | -8.49 |  | fail_low_response_condition |
| 6016 | 康和證 | 金融業 | defensive_or_traditional |  | 231.1165002789404 | 2150.902577889129 | 6.27 | 22.55 | 67.93 | 121.54 | 76.69 | 122.39 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.08 | -5.21 | 0 | 0 | -3.54 | 1.6 | -21.1 |  | fail_already_priced_in |
| 6020 | 大展證 | 金融業 | defensive_or_traditional |  | 1284.9769830028329 | 35336.78678678679 | 4.11 | 2.24 | 17.22 | 21.28 | 21.28 | 22.58 | False |  | mild_accumulation | -0.58 | 0.06 | 0 | 1 | -2.58 | 0.11 | -12.81 |  | fail_low_response_condition |
| 6021 | 美好證 | 金融業 | defensive_or_traditional |  | 830.6472568897998 | 16709.70054829186 | 6.71 | 28.42 | 35.8 | 67.41 | 47.42 | 67.41 | True | 近20日漲幅>25% | distribution_warning | -0.1 | -0.02 | 2 | 1 | 5.65 | 7.05 | -6.87 |  | fail_low_response_condition |
| 6023 | 元大期貨 | 金融業 | defensive_or_traditional |  | 80.3824419941387 | 29.22341641893437 | 1.01 | 2.15 | 4.06 | 4.28 | 4.6 | 7.87 | False |  | strong_accumulation | 0.15 | 0.32 | 2 | 2 | 0.43 | 0.51 | -2.44 |  | fail_low_response_condition |
| 6101 | 寬魚國際 | 文化創意業 | defensive_or_traditional |  | 224.2759693633317 | 212.49587530318647 | 6.11 | -0.48 | 9.03 | 11.96 | 14.27 | 17.66 | False |  | distribution_warning | -0.82 | -0.07 | 0 | 2 | 3.53 | 3.82 | -2.23 |  | fail_low_response_condition |
| 6111 | 光聚晶電 | 文化創意業 | defensive_or_traditional |  | 253.9600301050991 | 151.7320498828784 | 1.7 | -2.4 | 4.68 | -3.87 | 12.16 | 12.16 | False |  | strong_accumulation | 0.76 | 0.8 | 3 | 3 | 0.57 | -0.31 | -11.39 |  | fail_low_response_condition |
| 6113 | 亞矽 | 電子通路業 | mainstream_growth |  | 66.88659649857743 | 37.95758290325541 | 4.6 | 4.41 | 43.07 | 41.65 | 52.69 | 52.69 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.83 | 1.88 | 2 | 2 | 5.0 | 5.94 | -6.43 |  | fail_low_response_condition |
| 6125 | 廣運 | 電機機械 | cyclical_turnaround | D_僅留完整清單 | 79.19877909194963 | 45.54169719365739 | 6.18 | -2.75 | 12.17 | -3.78 | 23.5 | 23.5 | False |  | mild_accumulation | -0.07 | 1.35 | 2 | 2 | -1.84 | 1.62 | -16.21 | 15 | selected |
| 6126 | 信音 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 56.38171710218037 | 49.66796148784725 | -3.01 | 11.33 | 31.7 | 29.58 | 39.69 | 39.69 | False |  | strong_accumulation | 3.18 | 4.09 | 3 | 2 | 3.47 | 4.15 | -9.44 | 19 | selected |
| 6134 | 萬旭 | 電子零組件業 | mainstream_growth | A_優先追蹤 | 63.51463391370063 | 52.1554016481993 | 0.28 | 10.92 | 20.3 | 35.69 | 29.04 | 35.69 | False |  | mild_accumulation | 0.3 | 0.0 | 1 | 1 | 0.01 | 2.02 | -14.95 | 18 | selected |
| 6161 | 捷波 | 電腦及週邊設備業 | mainstream_growth |  | 82.74287656488983 | 28.47706568483651 | -2.04 | -10.66 | 28.94 | 18.65 | 34.35 | 34.35 | False |  | distribution_warning | -0.11 | 0.0 | 0 | 0 | -5.64 | -1.26 | -18.77 |  | fail_low_response_condition |
| 6171 | 大城地產 | 建材營造 | neutral |  | 53503.030303030304 | 675.0912523599749 | 3.75 | 3.75 | -10.59 | -9.95 | 8.03 | 8.03 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 1 | 4.6 | 3.31 | -11.55 |  | fail_low_response_condition |
| 6179 | 亞通 | 其他 | neutral |  | 121.75087091958048 | 68.29271469695588 | 14.78 | 7.85 | 4.69 | -8.06 | 22.65 | 22.65 | False |  | distribution_warning | -2.29 | -2.05 | 0 | 0 | 11.12 | 9.59 | -1.29 |  | fail_low_response_condition |
| 6199 | 天品 | 其他 | neutral | B_可觀察 | 724.1009386809703 | 914.4808811408876 | 4.66 | 2.43 | -7.34 | 3.06 | 15.96 | 15.96 | False |  | mild_accumulation | 1.06 | 2.03 | 2 | 1 | 8.7 | 6.78 | -20.78 | 16 | selected |
| 6217 | 中探針 | 電子零組件業 | mainstream_growth |  | 51.17778846404754 | 36.31497905523737 | 8.33 | -13.49 | 34.24 | 389.11 | 51.07 | 407.19 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.51 | -3.83 | 1 | 1 | -6.19 | -3.91 | -33.42 |  | fail_low_response_condition |
| 6219 | 富旺 | 建材營造 | neutral |  | 7033.766233766234 | 18538.71359223301 | 2.39 | 9.83 | -13.47 | -36.54 | 12.72 | 12.72 | False |  | strong_accumulation | 1.3 | 0.3 | 3 | 2 | 2.15 | 0.87 | -14.33 |  | fail_low_response_condition |
| 6223 | 旺矽 | 半導體業 | mainstream_growth |  | 57.81298997442514 | 46.20299555286819 | 5.34 | 3.47 | 75.03 | 178.31 | 85.14 | 216.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.57 | -6.0 | 1 | 2 | 6.2 | 6.73 | -7.7 |  | fail_low_response_condition |
| 6229 | 研通 | 半導體業 | mainstream_growth |  | 76.70780960505445 | 53.80581816729727 | 5.92 | 0.54 | 30.28 | 24.44 | 38.75 | 38.75 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | 3.9 | 3.88 | -11.2 |  | fail_low_response_condition |
| 6264 | 富裔 | 建材營造 | neutral |  | 226.0680557637536 | 58.63577003674796 | -1.48 | -0.5 | -5.06 | -17.67 | 4.52 | 4.52 | False |  | strong_accumulation | 0.08 | 0.08 | 3 | 3 | -0.9 | -1.02 | -8.52 |  | fail_low_response_condition |
| 6265 | 方土昶 | 電子通路業 | mainstream_growth |  | 1076.3549823430062 | 648.3820919234922 | -0.17 | 8.88 | 49.61 | 180.29 | 64.34 | 181.66 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 2.63 | 2 | 2 | 1.44 | 4.86 | -10.97 |  | fail_already_priced_in |
| 6274 | 台燿 | 電子零組件業 | mainstream_growth |  | 128.48732779782807 | 80.25773721086192 | 24.41 | 14.69 | 193.13 | 329.74 | 225.93 | 319.91 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.13 | -2.26 | 0 | 0 | 13.43 | 17.78 | 0.0 |  | fail_low_response_condition |
| 6292 | 迅德 | 電子零組件業 | mainstream_growth |  | 79.8700016455488 | 34.01579180294248 | 15.11 | 17.1 | 41.1 | 67.61 | 55.86 | 73.4 | True | 近60日漲幅>40%；距60日低點反彈>50% | neutral | 0.0 | 0.0 | 0 | 0 | 6.53 | 10.12 | -8.38 |  | fail_low_response_condition |
| 6419 | 京晨科 | 光電業 | mainstream_growth |  | 368.78637424785455 | 135.8943019763131 | 6.79 | -1.64 | 64.83 | 99.87 | 73.64 | 133.23 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | 5.56 | 4.81 | -23.14 |  | fail_low_response_condition |
| 6462 | 神盾 | 半導體業 | mainstream_growth |  | 135.52158343846233 | 97.64657459987085 | 3.64 | -26.45 | 8.06 | -9.16 | 17.28 | 19.12 | False |  | distribution_warning | -5.84 | -5.02 | 0 | 1 | -4.24 | -4.02 | -28.97 |  | fail_low_response_condition |
| 6465 | 威潤 | 通信網路業 | mainstream_growth |  | 169.583931133429 | 93.13670993689304 | 28.52 | 38.79 | 57.52 | 84.94 | 69.12 | 130.79 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.18 | 0.0 | 2 | 0 | 29.12 | 25.63 | -8.01 |  | fail_low_response_condition |
| 6494 | 九齊 | 半導體業 | mainstream_growth |  | 79.43355218989315 | 43.11525942708911 | 22.48 | 20.98 | 52.42 | 93.03 | 63.4 | 99.71 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.41 | 0.0 | 1 | 0 | 17.61 | 16.85 | -1.84 |  | fail_low_response_condition |
| 6576 | 逸達 | 生技醫療業 | defensive_or_traditional |  | 749.5590449559045 | 36.985314582276 | -0.76 | 0.0 | 0.9 | -0.13 | 4.39 | 4.39 | False |  | strong_accumulation | 0.31 | 0.37 | 2 | 2 | 0.69 | -0.1 | -6.33 |  | fail_low_response_condition |
| 6588 | 東典光電 | 通信網路業 | mainstream_growth |  | 159.9830396683313 | 165.38190032472116 | 8.15 | -17.62 | -8.9 | 128.72 | 13.52 | 131.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.53 | -0.08 | 0 | 0 | -2.8 | -4.72 | -35.44 |  | fail_low_response_condition |
| 6596 | 寬宏藝術 | 文化創意業 | defensive_or_traditional |  | 122.48698203153648 | 91.71375346744868 | 0.0 | -3.79 | -18.61 | -34.27 | 1.84 | 1.84 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -1.7 | -2.06 | -16.07 |  | fail_low_response_condition |
| 6613 | 朋億* | 其他電子業 | mainstream_growth |  | 81.72059250458541 | 25.75033629369081 | 33.16 | 40.0 | 85.64 | 97.16 | 94.15 | 113.73 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.66 | 0.0 | 1 | 0 | 33.25 | 30.46 | -0.13 |  | fail_low_response_condition |
| 6617 | 共信-KY | 生技醫療業 | defensive_or_traditional |  | 68.48115721355158 | 25.969105217137862 | -0.73 | 3.36 | -0.29 | -20.47 | 15.95 | 15.95 | False |  | strong_accumulation | 0.17 | 0.16 | 2 | 2 | -2.35 | -0.77 | -15.82 |  | fail_low_response_condition |
| 6629 | 泰金-KY | 居家生活 | neutral |  | 90.1053928142166 | 88.43635222920778 | 0.88 | -3.8 | 8.06 | -12.31 | 10.68 | 12.87 | False |  | mild_accumulation | 0.16 | 0.0 | 1 | 0 | -2.06 | -2.25 | -16.79 |  | fail_low_response_condition |
| 6654 | 天正國際 | 其他電子業 | mainstream_growth |  | 106.68524559014472 | 77.30403434460713 | 29.55 | 105.69 | 140.84 | 152.33 | 155.9 | 171.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.07 | 0.0 | 3 | 0 | 28.65 | 31.42 | -10.33 |  | fail_low_response_condition |
| 6693 | 廣閎科 | 半導體業 | mainstream_growth |  | 115.16072542823213 | 78.42165561482598 | 38.71 | 45.27 | 101.88 | 184.77 | 111.82 | 184.77 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | 0.0 | 2 | 0 | 31.44 | 29.25 | 0.0 |  | fail_low_response_condition |
| 6727 | 亞泰金屬 | 電子零組件業 | mainstream_growth |  | 54.1070669876788 | 112.73549191644769 | 14.25 | -31.97 | 49.67 | 138.2 | 56.17 | 171.3 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.24 | -2.47 | 1 | 1 | -9.83 | -4.64 | -35.58 |  | fail_low_response_condition |
| 6735 | 美達科技 | 其他電子業 | mainstream_growth |  | 155.07788585810488 | 67.66569790909824 | 4.89 | -14.57 | 62.2 | 68.57 | 71.32 | 85.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.64 | 0.0 | 1 | 0 | -5.92 | -5.38 | -36.86 |  | fail_low_response_condition |
| 6739 | 竹陞科技 | 其他電子業 | mainstream_growth |  | 99.25885395941106 | 95.52796729930556 | 1.82 | -17.34 | -8.94 | 54.27 | 3.23 | 62.08 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | -7.84 | -7.59 | -36.36 |  | fail_low_response_condition |
| 6870 | 騰雲 | 數位雲端 | neutral |  | 56.14728080694082 | 48.35214011534826 | -4.83 | 22.53 | 49.87 | 10.23 | 70.96 | 70.96 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -1.18 | 3.38 | 1 | 2 | 1.65 | 5.25 | -14.01 |  | fail_low_response_condition |
| 6894 | 衛司特 | 綠能環保 | neutral |  | 92.69510884705696 | 71.87896672768468 | 9.18 | 0.0 | 7.0 | 92.05 | 24.83 | 96.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | 0.0 | 0 | 0 | 0.62 | 2.96 | -10.41 |  | fail_low_response_condition |
| 6903 | 巨漢 | 其他電子業 | mainstream_growth |  | 229.1376005375176 | 312.2566060056191 | 6.79 | -5.42 | 32.77 | 70.87 | 42.39 | 85.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.24 | -0.13 | 2 | 0 | -0.74 | 0.14 | -12.96 |  | fail_low_response_condition |