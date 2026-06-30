# AGENTS.md

精確.按照規則辦事

## Code Change Completion Boundary

For code conversations, do not call a task complete just because code was edited,
debugged, committed, pushed, or a branch check passed.

When the requested code change is intended to land in `main` or the configured
primary branch, completion requires commit, push, PR/branch validation, merge to
`main`, merge commit evidence, post-merge `main` workflow/tests/validators, and
inspection of the final runtime behavior or user-facing artifacts when outputs
are affected.

If the requested scope stops before merge, report the narrower state such as
`local_validated`, `committed`, `pr_open`, `branch_action_passed`, or
`merged_pending_main_validation`. Do not use `complete`, `done`, `fixed`,
`ready`, or equivalent wording unless the requested scope's real stop condition
has been met.

`Debug complete` means the relevant failure mode was reproduced or otherwise
identified, the fix was verified against that failure mode, appropriate
regression coverage or validator evidence exists, and any remaining unverified
risk is reported instead of hidden.

## Traditional Chinese User-Facing Language Boundary

All user-facing replies from this worktree must use Traditional Chinese by
default, including explanations, status updates, validation summaries, PR
summaries, blockers, handoffs, and final responses.

Do not write user-facing prose in English or Simplified Chinese unless the user
explicitly asks for that language in the current task.

Preserve exact technical identifiers in their original form, including file
paths, commands, branch names, workflow/check names, repository names,
filenames, code symbols, quoted logs, validator names, and PR titles. Explain
their meaning in Traditional Chinese around those identifiers.

## Default Engineering Rule

All business-facing code in this repository defaults to independent ownership.

Do not share business-semantic code across unrelated reports, models, parameters,
ranking rules, filters, PDF layouts, packets, validations, workflows, or output
contracts unless the coupling is explicitly documented in repo rules and the
user has approved it.

Shared code is allowed only for low-level technical utilities that do not decide
business content, such as file reads, type conversion, date formatting, font
registration, basic table drawing, PDF file writing, and generic validation
plumbing.

Before editing any shared function, parameter table, helper, or workflow step,
first identify which reports, models, outputs, and validations depend on it. If
the requested change is for one surface, split the shared code path before
changing behavior.

Stock model parameters, thresholds, scoring weights, ranking rules, and gates
must be independent by default. They may be shared only when the same backtest
evidence explicitly proves that the models should share the parameter, and that
relationship is encoded in source rules and tests.

Changing A must not silently change B. If A and B are intentionally coupled,
state that coupling before making the change.

This is a repository-level engineering gate, not a style preference. Daily
production validation must run `scripts/validate_repo_code_isolation_policy.py`
and `scripts/validate_chatgpt_side_pdf_layout_independence.py`; weakening these
guards requires changing the validator and tests in the same reviewed PR.

## Formal Daily Model Change Rule

Formal daily Taiwan stock recommendation model, ranking, or scoring changes
belong to the `daily_model_maintenance` lane:

```text
C:\Users\p4693\Documents\Codex\projects\taiwan-stock-recommendation\maintenance\daily-model-maintenance
```

When changing formal production model conditions, ranking, or scoring, update
`config/stock_model_contract_registry.csv` in the same change when the contract
surface is affected.

After any formal daily model/ranking/scoring change, check research/backtest
parity. If research/backtest parity is inconsistent, do not copy research
recommendations or variants into the production baseline. Report that the
`research_backtest` lane must be synchronized, or create an explicit
promotion/sync PR when that is requested.

Required validation for formal daily model/ranking/scoring changes:

```text
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_daily_pdf_contract_consumers.py
python scripts/validate_research_against_stock_model_contract.py
python scripts/validate_daily_model_research_parity.py
```

## Official Daily PDF Entrypoint

Official ChatGPT-side daily PDF generation must start from:

`python scripts/run_chatgpt_daily_report_entrypoint.py`

