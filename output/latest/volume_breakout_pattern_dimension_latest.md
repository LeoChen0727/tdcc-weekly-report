# Volume Breakout Pattern Dimensions

- generated_at: `2026-06-14 17:09:30 Asia/Taipei`
- model_id: `volume_range_breakout`
- unique_event_rows: `4068`
- dimensions: consolidation, price position, attack method, candle quality, follow-through, risk type.
- scope: research only; all rows keep `approved_for_daily=False`.

## Dimension Counts

| dimension_type | dimension_type_zh | dimension_id | dimension_name_zh | event_count |
| --- | --- | --- | --- | --- |
| consolidation_type | 盤整型態 | long_consolidation | 長盤整 | 1599 |
| consolidation_type | 盤整型態 | non_consolidation | 非盤整 | 2174 |
| consolidation_type | 盤整型態 | short_consolidation | 短盤整 | 295 |
| price_position_type | 位階 | high_position | 高位階 | 2971 |
| price_position_type | 位階 | low_position | 低位階 | 465 |
| price_position_type | 位階 | middle_position | 中位階 | 315 |
| price_position_type | 位階 | unknown_position | 位階資料不足 | 317 |
| attack_method | 攻擊方式 | general_breakout | 一般突破 | 1275 |
| attack_method | 攻擊方式 | locked_limit_up | 鎖量漲停 | 252 |
| attack_method | 攻擊方式 | volume_attack | 放量攻擊 | 2541 |
| candle_quality | K棒品質 | close_at_high | 收最高 | 2130 |
| candle_quality | K棒品質 | explosive_long_red | 爆量長紅 | 657 |
| candle_quality | K棒品質 | false_breakout | 假突破 | 473 |
| candle_quality | K棒品質 | standard_candle | 一般K棒 | 501 |
| candle_quality | K棒品質 | upper_shadow | 留上影 | 307 |
| follow_through_type | 後續走法 | break_signal_low | 跌破訊號低點 | 1844 |
| follow_through_type | 後續走法 | next_day_continuation | 隔日續強 | 1206 |
| follow_through_type | 後續走法 | next_day_gap_fade | 隔日開高走低 | 622 |
| follow_through_type | 後續走法 | pullback_10ma | 回測10MA | 313 |
| follow_through_type | 後續走法 | pullback_5ma | 回測5MA | 83 |
| risk_type | 風險型態 | breakout_failure | 突破失敗 | 1907 |
| risk_type | 風險型態 | high_position_chase | 高位階追價 | 1334 |
| risk_type | 風險型態 | normal_risk | 一般風險 | 530 |
| risk_type | 風險型態 | stop_loss_easy_trigger | 停損容易被打到 | 104 |
| risk_type | 風險型態 | volume_overheat | 量能過熱 | 193 |

## Best Operation Patterns By Dimension

