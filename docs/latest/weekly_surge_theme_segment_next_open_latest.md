# Weekly Surge Theme Segment Next-Open Research

- generated_at: `2026-05-28 13:25:49 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+5 / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+5 | 30042 | 13.81% |
| D+10 | 51881 | 23.85% |
| D+20 | 76870 | 35.33% |

## Strict No-Lookahead Status

- current_status: insufficient_history
- reason: daily theme status history has only started accumulating; strict historical labels are not mature enough for conclusions.

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 139 | 52.52 | 10.8 | 0.53 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 476 | 48.32 | 9.31 | 0.85 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 1797 | 47.41 | 9.23 | 0.64 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 2259 | 46.66 | 9.17 | 0.82 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 4616 | 46.21 | 9.03 | 0.72 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 3432 | 45.8 | 8.96 | 1.0 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 5099 | 45.79 | 8.92 | 0.8 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 1607 | 45.49 | 9.0 | 1.12 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 8363 | 44.95 | 8.58 | 0.71 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 8593 | 44.41 | 8.46 | 0.77 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 5665 | 44.38 | 8.62 | 0.91 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 8061 | 43.39 | 8.31 | 0.86 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 12402 | 43.36 | 8.17 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 12435 | 43.05 | 8.13 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 10621 | 42.41 | 8.06 | 0.81 | provisional_latest_label_only |
| D+10 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 3938 | 35.27 | 6.68 | 0.53 | provisional_latest_label_only |
| D+10 | mainstream_supported | start_day_volume_ratio | 3.0 | 1393 | 35.25 | 6.56 | 0.81 | provisional_latest_label_only |
| D+10 | mainstream_supported | prev_5d_avg_volume_ratio | 2.0 | 1477 | 35.14 | 6.82 | 0.55 | provisional_latest_label_only |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 1919 | 34.81 | 6.71 | 0.62 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 2926 | 34.35 | 5.86 | 0.7 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 3432 | 30.27 | 5.65 | 1.0 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 1607 | 30.18 | 5.7 | 1.12 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 5099 | 29.46 | 5.43 | 0.8 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 2259 | 29.44 | 5.45 | 0.82 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 1797 | 29.16 | 5.49 | 0.64 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 4616 | 29.14 | 5.31 | 0.72 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 5665 | 28.88 | 5.4 | 0.91 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 476 | 28.57 | 5.66 | 0.85 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 8363 | 28.12 | 4.99 | 0.71 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 8593 | 28.03 | 5.1 | 0.77 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 8061 | 27.75 | 5.2 | 0.86 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 10621 | 26.71 | 4.99 | 0.81 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 12402 | 26.58 | 4.78 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 12435 | 26.45 | 4.84 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 139 | 25.9 | 5.87 | 0.53 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 2926 | 24.06 | 4.18 | 0.7 | provisional_latest_label_only |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 3.0 | 417 | 23.74 | 4.42 | 0.59 | provisional_latest_label_only |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 1919 | 22.82 | 4.17 | 0.62 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 1187 | 22.75 | 3.96 | 0.58 | provisional_latest_label_only |
| D+5 | mainstream_supported | prev_5d_avg_volume_ratio | 2.0 | 1477 | 22.55 | 4.27 | 0.55 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | 12435 | 43.05 | 42.02 | provisional_latest_label_only |
| D+10 | mainstream_supported | 10989 | 32.2 | 30.65 | provisional_latest_label_only |
| D+10 | non_mainstream | 4549 | 14.29 | 13.76 | provisional_latest_label_only |
| D+10 | unlabeled | 69653 | 21.5 | 20.32 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 12435 | 59.11 | 58.66 | provisional_latest_label_only |
| D+20 | mainstream_supported | 10989 | 49.29 | 47.73 | provisional_latest_label_only |
| D+20 | non_mainstream | 4549 | 21.76 | 22.15 | provisional_latest_label_only |
| D+20 | unlabeled | 69653 | 31.27 | 30.26 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 12435 | 26.45 | 25.23 | provisional_latest_label_only |
| D+5 | mainstream_supported | 10989 | 17.6 | 16.54 | provisional_latest_label_only |
| D+5 | non_mainstream | 4549 | 9.32 | 7.74 | provisional_latest_label_only |
| D+5 | unlabeled | 69653 | 12.98 | 11.81 | provisional_latest_label_only |

