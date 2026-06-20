# TDCC Weekly Artifact Relocation Plan - 2026-06-21

- source_inventory: `production/tdcc-daily-production/config/output_latest_artifact_inventory.csv`
- filter: `owner_lane=tdcc_weekly`
- artifact_count: `42`
- relocated_now: `0`
- compatibility_alias_retained: `42`
- root_csv_md_reduction_now: `0`
- planned_machine_container: `output/latest/tdcc_weekly/`
- published_pdf_container: `output/latest/published_reports/tdcc_weekly/`
- boundary: this plan does not move individual-stock artifacts, research/backtest artifacts, daily market PDFs, stale/unknown artifacts, or daily six-PDF ranking/buy/sell logic.

## Decision

The 42 audited TDCC weekly CSV/MD artifacts are not safe to remove from
`output/latest` root in a single relocation PR. Current TDCC weekly builders,
validators, workflows, `rules/tdcc_weekly_rules.md`, generated packets, and raw
link surfaces still use the root latest paths as compatibility aliases.

This PR therefore records the target layout and retained-alias contract first.
The next safe migration PR must update producer, validator, workflow staging,
docs/latest mirroring, and raw-link packet references together, then prove root
alias parity before any root alias is retired.

## Target Layout

Machine-facing TDCC weekly latest artifacts should migrate behind a reviewed
producer/consumer change to:

```text
output/latest/tdcc_weekly/
output/latest/tdcc_weekly/history/
output/latest/tdcc_weekly/holder_flow/
output/latest/tdcc_weekly/rankings/
output/latest/tdcc_weekly/reports/
output/latest/tdcc_weekly/tracking/
output/latest/tdcc_weekly/status/
output/latest/tdcc_weekly/diagnostics/
```

Human-facing TDCC weekly PDFs already belong under:

```text
output/latest/published_reports/tdcc_weekly/
```

## Compatibility Aliases Retained

All 42 root paths stay as compatibility aliases in this phase. The retained
aliases include four groups:

- TDCC weekly report contract: report-ready CSV/MD files, section manifest,
  weekly candidate MD, validation MD, report MD, and run status.
- TDCC holder-flow/tracking support: tracking packet, ranking tables, ABM,
  phase distribution, risk list, signal effectiveness, signal performance,
  stock-history manifest, and backfill manifest.
- Cross-lane TDCC/research support: overheated short-term edge artifacts remain
  root aliases until TDCC and research consumers are split in a dedicated PR.
- Out-of-scope research/backtest artifacts: `tdcc_weekly_ranking_backtest_*`
  remain untouched here because active consumers are in the research/backtest
  workflow and validator.

## Full 42-Artifact Plan

The exact source path, target path, decision, and retention reason for every
audited TDCC weekly artifact is in:

```text
docs/tdcc_weekly_artifact_relocation_plan_20260621.csv
```

## Future Migration Gate

A future PR may reduce `output/latest` root count only after it proves all of
the following:

- TDCC producers write canonical copies under `output/latest/tdcc_weekly/`.
- TDCC validators read canonical paths and verify root compatibility aliases.
- `.github/workflows/tdcc_weekly.yml` stages canonical TDCC weekly paths plus
  any deliberately retained root aliases.
- `docs/latest` and raw-link packet surfaces point to canonical paths or clearly
  documented compatibility aliases.
- `rules/tdcc_weekly_rules.md` keeps the report-ready signal-date contract and
  section-manifest contract intact.
- `python scripts/validate_daily_production_boundaries.py` passes.
- `python scripts/validate_repo_file_lifecycle_inventory.py` passes.
- `python -m pytest tests/test_tdcc_weekly_delivery_filenames.py -q` passes.

## Explicit Exclusions

This plan does not handle:

- individual-stock artifacts, already handled by PR #167;
- research/backtest artifacts, already handled by PR #169 except rows that still
  require a research-owned compatibility plan;
- daily market PDFs, already handled by PR #164;
- stale/unknown root artifacts;
- TDCC model, ranking, threshold, scoring, candidate, or PDF content logic.
