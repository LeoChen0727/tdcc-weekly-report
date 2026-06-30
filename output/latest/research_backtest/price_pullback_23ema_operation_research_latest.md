# Price Pullback 23EMA Operation Research

- generated_at: `2026-06-30 18:04:12 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 299969 | 286853 | 17.09 | 55.81 | 27.1 | 0.0 | 0.68 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 299969 | 272800 | 23.43 | 43.25 | 33.32 | 0.0 | 1.62 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 299969 | 272800 | 32.46 | 19.28 | 29.65 | 18.6 | 1.62 | 9.76 | 51.07 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 299969 | 272800 | 24.41 | 27.33 | 36.21 | 12.04 | 1.62 | 9.76 | 51.07 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 30465 | 29362 | 15.99 | 55.24 | 28.78 | 0.0 | 0.38 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 30465 | 27294 | 22.63 | 42.78 | 34.59 | 0.0 | 1.24 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 30465 | 27294 | 31.68 | 20.08 | 31.05 | 17.2 | 1.24 | 9.25 | 48.88 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 30465 | 27294 | 23.91 | 27.84 | 37.09 | 11.16 | 1.24 | 9.25 | 48.88 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 15962 | 15419 | 15.79 | 56.29 | 27.91 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 15962 | 14284 | 21.98 | 44.01 | 34.0 | 0.0 | 1.1 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 15962 | 14284 | 31.62 | 21.47 | 30.75 | 16.16 | 1.1 | 8.91 | 47.77 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 15962 | 14284 | 23.65 | 29.44 | 36.84 | 10.07 | 1.1 | 8.91 | 47.77 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10276 | 9906 | 15.61 | 55.13 | 29.27 | 0.0 | 0.26 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10276 | 9108 | 21.98 | 42.85 | 35.17 | 0.0 | 0.96 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10276 | 9108 | 30.91 | 20.78 | 31.73 | 16.58 | 0.96 | 8.96 | 47.49 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10276 | 9108 | 23.28 | 28.41 | 37.96 | 10.35 | 0.96 | 8.96 | 47.49 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d10_close_target5_loss3 | 59068 | 54356 | 27.1 | 36.58 | 36.32 | 0.0 | 1.77 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_close_target5_loss3 | 59068 | 49561 | 33.21 | 27.46 | 39.32 | 0.0 | 3.87 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target5_low_stop5_order_unresolved | 59068 | 49561 | 30.42 | 2.59 | 28.32 | 38.66 | 3.87 | 15.9 | 69.08 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target8_low_stop5_order_unresolved | 59068 | 49561 | 27.46 | 5.55 | 38.5 | 28.49 | 3.87 | 15.9 | 69.08 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d10_close_target5_loss3 | 64894 | 60482 | 25.36 | 39.41 | 35.23 | 0.0 | 1.49 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_close_target5_loss3 | 64894 | 55701 | 30.71 | 29.99 | 39.3 | 0.0 | 3.17 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target5_low_stop5_order_unresolved | 64894 | 55701 | 30.54 | 3.9 | 29.23 | 36.33 | 3.17 | 14.73 | 66.87 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target8_low_stop5_order_unresolved | 64894 | 55701 | 26.87 | 7.57 | 39.38 | 26.18 | 3.17 | 14.73 | 66.87 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d10_close_target5_loss3 | 91226 | 86680 | 21.77 | 45.91 | 32.32 | 0.0 | 1.08 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_close_target5_loss3 | 91226 | 81923 | 28.37 | 34.8 | 36.83 | 0.0 | 2.58 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target5_low_stop5_order_unresolved | 91226 | 81923 | 32.21 | 8.67 | 29.6 | 29.52 | 2.58 | 12.79 | 61.73 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target8_low_stop5_order_unresolved | 91226 | 81923 | 26.55 | 14.33 | 38.59 | 20.53 | 2.58 | 12.79 | 61.73 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
