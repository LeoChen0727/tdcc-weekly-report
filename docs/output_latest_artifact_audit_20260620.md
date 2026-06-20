# output/latest CSV / MD Artifact Audit - 20260620

Scope: classification-only inventory for CSV and Markdown artifacts under `output/latest`, scanned recursively. No CSV/MD artifacts were moved or deleted by this audit.

## Rules Applied

- Root `output/latest` may keep machine-readable latest aliases and pipeline/validator/packet dependencies.
- Human-facing PDFs are outside this CSV/MD audit and are governed by the daily market published reports cleanup PR.
- PDF layout experiments must not be stored in `output/latest`.
- CSV/MD artifacts required by pipeline, validators, packets, manifests, `docs/latest`, or raw-link surfaces remain classified as keep.
- Artifacts owned by TDCC weekly, research/backtest, or individual-stock lanes are marked by `owner_lane` only; this daily PR does not move, delete, or repair them.
- `recommended_action` is restricted to `keep`, `review`, `candidate_for_future_cleanup`, or `unknown`; this audit does not approve deletion.

## Method

- Artifact list: `rg --files output/latest -g *.csv -g *.md`.
- Reference evidence: `rg -F output/latest/` across repo workflow, script, test, doc, config, latest-output, and latest-doc scopes, then parsed for CSV/MD paths. This audit document and the generated inventory CSV were excluded as consumers to avoid self-reference.
- Lineage evidence: report artifact lineage, repo lifecycle inventory, and runtime file lineage contract CSVs.
- Last modified date: newest git log occurrence for each tracked path, using `core.quotePath=false` so non-ASCII paths are compared literally; filesystem mtime is only a fallback for new/untracked paths.
- Full source-level consumer evidence is in the inventory CSV; the Markdown summary intentionally avoids embedding exact workflow references.

## Summary

- Total CSV/MD artifacts inventoried: `7487`
- CSV artifacts: `4928`
- Markdown artifacts: `2559`
- Root-level artifacts: `280`
- Subdirectory artifacts: `7207`
- Tracked in git: `7487`
- Inventory CSV: `config/output_latest_artifact_inventory.csv`

## Classification Counts

| Value | Count |
| --- | ---: |
| `pipeline_necessary` | 30 |
| `validator_necessary` | 11 |
| `packet_manifest_necessary` | 7258 |
| `docs_raw_link_necessary` | 25 |
| `diagnostic_stale_candidate` | 18 |
| `unknown` | 30 |
| `belongs_to_other_lane` | 115 |

## Owner Lane Counts

| Value | Count |
| --- | ---: |
| `daily_production` | 140 |
| `individual_stock` | 7215 |
| `market_risk` | 9 |
| `research_backtest` | 73 |
| `tdcc_weekly` | 42 |
| `warrant` | 8 |

## Recommended Action Counts

| Value | Count |
| --- | ---: |
| `keep` | 7324 |
| `review` | 115 |
| `candidate_for_future_cleanup` | 18 |
| `unknown` | 30 |

## Delete Risk Counts

| Value | Count |
| --- | ---: |
| `high` | 7427 |
| `medium` | 30 |
| `unknown` | 30 |

## Individual-Stock Relocation Update

This PR moves individual-stock report payload artifacts from `output/latest`
root-level scatter paths into the canonical umbrella:

```text
output/latest/individual_stock_reports/
```

Moved or repointed artifact rows:

- `output/latest/individual_stock_chatgpt_packets/` -> `output/latest/individual_stock_reports/chatgpt_packets/`
- `output/latest/individual_stock_price_windows/` -> `output/latest/individual_stock_reports/price_windows/`
- `output/latest/individual_stock_tdcc_windows/` -> `output/latest/individual_stock_reports/tdcc_windows/`
- Root individual-stock index/read-protocol CSV/MD files -> `output/latest/individual_stock_reports/`

Current individual-stock inventory:

- `owner_lane=individual_stock`: `7215`
- Under `output/latest/individual_stock_reports/`: `7207`
- Retained root machine aliases/dependencies: `8`
- Root files whose names still start with `individual_stock`: `2`

Retained root aliases/dependencies:

- `output/latest/individual_stock_technical_snapshot_latest.csv`
- `output/latest/individual_stock_technical_snapshot_latest.md`
- `output/latest/raw_data_fetch_status_latest.csv`
- `output/latest/raw_data_fetch_status_latest.md`
- `output/latest/sell_strategy_performance_latest.csv`
- `output/latest/sell_strategy_performance_latest.md`
- `output/latest/stock_price_history_manifest.csv`
- `output/latest/stock_price_history_manifest.md`

The retained root files are machine-readable pipeline or shared raw-data
dependencies, not per-stock report payloads. They are marked `keep` in
`config/output_latest_artifact_inventory.csv`.

## High-Risk Keep Samples

These rows have direct pipeline, validator, packet/manifest, docs/latest, or raw-link evidence. They should remain in place unless a later PR moves every known consumer first.

