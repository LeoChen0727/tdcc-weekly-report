# Five-Trading-Day Surge Theme Segment Next-Open Research

- generated_at: `2026-07-05 04:14:09 Asia/Taipei`
- entry_basis: D+1 open, because the signal is only known after D0 close.
- target: max high from D+1 through D+1 / ... / D+10 / D+20 reaches at least 10% above D+1 open.
- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.
- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.
- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.

## Overall Base Hit Rates

| Window | Hit Count | Base Hit Rate |
|---|---:|---:|
| D+1 | 2055 | 0.50% |
| D+2 | 16546 | 4.01% |
| D+3 | 29325 | 7.11% |
| D+4 | 40336 | 9.78% |
| D+5 | 50180 | 12.17% |
| D+6 | 59156 | 14.34% |
| D+7 | 67338 | 16.33% |
| D+8 | 74860 | 18.15% |
| D+9 | 81952 | 19.87% |
| D+10 | 88474 | 21.45% |
| D+20 | 135510 | 32.86% |

## Strict No-Lookahead Status

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 183 | 46.45 | 9.12 | 1.25 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 3.0 | 147 | 43.54 | 7.88 | 0.05 | ok |
| D+20 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 85 | 42.35 | 7.62 | 1.19 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.5 | 340 | 42.06 | 8.02 | 0.75 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 2.0 | 304 | 41.78 | 8.05 | 1.01 | ok |
| D+10 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 183 | 41.53 | 7.88 | 1.25 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.0 | 1022 | 41.29 | 7.55 | 0.43 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.0 | 918 | 41.18 | 7.45 | 0.49 | ok |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 85 | 41.18 | 7.62 | 1.19 | ok |
| D+8 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 85 | 41.18 | 6.62 | 1.19 | ok |
| D+9 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 85 | 41.18 | 6.62 | 1.19 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.2 | 725 | 40.69 | 7.26 | 0.62 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.2 | 726 | 40.08 | 7.48 | 0.51 | ok |
| D+20 | mainstream_supported | start_5d_avg_volume_ratio | 1.5 | 416 | 39.9 | 7.67 | 0.6 | ok |
| D+20 | mainstream_supported | start_day_volume_ratio | 1.5 | 519 | 39.69 | 7.16 | 0.72 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.0 | 981 | 39.45 | 7.31 | 0.41 | ok |
| D+20 | mainstream_supported | prev_5d_avg_volume_ratio | 1.2 | 625 | 39.36 | 7.46 | 0.47 | ok |
| D+9 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 183 | 39.34 | 7.3 | 1.25 | ok |
| D+7 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 85 | 38.82 | 6.5 | 1.19 | ok |
| D+10 | mainstream_supported | start_day_volume_ratio | 3.0 | 147 | 38.78 | 6.67 | 0.05 | ok |

## Provisional Exploration - Best D+10 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 710 | 41.55 | 7.99 | 0.67 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 2121 | 41.49 | 7.83 | 0.68 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 7291 | 37.88 | 7.09 | 0.59 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 9316 | 37.61 | 7.07 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 3.0 | 6644 | 37.07 | 6.76 | 0.84 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 2.0 | 14054 | 35.51 | 6.36 | 0.73 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 19009 | 35.14 | 6.43 | 0.55 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 20990 | 34.8 | 6.36 | 0.62 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.5 | 23494 | 33.92 | 6.05 | 0.66 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 36639 | 32.52 | 5.84 | 0.55 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 35557 | 32.46 | 5.83 | 0.52 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.2 | 34441 | 32.15 | 5.74 | 0.6 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_day_volume_ratio | 1.0 | 45989 | 31.04 | 5.55 | 0.56 | provisional_latest_label_only |
| D+10 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 53742 | 30.96 | 5.54 | 0.51 | provisional_latest_label_only |
| D+10 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 53987 | 30.7 | 5.48 | 0.48 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 5128 | 30.64 | 5.17 | 0.61 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 2079 | 28.52 | 4.88 | 0.51 | provisional_latest_label_only |
| D+10 | non_mainstream | start_day_volume_ratio | 1.5 | 116 | 27.59 | 6.02 | 1.07 | provisional_latest_label_only |
| D+10 | unlabeled | start_5d_avg_volume_ratio | 2.0 | 20167 | 27.31 | 4.5 | 0.52 | provisional_latest_label_only |
| D+10 | unlabeled | prev_5d_avg_volume_ratio | 2.0 | 15947 | 27.17 | 4.52 | 0.46 | provisional_latest_label_only |

