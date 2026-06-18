# Volume Breakout Confirmed Operation Backtest

- generated_at: `2026-06-18 11:38:53 Asia/Taipei`
- model_id: `volume_range_breakout`
- entry_rule: `confirmation_next_open`
- stop_exit_rule: `signal_low_stop_or_fixed_10d_close`
- tdcc_as_of_rule: `tdcc_signal_date <= confirmation_date and tdcc_signal_age_days <= 7`
- event_rows: `7468`
- summary_rows: `341`
- scope: research only; all rows keep `approved_for_daily=False`.

## Event Counts

| tdcc_list_type | trigger_id | event_rows | unique_confirmations |
| --- | --- | --- | --- |
| consecutive_accumulation | next_day_break_signal_high_confirmed | 5 | 5 |
| consecutive_accumulation | next_day_continuation_confirmed | 5 | 5 |
| consecutive_accumulation | pullback_10ma_confirmed | 9 | 5 |
| consecutive_accumulation | pullback_5ma_confirmed | 21 | 14 |
| no_tdcc | next_day_break_signal_high_confirmed | 2131 | 2131 |
| no_tdcc | next_day_continuation_confirmed | 1913 | 1913 |
| no_tdcc | pullback_10ma_confirmed | 1085 | 900 |
| no_tdcc | pullback_5ma_confirmed | 2136 | 1653 |
| weekly_increase | next_day_break_signal_high_confirmed | 44 | 44 |
| weekly_increase | next_day_continuation_confirmed | 42 | 42 |
| weekly_increase | pullback_10ma_confirmed | 17 | 13 |
| weekly_increase | pullback_5ma_confirmed | 60 | 41 |

