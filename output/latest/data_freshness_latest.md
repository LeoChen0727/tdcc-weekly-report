# Data Freshness Status

- generated_at: `2026-06-01 22:23:38` Asia/Taipei
- main_price_date: `20260601`
- actual_stock_price_history_date: `20260601`
- report_ready: `True`
- report_ready_note: core daily data dates match main_price_date

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260601 | 20260601 | ready |
| official_price_fetch_latest | 20260601 | 20260601 | ready |
| stock_monitor_latest.md | 20260601 | 20260601 | ready |
| warrant_flow_latest.csv | 20260601 | 20260601 | ready |

## Rule

When an upstream daily snapshot has a weekend or non-trading raw date newer than `data/stock_price_history`, the effective report date is capped to the actual latest stock price history date. This prevents copied weekend prices from becoming a fake main_price_date.
