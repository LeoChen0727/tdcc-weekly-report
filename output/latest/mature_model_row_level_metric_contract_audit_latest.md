# Mature Model Row-Level Metric Contract Audit

- audit_id: `mature_model_row_level_metric_contract_audit_20260710`
- audit_version: `v1`
- generated_at: `2026-07-11 10:43:27 Asia/Taipei`

## Contract

- Single add-score item may use the approved single-item metric.
- Multi-item add-score combinations must use the exact recomputed combination metric.
- A promoted row-level combination must not be worse than the baseline on all primary metrics.
- PDF operation rows must use the matched row-level metric when the model-owned adapter provides one.
- Research-only combo rows must remain unavailable to PDF operation rows until a model-specific promotion PR wires an approved adapter metric.

## Audit Rows

| scope | model_id | metric_scope | row_level_metric_status | combo_policy | production_readiness | issues |
| --- | --- | --- | --- | --- | --- | --- |
| mature_model | `volume_range_breakout_v2_low_position_volume_attack` | baseline_plus_generic_row_level_combo | not_applicable_no_formal_row_level_add_score_metric | pdf_bonus_combo:no_current_metric_rows / pdf_bonus_combo:not_applicable_no_current_metric_rows | production_adapter_contract_checked | none |
| mature_model | `volume_range_breakout_v2_mid_position_momentum_attack` | baseline_plus_generic_row_level_combo | not_applicable_no_formal_row_level_add_score_metric | pdf_bonus_combo:no_current_metric_rows / pdf_bonus_combo:not_applicable_no_current_metric_rows | production_adapter_contract_checked | none |
| mature_model | `volume_range_breakout_v2_high_position_volume_attack` | baseline_plus_generic_row_level_combo | not_applicable_no_formal_row_level_add_score_metric | pdf_bonus_combo:no_current_metric_rows / pdf_bonus_combo:not_applicable_no_current_metric_rows | production_adapter_contract_checked | none |
| mature_model | `w_bottom_right_side` | baseline_only_no_formal_add_score_metric | not_applicable_no_formal_row_level_add_score_metric | not_applicable_no_formal_row_level_add_score_metric / not_applicable_no_formal_row_level_add_score_metric | production_adapter_contract_checked | none |
| mature_model | `neckline_volume_breakout_confirmation` | baseline_only_no_formal_add_score_metric | not_applicable_no_formal_row_level_add_score_metric | not_applicable_no_formal_row_level_add_score_metric / not_applicable_no_formal_row_level_add_score_metric | production_adapter_contract_checked | none |
| mature_model | `price_pullback_23ema` | baseline_plus_technical_package | pass_technical_package_metrics_present_for_technical_strength_rows | pass_exact_package_metric_required_for_multi_feature_technical_strength / pass_improves_win_and_avg_vs_baseline | production_adapter_contract_checked | none |
