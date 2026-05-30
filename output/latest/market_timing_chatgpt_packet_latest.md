# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-05-30 17:32:29 Asia/Taipei
- main_price_date: 20260529
- index_list: TPEX, TWSE
- data_range: 20241202 ~ 20260529
- source_files: data/market_index_history.csv, data/market_index_ohlc_history.csv, output/history/market_timing/market_breadth_history.csv, output/history/market_timing/market_technical_event_log.csv
- tuning_status: not_ready

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | market_regime | risk_level | trend_summary | momentum_summary | kd_summary | volatility_summary | volume_flow_summary | breadth_summary | futures_options_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPEX | 20260529 | 443.64 | 4.82 | 15.36 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 健康 | 擴散 | 期權資料已整合 |
| TWSE | 20260529 | 44732.94 | 5.83 | 14.92 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 健康 | 擴散 | 期權資料已整合 |

## Six-Layer Technical Summary
### 趨勢 / 均線
- current_state: MA/EMA、均線距離、斜率、交叉與排列。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

### 動能指標
- current_state: MACD、RSI、ROC、Williams、CCI。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

### KD / 隨機指標
- current_state: KD 低檔轉強、高檔轉弱、超買超賣與鈍化。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

### 波動 / 通道
- current_state: Bollinger、ATR、Keltner、Donchian。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

### 價量 / 資金
- current_state: 量比、OBV、MFI、A/D、CMF。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

### 市場廣度 / 內部結構
- current_state: 上漲下跌家數、站上均線比例、創高創低與候選數。
- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。

## Active Technical Events
| event_date | index_id | event_name | event_group | close_on_event | market_regime | risk_level |
| --- | --- | --- | --- | --- | --- | --- |
| 20260525 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 43644.4 | strong_bull | low_risk |
| 20260525 | TWSE | adx_trend_plus_di_dominant | trend_ma | 43644.4 | strong_bull | low_risk |
| 20260525 | TPEX | adx_trend_plus_di_dominant | trend_ma | 434.99 | strong_bull | low_risk |
| 20260525 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 434.99 | strong_bull | low_risk |
| 20260526 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 439.3 | strong_bull | low_risk |
| 20260526 | TWSE | adx_trend_plus_di_dominant | trend_ma | 43525.37 | strong_bull | low_risk |
| 20260526 | TWSE | composite_bull_confirmation | composite_signal | 43525.37 | strong_bull | low_risk |
| 20260526 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 43525.37 | strong_bull | low_risk |
| 20260526 | TWSE | macd_hist_turn_positive | momentum | 43525.37 | strong_bull | low_risk |
| 20260527 | TWSE | bb_upper_breakout_long_upper_shadow | volatility_channel | 44256.8 | strong_bull | low_risk |
| 20260527 | TWSE | composite_bull_confirmation | composite_signal | 44256.8 | strong_bull | low_risk |
| 20260527 | TWSE | adx_trend_plus_di_dominant | trend_ma | 44256.8 | strong_bull | low_risk |
| 20260527 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 44256.8 | strong_bull | low_risk |
| 20260527 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 440.19 | strong_bull | low_risk |
| 20260527 | TPEX | composite_bull_confirmation | composite_signal | 440.19 | strong_bull | low_risk |
| 20260527 | TPEX | macd_hist_turn_positive | momentum | 440.19 | strong_bull | low_risk |
| 20260528 | TWSE | adx_trend_plus_di_dominant | trend_ma | 43636.44 | strong_bull | low_risk |
| 20260528 | TWSE | composite_bull_confirmation | composite_signal | 43636.44 | strong_bull | low_risk |
| 20260528 | TPEX | composite_bull_confirmation | composite_signal | 432.48 | strong_bull | low_risk |
| 20260528 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 432.48 | strong_bull | low_risk |
| 20260528 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 43636.44 | strong_bull | low_risk |
| 20260529 | TWSE | composite_bull_confirmation | composite_signal | 44732.94 | strong_bull | low_risk |
| 20260529 | TWSE | adx_trend_plus_di_dominant | trend_ma | 44732.94 | strong_bull | low_risk |
| 20260529 | TWSE | high_put_call_ratio_index_holds_ma20 | futures_options | 44732.94 | strong_bull | low_risk |
| 20260529 | TPEX | high_put_call_ratio_index_holds_ma20 | futures_options | 443.64 | strong_bull | low_risk |
| 20260529 | TPEX | composite_bull_confirmation | composite_signal | 443.64 | strong_bull | low_risk |
| 20260529 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 443.64 | strong_bull | low_risk |
| 20260529 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 44732.94 | strong_bull | low_risk |

