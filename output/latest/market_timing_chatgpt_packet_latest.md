# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-06-05 19:16:04 Asia/Taipei
- main_price_date: 20260604
- index_list: TPEX, TWSE
- data_range: 20241202 ~ 20260604
- source_files: data/market_index_history.csv, data/market_index_ohlc_history.csv, output/history/market_timing/market_breadth_history.csv, output/history/market_timing/market_technical_event_log.csv
- tuning_status: not_ready

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | market_regime | risk_level | trend_summary | momentum_summary | kd_summary | volatility_summary | volume_flow_summary | breadth_summary | futures_options_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPEX | 20260604 | 440.1 | 1.76 | 5.69 | strong_bull | low_risk | 多頭 | 中性 | 高檔轉弱 | 正常 | 中性 | 擴散 | 期權資料已整合 |
| TWSE | 20260604 | 45677.46 | 4.68 | 8.93 | strong_bull | elevated_risk | 多頭 | 增強 | 中性 | 放大 | 出貨疑慮 | 擴散 | 期權資料已整合 |

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
| 20260529 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 443.64 | strong_bull | low_risk |
| 20260529 | TWSE | adx_trend_plus_di_dominant | trend_ma | 44732.94 | strong_bull | low_risk |
| 20260529 | TWSE | composite_bull_confirmation | composite_signal | 44732.94 | strong_bull | low_risk |
| 20260529 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 44732.94 | strong_bull | low_risk |
| 20260601 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45337.91 | strong_bull | low_risk |
| 20260601 | TWSE | bb_upper_breakout_long_upper_shadow | volatility_channel | 45337.91 | strong_bull | low_risk |
| 20260601 | TWSE | composite_bull_confirmation | composite_signal | 45337.91 | strong_bull | low_risk |
| 20260601 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 446.02 | strong_bull | low_risk |
| 20260601 | TPEX | composite_bull_confirmation | composite_signal | 446.02 | strong_bull | low_risk |
| 20260601 | TWSE | adx_trend_plus_di_dominant | trend_ma | 45337.91 | strong_bull | low_risk |
| 20260602 | TPEX | composite_bull_confirmation | composite_signal | 440.64 | strong_bull | low_risk |
| 20260602 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 440.64 | strong_bull | low_risk |
| 20260602 | TWSE | adx_trend_plus_di_dominant | trend_ma | 45557.31 | strong_bull | elevated_risk |
| 20260602 | TWSE | composite_bull_confirmation | composite_signal | 45557.31 | strong_bull | elevated_risk |
| 20260602 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45557.31 | strong_bull | elevated_risk |
| 20260602 | TWSE | rsi14_overbought_70 | momentum | 45557.31 | strong_bull | elevated_risk |
| 20260603 | TWSE | rsi14_overbought_70 | momentum | 46459.16 | strong_bull | elevated_risk |
| 20260603 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 46459.16 | strong_bull | elevated_risk |
| 20260603 | TWSE | adx_trend_plus_di_dominant | trend_ma | 46459.16 | strong_bull | elevated_risk |
| 20260603 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 446.82 | strong_bull | low_risk |
| 20260603 | TWSE | composite_bull_confirmation | composite_signal | 46459.16 | strong_bull | elevated_risk |
| 20260604 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45677.46 | strong_bull | elevated_risk |
| 20260604 | TPEX | high_put_call_ratio_index_holds_ma20 | futures_options | 440.1 | strong_bull | low_risk |
| 20260604 | TPEX | kd_high_death_cross | kd_stochastic | 440.1 | strong_bull | low_risk |
| 20260604 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 440.1 | strong_bull | low_risk |
| 20260604 | TWSE | adx_trend_plus_di_dominant | trend_ma | 45677.46 | strong_bull | elevated_risk |
| 20260604 | TWSE | composite_bull_confirmation | composite_signal | 45677.46 | strong_bull | elevated_risk |
| 20260604 | TWSE | high_put_call_ratio_index_holds_ma20 | futures_options | 45677.46 | strong_bull | elevated_risk |
| 20260604 | TWSE | rsi14_overbought_70 | momentum | 45677.46 | strong_bull | elevated_risk |

