# TDCC Weekly Report Master Priority Rules

Last updated: 2026-05-27

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

## Calendar-Date Tasks Versus Trading-Date Data

Some tasks are calendar-date tasks, not trading-date tasks. Astrology / Zi Wei / Ba Zi reports must use the user's requested calendar date as the report date and chart calculation date.

For astrology tasks:

- `main_price_date` and `report_ready` are only stock-market data status fields.
- A stale or previous-trading-day `main_price_date` must not block the astrology report.
- Repo market data may be used only as an auxiliary reality check for the wealth / stock behavior-risk paragraph.
- If repo market data is stale or unreadable, write the available market-data date and continue the astrology report from the calendar date.
- Do not say the astrology report cannot be produced just because the stock repo date differs from the calendar date.

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

## Data Sufficiency

If required data is missing or immature, write:

`資料不足 / 僅能觀察`

Do not force conclusions from insufficient data. `pending` is not success or failure. `sample_status=insufficient_sample` or `pending_only` cannot be treated as verified effectiveness.

## Deliverables

Repo pipeline artifacts are source artifacts. A repo artifact being present does not mean ChatGPT has completed a requested final report.

If the user asks to perform a task or produce a report, ChatGPT must produce the requested deliverable after reading repo structured data. Do not stop at repo PDF links unless the user asked only for repo artifact status or links.
