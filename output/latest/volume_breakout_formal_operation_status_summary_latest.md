# Volume Breakout Formal Operation Status Summary

- generated_at: `2026-06-20 07:25:14 Asia/Taipei`
- model_id: `volume_range_breakout`
- scope: research only; all rows keep `approved_for_daily=False`.
- as_published_report_bucket comes only from historical daily model snapshots; missing snapshots are labeled `snapshot_missing`.
- current daily adapter rows use the full PDF view only to avoid highlight/full duplicate counts.

## Status Counts

| status_source | status_bucket | rows | current_data_rows |
| --- | --- | --- | --- |
| current_daily_adapter_full_view | active_operation | 1 | 2 |
| current_daily_adapter_full_view | confirmed_operation | 1 | 0 |
| current_daily_adapter_full_view | confirmed_unranked_operation | 3 | 8 |
| current_daily_adapter_full_view | pending_confirmation | 2 | 27 |
| historical_mature_formal_event | confirmed_operation | 16 | 6138 |

## Mature Performance Rows

| status_bucket | as_published_report_bucket | trigger_id | tdcc_list_type | mature_sample_size | win_rate | avg_return | median_return | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed_operation | all_events | next_day_break_signal_high_confirmed | no_tdcc | 2157 | 36.95 | 0.14 | -3.7037 | False | medium |
| confirmed_operation | snapshot_missing | next_day_break_signal_high_confirmed | no_tdcc | 2157 | 36.95 | 0.14 | -3.7037 | False | medium |
| confirmed_operation | all_events | pullback_5ma_confirmed | no_tdcc | 766 | 37.21 | 1.2616 | -2.0907 | False | medium |
| confirmed_operation | snapshot_missing | pullback_5ma_confirmed | no_tdcc | 766 | 37.21 | 1.2616 | -2.0907 | False | medium |
| confirmed_operation | all_events | pullback_10ma_confirmed | no_tdcc | 73 | 30.14 | 1.2622 | -1.996 | False | medium |
| confirmed_operation | snapshot_missing | pullback_10ma_confirmed | no_tdcc | 73 | 30.14 | 1.2622 | -1.996 | False | medium |
| confirmed_operation | all_events | next_day_break_signal_high_confirmed | weekly_increase | 43 | 46.51 | 9.0158 | -2.2222 | False | medium |
| confirmed_operation | snapshot_missing | next_day_break_signal_high_confirmed | weekly_increase | 43 | 46.51 | 9.0158 | -2.2222 | False | medium |
| confirmed_operation | all_events | pullback_5ma_confirmed | weekly_increase | 17 | 52.94 | 12.6883 | 6.1047 | True | low |
| confirmed_operation | snapshot_missing | pullback_5ma_confirmed | weekly_increase | 17 | 52.94 | 12.6883 | 6.1047 | True | low |
| confirmed_operation | all_events | pullback_5ma_confirmed | consecutive_accumulation | 7 | 71.43 | 18.3282 | 19.6429 | False | low |
| confirmed_operation | snapshot_missing | pullback_5ma_confirmed | consecutive_accumulation | 7 | 71.43 | 18.3282 | 19.6429 | False | low |
| confirmed_operation | all_events | next_day_break_signal_high_confirmed | consecutive_accumulation | 5 | 20.0 | -6.5604 | -11.315 | False | low |
| confirmed_operation | snapshot_missing | next_day_break_signal_high_confirmed | consecutive_accumulation | 5 | 20.0 | -6.5604 | -11.315 | False | low |
| confirmed_operation | all_events | pullback_10ma_confirmed | weekly_increase | 1 | 100.0 | 6.6986 | 6.6986 | False | low |
| confirmed_operation | snapshot_missing | pullback_10ma_confirmed | weekly_increase | 1 | 100.0 | 6.6986 | 6.6986 | False | low |

## Current Adapter Full View

| status_bucket | as_published_report_bucket | trigger_id | tdcc_list_type | current_row_count | current_data_row_count | metric_sample_scope |
| --- | --- | --- | --- | --- | --- | --- |
| active_operation | snapshot_missing | next_day_break_signal_high_confirmed | weekly_increase | 2 | 2 | current_unmatured_status_count_only |
| confirmed_operation | snapshot_missing |  |  | 1 | 0 | current_unmatured_status_count_only |
| confirmed_unranked_operation | mainstream | next_day_break_signal_high_confirmed | no_tdcc | 6 | 6 | current_unmatured_status_count_only |
| confirmed_unranked_operation | non_mainstream | next_day_break_signal_high_confirmed | no_tdcc | 1 | 1 | current_unmatured_status_count_only |
| confirmed_unranked_operation | non_mainstream | pullback_5ma_confirmed | no_tdcc | 1 | 1 | current_unmatured_status_count_only |
| pending_confirmation | mainstream |  |  | 20 | 20 | current_unmatured_status_count_only |
| pending_confirmation | non_mainstream |  |  | 7 | 7 | current_unmatured_status_count_only |
