# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-06-30 22:24:15 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 1940 | 0.48% |
| D+2 | 16008 | 3.94% |
| D+3 | 28421 | 7.00% |
| D+4 | 39153 | 9.64% |
| D+5 | 48787 | 12.01% |
| D+6 | 57566 | 14.17% |
| D+7 | 65586 | 16.15% |
| D+8 | 72950 | 17.96% |
| D+9 | 79935 | 19.68% |
| D+10 | 86339 | 21.26% |
| D+20 | 132519 | 32.63% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 45.0 | 8.95 | 1.27 | ok |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 41.67 | 7.94 | 1.27 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 3.0 | 144 | 40.97 | 7.39 | 0.08 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 2.0 | 299 | 40.8 | 7.88 | 1.05 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 338 | 40.53 | 7.43 | 0.75 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.0 | 1011 | 39.96 | 7.27 | 0.44 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.0 | 899 | 39.71 | 7.16 | 0.51 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.2 | 712 | 39.61 | 6.96 | 0.64 | ok |
| D+9 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 39.44 | 7.5 | 1.27 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.2 | 717 | 39.33 | 7.16 | 0.52 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.5 | 510 | 39.02 | 6.75 | 0.74 | ok |
| D+20 | non_mainstream | start_5d_avg_volume_ratio | 3.0 | 36 | 38.89 | 7.36 | 2.5 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.5 | 412 | 38.59 | 7.1 | 0.61 | ok |
| D+8 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 38.33 | 6.86 | 1.27 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.2 | 621 | 38.0 | 6.83 | 0.47 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.0 | 968 | 37.81 | 6.96 | 0.42 | ok |
| D+7 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 37.78 | 6.67 | 1.27 | ok |
| D+10 | mainstream_supported | start_day_volume_ratio | 3.0 | 144 | 36.81 | 6.73 | 0.08 | ok |
| D+6 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 180 | 36.67 | 6.58 | 1.27 | ok |
| D+10 | mainstream_supported | start_day_volume_ratio | 2.0 | 299 | 35.79 | 6.89 | 1.05 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1421 | 41.94 | 7.92 | 0.68 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 5280 | 39.49 | 7.36 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 6821 | 39.22 | 7.3 | 0.7 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 458 | 38.86 | 7.63 | 0.63 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 4834 | 38.29 | 7.12 | 0.87 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 10600 | 37.08 | 6.76 | 0.74 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 14251 | 36.24 | 6.6 | 0.55 | provisional_latest_label_only |
| D+10 | non_mainstream | start_day_volume_ratio | 3.0 | 137 | 35.77 | 5.35 | 1.23 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 15819 | 35.72 | 6.53 | 0.62 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 18042 | 35.53 | 6.37 | 0.67 | provisional_latest_label_only |
| D+10 | non_mainstream | prev_5d_avg_volume_ratio | 2.0 | 154 | 34.42 | 6.21 | 0.65 | provisional_latest_label_only |
| D+10 | non_mainstream | start_day_volume_ratio | 2.0 | 255 | 34.12 | 5.43 | 0.95 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 27301 | 34.03 | 6.12 | 0.52 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 28097 | 34.02 | 6.14 | 0.56 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 26682 | 33.93 | 6.09 | 0.61 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 35698 | 32.93 | 5.9 | 0.57 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 41632 | 32.72 | 5.87 | 0.52 | provisional_latest_label_only |
| D+10 | non_mainstream | start_5d_avg_volume_ratio | 2.0 | 190 | 32.63 | 6.15 | 0.72 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 41802 | 32.47 | 5.8 | 0.49 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 5725 | 31.23 | 5.27 | 0.62 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1421 | 29.2 | 5.03 | 0.68 | provisional_latest_label_only |
| D+5 | non_mainstream | start_day_volume_ratio | 3.0 | 137 | 28.47 | 4.65 | 1.23 | provisional_latest_label_only |
| D+5 | non_mainstream | start_5d_avg_volume_ratio | 2.0 | 190 | 26.84 | 4.81 | 0.72 | provisional_latest_label_only |
| D+5 | non_mainstream | prev_5d_avg_volume_ratio | 2.0 | 154 | 26.62 | 4.72 | 0.65 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 4834 | 26.33 | 4.69 | 0.87 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 6821 | 25.86 | 4.68 | 0.7 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 458 | 25.76 | 4.87 | 0.63 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 5280 | 25.44 | 4.75 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 10600 | 24.78 | 4.41 | 0.74 | provisional_latest_label_only |
| D+5 | non_mainstream | start_day_volume_ratio | 2.0 | 255 | 23.92 | 3.44 | 0.95 | provisional_latest_label_only |
| D+5 | non_mainstream | start_5d_avg_volume_ratio | 1.5 | 380 | 23.16 | 3.59 | 0.85 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 15819 | 23.0 | 4.24 | 0.62 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 18042 | 22.96 | 4.11 | 0.67 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 14251 | 22.57 | 4.23 | 0.55 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 5725 | 22.13 | 3.84 | 0.62 | provisional_latest_label_only |
| D+5 | non_mainstream | prev_5d_avg_volume_ratio | 1.5 | 345 | 21.45 | 3.5 | 0.71 | provisional_latest_label_only |
| D+5 | non_mainstream | start_day_volume_ratio | 1.5 | 411 | 21.41 | 3.17 | 0.48 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 26682 | 21.25 | 3.87 | 0.61 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 28097 | 20.89 | 3.88 | 0.56 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 27301 | 20.5 | 3.85 | 0.52 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 41632 | 0.72 | 0.6 | provisional_latest_label_only |
| D+1 | mainstream_supported | 1407 | 0.36 | 0.19 | provisional_latest_label_only |
| D+1 | non_mainstream | 874 | 0.69 | 0.67 | provisional_latest_label_only |
| D+1 | unlabeled | 132816 | 0.57 | 0.44 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 41632 | 32.72 | 31.41 | provisional_latest_label_only |
| D+10 | mainstream_supported | 1407 | 14.14 | 11.81 | provisional_latest_label_only |
| D+10 | non_mainstream | 874 | 26.66 | 23.66 | provisional_latest_label_only |
| D+10 | unlabeled | 132816 | 19.28 | 18.28 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 41632 | 6.87 | 5.97 | provisional_latest_label_only |
| D+2 | mainstream_supported | 1407 | 2.49 | 1.65 | provisional_latest_label_only |
| D+2 | non_mainstream | 874 | 6.98 | 4.95 | provisional_latest_label_only |
| D+2 | unlabeled | 132816 | 4.05 | 3.35 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 41632 | 48.43 | 46.75 | provisional_latest_label_only |
| D+20 | mainstream_supported | 1407 | 22.46 | 20.37 | provisional_latest_label_only |
| D+20 | non_mainstream | 874 | 42.33 | 36.79 | provisional_latest_label_only |
| D+20 | unlabeled | 132816 | 29.37 | 28.47 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 41632 | 11.72 | 10.61 | provisional_latest_label_only |
| D+3 | mainstream_supported | 1407 | 4.19 | 3.09 | provisional_latest_label_only |
| D+3 | non_mainstream | 874 | 11.44 | 8.47 | provisional_latest_label_only |
| D+3 | unlabeled | 132816 | 6.93 | 5.94 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 41632 | 15.83 | 14.63 | provisional_latest_label_only |
| D+4 | mainstream_supported | 1407 | 5.83 | 4.3 | provisional_latest_label_only |
| D+4 | non_mainstream | 874 | 14.53 | 11.47 | provisional_latest_label_only |
| D+4 | unlabeled | 132816 | 9.3 | 8.18 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 41632 | 19.46 | 18.19 | provisional_latest_label_only |
| D+5 | mainstream_supported | 1407 | 7.46 | 5.57 | provisional_latest_label_only |
| D+5 | non_mainstream | 874 | 17.28 | 14.18 | provisional_latest_label_only |
| D+5 | unlabeled | 132816 | 11.37 | 10.2 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 41632 | 22.55 | 21.36 | provisional_latest_label_only |
| D+6 | mainstream_supported | 1407 | 8.96 | 6.94 | provisional_latest_label_only |
| D+6 | non_mainstream | 874 | 19.22 | 16.09 | provisional_latest_label_only |
| D+6 | unlabeled | 132816 | 13.23 | 12.07 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 41632 | 25.42 | 24.16 | provisional_latest_label_only |
| D+7 | mainstream_supported | 1407 | 10.31 | 8.08 | provisional_latest_label_only |
| D+7 | non_mainstream | 874 | 21.28 | 18.09 | provisional_latest_label_only |
| D+7 | unlabeled | 132816 | 14.94 | 13.8 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 41632 | 28.03 | 26.76 | provisional_latest_label_only |
| D+8 | mainstream_supported | 1407 | 11.8 | 9.42 | provisional_latest_label_only |
| D+8 | non_mainstream | 874 | 23.46 | 20.42 | provisional_latest_label_only |
| D+8 | unlabeled | 132816 | 16.48 | 15.38 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 41632 | 30.54 | 29.21 | provisional_latest_label_only |
| D+9 | mainstream_supported | 1407 | 12.79 | 10.66 | provisional_latest_label_only |
| D+9 | non_mainstream | 874 | 24.83 | 21.99 | provisional_latest_label_only |
| D+9 | unlabeled | 132816 | 17.92 | 16.89 | provisional_latest_label_only |

