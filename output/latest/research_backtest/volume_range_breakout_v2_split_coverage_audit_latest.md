# Volume Range Breakout V2 Split Coverage Audit

- research_id: `volume_range_breakout_v2_split_coverage_audit`
- artifact_version: `volume_range_breakout_v2_split_coverage_audit_20260709`
- source_research_id: `volume_range_breakout_v2_semantic_audit`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- Scope: research-only split coverage on existing v1 source events; this is not a production registry change.
- Rule: every `source_event_key` must be assigned to exactly one split bucket.
- Candidate buckets are mutually exclusive by explicit width/position rules, not by the legacy `consolidation_type` label.

## Split Definitions

- `momentum_breakout_candidate`: 60d breakout, `range_width_40_pct > 40`, and `breakout_over_prev60_pct >= 2`.
- `lowbase_consolidation_candidate`: 60d breakout, `off_120d_low_pct <= 40`, and `range_width_40_pct <= 40`.
- `prev60_residual_research_pool`: 60d breakout but not in the two candidate buckets.
- `legacy_non_prev60_residual`: old v1 source events outside the new 60d breakout direction.

## Detail Coverage

| bucket_id                       |   detail_event_count |
|:--------------------------------|---------------------:|
| legacy_non_prev60_residual      |                 1385 |
| momentum_breakout_candidate     |                  825 |
| prev60_residual_research_pool   |                  707 |
| lowbase_consolidation_candidate |                  273 |

## Same-Stock Non-Overlap Metrics

| bucket_id                       |   source_event_count |   stock_count |   source_coverage_pct |   metric_event_count |   sample_size |   win_rate_pct |   loss_rate_pct |   avg_return_pct |   median_return_pct | split_gate_status        | decision_hint                                                |
|:--------------------------------|---------------------:|--------------:|----------------------:|---------------------:|--------------:|---------------:|----------------:|-----------------:|--------------------:|:-------------------------|:-------------------------------------------------------------|
| legacy_non_prev60_residual      |                 1385 |           789 |                 43.42 |                 1108 |          1108 |          36.55 |           61.82 |          -0.2305 |             -2.425  | fails_return_or_win_gate | low_priority_legacy_baseline_only                            |
| lowbase_consolidation_candidate |                  273 |           224 |                  8.56 |                  241 |           241 |          28.22 |           69.71 |          -1.862  |             -4.2938 | fails_return_or_win_gate | semantic_candidate_but_not_performance_ready                 |
| momentum_breakout_candidate     |                  825 |           388 |                 25.86 |                  539 |           539 |          38.22 |           60.11 |           1.61   |             -3.6514 | fails_return_or_win_gate | primary_v2_candidate_continue_exit_and_raw_producer_research |
| prev60_residual_research_pool   |                  707 |           442 |                 22.16 |                  563 |           563 |          39.96 |           58.08 |           0.8374 |             -2.2222 | fails_return_or_win_gate | research_pool_only_do_feature_audit_before_model_split       |

## Prev60 Residual Reasons

| residual_reason                          |   source_event_count |   stock_count |   source_coverage_pct |   metric_event_count |   win_rate_pct |   loss_rate_pct |   avg_return_pct |   median_return_pct | decision_hint                                          |
|:-----------------------------------------|---------------------:|--------------:|----------------------:|---------------------:|---------------:|----------------:|-----------------:|--------------------:|:-------------------------------------------------------|
| consolidated_but_not_lowbase_off120_gt40 |                  340 |           256 |                 10.66 |                  289 |          38.06 |           59.86 |           0.144  |             -3.6364 | research_pool_only_do_feature_audit_before_model_split |
| consolidated_but_off120_missing          |                  367 |           264 |                 11.5  |                  275 |          41.82 |           56.36 |           1.5524 |             -1.4423 | audit_data_coverage_before_model_discussion            |

## Governance Notes

- The sum of the two candidate buckets is intentionally not required to equal the old v1 source population.
- The residual pool remains research-only until a feature audit proves a separate semantic edge.
- Performance rows are diagnostic; they use current v1 operation returns and must not be treated as promotion evidence.

## Outputs

- summary_csv: `output\latest\research_backtest\volume_range_breakout_v2_split_coverage_audit_latest.csv`
- detail_csv: `output\latest\research_backtest\volume_range_breakout_v2_split_coverage_audit_detail_latest.csv`
- history_summary_csv: `output\history\research\volume_range_breakout_v2_split_coverage_audit.csv`
- history_detail_csv: `output\history\research\volume_range_breakout_v2_split_coverage_audit_detail.csv`
