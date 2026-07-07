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
| all_dedup_mature_formal_operations | 3136 | 36.93 | 1.79 | 61.29 | 0.5336 | -2.9162 | -89.8551 | 91.0714 |

## 20/40/60 Previous High

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | value_c |
| --- | --- | --- | --- | --- | --- | --- |
| previous_20d_high | 3136 | 36.93 | 61.29 | 0.5336 | -2.9162 | coverage_pct=100.00 |
| previous_40d_high | 2292 | 37.09 | 61.13 | 0.7682 | -3.0993 | coverage_pct=73.09 |
| previous_60d_high | 1762 | 37.8 | 60.27 | 1.1468 | -3.2976 | coverage_pct=56.19 |

## Semantic Slices

| audit_key | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- |
| all_dedup | 3136 | 36.93 | 61.29 | 0.5336 | -2.9162 |
| low_position_60_le_60 | 191 | 28.8 | 68.59 | -1.1088 | -3.3473 |
| low_position_60_le_80 | 413 | 31.48 | 66.59 | -0.9669 | -2.8571 |
| high_position_60_gt_80 | 2154 | 38.35 | 59.84 | 1.1886 | -2.9576 |
| consolidated_any | 1449 | 34.99 | 63.01 | -0.2359 | -2.5641 |
| long_consolidation | 1194 | 34.0 | 63.99 | -0.5599 | -2.6924 |
| short_consolidation | 255 | 39.61 | 58.43 | 1.2811 | -2.0619 |
| non_consolidation | 1687 | 38.59 | 59.81 | 1.1946 | -3.5124 |
| locked_limit_up | 1872 | 36.54 | 61.49 | 0.184 | -3.6831 |
| not_locked_limit_up | 1264 | 37.5 | 61.0 | 1.0514 | -2.3362 |
| low_position_60_le_80_and_consolidated | 317 | 30.91 | 67.51 | -1.0091 | -2.432 |
| high_position_60_gt_80_non_consolidation | 1290 | 39.38 | 59.22 | 1.7846 | -3.3601 |
| volume_attack_not_locked | 803 | 36.74 | 61.89 | 1.0937 | -2.4518 |

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
