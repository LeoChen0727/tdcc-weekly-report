# Financial Statement Point-In-Time Coverage

- generated_at: `2026-07-16 01:32:03 Asia/Taipei`
- audit_id: `financial_statement_pit_coverage_v1`
- captured_sources: `12`
- captured_raw_rows: `1972`
- normalized_history_rows: `1968`
- unique_stocks: `1968`
- fiscal_period_range: `2026Q1` to `2026Q1`
- unresolved_numerical_anomaly_candidates: `36`; all remain in primary data.
- pit_coverage_status: `current_snapshot_only_not_historical_pit`
- formal_model_use_allowed: `False`
- boundary: current TWSE/TPEX OpenAPI data is recorded from `first_observed_at` forward. The global table date is not treated as a company filing date.
- historical requirement: exact company filing availability, revision-preserving MOPS/XBRL history, and coverage validation must pass before any model may consume EPS, margins, operating income, non-operating income, or net income as formal evidence.

## Coverage Rows

| market | industry_schema | rows | stocks | EPS coverage | net income coverage | PIT status |
|---|---|---:|---:|---:|---:|---|
| ALL | ALL | 1968 | 1968 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TPEX | banking | 0 | 0 | 0.0000% | 0.0000% | current_snapshot_empty_placeholder |
| TPEX | financial_holding | 0 | 0 | 0.0000% | 0.0000% | current_snapshot_empty_placeholder |
| TPEX | general | 884 | 884 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TPEX | insurance | 0 | 0 | 0.0000% | 0.0000% | current_snapshot_empty_placeholder |
| TPEX | other | 0 | 0 | 0.0000% | 0.0000% | current_snapshot_empty_placeholder |
| TPEX | securities | 7 | 7 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | banking | 10 | 10 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | financial_holding | 13 | 13 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | general | 1041 | 1041 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | insurance | 6 | 6 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | other | 4 | 4 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
| TWSE | securities | 3 | 3 | 100.0000% | 100.0000% | current_snapshot_only_not_historical_pit |
