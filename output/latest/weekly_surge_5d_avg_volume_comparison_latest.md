# Five-Trading-Day Surge 5D Average Volume Comparison

- generated_at: 2026-05-30 17:39:38 Asia/Taipei
- not_weekly_candle: True. This compares rolling five-trading-day high-low event volume filters.
- return definition: max high from D0 through D+5 divided by D0 low.
- start_5d_avg_volume_ratio: average volume from D-4 through D0 divided by the previous 20-day average volume before D0.
- prev_5d_avg_volume_ratio: average volume from D-5 through D-1 divided by the previous 20-day average volume before D0.
- both volume filters are available by D0 close or earlier; no future volume is used.
- focus: hit_rate_pct.

## start_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                195920 |            13427 |           6.85 |                      87.15 |                6.96 |
|                  20 |         0.8 |                139695 |            10585 |           7.58 |                      68.7  |                6.96 |
|                  20 |         1   |                 99347 |             8472 |           8.53 |                      54.99 |                6.96 |
|                  20 |         1.2 |                 67388 |             6626 |           9.83 |                      43.01 |                6.96 |
|                  20 |         1.5 |                 37769 |             4504 |          11.93 |                      29.23 |                6.96 |
|                  20 |         2   |                 16504 |             2399 |          14.54 |                      15.57 |                6.96 |
|                  20 |         3   |                  4031 |              708 |          17.56 |                       4.6  |                6.96 |
|                  20 |         5   |                   407 |               74 |          18.18 |                       0.48 |                6.96 |
|                  10 |         0.5 |                195920 |            42966 |          21.93 |                      87.56 |               22.15 |
|                  10 |         0.8 |                139695 |            32736 |          23.43 |                      66.72 |               22.15 |
|                  10 |         1   |                 99347 |            25496 |          25.66 |                      51.96 |               22.15 |
|                  10 |         1.2 |                 67388 |            19396 |          28.78 |                      39.53 |               22.15 |
|                  10 |         1.5 |                 37769 |            13018 |          34.47 |                      26.53 |               22.15 |
|                  10 |         2   |                 16504 |             6941 |          42.06 |                      14.15 |               22.15 |
|                  10 |         3   |                  4031 |             2101 |          52.12 |                       4.28 |               22.15 |
|                  10 |         5   |                   407 |              237 |          58.23 |                       0.48 |               22.15 |

## prev_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                198612 |            13442 |           6.77 |                      87.25 |                6.96 |
|                  20 |         0.8 |                142447 |            10327 |           7.25 |                      67.03 |                6.96 |
|                  20 |         1   |                 99258 |             7961 |           8.02 |                      51.67 |                6.96 |
|                  20 |         1.2 |                 65099 |             5991 |           9.2  |                      38.88 |                6.96 |
|                  20 |         1.5 |                 33902 |             3726 |          10.99 |                      24.18 |                6.96 |
|                  20 |         2   |                 12874 |             1647 |          12.79 |                      10.69 |                6.96 |
|                  20 |         3   |                  1516 |              214 |          14.12 |                       1.39 |                6.96 |
|                  20 |         5   |                     0 |                0 |           0    |                       0    |                6.96 |
|                  10 |         0.5 |                198612 |            43173 |          21.74 |                      87.99 |               22.15 |
|                  10 |         0.8 |                142447 |            32242 |          22.63 |                      65.71 |               22.15 |
|                  10 |         1   |                 99258 |            24199 |          24.38 |                      49.32 |               22.15 |
|                  10 |         1.2 |                 65099 |            17556 |          26.97 |                      35.78 |               22.15 |
|                  10 |         1.5 |                 33902 |            10805 |          31.87 |                      22.02 |               22.15 |
|                  10 |         2   |                 12874 |             4790 |          37.21 |                       9.76 |               22.15 |
|                  10 |         3   |                  1516 |              623 |          41.09 |                       1.27 |               22.15 |
|                  10 |         5   |                     0 |                0 |           0    |                       0    |               22.15 |
