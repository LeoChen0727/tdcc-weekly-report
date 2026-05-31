# 營收爆發低反應股 Debug Report

- 產生時間：`2026-05-31 20:41:39 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 884 |
| standardized_revenue_rows | 884 |
| price_rows | 567349 |
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
| 1591 | 駿吉-KY | 電機機械 | cyclical_turnaround |  | 510.66838046272494 | 743.7470682052725 | -12.04 | -37.77 | -8.74 | -12.61 | 23.69 | 23.69 | False |  | distribution_warning | -0.56 | 0.0 | 2 | 0 | -12.3 | -12.7 | -42.32 |  | fail_low_response_condition |
| 1799 | 易威 | 生技醫療業 | defensive_or_traditional |  | 240.44451280473737 | 83.17816490095692 | -1.63 | -13.75 | 14.66 | -4.86 | 20.25 | 20.25 | False |  | mild_accumulation | 0.34 | 0.0 | 3 | 2 | -4.34 | -5.0 | -25.95 |  | fail_low_response_condition |
| 1815 | 富喬 | 電子零組件業 | mainstream_growth |  | 53.16278671723507 | 40.47675320517641 | -1.85 | -3.64 | 9.17 | 34.35 | 12.53 | 34.18 | False |  | distribution_warning | -3.84 | -3.61 | 1 | 0 | 0.5 | -0.42 | -18.15 |  | fail_low_response_condition |
| 2230 | 泰茂 | 電機機械 | cyclical_turnaround |  | 77.86861915651653 | 65.520105323096 | -4.07 | -19.4 | -22.81 | -72.84 | 6.2 | 6.2 | False |  | strong_accumulation | 0.61 | 0.09 | 3 | 2 | -3.99 | -3.71 | -25.56 |  | fail_low_response_condition |
| 3081 | 聯亞 | 通信網路業 | mainstream_growth |  | 115.38448966249898 | 103.7026472556527 | -17.25 | -1.69 | 93.7 | 393.4 | 93.7 | 396.2 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.09 | -1.29 | 2 | 1 | -4.6 | -2.53 | -20.88 |  | fail_low_response_condition |
| 3085 | 新零售 | 數位雲端 | neutral |  | 96.80824327720532 | 18.285783074515468 | 1.22 | 5.51 | -1.19 | -19.68 | 14.22 | 14.22 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 0.5 | 1.15 | -12.32 |  | fail_low_response_condition |
| 3088 | 艾訊 | 電腦及週邊設備業 | mainstream_growth |  | 65.88230816535429 | 38.0977827651226 | -0.7 | 13.71 | 82.64 | 86.51 | 76.25 | 88.5 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.23 | 2.64 | 2 | 2 | 3.37 | 6.65 | -7.24 |  | fail_low_response_condition |
| 3147 | 大綜 | 資訊服務業 | mainstream_growth |  | 90.07098363534266 | 9.456031185015002 | -0.82 | 3.4 | 3.11 | 3.4 | 18.89 | 20.46 | False |  | distribution_warning | -0.95 | 0.0 | 2 | 0 | 1.01 | 1.43 | -5.93 |  | fail_low_response_condition |
| 3171 | 炎洲流通 | 居家生活 | neutral |  | 126.3478178187696 | 90.66142908048124 | -0.57 | 4.16 | 39.09 | 49.15 | 39.92 | 53.06 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 2.48 | 2.07 | -5.01 |  | fail_low_response_condition |
| 3188 | 鑫龍騰 | 建材營造 | neutral |  | 914.834168710675 | 892.3303586904568 | -2.18 | -8.92 | -31.13 | -27.23 | 0.45 | 0.45 | False |  | strong_accumulation | 0.34 | 0.31 | 2 | 2 | -5.37 | -6.22 | -37.2 |  | fail_low_response_condition |
| 3205 | 佰研 | 生技醫療業 | defensive_or_traditional |  | 67.90192099191015 | 51.567453071360745 | 1.31 | -3.57 | 5.47 | 20.4 | 8.76 | 21.9 | False |  | mild_accumulation | -0.4 | 2.01 | 1 | 1 | -0.24 | -1.07 | -19.4 |  | fail_low_response_condition |
| 3260 | 威剛 | 半導體業 | mainstream_growth |  | 169.50705162133545 | 165.38579121733795 | 1.22 | -10.08 | 36.51 | 137.14 | 35.84 | 141.98 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.69 | -5.27 | 0 | 0 | -1.37 | -0.3 | -20.95 |  | fail_low_response_condition |
| 3290 | 東浦 | 電子零組件業 | mainstream_growth |  | 69.35257646971267 | 79.9307324458115 | 0.1 | 3.08 | 14.93 | 16.03 | 18.87 | 20.8 | False |  | distribution_warning | -0.27 | -0.42 | 2 | 1 | 1.89 | 1.61 | -6.73 |  | fail_low_response_condition |
| 3297 | 杭特 | 光電業 | mainstream_growth |  | 53.69808926179228 | 21.124604723137995 | -2.33 | -7.84 | -16.36 | -31.79 | 0.34 | 0.34 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.13 | -4.67 | -25.38 |  | fail_low_response_condition |
| 3313 | 斐成 | 其他 | neutral |  | 125.59241706161136 | 626.336898395722 | -0.89 | -5.93 | -7.88 | -23.97 | 2.3 | 2.3 | False |  | strong_accumulation | 0.35 | 0.37 | 3 | 3 | -2.78 | -3.66 | -20.43 |  | fail_low_response_condition |
| 3354 | 律勝 | 電子零組件業 | mainstream_growth |  | 52.02821869488536 | 20.249566527386943 | -7.31 | -7.31 | 25.79 | 87.02 | 34.32 | 87.02 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.24 | 0.0 | 1 | 0 | -4.8 | -1.21 | -15.69 |  | fail_low_response_condition |
| 3466 | 德晉 | 通信網路業 | mainstream_growth |  | 2243.126742440489 | 1259.5214156444802 | -2.08 | -19.34 | -7.44 | -29.14 | 1.54 | 1.54 | False |  | mild_accumulation | -0.56 | 1.36 | 1 | 3 | -7.1 | -6.32 | -28.06 |  | fail_low_response_condition |
| 3489 | 森寶 | 建材營造 | neutral |  | 113.51012213485026 | 120.45474675135702 | -0.46 | -0.68 | 14.44 | 10.66 | 12.95 | 15.34 | False |  | mild_accumulation | 0.57 | 0.0 | 1 | 0 | -0.67 | -0.87 | -11.02 |  | fail_low_response_condition |
| 3491 | 昇達科 | 通信網路業 | mainstream_growth |  | 83.9939064567311 | 69.07810246379388 | 6.02 | 35.8 | 86.44 | 318.25 | 95.56 | 327.18 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.1 | 0.06 | 2 | 1 | 15.38 | 14.3 | 0.0 |  | fail_low_response_condition |
| 3498 | 陽程 | 其他電子業 | mainstream_growth |  | 137.82244323121327 | 107.83813918263162 | -2.58 | 55.19 | 172.56 | 191.51 | 150.83 | 221.96 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 9.57 | 8.4 | 3 | 2 | 6.53 | 10.55 | -8.21 |  | fail_low_response_condition |
| 3512 | 皇龍 | 建材營造 | neutral |  | 147.80032587764777 | -67.85821774084044 | 0.49 | 0.49 | 0.49 | 0.0 | 3.27 | 3.79 | False |  | mild_accumulation | 0.02 | -0.03 | 1 | 0 | 0.85 | -0.1 | -6.59 |  | fail_low_response_condition |
| 3523 | 迎輝 | 光電業 | mainstream_growth |  | 197.78021375719376 | -28.177372219240173 | 32.92 | 27.09 | -0.31 | -11.88 | 66.84 | 66.84 | True | 近20日漲幅>25%；距60日低點反彈>50% | mild_accumulation | 0.47 | 0.0 | 2 | 0 | 32.6 | 24.52 | -13.32 |  | fail_low_response_condition |
| 3555 | 博士旺 | 半導體業 | mainstream_growth |  | 2832.482993197279 | 3831.740379092476 | -11.96 | -10.48 | 81.7 | 202.41 | 79.41 | 220.57 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.88 | 0.88 | 1 | 1 | -2.32 | -3.4 | -24.16 |  | fail_low_response_condition |
| 3577 | 泓格 | 電腦及週邊設備業 | mainstream_growth |  | 89.01210915432416 | 36.29945032117057 | 2.61 | 79.79 | 174.87 | 154.85 | 169.23 | 178.27 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.45 | 0.02 | 1 | 1 | 19.74 | 19.75 | -9.22 |  | fail_low_response_condition |
| 3594 | 磐儀 | 電腦及週邊設備業 | mainstream_growth |  | 50.36666640125487 | 36.33687909638193 | -4.91 | -9.21 | 25.91 | 32.89 | 32.02 | 42.7 | False |  | distribution_warning | -0.23 | -0.21 | 2 | 0 | -2.87 | -1.61 | -15.6 |  | fail_low_response_condition |
| 3629 | 地心引力 | 文化創意業 | defensive_or_traditional |  | 261400.0 | 75119.04761904762 | -0.9 | 2.81 | -24.19 | 0.0 | 4.44 | 4.44 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.22 | -2.6 | -24.37 |  | fail_low_response_condition |
| 3672 | 康聯訊 | 通信網路業 | mainstream_growth |  | 120.0719634347953 | -21.66306364905971 | 0.0 | -8.33 | -6.38 | -12.35 | 6.28 | 6.28 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -1.37 | -1.85 | -23.61 |  | fail_low_response_condition |
| 3680 | 家登 | 半導體業 | mainstream_growth |  | 52.739619752984254 | 20.16580656803387 | -8.32 | -7.69 | 48.15 | 60.71 | 45.16 | 72.52 | True | 近60日漲幅>40% | mild_accumulation | -1.62 | 1.2 | 2 | 1 | -3.76 | -0.73 | -13.32 |  | fail_low_response_condition |
| 3685 | 元創精密 | 電機機械 | cyclical_turnaround |  | 74.29675942423358 | 55.40714795511386 | -1.93 | -4.61 | -11.27 | -19.68 | 10.47 | 10.47 | False |  | distribution_warning | -0.05 | -0.2 | 2 | 0 | -2.3 | -3.59 | -22.79 |  | fail_low_response_condition |
| 3691 | 碩禾 | 光電業 | mainstream_growth |  | 163.4117868279612 | 175.67923400100153 | 3.18 | 23.19 | 43.36 | 129.46 | 58.82 | 129.79 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.65 | -2.83 | 1 | 0 | 8.6 | 10.85 | -3.57 |  | fail_low_response_condition |
| 4127 | 天良 | 生技醫療業 | defensive_or_traditional |  | 66.79204076680418 | 69.33155758498225 | 1.32 | 78.06 | 90.87 | 127.72 | 99.13 | 137.93 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 6.87 | 3.69 | 2 | 2 | 23.4 | 21.4 | -7.75 |  | fail_low_response_condition |
| 4154 | 樂威科-KY | 其他 | neutral |  | 99.26590538336052 | 1.244490536686544 | -3.68 | 16.44 | 16.44 | -23.39 | 39.51 | 39.51 | False |  | mild_accumulation | 0.83 | -0.45 | 3 | 0 | -2.66 | -2.49 | -15.48 |  | fail_low_response_condition |
| 4168 | 醣聯 | 生技醫療業 | defensive_or_traditional |  | 185.7142857142857 | -1.9671209779401435 | -9.89 | 11.6 | 6.25 | 20.57 | 15.38 | 20.57 | False |  | mild_accumulation | 0.01 | 0.01 | 1 | 1 | 0.66 | 0.01 | -12.07 |  | fail_low_response_condition |
| 4529 | 淳紳 | 其他 | neutral |  | 472.1603563474388 | 113.87800783435928 | -4.53 | 5.66 | 32.51 | 25.0 | 72.6 | 72.6 | True | 距60日低點反彈>50% | neutral | 0.0 | 0.0 | 0 | 0 | -7.91 | -4.44 | -26.29 |  | fail_low_response_condition |
| 4530 | 宏易 | 觀光餐旅 | defensive_or_traditional |  | 230.49152002910017 | 78.04070042593469 | -1.96 | -1.57 | -12.89 | 128.31 | 8.23 | 140.38 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.11 | 0.0 | 3 | 0 | -1.79 | -2.59 | -20.89 |  | fail_low_response_condition |
| 4558 | 寶緯 | 電機機械 | cyclical_turnaround |  | 84.83396047199795 | 4.509365967190961 | -1.75 | 3.42 | 6.22 | -1.26 | 6.5 | 8.56 | False |  | distribution_warning | -0.11 | -0.09 | 0 | 0 | -0.95 | -0.31 | -13.82 |  | fail_low_response_condition |
| 4577 | 達航科技 | 其他電子業 | mainstream_growth |  | 62.5793018983466 | 56.34887065392099 | -18.32 | -28.75 | 32.42 | 106.86 | 37.48 | 126.4 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.29 | -4.71 | 1 | 0 | -13.48 | -13.84 | -41.32 |  | fail_low_response_condition |
| 4711 | 永純 | 化學工業 | cyclical_turnaround |  | 89.32523504451285 | 23.470589276860967 | -1.47 | 7.4 | 11.71 | 12.08 | 12.46 | 14.78 | False |  | distribution_warning | -1.09 | -0.16 | 0 | 0 | 0.44 | 0.98 | -14.14 |  | fail_low_response_condition |
| 4714 | 永捷 | 化學工業 | cyclical_turnaround |  | 96.03344108366043 | 95.91632424000304 | -6.29 | -10.67 | -11.55 | -18.04 | 4.28 | 4.28 | False |  | distribution_warning | -1.33 | -0.72 | 0 | 1 | -1.85 | -3.03 | -23.21 |  | fail_low_response_condition |
| 4726 | 永昕 | 生技醫療業 | defensive_or_traditional |  | 301.006875305256 | 104.64090930541416 | -1.09 | -5.4 | -17.85 | -15.68 | 0.56 | 0.56 | False |  | neutral | 0.0 | 0.0 | 1 | 0 | -3.77 | -3.8 | -18.47 |  | fail_low_response_condition |
| 4743 | 合一 | 生技醫療業 | defensive_or_traditional |  | 101.82665424044734 | 62.11088547027568 | -0.59 | -4.73 | -3.82 | -26.32 | 2.86 | 2.86 | False |  | distribution_warning | -0.52 | -0.58 | 2 | 1 | -1.53 | -2.11 | -14.58 |  | fail_low_response_condition |
| 4760 | 勤凱科技 | 其他電子業 | mainstream_growth |  | 63.098631698973776 | 54.91021842087173 | 18.33 | 75.28 | 187.12 | 160.0 | 180.24 | 189.78 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.21 | -3.56 | 1 | 0 | 33.59 | 31.75 | 0.0 |  | fail_low_response_condition |
| 4768 | 晶呈科技 | 化學工業 | cyclical_turnaround |  | 191.53168275283247 | 166.3777307047525 | -5.44 | -9.36 | 16.94 | 126.27 | 17.23 | 125.72 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.99 | -4.87 | 1 | 0 | 1.22 | -0.42 | -19.74 |  | fail_low_response_condition |
| 4772 | 台特化 | 化學工業 | cyclical_turnaround |  | 210.12358034898395 | 266.4543899237024 | -0.99 | -2.6 | 1.01 | -1.48 | 10.09 | 10.09 | False |  | strong_accumulation | 0.14 | 0.27 | 2 | 2 | -1.25 | -1.1 | -13.17 |  | fail_low_response_condition |
| 4907 | 富宇 | 建材營造 | neutral |  | 402.7102995324487 | 265.58397526745915 | -3.78 | -4.94 | -9.87 | -14.93 | 1.42 | 1.42 | False |  | mild_accumulation | 0.01 | 0.0 | 1 | 0 | -5.62 | -4.97 | -15.24 |  | fail_low_response_condition |
| 4931 | 新盛力 | 電腦及週邊設備業 | mainstream_growth |  | 97.38306551458992 | 35.10154042171776 | 6.74 | 39.94 | 90.46 | 37.84 | 87.35 | 92.86 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | mild_accumulation | 5.47 | 2.61 | 2 | 1 | 12.76 | 14.52 | -3.57 |  | fail_low_response_condition |
| 4973 | 廣穎電通 | 半導體業 | mainstream_growth |  | 106.0995211097044 | 82.0904184804944 | 26.48 | 67.54 | 247.45 | 373.37 | 224.87 | 391.55 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 2.65 | 2.69 | 2 | 2 | 28.53 | 29.34 | -3.03 |  | fail_low_response_condition |
| 4991 | 環宇-KY | 半導體業 | mainstream_growth |  | 67.9225669656687 | 55.01101125702958 | -16.09 | 5.8 | 136.25 | 357.68 | 153.47 | 359.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.68 | -0.57 | 2 | 2 | -1.05 | 0.55 | -18.44 |  | fail_low_response_condition |
| 5228 | 鈺鎧 | 電子零組件業 | mainstream_growth |  | 62.02852912838108 | 51.74961237953364 | 16.58 | 76.07 | 201.89 | 266.76 | 201.18 | 275.37 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -8.34 | -2.85 | 0 | 0 | 22.37 | 24.56 | -1.54 |  | fail_low_response_condition |
| 5263 | 智崴 | 文化創意業 | defensive_or_traditional |  | 61.94202436252717 | 36.68329399189418 | -4.17 | -0.48 | 7.92 | 19.79 | 17.08 | 20.91 | False |  | mild_accumulation | 1.28 | -0.07 | 2 | 1 | -3.02 | -1.43 | -10.0 |  | fail_low_response_condition |
| 5274 | 信驊 | 半導體業 | mainstream_growth |  | 81.593085197006 | 59.80710332909424 | 9.92 | 5.93 | 104.86 | 174.04 | 104.2 | 195.86 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.4 | -0.25 | 2 | 0 | 8.01 | 9.04 | -2.87 |  | fail_low_response_condition |
| 5289 | 宜鼎 | 電腦及週邊設備業 | mainstream_growth |  | 583.1104370746453 | 452.2084788945506 | 7.1 | 14.92 | 119.93 | 274.74 | 119.39 | 306.29 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.45 | -0.01 | 0 | 1 | 3.71 | 9.37 | -6.46 |  | fail_low_response_condition |
| 5291 | 邑昇 | 電子零組件業 | mainstream_growth |  | 69.45516610517392 | 36.664686579042986 | -3.88 | 12.19 | 31.26 | 157.81 | 48.04 | 171.97 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 3.04 | -2.75 | 2 | 2 | -1.47 | -0.01 | -15.13 |  | fail_low_response_condition |
| 5314 | 世紀* | 其他 | neutral |  | 138.62470941331696 | 161.5030245941451 | 0.0 | -12.62 | -21.05 | -43.24 | 2.94 | 2.94 | False |  | distribution_warning | -1.69 | -0.94 | 1 | 1 | -5.43 | -6.06 | -28.33 |  | fail_low_response_condition |
| 5345 | 馥鴻 | 其他 | neutral |  | 562.4398073836276 | 355.7700377675199 | 18.47 | 5.9 | -1.1 | -9.66 | 23.01 | 23.01 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | 8.1 | 6.61 | -6.46 |  | fail_low_response_condition |
| 5351 | 鈺創 | 半導體業 | mainstream_growth |  | 417.0626132083888 | 359.7438728245971 | 4.87 | 11.51 | 56.44 | 123.61 | 54.48 | 131.41 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.13 | 1.35 | 2 | 2 | 4.72 | 6.94 | -8.3 |  | fail_low_response_condition |
| 5386 | 青雲 | 電腦及週邊設備業 | mainstream_growth |  | 405.25703262628434 | 537.622375622673 | 8.01 | 13.6 | 107.34 | 713.44 | 129.84 | 756.94 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -2.16 | 0.0 | 0 | 0 | 19.71 | 18.73 | -5.57 |  | fail_low_response_condition |
| 5410 | 國眾 | 資訊服務業 | mainstream_growth |  | 122.27479364891022 | 37.89174869171116 | 5.83 | 9.45 | 31.85 | 31.63 | 34.06 | 37.29 | False |  | strong_accumulation | 1.63 | 1.48 | 2 | 2 | 4.62 | 6.29 | 0.0 |  | fail_low_response_condition |
| 5475 | 德宏 | 電子零組件業 | mainstream_growth |  | 120.58864400655902 | 101.17685065534428 | -11.48 | -22.41 | 46.34 | 365.52 | 51.26 | 363.12 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.28 | -1.69 | 2 | 2 | -8.54 | -8.46 | -33.25 |  | fail_low_response_condition |
| 5488 | 松普 | 電子零組件業 | mainstream_growth |  | 93.29563197379946 | 37.99866980581613 | 2.95 | 22.0 | 29.65 | 28.96 | 31.89 | 37.08 | False |  | strong_accumulation | 1.43 | 1.15 | 3 | 2 | 8.66 | 8.11 | -1.61 |  | fail_low_response_condition |
| 5498 | 凱崴 | 電子零組件業 | mainstream_growth |  | 54.63972516047374 | 50.28516602297845 | -6.4 | -11.8 | 19.42 | 144.16 | 26.78 | 160.59 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -3.2 | -2.0 | 1 | 0 | -3.26 | -2.96 | -24.54 |  | fail_low_response_condition |
| 5514 | 三豐 | 建材營造 | neutral |  | 359.86984815618223 | 34979.69569779643 | -7.33 | -11.46 | -12.3 | 0.0 | 1.46 | 1.46 | False |  | mild_accumulation | 0.07 | 0.01 | 2 | 1 | -7.79 | -7.2 | -17.26 |  | fail_low_response_condition |
| 5529 | 鉅陞 | 建材營造 | neutral |  | 3460.343434343434 | 2385.27557453732 | -6.71 | 1.83 | -13.09 | -12.57 | 5.95 | 5.95 | False |  | mild_accumulation | -0.1 | 0.08 | 2 | 2 | -2.98 | -3.38 | -20.54 |  | fail_low_response_condition |
| 5864 | 致和證 | 金融業 | defensive_or_traditional |  | 2037.1729784841127 | 779.9502128124395 | 22.65 | 25.51 | 84.37 | 185.1 | 86.77 | 208.6 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.65 | -1.7 | 1 | 1 | 22.99 | 22.84 | 0.0 |  | fail_low_response_condition |
| 5905 | 南仁湖 | 觀光餐旅 | defensive_or_traditional |  | 686.3773953069496 | 307.26437021074355 | -1.38 | -2.12 | -3.8 | -13.47 | 3.16 | 3.16 | False |  | mild_accumulation | 0.08 | -0.43 | 2 | 0 | -3.1 | -2.2 | -14.97 |  | fail_low_response_condition |
| 6015 | 宏遠證 | 金融業 | defensive_or_traditional |  | 4229.158188258347 | 732.2032127625579 | 18.04 | 20.25 | 50.78 | 84.69 | 49.03 | 85.58 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 1.86 | 1.08 | 2 | 2 | 18.02 | 17.31 | -1.03 |  | fail_low_response_condition |
| 6016 | 康和證 | 金融業 | defensive_or_traditional |  | 1127.2871745131688 | 4803.222264258889 | 21.81 | 35.16 | 83.28 | 129.46 | 81.6 | 131.25 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -1.19 | -0.5 | 0 | 1 | 22.23 | 22.41 | 0.0 |  | fail_low_response_condition |
| 6020 | 大展證 | 金融業 | defensive_or_traditional |  | 2338.3188675346146 | 2577.8824833702884 | 8.56 | 23.91 | 26.84 | 29.92 | 28.19 | 30.98 | False |  | distribution_warning | -0.3 | -0.48 | 1 | 1 | 8.38 | 9.47 | -3.79 |  | fail_low_response_condition |
| 6021 | 美好證 | 金融業 | defensive_or_traditional |  | 5212.463185451826 | 1481.8435288230107 | 14.42 | 5.73 | 20.2 | 45.85 | 31.55 | 50.0 | False |  | distribution_warning | 0.0 | -0.01 | 1 | 1 | 10.47 | 9.78 | -0.67 |  | fail_low_response_condition |
| 6026 | 福邦證 | 金融業 | defensive_or_traditional |  | 461.7024055162327 | 380.76366102689127 | 6.98 | 0.9 | 27.17 | 39.26 | 24.35 | 39.83 | False |  | distribution_warning | -0.38 | -0.83 | 1 | 1 | 6.16 | 6.17 | -0.88 |  | fail_low_response_condition |
| 6111 | 光聚晶電 | 文化創意業 | defensive_or_traditional |  | 149.45364292025778 | 134.09032530399222 | -0.44 | -5.14 | 9.44 | -1.31 | 13.28 | 13.28 | False |  | strong_accumulation | 1.42 | 1.25 | 3 | 3 | -3.41 | -2.17 | -10.5 |  | fail_low_response_condition |
| 6125 | 廣運 | 光電業 | mainstream_growth |  | 56.77567839472995 | 37.581989499569296 | -2.49 | 12.67 | 17.02 | 7.75 | 29.51 | 29.51 | False |  | mild_accumulation | 0.37 | -0.77 | 2 | 1 | 8.86 | 7.94 | -6.84 |  | fail_low_response_condition |
| 6171 | 大城地產 | 建材營造 | neutral |  | 211784.84848484848 | 565.1510373967333 | -2.5 | -8.24 | -15.83 | -14.6 | 1.3 | 1.3 | False |  | strong_accumulation | 0.11 | 0.11 | 2 | 2 | -2.84 | -3.64 | -17.46 |  | fail_low_response_condition |
| 6179 | 亞通 | 其他 | neutral |  | 69.36285627295153 | 54.76822782478532 | -1.85 | -0.83 | -4.79 | -26.95 | 2.36 | 2.36 | False |  | strong_accumulation | 0.53 | 0.25 | 2 | 2 | -2.62 | -2.33 | -18.74 |  | fail_low_response_condition |
| 6199 | 天品 | 其他 | neutral |  | 516.9373318720733 | 963.5349918331448 | -3.29 | -5.99 | -2.99 | -2.15 | 3.64 | 3.64 | False |  | distribution_warning | -3.58 | -3.33 | 0 | 0 | -6.74 | -5.79 | -28.63 |  | fail_low_response_condition |
| 6218 | 豪勉 | 通信網路業 | mainstream_growth |  | 98.94734925057824 | 24.203979861860773 | -0.76 | 5.12 | 65.96 | 116.07 | 71.81 | 116.67 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 0.61 | 0.33 | 2 | 2 | -2.79 | -0.21 | -16.31 |  | fail_low_response_condition |
| 6219 | 富旺 | 建材營造 | neutral |  | 21424.40677966101 | 18959.528301886792 | 1.26 | -6.59 | -18.31 | -38.05 | 5.7 | 5.7 | False |  | strong_accumulation | 1.4 | 0.64 | 3 | 3 | -1.11 | -2.34 | -28.27 |  | fail_low_response_condition |
| 6223 | 旺矽 | 半導體業 | mainstream_growth |  | 52.59594490792657 | 42.51276664792454 | -4.49 | 18.49 | 119.12 | 176.57 | 107.67 | 194.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.24 | -0.27 | 1 | 1 | 1.6 | 3.98 | -10.58 |  | fail_low_response_condition |
| 6228 | 全譜 | 電腦及週邊設備業 | mainstream_growth |  | 101.31396957123098 | -15.30696332921302 | -1.9 | -7.81 | -15.71 | -17.23 | 1.23 | 1.23 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -4.45 | -5.39 | -20.42 |  | fail_low_response_condition |
| 6229 | 研通 | 半導體業 | mainstream_growth |  | 57.360134931273095 | 48.52972335584195 | -3.44 | -14.45 | 20.59 | 19.78 | 33.25 | 33.25 | False |  | mild_accumulation | -0.17 | 0.05 | 1 | 1 | -2.93 | -0.65 | -14.72 |  | fail_low_response_condition |
| 6237 | 驊訊 | 半導體業 | mainstream_growth |  | 116.12150730581902 | 55.45139627457535 | -6.16 | 26.7 | 41.09 | 26.22 | 44.96 | 44.96 | True | 近20日漲幅>25%；近60日漲幅>40% | strong_accumulation | 2.18 | 1.82 | 2 | 3 | 1.46 | 3.51 | -14.02 |  | fail_low_response_condition |
| 6264 | 富裔 | 建材營造 | neutral |  | 539.4547163898465 | 16.095368677635587 | 0.33 | -0.49 | -9.13 | -16.74 | 5.57 | 5.57 | False |  | mild_accumulation | 0.02 | 0.04 | 1 | 1 | -0.38 | -0.59 | -12.91 |  | fail_low_response_condition |
| 6265 | 方土昶 | 電子通路業 | mainstream_growth |  | 885.8204211362734 | 548.8883789709856 | 4.35 | 27.19 | 63.31 | 214.53 | 62.35 | 221.87 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | strong_accumulation | 5.88 | 5.83 | 2 | 2 | 14.23 | 13.35 | -4.99 |  | fail_low_response_condition |
| 6274 | 台燿 | 電子零組件業 | mainstream_growth |  | 97.9669823575258 | 68.62207240731209 | 6.96 | 16.96 | 272.25 | 307.23 | 283.22 | 324.09 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | -0.63 | 0.08 | 2 | 1 | 15.44 | 18.46 | -2.59 |  | fail_low_response_condition |
| 6419 | 京晨科 | 光電業 | mainstream_growth |  | 328.6900742741391 | 98.87148285793438 | -8.77 | 4.07 | 106.31 | 145.63 | 102.45 | 164.1 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | neutral | 0.0 | 0.0 | 0 | 0 | -8.84 | -4.44 | -27.76 |  | fail_low_response_condition |
| 6465 | 威潤 | 通信網路業 | mainstream_growth |  | 81.01909078423293 | 82.18097534533356 | -5.52 | -4.01 | 42.77 | 111.01 | 53.53 | 95.51 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.29 | 0.0 | 1 | 0 | -1.64 | -1.68 | -15.67 |  | fail_low_response_condition |
| 6560 | 欣普羅 | 光電業 | mainstream_growth |  | 95.9716688800354 | 81.27312594216801 | -1.66 | -0.52 | -1.28 | -5.41 | 3.91 | 3.91 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | 0.4 | 0.12 | -14.06 |  | fail_low_response_condition |
| 6588 | 東典光電 | 通信網路業 | mainstream_growth |  | 155.81526861451462 | 166.62613189724436 | -16.04 | -24.75 | 56.03 | 227.51 | 63.52 | 225.14 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.43 | -0.08 | 0 | 0 | -12.66 | -11.58 | -32.43 |  | fail_low_response_condition |
| 6596 | 寬宏藝術 | 文化創意業 | defensive_or_traditional |  | 1704.816147082334 | 82.9410719325939 | -1.74 | -2.83 | -34.92 | -30.43 | 0.95 | 0.95 | False |  | mild_accumulation | 0.02 | 0.0 | 1 | 0 | -2.04 | -2.64 | -38.06 |  | fail_low_response_condition |
| 6629 | 泰金-KY | 居家生活 | neutral |  | 140.46779704024576 | 88.1077857191744 | -0.85 | -1.68 | 7.34 | -11.03 | 14.15 | 15.84 | False |  | mild_accumulation | 0.32 | 0.0 | 1 | 0 | -3.49 | -1.98 | -14.6 |  | fail_low_response_condition |
| 6640 | 均華 | 半導體業 | mainstream_growth |  | 142.3351566529373 | 104.95596788763844 | -6.51 | -1.8 | 68.31 | 148.63 | 61.35 | 148.63 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.88 | -0.82 | 0 | 0 | -1.16 | -1.76 | -26.61 |  | fail_low_response_condition |
| 6654 | 天正國際 | 其他電子業 | mainstream_growth |  | 157.90690703549865 | 68.70958777211672 | 32.76 | 69.79 | 74.01 | 81.18 | 81.6 | 92.5 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 2.84 | 0.0 | 3 | 0 | 40.9 | 34.72 | 0.0 |  | fail_low_response_condition |
| 6693 | 廣閎科 | 半導體業 | mainstream_growth |  | 85.69637275568802 | 69.80142959357887 | -5.71 | -1.0 | 79.78 | 87.03 | 78.06 | 96.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.15 | 0.0 | 2 | 0 | 0.63 | 1.57 | -11.61 |  | fail_low_response_condition |
| 6727 | 亞泰金屬 | 電子零組件業 | mainstream_growth |  | 51.14904238647987 | 133.04676341354383 | -9.98 | 27.81 | 220.22 | 246.75 | 232.01 | 262.85 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.93 | -2.14 | 2 | 2 | 3.91 | 7.28 | -15.93 |  | fail_low_response_condition |
| 6735 | 美達科技 | 其他電子業 | mainstream_growth |  | 74.12994772218073 | 52.439125540612594 | -6.52 | -20.37 | 102.45 | 67.97 | 110.37 | 110.78 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -0.95 | -0.01 | 0 | 0 | -7.71 | -3.62 | -28.09 |  | fail_low_response_condition |
| 6739 | 竹陞科技 | 其他電子業 | mainstream_growth |  | 100.21067543270192 | 94.4190928623524 | -9.19 | -9.85 | 30.69 | 90.88 | 32.09 | 91.77 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.33 | 0.0 | 0 | 0 | -4.19 | -5.43 | -29.83 |  | fail_low_response_condition |
| 6823 | 濾能 | 半導體業 | mainstream_growth |  | 51.373600076577006 | 20.159064410973897 | -9.43 | -25.89 | 26.08 | 11.11 | 21.67 | 27.85 | False |  | mild_accumulation | 3.27 | -0.42 | 3 | 0 | -9.16 | -7.89 | -35.68 |  | fail_low_response_condition |
| 6870 | 騰雲 | 數位雲端 | neutral |  | 81.4559743113064 | 46.16926822282687 | 14.16 | 47.78 | 46.56 | 39.27 | 59.28 | 59.28 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50% | strong_accumulation | 4.21 | 3.16 | 3 | 2 | 20.57 | 17.9 | -4.32 |  | fail_low_response_condition |
| 6872 | 浩宇生醫 | 生技醫療業 | defensive_or_traditional |  | 226.31578947368425 | 1191.606080634501 | -3.87 | -4.4 | -3.33 | -18.12 | 4.82 | 4.82 | False |  | mild_accumulation | 0.02 | -0.03 | 2 | 0 | -3.4 | -3.13 | -14.71 |  | fail_low_response_condition |
| 6894 | 衛司特 | 綠能環保 | neutral |  | 88.3694636975864 | 66.9373448501468 | 3.59 | 13.56 | 32.71 | 87.71 | 32.26 | 104.46 | True | 近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.01 | 0.0 | 0 | 0 | 8.75 | 7.67 | -6.82 |  | fail_low_response_condition |
| 6903 | 巨漢 | 其他電子業 | mainstream_growth |  | 297.0479452834268 | 340.505461957708 | -8.53 | -4.57 | 40.28 | 148.9 | 44.89 | 164.67 | True | 近60日漲幅>40%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -0.85 | -1.66 | 1 | 0 | -1.24 | -0.31 | -12.07 |  | fail_low_response_condition |
| 6907 | 雅特力-KY | 半導體業 | mainstream_growth |  | 121.6595027521801 | 86.77083705938229 | 0.0 | -8.3 | 17.96 | 0.0 | 24.87 | 196.34 | True | 距120日低點反彈>80% | distribution_warning | -0.69 | -0.69 | 0 | 0 | 0.83 | 0.65 | -30.57 |  | fail_low_response_condition |
| 7709 | 榮田 | 電機機械 | cyclical_turnaround |  | 62.90487773652541 | 26.63739686910983 | 20.5 | 25.14 | 136.62 | 190.79 | 132.14 | 195.06 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.27 | 0.0 | 1 | 0 | 21.58 | 20.57 | 0.0 |  | fail_low_response_condition |
| 7734 | 印能科技 | 半導體業 | mainstream_growth |  | 58.8980022049648 | 74.12973804714082 | 1.8 | 0.14 | 135.58 | 319.04 | 137.86 | 328.32 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 1.74 | -0.03 | 2 | 0 | 0.57 | 4.12 | -20.71 |  | fail_low_response_condition |
| 7744 | 崴寶 | 電子零組件業 | mainstream_growth |  | 80.50874225627649 | 69.42116815338996 | -2.57 | -11.51 | 18.27 | 73.85 | 17.0 | 85.66 | True | 近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.94 | -3.37 | 2 | 1 | -5.91 | -3.57 | -20.39 |  | fail_low_response_condition |
| 7751 | 竑騰 | 半導體業 | mainstream_growth |  | 67.2016980425343 | 71.46071764140272 | 0.28 | -18.1 | 63.43 | 233.65 | 54.82 | 220.33 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | mild_accumulation | 0.07 | 0.06 | 1 | 1 | 1.73 | -2.84 | -37.08 |  | fail_low_response_condition |
| 7777 | 能率亞洲 | 其他 | neutral |  | 1298.0289793309184 | 202.0893895348837 | 15.69 | 43.87 | 55.41 | 0.0 | 79.53 | 88.89 | True | 近20日漲幅>25%；近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -2.35 | -3.12 | 1 | 1 | 19.95 | 19.66 | 0.0 |  | fail_low_response_condition |
| 7810 | 捷創科技 | 半導體業 | mainstream_growth |  | 82.68924780400619 | 52.16988808566341 | -1.9 | 6.67 | 34.1 | 0.0 | 31.82 | 46.84 | False |  | distribution_warning | -0.06 | 0.0 | 0 | 0 | -0.23 | 0.16 | -18.88 |  | fail_low_response_condition |
| 7820 | 立盈 | 綠能環保 | neutral |  | 57.764384593652885 | 61.84958999236623 | -7.12 | -12.68 | 0.0 | 0.0 | 0.0 | 0.0 | False |  | neutral | 0.0 | 0.0 | 0 | 0 | -7.88 | -6.15 | -22.5 |  | fail_low_response_condition |
| 7828 | 創新服務 | 半導體業 | mainstream_growth |  | 32086.88118811881 | 180.37838911510576 | 0.36 | 18.49 | 0.0 | 0.0 | 42.42 | 42.42 | False |  | distribution_warning | -0.08 | 0.0 | 0 | 0 | 12.02 | 8.12 | -15.06 |  | fail_low_response_condition |
| 7842 | 天能綠電 | 綠能環保 | neutral |  | 52.8497323911156 | 75.97877416585146 | -9.09 | 0.0 | 0.0 | 0.0 | 11.11 | 11.11 | False |  | distribution_warning | -18.88 | -18.88 | 0 | 0 | 0.57 | 0.57 | -13.73 |  | fail_low_response_condition |
| 8034 | 榮群 | 通信網路業 | mainstream_growth |  | 106.45189301840917 | 59.3424941145042 | -1.24 | 0.84 | -0.62 | -12.45 | 4.82 | 4.82 | False |  | mild_accumulation | -0.5 | 2.1 | 2 | 3 | -1.46 | -1.14 | -11.48 |  | fail_low_response_condition |
| 8059 | 凱碩 | 通信網路業 | mainstream_growth |  | 228.65127813055827 | 576.1173591417349 | -3.79 | -7.07 | 11.4 | -4.75 | 12.39 | 13.73 | False |  | mild_accumulation | 0.33 | -0.02 | 2 | 0 | -1.99 | -2.05 | -22.56 |  | fail_low_response_condition |
| 8087 | 麗升能源 | 綠能環保 | neutral |  | 2881.2290969899664 | 328.017474558798 | 0.0 | 0.3 | 1.07 | -9.35 | 9.29 | 31.54 | False |  | distribution_warning | 0.0 | -1.85 | 1 | 2 | -1.69 | -1.32 | -16.79 |  | fail_low_response_condition |
| 8171 | 天宇 | 綠能環保 | neutral |  | 269.89458889669714 | 55.36585625139528 | 2.6 | 8.24 | -6.34 | -1.66 | 9.24 | 9.24 | False |  | distribution_warning | -0.13 | -0.05 | 0 | 1 | 0.46 | 0.73 | -13.69 |  | fail_low_response_condition |
| 8227 | 巨有科技 | 半導體業 | mainstream_growth |  | 207.0162789387709 | 125.3487613051306 | -5.57 | 3.92 | 73.06 | 42.28 | 87.61 | 87.61 | True | 近60日漲幅>40%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -1.53 | 0.0 | 2 | 0 | -1.49 | 3.1 | -14.86 |  | fail_low_response_condition |
| 8291 | 尚茂 | 電子零組件業 | mainstream_growth |  | 345.27363184079604 | 243.02925989672977 | 9.09 | 272.67 | 0.0 | 0.0 | 887.65 | 887.65 | True | 近20日漲幅>25%；距60日低點反彈>50%；距120日低點反彈>80% | distribution_warning | -4.25 | -0.04 | 0 | 0 | 44.65 | 42.27 | -9.77 |  | fail_low_response_condition |
| 8299 | 群聯 | 半導體業 | mainstream_growth |  | 236.6326033058058 | 208.3172163574361 | 2.79 | 7.74 | 60.44 | 133.03 | 74.58 | 153.69 | True | 近60日漲幅>40%；距60日低點反彈>50%；近120日漲幅>70%；距120日低點反彈>80% | distribution_warning | -5.52 | -6.21 | 0 | 0 | 1.57 | 6.77 | -10.59 |  | fail_low_response_condition |
| 8489 | 三貝德 | 其他 | neutral |  | 57.791556753915486 | 56.6216199659393 | -2.35 | -9.13 | 1.33 | -45.15 | 6.02 | 6.02 | False |  | mild_accumulation | -1.14 | 1.8 | 2 | 3 | -5.23 | -5.56 | -23.54 |  | fail_low_response_condition |
| 8927 | 北基 | 油電燃氣業 | defensive_or_traditional |  | 50.67630705716537 | 35.21911926139916 | 1.63 | -9.22 | -25.35 | -27.94 | 4.47 | 4.47 | False |  | strong_accumulation | 0.45 | 0.35 | 2 | 2 | -2.39 | -4.45 | -26.23 |  | fail_low_response_condition |