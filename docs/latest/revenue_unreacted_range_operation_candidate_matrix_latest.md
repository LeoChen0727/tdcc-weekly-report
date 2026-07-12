# Revenue Unreacted Range Operation Candidate Matrix

- generated_at: `2026-07-13 02:01:50 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.
- entry_basis: signal-date close condition, next trading day open entry.
- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.
- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| condition_test_id | exit_rule_id | accepted_trade_count | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | stop_trigger_rate_pct | accepted_trade_share_of_baseline_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_context_ready | d10_close_no_stop | 17069 | 292659 | 17.85 | 28.04 | 54.12 | 0.68 | -0.53 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_no_stop | 16780 | 292659 | 22.32 | 25.15 | 52.53 | 1.45 | -0.43 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_no_stop | 16159 | 292659 | 25.38 | 22.78 | 51.84 | 1.97 | -0.36 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d10_close_ma20_ema23_4d_stop | 15355 | 292659 | 17.37 | 27.9 | 54.73 | 0.74 | -0.6 | 13.98 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_ma20_ema23_4d_stop | 15023 | 292659 | 21.14 | 24.27 | 54.59 | 1.32 | -0.7 | 18.79 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_ma20_ema23_4d_stop | 14430 | 292659 | 23.44 | 22.04 | 54.51 | 1.8 | -0.77 | 23.58 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_no_stop | 5183 | 75593 | 22.4 | 23.79 | 53.81 | 1.02 | -0.71 | 0.0 | 30.36 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_no_stop | 4920 | 75593 | 27.42 | 21.48 | 51.1 | 2.19 | -0.33 | 0.0 | 29.32 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_no_stop | 4750 | 75593 | 29.94 | 18.76 | 51.31 | 2.94 | -0.35 | 0.0 | 29.4 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_ma20_ema23_4d_stop | 4729 | 75593 | 21.67 | 23.56 | 54.77 | 1.0 | -0.85 | 15.86 | 30.8 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_ma20_ema23_4d_stop | 4394 | 75593 | 26.17 | 20.44 | 53.39 | 2.01 | -0.78 | 21.53 | 29.25 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_ma20_ema23_4d_stop | 4296 | 75593 | 27.89 | 18.16 | 53.96 | 2.78 | -0.99 | 26.84 | 29.77 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_no_stop | 2712 | 36180 | 23.56 | 21.2 | 55.24 | 0.99 | -0.93 | 0.0 | 15.89 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_no_stop | 2528 | 36180 | 28.92 | 19.9 | 51.19 | 2.54 | -0.43 | 0.0 | 15.07 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_no_stop | 2430 | 36180 | 30.82 | 16.34 | 52.84 | 3.1 | -0.76 | 0.0 | 15.04 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_ma20_ema23_4d_stop | 2514 | 36180 | 23.03 | 20.68 | 56.28 | 0.94 | -1.07 | 16.55 | 16.37 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_ma20_ema23_4d_stop | 2287 | 36180 | 27.77 | 18.45 | 53.78 | 2.33 | -0.96 | 22.04 | 15.22 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_ma20_ema23_4d_stop | 2239 | 36180 | 29.3 | 14.69 | 56.01 | 2.92 | -1.52 | 27.51 | 15.52 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_no_stop | 1608 | 21594 | 23.45 | 19.84 | 56.72 | 0.98 | -1.23 | 0.0 | 9.42 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_no_stop | 1498 | 21594 | 29.84 | 17.62 | 52.54 | 2.7 | -0.66 | 0.0 | 8.93 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_no_stop | 1437 | 21594 | 31.11 | 15.66 | 53.24 | 3.42 | -0.83 | 0.0 | 8.89 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_ma20_ema23_4d_stop | 1501 | 21594 | 23.05 | 19.45 | 57.5 | 1.02 | -1.35 | 17.85 | 9.78 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_ma20_ema23_4d_stop | 1369 | 21594 | 28.34 | 16.73 | 54.93 | 2.61 | -1.09 | 23.89 | 9.11 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_ma20_ema23_4d_stop | 1334 | 21594 | 29.69 | 14.32 | 56.0 | 3.41 | -1.51 | 29.16 | 9.24 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_no_stop | 3204 | 41396 | 16.29 | 27.81 | 55.9 | 0.14 | -0.81 | 0.0 | 18.77 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_no_stop | 3104 | 41396 | 21.52 | 25.52 | 52.96 | 0.88 | -0.5 | 0.0 | 18.5 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_no_stop | 3032 | 41396 | 24.37 | 22.23 | 53.4 | 1.61 | -0.64 | 0.0 | 18.76 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_ma20_ema23_4d_stop | 2867 | 41396 | 15.97 | 27.45 | 56.57 | 0.14 | -0.86 | 10.5 | 18.67 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_ma20_ema23_4d_stop | 2731 | 41396 | 20.73 | 24.83 | 54.45 | 0.77 | -0.75 | 16.4 | 18.18 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_ma20_ema23_4d_stop | 2693 | 41396 | 22.76 | 21.17 | 56.07 | 1.35 | -1.12 | 21.35 | 18.66 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_no_stop | 2365 | 27475 | 14.71 | 29.68 | 55.6 | 0.03 | -0.77 | 0.0 | 13.86 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_no_stop | 2294 | 27475 | 20.1 | 26.33 | 53.57 | 0.8 | -0.59 | 0.0 | 13.67 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_no_stop | 2253 | 27475 | 22.9 | 24.01 | 53.08 | 1.2 | -0.48 | 0.0 | 13.94 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_ma20_ema23_4d_stop | 2126 | 27475 | 14.58 | 29.44 | 55.97 | 0.08 | -0.78 | 8.04 | 13.85 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_ma20_ema23_4d_stop | 2041 | 27475 | 19.55 | 25.62 | 54.83 | 0.81 | -0.72 | 13.57 | 13.59 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_ma20_ema23_4d_stop | 2021 | 27475 | 22.32 | 22.76 | 54.92 | 1.21 | -0.84 | 17.66 | 14.01 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_no_stop | 1178 | 11595 | 11.71 | 32.26 | 56.03 | -0.06 | -0.7 | 0.0 | 6.9 | not_candidate_metric |
| strong_revenue_range23_width_le10 | d15_close_no_stop | 1149 | 11595 | 14.97 | 31.07 | 53.96 | 0.13 | -0.58 | 0.0 | 6.85 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_no_stop | 1135 | 11595 | 17.89 | 27.58 | 54.54 | 0.22 | -0.66 | 0.0 | 7.02 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_ma20_ema23_4d_stop | 1055 | 11595 | 11.75 | 32.61 | 55.64 | 0.0 | -0.67 | 4.83 | 6.87 | not_candidate_metric |
| strong_revenue_range23_width_le10 | d15_close_ma20_ema23_4d_stop | 1024 | 11595 | 14.75 | 30.96 | 54.3 | 0.23 | -0.59 | 9.18 | 6.82 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_ma20_ema23_4d_stop | 1015 | 11595 | 17.54 | 26.7 | 55.76 | 0.24 | -0.83 | 13.4 | 7.03 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_no_stop | 2448 | 16137 | 19.36 | 25.0 | 55.64 | 0.64 | -0.75 | 0.0 | 14.34 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_no_stop | 2366 | 16137 | 24.85 | 21.47 | 53.68 | 1.7 | -0.62 | 0.0 | 14.1 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_no_stop | 2322 | 16137 | 27.65 | 19.08 | 53.27 | 2.57 | -0.62 | 0.0 | 14.37 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_ma20_ema23_4d_stop | 2310 | 16137 | 19.65 | 25.02 | 55.32 | 0.7 | -0.72 | 3.33 | 15.04 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_ma20_ema23_4d_stop | 2222 | 16137 | 25.16 | 21.11 | 53.74 | 1.81 | -0.63 | 7.83 | 14.79 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_ma20_ema23_4d_stop | 2179 | 16137 | 27.86 | 18.72 | 53.42 | 2.7 | -0.66 | 11.47 | 15.1 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_no_stop | 4832 | 63517 | 22.02 | 24.23 | 53.75 | 0.97 | -0.68 | 0.0 | 28.31 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_no_stop | 4593 | 63517 | 26.28 | 21.75 | 51.97 | 1.91 | -0.45 | 0.0 | 27.37 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_no_stop | 4450 | 63517 | 28.88 | 18.61 | 52.52 | 2.58 | -0.61 | 0.0 | 27.54 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_ma20_ema23_4d_stop | 4461 | 63517 | 21.05 | 23.81 | 55.14 | 0.9 | -0.89 | 17.37 | 29.05 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_ma20_ema23_4d_stop | 4169 | 63517 | 24.61 | 20.89 | 54.5 | 1.68 | -0.93 | 23.46 | 27.75 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_ma20_ema23_4d_stop | 4077 | 63517 | 26.51 | 18.0 | 55.48 | 2.37 | -1.23 | 28.82 | 28.25 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_no_stop | 3655 | 23576 | 23.64 | 21.94 | 54.42 | 1.03 | -0.83 | 0.0 | 21.41 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_no_stop | 3488 | 23576 | 27.84 | 19.18 | 52.98 | 2.35 | -0.65 | 0.0 | 20.79 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_no_stop | 3431 | 23576 | 30.2 | 16.93 | 52.87 | 3.06 | -0.7 | 0.0 | 21.23 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_ma20_ema23_4d_stop | 3637 | 23576 | 23.7 | 21.78 | 54.52 | 1.0 | -0.84 | 5.55 | 23.69 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_ma20_ema23_4d_stop | 3479 | 23576 | 27.57 | 18.88 | 53.55 | 2.2 | -0.79 | 11.47 | 23.16 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_ma20_ema23_4d_stop | 3414 | 23576 | 29.38 | 16.55 | 54.07 | 2.9 | -0.99 | 16.81 | 23.66 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d10_close_no_stop | 846 | 7471 | 26.12 | 24.82 | 49.05 | 1.78 | 0.17 | 0.0 | 4.96 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_no_stop | 709 | 7471 | 32.72 | 21.86 | 45.42 | 2.87 | 0.64 | 0.0 | 4.23 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_no_stop | 607 | 7471 | 38.06 | 19.11 | 42.83 | 3.6 | 1.65 | 0.0 | 3.76 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d10_close_ma20_ema23_4d_stop | 832 | 7471 | 25.36 | 25.0 | 49.64 | 1.67 | 0.0 | 18.51 | 5.42 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d15_close_ma20_ema23_4d_stop | 678 | 7471 | 30.97 | 22.27 | 46.76 | 2.51 | 0.34 | 24.34 | 4.51 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_ma20_ema23_4d_stop | 586 | 7471 | 34.98 | 18.43 | 46.59 | 3.08 | 0.76 | 30.2 | 4.06 | not_candidate_metric |
| latest_yoy_improving_2m | d10_close_no_stop | 4200 | 54124 | 18.93 | 25.26 | 55.81 | 0.76 | -0.74 | 0.0 | 24.61 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_no_stop | 3942 | 54124 | 22.5 | 24.07 | 53.42 | 1.38 | -0.56 | 0.0 | 23.49 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_no_stop | 3616 | 54124 | 26.36 | 22.15 | 51.49 | 2.26 | -0.37 | 0.0 | 22.38 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 3948 | 54124 | 18.24 | 24.87 | 56.89 | 0.66 | -0.86 | 12.77 | 25.71 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 3387 | 54124 | 21.14 | 23.18 | 55.68 | 1.04 | -0.83 | 17.48 | 22.55 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 3376 | 54124 | 24.5 | 21.06 | 54.44 | 1.97 | -0.8 | 22.51 | 23.4 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_no_stop | 5326 | 72211 | 18.81 | 26.42 | 54.77 | 0.85 | -0.63 | 0.0 | 31.2 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_no_stop | 4897 | 72211 | 22.89 | 25.12 | 51.99 | 1.6 | -0.36 | 0.0 | 29.18 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_no_stop | 4566 | 72211 | 26.98 | 22.54 | 50.48 | 2.44 | -0.18 | 0.0 | 28.26 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 4837 | 72211 | 18.44 | 26.4 | 55.16 | 0.86 | -0.68 | 12.86 | 31.5 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 4118 | 72211 | 21.76 | 24.82 | 53.42 | 1.44 | -0.51 | 16.8 | 27.41 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 4088 | 72211 | 25.49 | 21.67 | 52.84 | 2.29 | -0.59 | 21.92 | 28.33 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_no_stop | 3006 | 37102 | 14.27 | 25.08 | 60.65 | -0.2 | -1.21 | 0.0 | 17.61 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_no_stop | 2783 | 37102 | 18.76 | 25.12 | 56.13 | 0.79 | -0.9 | 0.0 | 16.59 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_no_stop | 2627 | 37102 | 21.96 | 21.7 | 56.34 | 1.03 | -1.07 | 0.0 | 16.26 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_ma20_ema23_4d_stop | 2841 | 37102 | 13.9 | 24.85 | 61.25 | -0.14 | -1.21 | 10.67 | 18.5 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_ma20_ema23_4d_stop | 2469 | 37102 | 17.86 | 24.26 | 57.88 | 0.63 | -1.07 | 14.54 | 16.43 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_ma20_ema23_4d_stop | 2467 | 37102 | 20.43 | 21.24 | 58.33 | 1.0 | -1.38 | 19.42 | 17.1 | average_positive_but_median_not_confirmed |
