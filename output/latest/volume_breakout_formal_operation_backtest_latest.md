# Volume Breakout Formal Operation Backtest

- generated_at: `2026-07-08 21:30:24 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `3310`
- lifecycle_event_rows: `4760`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 81 | 0 |
| active_operation | mature | 10 | 10 |
| confirmed_operation | confirmed_not_entered | 5 | 0 |
| expired | expired_unconfirmed | 1434 | 0 |
| expired | immature_active | 31 | 0 |
| expired | mature | 3180 | 3180 |
| pending_confirmation | pending_confirmation | 19 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 8 | 25.0 | -8.1535 | False | low | -92.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 8 | 25.0 | -8.1535 | False | low | -92.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 6 | 66.67 | 16.6636 | False | low | -94.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 60.0 | 13.6842 | False | low | -95.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 3 | 33.33 | -7.2931 | False | low | -97.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 3 | 33.33 | -7.2931 | False | low | -97.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 3 | 33.33 | -7.2931 | False | low | -97.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 10 | 20.0 | -8.6312 | False | low | -11.1699 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 10 | 20.0 | -8.6312 | False | low | -11.1699 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 7 | 57.14 | 13.6842 | False | low | -93.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 6 | 50.0 | 3.1956 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 4 | 25.0 | -8.6312 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -9.2951 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -9.2951 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -9.2951 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 3 | 33.33 | -9.621 | False | low | -97.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 3 | 33.33 | -9.621 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
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
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 11 | 27.27 | -7.6415 | False | low | -9.5632 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 11 | 27.27 | -7.6415 | False | low | -9.5632 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 9 | 55.56 | 13.6842 | False | low | -91.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 8 | 50.0 | 6.8421 | False | low | -92.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 6 | 16.67 | -9.0005 | False | low | -94.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 6 | 33.33 | -3.6465 | False | low | -94.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 6 | 33.33 | -3.6465 | False | low | -94.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 6 | 33.33 | -3.6465 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 5 | 40.0 | -7.6415 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 4 | 50.0 | 1.655 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 4 | 50.0 | 1.655 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 100.0 | 27.7739 | False | low | -98.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_10ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 1 | 100.0 | 10.3527 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 31 | 45.16 | -1.1194 | True | medium | 2.4321 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 25 | 52.0 | 0.5435 | False | low | 1.578 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 42 | 35.71 | -1.7383 | True | medium | 0.3309 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 191 | 41.88 | -1.2766 | False | medium | 0.2935 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 51 | 39.22 | -1.9608 | True | medium | -0.0139 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 51 | 39.22 | -1.9608 | True | medium | -0.0139 |
