# Historical Pattern Operation Registry

- generated_at: `2026-06-14 06:34:59 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `158218`
- registry_rows: `85`
- registry_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/historical_pattern_operation_registry_latest.csv
- detail_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/history/research/historical_pattern_operation_events.csv

## Scope

- This is research/backtest output only.
- It does not write production config, daily candidate files, or PDF operation text.
- `approved_for_daily` remains `False` until a separate promotion PR explicitly approves a pattern.
- `limit_locked_volume_lt2_research_only` is a comparison group for locked limit-up behavior and is not a current production model hit.

## Current Model Hit Patterns

| event_filter_id | pattern_id | sample_size | win_rate | avg_return | median_return | max_drawdown | avg_holding_days | profit_factor | out_of_sample_size | out_of_sample_win_rate | out_of_sample_avg_return | confidence_status | out_of_sample_pass | approved_for_daily |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current_model_hit_all | next_open_hold_20d | 3497 | 46.84 | 5.2545 | -0.9864 | -91.7928 | 20.0 | 1.9682 | 1183 | 54.1 | 11.4975 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2299 | 52.37 | 3.5238 | 0.5445 | -89.805 | 10.0 | 2.2057 | 866 | 61.09 | 7.1666 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3317 | 50.26 | 3.1335 | 0.1016 | -91.3518 | 10.0 | 1.9397 | 1197 | 55.72 | 6.1436 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 2803 | 45.7 | 2.5871 | -1.0651 | -90.5777 | 10.0 | 1.5777 | 1097 | 48.22 | 4.7025 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 3702 | 44.76 | 2.0344 | -1.2157 | -90.8539 | 10.0 | 1.4533 | 1388 | 47.84 | 4.2564 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 3805 | 46.28 | 1.6709 | -0.7042 | -32.2188 | 5.0 | 1.4942 | 1491 | 47.28 | 2.351 | high | True | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 3497 | 34.06 | 1.5762 | -3.4483 | -90.5777 | 8.55 | 1.3292 | 1183 | 34.57 | 4.0044 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 3702 | 39.36 | 1.42 | -2.2798 | -32.0847 | 6.7 | 1.3731 | 1388 | 39.77 | 2.8877 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 3702 | 31.9 | 0.9661 | -3.2306 | -90.5777 | 6.41 | 1.2309 | 1388 | 31.27 | 1.9898 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 3497 | 33.54 | 0.9231 | -2.6087 | -23.9623 | 4.68 | 1.248 | 1183 | 33.47 | 2.7425 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 3702 | 26.39 | 0.686 | -5.0 | -19.9536 | 5.18 | 1.1914 | 1388 | 22.98 | 1.1125 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 3805 | 41.29 | 0.1242 | -1.675 | -34.6101 | 5.0 | 1.0312 | 1491 | 42.99 | 0.4727 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 3749 | 30.17 | 0.0677 | -0.6659 | -36.5617 | 3.56 | 1.0236 | 1435 | 28.29 | 0.0708 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 3805 | 33.9 | -0.0794 | -2.5048 | -26.1603 | 3.82 | 0.978 | 1491 | 33.53 | 0.0792 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 3774 | 31.4 | -0.1554 | -1.407 | -28.5714 | 3.67 | 0.9509 | 1460 | 30.0 | -0.1806 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 3497 | 39.38 | -0.1903 | -2.7304 | -90.5777 | 5.51 | 0.9523 | 1183 | 41.84 | -0.0002 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 3702 | 50.81 | -0.4995 | 2.2176 | -90.5777 | 3.1 | 0.8335 | 1388 | 52.16 | -0.5951 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 1652 | 47.34 | 5.7265 | -0.9153 | -91.7928 | 20.0 | 1.9754 | 622 | 54.18 | 10.9159 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1042 | 54.03 | 4.5424 | 1.2481 | -89.805 | 10.0 | 2.5411 | 449 | 63.03 | 7.8383 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 1546 | 51.75 | 3.7266 | 0.5868 | -91.3518 | 10.0 | 2.0631 | 622 | 56.91 | 6.3687 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 1819 | 49.04 | 2.3719 | -0.241 | -29.912 | 5.0 | 1.6667 | 789 | 48.04 | 2.5584 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 1616 | 44.18 | 2.3706 | -1.323 | -90.5777 | 10.0 | 1.4876 | 673 | 46.81 | 4.0408 | high | True | False |
| limit_up_like_current_hit | next_open_hold_10d | 1762 | 44.38 | 2.3611 | -1.3077 | -90.5777 | 10.0 | 1.4936 | 732 | 47.13 | 4.0613 | high | True | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 1652 | 34.5 | 1.4364 | -4.1715 | -90.5777 | 8.75 | 1.2632 | 622 | 33.76 | 3.2207 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 1762 | 37.57 | 1.3544 | -2.9942 | -32.0847 | 6.09 | 1.325 | 732 | 37.43 | 2.3979 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 1762 | 33.65 | 0.9275 | -4.1565 | -90.5777 | 6.96 | 1.185 | 732 | 32.1 | 1.5657 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 1762 | 23.33 | 0.7522 | -5.0 | -17.4028 | 4.54 | 1.1968 | 732 | 19.95 | 0.9657 | medium | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 1652 | 33.72 | 0.3967 | -3.1037 | -22.3799 | 4.73 | 1.0917 | 622 | 33.28 | 1.4627 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 1819 | 41.34 | 0.0007 | -2.0218 | -34.6101 | 5.0 | 1.0001 | 789 | 43.73 | 0.0343 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 1784 | 31.33 | -0.1533 | -1.1597 | -30.999 | 3.78 | 0.9561 | 754 | 28.38 | -0.4321 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 1652 | 45.46 | -0.1865 | -1.745 | -90.5777 | 5.67 | 0.9596 | 622 | 46.46 | -0.0799 | low | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 1819 | 35.35 | -0.2138 | -2.8311 | -26.1603 | 4.03 | 0.95 | 789 | 35.11 | -0.2542 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 1762 | 57.83 | -0.4614 | 5.0 | -90.5777 | 3.03 | 0.8615 | 732 | 58.47 | -0.5028 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 1801 | 32.76 | -0.4968 | -1.8868 | -28.5714 | 3.89 | 0.871 | 771 | 30.09 | -0.7496 | low | False | False |
| long_base_low_position | signal_close_hold_5d | 179 | 44.69 | 1.7086 | -0.8251 | -16.2076 | 5.0 | 1.7217 | 48 | 33.33 | 0.1312 | medium | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 154 | 46.1 | 1.5493 | -0.1245 | -22.2365 | 10.0 | 1.6211 | 36 | 58.33 | 1.6782 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 162 | 42.59 | 0.8187 | -2.23 | -22.3164 | 20.0 | 1.1891 | 31 | 45.16 | 2.1009 | medium | True | False |
| long_base_low_position | next_open_5ma_trailing_20d | 162 | 37.04 | 0.3001 | -2.0273 | -13.961 | 4.88 | 1.107 | 31 | 19.35 | -2.9653 | medium | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 176 | 38.07 | 0.2846 | 0.0 | -14.5788 | 3.86 | 1.1323 | 45 | 33.33 | -1.0487 | medium | False | False |
| long_base_low_position | next_open_hold_5d | 179 | 40.78 | 0.1767 | -1.3378 | -19.3503 | 5.0 | 1.0604 | 48 | 33.33 | -1.2808 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 106 | 49.06 | 1.2582 | -0.0993 | -15.8349 | 10.0 | 1.6254 | 27 | 66.67 | 2.4916 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 179 | 36.31 | 0.0878 | -1.8265 | -16.2076 | 3.93 | 1.0306 | 48 | 27.08 | -1.8904 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 162 | 38.27 | -0.0052 | -2.5717 | -16.3594 | 6.78 | 0.9985 | 31 | 32.26 | -0.7089 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 162 | 28.4 | -0.0282 | -2.7542 | -14.9306 | 8.07 | 0.9924 | 31 | 19.35 | -2.4607 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 173 | 31.79 | -0.0412 | -0.5865 | -15.5894 | 3.75 | 0.9804 | 42 | 21.43 | -1.3598 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 171 | 39.77 | -0.1142 | -2.3316 | -15.6297 | 6.97 | 0.9657 | 40 | 20.0 | -3.3456 | low | False | False |
| long_base_low_position | next_open_hold_10d | 171 | 36.84 | -0.23 | -2.3316 | -20.6215 | 10.0 | 0.938 | 40 | 22.5 | -2.6851 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 171 | 27.49 | -0.4369 | -5.0 | -13.961 | 6.03 | 0.8693 | 40 | 15.0 | -2.9531 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 171 | 47.37 | -0.4713 | -0.8824 | -14.977 | 3.72 | 0.8292 | 40 | 35.0 | -1.6742 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 171 | 28.65 | -0.6742 | -2.521 | -15.8485 | 6.81 | 0.8092 | 40 | 12.5 | -3.6104 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 118 | 36.44 | -0.7348 | -2.8066 | -20.6215 | 10.0 | 0.8208 | 26 | 19.23 | -5.0519 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 3335 | 47.05 | 5.4699 | -0.9029 | -91.7928 | 20.0 | 1.9981 | 1152 | 54.34 | 11.7504 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2193 | 52.53 | 3.6333 | 0.5545 | -89.805 | 10.0 | 2.2247 | 839 | 60.91 | 7.317 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3163 | 50.46 | 3.2106 | 0.165 | -91.3518 | 10.0 | 1.9512 | 1161 | 55.64 | 6.282 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 2685 | 46.11 | 2.7331 | -0.9302 | -90.5777 | 10.0 | 1.608 | 1071 | 48.93 | 4.9393 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 3531 | 45.14 | 2.1441 | -1.1407 | -90.8539 | 10.0 | 1.4738 | 1348 | 48.59 | 4.4624 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 3626 | 46.36 | 1.669 | -0.6981 | -32.2188 | 5.0 | 1.4864 | 1443 | 47.75 | 2.4249 | high | True | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 3335 | 34.33 | 1.6542 | -3.4985 | -90.5777 | 8.57 | 1.3418 | 1152 | 34.98 | 4.1784 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 3531 | 39.34 | 1.4943 | -2.2782 | -32.0847 | 6.69 | 1.3902 | 1348 | 40.36 | 3.0726 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 3531 | 32.06 | 1.0455 | -3.2887 | -90.5777 | 6.39 | 1.248 | 1348 | 31.82 | 2.156 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 3335 | 33.37 | 0.9533 | -2.6726 | -23.9623 | 4.67 | 1.2531 | 1152 | 33.85 | 2.8961 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 3531 | 26.34 | 0.7404 | -5.0 | -19.9536 | 5.13 | 1.2059 | 1348 | 23.22 | 1.2331 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 3626 | 41.31 | 0.1216 | -1.7241 | -34.6101 | 5.0 | 1.0302 | 1443 | 43.31 | 0.5311 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 3576 | 30.09 | 0.073 | -0.6885 | -36.5617 | 3.55 | 1.0251 | 1393 | 28.5 | 0.114 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 3626 | 33.78 | -0.0877 | -2.5713 | -26.1603 | 3.81 | 0.976 | 1443 | 33.75 | 0.1447 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 3598 | 31.07 | -0.1769 | -1.4547 | -28.5714 | 3.66 | 0.945 | 1415 | 29.89 | -0.153 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 3335 | 39.43 | -0.1993 | -2.734 | -90.5777 | 5.44 | 0.9503 | 1152 | 42.1 | 0.0188 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 3531 | 50.98 | -0.5009 | 3.1008 | -90.5777 | 3.07 | 0.8337 | 1348 | 52.67 | -0.5631 | low | False | False |

## Research-Only Relaxed Comparison

| event_filter_id | pattern_id | sample_size | win_rate | avg_return | median_return | max_drawdown | out_of_sample_size | out_of_sample_avg_return | confidence_status | out_of_sample_pass | approved_for_daily |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| limit_locked_volume_lt2_research_only | next_open_hold_20d | 544 | 53.31 | 8.3342 | 2.9555 | -55.5556 | 311 | 12.5267 | high | True | False |
| limit_locked_volume_lt2_research_only | pullback_10ma_hold_10d | 348 | 56.03 | 5.0536 | 1.4935 | -45.3571 | 197 | 8.302 | high | True | False |
| limit_locked_volume_lt2_research_only | pullback_5ma_hold_10d | 514 | 54.86 | 4.7092 | 2.0446 | -41.7808 | 304 | 6.5863 | high | True | False |
| limit_locked_volume_lt2_research_only | signal_close_hold_5d | 640 | 53.12 | 3.4415 | 1.2376 | -36.5617 | 407 | 4.728 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_hold_10d | 612 | 50.0 | 3.0388 | 0.0878 | -41.2424 | 379 | 4.7265 | high | True | False |
| limit_locked_volume_lt2_research_only | next_day_break_signal_high_hold_10d | 569 | 49.38 | 2.833 | 0.0 | -41.2424 | 348 | 4.4565 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_large_black_exit_10d | 612 | 44.77 | 2.157 | -1.8264 | -41.2424 | 379 | 3.1137 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_10ma_trailing_20d | 544 | 38.42 | 2.1897 | -4.5679 | -28.5587 | 311 | 2.8652 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_signal_low_stop_10d | 612 | 36.44 | 1.8326 | -4.45 | -23.6842 | 379 | 2.14 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_5pct_stop_10d | 612 | 24.84 | 1.5015 | -5.0 | -17.9204 | 379 | 2.1297 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_5ma_trailing_20d | 544 | 35.85 | 1.1266 | -2.8757 | -25.7613 | 311 | 2.2417 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_hold_5d | 640 | 45.94 | 0.5839 | -0.9031 | -39.2111 | 407 | 1.5616 | medium | True | False |
| limit_locked_volume_lt2_research_only | chase_day1_signal_low_stop_5d | 640 | 37.66 | 0.3697 | -2.7561 | -23.6842 | 407 | 1.0709 | medium | False | False |
| limit_locked_volume_lt2_research_only | chase_day3_signal_low_stop_5d | 625 | 32.8 | 0.2191 | -1.0221 | -39.2111 | 392 | 0.5766 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_tp10_signal_low_stop_20d | 544 | 47.24 | 0.1797 | -0.7839 | -23.6842 | 311 | 0.67 | low | True | False |
| limit_locked_volume_lt2_research_only | chase_day2_signal_low_stop_5d | 632 | 34.49 | -0.0776 | -1.887 | -36.5617 | 399 | 0.3726 | low | False | False |
| limit_locked_volume_lt2_research_only | next_open_tp5_signal_low_stop_10d | 612 | 61.27 | -0.1197 | 5.0 | -23.6842 | 379 | 0.0543 | low | False | False |

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.
