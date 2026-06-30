# Price Pullback 23EMA Daily Row Parity Audit

- generated_at: `2026-06-30 15:43:16 Asia/Taipei`
- model_id: `price_pullback_23ema`
- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level
- rule: any missing or extra stock row keeps the model blocked from daily operation promotion
- gap interpretation: the research proxy currently runs on the full stock-day frame; exact parity still needs dated daily candidate-universe/source-row replay before promotion
- note: this audit does not change production selection, scoring, ranking, or PDF output

## Status Summary

| parity_status | count |
| --- | --- |
| blocked_not_exact_daily_row_parity | 9 |
| blocked_missing_research_frame_date | 1 |

## Snapshot Detail

| snapshot_report_date | research_frame_has_date | published_unique_stock_count | research_proxy_unique_stock_count | overlap_stock_count | published_not_in_proxy_rows | proxy_not_published_rows | published_proxy_coverage_pct | proxy_publish_precision_pct | parity_gap_driver | comparison_basis | candidate_universe_condition_stock_count | candidate_universe_replay_status | parity_status | parity_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | True | 181 | 1391 | 162 | 19 | 1229 | 89.5 | 11.65 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260616 | True | 154 | 1394 | 139 | 15 | 1255 | 90.26 | 9.97 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260617 | True | 159 | 1410 | 146 | 13 | 1264 | 91.82 | 10.35 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260618 | True | 198 | 1416 | 183 | 15 | 1233 | 92.42 | 12.92 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260622 | True | 253 | 1367 | 240 | 13 | 1127 | 94.86 | 17.56 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260623 | True | 233 | 1406 | 218 | 15 | 1188 | 93.56 | 15.5 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260624 | True | 230 | 1469 | 219 | 11 | 1250 | 95.22 | 14.91 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260626 | True | 217 | 1470 | 208 | 9 | 1262 | 95.85 | 14.15 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260629 | True | 219 | 1522 | 211 | 8 | 1311 | 96.35 | 13.86 | research_full_universe_proxy_exceeds_daily_candidate_publication_scope | full_research_frame_proxy |  | missing_historical_all_candidates_source_row_snapshot | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion |
| 20260630 | False | 233 | 233 | 233 | 0 | 0 | 100.0 | 100.0 | missing_research_frame_date | production_all_candidates_source_row_replay | 233 | candidate_universe_replay_exact_match | blocked_missing_research_frame_date | research frame does not include this published snapshot date |
