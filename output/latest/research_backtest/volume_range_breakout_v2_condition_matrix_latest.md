# Volume Range Breakout V2 Condition Matrix

- research_id: `volume_range_breakout_v2_condition_matrix`
- artifact_version: `volume_range_breakout_v2_condition_matrix_20260708`
- source_research_id: `volume_range_breakout_v2_semantic_audit`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This matrix is research-only and does not change `stock_model_contract_registry.csv`.
- The matrix consumes the semantic-audit detail artifact; it is not a full raw-market producer rerun.
- 20/40/60 previous-high windows are compared under the same deduped sample and operation return basis.
- Low/base proxies are tested as evidence, not assumed to be correct gates.
- Confirmation-timing and diagnostic rows require operation-contract review before any promotion discussion.

## Baseline

| condition_set_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- |
| baseline_all_dedup | 3175 | 36.82 | 61.35 | 0.5071 | -2.9091 |

## 20/40/60 High-Window Only

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- |
| prev20_high_only | 3175 | 100.0 | 36.82 | 61.35 | 0.5071 | -2.9091 |
| prev40_high_only | 2328 | 73.32 | 36.94 | 61.21 | 0.7292 | -3.094 |
| prev60_high_only | 1795 | 56.54 | 37.6 | 60.45 | 1.0907 | -3.2787 |

## Low/Base Proxy Rows

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_high_off60_le50_range60_le45 | 1447 | 45.57 | 36.97 | 61.23 | 0.3044 | -2.583 | weaker_than_baseline_do_not_promote_as_gate |
| prev20_high_off60_le40_range60_le35 | 1038 | 32.69 | 35.36 | 62.52 | -0.0406 | -2.6025 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1079 | 33.98 | 37.16 | 60.89 | 0.4473 | -2.682 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le40_range60_le35 | 744 | 23.43 | 35.62 | 62.1 | 0.0448 | -2.7511 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le50_range60_le45 | 842 | 26.52 | 36.82 | 61.05 | 0.3032 | -2.9329 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le40_range60_le35 | 565 | 17.8 | 33.63 | 63.72 | -0.3958 | -3.3099 | weaker_than_baseline_do_not_promote_as_gate |

## Best Reviewable Source-Signal Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_signal_return_lt_9_8 | 799 | 38.67 | 1.2913 | -2.7397 | mixed_result_research_only |
| prev60_high_volume_ratio_2_to_6 | 1377 | 38.49 | 1.2393 | -2.8889 | mixed_result_research_only |
| prev40_high_not_locked_limit_up | 834 | 37.65 | 1.22 | -2.4126 | mixed_result_research_only |
| prev60_high_not_locked_limit_up | 597 | 38.02 | 1.1762 | -2.6316 | mixed_result_research_only |
| prev60_high_only | 1795 | 37.6 | 1.0907 | -3.2787 | mixed_result_research_only |
| prev40_high_signal_return_lt_9_8 | 1096 | 37.32 | 0.9914 | -2.6883 | mixed_result_research_only |
| prev20_high_not_locked_limit_up | 1279 | 37.29 | 0.9754 | -2.3454 | mixed_result_research_only |
| prev40_high_volume_ratio_2_to_6 | 1791 | 37.74 | 0.9516 | -2.8139 | mixed_result_research_only |
| prev20_high_signal_return_lt_9_8 | 1606 | 36.92 | 0.7497 | -2.4964 | mixed_result_research_only |
| prev40_high_only | 2328 | 36.94 | 0.7292 | -3.094 | mixed_result_research_only |
| prev20_high_volume_ratio_2_to_6 | 2477 | 37.14 | 0.689 | -2.7638 | mixed_result_research_only |
| prev40_high_not_locked_off60_le50_range60_le45 | 450 | 37.11 | 0.6407 | -2.4221 | mixed_result_research_only |
| prev20_high_only | 3175 | 36.82 | 0.5071 | -2.9091 | mixed_result_research_only |
| prev20_high_not_locked_off60_le50_range60_le45 | 667 | 36.43 | 0.4589 | -2.3675 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1079 | 37.16 | 0.4473 | -2.682 | weaker_than_baseline_do_not_promote_as_gate |

## Confirmation-Timing Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_next_day_continuation | 808 | 52.48 | 4.9893 | 1.3482 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_pullback_5ma_or_10ma | 183 | 53.01 | 4.4937 | 0.7828 | mixed_result_research_only |
| prev40_high_next_day_continuation | 1033 | 50.73 | 4.029 | 0.4959 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_not_locked_next_day_continuation | 208 | 49.52 | 3.7001 | -0.2258 | mixed_result_research_only |
| prev40_high_pullback_5ma_or_10ma | 270 | 48.52 | 3.6891 | -0.5432 | mixed_result_research_only |
| prev40_high_not_locked_next_day_continuation | 295 | 48.47 | 3.2929 | -0.5202 | mixed_result_research_only |
| prev20_high_next_day_continuation | 1381 | 49.09 | 3.2824 | -0.2002 | mixed_result_research_only |
| prev20_high_pullback_5ma_or_10ma | 409 | 48.66 | 3.2376 | -0.3636 | mixed_result_research_only |
| prev20_high_not_locked_next_day_continuation | 440 | 47.5 | 2.7073 | -0.7874 | mixed_result_research_only |

## Diagnostic-Only Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev20_high_exclude_breakout_failure | 2435 | 48.01 | 2.959 | -0.5181 | diagnostic_only_not_promotion_evidence |
| prev40_high_exclude_breakout_failure | 1759 | 48.89 | 3.4649 | -0.3006 | diagnostic_only_not_promotion_evidence |
| prev60_high_exclude_breakout_failure | 1334 | 50.6 | 4.2248 | 0.2702 | diagnostic_only_not_promotion_evidence |

## Outputs

- matrix_csv: `output/latest/research_backtest/volume_range_breakout_v2_condition_matrix_latest.csv`
- history_csv: `output/history/research/volume_range_breakout_v2_condition_matrix.csv`
