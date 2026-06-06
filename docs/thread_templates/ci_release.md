# CI Release Thread Template

Copy this into a new Codex thread for branch health, pull requests, GitHub
Actions, Pages/raw alignment, automation pointers, or docs handoff work.

```text
Use active engineer mode for the tdcc-weekly-report repo.

Thread type: ci_release

Repo:
https://github.com/LeoChen0727/tdcc-weekly-report

Local checkout:
<paste current local checkout path>

Do not open or ask me to open the old crashed Codex conversation.

First read, in order:
1. output/latest/READ_ME_FIRST_DAILY_REPORT.txt
2. rules/master_priority_rules.md

Initial health check:
- git status
- branch and remote state
- recent GitHub Actions status
- output/latest/data_freshness_latest.csv
- whether automations or Apps Script dispatches point to the correct workflows

Scope:
- Branch and PR workflow.
- GitHub Actions health.
- Pages versus raw/main consistency.
- Automation and Apps Script workflow dispatch validation.
- Repo handoff docs and thread templates.

Hard boundaries:
- Do not change daily production logic, research logic, or TDCC model logic
  unless the task explicitly expands to that scope.
- If the checkout has unrelated dirty files, create a clean worktree from
  origin/main before editing.
- Stage only files that belong to the task.

Task:
<describe the CI/release/docs issue>

Completion condition:
- Explain current repo health state.
- Make scoped docs/CI/release changes only.
- Commit and push any file changes.
- Run local validation and the relevant GitHub Actions or PR checks.
- Debug Actions until the relevant workflow executes successfully.
- End with branch, commit, PR, Actions result, and residual risks.
```
