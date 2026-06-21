# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-06-21 20:47:21 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 1856 | 0.47% |
| D+2 | 15293 | 3.90% |
| D+3 | 27270 | 6.96% |
| D+4 | 37650 | 9.61% |
| D+5 | 46963 | 11.99% |
| D+6 | 55462 | 14.16% |
| D+7 | 63218 | 16.14% |
| D+8 | 70369 | 17.96% |
| D+9 | 77132 | 19.69% |
| D+10 | 83334 | 21.27% |
| D+20 | 128082 | 32.70% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 67 | 40.3 | 7.81 | -0.46 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 163 | 39.88 | 7.3 | -0.17 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 348 | 39.37 | 7.85 | -0.02 | ok |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 163 | 39.26 | 7.08 | -0.17 | ok |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 67 | 38.81 | 6.44 | -0.46 | ok |
| D+9 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 67 | 38.81 | 6.44 | -0.46 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 546 | 38.46 | 7.78 | 0.09 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 720 | 38.06 | 7.4 | 0.4 | ok |
| D+20 | mainstream_overheated | start_day_volume_ratio | 1.5 | 881 | 38.02 | 7.59 | 0.76 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 1144 | 37.94 | 7.36 | 0.48 | ok |
| D+20 | mainstream_overheated | start_day_volume_ratio | 2.0 | 577 | 37.78 | 7.32 | 0.66 | ok |
| D+9 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 163 | 37.42 | 6.89 | -0.17 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 1538 | 37.32 | 7.29 | 0.45 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 1033 | 37.17 | 7.33 | 0.29 | ok |
| D+20 | mainstream_overheated | start_day_volume_ratio | 1.2 | 1163 | 37.06 | 7.31 | 0.7 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 1505 | 36.94 | 7.07 | 0.32 | ok |
| D+7 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 163 | 36.81 | 6.65 | -0.17 | ok |
| D+8 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 163 | 36.81 | 6.67 | -0.17 | ok |
| D+20 | mainstream_overheated | start_day_volume_ratio | 1.0 | 1407 | 36.39 | 7.14 | 0.7 | ok |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 348 | 36.21 | 7.31 | -0.02 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1900 | 40.42 | 7.52 | 0.7 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 8158 | 38.28 | 6.95 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 5793 | 38.15 | 7.05 | 0.81 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 6303 | 37.82 | 6.81 | 0.63 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 650 | 37.38 | 7.14 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 12320 | 36.61 | 6.61 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 16610 | 35.89 | 6.42 | 0.55 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 18489 | 35.49 | 6.37 | 0.6 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 20637 | 34.95 | 6.19 | 0.67 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 32148 | 33.24 | 5.88 | 0.56 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 31153 | 33.16 | 5.83 | 0.51 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 30311 | 33.13 | 5.86 | 0.62 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 40311 | 31.88 | 5.62 | 0.58 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 46987 | 31.42 | 5.52 | 0.51 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 47123 | 31.15 | 5.45 | 0.48 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 4985 | 29.87 | 5.02 | 0.62 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1989 | 27.85 | 4.7 | 0.52 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 19895 | 26.22 | 4.33 | 0.51 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 15708 | 26.07 | 4.31 | 0.45 | provisional_latest_label_only |
| D+10 | unlabeled | start_day_volume_ratio | 3.0 | 14952 | 25.27 | 4.04 | 0.63 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1900 | 28.26 | 4.96 | 0.7 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 5793 | 25.89 | 4.59 | 0.81 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 650 | 24.92 | 4.91 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 8158 | 24.55 | 4.52 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 12320 | 24.5 | 4.28 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 6303 | 23.16 | 4.48 | 0.63 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 20637 | 22.63 | 3.97 | 0.67 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 18489 | 22.55 | 4.11 | 0.6 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 16610 | 22.03 | 4.1 | 0.55 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 4985 | 21.18 | 3.68 | 0.62 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 30311 | 20.83 | 3.75 | 0.62 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 32148 | 20.38 | 3.72 | 0.56 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 31153 | 19.87 | 3.66 | 0.51 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 40311 | 19.63 | 3.55 | 0.58 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 46987 | 18.78 | 3.47 | 0.51 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1989 | 18.7 | 3.36 | 0.52 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 47123 | 18.36 | 3.42 | 0.48 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 19895 | 17.36 | 3.06 | 0.51 | provisional_latest_label_only |
| D+5 | unlabeled | start_day_volume_ratio | 3.0 | 14952 | 17.15 | 2.89 | 0.63 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 15708 | 16.98 | 3.04 | 0.45 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 46987 | 0.73 | 0.61 | provisional_latest_label_only |
| D+1 | non_mainstream | 45 | 0.0 | 0.0 | provisional_latest_label_only |
| D+1 | unlabeled | 123335 | 0.53 | 0.43 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 46987 | 31.42 | 29.87 | provisional_latest_label_only |
| D+10 | non_mainstream | 45 | 11.11 | 6.92 | provisional_latest_label_only |
| D+10 | unlabeled | 123335 | 18.89 | 18.1 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 46987 | 6.6 | 5.66 | provisional_latest_label_only |
| D+2 | non_mainstream | 45 | 0.0 | 0.77 | provisional_latest_label_only |
| D+2 | unlabeled | 123335 | 3.88 | 3.26 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 46987 | 46.7 | 44.6 | provisional_latest_label_only |
| D+20 | non_mainstream | 45 | 11.11 | 14.62 | provisional_latest_label_only |
| D+20 | unlabeled | 123335 | 28.98 | 28.3 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 46987 | 11.39 | 10.1 | provisional_latest_label_only |
| D+3 | non_mainstream | 45 | 2.22 | 1.54 | provisional_latest_label_only |
| D+3 | unlabeled | 123335 | 6.65 | 5.8 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 46987 | 15.29 | 13.87 | provisional_latest_label_only |
| D+4 | non_mainstream | 45 | 4.44 | 2.31 | provisional_latest_label_only |
| D+4 | unlabeled | 123335 | 8.99 | 8.04 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 46987 | 18.78 | 17.24 | provisional_latest_label_only |
| D+5 | non_mainstream | 45 | 6.67 | 3.08 | provisional_latest_label_only |
| D+5 | unlabeled | 123335 | 11.01 | 10.05 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 46987 | 21.74 | 20.22 | provisional_latest_label_only |
| D+6 | non_mainstream | 45 | 8.89 | 3.85 | provisional_latest_label_only |
| D+6 | unlabeled | 123335 | 12.85 | 11.92 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 46987 | 24.42 | 22.88 | provisional_latest_label_only |
| D+7 | non_mainstream | 45 | 11.11 | 4.62 | provisional_latest_label_only |
| D+7 | unlabeled | 123335 | 14.54 | 13.65 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 46987 | 26.94 | 25.39 | provisional_latest_label_only |
| D+8 | non_mainstream | 45 | 11.11 | 5.38 | provisional_latest_label_only |
| D+8 | unlabeled | 123335 | 16.08 | 15.22 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 46987 | 29.29 | 27.7 | provisional_latest_label_only |
| D+9 | non_mainstream | 45 | 11.11 | 6.15 | provisional_latest_label_only |
| D+9 | unlabeled | 123335 | 17.54 | 16.73 | provisional_latest_label_only |

