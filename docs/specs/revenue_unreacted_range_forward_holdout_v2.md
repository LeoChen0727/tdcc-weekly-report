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

## Append-only canonical price-lineage migration (2026-08-29)

Migration
`revenue_forward_holdout_v2_price_semantic_projection_v1_20260829`, authorized
by `user_authorized_3A_3C_20260829`, replaces the promotion hard-gate identity
of the whole prepared price frame with a composite profile: a bounded canonical
raw-price input-lineage component plus exact replay of all five output frames.
The raw projection is not a standalone business-semantic hash. This migration
does not rewrite either existing capture. The next research capture appends under
`revenue_low_mid_falling_forward_holdout_data_v3_20260829`; predecessor history
rows receive only the exact additive blank columns needed by the new schema.
Any column removal, reorder, partial extension, or predecessor value change
fails closed.

The input-lineage component version is
`revenue_forward_holdout_raw_price_source_projection_v1_20260829`; its schema
SHA-256 is
`7ef675db9ab08c7fc88dc0382571f0a16ad346a646fe3ccdf0ccfe18bb5106a9`.
Rows are ordered by `date` within ascending `stock_id` and contain exactly:

- `session_sequence_index` as a zero-based exact integer;
- `date` as an eight-digit `YYYYMMDD` string;
- raw-source `open`, `high`, `low`, `close`, and
  `analysis_price_adjustment_factor` as scale-8 decimal strings using
  `ROUND_HALF_EVEN`, with missing values encoded as the empty string;
- `price_resolution_ids_on_date` as a trimmed exact string.

Each per-stock and aggregate identity also binds the observation cutoff,
`RULE_CANONICAL_SHA256`, and `DATA_CONTRACT_SHA256`. The component therefore
binds canonical raw price sessions and the company-action resolution basis,
without claiming that it alone binds every prepared business input or treating
runtime-derived pandas/numpy floats as portable source identity.
Prepared fields including `ma60`, `ma120`, `analysis_ema23`,
`cross_breakout_prev20`, `operation_ma20`, and `operation_ema23` are outside
this raw-input gate. Raw `volume` remains available in the whole-frame
provenance diagnostic but is not a hard gate because the frozen holdout and
operation rule do not consume it.

Excluding derived floats does not exempt their business effects. The
independent exact replay reconstructs and compares the five output surfaces:
manifest, event detail, maturity status, comparison, and anomaly sensitivity.
The promotion-preparation composite profile separately binds the committed
producer/validator identity and canonical hashes of those output frames; those
five output hashes, not the raw projection alone, are the business-semantic
hard gate.
If a derived-float difference changes a trigger, anchor feature, event set,
entry/exit result, maturity count, anomaly flag, metric, or permission, the
exact output gate fails even when the raw-input projection is unchanged. The
raw-input hash does not claim to distinguish two derived floats that have the
same raw source. A pre-start empty capture remains immature research evidence
and promotion remains blocked.

`price_input_canonical_sha256` and
`price_input_stock_canonical_sha256s` remain in the manifest as whole-frame
provenance diagnostics. They can reveal runtime, pandas/numpy, serialization,
or raw-layout differences, but they do not participate in `capture_id`, event
row semantic identity, append-only semantic parity, or promotion replay. Raw
blob SHA and CRLF/LF differences have the same diagnostic-only role. The
independent validator separately reconstructs the bounded projection and must
match its version, schema SHA-256, per-stock hashes, aggregate hash, row count,
stock count, cutoff, rule contract, and data contract.

This migration does not change the PR #462 rule, thresholds, event population,
primary or sensitivity metrics, anomaly treatment, maturity, permissions, or
the frozen v1 exact17 bundle. The model-governance readiness consumer must be
migrated separately before it may treat the new projection fields as its hard
gate; this research-owner migration does not edit that owner lane.
