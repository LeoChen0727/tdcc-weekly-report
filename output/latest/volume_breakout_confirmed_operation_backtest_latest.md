# Volume Breakout Confirmed Operation Backtest

- generated_at: `2026-06-20 07:24:16 Asia/Taipei`
- model_id: `volume_range_breakout`
- entry_rule: `confirmation_next_open`
- stop_exit_rule: `signal_low_stop_or_fixed_10d_close`
- tdcc_as_of_rule: `tdcc_signal_date <= confirmation_date and tdcc_signal_age_days <= 7`
- event_rows: `7636`
- summary_rows: `350`
- scope: research only; all rows keep `approved_for_daily=False`.

## Event Counts

| tdcc_list_type | trigger_id | event_rows | unique_confirmations |
| --- | --- | --- | --- |
| consecutive_accumulation | next_day_break_signal_high_confirmed | 5 | 5 |
| consecutive_accumulation | next_day_continuation_confirmed | 5 | 5 |
| consecutive_accumulation | pullback_10ma_confirmed | 9 | 5 |
| consecutive_accumulation | pullback_5ma_confirmed | 25 | 17 |
| no_tdcc | next_day_break_signal_high_confirmed | 2190 | 2190 |
| no_tdcc | next_day_continuation_confirmed | 1971 | 1971 |
| no_tdcc | pullback_10ma_confirmed | 1100 | 910 |
| no_tdcc | pullback_5ma_confirmed | 2156 | 1663 |
| weekly_increase | next_day_break_signal_high_confirmed | 45 | 45 |
| weekly_increase | next_day_continuation_confirmed | 43 | 43 |
| weekly_increase | pullback_10ma_confirmed | 20 | 16 |
| weekly_increase | pullback_5ma_confirmed | 67 | 44 |

