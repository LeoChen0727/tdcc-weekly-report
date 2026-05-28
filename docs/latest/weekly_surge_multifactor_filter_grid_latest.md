# Weekly Surge Multifactor Filter Grid

- generated_at: `2026-05-28 13:50:29 Asia/Taipei`
- entry_basis: D+1 open.
- target: D+1 open to D+5 / D+10 / D+20 max high >= 10%.
- strict parts: market regime is derived from historical index data; TDCC uses latest available weekly holder ratio as of each stock date.
- caveat: rules containing latest theme labels are still exploratory and can contain look-ahead bias until daily theme history accumulates.
- use: parameter discovery only; do not change core model weights from this table.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+5 | 30042 | 13.81% |
| D+10 | 51881 | 23.85% |
| D+20 | 76870 | 35.33% |

## Data Availability

- stock_day_count: `217570`
- tdcc_available_stock_days: `42526`
- tdcc_available_rate: `19.55%`
- market_regime_counts: `strong_bull=143504; mild_bull=36575; range_or_unclear=35590; weak_or_correction=1901`

## Best D+5 Rules

| rule_family            | rule_name                                          | source_type                     |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-----------------------|:---------------------------------------------------|:--------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_technical | mainstream_overheated__vol2__market_bull__bb_ok    | latest_theme_plus_strict_market |                   221 |          31.22 |                                  5.67 |                                    1.21 |                     40.72 | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__rsi50_75 | latest_theme_plus_strict_market |                  1061 |          30.73 |                                  5.61 |                                    0.67 |                     13.29 | provisional_latest_theme_label |
| theme_market_volume    | mainstream_overheated__vol2__market_bull           | latest_theme_plus_strict_market |                  1929 |          29.86 |                                  5.45 |                                    0.79 |                     12.7  | provisional_latest_theme_label |
| theme_market_volume    | mainstream_overheated__vol3__market_bull           | latest_theme_plus_strict_market |                   405 |          29.63 |                                  5.71 |                                    0.85 |                      8.15 | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__kd_good  | latest_theme_plus_strict_market |                   809 |          29.54 |                                  5.32 |                                    0.8  |                     15.2  | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__macd     | latest_theme_plus_strict_market |                  1158 |          28.24 |                                  5.26 |                                    0.86 |                     19    | provisional_latest_theme_label |
| tdcc_volume            | all_stock__vol2__tdcc_all_up                       | strict_tdcc                     |                   580 |          27.07 |                                  4.51 |                                    0.8  |                    100    | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_up                      | strict_tdcc                     |                   733 |          24.42 |                                  4.25 |                                    0.72 |                    100    | ok_initial_sample              |
| theme_market_volume    | mainstream_supported__vol2__market_bull            | latest_theme_plus_strict_market |                  1601 |          21.61 |                                  3.85 |                                    0.61 |                     18.05 | provisional_latest_theme_label |
| market_volume          | all_stock__vol2__market_bull                       | strict_market                   |                 14057 |          21.36 |                                  3.6  |                                    0.63 |                     15.17 | ok_initial_sample              |
| market_volume          | all_stock__vol2__market_strong_bull                | strict_market                   |                 11859 |          21.1  |                                  3.55 |                                    0.7  |                     16.93 | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_streak2                 | strict_tdcc                     |                   270 |          19.63 |                                  3.72 |                                    0.63 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+5 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                    66 |          43.94 |                                  8.5  |                                    0.95 |                       100 | insufficient_sample |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                    56 |          41.07 |                                  8.11 |                                    0.89 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                    96 |          35.42 |                                  6.92 |                                    0.97 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                    89 |          34.83 |                                  6.67 |                                    1.04 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                    89 |          34.83 |                                  6.67 |                                    1.04 |                       100 | insufficient_sample |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                    69 |          34.78 |                                  7.06 |                                    1.11 |                       100 | insufficient_sample |
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                    34 |          32.35 |                                  7.52 |                                    1.1  |                       100 | insufficient_sample |
| non_mainstream_tdcc      | non_mainstream__vol2__tdcc_high_up                     | latest_theme_plus_strict_tdcc        |                    41 |          21.95 |                                  3.31 |                                    0.81 |                       100 | insufficient_sample |

