# TDCC Weekly Thread Template

Copy this into a new Codex thread for weekly TDCC large-holder flow, weekly
candidate reports, or TDCC PDF artifact work.

```text
Use active engineer mode for the tdcc-weekly-report repo.

Thread type: tdcc_weekly

Repo:
https://github.com/LeoChen0727/tdcc-weekly-report

Local checkout:
<paste current local checkout path>

Do not open or ask me to open the old crashed Codex conversation.

First read, in order:
1. output/latest/READ_ME_FIRST_DAILY_REPORT.txt
2. rules/master_priority_rules.md
3. rules/tdcc_weekly_rules.md

Scope:
- TDCC weekly large-holder flow.
- Weekly TDCC candidate CSV/MD/PDF artifacts.
- TDCC tracking and validation scripts.

Hard boundaries:
- This is not the daily full-market recommendation workflow.
- This is not daily candidate model parameter research unless explicitly stated.
- Do not let weekly TDCC output changes pollute daily freshness or daily PDF
  source contracts.
- For public PDFs, do not expose raw internal slugs when display text is
  expected.

Task:
<describe the TDCC weekly issue or deliverable>

Completion condition:
- Make scoped TDCC weekly changes only.
- Run relevant TDCC validators, including PDF-facing validation when PDFs are touched.
- Commit and push any file changes.
- Open a PR and use `TDCC Weekly PR Validation` (`.github/workflows/tdcc_weekly_pr_validation.yml`) as PR-safe branch evidence.
- Do not treat a draft PR, branch check, or branch `workflow_dispatch` run as complete.
- If publishing or production workflow behavior is affected, complete requires merge to `main`, the post-merge `TDCC Weekly Report` (`.github/workflows/tdcc_weekly.yml`) production run, Pages deploy when artifacts are published, and raw-vs-Pages parity when published artifacts are affected.
- End with branch, commit, PR, validators, Actions result, `completion_state`, and residual risks.
```