## Event Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 2 | 0 |  |  | 0 |  |  | 0 |  |  | D+1 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 83 | 78 | 0.80 | 62.82 | 75 | 1.67 | 64.00 | 74 | 4.17 | 78.38 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| high_put_call_ratio_index_holds_ma20 | TPEX | 1 | 0 |  |  | 0 |  |  | 0 |  |  |  | D+1:pending_only;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| high_put_call_ratio_index_holds_ma20 | TWSE | 1 | 0 |  |  | 0 |  |  | 0 |  |  |  | D+1:pending_only;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| kd_high_death_cross | TPEX | 18 | 17 | 1.65 | 82.35 | 17 | 2.97 | 76.47 | 16 | 4.68 | 81.25 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_high_death_cross | TWSE | 29 | 29 | 0.70 | 58.62 | 29 | 2.14 | 68.97 | 28 | 3.66 | 82.14 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| kd_low_golden_cross | TPEX | 6 | 6 | 2.06 | 83.33 | 6 | 2.75 | 83.33 | 6 | 4.26 | 83.33 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_low_golden_cross | TWSE | 4 | 4 | 1.15 | 75.00 | 4 | 0.54 | 75.00 | 4 | 0.86 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | 8 | 8 | -0.78 | 50.00 | 8 | 2.61 | 75.00 | 7 | 6.36 | 100.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | 15 | 15 | 1.06 | 66.67 | 15 | 2.21 | 80.00 | 15 | 4.65 | 80.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TPEX | 6 | 6 | 0.01 | 66.67 | 6 | 1.45 | 66.67 | 6 | 2.65 | 66.67 | D+20 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TWSE | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | 50.00 | 2 | 0.06 | 50.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TPEX | 16 | 16 | 0.24 | 56.25 | 15 | 1.64 | 53.33 | 15 | 4.05 | 60.00 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TWSE | 20 | 20 | 1.04 | 70.00 | 19 | 0.85 | 52.63 | 19 | 3.00 | 63.16 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_overbought_70 | TPEX | 74 | 74 | 1.15 | 60.81 | 74 | 2.77 | 72.97 | 70 | 5.39 | 85.71 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_overbought_70 | TWSE | 93 | 90 | 0.79 | 64.44 | 90 | 2.47 | 77.78 | 85 | 5.61 | 88.24 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_oversold_30 | TPEX | 13 | 13 | 1.86 | 76.92 | 13 | 1.92 | 61.54 | 13 | 2.39 | 69.23 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_oversold_30 | TWSE | 11 | 11 | 2.59 | 81.82 | 11 | 1.03 | 45.45 | 11 | -2.55 | 45.45 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | 152 | 152 | 0.99 | 62.50 | 150 | 2.36 | 71.33 | 140 | 3.37 | 75.71 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| adx_trend_plus_di_dominant | TWSE | 210 | 205 | 1.33 | 68.29 | 200 | 2.66 | 75.50 | 190 | 4.69 | 87.89 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| golden_cross_ma20_ma60 | TPEX | 3 | 3 | 1.45 | 66.67 | 3 | 0.52 | 33.33 | 3 | 3.27 | 66.67 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | 5 | 5 | -0.75 | 20.00 | 5 | -0.22 | 60.00 | 5 | -0.83 | 60.00 | D+10 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | 190 | 185 | 1.02 | 60.54 | 180 | 2.74 | 68.89 | 172 | 5.29 | 75.00 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | 230 | 225 | 1.11 | 66.22 | 220 | 2.21 | 71.82 | 212 | 4.31 | 81.13 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TPEX | 24 | 24 | 1.18 | 70.83 | 24 | 2.09 | 66.67 | 23 | 3.33 | 69.57 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TWSE | 22 | 22 | 0.81 | 63.64 | 22 | 1.65 | 63.64 | 21 | 4.45 | 76.19 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TPEX | 7 | 7 | 2.76 | 71.43 | 7 | 4.87 | 85.71 | 7 | 10.47 | 85.71 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | 10 | 9 | 1.17 | 77.78 | 8 | 1.50 | 62.50 | 8 | 3.56 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| high_volume_long_black_break_ma20_ema23 | TWSE | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | 100.00 | 2 | 14.71 | 100.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |

## Composite Signal Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 2 | 0 |  |  | 0 |  |  | D+1 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 83 | 78 | 0.80 | 62.82 | 75 | 1.67 | 64.00 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |

