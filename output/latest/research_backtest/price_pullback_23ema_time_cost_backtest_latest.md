# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-07-10 17:43:21 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 310808 | 280902 | 41.23 | 39.5 | 0.13 | 19.14 | 6.38 | 7.07 | 9.25 |
| volume_red_k_vol1.2 | 31433 | 28661 | 39.8 | 40.05 | 0.13 | 20.02 | 6.21 | 6.93 | 9.26 |
| solid_volume_red_k_vol1.2 | 16502 | 15124 | 39.41 | 39.08 | 0.14 | 21.37 | 6.23 | 6.95 | 9.45 |
| solid_volume_red_k_vol1.5 | 10622 | 9696 | 38.81 | 40.37 | 0.11 | 20.71 | 6.13 | 6.79 | 9.26 |
| prior_ext20_ema10_runup20_pullback5 | 62813 | 52177 | 48.4 | 48.68 | 0.41 | 2.5 | 4.0 | 4.57 | 4.67 |
| prior_ext30_ema12_runup25_pullback8 | 68881 | 58375 | 47.49 | 48.35 | 0.38 | 3.78 | 4.22 | 4.81 | 5.1 |
| prior_ext60_ema15_runup35_pullback10 | 95357 | 84579 | 45.8 | 45.5 | 0.3 | 8.4 | 5.1 | 5.54 | 6.55 |
