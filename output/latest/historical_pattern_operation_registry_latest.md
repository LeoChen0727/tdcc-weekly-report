# Historical Pattern Operation Registry

- generated_at: `2026-07-09 11:28:50 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `190420`
- registry_rows: `68`
- registry_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/historical_pattern_operation_registry_latest.csv
- detail_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/history/research/historical_pattern_operation_events.csv

## Scope

- This is research/backtest output only.
- It does not write production config, daily candidate files, or PDF operation text.
- `approved_for_daily` remains `False` until a separate promotion PR explicitly approves a pattern.
- Current model hit groups include locked-limit breakouts without volume-ratio or 20D average-volume gates; non-current research comparisons must not reintroduce the removed volume gate.

## Current Model Hit Patterns

| event_filter_id | pattern_id | sample_size | win_rate | avg_return | median_return | max_drawdown | avg_holding_days | profit_factor | out_of_sample_size | out_of_sample_win_rate | out_of_sample_avg_return | confidence_status | out_of_sample_pass | approved_for_daily |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current_model_hit_all | next_open_hold_20d | 4374 | 46.64 | 4.4587 | -1.2158 | -91.7928 | 20.0 | 1.7636 | 1766 | 50.91 | 7.1199 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2850 | 52.7 | 3.8059 | 0.6195 | -89.805 | 10.0 | 2.3044 | 1219 | 57.92 | 6.2678 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 4098 | 49.61 | 3.0668 | -0.0312 | -91.3518 | 10.0 | 1.8836 | 1717 | 51.72 | 4.4311 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4659 | 48.1 | 2.2652 | -0.3802 | -37.4194 | 5.0 | 1.6496 | 2051 | 50.07 | 3.177 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3590 | 45.18 | 1.9714 | -1.3133 | -90.5777 | 10.0 | 1.4024 | 1618 | 45.8 | 2.3616 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4574 | 44.49 | 1.6146 | -1.4828 | -90.8539 | 10.0 | 1.3344 | 1966 | 45.83 | 2.2237 | high | True | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4574 | 38.98 | 0.9508 | -2.5621 | -47.7462 | 6.61 | 1.2299 | 1966 | 38.81 | 1.2642 | medium | False | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 4374 | 34.91 | 0.927 | -3.5774 | -90.5777 | 8.6 | 1.1819 | 1766 | 36.24 | 1.4056 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4574 | 30.52 | 0.4523 | -3.5581 | -90.5777 | 6.13 | 1.1039 | 1966 | 28.43 | 0.4001 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4574 | 25.4 | 0.3536 | -5.0 | -19.9536 | 4.98 | 1.0955 | 1966 | 21.87 | 0.0478 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 4374 | 33.77 | 0.1189 | -2.8239 | -26.2609 | 4.65 | 1.0296 | 1766 | 33.81 | 0.182 | low | False | False |
| current_model_hit_all | next_open_hold_5d | 4659 | 41.64 | 0.1124 | -1.7685 | -36.7391 | 5.0 | 1.0262 | 2051 | 42.91 | 0.3723 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4659 | 33.35 | 0.0376 | -2.5788 | -26.1603 | 3.71 | 1.0102 | 2051 | 32.13 | 0.2055 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4611 | 29.28 | -0.134 | -0.4651 | -30.999 | 3.47 | 0.955 | 2003 | 27.66 | -0.2864 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4638 | 30.62 | -0.2295 | -1.3408 | -28.5714 | 3.56 | 0.9305 | 2030 | 29.41 | -0.2234 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 4374 | 38.96 | -0.2753 | -2.7259 | -90.5777 | 5.11 | 0.9321 | 1766 | 39.98 | -0.2386 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4574 | 49.87 | -0.6168 | 0.0 | -90.5777 | 2.93 | 0.7993 | 1966 | 49.34 | -0.7898 | low | False | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1537 | 53.42 | 4.5626 | 1.0055 | -89.805 | 10.0 | 2.4982 | 772 | 57.9 | 6.2449 | high | True | False |
| limit_up_like_current_hit | next_open_hold_20d | 2459 | 46.2 | 4.5141 | -1.8072 | -91.7928 | 20.0 | 1.6821 | 1150 | 48.78 | 6.0504 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2649 | 51.91 | 3.5675 | 0.6803 | -37.4194 | 5.0 | 1.9737 | 1340 | 53.21 | 4.4421 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2256 | 49.87 | 3.4269 | 0.0 | -91.3518 | 10.0 | 1.9128 | 1085 | 50.23 | 4.0372 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2394 | 43.86 | 1.9077 | -1.722 | -90.5777 | 10.0 | 1.3518 | 1187 | 44.57 | 2.1256 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_10d | 2588 | 43.74 | 1.8773 | -1.8286 | -90.5777 | 10.0 | 1.3508 | 1279 | 44.41 | 2.0549 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2588 | 37.67 | 1.0684 | -3.1488 | -47.7462 | 6.09 | 1.2339 | 1279 | 37.69 | 1.2535 | medium | False | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2459 | 35.1 | 0.8448 | -4.4397 | -90.5777 | 8.76 | 1.1429 | 1150 | 35.65 | 0.9418 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2588 | 22.76 | 0.5585 | -5.0 | -18.1818 | 4.42 | 1.1423 | 1279 | 20.09 | 0.2656 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2588 | 31.07 | 0.5528 | -4.4427 | -90.5777 | 6.32 | 1.1107 | 1279 | 28.69 | 0.4276 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2649 | 34.31 | 0.2503 | -2.7972 | -26.1603 | 3.76 | 1.0599 | 1340 | 33.88 | 0.594 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2649 | 41.98 | 0.1331 | -2.1195 | -36.7391 | 5.0 | 1.0269 | 1340 | 43.88 | 0.4323 | low | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2459 | 34.36 | -0.0849 | -3.4565 | -26.2609 | 4.73 | 0.9819 | 1150 | 34.7 | -0.1237 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2459 | 42.66 | -0.34 | -1.9504 | -90.5777 | 4.92 | 0.9248 | 1150 | 41.83 | -0.372 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2616 | 29.32 | -0.3497 | -0.5338 | -30.999 | 3.56 | 0.8999 | 1307 | 27.16 | -0.6507 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2634 | 31.25 | -0.411 | -1.556 | -28.5714 | 3.63 | 0.8939 | 1325 | 29.81 | -0.33 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2588 | 54.52 | -0.5857 | 5.0 | -90.5777 | 2.71 | 0.8221 | 1279 | 53.24 | -0.6529 | low | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 130 | 50.77 | 2.5194 | 0.1259 | -15.5556 | 10.0 | 2.2532 | 57 | 57.89 | 2.4073 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 142 | 42.25 | 1.3696 | -2.0309 | -30.0599 | 20.0 | 1.3228 | 62 | 40.32 | 1.7177 | medium | False | False |
| long_base_low_position | signal_close_hold_5d | 142 | 42.25 | 1.2813 | -1.099 | -15.572 | 5.0 | 1.5222 | 62 | 37.1 | 1.0409 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 98 | 58.16 | 2.1053 | 1.3956 | -11.9374 | 10.0 | 2.451 | 45 | 73.33 | 3.3154 | low | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 142 | 35.92 | -0.0172 | -0.12 | -15.0198 | 3.63 | 0.992 | 62 | 32.26 | -0.7423 | low | False | False |
| long_base_low_position | next_open_hold_5d | 142 | 39.44 | -0.2271 | -1.4021 | -19.3503 | 5.0 | 0.9254 | 62 | 33.87 | -0.5172 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 142 | 30.28 | -0.2401 | -0.5639 | -15.5894 | 3.64 | 0.89 | 62 | 25.81 | -0.8616 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 142 | 28.17 | -0.6165 | -3.0739 | -19.2308 | 8.09 | 0.8438 | 62 | 24.19 | -2.0768 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 142 | 35.92 | -0.6179 | -2.9486 | -16.8498 | 6.94 | 0.8259 | 62 | 27.42 | -2.2366 | low | False | False |
| long_base_low_position | next_open_hold_10d | 142 | 35.92 | -0.6403 | -2.7622 | -20.6215 | 10.0 | 0.8305 | 62 | 30.65 | -1.5203 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 142 | 31.69 | -0.6498 | -2.1601 | -16.8498 | 3.71 | 0.7876 | 62 | 22.58 | -1.8485 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 142 | 33.8 | -0.6545 | -2.5717 | -16.8498 | 6.56 | 0.8225 | 62 | 27.42 | -1.6872 | low | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 142 | 32.39 | -0.7394 | -2.623 | -16.8498 | 4.55 | 0.7637 | 62 | 20.97 | -2.3958 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 142 | 26.76 | -1.0737 | -5.0 | -13.961 | 5.56 | 0.6945 | 62 | 19.35 | -2.4922 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 142 | 38.73 | -1.3295 | -2.225 | -16.8498 | 3.82 | 0.5845 | 62 | 27.42 | -2.5283 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 92 | 32.61 | -1.5496 | -3.151 | -20.6215 | 10.0 | 0.6462 | 40 | 27.5 | -2.5548 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 142 | 24.65 | -1.566 | -2.9909 | -16.8498 | 6.26 | 0.5984 | 62 | 14.52 | -3.2057 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 4232 | 46.79 | 4.5623 | -1.1544 | -91.7928 | 20.0 | 1.7743 | 1704 | 51.29 | 7.3164 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2752 | 52.51 | 3.8664 | 0.6069 | -89.805 | 10.0 | 2.3019 | 1174 | 57.33 | 6.3809 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3968 | 49.57 | 3.0847 | -0.0828 | -91.3518 | 10.0 | 1.8767 | 1660 | 51.51 | 4.5006 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4517 | 48.28 | 2.2961 | -0.3552 | -37.4194 | 5.0 | 1.6524 | 1989 | 50.48 | 3.2436 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3498 | 45.51 | 2.064 | -1.2073 | -90.5777 | 10.0 | 1.4201 | 1578 | 46.26 | 2.4862 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4432 | 44.77 | 1.6869 | -1.381 | -90.8539 | 10.0 | 1.347 | 1904 | 46.32 | 2.3456 | high | True | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4432 | 39.08 | 1.0011 | -2.5447 | -47.7462 | 6.6 | 1.241 | 1904 | 39.18 | 1.3782 | medium | False | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 4232 | 35.14 | 0.9788 | -3.6088 | -90.5777 | 8.62 | 1.1906 | 1704 | 36.68 | 1.5323 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4432 | 30.71 | 0.517 | -3.5785 | -90.5777 | 6.12 | 1.1183 | 1904 | 28.89 | 0.5175 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4432 | 25.36 | 0.3994 | -5.0 | -19.9536 | 4.96 | 1.1077 | 1904 | 21.95 | 0.1305 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 4232 | 33.81 | 0.1477 | -2.8263 | -26.2609 | 4.65 | 1.0365 | 1704 | 34.27 | 0.2758 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4517 | 41.71 | 0.123 | -1.7742 | -36.7391 | 5.0 | 1.0284 | 1989 | 43.19 | 0.4001 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4517 | 33.41 | 0.0592 | -2.6166 | -26.1603 | 3.71 | 1.016 | 1989 | 32.43 | 0.2695 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4469 | 29.25 | -0.1307 | -0.4587 | -30.999 | 3.46 | 0.9565 | 1941 | 27.72 | -0.268 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4496 | 30.45 | -0.2362 | -1.3786 | -28.5714 | 3.56 | 0.9293 | 1968 | 29.32 | -0.207 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 4232 | 39.13 | -0.2625 | -2.7299 | -90.5777 | 5.06 | 0.9355 | 1704 | 40.43 | -0.1859 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4432 | 50.23 | -0.594 | 0.7551 | -90.5777 | 2.9 | 0.8065 | 1904 | 50.05 | -0.7332 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

