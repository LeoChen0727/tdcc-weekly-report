# Price Pullback 23EMA Operation Research

- generated_at: `2026-07-10 17:43:21 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 310808 | 296794 | 17.03 | 55.85 | 27.11 | 0.0 | 0.67 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 310808 | 282408 | 23.54 | 43.26 | 33.21 | 0.0 | 1.65 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 310808 | 282408 | 32.55 | 19.12 | 29.49 | 18.85 | 1.65 | 9.83 | 51.4 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 310808 | 282408 | 24.47 | 27.2 | 36.09 | 12.25 | 1.65 | 9.83 | 51.4 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 31433 | 30307 | 16.02 | 55.14 | 28.84 | 0.0 | 0.38 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 31433 | 28864 | 22.54 | 42.98 | 34.48 | 0.0 | 1.24 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 31433 | 28864 | 31.73 | 19.97 | 30.95 | 17.34 | 1.24 | 9.26 | 49.07 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 31433 | 28864 | 23.88 | 27.83 | 37.03 | 11.26 | 1.24 | 9.26 | 49.07 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 16502 | 15879 | 15.78 | 56.25 | 27.97 | 0.0 | 0.38 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 16502 | 15200 | 21.93 | 44.17 | 33.89 | 0.0 | 1.12 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 16502 | 15200 | 31.65 | 21.36 | 30.68 | 16.31 | 1.12 | 8.92 | 47.96 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 16502 | 15200 | 23.63 | 29.38 | 36.78 | 10.21 | 1.12 | 8.92 | 47.96 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10622 | 10213 | 15.56 | 55.05 | 29.39 | 0.0 | 0.24 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10622 | 9756 | 21.74 | 43.17 | 35.09 | 0.0 | 0.94 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10622 | 9756 | 30.95 | 20.64 | 31.75 | 16.66 | 0.94 | 8.93 | 47.6 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10622 | 9756 | 23.18 | 28.41 | 38.04 | 10.37 | 0.94 | 8.93 | 47.6 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d10_close_target5_loss3 | 62813 | 57897 | 26.61 | 36.77 | 36.62 | 0.0 | 1.66 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_close_target5_loss3 | 62813 | 52750 | 33.33 | 27.44 | 39.23 | 0.0 | 3.88 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target5_low_stop5_order_unresolved | 62813 | 52750 | 30.44 | 2.5 | 28.02 | 39.04 | 3.88 | 16.01 | 69.48 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target8_low_stop5_order_unresolved | 62813 | 52750 | 27.52 | 5.42 | 38.22 | 28.84 | 3.88 | 16.01 | 69.48 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d10_close_target5_loss3 | 68881 | 63841 | 25.05 | 39.35 | 35.59 | 0.0 | 1.42 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_close_target5_loss3 | 68881 | 58936 | 30.89 | 29.83 | 39.28 | 0.0 | 3.18 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target5_low_stop5_order_unresolved | 68881 | 58936 | 30.48 | 3.76 | 28.98 | 36.79 | 3.18 | 14.86 | 67.27 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target8_low_stop5_order_unresolved | 68881 | 58936 | 26.9 | 7.34 | 39.16 | 26.61 | 3.18 | 14.86 | 67.27 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d10_close_target5_loss3 | 95357 | 90119 | 21.67 | 45.68 | 32.65 | 0.0 | 1.06 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_close_target5_loss3 | 95357 | 85135 | 28.53 | 34.54 | 36.93 | 0.0 | 2.61 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target5_low_stop5_order_unresolved | 95357 | 85135 | 32.15 | 8.36 | 29.46 | 30.03 | 2.61 | 12.95 | 62.18 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target8_low_stop5_order_unresolved | 95357 | 85135 | 26.59 | 13.92 | 38.5 | 20.99 | 2.61 | 12.95 | 62.18 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
