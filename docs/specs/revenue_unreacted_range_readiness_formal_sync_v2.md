# Revenue Unreacted Range Readiness Formal Sync v2

## Authority and fixed scope

- `contract_version=revenue_readiness_sync_3c_v2_20260829`
- `exception_id=revenue_unreacted_range_readiness_formal_sync_3c_v2_20260829`
- `authorization_reference=user_authorized_3A_3C_20260829`
- `target_branch=codex/revenue-unreacted-range-readiness-formal-sync-3c-v2-20260829`
- `confirmation=sync_revenue_unreacted_range_readiness_v2_20260829`
- workflow owner: `workflow_automation_maintenance`
- readiness semantics owner: `daily_model_maintenance/model_governance`
- inventory owner: `daily_recommendation_maintenance`

The exact workflow surface is
`.github/workflows/revenue_unreacted_range_readiness_formal_sync.yml`.

This is a one-shot, exact-main readiness-mirror synchronization. It does not
authorize production, Daily Full, PDF, packet rendering, Apps Script, a formal
buy/sell directive, or any change to another model. The workflow may push one
validated direct-child commit only to the inert target above. It never checks
out or executes code from that target.

The model scope remains exactly
`revenue_unreacted_range/source_mid_falling v2`. It uses monthly revenue only.
EPS, gross margin, operating margin, operating income, non-operating income,
net income, and quarterly or annual financial-statement fields are not model
conditions, scores, ranking inputs, or promotion evidence.

## Sole producer and canonical source gates

The sole writer is:

`producer=scripts/sync_revenue_unreacted_range_operation_readiness.py`

The workflow invokes that producer exactly once. The producer owns the calls to
the canonical anomaly-disposition validator, disabled-adapter validator,
forward-holdout validation, and exact replay. The workflow and the dedicated
formal-sync validator must not reimplement those business rules or infer their
results from raw registries.

The dedicated validator is:

`validator=scripts/validate_revenue_unreacted_range_readiness_formal_sync_v2.py`

It validates only the exact-four readiness artifacts, their persisted
permission/readiness meanings, cross-model preservation, and the Git phase
boundary (`working-tree`, `staged`, or `committed`). It does not import or call
an anomaly classifier, adapter business module, research producer, PDF
renderer, packet producer, Daily Full entrypoint, or Apps Script surface.

## Required readiness result

The producer's canonical gates must have established all of the following
before any readiness mirror is written:

- nine anomaly rows total;
- `verified_real_extreme=8`, retained in Primary;
- `verified_data_error_repaired=1`, for the repaired 6177 derived attribution;
- `unresolved_anomalies=0`;
- `effective_anomaly_blockers=0`;
- `operation_module_status=disabled_adapter_preparation_validated`;
- `daily_adapter_status=disabled_no_runtime_artifact`;
- `operation_module_id=revenue_unreacted_range_source_mid_falling_v2_operation_v1`;
- `daily_adapter_row_count=0`;
- `daily_adapter_data_row_count=0`;
- `daily_adapter_sections` is empty;
- `formal_model_use_allowed=False`;
- `approved_for_daily=False`;
- `presentation_allowed=False`;
- `production_allowed=False`.

The exact readiness blocker is only:

`blocker=forward_holdout_v2_mature=0/20`

This records current natural maturity without waiting for it or treating
bridge, right-censored, or immature events as formal results. No holdout result
may be used to add a condition, change a threshold, reselect a sample, or tune
the fixed rule.

`disabled_adapter_preparation_validated` means the model-owned adapter and its
validators have passed in disabled, in-memory preparation mode. It does not
mean a runtime artifact exists, the model is approved, the model is buyable,
or a PDF/packet consumer is connected.

## Exact-four artifact and phase contract

The only writable artifacts are:

1. `output/latest/model_operation_readiness_latest.csv`
2. `output/latest/model_operation_readiness_latest.md`
3. `docs/latest/model_operation_readiness_latest.csv`
4. `docs/latest/model_operation_readiness_latest.md`

The two CSV mirrors must be byte-identical. The two Markdown mirrors must be
byte-identical. The Markdown Status Table must agree with the CSV for the
revenue row and its four disabled permission fields. Non-revenue rows must be
unchanged from the exact base commit except for the shared `generated_at`
timestamp; the two revenue-only permission columns remain blank on non-revenue
legacy rows.

The `working-tree` phase requires the exact base SHA at `HEAD`, no staged or
untracked paths, and exactly four unstaged mirror modifications. The `staged`
phase requires the same exact base SHA, exactly four staged mirror
modifications, and no unstaged or untracked paths. The `committed` phase
requires a clean worktree and exactly one direct-child commit whose diff is the
same four paths. Rename, copy, deletion, symlink, submodule, extra path, and
replacement-object substitution fail closed.

The bundle contains only the four mirrors plus `SHA256SUMS` and `CONTRACT`.
Both jobs independently bind remote `main`, the inert target, the exact base
SHA, the exact producer, and the dedicated validator. The apply job verifies
the bundle hashes and exact contract before staging. The final step revalidates
the committed phase and performs the workflow's only non-force push. The
deploy key is available only in that final step and is removed on exit.

## Explicitly forbidden effects

This synchronization must not:

- create or write a daily adapter/runtime artifact;
- change model conditions, thresholds, ranking, samples, or operation rules;
- modify anomaly evidence, holdout evidence, promotion registries, or v1 data;
- change another model's readiness row beyond the permitted timestamp;
- set any of the four revenue permissions to `True`;
- invoke production, Daily Full, PDF, packet, Apps Script, or deployment;
- push to `main`, force-push, or push to an arbitrary branch.

After the one-shot artifact PR is merged, the inert target no longer equals
current `main`, so the unchanged workflow cannot be reused without a new,
explicitly reviewed contract.
