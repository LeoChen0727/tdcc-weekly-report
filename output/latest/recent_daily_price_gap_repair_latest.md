# Recent Daily Price Gap Repair

- status: `repaired`
- as_of_date: `20260902`
- date_boundary: `include_as_of_date_if_trading`
- target_end_date: `20260902`
- lookback_days: `7`
- expected_trading_dates: `20260826, 20260827, 20260828, 20260831, 20260901, 20260902`
- non_trading_days_in_window: ``
- missing_before: `20260902`
- missing_after: ``
- rebuild_history_status: `completed`

## Actions

| date | action | result | target |
|---|---|---|---|
| 20260902 | repair_daily_price_range | 0 | data/daily_price/daily_price_20260902.csv |
