# Repo Hidden Coupling Audit

Scope: repository-wide hidden coupling and governance gaps observed after the
daily PDF role, golden regression, shared-path, and completion hard-gate PRs.
This audit does not change stock model conditions, scoring, ranking,
research/backtest baselines, PDF layout, or generated report content.

## Plain-Language Conclusion

The original daily PDF substring bug class is now guarded for the six
ChatGPT-side daily PDFs: role matching must use the runtime `pdf_role` manifest,
and output PDF replay must pass the completion hard gate before the daily
pipeline can succeed.

The remaining repo risk is broader: several production surfaces still depend on
large shared files, manually interpreted fallback behavior, validators that may
exist without workflow wiring, and generated artifacts whose owner/lineage is
tracked at a broad class level instead of one artifact at a time. These are not
all immediate defects, but they are the places where "change A unexpectedly
changes B" can return if future PRs are not scoped carefully.

## Audit Matrix

Source of truth: `config/repo_hidden_coupling_audit.csv`.

| issue_id | category_id | plain category | risk | status | next action |
|---|---|---|---:|---|---|
| HC-001 | `filename_substring_title_token_matching` | filename / title / substring matching | high | guarded for daily, open repo-wide | Extend machine-readable role and section manifests beyond daily ChatGPT-side PDFs. |
| HC-002 | `fallback_inference` | fallback inference | high | partially guarded | Create a fallback semantics registry with owner, freshness limit, fail-closed policy, and downstream effect rules. |
| HC-003 | `pdf_side_lifecycle_invention` | PDF-side lifecycle invention | critical | guarded for daily, open for other consumers | Extend adapter-only lifecycle validation to packets, individual reports, and future model-facing PDFs. |
| HC-004 | `model_condition_scoring_ranking_shared_coupling` | model condition / scoring / ranking shared coupling | high | open | Split per-model condition/scoring modules or add an AST owner-map validator. |
| HC-005 | `validators_not_workflow_called` | validators not called by workflow | medium | open | Add a validator tier registry for `ci_required`, `pr_required`, `manual_only`, or retired validators. |
| HC-006 | `artifact_lineage_owner_gaps` | artifact lineage / owner gaps | high | open | Build artifact lineage v2 with pattern-level generated artifact classes and producer-owned manifests. |

## Evidence Summary

- This audit is validated by
  `scripts/validate_repo_hidden_coupling_audit.py`, and the validator is wired
  into both Daily Full Pipeline and daily model PR validation.
- Daily PDF role matching is now protected by
  `scripts/validate_daily_pdf_role_manifest_contract.py` and
  `scripts/validate_chatgpt_daily_report_new_conversation_replay.py`.
- Daily PDF completion is now protected by
  `scripts/validate_daily_pdf_completion_hard_gate.py`, including runtime
  manifest, six generated PDFs, output text regression, and formal operation
  adapter readiness consistency.
- Daily shared PDF path ownership is now inventoried by
  `config/daily_pdf_shared_path_inventory.csv` and guarded by
  `scripts/validate_daily_pdf_shared_path_isolation.py`.
- Stock model contracts exist in `config/stock_model_contract_registry.csv`, but
  the implementation hotspot remains `scripts/build_daily_candidate_model_layer.py`.
- A 2026-07-06 scan found 126 tracked `scripts/validate*.py` files and 58
  without direct workflow invocation. Many are legitimate manual research/audit
  validators; the gap is that their tier is not explicit.
- A 2026-07-06 scan found high-volume `docs/latest` and `output/latest`
  generated artifacts that exceed the current artifact-level lineage coverage.
  The existing inventories cover major surfaces and classes, but cleanup and
  stale-artifact decisions still need a stronger generated-artifact lineage
  model.

## Follow-Up PR Order

1. Fallback semantics registry and validator.
2. Per-model condition/scoring owner-map validator or module split.
3. Validator tier registry and workflow coverage validator.
4. Artifact lineage v2 for generated latest/history artifacts.
5. Extend machine-readable role/section manifests to non-daily PDFs and packets.

No row in this audit authorizes deleting artifacts, changing model behavior,
changing PDF layout, or promoting research-only evidence into production.
