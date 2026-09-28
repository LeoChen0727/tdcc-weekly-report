# Data Freshness Status

- generated_at: `2026-09-28 19:32:22` Asia/Taipei
- market_session_status: `closed_scheduled`
- market_session_date: `20260928`
- expected_main_price_date: `20260924`
- market_session_reason_code: `twse_annual_holiday`
- main_price_date: `20260924`
- main_price_date_source: `validated_stock_history`
- historical_replay_main_price_date: ``
- expected_price_history_high_water_date: ``
- actual_stock_price_history_date: `20260924`
- report_ready: `False`
- report_ready_note: market session is not open_confirmed: market_session_status=closed_scheduled
- warrant_ready: `True`
- warrant_ready_note: warrant_flow_date matches main_price_date
- warrant_source_status: `ok`
- warrant_source_status_note: current-date warrant layer ready
- warrant_source_consecutive_unavailable_days: `0`
- warrant_daily_publish_allowed: `True`
- warrant_pdf_visibility: `visible`
- warrant_model_effect_allowed: `True`
- warrant_pdf_effect_allowed: `True`
- daily_pdf_ready: `False`
- daily_pdf_ready_note: core daily data not ready: market session is not open_confirmed: market_session_status=closed_scheduled

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260924 | 20260924 | ready |
| official_price_fetch_latest | 20260924 | 20260924 | ready |
| stock_monitor_latest.md | 20260924 | 20260924 | ready |
| warrant_flow_latest.csv | 20260924 | 20260924 | ready |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.

## Daily Authority Release

- release_id: `daily-authority-20260928-36415472390-1`
- generation_id: `daily-authority-20260928-36415472390-1`
- producer: `daily_full_pipeline`
- base_commit_sha: `7ce50e1bc36a962dde9d5bff239063be03b5dcd8`
- market_session_date: `20260928`
- expected_main_price_date: `20260924`
- market_status: `closed_scheduled`
