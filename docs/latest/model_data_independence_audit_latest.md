# 每日股票模型與資料獨立性稽核

- 產生時間：`2026-09-02 18:51:02 Asia/Taipei`
- 結果：`CONTAINED=23, DISCLOSED_NOT_INDEPENDENT=4, PASS=74`
- 原則：新模型與新資料 family 預設獨立；跨模型共用商業語意必須先有使用者核准與 migration evidence。
- `CONTAINED` 代表既有共用已被凍結與精確盤點，不代表已物理拆分。
- `DISCLOSED_NOT_INDEPENDENT` 代表該 validator 只能做 implementation consistency，不得當成獨立模型正確性證據。

| 領域 | 對象 | 狀態 | ownership | 剩餘缺口 |
|---|---|---|---|---|
| production_model_semantics | hot_theme_pullback | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | neckline_volume_breakout_confirmation | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | price_pullback_23ema | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | pullback_short_reclaim | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | revenue_unreacted_range | PASS | model_owned_module | none |
| production_model_semantics | tdcc_short_term_continuation_d5_d10 | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | tdcc_stealth_accumulation | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | volume_range_breakout_v2_high_position_volume_attack | CONTAINED | contained_model_family_dispatcher | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | volume_range_breakout_v2_low_position_volume_attack | CONTAINED | contained_model_family_dispatcher | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | volume_range_breakout_v2_mid_position_momentum_attack | CONTAINED | contained_model_family_dispatcher | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| production_model_semantics | w_bottom_right_side | CONTAINED | contained_legacy_monolith | existing shared producer/semantic remains frozen; future model must use a model-owned module |
| shared_production_semantics | contained_legacy_cross_model_semantic | CONTAINED | contained_legacy_cross_model_semantic | legacy sharing is contained but not physically separated |
| shared_production_semantics | contained_model_family_semantic | CONTAINED | contained_model_family_semantic | legacy sharing is contained but not physically separated |
| shared_production_semantics | registered_cross_model_runtime_semantic | CONTAINED | registered_cross_model_runtime_semantic | legacy sharing is contained but not physically separated |
| shared_production_semantics | shared_technical | PASS | shared_technical | none |
| data_family_ownership | pullback_short_reclaim_research_outputs | PASS | model_owned_not_shared | none |
| data_family_ownership | hot_theme_pullback_published_signal_research_outputs | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_snapshot_projection_v1_archive | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_snapshot_projection_v2_candidate | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_snapshot_projection_v1_v2_diff | PASS | model_owned_not_shared | none |
| data_family_ownership | stock_price_history | PASS | approved_shared_objective | none |
| data_family_ownership | tdcc_stock_history | PASS | approved_shared_objective | none |
| data_family_ownership | market_index_history | PASS | approved_shared_objective | none |
| data_family_ownership | market_sentiment_context_history | PASS | approved_shared_objective | none |
| data_family_ownership | daily_model_signal_snapshots | PASS | approved_shared_replay_read_only | none |
| data_family_ownership | daily_all_candidates_snapshots | PASS | approved_shared_replay_read_only | none |
| data_family_ownership | daily_model_snapshot_revision_manifest | PASS | approved_shared_replay_read_only | none |
| data_family_ownership | daily_model_signal_background_feature_panel | PASS | approved_shared_objective | none |
| data_family_ownership | daily_model_background_feature_catalog | PASS | approved_shared_objective | none |
| data_family_ownership | monthly_revenue_history | PASS | approved_shared_objective | none |
| data_family_ownership | monthly_revenue_coverage_backfill_audit | PASS | approved_shared_objective | none |
| data_family_ownership | monthly_revenue_point_in_time_panel | PASS | approved_shared_objective | none |
| data_family_ownership | theme_taxonomy_latest | CONTAINED | latest_context_not_historical | legacy/latest/audit data is barred from formal model evidence |
| data_family_ownership | price_pullback_23ema_research_outputs | PASS | model_owned_not_shared | none |
| data_family_ownership | price_pullback_23ema_revenue_condition_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | price_pullback_23ema_promotion_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_revenue_condition_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_operation_candidate_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_feature_contrast_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_close_confirmation_timing_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_fixed_confirmation_feature_contrast_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_extreme_return_path_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_lag_strength_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | volume_range_breakout_v2_high_position_improvement_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | mature_model_row_level_metric_contract_audit | CONTAINED | cross_model_audit_not_model_evidence | legacy/latest/audit data is barred from formal model evidence |
| data_family_ownership | neckline_context_interpretation | PASS | model_family_owned_not_shared | none |
| data_family_ownership | w_bottom_shape_interpretation | PASS | model_family_owned_not_shared | none |
| data_family_ownership | volume_breakout_operation_research_outputs | CONTAINED | legacy_frozen_no_new_consumers | legacy/latest/audit data is barred from formal model evidence |
| data_family_ownership | revenue_unreacted_range_launch_timing_feature_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_first_condition_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_snapshot_projection | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_source_snapshot_projection_v2_supersede_evidence | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_forward_confirmation_feature_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_rearmed_operation_grid | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_operation_lag_bucket_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_position_shape_transition_matrix | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_low_mid_falling_candidate_audit | PASS | model_owned_not_shared | none |
| data_family_ownership | financial_statement_point_in_time_history | PASS | approved_shared_objective | none |
| data_family_ownership | financial_statement_source_manifest | PASS | approved_shared_objective | none |
| data_family_ownership | financial_statement_pit_coverage_audit | PASS | approved_shared_objective | none |
| data_family_ownership | financial_statement_historical_pit_source_audit | PASS | approved_shared_objective | none |
| data_family_ownership | official_warrant_flow_current_snapshot | CONTAINED | latest_context_not_historical | legacy/latest/audit data is barred from formal model evidence |
| data_family_ownership | revenue_unreacted_range_forward_holdout | PASS | model_owned_not_shared | none |
| data_family_ownership | revenue_unreacted_range_forward_holdout_v2 | PASS | model_owned_not_shared | none |
| data_family_ownership | volume_v2_watch_committed_lineage_audit | PASS | model_family_owned_not_shared | none |
| numerical_anomaly_governance | repo_wide_root_cause_disposition_contract | PASS | repo_wide_governance_contract | none |
| numerical_anomaly_governance | monthly_revenue_history_legacy_threshold_flag | CONTAINED | legacy_threshold_flag_candidate_only | source schema still uses a legacy anomaly field name and must be treated as candidate-only |
| numerical_anomaly_governance | revenue_unreacted_range | CONTAINED | model_owned_root_cause_pending | corporate-action PIT, independent-source corroboration, and adjustment-basis checks remain incomplete |
| numerical_anomaly_governance | price_pullback_23ema | CONTAINED | model_owned_root_cause_pending | all root-cause checks must complete before any candidate may be excluded |
| numerical_anomaly_governance | volume_range_breakout_v2_legacy_quantile_artifacts | CONTAINED | legacy_threshold_artifacts_contained | republish under the root-cause disposition contract before reopening or promotion |
| research_producer_ownership | hot_theme_pullback | PASS | model_owned_write | none |
| research_producer_ownership | neckline_volume_breakout_confirmation | CONTAINED | no_enabled_model_owned_research_entrypoint | before reopening research this model needs its own producer artifact allowlist and sentinel test |
| research_producer_ownership | price_pullback_23ema | PASS | model_owned_write | none |
| research_producer_ownership | pullback_short_reclaim | PASS | model_owned_write | none |
| research_producer_ownership | revenue_unreacted_range | PASS | model_owned_write | none |
| research_producer_ownership | tdcc_short_term_continuation_d5_d10 | PASS | model_owned_write | none |
| research_producer_ownership | tdcc_stealth_accumulation | PASS | model_owned_write | none |
| research_producer_ownership | volume_range_breakout_v2_high_position_volume_attack | PASS | model_owned_write | none |
| research_producer_ownership | volume_range_breakout_v2_low_position_volume_attack | PASS | model_owned_write | none |
| research_producer_ownership | volume_range_breakout_v2_mid_position_momentum_attack | PASS | model_owned_write | none |
| research_producer_ownership | w_bottom_right_side | CONTAINED | no_enabled_model_owned_research_entrypoint | before reopening research this model needs its own producer artifact allowlist and sentinel test |
| formal_evidence_binding | neckline_volume_breakout_confirmation | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | price_pullback_23ema | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | revenue_unreacted_range | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | volume_range_breakout_v2_high_position_volume_attack | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | volume_range_breakout_v2_low_position_volume_attack | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | volume_range_breakout_v2_mid_position_momentum_attack | PASS | pinned_formal_evidence | none |
| formal_evidence_binding | w_bottom_right_side | PASS | pinned_formal_evidence | none |
| validator_independence | scripts/audit_daily_candidate_model_selection_correctness.py | DISCLOSED_NOT_INDEPENDENT | implementation_consistency_audit | may verify implementation consistency only; cannot prove model correctness independently |
| validator_independence | scripts/audit_daily_candidate_pipeline_integrity.py | DISCLOSED_NOT_INDEPENDENT | implementation_consistency_audit | may verify implementation consistency only; cannot prove model correctness independently |
| validator_independence | scripts/validate_daily_model_research_parity.py | DISCLOSED_NOT_INDEPENDENT | production_research_contract_consistency | may verify implementation consistency only; cannot prove model correctness independently |
| validator_independence | scripts/validate_model_data_independence.py | PASS | independent_contract_ast_guard | none |
| validator_independence | scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py | PASS | independent_contract_ast_guard | none |
| validator_independence | scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py | PASS | independent_source_lineage_validator | none |
| validator_independence | scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py | PASS | independent_research_replay_validator | none |
| validator_independence | scripts/validate_revenue_unreacted_range_promotion_preparation.py | PASS | independent_contract_artifact_binding_validator | none |
| validator_independence | scripts/validate_research_against_stock_model_contract.py | DISCLOSED_NOT_INDEPENDENT | production_research_contract_consistency | may verify implementation consistency only; cannot prove model correctness independently |
| validator_independence | scripts/validate_revenue_unreacted_range_source_snapshot_projection.py | PASS | independent_source_lineage_validator | none |
| validator_independence | scripts/validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff.py | PASS | independent_contract_artifact_binding_validator | none |
| validator_independence | scripts/validate_revenue_unreacted_range_forward_holdout.py | PASS | input_bound_in_process_independent_validator | none |
| validator_independence | scripts/validate_revenue_unreacted_range_forward_holdout_v2.py | PASS | input_bound_in_process_independent_validator | none |
