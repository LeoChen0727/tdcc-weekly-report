# Research Against Stock Model Contract Parity

- generated_at: `2026-06-29 05:17:53 Asia/Taipei`
- production_contract_source: `config/stock_model_contract_registry.csv`
- production_condition_spec: `config/daily_model_condition_spec.csv`
- research_parity: `output/latest/research_backtest/daily_model_research_parity_latest.csv`
- research_metrics: `output/latest/daily_model_parameter_research_latest.csv`
- scope: research/backtest advisory-only; this artifact is not a daily production baseline.
- rule: config/stock_model_contract_registry.csv is the production stock-model source of truth for this validator.
- rule: production contract drift and missing research baselines fail validation.
- rule: research proxy rows are marked as research variants and require explicit promotion PR before daily production use.
- rule: this validator does not read or create stock_model_contract_snapshot_latest.json.

## Status Summary

| parity_status | count |
| --- | --- |
| hard_fail_contract_drift | 0 |
| missing_research_baseline | 0 |
| ok | 1 |
| warning_research_variant_only | 10 |

## OK Models

| model_id | production_contract_version | research_contract_version | d5_metric_available | d10_metric_available | d20_metric_available |
| --- | --- | --- | --- | --- | --- |
| volume_range_breakout | v1 | v1 | True | True | True |

## Research Variant / Proxy Only

| model_id | research_contract_version | promotion_required | parity_blocker | recommended_action |
| --- | --- | --- | --- | --- |
| hot_theme_pullback | research:production_current_proxy | True | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| near_high_neckline_challenge | research:production_current_proxy | True | neckline-specific fields and already-confirmed-breakout flags are not fully backfilled | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| neckline_volume_breakout_confirmation | research:production_current_proxy | True | structured neckline production detector is row/context based and not yet optimized for historical batch replay | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| platform_strengthening | research:production_current_proxy | True | platform_base_flag and platform width fields are not fully point-in-time backfilled | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| price_pullback_23ema | research:production_current_proxy | True | support/platform entry flags are not fully backfilled in the historical research frame | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| pullback_short_reclaim | research:production_current_proxy | True | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| revenue_unreacted_range | research:production_current_proxy | True | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| tdcc_short_term_continuation_d5_d10 | research:production_current_proxy | True | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| tdcc_stealth_accumulation | research:production_current_proxy | True | tdcc_price_phase is not fully available historically for every signal date | research_variant_only_do_not_promote_without_explicit_promotion_pr |
| w_bottom_right_side | research:production_current_proxy | True | full production W-bottom detector is row/context based; exact historical replay is too slow until an optimized batch detector exists | research_variant_only_do_not_promote_without_explicit_promotion_pr |

## Missing Research Baseline

No rows.

## Hard Fail Contract Drift

No rows.
