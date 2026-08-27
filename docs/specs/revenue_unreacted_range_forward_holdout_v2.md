# Revenue Unreacted Range Forward Holdout v2

## Scope

This is an independent research-only append-only holdout family for
`revenue_unreacted_range`. It does not replace or rewrite the v1 family and it
does not authorize production, Daily Full, PDF, Apps Script dispatch, formal
adapter, ranking, scoring, or promotion use.

The PR #462 business rule remains unchanged. The v2 migration changes only the
selected source-projection evidence envelope:

- authorization: `user_authorized_2A_20260828`
- selected projection: `source_snapshot_projection_v2_20260822`
- projected rows: `19565`
- projected semantic SHA-256:
  `dacd5046e8af9abcd766b11b9557035481cc82af9d7fba746a8dad1ff183a967`
- selected manifest canonical SHA-256:
  `74b51a715c560777ea302fe559d89f74575ff94381c8cee1fa49496c25b7db2b`
- bridge: `20260714` through `20260830`
- first eligible holdout date: `20260831`

Before `20260831` the family must publish an empty detail capture with
`holdout_status=preregistered_waiting_for_start`. Bridge rows remain excluded.
Beginning `20260831` the family accumulates the unchanged D2-open / D30-close
rule with right censoring, same-stock non-overlap, and unresolved anomaly
candidate retention in primary metrics.

## Frozen v1 boundary

Every v2 stage validates all 17 v1 paths before and after the run. The canonical
bundle algorithm sorts repository-relative paths and hashes the UTF-8 sequence
`path|byte_count|sha256\n`. The required v1 bundle SHA-256 is:

`445b53afa31525e18adb86b91d9b90f055d1d9858cc4643038e256431537488c`

Any missing or byte-drifted v1 path blocks the v2 stage.

## Financial-statement boundary

This family uses monthly revenue only. EPS, gross margin, operating margin,
operating income, non-operating income, net income, and quarterly or annual
financial-statement fields remain excluded. They are disclosure context only
until a separately approved point-in-time objective data layer is complete.

## Output family

The family owns exactly 17 paths under these independent prefixes:

- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_v2_*`
- `output/history/research/revenue_unreacted_range_forward_holdout_v2_*`
- `docs/latest/revenue_unreacted_range_forward_holdout_v2_*`

The output consists of five latest mirrors, five append-only history surfaces,
five documentation mirrors, and two byte-identical current replay-source
mirrors. All formal-use flags must remain false.
