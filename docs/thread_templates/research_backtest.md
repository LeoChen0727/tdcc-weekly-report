# Research Backtest Thread Template

Copy this into a new Codex thread for backtests, model parameter research,
historical performance, or research-output maintenance.

```text
Use active engineer mode for the tdcc-weekly-report repo.

Thread type: research_backtest

Repo:
https://github.com/LeoChen0727/tdcc-weekly-report

Local checkout:
<paste current local checkout path>

Do not open or ask me to open the old crashed Codex conversation.

First read, in order:
1. output/latest/READ_ME_FIRST_DAILY_REPORT.txt
2. rules/master_priority_rules.md
3. rules/daily_stock_candidate_rules.md if daily candidate model research is involved
4. .github/workflows/research_backtest_pipeline.yml
5. docs/apps_script_workflow_trigger.gs
6. scripts/validate_apps_script_workflow_triggers.py

Hard boundaries:
- Research/backtest code must be separate from daily production.
- Do not make daily_full_pipeline run long backtests, broad history rebuilds,
  parameter grids, or nonessential research refreshes.
- Research cadence belongs to explicit workflow dispatch or external scheduler,
  not hidden internal date gates.
- Stock screening models must keep independent tunable parameters.
- Backtest evidence may inform future program-side changes, but it must not
  silently change daily PDF-side selection logic.

Task:
<describe the research or backtest issue>

Completion condition:
- Identify the exact research workflow/script boundary.
- Make scoped changes only in the research/backtest layer unless explicitly
  productizing a result into daily production.
- Commit and push any file changes.
- Run relevant local validation and the relevant GitHub Actions.
- Debug Actions until the selected workflow executes successfully.
- End with branch, commit, PR, Actions result, and residual risks.
```
