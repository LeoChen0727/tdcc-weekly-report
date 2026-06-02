# Data Freshness Status

- generated_at: `2026-06-02 19:37:24` Asia/Taipei
- main_price_date: `20260601`
- actual_stock_price_history_date: `20260602`
- report_ready: `False`
- report_ready_note: official price fetch date does not match main_price_date

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260601 | 20260601 | ready |
| official_price_fetch_latest | 20260602 | 20260602 | future_date=20260602 |
| stock_monitor_latest.md | 20260602 | 20260602 | future_date=20260602 |
| warrant_flow_latest.csv | 20260601 | 20260601 | ready |

## Rule

When an upstream daily snapshot has a weekend or non-trading raw date newer than `data/stock_price_history`, the effective report date is capped to the actual latest stock price history date. This prevents copied weekend prices from becoming a fake main_price_date.
