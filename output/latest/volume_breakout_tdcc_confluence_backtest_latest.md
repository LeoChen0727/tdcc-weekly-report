# Volume Breakout TDCC Confluence Backtest

- generated_at: `2026-06-14 20:38:08 Asia/Taipei`
- model_id: `volume_range_breakout`
- overlay_model_id: `tdcc_weekly_ranking_formula`
- tdcc_as_of_rule: `tdcc_signal_date <= event_date and tdcc_signal_age_days <= 7`
- confluence_event_rows: `859`
- summary_rows: `2293`
- scope: research only; all rows keep `approved_for_daily=False`.

## Matched Event Counts

| tdcc_list_type | operation_rows | unique_signal_events |
| --- | --- | --- |
| consecutive_accumulation | 127 | 12 |
| weekly_increase | 732 | 63 |

## Best Confluence Rows

| tdcc_list_type | rank_bucket | confluence_scope | confluence_id | pattern_id | sample_size | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass | ranking_research_score | ranking_research_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | tdcc_rank_only | all_current_volume_breakout | signal_close_hold_5d | 11 | 81.82 | 6.6103 | 4.2789 | low | True | 11.59 | 1 |
| consecutive_accumulation | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_5d | 11 | 63.64 | 2.2968 | 4.2857 | low | True | 7.2007 | 4 |
| consecutive_accumulation | top_20 | tdcc_rank_only | all_current_volume_breakout | chase_day2_signal_low_stop_5d | 11 | 36.36 | 1.2829 | 0.0 | low | False | -0.9541 | 7 |
| consecutive_accumulation | top_20 | tdcc_rank_only | all_current_volume_breakout | chase_day3_signal_low_stop_5d | 11 | 36.36 | 3.1269 | -2.0067 | low | False | -1.9303 | 10 |
| consecutive_accumulation | top_20 | tdcc_rank_only | all_current_volume_breakout | chase_day1_signal_low_stop_5d | 11 | 27.27 | -1.7389 | -5.5019 | low | False | -7.2656 | 13 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | signal_close_hold_5d | 12 | 83.33 | 6.1313 | 3.7645 | low | True | 11.1323 | 2 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_5d | 12 | 58.33 | 1.9654 | 3.8724 | low | True | 5.9798 | 6 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_10d | 10 | 50.0 | 0.7897 | 2.5081 | low | True | 3.0627 | 9 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | chase_day2_signal_low_stop_5d | 12 | 33.33 | 0.676 | 0.0 | low | False | -1.2102 | 13 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | chase_day3_signal_low_stop_5d | 12 | 33.33 | 2.6205 | -2.0989 | low | False | -2.2242 | 17 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_tp5_signal_low_stop_10d | 10 | 40.0 | -2.0648 | -3.5606 | low | False | -5.6837 | 20 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_large_black_exit_10d | 10 | 40.0 | -1.2868 | -4.0712 | low | False | -5.7931 | 23 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_signal_low_stop_10d | 10 | 30.0 | -0.9693 | -5.5394 | low | False | -6.9716 | 26 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | chase_day1_signal_low_stop_5d | 12 | 25.0 | -2.2476 | -5.5394 | low | False | -7.5112 | 30 |
| consecutive_accumulation | top_50 | tdcc_rank_only | all_current_volume_breakout | next_open_5pct_stop_10d | 10 | 10.0 | -3.5833 | -5.0 | low | False | -7.6625 | 33 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | pullback_5ma_hold_10d | 14 | 85.71 | 17.3169 | 26.8985 | low | True | 37.3379 | 2 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_day_break_signal_high_hold_10d | 14 | 78.57 | 17.6099 | 19.267 | low | True | 29.6375 | 6 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_10d | 15 | 73.33 | 16.3566 | 19.2833 | low | True | 28.3942 | 8 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_large_black_exit_10d | 15 | 60.0 | 13.0792 | 9.8592 | low | True | 16.6382 | 12 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_signal_low_stop_10d | 15 | 53.33 | 13.7258 | 9.8592 | low | True | 16.0287 | 14 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | signal_close_hold_5d | 19 | 63.16 | 5.1798 | 5.493 | low | True | 9.6266 | 19 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_tp5_signal_low_stop_10d | 15 | 60.0 | 0.9639 | 5.0 | low | True | 6.813 | 23 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_5d | 19 | 52.63 | 3.0061 | 3.673 | low | True | 5.5889 | 25 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | chase_day3_signal_low_stop_5d | 18 | 44.44 | 3.6242 | 0.0 | low | True | 2.1958 | 27 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | chase_day2_signal_low_stop_5d | 18 | 38.89 | 1.6528 | 0.0 | low | False | -0.6914 | 30 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | chase_day1_signal_low_stop_5d | 19 | 36.84 | 0.3213 | -2.4324 | low | False | -3.4691 | 34 |
| weekly_increase | top_10 | tdcc_rank_only | all_current_volume_breakout | next_open_5pct_stop_10d | 15 | 13.33 | 0.4652 | -5.0 | low | False | -5.7614 | 37 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_open_hold_10d | 11 | 90.91 | 30.5287 | 34.981 | low | True | 51.2123 | 1 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_day_break_signal_high_hold_10d | 11 | 90.91 | 30.0784 | 34.8449 | low | True | 50.8872 | 2 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_open_signal_low_stop_10d | 11 | 81.82 | 30.0052 | 34.981 | low | True | 49.7496 | 3 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_open_large_black_exit_10d | 11 | 81.82 | 27.3761 | 34.981 | low | True | 48.5665 | 4 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | pullback_5ma_hold_10d | 10 | 100.0 | 27.1067 | 25.8633 | low | True | 42.675 | 6 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | pullback_5ma_hold_10d | 11 | 100.0 | 19.7047 | 26.0434 | low | True | 39.5248 | 8 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | pullback_10ma_hold_10d | 10 | 90.0 | 25.6286 | 20.3781 | low | False | 33.7232 | 9 |
| weekly_increase | top_20 | tdcc_classification | high_position_breakout | pullback_5ma_hold_10d | 10 | 90.0 | 23.4589 | 21.2554 | low | False | 33.5364 | 11 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_day_break_signal_high_hold_10d | 12 | 75.0 | 22.5761 | 17.267 | low | True | 29.5602 | 13 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_20d | 12 | 58.33 | 25.3861 | 18.1987 | low | True | 29.4128 | 14 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | pullback_5ma_hold_10d | 25 | 88.0 | 20.1695 | 14.1626 | low | True | 27.5817 | 16 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_day_break_signal_high_hold_10d | 11 | 72.73 | 23.6099 | 12.5 | low | True | 25.4116 | 18 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | next_day_break_signal_high_hold_10d | 11 | 63.64 | 15.7067 | 16.5 | low | True | 24.228 | 21 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | signal_close_hold_5d | 11 | 100.0 | 12.914 | 12.1718 | low | True | 23.9845 | 23 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_open_hold_10d | 12 | 75.0 | 21.7892 | 11.1796 | low | True | 23.7274 | 24 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_open_hold_10d | 13 | 69.23 | 20.4077 | 12.5 | low | True | 23.5308 | 25 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_10d | 32 | 59.38 | 11.5261 | 5.9687 | medium | True | 20.837 | 27 |
| weekly_increase | top_20 | tdcc_classification | high_position_breakout | next_day_break_signal_high_hold_10d | 10 | 60.0 | 16.157 | 13.9372 | low | False | 19.6141 | 29 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_open_large_black_exit_10d | 13 | 61.54 | 17.2246 | 9.8592 | low | True | 18.6835 | 31 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_day_break_signal_high_hold_10d | 28 | 64.29 | 13.8664 | 9.513 | low | True | 17.382 | 35 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_open_large_black_exit_10d | 12 | 66.67 | 18.6129 | 6.8046 | low | True | 17.236 | 37 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | signal_close_hold_5d | 16 | 87.5 | 9.5126 | 7.9536 | low | True | 17.0433 | 38 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_open_signal_low_stop_10d | 13 | 53.85 | 16.8089 | 9.1667 | low | True | 16.8351 | 39 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | next_open_hold_10d | 13 | 53.85 | 12.2873 | 11.3744 | low | True | 16.7873 | 40 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | chase_day1_signal_low_stop_5d | 11 | 81.82 | 9.2784 | 8.5551 | low | True | 16.6392 | 41 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_open_hold_5d | 11 | 81.82 | 9.2784 | 8.5551 | low | True | 16.6392 | 42 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_open_hold_5d | 16 | 75.0 | 6.8602 | 7.8736 | low | True | 14.0902 | 45 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | next_open_tp5_signal_low_stop_10d | 11 | 100.0 | 5.0 | 5.0 | low | True | 13.9686 | 46 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | signal_close_hold_5d | 36 | 63.89 | 4.0375 | 4.3326 | medium | True | 13.8195 | 48 |
| weekly_increase | top_20 | tdcc_classification | high_position_breakout | next_open_hold_10d | 12 | 58.33 | 12.9921 | 5.9317 | low | True | 12.7952 | 50 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | signal_close_hold_5d | 16 | 68.75 | 7.1287 | 6.5229 | low | True | 12.1516 | 52 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_open_signal_low_stop_10d | 12 | 50.0 | 17.3723 | 3.0784 | low | True | 11.0737 | 53 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_large_black_exit_10d | 32 | 53.12 | 9.8922 | 1.0553 | medium | True | 10.833 | 54 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_open_hold_5d | 16 | 62.5 | 4.7999 | 6.0809 | low | True | 9.8621 | 57 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | chase_day3_signal_low_stop_5d | 11 | 63.64 | 6.161 | 2.7397 | low | True | 7.5482 | 63 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_tp5_signal_low_stop_10d | 32 | 53.12 | -0.3666 | 5.0 | medium | False | 7.0559 | 64 |
| weekly_increase | top_20 | tdcc_classification | limit_up_like_breakout | next_open_tp5_signal_low_stop_10d | 13 | 61.54 | 0.4875 | 5.0 | low | True | 6.7785 | 67 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | next_open_tp5_signal_low_stop_10d | 13 | 61.54 | 0.2678 | 5.0 | low | True | 6.6797 | 68 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | next_open_tp5_signal_low_stop_10d | 12 | 58.33 | 0.04 | 5.0 | low | True | 6.1282 | 70 |
| weekly_increase | top_20 | tdcc_classification | high_position_breakout | next_open_tp5_signal_low_stop_10d | 12 | 58.33 | -0.198 | 5.0 | low | True | 6.0211 | 71 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_tp10_signal_low_stop_20d | 12 | 50.0 | 1.9553 | 5.0 | low | True | 5.8655 | 73 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_10ma_trailing_20d | 12 | 41.67 | 17.9292 | -3.001 | low | True | 5.8529 | 75 |
| weekly_increase | top_20 | tdcc_follow_through | break_signal_low | pullback_5ma_hold_10d | 10 | 70.0 | 4.0593 | 3.1098 | low | False | 5.7755 | 77 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | signal_close_hold_5d | 13 | 61.54 | 2.3932 | 2.5219 | low | True | 5.4058 | 78 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_5ma_trailing_20d | 12 | 50.0 | 11.6601 | -0.4824 | low | True | 5.2985 | 79 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | next_open_signal_low_stop_10d | 13 | 46.15 | 10.6908 | -0.8584 | low | True | 4.5396 | 81 |
| weekly_increase | top_20 | tdcc_classification | high_position_breakout | next_open_large_black_exit_10d | 12 | 50.0 | 10.2844 | -0.8716 | low | True | 4.3292 | 83 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_signal_low_stop_10d | 32 | 40.62 | 9.8849 | -1.6418 | medium | False | 4.0798 | 84 |
| weekly_increase | top_20 | tdcc_follow_through | next_day_continuation | chase_day2_signal_low_stop_5d | 11 | 54.55 | 3.5658 | 1.5 | low | True | 4.0375 | 86 |
| weekly_increase | top_20 | tdcc_attack_method | volume_attack | next_open_large_black_exit_10d | 13 | 46.15 | 9.5367 | -2.2321 | low | True | 2.7839 | 88 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | next_open_hold_5d | 36 | 50.0 | 1.3057 | 0.1956 | medium | True | 2.4399 | 90 |
| weekly_increase | top_20 | tdcc_attack_method | general_breakout | chase_day3_signal_low_stop_5d | 15 | 46.67 | 6.6167 | 0.0 | low | False | 1.5068 | 94 |
| weekly_increase | top_20 | tdcc_rank_only | all_current_volume_breakout | chase_day3_signal_low_stop_5d | 35 | 37.14 | 3.0751 | 0.0 | medium | False | 1.4644 | 95 |
