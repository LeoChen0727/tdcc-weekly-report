# Weekly 20pct Surge Volume Research

- generated_at: 2026-05-28 11:38:17 Asia/Taipei
- definition: start date is any stock trading day; hit if max high from D0 through D+5 divided by D0 low is >= 20%.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 219537
- hit_stock_day_count: 15083
- base_hit_rate: 6.87%
- hit_unique_stocks: 1140

## Threshold Hit Rate - start_day_volume_ratio

| summary_type   | filter_metric          | filter_rule                           |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|:---------------|:-----------------------|:--------------------------------------|------------:|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|---------------------------:|--------------------:|
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=0.5 |         0.5 |                165416 |            11907 |           7.2  |                     1966 |                1127 |                      78.94 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=0.8 |         0.8 |                111240 |             9267 |           8.33 |                     1966 |                1101 |                      61.44 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1   |         1   |                 83645 |             7759 |           9.28 |                     1965 |                1071 |                      51.44 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1.2 |         1.2 |                 63396 |             6539 |          10.31 |                     1964 |                1045 |                      43.35 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=1.5 |         1.5 |                 43741 |             5222 |          11.94 |                     1963 |                1009 |                      34.62 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=2   |         2   |                 26163 |             3687 |          14.09 |                     1962 |                 926 |                      24.44 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=3   |         3   |                 12260 |             2095 |          17.09 |                     1895 |                 755 |                      13.89 |                6.87 |
| threshold_ge   | start_day_volume_ratio | start_day_volume_ratio_vs_prev20>=5   |         5   |                  4707 |              908 |          19.29 |                     1485 |                 499 |                       6.02 |                6.87 |

## Threshold Hit Rate - previous_day_volume_ratio

| summary_type   | filter_metric             | filter_rule                          |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|:---------------|:--------------------------|:-------------------------------------|------------:|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|---------------------------:|--------------------:|
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=0.5 |         0.5 |                165243 |            11489 |           6.95 |                     1966 |                1112 |                      76.17 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=0.8 |         0.8 |                110828 |             8487 |           7.66 |                     1965 |                1067 |                      56.27 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1   |         1   |                 83291 |             6831 |           8.2  |                     1965 |                1010 |                      45.29 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1.2 |         1.2 |                 63141 |             5570 |           8.82 |                     1964 |                 957 |                      36.93 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=1.5 |         1.5 |                 43544 |             4264 |           9.79 |                     1963 |                 895 |                      28.27 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=2   |         2   |                 26059 |             2820 |          10.82 |                     1962 |                 759 |                      18.7  |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=3   |         3   |                 12231 |             1515 |          12.39 |                     1894 |                 575 |                      10.04 |                6.87 |
| threshold_ge   | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20>=5   |         5   |                  4714 |              622 |          13.19 |                     1488 |                 340 |                       4.12 |                6.87 |

## Bin Hit Rate - start_day_volume_ratio

| summary_type   | filter_metric          | filter_rule                                  | threshold   |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks | coverage_of_all_hits_pct   | base_hit_rate_pct   |
|:---------------|:-----------------------|:---------------------------------------------|:------------|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|:---------------------------|:--------------------|
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in <0.5x    | <0.5x       |                 54121 |             3176 |           5.87 |                     1964 |                 715 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 0.5-0.8x | 0.5-0.8x    |                 54176 |             2640 |           4.87 |                     1966 |                 829 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 0.8-1.0x | 0.8-1.0x    |                 27595 |             1508 |           5.46 |                     1961 |                 709 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.0-1.2x | 1.0-1.2x    |                 20249 |             1220 |           6.02 |                     1961 |                 611 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.2-1.5x | 1.2-1.5x    |                 19655 |             1317 |           6.7  |                     1959 |                 620 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 1.5-2.0x | 1.5-2.0x    |                 17578 |             1535 |           8.73 |                     1958 |                 681 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 2.0-3.0x | 2.0-3.0x    |                 13903 |             1592 |          11.45 |                     1955 |                 693 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in 3.0-5.0x | 3.0-5.0x    |                  7553 |             1187 |          15.72 |                     1852 |                 593 |                            |                     |
| bin            | start_day_volume_ratio | start_day_volume_ratio_vs_prev20 in >=5.0x   | >=5.0x      |                  4707 |              908 |          19.29 |                     1485 |                 499 |                            |                     |

## Bin Hit Rate - previous_day_volume_ratio

