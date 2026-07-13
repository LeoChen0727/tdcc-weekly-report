# output/latest Artifact Layout

This document defines where generated artifacts belong under `output/latest`.
It is a layout rule only. It does not define stock selection, model parameters,
ranking, scoring, or PDF content.

## Root Directory

The `output/latest` root is reserved for machine-readable latest aliases and
pipeline handoff files. Root artifacts may include stable CSV, JSON, MD, TXT,
and compatibility PDF aliases when downstream automation, validators, packets,
or raw-health checks still depend on those exact paths.

Allowed root examples:

- `output/latest/data_freshness_latest.csv`
- `output/latest/market_session_status_latest.json`
- `output/latest/daily_market_summary_latest.pdf`
- `output/latest/daily_market_full_latest.pdf`
- `output/latest/chatgpt_daily_report_packet_latest.txt`
- `output/latest/report_manifest_latest.json`

Root-level files must remain stable aliases, not human-facing delivery copies
with changing date semantics.

## Human-Facing PDFs

Human-facing official or published PDFs belong under:

```text
output/latest/published_reports/<report_family>/
```

Examples:

- `output/latest/published_reports/daily_market/`
- `output/latest/published_reports/tdcc_weekly/`

Date-stamped human-facing PDF filenames must use the formal source data date
for that report family. For daily market artifacts, use
`output/latest/data_freshness_latest.csv` field `main_price_date`, not wall-clock
runtime.

## Pipeline And Validator Artifacts

CSV, JSON, MD, and TXT artifacts that are consumed by pipeline steps,
validators, packets, readiness gates, or raw-health checks may remain in
`output/latest` until their consumers are moved in a reviewed PR.

Do not move a pipeline dependency only because it is human-readable. First
identify the producer, consumer, validator, packet, workflow, and lifecycle
inventory entries that depend on the path.

`output/latest/market_session_status_latest.json` is the machine handoff for the
four-state Taiwan market-session decision and `expected_main_price_date`. The
official six-PDF entrypoint must also refresh the live official calendar before
accepting this committed state, so a stale status file and stale freshness file
cannot validate each other.

## TDCC Weekly Artifacts

Machine-facing TDCC weekly CSV/MD artifacts should migrate toward:

```text
output/latest/tdcc_weekly/
```

Canonical subdirectories for future TDCC weekly cleanup are:

- `output/latest/tdcc_weekly/history/`
- `output/latest/tdcc_weekly/holder_flow/`
- `output/latest/tdcc_weekly/rankings/`
- `output/latest/tdcc_weekly/reports/`
- `output/latest/tdcc_weekly/tracking/`
- `output/latest/tdcc_weekly/status/`
- `output/latest/tdcc_weekly/diagnostics/`

The current root `output/latest/tdcc_*` CSV/MD files are compatibility aliases
when TDCC weekly builders, validators, workflows, rules, packets, raw links, or
docs/latest still depend on those exact paths. Do not retire a TDCC weekly root
alias until the producer, validator, workflow staging, docs/latest mirror, and
raw-link packet surfaces are updated in the same reviewed PR.

TDCC weekly human-facing PDFs belong under:

```text
output/latest/published_reports/tdcc_weekly/
```

The detailed TDCC weekly root-alias plan is:

```text
docs/tdcc_weekly_artifact_relocation_plan_20260621.md
```

## Individual Stock Reports

Individual-stock human and packet-facing artifacts belong under:

```text
output/latest/individual_stock_reports/
```

Canonical subdirectories:

- `output/latest/individual_stock_reports/chatgpt_packets/`
- `output/latest/individual_stock_reports/price_windows/`
- `output/latest/individual_stock_reports/tdcc_windows/`

Individual-stock index and read-protocol CSV/MD files also belong directly
under `output/latest/individual_stock_reports/`, not the `output/latest` root.

The `output/latest` root may retain machine aliases that are shared with daily
pipeline, raw-health, or sell-strategy checks, such as technical snapshots,
raw-data fetch status, stock-price manifests, or sell-strategy performance
summaries. These aliases are not the per-stock report payload directory.

## PDF Layout Experiments

PDF layout experiments, screenshots, previews, ad hoc render checks, and lab
outputs must not be written under `output/latest`.

Use a lab, temporary, or explicitly documented output location instead, such as:

- `pdf-layout-lab/`
- a task-specific output directory
- a documented temporary validation directory

## Deletion And Retirement

Do not manually delete an uncertain `output/latest` artifact.

Before moving, renaming, retiring, or deleting any artifact whose consumers are
not fully known, first update or create lifecycle evidence in:

- `config/report_artifact_lineage.csv`
- `config/repo_file_lifecycle_inventory.csv`
- the relevant validator or test

A cleanup PR must state whether the artifact is:

- a machine compatibility alias;
- a human-facing published report;
- a pipeline or validator dependency;
- a packet/readiness/raw-health dependency;
- deprecated but still required for compatibility;
- safe to retire.
