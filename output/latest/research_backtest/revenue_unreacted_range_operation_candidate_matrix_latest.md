# Revenue Unreacted Range Operation Candidate Matrix

- generated_at: `2026-07-11 16:08:09 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.
- entry_basis: signal-date close condition, next trading day open entry.
- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.
- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| condition_test_id | exit_rule_id | accepted_trade_count | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | stop_trigger_rate_pct | accepted_trade_share_of_baseline_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_context_ready | d10_close_no_stop | 18571 | 317134 | 18.71 | 29.08 | 52.21 | 0.93 | -0.34 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_no_stop | 18191 | 317134 | 21.76 | 25.31 | 52.93 | 1.34 | -0.47 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_no_stop | 17666 | 317134 | 25.44 | 22.87 | 51.69 | 1.99 | -0.37 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d10_close_ma20_ema23_4d_stop | 16596 | 317134 | 17.64 | 28.26 | 54.1 | 0.81 | -0.5 | 13.58 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_ma20_ema23_4d_stop | 16130 | 317134 | 20.66 | 24.92 | 54.42 | 1.28 | -0.62 | 18.09 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_ma20_ema23_4d_stop | 15679 | 317134 | 23.23 | 22.34 | 54.42 | 1.78 | -0.78 | 22.6 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_no_stop | 5370 | 77514 | 22.76 | 24.49 | 52.76 | 1.19 | -0.49 | 0.0 | 28.92 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_no_stop | 5102 | 77514 | 27.22 | 21.54 | 51.23 | 2.24 | -0.36 | 0.0 | 28.05 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_no_stop | 4954 | 77514 | 31.01 | 18.41 | 50.59 | 3.25 | -0.24 | 0.0 | 28.04 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_ma20_ema23_4d_stop | 4720 | 77514 | 21.14 | 23.62 | 55.23 | 0.95 | -0.86 | 15.47 | 28.44 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_ma20_ema23_4d_stop | 4372 | 77514 | 25.55 | 20.56 | 53.89 | 1.95 | -0.79 | 20.93 | 27.1 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_ma20_ema23_4d_stop | 4305 | 77514 | 28.06 | 17.51 | 54.43 | 2.82 | -1.05 | 26.04 | 27.46 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_no_stop | 2621 | 34477 | 24.23 | 21.82 | 53.95 | 1.17 | -0.74 | 0.0 | 14.11 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_no_stop | 2447 | 34477 | 29.3 | 20.31 | 50.39 | 2.83 | -0.27 | 0.0 | 13.45 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_no_stop | 2369 | 34477 | 32.67 | 17.05 | 50.27 | 3.81 | -0.15 | 0.0 | 13.41 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_ma20_ema23_4d_stop | 2305 | 34477 | 23.17 | 20.43 | 56.4 | 1.04 | -1.07 | 15.88 | 13.89 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_ma20_ema23_4d_stop | 2088 | 34477 | 27.59 | 18.49 | 53.93 | 2.46 | -1.02 | 21.02 | 12.94 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_ma20_ema23_4d_stop | 2059 | 34477 | 29.72 | 15.1 | 55.17 | 3.24 | -1.32 | 26.32 | 13.13 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_no_stop | 1406 | 18176 | 24.32 | 20.2 | 55.48 | 1.28 | -1.1 | 0.0 | 7.57 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_no_stop | 1306 | 18176 | 31.01 | 17.23 | 51.76 | 3.42 | -0.45 | 0.0 | 7.18 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_no_stop | 1263 | 18176 | 34.05 | 16.07 | 49.88 | 4.82 | 0.0 | 0.0 | 7.15 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_ma20_ema23_4d_stop | 1244 | 18176 | 23.23 | 19.05 | 57.72 | 1.19 | -1.33 | 17.04 | 7.5 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_ma20_ema23_4d_stop | 1124 | 18176 | 28.91 | 16.28 | 54.8 | 3.02 | -1.12 | 22.15 | 6.97 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_ma20_ema23_4d_stop | 1105 | 18176 | 30.86 | 14.66 | 54.48 | 4.15 | -1.18 | 27.69 | 7.05 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_no_stop | 2968 | 37592 | 16.44 | 28.17 | 55.39 | 0.28 | -0.7 | 0.0 | 15.98 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_no_stop | 2865 | 37592 | 21.4 | 26.35 | 52.25 | 0.99 | -0.43 | 0.0 | 15.75 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_no_stop | 2801 | 37592 | 24.24 | 22.63 | 53.12 | 1.66 | -0.62 | 0.0 | 15.86 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_ma20_ema23_4d_stop | 2925 | 37592 | 15.86 | 27.86 | 56.27 | 0.23 | -0.77 | 10.5 | 17.62 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_ma20_ema23_4d_stop | 2785 | 37592 | 20.22 | 25.82 | 53.97 | 0.84 | -0.65 | 16.16 | 17.27 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_ma20_ema23_4d_stop | 2755 | 37592 | 22.36 | 21.52 | 56.12 | 1.41 | -1.1 | 20.47 | 17.57 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_no_stop | 2178 | 24849 | 15.15 | 29.89 | 54.96 | 0.2 | -0.59 | 0.0 | 11.73 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_no_stop | 2102 | 24849 | 20.08 | 26.83 | 53.09 | 0.94 | -0.44 | 0.0 | 11.56 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_no_stop | 2067 | 24849 | 22.98 | 23.71 | 53.31 | 1.27 | -0.57 | 0.0 | 11.7 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_ma20_ema23_4d_stop | 2149 | 24849 | 14.66 | 29.6 | 55.75 | 0.16 | -0.72 | 7.96 | 12.95 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_ma20_ema23_4d_stop | 2060 | 24849 | 19.22 | 26.26 | 54.51 | 0.86 | -0.65 | 13.01 | 12.77 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_ma20_ema23_4d_stop | 2044 | 24849 | 22.16 | 22.65 | 55.19 | 1.18 | -0.82 | 16.73 | 13.04 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_no_stop | 1074 | 10564 | 11.64 | 33.61 | 54.75 | 0.09 | -0.52 | 0.0 | 5.78 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d15_close_no_stop | 1043 | 10564 | 14.67 | 32.02 | 53.31 | 0.3 | -0.43 | 0.0 | 5.73 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_no_stop | 1031 | 10564 | 18.04 | 27.06 | 54.9 | 0.31 | -0.66 | 0.0 | 5.84 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_ma20_ema23_4d_stop | 1063 | 10564 | 11.38 | 33.49 | 55.13 | 0.07 | -0.56 | 4.7 | 6.41 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d15_close_ma20_ema23_4d_stop | 1030 | 10564 | 14.56 | 31.46 | 53.98 | 0.34 | -0.46 | 8.64 | 6.39 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_ma20_ema23_4d_stop | 1023 | 10564 | 17.79 | 26.3 | 55.91 | 0.3 | -0.77 | 12.02 | 6.52 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_no_stop | 2581 | 17366 | 20.26 | 25.22 | 54.51 | 0.75 | -0.6 | 0.0 | 13.9 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_no_stop | 2504 | 17366 | 25.6 | 21.49 | 52.92 | 1.85 | -0.47 | 0.0 | 13.77 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_no_stop | 2466 | 17366 | 29.2 | 19.06 | 51.74 | 2.96 | -0.34 | 0.0 | 13.96 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_ma20_ema23_4d_stop | 2240 | 17366 | 19.51 | 24.96 | 55.54 | 0.64 | -0.76 | 3.57 | 13.5 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_ma20_ema23_4d_stop | 2157 | 17366 | 24.94 | 21.28 | 53.78 | 1.81 | -0.63 | 7.97 | 13.37 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_ma20_ema23_4d_stop | 2122 | 17366 | 27.47 | 18.94 | 53.58 | 2.65 | -0.66 | 11.5 | 13.53 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_no_stop | 4184 | 55206 | 21.94 | 24.28 | 53.78 | 1.05 | -0.66 | 0.0 | 22.53 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_no_stop | 3952 | 55206 | 25.76 | 21.31 | 52.94 | 1.84 | -0.65 | 0.0 | 21.73 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_no_stop | 3826 | 55206 | 28.88 | 18.61 | 52.51 | 2.69 | -0.63 | 0.0 | 21.66 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_ma20_ema23_4d_stop | 3814 | 55206 | 20.5 | 23.44 | 56.06 | 0.89 | -0.95 | 18.88 | 22.98 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_ma20_ema23_4d_stop | 3523 | 55206 | 23.84 | 20.64 | 55.52 | 1.54 | -1.04 | 24.69 | 21.84 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_ma20_ema23_4d_stop | 3457 | 55206 | 25.86 | 17.56 | 56.58 | 2.28 | -1.45 | 30.34 | 22.05 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_no_stop | 3412 | 21854 | 23.62 | 22.22 | 54.16 | 1.07 | -0.82 | 0.0 | 18.37 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_no_stop | 3253 | 21854 | 28.31 | 19.15 | 52.54 | 2.53 | -0.57 | 0.0 | 17.88 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_no_stop | 3205 | 21854 | 30.8 | 16.72 | 52.48 | 3.29 | -0.63 | 0.0 | 18.14 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_ma20_ema23_4d_stop | 3397 | 21854 | 23.67 | 22.11 | 54.22 | 1.05 | -0.83 | 5.42 | 20.47 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_ma20_ema23_4d_stop | 3246 | 21854 | 28.03 | 18.85 | 53.11 | 2.37 | -0.68 | 11.24 | 20.12 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_ma20_ema23_4d_stop | 3191 | 21854 | 29.96 | 16.33 | 53.71 | 3.1 | -0.9 | 16.58 | 20.35 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d10_close_no_stop | 763 | 6553 | 25.82 | 25.95 | 48.23 | 1.96 | 0.31 | 0.0 | 4.11 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_no_stop | 629 | 6553 | 33.7 | 21.62 | 44.67 | 3.12 | 0.93 | 0.0 | 3.46 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_no_stop | 536 | 6553 | 38.43 | 19.59 | 41.98 | 3.74 | 1.67 | 0.0 | 3.03 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d10_close_ma20_ema23_4d_stop | 748 | 6553 | 25.0 | 26.2 | 48.8 | 1.84 | 0.06 | 18.18 | 4.51 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_ma20_ema23_4d_stop | 597 | 6553 | 31.99 | 22.45 | 45.56 | 2.8 | 0.5 | 23.28 | 3.7 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_ma20_ema23_4d_stop | 513 | 6553 | 35.09 | 19.69 | 45.22 | 3.44 | 1.11 | 29.24 | 3.27 | not_candidate_metric |
| latest_yoy_improving_2m | d10_close_no_stop | 4432 | 57076 | 19.2 | 26.62 | 54.17 | 0.87 | -0.53 | 0.0 | 23.87 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_no_stop | 4180 | 57076 | 21.58 | 24.81 | 53.61 | 1.3 | -0.53 | 0.0 | 22.98 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_no_stop | 3859 | 57076 | 26.25 | 23.06 | 50.69 | 2.27 | -0.21 | 0.0 | 21.84 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 3889 | 57076 | 18.51 | 25.04 | 56.44 | 0.71 | -0.82 | 12.63 | 23.43 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 3337 | 57076 | 21.04 | 23.16 | 55.8 | 1.12 | -0.82 | 17.17 | 20.69 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 3327 | 57076 | 24.29 | 21.43 | 54.28 | 2.02 | -0.78 | 22.06 | 21.22 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_no_stop | 5767 | 78490 | 19.66 | 28.13 | 52.21 | 1.14 | -0.37 | 0.0 | 31.05 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_no_stop | 5354 | 78490 | 22.49 | 25.53 | 51.98 | 1.67 | -0.36 | 0.0 | 29.43 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_no_stop | 5031 | 78490 | 26.52 | 23.32 | 50.17 | 2.51 | -0.13 | 0.0 | 28.48 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 4964 | 78490 | 18.98 | 26.47 | 54.55 | 0.96 | -0.59 | 12.49 | 29.91 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 4260 | 78490 | 21.92 | 25.12 | 52.96 | 1.53 | -0.45 | 16.17 | 26.41 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 4235 | 78490 | 25.17 | 22.03 | 52.8 | 2.23 | -0.56 | 20.85 | 27.01 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_no_stop | 3100 | 38939 | 14.71 | 25.9 | 59.39 | -0.01 | -1.1 | 0.0 | 16.69 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_no_stop | 2882 | 38939 | 18.42 | 25.71 | 55.86 | 0.82 | -0.85 | 0.0 | 15.84 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_no_stop | 2731 | 38939 | 22.15 | 22.34 | 55.51 | 1.2 | -0.93 | 0.0 | 15.46 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_ma20_ema23_4d_stop | 2737 | 38939 | 14.03 | 25.14 | 60.83 | -0.05 | -1.19 | 10.74 | 16.49 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_ma20_ema23_4d_stop | 2377 | 38939 | 18.09 | 24.53 | 57.38 | 0.76 | -1.02 | 14.3 | 14.74 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_ma20_ema23_4d_stop | 2375 | 38939 | 20.63 | 21.56 | 57.81 | 1.16 | -1.29 | 19.28 | 15.15 | average_positive_but_median_not_confirmed |
