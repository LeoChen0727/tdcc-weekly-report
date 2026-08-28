# Revenue Unreacted Range Readiness Formal Sync v1

## Authority and owner handoff

- `exception_id=revenue_unreacted_range_readiness_formal_sync_3a_v1_20260828`
- `authorization_reference=user_authorized_3A_3C_20260828`
- `contract_version=revenue_readiness_sync_3a_v1_20260828`
- workflow implementation owner: `workflow_automation_maintenance`
- readiness semantics owner: `daily_model_maintenance/model_governance`
- inventory owner: `daily_recommendation_maintenance`
- literal target: `codex/revenue-unreacted-range-readiness-formal-sync-3a-v1-20260828`

This is an exact one-shot exception to the normal PR-safe workflow boundary. It
does not authorize any other workflow to commit, push, deploy, or publish.

## Trusted input and immutable output scope

The manual workflow must start from an exact current remote `main` SHA. The
literal target branch must already exist at that same SHA. The builder may
change exactly these four byte-paired readiness mirrors:

1. `output/latest/model_operation_readiness_latest.csv`
2. `output/latest/model_operation_readiness_latest.md`
3. `docs/latest/model_operation_readiness_latest.csv`
4. `docs/latest/model_operation_readiness_latest.md`

The generated row remains bound to
`revenue_unreacted_range/source_mid_falling v2`. Its exact blocker is:

`anomaly_disposition_blockers=9; unresolved_anomalies=9; forward_holdout_v2_mature=0/20; formal_adapter=not_started`

The canonical evidence must still prove all four disabled meanings:
`formal_model_use_allowed=False`, `approved_for_daily=False`,
`presentation_allowed=False`, and `production_allowed=False`. The last meaning
is derived fail-closed from canonical `production_change=False` together with
`operation_directive_level=no_operation_directive` and no adapter.

## Atomic commit and push boundary

The apply job must independently verify the content hashes and exact contract,
stage exactly the four mirrors, validate the staged phase, and create exactly
one direct-child commit. It must then run both readiness validators again in the
committed phase and require a clean index, worktree, and untracked-file set.

The privileged step is the final workflow step. It must revalidate committed
semantics, re-read both remote identities, perform exactly one non-force push,
remove the temporary key on both success and failure, and then prove:

- remote `main` remains the expected input SHA;
- the literal target equals the emitted sync commit SHA.

Because the target must equal remote `main` before the push, the same target
cannot be reused after a successful run.

## Forbidden surfaces

This exception does not authorize a `schedule` or `push` trigger, force-push,
arbitrary `codex/*` target, chained workflow dispatch, admin bypass, production
model use, Daily Full, PDF or packet rendering, Apps Script, formal adapter
enablement, operation directives, or writes outside the exact four mirrors.
