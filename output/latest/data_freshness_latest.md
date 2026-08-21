# Data Freshness Status

- generated_at: `2026-08-21 20:04:04` Asia/Taipei
- market_session_status: `open_confirmed`
- market_session_date: `20260821`
- expected_main_price_date: `20260821`
- market_session_reason_code: `twse_tpex_target_date_confirmed`
- main_price_date: `20260821`
- main_price_date_source: `validated_stock_history`
- historical_replay_main_price_date: ``
- expected_price_history_high_water_date: ``
- actual_stock_price_history_date: `20260821`
- report_ready: `True`
- report_ready_note: core daily data dates match main_price_date
- warrant_ready: `True`
- warrant_ready_note: warrant_flow_date matches main_price_date
- warrant_source_status: `ok`
- warrant_source_status_note: current-date warrant layer ready
- warrant_source_consecutive_unavailable_days: `0`
- warrant_daily_publish_allowed: `True`
- warrant_pdf_visibility: `visible`
- warrant_model_effect_allowed: `True`
- warrant_pdf_effect_allowed: `True`
- daily_pdf_ready: `True`
- daily_pdf_ready_note: core daily data, warrant layer, and PDF theme display are ready for daily PDF source use; group rotation themes resolved for PDF display

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260821 | 20260821 | ready |
| official_price_fetch_latest | 20260821 | 20260821 | ready |
| stock_monitor_latest.md | 20260821 | 20260821 | ready |
| warrant_flow_latest.csv | 20260821 | 20260821 | ready |

## Rule

When an upstream daily snapshot has a raw date newer than the latest validated all-market price history date, the effective report date is capped to the validated price date. A stock price history date is rejected when many symbols have the exact same OHLCV as recent prior rows, because that indicates a copied or stale upstream snapshot rather than a trustworthy trading-day close.

## Daily Authority Release

- release_id: `daily-authority-20260821-32478042113-1`
- generation_id: `daily-authority-20260821-32478042113-1`
- producer: `daily_full_pipeline`
- base_commit_sha: `fd327a92bb990bbd47876b2ea6cb1955378a5087`
- market_session_date: `20260821`
- expected_main_price_date: `20260821`
- market_status: `open_confirmed`
