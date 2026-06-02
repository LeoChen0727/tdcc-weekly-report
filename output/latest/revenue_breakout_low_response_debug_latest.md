# 營收爆發低反應股 Debug Report

- 產生時間：`2026-06-02 19:37:19 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 884 |
| standardized_revenue_rows | 884 |
| price_rows | 571285 |
| tdcc_rows | 1972 |
| tdcc_trend_rows | 1972 |
| tdcc_strong_accumulation_count | 470 |
| tdcc_mild_accumulation_count | 736 |
| tdcc_distribution_warning_count | 618 |
| revenue_condition_pass | 121 |
| price_metrics_pass | 121 |
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
| fail_revenue_condition | 763 |
| fail_low_response_condition | 121 |

## 樣本資料

| stock_id | stock_name | industry | theme_group | revaluation_priority | latest_revenue_yoy | cumulative_revenue_yoy | return_5d | return_20d | return_60d | return_120d | off_60d_low_pct | off_120d_low_pct | already_priced_in | priced_in_reason | tdcc_accumulation_signal | tdcc_400_change_sum | tdcc_1000_change_sum | tdcc_400_up_weeks | tdcc_1000_up_weeks | distance_to_ma20_pct | distance_to_ema23_pct | distance_to_high_60_pct | score | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1591 | 駿吉-KY | 電機機械 | cyclical_turnaround |  | 510.66838046272494 | 743.7470682052725 | -0.59 | -34.2 | -11.43 | -11.99 | 28.77 | 28.77 | False |  | distribution_warning | -0.56 | 0.0 | 2 | 0 | -4.06 | -7.79 | -39.96 |  | fail_low_response_condition |
| 1799 | 易威 | 生技醫療業 | defensive_or_traditional |  | 240.44451280473737 | 83.17816490095692 | 0.6 | -6.83 | 13.03 | -0.89 | 13.22 | 20.8 | False |  | mild_accumulation | 0.34 | 0.0 | 3 | 2 | -3.15 | -3.79 | -25.61 |  | fail_low_response_condition |
| 1815 | 富喬 | 電子零組件業 | mainstream_growth |  | 53.16278671723507 | 40.47675320517641 | 5.8 | -0.9 | 3.79 | 33.21 | 16.24 | 38.61 | False |  | distribution_warning | -3.84 | -3.61 | 1 | 0 | 3.77 | 2.43 | -15.44 |  | fail_low_response_condition |
| 2230 | 泰茂 | 電機機械 | cyclical_turnaround |  | 77.86861915651653 | 65.520105323096 | -0.71 | -10.53 | -18.58 | -72.5 | 5.45 | 5.45 | False |  | strong_accumulation | 0.61 | 0.09 | 3 | 2 | -3.18 | -3.74 | -26.09 |  | fail_low_response_condition |
| 3081 | 聯亞 | 通信網路業 | mainstream_growth |  | 115.38448966249898 | 103.7026472556527 | -2.83 | -7.37 | 65.59 | 375.09 | 90.74 | 379.52 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.09 | -1.29 | 2 | 1 | -5.82 | -3.71 | -22.09 |  | fail_low_response_condition |
| 3085 | 新零售 | 數位雲端 | neutral |  | 96.80824327720532 | 18.285783074515468 | 0.4 | -3.47 | 7.3 | -17.76 | 14.68 | 14.68 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.81 | 1.31 | -11.97 |  | fail_low_response_condition |
| 3088 | 艾訊 | 電腦及週邊設備業 | mainstream_growth |  | 65.88230816535429 | 38.0977827651226 | 0.71 | 10.16 | 71.95 | 86.02 | 76.25 | 87.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.23 | 2.64 | 2 | 2 | 2.25 | 5.5 | -7.24 |  | fail_low_response_condition |
| 3147 | 大綜 | 資訊服務業 | mainstream_growth |  | 90.07098363534266 | 9.456031185015002 | 23.88 | 21.82 | 22.16 | 25.64 | 43.65 | 45.54 | False |  | distribution_warning | -0.95 | 0.0 | 2 | 0 | 20.02 | 19.27 | 0.0 |  | fail_low_response_condition |
| 3171 | 炎洲流通 | 居家生活 | neutral |  | 126.3478178187696 | 90.66142908048124 | 5.67 | 7.54 | 41.17 | 51.93 | 42.55 | 58.73 | True | 近60日漲幅>40% | neutral | 0.0 | 0.0 | 0 | 0 | 5.46 | 5.24 | -1.49 |  | fail_low_response_condition |
| 3188 | 鑫龍騰 | 建材營造 | neutral |  | 914.834168710675 | 892.3303586904568 | -0.88 | -6.22 | -34.11 | -28.59 | 1.8 | 1.8 | False |  | strong_accumulation | 0.34 | 0.31 | 2 | 2 | -4.07 | -4.73 | -35.7 |  | fail_low_response_condition |
| 3205 | 佰研 | 生技醫療業 | defensive_or_traditional |  | 67.90192099191015 | 51.567453071360745 | -3.51 | -7.27 | 1.36 | 13.82 | 5.34 | 16.61 | False |  | mild_accumulation | -0.4 | 2.01 | 1 | 1 | -2.73 | -3.67 | -21.94 |  | fail_low_response_condition |
| 3260 | 威剛 | 半導體業 | mainstream_growth |  | 169.50705162133545 | 165.38579121733795 | 16.07 | 2.74 | 33.95 | 169.05 | 40.57 | 173.76 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.69 | -5.27 | 0 | 0 | 11.7 | 11.39 | -10.57 |  | fail_low_response_condition |
| 3290 | 東浦 | 電子零組件業 | mainstream_growth |  | 69.35257646971267 | 79.9307324458115 | 1.25 | -0.1 | 6.82 | 15.05 | 19.0 | 20.92 | False |  | distribution_warning | -0.27 | -0.42 | 2 | 1 | 1.77 | 1.4 | -6.63 |  | fail_low_response_condition |
| 3297 | 杭特 | 光電業 | mainstream_growth |  | 53.69808926179228 | 21.124604723137995 | 15.15 | 4.91 | -10.0 | -20.47 | 16.72 | 16.72 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 11.36 | 9.82 | -13.2 |  | fail_low_response_condition |
| 3313 | 斐成 | 其他 | neutral |  | 125.59241706161136 | 626.336898395722 | 1.82 | -1.75 | -11.81 | -21.68 | 3.7 | 3.7 | False |  | strong_accumulation | 0.35 | 0.37 | 3 | 3 | -1.58 | -2.33 | -19.71 |  | fail_low_response_condition |
| 3354 | 律勝 | 電子零組件業 | mainstream_growth |  | 52.02821869488536 | 20.249566527386943 | 5.9 | -5.14 | 19.86 | 62.35 | 40.68 | 71.13 | False |  | distribution_warning | -0.24 | 0.0 | 1 | 0 | 0.1 | 2.56 | -11.7 |  | fail_low_response_condition |
| 3466 | 德晉 | 通信網路業 | mainstream_growth |  | 2243.126742440489 | 1259.5214156444802 | -0.31 | -17.86 | -9.31 | -28.87 | 0.62 | 0.62 | False |  | mild_accumulation | -0.56 | 1.36 | 1 | 3 | -5.87 | -6.09 | -28.71 |  | fail_low_response_condition |
| 3489 | 森寶 | 建材營造 | neutral |  | 113.51012213485026 | 120.45474675135702 | 0.0 | -3.35 | 10.18 | 8.25 | 1.64 | 14.55 | False |  | mild_accumulation | 0.57 | 0.0 | 1 | 0 | -1.09 | -1.33 | -11.63 |  | fail_low_response_condition |
| 3491 | 昇達科 | 通信網路業 | mainstream_growth |  | 83.9939064567311 | 69.07810246379388 | 3.5 | 13.74 | 63.64 | 292.79 | 65.6 | 298.08 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.1 | 0.06 | 2 | 1 | 6.44 | 5.87 | -5.91 |  | fail_low_response_condition |
| 3498 | 陽程 | 其他電子業 | mainstream_growth |  | 137.82244323121327 | 107.83813918263162 | -3.1 | 37.07 | 110.01 | 177.67 | 105.71 | 199.57 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.57 | 8.4 | 3 | 2 | -3.88 | 2.2 | -14.59 |  | fail_low_response_condition |
| 3512 | 皇龍 | 建材營造 | neutral |  | 147.80032587764777 | -67.85821774084044 | -0.97 | 0.0 | -1.93 | -0.73 | 2.26 | 2.78 | False |  | mild_accumulation | 0.02 | -0.03 | 1 | 0 | -0.23 | -1.0 | -7.5 |  | fail_low_response_condition |
| 3523 | 迎輝 | 光電業 | mainstream_growth |  | 197.78021375719376 | -28.177372219240173 | 32.76 | 55.24 | 20.31 | 4.05 | 101.36 | 101.36 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 0.47 | 0.0 | 2 | 0 | 52.61 | 40.46 | 0.0 |  | fail_low_response_condition |
| 3555 | 博士旺 | 半導體業 | mainstream_growth |  | 2832.482993197279 | 3831.740379092476 | -0.24 | -2.98 | 57.25 | 215.2 | 45.36 | 217.57 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | 0.88 | 1 | 1 | -2.79 | -3.63 | -24.87 |  | fail_low_response_condition |
| 3577 | 泓格 | 電腦及週邊設備業 | mainstream_growth |  | 89.01210915432416 | 36.29945032117057 | -9.94 | 57.44 | 127.99 | 129.79 | 136.54 | 156.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.45 | 0.02 | 1 | 1 | 5.56 | 7.98 | -16.43 |  | fail_low_response_condition |
| 3594 | 磐儀 | 電腦及週邊設備業 | mainstream_growth |  | 50.36666640125487 | 36.33687909638193 | -1.67 | -10.8 | 17.39 | 27.1 | 31.1 | 41.7 | False |  | distribution_warning | -0.23 | -0.21 | 2 | 0 | -2.57 | -2.1 | -16.19 |  | fail_low_response_condition |
| 3629 | 地心引力 | 文化創意業 | defensive_or_traditional |  | 261400.0 | 75119.04761904762 | -5.75 | 2.5 | -21.9 | -0.3 | 4.46 | 4.46 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.63 | -2.66 | -24.6 |  | fail_low_response_condition |
| 3672 | 康聯訊 | 通信網路業 | mainstream_growth |  | 120.0719634347953 | -21.66306364905971 | 5.66 | -3.45 | -4.68 | -11.81 | 8.21 | 8.21 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.74 | -0.06 | -22.22 |  | fail_low_response_condition |
| 3680 | 家登 | 半導體業 | mainstream_growth |  | 52.739619752984254 | 20.16580656803387 | -1.5 | -14.45 | 35.13 | 55.0 | 41.67 | 68.37 | False |  | mild_accumulation | -1.62 | 1.2 | 2 | 1 | -5.12 | -2.76 | -15.41 |  | fail_low_response_condition |
| 3685 | 元創精密 | 電機機械 | cyclical_turnaround |  | 74.29675942423358 | 55.40714795511386 | -6.15 | -11.0 | -17.97 | -32.06 | 5.53 | 5.53 | False |  | distribution_warning | -0.05 | -0.2 | 2 | 0 | -5.75 | -7.0 | -26.24 |  | fail_low_response_condition |
| 3691 | 碩禾 | 光電業 | mainstream_growth |  | 163.4117868279612 | 175.67923400100153 | 5.3 | 12.77 | 34.75 | 120.22 | 55.88 | 125.53 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.65 | -2.83 | 1 | 0 | 4.74 | 6.71 | -8.09 |  | fail_low_response_condition |
| 4127 | 天良 | 生技醫療業 | defensive_or_traditional |  | 66.79204076680418 | 69.33155758498225 | 4.1 | 72.11 | 87.41 | 127.2 | 97.69 | 136.21 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.87 | 3.69 | 2 | 2 | 16.46 | 16.67 | -8.42 |  | fail_low_response_condition |
| 4154 | 樂威科-KY | 其他 | neutral |  | 99.26590538336052 | 1.244490536686544 | -2.27 | 4.88 | 17.81 | -24.34 | 37.38 | 37.38 | False |  | mild_accumulation | 0.83 | -0.45 | 3 | 0 | -4.36 | -3.65 | -16.77 |  | fail_low_response_condition |
| 4168 | 醣聯 | 生技醫療業 | defensive_or_traditional |  | 185.7142857142857 | -1.9671209779401435 | -4.73 | 16.96 | 6.29 | 20.74 | 18.55 | 23.58 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | 1.93 | 2.32 | -9.66 |  | fail_low_response_condition |
| 4529 | 淳紳 | 其他 | neutral |  | 472.1603563474388 | 113.87800783435928 | 2.07 | 9.78 | 39.15 | 28.31 | 75.8 | 75.8 | True | 距60日低點反彈>50% | neutral | 0.0 | 0.0 | 0 | 0 | -6.47 | -1.91 | -24.92 |  | fail_low_response_condition |
| 4530 | 宏易 | 觀光餐旅 | defensive_or_traditional |  | 230.49152002910017 | 78.04070042593469 | 6.64 | 4.13 | -4.68 | 150.0 | 14.72 | 152.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | 0.0 | 3 | 0 | 4.07 | 3.34 | -16.14 |  | fail_low_response_condition |
| 4558 | 寶緯 | 電機機械 | cyclical_turnaround |  | 84.83396047199795 | 4.509365967190961 | 0.51 | -2.95 | 3.67 | 1.28 | 7.05 | 9.12 | False |  | distribution_warning | -0.11 | -0.09 | 0 | 0 | -0.24 | 0.38 | -13.38 |  | fail_low_response_condition |
| 4577 | 達航科技 | 其他電子業 | mainstream_growth |  | 62.5793018983466 | 56.34887065392099 | -10.73 | -25.45 | 11.23 | 90.48 | 22.5 | 111.17 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.29 | -4.71 | 1 | 0 | -17.13 | -17.33 | -45.26 |  | fail_low_response_condition |
| 4711 | 永純 | 化學工業 | cyclical_turnaround |  | 89.32523504451285 | 23.470589276860967 | 7.99 | 9.94 | 22.07 | 21.26 | 22.07 | 25.43 | False |  | distribution_warning | -1.09 | -0.16 | 0 | 0 | 9.04 | 9.38 | -6.17 |  | fail_low_response_condition |
| 4714 | 永捷 | 化學工業 | cyclical_turnaround |  | 96.03344108366043 | 95.91632424000304 | 1.12 | -8.11 | -14.47 | -16.31 | 5.84 | 5.84 | False |  | distribution_warning | -1.33 | -0.72 | 0 | 1 | 0.52 | -1.28 | -22.06 |  | fail_low_response_condition |
| 4726 | 永昕 | 生技醫療業 | defensive_or_traditional |  | 301.006875305256 | 104.64090930541416 | -1.28 | -7.86 | -15.12 | -16.43 | 3.06 | 3.06 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -3.83 | -3.83 | -17.96 |  | fail_low_response_condition |
| 4743 | 合一 | 生技醫療業 | defensive_or_traditional |  | 101.82665424044734 | 62.11088547027568 | 3.02 | -0.58 | -3.94 | -25.69 | 4.49 | 4.49 | False |  | distribution_warning | -0.52 | -0.58 | 2 | 1 | 0.11 | -0.45 | -13.22 |  | fail_low_response_condition |
| 4760 | 勤凱科技 | 其他電子業 | mainstream_growth |  | 63.098631698973776 | 54.91021842087173 | -5.52 | 43.83 | 125.84 | 102.52 | 133.04 | 148.92 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.21 | -3.56 | 1 | 0 | 10.58 | 10.21 | -21.18 |  | fail_low_response_condition |
| 4768 | 晶呈科技 | 化學工業 | cyclical_turnaround |  | 191.53168275283247 | 166.3777307047525 | 0.2 | 0.72 | 11.69 | 112.07 | 21.63 | 120.63 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.99 | -4.87 | 1 | 0 | 6.21 | 3.64 | -15.9 |  | fail_low_response_condition |
| 4772 | 台特化 | 化學工業 | cyclical_turnaround |  | 210.12358034898395 | 266.4543899237024 | -0.17 | -5.98 | -11.16 | -3.24 | 9.54 | 9.54 | False |  | strong_accumulation | 0.14 | 0.27 | 2 | 2 | -1.13 | -1.46 | -13.6 |  | fail_low_response_condition |
| 4907 | 富宇 | 建材營造 | neutral |  | 402.7102995324487 | 265.58397526745915 | 3.93 | -6.21 | -8.42 | -11.9 | 5.41 | 5.41 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -1.62 | -1.14 | -11.9 |  | fail_low_response_condition |
| 4931 | 新盛力 | 電腦及週邊設備業 | mainstream_growth |  | 97.38306551458992 | 35.10154042171776 | 10.53 | 23.53 | 79.07 | 40.0 | 84.06 | 94.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 5.47 | 2.61 | 2 | 1 | 10.45 | 12.21 | -7.41 |  | fail_low_response_condition |
| 4973 | 廣穎電通 | 半導體業 | mainstream_growth |  | 106.0995211097044 | 82.0904184804944 | 2.62 | 42.92 | 181.47 | 363.7 | 176.99 | 380.8 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.65 | 2.69 | 2 | 2 | 20.69 | 21.37 | -6.29 |  | fail_low_response_condition |
| 4991 | 環宇-KY | 半導體業 | mainstream_growth |  | 67.9225669656687 | 55.01101125702958 | -0.43 | 2.33 | 106.77 | 338.75 | 127.92 | 338.75 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -0.57 | 2 | 2 | -5.53 | -3.13 | -21.56 |  | fail_low_response_condition |
| 5228 | 鈺鎧 | 電子零組件業 | mainstream_growth |  | 62.02852912838108 | 51.74961237953364 | 1.74 | 54.2 | 188.34 | 240.21 | 202.59 | 267.43 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -8.34 | -2.85 | 0 | 0 | 17.62 | 20.25 | -8.66 |  | fail_low_response_condition |
| 5263 | 智崴 | 文化創意業 | defensive_or_traditional |  | 61.94202436252717 | 36.68329399189418 | 2.38 | 3.37 | 6.44 | 14.85 | 21.61 | 21.61 | False |  | mild_accumulation | 1.28 | -0.07 | 2 | 1 | 0.68 | 2.47 | -6.52 |  | fail_low_response_condition |
| 5274 | 信驊 | 半導體業 | mainstream_growth |  | 81.593085197006 | 59.80710332909424 | 1.46 | 1.51 | 79.96 | 175.63 | 80.77 | 182.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | -0.25 | 2 | 0 | 2.6 | 3.26 | -7.25 |  | fail_low_response_condition |
| 5289 | 宜鼎 | 電腦及週邊設備業 | mainstream_growth |  | 583.1104370746453 | 452.2084788945506 | 10.29 | 6.53 | 88.44 | 309.84 | 127.27 | 320.88 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.45 | -0.01 | 0 | 1 | 6.16 | 10.79 | -3.85 |  | fail_low_response_condition |
| 5291 | 邑昇 | 電子零組件業 | mainstream_growth |  | 69.45516610517392 | 36.664686579042986 | -3.52 | -4.2 | 29.25 | 140.77 | 37.0 | 159.47 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.04 | -2.75 | 2 | 2 | -5.87 | -4.2 | -19.03 |  | fail_low_response_condition |
| 5314 | 世紀* | 其他 | neutral |  | 138.62470941331696 | 161.5030245941451 | 3.27 | -14.71 | -15.62 | -41.48 | 3.27 | 3.27 | False |  | distribution_warning | -1.69 | -0.94 | 1 | 1 | -3.69 | -5.12 | -28.1 |  | fail_low_response_condition |
| 5345 | 馥鴻 | 其他 | neutral |  | 562.4398073836276 | 355.7700377675199 | 17.36 | 10.34 | 2.78 | -1.44 | 31.51 | 31.51 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 14.15 | 11.23 | -4.0 |  | fail_low_response_condition |
| 5351 | 鈺創 | 半導體業 | mainstream_growth |  | 417.0626132083888 | 359.7438728245971 | 12.47 | 15.98 | 52.8 | 143.83 | 56.13 | 149.4 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.13 | 1.35 | 2 | 2 | 11.01 | 12.85 | -2.62 |  | fail_low_response_condition |
| 5386 | 青雲 | 電腦及週邊設備業 | mainstream_growth |  | 405.25703262628434 | 537.622375622673 | -2.78 | 27.19 | 75.24 | 680.73 | 116.67 | 707.8 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.16 | 0.0 | 0 | 0 | 10.28 | 9.47 | -10.99 |  | fail_low_response_condition |
| 5410 | 國眾 | 資訊服務業 | mainstream_growth |  | 122.27479364891022 | 37.89174869171116 | 5.77 | 11.49 | 33.5 | 33.93 | 38.42 | 41.75 | False |  | strong_accumulation | 1.63 | 1.48 | 2 | 2 | 6.73 | 7.96 | -2.14 |  | fail_low_response_condition |
| 5475 | 德宏 | 電子零組件業 | mainstream_growth |  | 120.58864400655902 | 101.17685065534428 | 20.08 | -3.47 | 59.2 | 356.49 | 77.78 | 377.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.69 | 2 | 2 | 9.13 | 7.67 | -20.89 |  | fail_low_response_condition |
| 5488 | 松普 | 電子零組件業 | mainstream_growth |  | 93.29563197379946 | 37.99866980581613 | 23.91 | 37.02 | 49.53 | 50.16 | 52.41 | 60.11 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 1.43 | 1.15 | 3 | 2 | 23.0 | 21.86 | -0.7 |  | fail_low_response_condition |
| 5498 | 凱崴 | 電子零組件業 | mainstream_growth |  | 54.63972516047374 | 50.28516602297845 | -3.5 | -8.25 | 3.43 | 137.9 | 22.16 | 151.09 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.2 | -2.0 | 1 | 0 | -5.98 | -5.8 | -27.29 |  | fail_low_response_condition |
| 5514 | 三豐 | 建材營造 | neutral |  | 359.86984815618223 | 34979.69569779643 | -0.69 | -9.46 | -9.46 | 3.24 | 5.51 | 5.51 | False |  | mild_accumulation | 0.07 | 0.01 | 2 | 1 | -3.71 | -3.35 | -14.58 |  | fail_low_response_condition |
| 5529 | 鉅陞 | 建材營造 | neutral |  | 3460.343434343434 | 2385.27557453732 | 2.51 | 2.74 | -12.11 | -6.44 | 7.14 | 7.14 | False |  | mild_accumulation | -0.1 | 0.08 | 2 | 2 | -2.07 | -1.84 | -19.64 |  | fail_low_response_condition |
| 5864 | 致和證 | 金融業 | defensive_or_traditional |  | 2037.1729784841127 | 779.9502128124395 | 13.93 | 23.71 | 83.43 | 198.68 | 96.96 | 225.45 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.65 | -1.7 | 1 | 1 | 26.59 | 24.22 | -1.94 |  | fail_low_response_condition |
| 5905 | 南仁湖 | 觀光餐旅 | defensive_or_traditional |  | 686.3773953069496 | 307.26437021074355 | 2.56 | -8.99 | -6.1 | -13.89 | 5.26 | 5.26 | False |  | mild_accumulation | 0.08 | -0.43 | 2 | 0 | -0.55 | -0.04 | -13.23 |  | fail_low_response_condition |
| 6015 | 宏遠證 | 金融業 | defensive_or_traditional |  | 4229.158188258347 | 732.2032127625579 | 15.83 | 23.37 | 51.09 | 95.77 | 61.0 | 98.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.86 | 1.08 | 2 | 2 | 24.63 | 22.14 | -0.48 |  | fail_low_response_condition |
| 6016 | 康和證 | 金融業 | defensive_or_traditional |  | 1127.2871745131688 | 4803.222264258889 | 20.59 | 35.14 | 85.19 | 149.04 | 99.39 | 153.91 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.19 | -0.5 | 0 | 1 | 29.71 | 28.29 | -1.22 |  | fail_low_response_condition |
| 6020 | 大展證 | 金融業 | defensive_or_traditional |  | 2338.3188675346146 | 2577.8824833702884 | 1.93 | 1.49 | 24.28 | 26.6 | 26.6 | 29.35 | False |  | distribution_warning | -0.3 | -0.48 | 1 | 1 | 6.29 | 6.61 | -4.99 |  | fail_low_response_condition |
| 6021 | 美好證 | 金融業 | defensive_or_traditional |  | 5212.463185451826 | 1481.8435288230107 | 11.6 | 11.44 | 20.09 | 52.91 | 40.64 | 60.37 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | 16.92 | 14.65 | -1.25 |  | fail_low_response_condition |
| 6026 | 福邦證 | 金融業 | defensive_or_traditional |  | 461.7024055162327 | 380.76366102689127 | 9.54 | 7.23 | 25.8 | 45.9 | 25.8 | 47.11 | False |  | distribution_warning | -0.38 | -0.83 | 1 | 1 | 11.55 | 10.28 | -1.11 |  | fail_low_response_condition |
| 6111 | 光聚晶電 | 文化創意業 | defensive_or_traditional |  | 149.45364292025778 | 134.09032530399222 | -1.02 | -8.36 | 2.45 | -4.15 | 9.9 | 9.9 | False |  | strong_accumulation | 1.42 | 1.25 | 3 | 3 | -5.45 | -4.35 | -13.17 |  | fail_low_response_condition |
| 6125 | 廣運 | 光電業 | mainstream_growth |  | 56.77567839472995 | 37.581989499569296 | 8.23 | 18.93 | 13.96 | 11.99 | 37.86 | 37.86 | False |  | mild_accumulation | 0.37 | -0.77 | 2 | 1 | 13.52 | 11.92 | -6.46 |  | fail_low_response_condition |
| 6171 | 大城地產 | 建材營造 | neutral |  | 211784.84848484848 | 565.1510373967333 | 0.0 | -6.79 | -14.31 | -16.01 | 1.3 | 1.3 | False |  | strong_accumulation | 0.11 | 0.11 | 2 | 2 | -2.23 | -3.19 | -17.64 |  | fail_low_response_condition |
| 6179 | 亞通 | 其他 | neutral |  | 69.36285627295153 | 54.76822782478532 | -0.21 | -4.45 | -11.94 | -24.84 | 1.29 | 1.29 | False |  | strong_accumulation | 0.53 | 0.25 | 2 | 2 | -3.45 | -2.9 | -19.59 |  | fail_low_response_condition |
| 6199 | 天品 | 其他 | neutral |  | 516.9373318720733 | 963.5349918331448 | -2.16 | -10.05 | -4.84 | -9.33 | 2.96 | 2.96 | False |  | distribution_warning | -3.58 | -3.33 | 0 | 0 | -6.58 | -5.41 | -29.1 |  | fail_low_response_condition |
| 6218 | 豪勉 | 通信網路業 | mainstream_growth |  | 98.94734925057824 | 24.203979861860773 | -4.56 | 1.07 | 61.8 | 108.29 | 66.08 | 108.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.61 | 0.33 | 2 | 2 | -6.0 | -3.11 | -19.1 |  | fail_low_response_condition |
| 6219 | 富旺 | 建材營造 | neutral |  | 21424.40677966101 | 18959.528301886792 | 4.68 | -4.65 | -23.6 | -36.6 | 7.89 | 7.89 | False |  | strong_accumulation | 1.4 | 0.64 | 3 | 3 | 1.59 | -0.14 | -25.0 |  | fail_low_response_condition |
| 6223 | 旺矽 | 半導體業 | mainstream_growth |  | 52.59594490792657 | 42.51276664792454 | -6.76 | 10.63 | 67.88 | 154.15 | 67.12 | 172.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.24 | -0.27 | 1 | 1 | -6.92 | -3.41 | -17.25 |  | fail_low_response_condition |
| 6228 | 全譜 | 電腦及週邊設備業 | mainstream_growth |  | 101.31396957123098 | -15.30696332921302 | 0.95 | -4.07 | -13.11 | -13.29 | 3.92 | 3.92 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.36 | -2.34 | -18.3 |  | fail_low_response_condition |
| 6229 | 研通 | 半導體業 | mainstream_growth |  | 57.360134931273095 | 48.52972335584195 | 1.7 | -8.18 | 23.62 | 19.78 | 34.75 | 34.75 | False |  | mild_accumulation | -0.17 | 0.05 | 1 | 1 | -1.06 | 0.35 | -13.76 |  | fail_low_response_condition |
| 6237 | 驊訊 | 半導體業 | mainstream_growth |  | 116.12150730581902 | 55.45139627457535 | -1.92 | 12.09 | 34.39 | 28.46 | 46.97 | 46.97 | False |  | strong_accumulation | 2.18 | 1.82 | 2 | 3 | 1.66 | 4.31 | -12.82 |  | fail_low_response_condition |
| 6264 | 富裔 | 建材營造 | neutral |  | 539.4547163898465 | 16.095368677635587 | -0.66 | -0.98 | -10.77 | -19.12 | 5.22 | 5.22 | False |  | mild_accumulation | 0.02 | 0.04 | 1 | 1 | -0.62 | -0.78 | -12.82 |  | fail_low_response_condition |
| 6265 | 方土昶 | 電子通路業 | mainstream_growth |  | 885.8204211362734 | 548.8883789709856 | 14.5 | 35.68 | 63.18 | 231.18 | 75.75 | 238.46 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.88 | 5.83 | 2 | 2 | 23.88 | 22.39 | 0.0 |  | fail_low_response_condition |
| 6274 | 台燿 | 電子零組件業 | mainstream_growth |  | 97.9669823575258 | 68.62207240731209 | 3.25 | 9.28 | 225.49 | 284.52 | 260.54 | 299.0 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.63 | 0.08 | 2 | 1 | 6.89 | 8.79 | -12.4 |  | fail_low_response_condition |
| 6419 | 京晨科 | 光電業 | mainstream_growth |  | 328.6900742741391 | 98.87148285793438 | 6.79 | 9.12 | 90.93 | 165.54 | 87.34 | 181.02 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -3.33 | 1.81 | -23.14 |  | fail_low_response_condition |
| 6465 | 威潤 | 通信網路業 | mainstream_growth |  | 81.01909078423293 | 82.18097534533356 | 2.87 | 10.09 | 53.75 | 95.71 | 60.9 | 104.9 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.29 | 0.0 | 1 | 0 | 2.52 | 2.83 | -11.62 |  | fail_low_response_condition |
| 6560 | 欣普羅 | 光電業 | mainstream_growth |  | 95.9716688800354 | 81.27312594216801 | 4.99 | 1.52 | -2.68 | -2.2 | 7.83 | 7.83 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 4.35 | 3.65 | -10.83 |  | fail_low_response_condition |
| 6588 | 東典光電 | 通信網路業 | mainstream_growth |  | 155.81526861451462 | 166.62613189724436 | -3.9 | -23.45 | 39.1 | 170.73 | 53.53 | 212.24 | True | 距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.43 | -0.08 | 0 | 0 | -11.43 | -10.75 | -33.33 |  | fail_low_response_condition |
| 6596 | 寬宏藝術 | 文化創意業 | defensive_or_traditional |  | 1704.816147082334 | 82.9410719325939 | 1.04 | -6.73 | -35.55 | -29.96 | 2.0 | 2.0 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -0.6 | -1.4 | -35.97 |  | fail_low_response_condition |
| 6629 | 泰金-KY | 居家生活 | neutral |  | 140.46779704024576 | 88.1077857191744 | 0.43 | -2.48 | 7.27 | -9.92 | 14.56 | 16.83 | False |  | mild_accumulation | 0.32 | 0.0 | 1 | 0 | -2.42 | -0.83 | -13.87 |  | fail_low_response_condition |
| 6640 | 均華 | 半導體業 | mainstream_growth |  | 142.3351566529373 | 104.95596788763844 | -4.1 | -8.54 | 33.44 | 128.65 | 38.47 | 127.43 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -0.82 | 0 | 0 | -6.27 | -6.55 | -30.91 |  | fail_low_response_condition |
| 6654 | 天正國際 | 其他電子業 | mainstream_growth |  | 157.90690703549865 | 68.70958777211672 | 21.43 | 87.02 | 82.6 | 88.89 | 100.47 | 112.5 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.84 | 0.0 | 3 | 0 | 45.02 | 38.07 | -8.36 |  | fail_low_response_condition |
| 6693 | 廣閎科 | 半導體業 | mainstream_growth |  | 85.69637275568802 | 69.80142959357887 | -1.33 | -5.13 | 60.69 | 85.23 | 61.57 | 96.03 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.15 | 0.0 | 2 | 0 | 0.46 | 0.82 | -11.9 |  | fail_low_response_condition |
| 6727 | 亞泰金屬 | 電子零組件業 | mainstream_growth |  | 51.14904238647987 | 133.04676341354383 | -7.27 | 8.28 | 148.15 | 224.85 | 151.05 | 231.89 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.93 | -2.14 | 2 | 2 | -5.74 | -1.85 | -23.1 |  | fail_low_response_condition |
| 6735 | 美達科技 | 其他電子業 | mainstream_growth |  | 74.12994772218073 | 52.439125540612594 | -8.2 | -20.32 | 81.42 | 60.65 | 84.44 | 95.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.95 | -0.01 | 0 | 0 | -12.69 | -9.43 | -33.38 |  | fail_low_response_condition |
| 6739 | 竹陞科技 | 其他電子業 | mainstream_growth |  | 100.21067543270192 | 94.4190928623524 | 2.39 | -10.76 | 27.86 | 79.22 | 26.6 | 85.96 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.33 | 0.0 | 0 | 0 | 0.57 | -1.17 | -26.99 |  | fail_low_response_condition |
| 6823 | 濾能 | 半導體業 | mainstream_growth |  | 51.373600076577006 | 20.159064410973897 | 1.65 | -16.78 | 18.24 | 11.97 | 22.76 | 29.42 | False |  | mild_accumulation | 3.27 | -0.42 | 3 | 0 | -6.32 | -5.75 | -34.89 |  | fail_low_response_condition |
| 6870 | 騰雲 | 數位雲端 | neutral |  | 81.4559743113064 | 46.16926822282687 | 22.24 | 69.21 | 66.58 | 69.66 | 92.51 | 92.51 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | strong_accumulation | 4.21 | 3.16 | 3 | 2 | 38.32 | 34.68 | 0.0 |  | fail_low_response_condition |
| 6872 | 浩宇生醫 | 生技醫療業 | defensive_or_traditional |  | 226.31578947368425 | 1191.606080634501 | -1.7 | -3.89 | -3.35 | -15.82 | 4.22 | 4.22 | False |  | mild_accumulation | 0.02 | -0.03 | 2 | 0 | -3.53 | -3.04 | -15.2 |  | fail_low_response_condition |
| 6894 | 衛司特 | 綠能環保 | neutral |  | 88.3694636975864 | 66.9373448501468 | 10.83 | 17.53 | 29.34 | 97.52 | 33.0 | 109.45 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.01 | 0.0 | 0 | 0 | 9.61 | 8.29 | -4.55 |  | fail_low_response_condition |
| 6903 | 巨漢 | 其他電子業 | mainstream_growth |  | 297.0479452834268 | 340.505461957708 | -1.75 | -3.09 | 31.71 | 153.23 | 42.21 | 151.6 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.85 | -1.66 | 1 | 0 | -1.95 | -1.38 | -13.07 |  | fail_low_response_condition |
| 6907 | 雅特力-KY | 半導體業 | mainstream_growth |  | 121.6595027521801 | 86.77083705938229 | 8.51 | -4.14 | 22.6 | 4.94 | 29.97 | 210.98 | True | 距120日低點反彈>80% | distribution_warning | -0.69 | -0.69 | 0 | 0 | 6.12 | 4.64 | -27.14 |  | fail_low_response_condition |
| 7709 | 榮田 | 電機機械 | cyclical_turnaround |  | 62.90487773652541 | 26.63739686910983 | 32.84 | 61.23 | 136.7 | 249.02 | 148.14 | 256.0 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.27 | 0.0 | 1 | 0 | 40.11 | 37.04 | 0.0 |  | fail_low_response_condition |
| 7734 | 印能科技 | 半導體業 | mainstream_growth |  | 58.8980022049648 | 74.12973804714082 | -11.99 | -15.0 | 86.17 | 266.21 | 96.95 | 276.46 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.74 | -0.03 | 2 | 0 | -10.65 | -7.6 | -30.31 |  | fail_low_response_condition |
| 7744 | 崴寶 | 電子零組件業 | mainstream_growth |  | 80.50874225627649 | 69.42116815338996 | 4.6 | -9.58 | 1.42 | 76.06 | 18.91 | 88.68 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | -3.37 | 2 | 1 | -3.33 | -1.74 | -19.09 |  | fail_low_response_condition |
| 7751 | 竑騰 | 半導體業 | mainstream_growth |  | 67.2016980425343 | 71.46071764140272 | -3.19 | -4.57 | 28.46 | 177.41 | 33.07 | 187.93 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.06 | 1 | 1 | -3.22 | -7.5 | -40.46 |  | fail_low_response_condition |
| 7777 | 能率亞洲 | 其他 | neutral |  | 1298.0289793309184 | 202.0893895348837 | 8.31 | 42.78 | 42.78 | -1.44 | 76.94 | 86.17 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.35 | -3.12 | 1 | 1 | 13.78 | 14.04 | -10.37 |  | fail_low_response_condition |
| 7810 | 捷創科技 | 半導體業 | mainstream_growth |  | 82.68924780400619 | 52.16988808566341 | 3.76 | 0.64 | 25.07 | 1.08 | 26.42 | 48.42 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | 0.13 | 0.72 | -18.01 |  | fail_low_response_condition |
| 7820 | 立盈 | 綠能環保 | neutral |  | 57.764384593652885 | 61.84958999236623 | -3.16 | -18.33 | -1.21 | -1.21 | 2.08 | 2.08 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -7.58 | -6.46 | -23.44 |  | fail_low_response_condition |
| 7828 | 創新服務 | 半導體業 | mainstream_growth |  | 32086.88118811881 | 180.37838911510576 | 6.79 | 22.04 | 6.03 | 6.03 | 51.01 | 51.01 | True | 距60日低點反彈>50% | distribution_warning | -0.08 | 0.0 | 0 | 0 | 15.98 | 12.31 | -9.94 |  | fail_low_response_condition |
| 7842 | 天能綠電 | 綠能環保 | neutral |  | 52.8497323911156 | 75.97877416585146 | 0.9 | -11.16 | 1.36 | 1.36 | 12.63 | 12.63 | False |  | distribution_warning | -18.88 | -18.88 | 0 | 0 | 2.46 | 1.52 | -12.55 |  | fail_low_response_condition |
| 8034 | 榮群 | 通信網路業 | mainstream_growth |  | 106.45189301840917 | 59.3424941145042 | 5.47 | -1.38 | 0.4 | -8.58 | 9.87 | 9.87 | False |  | mild_accumulation | -0.5 | 2.1 | 2 | 3 | 3.59 | 3.28 | -7.22 |  | fail_low_response_condition |
| 8059 | 凱碩 | 通信網路業 | mainstream_growth |  | 228.65127813055827 | 576.1173591417349 | 4.99 | -4.08 | 8.7 | -0.25 | 17.99 | 19.4 | False |  | mild_accumulation | 0.33 | -0.02 | 2 | 0 | 3.51 | 2.73 | -18.7 |  | fail_low_response_condition |
| 8087 | 麗升能源 | 綠能環保 | neutral |  | 2881.2290969899664 | 328.017474558798 | 4.81 | -0.59 | -0.73 | -3.43 | 12.11 | 34.93 | False |  | distribution_warning | 0.0 | -1.85 | 1 | 2 | 0.75 | 1.01 | -14.65 |  | fail_low_response_condition |
| 8171 | 天宇 | 綠能環保 | neutral |  | 269.89458889669714 | 55.36585625139528 | 3.7 | -1.04 | -9.33 | -4.61 | 9.93 | 9.93 | False |  | distribution_warning | -0.13 | -0.05 | 0 | 1 | 0.93 | 0.85 | -13.14 |  | fail_low_response_condition |
| 8227 | 巨有科技 | 半導體業 | mainstream_growth |  | 207.0162789387709 | 125.3487613051306 | 4.94 | -1.33 | 72.2 | 49.16 | 97.35 | 97.35 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.53 | 0.0 | 2 | 0 | 3.7 | 7.16 | -10.44 |  | fail_low_response_condition |
| 8291 | 尚茂 | 電子零組件業 | mainstream_growth |  | 345.27363184079604 | 243.02925989672977 | -26.92 | 149.87 | -19.0 | -19.0 | 700.0 | 700.0 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -4.25 | -0.04 | 0 | 0 | 8.6 | 11.44 | -26.92 |  | fail_low_response_condition |
| 8299 | 群聯 | 半導體業 | mainstream_growth |  | 236.6326033058058 | 208.3172163574361 | 15.1 | 5.62 | 49.21 | 163.55 | 91.19 | 177.83 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.52 | -6.21 | 0 | 0 | 10.17 | 14.03 | -2.08 |  | fail_low_response_condition |
| 8489 | 三貝德 | 其他 | neutral |  | 57.791556753915486 | 56.6216199659393 | -0.44 | -9.6 | 3.91 | -45.15 | 3.91 | 4.63 | False |  | mild_accumulation | -1.14 | 1.8 | 2 | 3 | -5.71 | -5.98 | -24.54 |  | fail_low_response_condition |
| 8927 | 北基 | 油電燃氣業 | defensive_or_traditional |  | 50.67630705716537 | 35.21911926139916 | 7.71 | -2.25 | -18.2 | -29.42 | 9.22 | 9.22 | False |  | strong_accumulation | 0.45 | 0.35 | 2 | 2 | 2.54 | 0.16 | -22.88 |  | fail_low_response_condition |