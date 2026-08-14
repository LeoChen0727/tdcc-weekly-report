# Recent Daily Price Gap Repair

- status: `repaired`
- as_of_date: `20260814`
- date_boundary: `include_as_of_date_if_trading`
- target_end_date: `20260814`
- lookback_days: `7`
- expected_trading_dates: `20260807, 20260810, 20260811, 20260812, 20260813, 20260814`
- non_trading_days_in_window: ``
- missing_before: `20260812, 20260813, 20260814`
- missing_after: ``
- rebuild_history_status: `completed`

## Actions

| date | action | result | target |
|---|---|---|---|
| 20260812 | repair_daily_price_range | 0 | data/daily_price/daily_price_20260812.csv |
| 20260813 | repair_daily_price_range | 0 | data/daily_price/daily_price_20260813.csv |
| 20260814 | repair_daily_price_range | 0 | data/daily_price/daily_price_20260814.csv |
