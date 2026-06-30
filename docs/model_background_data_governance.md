# Daily Model Background Data Governance

This document defines the boundary between shared background data and
model-specific interpretation for daily stock model research.

## Rule

Shared background data may contain only objective point-in-time facts or
measurements. Examples include OHLCV history, TDCC holder-flow ratios, market
index returns, and raw 20/45/90-day price-window metrics computed on or before
`signal_date`.

Model-specific interpretation must stay outside shared data families. Examples:

- `neckline_context_*` is owned by `neckline_volume_breakout_confirmation`.
- `w_bottom_*` geometry and path-quality fields are owned by W-bottom model
  families.
- `price_pullback_23ema_*` research outputs are owned by `price_pullback_23ema`.

The shared 45/90-day numeric features can be reused. The neckline 45-day
non-bearish filter cannot be reused as a 23EMA rule.

## Registry

The contract table is:

`config/daily_model_background_data_registry.csv`

Each row is a data family, not a single column. Important fields:

- `scope`: shared objective data, replay evidence, latest-only context,
  model-specific interpretation, model research output, or a missing shared
  data family.
- `consumer_models`: `all_models` is allowed only for shared objective/replay
  data, never for model-specific interpretation.
- `point_in_time_status`: whether the family can be used safely for historical
  signal dates.
- `allowed_use` / `forbidden_use`: the operational boundary.
- `cleanup_status`: whether the data is active, blocked, or a deletion review
  candidate.

The validator is:

`python scripts/validate_daily_model_background_data_registry.py`

## Cleanup Audit

Before deleting or relocating a registered data family, run:

```text
python scripts/build_daily_model_background_data_cleanup_audit.py
python scripts/validate_daily_model_background_data_cleanup_audit.py
```

The audit artifacts are:

- `output/latest/research_backtest/daily_model_background_data_cleanup_audit_latest.csv`
- `output/latest/research_backtest/daily_model_background_data_cleanup_audit_latest.md`
- `docs/latest/daily_model_background_data_cleanup_audit_latest.csv`
- `docs/latest/daily_model_background_data_cleanup_audit_latest.md`

These files are a deletion gate, not deletion approval. A row can become a
cleanup PR candidate only when `cleanup_status=deprecated_candidate` and the
audit finds no active workflow, inventory, lineage, validator, replay, parity,
or promotion dependency.

## Cleanup Policy

Do not delete research, history, or latest artifacts just because they look
old. A data family can be deleted only after a separate cleanup PR proves:

1. No active workflow consumes it.
2. No validator or report/packet consumer depends on it.
3. It is not historical replay evidence.
4. It is not required for model parity, readiness, or promotion audit trail.
5. The registry marks it `deprecated_candidate`.
6. The cleanup audit marks `deletion_allowed=True`.

This PR intentionally lists cleanup boundaries but does not delete historical
snapshots or model research evidence.

## Revenue Gap

Revenue can be used where current production code already has current daily
fields, but it must not become a formal historical model gate until a dated
monthly revenue point-in-time panel exists and has its own validator.
