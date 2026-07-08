# Volume Range Breakout V2 Overlap Sensitivity Contract

This contract applies to research-only `volume_range_breakout` v2 semantic
audits and condition matrices.

## Rule

Event-level rows are not sufficient promotion evidence when a stock can produce
multiple signals while a prior accepted trade is still active.

Every research/backtest artifact that compares v2 conditions for operation
promotion must publish both:

1. An event-level diagnostic basis, preserving all deduped source events.
2. A same-stock non-overlap basis, accepting only one active trade per stock and
   suppressing later events whose `entry_date` falls on or before the accepted
   trade's `exit_date`.

The event-level basis may be used only for diagnostics, source coverage checks,
and signal-frequency review. It must not be cited alone as promotion evidence.

## Required Guardrails

- `source_event_key` must remain unique in source and detail artifacts.
- `same_stock_non_overlap` summary rows must have `overlap_pair_count=0`.
- Suppressed rows must remain visible in an audit detail artifact with
  `same_stock_active_position_overlap`.
- Known regression rows must be pinned in validation. Current fixture:
  `stock_id=8454` has three v2 rows; only the first row may be accepted under
  the same-stock non-overlap basis.
- All rows remain `approved_for_daily=False` and
  `production_readiness=not_production_ready_research_only` until an explicit
  promotion PR updates the formal production contract.

## Current Artifacts

- `output/latest/research_backtest/volume_range_breakout_v2_overlap_sensitivity_latest.csv`
- `output/latest/research_backtest/volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv`
- `output/latest/research_backtest/volume_range_breakout_v2_overlap_sensitivity_latest.md`

The corresponding history copies live under `output/history/research/`.

## Validator

Run:

```text
python scripts/validate_volume_range_breakout_v2_overlap_sensitivity.py
```

The validator fails closed when latest/history artifacts diverge, non-overlap
rows still overlap, regression rows are not suppressed correctly, or any row is
marked as production-approved.