| summary_type   | filter_metric             | filter_rule                                 | threshold   |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   selected_unique_stocks |   hit_unique_stocks | coverage_of_all_hits_pct   | base_hit_rate_pct   |
|:---------------|:--------------------------|:--------------------------------------------|:------------|----------------------:|-----------------:|---------------:|-------------------------:|--------------------:|:---------------------------|:--------------------|
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in <0.5x    | <0.5x       |                 54294 |             3594 |           6.62 |                     1964 |                 744 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 0.5-0.8x | 0.5-0.8x    |                 54415 |             3002 |           5.52 |                     1966 |                 880 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 0.8-1.0x | 0.8-1.0x    |                 27537 |             1656 |           6.01 |                     1960 |                 744 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.0-1.2x | 1.0-1.2x    |                 20150 |             1261 |           6.26 |                     1961 |                 643 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.2-1.5x | 1.2-1.5x    |                 19597 |             1306 |           6.66 |                     1959 |                 635 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 1.5-2.0x | 1.5-2.0x    |                 17485 |             1444 |           8.26 |                     1958 |                 662 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 2.0-3.0x | 2.0-3.0x    |                 13828 |             1305 |           9.44 |                     1956 |                 594 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in 3.0-5.0x | 3.0-5.0x    |                  7517 |              893 |          11.88 |                     1850 |                 480 |                            |                     |
| bin            | previous_day_volume_ratio | prev_day_volume_ratio_vs_prev20 in >=5.0x   | >=5.0x      |                  4714 |              622 |          13.19 |                     1488 |                 340 |                            |                     |

## Top Hit Events