## Best D+10 Rules

| rule_family            | rule_name                                          | source_type                     |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-----------------------|:---------------------------------------------------|:--------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_volume    | mainstream_overheated__vol3__market_bull           | latest_theme_plus_strict_market |                   405 |          49.88 |                                  9.94 |                                    0.85 |                      8.15 | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__bb_ok    | latest_theme_plus_strict_market |                   221 |          48.87 |                                  9.61 |                                    1.21 |                     40.72 | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__rsi50_75 | latest_theme_plus_strict_market |                  1061 |          48.07 |                                  9.41 |                                    0.67 |                     13.29 | provisional_latest_theme_label |
| theme_market_volume    | mainstream_overheated__vol2__market_bull           | latest_theme_plus_strict_market |                  1929 |          46.92 |                                  9.17 |                                    0.79 |                     12.7  | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__kd_good  | latest_theme_plus_strict_market |                   809 |          46.35 |                                  8.75 |                                    0.8  |                     15.2  | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__macd     | latest_theme_plus_strict_market |                  1158 |          45.08 |                                  8.82 |                                    0.86 |                     19    | provisional_latest_theme_label |
| tdcc_volume            | all_stock__vol2__tdcc_all_up                       | strict_tdcc                     |                   580 |          37.93 |                                  5.93 |                                    0.8  |                    100    | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_up                      | strict_tdcc                     |                   733 |          35.88 |                                  5.69 |                                    0.72 |                    100    | ok_initial_sample              |
| theme_market_volume    | mainstream_supported__vol2__market_bull            | latest_theme_plus_strict_market |                  1601 |          34.1  |                                  6.54 |                                    0.61 |                     18.05 | provisional_latest_theme_label |
| market_volume          | all_stock__vol2__market_bull                       | strict_market                   |                 14057 |          33    |                                  5.52 |                                    0.63 |                     15.17 | ok_initial_sample              |
| market_volume          | all_stock__vol2__market_strong_bull                | strict_market                   |                 11859 |          32.89 |                                  5.49 |                                    0.7  |                     16.93 | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_streak2                 | strict_tdcc                     |                   270 |          27.04 |                                  4.54 |                                    0.63 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+10 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                    56 |          69.64 |                                 14.41 |                                    0.89 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                    66 |          68.18 |                                 13.88 |                                    0.95 |                       100 | insufficient_sample |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                    69 |          60.87 |                                 12.74 |                                    1.11 |                       100 | insufficient_sample |
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                    34 |          58.82 |                                 14.36 |                                    1.1  |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                    96 |          56.25 |                                 11.91 |                                    0.97 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                    89 |          55.06 |                                 11.86 |                                    1.04 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                    89 |          55.06 |                                 11.86 |                                    1.04 |                       100 | insufficient_sample |
| non_mainstream_tdcc      | non_mainstream__vol2__tdcc_high_up                     | latest_theme_plus_strict_tdcc        |                    41 |          34.15 |                                  4.01 |                                    0.81 |                       100 | insufficient_sample |

## Best D+20 Rules

