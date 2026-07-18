# TDCC Weekly Run Status

- generated_at: `2026-07-19 02:24:45 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/29655376696
- commit: `f58e2beff54912b33376fe89182ffe1a192ed498`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_weekly_data_readiness_latest.json` | yes | 66 |
| `output/latest/tdcc_weekly_data_readiness_latest.md` | yes | 13 |
| `output/latest/tdcc_weekly_history_continuity_latest.json` | yes | 72 |
| `output/latest/tdcc_weekly_history_continuity_latest.md` | yes | 28 |
| `output/latest/tdcc_invalid_holder_distribution_latest.csv` | yes | 1 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 521 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 117 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 170 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 295 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 39 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 28 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 116 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 88 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 67 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 49 |
| `output/latest/tdcc_overheated_short_term_edge_latest.md` | yes | 47 |
| `output/latest/tdcc_overheated_short_term_edge_latest.csv` | yes | 7 |
| `output/latest/tdcc_overheated_short_term_edge_candidates_latest.csv` | yes | 12 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 463 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 59 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 405 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 22 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 14 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 19 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 11 |
| `output/latest/tdcc_weekly_report_section_manifest_latest.csv` | yes | 5 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md` | yes | 55 |
| `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv` | yes | 31 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.md` | yes | 98 |
| `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv` | yes | 74 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 55 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 98 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.pdf` | yes | 921 |
| `output/latest/tdcc_weekly_candidate_full_latest.pdf` | yes | 1177 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260618.pdf` | yes | 780 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260626.pdf` | yes | 1243 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260703.pdf` | yes | 1301 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260717.pdf` | yes | 1177 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260618.pdf` | yes | 590 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260626.pdf` | yes | 954 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260703.pdf` | yes | 873 |
| `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260717.pdf` | yes | 921 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.md` | yes | 60 |
| `output/latest/tdcc_weekly_candidate_report_validation_latest.json` | yes | 107 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.md` | yes | 14 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.json` | yes | 5 |
| `output/history/tdcc_signals/tdcc_signal_log.csv` | yes | 999 |
| `output/history/tdcc_signals/tdcc_signal_performance.csv` | yes | 999 |
| `output/history/tdcc_signals/tdcc_signal_snapshot.csv` | yes | 13909 |
| `output/history/tdcc_signals/tdcc_normalized_signal_log.csv` | yes | 13909 |
| `output/history/tdcc_signals/theme_breadth_history.csv` | yes | 128 |
| `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv` | yes | 9327 |
| `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` | yes | 109 |

## Notes

- Normalized signal files dedupe by one stock per TDCC week.
- ABM ranking is separated from TDCC strength ranking.
- TDCC performance/effectiveness backtests are maintained by research_backtest_pipeline.yml.
- Pending D+N performance is not treated as positive or negative.
