# Repo Production Inventory

This repository uses an explicit production inventory so script ownership and
workflow boundaries are validated by code, not by memory or convention.

Authoritative manifest:

- `config/repo_production_inventory.csv`
- `config/repo_file_lifecycle_inventory.csv`

Validator:

- `python scripts/validate_repo_production_inventory.py`
- `python scripts/validate_repo_file_lifecycle_inventory.py`
- `python scripts/validate_repo_semantic_integrity.py`
- `python scripts/validate_repo_advanced_integrity.py`

Report artifact lineage manifest:

- `config/report_artifact_lineage.csv`

## Inventory Contract

Every tracked root-level `*.py`, every tracked `scripts/**/*.py`, every tracked
`tests/**/*.py`, every tracked non-Python executable script such as `.sh` or
Apps Script `.gs`, and every tracked `.github/workflows/*.yml` or `.yaml` file
must have one manifest row.

Required fields:

- `path`: repository-relative path.
- `kind`: `python`, `test_python`, `executable_script`, or `workflow`.
- `owner`: business or infrastructure lane owner.
- `status`: `active`, `manual_diagnostic`, or `legacy_deprecated`.
- `purpose`: human-readable purpose.
- `allowed_workflows`: semicolon-separated workflow allow list for non-shared
  scripts when a tighter allow list is required.
- `allowed_stage_patterns`: explicit stage patterns expected inside workflow
  files when a workflow commits generated outputs.

Any new script, test, executable helper, or workflow without an inventory row
fails validation.

The validator also scans active guidance text so docs and generated latest
artifacts cannot point users to retired executable entrypoints. The active
guidance scan includes:

- `AGENTS.md`
- `README.md`
- `rules/**/*.md`
- root-level `docs/*.md` and `docs/*.txt`
- `docs/latest/**/*.md` and `docs/latest/**/*.txt`
- `output/latest/**/*.md` and `output/latest/**/*.txt`

Historical folders are intentionally not treated as live entrypoint guidance.

## Lifecycle Contract

`config/repo_file_lifecycle_inventory.csv` is the deletion-readiness manifest.
It extends the owner inventory with executable evidence:

- workflow callers;
- AST import callers;
- tests that reference a script;
- active guidance documents that mention a path;
- report artifacts written by a producer;
- source artifacts read by a producer;
- keep reason;
- delete reason;
- removal risk.

Lifecycle status values:

- `active`: still part of a formal lane or validator surface.
- `manual_diagnostic`: manually invoked diagnostic surface, not production.
- `generated_artifact`: generated active guidance checked for stale commands.
- `historical_artifact`: historical record, not active guidance.
- `deprecated`: retained temporarily with no production workflow caller.
- `delete_candidate`: verified no workflow/import/docs runtime reference and
  ready for scoped removal review.

Any `delete_candidate` or `deprecated` file that is invoked by workflow or AST
import fails validation. Active guidance also fails if it names retired formal
daily PDF artifact paths.

## Lane Owners

- `daily_production`: daily candidate generation, daily model layer, and
  ChatGPT-side daily report route.
- `research_backtest`: research-only parameter studies, backtests, operation
  readiness evidence, and historical performance outputs.
- `tdcc_weekly`: TDCC holder-flow, weekly candidate reports, TDCC-specific
  tracking artifacts, and bounded TDCC history gap repair. The GitHub weekly
  report workflow remains the repo artifact production entrypoint; Codex report
  automation must run `scripts/run_tdcc_weekly_report_entrypoint.py` from an
  isolated worktree and pass the fixed holder-flow worktree through
  `--delivery-root`. The isolated checkout owns the clean `origin/main` source
  gate, while the fixed worktree is only the final delivery target.
  `scripts/repair_tdcc_monthly_history_gaps.py`
  is the source-integrity entrypoint for current-month TDCC history repairs
  before the current week.
- `individual_stock`: single-stock packet/report generation and single-stock
  raw-data indexes.
- `catalyst_event`: catalyst and event-calendar data builders and validators.
- `market_risk`: market regime, sentiment, timing, and index-context surfaces.
- `warrant`: warrant daily fetch, warrant flow, and warrant auxiliary outputs.
- `official_price_data`: official TWSE/TPEx daily price fetch and price-history
  maintenance. `scripts/repair_recent_daily_price_gaps.py` is the source
  integrity entrypoint for proactive recent daily price gap repair before
  report generation; workflow/Apps Script scheduling is handled separately by
  the workflow automation lane.
- `current_holdings`: current-holdings observation workflow.
- `diagnostics`: manual diagnostic scripts and workflows.
- `repo_infrastructure`: validators, source freshness gates, publish checks,
  and low-level repository plumbing.

## Manual Research Surfaces

The W-bottom research builders below are manual research/backtest surfaces.
They are retained to reproduce review packets, filter grids, left-anchor
audits, and event replays for `w_bottom_right_side` and
`neckline_volume_breakout_confirmation`. They are not production model
entrypoints, must not be called by daily production workflows, and must not
write research variants into production baselines:

