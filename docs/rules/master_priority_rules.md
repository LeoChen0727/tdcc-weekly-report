# TDCC Weekly Report Master Priority Rules

Last updated: 2026-05-28

This file is the highest-priority rule header for all ChatGPT tasks that use the `tdcc-weekly-report` repo.

## Priority Order

1. User's latest explicit instruction in the current conversation.
2. Program-side structured fields from this repo.
3. This master rule file.
4. Task-specific rule files under `rules/`.
5. `output/latest/CHATGPT_DAILY_REPORT_RULES.txt` or other generated task rules.
6. ChatGPT memory, old PDFs, old Markdown summaries, or ad-hoc interpretation.

If memory, old summaries, or PDFs conflict with program-side fields or repo rules, use the program-side fields and latest repo rules.

## Required Read Flow

For every repo-related task:

1. Read `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`.
2. Read this file: `rules/master_priority_rules.md`.
3. Read the task-specific rule file.
4. Read task packet / CSV / feature panel / event log / top list.
5. Use PDFs only as auxiliary shareable artifacts or cross-checks.

Do not use old-date data as a new-date report. If `main_price_date` differs from the requested date, state the available repo date clearly.

## Repo Change Completion Gate

For daily production scope code, rule, workflow, Apps Script trigger, or generated contract changes, a pull-request branch with passing PR checks is not a completion point.

The task may be reported complete only after all of these are true:

1. The intended files are committed.
2. The branch is pushed.
3. A pull request is opened or updated.
4. The PR checks pass, or any failures are debugged and fixed.
5. The PR is merged to `main`.
6. The follow-up `main` branch GitHub Actions triggered by the merge complete successfully.
7. The final response reports the branch, commit, PR, merge commit, main Action run, and any residual risk.

If any item is still pending, say it is pending and keep working unless the user explicitly asks to stop.

## Daily Data Read Contract

For daily stock recommendation tasks, daily PDF tasks, and any task that requires the latest `main_price_date`, raw GitHub URLs and GitHub API contents are the authoritative read path.

- Prefer raw / GitHub API entries before GitHub Pages entries.
- Treat GitHub Pages as an auxiliary share view only. Pages may lag behind `main` after a successful workflow or during a Pages deployment queue.
- If Pages and raw/API disagree on `main_price_date`, `commit_sha`, or `report_ready`, ignore the stale Pages value and use raw/API.
- If raw/API is unreadable but Pages is readable, use Pages only after explicitly checking that its date and commit match another current source. Otherwise stop and report the stale/unreadable state.
- Generated README and rule files must not instruct daily-report conversations to read Pages before raw/API.

## Calendar-Date Tasks Versus Trading-Date Data

Some tasks are calendar-date tasks, not trading-date tasks. Astrology / Zi Wei / Ba Zi reports must use the user's requested calendar date as the report date and chart calculation date.

For astrology tasks:

- `main_price_date` and `report_ready` are only stock-market data status fields.
- A stale or previous-trading-day `main_price_date` must not block the astrology report.
- Repo market data may be used only as an auxiliary reality check for the wealth / stock behavior-risk paragraph.
- If repo market data is stale or unreadable, mention it only briefly in the wealth / stock paragraph or a final data note, then continue the astrology report from the calendar date.
- Do not put raw fetch status, Pages status, GitHub API status, `cache_miss`, `internal_fetch_error`, or similar debug labels in the visible opening of an astrology report unless the user explicitly asks for data-reading diagnostics.
- Do not say the astrology report cannot be produced just because the stock repo date differs from the calendar date.
- The visible astrology report must not start with headings such as `資料狀態`, `資料日期與流程狀態`, `repo 入口讀取狀態`, or `READ_ME_FIRST 讀取狀態`.
- Before finalizing an astrology report, inspect the first 300 visible characters. If they contain `repo`, `READ_ME_FIRST`, `main_price_date`, `report_ready`, `raw_fetch`, `pages`, `cache`, or `GitHub API` before astrology content, rewrite the opening.

## Raw Data And Fetch Failures

Structured repo data wins over PDF prose:

- packet
- source CSV
- signal log
- feature panel
- event log
- index
- validation file
- Markdown summary

Do not treat `Cache miss`, `Internal Error`, `Total lines: 1`, or `content_not_expanded` as proof that the repo has no data.

Use these statuses instead:

- `missing_file`: real 404.
- `raw_fetch_failed`: raw endpoint failed.
- `cache_miss`: reader cache failure.
- `internal_fetch_error`: reader internal failure.
- `content_not_expanded`: opened but content did not expand.
- `suspicious_single_line`: expected multiline content but only one line displayed.
- `file_exists_but_content_unreadable`: blob/index proves file exists but content cannot be read.

