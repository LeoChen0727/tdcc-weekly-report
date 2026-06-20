# Research Backtest Artifact Relocation Plan - 2026-06-21

- source_inventory: `production/tdcc-daily-production/config/output_latest_artifact_inventory.csv`
- filter: `owner_lane=research_backtest`
- artifact_count: `73`
- relocated_now: `14`
- compatibility_alias_retained: `59`
- target_container: `output/latest/research_backtest/`
- boundary: advisory research remains advisory; no daily production baseline, ranking, buy/sell logic, TDCC weekly, individual_stock, or daily market PDF artifact is changed.

## Relocated In This PR

| original_path | target_path |
| --- | --- |
| `output/latest/daily_model_research_parity_latest.csv` | `output/latest/research_backtest/daily_model_research_parity_latest.csv` |
| `output/latest/daily_model_research_parity_latest.md` | `output/latest/research_backtest/daily_model_research_parity_latest.md` |
| `output/latest/daily_published_snapshot_ranking_backtest_latest.csv` | `output/latest/research_backtest/daily_published_snapshot_ranking_backtest_latest.csv` |
| `output/latest/daily_published_snapshot_ranking_backtest_latest.md` | `output/latest/research_backtest/daily_published_snapshot_ranking_backtest_latest.md` |
| `output/latest/daily_signal_performance_validation_latest.md` | `output/latest/research_backtest/daily_signal_performance_validation_latest.md` |
| `output/latest/volume_breakout_confirmed_operation_backtest_latest.csv` | `output/latest/research_backtest/volume_breakout_confirmed_operation_backtest_latest.csv` |
| `output/latest/volume_breakout_confirmed_operation_backtest_latest.md` | `output/latest/research_backtest/volume_breakout_confirmed_operation_backtest_latest.md` |
| `output/latest/volume_breakout_tdcc_confluence_backtest_latest.csv` | `output/latest/research_backtest/volume_breakout_tdcc_confluence_backtest_latest.csv` |
| `output/latest/volume_breakout_tdcc_confluence_backtest_latest.md` | `output/latest/research_backtest/volume_breakout_tdcc_confluence_backtest_latest.md` |
| `output/latest/weekly_surge_5d_avg_volume_comparison_latest.csv` | `output/latest/research_backtest/weekly_surge_5d_avg_volume_comparison_latest.csv` |
| `output/latest/weekly_surge_5d_avg_volume_comparison_latest.md` | `output/latest/research_backtest/weekly_surge_5d_avg_volume_comparison_latest.md` |
| `output/latest/weekly_surge_next_open_hit_rate_latest.csv` | `output/latest/research_backtest/weekly_surge_next_open_hit_rate_latest.csv` |
| `output/latest/weekly_surge_next_open_hit_rate_latest.md` | `output/latest/research_backtest/weekly_surge_next_open_hit_rate_latest.md` |
| `output/latest/weekly_surge_strict_parameter_search_all_rules_latest.csv` | `output/latest/research_backtest/weekly_surge_strict_parameter_search_all_rules_latest.csv` |

## Compatibility Aliases Retained

