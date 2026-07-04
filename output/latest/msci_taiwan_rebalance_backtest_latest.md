# MSCI Taiwan Rebalance Event Backtest

- generated_at: 2026-07-05 05:08:59 Asia/Taipei
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
| global_standard      | addition |             11 |         10 |                    10 |             40    |                0.5  |                     10 |              50    |                 2.46 |                     10 |              50    |                -1.44 |
| global_standard      | deletion |             22 |         20 |                    20 |             65    |                2.23 |                     20 |              60    |                 0.02 |                     20 |              40    |                -1.62 |
| small_cap            | addition |             48 |         37 |                    37 |             51.35 |                0.14 |                     37 |              45.95 |                -1.74 |                     37 |              43.24 |                -1.7  |
| small_cap            | deletion |             37 |         35 |                    35 |             48.57 |                2.44 |                     35 |              48.57 |                 2.12 |                     35 |              40    |                -0.2  |

## Recent Backtest Rows

|   effective_date | msci_index_segment   | action   |   stock_id | stock_name   |   entry_date |   entry_open |   ret_d5_return |   ret_d10_return |   ret_d15_return |   ret_d20_return | sample_status   |
|-----------------:|:---------------------|:---------|-----------:|:-------------|-------------:|-------------:|----------------:|-----------------:|-----------------:|-----------------:|:----------------|
|         20260529 | small_cap            | deletion |       9938 | 百和           |     20260601 |        43.3  |          5.1963 |           4.7344 |           1.7321 |           2.6559 | ok              |
|         20260529 | small_cap            | deletion |       9802 | 鈺齊-KY        |     20260601 |        74.5  |          6.0403 |           6.3087 |           1.745  |          -1.2081 | ok              |
|         20260529 | small_cap            | deletion |       6873 | 泓德能源         |     20260601 |        89.9  |          3.4483 |          -9.1212 |          -9.01   |          -8.0089 | ok              |
|         20260529 | small_cap            | deletion |       6589 | 台康生技         |     20260601 |        42.35 |          4.7226 |           5.9032 |           9.209  |          13.8135 | ok              |
|         20260529 | small_cap            | deletion |       6550 | 北極星藥業-KY     |     20260601 |        13.3  |          0.7519 |          -0.7519 |          -0.7519 |          -0.3759 | ok              |
|         20260529 | small_cap            | deletion |       6223 | 旺矽           |     20260601 |      6015    |         -4.1563 |           7.8138 |           6.8163 |           0.7481 | ok              |
|         20260529 | small_cap            | deletion |       6125 | 廣運           |     20260601 |        69.4  |         -6.6282 |         -12.8242 |          -9.7983 |         -16.7147 | ok              |
|         20260529 | small_cap            | deletion |       5530 | 龍巖           |     20260601 |        46.55 |         10.8485 |           6.7669 |           5.6928 |           1.0741 | ok              |
|         20260529 | small_cap            | deletion |       4147 | 中裕           |     20260601 |        50.1  |         10.5788 |          14.3713 |          15.1697 |          27.3453 | ok              |
|         20260529 | small_cap            | deletion |       3687 | 歐買尬          |     20260601 |        78    |         -1.5385 |           1.6667 |           0      |          -5      | ok              |
|         20260529 | small_cap            | deletion |       2605 | 新興           |     20260601 |        30.5  |          5.2459 |           3.6066 |           4.7541 |          -1.9672 | ok              |
|         20260529 | small_cap            | deletion |       1536 | 和大           |     20260601 |        53.5  |         -5.6075 |          -8.4112 |          -3.5514 |         -11.028  | ok              |
|         20260529 | small_cap            | addition |       8039 | 台虹           |     20260601 |       161.5  |        -13.0031 |          -7.4303 |          -5.2632 |         -14.8607 | ok              |
|         20260529 | small_cap            | addition |       6835 | 圓裕           |     20260601 |        39.3  |         -1.9084 |          -7.2519 |          -6.3613 |         -10.5598 | ok              |
|         20260529 | small_cap            | addition |       6640 | 均華           |     20260601 |      1370    |        -13.1387 |         -21.1679 |         -19.708  |         -24.4526 | ok              |
|         20260529 | small_cap            | addition |       6456 | GIS-KY       |     20260601 |        78.4  |          5.2296 |          -9.3112 |          -2.9337 |          -9.5663 | ok              |
|         20260529 | small_cap            | addition |       3673 | TPK-KY       |     20260601 |        87.5  |         -1.7143 |          -8.8    |           1.1429 |         -12.5714 | ok              |
|         20260529 | small_cap            | addition |       2633 | 台灣高鐵         |     20260601 |        25.2  |          1.1905 |           0.9921 |           2.9762 |           5.1587 | ok              |
|         20260529 | small_cap            | addition |       2610 | 華航           |     20260601 |        19.2  |          3.9062 |           6.25   |          13.5417 |          20.3125 | ok              |
|         20260529 | small_cap            | addition |       2474 | 可成           |     20260601 |       223.5  |          3.132  |          -8.0537 |          -7.83   |          -9.1723 | ok              |
|         20260529 | small_cap            | addition |       2472 | 立隆電          |     20260601 |       383    |         -5.0914 |          -3.0026 |           2.7415 |           7.7023 | ok              |
|         20260529 | small_cap            | addition |       2351 | 順德           |     20260601 |       211    |         -4.9763 |         -13.2701 |           1.6588 |          -6.3981 | ok              |
|         20260529 | small_cap            | addition |       2324 | 仁寶           |     20260601 |        40.05 |          3.3708 |          -9.2385 |          -6.367  |         -14.6067 | ok              |
|         20260529 | small_cap            | addition |       1504 | 東元           |     20260601 |        76    |          3.1579 |          -6.5789 |          -5      |          -9.2105 | ok              |
|         20260529 | small_cap            | addition |       1402 | 遠東新          |     20260601 |        25.6  |          7.6172 |           5.4688 |          12.5    |          13.4766 | ok              |
|         20260529 | small_cap            | addition |       1102 | 亞泥           |     20260601 |        34    |          1.1765 |           3.5294 |           6.9118 |           4.2647 | ok              |
|         20260529 | global_standard      | deletion |       2633 | 台灣高鐵         |     20260601 |        25.2  |          1.1905 |           0.9921 |           2.9762 |           5.1587 | ok              |
|         20260529 | global_standard      | deletion |       2610 | 華航           |     20260601 |        19.2  |          3.9062 |           6.25   |          13.5417 |          20.3125 | ok              |
|         20260529 | global_standard      | deletion |       2474 | 可成           |     20260601 |       223.5  |          3.132  |          -8.0537 |          -7.83   |          -9.1723 | ok              |
|         20260529 | global_standard      | deletion |       2324 | 仁寶           |     20260601 |        40.05 |          3.3708 |          -9.2385 |          -6.367  |         -14.6067 | ok              |
|         20260529 | global_standard      | deletion |       1504 | 東元           |     20260601 |        76    |          3.1579 |          -6.5789 |          -5      |          -9.2105 | ok              |
|         20260529 | global_standard      | deletion |       1402 | 遠東新          |     20260601 |        25.6  |          7.6172 |           5.4688 |          12.5    |          13.4766 | ok              |
|         20260529 | global_standard      | deletion |       1102 | 亞泥           |     20260601 |        34    |          1.1765 |           3.5294 |           6.9118 |           4.2647 | ok              |
|         20260529 | global_standard      | addition |       6223 | 旺矽           |     20260601 |      6015    |         -4.1563 |           7.8138 |           6.8163 |           0.7481 | ok              |
|         20260227 | small_cap            | deletion |       8114 | 振樺電          |     20260302 |       175.5  |          2.2792 |           0      |           4.2735 |          -0.2849 | ok              |
|         20260227 | small_cap            | deletion |       6869 | 雲豹能源         |     20260302 |       107.5  |          0      |          -3.7209 |          -9.4884 |         -15.3488 | ok              |
|         20260227 | small_cap            | deletion |       6806 | 森崴能源         |     20260302 |        43.2  |         -2.3148 |          -7.5231 |          -5.9028 |          -8.4491 | ok              |
|         20260227 | small_cap            | deletion |       6533 | 晶心科          |     20260302 |       212.5  |         -5.6471 |          -9.6471 |         -10.1176 |         -16      | ok              |
|         20260227 | small_cap            | deletion |       6469 | 大樹           |     20260302 |        86.1  |         -2.439  |          -3.4843 |          -7.2009 |          -4.065  | ok              |
|         20260227 | small_cap            | deletion |       6456 | GIS-KY       |     20260302 |        46.1  |         36.0087 |          36.6594 |          37.961  |          27.9826 | ok              |