## Event Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 8 | 5 | 3.16 | 100.00 | 5 | -0.20 | 40.00 | 0 |  |  | D+5 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 79 | 75 | 0.64 | 61.33 | 75 | 1.67 | 64.00 | 71 | 3.87 | 77.46 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| high_put_call_ratio_index_holds_ma20 | TPEX | 1 | 0 |  |  | 0 |  |  | 0 |  |  |  | D+1:pending_only;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| high_put_call_ratio_index_holds_ma20 | TWSE | 1 | 0 |  |  | 0 |  |  | 0 |  |  |  | D+1:pending_only;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| kd_high_death_cross | TPEX | 17 | 17 | 1.65 | 82.35 | 17 | 2.97 | 76.47 | 16 | 4.68 | 81.25 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_high_death_cross | TWSE | 29 | 29 | 0.70 | 58.62 | 29 | 2.14 | 68.97 | 28 | 3.66 | 82.14 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| kd_low_golden_cross | TPEX | 6 | 6 | 2.06 | 83.33 | 6 | 2.75 | 83.33 | 6 | 4.26 | 83.33 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_low_golden_cross | TWSE | 4 | 4 | 1.15 | 75.00 | 4 | 0.54 | 75.00 | 4 | 0.86 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | 5 | 5 | -1.52 | 40.00 | 5 | 1.92 | 60.00 | 4 | 6.04 | 100.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | 10 | 10 | 1.99 | 80.00 | 10 | 2.73 | 80.00 | 9 | 5.97 | 88.89 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TPEX | 6 | 6 | 0.01 | 66.67 | 6 | 1.45 | 66.67 | 6 | 2.65 | 66.67 | D+20 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TWSE | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | 50.00 | 2 | 0.06 | 50.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TPEX | 16 | 15 | 0.16 | 53.33 | 15 | 1.64 | 53.33 | 15 | 4.05 | 60.00 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TWSE | 20 | 19 | 0.85 | 68.42 | 19 | 0.85 | 52.63 | 19 | 3.00 | 63.16 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_overbought_70 | TPEX | 74 | 74 | 1.15 | 60.81 | 74 | 2.77 | 72.97 | 66 | 5.19 | 84.85 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_overbought_70 | TWSE | 90 | 90 | 0.79 | 64.44 | 90 | 2.47 | 77.78 | 81 | 5.33 | 87.65 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_oversold_30 | TPEX | 13 | 13 | 1.86 | 76.92 | 13 | 1.92 | 61.54 | 13 | 2.39 | 69.23 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_oversold_30 | TWSE | 11 | 11 | 2.59 | 81.82 | 11 | 1.03 | 45.45 | 11 | -2.55 | 45.45 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | 152 | 151 | 0.98 | 62.25 | 146 | 2.16 | 70.55 | 136 | 3.22 | 75.00 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| adx_trend_plus_di_dominant | TWSE | 206 | 201 | 1.26 | 67.66 | 196 | 2.46 | 75.00 | 186 | 4.55 | 87.63 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| golden_cross_ma20_ma60 | TPEX | 3 | 3 | 1.45 | 66.67 | 3 | 0.52 | 33.33 | 3 | 3.27 | 66.67 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | 5 | 5 | -0.75 | 20.00 | 5 | -0.22 | 60.00 | 5 | -0.83 | 60.00 | D+10 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | 186 | 181 | 1.01 | 59.67 | 178 | 2.67 | 68.54 | 168 | 5.20 | 74.40 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | 226 | 221 | 1.04 | 65.61 | 218 | 2.14 | 71.56 | 208 | 4.18 | 80.77 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TPEX | 24 | 24 | 1.18 | 70.83 | 23 | 1.86 | 65.22 | 23 | 3.33 | 69.57 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TWSE | 22 | 22 | 0.81 | 63.64 | 21 | 1.23 | 61.90 | 21 | 4.45 | 76.19 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TPEX | 7 | 7 | 2.76 | 71.43 | 7 | 4.87 | 85.71 | 7 | 10.47 | 85.71 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | 9 | 8 | 0.70 | 75.00 | 8 | 1.50 | 62.50 | 8 | 3.56 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| high_volume_long_black_break_ma20_ema23 | TWSE | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | 100.00 | 2 | 14.71 | 100.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |

