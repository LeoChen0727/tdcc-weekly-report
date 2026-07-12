# Revenue Unreacted Range Operation Candidate Matrix

- generated_at: `2026-07-12 17:22:34 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.
- entry_basis: signal-date close condition, next trading day open entry.
- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.
- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| condition_test_id | exit_rule_id | accepted_trade_count | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | stop_trigger_rate_pct | accepted_trade_share_of_baseline_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_context_ready | d10_close_no_stop | 16755 | 285943 | 17.78 | 28.13 | 54.09 | 0.67 | -0.52 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_no_stop | 16449 | 285943 | 22.4 | 25.19 | 52.4 | 1.47 | -0.41 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_no_stop | 15857 | 285943 | 25.48 | 22.78 | 51.74 | 2.0 | -0.35 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d10_close_ma20_ema23_4d_stop | 15081 | 285943 | 17.32 | 27.95 | 54.73 | 0.74 | -0.59 | 14.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_ma20_ema23_4d_stop | 14719 | 285943 | 21.22 | 24.27 | 54.51 | 1.34 | -0.68 | 18.67 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_ma20_ema23_4d_stop | 14169 | 285943 | 23.55 | 22.0 | 54.45 | 1.82 | -0.76 | 23.4 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_no_stop | 4823 | 69245 | 22.35 | 24.03 | 53.62 | 1.03 | -0.66 | 0.0 | 28.79 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_no_stop | 4561 | 69245 | 27.76 | 21.46 | 50.78 | 2.32 | -0.27 | 0.0 | 27.73 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_no_stop | 4409 | 69245 | 30.62 | 18.73 | 50.65 | 3.15 | -0.22 | 0.0 | 27.8 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_ma20_ema23_4d_stop | 4406 | 69245 | 21.65 | 23.65 | 54.7 | 1.01 | -0.83 | 15.73 | 29.22 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_ma20_ema23_4d_stop | 4066 | 69245 | 26.54 | 20.46 | 53.0 | 2.12 | -0.69 | 20.95 | 27.62 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_ma20_ema23_4d_stop | 3993 | 69245 | 28.47 | 18.13 | 53.39 | 2.95 | -0.88 | 26.3 | 28.18 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_no_stop | 2393 | 31111 | 23.82 | 21.48 | 54.7 | 1.12 | -0.85 | 0.0 | 14.28 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_no_stop | 2218 | 31111 | 29.76 | 19.57 | 50.68 | 2.89 | -0.33 | 0.0 | 13.48 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_no_stop | 2138 | 31111 | 31.95 | 16.42 | 51.64 | 3.58 | -0.44 | 0.0 | 13.48 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_ma20_ema23_4d_stop | 2224 | 31111 | 23.25 | 20.95 | 55.8 | 1.08 | -0.99 | 15.96 | 14.75 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_ma20_ema23_4d_stop | 2006 | 31111 | 28.51 | 18.1 | 53.39 | 2.62 | -0.91 | 20.79 | 13.63 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_ma20_ema23_4d_stop | 1975 | 31111 | 30.28 | 14.53 | 55.19 | 3.31 | -1.32 | 26.68 | 13.94 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_no_stop | 1290 | 16567 | 23.95 | 20.08 | 55.97 | 1.23 | -1.12 | 0.0 | 7.7 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_no_stop | 1190 | 16567 | 31.6 | 16.39 | 52.02 | 3.38 | -0.5 | 0.0 | 7.23 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_no_stop | 1146 | 16567 | 32.98 | 16.14 | 50.87 | 4.4 | -0.25 | 0.0 | 7.23 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_ma20_ema23_4d_stop | 1212 | 16567 | 23.51 | 19.8 | 56.68 | 1.31 | -1.19 | 17.08 | 8.04 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_ma20_ema23_4d_stop | 1091 | 16567 | 29.97 | 15.77 | 54.26 | 3.24 | -0.96 | 21.91 | 7.41 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_ma20_ema23_4d_stop | 1071 | 16567 | 31.47 | 14.47 | 54.06 | 4.28 | -1.05 | 28.01 | 7.56 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_no_stop | 2976 | 37816 | 16.23 | 28.02 | 55.75 | 0.19 | -0.77 | 0.0 | 17.76 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_no_stop | 2875 | 37816 | 21.7 | 25.81 | 52.49 | 1.0 | -0.43 | 0.0 | 17.48 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_no_stop | 2809 | 37816 | 24.53 | 22.64 | 52.83 | 1.76 | -0.53 | 0.0 | 17.71 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_ma20_ema23_4d_stop | 2665 | 37816 | 16.02 | 27.69 | 56.29 | 0.22 | -0.81 | 10.28 | 17.67 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_ma20_ema23_4d_stop | 2529 | 37816 | 20.96 | 25.27 | 53.78 | 0.89 | -0.64 | 16.21 | 17.18 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_ma20_ema23_4d_stop | 2496 | 37816 | 22.96 | 21.51 | 55.53 | 1.49 | -1.01 | 20.91 | 17.62 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_no_stop | 2190 | 25073 | 14.79 | 30.09 | 55.11 | 0.1 | -0.66 | 0.0 | 13.07 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_no_stop | 2115 | 25073 | 20.24 | 26.62 | 53.14 | 0.87 | -0.46 | 0.0 | 12.86 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_no_stop | 2079 | 25073 | 22.99 | 24.63 | 52.38 | 1.33 | -0.38 | 0.0 | 13.11 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_ma20_ema23_4d_stop | 1965 | 25073 | 14.71 | 29.87 | 55.42 | 0.14 | -0.71 | 7.63 | 13.03 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_ma20_ema23_4d_stop | 1878 | 25073 | 19.7 | 25.99 | 54.31 | 0.89 | -0.66 | 13.1 | 12.76 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_ma20_ema23_4d_stop | 1861 | 25073 | 22.41 | 23.37 | 54.22 | 1.31 | -0.76 | 17.09 | 13.13 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_no_stop | 1088 | 10720 | 11.49 | 33.09 | 55.42 | -0.04 | -0.6 | 0.0 | 6.49 | not_candidate_metric |
| strong_revenue_range23_width_le10 | d15_close_no_stop | 1057 | 10720 | 14.76 | 31.79 | 53.45 | 0.18 | -0.46 | 0.0 | 6.43 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_no_stop | 1045 | 10720 | 18.18 | 27.85 | 53.97 | 0.3 | -0.56 | 0.0 | 6.59 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_ma20_ema23_4d_stop | 974 | 10720 | 11.7 | 33.37 | 54.93 | 0.05 | -0.58 | 4.41 | 6.46 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d15_close_ma20_ema23_4d_stop | 941 | 10720 | 14.67 | 31.56 | 53.77 | 0.27 | -0.46 | 8.5 | 6.39 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_ma20_ema23_4d_stop | 934 | 10720 | 17.88 | 26.87 | 55.25 | 0.29 | -0.75 | 12.21 | 6.59 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_no_stop | 2290 | 14975 | 19.21 | 25.28 | 55.5 | 0.65 | -0.73 | 0.0 | 13.67 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_no_stop | 2213 | 14975 | 25.03 | 21.28 | 53.68 | 1.78 | -0.58 | 0.0 | 13.45 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_no_stop | 2176 | 14975 | 27.85 | 19.12 | 53.03 | 2.67 | -0.56 | 0.0 | 13.72 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_ma20_ema23_4d_stop | 2163 | 14975 | 19.56 | 25.24 | 55.2 | 0.71 | -0.72 | 3.51 | 14.34 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_ma20_ema23_4d_stop | 2081 | 14975 | 25.32 | 20.9 | 53.77 | 1.88 | -0.63 | 7.98 | 14.14 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_ma20_ema23_4d_stop | 2046 | 14975 | 28.1 | 18.62 | 53.27 | 2.8 | -0.63 | 11.63 | 14.44 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_no_stop | 4487 | 57956 | 21.97 | 24.23 | 53.8 | 1.0 | -0.67 | 0.0 | 26.78 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_no_stop | 4250 | 57956 | 26.61 | 21.55 | 51.84 | 2.04 | -0.42 | 0.0 | 25.84 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_no_stop | 4121 | 57956 | 29.41 | 18.66 | 51.93 | 2.78 | -0.46 | 0.0 | 25.99 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_ma20_ema23_4d_stop | 4143 | 57956 | 21.07 | 23.68 | 55.25 | 0.95 | -0.88 | 17.11 | 27.47 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_ma20_ema23_4d_stop | 3848 | 57956 | 25.0 | 20.79 | 54.21 | 1.8 | -0.88 | 22.79 | 26.14 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_ma20_ema23_4d_stop | 3777 | 57956 | 27.01 | 17.98 | 55.02 | 2.53 | -1.13 | 28.33 | 26.66 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_no_stop | 3412 | 21854 | 23.62 | 22.22 | 54.16 | 1.07 | -0.82 | 0.0 | 20.36 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_no_stop | 3253 | 21854 | 28.31 | 19.15 | 52.54 | 2.53 | -0.57 | 0.0 | 19.78 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_no_stop | 3205 | 21854 | 30.8 | 16.72 | 52.48 | 3.29 | -0.63 | 0.0 | 20.21 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_ma20_ema23_4d_stop | 3397 | 21854 | 23.67 | 22.11 | 54.22 | 1.05 | -0.83 | 5.42 | 22.53 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_ma20_ema23_4d_stop | 3246 | 21854 | 28.03 | 18.85 | 53.11 | 2.37 | -0.68 | 11.24 | 22.05 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_ma20_ema23_4d_stop | 3191 | 21854 | 29.96 | 16.33 | 53.71 | 3.1 | -0.9 | 16.58 | 22.52 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d10_close_no_stop | 758 | 6503 | 26.12 | 25.73 | 48.15 | 2.01 | 0.37 | 0.0 | 4.52 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_no_stop | 624 | 6503 | 33.81 | 21.79 | 44.39 | 3.16 | 0.97 | 0.0 | 3.79 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_no_stop | 532 | 6503 | 38.72 | 19.17 | 42.11 | 3.73 | 1.71 | 0.0 | 3.35 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d10_close_ma20_ema23_4d_stop | 746 | 6503 | 25.07 | 26.14 | 48.79 | 1.85 | 0.06 | 18.23 | 4.95 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_ma20_ema23_4d_stop | 595 | 6503 | 31.93 | 22.52 | 45.55 | 2.81 | 0.5 | 23.36 | 4.04 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_ma20_ema23_4d_stop | 511 | 6503 | 35.23 | 19.37 | 45.4 | 3.41 | 1.08 | 29.35 | 3.61 | not_candidate_metric |
| latest_yoy_improving_2m | d10_close_no_stop | 4031 | 51947 | 19.1 | 25.5 | 55.4 | 0.83 | -0.69 | 0.0 | 24.06 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_no_stop | 3780 | 51947 | 22.35 | 24.34 | 53.31 | 1.42 | -0.53 | 0.0 | 22.98 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_no_stop | 3461 | 51947 | 26.38 | 22.48 | 51.14 | 2.31 | -0.32 | 0.0 | 21.83 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 3796 | 51947 | 18.36 | 24.97 | 56.66 | 0.7 | -0.83 | 12.54 | 25.17 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 3246 | 51947 | 21.01 | 23.35 | 55.64 | 1.06 | -0.8 | 17.04 | 22.05 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 3236 | 51947 | 24.51 | 21.38 | 54.11 | 2.03 | -0.75 | 22.03 | 22.84 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_no_stop | 5121 | 69313 | 18.86 | 26.71 | 54.42 | 0.91 | -0.56 | 0.0 | 30.56 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_no_stop | 4709 | 69313 | 22.81 | 25.53 | 51.67 | 1.66 | -0.33 | 0.0 | 28.63 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_no_stop | 4385 | 69313 | 27.05 | 22.83 | 50.13 | 2.47 | -0.13 | 0.0 | 27.65 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 4656 | 69313 | 18.56 | 26.55 | 54.9 | 0.92 | -0.63 | 12.54 | 30.87 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 3953 | 69313 | 21.71 | 25.04 | 53.25 | 1.48 | -0.49 | 16.14 | 26.86 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 3927 | 69313 | 25.57 | 21.93 | 52.51 | 2.33 | -0.53 | 21.26 | 27.72 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_no_stop | 2917 | 35925 | 14.54 | 25.4 | 60.06 | -0.09 | -1.17 | 0.0 | 17.41 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_no_stop | 2701 | 35925 | 19.1 | 25.21 | 55.68 | 0.93 | -0.83 | 0.0 | 16.42 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_no_stop | 2551 | 35925 | 22.27 | 21.87 | 55.86 | 1.2 | -0.97 | 0.0 | 16.09 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_ma20_ema23_4d_stop | 2754 | 35925 | 14.16 | 25.16 | 60.68 | -0.03 | -1.18 | 10.68 | 18.26 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_ma20_ema23_4d_stop | 2395 | 35925 | 18.2 | 24.47 | 57.33 | 0.78 | -1.01 | 14.24 | 16.27 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_ma20_ema23_4d_stop | 2393 | 35925 | 20.69 | 21.48 | 57.84 | 1.16 | -1.3 | 19.18 | 16.89 | average_positive_but_median_not_confirmed |