| alias_path | planned_target | reason |
| --- | --- | --- |
| `output/latest/approved_operation_patterns_latest.csv` | `output/latest/research_backtest/approved_operation_patterns_latest.csv` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/approved_operation_patterns_latest.md` | `output/latest/research_backtest/approved_operation_patterns_latest.md` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/daily_model_parameter_recommendations_latest.csv` | `output/latest/research_backtest/daily_model_parameter_recommendations_latest.csv` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_model_parameter_recommendations_latest.md` | `output/latest/research_backtest/daily_model_parameter_recommendations_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_model_parameter_research_horizon_detail_latest.csv` | `output/latest/research_backtest/daily_model_parameter_research_horizon_detail_latest.csv` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_model_parameter_research_horizon_detail_latest.md` | `output/latest/research_backtest/daily_model_parameter_research_horizon_detail_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_model_parameter_research_latest.csv` | `output/latest/research_backtest/daily_model_parameter_research_latest.csv` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_model_parameter_research_latest.md` | `output/latest/research_backtest/daily_model_parameter_research_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_short_term_specialty_packet_latest.md` | `output/latest/research_backtest/daily_short_term_specialty_packet_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_signal_performance_monthly_latest.md` | `output/latest/research_backtest/daily_signal_performance_monthly_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_signal_performance_summary_latest.csv` | `output/latest/research_backtest/daily_signal_performance_summary_latest.csv` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_signal_performance_summary_latest.md` | `output/latest/research_backtest/daily_signal_performance_summary_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_signal_performance_weekly_latest.md` | `output/latest/research_backtest/daily_signal_performance_weekly_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv` | `output/latest/research_backtest/daily_volume_breakout_operation_evidence_audit_latest.csv` | daily adapter audit contract and validator still reference root path |
| `output/latest/daily_volume_breakout_operation_evidence_audit_latest.md` | `output/latest/research_backtest/daily_volume_breakout_operation_evidence_audit_latest.md` | daily adapter audit contract and validator still reference root path |
| `output/latest/daily_volume_breakout_operation_section_latest.csv` | `output/latest/research_backtest/daily_volume_breakout_operation_section_latest.csv` | daily PDF renderer and published snapshot contract still read this adapter artifact from root |
| `output/latest/daily_volume_breakout_operation_section_latest.md` | `output/latest/research_backtest/daily_volume_breakout_operation_section_latest.md` | daily PDF renderer and published snapshot contract still read this adapter artifact from root |
| `output/latest/explosive_volume_up_backtest_latest.csv` | `output/latest/research_backtest/explosive_volume_up_backtest_latest.csv` | active source reference remains: docs |
| `output/latest/explosive_volume_up_backtest_latest.md` | `output/latest/research_backtest/explosive_volume_up_backtest_latest.md` | active source reference remains: docs |
| `output/latest/explosive_volume_up_position_backtest_latest.csv` | `output/latest/research_backtest/explosive_volume_up_position_backtest_latest.csv` | active source reference remains: docs |
| `output/latest/historical_pattern_operation_registry_latest.csv` | `output/latest/research_backtest/historical_pattern_operation_registry_latest.csv` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/historical_pattern_operation_registry_latest.md` | `output/latest/research_backtest/historical_pattern_operation_registry_latest.md` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/market_timing_backtest_latest.csv` | `output/latest/research_backtest/market_timing_backtest_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/market_timing_backtest_latest.md` | `output/latest/research_backtest/market_timing_backtest_latest.md` | active source reference remains: docs |
| `output/latest/market_timing_composite_backtest_latest.csv` | `output/latest/research_backtest/market_timing_composite_backtest_latest.csv` | active source reference remains: docs |
| `output/latest/market_timing_composite_backtest_latest.md` | `output/latest/research_backtest/market_timing_composite_backtest_latest.md` | active source reference remains: docs |
| `output/latest/model_operation_readiness_latest.csv` | `output/latest/research_backtest/model_operation_readiness_latest.csv` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/model_operation_readiness_latest.md` | `output/latest/research_backtest/model_operation_readiness_latest.md` | daily README/packet/indicator guide currently publishes or reads this advisory surface as a fixed alias |
| `output/latest/msci_taiwan_rebalance_backtest_latest.csv` | `output/latest/research_backtest/msci_taiwan_rebalance_backtest_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/msci_taiwan_rebalance_backtest_latest.md` | `output/latest/research_backtest/msci_taiwan_rebalance_backtest_latest.md` | active source reference remains: docs |
| `output/latest/signal_performance_latest.md` | `output/latest/research_backtest/signal_performance_latest.md` | active source reference remains: workflows |
| `output/latest/surge_model_backtest_latest.csv` | `output/latest/research_backtest/surge_model_backtest_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/surge_model_backtest_latest.md` | `output/latest/research_backtest/surge_model_backtest_latest.md` | active source reference remains: docs |
| `output/latest/surge_precondition_candidates_latest.csv` | `output/latest/research_backtest/surge_precondition_candidates_latest.csv` | active source reference remains: scripts,workflows,docs |
| `output/latest/surge_precondition_candidates_latest.md` | `output/latest/research_backtest/surge_precondition_candidates_latest.md` | active source reference remains: workflows,docs |
| `output/latest/volume_breakout_backtest_latest.csv` | `output/latest/research_backtest/volume_breakout_backtest_latest.csv` | active source reference remains: docs |
| `output/latest/volume_breakout_backtest_latest.md` | `output/latest/research_backtest/volume_breakout_backtest_latest.md` | active source reference remains: docs |
| `output/latest/volume_breakout_confirmed_operation_rank_latest.csv` | `output/latest/research_backtest/volume_breakout_confirmed_operation_rank_latest.csv` | active source reference remains: docs |
| `output/latest/volume_breakout_confirmed_operation_rank_latest.md` | `output/latest/research_backtest/volume_breakout_confirmed_operation_rank_latest.md` | not moved in first low-risk PR; retained for compatibility until producer/consumer is separately redirected |
| `output/latest/volume_breakout_formal_operation_backtest_latest.csv` | `output/latest/research_backtest/volume_breakout_formal_operation_backtest_latest.csv` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/volume_breakout_formal_operation_backtest_latest.md` | `output/latest/research_backtest/volume_breakout_formal_operation_backtest_latest.md` | daily volume breakout adapter/validator still consumes this research-owned support artifact |
| `output/latest/volume_breakout_formal_operation_lifecycle_latest.csv` | `output/latest/research_backtest/volume_breakout_formal_operation_lifecycle_latest.csv` | active source reference remains: docs |
| `output/latest/volume_breakout_operation_pdf_preview_latest.csv` | `output/latest/research_backtest/volume_breakout_operation_pdf_preview_latest.csv` | active source reference remains: docs |
| `output/latest/volume_breakout_operation_pdf_preview_latest.md` | `output/latest/research_backtest/volume_breakout_operation_pdf_preview_latest.md` | active source reference remains: docs |
| `output/latest/volume_breakout_pending_operation_queue_latest.csv` | `output/latest/research_backtest/volume_breakout_pending_operation_queue_latest.csv` | active source reference remains: docs |
| `output/latest/volume_breakout_pending_operation_queue_latest.md` | `output/latest/research_backtest/volume_breakout_pending_operation_queue_latest.md` | not moved in first low-risk PR; retained for compatibility until producer/consumer is separately redirected |
| `output/latest/warrant_signal_performance_latest.md` | `output/latest/research_backtest/warrant_signal_performance_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_multifactor_candidates_latest.csv` | `output/latest/research_backtest/weekly_surge_multifactor_candidates_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/weekly_surge_multifactor_candidates_latest.md` | `output/latest/research_backtest/weekly_surge_multifactor_candidates_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_multifactor_filter_grid_latest.csv` | `output/latest/research_backtest/weekly_surge_multifactor_filter_grid_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/weekly_surge_multifactor_filter_grid_latest.md` | `output/latest/research_backtest/weekly_surge_multifactor_filter_grid_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_strict_parameter_candidates_latest.csv` | `output/latest/research_backtest/weekly_surge_strict_parameter_candidates_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/weekly_surge_strict_parameter_candidates_latest.md` | `output/latest/research_backtest/weekly_surge_strict_parameter_candidates_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_strict_parameter_search_latest.csv` | `output/latest/research_backtest/weekly_surge_strict_parameter_search_latest.csv` | active source reference remains: scripts,validators,docs |
| `output/latest/weekly_surge_strict_parameter_search_latest.md` | `output/latest/research_backtest/weekly_surge_strict_parameter_search_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_technical_filter_grid_latest.csv` | `output/latest/research_backtest/weekly_surge_technical_filter_grid_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/weekly_surge_technical_filter_grid_latest.md` | `output/latest/research_backtest/weekly_surge_technical_filter_grid_latest.md` | active source reference remains: docs |
| `output/latest/weekly_surge_theme_segment_next_open_latest.csv` | `output/latest/research_backtest/weekly_surge_theme_segment_next_open_latest.csv` | active source reference remains: scripts,docs |
| `output/latest/weekly_surge_theme_segment_next_open_latest.md` | `output/latest/research_backtest/weekly_surge_theme_segment_next_open_latest.md` | active source reference remains: docs |

## Full Machine-Readable Plan

- `docs/research_backtest_artifact_relocation_plan_20260621.csv`
