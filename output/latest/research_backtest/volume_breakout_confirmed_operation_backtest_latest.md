# Volume Breakout Confirmed Operation Backtest

- generated_at: `2026-07-08 16:30:27 Asia/Taipei`
- model_id: `volume_range_breakout`
- entry_rule: `confirmation_next_open`
- stop_exit_rule: `signal_low_stop_or_fixed_10d_close`
- tdcc_as_of_rule: `tdcc_signal_date <= confirmation_date and tdcc_signal_age_days <= 7`
- event_rows: `8184`
- summary_rows: `368`
- scope: research only; all rows keep `approved_for_daily=False`.

## Event Counts

| tdcc_list_type | trigger_id | event_rows | unique_confirmations |
| --- | --- | --- | --- |
| consecutive_accumulation | next_day_break_signal_high_confirmed | 11 | 11 |
| consecutive_accumulation | next_day_continuation_confirmed | 10 | 10 |
| consecutive_accumulation | pullback_10ma_confirmed | 14 | 10 |
| consecutive_accumulation | pullback_5ma_confirmed | 33 | 23 |
| no_tdcc | next_day_break_signal_high_confirmed | 2314 | 2314 |
| no_tdcc | next_day_continuation_confirmed | 2082 | 2082 |
| no_tdcc | pullback_10ma_confirmed | 1175 | 973 |
| no_tdcc | pullback_5ma_confirmed | 2290 | 1774 |
| weekly_increase | next_day_break_signal_high_confirmed | 73 | 73 |
| weekly_increase | next_day_continuation_confirmed | 67 | 67 |
| weekly_increase | pullback_10ma_confirmed | 27 | 23 |
| weekly_increase | pullback_5ma_confirmed | 88 | 60 |

