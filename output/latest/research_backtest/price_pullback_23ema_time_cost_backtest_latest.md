# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-06-29 21:37:12 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 296964 | 268688 | 40.91 | 39.62 | 0.11 | 19.37 | 6.47 | 7.16 | 9.36 |
| volume_red_k_vol1.2 | 30326 | 26592 | 39.32 | 40.46 | 0.12 | 20.1 | 6.31 | 6.96 | 9.32 |
| solid_volume_red_k_vol1.2 | 15893 | 13878 | 38.8 | 39.52 | 0.13 | 21.55 | 6.35 | 6.97 | 9.53 |
| solid_volume_red_k_vol1.5 | 10223 | 8842 | 38.27 | 40.76 | 0.11 | 20.86 | 6.22 | 6.78 | 9.32 |
