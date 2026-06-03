# TDCC Weekly Report Rules Index

Last updated: 2026-06-01

## Priority

1. Read `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`.
2. Read `rules/master_priority_rules.md`.
3. Read the task-specific rule file.
4. Read generated task rules and indicator guide.
5. Read task data.

## Rule Files

| file | task | priority |
|---|---|---:|
| `rules/master_priority_rules.md` | all tdcc-weekly-report tasks | 1 |
| `rules/daily_stock_candidate_rules.md` | daily full-market candidate report | 2 |
| `rules/single_stock_report_rules.md` | single-stock report and individual packet interpretation | 2 |
| `rules/tdcc_weekly_rules.md` | TDCC weekly large-holder flow report | 2 |
| `rules/market_opening_prep_rules.md` | market opening prep and market-risk analysis | 2 |
| `rules/futures_options_vix_rules.md` | futures/options, VIX, Put/Call, retail MTX interpretation | 2 |
| `rules/astrology_rules.md` | Zi Wei / Ba Zi calendar-date strategy report | 2 |

## Workflow Split

| workflow | purpose | normal trigger |
|---|---|---|
| `.github/workflows/daily_full_pipeline.yml` | daily report-critical artifacts, packets, rules, and PDFs | manual daily run; heavy options default off |
| `.github/workflows/research_backtest_pipeline.yml` | long backtests, weekly surge parameter research, surge model, signal performance reports | manual dispatch or external biweekly Apps Script trigger |
| `.github/workflows/tdcc_history_backfill.yml` | TDCC historical data backfill and bounded derived-output rebuild | manual backfill |

Research/backtest workflows must not contain hidden internal date gates. If a workflow run is created, it should run the selected research steps. Biweekly cadence belongs to the external scheduler, not to an in-workflow skip step.

## Conflict Handling

If rules conflict:

1. User's latest explicit instruction wins.
2. Program-side fields win over PDF prose and memory.
3. `rules/master_priority_rules.md` wins over generated summaries.
4. Task-specific rule files win over generic generated task text.

If a required rule file is missing, state `rules_missing` and continue with `output/latest/CHATGPT_DAILY_REPORT_RULES.txt`, but do not pretend the master rule file was read.
