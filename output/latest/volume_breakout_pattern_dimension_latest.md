# Volume Breakout Pattern Dimensions

- generated_at: `2026-07-19 11:11:20 Asia/Taipei`
- model_id: `volume_range_breakout`
- unique_event_rows: `4773`
- dimensions: consolidation, price position, attack method, candle quality, follow-through, risk type.
- scope: research only; all rows keep `approved_for_daily=False`.

## Dimension Counts

| dimension_type | dimension_type_zh | dimension_id | dimension_name_zh | event_count |
| --- | --- | --- | --- | --- |
| consolidation_type | 盤整型態 | long_consolidation | 長盤整 | 1705 |
| consolidation_type | 盤整型態 | non_consolidation | 非盤整 | 2712 |
| consolidation_type | 盤整型態 | short_consolidation | 短盤整 | 356 |
| price_position_type | 位階 | high_position | 高位階 | 3364 |
| price_position_type | 位階 | low_position | 低位階 | 289 |
| price_position_type | 位階 | middle_position | 中位階 | 332 |
| price_position_type | 位階 | unknown_position | 位階資料不足 | 788 |
| attack_method | 攻擊方式 | general_breakout | 一般突破 | 731 |
| attack_method | 攻擊方式 | locked_limit_up | 鎖量漲停 | 2722 |
| attack_method | 攻擊方式 | volume_attack | 放量攻擊 | 1320 |
| candle_quality | K棒品質 | close_at_high | 收最高 | 2625 |
| candle_quality | K棒品質 | explosive_long_red | 爆量長紅 | 702 |
| candle_quality | K棒品質 | false_breakout | 假突破 | 585 |
| candle_quality | K棒品質 | standard_candle | 一般K棒 | 537 |
| candle_quality | K棒品質 | upper_shadow | 留上影 | 324 |
| follow_through_type | 後續走法 | break_signal_low | 跌破訊號低點 | 2251 |
| follow_through_type | 後續走法 | next_day_continuation | 隔日續強 | 1418 |
| follow_through_type | 後續走法 | next_day_gap_fade | 隔日開高走低 | 677 |
| follow_through_type | 後續走法 | pullback_10ma | 回測10MA | 335 |
| follow_through_type | 後續走法 | pullback_5ma | 回測5MA | 92 |
| risk_type | 風險型態 | breakout_failure | 突破失敗 | 2321 |
| risk_type | 風險型態 | high_position_chase | 高位階追價 | 1505 |
| risk_type | 風險型態 | normal_risk | 一般風險 | 592 |
| risk_type | 風險型態 | stop_loss_easy_trigger | 停損容易被打到 | 117 |
| risk_type | 風險型態 | volume_overheat | 量能過熱 | 238 |

## Best Operation Patterns By Dimension

