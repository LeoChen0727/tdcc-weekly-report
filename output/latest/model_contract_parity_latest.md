# Research Against Stock Model Contract Parity

- generated_at: `2026-08-31 02:08:59 Asia/Taipei`
- production_contract_source: `config/stock_model_contract_registry.csv`
- production_condition_spec: `config/daily_model_condition_spec.csv`
- research_parity: `output/latest/research_backtest/daily_model_research_parity_latest.csv`
- research_metrics: `output/latest/daily_model_parameter_research_latest.csv`
- scope: research/backtest advisory-only; this artifact is not a daily production baseline.
- rule: config/stock_model_contract_registry.csv is the production stock-model source of truth for this validator.
- rule: production contract drift and missing research baselines fail validation.
- rule: research proxy rows are marked as research variants and require explicit promotion PR before daily production use.
- revenue pre-promotion rule: exact frozen evidence may be bound while parity remains proxy_only/warning and all production permissions remain false.
- rule: this validator does not read or create stock_model_contract_snapshot_latest.json.

## Status Summary

| parity_status | count |
| --- | --- |
| hard_fail_contract_drift | 0 |
| missing_research_baseline | 0 |
| ok | 6 |
| warning_research_variant_only | 5 |

## OK Models

| model_id | production_contract_version | research_contract_version | d5_metric_available | d10_metric_available | d20_metric_available | research_evidence_path | research_evidence_status | research_permission_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| neckline_volume_breakout_confirmation | v1 | v1 | True | True | True |  |  |  |
| price_pullback_23ema | v3 | v3 | True | True | True |  |  |  |
| volume_range_breakout_v2_high_position_volume_attack | v1 | v1 | False | False | False |  |  |  |
| volume_range_breakout_v2_low_position_volume_attack | v1 | v1 | True | True | True |  |  |  |
| volume_range_breakout_v2_mid_position_momentum_attack | v1 | v1 | True | True | True |  |  |  |
| w_bottom_right_side | v1 | v1 | True | True | True |  |  |  |

## Research Variant / Proxy Only

| model_id | research_contract_version | promotion_required | parity_blocker | research_evidence_path | research_evidence_status | research_permission_status | recommended_action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hot_theme_pullback | research:production_current_proxy | True | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields |  |  |  | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| pullback_short_reclaim | research:production_current_proxy | True | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled |  |  |  | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| revenue_unreacted_range | research:revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830 | True | exact_frozen_evidence_ready_but_daily_model_condition_spec_and_production_permissions_not_promoted | config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_manifest.csv | provisional_backtest_supported_oos_unconfirmed | evidence_only_no_permission_grant | exact_frozen_evidence_ready_do_not_promote_until_model_contract_sync |
| tdcc_short_term_continuation_d5_d10 | research:production_current_proxy | True | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies |  |  |  | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| tdcc_stealth_accumulation | research:production_current_proxy | True | tdcc_price_phase is not fully available historically for every signal date |  |  |  | research_variant_only_do_not_promote_without_explicit_promotion_pr |

## Missing Research Baseline

No rows.

## Hard Fail Contract Drift

No rows.
