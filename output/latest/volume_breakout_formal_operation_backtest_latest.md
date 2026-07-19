# Volume Breakout Formal Operation Backtest

- generated_at: `2026-07-19 11:14:38 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- formal_trigger_ids: `next_day_continuation_confirmed`.
- legacy trigger empty-state rows: not emitted; retired triggers are outside the formal v2 contract.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `2215`
- lifecycle_event_rows: `4837`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 38 | 0 |
| active_operation | mature | 4 | 4 |
| confirmed_operation | confirmed_not_entered | 3 | 0 |
| expired | expired_unconfirmed | 2622 | 0 |
| expired | immature_active | 19 | 0 |
| expired | mature | 2130 | 2130 |
| pending_confirmation | pending_confirmation | 21 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 7 | 28.57 | -9.621 | False | low | -93.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 7 | 28.57 | -9.621 | False | low | -93.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_10 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 2 | 50.0 | 12.5449 | False | low | -98.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 9 | 22.22 | -9.621 | False | low | -91.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 9 | 22.22 | -9.621 | False | low | -91.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 4 | 25.0 | -8.6312 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 3 | 33.33 | -9.621 | False | low | -97.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 3 | 33.33 | -9.621 | False | low | -97.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_20 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 10 | 30.0 | -8.6312 | False | low | -10.3888 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 10 | 30.0 | -8.6312 | False | low | -10.3888 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 5 | 40.0 | -7.6415 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 4 | 50.0 | 1.655 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 4 | 50.0 | 1.655 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| consecutive_accumulation | top_50 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 1 | 0.0 | -7.6415 | False | low | -99.0 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 18 | 66.67 | 3.707 | False | low | 7.6465 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | long_base_low_position | mature_selected_operation_only | 21 | 57.14 | 1.1481 | False | low | 1.4252 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | low_position_breakout | mature_selected_operation_only | 14 | 42.86 | -1.2479 | False | low | 0.8164 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 54 | 40.74 | -1.2732 | False | low | -1.439 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 245 | 42.45 | -2.0362 | False | medium | -2.8072 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__middle_position | mature_selected_operation_only | 84 | 35.71 | -1.8058 | False | medium | -3.3229 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | volume_attack__low_position | mature_selected_operation_only | 17 | 35.29 | -2.9167 | False | low | -3.7246 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | standard_breakout | mature_selected_operation_only | 130 | 36.92 | -2.2692 | False | medium | -3.9649 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 235 | 39.57 | -3.1792 | False | medium | -4.1749 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | middle_position | mature_selected_operation_only | 127 | 35.43 | -2.2535 | False | medium | -4.4125 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 393 | 40.46 | -3.255 | False | medium | -4.632 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | volume_attack__unknown_position | mature_selected_operation_only | 80 | 33.75 | -3.7656 | False | low | -4.8508 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | unknown_position | mature_selected_operation_only | 341 | 36.07 | -3.5616 | False | low | -4.8754 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 158 | 41.77 | -3.2942 | False | medium | -5.2017 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 360 | 38.06 | -3.6282 | False | medium | -5.4046 |
| no_tdcc | all | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 2134 | 37.77 | -3.759 | False | medium | -5.8265 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 1561 | 38.44 | -4.0445 | False | medium | -5.8594 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | volume_attack__middle_position | mature_selected_operation_only | 28 | 39.29 | -4.6045 | False | low | -6.1551 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 1168 | 37.76 | -4.3665 | False | medium | -6.3568 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__unknown_position | mature_selected_operation_only | 207 | 35.75 | -5.0336 | False | low | -6.6881 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 1529 | 36.95 | -4.3614 | False | medium | -6.8529 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 1529 | 36.95 | -4.3614 | False | medium | -6.8529 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 15 | 26.67 | -4.7445 | False | low | -7.0157 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | low_position | mature_selected_operation_only | 105 | 36.19 | -4.1509 | False | medium | -7.1735 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 47 | 34.04 | -4.8077 | False | medium | -8.251 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__low_position | mature_selected_operation_only | 70 | 28.57 | -6.9851 | False | medium | -13.242 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 18 | 61.11 | 10.7574 | True | low | 19.9073 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 18 | 61.11 | 10.7574 | True | low | 19.9073 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 18 | 61.11 | 10.7574 | True | low | 19.9073 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 21 | 57.14 | 9.5745 | True | low | 17.3772 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 21 | 57.14 | 9.5745 | True | low | 17.3772 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 3 | 33.33 | -2.2321 | False | low | -97.0 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 3 | 33.33 | -2.2321 | False | low | -97.0 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 3 | 33.33 | -2.2321 | False | low | -97.0 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 34 | 55.88 | 4.7286 | True | medium | 18.8717 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 34 | 55.88 | 4.7286 | True | medium | 18.8717 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 34 | 55.88 | 4.7286 | True | medium | 18.8717 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 41 | 51.22 | 0.7557 | True | medium | 11.2648 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 41 | 51.22 | 0.7557 | True | medium | 11.2648 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 7 | 28.57 | -9.621 | False | low | -93.0 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 5 | 20.0 | -9.621 | False | low | -95.0 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 5 | 20.0 | -9.621 | False | low | -95.0 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 2 | 50.0 | 34.4755 | False | low | -98.0 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 2 | 50.0 | 34.4755 | False | low | -98.0 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 12 | 50.0 | -0.0653 | True | low | 4.8246 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 71 | 47.89 | -0.9346 | False | medium | 4.2937 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | mature_selected_operation_only | 71 | 47.89 | -0.9346 | False | medium | 4.2937 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 59 | 47.46 | -0.9346 | False | medium | 4.0255 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 59 | 47.46 | -0.9346 | False | medium | 4.0255 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 59 | 47.46 | -0.9346 | False | medium | 4.0255 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 9 | 55.56 | 2.1016 | False | low | -91.0 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 9 | 55.56 | 2.1016 | False | low | -91.0 |