## Provisional Exploration - Best D+5 Rows

| target_window | theme_status_group | filter_metric | threshold | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 3.0 | 2121 | 28.67 | 5.16 | 0.68 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 3.0 | 710 | 27.04 | 5.19 | 0.67 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 3.0 | 6644 | 25.51 | 4.56 | 0.84 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 2.0 | 9316 | 24.47 | 4.57 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 2.0 | 7291 | 23.84 | 4.62 | 0.59 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 2.0 | 14054 | 23.6 | 4.15 | 0.73 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.5 | 20990 | 22.2 | 4.09 | 0.62 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.5 | 23494 | 21.8 | 3.87 | 0.66 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.5 | 19009 | 21.78 | 4.1 | 0.55 | provisional_latest_label_only |
| D+5 | unlabeled | start_5d_avg_volume_ratio | 3.0 | 5128 | 21.74 | 3.74 | 0.61 | provisional_latest_label_only |
| D+5 | non_mainstream | start_day_volume_ratio | 1.5 | 116 | 20.69 | 3.44 | 1.07 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.2 | 34441 | 20.03 | 3.63 | 0.6 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.2 | 36639 | 20.0 | 3.7 | 0.55 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.2 | 35557 | 19.68 | 3.67 | 0.52 | provisional_latest_label_only |
| D+5 | unlabeled | prev_5d_avg_volume_ratio | 3.0 | 2079 | 19.62 | 3.44 | 0.51 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_day_volume_ratio | 1.0 | 45989 | 18.86 | 3.47 | 0.56 | provisional_latest_label_only |
| D+5 | mainstream_overheated | start_5d_avg_volume_ratio | 1.0 | 53742 | 18.4 | 3.45 | 0.51 | provisional_latest_label_only |
| D+5 | mainstream_supported | start_5d_avg_volume_ratio | 2.0 | 245 | 18.37 | 2.29 | 0.41 | provisional_latest_label_only |
| D+5 | non_mainstream | start_day_volume_ratio | 1.0 | 218 | 18.35 | 3.16 | 0.74 | provisional_latest_label_only |
| D+5 | mainstream_overheated | prev_5d_avg_volume_ratio | 1.0 | 53987 | 18.04 | 3.4 | 0.48 | provisional_latest_label_only |

## Provisional Group Baselines

