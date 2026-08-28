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
The only implementation covered by this contract is
`.github/workflows/revenue_unreacted_range_readiness_formal_sync.yml`.

The exact sole readiness producer is
`scripts/sync_revenue_unreacted_range_operation_readiness.py`. The bundle
contract and the apply job must both bind the exact token
`producer=scripts/sync_revenue_unreacted_range_operation_readiness.py`.
The legacy broad builder `scripts/build_model_operation_readiness.py` is
forbidden in this workflow because it may recompute unrelated model rows.

## Trusted input and immutable output scope

The manual workflow must start from an exact current remote `main` SHA. The
literal target branch must already exist at that same SHA. The sole producer may
change exactly these four byte-paired readiness mirrors:

1. `output/latest/model_operation_readiness_latest.csv`
2. `output/latest/model_operation_readiness_latest.md`
3. `docs/latest/model_operation_readiness_latest.csv`
4. `docs/latest/model_operation_readiness_latest.md`

The generated row remains bound to
`revenue_unreacted_range/source_mid_falling v2`. Its exact blocker is:

`anomaly_disposition_blockers=9; unresolved_anomalies=9; forward_holdout_v2_mature=0/20; formal_adapter=not_started`

Both committed CSV mirrors and the committed Markdown status table must persist
all four disabled fields on the revenue row:
`formal_model_use_allowed=False`, `approved_for_daily=False`,
`presentation_allowed=False`, and `production_allowed=False`. A missing field is
a hard failure; an uncommitted bundle sidecar or derived-only inference is not
canonical readiness evidence. For existing non-revenue rows, both new fields
must remain empty legacy-neutral values. An empty value is neither `False` nor
`True` and must not be interpreted as a permission decision. In particular,
`formal_model_use_allowed` must not be derived from `approved_for_daily`, and
`production_allowed` must not be derived from `presentation_allowed`.

During the one-time bootstrap, the general readiness validator may accept the
four legacy mirrors only when their filtered Git blob identities and canonical
CSV-row/Markdown hashes exactly match the pinned
`7b05900722aa57df2271d8025da07aa0f81b74e0` baseline. Raw CRLF bytes are not a
gate. Any semantic or filtered-blob drift fails closed. The dedicated formal
sync validator never accepts the legacy schema: working-tree, staged, and
committed phases all require the new columns, explicit revenue `False` values,
and neutral non-revenue cells. After the artifact commit is merged, a follow-up
hardening PR must remove this exact legacy bootstrap allowance.

Ownership history is recorded as four separate registry-surface migrations:
the previously absent docs ownership rule, the two output-latest inventory
records, the builder/validator lifecycle records, and the builder/validator
production-inventory records. The pre-existing
`output/latest/model_operation_readiness_latest.*` ownership rule was already
`model_governance` and is not an ownership migration. The canonical ownership
validator must reconcile each appended migration against both the named base
registry fact and the current registry fact.

## Exact same-model replay dependency

Before changing any readiness mirror, each readiness writer entrypoint must
run exactly one canonical exact-replay gate. The legacy workflow entrypoint
delegates both this gate and its one exact-four-mirror write call to the
model-owned sync module; the companion workflow cutover removes only that
entrypoint indirection. The gate must create a temporary clean detached worktree
at the exact input commit and run one declared same-model, read-only,
in-memory replay child. Its direct replay entry
modules are
`revenue_unreacted_range_forward_holdout_v2` and
`validate_revenue_unreacted_range_forward_holdout_v2`; absence of a static
parent-process import is not, by itself, isolation evidence. The producer's
registered transitive research and objective-data dependencies remain part of
the runtime graph; the contract does not claim that only two modules are
loaded.

The child must bind the exact commit/tree identity and Python/pandas/numpy
runtime fingerprint. Worktree materialization and child identity checks must
ignore local Git replacement objects (`--no-replace-objects` and
`GIT_NO_REPLACE_OBJECTS=1`), so a local `refs/replace` entry cannot substitute
a different clean tree while preserving the requested commit name. The
temporary checkout must also use `core.autocrlf=false` so registered Git blob
evidence is materialized byte-for-byte instead of acquiring an operating-system
line-ending transformation. This does not change repository configuration or
turn raw-blob formatting into promotion evidence. The persisted
`monthly_revenue_history_blob_sha256` and the legacy
`source_detail_canonical_sha256`, `capture_id`, and
`event_row_canonical_sha256` values that transitively include it are
diagnostic-only when persisted and exact bundles are compared. Each bundle must
still pass its own internal legacy-envelope validation. Cross-bundle promotion
equivalence excludes only those fields and hashes the complete replay source
with only the raw blob token removed. The child
must run `validate_v1_exact17_freeze` before and after replay,
materialize the producer's current inputs without changing its observation
cutoff semantics, build all five v2 frames (`manifest`, `detail`, `summary`,
`comparison`, `anomaly`), and require the independent validator to pass. It
must also require every committed persisted frame to have the same canonical
promotion-semantic SHA as the independently validated exact build. The hard
projection retains monthly canonical-table/resolution SHA values, source-row
canonical hashes, cutoff/calendar dates and rows, rule/data-contract SHA,
per-stock and aggregate price SHA/counts, every event/business field, schema,
and extra columns. This closes event-set, PIT/source linkage, frozen membership,
D+1 confirmation, D+2/D+30 maturity, price lineage, and union-summary drift.

