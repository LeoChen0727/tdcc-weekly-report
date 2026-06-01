# Daily Candidate Model Selection Audit

- status: `pass`
- main_price_date: `20260601`
- all_candidates_rows: `851`
- raw_model_signal_rows: `885`
- report_model_signal_rows: `885`
- selected_condition_error_count: `0`
- selected_condition_warning_count: `0`
- expected_volume_breakout_stock_count: `172`
- expected_tdcc_short_stock_count: `70`

## Errors

- none

## Warnings

- volume_watch signal_date mismatch: expected 20260601, got ['20260529']; stale auxiliary table ignored for date gating
- tdcc_short_edge signal_date mismatch: expected 20260601, got ['20260529']; stale auxiliary table ignored for date gating

## Review Details

- missing_volume_breakout_model_stocks: `[]`
- missing_tdcc_short_model_stocks: `[]`
- review_missing_w_bottom_candidates: `[]`
- review_missing_breakout_candidates: `[]`
