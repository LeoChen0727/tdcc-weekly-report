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
| `tdcc_weekly` | Weekly large-holder chip flow, TDCC weekly reports, TDCC PDF artifacts | `tdcc_weekly.yml`, TDCC scripts, TDCC rules, weekly outputs |
| `ci_release` | Branch health, PRs, GitHub Actions, Pages/raw alignment, automation pointers, docs handoff | `.github/workflows/`, `docs/`, validation scripts, Apps Script trigger docs |

## Hard Boundaries

- Daily production must not require long research jobs, parameter grids, broad
  raw health sweeps, TDCC historical backfills, or nonessential backtest work.
- Research/backtest work must not silently change daily production weights,
  ranking, PDF logic, or model behavior.
- Stock screening models must remain independent at the code and parameter
  level. Shared helpers are allowed only when they do not hide shared model
  parameters, thresholds, weights, ranking settings, or decision logic.
- A stock may appear in multiple models. Do not collapse model hits into one
  global ranking unless a program-side contract explicitly does that.
- Do not invent buy/sell decisions, mainstream/non-mainstream labels, ranking,
  risk vetoes, or model judgments in the PDF layer.
- Do not modify `generate_repo_chatgpt_side_reports.py` unless the user
  explicitly asks for that file.
- `report_ready=True` means repo artifacts are available. It does not mean a
  ChatGPT-side PDF task has already been completed.
- Prefer raw GitHub or GitHub API data over Pages for daily freshness. Pages is
  a share view and can lag behind `main`.

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

For documentation-only changes, use the smallest relevant validation set and
still publish through branch plus PR.

## Exit Summary

Every thread that changes the repo should end with a short handoff summary:

- Thread type
- Branch
- Commit
- Pull request
- Files changed
- Local validation
- GitHub Actions result or pending run URL
- Residual risks or follow-up items

Do not use an old conversation as the source of truth. If a future thread needs
context, point it to the PR, this document, and the latest repo artifacts.

## Templates

Copy the matching template into a new Codex thread:

- `docs/thread_templates/daily_production.md`
- `docs/thread_templates/research_backtest.md`
- `docs/thread_templates/tdcc_weekly.md`
- `docs/thread_templates/ci_release.md`
