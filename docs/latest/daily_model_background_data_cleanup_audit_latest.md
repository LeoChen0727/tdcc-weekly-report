# Daily Model Background Data Cleanup Audit

- generated_at: `2026-07-04 21:43:56 Asia/Taipei`
- registry: `config/daily_model_background_data_registry.csv`
- rows: `19`
- deletion_allowed_rows: `0`
- deprecated_candidate_rows: `0`

This audit is a deletion gate. It does not delete artifacts. A data family
can move to a cleanup PR only when the registry marks it
`deprecated_candidate` and dependency checks do not find active workflow,
inventory, lineage, validator, replay, parity, or promotion references.

## Decision Summary

| deletion_decision | rows |
| --- | --- |
| retain_historical_replay_evidence | 2 |
| retain_latest_only_context | 1 |
| retain_model_research_evidence | 5 |
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
| neckline_context_interpretation | model_specific | active | retain_model_specific_semantics | False | keep with owning model contract; do not reuse across unrelated models |
| w_bottom_shape_interpretation | model_specific | active | retain_model_specific_semantics | False | keep with owning model contract; do not reuse across unrelated models |
| volume_breakout_operation_research_outputs | model_research_output | active | retain_model_research_evidence | False | keep until superseded by explicit approved operation or cleanup PR |

## Dependency Counts

| data_family_id | artifact_match_count | workflow_reference_count | inventory_reference_count | lineage_reference_count | script_test_reference_count | docs_reference_count |
| --- | --- | --- | --- | --- | --- | --- |
| stock_price_history | 2376 | 7 | 2 | 1 | 66 | 55 |
| tdcc_stock_history | 1974 | 3 | 2 | 1 | 18 | 33 |
| market_index_history | 1 | 2 | 2 | 1 | 24 | 18 |
| market_sentiment_context_history | 1 | 1 | 2 | 1 | 11 | 18 |
| daily_model_signal_snapshots | 13 | 1 | 2 | 1 | 35 | 19 |
| daily_all_candidates_snapshots | 13 | 5 | 2 | 1 | 58 | 19 |
| daily_model_signal_background_feature_panel | 1 | 9 | 2 | 1 | 87 | 63 |
| daily_model_background_feature_catalog | 1 | 1 | 2 | 1 | 4 | 2 |
| monthly_revenue_history | 1 | 1 | 2 | 1 | 13 | 11 |
| monthly_revenue_coverage_backfill_audit | 1 | 2 | 2 | 1 | 18 | 9 |
| monthly_revenue_point_in_time_panel | 1 | 5 | 2 | 1 | 65 | 22 |
| theme_taxonomy_latest | 1 | 1 | 2 | 1 | 29 | 17 |
| price_pullback_23ema_research_outputs | 14 | 1 | 2 | 1 | 18 | 34 |
| price_pullback_23ema_revenue_condition_matrix | 1 | 1 | 2 | 1 | 7 | 7 |
| price_pullback_23ema_promotion_matrix | 1 | 1 | 2 | 1 | 5 | 4 |
| revenue_unreacted_range_revenue_condition_matrix | 1 | 6 | 2 | 1 | 62 | 45 |
| neckline_context_interpretation | 1 | 6 | 2 | 1 | 79 | 51 |
| w_bottom_shape_interpretation | 1 | 5 | 2 | 1 | 77 | 52 |
| volume_breakout_operation_research_outputs | 15 | 8 | 2 | 1 | 242 | 176 |
