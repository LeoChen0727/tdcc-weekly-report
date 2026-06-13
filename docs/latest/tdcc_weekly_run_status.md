# TDCC Weekly Run Status

- generated_at: `2026-06-13 18:54:42 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/27464684602
- commit: `6092becc040f964ce05a5990de12547d46cef481`

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
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 481 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 57 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 1095 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 57 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 819 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 27 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 21 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md` | yes | 63 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv` | yes | 41 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.md` | yes | 143 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv` | yes | 121 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 63 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 143 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.pdf` | yes | 299 |
| `output/latest/tdcc_weekly_candidate_full_latest.pdf` | yes | 566 |
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
