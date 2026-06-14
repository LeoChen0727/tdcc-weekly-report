# TDCC Weekly Run Status

- generated_at: `2026-06-14 20:49:36 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/27499246086
- commit: `0afe050ca2326844a53f51fdb949d592359aed61`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 501 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 104 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 165 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 266 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 43 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 32 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 131 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 103 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 79 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 61 |
| `output/latest/tdcc_overheated_short_term_edge_latest.md` | yes | 61 |
| `output/latest/tdcc_overheated_short_term_edge_latest.csv` | yes | 7 |
| `output/latest/tdcc_overheated_short_term_edge_candidates_latest.csv` | yes | 26 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 483 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 59 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 417 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 35 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 27 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 25 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 17 |
| `output/latest/tdcc_weekly_report_section_manifest_latest.csv` | yes | 5 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md` | yes | 56 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv` | yes | 32 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.md` | yes | 117 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv` | yes | 93 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 56 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 117 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.pdf` | yes | 241 |
| `output/latest/tdcc_weekly_candidate_full_latest.pdf` | yes | 451 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.md` | yes | 43 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.json` | yes | 69 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.md` | yes | 14 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.json` | yes | 5 |
| `output/history/tdcc_signals/tdcc_signal_log.csv` | yes | 501 |
| `output/history/tdcc_signals/tdcc_signal_performance.csv` | yes | 501 |
| `output/history/tdcc_signals/tdcc_signal_snapshot.csv` | yes | 8237 |
| `output/history/tdcc_signals/tdcc_normalized_signal_log.csv` | yes | 8237 |
| `output/history/tdcc_signals/theme_breadth_history.csv` | yes | 83 |
| `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv` | yes | 4637 |
| `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` | yes | 37 |

## Notes

- Normalized signal files dedupe by one stock per TDCC week.
- ABM ranking is separated from TDCC strength ranking.
- TDCC performance/effectiveness backtests are maintained by research_backtest_pipeline.yml.
- Pending D+N performance is not treated as positive or negative.
