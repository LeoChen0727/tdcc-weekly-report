# Revenue unreacted range trigger-as-of anomaly migration v1

## Scope

This is an append-only, research-only migration for `revenue_unreacted_range` /
`source_mid_falling`. It changes anomaly attribution only. It does not change the
selected operation identity, model conditions, thresholds, entry/exit rules,
holding period, primary performance metrics, formal adapters, readiness,
production, Daily Full, PDF, or Apps Script.

Monthly revenue is the only fundamental input in scope. EPS, gross margin,
operating margin, operating income, non-operating income, net income, and
quarterly or annual financial-statement fields are not conditions, scores, or
promotion evidence in this migration.

## Immutable inputs and append-only outputs

- `source_first_condition_v3_20260720` remains byte/schema/semantic immutable.
- All v1 and v2 research artifacts remain immutable.
- Per-event anomaly flags are attached to an in-memory copy after the immutable
  source projection binding passes.
- New outputs are written only under `output/history/research` with the versions:
  - `source_first_qualifying_event_anomaly_v1_20260829`
  - `rearmed_operation_grid_v3_20260829`
  - `operation_lag_bucket_v3_20260829`
  - `position_shape_transition_matrix_v3_20260829`
  - `low_mid_falling_candidate_v3_20260829`
  - `trigger_asof_anomaly_migration_v1_20260829`

The canonical manifest is
`output/history/research/revenue_unreacted_range_trigger_asof_anomaly_migration_manifest_v1_20260829.csv`.
Raw blob hashes, raw file hashes, byte hashes, and CRLF differences remain
provenance diagnostics. Append-only identity and promotion-blocking validation
use canonical semantic hashes, canonical row hashes, and row counts. A replay
with byte-only differences preserves the existing bytes; a semantic difference
fails closed.

## Attribution rule

`trigger_asof_qualifying_event_v1_20260829` attributes a monthly-revenue anomaly
to an operation only when the qualifying event's availability trading date is
on or before that operation's trigger date. The episode-level anomaly flag is
retained as a diagnostic and is not used as the v3 operation attribution.

For stock `6177`, the operation triggered on `20251204`. The qualifying events
available on `20250519` and `20251017` are not anomaly candidates. The `202512`
event is an anomaly candidate but is first available on `20260119`; it therefore
must not flow backward into the `20251204` operation.

## Required invariants

- Selected operation count remains 53.
- Selected operation business-field change count is 0.
- Primary metrics remain 41 wins, 0 neutral, 12 failures, average return
  `14.895`, and median return `9.4077`.
- Unresolved anomaly candidates remain in primary metrics.
- Candidate exclusion remains sensitivity-only.
- The nine previously selected candidate operations remain present; only the
  `6177` operation changes from episode-aggregate source anomaly `True` to
  trigger-as-of source anomaly `False`.
- Raw/blob/CRLF-only mutations must not change any canonical promotion hash.
- A business or point-in-time field mutation must change every affected
  canonical promotion hash.
- `approved_for_daily=False`, `presentation_allowed=False`,
  `formal_model_use_allowed=False`, and `production_change=False` remain fixed.

Build and validate with:

```text
python scripts/revenue_unreacted_range_trigger_asof_anomaly_migration.py
python scripts/revenue_unreacted_range_trigger_asof_anomaly_migration.py --validate-only
```
