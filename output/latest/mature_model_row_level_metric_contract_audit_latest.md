# Mature Model Row-Level Metric Contract Audit

- audit_id: `mature_model_row_level_metric_contract_audit_20260711`
- audit_version: `v2`
- generated_at: `2026-08-28 20:59:29 Asia/Taipei`

## Contract

- Single add-score item may use the approved single-item metric.
- Multi-item add-score combinations must use the exact recomputed combination metric.
- A promoted exact combination may be used only when it is not worse than the best matching single item on win rate, average return, and median return; otherwise use that best single item.
- Daily row-level comparisons against the whole-model baseline remain fully reported as advisory evidence and must not block production publication; malformed metrics, schema/source/lineage conflicts, and baseline substitution still fail closed.
- Whole-model baseline performance is header-only and must never substitute for a stock-row add-score metric.
- PDF and packet operation rows must consume only adapter `row_metric_*` fields.
- Research-only combo rows must remain unavailable to PDF operation rows until a model-specific promotion PR wires an approved adapter metric.

## Findings

- Mature operation stock rows audited: `508`.
- Unique stock lifecycle rows after removing highlight/full view duplication: `254`.
- Ready row-level metrics: `240`; explicit unavailable rows: `268`.
- Invalid row metrics: `0`; baseline misuse rows: `0`; duplicate adapter keys: `0`.
- W-bottom, W-bottom neckline, low-position volume attack, and mid-position momentum score components remain ranking-only until same-basis performance packages are promoted.
- PDF layout integration remains pending; this artifact validates the model-owned adapter contract and does not claim final PDF rendering completion.

## Audit Rows

| scope | model_id | consumer rows | unique stock lifecycle | ready | unavailable | metric_scope | row_level_metric_status | combo_policy | production_readiness | issues |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| mature_model | `volume_range_breakout_v2_low_position_volume_attack` | 16 | 8 | 0 | 16 | no_current_formal_row_metric | pass_explicit_unavailable_no_baseline_substitution | not_available_unvalidated_ranking_score_components / not_applicable_no_approved_combo_metric | adapter_contract_ready_pdf_packet_consumers_integrated | none |
| mature_model | `volume_range_breakout_v2_mid_position_momentum_attack` | 16 | 8 | 0 | 16 | no_current_formal_row_metric | pass_explicit_unavailable_no_baseline_substitution | not_available_unvalidated_ranking_score_components / not_applicable_no_approved_combo_metric | adapter_contract_ready_pdf_packet_consumers_integrated | none |
| mature_model | `volume_range_breakout_v2_high_position_volume_attack` | 12 | 6 | 10 | 2 | exact_combo|single_add_score | pass_ready_rows_use_formal_row_metric | pass_exact_recomputed_combo_metrics_match_research_source / pass_exact_combo_or_best_single_fallback_policy | adapter_contract_ready_pdf_packet_consumers_integrated | none |
| mature_model | `w_bottom_right_side` | 18 | 9 | 0 | 18 | no_current_formal_row_metric | pass_explicit_unavailable_no_baseline_substitution | not_available_unvalidated_ranking_score_components / not_applicable_no_approved_combo_metric | adapter_contract_ready_pdf_packet_consumers_integrated | none |
| mature_model | `neckline_volume_breakout_confirmation` | 0 | 0 | 0 | 0 | no_current_formal_row_metric | pass_explicit_unavailable_no_baseline_substitution | not_available_unvalidated_ranking_score_components / not_applicable_no_approved_combo_metric | adapter_contract_ready_pdf_packet_consumers_integrated | none |
| mature_model | `price_pullback_23ema` | 446 | 223 | 230 | 216 | exact_combo | pass_ready_rows_use_formal_row_metric | pass_exact_package_metric_required_for_multi_feature_technical_strength / pass_improves_win_and_avg_vs_baseline | adapter_contract_ready_pdf_packet_consumers_integrated | none |
