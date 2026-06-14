# Historical Pattern Operation Registry

- generated_at: `2026-06-14 21:35:21 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `170409`
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
| current_model_hit_all | next_open_hold_20d | 3685 | 47.11 | 5.5063 | -0.9302 | -91.7928 | 20.0 | 2.0044 | 1304 | 54.52 | 11.9448 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2400 | 52.33 | 3.6871 | 0.551 | -89.805 | 10.0 | 2.2467 | 936 | 60.79 | 7.3882 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3498 | 50.49 | 3.2449 | 0.1608 | -91.3518 | 10.0 | 1.9609 | 1317 | 56.26 | 6.3336 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3019 | 46.04 | 2.896 | -0.9363 | -90.5777 | 10.0 | 1.6351 | 1255 | 49.0 | 5.3001 | high | True | False |
| current_model_hit_all | next_open_hold_10d | 3931 | 45.1 | 2.2853 | -1.1407 | -90.8539 | 10.0 | 1.5016 | 1550 | 48.52 | 4.7594 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4068 | 47.15 | 2.0355 | -0.5307 | -34.3949 | 5.0 | 1.6024 | 1687 | 49.32 | 3.1362 | high | True | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 3685 | 34.3 | 1.8528 | -3.442 | -90.5777 | 8.62 | 1.3822 | 1304 | 35.28 | 4.5977 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 3931 | 39.76 | 1.6748 | -2.2222 | -44.7633 | 6.77 | 1.4328 | 1550 | 40.65 | 3.4197 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 3931 | 31.42 | 1.1488 | -3.2028 | -90.5777 | 6.28 | 1.2762 | 1550 | 30.65 | 2.2962 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 3685 | 33.76 | 1.1003 | -2.5532 | -26.2609 | 4.71 | 1.2925 | 1304 | 33.97 | 3.1273 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 3931 | 26.46 | 0.8691 | -5.0 | -19.9536 | 5.17 | 1.2416 | 1550 | 23.23 | 1.5326 | medium | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 3991 | 30.12 | 0.1463 | -0.5464 | -36.5617 | 3.52 | 1.0511 | 1610 | 28.82 | 0.2436 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 4068 | 41.45 | 0.2019 | -1.6412 | -34.6101 | 5.0 | 1.0497 | 1687 | 43.27 | 0.6396 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4068 | 33.36 | 0.017 | -2.4569 | -31.2057 | 3.75 | 1.0047 | 1687 | 32.9 | 0.2727 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4027 | 31.11 | -0.1063 | -1.3605 | -31.2057 | 3.62 | 0.9667 | 1646 | 30.26 | -0.0535 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 3685 | 39.05 | -0.1658 | -2.6362 | -90.5777 | 5.35 | 0.9579 | 1304 | 41.72 | 0.0264 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 3931 | 50.17 | -0.5048 | 0.2933 | -90.5777 | 3.01 | 0.8304 | 1550 | 51.48 | -0.6177 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 1914 | 47.54 | 6.8845 | -0.8972 | -91.7928 | 20.0 | 2.1455 | 785 | 54.39 | 13.5284 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1185 | 52.91 | 4.6055 | 0.8206 | -89.805 | 10.0 | 2.488 | 542 | 61.25 | 7.8994 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 1783 | 51.6 | 3.8199 | 0.5683 | -91.3518 | 10.0 | 2.0552 | 773 | 57.05 | 6.5925 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2165 | 50.67 | 3.2967 | 0.3306 | -34.3949 | 5.0 | 1.9408 | 1036 | 51.54 | 4.2531 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 1908 | 44.81 | 3.2533 | -1.2489 | -90.5777 | 10.0 | 1.6493 | 873 | 48.22 | 5.8533 | high | True | False |
| limit_up_like_current_hit | next_open_hold_10d | 2069 | 44.8 | 3.1197 | -1.25 | -90.5777 | 10.0 | 1.6282 | 940 | 48.3 | 5.6642 | high | True | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 1914 | 35.16 | 2.8795 | -4.0944 | -90.5777 | 8.89 | 1.5187 | 785 | 35.54 | 6.4738 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2069 | 38.57 | 2.2491 | -2.8056 | -44.7633 | 6.26 | 1.5268 | 940 | 39.68 | 4.1919 | medium | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 1914 | 34.64 | 1.828 | -3.0545 | -26.2609 | 4.84 | 1.4178 | 785 | 34.9 | 4.7296 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2069 | 32.43 | 1.6559 | -3.9568 | -90.5777 | 6.59 | 1.3409 | 940 | 30.85 | 2.9382 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2069 | 23.78 | 1.4324 | -5.0 | -18.1025 | 4.58 | 1.3738 | 940 | 21.38 | 2.4196 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2165 | 41.76 | 0.2806 | -1.9481 | -34.6101 | 5.0 | 1.0604 | 1036 | 44.02 | 0.6008 | medium | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2109 | 31.01 | 0.1491 | -0.6659 | -31.2057 | 3.66 | 1.0439 | 980 | 29.08 | 0.1883 | low | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2165 | 34.09 | 0.129 | -2.7381 | -31.2057 | 3.85 | 1.0309 | 1036 | 33.49 | 0.343 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 1914 | 44.1 | -0.1169 | -1.109 | -90.5777 | 5.26 | 0.9736 | 785 | 44.97 | -0.0433 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2137 | 31.96 | -0.263 | -1.6997 | -31.2057 | 3.74 | 0.9317 | 1008 | 30.26 | -0.233 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2069 | 55.63 | -0.4726 | 5.0 | -90.5777 | 2.84 | 0.8539 | 940 | 55.64 | -0.5872 | low | False | False |
| long_base_low_position | signal_close_hold_5d | 182 | 45.6 | 1.782 | -0.7368 | -16.2076 | 5.0 | 1.7653 | 51 | 37.25 | 0.4858 | medium | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 155 | 46.45 | 1.6363 | -0.1245 | -22.2365 | 10.0 | 1.6603 | 37 | 59.46 | 2.0391 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 164 | 43.29 | 0.8701 | -2.2024 | -22.3164 | 20.0 | 1.2034 | 33 | 48.48 | 2.2785 | medium | True | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 179 | 38.55 | 0.3442 | 0.0 | -14.5788 | 3.85 | 1.1627 | 48 | 35.42 | -0.7432 | medium | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 164 | 37.2 | 0.2744 | -2.0273 | -13.961 | 4.9 | 1.0982 | 33 | 21.21 | -2.8952 | medium | False | False |
| long_base_low_position | next_open_hold_5d | 182 | 40.66 | 0.1626 | -1.3795 | -19.3503 | 5.0 | 1.0558 | 51 | 33.33 | -1.2456 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 107 | 49.53 | 1.3927 | -0.0387 | -15.8349 | 10.0 | 1.6987 | 28 | 67.86 | 2.9614 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 182 | 35.71 | 0.0477 | -1.8898 | -16.2076 | 3.92 | 1.0167 | 51 | 25.49 | -1.9173 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 176 | 31.82 | 0.0157 | -0.5927 | -15.5894 | 3.77 | 1.0075 | 45 | 22.22 | -1.0496 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 164 | 38.41 | 0.0058 | -2.5016 | -16.3594 | 6.82 | 1.0017 | 33 | 33.33 | -0.6116 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 164 | 28.66 | -0.0028 | -2.7542 | -14.9306 | 8.12 | 0.9992 | 33 | 21.21 | -2.1869 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 173 | 39.31 | -0.1621 | -2.3729 | -15.6297 | 6.95 | 0.9514 | 42 | 19.05 | -3.3893 | low | False | False |
| long_base_low_position | next_open_hold_10d | 173 | 36.99 | -0.2077 | -2.3316 | -20.6215 | 10.0 | 0.9436 | 42 | 23.81 | -2.4763 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 173 | 27.17 | -0.4896 | -5.0 | -13.961 | 5.97 | 0.8544 | 42 | 14.29 | -3.0505 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 173 | 46.82 | -0.4896 | -1.1538 | -14.977 | 3.74 | 0.822 | 42 | 33.33 | -1.6921 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 173 | 28.32 | -0.6901 | -2.521 | -15.8485 | 6.79 | 0.8037 | 42 | 11.9 | -3.5361 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 120 | 36.67 | -0.6942 | -2.8066 | -20.6215 | 10.0 | 0.8288 | 28 | 21.43 | -4.5697 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 3521 | 47.29 | 5.7222 | -0.8475 | -91.7928 | 20.0 | 2.0333 | 1271 | 54.68 | 12.1958 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2293 | 52.46 | 3.7941 | 0.5545 | -89.805 | 10.0 | 2.2637 | 908 | 60.57 | 7.5247 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3343 | 50.67 | 3.3195 | 0.2358 | -91.3518 | 10.0 | 1.971 | 1280 | 56.17 | 6.4578 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 2899 | 46.43 | 3.0446 | -0.8602 | -90.5777 | 10.0 | 1.6646 | 1227 | 49.63 | 5.5253 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 3758 | 45.48 | 2.4001 | -1.0807 | -90.8539 | 10.0 | 1.5222 | 1508 | 49.2 | 4.961 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 3886 | 47.22 | 2.0474 | -0.496 | -34.3949 | 5.0 | 1.5972 | 1636 | 49.69 | 3.2188 | high | True | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 3521 | 34.56 | 1.9393 | -3.4796 | -90.5777 | 8.64 | 1.3956 | 1271 | 35.64 | 4.7738 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 3758 | 39.78 | 1.7594 | -2.2048 | -44.7633 | 6.76 | 1.4518 | 1508 | 41.25 | 3.6094 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 3758 | 31.56 | 1.2334 | -3.2353 | -90.5777 | 6.25 | 1.2945 | 1508 | 31.17 | 2.4587 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 3521 | 33.6 | 1.1388 | -2.6144 | -26.2609 | 4.7 | 1.2991 | 1271 | 34.3 | 3.2836 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 3758 | 26.42 | 0.9316 | -5.0 | -19.9536 | 5.13 | 1.2582 | 1508 | 23.47 | 1.6603 | medium | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 3815 | 30.04 | 0.1523 | -0.5396 | -36.5617 | 3.51 | 1.0525 | 1565 | 29.01 | 0.2807 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 3886 | 41.48 | 0.2038 | -1.6779 | -34.6101 | 5.0 | 1.0495 | 1636 | 43.58 | 0.6984 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 3886 | 33.25 | 0.0156 | -2.5 | -31.2057 | 3.74 | 1.0043 | 1636 | 33.13 | 0.341 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 3848 | 30.77 | -0.1273 | -1.4105 | -31.2057 | 3.61 | 0.9607 | 1598 | 30.1 | -0.0328 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 3521 | 39.08 | -0.1738 | -2.6419 | -90.5777 | 5.28 | 0.9561 | 1271 | 41.94 | 0.0429 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 3758 | 50.32 | -0.5055 | 0.8779 | -90.5777 | 2.98 | 0.8307 | 1508 | 51.99 | -0.5877 | low | False | False |

## Research-Only Relaxed Comparison

| event_filter_id | pattern_id | sample_size | win_rate | avg_return | median_return | max_drawdown | out_of_sample_size | out_of_sample_avg_return | confidence_status | out_of_sample_pass | approved_for_daily |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| limit_locked_volume_lt2_research_only | next_open_hold_20d | 538 | 53.53 | 8.4594 | 3.0303 | -55.5556 | 307 | 12.6868 | high | True | False |
| limit_locked_volume_lt2_research_only | pullback_10ma_hold_10d | 344 | 56.69 | 5.167 | 1.6528 | -45.3571 | 195 | 8.4311 | high | True | False |
| limit_locked_volume_lt2_research_only | pullback_5ma_hold_10d | 509 | 55.4 | 4.8776 | 2.3815 | -41.7808 | 301 | 6.7871 | high | True | False |
| limit_locked_volume_lt2_research_only | signal_close_hold_5d | 630 | 53.17 | 3.3799 | 1.2376 | -36.5617 | 399 | 4.585 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_hold_10d | 605 | 50.08 | 3.0809 | 0.1757 | -41.2424 | 374 | 4.7186 | high | True | False |
| limit_locked_volume_lt2_research_only | next_day_break_signal_high_hold_10d | 563 | 49.38 | 2.8123 | 0.0 | -41.2424 | 344 | 4.3333 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_large_black_exit_10d | 605 | 44.79 | 2.1708 | -1.845 | -41.2424 | 374 | 3.1143 | high | True | False |
| limit_locked_volume_lt2_research_only | next_open_10ma_trailing_20d | 538 | 38.48 | 2.2572 | -4.5391 | -28.5587 | 307 | 2.9081 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_signal_low_stop_10d | 605 | 36.69 | 1.8534 | -4.5273 | -23.6842 | 374 | 2.1513 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_5pct_stop_10d | 605 | 24.79 | 1.4669 | -5.0 | -17.9204 | 374 | 2.0473 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_5ma_trailing_20d | 538 | 36.06 | 1.1384 | -2.8571 | -25.7613 | 307 | 2.2007 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_hold_5d | 630 | 46.03 | 0.5399 | -0.8929 | -39.2111 | 399 | 1.4448 | medium | True | False |
| limit_locked_volume_lt2_research_only | chase_day1_signal_low_stop_5d | 630 | 37.94 | 0.2841 | -2.7561 | -23.6842 | 399 | 0.9323 | medium | False | False |
| limit_locked_volume_lt2_research_only | chase_day3_signal_low_stop_5d | 617 | 32.74 | 0.2015 | -1.2012 | -39.2111 | 386 | 0.5529 | medium | False | False |
| limit_locked_volume_lt2_research_only | next_open_tp10_signal_low_stop_20d | 538 | 47.21 | 0.1375 | -1.3487 | -23.6842 | 307 | 0.5811 | low | True | False |
| limit_locked_volume_lt2_research_only | next_open_tp5_signal_low_stop_10d | 605 | 61.49 | -0.1322 | 5.0 | -23.6842 | 374 | 0.0203 | low | False | False |
| limit_locked_volume_lt2_research_only | chase_day2_signal_low_stop_5d | 623 | 34.51 | -0.1529 | -1.8692 | -36.5617 | 392 | 0.2358 | low | False | False |

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

