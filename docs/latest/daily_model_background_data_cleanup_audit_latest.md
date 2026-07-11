# Daily Model Background Data Cleanup Audit

- generated_at: `2026-07-12 01:24:46 Asia/Taipei`
- registry: `config/daily_model_background_data_registry.csv`
- rows: `25`
- deletion_allowed_rows: `0`
- deprecated_candidate_rows: `1`

This audit is a deletion gate. It does not delete artifacts. A data family
can move to a cleanup PR only when the registry marks it
`deprecated_candidate` and dependency checks do not find active workflow,
inventory, lineage, validator, replay, parity, or promotion references.

## Decision Summary

| deletion_decision | rows |
| --- | --- |
| blocked_deprecated_candidate_has_dependencies | 1 |
| retain_historical_replay_evidence | 2 |
| retain_latest_only_context | 1 |
| retain_model_research_evidence | 10 |
| retain_model_specific_semantics | 2 |
| retain_shared_objective_source | 9 |

## Data Family Decisions

| data_family_id | scope | cleanup_status | deletion_decision | deletion_allowed | required_next_step |
| --- | --- | --- | --- | --- | --- |
| stock_price_history | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| tdcc_stock_history | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| market_index_history | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| market_sentiment_context_history | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| daily_model_signal_snapshots | shared_replay_evidence | active | retain_historical_replay_evidence | False | do not delete; preserve replay and parity audit trail |
| daily_all_candidates_snapshots | shared_replay_source | active | retain_historical_replay_evidence | False | do not delete; preserve replay and parity audit trail |
| daily_model_signal_background_feature_panel | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| daily_model_background_feature_catalog | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| monthly_revenue_history | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| monthly_revenue_coverage_backfill_audit | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| monthly_revenue_point_in_time_panel | shared_objective | active | retain_shared_objective_source | False | reuse only with point-in-time rules; do not convert to model gate by itself |
| theme_taxonomy_latest | latest_only_context | active | retain_latest_only_context | False | do not use as historical point-in-time label |
| price_pullback_23ema_research_outputs | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| price_pullback_23ema_revenue_condition_matrix | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| price_pullback_23ema_promotion_matrix | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| revenue_unreacted_range_revenue_condition_matrix | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| revenue_unreacted_range_operation_candidate_matrix | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| revenue_unreacted_range_feature_contrast_audit | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| revenue_unreacted_range_close_confirmation_timing_audit | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| revenue_unreacted_range_fixed_confirmation_feature_contrast_audit | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| volume_range_breakout_v2_high_position_improvement_audit | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| mature_model_row_level_metric_contract_audit | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |
| neckline_context_interpretation | model_specific | active | retain_model_specific_semantics | False | keep with owning model contract; do not reuse across unrelated models |
| w_bottom_shape_interpretation | model_specific | active | retain_model_specific_semantics | False | keep with owning model contract; do not reuse across unrelated models |
| volume_breakout_operation_research_outputs | model_research_output | deprecated_candidate | blocked_deprecated_candidate_has_dependencies | False | remove or migrate dependencies in a reviewed cleanup PR before deleting artifacts |

## Dependency Counts

| data_family_id | artifact_match_count | workflow_reference_count | inventory_reference_count | lineage_reference_count | script_test_reference_count | docs_reference_count |
| --- | --- | --- | --- | --- | --- | --- |
| stock_price_history | 2376 | 9 | 2 | 1 | 86 | 57 |
| tdcc_stock_history | 1974 | 3 | 2 | 1 | 18 | 33 |
| market_index_history | 1 | 2 | 2 | 1 | 25 | 18 |
| market_sentiment_context_history | 1 | 1 | 2 | 1 | 11 | 18 |
| daily_model_signal_snapshots | 17 | 5 | 2 | 1 | 45 | 19 |
| daily_all_candidates_snapshots | 17 | 6 | 2 | 1 | 60 | 19 |
| daily_model_signal_background_feature_panel | 1 | 11 | 2 | 1 | 95 | 62 |
| daily_model_background_feature_catalog | 1 | 1 | 2 | 1 | 4 | 2 |
| monthly_revenue_history | 1 | 1 | 2 | 1 | 13 | 12 |
| monthly_revenue_coverage_backfill_audit | 1 | 2 | 2 | 1 | 20 | 10 |
| monthly_revenue_point_in_time_panel | 1 | 5 | 2 | 1 | 65 | 22 |
| theme_taxonomy_latest | 1 | 1 | 2 | 1 | 30 | 17 |
| price_pullback_23ema_research_outputs | 14 | 3 | 2 | 1 | 37 | 49 |
| price_pullback_23ema_revenue_condition_matrix | 1 | 1 | 2 | 1 | 8 | 9 |
| price_pullback_23ema_promotion_matrix | 1 | 1 | 2 | 1 | 6 | 6 |
| revenue_unreacted_range_revenue_condition_matrix | 1 | 6 | 2 | 1 | 71 | 45 |
| revenue_unreacted_range_operation_candidate_matrix | 1 | 9 | 2 | 1 | 78 | 57 |
| revenue_unreacted_range_feature_contrast_audit | 1 | 9 | 2 | 1 | 85 | 61 |
| revenue_unreacted_range_close_confirmation_timing_audit | 1 | 6 | 2 | 1 | 71 | 50 |
| revenue_unreacted_range_fixed_confirmation_feature_contrast_audit | 1 | 9 | 2 | 1 | 85 | 63 |
| volume_range_breakout_v2_high_position_improvement_audit | 1 | 6 | 2 | 1 | 72 | 46 |
| mature_model_row_level_metric_contract_audit | 1 | 3 | 2 | 1 | 34 | 28 |
| neckline_context_interpretation | 1 | 7 | 2 | 1 | 91 | 51 |
| w_bottom_shape_interpretation | 1 | 6 | 2 | 1 | 89 | 52 |
| volume_breakout_operation_research_outputs | 15 | 9 | 2 | 1 | 290 | 198 |
