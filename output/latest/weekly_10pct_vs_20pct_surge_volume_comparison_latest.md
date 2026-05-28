# Weekly Surge Volume Target Comparison

- generated_at: 2026-05-28 12:28:18 Asia/Taipei
- definition: start date is any stock trading day; future return uses max high from D0 through D+5 divided by D0 low.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- purpose: compare the same volume filters under 20% and 10% weekly high-from-low targets.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 217570
- weekly_20pct_hit_stock_days: 15083
- weekly_20pct_base_hit_rate: 6.93%
- weekly_10pct_hit_stock_days: 47983
- weekly_10pct_base_hit_rate: 22.05%

## Target Comparison - start_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                164107 |            11907 |           7.26 |                      78.94 |                6.93 |
|                  20 |         0.8 |                110212 |             9267 |           8.41 |                      61.44 |                6.93 |
|                  20 |         1   |                 82852 |             7759 |           9.36 |                      51.44 |                6.93 |
|                  20 |         1.2 |                 62800 |             6539 |          10.41 |                      43.35 |                6.93 |
|                  20 |         1.5 |                 43323 |             5222 |          12.05 |                      34.62 |                6.93 |
|                  20 |         2   |                 25919 |             3687 |          14.23 |                      24.44 |                6.93 |
|                  20 |         3   |                 12157 |             2095 |          17.23 |                      13.89 |                6.93 |
|                  20 |         5   |                  4677 |              908 |          19.41 |                       6.02 |                6.93 |
|                  10 |         0.5 |                164107 |            37712 |          22.98 |                      78.59 |               22.05 |
|                  10 |         0.8 |                110212 |            28209 |          25.6  |                      58.79 |               22.05 |
|                  10 |         1   |                 82852 |            23165 |          27.96 |                      48.28 |               22.05 |
|                  10 |         1.2 |                 62800 |            19102 |          30.42 |                      39.81 |               22.05 |
|                  10 |         1.5 |                 43323 |            14909 |          34.41 |                      31.07 |               22.05 |
|                  10 |         2   |                 25919 |            10367 |          40    |                      21.61 |               22.05 |
|                  10 |         3   |                 12157 |             5900 |          48.53 |                      12.3  |               22.05 |
|                  10 |         5   |                  4677 |             2615 |          55.91 |                       5.45 |               22.05 |

## Target Comparison - previous_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                163974 |            11489 |           7.01 |                      76.17 |                6.93 |
|                  20 |         0.8 |                109915 |             8487 |           7.72 |                      56.27 |                6.93 |
|                  20 |         1   |                 82592 |             6831 |           8.27 |                      45.29 |                6.93 |
|                  20 |         1.2 |                 62610 |             5570 |           8.9  |                      36.93 |                6.93 |
|                  20 |         1.5 |                 43159 |             4264 |           9.88 |                      28.27 |                6.93 |
|                  20 |         2   |                 25820 |             2820 |          10.92 |                      18.7  |                6.93 |
|                  20 |         3   |                 12122 |             1515 |          12.5  |                      10.04 |                6.93 |
|                  20 |         5   |                  4678 |              622 |          13.3  |                       4.12 |                6.93 |
|                  10 |         0.5 |                163974 |            36355 |          22.17 |                      75.77 |               22.05 |
|                  10 |         0.8 |                109915 |            25972 |          23.63 |                      54.13 |               22.05 |
|                  10 |         1   |                 82592 |            20636 |          24.99 |                      43.01 |               22.05 |
|                  10 |         1.2 |                 62610 |            16526 |          26.4  |                      34.44 |               22.05 |
|                  10 |         1.5 |                 43159 |            12411 |          28.76 |                      25.87 |               22.05 |
|                  10 |         2   |                 25820 |             8233 |          31.89 |                      17.16 |               22.05 |
|                  10 |         3   |                 12122 |             4438 |          36.61 |                       9.25 |               22.05 |
|                  10 |         5   |                  4678 |             1901 |          40.64 |                       3.96 |               22.05 |
