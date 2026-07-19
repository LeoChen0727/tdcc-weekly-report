# TDCC Analytics Store Contract

The TDCC analytics store is a rebuildable machine-query layer derived from the
canonical TDCC dataset contract. It is not a second source of truth.

## Source Contract

The only accepted source is:

```text
output/latest/tdcc_dataset_manifest_latest.json
```

The builder reads every entry in `history_snapshots`, verifies each normalized
snapshot hash, and records the exact `source_tdcc_dataset_id`. It does not glob
files, consume individual-stock packets, or infer missing periods from calendar
dates.

## Outputs

```text
output/latest/tdcc_analytics/tdcc_holder_ratio_history_latest.parquet
output/latest/tdcc_analytics/tdcc_analytics_latest.duckdb
output/latest/tdcc_analytics/tdcc_analytics_manifest_latest.json
```

The same directory is mirrored to `docs/latest/tdcc_analytics/` by the official
TDCC weekly workflow.

The Parquet file is the portable long-table representation. The DuckDB file is
a rebuildable query database with these tables:

- `tdcc_holder_ratio_history`
- `tdcc_dataset_metadata`
- `tdcc_snapshot_metadata`

It also provides:

- `tdcc_holder_ratio_latest`
- `tdcc_holder_ratio_previous_official`
- `tdcc_holder_ratio_latest_comparison`

`tdcc_holder_ratio_latest_comparison` joins only to `period_index - 1`. If a
stock is absent from that exact official period, previous values remain `NULL`;
the view never jumps back to an older observation and labels it as one period.

## Failure Boundary

Build or validation fails closed when the canonical manifest is missing,
snapshot hashes drift, dataset ids differ, snapshot metadata changes, Parquet
and DuckDB rows diverge, or the latest/previous views no longer use adjacent
official period indices.

The analytics store does not define TDCC scoring, ranking, candidate selection,
PDF text, or model parameters. Research and production consumers remain bound
to their own contracts while sharing the same canonical TDCC dataset identity.
