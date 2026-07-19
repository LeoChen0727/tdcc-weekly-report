# Historical Pattern Operation Registry

- generated_at: `2026-07-19 11:09:28 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `195130`
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
| current_model_hit_all | next_open_hold_20d | 4481 | 46.24 | 4.2537 | -1.3208 | -91.7928 | 20.0 | 1.7165 | 1815 | 50.14 | 6.7583 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2941 | 52.3 | 3.6847 | 0.5545 | -89.805 | 10.0 | 2.2274 | 1269 | 56.74 | 5.8721 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 4173 | 49.48 | 2.9867 | -0.0852 | -91.3518 | 10.0 | 1.8438 | 1736 | 51.04 | 4.0194 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4773 | 47.64 | 2.1122 | -0.4396 | -37.4194 | 5.0 | 1.5907 | 2107 | 49.12 | 2.8544 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3671 | 45.41 | 2.0655 | -1.236 | -90.5777 | 10.0 | 1.4185 | 1661 | 46.18 | 2.429 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4672 | 44.61 | 1.6554 | -1.4591 | -90.8539 | 10.0 | 1.339 | 2006 | 45.96 | 2.1527 | high | True | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4672 | 39.17 | 1.0269 | -2.5574 | -47.7462 | 6.6 | 1.2475 | 2006 | 39.33 | 1.3468 | medium | False | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 4481 | 34.88 | 0.9207 | -3.6036 | -90.5777 | 8.6 | 1.1809 | 1815 | 36.03 | 1.4201 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4672 | 30.69 | 0.5604 | -3.5439 | -90.5777 | 6.13 | 1.1287 | 2006 | 29.21 | 0.636 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4672 | 25.56 | 0.4735 | -5.0 | -19.9536 | 4.98 | 1.128 | 2006 | 22.43 | 0.2363 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 4481 | 33.94 | 0.1372 | -2.7963 | -26.2609 | 4.65 | 1.0343 | 1815 | 34.21 | 0.2292 | low | False | False |
| current_model_hit_all | next_open_hold_5d | 4773 | 41.27 | -0.0517 | -1.8462 | -36.7391 | 5.0 | 0.9882 | 2107 | 42.1 | -0.0026 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4773 | 33.0 | -0.0869 | -2.6756 | -26.1603 | 3.69 | 0.9768 | 2107 | 31.66 | -0.0447 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4752 | 29.21 | -0.1446 | -0.458 | -30.999 | 3.45 | 0.9514 | 2086 | 27.61 | -0.3295 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 4481 | 39.01 | -0.2665 | -2.7244 | -90.5777 | 5.11 | 0.9342 | 1815 | 40.5 | -0.1752 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4760 | 30.46 | -0.2782 | -1.3268 | -28.5714 | 3.54 | 0.9161 | 2094 | 29.27 | -0.333 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4672 | 50.06 | -0.6004 | 0.193 | -90.5777 | 2.91 | 0.8043 | 2006 | 50.3 | -0.7205 | low | False | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1594 | 53.01 | 4.3713 | 0.8585 | -89.805 | 10.0 | 2.3979 | 802 | 57.23 | 5.8669 | high | True | False |
| limit_up_like_current_hit | next_open_hold_20d | 2520 | 45.95 | 4.3558 | -1.8424 | -91.7928 | 20.0 | 1.6507 | 1170 | 48.55 | 5.934 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2722 | 51.43 | 3.394 | 0.563 | -37.4194 | 5.0 | 1.9049 | 1372 | 52.33 | 4.1231 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2310 | 49.74 | 3.337 | 0.0 | -91.3518 | 10.0 | 1.8719 | 1100 | 49.64 | 3.615 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2460 | 44.23 | 2.0383 | -1.6172 | -90.5777 | 10.0 | 1.3737 | 1220 | 45.16 | 2.2162 | high | True | False |
| limit_up_like_current_hit | next_open_hold_10d | 2659 | 44.08 | 1.9696 | -1.7301 | -90.5777 | 10.0 | 1.3645 | 1309 | 44.92 | 2.029 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2659 | 38.06 | 1.2098 | -3.1325 | -47.7462 | 6.1 | 1.2645 | 1309 | 38.5 | 1.3916 | medium | False | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2520 | 35.2 | 0.8894 | -4.4048 | -90.5777 | 8.76 | 1.1513 | 1170 | 35.64 | 1.012 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2659 | 23.09 | 0.7426 | -5.0 | -18.1818 | 4.44 | 1.1898 | 1309 | 20.78 | 0.4685 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2659 | 31.37 | 0.7159 | -4.3668 | -90.5777 | 6.32 | 1.1438 | 1309 | 29.56 | 0.674 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2722 | 33.98 | 0.1049 | -2.862 | -26.1603 | 3.74 | 1.0247 | 1372 | 33.38 | 0.2966 | low | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2520 | 34.68 | -0.0002 | -3.3543 | -26.2609 | 4.74 | 1.0 | 1170 | 35.3 | 0.0112 | low | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2722 | 41.7 | -0.0426 | -2.2123 | -36.7391 | 5.0 | 0.9916 | 1372 | 43.29 | 0.0614 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2520 | 42.86 | -0.2956 | -1.8743 | -90.5777 | 4.9 | 0.9343 | 1170 | 42.56 | -0.2818 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2710 | 29.26 | -0.3549 | -0.525 | -30.999 | 3.54 | 0.8984 | 1360 | 27.06 | -0.6973 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2715 | 31.12 | -0.4613 | -1.532 | -28.5714 | 3.61 | 0.8814 | 1365 | 29.67 | -0.4618 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2659 | 54.68 | -0.5675 | 5.0 | -90.5777 | 2.68 | 0.8272 | 1309 | 54.01 | -0.6121 | low | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 130 | 50.77 | 2.5194 | 0.1259 | -15.5556 | 10.0 | 2.2532 | 57 | 57.89 | 2.4073 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 142 | 42.25 | 1.3696 | -2.0309 | -30.0599 | 20.0 | 1.3228 | 62 | 40.32 | 1.7177 | medium | False | False |
| long_base_low_position | signal_close_hold_5d | 145 | 41.38 | 1.1058 | -1.3636 | -15.572 | 5.0 | 1.4333 | 65 | 35.38 | 0.6605 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 98 | 58.16 | 2.1053 | 1.3956 | -11.9374 | 10.0 | 2.451 | 45 | 73.33 | 3.3154 | low | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 145 | 35.17 | -0.0827 | -0.1346 | -15.0198 | 3.61 | 0.9621 | 65 | 30.77 | -0.8548 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 144 | 29.86 | -0.2975 | -0.5639 | -15.5894 | 3.62 | 0.8656 | 64 | 25.0 | -0.9713 | low | False | False |
| long_base_low_position | next_open_hold_5d | 145 | 38.62 | -0.3441 | -1.4663 | -19.3503 | 5.0 | 0.889 | 65 | 32.31 | -0.765 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 142 | 28.17 | -0.6165 | -3.0739 | -19.2308 | 8.09 | 0.8438 | 62 | 24.19 | -2.0768 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 142 | 35.92 | -0.6179 | -2.9486 | -16.8498 | 6.94 | 0.8259 | 62 | 27.42 | -2.2366 | low | False | False |
| long_base_low_position | next_open_hold_10d | 142 | 35.92 | -0.6403 | -2.7622 | -20.6215 | 10.0 | 0.8305 | 62 | 30.65 | -1.5203 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 142 | 33.8 | -0.6545 | -2.5717 | -16.8498 | 6.56 | 0.8225 | 62 | 27.42 | -1.6872 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 145 | 31.03 | -0.692 | -2.0833 | -16.8498 | 3.69 | 0.7732 | 65 | 21.54 | -1.8874 | low | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 142 | 32.39 | -0.7394 | -2.623 | -16.8498 | 4.55 | 0.7637 | 62 | 20.97 | -2.3958 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 142 | 26.76 | -1.0737 | -5.0 | -13.961 | 5.56 | 0.6945 | 62 | 19.35 | -2.4922 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 142 | 38.73 | -1.3295 | -2.225 | -16.8498 | 3.82 | 0.5845 | 62 | 27.42 | -2.5283 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 92 | 32.61 | -1.5496 | -3.151 | -20.6215 | 10.0 | 0.6462 | 40 | 27.5 | -2.5548 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 142 | 24.65 | -1.566 | -2.9909 | -16.8498 | 6.26 | 0.5984 | 62 | 14.52 | -3.2057 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 4339 | 46.37 | 4.3481 | -1.2903 | -91.7928 | 20.0 | 1.7256 | 1753 | 50.48 | 6.9366 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2843 | 52.09 | 3.7391 | 0.5362 | -89.805 | 10.0 | 2.2237 | 1224 | 56.13 | 5.9661 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 4043 | 49.44 | 3.0017 | -0.1172 | -91.3518 | 10.0 | 1.8364 | 1679 | 50.8 | 4.0741 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3579 | 45.74 | 2.1584 | -1.1551 | -90.5777 | 10.0 | 1.4361 | 1621 | 46.64 | 2.552 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4628 | 47.84 | 2.1437 | -0.406 | -37.4194 | 5.0 | 1.5941 | 2042 | 49.56 | 2.9242 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4530 | 44.88 | 1.7274 | -1.3575 | -90.8539 | 10.0 | 1.3512 | 1944 | 46.45 | 2.2698 | high | True | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4530 | 39.27 | 1.0785 | -2.5321 | -47.7462 | 6.59 | 1.2588 | 1944 | 39.71 | 1.4611 | medium | False | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 4339 | 35.1 | 0.971 | -3.6364 | -90.5777 | 8.61 | 1.1894 | 1753 | 36.45 | 1.5438 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4530 | 30.88 | 0.627 | -3.5628 | -90.5777 | 6.13 | 1.1435 | 1944 | 29.68 | 0.7586 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4530 | 25.52 | 0.522 | -5.0 | -19.9536 | 4.97 | 1.1409 | 1944 | 22.53 | 0.3233 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 4339 | 33.99 | 0.1659 | -2.8078 | -26.2609 | 4.66 | 1.0412 | 1753 | 34.68 | 0.322 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4628 | 41.36 | -0.0426 | -1.8592 | -36.7391 | 5.0 | 0.9904 | 2042 | 42.41 | 0.0217 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4628 | 33.06 | -0.068 | -2.6929 | -26.1603 | 3.69 | 0.982 | 2042 | 31.98 | 0.014 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4608 | 29.19 | -0.1398 | -0.4549 | -30.999 | 3.45 | 0.9534 | 2022 | 27.7 | -0.3092 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 4339 | 39.18 | -0.2538 | -2.7295 | -90.5777 | 5.07 | 0.9375 | 1753 | 40.96 | -0.1217 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4615 | 30.31 | -0.2844 | -1.3631 | -28.5714 | 3.54 | 0.9152 | 2029 | 29.23 | -0.3162 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4530 | 50.42 | -0.5776 | 1.1811 | -90.5777 | 2.88 | 0.8115 | 1944 | 51.03 | -0.6628 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

