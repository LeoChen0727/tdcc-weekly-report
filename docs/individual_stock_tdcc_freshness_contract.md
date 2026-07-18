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

## Historical-only noncurrent packets

The repository does not currently provide a formal point-in-time listing-status
source. Runtime code therefore must not infer `delisted` from an announcement,
stock name, or an old price/TDCC date. Until a formal listing-status source is
registered, the fail-closed current-universe evidence is:

```text
output/latest/official_daily_price_latest.csv
```

This artifact must contain one date only, and that date must equal
`data_freshness_latest.csv.main_price_date`. Packet/index metadata records:

- `current_main_price_date`
- `current_main_price_universe_status`
- `current_main_price_universe_source=official_daily_price_latest_main_price_date`
- `listing_status_source_status=formal_listing_status_source_unavailable`

A stock absent from that dated current main-price universe is marked
`current_main_price_universe_status=historical_only_noncurrent`. If it retains
TDCC rows, its real last TDCC date is preserved and both
`tdcc_history_status` and `tdcc_freshness_status` are
`historical_only_noncurrent`. This is not a stale-current claim, does not request
source backfill, and does not assert a formal delisting status. The packet is
historical-only and must not be presented as current TDCC data.

For a stock present in the current main-price universe, any non-empty TDCC
window whose last date differs from the official TDCC signal date remains
`tdcc_window_stale` and fails validation. Absence from the current price
universe must never be used to rewrite or fabricate either price or TDCC dates.

### Known non-runtime audit evidence

The initial `historical_only_noncurrent` cases are auditable without making the
builder depend on web access:

- `3426` is absent from the `20260717` official current-price artifact; repo
  price history ends `20260601` and TDCC history ends `20260529`. TPEx separately
  announced termination of OTC trading effective `20260608`:
  `https://www.tpex.org.tw/storage/about_otc_news/2026/04/1776935023715_1458144_news.pdf`.
- `4987` is absent from the `20260717` official current-price artifact; repo
  price history ends `20260520` and TDCC history ends `20260522`. TPEx separately
  announced termination of OTC trading effective `20260529`:
  `https://www.tpex.org.tw/storage/about_otc_news/2026/04/1776934842791_1458144_news.pdf`.

These announcement links are audit context, not runtime classification inputs.
The machine-enforced status remains `historical_only_noncurrent` rather than
`delisted` until the repository registers a formal listing-status source.

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
