# TDCC Weekly Run Status

- generated_at: `2026-07-11 15:43:52 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/29144792887
- commit: `fe14ca42eb2d78994d208c1a2936c747d7edc930`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_invalid_holder_distribution_latest.csv` | yes | 1 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 501 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 106 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 167 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 297 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 62 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 134 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 106 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 79 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 61 |
| `output/latest/tdcc_overheated_short_term_edge_latest.md` | yes | 69 |
| `output/latest/tdcc_overheated_short_term_edge_latest.csv` | yes | 7 |
| `output/latest/tdcc_overheated_short_term_edge_candidates_latest.csv` | yes | 34 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 487 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 59 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 396 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 28 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 20 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 31 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 23 |
| `output/latest/tdcc_weekly_report_section_manifest_latest.csv` | yes | 5 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md` | yes | 57 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv` | yes | 33 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.md` | yes | 116 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv` | yes | 92 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 57 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 116 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.pdf` | yes | 889 |
| `output/latest/tdcc_weekly_candidate_full_latest.pdf` | yes | 1328 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260618.pdf` | yes | 780 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260626.pdf` | yes | 1243 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260703.pdf` | yes | 1328 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260618.pdf` | yes | 590 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260626.pdf` | yes | 954 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260703.pdf` | yes | 889 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.md` | yes | 60 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.json` | yes | 107 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.md` | yes | 14 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.json` | yes | 5 |
| `output/history/tdcc_signals/tdcc_signal_log.csv` | yes | 806 |
| `output/history/tdcc_signals/tdcc_signal_performance.csv` | yes | 806 |
| `output/history/tdcc_signals/tdcc_signal_snapshot.csv` | yes | 11579 |
| `output/history/tdcc_signals/tdcc_normalized_signal_log.csv` | yes | 11579 |
| `output/history/tdcc_signals/theme_breadth_history.csv` | yes | 109 |
| `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv` | yes | 7979 |
| `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` | yes | 73 |

## Notes

- Normalized signal files dedupe by one stock per TDCC week.
- ABM ranking is separated from TDCC strength ranking.
- TDCC performance/effectiveness backtests are maintained by research_backtest_pipeline.yml.
- Pending D+N performance is not treated as positive or negative.
