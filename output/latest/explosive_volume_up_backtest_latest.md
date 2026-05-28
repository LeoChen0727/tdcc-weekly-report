# Explosive Volume Up Backtest

- generated_at: `2026-05-28 21:23:14 Asia/Taipei`
- signal_definition: signal day volume / previous 20 trading day average volume >= threshold, and signal day close-to-close return >= minimum return.
- entry_basis: next trading day open.
- close_return: next open to D+N close.
- high_hit_rate: next open to the highest high within D+N reaches target return.
- purpose: research only; do not mix into daily candidate core ranking until sample and regime tests mature.

## Data Summary

- total_event_rows: `17802`
- unique_stock_days: `17802`
- date_range: `20251117` to `20260527`

## D+10 Highest +10% Hit Rate

| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | avg_mfe_pct | avg_mae_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 4631 | 4322 | 45.16 | 2.29 | -1.34 | 46.07 | 23.92 | 14.0 | -9.56 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 3195 | 3007 | 43.33 | 1.97 | -1.85 | 44.23 | 22.98 | 13.59 | -9.4 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 6573 | 6122 | 44.71 | 2.03 | -1.33 | 43.65 | 22.02 | 13.16 | -9.06 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 2283 | 2165 | 42.73 | 1.64 | -2.01 | 43.33 | 21.89 | 13.27 | -9.25 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 4396 | 4134 | 43.23 | 1.82 | -1.75 | 42.33 | 21.19 | 12.88 | -8.95 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 1680 | 1614 | 40.77 | 0.75 | -2.42 | 42.19 | 20.2 | 12.47 | -9.28 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 3042 | 2877 | 42.61 | 1.5 | -1.89 | 41.64 | 20.23 | 12.63 | -8.82 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 2169 | 2071 | 41.14 | 0.89 | -2.31 | 41.28 | 19.31 | 12.16 | -8.9 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 1261 | 1226 | 39.97 | 0.53 | -2.49 | 41.27 | 19.41 | 12.13 | -9.18 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 737 | 720 | 38.89 | 0.21 | -2.83 | 41.25 | 20.14 | 12.01 | -9.21 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 1624 | 1569 | 40.41 | 0.71 | -2.33 | 40.47 | 18.67 | 11.88 | -8.84 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 9777 | 9123 | 44.12 | 1.76 | -1.27 | 39.73 | 19.48 | 12.02 | -8.35 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 928 | 904 | 38.61 | 0.04 | -2.85 | 39.6 | 18.25 | 11.42 | -8.97 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+10 | 4007 | 3796 | 42.33 | 1.33 | -1.84 | 39.41 | 18.68 | 11.88 | -8.41 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+10 | 6051 | 5698 | 42.77 | 1.58 | -1.7 | 39.36 | 19.15 | 11.96 | -8.4 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+10 | 2806 | 2676 | 40.58 | 0.76 | -2.11 | 38.79 | 17.9 | 11.46 | -8.52 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 472 | 461 | 34.06 | -1.05 | -3.64 | 38.18 | 16.05 | 10.8 | -9.25 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_3pct | D+10 | 2045 | 1978 | 39.48 | 0.49 | -2.32 | 38.17 | 17.49 | 11.22 | -8.58 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 595 | 581 | 35.46 | -0.87 | -3.47 | 37.52 | 14.97 | 10.49 | -9.0 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+10 | 1163 | 1132 | 37.81 | -0.16 | -2.93 | 37.28 | 16.78 | 10.72 | -8.75 | ok |

## D+20 Highest +10% Hit Rate

| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | avg_mfe_pct | avg_mae_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 4631 | 3861 | 46.0 | 5.19 | -1.61 | 57.21 | 36.44 | 21.43 | -11.82 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 6573 | 5452 | 45.95 | 4.75 | -1.46 | 55.32 | 34.56 | 20.25 | -11.3 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 3195 | 2726 | 43.62 | 4.0 | -2.46 | 54.73 | 34.01 | 20.23 | -11.7 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 4396 | 3728 | 44.02 | 3.72 | -2.21 | 53.46 | 32.27 | 19.25 | -11.24 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 2283 | 1980 | 42.17 | 3.07 | -3.07 | 53.08 | 31.92 | 19.16 | -11.61 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 3042 | 2625 | 42.55 | 2.91 | -2.74 | 52.0 | 30.32 | 18.34 | -11.15 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 9777 | 8171 | 45.91 | 4.15 | -1.26 | 51.94 | 31.15 | 18.42 | -10.47 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 1680 | 1490 | 40.74 | 2.1 | -3.3 | 51.88 | 30.6 | 17.9 | -11.61 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 6051 | 5168 | 44.49 | 3.41 | -1.73 | 51.28 | 29.72 | 17.89 | -10.58 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 2169 | 1915 | 40.94 | 2.12 | -3.12 | 51.07 | 29.5 | 17.47 | -11.22 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 737 | 674 | 39.17 | 1.43 | -3.69 | 50.89 | 29.38 | 17.07 | -11.43 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 1261 | 1134 | 39.51 | 1.71 | -3.55 | 50.62 | 29.81 | 17.33 | -11.41 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 1624 | 1454 | 40.1 | 1.71 | -3.34 | 50.28 | 28.75 | 16.91 | -11.1 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+20 | 4007 | 3476 | 42.61 | 2.71 | -2.42 | 50.17 | 28.45 | 17.34 | -10.67 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 928 | 843 | 38.2 | 0.8 | -3.76 | 48.99 | 26.81 | 16.07 | -11.35 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+20 | 2806 | 2480 | 40.89 | 1.92 | -2.85 | 48.79 | 27.46 | 16.54 | -10.75 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_3pct | D+20 | 2045 | 1835 | 39.46 | 1.44 | -3.33 | 48.17 | 26.98 | 16.13 | -10.83 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 472 | 434 | 36.18 | 0.23 | -4.49 | 48.16 | 26.04 | 15.68 | -11.48 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+20 | 595 | 545 | 35.6 | 0.02 | -4.52 | 47.16 | 23.85 | 14.93 | -11.31 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+20 | 1163 | 1062 | 37.66 | 0.61 | -4.01 | 46.89 | 25.24 | 15.33 | -11.12 | ok |

## Threshold Matrix: D+10

| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | avg_mfe_pct | avg_mae_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_10x_signal_return_ge_0pct | D+10 | 964 | 932 | 36.48 | -0.63 | -2.72 | 32.62 | 13.2 | 9.49 | -8.24 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_3pct | D+10 | 739 | 722 | 35.18 | -1.0 | -3.22 | 35.32 | 13.85 | 9.91 | -8.81 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 595 | 581 | 35.46 | -0.87 | -3.47 | 37.52 | 14.97 | 10.49 | -9.0 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 472 | 461 | 34.06 | -1.05 | -3.64 | 38.18 | 16.05 | 10.8 | -9.25 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_0pct | D+10 | 1518 | 1458 | 38.61 | -0.03 | -2.38 | 34.77 | 15.5 | 10.15 | -8.21 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+10 | 1163 | 1132 | 37.81 | -0.16 | -2.93 | 37.28 | 16.78 | 10.72 | -8.75 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 928 | 904 | 38.61 | 0.04 | -2.85 | 39.6 | 18.25 | 11.42 | -8.97 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 737 | 720 | 38.89 | 0.21 | -2.83 | 41.25 | 20.14 | 12.01 | -9.21 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_0pct | D+10 | 2690 | 2576 | 39.6 | 0.45 | -1.93 | 35.13 | 15.99 | 10.45 | -8.03 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_3pct | D+10 | 2045 | 1978 | 39.48 | 0.49 | -2.32 | 38.17 | 17.49 | 11.22 | -8.58 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 1624 | 1569 | 40.41 | 0.71 | -2.33 | 40.47 | 18.67 | 11.88 | -8.84 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 1261 | 1226 | 39.97 | 0.53 | -2.49 | 41.27 | 19.41 | 12.13 | -9.18 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_0pct | D+10 | 3771 | 3564 | 40.77 | 0.73 | -1.75 | 35.47 | 16.36 | 10.63 | -7.92 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+10 | 2806 | 2676 | 40.58 | 0.76 | -2.11 | 38.79 | 17.9 | 11.46 | -8.52 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 2169 | 2071 | 41.14 | 0.89 | -2.31 | 41.28 | 19.31 | 12.16 | -8.9 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 1680 | 1614 | 40.77 | 0.75 | -2.42 | 42.19 | 20.2 | 12.47 | -9.28 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_0pct | D+10 | 5571 | 5243 | 42.08 | 1.12 | -1.49 | 35.29 | 16.48 | 10.79 | -7.77 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+10 | 4007 | 3796 | 42.33 | 1.33 | -1.84 | 39.41 | 18.68 | 11.88 | -8.41 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 3042 | 2877 | 42.61 | 1.5 | -1.89 | 41.64 | 20.23 | 12.63 | -8.82 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 2283 | 2165 | 42.73 | 1.64 | -2.01 | 43.33 | 21.89 | 13.27 | -9.25 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_0pct | D+10 | 9138 | 8561 | 42.53 | 1.34 | -1.29 | 34.32 | 16.38 | 10.58 | -7.51 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+10 | 6051 | 5698 | 42.77 | 1.58 | -1.7 | 39.36 | 19.15 | 11.96 | -8.4 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 4396 | 4134 | 43.23 | 1.82 | -1.75 | 42.33 | 21.19 | 12.88 | -8.95 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 3195 | 3007 | 43.33 | 1.97 | -1.85 | 44.23 | 22.98 | 13.59 | -9.4 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_0pct | D+10 | 17802 | 16626 | 43.35 | 1.35 | -0.91 | 32.28 | 14.81 | 9.93 | -6.97 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 9777 | 9123 | 44.12 | 1.76 | -1.27 | 39.73 | 19.48 | 12.02 | -8.35 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 6573 | 6122 | 44.71 | 2.03 | -1.33 | 43.65 | 22.02 | 13.16 | -9.06 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 4631 | 4322 | 45.16 | 2.29 | -1.34 | 46.07 | 23.92 | 14.0 | -9.56 | ok |

