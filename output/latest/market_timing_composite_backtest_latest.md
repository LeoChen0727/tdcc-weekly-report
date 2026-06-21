# Market Timing Composite Signal Backtest

- Composite signals combine trend, momentum, volatility, volume, breadth, and derivatives context.
- Current stage is reporting/backtesting only; no core model weights are changed here.

| event_name | index_id | event_group | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | avg_mfe_d5 | avg_mae_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | composite_signal | 2 | 2 | -5.56 | 0.00 | 1.55 | -10.86 | 2 | -3.04 | 0.00 | 0 |  |  | D+1 | D+1:insufficient_sample;D+3:insufficient_sample;D+5:insufficient_sample;D+10:insufficient_sample;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | composite_signal | 83 | 83 | 0.54 | 60.24 | 2.31 | -1.78 | 83 | 1.50 | 62.65 | 75 | 4.23 | 78.67 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
