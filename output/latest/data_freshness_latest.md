# Data Freshness Status

- generated_at: `2026-08-06 10:41:10` Asia/Taipei
- market_session_status: `unknown`
- market_session_date: `20260805`
- expected_main_price_date: `20260805`
- market_session_reason_code: `awaiting_official_price_confirmation`
- main_price_date: `20260805`
- main_price_date_source: `historical_replay_override`
- historical_replay_main_price_date: `20260805`
- expected_price_history_high_water_date: `20260805`
- actual_stock_price_history_date: `20260805`
- report_ready: `False`
- report_ready_note: historical structured-source replay updates objective-source freshness only; publish artifacts remain stale
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
- daily_pdf_ready_note: historical structured-source replay must not mark stale daily PDFs ready

## Component Dates

| source | effective_date | raw_date | note |
|---|---:|---:|---|
| all_candidates_latest.csv | 20260717 | 20260717 | stale_date=20260717 |
| official_price_fetch_latest | 20260805 | 20260805 | ready |
| stock_monitor_latest.md | 20260717 | 20260717 | stale_date=20260717 |
| warrant_flow_latest.csv | 20260805 | 20260805 | ready |

## Rule

Historical structured-source replay explicitly pins the canonical main_price_date while preserving the same or newer validated raw price/history high-water date. The two dates remain visible and publish/PDF readiness must stay false until current publication artifacts are rebuilt.