|     date |   stock_id | stock_name   |    low |   future_5d_high |   future_5d_high_from_start_low_pct |   future_5d_high_day_offset |   start_day_volume_ratio_vs_prev20 |   prev_day_volume_ratio_vs_prev20 |
|---------:|-----------:|:-------------|-------:|-----------------:|------------------------------------:|----------------------------:|-----------------------------------:|----------------------------------:|
| 20251211 |       4530 | 宏易         |  12.05 |            34.4  |                            185.477  |                           5 |                           0.414079 |                          0.675818 |
| 20251217 |       4530 | 宏易         |  12.05 |            34.4  |                            185.477  |                           1 |                           1.71665  |                          0.266121 |
| 20251215 |       4530 | 宏易         |  12.2  |            34.4  |                            181.967  |                           3 |                           0.689655 |                          0.392157 |
| 20251212 |       4530 | 宏易         |  12.2  |            34.4  |                            181.967  |                           4 |                           0.392157 |                          0.414079 |
| 20251216 |       4530 | 宏易         |  12.25 |            34.4  |                            180.816  |                           2 |                           0.266121 |                          0.689655 |
| 20260122 |       4174 | 浩鼎         |  25.05 |            55.2  |                            120.359  |                           3 |                           0.894118 |                          1.21681  |
| 20260121 |       4174 | 浩鼎         |  25.25 |            55.2  |                            118.614  |                           4 |                           1.21681  |                          1.61885  |
| 20260123 |       4174 | 浩鼎         |  25.25 |            55.2  |                            118.614  |                           2 |                           1.2367   |                          0.894118 |
| 20260120 |       4174 | 浩鼎         |  25.8  |            55.2  |                            113.953  |                           5 |                           1.61885  |                          1.67015  |
| 20260126 |       4174 | 浩鼎         |  26.15 |            55.2  |                            111.09   |                           1 |                           2.57912  |                          1.2367   |
| 20260211 |       2489 | 瑞軒         |  23.25 |            43.55 |                             87.3118 |                           5 |                           4.52735  |                          0.937666 |
| 20251230 |       8093 | 保銳         |  12.55 |            22.95 |                             82.8685 |                           1 |                           3.00406  |                          1.23626  |
| 20251204 |       3593 | 力銘         |   7.6  |            13.85 |                             82.2368 |                           5 |                           1.52979  |                          1.41361  |
| 20260520 |       5321 | 美而快       |  28.6  |            51.7  |                             80.7692 |                           5 |                           3.0128   |                          4.66089  |
| 20260407 |       6451 | 訊芯-KY      | 288    |           520    |                             80.5556 |                           5 |                           2.00249  |                          0.390735 |
| 20260420 |       4529 | 淳紳         |   3.03 |             5.47 |                             80.5281 |                           5 |                           1.8705   |                          1.94125  |
| 20251205 |       3593 | 力銘         |   7.7  |            13.85 |                             79.8701 |                           4 |                           7.1058   |                          1.52979  |
| 20260506 |       3664 | 安瑞-KY      |   5.77 |            10.35 |                             79.3761 |                           5 |                           0.777039 |                          1.43302  |
| 20260427 |       6405 | 悅城         |  34.4  |            61.4  |                             78.4884 |                           5 |                           1.14784  |                          0.414722 |
| 20260223 |       3576 | 聯合再生     |  15    |            26.7  |                             78      |                           5 |                           1.26551  |                          1.23288  |
| 20260415 |       6806 | 森崴能源     |  16.75 |            29.8  |                             77.9104 |                           4 |                           5.23556  |                          0.642899 |
| 20260421 |       4529 | 淳紳         |   3.38 |             6.01 |                             77.8107 |                           5 |                           5.7631   |                          1.8705   |
| 20251208 |       3593 | 力銘         |   7.8  |            13.85 |                             77.5641 |                           3 |                           2.75129  |                          7.1058   |
| 20260428 |       3016 | 嘉晶         |  66.8  |           118.5  |                             77.3952 |                           5 |                           1.31625  |                          1.45412  |
| 20260211 |       3576 | 聯合再生     |  13.75 |            24.3  |                             76.7273 |                           5 |                           1.23288  |                          1.40644  |
| 20260313 |       6226 | 光鼎         |   8.9  |            15.7  |                             76.4045 |                           5 |                           5.60481  |                          1.75247  |
| 20260424 |       8291 | 尚茂         |  13.75 |            24.25 |                             76.3636 |                           5 |                           2.05714  |                          0.337079 |
| 20260518 |       5321 | 美而快       |  24.25 |            42.75 |                             76.2887 |                           5 |                           1.49338  |                          1.22619  |
| 20260430 |       8291 | 尚茂         |  20.1  |            35.4  |                             76.1194 |                           5 |                           9.01639  |                          0.242915 |
| 20260417 |       6735 | 美達科技     |  69    |           121.5  |                             76.087  |                           5 |                           2.41806  |                          1.34162  |
| 20260506 |       6173 | 信昌電       |  90.3  |           159    |                             76.0797 |                           5 |                           3.42428  |                          0.431179 |
| 20260428 |       1597 | 直得         | 108    |           190    |                             75.9259 |                           5 |                           0.826396 |                          0.904981 |
| 20260309 |       4973 | 廣穎         |  42.05 |            73.9  |                             75.7432 |                           5 |                           2.5917   |                          0.239351 |
| 20260223 |       2338 | 光罩         |  33.8  |            59.4  |                             75.7396 |                           5 |                           1.54689  |                          0.503692 |
| 20260317 |       4905 | 台聯電       |  61.2  |           107.5  |                             75.6536 |                           5 |                          11.1558   |                          0.808081 |
| 20260505 |       3664 | 安瑞-KY      |   5.38 |             9.44 |                             75.4647 |                           5 |                           1.43302  |                          0.778249 |
| 20260423 |       6658 | 聯策         |  88    |           154    |                             75      |                           5 |                           4.51795  |                          1.32986  |
| 20260424 |       4951 | 精拓科       |  74.6  |           130.5  |                             74.933  |                           5 |                          10.6381   |                          2.81931  |
| 20260304 |       5386 | 青雲         | 198    |           345.5  |                             74.4949 |                           5 |                           0.250013 |                          0.325232 |
| 20260422 |       6658 | 聯策         |  84    |           146.5  |                             74.4048 |                           5 |                           1.32986  |                          1.10972  |
| 20260313 |       6907 | 雅特力-KY    | 100.5  |           175    |                             74.1294 |                           5 |                           0.518711 |                          0.466139 |
| 20260506 |       8291 | 尚茂         |  27    |            47    |                             74.0741 |                           5 |                           5.22034  |                          7.49425  |
| 20260504 |       3026 | 禾伸堂       | 202    |           351.5  |                             74.0099 |                           5 |                           1.90385  |                          2.10283  |
| 20260312 |       4973 | 廣穎         |  56.5  |            98.2  |                             73.8053 |                           5 |                           8.33941  |                          1.23962  |
| 20260417 |       6861 | 睿生光電     | 149.5  |           259    |                             73.2441 |                           5 |                           4.97738  |                          1.63143  |
| 20260416 |       6829 | 千附精密     | 166    |           287.5  |                             73.1928 |                           5 |                           3.93282  |                          4.30284  |
| 20260519 |       5321 | 美而快       |  27.15 |            47    |                             73.1123 |                           5 |                           4.66089  |                          1.49338  |
| 20260429 |       3016 | 嘉晶         |  69.9  |           121    |                             73.1044 |                           5 |                           5.07603  |                          1.31625  |
| 20260518 |       3090 | 日電貿       | 137    |           236.5  |                             72.6277 |                           5 |                           3.38605  |                          1.42632  |
| 20251224 |       6265 | 方土昶       |  20.45 |            35.3  |                             72.6161 |                           5 |                           1.25744  |                          0.682608 |
