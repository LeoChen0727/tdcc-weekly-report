# Volume Breakout Formal Operation Backtest

- generated_at: `2026-06-30 22:56:16 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `3183`
- lifecycle_event_rows: `4634`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 70 | 0 |
| active_operation | mature | 10 | 10 |
| confirmed_operation | confirmed_not_entered | 10 | 0 |
| expired | expired_unconfirmed | 1385 | 0 |
| expired | immature_active | 45 | 0 |
| expired | mature | 3081 | 3081 |
| pending_confirmation | pending_confirmation | 33 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
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
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 6 | 16.67 | -9.4782 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 6 | 16.67 | -9.4782 | False | low | -94.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 6 | 66.67 | 16.6636 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 60.0 | 13.6842 | False | low | -95.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 3 | 33.33 | -11.2971 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 3 | 33.33 | -11.2971 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 3 | 33.33 | -11.2971 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_10ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 8 | 62.5 | 16.6636 | False | low | -92.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 7 | 28.57 | -7.6415 | False | low | -93.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 7 | 28.57 | -7.6415 | False | low | -93.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 7 | 57.14 | 13.6842 | False | low | -93.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 40.0 | 0.0 | False | low | -95.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 40.0 | 0.0 | False | low | -95.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 40.0 | 0.0 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 50.0 | 2.6447 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 1 | 100.0 | 12.931 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 1 | 100.0 | 12.931 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 29 | 44.83 | -1.1194 | True | low | 1.6516 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 25 | 52.0 | 0.5435 | False | low | 1.578 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 186 | 42.47 | -1.192 | False | medium | 0.4966 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 49 | 38.78 | -1.9608 | True | medium | 0.1207 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 49 | 38.78 | -1.9608 | True | medium | 0.1207 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 284 | 40.49 | -1.2773 | False | medium | -0.3391 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_classification | low_position_breakout | mature_selected_operation_only | 21 | 38.1 | -2.1505 | False | low | -0.5469 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 40 | 37.5 | -1.9784 | False | medium | -1.2626 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 12 | 41.67 | -1.7426 | False | low | -1.2959 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 299 | 40.13 | -1.6687 | False | medium | -1.3315 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 63 | 42.86 | -1.2959 | False | low | -1.4349 |
