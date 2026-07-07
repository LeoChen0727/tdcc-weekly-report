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
| baseline_all_dedup | 3136 | 36.93 | 61.29 | 0.5336 | -2.9162 |

## 20/40/60 High-Window Only

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- |
| prev20_high_only | 3136 | 100.0 | 36.93 | 61.29 | 0.5336 | -2.9162 |
| prev40_high_only | 2292 | 73.09 | 37.09 | 61.13 | 0.7682 | -3.0993 |
| prev60_high_only | 1762 | 56.19 | 37.8 | 60.27 | 1.1468 | -3.2976 |

## Low/Base Proxy Rows

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_high_off60_le50_range60_le45 | 1434 | 45.73 | 36.82 | 61.37 | 0.3071 | -2.6152 | weaker_than_baseline_do_not_promote_as_gate |
| prev20_high_off60_le40_range60_le35 | 1029 | 32.81 | 35.08 | 62.78 | -0.0584 | -2.6415 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1066 | 33.99 | 36.96 | 61.07 | 0.4527 | -2.7195 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le40_range60_le35 | 735 | 23.44 | 35.24 | 62.45 | 0.0209 | -2.847 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le50_range60_le45 | 830 | 26.47 | 36.63 | 61.2 | 0.3135 | -2.9692 | weaker_than_baseline_do_not_promote_as_gate |
| prev60_high_off60_le40_range60_le35 | 557 | 17.76 | 33.21 | 64.09 | -0.4249 | -3.4965 | weaker_than_baseline_do_not_promote_as_gate |

## Best Reviewable Source-Signal Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_signal_return_lt_9_8 | 784 | 39.03 | 1.4209 | -2.7374 | mixed_result_research_only |
| prev60_high_not_locked_limit_up | 584 | 38.53 | 1.3475 | -2.4899 | mixed_result_research_only |
| prev40_high_not_locked_limit_up | 820 | 37.93 | 1.3382 | -2.3908 | mixed_result_research_only |
| prev60_high_volume_ratio_2_to_6 | 1356 | 38.72 | 1.3195 | -2.8807 | mixed_result_research_only |
| prev60_high_only | 1762 | 37.8 | 1.1468 | -3.2976 | mixed_result_research_only |
| prev40_high_signal_return_lt_9_8 | 1080 | 37.5 | 1.0777 | -2.6883 | mixed_result_research_only |
| prev20_high_not_locked_limit_up | 1264 | 37.5 | 1.0514 | -2.3362 | mixed_result_research_only |
| prev40_high_volume_ratio_2_to_6 | 1767 | 37.92 | 1.0115 | -2.8139 | mixed_result_research_only |
| prev20_high_signal_return_lt_9_8 | 1588 | 37.03 | 0.8028 | -2.5409 | mixed_result_research_only |
| prev40_high_only | 2292 | 37.09 | 0.7682 | -3.0993 | mixed_result_research_only |
| prev20_high_volume_ratio_2_to_6 | 2450 | 37.27 | 0.7305 | -2.7693 | mixed_result_research_only |
| prev40_high_not_locked_off60_le50_range60_le45 | 443 | 37.02 | 0.7027 | -2.4345 | mixed_result_research_only |
| prev20_high_only | 3136 | 36.93 | 0.5336 | -2.9162 | mixed_result_research_only |
| prev20_high_not_locked_off60_le50_range60_le45 | 660 | 36.36 | 0.4986 | -2.363 | weaker_than_baseline_do_not_promote_as_gate |
| prev40_high_off60_le50_range60_le45 | 1066 | 36.96 | 0.4527 | -2.7195 | weaker_than_baseline_do_not_promote_as_gate |

## Confirmation-Timing Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev60_high_next_day_continuation | 798 | 52.51 | 5.0304 | 1.4049 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_pullback_5ma_or_10ma | 181 | 53.59 | 4.5671 | 0.7979 | mixed_result_research_only |
| prev40_high_next_day_continuation | 1022 | 50.68 | 4.0508 | 0.4626 | interesting_confirmation_timing_needs_contract_review |
| prev60_high_not_locked_next_day_continuation | 204 | 50.0 | 4.0046 | 0.188 | mixed_result_research_only |
| prev40_high_pullback_5ma_or_10ma | 268 | 48.88 | 3.7327 | -0.496 | mixed_result_research_only |
| prev40_high_not_locked_next_day_continuation | 290 | 48.62 | 3.4957 | -0.4859 | mixed_result_research_only |
| prev20_high_next_day_continuation | 1369 | 49.01 | 3.2892 | -0.2169 | mixed_result_research_only |
| prev20_high_pullback_5ma_or_10ma | 407 | 48.89 | 3.2641 | -0.3584 | mixed_result_research_only |
| prev20_high_not_locked_next_day_continuation | 435 | 47.59 | 2.8358 | -0.7812 | mixed_result_research_only |

## Diagnostic-Only Rows

| condition_set_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | candidate_interpretation |
| --- | --- | --- | --- | --- | --- |
| prev20_high_exclude_breakout_failure | 2415 | 47.95 | 2.9707 | -0.5202 | diagnostic_only_not_promotion_evidence |
| prev40_high_exclude_breakout_failure | 1740 | 48.85 | 3.4896 | -0.3023 | diagnostic_only_not_promotion_evidence |
| prev60_high_exclude_breakout_failure | 1317 | 50.57 | 4.2618 | 0.2548 | diagnostic_only_not_promotion_evidence |

## Outputs

- matrix_csv: `output/latest/research_backtest/volume_range_breakout_v2_condition_matrix_latest.csv`
- history_csv: `output/history/research/volume_range_breakout_v2_condition_matrix.csv`
