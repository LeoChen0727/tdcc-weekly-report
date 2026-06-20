# output/latest CSV / MD Artifact Audit - 20260620

Scope: classification-only audit for CSV and Markdown artifacts under `output/latest`, scanned recursively. No files were moved or deleted.

## Summary

- Total CSV/MD artifacts scanned: `7487`
- Root-level artifacts: `289`
- Subdirectory artifacts: `7198`
- Tracked in git: `7487`
- Inventory CSV: `config/output_latest_artifact_inventory.csv`

## Primary Classification Counts

| Primary classification | Count |
| --- | ---: |
| `pipeline_necessary` | 163 |
| `validator_necessary` | 0 |
| `packet_manifest_necessary` | 7251 |
| `docs_raw_link_necessary` | 0 |
| `diagnostic_stale_candidate` | 40 |
| `unknown` | 33 |

## Category Flag Counts

A file can have multiple category flags when it has more than one kind of evidence.

| Category flag | Count |
| --- | ---: |
| `pipeline_necessary` | 163 |
| `validator_necessary` | 25 |
| `packet_manifest_necessary` | 7361 |
| `docs_raw_link_necessary` | 7370 |
| `diagnostic_stale_candidate` | 40 |
| `unknown` | 33 |

## Largest Directory Groups

| Scope directory | Count |
| --- | ---: |
| `individual_stock_chatgpt_packets` | 2397 |
| `individual_stock_price_windows` | 2397 |
| `individual_stock_tdcc_windows` | 2397 |
| `.` | 289 |
| `individual_stock_reports` | 7 |

## Classification Rules

- `pipeline_necessary`: referenced by workflow/script/config lineage/lifecycle as an input or output.
- `validator_necessary`: referenced by validators or tests, or declared as validator-covered lineage.
- `packet_manifest_necessary`: referenced by packet, manifest, README, or ChatGPT handoff surfaces.
- `docs_raw_link_necessary`: referenced by `docs/latest`, raw-health, publish checks, or raw/API link surfaces.
- `diagnostic_stale_candidate`: no hard dependency found, but filename indicates audit, validation, debug, backtest, proposal, preview, candidate, research, performance, status, repair, evidence, registry, or similar diagnostic/stale surfaces.
- `unknown`: no hard dependency found and no diagnostic/stale naming signal found.

## Cleanup Boundary

This audit is not deletion approval. Artifacts classified as `diagnostic_stale_candidate` or `unknown` must not be manually deleted. A later cleanup PR must update lifecycle evidence before moving, retiring, or deleting any artifact.

## Diagnostic / Stale Candidate Samples

- `output/latest/candidate_repeat_appearance_validation_latest.md`
- `output/latest/chip_flow_source_status_latest.md`
- `output/latest/daily_candidate_regression_2484_latest.csv`
- `output/latest/daily_candidate_regression_2484_latest.md`
- `output/latest/daily_candidate_regression_8069_latest.csv`
- `output/latest/daily_candidate_regression_8069_latest.md`
- `output/latest/daily_data_layer_consistency_audit_latest.md`
- `output/latest/daily_price_history_continuity_latest.md`
- `output/latest/daily_signal_performance_validation_latest.md`
- `output/latest/daily_theme_leadership_validation_latest.md`
- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv`
- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.md`
- `output/latest/historical_pattern_operation_registry_latest.csv`
- `output/latest/historical_pattern_operation_registry_latest.md`
- `output/latest/repair_daily_price_range_latest.csv`
- `output/latest/repair_daily_price_range_latest.md`
- `output/latest/repair_one_daily_price_latest.md`
- `output/latest/revenue_breakout_low_response_debug_latest.md`
- `output/latest/stock_price_history_manifest.md`
- `output/latest/stock_theme_authorized_seed_preview_latest.csv`
- `output/latest/stock_theme_authorized_seed_preview_latest.md`
- `output/latest/tdcc_history_backfill_manifest_latest.csv`
- `output/latest/tdcc_signal_effectiveness_latest.csv`
- `output/latest/volume_attack_theme_layer_validation_latest.md`
- `output/latest/volume_breakout_buy_signal_best_candidates_latest.csv`
- `output/latest/volume_breakout_buy_signal_evidence_registry_latest.csv`
- `output/latest/volume_breakout_buy_signal_grid_latest.csv`
- `output/latest/volume_breakout_buy_signal_grid_summary_latest.md`
- `output/latest/volume_breakout_buy_signal_proposal_latest.md`
- `output/latest/volume_breakout_confirmed_operation_backtest_latest.csv`

## Unknown Samples

- `output/latest/breakout_latest.csv`
- `output/latest/daily_pattern_watch_latest.csv`
- `output/latest/futures_options_call_put_latest.csv`
- `output/latest/futures_options_contracts_latest.csv`
- `output/latest/futures_options_institutional_fo_latest.csv`
- `output/latest/futures_options_put_call_ratio_latest.csv`
- `output/latest/official_price_fetch_latest.md`
- `output/latest/pullback_rebound_latest.csv`
- `output/latest/range_rebound_watch_latest.csv`
- `output/latest/reorganize_output_files_latest.md`
- `output/latest/revenue_breakout_low_response_latest.csv`
- `output/latest/revenue_breakout_low_response_latest.md`
- `output/latest/revenue_industry_applicability_latest.md`
- `output/latest/revenue_pullback_latest.csv`
- `output/latest/surge_model_score_latest.csv`
- `output/latest/surge_model_score_latest.md`
- `output/latest/taiwan_vix_latest.csv`
- `output/latest/volume_breakout_confirmed_operation_rank_latest.md`
- `output/latest/volume_breakout_formal_operation_lifecycle_latest.csv`
- `output/latest/volume_breakout_pattern_classification_latest.csv`
- `output/latest/volume_breakout_pattern_classification_latest.md`
- `output/latest/volume_breakout_pattern_dimension_latest.csv`
- `output/latest/volume_breakout_pattern_dimension_latest.md`
- `output/latest/volume_breakout_pending_operation_queue_latest.md`
- `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.csv`
- `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.md`
- `output/latest/weekly_20pct_surge_volume_events_latest.csv`
- `output/latest/weekly_20pct_surge_volume_hit_rate_latest.csv`
- `output/latest/weekly_20pct_surge_volume_hit_rate_latest.md`
- `output/latest/weekly_surge_5d_avg_volume_comparison_latest.csv`

## Method

The audit scanned tracked repo text references, workflows, validators, tests, `config/report_artifact_lineage.csv`, and `config/repo_file_lifecycle_inventory.csv`. It also searched generated latest/docs surfaces for raw-link and packet references. The full row-level classification is in `config/output_latest_artifact_inventory.csv`.
