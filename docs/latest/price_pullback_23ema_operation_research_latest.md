# Price Pullback 23EMA Operation Research

- generated_at: `2026-07-04 18:45:18 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| entry_filter_id | operation_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | d10_close_target5_loss3 | 304517 | 291070 | 17.07 | 55.83 | 27.1 | 0.0 | 0.68 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_close_target5_loss3 | 304517 | 276640 | 23.4 | 43.25 | 33.35 | 0.0 | 1.61 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target5_low_stop5_order_unresolved | 304517 | 276640 | 32.3 | 19.24 | 29.71 | 18.75 | 1.61 | 9.76 | 51.06 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| baseline_replay | d20_high_target8_low_stop5_order_unresolved | 304517 | 276640 | 24.28 | 27.26 | 36.3 | 12.16 | 1.61 | 9.76 | 51.06 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d10_close_target5_loss3 | 30879 | 29825 | 16.02 | 55.18 | 28.8 | 0.0 | 0.39 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_close_target5_loss3 | 30879 | 27860 | 22.51 | 42.94 | 34.54 | 0.0 | 1.23 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 30879 | 27860 | 31.55 | 20.19 | 31.11 | 17.15 | 1.23 | 9.21 | 48.7 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 30879 | 27860 | 23.8 | 27.94 | 37.14 | 11.12 | 1.23 | 9.21 | 48.7 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d10_close_target5_loss3 | 16206 | 15650 | 15.79 | 56.29 | 27.92 | 0.0 | 0.4 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_close_target5_loss3 | 16206 | 14642 | 21.85 | 44.23 | 33.92 | 0.0 | 1.1 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target5_low_stop5_order_unresolved | 16206 | 14642 | 31.5 | 21.58 | 30.79 | 16.12 | 1.1 | 8.86 | 47.62 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.2 | d20_high_target8_low_stop5_order_unresolved | 16206 | 14642 | 23.53 | 29.55 | 36.87 | 10.05 | 1.1 | 8.86 | 47.62 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d10_close_target5_loss3 | 10435 | 10061 | 15.59 | 55.11 | 29.29 | 0.0 | 0.25 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_close_target5_loss3 | 10435 | 9352 | 21.76 | 43.21 | 35.03 | 0.0 | 0.94 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target5_low_stop5_order_unresolved | 10435 | 9352 | 30.77 | 20.93 | 31.8 | 16.5 | 0.94 | 8.89 | 47.27 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| solid_volume_red_k_vol1.5 | d20_high_target8_low_stop5_order_unresolved | 10435 | 9352 | 23.12 | 28.58 | 38.01 | 10.29 | 0.94 | 8.89 | 47.27 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d10_close_target5_loss3 | 60754 | 55863 | 26.98 | 36.69 | 36.33 | 0.0 | 1.76 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_close_target5_loss3 | 60754 | 50712 | 33.13 | 27.42 | 39.46 | 0.0 | 3.82 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target5_low_stop5_order_unresolved | 60754 | 50712 | 30.02 | 2.56 | 28.48 | 38.94 | 3.82 | 15.86 | 68.96 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext20_ema10_runup20_pullback5 | d20_high_target8_low_stop5_order_unresolved | 60754 | 50712 | 27.11 | 5.47 | 38.75 | 28.67 | 3.82 | 15.86 | 68.96 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d10_close_target5_loss3 | 66466 | 61920 | 25.36 | 39.38 | 35.26 | 0.0 | 1.51 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_close_target5_loss3 | 66466 | 56873 | 30.64 | 29.89 | 39.47 | 0.0 | 3.11 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target5_low_stop5_order_unresolved | 66466 | 56873 | 30.13 | 3.84 | 29.42 | 36.61 | 3.11 | 14.7 | 66.75 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext30_ema12_runup25_pullback8 | d20_high_target8_low_stop5_order_unresolved | 66466 | 56873 | 26.53 | 7.44 | 39.65 | 26.38 | 3.11 | 14.7 | 66.75 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d10_close_target5_loss3 | 92813 | 88066 | 21.81 | 45.82 | 32.37 | 0.0 | 1.11 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_close_target5_loss3 | 92813 | 83016 | 28.35 | 34.68 | 36.97 | 0.0 | 2.56 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target5_low_stop5_order_unresolved | 92813 | 83016 | 31.97 | 8.54 | 29.73 | 29.76 | 2.56 | 12.81 | 61.73 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| prior_ext60_ema15_runup35_pullback10 | d20_high_target8_low_stop5_order_unresolved | 92813 | 83016 | 26.37 | 14.14 | 38.78 | 20.71 | 2.56 | 12.81 | 61.73 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
