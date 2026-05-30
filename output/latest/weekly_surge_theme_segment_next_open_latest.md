# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-05-30 17:43:07 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 1207 | 0.54% |
| D+2 | 10059 | 4.54% |
| D+3 | 17974 | 8.12% |
| D+4 | 24705 | 11.15% |
| D+5 | 30614 | 13.82% |
| D+6 | 35925 | 16.22% |
| D+7 | 40744 | 18.40% |
| D+8 | 45056 | 20.34% |
| D+9 | 49178 | 22.20% |
| D+10 | 52884 | 23.88% |
| D+20 | 78421 | 35.41% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+2 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+3 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+4 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+6 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+7 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+8 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+9 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 43 | 18.6 | 2.87 | 0.74 | ok |
| D+10 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+2 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+3 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+4 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+5 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+6 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+7 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+8 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |
| D+9 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 70 | 14.29 | 2.82 | 0.75 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 232 | 46.55 | 9.21 | 0.59 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 761 | 45.6 | 8.85 | 0.82 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 2737 | 44.28 | 8.57 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 3479 | 43.81 | 8.42 | 0.81 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 2456 | 43.04 | 8.3 | 1.02 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 6938 | 42.91 | 8.21 | 0.72 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 5168 | 42.82 | 8.21 | 0.99 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 7692 | 42.41 | 8.2 | 0.78 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 12600 | 42.4 | 8.09 | 0.69 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 8445 | 41.99 | 8.06 | 0.91 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 13029 | 41.78 | 7.98 | 0.75 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 18471 | 41.12 | 7.81 | 0.65 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 12069 | 40.93 | 7.79 | 0.85 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 18587 | 40.85 | 7.72 | 0.71 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 15908 | 40.33 | 7.62 | 0.81 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 3118 | 33.29 | 5.69 | 0.68 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1240 | 31.21 | 5.45 | 0.57 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 9546 | 30.99 | 5.07 | 0.58 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 12221 | 30.89 | 5.01 | 0.64 | provisional_latest_label_only |
| D+10 | unlabeled | start_day_volume_ratio | 3.0 | 9275 | 29.24 | 4.57 | 0.75 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 761 | 29.57 | 5.56 | 0.82 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 2456 | 29.23 | 5.49 | 1.02 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 3479 | 28.66 | 5.37 | 0.81 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 5168 | 28.37 | 5.31 | 0.99 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 2737 | 28.24 | 5.44 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 7692 | 27.28 | 5.15 | 0.78 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 8445 | 26.99 | 5.03 | 0.91 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 6938 | 26.85 | 5.07 | 0.72 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 12600 | 25.92 | 4.83 | 0.69 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 12069 | 25.92 | 4.92 | 0.85 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 13029 | 25.62 | 4.83 | 0.75 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 15908 | 24.86 | 4.74 | 0.81 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 18471 | 24.77 | 4.65 | 0.65 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 18587 | 24.62 | 4.66 | 0.71 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 232 | 23.71 | 5.51 | 0.59 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 3118 | 23.09 | 4.11 | 0.68 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1240 | 22.18 | 3.83 | 0.57 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 12221 | 20.24 | 3.38 | 0.64 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 9546 | 19.97 | 3.39 | 0.58 | provisional_latest_label_only |
| D+5 | unlabeled | start_day_volume_ratio | 3.0 | 9275 | 19.76 | 3.13 | 0.75 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 18587 | 0.97 | 0.79 | provisional_latest_label_only |
| D+1 | mainstream_supported | 6565 | 0.35 | 0.24 | provisional_latest_label_only |
| D+1 | non_mainstream | 241 | 0.0 | 0.0 | provisional_latest_label_only |
| D+1 | unlabeled | 73954 | 0.64 | 0.51 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 18587 | 40.85 | 39.63 | provisional_latest_label_only |
| D+10 | mainstream_supported | 6565 | 18.66 | 18.37 | provisional_latest_label_only |
| D+10 | non_mainstream | 241 | 17.43 | 11.25 | provisional_latest_label_only |
| D+10 | unlabeled | 73954 | 21.71 | 20.56 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 18587 | 8.64 | 7.61 | provisional_latest_label_only |
| D+2 | mainstream_supported | 6565 | 3.03 | 2.51 | provisional_latest_label_only |
| D+2 | non_mainstream | 241 | 1.66 | 1.09 | provisional_latest_label_only |
| D+2 | unlabeled | 73954 | 4.74 | 3.98 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 18587 | 57.83 | 56.6 | provisional_latest_label_only |
| D+20 | mainstream_supported | 6565 | 31.2 | 31.4 | provisional_latest_label_only |
| D+20 | non_mainstream | 241 | 26.97 | 19.24 | provisional_latest_label_only |
| D+20 | unlabeled | 73954 | 31.59 | 30.65 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 18587 | 14.8 | 13.64 | provisional_latest_label_only |
| D+3 | mainstream_supported | 6565 | 5.32 | 4.75 | provisional_latest_label_only |
| D+3 | non_mainstream | 241 | 2.9 | 2.18 | provisional_latest_label_only |
| D+3 | unlabeled | 73954 | 8.18 | 7.08 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 18587 | 20.11 | 18.81 | provisional_latest_label_only |
| D+4 | mainstream_supported | 6565 | 7.4 | 6.97 | provisional_latest_label_only |
| D+4 | non_mainstream | 241 | 4.98 | 4.17 | provisional_latest_label_only |
| D+4 | unlabeled | 73954 | 10.86 | 9.68 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 18587 | 24.62 | 23.3 | provisional_latest_label_only |
| D+5 | mainstream_supported | 6565 | 9.44 | 8.99 | provisional_latest_label_only |
| D+5 | non_mainstream | 241 | 6.64 | 5.44 | provisional_latest_label_only |
| D+5 | unlabeled | 73954 | 13.13 | 11.96 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 18587 | 28.39 | 27.27 | provisional_latest_label_only |
| D+6 | mainstream_supported | 6565 | 11.62 | 11.08 | provisional_latest_label_only |
| D+6 | non_mainstream | 241 | 8.71 | 7.08 | provisional_latest_label_only |
| D+6 | unlabeled | 73954 | 15.16 | 14.01 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 18587 | 31.9 | 30.81 | provisional_latest_label_only |
| D+7 | mainstream_supported | 6565 | 13.62 | 13.03 | provisional_latest_label_only |
| D+7 | non_mainstream | 241 | 11.62 | 8.53 | provisional_latest_label_only |
| D+7 | unlabeled | 73954 | 17.03 | 15.87 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 18587 | 35.13 | 33.92 | provisional_latest_label_only |
| D+8 | mainstream_supported | 6565 | 15.28 | 14.84 | provisional_latest_label_only |
| D+8 | non_mainstream | 241 | 13.69 | 9.44 | provisional_latest_label_only |
| D+8 | unlabeled | 73954 | 18.72 | 17.55 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 18587 | 38.09 | 36.96 | provisional_latest_label_only |
| D+9 | mainstream_supported | 6565 | 17.04 | 16.71 | provisional_latest_label_only |
| D+9 | non_mainstream | 241 | 16.18 | 10.71 | provisional_latest_label_only |
| D+9 | unlabeled | 73954 | 20.29 | 19.13 | provisional_latest_label_only |

