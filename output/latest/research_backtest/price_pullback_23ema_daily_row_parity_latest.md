# Price Pullback 23EMA Daily Row Parity Audit

- generated_at: `2026-07-04 14:40:02 Asia/Taipei`
- model_id: `price_pullback_23ema`
- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level
- rule: any missing or extra stock row keeps the model blocked from daily operation promotion
- gap interpretation: the research proxy currently runs on the full stock-day frame; exact parity still needs dated daily candidate-universe/source-row replay before promotion
- date rule: `outcome_research_frame_has_date` tracks mature next-open/D+N outcome rows; `source_row_research_frame_has_date` tracks dated all_candidates/source-row replay for as-of daily row parity.
- note: this audit does not change production selection, scoring, ranking, or PDF output

## Status Summary

| parity_status | count |
| --- | --- |
| exact_daily_row_parity_pass | 13 |

## Snapshot Detail

| snapshot_report_date | research_frame_has_date | outcome_research_frame_has_date | source_row_research_frame_has_date | research_frame_date_basis | published_unique_stock_count | research_proxy_unique_stock_count | overlap_stock_count | published_not_in_proxy_rows | proxy_not_published_rows | published_proxy_coverage_pct | proxy_publish_precision_pct | parity_gap_driver | comparison_basis | candidate_universe_condition_stock_count | candidate_universe_replay_status | parity_status | parity_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 181 | 181 | 181 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 181 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260616 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 154 | 154 | 154 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 154 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260617 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 159 | 159 | 159 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 159 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260618 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 198 | 198 | 198 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 198 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260622 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 253 | 253 | 253 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 253 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260623 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 233 | 233 | 233 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 233 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260624 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 230 | 230 | 230 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 230 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260626 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 217 | 217 | 217 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 217 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260629 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 219 | 219 | 219 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 219 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260630 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 233 | 233 | 233 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 233 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260701 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 222 | 222 | 222 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 222 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260702 | True | True | True | outcome_research_frame;production_all_candidates_source_row_replay | 236 | 236 | 236 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 236 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
| 20260703 | True | False | True | production_all_candidates_source_row_replay | 237 | 237 | 237 | 0 | 0 | 100.0 | 100.0 | none_exact | production_all_candidates_source_row_replay | 237 | candidate_universe_replay_exact_match | exact_daily_row_parity_pass |  |
