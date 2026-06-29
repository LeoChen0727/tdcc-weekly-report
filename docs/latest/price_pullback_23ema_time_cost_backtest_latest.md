# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-06-29 23:23:26 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 298431 | 270127 | 41.03 | 39.53 | 0.11 | 19.33 | 6.45 | 7.15 | 9.34 |
| volume_red_k_vol1.2 | 30382 | 26748 | 39.44 | 40.37 | 0.12 | 20.06 | 6.29 | 6.96 | 9.31 |
| solid_volume_red_k_vol1.2 | 15913 | 13938 | 38.87 | 39.47 | 0.14 | 21.52 | 6.34 | 6.96 | 9.52 |
| solid_volume_red_k_vol1.5 | 10239 | 8891 | 38.36 | 40.7 | 0.11 | 20.82 | 6.2 | 6.78 | 9.3 |
