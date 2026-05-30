# Five-Trading-Day Surge 5D Average Volume Comparison

- generated_at: 2026-05-30 19:23:04 Asia/Taipei
- not_weekly_candle: True. This compares rolling five-trading-day high-low event volume filters.
- return definition: max high from D0 through D+5 divided by D0 low.
- start_5d_avg_volume_ratio: average volume from D-4 through D0 divided by the previous 20-day average volume before D0.
- prev_5d_avg_volume_ratio: average volume from D-5 through D-1 divided by the previous 20-day average volume before D0.
- both volume filters are available by D0 close or earlier; no future volume is used.
- focus: hit_rate_pct.

## start_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                463654 |            23293 |           5.02 |                      90.39 |                5.05 |
|                  20 |         0.8 |                362580 |            19522 |           5.38 |                      75.75 |                5.05 |
|                  20 |         1   |                291362 |            16685 |           5.73 |                      64.75 |                5.05 |
|                  20 |         1.2 |                108881 |             8601 |           7.9  |                      33.38 |                5.05 |
|                  20 |         1.5 |                 60444 |             5846 |           9.67 |                      22.69 |                5.05 |
|                  20 |         2   |                 26423 |             3234 |          12.24 |                      12.55 |                5.05 |
|                  20 |         3   |                  6607 |             1057 |          16    |                       4.1  |                5.05 |
|                  20 |         5   |                   704 |              128 |          18.18 |                       0.5  |                5.05 |
|                  10 |         0.5 |                463654 |            75650 |          16.32 |                      89.89 |               16.48 |
|                  10 |         0.8 |                362580 |            60508 |          16.69 |                      71.89 |               16.48 |
|                  10 |         1   |                291362 |            49811 |          17.1  |                      59.18 |               16.48 |
|                  10 |         1.2 |                108881 |            27236 |          25.01 |                      32.36 |               16.48 |
|                  10 |         1.5 |                 60444 |            18255 |          30.2  |                      21.69 |               16.48 |
|                  10 |         2   |                 26423 |             9895 |          37.45 |                      11.76 |               16.48 |
|                  10 |         3   |                  6607 |             3195 |          48.36 |                       3.8  |               16.48 |
|                  10 |         5   |                   704 |              400 |          56.82 |                       0.48 |               16.48 |

## prev_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                468899 |            23278 |           4.96 |                      90.33 |                5.05 |
|                  20 |         0.8 |                368686 |            19141 |           5.19 |                      74.28 |                5.05 |
|                  20 |         1   |                292759 |            15943 |           5.45 |                      61.87 |                5.05 |
|                  20 |         1.2 |                105396 |             7636 |           7.25 |                      29.63 |                5.05 |
|                  20 |         1.5 |                 54367 |             4748 |           8.73 |                      18.42 |                5.05 |
|                  20 |         2   |                 20627 |             2190 |          10.62 |                       8.5  |                5.05 |
|                  20 |         3   |                  2508 |              308 |          12.28 |                       1.2  |                5.05 |
|                  20 |         5   |                     0 |                0 |           0    |                       0    |                5.05 |
|                  10 |         0.5 |                468899 |            75934 |          16.19 |                      90.22 |               16.48 |
|                  10 |         0.8 |                368686 |            59727 |          16.2  |                      70.97 |               16.48 |
|                  10 |         1   |                292759 |            47773 |          16.32 |                      56.76 |               16.48 |
|                  10 |         1.2 |                105396 |            24308 |          23.06 |                      28.88 |               16.48 |
|                  10 |         1.5 |                 54367 |            14889 |          27.39 |                      17.69 |               16.48 |
|                  10 |         2   |                 20627 |             6746 |          32.7  |                       8.02 |               16.48 |
|                  10 |         3   |                  2508 |              950 |          37.88 |                       1.13 |               16.48 |
|                  10 |         5   |                     0 |                0 |           0    |                       0    |               16.48 |
