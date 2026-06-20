# Individual Stock Artifact Relocation Plan - 20260620

This plan defines the individual-stock artifact relocation implemented after the
`output/latest` CSV/MD artifact audit. It does not delete or retire artifacts.

## Scope

Canonical individual-stock report payload location:

```text
output/latest/individual_stock_reports/
```

Moved or repointed artifact groups:

- `output/latest/individual_stock_chatgpt_packets/` -> `output/latest/individual_stock_reports/chatgpt_packets/`
- `output/latest/individual_stock_price_windows/` -> `output/latest/individual_stock_reports/price_windows/`
- `output/latest/individual_stock_tdcc_windows/` -> `output/latest/individual_stock_reports/tdcc_windows/`
- Root individual-stock index/read-protocol CSV/MD files -> `output/latest/individual_stock_reports/`
- `docs/latest` individual-stock index/read-protocol mirrors -> `docs/latest/individual_stock_reports/`

The producer, validator, raw-health, publisher, workflow, and inventory
references use the canonical location.

## Retained Root Machine Aliases

These root artifacts are retained because they are machine-readable pipeline or
shared raw-data dependencies, not per-stock report payloads:

- `output/latest/individual_stock_technical_snapshot_latest.csv`
- `output/latest/individual_stock_technical_snapshot_latest.md`
- `output/latest/raw_data_fetch_status_latest.csv`
- `output/latest/raw_data_fetch_status_latest.md`
- `output/latest/sell_strategy_performance_latest.csv`
- `output/latest/sell_strategy_performance_latest.md`
- `output/latest/stock_price_history_manifest.csv`
- `output/latest/stock_price_history_manifest.md`

They are marked `keep` in `config/output_latest_artifact_inventory.csv`.

## Exclusions

This relocation does not affect:

- official daily six ChatGPT-side PDFs;
- TDCC weekly artifacts or workflows;
- research/backtest artifacts;
- daily model ranking, scoring, filtering, buy/sell, stop-loss, or PDF decision logic.

## Validation Contract

Required checks for this PR:

- individual-stock producer emits no root-level per-stock report payloads;
- `output/latest` root no longer has the old three individual-stock payload directories;
- old individual-stock root index/read-protocol paths are not referenced by current scripts, workflows, validators, config, or latest docs;
- `scripts/validate_individual_stock_outputs.py` reads the canonical path;
- daily PDF contract validators still pass.
