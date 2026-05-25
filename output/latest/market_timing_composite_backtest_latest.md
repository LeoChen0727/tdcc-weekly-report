# Market Timing Composite Signal Backtest

- Composite signals combine trend, momentum, volatility, volume, breadth, and derivatives context.
- Current stage is reporting/backtesting only; no core model weights are changed here.

| event_name | index_id | event_group | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | avg_mfe_d5 | avg_mae_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | composite_signal | 5 | 5 | 3.16 | 100.00 | 5.10 | -1.40 | 5 | -0.20 | 40.00 | 0 |  |  | D+5 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | composite_signal | 75 | 75 | 0.64 | 61.33 | 2.21 | -1.51 | 75 | 1.67 | 64.00 | 71 | 3.87 | 77.46 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
