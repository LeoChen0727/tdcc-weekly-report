# Daily Model Research Baseline Parity

- generated_at: `2026-06-30 11:05:58 Asia/Taipei`
- purpose: verify that every daily production core model has a research production-baseline row before parameter variants are compared
- production_parity: historical research fields can replay the production baseline directly
- production_proxy / proxy_only: baseline exists, but one or more production fields are not fully available point-in-time in the research frame
- rule: variants must compare against the production_baseline row of the same model_id; proxy rows cannot be promoted without resolving blockers

## Status Summary

| research_baseline_status | count |
| --- | --- |
| production_proxy | 5 |
| production_parity | 3 |
| proxy_only | 1 |

## Model Parity Detail

| model_id | research_baseline_status | research_baseline_parameter_set_id | research_variant_count | baseline_selected_stock_days | baseline_selected_unique_stocks | parity_blocker | completion_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | production_parity | production_current | 28 | 4297 | 1214 |  | usable_as_exact_baseline |
| price_pullback_23ema | production_proxy | production_current_proxy | 12 | 298431 | 1971 | as-published daily candidate row parity and a validated operation module are still pending | usable_for_relative_research_only_until_blocker_resolved |
| hot_theme_pullback | production_proxy | production_current_proxy | 6 | 3517 | 787 | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | usable_for_relative_research_only_until_blocker_resolved |
| revenue_unreacted_range | proxy_only | production_current_proxy | 2 | 333702 | 1986 | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | usable_for_relative_research_only_until_blocker_resolved |
| w_bottom_right_side | production_parity | w_bottom_early_entry_operation_v2 | 3 | 44 | 44 |  | usable_as_exact_baseline |
| neckline_volume_breakout_confirmation | production_parity | neckline_strict_45_signal_90_score_v1 | 0 | 51 | 51 |  | usable_as_exact_baseline |
| pullback_short_reclaim | production_proxy | production_current_proxy | 3 | 85716 | 1853 | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | usable_for_relative_research_only_until_blocker_resolved |
| tdcc_stealth_accumulation | production_proxy | production_current_proxy | 3 | 34681 | 1765 | tdcc_price_phase is not fully available historically for every signal date | usable_for_relative_research_only_until_blocker_resolved |
| tdcc_short_term_continuation_d5_d10 | production_proxy | production_current_proxy | 2 | 3288 | 791 | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | usable_for_relative_research_only_until_blocker_resolved |
