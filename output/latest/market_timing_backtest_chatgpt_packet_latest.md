# MARKET TIMING BACKTEST CHATGPT PACKET

## Metadata
- generated_at: 2026-06-21 20:33:24 Asia/Taipei
- main_price_date: 20260618
- packet_source: market_timing_technical_backtest
- index_list: TPEX, TWSE
- data_range: 20241202 ~ 20260618
- source_files: data/market_index_history.csv, data/market_index_ohlc_history.csv, output/history/market_timing/market_breadth_history.csv, output/history/market_timing/market_technical_event_log.csv
- tuning_status: not_ready

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | market_regime | risk_level | trend_summary | momentum_summary | kd_summary | volatility_summary | volume_flow_summary | breadth_summary | futures_options_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPEX | 20260618 | 447.06 | 9.82 | 9.09 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 中性 | 擴散 | 期權資料已整合 |
| TWSE | 20260618 | 46465.2 | 7.68 | 12.32 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 健康 | 擴散 | 期權資料已整合 |

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
| 20260612 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 44169.04 | strong_bull | low_risk |
| 20260612 | TWSE | reclaim_ma20_after_breakdown | trend_ma | 44169.04 | strong_bull | low_risk |
| 20260615 | TPEX | reclaim_ma20_after_breakdown | trend_ma | 429.37 | mild_bull | low_risk |
| 20260615 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45396.99 | strong_bull | low_risk |
| 20260616 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 430.26 | strong_bull | low_risk |
| 20260616 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45809.19 | strong_bull | low_risk |
| 20260617 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 433.34 | strong_bull | low_risk |
| 20260617 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 45877.39 | strong_bull | low_risk |
| 20260618 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 447.06 | strong_bull | low_risk |
| 20260618 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 46465.2 | strong_bull | low_risk |

## Event Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 2 | 2 | -5.56 | 0.00 | 2 | -3.04 | 0.00 | 0 |  |  | D+1 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 83 | 83 | 0.54 | 60.24 | 83 | 1.50 | 62.65 | 75 | 4.23 | 78.67 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| kd_high_death_cross | TPEX | 18 | 18 | 1.14 | 77.78 | 18 | 2.90 | 77.78 | 17 | 4.53 | 82.35 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_high_death_cross | TWSE | 30 | 30 | 0.61 | 56.67 | 29 | 2.14 | 68.97 | 29 | 3.68 | 82.76 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| kd_low_golden_cross | TPEX | 6 | 6 | 2.06 | 83.33 | 6 | 2.75 | 83.33 | 6 | 4.26 | 83.33 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_low_golden_cross | TWSE | 4 | 4 | 1.15 | 75.00 | 4 | 0.54 | 75.00 | 4 | 0.86 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | 8 | 8 | -0.78 | 50.00 | 8 | 2.61 | 75.00 | 8 | 5.54 | 87.50 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | 15 | 15 | 1.06 | 66.67 | 15 | 2.21 | 80.00 | 15 | 4.65 | 80.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TPEX | 6 | 6 | 0.01 | 66.67 | 6 | 1.45 | 66.67 | 6 | 2.65 | 66.67 | D+20 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TWSE | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | 50.00 | 2 | 0.06 | 50.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TPEX | 16 | 16 | 0.24 | 56.25 | 16 | 1.05 | 50.00 | 15 | 4.05 | 60.00 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TWSE | 20 | 20 | 1.04 | 70.00 | 20 | 0.95 | 55.00 | 19 | 3.00 | 63.16 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_overbought_70 | TPEX | 74 | 74 | 1.15 | 60.81 | 74 | 2.77 | 72.97 | 74 | 5.07 | 82.43 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_overbought_70 | TWSE | 94 | 94 | 0.58 | 61.70 | 93 | 2.41 | 77.42 | 90 | 5.60 | 88.89 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_oversold_30 | TPEX | 13 | 13 | 1.86 | 76.92 | 13 | 1.92 | 61.54 | 13 | 2.39 | 69.23 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_oversold_30 | TWSE | 11 | 11 | 2.59 | 81.82 | 11 | 1.03 | 45.45 | 11 | -2.55 | 45.45 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | 152 | 152 | 0.99 | 62.50 | 152 | 2.31 | 71.05 | 150 | 3.34 | 74.67 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| adx_trend_plus_di_dominant | TWSE | 214 | 214 | 1.24 | 67.29 | 210 | 2.56 | 74.29 | 200 | 4.88 | 88.50 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| golden_cross_ma20_ma60 | TPEX | 3 | 3 | 1.45 | 66.67 | 3 | 0.52 | 33.33 | 3 | 3.27 | 66.67 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | 5 | 5 | -0.75 | 20.00 | 5 | -0.22 | 60.00 | 5 | -0.83 | 60.00 | D+10 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | 194 | 191 | 0.82 | 58.64 | 190 | 2.42 | 66.32 | 180 | 5.11 | 73.89 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | 238 | 233 | 1.01 | 65.24 | 230 | 2.14 | 70.87 | 220 | 4.42 | 81.82 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TPEX | 25 | 24 | 1.18 | 70.83 | 24 | 2.09 | 66.67 | 24 | 3.57 | 70.83 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TWSE | 23 | 22 | 0.81 | 63.64 | 22 | 1.65 | 63.64 | 22 | 4.81 | 77.27 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| bb_upper_breakout_long_upper_shadow | TPEX | 7 | 7 | 2.76 | 71.43 | 7 | 4.87 | 85.71 | 7 | 10.47 | 85.71 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | 10 | 10 | 0.65 | 70.00 | 10 | 0.98 | 60.00 | 8 | 3.56 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| high_volume_long_black_break_ma20_ema23 | TWSE | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | 100.00 | 2 | 14.71 | 100.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |

