# Candidate Repeat Appearance Validation

- generated_at: `2026-06-02 19:42:07 Asia/Taipei`
- status: `pass`
- main_price_date: `20260602`
- history_available_days: `9`

## Files
- signal_log: `output/history/daily_signals/daily_candidate_signal_log.csv`
- signal_log_alias: `output/history/daily_candidates/daily_candidate_signal_log.csv`
- repeat_csv: `output/latest/candidate_repeat_appearance_latest.csv`
- repeat_md: `output/latest/candidate_repeat_appearance_latest.md`
- all_candidates: `output/latest/all_candidates_latest.csv`

## Row Counts
- signal_log: `6095`
- signal_log_alias: `6095`
- repeat_csv: `531`
- all_candidates: `787`

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
- preferred_date=20260601 differs from candidate signal_date=20260602; using candidate signal_date
