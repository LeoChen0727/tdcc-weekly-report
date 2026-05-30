# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-05-30 19:29:02 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 6107 | 1.20% |
| D+2 | 18641 | 3.65% |
| D+3 | 30092 | 5.89% |
| D+4 | 40199 | 7.87% |
| D+5 | 49366 | 9.67% |
| D+6 | 57764 | 11.31% |
| D+7 | 65489 | 12.83% |
| D+8 | 72618 | 14.22% |
| D+9 | 79413 | 15.55% |
| D+10 | 85667 | 16.78% |
| D+20 | 131998 | 25.85% |

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
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 482 | 40.66 | 7.62 | 0.58 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1500 | 40.53 | 7.18 | 0.7 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 4971 | 37.82 | 6.96 | 0.61 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 4475 | 37.63 | 6.79 | 0.88 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 6332 | 37.43 | 6.84 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 9328 | 36.99 | 6.69 | 0.81 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 12496 | 35.87 | 6.59 | 0.63 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 15370 | 35.74 | 6.47 | 0.74 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 13830 | 35.7 | 6.59 | 0.68 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 23203 | 34.66 | 6.29 | 0.59 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 23909 | 34.5 | 6.28 | 0.63 | provisional_latest_label_only |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 3.0 | 334 | 34.43 | 5.93 | 0.75 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 22375 | 34.25 | 6.26 | 0.68 | provisional_latest_label_only |
| D+10 | mainstream_supported | prev_5d_avg_volume_ratio | 3.0 | 109 | 33.94 | 6.15 | 1.03 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 4771 | 30.2 | 5.09 | 0.57 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1917 | 28.27 | 4.88 | 0.46 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 41777 | 28.14 | 4.81 | 0.44 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 41924 | 28.07 | 4.8 | 0.41 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 14410 | 27.63 | 4.47 | 0.46 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 36701 | 27.53 | 4.61 | 0.47 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 1500 | 27.27 | 4.94 | 0.7 | provisional_latest_label_only |
| D+5 | mainstream_supported | prev_5d_avg_volume_ratio | 3.0 | 109 | 25.69 | 4.12 | 1.03 | provisional_latest_label_only |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 3.0 | 334 | 25.45 | 3.88 | 0.75 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 4475 | 25.34 | 4.65 | 0.88 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 9328 | 24.04 | 4.44 | 0.81 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 482 | 23.65 | 5.01 | 0.58 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 6332 | 23.59 | 4.57 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 4971 | 22.91 | 4.58 | 0.61 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 15370 | 22.43 | 4.2 | 0.74 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 13830 | 22.24 | 4.27 | 0.68 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 12496 | 21.58 | 4.22 | 0.63 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 22375 | 21.07 | 4.03 | 0.68 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 4771 | 20.94 | 3.65 | 0.57 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 23909 | 20.51 | 3.97 | 0.63 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 23203 | 20.4 | 3.96 | 0.59 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1917 | 19.2 | 3.37 | 0.46 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 18410 | 17.88 | 3.08 | 0.51 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 14410 | 17.64 | 3.08 | 0.46 | provisional_latest_label_only |
| D+5 | unlabeled | start_day_volume_ratio | 3.0 | 14161 | 17.34 | 2.89 | 0.61 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 36701 | 16.4 | 3.29 | 0.47 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 41777 | 0.58 | 0.47 | provisional_latest_label_only |
| D+1 | mainstream_supported | 14051 | 0.23 | 0.17 | provisional_latest_label_only |
| D+1 | non_mainstream | 499 | 0.0 | 0.0 | provisional_latest_label_only |
| D+1 | unlabeled | 235035 | 2.2 | 1.44 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 41777 | 28.14 | 28.93 | provisional_latest_label_only |
| D+10 | mainstream_supported | 14051 | 15.35 | 15.17 | provisional_latest_label_only |
| D+10 | non_mainstream | 499 | 17.64 | 13.25 | provisional_latest_label_only |
| D+10 | unlabeled | 235035 | 12.51 | 14.19 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 41777 | 5.6 | 5.07 | provisional_latest_label_only |
| D+2 | mainstream_supported | 14051 | 2.55 | 2.1 | provisional_latest_label_only |
| D+2 | non_mainstream | 499 | 1.4 | 1.1 | provisional_latest_label_only |
| D+2 | unlabeled | 235035 | 4.02 | 3.46 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 41777 | 42.3 | 43.79 | provisional_latest_label_only |
| D+20 | mainstream_supported | 14051 | 26.43 | 26.57 | provisional_latest_label_only |
| D+20 | non_mainstream | 499 | 26.85 | 22.03 | provisional_latest_label_only |
| D+20 | unlabeled | 235035 | 18.68 | 21.78 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 41777 | 9.58 | 9.18 | provisional_latest_label_only |
| D+3 | mainstream_supported | 14051 | 4.44 | 3.89 | provisional_latest_label_only |
| D+3 | non_mainstream | 499 | 2.81 | 2.29 | provisional_latest_label_only |
| D+3 | unlabeled | 235035 | 5.57 | 5.32 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 41777 | 13.17 | 12.89 | provisional_latest_label_only |
| D+4 | mainstream_supported | 14051 | 6.21 | 5.69 | provisional_latest_label_only |
| D+4 | non_mainstream | 499 | 4.61 | 3.84 | provisional_latest_label_only |
| D+4 | unlabeled | 235035 | 6.85 | 6.93 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 41777 | 16.35 | 16.21 | provisional_latest_label_only |
| D+5 | mainstream_supported | 14051 | 7.94 | 7.43 | provisional_latest_label_only |
| D+5 | non_mainstream | 499 | 6.61 | 5.39 | provisional_latest_label_only |
| D+5 | unlabeled | 235035 | 7.98 | 8.39 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 41777 | 19.06 | 19.21 | provisional_latest_label_only |
| D+6 | mainstream_supported | 14051 | 9.66 | 9.14 | provisional_latest_label_only |
| D+6 | non_mainstream | 499 | 9.02 | 7.31 | provisional_latest_label_only |
| D+6 | unlabeled | 235035 | 9.01 | 9.72 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 41777 | 21.56 | 21.88 | provisional_latest_label_only |
| D+7 | mainstream_supported | 14051 | 11.27 | 10.77 | provisional_latest_label_only |
| D+7 | non_mainstream | 499 | 11.42 | 9.14 | provisional_latest_label_only |
| D+7 | unlabeled | 235035 | 9.98 | 10.97 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 41777 | 23.91 | 24.39 | provisional_latest_label_only |
| D+8 | mainstream_supported | 14051 | 12.68 | 12.32 | provisional_latest_label_only |
| D+8 | non_mainstream | 499 | 13.83 | 10.6 | provisional_latest_label_only |
| D+8 | unlabeled | 235035 | 10.87 | 12.1 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 41777 | 26.06 | 26.74 | provisional_latest_label_only |
| D+9 | mainstream_supported | 14051 | 14.08 | 13.83 | provisional_latest_label_only |
| D+9 | non_mainstream | 499 | 16.23 | 12.34 | provisional_latest_label_only |
| D+9 | unlabeled | 235035 | 11.73 | 13.19 | provisional_latest_label_only |

