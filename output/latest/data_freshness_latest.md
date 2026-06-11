# Data Freshness Status

- generated_at: `2026-06-11 18:25:30` Asia/Taipei
- main_price_date: `20260605`
- actual_stock_price_history_date: `20260605`
- report_ready: `True`
- report_ready_note: core daily data dates match main_price_date
- warrant_ready: `False`
- warrant_ready_note: warrant_flow_date does not match main_price_date (warrant_flow_date=20260602, main_price_date=20260605)
- daily_pdf_ready: `False`
- daily_pdf_ready_note: warrant layer not ready: warrant_flow_date does not match main_price_date (warrant_flow_date=20260602, main_price_date=20260605)

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260605 | 20260605 | ready |
| official_price_fetch_latest | 20260605 | 20260611 | raw_date=20260611; capped_to_actual_trading_date=20260605 |
| stock_monitor_latest.md | 20260605 | 20260605 | ready |
| warrant_flow_latest.csv | 20260602 | 20260602 | stale_date=20260602 |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.
