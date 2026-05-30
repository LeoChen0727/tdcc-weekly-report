# Candidate Repeat Appearance Validation

- generated_at: `2026-05-30 23:36:42 Asia/Taipei`
- status: `pass`
- main_price_date: `20260530`
- history_available_days: `8`

## Files
- signal_log: `output/history/daily_signals/daily_candidate_signal_log.csv`
- signal_log_alias: `output/history/daily_candidates/daily_candidate_signal_log.csv`
- repeat_csv: `output/latest/candidate_repeat_appearance_latest.csv`
- repeat_md: `output/latest/candidate_repeat_appearance_latest.md`
- all_candidates: `output/latest/all_candidates_latest.csv`

## Row Counts
- signal_log: `5202`
- signal_log_alias: `5202`
- repeat_csv: `470`
- all_candidates: `681`

## Checks
- signal_log_exists: `True`
- signal_log_alias_exists: `True`
- main_price_date_appended: `True`
- repeat_csv_exists: `True`
- repeat_columns_present: `True`
- all_candidates_repeat_columns_present: `True`
- no_duplicate_stock_day_in_repeat: `True`

## Errors
- none

## Warnings
- preferred_date=20260529 differs from signal_date=20260530; using signal_date
