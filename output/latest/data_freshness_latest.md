# Data Freshness Status

- generated_at: `2026-06-05 02:32:22` Asia/Taipei
- main_price_date: `20260603`
- actual_stock_price_history_date: `20260603`
- report_ready: `True`
- report_ready_note: core daily data dates match main_price_date

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260603 | 20260603 | ready |
| official_price_fetch_latest | 20260603 | 20260604 | raw_date=20260604; capped_to_actual_trading_date=20260603 |
| stock_monitor_latest.md | 20260603 | 20260604 | raw_date=20260604; capped_to_actual_trading_date=20260603 |
| warrant_flow_latest.csv | 20260603 | 20260604 | raw_date=20260604; capped_to_actual_trading_date=20260603 |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.
