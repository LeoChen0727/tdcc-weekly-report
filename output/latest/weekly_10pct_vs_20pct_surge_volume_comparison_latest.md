# Five-Trading-Day Surge Volume Target Comparison

- generated_at: 2026-07-19 10:51:03 Asia/Taipei
- not_weekly_candle: True. This compares rolling five-trading-day high-low event targets.
- definition: start date is any stock trading day; future return uses max high from D0 through D+5 divided by D0 low.
- volume baseline: previous 20 completed trading days, excluding the measured day.
- purpose: compare the same volume filters under 20% and 10% weekly high-from-low targets.
- counting: stock-day level; one stock can appear on multiple start dates.

## Overall

- stock_day_count: 431379
- weekly_20pct_hit_stock_days: 24354
- weekly_20pct_base_hit_rate: 5.65%
- weekly_10pct_hit_stock_days: 84589
- weekly_10pct_base_hit_rate: 19.61%

## Target Comparison - start_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                320130 |            19083 |           5.96 |                      78.36 |                5.65 |
|                  20 |         0.8 |                211283 |            14872 |           7.04 |                      61.07 |                5.65 |
|                  20 |         1   |                157312 |            12488 |           7.94 |                      51.28 |                5.65 |
|                  20 |         1.2 |                118607 |            10508 |           8.86 |                      43.15 |                5.65 |
|                  20 |         1.5 |                 81227 |             8410 |          10.35 |                      34.53 |                5.65 |
|                  20 |         2   |                 48172 |             6001 |          12.46 |                      24.64 |                5.65 |
|                  20 |         3   |                 22616 |             3494 |          15.45 |                      14.35 |                5.65 |
|                  20 |         5   |                  8706 |             1560 |          17.92 |                       6.41 |                5.65 |
|                  10 |         0.5 |                320130 |            65921 |          20.59 |                      77.93 |               19.61 |
|                  10 |         0.8 |                211283 |            49186 |          23.28 |                      58.15 |               19.61 |
|                  10 |         1   |                157312 |            40291 |          25.61 |                      47.63 |               19.61 |
|                  10 |         1.2 |                118607 |            33176 |          27.97 |                      39.22 |               19.61 |
|                  10 |         1.5 |                 81227 |            25728 |          31.67 |                      30.42 |               19.61 |
|                  10 |         2   |                 48172 |            17888 |          37.13 |                      21.15 |               19.61 |
|                  10 |         3   |                 22616 |            10291 |          45.5  |                      12.17 |               19.61 |
|                  10 |         5   |                  8706 |             4626 |          53.14 |                       5.47 |               19.61 |

## Target Comparison - previous_day_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                320222 |            18361 |           5.73 |                      75.39 |                5.65 |
|                  20 |         0.8 |                211370 |            13555 |           6.41 |                      55.66 |                5.65 |
|                  20 |         1   |                157379 |            10961 |           6.96 |                      45.01 |                5.65 |
|                  20 |         1.2 |                118660 |             8923 |           7.52 |                      36.64 |                5.65 |
|                  20 |         1.5 |                 81268 |             6826 |           8.4  |                      28.03 |                5.65 |
|                  20 |         2   |                 48200 |             4563 |           9.47 |                      18.74 |                5.65 |
|                  20 |         3   |                 22642 |             2502 |          11.05 |                      10.27 |                5.65 |
|                  20 |         5   |                  8710 |             1055 |          12.11 |                       4.33 |                5.65 |
|                  10 |         0.5 |                320222 |            63400 |          19.8  |                      74.95 |               19.61 |
|                  10 |         0.8 |                211370 |            45044 |          21.31 |                      53.25 |               19.61 |
|                  10 |         1   |                157379 |            35736 |          22.71 |                      42.25 |               19.61 |
|                  10 |         1.2 |                118660 |            28526 |          24.04 |                      33.72 |               19.61 |
|                  10 |         1.5 |                 81268 |            21276 |          26.18 |                      25.15 |               19.61 |
|                  10 |         2   |                 48200 |            14088 |          29.23 |                      16.65 |               19.61 |
|                  10 |         3   |                 22642 |             7632 |          33.71 |                       9.02 |               19.61 |
|                  10 |         5   |                  8710 |             3290 |          37.77 |                       3.89 |               19.61 |
