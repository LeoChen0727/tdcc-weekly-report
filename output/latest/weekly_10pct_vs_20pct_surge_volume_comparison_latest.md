# Five-Trading-Day Surge Volume Target Comparison

- generated_at: 2026-05-28 23:15:55 Asia/Taipei
- not_weekly_candle: True. This compares rolling five-trading-day high-low event targets.
- definition: start date is any stock trading day; future return uses max high from D0 through D+5 divided by D0 low.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- purpose: compare the same volume filters under 20% and 10% weekly high-from-low targets.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 219530
- weekly_20pct_hit_stock_days: 15243
- weekly_20pct_base_hit_rate: 6.94%
- weekly_10pct_hit_stock_days: 48523
- weekly_10pct_base_hit_rate: 22.10%

## Target Comparison - start_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                165411 |            12012 |           7.26 |                      78.8  |                6.94 |
|                  20 |         0.8 |                111237 |             9344 |           8.4  |                      61.3  |                6.94 |
|                  20 |         1   |                 83643 |             7821 |           9.35 |                      51.31 |                6.94 |
|                  20 |         1.2 |                 63394 |             6591 |          10.4  |                      43.24 |                6.94 |
|                  20 |         1.5 |                 43739 |             5263 |          12.03 |                      34.53 |                6.94 |
|                  20 |         2   |                 26162 |             3714 |          14.2  |                      24.37 |                6.94 |
|                  20 |         3   |                 12258 |             2108 |          17.2  |                      13.83 |                6.94 |
|                  20 |         5   |                  4706 |              912 |          19.38 |                       5.98 |                6.94 |
|                  10 |         0.5 |                165411 |            38014 |          22.98 |                      78.34 |               22.1  |
|                  10 |         0.8 |                111237 |            28461 |          25.59 |                      58.65 |               22.1  |
|                  10 |         1   |                 83643 |            23381 |          27.95 |                      48.19 |               22.1  |
|                  10 |         1.2 |                 63394 |            19283 |          30.42 |                      39.74 |               22.1  |
|                  10 |         1.5 |                 43739 |            15050 |          34.41 |                      31.02 |               22.1  |
|                  10 |         2   |                 26162 |            10468 |          40.01 |                      21.57 |               22.1  |
|                  10 |         3   |                 12258 |             5947 |          48.52 |                      12.26 |               22.1  |
|                  10 |         5   |                  4706 |             2633 |          55.95 |                       5.43 |               22.1  |

## Target Comparison - previous_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                165237 |            11588 |           7.01 |                      76.02 |                6.94 |
|                  20 |         0.8 |                110824 |             8562 |           7.73 |                      56.17 |                6.94 |
|                  20 |         1   |                 83287 |             6892 |           8.28 |                      45.21 |                6.94 |
|                  20 |         1.2 |                 63138 |             5614 |           8.89 |                      36.83 |                6.94 |
|                  20 |         1.5 |                 43541 |             4296 |           9.87 |                      28.18 |                6.94 |
|                  20 |         2   |                 26059 |             2843 |          10.91 |                      18.65 |                6.94 |
|                  20 |         3   |                 12230 |             1527 |          12.49 |                      10.02 |                6.94 |
|                  20 |         5   |                  4713 |              627 |          13.3  |                       4.11 |                6.94 |
|                  10 |         0.5 |                165237 |            36657 |          22.18 |                      75.55 |               22.1  |
|                  10 |         0.8 |                110824 |            26198 |          23.64 |                      53.99 |               22.1  |
|                  10 |         1   |                 83287 |            20824 |          25    |                      42.92 |               22.1  |
|                  10 |         1.2 |                 63138 |            16695 |          26.44 |                      34.41 |               22.1  |
|                  10 |         1.5 |                 43541 |            12554 |          28.83 |                      25.87 |               22.1  |
|                  10 |         2   |                 26059 |             8336 |          31.99 |                      17.18 |               22.1  |
|                  10 |         3   |                 12230 |             4487 |          36.69 |                       9.25 |               22.1  |
|                  10 |         5   |                  4713 |             1922 |          40.78 |                       3.96 |               22.1  |