## Composite Signal Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | 2 | 2 | -5.56 | 0.00 | 2 | -3.04 | 0.00 | D+1 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | 83 | 83 | 0.54 | 60.24 | 83 | 1.50 | 62.65 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |

## Regime Sensitivity
| event_name | index_id | market_regime | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adx_trend_plus_di_dominant | TPEX | correction | 6 | 6 | 4.48 | 83.33 | 6 | 5.03 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | high_risk | 10 | 10 | 0.72 | 70.00 | 10 | 2.40 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | mild_bull | 35 | 35 | 0.59 | 57.14 | 35 | 1.10 | ok |
| adx_trend_plus_di_dominant | TPEX | range_bound | 19 | 19 | 0.51 | 47.37 | 19 | 0.89 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | strong_bull | 82 | 82 | 1.04 | 65.85 | 82 | 2.95 | ok |
| adx_trend_plus_di_dominant | TWSE | correction | 11 | 11 | 3.59 | 81.82 | 10 | 3.94 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | high_risk | 5 | 5 | 1.81 | 100.00 | 5 | 6.28 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | mild_bull | 58 | 58 | 0.81 | 60.34 | 57 | 2.13 | ok |
| adx_trend_plus_di_dominant | TWSE | range_bound | 6 | 6 | 3.83 | 100.00 | 6 | 3.66 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | strong_bull | 134 | 134 | 1.10 | 66.42 | 132 | 2.45 | ok |
| bb_upper_breakout_long_upper_shadow | TPEX | mild_bull | 4 | 4 | 0.35 | 50.00 | 4 | 2.52 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TPEX | strong_bull | 3 | 3 | 5.97 | 100.00 | 3 | 8.01 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | mild_bull | 1 | 1 | -3.61 | 0.00 | 1 | -1.49 | insufficient_sample |
| bb_upper_breakout_long_upper_shadow | TWSE | strong_bull | 9 | 9 | 1.13 | 77.78 | 9 | 1.26 | insufficient_sample |
| composite_bull_confirmation | TPEX | strong_bull | 2 | 2 | -5.56 | 0.00 | 2 | -3.04 | insufficient_sample |
| composite_bull_confirmation | TWSE | mild_bull | 21 | 21 | 0.94 | 61.90 | 21 | 1.59 | insufficient_sample |
| composite_bull_confirmation | TWSE | range_bound | 2 | 2 | 1.39 | 100.00 | 2 | 0.98 | insufficient_sample |
| composite_bull_confirmation | TWSE | strong_bull | 60 | 60 | 0.37 | 58.33 | 60 | 1.49 | ok |
| golden_cross_ma20_ma60 | TPEX | mild_bull | 1 | 1 | 1.45 | 100.00 | 1 | -0.68 | insufficient_sample |
| golden_cross_ma20_ma60 | TPEX | strong_bull | 2 | 2 | 1.46 | 50.00 | 2 | 1.13 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | correction | 1 | 1 | -0.24 | 0.00 | 1 | -1.67 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | mild_bull | 3 | 3 | -0.53 | 33.33 | 3 | -0.90 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | strong_bull | 1 | 1 | -1.90 | 0.00 | 1 | 3.28 | insufficient_sample |
| high_volume_long_black_break_ma20_ema23 | TWSE | high_risk | 2 | 2 | 9.75 | 100.00 | 2 | 7.36 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | mild_bull | 2 | 2 | 0.54 | 50.00 | 2 | 3.79 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | strong_bull | 6 | 6 | -1.22 | 50.00 | 6 | 2.22 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | strong_bull | 15 | 15 | 1.06 | 66.67 | 15 | 2.21 | insufficient_sample |
| kd_high_death_cross | TPEX | mild_bull | 5 | 5 | 0.08 | 60.00 | 5 | -0.16 | insufficient_sample |
| kd_high_death_cross | TPEX | range_bound | 2 | 2 | 1.66 | 100.00 | 2 | 0.42 | insufficient_sample |
| kd_high_death_cross | TPEX | strong_bull | 11 | 11 | 1.53 | 81.82 | 11 | 4.74 | insufficient_sample |
| kd_high_death_cross | TWSE | correction | 1 | 1 | -0.46 | 0.00 | 1 | -0.02 | insufficient_sample |
| kd_high_death_cross | TWSE | mild_bull | 9 | 9 | -0.21 | 44.44 | 9 | 0.10 | insufficient_sample |
| kd_high_death_cross | TWSE | range_bound | 1 | 1 | 6.02 | 100.00 | 1 | 6.12 | insufficient_sample |
| kd_high_death_cross | TWSE | strong_bull | 19 | 19 | 0.77 | 63.16 | 18 | 3.07 | insufficient_sample |
| kd_low_golden_cross | TPEX | correction | 2 | 2 | 2.20 | 100.00 | 2 | 0.76 | insufficient_sample |
| kd_low_golden_cross | TPEX | high_risk | 4 | 4 | 2.00 | 75.00 | 4 | 3.75 | insufficient_sample |
| kd_low_golden_cross | TWSE | correction | 2 | 2 | 1.45 | 100.00 | 2 | 3.03 | insufficient_sample |
| kd_low_golden_cross | TWSE | high_risk | 2 | 2 | 0.86 | 50.00 | 2 | -1.96 | insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | mild_bull | 78 | 78 | 0.42 | 51.28 | 78 | 1.77 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | strong_bull | 116 | 113 | 1.09 | 63.72 | 112 | 2.87 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | mild_bull | 87 | 87 | 0.81 | 62.07 | 86 | 1.56 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | strong_bull | 151 | 146 | 1.13 | 67.12 | 144 | 2.49 | ok |
| macd_dif_low_cross_signal | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_dif_low_cross_signal | TPEX | mild_bull | 2 | 2 | -3.15 | 0.00 | 2 | -2.51 | insufficient_sample |
| macd_dif_low_cross_signal | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_hist_turn_positive | TPEX | mild_bull | 7 | 7 | -0.69 | 42.86 | 7 | -0.73 | insufficient_sample |
| macd_hist_turn_positive | TPEX | strong_bull | 5 | 5 | 0.47 | 40.00 | 5 | 1.65 | insufficient_sample |
| macd_hist_turn_positive | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TWSE | mild_bull | 9 | 9 | 0.16 | 77.78 | 9 | 0.58 | insufficient_sample |
| macd_hist_turn_positive | TWSE | strong_bull | 9 | 9 | 2.11 | 66.67 | 9 | 2.34 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | high_risk | 5 | 5 | -0.25 | 80.00 | 5 | 1.87 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | mild_bull | 15 | 14 | 1.19 | 64.29 | 14 | 1.44 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | range_bound | 2 | 2 | 1.67 | 100.00 | 2 | 1.15 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | strong_bull | 3 | 3 | 3.22 | 66.67 | 3 | 6.18 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | high_risk | 1 | 1 | 3.32 | 100.00 | 1 | 6.32 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | mild_bull | 16 | 16 | 0.52 | 62.50 | 16 | 1.51 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | strong_bull | 6 | 5 | 1.24 | 60.00 | 5 | 1.13 | insufficient_sample |
| rsi14_overbought_70 | TPEX | high_risk | 1 | 1 | -1.33 | 0.00 | 1 | 4.03 | insufficient_sample |
| rsi14_overbought_70 | TPEX | mild_bull | 12 | 12 | 0.16 | 50.00 | 12 | 2.95 | insufficient_sample |

## Time Effect Summary
- D+1 / D+3: 適合檢查短線轉折、假突破、KD 高低檔交叉。
- D+5 / D+10: 適合檢查 MACD 翻正、站回 MA20、期權極端後回歸。
- D+20 / D+40 / D+60: 適合檢查均線黃金交叉與中期趨勢事件。
- 樣本不足或 pending 時只能標示待回測假設，目前只作為觀察，不作為模型加權依據。

## Data Quality Notes
- missing_fields: TWSE_history_had_large_gap_keep_latest_continuous_segment
- pending_events: 70
- benchmark_available: TWSE/TPEX index history available=True
- regime_available: True
- breadth_available: True
- mature_counts: {'mature_d1_count': 1273, 'mature_d3_count': 1269, 'mature_d5_count': 1265, 'mature_d10_count': 1255, 'mature_d20_count': 1205, 'mature_d40_count': 1086, 'mature_d60_count': 1018}

## Model Tuning Recommendation
- tuning_status = not_ready
- allowed_changes = reporting_only
- forbidden_changes = core_weight_change
- reason = market timing event samples still need mature D+10 / D+20 accumulation before formal weighting.
