# Price Pullback 23EMA Daily Row Parity Audit

- generated_at: `2026-06-30 12:44:01 Asia/Taipei`
- model_id: `price_pullback_23ema`
- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level
- rule: any missing or extra stock row keeps the model blocked from daily operation promotion
- note: this audit does not change production selection, scoring, ranking, or PDF output

## Status Summary

| parity_status | count |
| --- | --- |
| blocked_not_exact_daily_row_parity | 8 |
| blocked_missing_research_frame_date | 1 |

## Snapshot Detail

| snapshot_report_date | research_frame_has_date | published_unique_stock_count | research_proxy_unique_stock_count | overlap_stock_count | published_not_in_proxy_rows | proxy_not_published_rows | published_proxy_coverage_pct | proxy_publish_precision_pct | parity_status | parity_blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | True | 181 | 1391 | 162 | 19 | 1229 | 89.5 | 11.65 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260616 | True | 154 | 1394 | 139 | 15 | 1255 | 90.26 | 9.97 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260617 | True | 159 | 1410 | 146 | 13 | 1264 | 91.82 | 10.35 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260618 | True | 198 | 1416 | 183 | 15 | 1233 | 92.42 | 12.92 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260622 | True | 253 | 1367 | 240 | 13 | 1127 | 94.86 | 17.56 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260623 | True | 233 | 1406 | 218 | 15 | 1188 | 93.56 | 15.5 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260624 | True | 230 | 1469 | 219 | 11 | 1250 | 95.22 | 14.91 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260626 | True | 217 | 1459 | 208 | 9 | 1251 | 95.85 | 14.26 | blocked_not_exact_daily_row_parity | research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; daily selection/ranking/report eligibility must be reconciled before promotion |
| 20260629 | False | 219 | 0 | 0 | 219 | 0 | 0.0 |  | blocked_missing_research_frame_date | research frame does not include this published snapshot date |
