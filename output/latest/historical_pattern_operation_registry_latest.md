# Historical Pattern Operation Registry

- generated_at: `2026-06-15 16:16:27 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `172419`
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
| current_model_hit_all | next_open_hold_20d | 3898 | 46.69 | 5.166 | -1.1429 | -91.7928 | 20.0 | 1.9134 | 1413 | 53.64 | 11.2334 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2520 | 52.18 | 3.6221 | 0.5169 | -89.805 | 10.0 | 2.2194 | 1002 | 60.68 | 7.199 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3682 | 49.95 | 3.117 | 0.0 | -91.3518 | 10.0 | 1.9044 | 1414 | 55.23 | 6.0161 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3253 | 45.77 | 2.6571 | -1.0695 | -90.5777 | 10.0 | 1.556 | 1389 | 48.67 | 4.8777 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4339 | 47.85 | 2.3793 | -0.4032 | -34.3949 | 5.0 | 1.7016 | 1854 | 50.38 | 3.7079 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 4175 | 44.91 | 2.1205 | -1.2168 | -90.8539 | 10.0 | 1.4484 | 1690 | 48.22 | 4.4253 | high | True | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 3898 | 34.33 | 1.6617 | -3.5044 | -90.5777 | 8.63 | 1.3345 | 1413 | 35.53 | 4.2555 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4175 | 39.76 | 1.581 | -2.2556 | -65.1653 | 6.72 | 1.3967 | 1690 | 40.89 | 3.2195 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4175 | 31.31 | 1.1523 | -3.207 | -90.5777 | 6.21 | 1.2767 | 1690 | 30.77 | 2.2894 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 3898 | 33.86 | 0.9765 | -2.6115 | -26.2609 | 4.72 | 1.2522 | 1413 | 34.25 | 2.8435 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4175 | 26.56 | 0.9131 | -5.0 | -19.9536 | 5.16 | 1.2532 | 1690 | 23.73 | 1.6034 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 4339 | 41.48 | 0.2077 | -1.675 | -34.6101 | 5.0 | 1.0495 | 1854 | 43.53 | 0.7507 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4339 | 33.39 | 0.1513 | -2.4444 | -31.2057 | 3.72 | 1.0418 | 1854 | 33.44 | 0.5818 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4250 | 29.69 | 0.0351 | -0.4788 | -36.5617 | 3.5 | 1.012 | 1765 | 28.39 | 0.0045 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4292 | 30.96 | -0.1026 | -1.3018 | -31.2057 | 3.59 | 0.9683 | 1807 | 30.33 | -0.0178 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 3898 | 38.84 | -0.1668 | -2.5936 | -90.5777 | 5.23 | 0.9575 | 1413 | 41.61 | 0.0575 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4175 | 50.18 | -0.4833 | 0.3279 | -90.5777 | 2.96 | 0.8364 | 1690 | 52.19 | -0.4993 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 2120 | 46.79 | 6.1388 | -1.3448 | -91.7928 | 20.0 | 1.9756 | 894 | 53.02 | 12.2109 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1304 | 52.53 | 4.3986 | 0.6823 | -89.805 | 10.0 | 2.4146 | 608 | 61.02 | 7.5322 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2429 | 51.54 | 3.7784 | 0.5634 | -34.3949 | 5.0 | 2.0736 | 1203 | 52.87 | 4.9791 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 1963 | 50.59 | 3.5388 | 0.165 | -91.3518 | 10.0 | 1.9486 | 870 | 55.29 | 6.0475 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2137 | 44.5 | 2.8529 | -1.3514 | -90.5777 | 10.0 | 1.5379 | 1007 | 47.86 | 5.1971 | high | True | False |
| limit_up_like_current_hit | next_open_hold_10d | 2306 | 44.49 | 2.7402 | -1.3813 | -90.5777 | 10.0 | 1.5224 | 1080 | 47.87 | 5.0241 | high | True | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2120 | 35.09 | 2.4334 | -4.1616 | -90.5777 | 8.88 | 1.4259 | 894 | 35.91 | 5.7041 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2306 | 38.68 | 2.0231 | -2.8495 | -65.1653 | 6.21 | 1.455 | 1080 | 40.19 | 3.7785 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2306 | 32.18 | 1.614 | -3.9496 | -90.5777 | 6.45 | 1.3358 | 1080 | 31.02 | 2.8443 | medium | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2120 | 34.72 | 1.5286 | -3.1782 | -26.2609 | 4.84 | 1.3375 | 894 | 35.23 | 4.0857 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2306 | 24.2 | 1.4555 | -5.0 | -18.1818 | 4.6 | 1.3801 | 1080 | 22.41 | 2.4153 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2429 | 34.13 | 0.3573 | -2.7027 | -31.2057 | 3.78 | 1.0862 | 1203 | 34.25 | 0.8096 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2429 | 41.79 | 0.2822 | -2.0218 | -34.6101 | 5.0 | 1.0584 | 1203 | 44.31 | 0.7773 | medium | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2361 | 30.2 | -0.0518 | -0.5263 | -33.5 | 3.6 | 0.985 | 1135 | 28.37 | -0.1759 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2120 | 43.35 | -0.1232 | -1.2862 | -90.5777 | 5.06 | 0.9718 | 894 | 44.41 | 0.0143 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2395 | 31.61 | -0.2407 | -1.5842 | -31.2057 | 3.67 | 0.9376 | 1169 | 30.37 | -0.1531 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2306 | 55.2 | -0.438 | 5.0 | -90.5777 | 2.76 | 0.8622 | 1080 | 56.2 | -0.4059 | low | False | False |
| long_base_low_position | signal_close_hold_5d | 187 | 46.52 | 2.1482 | -0.6536 | -16.2076 | 5.0 | 1.9347 | 53 | 39.62 | 1.0295 | medium | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 158 | 46.84 | 1.8316 | -0.1048 | -22.2365 | 10.0 | 1.7495 | 38 | 60.53 | 2.4243 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 169 | 43.79 | 1.1269 | -2.2005 | -22.3164 | 20.0 | 1.2618 | 35 | 48.57 | 2.8089 | medium | True | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 184 | 39.13 | 0.4748 | 0.0 | -14.5788 | 3.84 | 1.2288 | 50 | 36.0 | -0.4788 | medium | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 169 | 37.87 | 0.4501 | -2.0221 | -16.8498 | 4.96 | 1.1565 | 35 | 22.86 | -2.8651 | medium | False | False |
| long_base_low_position | next_open_hold_5d | 187 | 41.18 | 0.3449 | -1.3378 | -19.3503 | 5.0 | 1.1182 | 53 | 33.96 | -0.8765 | medium | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 187 | 36.36 | 0.2303 | -1.8265 | -16.8498 | 3.91 | 1.0802 | 53 | 26.42 | -1.6369 | medium | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 169 | 29.59 | 0.2256 | -2.7237 | -19.2308 | 8.22 | 1.061 | 35 | 22.86 | -1.8658 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 109 | 49.54 | 1.4964 | -0.0387 | -15.8349 | 10.0 | 1.7551 | 29 | 68.97 | 3.4394 | low | False | False |
| long_base_low_position | next_open_hold_10d | 178 | 37.64 | 0.1425 | -2.2599 | -20.6215 | 10.0 | 1.0389 | 44 | 25.0 | -2.0017 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 178 | 39.89 | 0.1117 | -2.3522 | -16.8498 | 6.95 | 1.0329 | 44 | 20.45 | -3.2186 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 181 | 32.6 | 0.1018 | -0.4878 | -15.5894 | 3.76 | 1.0499 | 47 | 23.4 | -0.8966 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 169 | 39.05 | 0.0865 | -2.4823 | -16.8498 | 6.69 | 1.0246 | 35 | 34.29 | -0.5474 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 178 | 28.09 | -0.1087 | -5.0 | -13.961 | 5.98 | 0.9673 | 44 | 15.91 | -2.6635 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 125 | 37.6 | -0.1761 | -2.5057 | -20.6215 | 10.0 | 0.956 | 30 | 23.33 | -3.734 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 178 | 29.21 | -0.3392 | -2.5147 | -16.8498 | 6.79 | 0.9033 | 44 | 13.64 | -3.2173 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 178 | 47.19 | -0.4834 | -1.0181 | -16.8498 | 3.68 | 0.8252 | 44 | 34.09 | -1.7056 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 3729 | 46.82 | 5.3491 | -1.0345 | -91.7928 | 20.0 | 1.9357 | 1378 | 53.77 | 11.4474 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2411 | 52.3 | 3.7182 | 0.5476 | -89.805 | 10.0 | 2.2332 | 973 | 60.43 | 7.3111 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3524 | 50.09 | 3.1746 | 0.0421 | -91.3518 | 10.0 | 1.9092 | 1376 | 55.09 | 6.1153 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3128 | 46.1 | 2.7703 | -0.9369 | -90.5777 | 10.0 | 1.576 | 1359 | 49.23 | 5.0678 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4152 | 47.9 | 2.3897 | -0.3891 | -34.3949 | 5.0 | 1.6946 | 1801 | 50.69 | 3.7867 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 3997 | 45.23 | 2.2086 | -1.1538 | -90.8539 | 10.0 | 1.4624 | 1646 | 48.85 | 4.5971 | high | True | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 3729 | 34.54 | 1.7268 | -3.5672 | -90.5777 | 8.64 | 1.3436 | 1378 | 35.85 | 4.4109 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 3997 | 39.75 | 1.6464 | -2.2535 | -65.1653 | 6.71 | 1.4104 | 1646 | 41.43 | 3.3916 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 3997 | 31.4 | 1.2187 | -3.2407 | -90.5777 | 6.18 | 1.2907 | 1646 | 31.23 | 2.4366 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 3729 | 33.68 | 1.0004 | -2.6846 | -26.2609 | 4.71 | 1.2554 | 1378 | 34.54 | 2.9884 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 3997 | 26.49 | 0.9586 | -5.0 | -19.9536 | 5.12 | 1.2649 | 1646 | 23.94 | 1.7174 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4152 | 41.5 | 0.2015 | -1.7229 | -34.6101 | 5.0 | 1.0474 | 1801 | 43.81 | 0.7986 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4152 | 33.26 | 0.1478 | -2.4903 | -31.2057 | 3.71 | 1.0405 | 1801 | 33.65 | 0.6471 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4069 | 29.57 | 0.0321 | -0.4768 | -36.5617 | 3.48 | 1.0108 | 1718 | 28.52 | 0.0292 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4108 | 30.6 | -0.1285 | -1.3586 | -31.2057 | 3.57 | 0.9609 | 1757 | 30.17 | -0.0046 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 3729 | 38.83 | -0.1783 | -2.6087 | -90.5777 | 5.17 | 0.9548 | 1378 | 41.8 | 0.0728 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 3997 | 50.31 | -0.4833 | 0.8487 | -90.5777 | 2.93 | 0.8369 | 1646 | 52.67 | -0.467 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

