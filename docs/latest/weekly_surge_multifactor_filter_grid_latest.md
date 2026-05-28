# Weekly Surge Multifactor Filter Grid

- generated_at: `2026-05-28 20:08:13 Asia/Taipei`
- entry_basis: D+1 open.
- target: D+1 open to D+5 / D+10 / D+20 max high >= 10%.
- strict parts: market regime is derived from historical index data; TDCC uses latest available weekly holder ratio as of each stock date.
- caveat: rules containing latest theme labels are still exploratory and can contain look-ahead bias until daily theme history accumulates.
- use: parameter discovery only; do not change core model weights from this table.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+5 | 30306 | 13.80% |
| D+10 | 52345 | 23.84% |
| D+20 | 77588 | 35.34% |

## Data Availability

- stock_day_count: `219530`
- tdcc_available_stock_days: `44478`
- tdcc_available_rate: `20.26%`
- market_regime_counts: `strong_bull=145464; mild_bull=36575; range_or_unclear=35590; weak_or_correction=1901`

## Best D+5 Rules

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   413 |          33.66 |                                  6.64 |                                    1.06 |                     45.04 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   134 |          33.58 |                                  5.97 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   117 |          30.77 |                                  5.64 |                                    0.97 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1318 |          29.06 |                                  5.29 |                                    0.76 |                     20.64 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  1776 |          28.89 |                                  5.46 |                                    0.63 |                     17.62 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   196 |          28.57 |                                  5.35 |                                    0.94 |                    100    | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                   642 |          28.04 |                                  5.12 |                                    0.78 |                      8.41 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  3045 |          27.98 |                                  5.18 |                                    0.73 |                     15.89 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   178 |          27.53 |                                  5.27 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   178 |          27.53 |                                  5.27 |                                    1.06 |                    100    | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          27.11 |                                  4.56 |                                    0.79 |                    100    | ok_initial_sample              |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  1884 |          27.07 |                                  5.26 |                                    0.77 |                     23.51 | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   150 |          26    |                                  5.27 |                                    1.03 |                    100    | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          24.32 |                                  4.31 |                                    0.71 |                    100    | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          21.32 |                                  3.6  |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          21.03 |                                  3.55 |                                    0.7  |                     17.94 | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          18.92 |                                  3.94 |                                    0.61 |                    100    | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   629 |          15.9  |                                  2.96 |                                    0.6  |                     22.42 | provisional_latest_theme_label |

## Small-Sample High-Hit D+5 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up            | latest_theme_plus_strict_tdcc |                    66 |          25.76 |                                  6.19 |                                    0.95 |                       100 | insufficient_sample |
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    43 |          25.58 |                                  6.18 |                                    1    |                       100 | insufficient_sample |
| non_mainstream_tdcc | non_mainstream__vol2__tdcc_high_up                               | latest_theme_plus_strict_tdcc |                    85 |          14.12 |                                  2.88 |                                    0.76 |                       100 | insufficient_sample |

## Best D+10 Rules

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   134 |          52.24 |                                 11.36 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   117 |          51.28 |                                 11.12 |                                    0.97 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   413 |          50.12 |                                 10.03 |                                    1.06 |                     45.04 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                   642 |          45.33 |                                  8.73 |                                    0.78 |                      8.41 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  1776 |          44.31 |                                  8.5  |                                    0.63 |                     17.62 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   196 |          43.88 |                                  8.23 |                                    0.94 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1318 |          43.7  |                                  8.22 |                                    0.76 |                     20.64 | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   150 |          43.33 |                                  8.23 |                                    1.03 |                    100    | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  3045 |          42.96 |                                  8.2  |                                    0.73 |                     15.89 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   178 |          42.7  |                                  8.03 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   178 |          42.7  |                                  8.03 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  1884 |          41.51 |                                  8    |                                    0.77 |                     23.51 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          37.99 |                                  6.22 |                                    0.79 |                    100    | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          35.78 |                                  5.8  |                                    0.71 |                    100    | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          32.9  |                                  5.51 |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          32.75 |                                  5.47 |                                    0.7  |                     17.94 | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   629 |          26.71 |                                  4.62 |                                    0.6  |                     22.42 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          26.35 |                                  4.63 |                                    0.61 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+10 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    43 |          51.16 |                                 11.12 |                                    1    |                       100 | insufficient_sample |
| theme_tdcc_momentum | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up            | latest_theme_plus_strict_tdcc |                    66 |          50    |                                 10.21 |                                    0.95 |                       100 | insufficient_sample |
| non_mainstream_tdcc | non_mainstream__vol2__tdcc_high_up                               | latest_theme_plus_strict_tdcc |                    85 |          22.35 |                                  4.31 |                                    0.76 |                       100 | insufficient_sample |

## Best D+20 Rules

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   413 |          67.55 |                                 14.92 |                                    1.06 |                     45.04 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  1776 |          59.35 |                                 13.3  |                                    0.63 |                     17.62 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                   642 |          59.03 |                                 13.24 |                                    0.78 |                      8.41 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  3045 |          57.57 |                                 12.55 |                                    0.73 |                     15.89 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1318 |          57.44 |                                 12.08 |                                    0.76 |                     20.64 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  1884 |          56.63 |                                 12.16 |                                    0.77 |                     23.51 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   134 |          53.73 |                                 12.06 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   117 |          52.99 |                                 11.96 |                                    0.97 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   196 |          48.98 |                                  9.83 |                                    0.94 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   150 |          48.67 |                                  9.43 |                                    1.03 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   178 |          48.31 |                                  9.21 |                                    1.06 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   178 |          48.31 |                                  9.21 |                                    1.06 |                    100    | provisional_latest_theme_label |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          43.67 |                                  8.03 |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          42.93 |                                  7.88 |                                    0.7  |                     17.94 | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          41.72 |                                  7.96 |                                    0.79 |                    100    | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   629 |          41.34 |                                  7.6  |                                    0.6  |                     22.42 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          40.67 |                                  7.41 |                                    0.71 |                    100    | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          31.76 |                                  5.27 |                                    0.61 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+20 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    43 |          58.14 |                                 12.44 |                                    1    |                       100 | insufficient_sample |
| theme_tdcc_momentum | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up            | latest_theme_plus_strict_tdcc |                    66 |          54.55 |                                 11.69 |                                    0.95 |                       100 | insufficient_sample |
| non_mainstream_tdcc | non_mainstream__vol2__tdcc_high_up                               | latest_theme_plus_strict_tdcc |                    85 |          30.59 |                                  4.55 |                                    0.76 |                       100 | insufficient_sample |