## Best Rows

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | sample_size | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass | ranking_research_score | ranking_research_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 33 | 72.73 | 15.1285 | 13.6842 | medium | True | 38.9782 | 1 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 35 | 71.43 | 14.2386 | 12.5 | medium | True | 36.2124 | 2 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 19 | 84.21 | 27.5446 | 13.6842 | low | True | 30.6744 | 1 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 18 | 83.33 | 26.7491 | 13.6842 | low | True | 30.1672 | 2 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 17 | 82.35 | 24.4317 | 13.6842 | low | True | 28.9589 | 1 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 1 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 2 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 3 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 4 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 5 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 10 | 70.0 | 21.8617 | 16.9871 | low | True | 28.7262 | 6 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 16 | 81.25 | 23.3422 | 13.6842 | low | True | 28.2835 | 2 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | 10 | 80.0 | 18.0106 | 15.3268 | low | True | 27.0739 | 1 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | 10 | 80.0 | 18.0106 | 15.3268 | low | True | 27.0739 | 2 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | 10 | 80.0 | 18.0106 | 15.3268 | low | True | 27.0739 | 3 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 13 | 76.92 | 20.5864 | 12.5 | low | True | 25.2551 | 3 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 13 | 76.92 | 20.5864 | 12.5 | low | True | 25.2551 | 4 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 13 | 76.92 | 20.5864 | 12.5 | low | True | 25.2551 | 5 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 14 | 71.43 | 16.903 | 15.1816 | low | True | 25.1608 | 7 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 14 | 71.43 | 16.903 | 15.1816 | low | True | 25.1608 | 8 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 14 | 71.43 | 16.903 | 15.1816 | low | True | 25.1608 | 9 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 25 | 68.0 | 20.2791 | 13.6842 | low | True | 24.9054 | 1 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 21 | 71.43 | 16.7803 | 13.7778 | low | True | 23.9214 | 10 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 24 | 66.67 | 19.3797 | 13.0921 | low | True | 23.7504 | 2 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 21 | 76.19 | 14.3827 | 13.7778 | low | True | 23.5922 | 3 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 21 | 76.19 | 14.3827 | 13.7778 | low | True | 23.5922 | 4 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 21 | 76.19 | 14.3827 | 13.7778 | low | True | 23.5922 | 5 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | 19 | 78.95 | 17.5938 | 11.6059 | low | True | 23.4976 | 4 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 12 | 75.0 | 17.4115 | 12.3529 | low | True | 23.3759 | 3 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 12 | 75.0 | 17.4115 | 12.3529 | low | True | 23.3759 | 4 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 12 | 75.0 | 17.4115 | 12.3529 | low | True | 23.3759 | 5 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 61 | 60.66 | 11.0927 | 6.3776 | medium | True | 22.0232 | 5 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 20 | 75.0 | 16.5681 | 10.9685 | low | True | 21.8503 | 6 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 13 | 61.54 | 17.7492 | 11.9403 | low | True | 21.0522 | 11 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | 13 | 61.54 | 17.7492 | 11.9403 | low | True | 21.0522 | 12 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 15 | 60.0 | 15.7847 | 11.9403 | low | True | 19.9536 | 13 |
| weekly_increase | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 15 | 60.0 | 15.7847 | 11.9403 | low | True | 19.9536 | 14 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 18 | 61.11 | 14.5184 | 12.2059 | low | True | 19.8333 | 3 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 18 | 61.11 | 14.5184 | 12.2059 | low | True | 19.8333 | 4 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 18 | 61.11 | 14.5184 | 12.2059 | low | True | 19.8333 | 5 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 6 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 7 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 8 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 9 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 10 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 19 | 63.16 | 16.8408 | 8.9961 | low | True | 18.323 | 11 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 19 | 73.68 | 15.5421 | 7.561 | low | True | 18.1039 | 7 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 67 | 59.7 | 10.7356 | 3.9773 | medium | True | 17.9335 | 8 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_price_position | high_position | 10 | 70.0 | 9.7225 | 10.9685 | low | True | 17.8468 | 12 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 23 | 69.57 | 15.2825 | 7.561 | low | True | 17.3771 | 15 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 12 | 83.33 | 9.5939 | 7.8009 | low | True | 17.0732 | 9 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 13 | 84.62 | 9.0291 | 7.561 | low | True | 16.8219 | 10 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 25 | 56.0 | 15.5152 | 8.3888 | low | True | 16.1058 | 13 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | 25 | 56.0 | 15.5152 | 8.3888 | low | True | 16.1058 | 14 |
| weekly_increase | top_20 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 11 | 63.64 | 8.5733 | 10.3311 | low | True | 15.7729 | 15 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 12 | 66.67 | 16.4336 | 5.7691 | low | True | 15.6985 | 16 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 27 | 55.56 | 14.5893 | 8.3888 | low | True | 15.6349 | 17 |
| weekly_increase | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 27 | 55.56 | 14.5893 | 8.3888 | low | True | 15.6349 | 18 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 42 | 54.76 | 9.0798 | 3.705 | medium | True | 14.8343 | 11 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 45 | 53.33 | 8.5113 | 1.0323 | medium | True | 10.046 | 12 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 45 | 53.33 | 8.5113 | 1.0323 | medium | True | 10.046 | 13 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | 18 | 66.67 | 6.933 | 3.707 | low | False | 7.6465 | 1 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 386 | 44.56 | 3.557 | -1.1282 | high | True | 3.3006 | 2 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 14 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 15 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 16 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 17 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 18 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | 34 | 47.06 | 8.446 | -1.5403 | medium | False | 3.1727 | 19 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | 600 | 44.17 | 2.9025 | -1.1527 | high | True | 2.5971 | 3 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 43 | 46.51 | 8.7732 | -2.2222 | medium | False | 2.4717 | 20 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | 43 | 46.51 | 8.7732 | -2.2222 | medium | False | 2.4717 | 21 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | 83 | 44.58 | 3.6162 | -1.1268 | medium | True | 2.4613 | 4 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | 11 | 45.45 | 8.7376 | -2.2321 | low | True | 2.3917 | 22 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | 45 | 46.67 | 8.5173 | -2.2222 | medium | False | 2.2946 | 23 |
| weekly_increase | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | 45 | 46.67 | 8.5173 | -2.2222 | medium | False | 2.2946 | 24 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__low_position | 25 | 52.0 | 4.7662 | 0.5435 | low | False | 1.578 | 5 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | long_base_low_position | 21 | 57.14 | 1.4941 | 1.1481 | low | False | 1.4252 | 6 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | 618 | 41.59 | 2.2782 | -1.6929 | high | True | 0.8924 | 7 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | low_position_breakout | 14 | 42.86 | 7.6084 | -1.2479 | low | False | 0.8164 | 8 |
