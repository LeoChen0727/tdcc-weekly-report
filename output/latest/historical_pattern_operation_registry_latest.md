# Historical Pattern Operation Registry

- generated_at: `2026-07-05 04:45:44 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `187503`
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
| current_model_hit_all | next_open_hold_20d | 4316 | 46.57 | 4.457 | -1.2238 | -91.7928 | 20.0 | 1.764 | 1777 | 50.59 | 7.0707 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2805 | 53.01 | 3.8702 | 0.6766 | -89.805 | 10.0 | 2.3367 | 1231 | 59.79 | 6.661 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 4012 | 49.68 | 3.0728 | 0.0 | -91.3518 | 10.0 | 1.8876 | 1699 | 52.21 | 4.7253 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4596 | 47.89 | 2.2156 | -0.4097 | -37.4194 | 5.0 | 1.6343 | 2057 | 49.2 | 2.9124 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3526 | 45.15 | 1.9797 | -1.2947 | -90.5777 | 10.0 | 1.4051 | 1606 | 45.83 | 2.4887 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4499 | 44.5 | 1.6225 | -1.4599 | -90.8539 | 10.0 | 1.3367 | 1960 | 45.77 | 2.2966 | high | True | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4499 | 39.1 | 0.9747 | -2.521 | -47.7462 | 6.64 | 1.2362 | 1960 | 38.83 | 1.2947 | medium | False | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 4316 | 34.64 | 0.864 | -3.6364 | -90.5777 | 8.6 | 1.1686 | 1777 | 35.23 | 1.1108 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4499 | 30.76 | 0.5102 | -3.5385 | -90.5777 | 6.16 | 1.1175 | 1960 | 28.67 | 0.4193 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4499 | 25.61 | 0.4042 | -5.0 | -19.9536 | 5.01 | 1.1095 | 1960 | 21.84 | 0.0909 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 4316 | 33.64 | 0.0931 | -2.8445 | -26.2609 | 4.65 | 1.0232 | 1777 | 33.26 | 0.076 | low | False | False |
| current_model_hit_all | next_open_hold_5d | 4596 | 41.45 | 0.0753 | -1.7925 | -36.7391 | 5.0 | 1.0176 | 2057 | 42.44 | 0.174 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4596 | 33.16 | -0.0092 | -2.6178 | -26.1603 | 3.71 | 0.9975 | 2057 | 31.45 | -0.014 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4571 | 29.16 | -0.1641 | -0.4768 | -30.999 | 3.46 | 0.9449 | 2032 | 26.92 | -0.4759 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4586 | 30.44 | -0.2727 | -1.3618 | -28.5714 | 3.55 | 0.9176 | 2047 | 28.29 | -0.5138 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 4316 | 38.9 | -0.3005 | -2.7554 | -90.5777 | 5.12 | 0.9263 | 1777 | 39.73 | -0.3859 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4499 | 50.14 | -0.5901 | 0.2933 | -90.5777 | 2.94 | 0.8072 | 1960 | 49.85 | -0.8144 | low | False | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1511 | 53.81 | 4.6371 | 1.2528 | -89.805 | 10.0 | 2.5314 | 786 | 60.18 | 6.721 | high | True | False |
| limit_up_like_current_hit | next_open_hold_20d | 2420 | 46.07 | 4.4581 | -1.8135 | -91.7928 | 20.0 | 1.6728 | 1162 | 48.8 | 6.0179 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2606 | 51.61 | 3.4921 | 0.5831 | -37.4194 | 5.0 | 1.951 | 1348 | 52.3 | 4.135 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2206 | 49.91 | 3.4344 | 0.0 | -91.3518 | 10.0 | 1.9164 | 1085 | 51.24 | 4.5209 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2343 | 43.79 | 1.9053 | -1.7199 | -90.5777 | 10.0 | 1.352 | 1180 | 44.83 | 2.3241 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_10d | 2533 | 43.74 | 1.8742 | -1.8248 | -90.5777 | 10.0 | 1.3508 | 1275 | 44.71 | 2.2137 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2533 | 37.78 | 1.0895 | -3.1301 | -47.7462 | 6.12 | 1.2386 | 1275 | 37.8 | 1.2995 | medium | False | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2420 | 34.79 | 0.7254 | -4.5354 | -90.5777 | 8.75 | 1.1218 | 1162 | 34.77 | 0.6197 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2533 | 31.39 | 0.6321 | -4.3902 | -90.5777 | 6.37 | 1.1269 | 1275 | 29.1 | 0.4554 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2533 | 22.98 | 0.6205 | -5.0 | -18.1818 | 4.45 | 1.1585 | 1275 | 20.16 | 0.3302 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2606 | 34.04 | 0.1828 | -2.8215 | -26.1603 | 3.75 | 1.0437 | 1348 | 33.09 | 0.3367 | low | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2606 | 41.67 | 0.078 | -2.1755 | -36.7391 | 5.0 | 1.0157 | 1348 | 43.4 | 0.2327 | low | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2420 | 34.26 | -0.1266 | -3.4851 | -26.2609 | 4.73 | 0.9731 | 1162 | 34.42 | -0.1799 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2420 | 42.52 | -0.3901 | -2.0791 | -90.5777 | 4.94 | 0.9143 | 1162 | 41.57 | -0.5513 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2588 | 29.21 | -0.391 | -0.565 | -30.999 | 3.55 | 0.8884 | 1330 | 26.47 | -0.8906 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2598 | 31.1 | -0.4553 | -1.5753 | -28.5714 | 3.63 | 0.8828 | 1340 | 28.73 | -0.6709 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2533 | 54.95 | -0.5481 | 5.0 | -90.5777 | 2.71 | 0.8327 | 1275 | 53.96 | -0.6769 | low | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 130 | 50.77 | 2.5194 | 0.1259 | -15.5556 | 10.0 | 2.2532 | 57 | 57.89 | 2.4073 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 140 | 42.14 | 1.5659 | -2.0309 | -22.3164 | 20.0 | 1.383 | 60 | 40.0 | 2.1873 | medium | False | False |
| long_base_low_position | signal_close_hold_5d | 142 | 42.25 | 1.2813 | -1.099 | -15.572 | 5.0 | 1.5222 | 62 | 37.1 | 1.0409 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 98 | 58.16 | 2.1053 | 1.3956 | -11.9374 | 10.0 | 2.451 | 45 | 73.33 | 3.3154 | low | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 142 | 35.92 | -0.0172 | -0.12 | -15.0198 | 3.63 | 0.992 | 62 | 32.26 | -0.7423 | low | False | False |
| long_base_low_position | next_open_hold_5d | 142 | 39.44 | -0.2271 | -1.4021 | -19.3503 | 5.0 | 0.9254 | 62 | 33.87 | -0.5172 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 142 | 30.28 | -0.2401 | -0.5639 | -15.5894 | 3.64 | 0.89 | 62 | 25.81 | -0.8616 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 140 | 34.29 | -0.6078 | -2.5717 | -16.8498 | 6.63 | 0.835 | 60 | 28.33 | -1.6126 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 142 | 35.92 | -0.6179 | -2.9486 | -16.8498 | 6.94 | 0.8259 | 62 | 27.42 | -2.2366 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 140 | 27.86 | -0.621 | -3.0739 | -19.2308 | 8.13 | 0.8431 | 60 | 23.33 | -2.136 | low | False | False |
| long_base_low_position | next_open_hold_10d | 142 | 35.92 | -0.6403 | -2.7622 | -20.6215 | 10.0 | 0.8305 | 62 | 30.65 | -1.5203 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 142 | 31.69 | -0.6498 | -2.1601 | -16.8498 | 3.71 | 0.7876 | 62 | 22.58 | -1.8485 | low | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 140 | 32.14 | -0.773 | -2.623 | -16.8498 | 4.56 | 0.7529 | 60 | 20.0 | -2.5294 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 142 | 26.76 | -1.0737 | -5.0 | -13.961 | 5.56 | 0.6945 | 62 | 19.35 | -2.4922 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 142 | 38.73 | -1.3295 | -2.225 | -16.8498 | 3.82 | 0.5845 | 62 | 27.42 | -2.5283 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 92 | 32.61 | -1.5496 | -3.151 | -20.6215 | 10.0 | 0.6462 | 40 | 27.5 | -2.5548 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 142 | 24.65 | -1.566 | -2.9909 | -16.8498 | 6.26 | 0.5984 | 62 | 14.52 | -3.2057 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 4176 | 46.72 | 4.5539 | -1.1864 | -91.7928 | 20.0 | 1.7729 | 1717 | 50.96 | 7.2413 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2707 | 52.83 | 3.9341 | 0.6711 | -89.805 | 10.0 | 2.3347 | 1186 | 59.27 | 6.788 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3882 | 49.64 | 3.0914 | -0.0653 | -91.3518 | 10.0 | 1.8806 | 1642 | 52.01 | 4.8058 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4454 | 48.07 | 2.2454 | -0.3826 | -37.4194 | 5.0 | 1.6368 | 1995 | 49.57 | 2.9706 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3434 | 45.49 | 2.0743 | -1.1744 | -90.5777 | 10.0 | 1.4232 | 1566 | 46.3 | 2.6175 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4357 | 44.78 | 1.6963 | -1.3575 | -90.8539 | 10.0 | 1.3496 | 1898 | 46.26 | 2.4213 | high | True | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4357 | 39.2 | 1.0266 | -2.5 | -47.7462 | 6.63 | 1.2477 | 1898 | 39.2 | 1.4101 | medium | False | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 4176 | 34.87 | 0.9138 | -3.6775 | -90.5777 | 8.61 | 1.177 | 1717 | 35.64 | 1.2242 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4357 | 30.96 | 0.5778 | -3.5539 | -90.5777 | 6.16 | 1.1327 | 1898 | 29.14 | 0.5377 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4357 | 25.57 | 0.4523 | -5.0 | -19.9536 | 4.99 | 1.1223 | 1898 | 21.92 | 0.1753 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 4176 | 33.69 | 0.1222 | -2.8545 | -26.2609 | 4.65 | 1.0301 | 1717 | 33.72 | 0.167 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4454 | 41.51 | 0.085 | -1.8216 | -36.7391 | 5.0 | 1.0196 | 1995 | 42.71 | 0.1955 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4454 | 33.21 | 0.0112 | -2.6532 | -26.1603 | 3.71 | 1.003 | 1995 | 31.73 | 0.043 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4429 | 29.13 | -0.1617 | -0.4762 | -30.999 | 3.46 | 0.9462 | 1970 | 26.95 | -0.4637 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4444 | 30.27 | -0.2808 | -1.4085 | -28.5714 | 3.55 | 0.9161 | 1985 | 28.16 | -0.5067 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 4176 | 39.06 | -0.2902 | -2.8005 | -90.5777 | 5.07 | 0.929 | 1717 | 40.13 | -0.3431 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4357 | 50.52 | -0.566 | 1.2939 | -90.5777 | 2.91 | 0.8148 | 1898 | 50.58 | -0.7584 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

