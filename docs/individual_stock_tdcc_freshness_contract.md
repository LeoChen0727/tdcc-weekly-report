# Individual Stock TDCC Freshness Contract

## Scope

This contract belongs to `owner=individual_stock`. It governs structured
individual-stock ChatGPT packets, TDCC windows, and packet indexes. It does not
change the TDCC weekly producer, workflow trigger order, individual-stock PDF
renderer or layout, stock models, ranking, scoring, daily recommendations, or
research/backtest outputs.

## Official date source

The only official TDCC date for individual-stock packets is read from:

```text
output/latest/tdcc_weekly_candidate_report_validation_latest.json
```

The contract fails closed unless all of these conditions hold:

- `status=pass`
- `date_contract.date_source=report_ready_csv_signal_date`
- root `signal_date` is a valid `YYYYMMDD` date

The builder and validator must not infer the date from wall-clock time, TDCC
window maxima, README text, report filenames, or another latest artifact.

## Packet and index semantics

Every packet and packet-index row records:

- `official_tdcc_signal_date`
- `latest_tdcc_date`
- `tdcc_rows`
- `tdcc_history_status`
- `tdcc_freshness_status`

`tdcc_history_status=tdcc_history_ready` is allowed only when `tdcc_rows >= 8`
and `latest_tdcc_date == official_tdcc_signal_date`. For `tdcc_rows > 0`, a date
mismatch must be represented by both `tdcc_history_status=tdcc_window_stale`
and `tdcc_freshness_status=tdcc_window_stale`; it must not claim that TDCC
history is current. Current windows use
`tdcc_freshness_status=tdcc_window_fresh`, while current windows with fewer than
eight rows remain `tdcc_history_status=insufficient_tdcc_history`.

Stocks with no TDCC rows are a separate valid state: `tdcc_rows=0`, blank
`latest_tdcc_date`, `tdcc_history_status=tdcc_missing`, and
`tdcc_freshness_status=tdcc_missing`. The packet and index still record the
official signal date for audit, but they do not fabricate a latest TDCC date and
must not classify the missing window as stale.

## Validation boundary

`python scripts/validate_individual_stock_outputs.py --all` reads the same
official contract and checks every packet-index row and corresponding packet.
Missing or malformed contracts, non-`pass` status, unexpected date source,
missing metadata, date mismatch, stale status, or index/packet disagreement are
hard failures.

Sparse PR worktrees may use fixtures for regression coverage because protected
`data/` and `output/` are not materialized there. The authoritative whole-set
gate runs after merge through `individual_stock_data_refresh.yml`, rebuilds all
packets, and validates the complete packet population against the official TDCC
signal date.
