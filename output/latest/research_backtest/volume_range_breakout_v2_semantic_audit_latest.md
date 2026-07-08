# Volume Range Breakout V2 Semantic Audit

- research_id: `volume_range_breakout_v2_semantic_audit`
- artifact_version: `volume_range_breakout_v2_semantic_audit_20260708`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This is not a production recommendation and does not change `stock_model_contract_registry.csv`.
- Audit goal: compare current `volume_range_breakout` semantics against bottom/base volume attack intent before any v2 promotion.
- Dedupe rule: one underlying trade per stock/signal/confirmation/trigger/entry/exit/entry_price/exit_price, preferring the `no_tdcc` overlay for base semantic analysis.
- Previous-high test: compare current 20-day breakout against stricter 40-day and 60-day previous-high gates on the same deduped formal operation events.
- Guardrail: evidence confluence used for buy ranking must match the source signal classification; the 4989 20260703 legacy locked-limit-up mismatch is recorded as a guard case.

## Overall

| audit_key | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | min_return_pct | max_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_dedup_mature_formal_operations | 3175 | 36.82 | 1.83 | 61.35 | 0.5071 | -2.9091 | -89.8551 | 91.0714 |

## 20/40/60 Previous High

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | value_c |
| --- | --- | --- | --- | --- | --- | --- |
| previous_20d_high | 3175 | 36.82 | 61.35 | 0.5071 | -2.9091 | coverage_pct=100.00 |
| previous_40d_high | 2328 | 36.94 | 61.21 | 0.7292 | -3.094 | coverage_pct=73.32 |
| previous_60d_high | 1795 | 37.6 | 60.45 | 1.0907 | -3.2787 | coverage_pct=56.54 |

## Semantic Slices

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- |
| all_dedup | 3175 | 36.82 | 61.35 | 0.5071 | -2.9091 |
| low_position_60_le_60 | 192 | 29.17 | 68.23 | -1.0615 | -3.2964 |
| low_position_60_le_80 | 415 | 31.57 | 66.51 | -0.9559 | -2.8571 |
| high_position_60_gt_80 | 2191 | 38.16 | 59.97 | 1.1384 | -2.9197 |
| consolidated_any | 1460 | 35.21 | 62.81 | -0.2171 | -2.5007 |
| long_consolidation | 1203 | 34.16 | 63.84 | -0.5438 | -2.6667 |
| short_consolidation | 257 | 40.08 | 57.98 | 1.3122 | -2.0408 |
| non_consolidation | 1715 | 38.19 | 60.12 | 1.1236 | -3.5363 |
| locked_limit_up | 1896 | 36.5 | 61.45 | 0.1912 | -3.6606 |
| not_locked_limit_up | 1279 | 37.29 | 61.22 | 0.9754 | -2.3454 |
| low_position_60_le_80_and_consolidated | 318 | 31.13 | 67.3 | -0.9808 | -2.4289 |
| high_position_60_gt_80_non_consolidation | 1317 | 38.88 | 59.61 | 1.685 | -3.4026 |
| volume_attack_not_locked | 807 | 36.56 | 62.08 | 1.0469 | -2.5281 |

## 4989 Evidence Matching Guard

| audit_key | status | value_a | value_b | value_c |
| --- | --- | --- | --- | --- |
| legacy_locked_limit_up_mismatch | guard_required | source_locked_limit_up_met=False;source_contains_bottom_volume_attack=True | legacy_evidence_confluence_id=locked_limit_up_breakout;legacy_buy_rank_eligible=True | current_included_in_confirmed_or_active=False;current_audit_states=confirmed_unranked_expired |

## Extreme Return Rows

- Extreme rows are marked in the detail artifact with `anomaly_flag`.
- These rows must be reviewed before average return is used as promotion evidence.

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_semantic_audit_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_semantic_audit_detail_latest.csv`
