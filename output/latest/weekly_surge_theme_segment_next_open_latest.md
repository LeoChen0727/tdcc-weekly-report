# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-07-19 10:53:33 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 2128 | 0.49% |
| D+2 | 17133 | 3.97% |
| D+3 | 30382 | 7.04% |
| D+4 | 41765 | 9.68% |
| D+5 | 51962 | 12.05% |
| D+6 | 61283 | 14.21% |
| D+7 | 69731 | 16.16% |
| D+8 | 77491 | 17.96% |
| D+9 | 84837 | 19.67% |
| D+10 | 91575 | 21.23% |
| D+20 | 140074 | 32.47% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 50.0 | 9.92 | 1.12 | ok |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 47.17 | 8.64 | 1.12 | ok |
| D+9 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 46.23 | 8.43 | 1.12 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 243 | 44.86 | 8.88 | 0.98 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 428 | 43.46 | 8.03 | 0.6 | ok |
| D+8 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 43.4 | 7.27 | 1.12 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 983 | 42.01 | 7.87 | 0.79 | ok |
| D+20 | non_mainstream | start_5d_avg_volume_ratio | 3.0 | 43 | 41.86 | 7.64 | 2.4 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 1433 | 40.4 | 7.48 | 0.65 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 447 | 40.04 | 7.38 | 0.6 | ok |
| D+7 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 39.62 | 6.49 | 1.12 | ok |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 428 | 39.25 | 7.0 | 0.6 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 2148 | 39.15 | 7.36 | 0.61 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.0 | 1284 | 38.86 | 6.94 | 0.35 | ok |
| D+9 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 428 | 38.79 | 6.53 | 0.6 | ok |
| D+20 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 2602 | 38.78 | 7.24 | 0.71 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 3.0 | 199 | 38.69 | 6.36 | 0.1 | ok |
| D+6 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 106 | 38.68 | 6.31 | 1.12 | ok |
| D+20 | non_mainstream | prev_5d_avg_volume_ratio | 1.5 | 125 | 38.4 | 7.82 | 2.11 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.2 | 790 | 38.35 | 7.12 | 0.41 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 366 | 41.26 | 7.76 | 0.59 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1041 | 40.83 | 7.85 | 0.8 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 4601 | 40.53 | 7.63 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 3580 | 40.45 | 7.65 | 0.71 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 3297 | 40.16 | 7.67 | 0.86 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 7140 | 39.12 | 7.35 | 0.79 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 9575 | 38.6 | 7.11 | 0.59 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 10552 | 38.25 | 7.11 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 12089 | 37.79 | 6.99 | 0.71 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 18037 | 36.77 | 6.67 | 0.57 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 18583 | 36.66 | 6.68 | 0.61 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 17813 | 36.34 | 6.62 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 23840 | 35.33 | 6.35 | 0.62 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 27739 | 35.1 | 6.33 | 0.57 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 27853 | 34.87 | 6.23 | 0.54 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 6302 | 33.18 | 5.6 | 0.61 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 2446 | 31.28 | 5.36 | 0.54 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 20022 | 28.96 | 4.85 | 0.47 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 25287 | 28.88 | 4.82 | 0.54 | provisional_latest_label_only |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 3.0 | 145 | 28.28 | 4.59 | 1.05 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1041 | 29.01 | 5.51 | 0.8 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 3297 | 28.06 | 4.93 | 0.86 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 7140 | 26.36 | 4.65 | 0.79 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 4601 | 26.32 | 4.83 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 3580 | 25.67 | 4.82 | 0.71 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 366 | 24.59 | 5.5 | 0.59 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 12089 | 24.55 | 4.42 | 0.71 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 10552 | 24.46 | 4.47 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 9575 | 23.86 | 4.43 | 0.59 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 6302 | 23.21 | 3.97 | 0.61 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 17813 | 22.93 | 4.21 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 18583 | 22.64 | 4.15 | 0.61 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 18037 | 22.34 | 4.09 | 0.57 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 23840 | 21.79 | 4.0 | 0.62 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 2446 | 21.3 | 3.75 | 0.54 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 27739 | 21.24 | 3.93 | 0.57 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 27853 | 20.74 | 3.86 | 0.54 | provisional_latest_label_only |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 3.0 | 145 | 19.31 | 3.79 | 1.05 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 25287 | 18.9 | 3.31 | 0.54 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 20022 | 18.67 | 3.34 | 0.47 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 27739 | 0.8 | 0.72 | provisional_latest_label_only |
| D+1 | mainstream_supported | 7216 | 0.26 | 0.2 | provisional_latest_label_only |
| D+1 | non_mainstream | 379 | 0.53 | 0.23 | provisional_latest_label_only |
| D+1 | unlabeled | 149888 | 0.61 | 0.47 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 27739 | 35.1 | 32.85 | provisional_latest_label_only |
| D+10 | mainstream_supported | 7216 | 17.52 | 16.24 | provisional_latest_label_only |
| D+10 | non_mainstream | 379 | 18.21 | 17.75 | provisional_latest_label_only |
| D+10 | unlabeled | 149888 | 20.58 | 19.39 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 27739 | 7.44 | 6.47 | provisional_latest_label_only |
| D+2 | mainstream_supported | 7216 | 2.67 | 2.11 | provisional_latest_label_only |
| D+2 | non_mainstream | 379 | 2.37 | 2.2 | provisional_latest_label_only |
| D+2 | unlabeled | 149888 | 4.39 | 3.61 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 27739 | 51.08 | 48.05 | provisional_latest_label_only |
| D+20 | mainstream_supported | 7216 | 29.53 | 27.95 | provisional_latest_label_only |
| D+20 | non_mainstream | 379 | 26.65 | 27.03 | provisional_latest_label_only |
| D+20 | unlabeled | 149888 | 31.23 | 29.91 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 27739 | 12.73 | 11.37 | provisional_latest_label_only |
| D+3 | mainstream_supported | 7216 | 4.86 | 4.08 | provisional_latest_label_only |
| D+3 | non_mainstream | 379 | 6.07 | 5.1 | provisional_latest_label_only |
| D+3 | unlabeled | 149888 | 7.47 | 6.41 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 27739 | 17.25 | 15.62 | provisional_latest_label_only |
| D+4 | mainstream_supported | 7216 | 6.9 | 6.01 | provisional_latest_label_only |
| D+4 | non_mainstream | 379 | 8.97 | 7.77 | provisional_latest_label_only |
| D+4 | unlabeled | 149888 | 9.99 | 8.79 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 27739 | 21.24 | 19.35 | provisional_latest_label_only |
| D+5 | mainstream_supported | 7216 | 8.8 | 7.89 | provisional_latest_label_only |
| D+5 | non_mainstream | 379 | 10.82 | 9.63 | provisional_latest_label_only |
| D+5 | unlabeled | 149888 | 12.17 | 10.94 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 27739 | 24.46 | 22.63 | provisional_latest_label_only |
| D+6 | mainstream_supported | 7216 | 10.77 | 9.74 | provisional_latest_label_only |
| D+6 | non_mainstream | 379 | 12.4 | 11.48 | provisional_latest_label_only |
| D+6 | unlabeled | 149888 | 14.16 | 12.91 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 27739 | 27.5 | 25.52 | provisional_latest_label_only |
| D+7 | mainstream_supported | 7216 | 12.58 | 11.48 | provisional_latest_label_only |
| D+7 | non_mainstream | 379 | 13.98 | 12.88 | provisional_latest_label_only |
| D+7 | unlabeled | 149888 | 15.98 | 14.71 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 27739 | 30.21 | 28.18 | provisional_latest_label_only |
| D+8 | mainstream_supported | 7216 | 14.22 | 13.12 | provisional_latest_label_only |
| D+8 | non_mainstream | 379 | 15.04 | 14.27 | provisional_latest_label_only |
| D+8 | unlabeled | 149888 | 17.63 | 16.37 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 27739 | 32.81 | 30.61 | provisional_latest_label_only |
| D+9 | mainstream_supported | 7216 | 15.98 | 14.77 | provisional_latest_label_only |
| D+9 | non_mainstream | 379 | 16.62 | 15.78 | provisional_latest_label_only |
| D+9 | unlabeled | 149888 | 19.16 | 17.94 | provisional_latest_label_only |

