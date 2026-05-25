# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-05-25 22:33:15 Asia/Taipei
- main_price_date: 20260522
- index_list: TPEX, TWSE
- data_range: 20241202 ~ 20260522
- source_files: data/market_index_history.csv, output/history/market_timing/market_breadth_history.csv, output/history/market_timing/market_technical_event_log.csv
- tuning_status: not_ready

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | market_regime | risk_level | trend_summary | momentum_summary | kd_summary | volatility_summary | volume_flow_summary | breadth_summary | futures_options_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPEX | 20260522 | 423.25 | 2.94 | 11.00 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 中性 | 擴散 | 期權資料已整合 |
| TWSE | 20260522 | 42267.97 | 2.66 | 12.07 | strong_bull | low_risk | 多頭 | 增強 | 中性 | 正常 | 中性 | 擴散 | 期權資料已整合 |

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
| 20260518 | TPEX | adx_trend_plus_di_dominant | trend_ma | 409.63 | strong_bull | low_risk |
| 20260518 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 409.63 | strong_bull | low_risk |
| 20260518 | TWSE | adx_trend_plus_di_dominant | trend_ma | 40891.82 | strong_bull | low_risk |
| 20260518 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 40891.82 | strong_bull | low_risk |
| 20260519 | TPEX | adx_trend_plus_di_dominant | trend_ma | 398.18 | correction | normal_risk |
| 20260519 | TWSE | adx_trend_plus_di_dominant | trend_ma | 40175.56 | correction | normal_risk |
| 20260520 | TPEX | adx_trend_plus_di_dominant | trend_ma | 396.42 | correction | normal_risk |
| 20260520 | TWSE | adx_trend_plus_di_dominant | trend_ma | 40020.82 | correction | normal_risk |
| 20260521 | TWSE | reclaim_ma20_after_breakdown | trend_ma | 41368.21 | strong_bull | low_risk |
| 20260521 | TPEX | adx_trend_plus_di_dominant | trend_ma | 409.8 | mild_bull | low_risk |
| 20260521 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 409.8 | mild_bull | low_risk |
| 20260521 | TPEX | reclaim_ma20_after_breakdown | trend_ma | 409.8 | mild_bull | low_risk |
| 20260521 | TWSE | adx_trend_plus_di_dominant | trend_ma | 41368.21 | strong_bull | low_risk |
| 20260521 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 41368.21 | strong_bull | low_risk |
| 20260522 | TPEX | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 423.25 | strong_bull | low_risk |
| 20260522 | TWSE | adx_trend_plus_di_dominant | trend_ma | 42267.97 | strong_bull | low_risk |
| 20260522 | TPEX | adx_trend_plus_di_dominant | trend_ma | 423.25 | strong_bull | low_risk |
| 20260522 | TWSE | ma20_slope_up_price_above_ma20_ma60 | trend_ma | 42267.97 | strong_bull | low_risk |

