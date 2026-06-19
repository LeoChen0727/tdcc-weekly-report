# Volume Breakout Formal Operation Backtest

- generated_at: `2026-06-20 07:24:16 Asia/Taipei`
- model_id: `volume_range_breakout`
- purpose: one signal produces one formal operation event.
- lifecycle_definition: `daily_volume_breakout_operation_lifecycle_v1`
- metric_sample_scope: `mature_selected_operation_only`
- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.
- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.
- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.
- formal_event_rows: `3069`
- lifecycle_event_rows: `4496`

## Lifecycle State Counts

| operation_lifecycle_state | sample_maturity_status | signal_events | mature_samples |
| --- | --- | --- | --- |
| active_operation | immature_active | 84 | 0 |
| active_operation | mature | 12 | 12 |
| confirmed_operation | confirmed_not_entered | 17 | 0 |
| expired | expired_unconfirmed | 1328 | 0 |
| expired | immature_active | 35 | 0 |
| expired | mature | 2984 | 2984 |
| pending_confirmation | pending_confirmation | 36 | 0 |

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | metric_sample_scope | sample_size | win_rate | median_return | out_of_sample_pass | confidence_status | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_10 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
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
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 80.0 | 19.6429 | False | low | -95.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_20 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
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
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 7 | 71.43 | 19.6429 | False | low | -93.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 6 | 66.67 | 16.6636 | False | low | -94.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_price_position | high_position | mature_selected_operation_only | 5 | 20.0 | -11.315 | False | low | -95.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_50 | next_day_break_signal_high_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 25.0 | -11.4075 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 4 | 50.0 | 9.8215 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 4 | 50.0 | 9.8215 | False | low | -96.0 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 4 | 50.0 | 9.8215 | False | low | -96.0 |
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
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | mature_selected_operation_only | 180 | 43.33 | -1.1282 | True | high | 3.6782 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__low_position | mature_selected_operation_only | 25 | 52.0 | 0.5435 | False | low | 1.578 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | locked_limit_up__high_position | mature_selected_operation_only | 28 | 42.86 | -1.5401 | True | low | 1.3308 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | mature_selected_operation_only | 291 | 40.55 | -1.6687 | True | high | 0.9696 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | mature_selected_operation_only | 48 | 37.5 | -2.0503 | True | medium | 0.0105 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | mature_selected_operation_only | 48 | 37.5 | -2.0503 | True | medium | 0.0105 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | mature_selected_operation_only | 275 | 41.09 | -1.278 | False | medium | -0.2248 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_classification | low_position_breakout | mature_selected_operation_only | 21 | 38.1 | -2.1505 | False | low | -0.5469 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 36 | 36.11 | -1.9784 | False | medium | -1.0764 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | high_position | mature_selected_operation_only | 481 | 40.54 | -1.7595 | False | medium | -1.3958 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 63 | 42.86 | -1.2959 | False | low | -1.4349 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | mature_selected_operation_only | 11 | 36.36 | -2.3585 | False | low | -1.7673 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | mature_selected_operation_only | 40 | 35.0 | -2.1191 | False | low | -2.3554 |
| no_tdcc | all | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 73 | 30.14 | -1.996 | False | medium | -2.6499 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | mature_selected_operation_only | 95 | 36.84 | -1.9397 | False | medium | -2.6715 |
| no_tdcc | all | next_day_break_signal_high_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 282 | 42.91 | -2.0934 | False | medium | -2.6828 |
| no_tdcc | all | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | mature_selected_operation_only | 766 | 37.21 | -2.0907 | False | medium | -2.6898 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | general_breakout | mature_selected_operation_only | 154 | 31.82 | -1.8086 | False | medium | -2.7144 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | long_base_low_position | mature_selected_operation_only | 24 | 25.0 | -1.5664 | False | low | -2.8944 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__low_position | mature_selected_operation_only | 21 | 33.33 | -1.5342 | False | low | -2.9331 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__unknown_position | mature_selected_operation_only | 59 | 38.98 | -2.0619 | False | low | -3.0378 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | unknown_position | mature_selected_operation_only | 159 | 32.7 | -2.0718 | False | low | -3.2062 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__unknown_position | mature_selected_operation_only | 36 | 22.22 | -1.8976 | False | low | -3.2618 |
