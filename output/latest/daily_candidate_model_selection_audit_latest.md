# Daily Candidate Model Selection Audit

- status: `pass`
- main_price_date: `20260603`
- all_candidates_rows: `543`
- raw_model_signal_rows: `676`
- report_model_signal_rows: `676`
- selected_condition_error_count: `0`
- selected_condition_warning_count: `14`
- expected_volume_breakout_stock_count: `149`
- expected_tdcc_short_stock_count: `0`

## Errors

- none

## Warnings

- volume_watch signal_date mismatch: expected 20260603, got ['20250711']; volume helper was excluded from date-gated checks
- 2312: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2344: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2369: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2484: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2495: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 4906: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 6127: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 6175: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 6265: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 6284: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 6706: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 8028: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2375: TDCC short-edge helper is stale/unavailable; accepted TDCC short continuation row without auxiliary-table cross-check
- 2888: volume_breakout_watch is stale/unavailable; accepted volume_range_breakout row without auxiliary-table cross-check

## Review Details

- missing_volume_breakout_model_stocks: `[]`
- missing_tdcc_short_model_stocks: `[]`
- review_missing_w_bottom_candidates: `[]`
- review_missing_breakout_candidates: `[]`