## Event Backtest Summary
| event_name | index_id | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| kd_high_death_cross | TPEX | 17 | 17 | 1.49 | 76.47 | 17 | 2.37 | 70.59 | 17 | 3.69 | 64.71 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_high_death_cross | TWSE | 26 | 26 | 1.00 | 61.54 | 25 | 1.78 | 72.00 | 23 | 2.73 | 73.91 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| kd_low_golden_cross | TPEX | 8 | 8 | 1.05 | 62.50 | 8 | 1.10 | 62.50 | 8 | 1.39 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| kd_low_golden_cross | TWSE | 4 | 4 | 1.15 | 75.00 | 4 | 0.54 | 75.00 | 4 | 0.86 | 75.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | 11 | 11 | 0.24 | 63.64 | 9 | 2.01 | 55.56 | 8 | 5.35 | 87.50 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | 11 | 11 | 1.53 | 72.73 | 11 | 2.47 | 72.73 | 8 | 4.80 | 87.50 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TPEX | 6 | 6 | 0.01 | 66.67 | 6 | 1.45 | 66.67 | 6 | 2.65 | 66.67 | D+20 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_dif_low_cross_signal | TWSE | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | 50.00 | 2 | 0.06 | 50.00 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TPEX | 15 | 15 | 0.16 | 53.33 | 15 | 1.64 | 53.33 | 15 | 4.05 | 60.00 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| macd_hist_turn_positive | TWSE | 19 | 19 | 0.85 | 68.42 | 19 | 0.85 | 52.63 | 19 | 3.00 | 63.16 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_overbought_70 | TPEX | 74 | 74 | 1.15 | 60.81 | 71 | 2.77 | 71.83 | 61 | 4.40 | 83.61 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_overbought_70 | TWSE | 90 | 90 | 0.79 | 64.44 | 86 | 2.36 | 76.74 | 76 | 4.89 | 86.84 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| rsi14_oversold_30 | TPEX | 13 | 13 | 1.86 | 76.92 | 13 | 1.92 | 61.54 | 13 | 2.39 | 69.23 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| rsi14_oversold_30 | TWSE | 11 | 11 | 2.59 | 81.82 | 11 | 1.03 | 45.45 | 11 | -2.55 | 45.45 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | 146 | 141 | 0.96 | 60.99 | 136 | 2.28 | 69.85 | 126 | 3.03 | 77.78 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| adx_trend_plus_di_dominant | TWSE | 187 | 182 | 1.24 | 68.68 | 177 | 2.38 | 73.45 | 167 | 4.17 | 86.23 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| golden_cross_ma20_ma60 | TPEX | 3 | 3 | 1.45 | 66.67 | 3 | 0.52 | 33.33 | 3 | 3.27 | 66.67 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | 5 | 5 | -0.75 | 20.00 | 5 | -0.22 | 60.00 | 5 | -0.83 | 60.00 | D+10 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:insufficient_sample;D+60:insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | 181 | 178 | 0.94 | 58.99 | 173 | 2.64 | 67.63 | 163 | 4.91 | 73.62 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | 221 | 218 | 0.98 | 65.14 | 213 | 2.05 | 70.89 | 203 | 3.99 | 80.30 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TPEX | 24 | 23 | 0.99 | 69.57 | 23 | 1.86 | 65.22 | 23 | 3.33 | 69.57 | D+60 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:ok |
| reclaim_ma20_after_breakdown | TWSE | 22 | 21 | 0.59 | 61.90 | 21 | 1.23 | 61.90 | 21 | 4.45 | 76.19 | D+40 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:insufficient_sample;D+40:ok;D+60:insufficient_sample |

## Composite Signal Backtest Summary
目前沒有可用資料。

