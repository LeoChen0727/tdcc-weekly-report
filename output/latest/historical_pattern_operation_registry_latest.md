# Historical Pattern Operation Registry

- generated_at: `2026-06-18 10:02:10 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `176327`
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
| current_model_hit_all | next_open_hold_20d | 3987 | 46.85 | 5.2907 | -1.0657 | -91.7928 | 20.0 | 1.9331 | 1488 | 53.76 | 11.3408 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2557 | 52.05 | 3.5423 | 0.5057 | -89.805 | 10.0 | 2.1784 | 1028 | 60.21 | 6.8633 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3760 | 49.95 | 3.0609 | 0.0 | -91.3518 | 10.0 | 1.8701 | 1479 | 54.97 | 5.672 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3323 | 45.65 | 2.518 | -1.1268 | -90.5777 | 10.0 | 1.5176 | 1450 | 48.21 | 4.4161 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4430 | 47.52 | 2.2753 | -0.4577 | -34.3949 | 5.0 | 1.6596 | 1931 | 49.72 | 3.4777 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4252 | 44.83 | 2.0122 | -1.2665 | -90.8539 | 10.0 | 1.4192 | 1753 | 47.86 | 4.0398 | high | True | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 3987 | 34.76 | 1.9046 | -3.442 | -90.5777 | 8.7 | 1.3857 | 1488 | 36.63 | 4.8028 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4252 | 39.7 | 1.4974 | -2.3014 | -71.203 | 6.74 | 1.3693 | 1753 | 40.79 | 2.9636 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4252 | 31.26 | 1.1115 | -3.2168 | -90.5777 | 6.2 | 1.2656 | 1753 | 30.75 | 2.1551 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 3987 | 33.78 | 1.0383 | -2.669 | -26.2609 | 4.73 | 1.2666 | 1488 | 34.07 | 2.9269 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4252 | 26.46 | 0.8646 | -5.0 | -20.6061 | 5.15 | 1.2384 | 1753 | 23.73 | 1.5002 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 4430 | 41.85 | 0.2822 | -1.5981 | -34.6101 | 5.0 | 1.0678 | 1931 | 44.43 | 0.9457 | medium | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4430 | 32.87 | 0.1412 | -2.2912 | -31.2057 | 3.67 | 1.0396 | 1931 | 32.31 | 0.5707 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4408 | 29.2 | -0.074 | -0.4717 | -36.7391 | 3.46 | 0.9752 | 1909 | 27.4 | -0.2291 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 3987 | 38.78 | -0.1656 | -2.6166 | -90.5777 | 5.21 | 0.9578 | 1488 | 41.33 | 0.0568 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4408 | 30.4 | -0.1844 | -1.3301 | -31.2057 | 3.54 | 0.9437 | 1909 | 29.13 | -0.1753 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4252 | 50.33 | -0.4671 | 0.8276 | -90.5777 | 2.95 | 0.8415 | 1753 | 52.48 | -0.456 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 2175 | 46.85 | 6.1905 | -1.3514 | -91.7928 | 20.0 | 1.9782 | 940 | 52.87 | 12.1218 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1328 | 52.11 | 4.2542 | 0.644 | -89.805 | 10.0 | 2.3379 | 625 | 60.0 | 7.1023 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2476 | 51.05 | 3.6442 | 0.4717 | -34.3949 | 5.0 | 2.0134 | 1241 | 52.05 | 4.7557 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2022 | 50.49 | 3.3887 | 0.1457 | -91.3518 | 10.0 | 1.8786 | 921 | 54.83 | 5.4779 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2192 | 44.25 | 2.6473 | -1.5086 | -90.5777 | 10.0 | 1.4879 | 1053 | 47.1 | 4.6001 | high | True | False |
| limit_up_like_current_hit | next_open_hold_10d | 2363 | 44.31 | 2.5582 | -1.5171 | -90.5777 | 10.0 | 1.4778 | 1128 | 47.25 | 4.4798 | high | True | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2175 | 35.63 | 2.6976 | -4.0498 | -90.5777 | 8.96 | 1.4759 | 940 | 37.13 | 6.1894 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2363 | 38.51 | 1.8687 | -2.9032 | -71.203 | 6.26 | 1.4101 | 1128 | 39.8 | 3.3688 | medium | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2175 | 34.76 | 1.6381 | -3.2028 | -26.2609 | 4.85 | 1.3612 | 940 | 35.43 | 4.213 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2363 | 32.04 | 1.5446 | -3.9604 | -90.5777 | 6.43 | 1.3201 | 1128 | 30.85 | 2.6502 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2363 | 23.95 | 1.3597 | -5.0 | -19.6375 | 4.59 | 1.3522 | 1128 | 22.07 | 2.2122 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2476 | 41.92 | 0.3579 | -2.0 | -34.6101 | 5.0 | 1.0746 | 1241 | 44.64 | 0.9752 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2476 | 33.56 | 0.3495 | -2.474 | -31.2057 | 3.73 | 1.0857 | 1241 | 33.2 | 0.8223 | medium | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2175 | 43.26 | -0.1133 | -1.2658 | -90.5777 | 5.02 | 0.9739 | 940 | 44.15 | 0.0325 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2467 | 29.47 | -0.1933 | -0.5236 | -36.7391 | 3.55 | 0.9453 | 1232 | 27.11 | -0.4355 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2467 | 30.93 | -0.3435 | -1.6014 | -31.2057 | 3.62 | 0.9125 | 1232 | 29.14 | -0.3088 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2363 | 55.18 | -0.4321 | 5.0 | -90.5777 | 2.75 | 0.8637 | 1128 | 56.03 | -0.4008 | low | False | False |
| long_base_low_position | signal_close_hold_5d | 193 | 46.11 | 2.1004 | -0.6536 | -16.2076 | 5.0 | 1.9247 | 59 | 38.98 | 0.987 | medium | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 159 | 46.54 | 1.8168 | -0.1245 | -22.2365 | 10.0 | 1.7472 | 39 | 58.97 | 2.3487 | medium | True | False |
| long_base_low_position | pullback_10ma_hold_10d | 112 | 50.89 | 1.5342 | 0.2194 | -15.8349 | 10.0 | 1.7955 | 32 | 71.88 | 3.3896 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 171 | 43.86 | 1.0902 | -2.2005 | -22.3164 | 20.0 | 1.2547 | 37 | 48.65 | 2.5483 | medium | True | False |
| long_base_low_position | next_open_hold_5d | 193 | 42.49 | 0.4828 | -1.25 | -19.3503 | 5.0 | 1.1703 | 59 | 38.98 | -0.3014 | medium | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 171 | 37.43 | 0.3952 | -2.0325 | -16.8498 | 4.94 | 1.1367 | 37 | 21.62 | -2.9392 | medium | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 191 | 37.7 | 0.3412 | 0.0 | -14.5788 | 3.79 | 1.1613 | 57 | 31.58 | -0.8096 | medium | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 193 | 35.75 | 0.2212 | -1.6216 | -16.8498 | 3.87 | 1.0792 | 59 | 25.42 | -1.4771 | medium | False | False |
| long_base_low_position | next_open_hold_10d | 181 | 38.12 | 0.1752 | -2.2049 | -20.6215 | 10.0 | 1.0481 | 47 | 27.66 | -1.7387 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 171 | 29.24 | 0.1602 | -2.7848 | -19.2308 | 8.18 | 1.0431 | 37 | 21.62 | -2.0546 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 181 | 39.78 | 0.0724 | -2.3729 | -16.8498 | 6.96 | 1.0211 | 47 | 21.28 | -3.1576 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 171 | 38.6 | 0.0279 | -2.521 | -16.8498 | 6.75 | 1.0079 | 37 | 32.43 | -0.7836 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 128 | 38.28 | -0.1223 | -2.4186 | -20.6215 | 10.0 | 0.9692 | 33 | 27.27 | -3.202 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 191 | 31.94 | -0.1257 | -0.5988 | -24.6561 | 3.77 | 0.944 | 57 | 22.81 | -1.4838 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 181 | 28.18 | -0.129 | -5.0 | -13.961 | 5.99 | 0.9614 | 47 | 17.02 | -2.5786 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 181 | 29.83 | -0.2984 | -2.5084 | -16.8498 | 6.84 | 0.9146 | 47 | 17.02 | -2.8767 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 181 | 47.51 | -0.465 | -0.8824 | -16.8498 | 3.74 | 0.8318 | 47 | 36.17 | -1.5569 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 3816 | 46.99 | 5.4789 | -0.9834 | -91.7928 | 20.0 | 1.9558 | 1451 | 53.89 | 11.565 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2445 | 52.11 | 3.6343 | 0.5096 | -89.805 | 10.0 | 2.1895 | 996 | 59.84 | 6.9749 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3601 | 50.1 | 3.1159 | 0.058 | -91.3518 | 10.0 | 1.8738 | 1440 | 54.86 | 5.7621 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3195 | 45.95 | 2.6238 | -1.0651 | -90.5777 | 10.0 | 1.5354 | 1417 | 48.69 | 4.5935 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4237 | 47.58 | 2.2832 | -0.4425 | -34.3949 | 5.0 | 1.6518 | 1872 | 50.05 | 3.5562 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4071 | 45.12 | 2.0939 | -1.2146 | -90.8539 | 10.0 | 1.4316 | 1706 | 48.42 | 4.199 | high | True | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 3816 | 35.01 | 1.9828 | -3.4783 | -90.5777 | 8.72 | 1.3971 | 1451 | 37.01 | 4.9777 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4071 | 39.7 | 1.5608 | -2.2831 | -71.203 | 6.73 | 1.3823 | 1706 | 41.32 | 3.1323 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4071 | 31.32 | 1.1742 | -3.2753 | -90.5777 | 6.17 | 1.2785 | 1706 | 31.13 | 2.2937 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 3816 | 33.62 | 1.0671 | -2.7088 | -26.2609 | 4.72 | 1.2708 | 1451 | 34.39 | 3.0765 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4071 | 26.38 | 0.9088 | -5.0 | -20.6061 | 5.11 | 1.2497 | 1706 | 23.92 | 1.6126 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4237 | 41.82 | 0.2731 | -1.6561 | -34.6101 | 5.0 | 1.0647 | 1872 | 44.6 | 0.985 | medium | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4237 | 32.74 | 0.1376 | -2.3333 | -31.2057 | 3.66 | 1.0382 | 1872 | 32.53 | 0.6353 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4217 | 29.07 | -0.0716 | -0.4651 | -36.7391 | 3.45 | 0.9763 | 1852 | 27.54 | -0.1905 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 3816 | 38.78 | -0.1743 | -2.6206 | -90.5777 | 5.14 | 0.9558 | 1451 | 41.56 | 0.0782 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4217 | 30.07 | -0.2082 | -1.3825 | -31.2057 | 3.53 | 0.9375 | 1852 | 29.05 | -0.1557 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4071 | 50.45 | -0.4672 | 1.1574 | -90.5777 | 2.91 | 0.8419 | 1706 | 52.93 | -0.4257 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

