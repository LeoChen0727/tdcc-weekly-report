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
- For ChatGPT-side daily PDF generation, do not manually read OneDrive,
  Pages, raw README, or local output/latest to decide the date. Run the only
  official entrypoint:
  python scripts/run_chatgpt_daily_report_entrypoint.py
- To check readiness without rendering, run:
  python scripts/run_chatgpt_daily_report_entrypoint.py --source-gate-only
- Directly running scripts/generate_chatgpt_side_daily_reports.py is blocked;
  it is the renderer, not the official entrypoint. README commit_sha is an
  artifact source hint and does not need to equal checkout HEAD.

Hard boundaries:
- daily_full_pipeline must not run nonessential research/backtest work.
- Stock screening models must keep independent parameters, thresholds, weights,
  ranking settings, and decision logic.
- A stock may appear in multiple models; do not collapse independent model hits
  into one ranking unless the program-side contract says so.
- Do not invent PDF-layer buy/sell, mainstream/non-mainstream, risk veto,
  ranking, or model judgment.
- ChatGPT-side PDF source-state handling belongs in
  scripts/run_chatgpt_daily_report_entrypoint.py. Rendering changes belong in
  scripts/generate_chatgpt_side_daily_reports.py. Do not leave durable fixes
  only in a OneDrive/local helper copy.

Task:
<describe the daily production issue or deliverable>

Completion condition:
- Explain current freshness state.
- Make scoped code/docs changes only if needed.
- Commit and push any file changes.
- Open or update the PR and verify PR checks pass.
- Do not stop at branch PR checks. Merge the PR into `main`.
- Wait for the follow-up `main` GitHub Actions run triggered by the merge.
- Debug Actions until the relevant `main` workflow executes successfully.
- End with branch, commit, PR, merge commit, main Actions result, and residual risks.
```
