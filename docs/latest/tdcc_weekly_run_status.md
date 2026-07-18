# TDCC Weekly Run Status

- generated_at: `2026-07-18 21:37:27 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/29646284040
- commit: `36985bd0b8b10ef62bbab0d86edc08975255bb34`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_invalid_holder_distribution_latest.csv` | yes | 1 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 501 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 100 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 166 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 295 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 37 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 26 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 118 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 90 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 66 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 48 |
| `output/latest/tdcc_overheated_short_term_edge_latest.md` | yes | 47 |
| `output/latest/tdcc_overheated_short_term_edge_latest.csv` | yes | 7 |
| `output/latest/tdcc_overheated_short_term_edge_candidates_latest.csv` | yes | 12 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 458 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 59 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 458 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 28 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 20 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 16 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 8 |
| `output/latest/tdcc_weekly_report_section_manifest_latest.csv` | yes | 5 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md` | yes | 52 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv` | yes | 28 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.md` | yes | 101 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv` | yes | 77 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 52 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 101 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.pdf` | yes | 905 |
| `output/latest/tdcc_weekly_candidate_full_latest.pdf` | yes | 1184 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260618.pdf` | yes | 780 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260626.pdf` | yes | 1243 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260703.pdf` | yes | 1301 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260717.pdf` | yes | 1184 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260618.pdf` | yes | 590 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260626.pdf` | yes | 954 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260703.pdf` | yes | 873 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260717.pdf` | yes | 905 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.md` | yes | 60 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.json` | yes | 107 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.md` | yes | 14 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.json` | yes | 5 |
| `output/history/tdcc_signals/tdcc_signal_log.csv` | yes | 906 |
| `output/history/tdcc_signals/tdcc_signal_performance.csv` | yes | 906 |
| `output/history/tdcc_signals/tdcc_signal_snapshot.csv` | yes | 12765 |
| `output/history/tdcc_signals/tdcc_normalized_signal_log.csv` | yes | 12765 |
| `output/history/tdcc_signals/theme_breadth_history.csv` | yes | 117 |
| `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv` | yes | 9165 |
| `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` | yes | 109 |

## Notes

- Normalized signal files dedupe by one stock per TDCC week.
- ABM ranking is separated from TDCC strength ranking.
- TDCC performance/effectiveness backtests are maintained by research_backtest_pipeline.yml.
- Pending D+N performance is not treated as positive or negative.
