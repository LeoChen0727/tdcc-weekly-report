# Weekly Surge Volume Target Comparison

- generated_at: 2026-05-28 12:09:55 Asia/Taipei
- definition: start date is any stock trading day; future return uses max high from D0 through D+5 divided by D0 low.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- purpose: compare the same volume filters under 20% and 10% weekly high-from-low targets.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 219537
- weekly_20pct_hit_stock_days: 15083
- weekly_20pct_base_hit_rate: 6.87%
- weekly_10pct_hit_stock_days: 48099
- weekly_10pct_base_hit_rate: 21.91%

## Target Comparison - start_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                165416 |            11907 |           7.2  |                      78.94 |                6.87 |
|                  20 |         0.8 |                111240 |             9267 |           8.33 |                      61.44 |                6.87 |
|                  20 |         1   |                 83645 |             7759 |           9.28 |                      51.44 |                6.87 |
|                  20 |         1.2 |                 63396 |             6539 |          10.31 |                      43.35 |                6.87 |
|                  20 |         1.5 |                 43741 |             5222 |          11.94 |                      34.62 |                6.87 |
|                  20 |         2   |                 26163 |             3687 |          14.09 |                      24.44 |                6.87 |
|                  20 |         3   |                 12260 |             2095 |          17.09 |                      13.89 |                6.87 |
|                  20 |         5   |                  4707 |              908 |          19.29 |                       6.02 |                6.87 |
|                  10 |         0.5 |                165416 |            37781 |          22.84 |                      78.55 |               21.91 |
|                  10 |         0.8 |                111240 |            28271 |          25.41 |                      58.78 |               21.91 |
|                  10 |         1   |                 83645 |            23221 |          27.76 |                      48.28 |               21.91 |
|                  10 |         1.2 |                 63396 |            19150 |          30.21 |                      39.81 |               21.91 |
|                  10 |         1.5 |                 43741 |            14953 |          34.19 |                      31.09 |               21.91 |
|                  10 |         2   |                 26163 |            10400 |          39.75 |                      21.62 |               21.91 |
|                  10 |         3   |                 12260 |             5914 |          48.24 |                      12.3  |               21.91 |
|                  10 |         5   |                  4707 |             2621 |          55.68 |                       5.45 |               21.91 |

## Target Comparison - previous_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                165243 |            11489 |           6.95 |                      76.17 |                6.87 |
|                  20 |         0.8 |                110828 |             8487 |           7.66 |                      56.27 |                6.87 |
|                  20 |         1   |                 83291 |             6831 |           8.2  |                      45.29 |                6.87 |
|                  20 |         1.2 |                 63141 |             5570 |           8.82 |                      36.93 |                6.87 |
|                  20 |         1.5 |                 43544 |             4264 |           9.79 |                      28.27 |                6.87 |
|                  20 |         2   |                 26059 |             2820 |          10.82 |                      18.7  |                6.87 |
|                  20 |         3   |                 12231 |             1515 |          12.39 |                      10.04 |                6.87 |
|                  20 |         5   |                  4714 |              622 |          13.19 |                       4.12 |                6.87 |
|                  10 |         0.5 |                165243 |            36419 |          22.04 |                      75.72 |               21.91 |
|                  10 |         0.8 |                110828 |            26026 |          23.48 |                      54.11 |               21.91 |
|                  10 |         1   |                 83291 |            20681 |          24.83 |                      43    |               21.91 |
|                  10 |         1.2 |                 63141 |            16569 |          26.24 |                      34.45 |               21.91 |
|                  10 |         1.5 |                 43544 |            12449 |          28.59 |                      25.88 |               21.91 |
|                  10 |         2   |                 26059 |             8261 |          31.7  |                      17.17 |               21.91 |
|                  10 |         3   |                 12231 |             4451 |          36.39 |                       9.25 |               21.91 |
|                  10 |         5   |                  4714 |             1905 |          40.41 |                       3.96 |               21.91 |
