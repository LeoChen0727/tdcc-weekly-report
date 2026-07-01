# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-07-01 13:13:02 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 299969 | 271499 | 41.12 | 39.47 | 0.11 | 19.3 | 6.43 | 7.15 | 9.33 |
| volume_red_k_vol1.2 | 30465 | 26974 | 39.58 | 40.25 | 0.12 | 20.05 | 6.27 | 6.96 | 9.3 |
| solid_volume_red_k_vol1.2 | 15962 | 14070 | 39.07 | 39.32 | 0.14 | 21.48 | 6.31 | 6.97 | 9.5 |
| solid_volume_red_k_vol1.5 | 10276 | 8971 | 38.57 | 40.54 | 0.11 | 20.78 | 6.17 | 6.78 | 9.29 |
| prior_ext20_ema10_runup20_pullback5 | 59068 | 49225 | 48.67 | 48.36 | 0.37 | 2.6 | 4.07 | 4.68 | 4.78 |
| prior_ext30_ema12_runup25_pullback8 | 64894 | 55332 | 47.73 | 48.03 | 0.33 | 3.91 | 4.3 | 4.93 | 5.21 |
| prior_ext60_ema15_runup35_pullback10 | 91226 | 81559 | 45.84 | 45.19 | 0.27 | 8.69 | 5.18 | 5.64 | 6.67 |