| dimension_type | dimension_id | dimension_name_zh | pattern_id | event_count | win_rate | avg_return | median_return | confidence_status | out_of_sample_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| attack_method | general_breakout | 一般突破 | next_open_hold_20d | 1146 | 50.96 | 7.3729 | 0.7984 | high | True |
| attack_method | general_breakout | 一般突破 | pullback_10ma_hold_10d | 731 | 53.9 | 4.0931 | 0.8082 | high | True |
| attack_method | locked_limit_up | 鎖量漲停 | next_open_hold_20d | 178 | 52.81 | 10.8254 | 1.0688 | medium | True |
| attack_method | locked_limit_up | 鎖量漲停 | signal_close_hold_5d | 252 | 60.71 | 7.5556 | 4.0576 | medium | True |
| attack_method | volume_attack | 放量攻擊 | next_open_hold_20d | 2361 | 44.81 | 4.1993 | -1.864 | high | True |
| attack_method | volume_attack | 放量攻擊 | pullback_10ma_hold_10d | 1569 | 51.69 | 3.2626 | 0.3567 | high | True |
| candle_quality | close_at_high | 收最高 | next_open_hold_20d | 1888 | 48.41 | 7.244 | -0.4425 | high | True |
| candle_quality | close_at_high | 收最高 | pullback_10ma_hold_10d | 1133 | 52.52 | 4.2695 | 0.6207 | high | True |
| candle_quality | explosive_long_red | 爆量長紅 | next_open_hold_20d | 616 | 49.03 | 6.0264 | 0.0 | high | True |
| candle_quality | explosive_long_red | 爆量長紅 | pullback_10ma_hold_10d | 394 | 52.54 | 3.6176 | 0.6422 | medium | True |
| candle_quality | false_breakout | 假突破 | pullback_10ma_hold_10d | 395 | 50.13 | 2.7581 | 0.0096 | medium | True |
| candle_quality | false_breakout | 假突破 | pullback_5ma_hold_10d | 455 | 45.27 | 1.8835 | -0.939 | medium | True |
| candle_quality | standard_candle | 一般K棒 | next_open_hold_20d | 470 | 51.91 | 6.1014 | 0.9286 | medium | True |
| candle_quality | standard_candle | 一般K棒 | pullback_10ma_hold_10d | 292 | 54.11 | 4.0131 | 0.7938 | medium | True |
| candle_quality | upper_shadow | 留上影 | next_open_hold_20d | 287 | 50.17 | 4.4042 | 0.2494 | medium | True |
| candle_quality | upper_shadow | 留上影 | next_day_break_signal_high_hold_10d | 124 | 54.03 | 3.6665 | 1.1715 | medium | True |
| consolidation_type | long_consolidation | 長盤整 | pullback_10ma_hold_10d | 993 | 49.45 | 1.9779 | 0.0 | high | True |
| consolidation_type | long_consolidation | 長盤整 | signal_close_hold_5d | 1599 | 44.22 | 1.1872 | -0.8489 | high | False |
| consolidation_type | non_consolidation | 非盤整 | next_open_hold_20d | 1921 | 51.95 | 9.3623 | 1.1538 | high | True |
| consolidation_type | non_consolidation | 非盤整 | pullback_10ma_hold_10d | 1218 | 55.34 | 5.4892 | 1.9512 | high | True |
| consolidation_type | short_consolidation | 短盤整 | next_open_hold_20d | 279 | 45.52 | 2.49 | -1.0846 | medium | False |
| consolidation_type | short_consolidation | 短盤整 | pullback_5ma_hold_10d | 261 | 52.49 | 1.4841 | 0.5807 | medium | True |
| follow_through_type | break_signal_low | 跌破訊號低點 | pullback_10ma_hold_10d | 1430 | 51.12 | 3.4851 | 0.247 | high | True |
| follow_through_type | break_signal_low | 跌破訊號低點 | pullback_5ma_hold_10d | 1705 | 44.52 | 1.4346 | -1.1438 | high | True |
| follow_through_type | next_day_continuation | 隔日續強 | next_open_hold_20d | 1095 | 62.47 | 16.2166 | 5.8659 | high | True |
| follow_through_type | next_day_continuation | 隔日續強 | next_open_10ma_trailing_20d | 1095 | 60.55 | 12.1118 | 2.5455 | high | True |
| follow_through_type | next_day_gap_fade | 隔日開高走低 | next_open_hold_20d | 573 | 52.36 | 5.8942 | 0.9537 | high | True |
| follow_through_type | next_day_gap_fade | 隔日開高走低 | pullback_10ma_hold_10d | 303 | 61.06 | 4.2875 | 1.9466 | medium | True |
| follow_through_type | pullback_10ma | 回測10MA | pullback_10ma_hold_10d | 211 | 54.98 | 4.3908 | 0.9615 | medium | True |
| follow_through_type | pullback_10ma | 回測10MA | next_open_hold_20d | 297 | 47.81 | 3.4297 | -0.4243 | medium | True |
| follow_through_type | pullback_5ma | 回測5MA | next_open_hold_20d | 76 | 90.79 | 23.8982 | 19.3943 | low | False |
| follow_through_type | pullback_5ma | 回測5MA | next_open_10ma_trailing_20d | 76 | 98.68 | 22.8478 | 17.3682 | low | False |
| price_position_type | high_position | 高位階 | next_open_hold_20d | 2645 | 48.02 | 5.6904 | -0.5671 | high | True |
| price_position_type | high_position | 高位階 | pullback_10ma_hold_10d | 1745 | 53.81 | 4.596 | 0.8585 | high | True |
| price_position_type | low_position | 低位階 | next_open_hold_20d | 432 | 49.54 | 11.0839 | -0.2203 | medium | True |
| price_position_type | low_position | 低位階 | next_open_10ma_trailing_20d | 432 | 34.95 | 9.3422 | -2.733 | medium | False |
| price_position_type | middle_position | 中位階 | pullback_10ma_hold_10d | 191 | 52.88 | 2.8917 | 0.5096 | medium | True |
| price_position_type | middle_position | 中位階 | next_open_hold_20d | 291 | 45.36 | 2.6105 | -1.8072 | medium | True |
| price_position_type | unknown_position | 位階資料不足 | signal_close_hold_5d | 317 | 41.96 | -0.1646 | -1.2165 | medium | False |
| price_position_type | unknown_position | 位階資料不足 | next_open_tp10_signal_low_stop_20d | 317 | 35.65 | -0.3195 | -3.0508 | medium | False |
| risk_type | breakout_failure | 突破失敗 | pullback_10ma_hold_10d | 1471 | 51.46 | 3.4676 | 0.3567 | high | True |
| risk_type | breakout_failure | 突破失敗 | pullback_5ma_hold_10d | 1763 | 45.09 | 1.5792 | -1.0406 | high | True |
| risk_type | high_position_chase | 高位階追價 | next_open_hold_20d | 1203 | 60.18 | 13.0274 | 5.5046 | high | True |
| risk_type | high_position_chase | 高位階追價 | signal_close_hold_5d | 1334 | 73.31 | 8.9072 | 5.5258 | high | True |
| risk_type | normal_risk | 一般風險 | next_open_hold_20d | 507 | 57.2 | 8.0221 | 2.6786 | high | True |
| risk_type | normal_risk | 一般風險 | signal_close_hold_5d | 530 | 68.3 | 5.4909 | 2.8403 | high | True |
| risk_type | stop_loss_easy_trigger | 停損容易被打到 | next_open_10ma_trailing_20d | 92 | 61.96 | 28.5864 | 2.702 | low | False |
| risk_type | stop_loss_easy_trigger | 停損容易被打到 | next_open_5ma_trailing_20d | 92 | 61.96 | 28.4176 | 1.8623 | low | False |
| risk_type | volume_overheat | 量能過熱 | next_open_hold_20d | 187 | 51.34 | 8.9107 | 0.625 | medium | False |
| risk_type | volume_overheat | 量能過熱 | next_open_5ma_trailing_20d | 187 | 46.52 | 7.253 | -0.3135 | medium | False |
