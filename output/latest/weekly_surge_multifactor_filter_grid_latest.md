# Weekly Surge Multifactor Filter Grid

- generated_at: `2026-05-28 19:20:26 Asia/Taipei`
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
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   191 |          37.17 |                                  6.67 |                                    1.03 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   620 |          34.52 |                                  6.49 |                                    1.06 |                     41.45 | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   160 |          34.38 |                                  6.17 |                                    0.98 |                    100    | provisional_latest_theme_label |
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                   100 |          34    |                                  7.28 |                                    0.78 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   277 |          33.94 |                                  6.16 |                                    0.9  |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   251 |          32.27 |                                  5.92 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   251 |          32.27 |                                  5.92 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                  1039 |          31.28 |                                  5.67 |                                    0.81 |                      7.89 | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   207 |          30.43 |                                  5.65 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1968 |          30.34 |                                  5.43 |                                    0.74 |                     20.53 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  2907 |          30.2  |                                  5.56 |                                    0.8  |                     22.29 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  2631 |          29.87 |                                  5.52 |                                    0.61 |                     17.37 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  4676 |          29.77 |                                  5.39 |                                    0.76 |                     15.16 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          27.11 |                                  4.56 |                                    0.79 |                    100    | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          24.32 |                                  4.31 |                                    0.71 |                    100    | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          21.32 |                                  3.6  |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          21.03 |                                  3.55 |                                    0.7  |                     17.94 | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          18.92 |                                  3.94 |                                    0.61 |                    100    | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   423 |          10.87 |                                  2.71 |                                    0.47 |                     26.24 | provisional_latest_theme_label |

## Small-Sample High-Hit D+5 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    69 |          33.33 |                                  6.81 |                                    1.01 |                       100 | insufficient_sample |

## Best D+10 Rules

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                   100 |          58    |                                 13.64 |                                    0.78 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   191 |          54.97 |                                 12.13 |                                    1.03 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   160 |          54.37 |                                 11.98 |                                    0.98 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   620 |          52.26 |                                 10.47 |                                    1.06 |                     41.45 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   277 |          50.18 |                                 10.09 |                                    0.9  |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   207 |          49.76 |                                  9.93 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   251 |          49    |                                  9.29 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   251 |          49    |                                  9.29 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                  1039 |          48.99 |                                  9.63 |                                    0.81 |                      7.89 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  2631 |          47.24 |                                  9.24 |                                    0.61 |                     17.37 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1968 |          46.75 |                                  8.94 |                                    0.74 |                     20.53 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  2907 |          46.37 |                                  9.1  |                                    0.8  |                     22.29 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  4676 |          46.36 |                                  9.01 |                                    0.76 |                     15.16 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          37.99 |                                  6.22 |                                    0.79 |                    100    | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          35.78 |                                  5.8  |                                    0.71 |                    100    | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          32.9  |                                  5.51 |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          32.75 |                                  5.47 |                                    0.7  |                     17.94 | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          26.35 |                                  4.63 |                                    0.61 |                    100    | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   423 |          18.68 |                                  4    |                                    0.47 |                     26.24 | provisional_latest_theme_label |

## Small-Sample High-Hit D+10 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    69 |          59.42 |                                 15.54 |                                    1.01 |                       100 | insufficient_sample |

## Best D+20 Rules

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_technical   | mainstream_overheated__vol2__market_bull__bb_ok        | latest_theme_plus_strict_market      |                   620 |          67.74 |                                 16.75 |                                    1.06 |                     41.45 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol3__market_bull               | latest_theme_plus_strict_market      |                  1039 |          64    |                                 15.83 |                                    0.81 |                      7.89 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__rsi50_75     | latest_theme_plus_strict_market      |                  2631 |          61.88 |                                 14.81 |                                    0.61 |                     17.37 | provisional_latest_theme_label |
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                   100 |          61    |                                 14.18 |                                    0.78 |                    100    | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__macd         | latest_theme_plus_strict_market      |                  2907 |          60.61 |                                 14.45 |                                    0.8  |                     22.29 | provisional_latest_theme_label |
| theme_market_volume      | mainstream_overheated__vol2__market_bull               | latest_theme_plus_strict_market      |                  4676 |          60.46 |                                 13.98 |                                    0.76 |                     15.16 | provisional_latest_theme_label |
| theme_market_technical   | mainstream_overheated__vol2__market_bull__kd_good      | latest_theme_plus_strict_market      |                  1968 |          60.21 |                                 13.26 |                                    0.74 |                     20.53 | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                   191 |          57.59 |                                 12.79 |                                    1.03 |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                   160 |          57.5  |                                 12.54 |                                    0.98 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                   277 |          55.23 |                                 12    |                                    0.9  |                    100    | provisional_latest_theme_label |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                   207 |          55.07 |                                 12    |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                   251 |          54.58 |                                 11.83 |                                    1.01 |                    100    | provisional_latest_theme_label |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                   251 |          54.58 |                                 11.83 |                                    1.01 |                    100    | provisional_latest_theme_label |
| market_volume            | all_stock__vol2__market_bull                           | strict_market                        |                 14203 |          43.67 |                                  8.03 |                                    0.63 |                     16.04 | ok_initial_sample              |
| market_volume            | all_stock__vol2__market_strong_bull                    | strict_market                        |                 12005 |          42.93 |                                  7.88 |                                    0.7  |                     17.94 | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_all_up                           | strict_tdcc                          |                   616 |          41.72 |                                  7.96 |                                    0.79 |                    100    | ok_initial_sample              |
| tdcc_volume              | all_stock__vol2__tdcc_high_up                          | strict_tdcc                          |                   777 |          40.67 |                                  7.41 |                                    0.71 |                    100    | ok_initial_sample              |
| theme_market_volume      | mainstream_supported__vol2__market_bull                | latest_theme_plus_strict_market      |                   423 |          34.99 |                                  6.43 |                                    0.47 |                     26.24 | provisional_latest_theme_label |
| tdcc_volume              | all_stock__vol2__tdcc_high_streak2                     | strict_tdcc                          |                   296 |          31.76 |                                  5.27 |                                    0.61 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+20 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family         | rule_name                                                        | source_type                   |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:--------------------|:-----------------------------------------------------------------|:------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_momentum | mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up | latest_theme_plus_strict_tdcc |                    69 |          63.77 |                                 17.44 |                                    1.01 |                       100 | insufficient_sample |

