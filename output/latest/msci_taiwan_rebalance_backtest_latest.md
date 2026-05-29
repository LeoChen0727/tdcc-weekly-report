# MSCI Taiwan Rebalance Event Backtest

- generated_at: 2026-05-29 13:39:08 Asia/Taipei
- event_type: msci_index_rebalance
- source: MSCI official Global Standard / Small Cap public list PDFs
- entry rule: first trading day after MSCI effective date, entry at open
- exit rule: D+5 / D+10 / D+15 / D+20 trading-day close; entry day is D+1
- deletion return is not inverted; it is the stock's post-deletion long-side performance.
- this is an event tag / research layer, not a buy or sell signal.

## Data Quality

- parsed_events: 196
- mapped_events: 118
- unmatched_events: 78
- backtested_rows: 118

## Summary By MSCI Segment And Action

| msci_index_segment   | action   |   sample_count |   ok_count |   ret_d5_mature_count |   ret_d5_win_rate |   ret_d5_avg_return |   ret_d10_mature_count |   ret_d10_win_rate |   ret_d10_avg_return |   ret_d20_mature_count |   ret_d20_win_rate |   ret_d20_avg_return |
|:---------------------|:---------|---------------:|-----------:|----------------------:|------------------:|--------------------:|-----------------------:|-------------------:|---------------------:|-----------------------:|-------------------:|---------------------:|
| global_standard      | addition |             11 |          7 |                     7 |             42.86 |               -0.45 |                      7 |              28.57 |                -1.85 |                      7 |              42.86 |                -2.37 |
| global_standard      | deletion |             22 |         11 |                    11 |             45.45 |                1.95 |                     11 |              54.55 |                 0.08 |                     11 |              18.18 |                -4.02 |
| small_cap            | addition |             48 |         20 |                    20 |             45    |                0.51 |                     20 |              50    |                 0.08 |                     20 |              40    |                -0.48 |
| small_cap            | deletion |             37 |         18 |                    18 |             38.89 |                2.55 |                     18 |              33.33 |                 1.45 |                     18 |              27.78 |                -1.34 |

## Recent Backtest Rows

|   effective_date | msci_index_segment   | action   |   stock_id | stock_name   |    entry_date |   entry_open |   ret_d5_return |   ret_d10_return |   ret_d15_return |   ret_d20_return | sample_status         |
|-----------------:|:---------------------|:---------|-----------:|:-------------|--------------:|-------------:|----------------:|-----------------:|-----------------:|-----------------:|:----------------------|
|         20260529 | small_cap            | deletion |       9938 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       9802 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       6873 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       6589 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       6550 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       6223 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       6125 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       5530 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       4147 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       3687 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       2605 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | deletion |       1536 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       8039 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       6835 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       6640 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       6456 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       3673 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2633 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2610 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2474 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2472 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2351 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       2324 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       1504 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       1402 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | small_cap            | addition |       1102 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       2633 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       2610 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       2474 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       2324 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       1504 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       1402 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | deletion |       1102 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260529 | global_standard      | addition |       6223 | nan          | nan           |        nan   |        nan      |         nan      |         nan      |         nan      | pending_no_next_trade |
|         20260227 | small_cap            | deletion |       8114 | 振樺電       |   2.02603e+07 |        175.5 |          2.2792 |           0      |           4.2735 |          -0.2849 | ok                    |
|         20260227 | small_cap            | deletion |       6869 | 雲豹能源     |   2.02603e+07 |        107.5 |          0      |          -3.7209 |          -9.4884 |         -15.3488 | ok                    |
|         20260227 | small_cap            | deletion |       6806 | 森崴能源     |   2.02603e+07 |         43.2 |         -2.3148 |          -7.5231 |          -5.9028 |          -8.4491 | ok                    |
|         20260227 | small_cap            | deletion |       6533 | 晶心科       |   2.02603e+07 |        212.5 |         -5.6471 |          -9.6471 |         -10.1176 |         -16      | ok                    |
|         20260227 | small_cap            | deletion |       6469 | 大樹         |   2.02603e+07 |         86.1 |         -2.439  |          -3.4843 |          -7.2009 |          -4.065  | ok                    |
|         20260227 | small_cap            | deletion |       6456 | GIS-KY       |   2.02603e+07 |         46.1 |         36.0087 |          36.6594 |          37.961  |          27.9826 | ok                    |