When CSV/raw does not expand, use packet, HTML/TXT window, index, or GitHub API contents endpoint before downgrading the analysis. Do not replace repo price / TDCC / market raw data with external websites.

## Task Separation

Do not mix task types:

- daily full-market candidate report
- current holdings report
- single-stock report
- TDCC weekly flow report
- market opening prep
- warrant auxiliary report
- backtest/model tracking
- overseas peer mapping
- astrology

Daily candidate reports are not holdings management. Holdings reports are not full-market ranking reports. Market reports are not stock recommendation lists.

## Default Code Isolation

Program code must default to independent business surfaces. Report builders, model parameters, scoring logic, filters, ranking, field transforms, validation contracts, output writers, and workflow steps must not share business-semantic code across unrelated outputs unless the relationship is explicit in repo rules or the user has approved the coupling.

Shared code is allowed only for low-level technical utilities that do not decide business content, such as file reads, type conversion, date formatting, font registration, basic table drawing, PDF file writing, and validation plumbing.

Before changing any shared function that can affect multiple reports, models, parameters, or workflows, state the affected outputs and either split the code path first or make the coupling explicit in the change. A request to adjust one report, model, parameter, or field must not silently change another surface.

## Daily Model / Presentation Display Fields

Daily PDF and daily packet text must be sourced from the model layer and presentation-routing layer. They must not create a separate operation or trade-decision layer.

For daily reports:

- The canonical daily model source is `daily_candidate_model_signals_for_report_latest.csv`.
- Use model-layer fields such as `model_id`, `model_name_zh`, `model_score`, `model_rank`, `score_components`, `risk_penalty_tags`, `risk_tags`, `tdcc_status`, `warrant_flow_signal`, `next_confirmation`, and report-line / presentation fields such as `report_bucket`, `candidate_line_group`, `presentation_priority`, and `theme_final_status`.
- Formal daily PDF / Markdown prose must not print raw enum values or internal field names such as `action_rating`, `starter_position`, `decision_score`, `decision_priority`, `trade_decision`, `entry_style`, `position_sizing`, `model_slug`, `packet`, `raw field name`, or `程式端欄位`.
- Do not output daily buy/sell/position-sizing conclusions such as buy now, wait, no-buy, starter position, or normal position unless a future historical operation module supplies evidence-backed operation fields.
- If display text is missing, write `資料不足 / 暫用現有資料`; do not expose raw internal values.
- Single-stock reports may still have their own `ACTION_DISPLAY` contract, but that contract must not be used as a fallback for daily PDF or daily packet conclusions.

## Pipeline Runtime Separation

Daily report generation and research/backfill jobs must remain separated.

- `daily_full_pipeline.yml` is for daily report-critical data, packets, rule files, and PDF artifacts.
- Heavy research, long backtests, parameter grids, raw URL health sweeps, and TDCC historical backfill must not be required for a normal daily run.
- Research/backtest refreshes belong in `research_backtest_pipeline.yml` or a dedicated manual workflow.
- Model-parameter evidence tables such as `daily_model_parameter_research_latest.csv/md` and `daily_model_parameter_research_horizon_detail_latest.csv/md` belong to the research/backtest layer. They should use signal-date next trading day open as entry and keep D+1..D+10 close-return and high-return statistics separate.
- `daily_model_parameter_recommendations_latest.csv/md` is the program-side translation from backtest evidence into reporting usage. It can mark parameters as core, secondary, score-only, intraday-target watch, or research-only, but it still must not silently change core model weights.
- Research/backtest cadence must not be hidden behind an internal date gate inside the workflow. If the workflow appears to run, it must actually run the requested research steps. Biweekly cadence should be controlled by an external scheduler such as Apps Script, or by an explicit manual dispatch.
- TDCC history backfill belongs in `tdcc_history_backfill.yml` and must use bounded request and rebuild windows unless explicitly running a full research rebuild.
- Daily reports may consume the latest available research outputs as specialty sections, but stale or missing research outputs must not block daily report generation.
- If a daily report uses a research output, it must preserve `sample_status`, `tuning_status`, and `reporting_priority_only` limits.
- Daily production commit steps must reject staged TDCC weekly, research/backtest, and long-history output paths. If such paths are staged during `daily_full_pipeline.yml`, treat it as a boundary failure and fix the owner workflow instead of publishing them through daily production.

## Data Sufficiency

If required data is missing or immature, write:

`資料不足 / 僅能觀察`

Do not force conclusions from insufficient data. `pending` is not success or failure. `sample_status=insufficient_sample` or `pending_only` cannot be treated as verified effectiveness.

## Deliverables

Repo pipeline artifacts are source artifacts. A repo artifact being present does not mean ChatGPT has completed a requested final report.

If the user asks to perform a task or produce a report, ChatGPT must produce the requested deliverable after reading repo structured data. Do not stop at repo PDF links unless the user asked only for repo artifact status or links.
