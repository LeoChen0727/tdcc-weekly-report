# TDCC Weekly Candidate Report Validation

- status: pass
- signal_date: 20260626
- date_source: report_ready_csv_signal_date
- error_count: 0
- warning_count: 2

## Date Contract

- date_source: `report_ready_csv_signal_date`
- report_date: `20260626`
- highlight_report_ready_signal_dates: `['20260626']`
- full_report_ready_signal_dates: `['20260626']`
- weekly_source_signal_dates: `['20260626']`
- consecutive_source_signal_dates: `['20260626']`

## Manifest Sections

- 1. `weekly_increase` (tdcc_ranking): highlight=10, full=50
- 2. `consecutive_accumulation` (tdcc_ranking): highlight=10, full=50
- 3. `model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10` (model_cross): highlight=10, full=50
- 4. `model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10` (model_cross): highlight=10, full=50

## Report Row Counts

- weekly_increase: 413
- consecutive_accumulation: 28
- model_cross: 8
- highlight_report: 28
- full_report: 86
- manifest_sections: 4

## Section Row Counts

### highlight
- `weekly_increase`: 10
- `consecutive_accumulation`: 10
- `model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10`: 8
- `model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10`: 0
### full
- `weekly_increase`: 50
- `consecutive_accumulation`: 28
- `model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10`: 8
- `model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10`: 0

## Font Contract

- `output/latest/tdcc_weekly_candidate_highlight_latest.pdf`: `['/AAAAAA+TDCCSansTC-Regular', '/AAAAAB+TDCCSansTC-Regular', '/Helvetica']`
- `output/latest/tdcc_weekly_candidate_full_latest.pdf`: `['/AAAAAA+TDCCSansTC-Regular', '/AAAAAB+TDCCSansTC-Regular', '/Helvetica']`
- `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260626.pdf`: `['/AAAAAA+TDCCSansTC-Regular', '/AAAAAB+TDCCSansTC-Regular', '/Helvetica']`
- `output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260626.pdf`: `['/AAAAAA+TDCCSansTC-Regular', '/AAAAAB+TDCCSansTC-Regular', '/Helvetica']`

## Errors

- none

## Warnings

- highlight report-ready CSV section has no rows and will render an explicit empty state: model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10
- full report-ready CSV section has no rows and will render an explicit empty state: model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10