| dimension_type | dimension_id | dimension_name_zh | pattern_id | event_count | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| attack_method | general_breakout | 一般突破 | next_open_hold_20d | 700 | 47.57 | 4.0214 | -0.6274 | high | True |
| attack_method | general_breakout | 一般突破 | pullback_10ma_hold_10d | 484 | 49.38 | 2.3996 | -0.0158 | medium | True |
| attack_method | locked_limit_up | 鎖量漲停 | pullback_10ma_hold_10d | 1594 | 53.01 | 4.3713 | 0.8585 | high | True |
| attack_method | locked_limit_up | 鎖量漲停 | next_open_hold_20d | 2520 | 45.95 | 4.3558 | -1.8424 | high | False |
| attack_method | volume_attack | 放量攻擊 | next_open_hold_20d | 1261 | 46.07 | 4.1785 | -1.1507 | high | True |
| attack_method | volume_attack | 放量攻擊 | pullback_10ma_hold_10d | 863 | 52.61 | 3.1373 | 0.5544 | high | True |
| candle_quality | close_at_high | 收最高 | next_open_hold_20d | 2448 | 47.39 | 4.9494 | -0.9831 | high | True |
| candle_quality | close_at_high | 收最高 | signal_close_hold_5d | 2625 | 54.82 | 4.3957 | 1.3043 | high | True |
| candle_quality | explosive_long_red | 爆量長紅 | next_open_hold_20d | 670 | 49.7 | 6.1282 | 0.0 | high | True |
| candle_quality | explosive_long_red | 爆量長紅 | pullback_10ma_hold_10d | 425 | 52.71 | 3.7985 | 0.6074 | medium | True |
| candle_quality | false_breakout | 假突破 | pullback_10ma_hold_10d | 483 | 50.52 | 2.9781 | 0.0527 | medium | True |
| candle_quality | false_breakout | 假突破 | pullback_5ma_hold_10d | 552 | 44.93 | 1.6778 | -1.066 | high | False |
| candle_quality | standard_candle | 一般K棒 | next_open_hold_20d | 521 | 50.86 | 6.0381 | 0.7101 | high | True |
| candle_quality | standard_candle | 一般K棒 | pullback_10ma_hold_10d | 329 | 54.1 | 3.8613 | 0.8082 | medium | True |
| candle_quality | upper_shadow | 留上影 | next_open_hold_20d | 314 | 49.04 | 4.225 | -0.1825 | medium | True |
| candle_quality | upper_shadow | 留上影 | next_day_break_signal_high_hold_10d | 140 | 50.0 | 2.7524 | 0.1973 | medium | False |
| consolidation_type | long_consolidation | 長盤整 | pullback_10ma_hold_10d | 1099 | 50.68 | 2.1332 | 0.1815 | high | True |
| consolidation_type | long_consolidation | 長盤整 | signal_close_hold_5d | 1705 | 45.22 | 1.7117 | -0.823 | high | False |
| consolidation_type | non_consolidation | 非盤整 | next_open_hold_20d | 2496 | 49.56 | 6.5337 | -0.0658 | high | True |
| consolidation_type | non_consolidation | 非盤整 | pullback_10ma_hold_10d | 1606 | 53.67 | 5.026 | 1.3954 | high | True |
| consolidation_type | short_consolidation | 短盤整 | pullback_10ma_hold_10d | 236 | 50.42 | 1.7818 | 0.0677 | medium | True |
| consolidation_type | short_consolidation | 短盤整 | next_open_hold_20d | 346 | 44.22 | 1.7582 | -1.1429 | medium | False |
| follow_through_type | break_signal_low | 跌破訊號低點 | pullback_10ma_hold_10d | 1812 | 51.55 | 3.5048 | 0.3916 | high | True |
| follow_through_type | break_signal_low | 跌破訊號低點 | pullback_5ma_hold_10d | 2131 | 43.59 | 1.197 | -1.2876 | high | False |
| follow_through_type | next_day_continuation | 隔日續強 | next_open_hold_20d | 1353 | 62.08 | 13.1462 | 5.6944 | high | True |
| follow_through_type | next_day_continuation | 隔日續強 | signal_close_hold_5d | 1418 | 84.63 | 12.5431 | 8.6022 | high | True |
| follow_through_type | next_day_gap_fade | 隔日開高走低 | next_open_hold_20d | 647 | 51.62 | 5.7095 | 0.8651 | high | True |
| follow_through_type | next_day_gap_fade | 隔日開高走低 | pullback_10ma_hold_10d | 343 | 59.18 | 4.1485 | 1.5747 | medium | True |
| follow_through_type | pullback_10ma | 回測10MA | pullback_10ma_hold_10d | 224 | 56.7 | 4.714 | 1.3214 | medium | True |
| follow_through_type | pullback_10ma | 回測10MA | next_open_hold_20d | 323 | 49.23 | 4.1486 | 0.0 | medium | True |
| follow_through_type | pullback_5ma | 回測5MA | next_open_hold_20d | 86 | 91.86 | 23.8536 | 19.4969 | low | False |
| follow_through_type | pullback_5ma | 回測5MA | pullback_5ma_hold_10d | 64 | 100.0 | 23.1584 | 16.9545 | low | False |
| price_position_type | high_position | 高位階 | next_open_hold_20d | 3110 | 48.65 | 6.0024 | -0.3956 | high | True |
| price_position_type | high_position | 高位階 | pullback_10ma_hold_10d | 2048 | 54.88 | 4.9774 | 1.3896 | high | True |
| price_position_type | low_position | 低位階 | pullback_5ma_hold_10d | 259 | 44.79 | 1.5186 | -0.6336 | medium | False |
| price_position_type | low_position | 低位階 | pullback_10ma_hold_10d | 202 | 50.0 | 1.4756 | 0.1015 | medium | True |
| price_position_type | middle_position | 中位階 | pullback_10ma_hold_10d | 201 | 54.23 | 3.2183 | 0.706 | medium | True |
| price_position_type | middle_position | 中位階 | next_open_hold_20d | 303 | 47.19 | 2.6053 | -0.6689 | medium | True |
| price_position_type | unknown_position | 位階資料不足 | signal_close_hold_5d | 788 | 44.54 | 0.707 | -0.9191 | high | False |
| price_position_type | unknown_position | 位階資料不足 | pullback_5ma_hold_10d | 730 | 45.48 | 0.1312 | -0.8723 | high | False |
| risk_type | breakout_failure | 突破失敗 | pullback_10ma_hold_10d | 1861 | 51.69 | 3.4633 | 0.4001 | high | True |
| risk_type | breakout_failure | 突破失敗 | pullback_5ma_hold_10d | 2197 | 44.11 | 1.3184 | -1.1757 | high | False |
| risk_type | high_position_chase | 高位階追價 | next_open_hold_20d | 1416 | 62.29 | 13.6696 | 6.3932 | high | True |
| risk_type | high_position_chase | 高位階追價 | signal_close_hold_5d | 1505 | 76.88 | 10.6882 | 7.0866 | high | True |
| risk_type | normal_risk | 一般風險 | next_open_hold_20d | 583 | 54.55 | 6.6702 | 1.7751 | high | True |
| risk_type | normal_risk | 一般風險 | signal_close_hold_5d | 592 | 66.89 | 5.1339 | 2.6218 | high | True |
| risk_type | stop_loss_easy_trigger | 停損容易被打到 | signal_close_hold_5d | 117 | 92.31 | 10.5688 | 6.3492 | medium | True |
| risk_type | stop_loss_easy_trigger | 停損容易被打到 | next_day_break_signal_high_hold_10d | 97 | 62.89 | 7.3473 | 3.4826 | low | False |
| risk_type | volume_overheat | 量能過熱 | signal_close_hold_5d | 238 | 62.61 | 4.5411 | 1.8407 | medium | True |
| risk_type | volume_overheat | 量能過熱 | next_open_hold_20d | 230 | 47.83 | 3.071 | -0.653 | medium | False |