| path | classification | owner_lane | delete_risk |
| --- | --- | --- | --- |
| `output/latest/all_candidates_latest.csv` | `validator_necessary` | `daily_production` | `high` |
| `output/latest/all_candidates_latest.md` | `pipeline_necessary` | `daily_production` | `high` |
| `output/latest/astrology_read_protocol_latest.md` | `docs_raw_link_necessary` | `daily_production` | `high` |
| `output/latest/calendar_data_source_status_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/candidate_repeat_appearance_latest.csv` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/candidate_repeat_appearance_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_data_source_status_latest.md` | `pipeline_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_layer_validation_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_needs_review_latest.csv` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_needs_review_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_summary_latest.csv` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/catalyst_summary_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/chatgpt_indicator_usage_guide_latest.md` | `packet_manifest_necessary` | `daily_production` | `high` |
| `output/latest/company_industry_snapshot_latest.csv` | `validator_necessary` | `daily_production` | `high` |
| `output/latest/current_holdings_pattern_latest.csv` | `pipeline_necessary` | `daily_production` | `high` |
| `output/latest/current_holdings_pattern_latest.md` | `pipeline_necessary` | `daily_production` | `high` |
| `output/latest/daily_candidate_frontpage_unique_latest.csv` | `docs_raw_link_necessary` | `daily_production` | `high` |
| `output/latest/daily_candidate_frontpage_unique_latest.md` | `pipeline_necessary` | `daily_production` | `high` |
| `output/latest/daily_candidate_group_rotation_latest.csv` | `docs_raw_link_necessary` | `daily_production` | `high` |
| `output/latest/daily_candidate_group_rotation_latest.md` | `docs_raw_link_necessary` | `daily_production` | `high` |
| `...(+89)` | `` | `` | `` |

## Diagnostic / Stale Candidate Samples

These rows have diagnostic/stale naming evidence but no hard daily-production keep classification in this audit. They are candidates for later lifecycle review only, not deletion in this PR.

| path | owner_lane | recommended_action | delete_risk |
| --- | --- | --- | --- |
| `output/latest/candidate_repeat_appearance_validation_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/chip_flow_source_status_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_candidate_regression_2484_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_candidate_regression_2484_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_candidate_regression_8069_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_candidate_regression_8069_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_data_layer_consistency_audit_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/daily_price_history_continuity_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/repair_daily_price_range_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/repair_daily_price_range_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/repair_one_daily_price_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/revenue_breakout_low_response_debug_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/volume_breakout_buy_signal_evidence_registry_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/volume_breakout_buy_signal_proposal_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/volume_breakout_tdcc_buy_signal_evidence_registry_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/volume_breakout_tdcc_buy_signal_proposal_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.csv` | `daily_production` | `candidate_for_future_cleanup` | `medium` |
| `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.md` | `daily_production` | `candidate_for_future_cleanup` | `medium` |

## Non-Daily Owner Samples

These rows appear to belong to another lane. They are marked for ownership review only; this PR does not cross into those lanes.

| path | owner_lane | classification | recommended_action |
| --- | --- | --- | --- |
| `output/latest/approved_operation_patterns_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/approved_operation_patterns_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_recommendations_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_recommendations_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_research_horizon_detail_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_research_horizon_detail_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_research_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_parameter_research_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_research_parity_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_model_research_parity_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_published_snapshot_ranking_backtest_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_published_snapshot_ranking_backtest_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_short_term_specialty_packet_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_signal_performance_monthly_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_signal_performance_summary_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_signal_performance_summary_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_signal_performance_validation_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_signal_performance_weekly_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_volume_breakout_operation_evidence_audit_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_volume_breakout_operation_section_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/daily_volume_breakout_operation_section_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/explosive_volume_up_backtest_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/explosive_volume_up_backtest_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/explosive_volume_up_position_backtest_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/historical_pattern_operation_registry_latest.csv` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `output/latest/historical_pattern_operation_registry_latest.md` | `research_backtest` | `belongs_to_other_lane` | `review` |
| `...(+88)` | `` | `` | `` |

## Unknown Samples

Unknown rows have no direct consumer evidence and no diagnostic/stale naming signal. They require future lifecycle review before any cleanup. The CSV contains every unknown row; this summary omits retired-surface names to avoid creating new guidance references.

| path | owner_lane | recommended_action | notes |
| --- | --- | --- | --- |
| `output/latest/breakout_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/daily_pattern_watch_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/institutional_investor_flow_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/official_daily_price_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete` |
| `output/latest/official_price_fetch_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/pullback_rebound_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/range_rebound_watch_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/reorganize_output_files_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/revenue_breakout_low_response_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete` |
| `output/latest/revenue_breakout_low_response_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/revenue_industry_applicability_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/revenue_pullback_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/surge_model_score_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/surge_model_score_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/taiwan_vix_latest.csv` | `market_risk` | `unknown` | `classification_only_no_move_no_delete` |
| `output/latest/volume_breakout_buy_signal_best_candidates_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete` |
| `output/latest/volume_breakout_buy_signal_grid_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete` |
| `output/latest/volume_breakout_buy_signal_grid_summary_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_pattern_classification_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_pattern_classification_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_pattern_dimension_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_pattern_dimension_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_tdcc_buy_signal_best_candidates_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_tdcc_buy_signal_grid_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/volume_breakout_tdcc_buy_signal_grid_summary_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/weekly_20pct_surge_volume_events_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/weekly_20pct_surge_volume_hit_rate_latest.csv` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |
| `output/latest/weekly_20pct_surge_volume_hit_rate_latest.md` | `daily_production` | `unknown` | `classification_only_no_move_no_delete;no_rg_or_lineage_consumer_found` |

## Completion Boundary

The original audit was classification-only. The follow-up individual-stock
relocation PR moved/repointed individual-stock report payload artifacts into
`output/latest/individual_stock_reports/` and updated the inventory. It did not
retire, delete, or move TDCC weekly or research/backtest artifacts.
