# Five-Trading-Day Surge 5D Average Volume Comparison

- generated_at: 2026-05-28 23:15:59 Asia/Taipei
- not_weekly_candle: True. This compares rolling five-trading-day high-low event volume filters.
- return definition: max high from D0 through D+5 divided by D0 low.
- start_5d_avg_volume_ratio: average volume from D-4 through D0 divided by the previous 20-day average volume before D0.
- prev_5d_avg_volume_ratio: average volume from D-5 through D-1 divided by the previous 20-day average volume before D0.
- both volume filters are available by D0 close or earlier; no future volume is used.
- focus: hit_rate_pct.

## start_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                194560 |            13298 |           6.83 |                      87.24 |                6.94 |
|                  20 |         0.8 |                138559 |            10487 |           7.57 |                      68.8  |                6.94 |
|                  20 |         1   |                 98456 |             8390 |           8.52 |                      55.04 |                6.94 |
|                  20 |         1.2 |                 66767 |             6560 |           9.83 |                      43.04 |                6.94 |
|                  20 |         1.5 |                 37435 |             4459 |          11.91 |                      29.25 |                6.94 |
|                  20 |         2   |                 16339 |             2381 |          14.57 |                      15.62 |                6.94 |
|                  20 |         3   |                  3998 |              706 |          17.66 |                       4.63 |                6.94 |
|                  20 |         5   |                   406 |               74 |          18.23 |                       0.49 |                6.94 |
|                  10 |         0.5 |                194560 |            42586 |          21.89 |                      87.76 |               22.1  |
|                  10 |         0.8 |                138559 |            32432 |          23.41 |                      66.84 |               22.1  |
|                  10 |         1   |                 98456 |            25260 |          25.66 |                      52.06 |               22.1  |
|                  10 |         1.2 |                 66767 |            19215 |          28.78 |                      39.6  |               22.1  |
|                  10 |         1.5 |                 37435 |            12900 |          34.46 |                      26.59 |               22.1  |
|                  10 |         2   |                 16339 |             6878 |          42.1  |                      14.17 |               22.1  |
|                  10 |         3   |                  3998 |             2087 |          52.2  |                       4.3  |               22.1  |
|                  10 |         5   |                   406 |              235 |          57.88 |                       0.48 |               22.1  |

## prev_5d_avg_volume_ratio

|   target_return_pct |   threshold |   selected_stock_days |   hit_stock_days |   hit_rate_pct |   coverage_of_all_hits_pct |   base_hit_rate_pct |
|--------------------:|------------:|----------------------:|-----------------:|---------------:|---------------------------:|--------------------:|
|                  20 |         0.5 |                197156 |            13301 |           6.75 |                      87.26 |                6.94 |
|                  20 |         0.8 |                141332 |            10214 |           7.23 |                      67.01 |                6.94 |
|                  20 |         1   |                 98452 |             7876 |           8    |                      51.67 |                6.94 |
|                  20 |         1.2 |                 64577 |             5930 |           9.18 |                      38.9  |                6.94 |
|                  20 |         1.5 |                 33632 |             3687 |          10.96 |                      24.19 |                6.94 |
|                  20 |         2   |                 12771 |             1634 |          12.79 |                      10.72 |                6.94 |
|                  20 |         3   |                  1506 |              214 |          14.21 |                       1.4  |                6.94 |
|                  20 |         5   |                     0 |                0 |           0    |                       0    |                6.94 |
|                  10 |         0.5 |                197156 |            42763 |          21.69 |                      88.13 |               22.1  |
|                  10 |         0.8 |                141332 |            31933 |          22.59 |                      65.81 |               22.1  |
|                  10 |         1   |                 98452 |            23980 |          24.36 |                      49.42 |               22.1  |
|                  10 |         1.2 |                 64577 |            17397 |          26.94 |                      35.85 |               22.1  |
|                  10 |         1.5 |                 33632 |            10698 |          31.81 |                      22.05 |               22.1  |
|                  10 |         2   |                 12771 |             4746 |          37.16 |                       9.78 |               22.1  |
|                  10 |         3   |                  1506 |              618 |          41.04 |                       1.27 |               22.1  |
|                  10 |         5   |                     0 |                0 |           0    |                       0    |               22.1  |