## Best Rows

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | sample_size | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass | ranking_research_score | ranking_research_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 18 | 88.89 | 29.9466 | 16.6636 | low | True | 35.1633 | 1 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 1 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 2 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 3 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 4 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 5 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 10 | 70.0 | 22.6826 | 21.0916 | low | True | 32.7896 | 6 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 17 | 88.24 | 29.2456 | 13.6842 | low | True | 32.0528 | 2 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 16 | 87.5 | 26.9394 | 13.6842 | low | True | 30.8866 | 1 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 15 | 86.67 | 25.9444 | 13.6842 | low | True | 30.2955 | 2 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 21 | 80.95 | 26.1059 | 13.6842 | low | True | 29.5331 | 1 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 31 | 67.74 | 16.2006 | 7.561 | medium | True | 29.2672 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 20 | 80.0 | 25.318 | 13.6842 | low | True | 29.0193 | 2 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 13 | 61.54 | 18.3806 | 20.1493 | low | True | 28.7245 | 7 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | 13 | 61.54 | 18.3806 | 20.1493 | low | True | 28.7245 | 8 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 12 | 83.33 | 23.6095 | 13.0921 | low | True | 28.1423 | 3 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 12 | 83.33 | 23.6095 | 13.0921 | low | True | 28.1423 | 4 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 12 | 83.33 | 23.6095 | 13.0921 | low | True | 28.1423 | 5 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 33 | 66.67 | 15.1918 | 6.3776 | medium | True | 26.475 | 2 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 11 | 81.82 | 20.4208 | 12.5 | low | True | 25.9196 | 3 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 11 | 81.82 | 20.4208 | 12.5 | low | True | 25.9196 | 4 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 11 | 81.82 | 20.4208 | 12.5 | low | True | 25.9196 | 5 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 54 | 62.96 | 13.4531 | 6.9693 | medium | True | 25.2451 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 15 | 73.33 | 19.5 | 12.5 | low | True | 24.2287 | 3 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 15 | 73.33 | 19.5 | 12.5 | low | True | 24.2287 | 4 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 15 | 73.33 | 19.5 | 12.5 | low | True | 24.2287 | 5 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 12 | 75.0 | 18.8712 | 12.5026 | low | True | 24.1675 | 9 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 12 | 75.0 | 18.8712 | 12.5026 | low | True | 24.1675 | 10 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 12 | 75.0 | 18.8712 | 12.5026 | low | True | 24.1675 | 11 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 60 | 61.67 | 12.8183 | 5.4914 | medium | True | 22.2478 | 2 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 19 | 68.42 | 15.0077 | 12.5 | low | True | 21.4801 | 3 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 19 | 68.42 | 15.0077 | 12.5 | low | True | 21.4801 | 4 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 68.42 | 15.0077 | 12.5 | low | True | 21.4801 | 5 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 15 | 60.0 | 16.332 | 13.0488 | low | True | 21.1976 | 12 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 15 | 60.0 | 16.332 | 13.0488 | low | True | 21.1976 | 13 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 35 | 57.14 | 11.0052 | 6.3776 | medium | True | 20.8526 | 3 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 18 | 77.78 | 20.498 | 6.9693 | low | True | 20.4367 | 14 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 17 | 70.59 | 15.5636 | 10.3311 | low | True | 20.0982 | 4 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | 17 | 70.59 | 15.5636 | 10.3311 | low | True | 20.0982 | 5 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 19 | 73.68 | 17.9625 | 7.561 | low | True | 19.1931 | 6 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 6 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 7 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 8 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 9 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 10 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 63.16 | 17.2071 | 8.9961 | low | True | 18.4878 | 11 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 38 | 55.26 | 10.1799 | 5.4914 | medium | True | 18.4376 | 7 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 38 | 55.26 | 10.1799 | 5.4914 | medium | True | 18.4376 | 8 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 20 | 75.0 | 18.4038 | 5.6278 | low | True | 17.8697 | 15 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 12 | 83.33 | 11.2497 | 7.8009 | low | True | 17.8183 | 9 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 13 | 84.62 | 10.5575 | 7.561 | low | True | 17.5097 | 10 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 12 | 66.67 | 18.0893 | 5.7691 | low | True | 16.4435 | 12 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 25 | 56.0 | 15.7936 | 8.3888 | low | True | 16.2311 | 13 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | 25 | 56.0 | 15.7936 | 8.3888 | low | True | 16.2311 | 14 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 27 | 55.56 | 14.8471 | 8.3888 | low | True | 15.7509 | 15 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 27 | 55.56 | 14.8471 | 8.3888 | low | True | 15.7509 | 16 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 10 | 60.0 | 8.2116 | 8.5148 | low | False | 11.3835 | 17 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_price_position | high_position | 10 | 60.0 | 8.2116 | 8.5148 | low | False | 11.3835 | 18 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 11 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 12 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 13 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 14 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 15 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 33 | 48.48 | 9.22 | -0.8584 | medium | False | 4.7663 | 16 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__low_position | 146 | 42.47 | 11.2298 | -2.311 | medium | False | 4.4558 | 1 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 42 | 47.62 | 9.3891 | -1.5403 | medium | False | 3.9488 | 17 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | 42 | 47.62 | 9.3891 | -1.5403 | medium | False | 3.9488 | 18 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__low_position | 150 | 42.0 | 10.7629 | -2.4332 | medium | False | 3.9224 | 2 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | 58 | 46.55 | 3.8274 | -0.1915 | medium | True | 3.9059 | 3 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 44 | 47.73 | 9.0994 | -1.5403 | medium | False | 3.7467 | 19 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 44 | 47.73 | 9.0994 | -1.5403 | medium | False | 3.7467 | 20 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | wide_range_breakout | 35 | 42.86 | 5.7559 | -1.2605 | medium | True | 3.5842 | 4 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | low_position | 210 | 42.86 | 8.6796 | -1.932 | medium | False | 3.1117 | 5 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | 11 | 45.45 | 8.7376 | -2.2321 | low | True | 2.3917 | 21 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 427 | 42.62 | 2.9592 | -1.4778 | high | True | 2.0036 | 6 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__low_position | 77 | 45.45 | 3.308 | 0.0 | medium | False | 1.8959 | 7 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_price_position | low_position | 239 | 41.84 | 7.7244 | -2.2857 | medium | False | 1.8648 | 8 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | 656 | 42.53 | 2.4387 | -1.3376 | high | True | 1.7635 | 9 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | 29 | 51.72 | 4.9058 | 0.5435 | low | False | 1.6257 | 10 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | 229 | 42.36 | 1.4682 | -1.278 | high | True | 0.9122 | 11 |
