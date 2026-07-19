# Five-Trading-Day 20pct High-Low Surge Event Volume Research

- generated_at: 2026-07-19 10:51:01 Asia/Taipei
- not_weekly_candle: True. This scans rolling five-trading-day windows at stock-day level.
- definition: start date is any stock trading day; hit if max high from D0 through D+5 divided by D0 low is >= 20%.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 431379
- hit_stock_day_count: 24354
- base_hit_rate: 5.65%
- hit_unique_stocks: 1379

## Threshold Hit Rate - start_day_volume_ratio

| summary_type   | filter_metric          | filter_rule                           |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|:---------------|:-----------------------|:--------------------------------------|------------:|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|---------------------------:|--------------------:|
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=0.5 |         0.5 |                320130 |            19083 |           5.96 |                     2130 |                1356 |                      78.36 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=0.8 |         0.8 |                211283 |            14872 |           7.04 |                     2128 |                1343 |                      61.07 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1   |         1   |                157312 |            12488 |           7.94 |                     2124 |                1315 |                      51.28 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1.2 |         1.2 |                118607 |            10508 |           8.86 |                     2115 |                1281 |                      43.15 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1.5 |         1.5 |                 81227 |             8410 |          10.35 |                     2098 |                1233 |                      34.53 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=2   |         2   |                 48172 |             6001 |          12.46 |                     2049 |                1168 |                      24.64 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=3   |         3   |                 22616 |             3494 |          15.45 |                     1997 |                1001 |                      14.35 |                5.65 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=5   |         5   |                  8706 |             1560 |          17.92 |                     1820 |                 715 |                       6.41 |                5.65 |

## Threshold Hit Rate - previous_day_volume_ratio

| summary_type   | filter_metric             | filter_rule                          |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|:---------------|:--------------------------|:-------------------------------------|------------:|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|---------------------------:|--------------------:|
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=0.5 |         0.5 |                320222 |            18361 |           5.73 |                     2130 |                1342 |                      75.39 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=0.8 |         0.8 |                211370 |            13555 |           6.41 |                     2129 |                1299 |                      55.66 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1   |         1   |                157379 |            10961 |           6.96 |                     2125 |                1255 |                      45.01 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1.2 |         1.2 |                118660 |             8923 |           7.52 |                     2117 |                1206 |                      36.64 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1.5 |         1.5 |                 81268 |             6826 |           8.4  |                     2099 |                1137 |                      28.03 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=2   |         2   |                 48200 |             4563 |           9.47 |                     2052 |                1001 |                      18.74 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=3   |         3   |                 22642 |             2502 |          11.05 |                     2001 |                 797 |                      10.27 |                5.65 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=5   |         5   |                  8710 |             1055 |          12.11 |                     1819 |                 520 |                       4.33 |                5.65 |

## Bin Hit Rate - start_day_volume_ratio

| summary_type   | filter_metric          | filter_rule                                  | threshold   |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks | coverage_of_all_hits_pct   | base_hit_rate_pct   |
|:---------------|:-----------------------|:---------------------------------------------|:------------|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|:---------------------------|:--------------------|
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in <0.5x    | <0.5x       |                111249 |             5271 |           4.74 |                     2110 |                 974 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 0.5-0.8x | 0.5-0.8x    |                108847 |             4211 |           3.87 |                     2125 |                1054 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 0.8-1.0x | 0.8-1.0x    |                 53971 |             2384 |           4.42 |                     2110 |                 929 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.0-1.2x | 1.0-1.2x    |                 38705 |             1980 |           5.12 |                     2095 |                 845 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.2-1.5x | 1.2-1.5x    |                 37380 |             2098 |           5.61 |                     2083 |                 858 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.5-2.0x | 1.5-2.0x    |                 33055 |             2409 |           7.29 |                     2074 |                 886 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 2.0-3.0x | 2.0-3.0x    |                 25556 |             2507 |           9.81 |                     2034 |                 916 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 3.0-5.0x | 3.0-5.0x    |                 13910 |             1934 |          13.9  |                     1981 |                 818 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in >=5.0x   | >=5.0x      |                  8706 |             1560 |          17.92 |                     1820 |                 715 |                            |                     |

## Bin Hit Rate - previous_day_volume_ratio

