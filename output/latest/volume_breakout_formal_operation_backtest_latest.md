# Volume Breakout Formal Operation Backtest

- generated_at: `2026-06-18 14:57:55 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `3008`
- lifecycle_event_rows: `4501`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 70 | 0 |
| active_operation | mature | 6 | 6 |
| confirmed_operation | confirmed_not_entered | 12 | 0 |
| expired | expired_unconfirmed | 1384 | 0 |
| expired | immature_active | 77 | 0 |
| expired | mature | 2933 | 2933 |
| pending_confirmation | pending_confirmation | 19 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 4 | 75.0 | 16.6636 | False | low | -96.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 4 | 75.0 | 16.6636 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 6 | 83.33 | 21.0913 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__low_position | mature_selected_operation_only | 148 | 42.57 | -2.311 | False | medium | 4.3 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 202 | 40.59 | -1.5011 | True | high | 2.1745 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_price_position | low_position | mature_selected_operation_only | 236 | 42.37 | -2.2181 | False | medium | 2.0937 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 32 | 50.0 | 0.495 | False | low | 1.0209 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 46 | 39.13 | -1.8617 | True | medium | 0.8595 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 46 | 39.13 | -1.8617 | True | medium | 0.8595 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 297 | 39.73 | -1.6774 | True | high | 0.7959 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 29 | 44.83 | -1.1194 | False | low | 0.0325 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 36 | 47.22 | -1.0001 | False | low | -0.3873 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 30 | 40.0 | -0.937 | False | low | -1.0499 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 40 | 35.0 | -2.0072 | False | medium | -1.1183 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 305 | 39.34 | -1.6687 | False | medium | -1.2416 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__unknown_position | mature_selected_operation_only | 26 | 46.15 | -0.574 | False | low | -1.7668 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 11 | 36.36 | -2.3585 | False | low | -1.7673 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_classification | long_base_low_position | mature_selected_operation_only | 37 | 48.65 | -1.7595 | False | low | -1.8745 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 519 | 39.69 | -2.0067 | False | medium | -2.1165 |
| no_tdcc | all | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 71 | 30.99 | -1.9608 | False | medium | -2.2552 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | low_position | mature_selected_operation_only | 12 | 25.0 | -0.9806 | False | low | -2.311 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 270 | 43.7 | -1.96 | False | medium | -2.3308 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__unknown_position | mature_selected_operation_only | 28 | 32.14 | -0.8159 | False | low | -2.4031 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_classification | low_position_breakout | mature_selected_operation_only | 51 | 37.25 | -2.9448 | False | low | -2.5641 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | unknown_position | mature_selected_operation_only | 76 | 31.58 | -1.436 | False | low | -2.6689 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 158 | 32.28 | -1.8086 | False | medium | -2.7499 |
