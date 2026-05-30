# TDCC Weekly Run Status

- generated_at: `2026-05-30 12:49:27 Asia/Taipei`
- github_run: https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/26674744889
- commit: `76c4cf9d21a9b47c3b15f89c5858fa79e2df8565`

## Outputs

| file | exists | lines |
|---|---:|---:|
| `output/latest/tdcc_weekly_report_latest.md` | yes | 146 |
| `output/latest/tdcc_holder_ratio_latest.csv` | yes | 1973 |
| `output/latest/tdcc_signal_performance_latest.md` | yes | 457 |
| `output/latest/tdcc_signal_structures_latest.md` | yes | 114 |
| `output/latest/tdcc_stock_history_manifest.csv` | yes | 1973 |
| `output/latest/tdcc_history_backfill_manifest_latest.md` | yes | 52 |
| `output/latest/tdcc_pre_move_accumulation_latest.md` | yes | 169 |
| `output/latest/tdcc_signal_effectiveness_latest.md` | yes | 259 |
| `output/latest/tdcc_strength_ranking_top_latest.md` | yes | 61 |
| `output/latest/tdcc_strength_ranking_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_pre_move_abm_top_latest.md` | yes | 62 |
| `output/latest/tdcc_pre_move_abm_top_latest.csv` | yes | 51 |
| `output/latest/tdcc_phase_distribution_latest.md` | yes | 149 |
| `output/latest/tdcc_phase_distribution_latest.csv` | yes | 121 |
| `output/latest/tdcc_top_risk_list_latest.md` | yes | 79 |
| `output/latest/tdcc_top_risk_list_latest.csv` | yes | 61 |
| `output/latest/tdcc_chatgpt_tracking_packet_latest.md` | yes | 525 |
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