| target_window | theme_status_group | selected_stock_days | hit_rate_pct | group_base_hit_rate_pct | sample_status |
| --- | --- | --- | --- | --- | --- |
| D+1 | mainstream_overheated | 53742 | 0.72 | 0.6 | provisional_latest_label_only |
| D+1 | mainstream_supported | 2347 | 0.38 | 0.22 | provisional_latest_label_only |
| D+1 | non_mainstream | 249 | 0.4 | 0.55 | provisional_latest_label_only |
| D+1 | unlabeled | 122297 | 0.59 | 0.46 | provisional_latest_label_only |
| D+10 | mainstream_overheated | 53742 | 30.96 | 29.32 | provisional_latest_label_only |
| D+10 | mainstream_supported | 2347 | 9.25 | 7.24 | provisional_latest_label_only |
| D+10 | non_mainstream | 249 | 23.69 | 25.0 | provisional_latest_label_only |
| D+10 | unlabeled | 122297 | 19.38 | 18.31 | provisional_latest_label_only |
| D+2 | mainstream_overheated | 53742 | 6.59 | 5.59 | provisional_latest_label_only |
| D+2 | mainstream_supported | 2347 | 1.83 | 1.15 | provisional_latest_label_only |
| D+2 | non_mainstream | 249 | 6.43 | 5.11 | provisional_latest_label_only |
| D+2 | unlabeled | 122297 | 4.06 | 3.38 | provisional_latest_label_only |
| D+20 | mainstream_overheated | 53742 | 45.93 | 44.04 | provisional_latest_label_only |
| D+20 | mainstream_supported | 2347 | 15.17 | 12.43 | provisional_latest_label_only |
| D+20 | non_mainstream | 249 | 37.75 | 41.06 | provisional_latest_label_only |
| D+20 | unlabeled | 122297 | 29.49 | 28.38 | provisional_latest_label_only |
| D+3 | mainstream_overheated | 53742 | 11.14 | 9.9 | provisional_latest_label_only |
| D+3 | mainstream_supported | 2347 | 3.03 | 2.01 | provisional_latest_label_only |
| D+3 | non_mainstream | 249 | 10.44 | 8.76 | provisional_latest_label_only |
| D+3 | unlabeled | 122297 | 7.0 | 5.99 | provisional_latest_label_only |
| D+4 | mainstream_overheated | 53742 | 15.0 | 13.6 | provisional_latest_label_only |
| D+4 | mainstream_supported | 2347 | 4.18 | 2.79 | provisional_latest_label_only |
| D+4 | non_mainstream | 249 | 12.85 | 11.31 | provisional_latest_label_only |
| D+4 | unlabeled | 122297 | 9.39 | 8.25 | provisional_latest_label_only |
| D+5 | mainstream_overheated | 53742 | 18.4 | 16.87 | provisional_latest_label_only |
| D+5 | mainstream_supported | 2347 | 5.54 | 3.78 | provisional_latest_label_only |
| D+5 | non_mainstream | 249 | 16.06 | 14.78 | provisional_latest_label_only |
| D+5 | unlabeled | 122297 | 11.46 | 10.28 | provisional_latest_label_only |
| D+6 | mainstream_overheated | 53742 | 21.39 | 19.87 | provisional_latest_label_only |
| D+6 | mainstream_supported | 2347 | 6.39 | 4.5 | provisional_latest_label_only |
| D+6 | non_mainstream | 249 | 17.67 | 16.79 | provisional_latest_label_only |
| D+6 | unlabeled | 122297 | 13.31 | 12.13 | provisional_latest_label_only |
| D+7 | mainstream_overheated | 53742 | 24.08 | 22.51 | provisional_latest_label_only |
| D+7 | mainstream_supported | 2347 | 7.12 | 5.12 | provisional_latest_label_only |
| D+7 | non_mainstream | 249 | 20.48 | 19.71 | provisional_latest_label_only |
| D+7 | unlabeled | 122297 | 15.03 | 13.85 | provisional_latest_label_only |
| D+8 | mainstream_overheated | 53742 | 26.55 | 24.96 | provisional_latest_label_only |
| D+8 | mainstream_supported | 2347 | 7.75 | 5.82 | provisional_latest_label_only |
| D+8 | non_mainstream | 249 | 22.09 | 21.53 | provisional_latest_label_only |
| D+8 | unlabeled | 122297 | 16.59 | 15.43 | provisional_latest_label_only |
| D+9 | mainstream_overheated | 53742 | 28.9 | 27.25 | provisional_latest_label_only |
| D+9 | mainstream_supported | 2347 | 8.39 | 6.59 | provisional_latest_label_only |
| D+9 | non_mainstream | 249 | 22.89 | 23.36 | provisional_latest_label_only |
| D+9 | unlabeled | 122297 | 18.03 | 16.92 | provisional_latest_label_only |