| rule_family            | rule_name                                          | source_type                     |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status                  |
|:-----------------------|:---------------------------------------------------|:--------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:-------------------------------|
| theme_market_technical | mainstream_overheated__vol2__market_bull__bb_ok    | latest_theme_plus_strict_market |                   221 |          63.8  |                                 14.71 |                                    1.21 |                     40.72 | provisional_latest_theme_label |
| theme_market_volume    | mainstream_overheated__vol3__market_bull           | latest_theme_plus_strict_market |                   405 |          62.96 |                                 15.6  |                                    0.85 |                      8.15 | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__rsi50_75 | latest_theme_plus_strict_market |                  1061 |          62.49 |                                 14.81 |                                    0.67 |                     13.29 | provisional_latest_theme_label |
| theme_market_volume    | mainstream_overheated__vol2__market_bull           | latest_theme_plus_strict_market |                  1929 |          61.07 |                                 13.88 |                                    0.79 |                     12.7  | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__macd     | latest_theme_plus_strict_market |                  1158 |          60.71 |                                 13.73 |                                    0.86 |                     19    | provisional_latest_theme_label |
| theme_market_technical | mainstream_overheated__vol2__market_bull__kd_good  | latest_theme_plus_strict_market |                   809 |          60.69 |                                 13.24 |                                    0.8  |                     15.2  | provisional_latest_theme_label |
| theme_market_volume    | mainstream_supported__vol2__market_bull            | latest_theme_plus_strict_market |                  1601 |          50.59 |                                 10.18 |                                    0.61 |                     18.05 | provisional_latest_theme_label |
| market_volume          | all_stock__vol2__market_bull                       | strict_market                   |                 14057 |          43.78 |                                  8.04 |                                    0.63 |                     15.17 | ok_initial_sample              |
| market_volume          | all_stock__vol2__market_strong_bull                | strict_market                   |                 11859 |          43.07 |                                  7.88 |                                    0.7  |                     16.93 | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_all_up                       | strict_tdcc                     |                   580 |          41.38 |                                  7.38 |                                    0.8  |                    100    | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_up                      | strict_tdcc                     |                   733 |          40.38 |                                  7.09 |                                    0.72 |                    100    | ok_initial_sample              |
| tdcc_volume            | all_stock__vol2__tdcc_high_streak2                 | strict_tdcc                     |                   270 |          32.96 |                                  5.36 |                                    0.63 |                    100    | ok_initial_sample              |

## Small-Sample High-Hit D+20 Watchlist

- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.

| rule_family              | rule_name                                              | source_type                          |   selected_stock_days |   hit_rate_pct |   median_next_open_to_high_return_pct |   avg_signal_close_to_next_open_gap_pct |   tdcc_available_rate_pct | sample_status       |
|:-------------------------|:-------------------------------------------------------|:-------------------------------------|----------------------:|---------------:|--------------------------------------:|----------------------------------------:|--------------------------:|:--------------------|
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_all_up  | latest_theme_plus_strict_market_tdcc |                    56 |          73.21 |                                 15.2  |                                    0.89 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_all_up               | latest_theme_plus_strict_tdcc        |                    66 |          71.21 |                                 14.89 |                                    0.95 |                       100 | insufficient_sample |
| theme_market_tdcc_volume | mainstream_overheated__vol2__market_bull__tdcc_high_up | latest_theme_plus_strict_market_tdcc |                    69 |          63.77 |                                 14.11 |                                    1.11 |                       100 | insufficient_sample |
| theme_tdcc_momentum      | mainstream_overheated__vol2__ret2w20_50__tdcc_high_up  | latest_theme_plus_strict_tdcc        |                    34 |          61.76 |                                 14.36 |                                    1.1  |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_sum_pos         | latest_theme_plus_strict_tdcc        |                    96 |          60.42 |                                 12.64 |                                    0.97 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_high_up              | latest_theme_plus_strict_tdcc        |                    89 |          59.55 |                                 12.5  |                                    1.04 |                       100 | insufficient_sample |
| theme_tdcc_volume        | mainstream_overheated__vol2__tdcc_streak1              | latest_theme_plus_strict_tdcc        |                    89 |          59.55 |                                 12.5  |                                    1.04 |                       100 | insufficient_sample |
| non_mainstream_tdcc      | non_mainstream__vol2__tdcc_high_up                     | latest_theme_plus_strict_tdcc        |                    41 |          43.9  |                                  5.84 |                                    0.81 |                       100 | insufficient_sample |

