# TDCC Weekly Report Rules

This task is the TDCC weekly large-holder flow report. It is not the daily full-market stock recommendation report, holdings management, a single-stock report, market-opening analysis, or backtest tuning report.

## Required Outputs

Every TDCC weekly report task must produce exactly two user-facing report deliverables:

1. TDCC weekly highlight report
2. TDCC weekly full report

Both user-facing deliverables must be PDF files:

- `output/latest/tdcc_weekly_candidate_highlight_latest.pdf`
- `output/latest/tdcc_weekly_candidate_full_latest.pdf`

PDF text and table content must use 標楷體 / DFKai-SB at 14 pt. Page count is not fixed; do not treat five pages as a rule.

TDCC ranking sections and daily-model cross sections must use different PDF table contracts:

- TDCC ranking sections use: section rank, stock id, stock name, TDCC phase, risk bucket, TDCC score, selected reason, next confirmation, operation note.
- Daily-model cross sections use the ranking columns plus daily model, model rank within TDCC list, and model score.

Ranking fields must render as integers when they are whole numbers. Do not display ranks as `1.00`, `2.00`, or similar decimal strings.

Score fields may use at most two decimals and must strip redundant trailing zeroes, for example `81.30` -> `81.3` and `74.00` -> `74`.

PDF text must not print raw slug or snake_case fields. If a display value has no approved Chinese label, render `資料不足 / 暫用現有資料` instead of the raw token.

The report-producing conversation or PDF generator must read these program-side report-ready sources first:

- `tdcc_weekly_candidate_highlight_for_report_latest.csv`
- `tdcc_weekly_candidate_highlight_for_report_latest.md`
- `tdcc_weekly_candidate_full_for_report_latest.csv`
- `tdcc_weekly_candidate_full_for_report_latest.md`

The older ranking, model-cross, and packet files are supporting data. They are not the primary rendering contract when the report-ready files exist.

## Ranking Lines

The weekly report has two independent TDCC ranking lines:

1. Weekly increase ranking: stocks with large one-week holder-ratio increases. A single week can qualify.
2. Consecutive accumulation ranking: stocks with at least two weeks of continued accumulation.

These two lists must be ranked separately. Do not merge them into one total ranking.

## Highlight Report

The highlight report must include:

- top 5 weekly-increase names
- top 5 consecutive-accumulation names
- weekly-increase names cross-ranked by daily candidate models, top 3 per model
- consecutive-accumulation names cross-ranked by daily candidate models, top 3 per model

The highlight report must make clear whether a row comes from weekly increase, consecutive accumulation, or a daily-model cross section.

## Full Report

The full report must use the same structure as the highlight report, but include all rows from the program-side report-ready table.

## Interpretation Rules

TDCC is a chip-flow background signal, not a standalone buy command.

- `tdcc_weekly_increase_score` ranks one-week large-holder increases.
- `tdcc_consecutive_accumulation_score` ranks continued accumulation.
- `tdcc_phase_group_zh`, `risk_bucket`, `report_usage_zh`, and `operation_note_zh` must be shown or summarized.
- Stocks that are price-leading, overheated, divergent, or data-insufficient must not be described as quiet accumulation.
- Daily model cross rows are used to show where TDCC-selected stocks appear in daily stock-selection models. Do not use them to rewrite TDCC ranking.

## Report Generator Rules

The report generator must render program-side fields. It must not:

- invent a new TDCC ranking
- combine weekly increase and consecutive accumulation into one rank
- drop rows because they are non-mainstream
- turn TDCC risk labels into automatic deletion rules unless the program-side table marks hard exclusion
- use raw PDF artifacts as the primary source when report-ready CSV/MD exists

If any report-ready field is missing, write `欄位尚未完成 / 暫用現有資料` rather than guessing.