## Regime Sensitivity
| event_name | index_id | market_regime | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adx_trend_plus_di_dominant | TPEX | correction | 6 | 6 | 4.48 | 83.33 | 6 | 5.03 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | high_risk | 10 | 10 | 0.72 | 70.00 | 10 | 2.40 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | mild_bull | 35 | 35 | 0.59 | 57.14 | 35 | 1.10 | ok |
| adx_trend_plus_di_dominant | TPEX | range_bound | 19 | 19 | 0.51 | 47.37 | 19 | 0.89 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | strong_bull | 82 | 82 | 1.04 | 65.85 | 80 | 3.06 | ok |
| adx_trend_plus_di_dominant | TWSE | correction | 10 | 10 | 3.34 | 80.00 | 10 | 3.94 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | high_risk | 5 | 5 | 1.81 | 100.00 | 5 | 6.28 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | mild_bull | 57 | 57 | 0.74 | 59.65 | 57 | 2.13 | ok |
| adx_trend_plus_di_dominant | TWSE | range_bound | 6 | 6 | 3.83 | 100.00 | 6 | 3.66 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | strong_bull | 132 | 127 | 1.29 | 68.50 | 122 | 2.61 | ok |
| bb_upper_breakout_long_upper_shadow | TPEX | mild_bull | 4 | 4 | 0.35 | 50.00 | 4 | 2.52 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TPEX | strong_bull | 3 | 3 | 5.97 | 100.00 | 3 | 8.01 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | mild_bull | 1 | 1 | -3.61 | 0.00 | 1 | -1.49 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | strong_bull | 9 | 8 | 1.77 | 87.50 | 7 | 1.93 | insufficient_sample |
| composite_bull_confirmation | TPEX | strong_bull | 2 | 0 |  |  | 0 |  | pending_only |
| composite_bull_confirmation | TWSE | mild_bull | 21 | 21 | 0.94 | 61.90 | 21 | 1.59 | insufficient_sample |
| composite_bull_confirmation | TWSE | range_bound | 2 | 2 | 1.39 | 100.00 | 2 | 0.98 | insufficient_sample |
| composite_bull_confirmation | TWSE | strong_bull | 60 | 55 | 0.72 | 61.82 | 52 | 1.73 | ok |
| golden_cross_ma20_ma60 | TPEX | mild_bull | 1 | 1 | 1.45 | 100.00 | 1 | -0.68 | insufficient_sample |
| golden_cross_ma20_ma60 | TPEX | strong_bull | 2 | 2 | 1.46 | 50.00 | 2 | 1.13 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | correction | 1 | 1 | -0.24 | 0.00 | 1 | -1.67 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | mild_bull | 3 | 3 | -0.53 | 33.33 | 3 | -0.90 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | strong_bull | 1 | 1 | -1.90 | 0.00 | 1 | 3.28 | insufficient_sample |
| high_put_call_ratio_index_holds_ma20 | TPEX | strong_bull | 1 | 0 |  |  | 0 |  | pending_only |
| high_put_call_ratio_index_holds_ma20 | TWSE | strong_bull | 1 | 0 |  |  | 0 |  | pending_only |
| high_volume_long_black_break_ma20_ema23 | TWSE | high_risk | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | mild_bull | 2 | 2 | 0.54 | 50.00 | 2 | 3.79 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | strong_bull | 6 | 6 | -1.22 | 50.00 | 6 | 2.22 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | strong_bull | 15 | 15 | 1.06 | 66.67 | 15 | 2.21 | insufficient_sample |
| kd_high_death_cross | TPEX | mild_bull | 5 | 5 | 0.08 | 60.00 | 5 | -0.16 | insufficient_sample |
| kd_high_death_cross | TPEX | range_bound | 2 | 2 | 1.66 | 100.00 | 2 | 0.42 | insufficient_sample |
| kd_high_death_cross | TPEX | strong_bull | 11 | 10 | 2.43 | 90.00 | 10 | 5.05 | insufficient_sample |
| kd_high_death_cross | TWSE | correction | 1 | 1 | -0.46 | 0.00 | 1 | -0.02 | insufficient_sample |
| kd_high_death_cross | TWSE | mild_bull | 9 | 9 | -0.21 | 44.44 | 9 | 0.10 | insufficient_sample |
| kd_high_death_cross | TWSE | range_bound | 1 | 1 | 6.02 | 100.00 | 1 | 6.12 | insufficient_sample |
| kd_high_death_cross | TWSE | strong_bull | 18 | 18 | 0.93 | 66.67 | 18 | 3.07 | insufficient_sample |
| kd_low_golden_cross | TPEX | correction | 2 | 2 | 2.20 | 100.00 | 2 | 0.76 | insufficient_sample |
| kd_low_golden_cross | TPEX | high_risk | 4 | 4 | 2.00 | 75.00 | 4 | 3.75 | insufficient_sample |
| kd_low_golden_cross | TWSE | correction | 2 | 2 | 1.45 | 100.00 | 2 | 3.03 | insufficient_sample |
| kd_low_golden_cross | TWSE | high_risk | 2 | 2 | 0.86 | 50.00 | 2 | -1.96 | insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | mild_bull | 78 | 78 | 0.42 | 51.28 | 78 | 1.77 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | strong_bull | 112 | 107 | 1.46 | 67.29 | 102 | 3.48 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | mild_bull | 86 | 86 | 0.77 | 61.63 | 86 | 1.56 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | strong_bull | 144 | 139 | 1.32 | 69.06 | 134 | 2.63 | ok |
| macd_dif_low_cross_signal | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_dif_low_cross_signal | TPEX | mild_bull | 2 | 2 | -3.15 | 0.00 | 2 | -2.51 | insufficient_sample |
| macd_dif_low_cross_signal | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_hist_turn_positive | TPEX | mild_bull | 7 | 7 | -0.69 | 42.86 | 7 | -0.73 | insufficient_sample |
| macd_hist_turn_positive | TPEX | strong_bull | 5 | 5 | 0.47 | 40.00 | 4 | 4.00 | insufficient_sample |
| macd_hist_turn_positive | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TWSE | mild_bull | 9 | 9 | 0.16 | 77.78 | 9 | 0.58 | insufficient_sample |
| macd_hist_turn_positive | TWSE | strong_bull | 9 | 9 | 2.11 | 66.67 | 8 | 2.29 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | high_risk | 5 | 5 | -0.25 | 80.00 | 5 | 1.87 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | mild_bull | 14 | 14 | 1.19 | 64.29 | 14 | 1.44 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | range_bound | 2 | 2 | 1.67 | 100.00 | 2 | 1.15 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | strong_bull | 3 | 3 | 3.22 | 66.67 | 3 | 6.18 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | high_risk | 1 | 1 | 3.32 | 100.00 | 1 | 6.32 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | mild_bull | 16 | 16 | 0.52 | 62.50 | 16 | 1.51 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | strong_bull | 5 | 5 | 1.24 | 60.00 | 5 | 1.13 | insufficient_sample |

