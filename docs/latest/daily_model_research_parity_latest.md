# Daily Model Research Baseline Parity

- generated_at: `2026-08-31 02:08:23 Asia/Taipei`
- purpose: verify that every daily production core model has a research production-baseline row before parameter variants are compared
- production_parity: historical research fields can replay the production baseline directly
- production_proxy / proxy_only: baseline exists, but one or more production fields are not fully available point-in-time in the research frame
- rule: variants must compare against the production_baseline row of the same model_id; proxy rows cannot be promoted without resolving blockers
- revenue exact-evidence preparation: `revenue_unreacted_range` is bound to the frozen `source_mid_falling v2` launch evidence while remaining `proxy_only`; its legacy generic proxy is advisory-only and the exact evidence grants no daily/PDF/production permission.

## Status Summary

| research_baseline_status | count |
| --- | --- |
| production_parity | 6 |
| production_proxy | 4 |
| proxy_only | 1 |

## Model Parity Detail

| model_id | research_baseline_status | research_baseline_parameter_set_id | research_variant_count | baseline_selected_stock_days | baseline_selected_unique_stocks | parity_blocker | completion_rule | research_baseline_evidence_path | research_baseline_evidence_status | research_baseline_rule_spec_id | research_baseline_rule_canonical_sha256 | research_baseline_outcome_basis | research_baseline_permission_status | research_baseline_forward_holdout_policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_position_volume_attack | production_parity | volume_range_breakout_v2_low_position_operation_v1 | 0 | 21 | 20 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| volume_range_breakout_v2_mid_position_momentum_attack | production_parity | volume_range_breakout_v2_mid_position_operation_v1 | 0 | 13 | 11 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| volume_range_breakout_v2_high_position_volume_attack | production_parity | volume_range_breakout_v2_high_position_operation_v1 | 0 | 231 | 187 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| price_pullback_23ema | production_parity | price_pullback_23ema_prev20_breakout_stop_v1 | 12 | 9612 | 1186 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| hot_theme_pullback | production_proxy | production_current_proxy | 6 | 5590 | 906 | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | usable_for_relative_research_only_until_blocker_resolved |  |  |  |  |  |  |  |
| revenue_unreacted_range | proxy_only | revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830 | 3 | 53 | 48 | exact_frozen_evidence_ready_but_daily_model_condition_spec_and_production_permissions_not_promoted | exact_frozen_rule_evidence_ready_contract_promotion_pending_no_permission_grant | config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_manifest.csv | provisional_backtest_supported_oos_unconfirmed | revenue_unreacted_range_source_mid_falling_d30_v1 | 1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633 | D2_open_after_close_confirmed_continuation_to_D30_close | evidence_only_no_permission_grant | post_launch_monitoring_non_hard_no_tuning |
| w_bottom_right_side | production_parity | w_bottom_early_entry_operation_v2 | 3 | 44 | 44 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| neckline_volume_breakout_confirmation | production_parity | neckline_strict_45_signal_90_score_v1 | 0 | 51 | 51 |  | usable_as_exact_baseline |  |  |  |  |  |  |  |
| pullback_short_reclaim | production_proxy | production_current_proxy | 3 | 89287 | 1863 | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | usable_for_relative_research_only_until_blocker_resolved |  |  |  |  |  |  |  |
| tdcc_stealth_accumulation | production_proxy | production_current_proxy | 3 | 41834 | 1790 | tdcc_price_phase is not fully available historically for every signal date | usable_for_relative_research_only_until_blocker_resolved |  |  |  |  |  |  |  |
| tdcc_short_term_continuation_d5_d10 | production_proxy | production_current_proxy | 2 | 3804 | 869 | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | usable_for_relative_research_only_until_blocker_resolved |  |  |  |  |  |  |  |
