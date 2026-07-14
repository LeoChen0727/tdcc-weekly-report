# Revenue Unreacted Range Operation Candidate Matrix

- generated_at: `2026-07-14 14:45:45 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.
- entry_basis: signal-date close condition, next trading day open entry.
- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.
- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| condition_test_id | exit_rule_id | accepted_trade_count | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | stop_trigger_rate_pct | accepted_trade_share_of_baseline_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_context_ready | d10_close_no_stop | 17107 | 294291 | 17.83 | 28.03 | 54.14 | 0.67 | -0.53 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_no_stop | 16863 | 294291 | 22.27 | 25.16 | 52.57 | 1.43 | -0.44 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_no_stop | 16217 | 294291 | 25.43 | 22.76 | 51.81 | 1.98 | -0.36 | 0.0 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d10_close_ma20_ema23_4d_stop | 15386 | 294291 | 17.35 | 27.88 | 54.77 | 0.73 | -0.6 | 13.98 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d15_close_ma20_ema23_4d_stop | 15098 | 294291 | 21.14 | 24.29 | 54.57 | 1.32 | -0.69 | 18.77 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_context_ready | d20_close_ma20_ema23_4d_stop | 14480 | 294291 | 23.45 | 22.04 | 54.51 | 1.8 | -0.77 | 23.61 | 100.0 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_no_stop | 5196 | 76145 | 22.38 | 23.73 | 53.89 | 1.01 | -0.71 | 0.0 | 30.37 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_no_stop | 5068 | 76145 | 27.19 | 21.69 | 51.12 | 2.13 | -0.34 | 0.0 | 30.05 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_no_stop | 4762 | 76145 | 29.97 | 18.75 | 51.28 | 2.94 | -0.35 | 0.0 | 29.36 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d10_close_ma20_ema23_4d_stop | 4743 | 76145 | 21.61 | 23.57 | 54.82 | 0.98 | -0.85 | 15.83 | 30.83 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d15_close_ma20_ema23_4d_stop | 4482 | 76145 | 25.99 | 20.75 | 53.26 | 1.98 | -0.75 | 21.64 | 29.69 | average_positive_but_median_not_confirmed |
| revenue_production_strong | d20_close_ma20_ema23_4d_stop | 4313 | 76145 | 27.85 | 18.13 | 54.02 | 2.77 | -1.01 | 26.96 | 29.79 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_no_stop | 2721 | 36501 | 23.56 | 21.13 | 55.31 | 0.97 | -0.94 | 0.0 | 15.91 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_no_stop | 2638 | 36501 | 28.54 | 19.9 | 51.55 | 2.41 | -0.49 | 0.0 | 15.64 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_no_stop | 2437 | 36501 | 30.82 | 16.33 | 52.85 | 3.07 | -0.77 | 0.0 | 15.03 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d10_close_ma20_ema23_4d_stop | 2527 | 36501 | 22.91 | 20.74 | 56.35 | 0.9 | -1.08 | 16.5 | 16.42 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d15_close_ma20_ema23_4d_stop | 2345 | 36501 | 27.55 | 18.89 | 53.56 | 2.28 | -0.94 | 22.05 | 15.53 | average_positive_but_median_not_confirmed |
| latest30_and_cumulative20 | d20_close_ma20_ema23_4d_stop | 2247 | 36501 | 29.24 | 14.69 | 56.07 | 2.9 | -1.54 | 27.64 | 15.52 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_no_stop | 1615 | 21794 | 23.47 | 19.75 | 56.78 | 0.96 | -1.23 | 0.0 | 9.44 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_no_stop | 1558 | 21794 | 29.46 | 17.27 | 53.27 | 2.48 | -0.82 | 0.0 | 9.24 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_no_stop | 1443 | 21794 | 31.12 | 15.66 | 53.22 | 3.39 | -0.83 | 0.0 | 8.9 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d10_close_ma20_ema23_4d_stop | 1509 | 21794 | 22.93 | 19.48 | 57.59 | 0.97 | -1.35 | 17.83 | 9.81 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d15_close_ma20_ema23_4d_stop | 1399 | 21794 | 28.16 | 17.16 | 54.68 | 2.55 | -1.08 | 24.02 | 9.27 | average_positive_but_median_not_confirmed |
| latest50_and_cumulative30 | d20_close_ma20_ema23_4d_stop | 1338 | 21794 | 29.6 | 14.35 | 56.05 | 3.4 | -1.51 | 29.3 | 9.24 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_no_stop | 3208 | 41583 | 16.37 | 27.77 | 55.86 | 0.15 | -0.81 | 0.0 | 18.75 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_no_stop | 3166 | 41583 | 21.35 | 25.77 | 52.87 | 0.87 | -0.5 | 0.0 | 18.77 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_no_stop | 3036 | 41583 | 24.37 | 22.23 | 53.39 | 1.61 | -0.64 | 0.0 | 18.72 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d10_close_ma20_ema23_4d_stop | 2872 | 41583 | 15.98 | 27.4 | 56.62 | 0.14 | -0.87 | 10.52 | 18.67 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d15_close_ma20_ema23_4d_stop | 2773 | 41583 | 20.63 | 25.1 | 54.27 | 0.78 | -0.73 | 16.3 | 18.37 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le20 | d20_close_ma20_ema23_4d_stop | 2701 | 41583 | 22.81 | 21.25 | 55.94 | 1.36 | -1.1 | 21.36 | 18.65 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_no_stop | 2368 | 27589 | 14.7 | 29.65 | 55.66 | 0.03 | -0.77 | 0.0 | 13.84 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_no_stop | 2334 | 27589 | 19.92 | 26.48 | 53.6 | 0.77 | -0.59 | 0.0 | 13.84 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_no_stop | 2254 | 27589 | 22.89 | 24.0 | 53.11 | 1.2 | -0.48 | 0.0 | 13.9 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d10_close_ma20_ema23_4d_stop | 2136 | 27589 | 14.65 | 29.4 | 55.95 | 0.08 | -0.78 | 8.01 | 13.88 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d15_close_ma20_ema23_4d_stop | 2066 | 27589 | 19.55 | 25.85 | 54.6 | 0.82 | -0.71 | 13.46 | 13.68 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le15 | d20_close_ma20_ema23_4d_stop | 2025 | 27589 | 22.27 | 22.77 | 54.96 | 1.2 | -0.85 | 17.73 | 13.98 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_no_stop | 1179 | 11629 | 11.79 | 32.23 | 55.98 | -0.05 | -0.69 | 0.0 | 6.89 | not_candidate_metric |
| strong_revenue_range23_width_le10 | d15_close_no_stop | 1164 | 11629 | 14.95 | 31.19 | 53.87 | 0.13 | -0.56 | 0.0 | 6.9 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_no_stop | 1135 | 11629 | 17.89 | 27.58 | 54.54 | 0.22 | -0.66 | 0.0 | 7.0 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d10_close_ma20_ema23_4d_stop | 1059 | 11629 | 11.8 | 32.58 | 55.62 | 0.01 | -0.67 | 4.82 | 6.88 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d15_close_ma20_ema23_4d_stop | 1030 | 11629 | 14.66 | 31.17 | 54.17 | 0.23 | -0.59 | 9.13 | 6.82 | average_positive_but_median_not_confirmed |
| strong_revenue_range23_width_le10 | d20_close_ma20_ema23_4d_stop | 1016 | 11629 | 17.52 | 26.77 | 55.71 | 0.24 | -0.83 | 13.39 | 7.02 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_no_stop | 2455 | 16203 | 19.35 | 24.97 | 55.68 | 0.63 | -0.75 | 0.0 | 14.35 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_no_stop | 2400 | 16203 | 24.67 | 21.62 | 53.71 | 1.66 | -0.62 | 0.0 | 14.23 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_no_stop | 2329 | 16203 | 27.61 | 19.11 | 53.28 | 2.55 | -0.62 | 0.0 | 14.36 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d10_close_ma20_ema23_4d_stop | 2317 | 16203 | 19.68 | 24.99 | 55.33 | 0.7 | -0.73 | 3.32 | 15.06 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d15_close_ma20_ema23_4d_stop | 2235 | 16203 | 25.19 | 21.16 | 53.65 | 1.81 | -0.63 | 7.79 | 14.8 | average_positive_but_median_not_confirmed |
| strong_revenue_near_range23_high | d20_close_ma20_ema23_4d_stop | 2191 | 16203 | 27.84 | 18.67 | 53.49 | 2.66 | -0.68 | 11.59 | 15.13 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_no_stop | 4847 | 64010 | 22.01 | 24.2 | 53.79 | 0.96 | -0.69 | 0.0 | 28.33 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_no_stop | 4725 | 64010 | 26.07 | 21.93 | 52.0 | 1.85 | -0.47 | 0.0 | 28.02 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_no_stop | 4468 | 64010 | 28.87 | 18.6 | 52.53 | 2.56 | -0.62 | 0.0 | 27.55 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d10_close_ma20_ema23_4d_stop | 4474 | 64010 | 20.99 | 23.78 | 55.23 | 0.88 | -0.9 | 17.32 | 29.08 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d15_close_ma20_ema23_4d_stop | 4237 | 64010 | 24.4 | 21.15 | 54.45 | 1.65 | -0.93 | 23.6 | 28.06 | average_positive_but_median_not_confirmed |
| strong_revenue_position120_le75 | d20_close_ma20_ema23_4d_stop | 4094 | 64010 | 26.45 | 17.98 | 55.57 | 2.35 | -1.24 | 28.97 | 28.27 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_no_stop | 3674 | 23719 | 23.57 | 21.88 | 54.55 | 1.0 | -0.84 | 0.0 | 21.48 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_no_stop | 3554 | 23719 | 27.6 | 19.27 | 53.12 | 2.3 | -0.67 | 0.0 | 21.08 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_no_stop | 3446 | 23719 | 30.15 | 16.98 | 52.87 | 3.06 | -0.69 | 0.0 | 21.25 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d10_close_ma20_ema23_4d_stop | 3655 | 23719 | 23.58 | 21.83 | 54.58 | 0.98 | -0.85 | 5.55 | 23.76 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d15_close_ma20_ema23_4d_stop | 3488 | 23719 | 27.49 | 18.98 | 53.53 | 2.19 | -0.79 | 11.55 | 23.1 | average_positive_but_median_not_confirmed |
| strong_revenue_above_ma20_ema23 | d20_close_ma20_ema23_4d_stop | 3431 | 23719 | 29.44 | 16.53 | 54.04 | 2.89 | -0.98 | 16.79 | 23.69 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d10_close_no_stop | 856 | 7684 | 26.05 | 24.53 | 49.42 | 1.72 | 0.06 | 0.0 | 5.0 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d15_close_no_stop | 758 | 7684 | 31.79 | 22.3 | 45.91 | 2.64 | 0.58 | 0.0 | 4.5 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_no_stop | 619 | 7684 | 37.96 | 19.06 | 42.97 | 3.59 | 1.61 | 0.0 | 3.82 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d10_close_ma20_ema23_4d_stop | 841 | 7684 | 25.21 | 24.85 | 49.94 | 1.62 | 0.0 | 18.55 | 5.47 | average_positive_but_median_not_confirmed |
| strong_revenue_tdcc_high_thresholds_up | d15_close_ma20_ema23_4d_stop | 704 | 7684 | 30.11 | 22.59 | 47.3 | 2.33 | 0.26 | 24.43 | 4.66 | not_candidate_metric |
| strong_revenue_tdcc_high_thresholds_up | d20_close_ma20_ema23_4d_stop | 602 | 7684 | 34.72 | 18.6 | 46.68 | 3.0 | 0.72 | 30.07 | 4.16 | not_candidate_metric |
| latest_yoy_improving_2m | d10_close_no_stop | 4213 | 54543 | 18.94 | 25.33 | 55.73 | 0.77 | -0.73 | 0.0 | 24.63 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_no_stop | 4106 | 54543 | 22.36 | 23.92 | 53.73 | 1.31 | -0.58 | 0.0 | 24.35 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_no_stop | 3619 | 54543 | 26.39 | 22.13 | 51.48 | 2.27 | -0.37 | 0.0 | 22.32 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 3961 | 54543 | 18.2 | 24.84 | 56.96 | 0.64 | -0.87 | 12.75 | 25.74 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 3702 | 54543 | 20.88 | 23.82 | 55.29 | 1.1 | -0.78 | 17.5 | 24.52 | average_positive_but_median_not_confirmed |
| latest_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 3378 | 54543 | 24.51 | 21.05 | 54.44 | 1.97 | -0.8 | 22.53 | 23.33 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_no_stop | 5343 | 72893 | 18.83 | 26.45 | 54.73 | 0.85 | -0.62 | 0.0 | 31.23 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_no_stop | 5176 | 72893 | 22.35 | 25.19 | 52.45 | 1.47 | -0.41 | 0.0 | 30.69 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_no_stop | 4571 | 72893 | 27.02 | 22.51 | 50.47 | 2.44 | -0.18 | 0.0 | 28.19 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d10_close_ma20_ema23_4d_stop | 4855 | 72893 | 18.41 | 26.39 | 55.2 | 0.84 | -0.7 | 12.83 | 31.55 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d15_close_ma20_ema23_4d_stop | 4425 | 72893 | 21.69 | 25.2 | 53.11 | 1.47 | -0.49 | 16.9 | 29.31 | average_positive_but_median_not_confirmed |
| cumulative_yoy_improving_2m | d20_close_ma20_ema23_4d_stop | 4096 | 72893 | 25.46 | 21.66 | 52.88 | 2.28 | -0.59 | 21.92 | 28.29 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_no_stop | 3008 | 37312 | 14.26 | 25.1 | 60.64 | -0.2 | -1.21 | 0.0 | 17.58 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_no_stop | 2960 | 37312 | 18.38 | 25.07 | 56.55 | 0.64 | -0.98 | 0.0 | 17.55 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_no_stop | 2628 | 37312 | 21.96 | 21.73 | 56.32 | 1.03 | -1.07 | 0.0 | 16.21 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d10_close_ma20_ema23_4d_stop | 2847 | 37312 | 13.91 | 24.87 | 61.22 | -0.15 | -1.21 | 10.64 | 18.5 | not_candidate_metric |
| turn_positive_and_cumulative_improving | d15_close_ma20_ema23_4d_stop | 2624 | 37312 | 17.72 | 24.81 | 57.47 | 0.68 | -1.04 | 14.67 | 17.38 | average_positive_but_median_not_confirmed |
| turn_positive_and_cumulative_improving | d20_close_ma20_ema23_4d_stop | 2468 | 37312 | 20.46 | 21.23 | 58.31 | 1.01 | -1.38 | 19.41 | 17.04 | average_positive_but_median_not_confirmed |
