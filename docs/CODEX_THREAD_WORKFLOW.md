# Codex Thread Workflow

This document defines how to split Codex work for this repository so long
conversations do not become the project state. Each thread should have one
clear workflow, one branch or pull request when files change, and one exit
summary.

Do not ask the user to open or read the old crashed Codex conversation. Treat
the repository, rules, current artifacts, current GitHub Actions, and this
document as the handoff surface.

## First Read Gate

For every repo-related thread, start by reading these files in order:

1. `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
2. `rules/master_priority_rules.md`
3. The task-specific rule file for the selected workflow

Task-specific rule files:

- Daily production: `rules/daily_stock_candidate_rules.md`
- TDCC weekly large-holder flow: `rules/tdcc_weekly_rules.md`
- Single-stock reports: `rules/single_stock_report_rules.md`
- Market opening preparation: `rules/market_opening_prep_rules.md`

For daily stock, single-stock, and PDF tasks, also check
`output/latest/data_freshness_latest.csv` before using latest artifacts. Report
`main_price_date`, `report_ready`, and any stale auxiliary dates plainly.

## Thread Types

Use one of these thread types. If work crosses boundaries, split it into
separate pull requests unless a single integration fix is clearly safer.

| Thread type | Main scope | Typical files |
| --- | --- | --- |
| `daily_production` | Daily Taiwan stock recommendation list, daily packets, daily PDFs, daily data freshness | `daily_full_pipeline.yml`, daily candidate scripts, daily rules, daily latest artifacts |
| `research_backtest` | Long research, parameter studies, model evidence tables, historical performance, backtests | `research_backtest_pipeline.yml`, research scripts, research outputs |
| `tdcc_weekly` | Weekly large-holder chip flow, TDCC weekly reports, TDCC PDF artifacts | `tdcc_weekly.yml`, `tdcc_weekly_pr_validation.yml`, TDCC scripts, TDCC rules, weekly outputs |
| `ci_release` | Branch health, PRs, GitHub Actions, Pages/raw alignment, automation pointers, docs handoff | `.github/workflows/`, `docs/`, validation scripts, Apps Script trigger docs |

## Hard Boundaries

- Daily production must not require long research jobs, parameter grids, broad
  raw health sweeps, TDCC historical backfills, or nonessential backtest work.
- Research/backtest work must not silently change daily production weights,
  ranking, PDF logic, or model behavior.
- Business-facing code defaults to independent ownership. Do not share
  report builders, model parameters, scoring logic, filters, ranking, field
  transforms, validation contracts, output writers, PDF layouts, or workflow
  behavior across unrelated surfaces unless the coupling is explicit in repo
  rules and approved by the user.
- Before editing any shared helper or parameter source, identify which reports,
  models, outputs, and validations depend on it. If the requested change is for
  one surface, split the shared path before changing behavior.
- Stock screening models must remain independent at the code and parameter
  level. Shared helpers are allowed only when they do not hide shared model
  parameters, thresholds, weights, ranking settings, or decision logic.
- Repository-level code-isolation policy is enforced by `scripts/validate_repo_code_isolation_policy.py`,
  pytest, and the Daily Full Pipeline.
- A stock may appear in multiple models. Do not collapse model hits into one
  global ranking unless a program-side contract explicitly does that.
- Do not invent buy/sell decisions, mainstream/non-mainstream labels, ranking,
  risk vetoes, or model judgments in the PDF layer.
- Official ChatGPT-side daily PDF generation must start from
  `scripts/run_chatgpt_daily_report_entrypoint.py`. That entrypoint gates on
  `origin/main` and creates a temporary clean source worktree before rendering.
- `scripts/generate_chatgpt_side_daily_reports.py` is the renderer, not the official entrypoint.
  Do not call it directly for official output, and do not
  leave durable fixes only in a OneDrive/local helper copy.
- `report_ready=True` means repo artifacts are available. It does not mean a
  ChatGPT-side PDF task has already been completed.
- Prefer raw GitHub or GitHub API data over Pages for daily freshness. Pages is
  a share view and can lag behind `main`.
- `.github/workflows/tdcc_weekly.yml` is the formal TDCC weekly production
  workflow. It may commit generated artifacts and push them for Pages. It is
  not a normal PR validation workflow.
- `.github/workflows/tdcc_weekly_pr_validation.yml` is the PR-safe TDCC weekly
  validation workflow. It runs on `pull_request`, builds and validates TDCC
  weekly outputs in the runner workspace, and must not commit, push, sync Pages,
  deploy Pages, or replace the formal production workflow.

## Branch And PR Discipline

For repo maintenance and code changes:

1. Do not work directly on a dirty `main` checkout.
2. Create a branch with the `codex/` prefix.
3. If the existing checkout has unrelated dirty files, create a separate
   worktree from `origin/main`.
4. Stage only files that belong to the task.
5. Commit the completed change.
6. Push the branch.
7. Open a pull request.
8. Run the relevant local validations and GitHub Actions. Debug failed Actions
   until the requested workflow can execute successfully.
9. For TDCC weekly PRs, use `TDCC Weekly PR Validation` as branch PR evidence.
   A draft PR, branch check, or temporary branch `workflow_dispatch` run is not
   completion evidence.
10. For `daily_production` code, TDCC weekly production workflow changes, rule,
   workflow, Apps Script trigger, or generated contract changes, do not stop at a
   branch PR with passing checks. Merge the PR to `main`, wait for the follow-up
   `main` production workflow run, and verify it succeeds before reporting the
   task complete.

For documentation-only changes, use the smallest relevant validation set and
still publish through branch plus PR.

## Completion Evidence

Use an explicit `completion_state` for production-affecting workflow, Pages,
report-artifact, model-contract, or `main` PR work:

```text
local_validated
pr_open
branch_action_passed
merged_pending_main_validation
complete
blocked
```

`local_validated`, `pr_open`, and `branch_action_passed` are not `complete`.
Temporary branch runs and branch `workflow_dispatch` evidence are validation
only. `complete` requires merge to `main` plus the applicable post-merge main
production workflow, Pages deploy, and raw-vs-Pages parity evidence when
publishing is affected.

## Exit Summary

Every thread that changes the repo should end with a short handoff summary:

- Thread type
- Branch
- Commit
- Pull request
- Files changed
- Local validation
- GitHub Actions result or pending run URL
- `completion_state`
- For production-affecting changes: merge commit and successful post-merge `main` Action run
- Residual risks or follow-up items

Do not use an old conversation as the source of truth. If a future thread needs
context, point it to the PR, this document, and the latest repo artifacts.

## Templates

Copy the matching template into a new Codex thread:

- `docs/thread_templates/daily_production.md`
- `docs/thread_templates/research_backtest.md`
- `docs/thread_templates/tdcc_weekly.md`
- `docs/thread_templates/ci_release.md`
