# output/latest cleanup round 1 summary - 2026-06-21

This summary closes `output/latest` cleanup round 1 as a coordination record.
It does not approve permanent deletion, broad artifact relocation, or daily PDF
business-logic changes.

## Completed PRs

| PR | Scope |
| --- | --- |
| #164 | daily market PDF lifecycle |
| #167 | individual_stock artifact relocation |
| #168 | TDCC weekly lifecycle / staging metadata |
| #169 | research_backtest artifact relocation |
| #170 | TDCC weekly artifact relocation plan / compatibility alias |
| #171 | diagnostic_stale_candidate review / relocation |
| #172 | unknown artifact review |

## Final output/latest root CSV/MD count

`output/latest` root CSV/MD final count after round 1: `264`.

## Completed cleanup

- `individual_stock` artifacts were moved under `output/latest/individual_stock_reports/`.
- Low-risk `research_backtest` artifacts were moved under `output/latest/research_backtest/`.
- TDCC weekly published PDFs and compatibility alias rules were documented.
- Diagnostics moved or retained under the diagnostic review rules.
- Unknown 30 artifacts were reviewed and reclassified.

## Remaining follow-up items

- quarantine_candidate: `3`
- manual_review_required=true: `4`
- research/backtest follow-up: `6`
- TDCC root compatibility alias: `42`
- daily market compatibility alias

## Next cleanup routing

- Daily cleanup, quarantine candidates, manual review, or daily market aliases:
  use `production/tdcc-daily-production`.
- Research/backtest follow-up:
  use `research/tdcc-research-backtest`.
- TDCC weekly root compatibility aliases:
  use `production/tdcc-holder-flow`.
- Individual stock artifacts:
  use `production/tdcc-holder-flow`.
- Cross-lane coordination only:
  use `projects/taiwan-stock-recommendation` or the Codex project governance
  conversation, then route work to the owning lane.

## Boundaries

- Do not permanently delete artifacts from `output/latest` based only on file
  names or File Explorer appearance.
- Do not open another broad mixed cleanup PR.
- Future cleanup must be small, owner-scoped, and backed by current reference
  checks and validator evidence.
- Do not modify daily six-PDF stock selection, ranking, buy/sell, or risk logic
  as part of artifact cleanup.
- Do not move TDCC, research, or individual-stock artifacts from the daily lane
  unless the task explicitly belongs to that lane and the owning validator
  supports the move.

## Validation baseline

Latest post-merge validation from #172 passed:

- daily production boundary validation
- repo file lifecycle inventory validation
- repo semantic integrity validation
- repo advanced integrity validation
- PDF production inventory validation
- ChatGPT-side PDF contract validation
- pytest coverage for daily boundaries, lifecycle inventory, and PDF inventory