## Composite Signal Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 8 | 5 | 3.16 | 100.00 | 5 | -0.20 | 40.00 | D+5 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 79 | 75 | 0.64 | 61.33 | 75 | 1.67 | 64.00 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |

## Regime Sensitivity
| event_name | index_id | market_regime | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adx_trend_plus_di_dominant | TPEX | correction | 6 | 6 | 4.48 | 83.33 | 4 | 1.70 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | high_risk | 10 | 10 | 0.72 | 70.00 | 10 | 2.40 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | mild_bull | 35 | 35 | 0.59 | 57.14 | 34 | 0.91 | ok |
| adx_trend_plus_di_dominant | TPEX | range_bound | 19 | 19 | 0.51 | 47.37 | 19 | 0.89 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | strong_bull | 82 | 81 | 1.02 | 65.43 | 79 | 2.99 | ok |
| adx_trend_plus_di_dominant | TWSE | correction | 10 | 10 | 3.34 | 80.00 | 8 | 1.23 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | high_risk | 5 | 5 | 1.81 | 100.00 | 5 | 6.28 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | mild_bull | 57 | 57 | 0.74 | 59.65 | 57 | 2.13 | ok |
| adx_trend_plus_di_dominant | TWSE | range_bound | 6 | 6 | 3.83 | 100.00 | 6 | 3.66 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | strong_bull | 128 | 123 | 1.19 | 67.48 | 120 | 2.48 | ok |
| bb_upper_breakout_long_upper_shadow | TPEX | mild_bull | 4 | 4 | 0.35 | 50.00 | 4 | 2.52 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TPEX | strong_bull | 3 | 3 | 5.97 | 100.00 | 3 | 8.01 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | mild_bull | 1 | 1 | -3.61 | 0.00 | 1 | -1.49 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | strong_bull | 8 | 7 | 1.31 | 85.71 | 7 | 1.93 | insufficient_sample |
| composite_bull_confirmation | TPEX | strong_bull | 8 | 5 | 3.16 | 100.00 | 5 | -0.20 | insufficient_sample |
| composite_bull_confirmation | TWSE | mild_bull | 21 | 21 | 0.94 | 61.90 | 21 | 1.59 | insufficient_sample |
| composite_bull_confirmation | TWSE | range_bound | 2 | 2 | 1.39 | 100.00 | 2 | 0.98 | insufficient_sample |
| composite_bull_confirmation | TWSE | strong_bull | 56 | 52 | 0.49 | 59.62 | 52 | 1.73 | ok |
| golden_cross_ma20_ma60 | TPEX | mild_bull | 1 | 1 | 1.45 | 100.00 | 1 | -0.68 | insufficient_sample |
| golden_cross_ma20_ma60 | TPEX | strong_bull | 2 | 2 | 1.46 | 50.00 | 2 | 1.13 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | correction | 1 | 1 | -0.24 | 0.00 | 1 | -1.67 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | mild_bull | 3 | 3 | -0.53 | 33.33 | 3 | -0.90 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | strong_bull | 1 | 1 | -1.90 | 0.00 | 1 | 3.28 | insufficient_sample |
| high_put_call_ratio_index_holds_ma20 | TPEX | strong_bull | 1 | 0 |  |  | 0 |  | pending_only |
| high_put_call_ratio_index_holds_ma20 | TWSE | strong_bull | 1 | 0 |  |  | 0 |  | pending_only |
| high_volume_long_black_break_ma20_ema23 | TWSE | high_risk | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | strong_bull | 5 | 5 | -1.52 | 40.00 | 5 | 1.92 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | strong_bull | 10 | 10 | 1.99 | 80.00 | 10 | 2.73 | insufficient_sample |
| kd_high_death_cross | TPEX | mild_bull | 5 | 5 | 0.08 | 60.00 | 5 | -0.16 | insufficient_sample |
| kd_high_death_cross | TPEX | range_bound | 2 | 2 | 1.66 | 100.00 | 2 | 0.42 | insufficient_sample |
| kd_high_death_cross | TPEX | strong_bull | 10 | 10 | 2.43 | 90.00 | 10 | 5.05 | insufficient_sample |
| kd_high_death_cross | TWSE | correction | 1 | 1 | -0.46 | 0.00 | 1 | -0.02 | insufficient_sample |
| kd_high_death_cross | TWSE | mild_bull | 9 | 9 | -0.21 | 44.44 | 9 | 0.10 | insufficient_sample |
| kd_high_death_cross | TWSE | range_bound | 1 | 1 | 6.02 | 100.00 | 1 | 6.12 | insufficient_sample |
| kd_high_death_cross | TWSE | strong_bull | 18 | 18 | 0.93 | 66.67 | 18 | 3.07 | insufficient_sample |
| kd_low_golden_cross | TPEX | correction | 2 | 2 | 2.20 | 100.00 | 2 | 0.76 | insufficient_sample |
| kd_low_golden_cross | TPEX | high_risk | 4 | 4 | 2.00 | 75.00 | 4 | 3.75 | insufficient_sample |
| kd_low_golden_cross | TWSE | correction | 2 | 2 | 1.45 | 100.00 | 2 | 3.03 | insufficient_sample |
| kd_low_golden_cross | TWSE | high_risk | 2 | 2 | 0.86 | 50.00 | 2 | -1.96 | insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | mild_bull | 78 | 78 | 0.42 | 51.28 | 77 | 1.69 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | strong_bull | 108 | 103 | 1.46 | 66.02 | 101 | 3.42 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | mild_bull | 86 | 86 | 0.77 | 61.63 | 86 | 1.56 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | strong_bull | 140 | 135 | 1.22 | 68.15 | 132 | 2.51 | ok |
| macd_dif_low_cross_signal | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_dif_low_cross_signal | TPEX | mild_bull | 2 | 2 | -3.15 | 0.00 | 2 | -2.51 | insufficient_sample |
| macd_dif_low_cross_signal | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_hist_turn_positive | TPEX | mild_bull | 7 | 7 | -0.69 | 42.86 | 7 | -0.73 | insufficient_sample |
| macd_hist_turn_positive | TPEX | strong_bull | 5 | 4 | 0.21 | 25.00 | 4 | 4.00 | insufficient_sample |
| macd_hist_turn_positive | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TWSE | mild_bull | 9 | 9 | 0.16 | 77.78 | 9 | 0.58 | insufficient_sample |
| macd_hist_turn_positive | TWSE | strong_bull | 9 | 8 | 1.79 | 62.50 | 8 | 2.29 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | high_risk | 5 | 5 | -0.25 | 80.00 | 5 | 1.87 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | mild_bull | 14 | 14 | 1.19 | 64.29 | 13 | 0.98 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | range_bound | 2 | 2 | 1.67 | 100.00 | 2 | 1.15 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | strong_bull | 3 | 3 | 3.22 | 66.67 | 3 | 6.18 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | high_risk | 1 | 1 | 3.32 | 100.00 | 1 | 6.32 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | mild_bull | 16 | 16 | 0.52 | 62.50 | 16 | 1.51 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | strong_bull | 5 | 5 | 1.24 | 60.00 | 4 | -1.19 | insufficient_sample |
| rsi14_overbought_70 | TPEX | high_risk | 1 | 1 | -1.33 | 0.00 | 1 | 4.03 | insufficient_sample |

## Time Effect Summary
- D+1 / D+3: 適合檢查短線轉折、假突破、KD 高低檔交叉。
- D+5 / D+10: 適合檢查 MACD 翻正、站回 MA20、期權極端後回歸。
- D+20 / D+40 / D+60: 適合檢查均線黃金交叉與中期趨勢事件。
- 樣本不足時只能標示待回測假設，目前只作為觀察，不作為模型加權依據。

## Data Quality Notes
- missing_fields: TWSE_history_had_large_gap_keep_latest_continuous_segment
- pending_events: 116
- benchmark_available: TWSE/TPEX index history available=True
- regime_available: True
- breadth_available: True
- mature_counts: {'mature_d1_count': 1227, 'mature_d3_count': 1215, 'mature_d5_count': 1206, 'mature_d10_count': 1188, 'mature_d20_count': 1118, 'mature_d40_count': 1016, 'mature_d60_count': 981}

## Model Tuning Recommendation
- tuning_status = not_ready
- allowed_changes = reporting_only
- forbidden_changes = core_weight_change
- reason = market timing event samples still need mature D+10 / D+20 accumulation before formal weighting.
