# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-16 23:10:59 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 888 |
| standardized_revenue_rows | 888 |
| price_rows | 585045 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 422 |
| tdcc_mild_accumulation_count | 721 |
| tdcc_distribution_warning_count | 681 |
| revenue_condition_pass | 151 |
| price_metrics_pass | 151 |
| low_response_pass | 0 |
| already_priced_in_excluded | 0 |
| overheat_pass | 0 |
| score_pass | 0 |
| theme_priority_pass | 0 |
| final_rows | 0 |

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
| fail_low_response_condition | 151 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1591 | 駿吉-KY | 電機機械 | cyclical_turnaround |  | 219.71633689371387 | 560.9285277947465 | 1.99 | -22.2 | -9.39 | -20.39 | 26.15 | 26.15 | False |  | distribution_warning | -0.02 | 0.0 | 1 | 0 | -1.39 | -8.02 | -41.18 |  | fail_low_response_condition |
| 1595 | 川寶 | 半導體業 | mainstream_growth |  | 173.84980525803311 | -1.0761190409435573 | -3.51 | -16.23 | 70.41 | 99.73 | 85.29 | 103.84 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.63 | -4.2 | 1 | 0 | -13.06 | -7.98 | -30.56 |  | fail_low_response_condition |
| 1781 | 合世 | 生技醫療業 | defensive_or_traditional |  | 89.11606383983379 | -4.203678293733901 | 0.0 | 14.29 | -2.04 | 7.14 | 18.23 | 18.23 | False |  | mild_accumulation | 0.98 | -2.55 | 2 | 0 | 6.57 | 5.48 | -4.76 |  | fail_low_response_condition |
| 1785 | 光洋科 | 其他電子業 | mainstream_growth |  | 95.4717440249422 | 73.6023469794557 | 2.15 | 3.26 | 49.06 | 120.25 | 63.61 | 152.21 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.24 | -4.2 | 1 | 1 | -2.8 | -2.5 | -22.97 |  | fail_low_response_condition |
| 1799 | 易威 | 生技醫療業 | defensive_or_traditional |  | 64.30326328872445 | 80.10002545416836 | -10.76 | -10.89 | -18.78 | -9.04 | 5.5 | 11.03 | False |  | mild_accumulation | 0.32 | -0.04 | 2 | 0 | -7.22 | -8.07 | -31.63 |  | fail_low_response_condition |
| 2073 | 雄順 | 鋼鐵工業 | cyclical_turnaround |  | 111.44875532630634 | 13.803571208213532 | -1.92 | -6.76 | -2.49 | -1.92 | 2.0 | 2.0 | False |  | mild_accumulation | 0.03 | -0.03 | 2 | 0 | -1.78 | -2.05 | -10.53 |  | fail_low_response_condition |
| 2230 | 泰茂 | 居家生活 | neutral |  | 62.61525358875298 | 65.1480007526132 | -7.26 | -8.71 | -20.12 | -73.8 | 1.16 | 1.16 | False |  | strong_accumulation | 0.14 | 0.18 | 2 | 3 | -7.17 | -7.26 | -30.96 |  | fail_low_response_condition |
| 2596 | 綠意 | 建材營造 | neutral |  | 157.27477860377417 | -30.48785196903357 | 2.36 | 5.39 | -8.73 | -11.79 | 15.21 | 15.21 | False |  | strong_accumulation | 1.04 | 3.45 | 3 | 3 | 5.82 | 3.76 | -8.73 |  | fail_low_response_condition |
| 2724 | 藝舍-KY | 其他 | neutral |  | 287.3424759080801 | 25.35770947318476 | -3.08 | -11.58 | -32.44 | -31.15 | 4.13 | 4.13 | False |  | mild_accumulation | 0.71 | 0.0 | 1 | 0 | -5.79 | -7.03 | -38.39 |  | fail_low_response_condition |
| 3066 | 李洲 | 光電業 | mainstream_growth |  | 83.9535434937189 | 30.77091697817158 | -15.03 | -1.93 | -9.96 | 48.0 | 19.35 | 56.54 | False |  | distribution_warning | -0.52 | -0.04 | 1 | 0 | -3.71 | -1.91 | -15.03 |  | fail_low_response_condition |
| 3073 | 天方能源 | 綠能環保 | neutral |  | 68.92239794041927 | 253.0646367756413 | -17.74 | 0.49 | -28.55 | -33.33 | 3.03 | 3.03 | False |  | strong_accumulation | 0.19 | 0.15 | 2 | 2 | -1.71 | -3.79 | -32.0 |  | fail_low_response_condition |
| 3081 | 聯亞 | 通信網路業 | mainstream_growth |  | 118.83628392642144 | 107.10735429516782 | -11.63 | -11.63 | 39.02 | 272.55 | 66.42 | 295.15 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.13 | -0.63 | 0 | 1 | -13.06 | -10.61 | -31.01 |  | fail_low_response_condition |
| 3085 | 新零售 | 數位雲端 | neutral |  | 80.85255066387141 | 31.133113311331133 | -2.72 | 4.17 | 9.65 | -17.49 | 14.68 | 14.68 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.83 | 0.23 | -11.97 |  | fail_low_response_condition |
| 3115 | 富榮綱 | 電子零組件業 | mainstream_growth |  | 428.3870967741936 | 187.4311926605505 | 2.36 | -2.99 | -7.34 | -12.17 | 20.4 | 20.4 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 5.85 | 1.79 | -18.84 |  | fail_low_response_condition |
| 3147 | 大綜 | 資訊服務業 | mainstream_growth |  | 812.4457522257431 | 75.04351412184546 | 31.33 | 96.08 | 102.31 | 105.88 | 128.01 | 131.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.65 | 3.1 | 3 | 2 | 53.09 | 44.52 | -0.57 |  | fail_low_response_condition |
| 3171 | 炎洲流通 | 居家生活 | neutral |  | 109.7805751973872 | 94.6972283019752 | -0.28 | 7.04 | 15.51 | 50.21 | 19.17 | 56.11 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 1.56 | 1.56 | -4.54 |  | fail_low_response_condition |
| 3188 | 鑫龍騰 | 建材營造 | neutral |  | 826.2341553353307 | 880.0626237824936 | 4.71 | 0.41 | -28.3 | -22.01 | 10.14 | 10.14 | False |  | distribution_warning | -0.04 | -0.92 | 1 | 0 | 4.11 | 2.2 | -27.66 |  | fail_low_response_condition |
| 3205 | 佰研 | 生技醫療業 | defensive_or_traditional |  | 129.60145788764757 | 68.47281902811075 | -6.05 | -2.04 | 5.6 | 3.53 | 6.34 | 12.1 | False |  | mild_accumulation | 0.07 | 0.0 | 2 | 0 | -2.19 | -2.66 | -21.19 |  | fail_low_response_condition |
| 3260 | 威剛 | 半導體業 | mainstream_growth |  | 210.4355947810273 | 175.82844223209355 | -8.95 | 2.84 | -8.85 | 124.8 | 24.85 | 136.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.48 | -2.25 | 1 | 1 | -0.99 | -1.27 | -15.59 |  | fail_low_response_condition |
| 3276 | 宇環 | 電子零組件業 | mainstream_growth |  | 67.31336658223881 | 20.76774563056572 | 3.36 | 10.0 | 10.39 | 4.41 | 14.5 | 14.5 | False |  | mild_accumulation | -0.02 | 0.02 | 2 | 1 | 6.12 | 4.6 | -12.0 |  | fail_low_response_condition |
| 3285 | 微端 | 其他電子業 | mainstream_growth |  | 216.7536335744519 | 71.32173394156858 | 38.35 | 61.4 | 58.08 | 55.67 | 75.57 | 75.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.29 | 2.51 | 3 | 3 | 39.73 | 35.16 | -4.27 |  | fail_low_response_condition |
| 3290 | 東浦 | 電子零組件業 | mainstream_growth |  | 96.15981646915073 | 83.08174943599377 | 31.74 | 41.78 | 49.66 | 50.68 | 61.76 | 64.38 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 4.11 | 2.96 | 3 | 2 | 28.37 | 25.13 | -0.3 |  | fail_low_response_condition |
| 3313 | 斐成 | 建材營造 | neutral |  | 12749.180327868851 | 1540.4202719406676 | 2.65 | -2.52 | -9.38 | -25.16 | 7.41 | 7.41 | False |  | mild_accumulation | -0.06 | 0.47 | 1 | 3 | 1.47 | 0.75 | -16.85 |  | fail_low_response_condition |
| 3324 | 雙鴻 | 其他電子業 | mainstream_growth |  | 93.75003472065764 | 80.47253733211849 | -11.39 | 11.82 | -1.41 | 14.38 | 20.0 | 20.0 | False |  | mild_accumulation | 0.71 | 1.6 | 1 | 1 | -1.68 | -2.17 | -19.54 |  | fail_low_response_condition |
| 3354 | 律勝 | 電子零組件業 | mainstream_growth |  | 72.62221041445271 | 29.48090566391159 | -11.25 | -13.07 | -2.13 | 30.5 | 16.95 | 42.27 | False |  | distribution_warning | -0.07 | 0.0 | 1 | 0 | -13.08 | -10.31 | -26.6 |  | fail_low_response_condition |
| 3360 | 尚立 | 電子通路業 | mainstream_growth |  | 125.62116562772736 | 59.94457164554596 | 3.03 | 6.62 | -0.97 | 14.61 | 16.79 | 22.4 | False |  | distribution_warning | -0.8 | 0.0 | 1 | 0 | 4.54 | 4.27 | -9.73 |  | fail_low_response_condition |
| 3390 | 旭軟 | 電子零組件業 | mainstream_growth |  | 66.10699853377677 | 26.55576804184805 | 2.17 | 4.81 | 28.64 | 26.62 | 37.71 | 37.71 | False |  | distribution_warning | -1.89 | 0.0 | 1 | 0 | -0.34 | 1.17 | -8.41 |  | fail_low_response_condition |
| 3465 | 進泰電子 | 其他電子業 | mainstream_growth |  | 190.50131595438023 | 14.137773080688476 | -5.96 | 12.15 | -30.23 | -34.07 | 13.21 | 13.21 | False |  | distribution_warning | -0.02 | -4.31 | 1 | 1 | 1.76 | -0.86 | -30.15 |  | fail_low_response_condition |
| 3466 | 德晉 | 通信網路業 | mainstream_growth |  | 1974.037442599788 | 1473.309846750044 | 2.13 | -3.03 | -6.55 | -25.86 | 11.09 | 11.09 | False |  | strong_accumulation | 0.1 | 2.55 | 2 | 3 | 1.91 | 0.06 | -26.75 |  | fail_low_response_condition |
| 3491 | 昇達科 | 通信網路業 | mainstream_growth |  | 57.235965671158574 | 66.84291354319335 | -19.49 | -10.54 | 8.28 | 154.05 | 25.6 | 167.01 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -1.12 | 4.55 | 1 | 3 | -19.73 | -15.5 | -28.64 |  | fail_low_response_condition |
| 3498 | 陽程 | 其他電子業 | mainstream_growth |  | 67.0910241535703 | 97.67221552663295 | -9.06 | -16.03 | 65.29 | 149.22 | 76.43 | 156.93 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.09 | -1.72 | 1 | 0 | -15.79 | -8.66 | -26.75 |  | fail_low_response_condition |
| 3512 | 皇龍 | 建材營造 | neutral |  | 190.4100879516796 | -64.49088145896657 | 0.24 | 2.71 | 0.0 | -4.58 | 4.77 | 5.3 | False |  | distribution_warning | -0.15 | -0.07 | 0 | 0 | 1.47 | 0.99 | -5.23 |  | fail_low_response_condition |
| 3546 | 宇峻 | 文化創意業 | defensive_or_traditional |  | 61.33511348464619 | 48.46909955811981 | 4.72 | 6.52 | 20.28 | 6.65 | 28.87 | 32.82 | False |  | mild_accumulation | 2.06 | 0.0 | 2 | 0 | 5.46 | 7.12 | -0.23 |  | fail_low_response_condition |
| 3555 | 博士旺 | 半導體業 | mainstream_growth |  | 904.2402826855124 | 2643.99235390497 | -14.81 | 1.79 | -2.7 | 136.59 | 36.43 | 149.06 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.06 | -0.07 | 1 | 0 | -9.18 | -7.6 | -29.48 |  | fail_low_response_condition |
| 3594 | 磐儀 | 電腦及週邊設備業 | mainstream_growth |  | 53.26802954536106 | 40.53142459523748 | -2.07 | -2.37 | 16.07 | 22.06 | 24.15 | 34.18 | False |  | mild_accumulation | 1.13 | -0.12 | 1 | 0 | -5.32 | -3.98 | -20.64 |  | fail_low_response_condition |
| 3629 | 地心引力 | 文化創意業 | defensive_or_traditional |  | 1328.0 | 23153.521126760563 | -8.81 | -9.91 | -25.0 | -8.81 | 4.17 | 4.17 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -8.93 | -8.7 | -31.03 |  | fail_low_response_condition |
| 3631 | 晟楠 | 電子零組件業 | mainstream_growth |  | 83.30658105939006 | 11.21441395229546 | 0.58 | -8.15 | 14.59 | 46.23 | 34.42 | 55.33 | False |  | mild_accumulation | 1.11 | 0.0 | 2 | 0 | -3.1 | -2.1 | -18.34 |  | fail_low_response_condition |
| 3672 | 康聯訊 | 通信網路業 | mainstream_growth |  | 87.63020833333333 | -14.885064690365532 | 3.54 | 5.41 | 2.18 | -13.33 | 13.04 | 13.04 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 3.49 | 2.46 | -18.75 |  | fail_low_response_condition |
| 3691 | 碩禾 | 光電業 | mainstream_growth |  | 131.16545520789458 | 165.32057110145806 | -4.56 | 12.95 | 35.34 | 99.24 | 53.92 | 110.74 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.1 | -1.13 | 1 | 1 | 0.51 | 1.7 | -11.3 |  | fail_low_response_condition |
| 3713 | 新晶投控 | 綠能環保 | neutral |  | 106.34920634920636 | 29.22878241575371 | -9.88 | 19.23 | -8.82 | -33.19 | 24.0 | 24.0 | False |  | strong_accumulation | 0.22 | 1.28 | 3 | 3 | 1.47 | -0.1 | -16.44 |  | fail_low_response_condition |
| 4131 | 浩泰 | 生技醫療業 | defensive_or_traditional |  | 135.43373240915773 | 15.253021148036254 | 12.44 | 6.69 | 2.74 | -5.78 | 15.03 | 15.03 | False |  | distribution_warning | -0.18 | 0.0 | 0 | 0 | 9.41 | 8.27 | -1.96 |  | fail_low_response_condition |
| 4154 | 樂威科-KY | 其他 | neutral |  | 134.11875589066918 | 17.31054131054131 | 0.38 | -4.36 | 28.92 | -16.51 | 27.67 | 40.04 | False |  | mild_accumulation | -0.37 | 0.39 | 2 | 1 | -2.59 | -1.48 | -15.16 |  | fail_low_response_condition |
| 4161 | 聿新科 | 生技醫療業 | defensive_or_traditional |  | 73.81430977345575 | 24.876432426467964 | -0.43 | -1.5 | -7.26 | -12.55 | 1.77 | 1.77 | False |  | mild_accumulation | 0.22 | 1.69 | 3 | 1 | -0.48 | -0.52 | -10.51 |  | fail_low_response_condition |
| 4162 | 智擎 | 生技醫療業 | defensive_or_traditional |  | 51.88562179660102 | 26.68920238317372 | 1.44 | 0.89 | -2.92 | -19.74 | 6.6 | 6.6 | False |  | strong_accumulation | 0.63 | 0.85 | 2 | 2 | 1.82 | 1.21 | -5.99 |  | fail_low_response_condition |
| 4523 | 永彰 | 電機機械 | cyclical_turnaround |  | 72.14966169589658 | 82.91134358916827 | -3.15 | 5.03 | -5.03 | -11.63 | 6.17 | 6.36 | False |  | mild_accumulation | 0.05 | -0.05 | 3 | 1 | -0.32 | -0.91 | -7.29 |  | fail_low_response_condition |
| 4529 | 淳紳 | 其他 | neutral |  | 689.8419864559819 | 228.2959641255605 | 0.61 | -18.91 | 49.39 | 27.06 | 75.44 | 75.44 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -3.74 | -1.27 | -25.08 |  | fail_low_response_condition |
| 4542 | 科嶠 | 電子零組件業 | mainstream_growth |  | 57.55107393699181 | 20.22830374472784 | 36.15 | 50.0 | 79.24 | 370.12 | 132.89 | 387.6 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.94 | -4.62 | 1 | 1 | 26.17 | 28.29 | -3.8 |  | fail_low_response_condition |
| 4702 | 中美實 | 居家生活 | neutral |  | 107.5968992248062 | 3.9315463650212297 | -0.98 | 4.55 | -1.46 | 1.2 | 5.65 | 7.56 | False |  | distribution_warning | -0.22 | -1.59 | 1 | 1 | 2.41 | 1.87 | -4.27 |  | fail_low_response_condition |
| 4714 | 永捷 | 化學工業 | cyclical_turnaround |  | 80.92069964588475 | 92.56251442285505 | -5.0 | 1.92 | -11.33 | -20.6 | 3.5 | 3.5 | False |  | mild_accumulation | -0.18 | 0.23 | 1 | 1 | -1.83 | -2.85 | -23.78 |  | fail_low_response_condition |
| 4760 | 勤凱科技 | 其他電子業 | mainstream_growth |  | 64.80898590294036 | 56.92625507265585 | -3.7 | 38.3 | 109.68 | 110.81 | 119.72 | 141.49 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -3.51 | 0.07 | 1 | 1 | -1.52 | 3.14 | -23.53 |  | fail_low_response_condition |
| 4768 | 晶呈科技 | 化學工業 | cyclical_turnaround |  | 64.24352567014994 | 145.4680749912152 | -16.19 | -5.55 | -21.36 | 55.06 | 7.13 | 59.58 | False |  | distribution_warning | -2.99 | -0.03 | 1 | 0 | -15.49 | -13.92 | -34.53 |  | fail_low_response_condition |
| 4772 | 台特化 | 化學工業 | cyclical_turnaround |  | 241.1891244566664 | 260.78257124863404 | -8.33 | -5.01 | -9.84 | -10.71 | 5.36 | 5.36 | False |  | mild_accumulation | -0.49 | 0.08 | 1 | 2 | -7.1 | -6.36 | -20.41 |  | fail_low_response_condition |
| 4806 | 桂田文創 | 文化創意業 | defensive_or_traditional |  | 863.7059724349158 | 225.76994499141583 | 5.5 | 5.5 | -12.81 | 1.93 | 8.76 | 8.76 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | 3.2 | 2.53 | -12.81 |  | fail_low_response_condition |
| 4907 | 富宇 | 建材營造 | neutral |  | 216.6538260804732 | 262.6125344300645 | 5.67 | 6.77 | 0.0 | -3.42 | 16.81 | 16.81 | False |  | mild_accumulation | 0.04 | 0.0 | 2 | 0 | 8.73 | 7.2 | -2.38 |  | fail_low_response_condition |
| 4924 | 欣厚-KY | 綠能環保 | neutral |  | 159.0667744998066 | 38.19968014621888 | -5.16 | 6.7 | 14.35 | 3.91 | 27.26 | 27.26 | False |  | strong_accumulation | 0.36 | 1.84 | 2 | 2 | -2.09 | -0.02 | -8.78 |  | fail_low_response_condition |
| 4931 | 新盛力 | 電腦及週邊設備業 | mainstream_growth |  | 178.64397014885378 | 57.43901205841665 | -3.65 | 32.19 | 78.93 | 40.73 | 92.69 | 110.5 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.06 | -0.83 | 1 | 2 | 9.62 | 11.59 | -8.58 |  | fail_low_response_condition |
| 4973 | 廣穎電通 | 半導體業 | mainstream_growth |  | 187.1927568325929 | 98.67266191343712 | 7.67 | 73.85 | 114.37 | 444.54 | 228.42 | 465.67 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.02 | -1.08 | 2 | 2 | 22.91 | 21.7 | -13.47 |  | fail_low_response_condition |
| 4991 | 環宇-KY | 半導體業 | mainstream_growth |  | 54.369695427950326 | 55.05158501826551 | -13.93 | -16.14 | 37.47 | 235.43 | 52.47 | 239.31 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.02 | -5.16 | 0 | 0 | -17.84 | -12.23 | -34.41 |  | fail_low_response_condition |
| 5205 | 中茂 | 綠能環保 | neutral |  | 124.65618860510806 | 69.36197094125079 | 13.88 | 16.44 | -5.48 | -20.46 | 30.56 | 30.56 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 9.65 | 9.06 | -16.34 |  | fail_low_response_condition |
| 5213 | 亞昕 | 建材營造 | neutral |  | 211.33890576943767 | -57.83231080937989 | -14.84 | -12.07 | -15.78 | -2.34 | 0.0 | 0.0 | False |  | mild_accumulation | -0.33 | 0.04 | 0 | 2 | -11.37 | -10.02 | -16.7 |  | fail_low_response_condition |
| 5228 | 鈺鎧 | 電子零組件業 | mainstream_growth |  | 51.87312361310534 | 51.77659185196097 | 14.42 | 44.11 | 186.51 | 281.0 | 220.89 | 312.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.43 | -1.13 | 0 | 0 | 15.78 | 18.08 | -11.84 |  | fail_low_response_condition |
| 5263 | 智崴 | 文化創意業 | defensive_or_traditional |  | 61.21424790731411 | 42.10896004509289 | -2.83 | -6.79 | 4.67 | 10.63 | 16.52 | 16.52 | False |  | mild_accumulation | -0.3 | 0.05 | 1 | 1 | -3.33 | -1.41 | -10.43 |  | fail_low_response_condition |
| 5274 | 信驊 | 半導體業 | mainstream_growth |  | 68.73818861369199 | 61.729958331940246 | -0.6 | 16.68 | 54.51 | 169.96 | 70.31 | 179.52 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.48 | -0.02 | 1 | 1 | 0.86 | 2.4 | -6.95 |  | fail_low_response_condition |
| 5289 | 宜鼎 | 電腦及週邊設備業 | mainstream_growth |  | 640.802244561199 | 493.9247662959244 | 2.62 | 16.72 | 62.24 | 291.0 | 136.97 | 313.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.47 | 0.01 | 1 | 2 | 9.19 | 10.73 | -3.46 |  | fail_low_response_condition |
| 5302 | 太欣 | 半導體業 | mainstream_growth |  | 107.48007357449416 | 102.38460228240504 | 13.9 | 28.54 | 7.63 | 40.95 | 31.2 | 43.99 | True | 近20日漲幅>25% | mild_accumulation | 0.67 | 0.0 | 2 | 0 | 17.4 | 14.85 | 0.0 |  | fail_low_response_condition |
| 5310 | 天剛 | 資訊服務業 | mainstream_growth |  | 1485.7142857142858 | -17.93103448275862 | 4.4 | 1.43 | -9.12 | -18.63 | 13.18 | 13.18 | False |  | mild_accumulation | 0.97 | 0.76 | 3 | 1 | 4.26 | 3.31 | -10.75 |  | fail_low_response_condition |
| 5314 | 世紀* | 其他 | neutral |  | 157.45570866141733 | 160.58565890325826 | -8.87 | -16.42 | -23.34 | -48.87 | 0.0 | 0.0 | False |  | distribution_warning | -1.37 | -1.34 | 0 | 0 | -10.15 | -10.73 | -33.29 |  | fail_low_response_condition |
| 5345 | 馥鴻 | 其他 | neutral |  | 1505.660377358491 | 510.6753812636165 | 39.32 | 45.95 | 32.68 | 24.09 | 67.95 | 67.95 | True | 近20日漲幅>25%；距60日低點反彈>50% | distribution_warning | -0.59 | -0.59 | 0 | 0 | 30.11 | 22.3 | -19.45 |  | fail_low_response_condition |
| 5348 | 正能量智能 | 運動休閒 | neutral |  | 53.49971639251276 | 32.58138458486699 | 7.79 | 8.5 | -3.49 | -1.78 | 14.48 | 14.48 | False |  | mild_accumulation | 0.26 | 0.0 | 2 | 0 | 2.88 | 3.41 | -6.21 |  | fail_low_response_condition |
| 5351 | 鈺創 | 半導體業 | mainstream_growth |  | 605.4820263517354 | 411.4344351891923 | 2.84 | 21.77 | 13.96 | 118.31 | 52.27 | 137.17 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.4 | -0.27 | 2 | 2 | 6.21 | 6.41 | -5.63 |  | fail_low_response_condition |
| 5386 | 青雲 | 電腦及週邊設備業 | mainstream_growth |  | 412.7919634117528 | 510.9980823759461 | -7.76 | 16.18 | 25.69 | 571.6 | 93.41 | 621.1 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.48 | 0.0 | 1 | 0 | -6.69 | -1.84 | -20.54 |  | fail_low_response_condition |
| 5410 | 國眾 | 資訊服務業 | mainstream_growth |  | 199.22657884057065 | 60.05520451885815 | 15.36 | 22.06 | 49.27 | 53.23 | 55.03 | 58.76 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 1.01 | -2.35 | 1 | 1 | 13.24 | 13.15 | -7.23 |  | fail_low_response_condition |
| 5439 | 高技 | 電子零組件業 | mainstream_growth |  | 58.304659282636976 | 59.76338375118807 | -11.89 | -11.52 | 5.39 | -8.64 | 20.34 | 32.44 | False |  | distribution_warning | -1.75 | -1.54 | 0 | 1 | -12.91 | -11.46 | -30.42 |  | fail_low_response_condition |
| 5475 | 德宏 | 電子零組件業 | mainstream_growth |  | 214.9584342703777 | 123.25387942257557 | -23.93 | -17.09 | 11.62 | 197.42 | 28.06 | 203.29 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.78 | 0.23 | 2 | 1 | -17.47 | -17.4 | -43.02 |  | fail_low_response_condition |
| 5498 | 凱崴 | 電子零組件業 | mainstream_growth |  | 86.3193558161101 | 57.82371596014622 | 8.35 | 7.99 | 7.12 | 125.17 | 27.55 | 129.07 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.92 | 1.87 | 2 | 1 | 0.42 | -0.39 | -24.08 |  | fail_low_response_condition |
| 5508 | 永信建 | 建材營造 | neutral |  | 116.37225189625435 | 3.136885648699773 | 1.83 | 14.76 | 1.28 | -25.77 | 22.2 | 22.2 | False |  | mild_accumulation | -0.42 | 0.01 | 1 | 1 | 10.98 | 8.24 | -6.08 |  | fail_low_response_condition |
| 5514 | 三豐 | 建材營造 | neutral |  | 545.4183266932271 | 27801.12126245848 | 2.18 | -8.17 | -12.19 | -17.6 | 3.69 | 3.69 | False |  | mild_accumulation | -0.03 | 0.01 | 1 | 1 | -2.35 | -2.66 | -16.37 |  | fail_low_response_condition |
| 5516 | 雙喜 | 建材營造 | neutral |  | 93.66502038023266 | 40.95635213400519 | -1.82 | -1.82 | -17.24 | -23.13 | 7.46 | 7.46 | False |  | distribution_warning | -0.93 | -2.45 | 0 | 0 | 2.08 | 0.24 | -17.87 |  | fail_low_response_condition |
| 5864 | 致和證 | 金融業 | defensive_or_traditional |  | 350.19622607796714 | 2479.527079224786 | -1.28 | 59.33 | 97.04 | 248.08 | 116.7 | 258.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.26 | -0.64 | 1 | 2 | 18.76 | 18.2 | -6.81 |  | fail_low_response_condition |
| 5905 | 南仁湖 | 觀光餐旅 | defensive_or_traditional |  | 427.0146646728408 | 331.90287943698826 | 0.84 | 4.99 | 4.08 | -5.82 | 10.79 | 10.79 | False |  | distribution_warning | -0.08 | -0.16 | 1 | 0 | 4.14 | 3.16 | -8.68 |  | fail_low_response_condition |
| 6015 | 宏遠證 | 金融業 | defensive_or_traditional |  | 342.8514727193849 | 576.5892061992969 | -18.22 | 26.9 | 33.33 | 72.77 | 42.08 | 73.58 | True | 近20日漲幅>25%；近120日漲幅>70% | strong_accumulation | 0.99 | 0.98 | 2 | 2 | -0.74 | 0.14 | -23.33 |  | fail_low_response_condition |
| 6016 | 康和證 | 金融業 | defensive_or_traditional |  | 231.1165002789404 | 2150.902577889129 | -17.56 | 33.49 | 64.87 | 123.85 | 78.53 | 127.34 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.08 | -5.21 | 0 | 0 | 2.97 | 4.04 | -20.27 |  | fail_low_response_condition |
| 6020 | 大展證 | 金融業 | defensive_or_traditional |  | 1284.9769830028329 | 35336.78678678679 | -9.7 | 8.06 | 16.92 | 21.28 | 21.28 | 23.91 | False |  | mild_accumulation | -0.58 | 0.06 | 0 | 1 | -1.52 | -0.41 | -12.81 |  | fail_low_response_condition |
| 6021 | 美好證 | 金融業 | defensive_or_traditional |  | 830.6472568897998 | 16709.70054829186 | -3.98 | 31.99 | 30.94 | 63.87 | 46.35 | 66.87 | True | 近20日漲幅>25% | distribution_warning | -0.1 | -0.02 | 2 | 1 | 10.48 | 9.01 | -7.55 |  | fail_low_response_condition |
| 6023 | 元大期貨 | 金融業 | defensive_or_traditional |  | 80.3824419941387 | 29.22341641893437 | -1.97 | 2.05 | 5.74 | 4.08 | 6.76 | 8.15 | False |  | strong_accumulation | 0.15 | 0.32 | 2 | 2 | 0.25 | 0.11 | -2.93 |  | fail_low_response_condition |
| 6101 | 寬魚國際 | 文化創意業 | defensive_or_traditional |  | 224.2759693633317 | 212.49587530318647 | -2.76 | 4.52 | 8.3 | 8.88 | 10.97 | 14.27 | False |  | distribution_warning | -0.82 | -0.07 | 0 | 2 | 1.6 | 1.46 | -4.15 |  | fail_low_response_condition |
| 6111 | 光聚晶電 | 文化創意業 | defensive_or_traditional |  | 253.9600301050991 | 151.7320498828784 | 3.22 | -3.44 | 0.67 | 1.47 | 12.53 | 12.53 | False |  | strong_accumulation | 0.76 | 0.8 | 3 | 3 | -0.74 | -0.61 | -11.09 |  | fail_low_response_condition |
| 6113 | 亞矽 | 電子通路業 | mainstream_growth |  | 66.88659649857743 | 37.95758290325541 | 11.35 | 17.21 | 40.19 | 39.52 | 55.65 | 55.65 | True | 近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 0.83 | 1.88 | 2 | 2 | 6.51 | 8.74 | -3.82 |  | fail_low_response_condition |
| 6125 | 廣運 | 電機機械 | cyclical_turnaround |  | 79.19877909194963 | 45.54169719365739 | -10.21 | 9.32 | 0.5 | -13.83 | 16.12 | 16.12 | False |  | mild_accumulation | -0.07 | 1.35 | 2 | 2 | -7.06 | -5.21 | -21.21 |  | fail_low_response_condition |
| 6126 | 信音 | 電子零組件業 | mainstream_growth |  | 56.38171710218037 | 49.66796148784725 | -8.37 | 15.71 | 19.94 | 29.18 | 36.57 | 36.57 | False |  | strong_accumulation | 3.18 | 4.09 | 3 | 2 | 3.64 | 3.72 | -11.46 |  | fail_low_response_condition |
| 6134 | 萬旭 | 電子零組件業 | mainstream_growth |  | 63.51463391370063 | 52.1554016481993 | -4.23 | 16.25 | 12.7 | 36.91 | 27.22 | 42.48 | False |  | mild_accumulation | 0.3 | 0.0 | 1 | 1 | 0.73 | 0.87 | -16.15 |  | fail_low_response_condition |
| 6161 | 捷波 | 電腦及週邊設備業 | mainstream_growth |  | 82.74287656488983 | 28.47706568483651 | -4.74 | 2.35 | 25.78 | 13.97 | 32.82 | 32.82 | False |  | distribution_warning | -0.11 | 0.0 | 0 | 0 | -7.49 | -3.22 | -19.69 |  | fail_low_response_condition |
| 6171 | 大城地產 | 建材營造 | neutral |  | 53503.030303030304 | 675.0912523599749 | 0.84 | 0.21 | -11.74 | -14.26 | 4.34 | 4.34 | False |  | mild_accumulation | 0.1 | 0.09 | 1 | 1 | 1.16 | 0.04 | -15.17 |  | fail_low_response_condition |
| 6179 | 亞通 | 其他 | neutral |  | 121.75087091958048 | 68.29271469695588 | 4.12 | 2.85 | -8.5 | -20.19 | 10.24 | 10.24 | False |  | distribution_warning | -2.29 | -2.05 | 0 | 0 | 3.73 | 4.33 | -11.85 |  | fail_low_response_condition |
| 6199 | 天品 | 其他 | neutral |  | 724.1009386809703 | 914.4808811408876 | 1.65 | -7.05 | -10.82 | -2.84 | 5.97 | 5.97 | False |  | mild_accumulation | 1.06 | 2.03 | 2 | 1 | -1.57 | -1.78 | -27.61 |  | fail_low_response_condition |
| 6217 | 中探針 | 電子零組件業 | mainstream_growth |  | 51.17778846404754 | 36.31497905523737 | -11.47 | -1.46 | 23.95 | 344.34 | 52.92 | 383.57 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.51 | -3.83 | 1 | 1 | -13.12 | -11.71 | -36.52 |  | fail_low_response_condition |
| 6219 | 富旺 | 建材營造 | neutral |  | 7033.766233766234 | 18538.71359223301 | 0.78 | 4.44 | -13.09 | -34.43 | 13.6 | 13.6 | False |  | strong_accumulation | 1.3 | 0.3 | 3 | 2 | 4.99 | 3.04 | -14.24 |  | fail_low_response_condition |
| 6223 | 旺矽 | 半導體業 | mainstream_growth |  | 57.81298997442514 | 46.20299555286819 | 6.18 | 13.47 | 66.97 | 171.37 | 86.54 | 218.27 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.57 | -6.0 | 1 | 2 | 6.74 | 8.55 | -7.27 |  | fail_low_response_condition |
| 6229 | 研通 | 半導體業 | mainstream_growth |  | 76.70780960505445 | 53.80581816729727 | -4.23 | -1.14 | 20.88 | 17.61 | 30.25 | 30.25 | False |  | distribution_warning | -0.1 | 0.0 | 1 | 0 | -3.37 | -2.72 | -16.64 |  | fail_low_response_condition |
| 6264 | 富裔 | 建材營造 | neutral |  | 226.0680557637536 | 58.63577003674796 | 0.16 | -2.41 | -5.0 | -16.14 | 5.74 | 5.74 | False |  | strong_accumulation | 0.08 | 0.08 | 3 | 3 | 0.18 | -0.14 | -10.06 |  | fail_low_response_condition |
| 6265 | 方土昶 | 電子通路業 | mainstream_growth |  | 1076.3549823430062 | 648.3820919234922 | -12.52 | 34.38 | 17.56 | 174.69 | 59.49 | 192.67 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.97 | 2.63 | 2 | 2 | 1.9 | 3.39 | -13.6 |  | fail_low_response_condition |
| 6274 | 台燿 | 電子零組件業 | mainstream_growth |  | 128.48732779782807 | 80.25773721086192 | -5.01 | 33.61 | 190.61 | 263.43 | 205.5 | 304.02 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.13 | -2.26 | 0 | 0 | 2.25 | 6.36 | -11.29 |  | fail_low_response_condition |
| 6292 | 迅德 | 電子零組件業 | mainstream_growth |  | 79.8700016455488 | 34.01579180294248 | 9.74 | 25.19 | 44.44 | 66.3 | 57.21 | 72.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | neutral | 0.0 | 0.0 | 0 | 0 | 8.89 | 10.88 | -8.65 |  | fail_low_response_condition |
| 6419 | 京晨科 | 光電業 | mainstream_growth |  | 368.78637424785455 | 135.8943019763131 | -4.17 | -3.83 | 61.4 | 103.84 | 72.93 | 115.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -5.74 | -4.74 | -29.05 |  | fail_low_response_condition |
| 6462 | 神盾 | 半導體業 | mainstream_growth |  | 135.52158343846233 | 97.64657459987085 | -5.93 | -17.47 | 9.36 | -12.94 | 15.15 | 15.99 | False |  | distribution_warning | -5.84 | -5.02 | 0 | 1 | -13.09 | -9.56 | -30.84 |  | fail_low_response_condition |
| 6465 | 威潤 | 通信網路業 | mainstream_growth |  | 169.583931133429 | 93.13670993689304 | 10.34 | 31.69 | 33.89 | 88.24 | 65.16 | 107.46 | True | 近20日漲幅>25%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.18 | 0.0 | 2 | 0 | 19.6 | 18.73 | -12.45 |  | fail_low_response_condition |
| 6494 | 九齊 | 半導體業 | mainstream_growth |  | 79.43355218989315 | 43.11525942708911 | 19.24 | 27.41 | 42.59 | 89.53 | 62.46 | 98.56 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.41 | 0.0 | 1 | 0 | 17.36 | 18.02 | -0.29 |  | fail_low_response_condition |
| 6576 | 逸達 | 生技醫療業 | defensive_or_traditional |  | 749.5590449559045 | 36.985314582276 | 3.27 | -3.07 | 2.6 | -0.38 | 5.19 | 5.19 | False |  | strong_accumulation | 0.31 | 0.37 | 2 | 2 | 0.93 | 0.83 | -5.62 |  | fail_low_response_condition |
| 6588 | 東典光電 | 通信網路業 | mainstream_growth |  | 159.9830396683313 | 165.38190032472116 | 2.3 | -9.76 | 1.37 | 137.43 | 17.21 | 146.94 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -4.53 | -0.08 | 0 | 0 | -5.04 | -5.04 | -33.33 |  | fail_low_response_condition |
| 6596 | 寬宏藝術 | 文化創意業 | defensive_or_traditional |  | 122.48698203153648 | 91.71375346744868 | -4.3 | -4.3 | -35.74 | -33.92 | 0.54 | 0.54 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -3.12 | -3.53 | -36.39 |  | fail_low_response_condition |
| 6613 | 朋億* | 其他電子業 | mainstream_growth |  | 81.72059250458541 | 25.75033629369081 | 35.34 | 45.45 | 71.43 | 85.57 | 83.21 | 101.68 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.66 | 0.0 | 1 | 0 | 30.28 | 29.34 | -4.38 |  | fail_low_response_condition |
| 6617 | 共信-KY | 生技醫療業 | defensive_or_traditional |  | 68.48115721355158 | 25.969105217137862 | 0.59 | 3.04 | -5.57 | -22.43 | 16.3 | 16.3 | False |  | strong_accumulation | 0.17 | 0.16 | 2 | 2 | -0.74 | -0.55 | -15.57 |  | fail_low_response_condition |
| 6629 | 泰金-KY | 居家生活 | neutral |  | 90.1053928142166 | 88.43635222920778 | -3.38 | -6.53 | 8.53 | -10.89 | 11.17 | 13.37 | False |  | mild_accumulation | 0.16 | 0.0 | 1 | 0 | -2.82 | -2.71 | -16.42 |  | fail_low_response_condition |
| 6654 | 天正國際 | 其他電子業 | mainstream_growth |  | 106.68524559014472 | 77.30403434460713 | 22.12 | 113.4 | 127.47 | 133.11 | 144.1 | 158.75 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.07 | 0.0 | 3 | 0 | 41.96 | 39.13 | 0.0 |  | fail_low_response_condition |
| 6693 | 廣閎科 | 半導體業 | mainstream_growth |  | 115.16072542823213 | 78.42165561482598 | 13.38 | 29.93 | 69.52 | 127.62 | 80.53 | 135.76 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.02 | 0.0 | 2 | 0 | 15.27 | 14.1 | -9.64 |  | fail_low_response_condition |
| 6727 | 亞泰金屬 | 電子零組件業 | mainstream_growth |  | 54.1070669876788 | 112.73549191644769 | -19.92 | -21.05 | 33.79 | 101.54 | 57.43 | 136.86 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -11.24 | -2.47 | 1 | 1 | -27.35 | -20.68 | -43.76 |  | fail_low_response_condition |
| 6735 | 美達科技 | 其他電子業 | mainstream_growth |  | 155.07788585810488 | 67.66569790909824 | -14.53 | -15.72 | 60.35 | 48.52 | 64.43 | 77.65 | True | 近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | 0.64 | 0.0 | 1 | 0 | -13.64 | -12.56 | -39.4 |  | fail_low_response_condition |
| 6739 | 竹陞科技 | 其他電子業 | mainstream_growth |  | 99.25885395941106 | 95.52796729930556 | -10.59 | -8.06 | -5.0 | 43.94 | 5.07 | 64.98 | False |  | distribution_warning | -0.03 | 0.0 | 0 | 0 | -8.67 | -8.65 | -35.23 |  | fail_low_response_condition |
| 6870 | 騰雲 | 數位雲端 | neutral |  | 56.14728080694082 | 48.35214011534826 | 1.63 | 37.25 | 43.59 | 28.74 | 67.66 | 67.66 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | mild_accumulation | -1.18 | 3.38 | 1 | 2 | 5.21 | 7.29 | -15.66 |  | fail_low_response_condition |
| 6894 | 衛司特 | 綠能環保 | neutral |  | 92.69510884705696 | 71.87896672768468 | -7.03 | 5.15 | -3.38 | 78.05 | 19.0 | 87.4 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.11 | 0.0 | 0 | 0 | -4.44 | -2.92 | -14.59 |  | fail_low_response_condition |