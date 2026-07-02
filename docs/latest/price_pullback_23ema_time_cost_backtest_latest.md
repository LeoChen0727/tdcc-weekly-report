# Price Pullback 23EMA Time Cost Backtest

- generated_at: `2026-07-02 14:05:48 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open`
- target_rule: first intraday high >= `+5%` through `D+20`
- stop_rule: first intraday low <= `-5%` through `D+20`
- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved
- scope: advisory time-cost research only; this does not approve daily production use

| entry_filter_id | selected_stock_days | mature_count | target_before_stop_rate_pct | stop_before_target_rate_pct | same_day_target_stop_rate_pct | no_decision_after_20d_rate_pct | avg_holding_days_if_win | avg_holding_days_if_loss | avg_first_decision_or_20d_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | 301487 | 272784 | 41.15 | 39.45 | 0.12 | 19.28 | 6.42 | 7.14 | 9.32 |
| volume_red_k_vol1.2 | 30593 | 27289 | 39.74 | 40.06 | 0.12 | 20.08 | 6.24 | 6.97 | 9.29 |
| solid_volume_red_k_vol1.2 | 16032 | 14280 | 39.32 | 39.08 | 0.13 | 21.47 | 6.28 | 6.98 | 9.5 |
| solid_volume_red_k_vol1.5 | 10317 | 9107 | 38.73 | 40.38 | 0.11 | 20.79 | 6.16 | 6.81 | 9.3 |
| prior_ext20_ema10_runup20_pullback5 | 59634 | 49559 | 48.6 | 48.44 | 0.37 | 2.59 | 4.06 | 4.67 | 4.76 |
| prior_ext30_ema12_runup25_pullback8 | 65409 | 55679 | 47.68 | 48.09 | 0.34 | 3.89 | 4.28 | 4.91 | 5.19 |
| prior_ext60_ema15_runup35_pullback10 | 91764 | 81897 | 45.83 | 45.24 | 0.27 | 8.66 | 5.17 | 5.63 | 6.66 |
