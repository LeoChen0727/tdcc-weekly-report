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
| baseline_all_dedup | 3190 | 36.71 | 61.47 | 0.4751 | -2.9175 |

## 20/40/60 High-Window Only

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- |
| prev20_high_only | 3190 | 100.0 | 36.71 | 61.47 | 0.4751 | -2.9175 |
| prev40_high_only | 2341 | 73.39 | 36.78 | 61.38 | 0.6769 | -3.1385 |
| prev60_high_only | 1805 | 56.58 | 37.45 | 60.61 | 1.0383 | -3.3033 |

## Low/Base Proxy Rows

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_high_off60_le50_range60_le45 | 1456 | 45.64 | 36.88 | 61.33 | 0.2847 | -2.5977 | weaker_than_baseline_do_not_promote_as_gate |
| prev20_high_off60_le40_range60_le35 | 1044 | 32.73 | 35.34 | 62.55 | -0.0389 | -2.6025 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1086 | 34.04 | 37.02 | 61.05 | 0.4037 | -2.7195 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le40_range60_le35 | 748 | 23.45 | 35.56 | 62.17 | 0.0221 | -2.7686 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le50_range60_le45 | 846 | 26.52 | 36.76 | 61.11 | 0.2842 | -2.9576 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le40_range60_le35 | 567 | 17.77 | 33.69 | 63.67 | -0.398 | -3.3099 | weaker_than_baseline_do_not_promote_as_gate |

## Best Reviewable Source-Signal Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_signal_return_lt_9_8 | 804 | 38.43 | 1.2296 | -2.7482 | mixed_result_research_only |
| prev40_high_not_locked_limit_up | 837 | 37.51 | 1.1905 | -2.4155 | mixed_result_research_only |
| prev60_high_volume_ratio_2_to_6 | 1386 | 38.31 | 1.1896 | -2.9162 | mixed_result_research_only |
| prev60_high_not_locked_limit_up | 600 | 37.83 | 1.1352 | -2.6366 | mixed_result_research_only |
| prev60_high_only | 1805 | 37.45 | 1.0383 | -3.3033 | mixed_result_research_only |
| prev20_high_not_locked_limit_up | 1284 | 37.23 | 0.9695 | -2.344 | mixed_result_research_only |
| prev40_high_signal_return_lt_9_8 | 1102 | 37.11 | 0.9337 | -2.7322 | mixed_result_research_only |
| prev40_high_volume_ratio_2_to_6 | 1801 | 37.59 | 0.9103 | -2.8526 | mixed_result_research_only |
| prev20_high_signal_return_lt_9_8 | 1614 | 36.8 | 0.7216 | -2.5409 | mixed_result_research_only |
| prev40_high_only | 2341 | 36.78 | 0.6769 | -3.1385 | mixed_result_research_only |
| prev20_high_volume_ratio_2_to_6 | 2489 | 37.04 | 0.667 | -2.7842 | mixed_result_research_only |
| prev40_high_not_locked_off60_le50_range60_le45 | 451 | 37.03 | 0.6147 | -2.4345 | mixed_result_research_only |
| prev20_high_only | 3190 | 36.71 | 0.4751 | -2.9175 | mixed_result_research_only |
| prev20_high_not_locked_off60_le50_range60_le45 | 670 | 36.42 | 0.4677 | -2.363 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1086 | 37.02 | 0.4037 | -2.7195 | weaker_than_baseline_do_not_promote_as_gate |

## Confirmation-Timing Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_next_day_continuation | 811 | 52.4 | 4.9629 | 1.3359 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_pullback_5ma_or_10ma | 185 | 52.43 | 4.3914 | 0.7528 | mixed_result_research_only |
| prev40_high_next_day_continuation | 1037 | 50.63 | 3.9997 | 0.4292 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_not_locked_next_day_continuation | 209 | 49.28 | 3.6293 | -0.4515 | mixed_result_research_only |
| prev40_high_pullback_5ma_or_10ma | 273 | 47.99 | 3.5865 | -0.7472 | mixed_result_research_only |
| prev20_high_next_day_continuation | 1385 | 49.03 | 3.2626 | -0.2169 | mixed_result_research_only |
| prev40_high_not_locked_next_day_continuation | 296 | 48.31 | 3.2443 | -0.5399 | mixed_result_research_only |
| prev20_high_pullback_5ma_or_10ma | 413 | 48.18 | 3.1614 | -0.4815 | mixed_result_research_only |
| prev20_high_not_locked_next_day_continuation | 441 | 47.39 | 2.676 | -0.7937 | mixed_result_research_only |

## Diagnostic-Only Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev20_high_exclude_breakout_failure | 2446 | 47.87 | 2.9271 | -0.5639 | diagnostic_only_not_promotion_evidence |
| prev40_high_exclude_breakout_failure | 1768 | 48.7 | 3.4111 | -0.314 | diagnostic_only_not_promotion_evidence |
| prev60_high_exclude_breakout_failure | 1341 | 50.41 | 4.1662 | 0.2273 | diagnostic_only_not_promotion_evidence |

## Outputs

- matrix_csv: `output/latest/research_backtest/volume_range_breakout_v2_condition_matrix_latest.csv`
- history_csv: `output/history/research/volume_range_breakout_v2_condition_matrix.csv`