This entrypoint gates on `origin/main`, verifies readiness through
`output/latest/data_freshness_latest.csv` and
`output/latest/READ_ME_FIRST_DAILY_REPORT.txt`, creates a temporary clean source
worktree, and then invokes the renderer. Do not manually decide the report date
from OneDrive/helper copies, Pages, raw README text, or local `output/latest`.

`scripts/generate_chatgpt_side_daily_reports.py` is the renderer, not the
official entrypoint. Its CLI is blocked unless the official entrypoint invokes
it.

## Repository PDF Contract And Independence Rules

This thread is governed by the repository PDF independence rule and the Daily
PDF Contract PR scope. The higher-level project rule is that every production
PDF and packet in this repository must have independent business ownership. The
six official daily PDFs listed below are the required minimum contract set for
this Daily Full Pipeline PR; they are not the limit of the repository-wide PDF
independence requirement.

The goal of this PR is to build an end-to-end contract and layout safety net for
the official daily production PDFs. Do not change stock models, ranking logic,
scoring, backtest logic, selection conditions, or PDF visual/content design
unless the user explicitly orders that separate change.

All production PDFs must be treated as separate production surfaces. For this
Daily PDF Contract PR, the six required official daily PDFs are:

1. Mainstream daily recommendation digest.
2. Mainstream full candidate list.
3. Non-mainstream daily recommendation digest.
4. Non-mainstream full candidate list.
5. Warrant market support analysis.
6. Market risk and index/options background.

Each production PDF must have independent template, renderer, and content
section assembly ownership. The six daily PDFs above must satisfy this
independence immediately in this PR. Shared code is allowed only for low-level,
business-neutral utilities such as font registration, page size constants, basic
style constants, file IO, and generic PDF validation plumbing. Do not share
field selection, section composition, sorting, table content, model blocks, or
operation blocks through one content renderer.

Changing PDF A must not silently affect PDF B. If two PDFs are intentionally
changed together, that coupling must be stated before implementation and must
be covered by validation.

The formal Daily PDF contract validator for this PR must read at least the six
official generated production PDFs, not single-page previews. It must use
`pypdf` to confirm each PDF opens, has a reasonable page count, and has
extractable text. It must verify that digest PDFs and full-list PDFs are not
crossed, that required first-page and candidate-area sections such as `newly
listed` and `consecutive listed` remain present, and that mainstream,
non-mainstream, warrant, and market-risk PDFs do not contaminate each other.

Daily Full Pipeline must run the PDF contract validator after official PDF
generation. Tests must prove that the workflow invokes the validator and that
the validator covers all six PDFs, digest/full boundaries, and newly-listed /
consecutive-listed section checks.

Do not modify `generate_repo_chatgpt_side_reports.py` for this work. Do not put
research or backtest artifacts directly into production PDFs.

Current known integration status: `model_operation_readiness_latest.csv` may
show `pdf_integration_status=pending_pdf_renderer` and
`packet_integration_status=pending_packet_renderer`; that is expected until the
official PDF/packet renderer integration is completed. When daily PDF rendering
uses readiness data, buy ranking must be driven by `buy_rank_eligible=True`,
not only by `approved_for_daily`, because pending rows can still contain module
approval fields.

Daily stock model PDF sections and tables must be stable and complete. Each
active PDF-eligible or presentation-allowed model for the applicable
mainstream/non-mainstream report line must render a model block even when it has
zero candidate rows that day. Zero-candidate model sections must use the
existing business-facing candidate/operation table style and include the exact
text `本日無股票推薦`. Do not add a separate technical model status, readiness,
candidate-count, or PDF integration summary table to the PDF. This is a PDF
presentation contract only; it must not create synthetic candidates or change
model condition, scoring, ranking, buy/sell, or research/backtest behavior.

Full-list PDFs can be large. Page-count validation must define an explicit
reasonable range instead of treating the current high page count as an implicit
failure.

## PDF Delivery Link Reporting Rule

When a task produces or prepares PDF deliverables for the user, the final reply
must include directly clickable links to the generated PDF files whenever
possible. At minimum, include a clickable link to the folder that contains the
PDF deliverables. Local links must use absolute workspace paths so the user can
open the folder or files with one click.