## Best Rows

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | sample_size | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass | ranking_research_score | ranking_research_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 39 | 74.36 | 14.0534 | 13.5714 | medium | True | 38.4849 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 33 | 63.64 | 17.135 | 13.5714 | medium | True | 37.9277 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 32 | 62.5 | 16.3623 | 13.0357 | medium | True | 36.2354 | 2 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 41 | 73.17 | 13.3462 | 12.5 | medium | True | 36.0514 | 2 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 13 | 84.62 | 24.4413 | 19.0476 | low | True | 34.0953 | 1 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_price_position | high_position | 13 | 84.62 | 24.4413 | 19.0476 | low | True | 34.0953 | 2 |
| consecutive_accumulation | top_10 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 10 | 80.0 | 23.7908 | 19.0476 | low | True | 33.0237 | 1 |
| consecutive_accumulation | top_10 | pullback_10ma_confirmed | operation_price_position | high_position | 10 | 80.0 | 23.7908 | 19.0476 | low | True | 33.0237 | 2 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 14 | 78.57 | 22.6955 | 19.0476 | low | True | 32.3713 | 3 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | 14 | 78.57 | 22.6955 | 19.0476 | low | True | 32.3713 | 4 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | 15 | 80.0 | 20.618 | 19.0476 | low | True | 31.6752 | 1 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | 15 | 80.0 | 20.618 | 19.0476 | low | True | 31.6752 | 2 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | 15 | 80.0 | 20.618 | 19.0476 | low | True | 31.6752 | 3 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | 26 | 80.77 | 18.9981 | 15.3268 | low | True | 27.8263 | 4 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 23 | 78.26 | 21.1229 | 13.6842 | low | True | 26.8848 | 3 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 27 | 74.07 | 21.5491 | 13.6842 | low | True | 26.448 | 3 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 22 | 77.27 | 20.1801 | 13.6278 | low | True | 26.2452 | 4 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 26 | 73.08 | 20.7678 | 13.6278 | low | True | 25.8824 | 4 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 27 | 77.78 | 18.1864 | 11.6059 | low | True | 23.6487 | 5 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 27 | 77.78 | 12.9955 | 13.5714 | low | True | 23.0817 | 3 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 27 | 77.78 | 12.9955 | 13.5714 | low | True | 23.0817 | 4 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 27 | 77.78 | 12.9955 | 13.5714 | low | True | 23.0817 | 5 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 24 | 70.83 | 15.4311 | 13.5714 | low | True | 23.0601 | 1 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 17 | 70.59 | 14.9765 | 13.7778 | low | True | 22.9361 | 2 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 17 | 70.59 | 14.9765 | 13.7778 | low | True | 22.9361 | 3 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 17 | 70.59 | 14.9765 | 13.7778 | low | True | 22.9361 | 4 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_classification | high_position_breakout | 11 | 81.82 | 16.7892 | 10.3527 | low | True | 22.3528 | 6 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 19 | 68.42 | 15.589 | 12.5 | low | True | 21.7416 | 5 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 19 | 68.42 | 15.589 | 12.5 | low | True | 21.7416 | 6 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 68.42 | 15.589 | 12.5 | low | True | 21.7416 | 7 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 17 | 70.59 | 14.6773 | 12.5 | low | True | 21.6514 | 5 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 17 | 70.59 | 14.6773 | 12.5 | low | True | 21.6514 | 6 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 17 | 70.59 | 14.6773 | 12.5 | low | True | 21.6514 | 7 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 30 | 56.67 | 13.401 | 4.7286 | medium | True | 20.0024 | 6 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 30 | 56.67 | 13.401 | 4.7286 | medium | True | 20.0024 | 7 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 30 | 56.67 | 13.401 | 4.7286 | medium | True | 20.0024 | 8 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 18 | 61.11 | 17.5798 | 10.7574 | low | True | 19.9073 | 5 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 18 | 61.11 | 17.5798 | 10.7574 | low | True | 19.9073 | 6 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 18 | 61.11 | 17.5798 | 10.7574 | low | True | 19.9073 | 7 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 26 | 69.23 | 14.2099 | 10.5662 | low | True | 19.5695 | 8 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 24 | 58.33 | 12.0792 | 12.2059 | low | True | 18.354 | 5 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 24 | 58.33 | 12.0792 | 12.2059 | low | True | 18.354 | 6 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 24 | 58.33 | 12.0792 | 12.2059 | low | True | 18.354 | 7 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 19 | 57.89 | 16.4216 | 9.5745 | low | True | 17.8249 | 9 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 19 | 57.89 | 16.4216 | 9.5745 | low | True | 17.8249 | 10 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 57.89 | 16.4216 | 9.5745 | low | True | 17.8249 | 11 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 21 | 57.14 | 15.6457 | 9.5745 | low | True | 17.3772 | 12 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | 21 | 57.14 | 15.6457 | 9.5745 | low | True | 17.3772 | 13 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_price_position | high_position | 12 | 66.67 | 9.5262 | 10.9685 | low | True | 17.2696 | 9 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 57 | 54.39 | 7.9256 | 5.8491 | medium | True | 17.1871 | 7 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 81 | 58.02 | 9.3319 | 3.9773 | medium | True | 16.5015 | 8 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 88 | 57.95 | 9.2003 | 3.8957 | medium | True | 16.289 | 9 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 12 | 66.67 | 16.4336 | 5.7691 | low | True | 15.6985 | 10 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 24 | 54.17 | 13.7568 | 8.9817 | low | True | 15.552 | 14 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 24 | 54.17 | 13.7568 | 8.9817 | low | True | 15.552 | 15 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 13 | 61.54 | 8.5689 | 10.3311 | low | True | 15.4728 | 11 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 17 | 76.47 | 8.6888 | 7.561 | low | True | 15.4376 | 10 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 15 | 73.33 | 8.9565 | 7.561 | low | True | 15.039 | 11 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 31 | 54.84 | 12.8259 | 1.0684 | medium | True | 13.611 | 12 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 31 | 54.84 | 12.8259 | 1.0684 | medium | True | 13.611 | 13 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 31 | 54.84 | 12.8259 | 1.0684 | medium | True | 13.611 | 14 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 60 | 53.33 | 7.5569 | 3.4407 | medium | True | 13.0365 | 12 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 60 | 53.33 | 7.5569 | 3.4407 | medium | True | 13.0365 | 13 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 24 | 66.67 | 12.672 | 3.8957 | low | True | 12.4552 | 14 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 37 | 51.35 | 12.4409 | 0.7557 | medium | True | 11.9948 | 15 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | 37 | 51.35 | 12.4409 | 0.7557 | medium | True | 11.9948 | 16 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | 11 | 54.55 | 18.955 | 2.2727 | low | True | 11.7604 | 15 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 40 | 50.0 | 11.5479 | -0.0514 | medium | True | 9.7854 | 17 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 40 | 50.0 | 11.5479 | -0.0514 | medium | True | 9.7854 | 18 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | 18 | 66.67 | 6.933 | 3.707 | low | False | 7.6465 | 1 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | high_position_breakout | 12 | 50.0 | 9.7728 | -0.0653 | low | True | 4.8246 | 16 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 67 | 47.76 | 8.7639 | -0.9346 | medium | False | 4.5406 | 17 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | 67 | 47.76 | 8.7639 | -0.9346 | medium | False | 4.5406 | 18 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 55 | 47.27 | 8.5438 | -0.9346 | medium | False | 4.3112 | 19 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 55 | 47.27 | 8.5438 | -0.9346 | medium | False | 4.3112 | 20 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 55 | 47.27 | 8.5438 | -0.9346 | medium | False | 4.3112 | 21 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 56 | 46.43 | 8.3121 | -1.5784 | medium | False | 3.1776 | 22 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 56 | 46.43 | 8.3121 | -1.5784 | medium | False | 3.1776 | 23 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 56 | 46.43 | 8.3121 | -1.5784 | medium | False | 3.1776 | 24 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | volume_attack__middle_position | 32 | 40.62 | 3.5167 | -0.5252 | medium | True | 2.9786 | 2 |
