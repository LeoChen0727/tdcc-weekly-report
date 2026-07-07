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

## Completion Claim Evidence Gate

For this repository, a final response may use `completion_state=complete` only
when the evidence is listed in the response itself. The response must include:

- PR number and URL.
- Merge commit on `main`.
- Post-merge official `main` workflow run id and conclusion when workflows are
  part of the requested completion boundary.
- Local post-merge validators or tests that were actually run.
- Runtime behavior or user-facing artifact inspection result when outputs,
  PDFs, packets, reports, or model presentation are affected.
- Direct clickable links to generated PDF files, or at minimum the containing
  folder plus exact PDF filenames, when PDF deliverables or PDF presentation are
  affected.
- Final `git status --short --branch` state.
- `remaining blocker`, explicitly set to `none` only when no known blocker
  remains.

If any required evidence is missing, stale, branch-only, inferred, or not yet
verified after merge, do not use `completion_state=complete`. Use a narrower
state such as `local_validated`, `pr_open`, `branch_action_passed`,
`merged_pending_main_validation`, or `main_workflow_passed_pending_artifact_inspection`.

For formal daily model promotions, `complete` is forbidden until the model
contract, operation readiness, dedicated operation-row adapter, PDF/packet
consumer contract, and post-merge official workflow evidence all match the
requested scope. A model being approved, a readiness row being marked
`pdf_integrated_daily_adapter`, or a dedicated adapter artifact existing is not
by itself PDF presentation completion. If PDF output is affected, the final
evidence must show that the renderer consumed the dedicated adapter, that the
PDF contract/replay validation passed after merge, and that the final response
contains the produced PDF link evidence. If no generated PDF file or PDF folder
link is available for inspection, `completion_state=complete` is forbidden.

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

When discussing any revenue-driven model, revenue condition, or revenue
interpretation, explicitly separate monthly revenue from quarterly/annual
financial-statement fundamentals. The discussion must state whether EPS, gross
margin, operating margin, operating income, non-operating income, net income,
or annual financial statement fields should be included in scope. If they are
needed, create or route to a formal shared objective financial-statement data
layer first; do not infer those fields from monthly revenue, catalyst labels,
PDF text, or latest-only artifacts. Until that data layer exists and passes
point-in-time coverage validation, those fields remain advisory/disclosure
context and must not become production gates, scores, rankings, PDF metrics, or
promotion evidence.

Formal operation buy/sell/stop/profit-taking rules must be close-confirmed by
default. A formal daily operation model may use only the next trading day open
after a qualifying close confirmation, the same-day close when the rule
explicitly waits for that close, or a fixed future close exit as the realized
operation price. It must not use intraday high/low as formal entry, exit, stop,
profit-taking, win, failure, or realized-return prices. Intraday high/low may
be used only for research-only observation, MFE/MAE, risk audit,
liquidity/slippage diagnostics, candle-quality features, or non-operation watch
statistics; it must be labeled advisory and cannot support promotion by itself.
Existing approved operation contracts with intraday stop or trigger semantics
are contract exceptions/gaps that must be listed explicitly, cannot be copied to
new models, and require a model-specific promotion PR before the behavior is
changed. For `price_pullback_23ema`, the earlier intraday previous-high touch
research result is not a formal v1 operation return basis; formal discussion
must keep intraday previous-high touch as `research_only_intraday_trigger` when
testing same-day close exits, or use close-confirmed previous-high breakout with
next trading day open exit semantics. `close_prev20_high_break_same_day_close`
is invalid because the close-confirmed breakout is known only after that close.

Daily model research/backtest conclusions must include a numerical anomaly
check before interpreting performance. The first trigger is the number itself,
not an assumed cause: any single trade, row, stock, date, return, price, volume,
or small group of rows that looks abnormal, dominates an average, changes a
conclusion, or is inconsistent with nearby observations must be reported to the
user for discussion before it is used as model evidence. The implementer may
then investigate possible causes such as corporate actions, capital reduction,
stock split, reverse split, cash capital reduction, exchange ratio changes,
ex-right/ex-dividend price adjustment gaps, delisting/relisting,
suspension/resumption windows, missing trading-date gaps, source-file defects,
column parsing errors, or unadjusted price jumps, but these are examples and
must not narrow the rule. Until resolved, such rows must be labeled
research-only data-quality exceptions, excluded from promotion evidence or rerun
with an approved adjusted basis, and summarized with both including-exception
and excluding-exception metrics. If the current lane cannot update the needed
rule, validator, or artifact, hand the issue to the project
governance/model_governance owner instead of silently continuing.

Daily model condition development must not default to arbitrary condition
stacking or win-rate-only tuning. Before promoting a new required condition,
add-score item, deduct-score item, or risk tag, first compare the features of
high-return and low-return trades under the same buy point, sell rule, holding
window, and anomaly-exclusion basis. Use that comparison to decide whether a
condition explains better payoff, merely raises win rate without payoff, reduces
tail loss, or only shrinks sample size. Report sample count, win/neutral/failure
rates, average and median realized return, high-return hit rate, loss rate, and
including/excluding-anomaly metrics before treating the condition as model
evidence. This method applies to future models and to any reopened discussion of
previously approved models; when an older model is revisited, explicitly remind
the user to evaluate high-return and low-return feature differences before
changing gates, scoring, ranking, or operation rules.

