# Individual Stock TDCC Freshness Contract

## Scope

This contract belongs to `owner=individual_stock`. It governs structured
individual-stock ChatGPT packets, TDCC windows, and packet indexes. It does not
change the TDCC weekly producer, workflow trigger order, individual-stock PDF
renderer or layout, stock models, ranking, scoring, daily recommendations, or
research/backtest outputs.

## Canonical dataset source

The only canonical TDCC dataset contract for individual-stock packets is read
from:

```text
output/latest/tdcc_dataset_manifest_latest.json
```

The contract fails closed unless all of these conditions hold:

- `status=pass`
- `schema_version=tdcc_dataset_manifest_v1`
- `dataset_id` matches the manifest `signal_date`
- `required_dates` is an ordered, unique official-date sequence ending on
  `signal_date`
- the signal-date snapshot exists and its stock count matches the manifest

The builder and validator must not infer the date or dataset identity from
wall-clock time, TDCC window maxima, README text, report filenames, or another
latest artifact.

## Packet and index semantics

Every packet and packet-index row records:

- `source_tdcc_dataset_id`
- `official_tdcc_signal_date`
- `latest_tdcc_date`
- `tdcc_rows`
- `tdcc_history_status`
- `tdcc_freshness_status`
- `tdcc_continuity_status`
- `tdcc_missing_official_dates`

`tdcc_history_status=tdcc_history_ready` is allowed only when `tdcc_rows >= 8`
and all of the following are true: the packet uses the canonical `dataset_id`,
the stock contains every required official date, its 1w/2w/3w changes and
consecutive-up streak recompute correctly on that date sequence, and
`latest_tdcc_date == official_tdcc_signal_date`. For stocks present in the
current main-price universe with `tdcc_rows > 0`, a latest-date mismatch must
be represented by both `tdcc_history_status=tdcc_window_stale` and
`tdcc_freshness_status=tdcc_window_stale`; it must not claim that TDCC history
is current. Current windows use
`tdcc_freshness_status=tdcc_window_fresh`, while current windows with fewer than
eight rows remain `tdcc_history_status=insufficient_tdcc_history`.

An individual stock/date omission explicitly recorded in
`accepted_history_exceptions` does not fail every stock packet. That stock is
marked `tdcc_history_status=tdcc_history_degraded_exception`,
`tdcc_freshness_status=tdcc_window_degraded`, and
`tdcc_continuity_status=accepted_history_exception`; the missing official dates
are disclosed. Any unapproved missing date is a hard failure. A change spanning
two official periods must never be written into a `change_1w` field.

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

Absence means only that the stock has no current main-price row for this report
period. It is a fail-closed packet-currentness state, not a formal finding that
the security is delisted, OTC trading was terminated, or the security is no
longer legally listed. `historical_only_noncurrent` must not claim either
current TDCC data or a formal listing-status conclusion.

For a stock present in the current main-price universe, any non-empty TDCC
window whose last date differs from the official TDCC signal date remains
`tdcc_window_stale` and fails validation. Absence from the current price
universe must never be used to rewrite or fabricate either price or TDCC dates.

### Known non-runtime audit evidence

Two known stale-date audit cases are auditable without making the builder
depend on web access:

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
canonical dataset contract and checks every packet-index row, packet, and TDCC
window.
For each stock it independently reads `data/tdcc_stock_history/{stock_id}.csv`
and verifies the exact required official dates, 1w/2w/3w changes, consecutive
up weeks, source row count, latest date, and `dataset_id`. Packet, index, and
window metadata must match that source lineage; agreement between generated
artifacts is not sufficient. A missing source file is accepted as
`tdcc_missing` only when the stock is absent from the canonical current TDCC
universe. Missing or malformed contracts, unapproved date gaps, derived-field
mismatch, missing lineage metadata, date mismatch, stale status, or
index/packet/window disagreement are hard failures.

Sparse PR worktrees may use fixtures for regression coverage because protected
`data/` and `output/` are not materialized there. The authoritative whole-set
gate runs after merge through `individual_stock_data_refresh.yml`, rebuilds all
packets, and validates the complete packet population against the official TDCC
signal date.
