# Daily Model Research Parity

- generated_at: `2026-07-09 20:00:25 Asia/Taipei`
- note: volume_range_breakout v1 is isolated; v2 low/mid formal rows are sourced from volume_range_breakout_v2_candidate_bucket_contract.

| model_id | research_baseline_status | baseline | blocker |
| --- | --- | --- | --- |
| volume_range_breakout_v2_low_position_volume_attack | production_parity | volume_range_breakout_v2_low_position_operation_v1 |  |
| volume_range_breakout_v2_mid_position_momentum_attack | production_parity | volume_range_breakout_v2_mid_position_operation_v1 |  |
| volume_range_breakout | production_parity | production_current | legacy v1 isolated; retained only for audit/research history after v2 split |
| hot_theme_pullback | production_proxy | production_current_proxy | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields |
| neckline_volume_breakout_confirmation | production_parity | neckline_strict_45_signal_90_score_v1 |  |
| price_pullback_23ema | production_parity | price_pullback_23ema_prev20_breakout_stop_v1 |  |
| pullback_short_reclaim | production_proxy | production_current_proxy | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled |
| revenue_unreacted_range | proxy_only | production_current_proxy | strong_revenue gate requires model-specific research matrix, contract update, exact parity, and promotion PR before formal use |
| tdcc_short_term_continuation_d5_d10 | production_proxy | production_current_proxy | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies |
| tdcc_stealth_accumulation | production_proxy | production_current_proxy | tdcc_price_phase is not fully available historically for every signal date |
| w_bottom_right_side | production_parity | w_bottom_early_entry_operation_v2 |  |