| summary_type   | filter_metric             | filter_rule                                 | threshold   |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks | coverage_of_all_hits_pct   | base_hit_rate_pct   |
|:---------------|:--------------------------|:--------------------------------------------|:------------|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|:---------------------------|:--------------------|
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in <0.5x    | <0.5x       |                111157 |             5993 |           5.39 |                     2110 |                1028 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 0.5-0.8x | 0.5-0.8x    |                108852 |             4806 |           4.42 |                     2126 |                1102 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 0.8-1.0x | 0.8-1.0x    |                 53991 |             2594 |           4.8  |                     2112 |                 953 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.0-1.2x | 1.0-1.2x    |                 38719 |             2038 |           5.26 |                     2099 |                 871 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.2-1.5x | 1.2-1.5x    |                 37392 |             2097 |           5.61 |                     2084 |                 860 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.5-2.0x | 1.5-2.0x    |                 33068 |             2263 |           6.84 |                     2075 |                 869 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 2.0-3.0x | 2.0-3.0x    |                 25558 |             2061 |           8.06 |                     2037 |                 803 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 3.0-5.0x | 3.0-5.0x    |                 13932 |             1447 |          10.39 |                     1984 |                 676 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in >=5.0x   | >=5.0x      |                  8710 |             1055 |          12.11 |                     1819 |                 520 |                            |                     |

## Top Hit Events

