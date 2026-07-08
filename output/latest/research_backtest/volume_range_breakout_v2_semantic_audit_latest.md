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
| all_dedup_mature_formal_operations | 3190 | 36.71 | 1.82 | 61.47 | 0.4751 | -2.9175 | -89.8551 | 91.0714 |

## 20/40/60 Previous High

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | value_c |
| --- | --- | --- | --- | --- | --- | --- |
| previous_20d_high | 3190 | 36.71 | 61.47 | 0.4751 | -2.9175 | coverage_pct=100.00 |
| previous_40d_high | 2341 | 36.78 | 61.38 | 0.6769 | -3.1385 | coverage_pct=73.39 |
| previous_60d_high | 1805 | 37.45 | 60.61 | 1.0383 | -3.3033 | coverage_pct=56.58 |

## Semantic Slices

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- |
| all_dedup | 3190 | 36.71 | 61.47 | 0.4751 | -2.9175 |
| low_position_60_le_60 | 192 | 29.17 | 68.23 | -1.0615 | -3.2964 |
| low_position_60_le_80 | 415 | 31.57 | 66.51 | -0.9559 | -2.8571 |
| high_position_60_gt_80 | 2206 | 37.99 | 60.15 | 1.0878 | -2.9696 |
| consolidated_any | 1464 | 35.18 | 62.84 | -0.2141 | -2.5007 |
| long_consolidation | 1207 | 34.13 | 63.88 | -0.5391 | -2.6667 |
| short_consolidation | 257 | 40.08 | 57.98 | 1.3122 | -2.0408 |
| non_consolidation | 1726 | 38.01 | 60.31 | 1.0596 | -3.5915 |
| locked_limit_up | 1906 | 36.36 | 61.59 | 0.142 | -3.7037 |
| not_locked_limit_up | 1284 | 37.23 | 61.29 | 0.9695 | -2.344 |
| low_position_60_le_80_and_consolidated | 318 | 31.13 | 67.3 | -0.9808 | -2.4289 |
| high_position_60_gt_80_non_consolidation | 1328 | 38.63 | 59.86 | 1.5972 | -3.5363 |
| volume_attack_not_locked | 811 | 36.5 | 62.15 | 1.0413 | -2.5281 |

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