The child executes only the reviewed same-model in-memory producer and
independent-validator APIs. The parent launches it with `-I -B`, removes
Python path/home/startup injection, and does not call any artifact-writing API.
The parent must require a post-child clean Git status, including untracked
files, across the entire temporary worktree before removing it. Any observed
repository artifact mutation fails the sync. This boundary is limited to
observed cleanliness of the exact detached worktree and does not assert
controls over external paths; the called same-model code remains
repository-reviewed trusted code.

The called APIs must not mutate research artifacts, other-model artifacts,
production outputs, Daily Full outputs, PDF/packet files, or Apps Script
surfaces in the detached worktree. The child's result is a single versioned
JSON attestation containing exact
commit/tree/runtime identity, five-frame canonical promotion-semantic
hashes/counts, capture identity, full replay-source promotion-semantic SHA, and
complete per-stock/aggregate price lineage. Protocol v2 defines its canonical
frame hashes as this promotion projection rather than raw envelope identity.
Cache identity is
limited to the exact protocol, commit, tree, and runtime within one process.
Regardless of replay reads, the workflow output allowlist remains exactly the
four readiness mirrors above.

`summarize_revenue_promotion_readiness`,
`validate_revenue_readiness_source_files`, and the general
`validate_model_operation_readiness.py` path perform only the cheap committed
schema, canonical-source, count, timing, lifecycle, and readiness-row
consistency checks. Its PIT checks cover replay list/scalar alignment, date
ordering, non-placeholder SHA-256 format, detail linkage, and observed-through
boundaries, but deliberately do not import research-owner code or independently
recompute raw monthly-revenue table and row truth. That independent truth remains
owned by the research-owner validator module
`scripts/validate_revenue_unreacted_range_forward_holdout_v2.py`, its independent
`tests/test_revenue_unreacted_range_forward_holdout_v2.py` coverage, and the
writer's single pre-write exact child. The standalone validator CLI requires the
producer's explicit normalized price bundle, so a cheap PR job must not pass raw
price CSVs as a substitute or rematerialize the same 10--18 minute exact replay.
Before this contract is formally applied, its workflow companion PR must run the
independent v2 suite while excluding exactly these three Git-freeze replay nodes:
`test_v1_exact17_metadata_reproduces_authorized_bundle_digest`,
`test_v1_exact17_freeze_reports_the_drifting_path`, and
`test_v1_exact17_freeze_uses_git_blob_identity_for_clean_crlf_checkout`. The
existing direct monthly/source validators and explicit cheap syncer nodes remain
required. No additional v2 test may be deselected. The writer remains the only
persisted-truth exact gate. Raw monthly
blob lineage and its legacy source/capture/event envelope remain provenance
diagnostic material in both the cheap and exact paths; each bundle still
requires well-formed, internally consistent legacy values.
Replay availability must also equal the source date itself when it is a
normalized registered trading session, or otherwise the first normalized
registered session after that date. The cheap session gate
uses one no-replacement `git cat-file --batch` process, requires an exact blob
response for every safe registered path, and requires every worktree price CSV
to have the same canonical CSV semantics as its committed blob; CRLF-only byte drift is
diagnostic-neutral while any date or cell change fails. It does not claim to
rebuild or re-hash the producer's 108-column prepared per-stock frame. That
manifest full-frame SHA contract remains a hard check in the single writer
pre-write exact replay. These cheap checks must not launch the exact replay
child. The readiness
validator is not independent promotion evidence and does not re-prove canonical
research truth; the single pre-write exact-replay gate is the canonical gate
for that truth. Failure of that gate must occur before the first of the four
mirror writes.

## Companion PR validation boundary

The Daily Model PR CI revenue job must directly run the registered monthly and
source validators plus the related independent cases in
`tests/test_revenue_unreacted_range_forward_holdout_v2.py`. Those
research-owner gates are the PR-time canonical raw-truth boundary; a general
readiness validator must not replace them. The standalone v2 validator CLI
requires a separate explicit normalized price bundle that is not a committed
repository input, so PR CI must not fabricate that bundle or repeat the
long-running exact materialization solely to invoke the CLI.

The same job must invoke the selected cheap cases from
`tests/test_sync_revenue_unreacted_range_operation_readiness.py` by explicit
pytest node ID. A fuzzy `-k` expression is forbidden. The unique full exact
replay case
`test_current_canonical_sources_build_exact_disabled_revenue_row` is excluded
from PR CI because it is the long-running writer-equivalence integration; the
formal writer still runs the canonical exact replay once before any mirror
write.

Revenue-only changes must leave the Daily Model PR CI
`production_pdf_contracts` scope false. Repository lifecycle, semantic,
worktree-safety, hidden-coupling, and code-isolation gates remain mandatory,
but Daily production, PDF, packet, renderer, published-snapshot, and their
regression suites run only when the dedicated production/PDF scope is true.
The scope output is fail-closed and a relevant production or PDF path must
still select the full hard gate.

The TDCC Weekly and Individual Stock PR workflows use their own affected-path
detectors. An unrelated revenue-only change may run only their lightweight
checkout, scope-output, whitespace, or trust-root guards; it must not run TDCC
continuity/build/tests or the affected Individual Stock contract suite. A
TDCC- or Individual Stock-owned path or owned row in a shared registry must
still select that workflow's complete business validation suite.

## Atomic commit and push boundary

The apply job must independently verify the content hashes, exact producer token,
and exact contract, stage exactly the four mirrors, validate the staged phase,
and create exactly one direct-child commit. It must then run both readiness
validators again in the committed phase and require a clean index, worktree,
and untracked-file set.

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
