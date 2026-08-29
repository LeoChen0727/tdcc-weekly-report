# Revenue Unreacted Range Readiness Bootstrap Hardening v1

## Scope

This append-only contract applies only to
`revenue_unreacted_range/source_mid_falling v2` operation-readiness validation.
It does not change model conditions, thresholds, ranking, samples, research
metrics, anomaly dispositions, forward-holdout interpretation, adapters,
production, Daily Full, PDF, packet, Apps Script, or any other model's business
semantics.

## Required predecessor lineage

The hardening change may merge only after the one-shot formal readiness sync has
committed the four canonical readiness mirrors and that artifact-only change has
merged to `main` through a normal PR without admin bypass. The registered sync
mechanism lineage is:

- Formal-sync foundation PR: `#602`
- Formal-sync foundation merge commit:
  `00d40db297dfc643303387b5872ac56d493730d0`
- Model-owned sync PR: `#604`
- Model-owned sync merge commit:
  `e80a7c30d53083b8bbe010e63fb49ae22bfc42de`
- Workflow-isolation PR: `#607`
- Workflow-isolation merge commit:
  `95cb2de334f0d6083f5ff5a6094ac75f84c43668`
- Semantic-replay PR: `#609`
- Semantic-replay merge commit:
  `f4dab51d40ebea39b09b8e6940bfeee8b2e3f51e`
- Revenue ownership marker-boundary PR: `#610`
- Revenue ownership marker-boundary merge commit:
  `67453a4a6e3662429e65654529f39e7e7f1404d8`
- Formal-sync workflow run: `33208090763` (`success`)
- Required artifact-only PR: `#611`
- Required artifact-only merge commit:
  `40648e7edc032a30d802cd2ee7a333b99a032ad2`

The artifact lineage above is the exact merged artifact PR and `main` merge
commit. Reusing a mechanism PR or mechanism merge commit as artifact evidence
is forbidden.

## Canonical readiness gate after hardening

After the predecessor artifact merge, every readiness CSV must contain both
`formal_model_use_allowed` and `production_allowed` as required columns. The
single `revenue_unreacted_range` row must persist all four disabled permissions:

- `formal_model_use_allowed=False`
- `approved_for_daily=False`
- `presentation_allowed=False`
- `production_allowed=False`

Non-revenue legacy rows remain neutral blank for the two revenue-only columns.
Missing columns, partial schemas, non-canonical boolean spellings, a missing or
duplicate revenue row, any enabled revenue permission, or non-neutral legacy
values fail closed.

The readiness validator continues to compare the committed revenue row against
the model-owned promotion, anomaly-disposition, and future-only forward-holdout
sources. The research matrix is complete and must not be reintroduced as a
blocker. Anomaly disposition, mature forward holdout, and a separately
authorized formal adapter remain the promotion gates.

## Retired bootstrap behavior

Once the artifact-only predecessor is on `main`, the validator must not accept
the pre-sync schema through a legacy fallback. Raw Git blob IDs, line-ending
conversion, and CRLF/LF differences are provenance diagnostics only; they are
not readiness or promotion gates. No raw-blob pin, CRLF normalization helper,
legacy mirror reader, or legacy-bootstrap acceptance path may remain in
`scripts/validate_model_operation_readiness.py`.

Promotion evidence remains fail-closed on canonical semantic SHA, cutoff rows,
canonical row hashes, PIT/lineage, anomaly disposition, append-only migrations,
model-owned artifact boundaries, immutable v1 evidence, future-only holdout
maturity, research-production isolation, and the formal adapter gate. This
hardening does not relax any of those invariants.

## Validation

Before publication, after the artifact-only predecessor has merged, the
hardening PR must run at least:

- `python -m pytest tests/test_model_operation_readiness.py`
- `python scripts/validate_model_operation_readiness.py`
- `python scripts/validate_repo_file_lifecycle_inventory.py`
- `python scripts/validate_repo_production_inventory.py`
- revenue-only scope-detector and workflow/formal-sync focused tests
- repository semantic-integrity and model-research-ownership focused tests

While this patch remains an unpublished preparation on the pre-artifact base,
the exact schema and writer-absence unit tests plus scope, inventory, and
ownership checks may run; the live readiness validator is expected to stay
blocked because the four mirrors still use the predecessor schema.

The four readiness mirror files are immutable in this hardening PR. No
production, Daily Full, PDF, packet, Apps Script, workflow dispatch, or formal
operation directive is authorized by this contract.

## V5 bootstrap retirement completion evidence

The v2 formal-sync mechanism merged through PR `#631` at
`6c6dc7b9f352415f7c13e0dd332abc5282227222`; post-merge revenue-only run
`33261085880` succeeded. One-shot formal-sync run `33262394430` emitted direct
child `209916db5c62bf9ec4e6c76de71442b42a9255ef`, changing exactly the four
readiness mirrors. Artifact-only PR `#632` merged that child to `main` at
`c37c805d1f7af3188096cfb25d5d3a0fe5836378`.

The merged readiness row is the v5 disabled-adapter state with
`forward_holdout_v2_mature=0/20` and all four formal permissions set to
`False`. The transitional exact-predecessor constants, mirror validator,
fallback acceptance path, and predecessor-only tests are therefore retired.
Current readiness remains fail-closed through direct comparison with the
model-owned promotion, anomaly, PIT/lineage, canonical-price, future-only
holdout, and adapter sources.
