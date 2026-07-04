# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-07-05 02:31:38 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 304517 | 275314 | 41.09 | 39.54 | 0.12 | 19.26 | 6.41 | 7.11 | 9.3 |
| volume_red_k_vol1.2 | 30879 | 27682 | 39.67 | 40.11 | 0.12 | 20.1 | 6.23 | 6.95 | 9.28 |
| solid_volume_red_k_vol1.2 | 16206 | 14544 | 39.26 | 39.14 | 0.13 | 21.47 | 6.26 | 6.97 | 9.49 |
| solid_volume_red_k_vol1.5 | 10435 | 9285 | 38.73 | 40.38 | 0.11 | 20.79 | 6.14 | 6.81 | 9.29 |
| prior_ext20_ema10_runup20_pullback5 | 60754 | 50314 | 48.33 | 48.72 | 0.38 | 2.57 | 4.05 | 4.63 | 4.74 |
| prior_ext30_ema12_runup25_pullback8 | 66466 | 56438 | 47.44 | 48.36 | 0.35 | 3.85 | 4.27 | 4.88 | 5.16 |
| prior_ext60_ema15_runup35_pullback10 | 92813 | 82590 | 45.72 | 45.43 | 0.28 | 8.57 | 5.15 | 5.6 | 6.62 |
