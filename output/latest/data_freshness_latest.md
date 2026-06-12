# Data Freshness Status

- generated_at: `2026-06-12 19:43:15` Asia/Taipei
- main_price_date: `20260612`
- actual_stock_price_history_date: `20260612`
- report_ready: `True`
- report_ready_note: core daily data dates match main_price_date
- warrant_ready: `True`
- warrant_ready_note: warrant_flow_date matches main_price_date
- daily_pdf_ready: `True`
- daily_pdf_ready_note: core daily data and warrant layer are ready for daily PDF source use

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260612 | 20260612 | ready |
| official_price_fetch_latest | 20260612 | 20260612 | ready |
| stock_monitor_latest.md | 20260612 | 20260612 | ready |
| warrant_flow_latest.csv | 20260612 | 20260612 | ready |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.
