# Price Pullback 23EMA Operation Research

- generated_at: `2026-06-29 18:45:28 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- entry_basis: `signal_date_next_open` after production proxy replay
- scope: advisory operation candidates only; this does not approve daily production use
- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion

| operation_candidate_id | mature_count | win_rate_pct | neutral_rate_pct | loss_rate_pct | ambiguous_order_rate_pct | avg_close_return_pct | avg_high_return_pct | high_5pct_hit_rate_pct | promotion_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| d10_close_target5_loss3 | 284059 | 17.14 | 55.87 | 26.99 | 0.0 | 0.7 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| d20_close_target5_loss3 | 270151 | 23.44 | 43.24 | 33.32 | 0.0 | 1.63 |  |  | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| d20_high_target5_low_stop5_order_unresolved | 270151 | 32.41 | 19.33 | 29.73 | 18.53 | 1.63 | 9.74 | 50.95 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
| d20_high_target8_low_stop5_order_unresolved | 270151 | 24.38 | 27.36 | 36.27 | 11.99 | 1.63 | 9.74 | 50.95 | requires exact daily candidate row parity plus validated buy/sell/stop operation module |