When a formal model promotion or model change makes an operation-oriented model
eligible for daily PDF or packet presentation, the daily model change must also
define the formal daily operation-row adapter contract. The model lane owns the
operation-row producer or approved equivalent, including artifact name, schema,
lifecycle sections, empty-state behavior, readiness fields, validators, and
PDF-safe consumer fields. Registry approval alone is not enough for PDF
operation presentation. Digest / highlight PDF rendering may consume those rows
only after `model_operation_readiness_latest.csv` reports
`pdf_integration_status=pdf_integrated_daily_adapter`; otherwise keep
`presentation_allowed=False` and do not expose PDF operation rows. The PDF
renderer must not convert candidate signal rows, research/backtest variants, or
advisory recommendations into buyable, active, pending, exit, or stop-loss
lifecycle rows.
PDF renderer must not convert candidate signal rows, research/backtest
variants, or advisory recommendations into lifecycle rows.

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

Operation-oriented stock model blocks in digest / highlight PDFs must use two
main tables only: `本日可買 / 已確認買入候選` first, then `操作中`. The first table
uses `本日無股票推薦` as its empty-state row when there are no buyable confirmed
candidates. The second table uses `目前無操作中追蹤列` as its empty-state row
when there are no active operation rows. Digest / highlight blocks must not
promote `待確認`, `已失效`, or `已出場` into main tables; `待確認` is full-list only
when the model's formal adapter provides it, and `已失效` / `已出場` remain
audit/lifecycle artifacts. `w_bottom_right_side` and
`neckline_volume_breakout_confirmation` have formal model-owned PDF operation
section adapters and must be rendered from their dedicated artifacts:
`output/latest/daily_w_bottom_right_side_operation_section_latest.csv` and
`output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv`.
The renderer may consume those rows only when
`model_operation_readiness_latest.csv` reports
`pdf_integration_status=pdf_integrated_daily_adapter` and the adapter provides
both `confirmed_operation` and `active_operation` sections. Missing artifacts or
missing required columns must fail closed; the PDF layer must not fall back to
candidate signal rows to infer W-bottom lifecycle. Future operation-oriented
models must follow this contract when their formal PDF operation adapters are
wired.

Daily stock operation-model highlight display limits are also contractual:
`confirmed_operation` / `本日可買 / 已確認買入候選` rows must be rendered in full
for the applicable report line, without a fixed 10-row cap.
`active_operation` / `操作中` rows must render at most the first 10 rows when
more than 10 rows exist, and all rows when 10 or fewer rows exist; a missing or
unlimited highlight active cap is forbidden. Full-list PDFs must not inherit
highlight caps. Every formal stock operation-model header summary must include
this standalone sentence:
`取樣：已確認欄位股票精華版全部列出，操作中欄位股票精華版最多列出十檔股票。`

Formal operation adapters must enforce lifecycle monotonicity. Within the same
model, report line, and PDF view, the same stock must not appear in both
`confirmed_operation` and `active_operation` on the same operation date. An
existing active position suppresses a new same-stock confirmed row until that
position exits. `active_operation` rows must be backed by a prior formal
buy-ranked confirmed operation row, not by re-evaluating old signals with newer
context. Rows that were `confirmed_unranked_operation` on their confirmation
date must not later be promoted into active tracking.

Official daily PDF generation must emit
`chatgpt_daily_pdf_semantic_manifest.csv` next to the six PDFs and
`chatgpt_daily_report_runtime_manifest.json`. The runtime manifest must record
`semantic_manifest_path`. The semantic manifest is the row-level source of truth
for formal operation-model PDF rendering and must include at least `pdf_role`,
`pdf_view`, `report_line`, `model_id`, `pdf_section`, `rendered_row_type`,
`stock_id`, `source_artifact`, and `source_sha256`. PR and main validators must
fail closed when the semantic manifest is missing, malformed, sourced from a
legacy/preview artifact, or inconsistent with configured golden semantic cases.

Legacy preview code or artifacts that can be confused with production operation
rows must be removed only after an owner/dependency audit proves no active
workflow, validator, inventory, spec, replay, or research lane still depends on
them. If a legacy artifact is still owned by another lane, the daily PDF layer
must instead forbid consuming it as a formal operation-row source and hand off a
separate cleanup/sync PR to that owner lane.

Full-list PDFs can be large. Page-count validation must define an explicit
reasonable range instead of treating the current high page count as an implicit
failure.

## PDF Delivery Link Reporting Rule

When a task produces or prepares PDF deliverables for the user, the final reply
must include directly clickable links to the generated PDF files whenever
possible. At minimum, include a clickable link to the folder that contains the
PDF deliverables. Local links must use absolute workspace paths so the user can
open the folder or files with one click.

