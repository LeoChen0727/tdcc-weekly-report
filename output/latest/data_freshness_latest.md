# Data Freshness Status

- generated_at: `2026-06-03 19:37:10` Asia/Taipei
- main_price_date: `20260602`
- actual_stock_price_history_date: `20260603`
- report_ready: `False`
- report_ready_note: official price fetch date does not match main_price_date

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260602 | 20260602 | ready |
| official_price_fetch_latest | 20260603 | 20260603 | future_date=20260603 |
| stock_monitor_latest.md | 20260603 | 20260603 | future_date=20260603 |
| warrant_flow_latest.csv | 20260602 | 20260602 | ready |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.
