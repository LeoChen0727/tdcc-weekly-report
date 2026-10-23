# Data Freshness Status

- generated_at: `2026-10-23 19:59:56` Asia/Taipei
- market_session_status: `closed_emergency`
- market_session_date: `20261023`
- expected_main_price_date: `20261022`
- market_session_reason_code: `taipei_full_day_or_morning_work_suspension`
- main_price_date: `20261021`
- main_price_date_source: `validated_stock_history`
- historical_replay_main_price_date: ``
- expected_price_history_high_water_date: ``
- actual_stock_price_history_date: `20261021`
- report_ready: `False`
- report_ready_note: market session is not open_confirmed: market_session_status=closed_emergency
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
- daily_pdf_ready_note: core daily data not ready: market session is not open_confirmed: market_session_status=closed_emergency

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20261021 | 20261021 | ready |
| official_price_fetch_latest | 20261021 | 20261021 | ready |
| stock_monitor_latest.md | 20261021 | 20261021 | ready |
| warrant_flow_latest.csv | 20261021 | 20261021 | ready |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.

## Daily Authority Release

- release_id: `daily-authority-20261023-39949390425-1`
- generation_id: `daily-authority-20261023-39949390425-1`
- producer: `daily_full_pipeline`
- base_commit_sha: `7f19b59184ea1927d0b61aa78d84a2db05e11c5a`
- market_session_date: `20261023`
- expected_main_price_date: `20261022`
- market_status: `closed_emergency`
