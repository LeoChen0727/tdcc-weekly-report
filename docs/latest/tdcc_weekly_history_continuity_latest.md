# TDCC Weekly History Continuity

- status: `pass`
- generated_at: `2026-07-31 00:42:55 Asia/Taipei`
- signal_date: `20260724`
- required_dates: `20260430, 20260508, 20260515, 20260522, 20260529, 20260605, 20260612, 20260618, 20260626, 20260703, 20260709, 20260717, 20260724`
- current_stock_count: 1971
- missing_rows_before: 2
- repaired_count: 0
- accepted_exception_count: 2
- official_no_data_count: 1
- invalid_holder_distribution_count: 1
- unresolved_missing_rows: 0

## Contract

- Required dates come from the official TDCC query form, not filename spacing or computer date.
- Missing historical rows are fetched before any 1w/2w/3w or consecutive calculation.
- A systemic or unresolved history gap blocks report production; a confirmed per-stock history exception is recorded explicitly.

## Missing Before

- `20260626`: missing_stock_count=2 existing_rows=1970

## Actions

- `20260626` `2380` invalid_holder_distribution attempts=1: single-holder or placeholder distribution
- `20260626` `3152` official_no_data attempts=3: official query returned no distribution row
