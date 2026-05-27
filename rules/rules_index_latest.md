# TDCC Weekly Report Rules Index

Last updated: 2026-05-27

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

## Conflict Handling

If rules conflict:

1. User's latest explicit instruction wins.
2. Program-side fields win over PDF prose and memory.
3. `rules/master_priority_rules.md` wins over generated summaries.
4. Task-specific rule files win over generic generated task text.

If a required rule file is missing, state `rules_missing` and continue with `output/latest/CHATGPT_DAILY_REPORT_RULES.txt`, but do not pretend the master rule file was read.

