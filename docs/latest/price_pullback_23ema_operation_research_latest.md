# Price Pullback 23EMA Operation Research

- generated_at: `2026-06-30 10:05:05 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 298431 | 285464 | 17.11 | 55.83 | 27.06 | 0.0 | 0.69 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 298431 | 271518 | 23.44 | 43.24 | 33.32 | 0.0 | 1.63 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 298431 | 271518 | 32.46 | 19.3 | 29.67 | 18.57 | 1.63 | 9.76 | 51.03 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 298431 | 271518 | 24.41 | 27.34 | 36.23 | 12.02 | 1.63 | 9.76 | 51.03 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 30382 | 29195 | 16.01 | 55.26 | 28.72 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 30382 | 26981 | 22.65 | 42.69 | 34.66 | 0.0 | 1.25 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 30382 | 26981 | 31.59 | 20.05 | 31.17 | 17.19 | 1.25 | 9.25 | 48.78 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 30382 | 26981 | 23.86 | 27.78 | 37.19 | 11.17 | 1.25 | 9.25 | 48.78 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 15913 | 15346 | 15.8 | 56.32 | 27.88 | 0.0 | 0.38 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 15913 | 14074 | 22.01 | 43.91 | 34.08 | 0.0 | 1.11 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 15913 | 14074 | 31.48 | 21.48 | 30.89 | 16.14 | 1.11 | 8.91 | 47.63 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 15913 | 14074 | 23.57 | 29.39 | 36.94 | 10.1 | 1.11 | 8.91 | 47.63 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10239 | 9855 | 15.62 | 55.13 | 29.25 | 0.0 | 0.26 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10239 | 8972 | 22.04 | 42.76 | 35.21 | 0.0 | 0.96 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10239 | 8972 | 30.8 | 20.78 | 31.79 | 16.64 | 0.96 | 8.96 | 47.44 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10239 | 8972 | 23.21 | 28.37 | 38.02 | 10.41 | 0.96 | 8.96 | 47.44 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d10_close_target5_loss3 | 58473 | 53855 | 27.18 | 36.61 | 36.21 | 0.0 | 1.78 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_close_target5_loss3 | 58473 | 49229 | 33.25 | 27.49 | 39.26 | 0.0 | 3.9 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target5_low_stop5_order_unresolved | 58473 | 49229 | 30.5 | 2.6 | 28.28 | 38.62 | 3.9 | 15.91 | 69.12 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target8_low_stop5_order_unresolved | 58473 | 49229 | 27.52 | 5.58 | 38.42 | 28.48 | 3.9 | 15.91 | 69.12 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d10_close_target5_loss3 | 64352 | 60006 | 25.41 | 39.44 | 35.15 | 0.0 | 1.51 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_close_target5_loss3 | 64352 | 55347 | 30.76 | 30.0 | 39.24 | 0.0 | 3.19 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target5_low_stop5_order_unresolved | 64352 | 55347 | 30.62 | 3.91 | 29.2 | 36.27 | 3.19 | 14.75 | 66.89 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target8_low_stop5_order_unresolved | 64352 | 55347 | 26.94 | 7.59 | 39.32 | 26.15 | 3.19 | 14.75 | 66.89 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d10_close_target5_loss3 | 90694 | 86250 | 21.78 | 45.97 | 32.25 | 0.0 | 1.09 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_close_target5_loss3 | 90694 | 81613 | 28.39 | 34.83 | 36.79 | 0.0 | 2.59 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target5_low_stop5_order_unresolved | 90694 | 81613 | 32.26 | 8.7 | 29.58 | 29.46 | 2.59 | 12.78 | 61.72 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target8_low_stop5_order_unresolved | 90694 | 81613 | 26.57 | 14.38 | 38.56 | 20.49 | 2.59 | 12.78 | 61.72 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
