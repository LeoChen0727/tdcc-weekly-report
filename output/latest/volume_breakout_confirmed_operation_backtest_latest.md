# Volume Breakout Confirmed Operation Backtest

- generated_at: `2026-06-14 23:21:58 Asia/Taipei`
- model_id: `volume_range_breakout`
- entry_rule: `confirmation_next_open`
- stop_exit_rule: `signal_low_stop_or_fixed_10d_close`
- tdcc_as_of_rule: `tdcc_signal_date <= confirmation_date and tdcc_signal_age_days <= 7`
- event_rows: `4894`
- summary_rows: `267`
- scope: research only; all rows keep `approved_for_daily=False`.

## Event Counts

| tdcc_list_type | trigger_id | event_rows | unique_confirmations |
| --- | --- | --- | --- |
| consecutive_accumulation | next_day_continuation_confirmed | 4 | 4 |
| consecutive_accumulation | pullback_10ma_confirmed | 6 | 4 |
| consecutive_accumulation | pullback_5ma_confirmed | 17 | 12 |
| no_tdcc | next_day_continuation_confirmed | 1704 | 1704 |
| no_tdcc | pullback_10ma_confirmed | 1034 | 862 |
| no_tdcc | pullback_5ma_confirmed | 2028 | 1583 |
| weekly_increase | next_day_continuation_confirmed | 38 | 38 |
| weekly_increase | pullback_10ma_confirmed | 13 | 11 |
| weekly_increase | pullback_5ma_confirmed | 50 | 36 |

## Best Rows

