# Volume Breakout Pattern Classification

- generated_at: `2026-07-19 11:11:20 Asia/Taipei`
- model_id: `volume_range_breakout`
- unique_event_rows: `4773`
- summary_rows: `102`
- scope: current model hits only; research classification, not production promotion.
- approved_for_daily: always `False` in this artifact.

## Classification Counts

| classification_id | classification_name_zh | event_count |
| --- | --- | --- |
| locked_limit_up_breakout | 鎖量漲停突破 | 2722 |
| high_position_breakout | 高位階突破 | 1322 |
| standard_breakout | 一般突破 | 401 |
| wide_range_breakout | 寬區間突破 | 173 |
| long_base_low_position | 長盤整低位階突破 | 95 |
| low_position_breakout | 低位階突破 | 60 |

## Best Operation Patterns By Classification

| classification_id | pattern_id | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_avg_return | confidence_status | out_of_sample_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| high_position_breakout | next_open_hold_20d | 1245 | 48.27 | 5.6215 | -0.3509 | 514 | 8.7768 | high | True |
| high_position_breakout | pullback_10ma_hold_10d | 860 | 53.14 | 3.9597 | 0.6936 | 369 | 6.0535 | high | True |
| high_position_breakout | pullback_5ma_hold_10d | 1190 | 50.5 | 3.3989 | 0.2519 | 509 | 5.3312 | high | True |
| locked_limit_up_breakout | pullback_10ma_hold_10d | 1594 | 53.01 | 4.3713 | 0.8585 | 802 | 5.8669 | high | True |
| locked_limit_up_breakout | next_open_hold_20d | 2520 | 45.95 | 4.3558 | -1.8424 | 1170 | 5.934 | high | False |
| locked_limit_up_breakout | signal_close_hold_5d | 2722 | 51.43 | 3.394 | 0.563 | 1372 | 4.1231 | high | True |
| long_base_low_position | pullback_5ma_hold_10d | 89 | 51.69 | 2.5735 | 0.1473 | 36 | 2.0688 | low | True |
| long_base_low_position | next_open_hold_20d | 93 | 47.31 | 2.3624 | -1.275 | 37 | 1.2683 | low | False |
| long_base_low_position | pullback_10ma_hold_10d | 66 | 62.12 | 2.0202 | 1.4374 | 28 | 1.9422 | low | False |
| low_position_breakout | next_open_hold_20d | 57 | 40.35 | 3.1291 | -1.9934 | 24 | 6.4006 | low | False |
| low_position_breakout | next_day_break_signal_high_hold_10d | 32 | 25.0 | 1.7332 | -7.594 | 10 | -4.58 | low | False |
| low_position_breakout | next_open_signal_low_stop_10d | 57 | 19.3 | 1.071 | -3.9648 | 24 | -2.7298 | low | False |
| standard_breakout | pullback_10ma_hold_10d | 263 | 46.01 | 0.5941 | -0.6865 | 26 | 4.317 | medium | False |
| standard_breakout | next_day_break_signal_high_hold_10d | 247 | 44.94 | 0.5608 | -1.2146 | 27 | -1.4619 | medium | False |
| standard_breakout | pullback_5ma_hold_10d | 368 | 44.57 | 0.2027 | -0.6846 | 34 | 1.4048 | medium | True |
| wide_range_breakout | next_open_hold_20d | 171 | 47.37 | 3.8226 | -0.5731 | 36 | 14.1991 | medium | True |
| wide_range_breakout | pullback_5ma_hold_10d | 163 | 53.37 | 2.6277 | 0.5795 | 33 | 6.161 | medium | True |
| wide_range_breakout | next_day_break_signal_high_hold_10d | 91 | 47.25 | 2.3257 | -0.3686 | 21 | 5.6697 | low | False |