## Regime Sensitivity
| event_name | index_id | market_regime | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | mature_d10_count | avg_ret_d10 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adx_trend_plus_di_dominant | TPEX | correction | 7 | 5 | 0.45 | 40.00 | 5 | 0.52 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | high_risk | 8 | 8 | 0.98 | 75.00 | 8 | 3.25 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | mild_bull | 26 | 25 | 0.33 | 48.00 | 25 | 0.87 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | range_bound | 18 | 18 | 0.45 | 44.44 | 18 | 0.71 | insufficient_sample |
| adx_trend_plus_di_dominant | TPEX | strong_bull | 87 | 85 | 1.28 | 68.24 | 80 | 3.08 | ok |
| adx_trend_plus_di_dominant | TWSE | correction | 10 | 8 | 1.82 | 75.00 | 8 | 0.85 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | high_risk | 6 | 6 | 2.06 | 100.00 | 6 | 6.29 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | mild_bull | 44 | 44 | 1.19 | 65.91 | 44 | 2.24 | ok |
| adx_trend_plus_di_dominant | TWSE | range_bound | 6 | 6 | 3.83 | 100.00 | 6 | 3.66 | insufficient_sample |
| adx_trend_plus_di_dominant | TWSE | strong_bull | 121 | 118 | 1.05 | 66.10 | 113 | 2.27 | ok |
| golden_cross_ma20_ma60 | TPEX | mild_bull | 1 | 1 | 1.45 | 100.00 | 1 | -0.68 | insufficient_sample |
| golden_cross_ma20_ma60 | TPEX | strong_bull | 2 | 2 | 1.46 | 50.00 | 2 | 1.13 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | correction | 1 | 1 | -0.24 | 0.00 | 1 | -1.67 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | mild_bull | 3 | 3 | -0.53 | 33.33 | 3 | -0.90 | insufficient_sample |
| golden_cross_ma20_ma60 | TWSE | strong_bull | 1 | 1 | -1.90 | 0.00 | 1 | 3.28 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TPEX | strong_bull | 11 | 11 | 0.24 | 63.64 | 9 | 2.01 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | mild_bull | 1 | 1 | -3.08 | 0.00 | 1 | -0.10 | insufficient_sample |
| index_new_high_but_ma20_breadth_down | TWSE | strong_bull | 10 | 10 | 1.99 | 80.00 | 10 | 2.73 | insufficient_sample |
| kd_high_death_cross | TPEX | correction | 1 | 1 | 0.72 | 100.00 | 1 | 1.08 | insufficient_sample |
| kd_high_death_cross | TPEX | mild_bull | 4 | 4 | -0.37 | 50.00 | 4 | -0.56 | insufficient_sample |
| kd_high_death_cross | TPEX | range_bound | 2 | 2 | 2.84 | 100.00 | 2 | 1.43 | insufficient_sample |
| kd_high_death_cross | TPEX | strong_bull | 10 | 10 | 2.04 | 80.00 | 10 | 3.87 | insufficient_sample |
| kd_high_death_cross | TWSE | mild_bull | 9 | 9 | 0.27 | 55.56 | 9 | 0.28 | insufficient_sample |
| kd_high_death_cross | TWSE | range_bound | 1 | 1 | 6.02 | 100.00 | 1 | 6.12 | insufficient_sample |
| kd_high_death_cross | TWSE | strong_bull | 16 | 16 | 1.09 | 62.50 | 15 | 2.38 | insufficient_sample |
| kd_low_golden_cross | TPEX | correction | 3 | 3 | 0.37 | 66.67 | 3 | 0.24 | insufficient_sample |
| kd_low_golden_cross | TPEX | high_risk | 5 | 5 | 1.46 | 60.00 | 5 | 1.61 | insufficient_sample |
| kd_low_golden_cross | TWSE | correction | 2 | 2 | 1.45 | 100.00 | 2 | 3.03 | insufficient_sample |
| kd_low_golden_cross | TWSE | high_risk | 2 | 2 | 0.86 | 50.00 | 2 | -1.96 | insufficient_sample |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | mild_bull | 78 | 77 | 0.36 | 50.65 | 77 | 1.69 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TPEX | strong_bull | 103 | 101 | 1.38 | 65.35 | 96 | 3.39 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | mild_bull | 86 | 86 | 0.77 | 61.63 | 86 | 1.56 | ok |
| ma20_slope_up_price_above_ma20_ma60 | TWSE | strong_bull | 135 | 132 | 1.11 | 67.42 | 127 | 2.39 | ok |
| macd_dif_low_cross_signal | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_dif_low_cross_signal | TPEX | mild_bull | 2 | 2 | -3.15 | 0.00 | 2 | -2.51 | insufficient_sample |
| macd_dif_low_cross_signal | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TPEX | high_risk | 4 | 4 | 1.59 | 100.00 | 4 | 3.42 | insufficient_sample |
| macd_hist_turn_positive | TPEX | mild_bull | 7 | 7 | -0.69 | 42.86 | 7 | -0.73 | insufficient_sample |
| macd_hist_turn_positive | TPEX | strong_bull | 4 | 4 | 0.21 | 25.00 | 4 | 4.00 | insufficient_sample |
| macd_hist_turn_positive | TWSE | high_risk | 2 | 2 | 0.20 | 50.00 | 2 | -3.64 | insufficient_sample |
| macd_hist_turn_positive | TWSE | mild_bull | 9 | 9 | 0.16 | 77.78 | 9 | 0.58 | insufficient_sample |
| macd_hist_turn_positive | TWSE | strong_bull | 8 | 8 | 1.79 | 62.50 | 8 | 2.29 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | high_risk | 5 | 5 | -0.25 | 80.00 | 5 | 1.87 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | mild_bull | 14 | 13 | 0.85 | 61.54 | 13 | 0.98 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | range_bound | 2 | 2 | 1.67 | 100.00 | 2 | 1.15 | insufficient_sample |
| reclaim_ma20_after_breakdown | TPEX | strong_bull | 3 | 3 | 3.22 | 66.67 | 3 | 6.18 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | high_risk | 1 | 1 | 3.32 | 100.00 | 1 | 6.32 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | mild_bull | 16 | 16 | 0.52 | 62.50 | 16 | 1.51 | insufficient_sample |
| reclaim_ma20_after_breakdown | TWSE | strong_bull | 5 | 4 | 0.18 | 50.00 | 4 | -1.19 | insufficient_sample |
| rsi14_overbought_70 | TPEX | high_risk | 1 | 1 | -1.33 | 0.00 | 1 | 4.03 | insufficient_sample |
| rsi14_overbought_70 | TPEX | mild_bull | 12 | 12 | 0.16 | 50.00 | 12 | 2.95 | insufficient_sample |
| rsi14_overbought_70 | TPEX | range_bound | 5 | 5 | -0.34 | 20.00 | 5 | -1.53 | insufficient_sample |
| rsi14_overbought_70 | TPEX | strong_bull | 56 | 56 | 1.54 | 67.86 | 53 | 3.12 | ok |
| rsi14_overbought_70 | TWSE | high_risk | 1 | 1 | 1.55 | 100.00 | 1 | 7.66 | insufficient_sample |
| rsi14_overbought_70 | TWSE | mild_bull | 10 | 10 | 0.72 | 70.00 | 10 | 2.29 | insufficient_sample |
| rsi14_overbought_70 | TWSE | range_bound | 3 | 3 | 2.41 | 100.00 | 3 | 1.83 | insufficient_sample |
| rsi14_overbought_70 | TWSE | strong_bull | 76 | 76 | 0.73 | 61.84 | 72 | 2.32 | ok |
| rsi14_oversold_30 | TPEX | high_risk | 13 | 13 | 1.86 | 76.92 | 13 | 1.92 | insufficient_sample |
| rsi14_oversold_30 | TWSE | correction | 2 | 2 | 1.85 | 100.00 | 2 | 3.79 | insufficient_sample |
| rsi14_oversold_30 | TWSE | high_risk | 9 | 9 | 2.75 | 77.78 | 9 | 0.42 | insufficient_sample |

## Time Effect Summary
- D+1 / D+3: 適合檢查短線轉折、假突破、KD 高低檔交叉。
- D+5 / D+10: 適合檢查 MACD 翻正、站回 MA20、期權極端後回歸。
- D+20 / D+40 / D+60: 適合檢查均線黃金交叉與中期趨勢事件。
- 樣本不足時只能標示待回測假設，目前只作為觀察，不作為模型加權依據。

## Data Quality Notes
- missing_fields: TWSE_history_had_large_gap_keep_latest_continuous_segment, high_unavailable_filled_with_close, low_unavailable_filled_with_close, open_unavailable_filled_with_close
- pending_events: 114
- benchmark_available: TWSE/TPEX index history available=True
- regime_available: True
- breadth_available: True
- mature_counts: {'mature_d1_count': 1092, 'mature_d3_count': 1084, 'mature_d5_count': 1078, 'mature_d10_count': 1048, 'mature_d20_count': 982, 'mature_d40_count': 917, 'mature_d60_count': 864}

## Model Tuning Recommendation
- tuning_status = not_ready
- allowed_changes = reporting_only
- forbidden_changes = core_weight_change
- reason = market timing event samples still need mature D+10 / D+20 accumulation before formal weighting.
