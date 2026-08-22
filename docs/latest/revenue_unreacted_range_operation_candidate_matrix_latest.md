# Revenue Unreacted Range Operation Candidate Matrix

- generated_at: `2026-08-23 07:25:15 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.
- entry_basis: signal-date close condition, next trading day open entry.
- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.
- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| condition_test_id | exit_rule_id | accepted_trade_count | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | stop_trigger_rate_pct | accepted_trade_share_of_baseline_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_context_ready | d10_close_no_stop | 20483 | 350726 | 18.53 | 27.0 | 54.47 | 0.54 | -0.6 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_no_stop | 20005 | 350726 | 21.53 | 24.56 | 53.9 | 0.85 | -0.63 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_no_stop | 19620 | 350726 | 23.69 | 21.87 | 54.45 | 1.33 | -0.79 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d10_close_ma20_ema23_4d_stop | 18683 | 350726 | 18.04 | 26.76 | 55.19 | 0.56 | -0.68 | 16.22 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_ma20_ema23_4d_stop | 18201 | 350726 | 19.89 | 23.26 | 56.84 | 0.65 | -0.99 | 22.08 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_ma20_ema23_4d_stop | 17758 | 350726 | 21.27 | 20.19 | 58.54 | 1.03 | -1.38 | 26.43 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_no_stop | 6262 | 95352 | 22.45 | 22.4 | 55.14 | 0.68 | -0.84 | 0.0 | 30.57 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_no_stop | 6172 | 95352 | 26.65 | 21.19 | 52.15 | 1.59 | -0.53 | 0.0 | 30.85 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_no_stop | 6045 | 95352 | 28.19 | 18.69 | 53.12 | 2.02 | -0.77 | 0.0 | 30.81 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_ma20_ema23_4d_stop | 5791 | 95352 | 21.41 | 22.36 | 56.23 | 0.53 | -0.97 | 19.86 | 31.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_ma20_ema23_4d_stop | 5686 | 95352 | 23.65 | 20.37 | 55.98 | 1.02 | -1.17 | 26.38 | 31.24 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_ma20_ema23_4d_stop | 5546 | 95352 | 24.86 | 17.36 | 57.77 | 1.54 | -1.72 | 31.32 | 31.23 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_no_stop | 3245 | 46034 | 23.88 | 20.28 | 55.84 | 0.56 | -1.02 | 0.0 | 15.84 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_no_stop | 3217 | 46034 | 28.47 | 19.02 | 52.5 | 1.8 | -0.7 | 0.0 | 16.08 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_no_stop | 3158 | 46034 | 28.66 | 16.85 | 54.5 | 1.87 | -1.2 | 0.0 | 16.1 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_ma20_ema23_4d_stop | 3047 | 46034 | 22.51 | 19.82 | 57.66 | 0.33 | -1.27 | 21.3 | 16.31 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_ma20_ema23_4d_stop | 3007 | 46034 | 24.71 | 18.19 | 57.1 | 1.01 | -1.53 | 27.87 | 16.52 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_ma20_ema23_4d_stop | 2941 | 46034 | 25.37 | 15.03 | 59.61 | 1.31 | -2.44 | 33.12 | 16.56 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_no_stop | 1934 | 27427 | 23.99 | 19.18 | 56.83 | 0.68 | -1.19 | 0.0 | 9.44 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_no_stop | 1918 | 27427 | 29.09 | 17.52 | 53.39 | 1.95 | -0.91 | 0.0 | 9.59 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_no_stop | 1881 | 27427 | 29.13 | 15.36 | 55.5 | 2.05 | -1.37 | 0.0 | 9.59 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_ma20_ema23_4d_stop | 1834 | 27427 | 22.68 | 19.03 | 58.29 | 0.54 | -1.42 | 22.19 | 9.82 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_ma20_ema23_4d_stop | 1811 | 27427 | 25.51 | 16.51 | 57.98 | 1.23 | -1.82 | 28.82 | 9.95 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_ma20_ema23_4d_stop | 1776 | 27427 | 25.73 | 13.85 | 60.42 | 1.66 | -2.56 | 34.91 | 10.0 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_no_stop | 3745 | 49643 | 16.61 | 26.38 | 57.01 | 0.01 | -0.86 | 0.0 | 18.28 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_no_stop | 3702 | 49643 | 20.83 | 26.2 | 52.97 | 0.75 | -0.56 | 0.0 | 18.51 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_no_stop | 3663 | 49643 | 24.22 | 22.71 | 53.07 | 1.45 | -0.6 | 0.0 | 18.67 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_ma20_ema23_4d_stop | 3401 | 49643 | 16.41 | 25.85 | 57.75 | -0.01 | -0.91 | 12.08 | 18.2 | not_candidate_metric |
| strong_revenue_range23_width_le20 | d15_close_ma20_ema23_4d_stop | 3355 | 49643 | 19.17 | 25.54 | 55.29 | 0.47 | -0.85 | 17.82 | 18.43 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_ma20_ema23_4d_stop | 3312 | 49643 | 22.13 | 21.04 | 56.82 | 1.02 | -1.17 | 22.22 | 18.65 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_no_stop | 2722 | 32880 | 14.29 | 29.83 | 55.88 | 0.02 | -0.73 | 0.0 | 13.29 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_no_stop | 2699 | 32880 | 19.38 | 27.2 | 53.43 | 0.74 | -0.49 | 0.0 | 13.49 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_no_stop | 2660 | 32880 | 22.59 | 23.91 | 53.5 | 1.14 | -0.52 | 0.0 | 13.56 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_ma20_ema23_4d_stop | 2482 | 32880 | 14.14 | 30.02 | 55.84 | 0.05 | -0.76 | 8.54 | 13.28 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_ma20_ema23_4d_stop | 2458 | 32880 | 18.31 | 27.05 | 54.64 | 0.68 | -0.63 | 13.59 | 13.5 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_ma20_ema23_4d_stop | 2416 | 32880 | 21.4 | 23.1 | 55.5 | 0.98 | -0.87 | 17.59 | 13.61 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_no_stop | 1363 | 13918 | 10.64 | 32.21 | 57.15 | -0.08 | -0.67 | 0.0 | 6.65 | not_candidate_metric |
| strong_revenue_range23_width_le10 | d15_close_no_stop | 1352 | 13918 | 14.94 | 31.36 | 53.7 | 0.16 | -0.5 | 0.0 | 6.76 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_no_stop | 1328 | 13918 | 16.64 | 28.54 | 54.82 | 0.19 | -0.68 | 0.0 | 6.77 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_ma20_ema23_4d_stop | 1255 | 13918 | 11.0 | 32.43 | 56.57 | 0.04 | -0.64 | 4.86 | 6.72 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d15_close_ma20_ema23_4d_stop | 1244 | 13918 | 14.63 | 31.19 | 54.18 | 0.2 | -0.56 | 8.68 | 6.83 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_ma20_ema23_4d_stop | 1218 | 13918 | 15.76 | 28.49 | 55.75 | 0.14 | -0.83 | 12.64 | 6.86 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_no_stop | 2821 | 19300 | 18.96 | 24.42 | 56.61 | 0.46 | -0.83 | 0.0 | 13.77 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_no_stop | 2777 | 19300 | 23.66 | 21.82 | 54.52 | 1.36 | -0.7 | 0.0 | 13.88 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_no_stop | 2747 | 19300 | 26.54 | 19.73 | 53.73 | 2.09 | -0.67 | 0.0 | 14.0 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_ma20_ema23_4d_stop | 2667 | 19300 | 19.39 | 24.07 | 56.54 | 0.5 | -0.84 | 3.34 | 14.28 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_ma20_ema23_4d_stop | 2623 | 19300 | 23.56 | 21.31 | 55.13 | 1.36 | -0.81 | 8.5 | 14.41 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_ma20_ema23_4d_stop | 2586 | 19300 | 26.22 | 19.26 | 54.52 | 2.09 | -0.91 | 12.3 | 14.56 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_no_stop | 5861 | 81192 | 21.89 | 23.0 | 55.11 | 0.6 | -0.86 | 0.0 | 28.61 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_no_stop | 5781 | 81192 | 25.51 | 21.5 | 52.98 | 1.28 | -0.66 | 0.0 | 28.9 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_no_stop | 5650 | 81192 | 27.01 | 19.35 | 53.65 | 1.64 | -0.87 | 0.0 | 28.8 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_ma20_ema23_4d_stop | 5475 | 81192 | 20.33 | 23.07 | 56.6 | 0.43 | -1.03 | 21.28 | 29.3 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_ma20_ema23_4d_stop | 5375 | 81192 | 22.23 | 20.84 | 56.93 | 0.74 | -1.34 | 28.37 | 29.53 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_ma20_ema23_4d_stop | 5235 | 81192 | 23.0 | 18.15 | 58.85 | 1.05 | -1.94 | 33.28 | 29.48 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_no_stop | 4295 | 28298 | 22.03 | 22.17 | 55.81 | 0.56 | -0.97 | 0.0 | 20.97 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_no_stop | 4179 | 28298 | 26.11 | 18.78 | 55.11 | 1.41 | -1.03 | 0.0 | 20.89 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_no_stop | 4150 | 28298 | 27.73 | 16.75 | 55.52 | 1.71 | -1.3 | 0.0 | 21.15 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_ma20_ema23_4d_stop | 4271 | 28298 | 21.96 | 22.01 | 56.03 | 0.52 | -1.02 | 6.67 | 22.86 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_ma20_ema23_4d_stop | 4178 | 28298 | 25.8 | 18.53 | 55.67 | 1.35 | -1.15 | 13.64 | 22.95 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_ma20_ema23_4d_stop | 4134 | 28298 | 26.83 | 16.23 | 56.94 | 1.73 | -1.68 | 19.38 | 23.28 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d10_close_no_stop | 1499 | 14412 | 24.35 | 22.41 | 53.24 | 0.32 | -0.56 | 0.0 | 7.32 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d15_close_no_stop | 1412 | 14412 | 27.69 | 19.9 | 52.41 | 0.33 | -0.57 | 0.0 | 7.06 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d20_close_no_stop | 1282 | 14412 | 28.39 | 16.85 | 54.76 | -0.55 | -1.31 | 0.0 | 6.53 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d10_close_ma20_ema23_4d_stop | 1492 | 14412 | 22.25 | 22.52 | 55.23 | 0.1 | -0.81 | 26.07 | 7.99 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d15_close_ma20_ema23_4d_stop | 1398 | 14412 | 22.68 | 19.81 | 57.51 | -0.49 | -1.55 | 34.55 | 7.68 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_ma20_ema23_4d_stop | 1264 | 14412 | 23.58 | 16.69 | 59.73 | -0.63 | -2.47 | 40.19 | 7.12 | not_candidate_metric |
| latest_yoy_improving_2m | d10_close_no_stop | 4834 | 67886 | 18.1 | 24.99 | 56.91 | 0.34 | -0.9 | 0.0 | 23.6 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_no_stop | 4817 | 67886 | 22.44 | 23.96 | 53.6 | 1.06 | -0.58 | 0.0 | 24.08 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_no_stop | 4767 | 67886 | 25.05 | 21.84 | 53.12 | 1.49 | -0.59 | 0.0 | 24.3 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 4598 | 67886 | 17.25 | 24.68 | 58.07 | 0.22 | -1.0 | 16.86 | 24.61 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 4575 | 67886 | 19.91 | 22.86 | 57.22 | 0.52 | -1.01 | 22.23 | 25.14 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 4516 | 67886 | 21.68 | 20.68 | 57.64 | 1.0 | -1.25 | 26.95 | 25.43 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_no_stop | 6379 | 95217 | 18.2 | 25.16 | 56.64 | 0.41 | -0.83 | 0.0 | 31.14 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_no_stop | 6338 | 95217 | 22.31 | 25.01 | 52.68 | 1.18 | -0.44 | 0.0 | 31.68 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_no_stop | 6252 | 95217 | 24.98 | 22.62 | 52.4 | 1.5 | -0.48 | 0.0 | 31.87 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 5895 | 95217 | 17.44 | 25.22 | 57.34 | 0.34 | -0.87 | 17.56 | 31.55 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 5838 | 95217 | 19.7 | 24.17 | 56.13 | 0.6 | -0.92 | 22.49 | 32.08 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 5736 | 95217 | 21.69 | 21.43 | 56.89 | 1.05 | -1.16 | 26.92 | 32.3 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_no_stop | 3272 | 43995 | 13.94 | 25.18 | 60.88 | -0.35 | -1.23 | 0.0 | 15.97 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_no_stop | 3270 | 43995 | 17.58 | 25.14 | 57.28 | 0.37 | -1.01 | 0.0 | 16.35 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_no_stop | 3258 | 43995 | 20.81 | 21.79 | 57.4 | 0.53 | -1.23 | 0.0 | 16.61 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_ma20_ema23_4d_stop | 3113 | 43995 | 13.49 | 25.47 | 61.03 | -0.24 | -1.19 | 12.62 | 16.66 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_ma20_ema23_4d_stop | 3109 | 43995 | 16.37 | 24.8 | 58.83 | 0.25 | -1.2 | 17.21 | 17.08 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_ma20_ema23_4d_stop | 3096 | 43995 | 18.38 | 21.25 | 60.37 | 0.37 | -1.58 | 22.58 | 17.43 | average_positive_but_median_not_confirmed |
