# Price Pullback 23EMA Daily Row Parity Audit

- generated_at: `2026-06-30 22:43:07 Asia/Taipei`
- model_id: `price_pullback_23ema`
- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level
- rule: any missing or extra stock row keeps the model blocked from daily operation promotion
- gap interpretation: the research proxy currently runs on the full stock-day frame; exact parity still needs dated daily candidate-universe/source-row replay before promotion
- note: this audit does not change production selection, scoring, ranking, or PDF output

## Status Summary

| parity_status | count |
| --- | --- |
| exact_daily_row_parity_pass | 9 |
| blocked_missing_research_frame_date | 1 |

## Snapshot Detail

| snapshot_report_date | research_frame_has_date | published_unique_stock_count | research_proxy_unique_stock_count | overlap_stock_count | published_not_in_proxy_rows | proxy_not_published_rows | published_proxy_coverage_pct | proxy_publish_precision_pct | parity_gap_driver | comparison_basis | candidate_universe_condition_stock_count | candidate_universe_replay_status | parity_status | parity_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | True | 181 | 181 | 181 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 181 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260616 | True | 154 | 154 | 154 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 154 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260617 | True | 159 | 159 | 159 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 159 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260618 | True | 198 | 198 | 198 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 198 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260622 | True | 253 | 253 | 253 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 253 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260623 | True | 233 | 233 | 233 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 233 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260624 | True | 230 | 230 | 230 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 230 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260626 | True | 217 | 217 | 217 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 217 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260629 | True | 219 | 219 | 219 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 219 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260630 | False | 233 | 233 | 233 | 0 | 0 | 100.0 | 100.0 | missing_research_frame_date | production_all_candidates_source_row_replay | 233 | candidate_universe_replay_exact_match | blocked_missing_research_frame_date | research frame does not include this published snapshot date |
