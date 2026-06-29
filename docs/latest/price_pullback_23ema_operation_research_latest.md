# Price Pullback 23EMA Operation Research

- generated_at: `2026-06-29 21:11:25 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 296964 | 284059 | 17.14 | 55.87 | 26.99 | 0.0 | 0.7 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 296964 | 270151 | 23.44 | 43.24 | 33.32 | 0.0 | 1.63 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 296964 | 270151 | 32.41 | 19.33 | 29.73 | 18.53 | 1.63 | 9.74 | 50.95 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 296964 | 270151 | 24.38 | 27.36 | 36.27 | 11.99 | 1.63 | 9.74 | 50.95 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 30326 | 29032 | 16.03 | 55.34 | 28.63 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 30326 | 26755 | 22.64 | 42.68 | 34.68 | 0.0 | 1.25 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 30326 | 26755 | 31.49 | 20.07 | 31.27 | 17.18 | 1.25 | 9.24 | 48.67 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 30326 | 26755 | 23.79 | 27.77 | 37.28 | 11.17 | 1.25 | 9.24 | 48.67 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 15893 | 15292 | 15.82 | 56.36 | 27.82 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 15893 | 13941 | 21.99 | 43.91 | 34.11 | 0.0 | 1.11 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 15893 | 13941 | 31.32 | 21.53 | 31.01 | 16.14 | 1.11 | 8.89 | 47.46 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 15893 | 13941 | 23.43 | 29.42 | 37.05 | 10.1 | 1.11 | 8.89 | 47.46 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10223 | 9815 | 15.64 | 55.18 | 29.18 | 0.0 | 0.27 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10223 | 8892 | 21.96 | 42.75 | 35.29 | 0.0 | 0.94 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10223 | 8892 | 30.6 | 20.83 | 31.92 | 16.66 | 0.94 | 8.93 | 47.26 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10223 | 8892 | 23.04 | 28.39 | 38.15 | 10.43 | 0.94 | 8.93 | 47.26 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
