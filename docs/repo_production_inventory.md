# Repo Production Inventory

This repository uses an explicit production inventory so script ownership and
workflow boundaries are validated by code, not by memory or convention.

Authoritative manifest:

- `config/repo_production_inventory.csv`

Validator:

- `python scripts/validate_repo_production_inventory.py`
- `python scripts/validate_repo_semantic_integrity.py`

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

## Lane Owners

- `daily_production`: daily candidate generation, daily model layer, and
  ChatGPT-side daily report route.
- `research_backtest`: research-only parameter studies, backtests, operation
  readiness evidence, and historical performance outputs.
- `tdcc_weekly`: TDCC holder-flow, weekly candidate reports, and TDCC-specific
  tracking artifacts.
- `individual_stock`: single-stock packet/report generation and single-stock
  raw-data indexes.
- `catalyst_event`: catalyst and event-calendar data builders and validators.
- `market_risk`: market regime, sentiment, timing, and index-context surfaces.
- `warrant`: warrant daily fetch, warrant flow, and warrant auxiliary outputs.
- `official_price_data`: official TWSE/TPEx daily price fetch and price-history
  maintenance.
- `current_holdings`: current-holdings observation workflow.
- `diagnostics`: manual diagnostic scripts and workflows.
- `repo_infrastructure`: validators, source freshness gates, publish checks,
  and low-level repository plumbing.

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

## Workflow Gate

The repo-wide validator is run by:

- `.github/workflows/daily_full_pipeline.yml`
- `.github/workflows/research_backtest_pipeline.yml`
- `.github/workflows/tdcc_weekly.yml`
- `.github/workflows/tdcc_history_backfill.yml`
- `.github/workflows/individual_stock_report.yml`
- `.github/workflows/individual_stock_data_refresh.yml`
- `.github/workflows/warrant_flow.yml`

Daily Full Pipeline remains the main production gate. The other workflow gates
prevent lane-specific PRs or manual runs from reviving old shared paths.
