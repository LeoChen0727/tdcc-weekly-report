# Market Timing Composite Signal Backtest

- Composite signals combine trend, momentum, volatility, volume, breadth, and derivatives context.
- Current stage is reporting/backtesting only; no core model weights are changed here.

| event_name | index_id | event_group | sample_count | mature_d5_count | avg_ret_d5 | win_rate_d5 | avg_mfe_d5 | avg_mae_d5 | mature_d10_count | avg_ret_d10 | win_rate_d10 | mature_d20_count | avg_ret_d20 | win_rate_d20 | best_horizon | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composite_bull_confirmation | TPEX | composite_signal | 2 | 0 |  |  |  |  | 0 |  |  | 0 |  |  | D+1 | D+1:insufficient_sample;D+3:pending_only;D+5:pending_only;D+10:pending_only;D+20:pending_only;D+40:pending_only;D+60:pending_only |
| composite_bull_confirmation | TWSE | composite_signal | 82 | 77 | 0.75 | 62.34 | 2.30 | -1.51 | 75 | 1.67 | 64.00 | 73 | 4.11 | 78.08 | D+60 | D+1:ok;D+3:ok;D+5:ok;D+10:ok;D+20:ok;D+40:ok;D+60:ok |