## Threshold Matrix: D+20

| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | avg_mfe_pct | avg_mae_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_10x_signal_return_ge_0pct | D+20 | 964 | 882 | 37.07 | 0.52 | -3.12 | 43.08 | 21.32 | 13.89 | -10.26 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_3pct | D+20 | 739 | 682 | 35.63 | -0.06 | -4.4 | 45.6 | 22.58 | 14.4 | -11.08 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+20 | 595 | 545 | 35.6 | 0.02 | -4.52 | 47.16 | 23.85 | 14.93 | -11.31 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 472 | 434 | 36.18 | 0.23 | -4.49 | 48.16 | 26.04 | 15.68 | -11.48 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_0pct | D+20 | 1518 | 1372 | 39.43 | 1.02 | -2.73 | 44.53 | 23.69 | 14.69 | -10.37 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+20 | 1163 | 1062 | 37.66 | 0.61 | -4.01 | 46.89 | 25.24 | 15.33 | -11.12 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 928 | 843 | 38.2 | 0.8 | -3.76 | 48.99 | 26.81 | 16.07 | -11.35 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 737 | 674 | 39.17 | 1.43 | -3.69 | 50.89 | 29.38 | 17.07 | -11.43 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_0pct | D+20 | 2690 | 2405 | 40.58 | 1.46 | -2.41 | 45.24 | 24.86 | 15.1 | -10.13 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_3pct | D+20 | 2045 | 1835 | 39.46 | 1.44 | -3.33 | 48.17 | 26.98 | 16.13 | -10.83 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 1624 | 1454 | 40.1 | 1.71 | -3.34 | 50.28 | 28.75 | 16.91 | -11.1 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 1261 | 1134 | 39.51 | 1.71 | -3.55 | 50.62 | 29.81 | 17.33 | -11.41 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_0pct | D+20 | 3771 | 3324 | 41.52 | 1.75 | -2.21 | 45.34 | 25.12 | 15.34 | -10.04 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+20 | 2806 | 2480 | 40.89 | 1.92 | -2.85 | 48.79 | 27.46 | 16.54 | -10.75 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 2169 | 1915 | 40.94 | 2.12 | -3.12 | 51.07 | 29.5 | 17.47 | -11.22 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 1680 | 1490 | 40.74 | 2.1 | -3.3 | 51.88 | 30.6 | 17.9 | -11.61 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_0pct | D+20 | 5571 | 4830 | 42.8 | 2.33 | -1.79 | 46.09 | 25.94 | 15.85 | -9.93 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+20 | 4007 | 3476 | 42.61 | 2.71 | -2.42 | 50.17 | 28.45 | 17.34 | -10.67 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 3042 | 2625 | 42.55 | 2.91 | -2.74 | 52.0 | 30.32 | 18.34 | -11.15 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 2283 | 1980 | 42.17 | 3.07 | -3.07 | 53.08 | 31.92 | 19.16 | -11.61 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_0pct | D+20 | 9138 | 7846 | 44.35 | 2.87 | -1.34 | 45.86 | 26.18 | 15.95 | -9.52 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 6051 | 5168 | 44.49 | 3.41 | -1.73 | 51.28 | 29.72 | 17.89 | -10.58 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 4396 | 3728 | 44.02 | 3.72 | -2.21 | 53.46 | 32.27 | 19.25 | -11.24 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 3195 | 2726 | 43.62 | 4.0 | -2.46 | 54.73 | 34.01 | 20.23 | -11.7 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_0pct | D+20 | 17802 | 15110 | 45.39 | 3.18 | -0.9 | 44.12 | 24.88 | 15.32 | -8.87 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 9777 | 8171 | 45.91 | 4.15 | -1.26 | 51.94 | 31.15 | 18.42 | -10.47 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 6573 | 5452 | 45.95 | 4.75 | -1.46 | 55.32 | 34.56 | 20.25 | -11.3 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 4631 | 3861 | 46.0 | 5.19 | -1.61 | 57.21 | 36.44 | 21.43 | -11.82 | ok |

## Interpretation

- If a high volume-ratio threshold has very few mature samples, the hit rate is unstable even if it looks high.
- If lowering the threshold increases sample size but hit rate falls toward 50%, volume alone is not discriminative enough.
- This module should next be segmented by theme/mainstream status, TDCC phase, market regime, and technical position.

