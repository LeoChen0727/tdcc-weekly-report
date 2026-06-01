# TDCC Weekly Run Status

- generated_at: `2026-06-01 18:58:59 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/26750386346
- commit: `b3aa514735e3129df433fc516a292a4b17d9ee3e`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 457 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 102 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 169 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 266 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 62 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 130 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 102 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 79 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 61 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 501 |
| `output/latest/tdcc_weekly_increase_ranking_latest.md` | yes | 978 |
| `output/latest/tdcc_weekly_increase_ranking_latest.csv` | yes | 971 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.md` | yes | 776 |
| `output/latest/tdcc_consecutive_accumulation_ranking_latest.csv` | yes | 769 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.md` | yes | 69 |
| `output/latest/tdcc_weekly_model_cross_summary_latest.csv` | yes | 55 |
| `output/latest/tdcc_weekly_candidate_highlight_latest.md` | yes | 89 |
| `output/latest/tdcc_weekly_candidate_full_latest.md` | yes | 1817 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.md` | yes | 14 |
| `output/latest/tdcc_chatgpt_tracking_validation_latest.json` | yes | 5 |
| `output/history/tdcc_signals/tdcc_signal_log.csv` | yes | 301 |
| `output/history/tdcc_signals/tdcc_signal_performance.csv` | yes | 301 |
| `output/history/tdcc_signals/tdcc_signal_snapshot.csv` | yes | 6013 |
| `output/history/tdcc_signals/tdcc_normalized_signal_log.csv` | yes | 6013 |
| `output/history/tdcc_signals/theme_breadth_history.csv` | yes | 68 |
| `output/history/tdcc_signals/tdcc_pre_move_accumulation_history.csv` | yes | 2413 |
| `output/history/tdcc_signals/tdcc_signal_factor_stats_monthly.csv` | yes | 37 |

## Notes

- Normalized signal files dedupe by one stock per TDCC week.
- ABM ranking is separated from TDCC strength ranking.
- TDCC performance/effectiveness backtests are maintained by research_backtest_pipeline.yml.
- Pending D+N performance is not treated as positive or negative.
