# Volume Breakout Pattern Classification

- generated_at: `2026-06-14 21:35:49 Asia/Taipei`
- model_id: `volume_range_breakout`
- unique_event_rows: `4068`
- summary_rows: `119`
- scope: current model hits only; research classification, not production promotion.
- approved_for_daily: always `False` in this artifact.

## Classification Counts

| classification_id | classification_name_zh | event_count |
| --- | --- | --- |
| limit_up_like_breakout | 類漲停放量突破 | 1913 |
| high_position_breakout | 高位階突破 | 1312 |
| locked_limit_up_breakout | 鎖量漲停突破 | 252 |
| standard_breakout | 一般突破 | 243 |
| low_position_breakout | 低位階突破 | 127 |
| long_base_low_position | 長盤整低位階突破 | 112 |
| wide_range_breakout | 寬區間突破 | 109 |

## Best Operation Patterns By Classification

| classification_id | pattern_id | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_avg_return | confidence_status | out_of_sample_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| high_position_breakout | next_open_hold_20d | 1202 | 46.51 | 4.38 | -1.0281 | 424 | 9.7704 | high | True |
| high_position_breakout | pullback_10ma_hold_10d | 834 | 53.24 | 3.4603 | 0.6446 | 319 | 7.1514 | high | True |
| high_position_breakout | pullback_5ma_hold_10d | 1174 | 49.74 | 3.0793 | -0.0132 | 447 | 6.8612 | high | True |
| limit_up_like_breakout | next_open_hold_20d | 1736 | 47.0 | 6.4805 | -1.1241 | 664 | 13.02 | high | True |
| limit_up_like_breakout | pullback_10ma_hold_10d | 1085 | 53.09 | 4.3499 | 0.8206 | 472 | 7.5686 | high | True |
| limit_up_like_breakout | pullback_5ma_hold_10d | 1613 | 51.27 | 3.6524 | 0.4518 | 654 | 6.3507 | high | True |
| locked_limit_up_breakout | next_open_hold_20d | 178 | 52.81 | 10.8254 | 1.0688 | 121 | 16.318 | medium | True |
| locked_limit_up_breakout | signal_close_hold_5d | 252 | 60.71 | 7.5556 | 4.0576 | 195 | 9.0096 | medium | True |
| locked_limit_up_breakout | next_open_10ma_trailing_20d | 178 | 39.33 | 7.486 | -3.572 | 121 | 10.3981 | medium | False |
| long_base_low_position | next_open_hold_20d | 101 | 50.5 | 2.8732 | 0.4839 | 16 | 5.5735 | medium | False |
| long_base_low_position | pullback_5ma_hold_10d | 98 | 51.02 | 2.5191 | 0.1259 | 22 | 2.2976 | low | False |
| long_base_low_position | pullback_10ma_hold_10d | 70 | 55.71 | 2.1639 | 0.6941 | 15 | 1.4478 | low | False |
| low_position_breakout | next_open_hold_20d | 125 | 47.2 | 6.449 | -0.4098 | 22 | 6.4855 | medium | False |
| low_position_breakout | next_day_break_signal_high_hold_10d | 76 | 43.42 | 3.6375 | -2.0312 | 11 | -6.2858 | low | False |
| low_position_breakout | pullback_5ma_hold_10d | 116 | 50.86 | 3.619 | 0.6013 | 21 | -1.3021 | medium | False |
| standard_breakout | next_open_hold_20d | 236 | 40.68 | 0.2218 | -2.2237 | 21 | 5.1652 | medium | False |
| standard_breakout | next_day_break_signal_high_hold_10d | 149 | 42.95 | 0.0235 | -1.4825 | 20 | -0.9599 | medium | False |
| standard_breakout | pullback_10ma_hold_10d | 160 | 41.25 | -0.2853 | -0.8761 | 17 | 1.6923 | medium | False |
| wide_range_breakout | next_open_hold_20d | 107 | 57.01 | 6.5445 | 1.6129 | 36 | 13.1472 | medium | True |
| wide_range_breakout | pullback_10ma_hold_10d | 73 | 57.53 | 4.5155 | 1.2389 | 27 | 10.8374 | low | False |
| wide_range_breakout | pullback_5ma_hold_10d | 103 | 57.28 | 3.2941 | 1.4451 | 34 | 4.3089 | medium | True |
