# Research TDCC Dataset Consumer Contract

## Ownership boundary

`research_backtest` is an advisory-only consumer of the canonical TDCC dataset. It must not produce a second TDCC raw dataset, modify the production baseline, or promote research parameters.

## Canonical input

Research jobs must start from `output/latest/tdcc_dataset_manifest_latest.json` and require all of these fields:

- `history_dates`
- `history_snapshots`
- `history_snapshot_count`
- `dataset_id`

`required_dates` and `snapshots` are the recent continuity window. They are not the research history. Research must use the full ordered `history_snapshots` list and verify every declared hash. Glob fallback, `data/tdcc_stock_history`, individual-stock packets, and latest-only holder reports are forbidden substitutes.

## Interval semantics

One-week change is valid only when both rows belong to adjacent official dates in `history_dates`. A missing stock row resets the consecutive-increase streak. Longer-window changes may be calculated only against the exact official period at that offset; a gap must never be compressed and mislabeled as one week.

The special official period `20260709` is an ordinary member of `history_dates` and must not be replaced by a guessed Friday date.

## Output lineage

Every TDCC-derived research CSV must contain `source_tdcc_dataset_id`. Every TDCC-derived Markdown artifact must state the same field and value. Validators fail closed when the manifest, snapshot hash, or output dataset id differs.

Validation entrypoint:

```text
python scripts/validate_research_tdcc_dataset_consumers.py
```
