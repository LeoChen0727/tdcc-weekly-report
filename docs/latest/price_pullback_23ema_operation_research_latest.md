# Price Pullback 23EMA Operation Research

- generated_at: `2026-07-02 14:05:48 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 301487 | 288246 | 17.08 | 55.82 | 27.1 | 0.0 | 0.68 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 301487 | 274107 | 23.41 | 43.26 | 33.33 | 0.0 | 1.62 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 301487 | 274107 | 32.45 | 19.27 | 29.64 | 18.64 | 1.62 | 9.76 | 51.09 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 301487 | 274107 | 24.39 | 27.32 | 36.22 | 12.07 | 1.62 | 9.76 | 51.09 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 30593 | 29450 | 15.99 | 55.22 | 28.79 | 0.0 | 0.38 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 30593 | 27426 | 22.61 | 42.81 | 34.57 | 0.0 | 1.25 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 30593 | 27426 | 31.69 | 20.08 | 31.04 | 17.2 | 1.25 | 9.25 | 48.89 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 30593 | 27426 | 23.91 | 27.85 | 37.08 | 11.16 | 1.25 | 9.25 | 48.89 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 16032 | 15462 | 15.79 | 56.29 | 27.92 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 16032 | 14381 | 21.99 | 44.05 | 33.95 | 0.0 | 1.12 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 16032 | 14381 | 31.66 | 21.44 | 30.73 | 16.17 | 1.12 | 8.92 | 47.83 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 16032 | 14381 | 23.67 | 29.43 | 36.83 | 10.08 | 1.12 | 8.92 | 47.83 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10317 | 9935 | 15.61 | 55.14 | 29.25 | 0.0 | 0.26 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10317 | 9173 | 21.96 | 42.92 | 35.12 | 0.0 | 0.97 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10317 | 9173 | 30.96 | 20.73 | 31.72 | 16.58 | 0.97 | 8.96 | 47.54 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10317 | 9173 | 23.3 | 28.4 | 37.97 | 10.33 | 0.97 | 8.96 | 47.54 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d10_close_target5_loss3 | 59634 | 54834 | 27.08 | 36.61 | 36.31 | 0.0 | 1.77 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_close_target5_loss3 | 59634 | 49942 | 33.18 | 27.42 | 39.4 | 0.0 | 3.85 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target5_low_stop5_order_unresolved | 59634 | 49942 | 30.34 | 2.58 | 28.36 | 38.73 | 3.85 | 15.89 | 69.06 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target8_low_stop5_order_unresolved | 59634 | 49942 | 27.39 | 5.53 | 38.57 | 28.51 | 3.85 | 15.89 | 69.06 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d10_close_target5_loss3 | 65409 | 60941 | 25.39 | 39.39 | 35.22 | 0.0 | 1.51 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_close_target5_loss3 | 65409 | 56082 | 30.68 | 29.94 | 39.37 | 0.0 | 3.15 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target5_low_stop5_order_unresolved | 65409 | 56082 | 30.45 | 3.87 | 29.27 | 36.41 | 3.15 | 14.73 | 66.86 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target8_low_stop5_order_unresolved | 65409 | 56082 | 26.8 | 7.52 | 39.45 | 26.23 | 3.15 | 14.73 | 66.86 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d10_close_target5_loss3 | 91764 | 87134 | 21.78 | 45.88 | 32.34 | 0.0 | 1.09 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_close_target5_loss3 | 91764 | 82296 | 28.34 | 34.75 | 36.91 | 0.0 | 2.56 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target5_low_stop5_order_unresolved | 91764 | 82296 | 32.14 | 8.62 | 29.63 | 29.6 | 2.56 | 12.79 | 61.74 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target8_low_stop5_order_unresolved | 91764 | 82296 | 26.5 | 14.26 | 38.66 | 20.57 | 2.56 | 12.79 | 61.74 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
