# Historical Pattern Operation Registry

- generated_at: `2026-06-21 00:37:55 Asia/Taipei`
- model_id: `volume_range_breakout`
- detail_rows: `176957`
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
| current_model_hit_all | next_open_hold_20d | 3944 | 47.59 | 5.0251 | -0.782 | -91.7928 | 20.0 | 1.8984 | 1518 | 53.43 | 9.3361 | high | True | False |
| current_model_hit_all | pullback_10ma_hold_10d | 2573 | 51.92 | 3.7054 | 0.5025 | -89.805 | 10.0 | 2.2441 | 1083 | 58.54 | 6.5898 | high | True | False |
| current_model_hit_all | pullback_5ma_hold_10d | 3834 | 49.27 | 2.9539 | -0.1354 | -91.3518 | 10.0 | 1.8433 | 1621 | 50.65 | 4.4179 | high | True | False |
| current_model_hit_all | signal_close_hold_5d | 4402 | 47.98 | 2.1757 | -0.3853 | -37.4194 | 5.0 | 1.6279 | 1976 | 49.7 | 2.9952 | high | True | False |
| current_model_hit_all | next_day_break_signal_high_hold_10d | 3382 | 44.91 | 1.896 | -1.3348 | -90.5777 | 10.0 | 1.3856 | 1557 | 44.77 | 2.3303 | medium | False | False |
| current_model_hit_all | next_open_hold_10d | 4313 | 44.19 | 1.5284 | -1.5228 | -90.8539 | 10.0 | 1.315 | 1887 | 44.36 | 2.0571 | medium | False | False |
| current_model_hit_all | next_open_10ma_trailing_20d | 3944 | 35.52 | 1.314 | -3.349 | -90.5777 | 8.71 | 1.2687 | 1518 | 36.89 | 2.529 | medium | False | False |
| current_model_hit_all | next_open_large_black_exit_10d | 4313 | 39.18 | 0.9993 | -2.5 | -47.7462 | 6.67 | 1.2424 | 1887 | 38.74 | 1.3955 | medium | False | False |
| current_model_hit_all | next_open_signal_low_stop_10d | 4313 | 30.7 | 0.4733 | -3.5398 | -90.5777 | 6.16 | 1.1087 | 1887 | 28.03 | 0.3319 | medium | False | False |
| current_model_hit_all | next_open_5pct_stop_10d | 4313 | 25.53 | 0.3689 | -5.0 | -19.9536 | 5.01 | 1.0998 | 1887 | 21.36 | 0.0917 | medium | False | False |
| current_model_hit_all | next_open_5ma_trailing_20d | 3944 | 34.2 | 0.2614 | -2.6959 | -26.2609 | 4.69 | 1.0671 | 1518 | 34.58 | 0.6329 | medium | False | False |
| current_model_hit_all | next_open_hold_5d | 4402 | 41.48 | 0.0553 | -1.7736 | -36.7391 | 5.0 | 1.013 | 1976 | 42.66 | 0.2495 | low | False | False |
| current_model_hit_all | chase_day1_signal_low_stop_5d | 4402 | 33.35 | -0.0167 | -2.5755 | -26.1603 | 3.72 | 0.9955 | 1976 | 32.19 | 0.1081 | low | False | False |
| current_model_hit_all | next_open_tp10_signal_low_stop_20d | 3944 | 39.88 | -0.0744 | -2.6126 | -90.5777 | 5.24 | 0.9811 | 1518 | 42.16 | 0.1343 | low | False | False |
| current_model_hit_all | chase_day3_signal_low_stop_5d | 4368 | 29.3 | -0.1407 | -0.4765 | -30.999 | 3.47 | 0.9525 | 1942 | 26.78 | -0.5089 | low | False | False |
| current_model_hit_all | chase_day2_signal_low_stop_5d | 4390 | 30.59 | -0.2959 | -1.3684 | -28.5714 | 3.56 | 0.9104 | 1964 | 28.72 | -0.5049 | low | False | False |
| current_model_hit_all | next_open_tp5_signal_low_stop_10d | 4313 | 50.08 | -0.6078 | 0.22 | -90.5777 | 2.94 | 0.8023 | 1887 | 49.87 | -0.8523 | low | False | False |
| limit_up_like_current_hit | next_open_hold_20d | 2158 | 47.5 | 5.2574 | -1.0147 | -91.7928 | 20.0 | 1.8346 | 950 | 52.53 | 8.7601 | high | True | False |
| limit_up_like_current_hit | pullback_10ma_hold_10d | 1357 | 52.32 | 4.3586 | 0.6662 | -89.805 | 10.0 | 2.3695 | 666 | 58.86 | 6.7229 | high | True | False |
| limit_up_like_current_hit | signal_close_hold_5d | 2475 | 51.68 | 3.4145 | 0.6472 | -37.4194 | 5.0 | 1.9373 | 1267 | 52.64 | 4.1807 | high | True | False |
| limit_up_like_current_hit | pullback_5ma_hold_10d | 2095 | 49.36 | 3.2472 | -0.2004 | -91.3518 | 10.0 | 1.8495 | 1018 | 50.1 | 4.2963 | high | True | False |
| limit_up_like_current_hit | next_day_break_signal_high_hold_10d | 2238 | 43.25 | 1.7194 | -1.8251 | -90.5777 | 10.0 | 1.3126 | 1125 | 43.38 | 2.0274 | medium | False | False |
| limit_up_like_current_hit | next_open_hold_10d | 2419 | 43.16 | 1.6773 | -1.9133 | -90.5777 | 10.0 | 1.3085 | 1211 | 43.19 | 1.8952 | medium | False | False |
| limit_up_like_current_hit | next_open_10ma_trailing_20d | 2158 | 36.01 | 1.3582 | -4.112 | -90.5777 | 8.93 | 1.2405 | 950 | 36.74 | 2.4187 | medium | False | False |
| limit_up_like_current_hit | next_open_large_black_exit_10d | 2419 | 37.58 | 1.0105 | -3.1646 | -47.7462 | 6.15 | 1.2191 | 1211 | 37.32 | 1.2524 | medium | False | False |
| limit_up_like_current_hit | next_open_5pct_stop_10d | 2419 | 22.65 | 0.5131 | -5.0 | -18.1818 | 4.43 | 1.1304 | 1211 | 19.41 | 0.2734 | medium | False | False |
| limit_up_like_current_hit | next_open_signal_low_stop_10d | 2419 | 31.05 | 0.4869 | -4.5187 | -90.5777 | 6.35 | 1.0967 | 1211 | 27.99 | 0.2052 | medium | False | False |
| limit_up_like_current_hit | chase_day1_signal_low_stop_5d | 2475 | 34.14 | 0.1376 | -2.8112 | -26.1603 | 3.77 | 1.0328 | 1267 | 33.46 | 0.3589 | low | False | False |
| limit_up_like_current_hit | next_open_5ma_trailing_20d | 2158 | 34.8 | 0.0925 | -3.3003 | -26.2609 | 4.78 | 1.0204 | 950 | 35.37 | 0.4672 | low | False | False |
| limit_up_like_current_hit | next_open_hold_5d | 2475 | 41.62 | 0.0102 | -2.1518 | -36.7391 | 5.0 | 1.0021 | 1267 | 43.41 | 0.2221 | low | False | False |
| limit_up_like_current_hit | next_open_tp10_signal_low_stop_20d | 2158 | 44.11 | -0.0796 | -1.3821 | -90.5777 | 5.07 | 0.9819 | 950 | 44.53 | 0.0088 | low | False | False |
| limit_up_like_current_hit | chase_day3_signal_low_stop_5d | 2458 | 29.21 | -0.3718 | -0.5642 | -30.999 | 3.55 | 0.8936 | 1250 | 26.16 | -0.9055 | low | False | False |
| limit_up_like_current_hit | chase_day2_signal_low_stop_5d | 2469 | 31.11 | -0.5501 | -1.5968 | -28.5714 | 3.63 | 0.8595 | 1261 | 28.87 | -0.7735 | low | False | False |
| limit_up_like_current_hit | next_open_tp5_signal_low_stop_10d | 2419 | 54.61 | -0.6161 | 5.0 | -90.5777 | 2.74 | 0.8148 | 1211 | 53.43 | -0.8196 | low | False | False |
| long_base_low_position | pullback_5ma_hold_10d | 122 | 48.36 | 2.3437 | 0.0 | -15.5556 | 10.0 | 2.0968 | 50 | 54.0 | 2.0437 | medium | True | False |
| long_base_low_position | next_open_hold_20d | 117 | 44.44 | 1.9027 | -1.9856 | -22.3164 | 20.0 | 1.4862 | 38 | 44.74 | 3.2893 | medium | False | False |
| long_base_low_position | signal_close_hold_5d | 142 | 42.25 | 1.2813 | -1.099 | -15.572 | 5.0 | 1.5222 | 63 | 38.1 | 1.0786 | medium | False | False |
| long_base_low_position | pullback_10ma_hold_10d | 84 | 54.76 | 1.8835 | 0.5876 | -11.9374 | 10.0 | 2.1939 | 32 | 71.88 | 3.2597 | low | False | False |
| long_base_low_position | chase_day2_signal_low_stop_5d | 142 | 35.92 | -0.0172 | -0.12 | -15.0198 | 3.63 | 0.992 | 63 | 31.75 | -0.8658 | low | False | False |
| long_base_low_position | next_open_10ma_trailing_20d | 117 | 29.91 | -0.1357 | -3.0336 | -19.2308 | 8.05 | 0.9653 | 38 | 26.32 | -1.7777 | low | False | False |
| long_base_low_position | next_open_hold_5d | 142 | 39.44 | -0.2271 | -1.4021 | -19.3503 | 5.0 | 0.9254 | 63 | 33.33 | -0.5536 | low | False | False |
| long_base_low_position | next_open_tp10_signal_low_stop_20d | 117 | 36.75 | -0.2276 | -2.4823 | -16.8498 | 6.56 | 0.9346 | 38 | 34.21 | -0.7445 | low | False | False |
| long_base_low_position | chase_day3_signal_low_stop_5d | 142 | 30.28 | -0.2401 | -0.5639 | -15.5894 | 3.64 | 0.89 | 63 | 25.4 | -1.0893 | low | False | False |
| long_base_low_position | next_open_5ma_trailing_20d | 117 | 35.04 | -0.5197 | -2.4818 | -16.8498 | 4.65 | 0.8307 | 38 | 21.05 | -2.82 | low | False | False |
| long_base_low_position | chase_day1_signal_low_stop_5d | 142 | 31.69 | -0.6498 | -2.1601 | -16.8498 | 3.71 | 0.7876 | 63 | 22.22 | -1.8638 | low | False | False |
| long_base_low_position | next_open_large_black_exit_10d | 140 | 35.71 | -0.6498 | -2.9486 | -16.8498 | 7.0 | 0.8172 | 61 | 26.23 | -2.4776 | low | False | False |
| long_base_low_position | next_open_hold_10d | 140 | 35.71 | -0.658 | -2.7622 | -20.6215 | 10.0 | 0.8268 | 61 | 29.51 | -1.7162 | low | False | False |
| long_base_low_position | next_open_5pct_stop_10d | 140 | 26.43 | -1.0943 | -5.0 | -13.961 | 5.56 | 0.6899 | 61 | 18.03 | -2.6272 | low | False | False |
| long_base_low_position | next_open_tp5_signal_low_stop_10d | 140 | 39.29 | -1.2924 | -2.225 | -16.8498 | 3.85 | 0.5947 | 61 | 29.51 | -2.3591 | low | False | False |
| long_base_low_position | next_open_signal_low_stop_10d | 140 | 25.0 | -1.5323 | -2.9909 | -16.8498 | 6.33 | 0.607 | 61 | 14.75 | -3.3534 | low | False | False |
| long_base_low_position | next_day_break_signal_high_hold_10d | 92 | 32.61 | -1.5496 | -3.151 | -20.6215 | 10.0 | 0.6462 | 41 | 26.83 | -2.7178 | low | False | False |
| simple_or_high_position_breakout | next_open_hold_20d | 3827 | 47.69 | 5.1206 | -0.7389 | -91.7928 | 20.0 | 1.9072 | 1480 | 53.65 | 9.4913 | high | True | False |
| simple_or_high_position_breakout | pullback_10ma_hold_10d | 2489 | 51.83 | 3.7668 | 0.4071 | -89.805 | 10.0 | 2.245 | 1051 | 58.14 | 6.6912 | high | True | False |
| simple_or_high_position_breakout | pullback_5ma_hold_10d | 3712 | 49.3 | 2.9739 | -0.1613 | -91.3518 | 10.0 | 1.8383 | 1571 | 50.54 | 4.4934 | high | True | False |
| simple_or_high_position_breakout | signal_close_hold_5d | 4260 | 48.17 | 2.2055 | -0.361 | -37.4194 | 5.0 | 1.6304 | 1913 | 50.08 | 3.0583 | high | True | False |
| simple_or_high_position_breakout | next_day_break_signal_high_hold_10d | 3290 | 45.26 | 1.9924 | -1.2665 | -90.5777 | 10.0 | 1.4039 | 1516 | 45.25 | 2.4669 | high | True | False |
| simple_or_high_position_breakout | next_open_hold_10d | 4173 | 44.48 | 1.6017 | -1.4599 | -90.8539 | 10.0 | 1.3277 | 1826 | 44.85 | 2.1832 | medium | False | False |
| simple_or_high_position_breakout | next_open_10ma_trailing_20d | 3827 | 35.69 | 1.3583 | -3.3735 | -90.5777 | 8.73 | 1.276 | 1480 | 37.16 | 2.6395 | medium | False | False |
| simple_or_high_position_breakout | next_open_large_black_exit_10d | 4173 | 39.3 | 1.0546 | -2.5 | -47.7462 | 6.66 | 1.2547 | 1826 | 39.16 | 1.5249 | medium | False | False |
| simple_or_high_position_breakout | next_open_signal_low_stop_10d | 4173 | 30.89 | 0.5406 | -3.5623 | -90.5777 | 6.16 | 1.1238 | 1826 | 28.48 | 0.455 | medium | False | False |
| simple_or_high_position_breakout | next_open_5pct_stop_10d | 4173 | 25.5 | 0.418 | -5.0 | -19.9536 | 4.99 | 1.1129 | 1826 | 21.47 | 0.1825 | medium | False | False |
| simple_or_high_position_breakout | next_open_5ma_trailing_20d | 3827 | 34.18 | 0.2853 | -2.7027 | -26.2609 | 4.7 | 1.0728 | 1480 | 34.93 | 0.7215 | medium | False | False |
| simple_or_high_position_breakout | next_open_hold_5d | 4260 | 41.55 | 0.0647 | -1.7881 | -36.7391 | 5.0 | 1.015 | 1913 | 42.97 | 0.2759 | low | False | False |
| simple_or_high_position_breakout | chase_day1_signal_low_stop_5d | 4260 | 33.4 | 0.0044 | -2.6115 | -26.1603 | 3.72 | 1.0012 | 1913 | 32.51 | 0.1731 | low | False | False |
| simple_or_high_position_breakout | next_open_tp10_signal_low_stop_20d | 3827 | 39.98 | -0.0697 | -2.6247 | -90.5777 | 5.2 | 0.9824 | 1480 | 42.36 | 0.1569 | low | False | False |
| simple_or_high_position_breakout | chase_day3_signal_low_stop_5d | 4226 | 29.27 | -0.1373 | -0.475 | -30.999 | 3.46 | 0.9541 | 1879 | 26.82 | -0.4894 | low | False | False |
| simple_or_high_position_breakout | chase_day2_signal_low_stop_5d | 4248 | 30.41 | -0.3052 | -1.4105 | -28.5714 | 3.56 | 0.9087 | 1901 | 28.62 | -0.493 | low | False | False |
| simple_or_high_position_breakout | next_open_tp5_signal_low_stop_10d | 4173 | 50.44 | -0.5848 | 1.1574 | -90.5777 | 2.91 | 0.8096 | 1826 | 50.55 | -0.802 | low | False | False |

## Research-Only Relaxed Comparison

_No rows._

## Promotion Gate

- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.
- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.