|     date |   stock_id | stock_name   |    low |   future_5d_high |   future_5d_high_from_start_low_pct |   future_5d_high_day_offset |   start_day_volume_ratio_vs_prev20 |   prev_day_volume_ratio_vs_prev20 |
|---------:|-----------:|:-------------|-------:|-----------------:|------------------------------------:|----------------------------:|-----------------------------------:|----------------------------------:|
| 20260610 |       2380 | 虹光           |   5.6  |            23.85 |                            325.893  |                           5 |                          0.588245  |                         0.555612  |
| 20260611 |       2380 | 虹光           |   5.61 |            23.85 |                            325.134  |                           4 |                          0.942569  |                         0.588245  |
| 20260612 |       2380 | 虹光           |   5.79 |            23.85 |                            311.917  |                           3 |                          4.23614   |                         0.942569  |
| 20250630 |       4414 | 如興           |   3.05 |            12.35 |                            304.918  |                           3 |                          1.07841   |                         0.587511  |
| 20250626 |       4414 | 如興           |   3.07 |            12.35 |                            302.28   |                           5 |                          0.743012  |                         1.15463   |
| 20250701 |       4414 | 如興           |   3.1  |            12.35 |                            298.387  |                           2 |                          2.18742   |                         1.07841   |
| 20250627 |       4414 | 如興           |   3.12 |            12.35 |                            295.833  |                           4 |                          0.587511  |                         0.743012  |
| 20250702 |       4414 | 如興           |   3.16 |            12.35 |                            290.823  |                           1 |                          1.53197   |                         2.18742   |
| 20260616 |       2380 | 虹光           |   6.26 |            23.85 |                            280.99   |                           1 |                          2.47622   |                         2.11089   |
| 20260615 |       2380 | 虹光           |   6.3  |            23.85 |                            278.571  |                           2 |                          2.11089   |                         4.23614   |
| 20251211 |       4530 | 宏易           |  12.05 |            34.4  |                            185.477  |                           5 |                          0.414079  |                         0.675818  |
| 20251217 |       4530 | 宏易           |  12.05 |            34.4  |                            185.477  |                           1 |                          1.71665   |                         0.266121  |
| 20251215 |       4530 | 宏易           |  12.2  |            34.4  |                            181.967  |                           3 |                          0.689655  |                         0.392157  |
| 20251212 |       4530 | 宏易           |  12.2  |            34.4  |                            181.967  |                           4 |                          0.392157  |                         0.414079  |
| 20251002 |       2314 | 台揚           |   9.45 |            26.6  |                            181.481  |                           3 |                          0.941206  |                         0.654744  |
| 20251216 |       4530 | 宏易           |  12.25 |            34.4  |                            180.816  |                           2 |                          0.266121  |                         0.689655  |
| 20251003 |       2314 | 台揚           |   9.5  |            26.6  |                            180      |                           2 |                          0.755292  |                         0.941206  |
| 20251001 |       2314 | 台揚           |  10    |            26.6  |                            166      |                           4 |                          0.654744  |                         0.741729  |
| 20250930 |       2314 | 台揚           |  10    |            26.6  |                            166      |                           5 |                          0.741729  |                         0.55207   |
| 20251007 |       2314 | 台揚           |  10.1  |            26.6  |                            163.366  |                           1 |                          1.07797   |                         0.755292  |
| 20260122 |       4174 | 浩鼎           |  25.05 |            55.2  |                            120.359  |                           3 |                          0.894118  |                         1.21681   |
| 20260121 |       4174 | 浩鼎           |  25.25 |            55.2  |                            118.614  |                           4 |                          1.21681   |                         1.61885   |
| 20260123 |       4174 | 浩鼎           |  25.25 |            55.2  |                            118.614  |                           2 |                          1.2367    |                         0.894118  |
| 20260120 |       4174 | 浩鼎           |  25.8  |            55.2  |                            113.953  |                           5 |                          1.61885   |                         1.67015   |
| 20260126 |       4174 | 浩鼎           |  26.15 |            55.2  |                            111.09   |                           1 |                          2.57912   |                         1.2367    |
| 20250902 |       3321 | 同泰           |   7.21 |            13.8  |                             91.4008 |                           4 |                          0.673566  |                         0.985052  |
| 20250901 |       3321 | 同泰           |   7.28 |            13.8  |                             89.5604 |                           5 |                          0.985052  |                         0.257378  |
| 20250904 |       3321 | 同泰           |   7.33 |            13.8  |                             88.2674 |                           2 |                          0.859817  |                         1.0773    |
| 20250903 |       3321 | 同泰           |   7.35 |            13.8  |                             87.7551 |                           3 |                          1.0773    |                         0.673566  |
| 20260211 |       2489 | 瑞軒           |  23.25 |            43.55 |                             87.3118 |                           5 |                          4.52735   |                         0.937666  |
| 20250905 |       3321 | 同泰           |   7.42 |            13.8  |                             85.9838 |                           1 |                          1.57056   |                         0.859817  |
| 20251016 |       4764 | 雙鍵           |  41.3  |            76.6  |                             85.4722 |                           5 |                          5.46249   |                         1.58338   |
| 20260602 |       8454 | 富邦媒          | 231    |           426.5  |                             84.632  |                           5 |                          4.24677   |                         5.71239   |
| 20251230 |       8093 | 保銳           |  12.55 |            22.95 |                             82.8685 |                           1 |                          3.00406   |                         1.23626   |
| 20260708 |       2434 | 統懋           |  49.8  |            90.8  |                             82.3293 |                           5 |                          1.11883   |                         1.6296    |
| 20251204 |       3593 | 力銘           |   7.6  |            13.85 |                             82.2368 |                           5 |                          1.52979   |                         1.41361   |
| 20260520 |       5321 | 美而快          |  28.6  |            51.7  |                             80.7692 |                           5 |                          3.0128    |                         4.66089   |
| 20260407 |       6451 | 訊芯-KY        | 288    |           520    |                             80.5556 |                           5 |                          2.00249   |                         0.390735  |
| 20260420 |       4529 | 淳紳           |   3.03 |             5.47 |                             80.5281 |                           5 |                          1.8705    |                         1.94125   |
| 20260612 |       2061 | 風青           |  32.15 |            58    |                             80.4044 |                           5 |                          1.17776   |                         1.43501   |
| 20251205 |       3593 | 力銘           |   7.7  |            13.85 |                             79.8701 |                           4 |                          7.1058    |                         1.52979   |
| 20250516 |       1419 | 新紡           |  45.5  |            81.7  |                             79.5604 |                           5 |                          8.65985   |                         0.561216  |
| 20260506 |       3664 | 安瑞-KY        |   5.77 |            10.35 |                             79.3761 |                           5 |                          0.777039  |                         1.43302   |
| 20260608 |       4556 | 旭然           |  41    |            73.4  |                             79.0244 |                           5 |                          3.59198   |                         0.13913   |
| 20260528 |       5701 | 劍湖山          |   3.27 |             5.85 |                             78.8991 |                           5 |                          0.0785083 |                         0.0546448 |
| 20250801 |       6949 | 沛爾生醫-創       | 190    |           339.5  |                             78.6842 |                           5 |                          2.28287   |                         2.78838   |
| 20260427 |       6405 | 悅城           |  34.4  |            61.4  |                             78.4884 |                           5 |                          1.14784   |                         0.414722  |
| 20260630 |       2466 | 冠西電          |  58.3  |           104    |                             78.3877 |                           5 |                          2.95006   |                         1.34076   |
| 20260223 |       3576 | 聯合再生         |  15    |            26.7  |                             78      |                           5 |                          1.26551   |                         1.23288   |
| 20260415 |       6806 | 森崴能源         |  16.75 |            29.8  |                             77.9104 |                           4 |                          5.23556   |                         0.642899  |
