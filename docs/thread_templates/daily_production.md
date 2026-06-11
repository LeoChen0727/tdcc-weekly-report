# Daily Production Thread Template

Copy this into a new Codex thread for daily Taiwan stock recommendation,
daily-market packet, or daily PDF-source work.

```text
Use active engineer mode for the tdcc-weekly-report repo.

Thread type: daily_production

Repo:
https://github.com/LeoChen0727/tdcc-weekly-report

Local checkout:
<paste current local checkout path>

Do not open or ask me to open the old crashed Codex conversation.

First read, in order:
1. output/latest/READ_ME_FIRST_DAILY_REPORT.txt
2. rules/master_priority_rules.md
3. rules/daily_stock_candidate_rules.md
4. output/latest/data_freshness_latest.csv

Freshness gate:
- Report main_price_date.
- Report report_ready.
- Check actual_stock_price_history_date, stock_monitor_price_date,
  all_candidates_date, official_price_fetch_date, warrant_flow_date, and notes.
- Do not use stale output/latest as current data.
- Before generating ChatGPT-side daily PDFs from a local checkout, run
  scripts/validate_daily_report_source_preflight.py or perform the equivalent
  check. Dirty/stale local checkouts are not official PDF sources; use a clean
  clone/worktree/archive instead. README commit_sha is an artifact source hint
  and does not need to equal checkout HEAD.

Hard boundaries:
- daily_full_pipeline must not run nonessential research/backtest work.
- Stock screening models must keep independent parameters, thresholds, weights,
  ranking settings, and decision logic.
- A stock may appear in multiple models; do not collapse independent model hits
  into one ranking unless the program-side contract says so.
- Do not invent PDF-layer buy/sell, mainstream/non-mainstream, risk veto,
  ranking, or model judgment.
- Do not modify generate_repo_chatgpt_side_reports.py unless I explicitly ask.

Task:
<describe the daily production issue or deliverable>

Completion condition:
- Explain current freshness state.
- Make scoped code/docs changes only if needed.
- Commit and push any file changes.
- Run the relevant local validation and GitHub Actions.
- Debug Actions until the relevant workflow executes successfully.
- End with branch, commit, PR, Actions result, and residual risks.
```
