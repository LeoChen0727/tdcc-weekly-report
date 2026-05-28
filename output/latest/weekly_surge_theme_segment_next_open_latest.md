# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-05-29 00:44:02 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 1205 | 0.55% |
| D+2 | 9954 | 4.53% |
| D+3 | 17784 | 8.10% |
| D+4 | 24455 | 11.14% |
| D+5 | 30306 | 13.80% |
| D+6 | 35561 | 16.20% |
| D+7 | 40333 | 18.37% |
| D+8 | 44601 | 20.32% |
| D+9 | 48675 | 22.17% |
| D+10 | 52345 | 23.84% |
| D+20 | 77588 | 35.34% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+2 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+3 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+4 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+6 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+7 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+8 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+9 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 32 | 6.25 | 2.76 | 0.41 | ok |
| D+1 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+2 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+3 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+4 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+6 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |
| D+7 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 34 | 5.88 | 2.85 | 0.83 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 232 | 48.28 | 9.52 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 767 | 47.33 | 9.25 | 0.86 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 2787 | 44.74 | 8.7 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 3541 | 44.0 | 8.51 | 0.78 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 7003 | 43.95 | 8.52 | 0.69 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 2522 | 43.62 | 8.4 | 1.04 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 12513 | 43.57 | 8.41 | 0.67 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 5219 | 43.55 | 8.38 | 0.97 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 7757 | 43.12 | 8.37 | 0.75 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 8407 | 43.06 | 8.28 | 0.88 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 12943 | 42.89 | 8.26 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 18060 | 42.34 | 8.14 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 11872 | 42.23 | 8.1 | 0.83 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 18150 | 42.17 | 8.09 | 0.7 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 15523 | 41.45 | 7.93 | 0.8 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 2857 | 34.23 | 5.96 | 0.69 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1134 | 32.01 | 5.61 | 0.56 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 8814 | 31.4 | 5.15 | 0.58 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 11206 | 31.38 | 5.09 | 0.65 | provisional_latest_label_only |
| D+10 | unlabeled | start_day_volume_ratio | 3.0 | 8478 | 29.41 | 4.57 | 0.75 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 767 | 29.86 | 5.53 | 0.86 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 2522 | 29.14 | 5.53 | 1.04 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 3541 | 28.78 | 5.34 | 0.78 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 5219 | 28.68 | 5.41 | 0.97 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 2787 | 28.45 | 5.47 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 8407 | 27.64 | 5.21 | 0.88 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 7757 | 27.45 | 5.18 | 0.75 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 7003 | 27.27 | 5.12 | 0.69 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 11872 | 26.66 | 5.07 | 0.83 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 12513 | 26.37 | 4.94 | 0.67 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 12943 | 26.14 | 4.96 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 15523 | 25.61 | 4.9 | 0.8 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 232 | 25.43 | 5.51 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 18060 | 25.42 | 4.79 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 18150 | 25.31 | 4.82 | 0.7 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 2857 | 23.84 | 4.25 | 0.69 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1134 | 22.84 | 3.97 | 0.56 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 11206 | 20.47 | 3.46 | 0.65 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 8814 | 20.08 | 3.46 | 0.58 | provisional_latest_label_only |
| D+5 | unlabeled | start_day_volume_ratio | 3.0 | 8478 | 20.0 | 3.17 | 0.75 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 18150 | 1.01 | 0.85 | provisional_latest_label_only |
| D+1 | mainstream_supported | 5885 | 0.44 | 0.29 | provisional_latest_label_only |
| D+1 | non_mainstream | 5099 | 0.43 | 0.33 | provisional_latest_label_only |
| D+1 | unlabeled | 69322 | 0.64 | 0.51 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 18150 | 42.17 | 40.89 | provisional_latest_label_only |
| D+10 | mainstream_supported | 5885 | 21.58 | 20.43 | provisional_latest_label_only |
| D+10 | non_mainstream | 5099 | 15.12 | 14.43 | provisional_latest_label_only |
| D+10 | unlabeled | 69322 | 21.63 | 20.49 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 18150 | 9.1 | 8.07 | provisional_latest_label_only |
| D+2 | mainstream_supported | 5885 | 3.52 | 2.82 | provisional_latest_label_only |
| D+2 | non_mainstream | 5099 | 3.14 | 2.36 | provisional_latest_label_only |
| D+2 | unlabeled | 69322 | 4.69 | 3.94 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 18150 | 59.38 | 58.37 | provisional_latest_label_only |
| D+20 | mainstream_supported | 5885 | 35.21 | 34.6 | provisional_latest_label_only |
| D+20 | non_mainstream | 5099 | 23.16 | 23.33 | provisional_latest_label_only |
| D+20 | unlabeled | 69322 | 31.45 | 30.44 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 18150 | 15.43 | 14.32 | provisional_latest_label_only |
| D+3 | mainstream_supported | 5885 | 6.24 | 5.34 | provisional_latest_label_only |
| D+3 | non_mainstream | 5099 | 5.41 | 4.31 | provisional_latest_label_only |
| D+3 | unlabeled | 69322 | 8.12 | 7.03 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 18150 | 20.82 | 19.62 | provisional_latest_label_only |
| D+4 | mainstream_supported | 5885 | 8.67 | 7.83 | provisional_latest_label_only |
| D+4 | non_mainstream | 5099 | 7.39 | 6.09 | provisional_latest_label_only |
| D+4 | unlabeled | 69322 | 10.81 | 9.63 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 18150 | 25.31 | 24.19 | provisional_latest_label_only |
| D+5 | mainstream_supported | 5885 | 11.05 | 10.12 | provisional_latest_label_only |
| D+5 | non_mainstream | 5099 | 9.1 | 7.74 | provisional_latest_label_only |
| D+5 | unlabeled | 69322 | 13.1 | 11.92 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 18150 | 29.25 | 28.27 | provisional_latest_label_only |
| D+6 | mainstream_supported | 5885 | 13.49 | 12.41 | provisional_latest_label_only |
| D+6 | non_mainstream | 5099 | 10.26 | 9.17 | provisional_latest_label_only |
| D+6 | unlabeled | 69322 | 15.13 | 13.96 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 18150 | 32.85 | 31.9 | provisional_latest_label_only |
| D+7 | mainstream_supported | 5885 | 15.72 | 14.51 | provisional_latest_label_only |
| D+7 | non_mainstream | 5099 | 11.61 | 10.65 | provisional_latest_label_only |
| D+7 | unlabeled | 69322 | 17.01 | 15.82 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 18150 | 36.15 | 35.06 | provisional_latest_label_only |
| D+8 | mainstream_supported | 5885 | 17.64 | 16.44 | provisional_latest_label_only |
| D+8 | non_mainstream | 5099 | 12.83 | 11.95 | provisional_latest_label_only |
| D+8 | unlabeled | 69322 | 18.7 | 17.5 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 18150 | 39.31 | 38.17 | provisional_latest_label_only |
| D+9 | mainstream_supported | 5885 | 19.73 | 18.57 | provisional_latest_label_only |
| D+9 | non_mainstream | 5099 | 14.06 | 13.29 | provisional_latest_label_only |
| D+9 | unlabeled | 69322 | 20.23 | 19.06 | provisional_latest_label_only |

