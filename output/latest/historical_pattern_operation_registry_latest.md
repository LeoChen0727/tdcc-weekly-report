# Historical Pattern Operation Registry

- generated_at: `2026-06-30 22:49:02 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `184141`
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
| current_model_hit_all | next_open_hold_20d | 4159 | 47.2 | 4.7521 | -0.9313 | -91.7928 | 20.0 | 1.8335 | 1675 | 52.24 | 8.0104 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2790 | 53.01 | 3.8927 | 0.6768 | -89.805 | 10.0 | 2.344 | 1262 | 60.38 | 6.7932 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3981 | 49.61 | 3.0648 | -0.0263 | -91.3518 | 10.0 | 1.8829 | 1723 | 52.0 | 4.7658 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4554 | 47.91 | 2.1747 | -0.4097 | -37.4194 | 5.0 | 1.6243 | 2070 | 48.99 | 2.7708 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3477 | 45.01 | 1.9314 | -1.3223 | -90.5777 | 10.0 | 1.3937 | 1603 | 45.23 | 2.3466 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4437 | 44.42 | 1.5966 | -1.4599 | -90.8539 | 10.0 | 1.3307 | 1953 | 45.21 | 2.1862 | high | True | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 4159 | 35.27 | 1.1079 | -3.4524 | -90.5777 | 8.67 | 1.2231 | 1675 | 36.24 | 1.5814 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4437 | 39.04 | 0.9784 | -2.5276 | -47.7462 | 6.63 | 1.237 | 1953 | 38.61 | 1.2755 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4437 | 30.76 | 0.5155 | -3.523 | -90.5777 | 6.16 | 1.1188 | 1953 | 28.42 | 0.3719 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4437 | 25.65 | 0.4105 | -5.0 | -19.9536 | 5.01 | 1.1113 | 1953 | 21.66 | 0.0898 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 4159 | 34.34 | 0.2561 | -2.6941 | -26.2609 | 4.7 | 1.0654 | 1675 | 34.63 | 0.4443 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 4554 | 41.46 | 0.0364 | -1.7826 | -36.7391 | 5.0 | 1.0085 | 2070 | 42.17 | 0.0174 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4554 | 33.18 | -0.0331 | -2.6115 | -26.1603 | 3.71 | 0.991 | 2070 | 31.45 | -0.103 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 4159 | 39.75 | -0.1247 | -2.6403 | -90.5777 | 5.18 | 0.9687 | 1675 | 41.73 | -0.0089 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4499 | 29.36 | -0.1387 | -0.4825 | -30.999 | 3.48 | 0.9534 | 2015 | 27.05 | -0.5207 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4535 | 30.54 | -0.2805 | -1.3575 | -28.5714 | 3.56 | 0.9151 | 2051 | 28.67 | -0.5332 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4437 | 50.01 | -0.6053 | 0.1241 | -90.5777 | 2.94 | 0.8028 | 1953 | 49.62 | -0.862 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 2318 | 46.81 | 4.7696 | -1.4108 | -91.7928 | 20.0 | 1.7382 | 1088 | 50.64 | 6.9748 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1500 | 53.73 | 4.6736 | 1.2561 | -89.805 | 10.0 | 2.5445 | 796 | 60.8 | 7.0275 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2578 | 51.63 | 3.4245 | 0.5831 | -37.4194 | 5.0 | 1.935 | 1348 | 52.23 | 4.0091 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2188 | 49.73 | 3.4121 | 0.0 | -91.3518 | 10.0 | 1.9068 | 1095 | 51.05 | 4.6769 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2313 | 43.62 | 1.838 | -1.7241 | -90.5777 | 10.0 | 1.3381 | 1178 | 44.23 | 2.2057 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_10d | 2502 | 43.61 | 1.8144 | -1.8286 | -90.5777 | 10.0 | 1.3383 | 1272 | 44.18 | 2.1134 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2502 | 37.61 | 1.0478 | -3.1488 | -47.7462 | 6.1 | 1.2287 | 1272 | 37.42 | 1.225 | medium | False | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2318 | 35.5 | 1.0044 | -4.2172 | -90.5777 | 8.84 | 1.1748 | 1088 | 35.75 | 1.1615 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2502 | 31.33 | 0.6094 | -4.3948 | -90.5777 | 6.35 | 1.1222 | 1272 | 28.69 | 0.3884 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2502 | 22.94 | 0.6002 | -5.0 | -18.1818 | 4.44 | 1.1532 | 1272 | 19.97 | 0.3377 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2578 | 34.02 | 0.1437 | -2.8281 | -26.1603 | 3.76 | 1.0344 | 1348 | 33.09 | 0.2347 | low | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2318 | 35.03 | 0.0582 | -3.2607 | -26.2609 | 4.78 | 1.0128 | 1088 | 35.75 | 0.2174 | low | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2578 | 41.66 | 0.0127 | -2.1755 | -36.7391 | 5.0 | 1.0026 | 1348 | 43.25 | 0.0742 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2318 | 43.57 | -0.1751 | -1.5886 | -90.5777 | 5.0 | 0.9606 | 1088 | 43.38 | -0.2046 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2533 | 29.49 | -0.3492 | -0.565 | -30.999 | 3.57 | 0.9003 | 1303 | 26.78 | -0.8988 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2561 | 31.24 | -0.4754 | -1.5686 | -28.5714 | 3.63 | 0.8774 | 1331 | 29.15 | -0.7066 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2502 | 54.76 | -0.5753 | 5.0 | -90.5777 | 2.72 | 0.8253 | 1272 | 53.54 | -0.7601 | low | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 130 | 50.77 | 2.5194 | 0.1259 | -15.5556 | 10.0 | 2.2532 | 57 | 57.89 | 2.4073 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 127 | 41.73 | 1.7133 | -2.2556 | -22.3164 | 20.0 | 1.4098 | 47 | 38.3 | 2.7575 | medium | False | False |
| long_base_low_position | signal_close_hold_5d | 142 | 42.25 | 1.2813 | -1.099 | -15.572 | 5.0 | 1.5222 | 62 | 37.1 | 1.0409 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 98 | 58.16 | 2.1053 | 1.3956 | -11.9374 | 10.0 | 2.451 | 45 | 73.33 | 3.3154 | low | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 142 | 35.92 | -0.0172 | -0.12 | -15.0198 | 3.63 | 0.992 | 62 | 32.26 | -0.7423 | low | False | False |
| long_base_low_position | next_open_hold_5d | 142 | 39.44 | -0.2271 | -1.4021 | -19.3503 | 5.0 | 0.9254 | 62 | 33.87 | -0.5172 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 142 | 30.28 | -0.2401 | -0.5639 | -15.5894 | 3.64 | 0.89 | 62 | 25.81 | -0.8616 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 127 | 29.13 | -0.3398 | -3.0336 | -19.2308 | 8.11 | 0.9147 | 47 | 25.53 | -1.7953 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 127 | 36.22 | -0.3984 | -2.4823 | -16.8498 | 6.53 | 0.8903 | 47 | 31.91 | -1.3247 | low | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 127 | 33.86 | -0.5603 | -2.4818 | -16.8498 | 4.62 | 0.8183 | 47 | 21.28 | -2.4404 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 142 | 35.92 | -0.6179 | -2.9486 | -16.8498 | 6.94 | 0.8259 | 62 | 27.42 | -2.2366 | low | False | False |
| long_base_low_position | next_open_hold_10d | 142 | 35.92 | -0.6403 | -2.7622 | -20.6215 | 10.0 | 0.8305 | 62 | 30.65 | -1.5203 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 142 | 31.69 | -0.6498 | -2.1601 | -16.8498 | 3.71 | 0.7876 | 62 | 22.58 | -1.8485 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 142 | 26.76 | -1.0737 | -5.0 | -13.961 | 5.56 | 0.6945 | 62 | 19.35 | -2.4922 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 142 | 38.73 | -1.3295 | -2.225 | -16.8498 | 3.82 | 0.5845 | 62 | 27.42 | -2.5283 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 92 | 32.61 | -1.5496 | -3.151 | -20.6215 | 10.0 | 0.6462 | 40 | 27.5 | -2.5548 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 142 | 24.65 | -1.566 | -2.9909 | -16.8498 | 6.26 | 0.5984 | 62 | 14.52 | -3.2057 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 4032 | 47.37 | 4.8478 | -0.8697 | -91.7928 | 20.0 | 1.8432 | 1628 | 52.64 | 8.1621 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2692 | 52.82 | 3.9577 | 0.6717 | -89.805 | 10.0 | 2.3421 | 1217 | 59.9 | 6.9218 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3851 | 49.57 | 3.0832 | -0.0888 | -91.3518 | 10.0 | 1.8758 | 1666 | 51.8 | 4.8465 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4412 | 48.1 | 2.2035 | -0.3814 | -37.4194 | 5.0 | 1.6266 | 2008 | 49.35 | 2.8242 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3385 | 45.35 | 2.0261 | -1.2146 | -90.5777 | 10.0 | 1.4118 | 1563 | 45.68 | 2.472 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4295 | 44.7 | 1.6705 | -1.3575 | -90.8539 | 10.0 | 1.3436 | 1891 | 45.69 | 2.3077 | high | True | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 4032 | 35.47 | 1.1535 | -3.4624 | -90.5777 | 8.69 | 1.2309 | 1628 | 36.55 | 1.6789 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4295 | 39.14 | 1.0312 | -2.5 | -47.7462 | 6.62 | 1.2487 | 1891 | 38.97 | 1.3906 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4295 | 30.97 | 0.5844 | -3.5398 | -90.5777 | 6.15 | 1.1343 | 1891 | 28.87 | 0.4892 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4295 | 25.61 | 0.4596 | -5.0 | -19.9536 | 4.99 | 1.1244 | 1891 | 21.73 | 0.1745 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 4032 | 34.35 | 0.2819 | -2.7014 | -26.2609 | 4.7 | 1.0715 | 1628 | 35.01 | 0.5276 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4412 | 41.52 | 0.0449 | -1.8024 | -36.7391 | 5.0 | 1.0104 | 2008 | 42.43 | 0.0339 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4412 | 33.23 | -0.0132 | -2.6463 | -26.1603 | 3.71 | 0.9964 | 2008 | 31.72 | -0.0491 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 4032 | 39.86 | -0.116 | -2.6528 | -90.5777 | 5.13 | 0.9709 | 1628 | 42.01 | 0.029 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4357 | 29.33 | -0.1354 | -0.4808 | -30.999 | 3.47 | 0.9549 | 1953 | 27.09 | -0.5099 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4393 | 30.37 | -0.289 | -1.3972 | -28.5714 | 3.56 | 0.9135 | 1989 | 28.56 | -0.5267 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4295 | 50.38 | -0.5813 | 0.939 | -90.5777 | 2.91 | 0.8103 | 1891 | 50.34 | -0.8074 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

