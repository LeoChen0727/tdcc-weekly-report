# Workspace Cleanup Policy

This policy separates tracked repository lifecycle work from local generated-output cleanup.

## Scope

- Tracked code, tests, workflows, rules, docs, and config files use the normal PR, CI, and `config/repo_file_lifecycle_inventory.csv` lifecycle.
- Untracked or ignored generated outputs may be inspected by workspace cleanup tooling.
- Suspicious code is never moved to `_workspace_quarantine/`; code cleanup must be handled by a PR.
- Cleanup must not be wired into `scripts/run_chatgpt_daily_report_entrypoint.py`.
- Cleanup must not run automatically from `Daily Full Pipeline`.
- `config/` is a cleanup hard block. Governance PRs may still intentionally edit `config/*.csv`.

## Phase Rules

- Phase 1 adds policy, schema, dry-run planning, validation, tests, and audit summaries only.
- Phase 1 does not add `scripts/apply_workspace_cleanup.py`.
- Phase 1 does not delete, move, or quarantine files or folders.
- Phase 2 is human review only.
- Phase 3 adds apply/quarantine tooling.
- Phase 4 performs the first cleanup PR. Permanent delete is limited to truly empty directories; all other output cleanup starts with quarantine.
- Every ChatGPT-side daily PDF report kind must retain at least the latest PDF as a layout-comparison baseline before any older PDF output can be quarantined or deleted.

## Protected Paths

Protected paths are defined in `config/workspace_cleanup_protected_paths.csv`.

The planner and validator must hard block protected paths, including:

- `.git/`
- `.github/workflows/`
- `config/`
- `rules/`
- `PROJECT_RULES.md`
- `output/latest/`
- `docs/latest/`
- `scripts/run_chatgpt_daily_report_entrypoint.py`
- `scripts/generate_chatgpt_side_daily_reports.py`
- legacy `generate_repo_chatgpt_side_reports.py` locations if present

Dynamic evidence, such as official PDF folders, replay evidence, runtime manifests, and freshness-gate evidence, is detected by the planner rather than hard-coded as a static protected path.

## PDF Layout Baseline Retention

The cleanup planner must detect PDF report kinds across `chatgpt_side_outputs*` and mark the latest PDF for each report kind as a layout baseline.

Baseline PDFs are not retained because the report content has long-term business value. They are retained so later PDF runs can be compared against the latest known layout and catch accidental template, pagination, section, or typography drift.

Rows containing a latest layout baseline must use `planned_action=keep`. Apply tooling must refuse to quarantine or delete those rows unless a newer replacement baseline is present in the same verified manifest.

## Planner Contract

`scripts/plan_workspace_cleanup.py` is dry-run only.

It may scan `chatgpt_side_outputs*` by filesystem because these outputs are ignored by git. It must not scan `_workspace_quarantine/` as a cleanup candidate. A manifest row must contain an exact repository-relative path, not a wildcard.

`latest_manifest.json` is only a pointer. Tools may accept it, but must first resolve the full manifest, verify `report_id`, and verify the manifest hash before using any row for a decision.

If a candidate root is a symlink, junction, reparse point, or permission-denied root, the planner fails closed and must not emit an applyable `latest_manifest.json`. If a descendant has a permission or reparse issue, that candidate is downgraded to `unknown_quarantine_candidate` with `planned_action=report_only`.

Validation is handled by `scripts/validate_workspace_cleanup_policy.py`.

## Apply Contract

Apply tooling is intentionally out of scope for Phase 1.

When introduced later, apply must:

- Default to validate-only.
- Require `--apply` to do anything.
- Require `--allow-delete` for permanent deletion.
- Recompute fingerprints before action.
- Refuse tracked code and protected paths.
- Resolve `latest_manifest.json` to the full manifest before any decision.
- Recheck empty directories using the live filesystem before deletion.
- Quarantine non-empty cleanup targets first, with a default 14-day `expires_at`.
- Create a one-time reminder after files are actually moved to `_workspace_quarantine/`, using the cleanup report id and `QUARANTINE_MANIFEST.csv` as the review target.

## Reporting

Full local reports stay in ignored `workspace_cleanup_reports/`.

Tracked summaries may be written only when explicitly requested with `--history-summary`; overwriting a tracked summary requires `--overwrite-history-summary`.
