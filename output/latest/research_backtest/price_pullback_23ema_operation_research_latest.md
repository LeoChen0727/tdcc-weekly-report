# Price Pullback 23EMA Operation Research

- generated_at: `2026-06-29 23:59:22 Asia/Taipei`
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