## Time Effect Summary
- D+1 / D+3: 適合檢查短線轉折、假突破、KD 高低檔交叉。
- D+5 / D+10: 適合檢查 MACD 翻正、站回 MA20、期權極端後回歸。
- D+20 / D+40 / D+60: 適合檢查均線黃金交叉與中期趨勢事件。
- 樣本不足或 pending 時只能標示待回測假設，目前只作為觀察，不作為模型加權依據。

## Data Quality Notes
- missing_fields: TWSE_history_had_large_gap_keep_latest_continuous_segment
- pending_events: 103
- benchmark_available: TWSE/TPEX index history available=True
- regime_available: True
- breadth_available: True
- mature_counts: {'mature_d1_count': 1249, 'mature_d3_count': 1238, 'mature_d5_count': 1228, 'mature_d10_count': 1205, 'mature_d20_count': 1154, 'mature_d40_count': 1032, 'mature_d60_count': 998}

## Model Tuning Recommendation
- tuning_status = not_ready
- allowed_changes = reporting_only
- forbidden_changes = core_weight_change
- reason = market timing event samples still need mature D+10 / D+20 accumulation before formal weighting.

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## MARKET_SENTIMENT_CONTEXT

market_sentiment_context:
  taiwan_vix:
    latest: 35.23
    percentile_252d: 54.4304
    percentile_504d: 
    rank_label: middle_range
    context_label: normal_range
    index_interpretation: trend_supported_no_extreme_vix
  retail_mtx:
    latest_proxy: 15615.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 
    percentile_504d: 
    rank_label: insufficient_history
    context_label: insufficient_history
    index_interpretation: insufficient_history_observe_only
  combined:
    combined_sentiment_interpretation: insufficient_history_observe_only
    sentiment_warning_level: insufficient
    sample_status: insufficient_history
    data_quality_note: 資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。

ChatGPT-friendly summary:
- VIX context: normal_range / trend_supported_no_extreme_vix
- Retail MTX context: insufficient_history / insufficient_history_observe_only
- Combined: insufficient_history_observe_only (warning=insufficient)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
