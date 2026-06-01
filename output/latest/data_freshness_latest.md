# Data Freshness Status

- generated_at: `2026-06-01 20:17:46` Asia/Taipei
- main_price_date: `20260601`
- actual_stock_price_history_date: `20260601`
- report_ready: `False`
- report_ready_note: all_candidates date does not match main_price_date

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260529 | 20260529 | stale_date=20260529 |
| official_price_fetch_latest | 20260601 | 20260601 | ready |
| stock_monitor_latest.md | 20260601 | 20260601 | ready |
| warrant_flow_latest.csv | 20260529 | 20260529 | stale_date=20260529 |

## Rule

When an upstream daily snapshot has a weekend or non-trading raw date newer than `data/stock_price_history`, the effective report date is capped to the actual latest stock price history date. This prevents copied weekend prices from becoming a fake main_price_date.