- `scripts/build_w_bottom_candidate_definition_audit.py`
- `scripts/build_w_bottom_candidate_filter_grid.py`
- `scripts/build_w_bottom_candidate_quality_audit.py`
- `scripts/build_w_bottom_core_mainstream_exclude_wv_review_packet.py`
- `scripts/build_w_bottom_left_anchor_rule_grid.py`
- `scripts/build_w_bottom_left_anchor_rule_replay.py`
- `scripts/build_w_bottom_nearest_micro_anchor_event_replay.py`
- `scripts/build_w_bottom_nearest_micro_anchor_chart_review_packet.py`
- `scripts/build_w_bottom_combined_condition_backtest.py`
- `scripts/build_w_bottom_split_entry_outcome_backtest.py`
- `scripts/build_w_bottom_early_entry_parameter_grid.py`
- `scripts/build_w_bottom_early_entry_stop_loss_audit.py`
- `scripts/build_w_bottom_early_entry_outcome_diagnostics.py`
- `scripts/build_w_bottom_early_entry_stability_audit.py`
- `scripts/build_w_bottom_early_entry_data_coverage_audit.py`
- `scripts/build_w_bottom_early_entry_backfill_feasibility_audit.py`
- `scripts/build_w_bottom_observation_confirmation_audit.py`
- `scripts/build_w_bottom_path_quality_filter_audit.py`
- `scripts/build_w_bottom_price_level_audit.py`
- `scripts/build_w_bottom_price_level_filter_grid.py`
- `scripts/build_w_bottom_wv_filter_stability_grid.py`

## Boundary Rules

The validator enforces these repository-wide rules:

- Daily production workflows may call daily, official price, warrant, catalyst,
  market-risk, and repo-infrastructure scripts only. They must not run TDCC
  weekly report builders or stage TDCC weekly PDFs.
- Research workflows may publish research artifacts, but must not mutate
  production config/source paths or rebuild daily PDF entrypoints.
- TDCC weekly workflows must not run or stage daily PDF outputs.
- Individual-stock workflows must not publish full-market daily report outputs.
- Warrant workflows must not stage source files or workflow files as part of a
  data refresh.
- Deprecated scripts cannot be invoked by workflows.
- Active guidance must not instruct users to run retired or renderer-only daily
  PDF entrypoints. The formal daily PDF entrypoint is
  `scripts/run_chatgpt_daily_report_entrypoint.py`; the renderer path and repo
  market artifact builder path may be mentioned only as non-entrypoint files.

The semantic integrity validator additionally enforces:

- AST import/dependency boundaries between daily production, research/backtest,
  TDCC weekly, individual stock, PDF/report, and infrastructure lanes.
- Production report date-source rules: formal report dates must come from
  freshness/source gates, not wall-clock `YYYYMMDD` fallbacks.
- Production data-source rules: daily production cannot read research/history
  artifacts unless a specific adapter allowlist exists.
- Report artifact lineage: publishable packets, reports, PDFs, and daily adapter
  artifacts must have a producer, source artifact list, validator, publisher,
  owner, and public surface.
- Daily model parity: every production core model must have an explicit
  research/backtest baseline status of `production_parity`,
  `production_proxy`, or `proxy_only`; proxy rows must state blockers.
- Orphan audit: active scripts without workflow/import/guidance references must
  be marked deprecated/manual or wired explicitly.
- Semantic assertions for stock taxonomy, daily volume operation rows, forbidden
  decision-layer report tokens, raw operation slug leakage, and shared model
  score profiles.

The advanced integrity validator adds the next layer of executable contracts:

- External daily report archive contract:
  `scripts/archive_daily_official_report_bundles.py` copies only bundles older
  than the authoritative current and baseline dates to an operator-supplied
  external root. It is a manual, copy-only producer and is not a workflow
  publisher or a cleanup command.

- Runtime file lineage contract:
  `config/runtime_file_lineage_contract.csv` defines expected read/write
  surfaces for formal producers, and `scripts/trace_runtime_file_lineage.py`
  can trace a Python entrypoint under monkeypatched file APIs.
- PDF golden regression contract:
  `config/pdf_golden_regression_contract.csv` defines the six formal
  ChatGPT-side PDFs, their builder functions, required sections, forbidden raw
  tokens, page bounds, and output route.
- Historical replay semantic contract:
  `config/historical_replay_semantic_contract.csv` validates recent model
  snapshot history for required columns, date consistency, report-line
  membership, model IDs, and absence of decision-layer columns.
- Machine-readable model condition spec:
  `config/daily_model_condition_spec.csv` maps production model IDs to
  condition functions, score functions, score profiles, and research parity
  statuses. The validator compares this file against the production AST and
  latest parity output.
- External source contract:
  `config/external_data_source_contract.csv` binds external data surfaces to
  freshness/readiness columns or JSON status paths, plus producer and validator
  ownership.

## Workflow Gate

The repo-wide validator is run by:

- `.github/workflows/daily_full_pipeline.yml`
- `.github/workflows/research_backtest_pipeline.yml`
- `.github/workflows/tdcc_weekly.yml`
- `.github/workflows/tdcc_history_backfill.yml`
- `.github/workflows/repair_tdcc_monthly_history_gaps.yml`
- `.github/workflows/individual_stock_report.yml`
- `.github/workflows/individual_stock_data_refresh.yml`
- `.github/workflows/warrant_flow.yml`
- `.github/workflows/repair_recent_daily_price_gaps.yml`

Daily Full Pipeline remains the main production gate. The other workflow gates
prevent lane-specific PRs or manual runs from reviving old shared paths.
