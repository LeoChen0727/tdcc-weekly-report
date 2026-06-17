# Volume Breakout Formal Operation Backtest

- generated_at: `2026-06-18 02:50:07 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `2946`
- lifecycle_event_rows: `4501`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 68 | 0 |
| active_operation | mature | 6 | 6 |
| confirmed_operation | confirmed_not_entered | 12 | 0 |
| expired | expired_unconfirmed | 1454 | 0 |
| expired | immature_active | 70 | 0 |
| expired | mature | 2869 | 2869 |
| pending_confirmation | pending_confirmation | 22 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
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
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 6 | 83.33 | 30.7533 | False | low | -94.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 2 | 50.0 | 4.1729 | False | low | -98.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 7 | 85.71 | 22.5397 | False | low | -93.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 6 | 83.33 | 21.0913 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -12.75 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -12.797 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 3 | 66.67 | 19.6429 | False | low | -97.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 3 | 100.0 | 41.8637 | False | low | -97.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 1 | 100.0 | 41.8637 | False | low | -99.0 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__low_position | mature_selected_operation_only | 146 | 42.47 | -2.311 | False | medium | 4.4558 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | low_position | mature_selected_operation_only | 210 | 42.86 | -1.932 | False | medium | 3.1117 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 36 | 41.67 | -0.5652 | True | medium | 2.1326 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 29 | 51.72 | 0.5435 | False | low | 1.6257 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | long_base_low_position | mature_selected_operation_only | 29 | 51.72 | 0.5435 | False | low | 0.8734 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 50 | 40.0 | -1.8617 | True | medium | 0.5945 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 50 | 40.0 | -1.8617 | True | medium | 0.5945 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 26 | 46.15 | -0.3968 | False | low | 0.2085 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 29 | 44.83 | -1.1194 | False | low | 0.0325 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__low_position | mature_selected_operation_only | 46 | 41.3 | -1.4693 | True | medium | -0.1186 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 249 | 38.55 | -1.6774 | False | medium | -0.9731 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 367 | 38.15 | -1.6807 | False | medium | -1.437 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | standard_breakout | mature_selected_operation_only | 73 | 45.21 | -0.7937 | False | low | -1.5755 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 369 | 38.75 | -1.7276 | False | medium | -1.6852 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 51 | 33.33 | -2.0183 | False | medium | -1.9554 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 224 | 43.75 | -1.8185 | False | medium | -2.1324 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 582 | 38.49 | -2.0858 | False | medium | -2.3837 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__middle_position | mature_selected_operation_only | 39 | 35.9 | -2.2609 | True | medium | -2.4514 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | low_position | mature_selected_operation_only | 15 | 26.67 | -1.0221 | False | low | -2.5053 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 27 | 22.22 | -1.5504 | False | low | -2.5443 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__unknown_position | mature_selected_operation_only | 30 | 30.0 | -0.9183 | False | low | -2.5541 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 186 | 32.8 | -1.7457 | False | medium | -2.5967 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 118 | 37.29 | -1.8384 | False | medium | -2.6419 |