| tdcc_list_type | rank_bucket | trigger_id | confluence_scope | confluence_id | sample_size | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass | ranking_research_score | ranking_research_rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 16 | 87.5 | 32.1642 | 22.7777 | low | True | 41.4219 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 17 | 88.24 | 31.598 | 22.5397 | low | True | 41.0813 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 16 | 87.5 | 30.9564 | 21.0913 | low | True | 39.3607 | 2 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | locked_limit_up__low_position | 15 | 73.33 | 40.0959 | 18.5484 | low | True | 38.9404 | 1 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_classification | limit_up_like_breakout | 10 | 90.0 | 29.1042 | 21.0913 | low | True | 38.8291 | 3 |
| consecutive_accumulation | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 15 | 86.67 | 31.5175 | 19.6429 | low | True | 38.1663 | 2 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 14 | 85.71 | 29.0442 | 16.6636 | low | True | 34.2072 | 1 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | 12 | 66.67 | 27.5497 | 19.1352 | low | True | 32.7302 | 1 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 12 | 66.67 | 21.6738 | 21.0916 | low | True | 31.8468 | 1 |
| weekly_increase | top_10 | next_day_continuation_confirmed | operation_price_position | high_position | 12 | 66.67 | 21.6738 | 21.0916 | low | True | 31.8468 | 2 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | 15 | 66.67 | 24.9822 | 18.6275 | low | True | 31.1615 | 1 |
| consecutive_accumulation | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 13 | 84.62 | 28.058 | 13.6842 | low | True | 30.8958 | 2 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_method | general_breakout | 13 | 61.54 | 25.1889 | 18.6275 | low | True | 30.4186 | 2 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 10 | 90.0 | 22.6873 | 13.6842 | low | True | 29.2751 | 4 |
| consecutive_accumulation | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 10 | 90.0 | 22.6873 | 13.6842 | low | True | 29.2751 | 5 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_classification | limit_up_like_breakout | 13 | 69.23 | 18.0674 | 16.0572 | low | True | 26.1118 | 3 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_method | general_breakout | 10 | 60.0 | 23.2815 | 14.2691 | low | True | 25.3439 | 4 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | 10 | 60.0 | 23.2815 | 14.2691 | low | True | 25.3439 | 5 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | limit_up_like_breakout | 14 | 78.57 | 16.6644 | 13.0921 | low | True | 24.2974 | 6 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | general_breakout | 18 | 61.11 | 22.7227 | 12.5026 | low | True | 23.7923 | 2 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_price_position | high_position | 44 | 63.64 | 12.7533 | 5.6278 | medium | True | 22.8198 | 3 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 50 | 62.0 | 12.0755 | 4.878 | medium | True | 20.7979 | 4 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_method | volume_attack | 10 | 80.0 | 14.1934 | 10.2239 | low | False | 18.7635 | 5 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_attack_position | volume_attack__high_position | 10 | 80.0 | 14.1934 | 10.2239 | low | False | 18.7635 | 6 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_price_position | high_position | 25 | 72.0 | 16.6372 | 7.561 | low | True | 18.3857 | 7 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_classification | limit_up_like_breakout | 20 | 60.0 | 13.1506 | 10.812 | low | True | 17.809 | 7 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | limit_up_like_breakout | 26 | 65.38 | 13.2672 | 9.2918 | low | True | 17.3919 | 8 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 13 | 69.23 | 10.2303 | 10.1167 | low | True | 17.2387 | 9 |
| weekly_increase | top_50 | pullback_10ma_confirmed | operation_price_position | high_position | 13 | 69.23 | 10.2303 | 10.1167 | low | True | 17.2387 | 10 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 16 | 75.0 | 15.7637 | 5.7691 | low | True | 16.7652 | 11 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | volume_attack | 14 | 64.29 | 9.6848 | 10.638 | low | True | 16.6988 | 12 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | volume_attack__high_position | 14 | 64.29 | 9.6848 | 10.638 | low | True | 16.6988 | 13 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 23 | 56.52 | 16.5651 | 8.3888 | low | True | 16.6439 | 8 |
| weekly_increase | top_20 | next_day_continuation_confirmed | operation_price_position | high_position | 23 | 56.52 | 16.5651 | 8.3888 | low | True | 16.6439 | 9 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_price_position | high_position | 15 | 73.33 | 17.7088 | 4.878 | low | True | 16.5629 | 3 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 27 | 70.37 | 15.3719 | 6.3776 | low | True | 16.5096 | 10 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_classification | limit_up_like_breakout | 10 | 70.0 | 15.7566 | 5.6278 | low | True | 15.7555 | 4 |
| weekly_increase | top_10 | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 17 | 70.59 | 15.5731 | 4.878 | low | True | 15.1947 | 5 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 25 | 72.0 | 8.8311 | 7.561 | low | True | 14.873 | 14 |
| weekly_increase | top_50 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 27 | 74.07 | 8.4864 | 6.1047 | low | True | 13.7482 | 15 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_classification | high_position_breakout | 11 | 63.64 | 16.6025 | 3.9773 | low | True | 13.6676 | 11 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_method | volume_attack | 14 | 78.57 | 6.256 | 4.878 | low | True | 12.2209 | 12 |
| weekly_increase | top_20 | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 13 | 76.92 | 6.5641 | 4.878 | low | True | 12.0852 | 13 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_method | general_breakout | 14 | 50.0 | 17.0461 | 3.0833 | low | True | 10.9615 | 16 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_attack_position | general_breakout__high_position | 14 | 50.0 | 17.0461 | 3.0833 | low | True | 10.9615 | 17 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_trigger | all_confirmed_volume_breakout | 38 | 50.0 | 10.685 | 0.105 | medium | True | 9.3561 | 18 |
| weekly_increase | top_50 | next_day_continuation_confirmed | operation_price_position | high_position | 38 | 50.0 | 10.685 | 0.105 | medium | True | 9.3561 | 19 |
| no_tdcc | all | next_day_continuation_confirmed | operation_price_position | low_position | 187 | 44.92 | 10.3489 | -1.7915 | high | True | 8.7659 | 2 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__low_position | 67 | 46.27 | 9.5929 | -0.1634 | medium | False | 6.3191 | 3 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | wide_range_breakout | 58 | 46.55 | 3.8274 | -0.1915 | medium | True | 3.9059 | 4 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | wide_range_breakout | 35 | 42.86 | 5.7559 | -1.2605 | medium | True | 3.5842 | 5 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | general_breakout__low_position | 46 | 50.0 | 4.1754 | 0.3572 | medium | False | 2.9144 | 6 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | locked_limit_up_breakout | 48 | 47.92 | 4.3934 | 0.0 | medium | False | 2.556 | 7 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | locked_limit_up | 48 | 47.92 | 4.3934 | 0.0 | medium | False | 2.556 | 8 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | locked_limit_up__high_position | 44 | 45.45 | 4.1754 | 0.0 | medium | False | 2.3641 | 9 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__high_position | 468 | 45.51 | 2.7906 | -1.2262 | high | True | 2.3382 | 10 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | high_position_breakout | 644 | 42.24 | 2.348 | -1.3986 | high | True | 1.5508 | 11 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | long_base_low_position | 29 | 51.72 | 3.2339 | 0.5435 | low | False | 0.8734 | 12 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | general_breakout__unknown_position | 46 | 50.0 | 3.2397 | 0.495 | low | False | 0.6516 | 13 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | general_breakout | 676 | 44.23 | 2.6208 | -1.0396 | medium | False | -0.0938 | 14 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_position | volume_attack__low_position | 105 | 40.0 | 6.5817 | -3.0369 | medium | False | -0.1191 | 15 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__unknown_position | 76 | 43.42 | 2.6808 | -0.3841 | low | False | -0.293 | 16 |
| no_tdcc | all | pullback_5ma_confirmed | operation_price_position | high_position | 1430 | 44.27 | 2.6827 | -1.2773 | medium | False | -0.4039 | 17 |
| no_tdcc | all | pullback_10ma_confirmed | operation_price_position | low_position | 130 | 42.31 | 2.1956 | -1.1872 | medium | False | -0.6341 | 18 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__middle_position | 38 | 44.74 | 2.4207 | -1.1268 | medium | False | -0.6898 | 19 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | volume_attack__high_position | 918 | 43.57 | 2.5561 | -1.4824 | medium | False | -0.8065 | 20 |
| no_tdcc | all | pullback_5ma_confirmed | operation_trigger | all_confirmed_volume_breakout | 2028 | 42.6 | 2.137 | -1.5424 | medium | False | -1.2108 | 21 |
| no_tdcc | all | next_day_continuation_confirmed | operation_attack_method | general_breakout | 555 | 43.6 | 2.6557 | -1.8838 | medium | False | -1.3339 | 22 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | limit_up_like_breakout | 1015 | 44.24 | 2.202 | -1.7094 | medium | False | -1.4126 | 23 |
| no_tdcc | all | next_day_continuation_confirmed | operation_classification | standard_breakout | 72 | 44.44 | 0.6734 | -0.7984 | low | False | -1.5797 | 24 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_position | general_breakout__low_position | 94 | 38.3 | 1.808 | -1.6267 | medium | False | -1.6042 | 25 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | general_breakout__unknown_position | 40 | 42.5 | 2.2225 | -1.5423 | low | False | -1.667 | 26 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | locked_limit_up_breakout | 17 | 41.18 | 4.0384 | -2.4528 | low | False | -1.8365 | 27 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_method | locked_limit_up | 17 | 41.18 | 4.0384 | -2.4528 | low | False | -1.8365 | 28 |
| no_tdcc | all | pullback_5ma_confirmed | operation_attack_method | volume_attack | 1304 | 41.56 | 1.8032 | -1.8009 | medium | False | -1.8489 | 29 |
| no_tdcc | all | pullback_5ma_confirmed | operation_classification | long_base_low_position | 57 | 31.58 | 1.1855 | -1.4045 | medium | False | -1.9007 | 30 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | volume_attack__high_position | 461 | 40.78 | 2.3244 | -2.1148 | medium | False | -1.9289 | 31 |
| no_tdcc | all | pullback_10ma_confirmed | operation_attack_position | general_breakout__middle_position | 18 | 33.33 | 2.37 | -1.7498 | low | False | -1.9434 | 32 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | long_base_low_position | 28 | 32.14 | 1.4491 | -1.4198 | low | False | -1.9745 | 33 |
| no_tdcc | all | pullback_10ma_confirmed | operation_classification | high_position_breakout | 306 | 39.22 | 2.0348 | -2.0326 | medium | False | -2.0228 | 34 |
