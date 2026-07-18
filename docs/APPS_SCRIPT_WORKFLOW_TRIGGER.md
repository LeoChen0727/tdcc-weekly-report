# Apps Script GitHub Actions Trigger

This document is the standard operating note for the Google Apps Script source
that dispatches GitHub Actions workflows for this repository.

Canonical source file:

```text
docs/apps_script_workflow_trigger.gs
```

Canonical contract validator:

```text
python scripts/validate_apps_script_workflow_triggers.py
```

Target repository:

```text
LeoChen0727/tdcc-weekly-report
```

## Script Properties

Do not hard-code the GitHub token in Apps Script source. Set it in Apps Script
Project Settings as a Script Property:

```text
GITHUB_PAT=<your GitHub token>
```

`GITHUB_TOKEN` is accepted only as a fallback property name for older deployed
scripts. Prefer `GITHUB_PAT`.

Required token access:

- Fine-grained token: select only `LeoChen0727/tdcc-weekly-report`.
- Repository permissions: Actions = read and write; Contents = read.
- Metadata: read.
- Classic token fallback: private repo access requires the `repo` scope.

## Functions To Run Manually

Run these from the Apps Script editor when validating or repairing the trigger:

```text
diagnoseDailyStockMonitorTrigger
diagnoseDailyPriceGapRepairTrigger
diagnoseTdccHistoryGapRepairTrigger
installDailyStockMonitorTrigger
installDailyPriceGapRepairTrigger
installTdccHistoryGapRepairTrigger
triggerDailyStockMonitor
triggerDailyFullPipeline
triggerDailyPriceGapRepair
triggerTdccWeeklyReport
orchestrateTdccIndividualRefresh
diagnoseTdccIndividualRefreshOrchestration
triggerTdccHistoryGapRepair
triggerIndividualStockDataRefresh
triggerEventCatalystUpdate
triggerWeeklyThemeReview
triggerResearchBacktestPipeline
installBiweeklyResearchBacktestTrigger
installTdccIndividualRefreshOrchestratorTrigger
removeTdccIndividualRefreshOrchestratorTrigger
installAllWorkflowTriggers
listAllTriggers
testGithubTokenAndWorkflowAccess
```

`triggerDailyStockMonitor` dispatches `.github/workflows/daily_full_pipeline.yml`
and is the function used by the scheduled daily stock monitor trigger.

`triggerDailyFullPipeline` is the manual full daily pipeline dispatcher.

## 每日市場狀態與完成語意

`daily_full_pipeline.yml` 是 `main` 正式產出 workflow。若用分支執行
`workflow_dispatch`，workflow 必須明確失敗；分支執行結果不得當成正式完成證據。
PR 的 `pull_request` workflow 只代表 `branch_action_passed`，合併後仍須以 `main`
正式 run 與最終產物驗證才能回報 `complete`。

正式 run 先執行 `market-session-preflight`：

- `closed_scheduled` 或 `closed_emergency`：只提交市場狀態與例外休市證據，摘要回報
  `休市，無新報告`；不得抓行情、重產前一交易日 PDF 或 dispatch Pages。
- `unknown`：workflow 必須失敗，不得猜測交易日。
- 預計開盤：將 `expected_main_price_date` 傳給 `fetch_official_daily_price.py`；只有
  TWSE 與 TPEx 目標日行情都確認後才能成為 `open_confirmed` 並繼續六份 PDF。
- `main_price_date`、`market_session_date` 與 `expected_main_price_date` 任一不一致，
  都不得回報正式產出成功。

`triggerDailyPriceGapRepair` dispatches
`.github/workflows/repair_recent_daily_price_gaps.yml` with a 7 calendar-day
lookback and a maximum of 5 automatic repair dates. The workflow excludes the
current Asia/Taipei date and uses the repository non-trading-day calendar before
attempting repairs.

`triggerTdccWeeklyReport` dispatches the TDCC weekly report workflow and records
the pre-dispatch run id, dispatch timestamp, and main SHA in Script Properties.
It does not use a fixed delay as completion evidence. If the tracked run fails
in the allowlisted TDCC period-readiness, current-snapshot, or history-continuity
steps, `orchestrateTdccIndividualRefresh` persists a nonterminal retry state and
redispatches `tdcc_weekly.yml` after 30 minutes. The initial dispatch pins
`target_as_of_date` in Asia/Taipei and every retry reuses it, so a long source
delay cannot silently move the report to a later week. Other failures remain
terminal.

`triggerTdccHistoryGapRepair` dispatches
`.github/workflows/repair_tdcc_monthly_history_gaps.yml`. The workflow checks
official TDCC query-form dates in the current calendar month, excludes the
current Asia/Taipei ISO week, and repairs missing TDCC history rows only for the
bounded TDCC report universe.

`triggerIndividualStockDataRefresh` dispatches
`.github/workflows/individual_stock_data_refresh.yml`.

## TDCC To Individual Refresh Orchestration

`orchestrateTdccIndividualRefresh` is an external, state-aware poller. It has no
permanent trigger. The Saturday 15:30 `triggerTdccWeeklyReport` handler creates
a temporary 5-minute trigger only after it persists a new TDCC chain. When an
allowlisted official-data/readiness step reports that data is not available,
the active poller is replaced by a one-time trigger for 30 minutes later. A
retry dispatch restores the temporary 5-minute poller while workflows are
active. Complete, duplicate, terminal-failure, missing-state, and terminal-state
paths remove both temporary trigger handlers.

The event-scoped chain passes every gate below:

1. Correlate exactly one new `tdcc_weekly.yml` main run by baseline run id and
   bounded dispatch timestamp.
2. Require the tracked run to finish with `conclusion=success`.
3. Read `output/latest/tdcc_weekly_run_status.md` from live `main` and require
   its run id and head SHA to match the tracked run.
4. Read
   `output/latest/tdcc_weekly_candidate_report_validation_latest.json` from
   live `main` and require `status=pass`, an eight-digit `signal_date`, and
   `date_contract.date_source=report_ready_csv_signal_date`.
5. Resolve the TDCC output commit and prove that both the upstream head and the
   output commit are contained in live `main`.
   Matching run/head evidence may wait for GitHub propagation for at most 30
   minutes; after that the chain fails closed instead of remaining active.
6. Reject a duplicate when either the TDCC run id or `signal_date` already
   exists in persistent dispatch history.
7. Dispatch `individual_stock_data_refresh.yml` once, then correlate exactly
   one downstream main run and require its head to contain the TDCC output
   commit.
8. Require the downstream run to succeed. The workflow writes
   `output/latest/individual_stock_reports/individual_stock_refresh_run_status_latest.json`
   after its builder and validator pass, and stages that file in the same commit
   as the refreshed outputs.
9. Require that run-status file on live `main` to match the tracked
   `GITHUB_RUN_ID`, `GITHUB_SHA`, official `signal_date`, and registered date
   source. Its commit must descend from the tracked run head and be contained in
   live `main` before the chain reaches `phase=complete`.

The persisted Script Properties are:

```text
TDCC_INDIVIDUAL_REFRESH_CHAIN_STATE
TDCC_INDIVIDUAL_REFRESH_DISPATCH_HISTORY
```

`TDCC_INDIVIDUAL_REFRESH_CHAIN_STATE` contains the upstream run id, upstream
head SHA, TDCC output commit, signal date, downstream run id, downstream head
SHA, downstream output commit, phase, conclusions, and timestamps. The history
keeps the latest 16 chain attempts. Duplicate suppression uses the exact
`tdcc_run_id + signal_date + tdcc_output_commit_sha` identity only. A repeated
poll of the same chain cannot dispatch twice, while a new TDCC run or corrected
output commit remains recoverable even when its `signal_date` is unchanged.

After a downstream run succeeds, the orchestrator waits up to 30 minutes for
its exact run-status artifact and commit to become visible on live `main`.
Transient Contents API or commit-propagation misses remain
`downstream_main_pending`; only expiry of that bounded window becomes
`downstream_main_gate_failed`.

The existing daily 22:20 `triggerIndividualStockDataRefresh` remains installed
as the normal refresh and fallback. It is independent of the TDCC chain and is
not used as proof that a TDCC-triggered refresh occurred.

To repair the trigger for an already active state, run:

```text
installTdccIndividualRefreshOrchestratorTrigger
diagnoseTdccIndividualRefreshOrchestration
```

The repair function reads persisted state. It installs a 5-minute poller only
for active workflow phases, installs one one-time trigger for
`tdcc_data_retry_wait`, and installs nothing for missing or terminal state. The
diagnostic logs the current state, dispatch history, and recent runs for both
workflows. A complete audit record must show one TDCC `run_id:signal_date`
chain key and exactly one correlated individual refresh run id.

`triggerEventCatalystUpdate` dispatches `.github/workflows/event_catalyst_update.yml`.

`triggerWeeklyThemeReview` dispatches `.github/workflows/weekly_theme_review.yml`.

`triggerResearchBacktestPipeline` dispatches
`.github/workflows/research_backtest_pipeline.yml` with every registered
research input explicitly set to `true`. Workflow inputs default to `false`, so
a manual run executes only the selected research surfaces. The scheduled
biweekly trigger remains an explicit full research/backtest run.

## Recovery Flow

If Apps Script shows `triggerDailyStockMonitor` failed quickly, especially in
about 1-2 seconds, and there is no matching GitHub Actions `workflow_dispatch`
run, treat it as an Apps Script token/configuration failure.

Run this sequence in Apps Script:

```text
diagnoseDailyStockMonitorTrigger
installDailyStockMonitorTrigger
triggerDailyStockMonitor
```

Expected successful diagnostic log:

```text
Status code: 200
GitHub token and workflow access OK.
Daily stock monitor diagnostics OK.
```

After `triggerDailyStockMonitor` succeeds, a GitHub Actions run should appear
under the Daily Full Pipeline workflow.

## HTTP Status Hints

```text
200 / 201 / 202 / 204 = GitHub accepted the request
401 = token is missing, invalid, expired, or not visible to Apps Script
403 = token lacks Actions read/write or Contents read permission
404 = token cannot see the repo or the workflow file name is wrong
422 = ref or dispatch payload is invalid
```

The Apps Script source intentionally throws on non-success HTTP responses. This
prevents silent failures where Apps Script appears successful but GitHub Actions
was never triggered.

## Scheduled Triggers

To recreate the scheduled daily trigger, run:

```text
installDailyStockMonitorTrigger
```

This removes existing `triggerDailyStockMonitor` triggers and installs a fresh
time-driven trigger for the evening run.

To recreate all scheduled workflow triggers, run:

```text
installAllWorkflowTriggers
```

The canonical Apps Script source currently installs the recurring schedule
below. Temporary TDCC reconciliation triggers are created only by an active
Saturday chain:

| handler | cadence | workflow |
|---|---|---|
| `triggerDailyPriceGapRepair` | daily 10:30 Asia/Taipei, skips Saturday/Sunday in handler | `repair_recent_daily_price_gaps.yml` |
| `triggerDailyStockMonitor` | daily 19:30 Asia/Taipei, skips Saturday/Sunday in handler | `daily_full_pipeline.yml` |
| `triggerIndividualStockDataRefresh` | daily 22:20 Asia/Taipei | `individual_stock_data_refresh.yml` |
| `triggerEventCatalystUpdate` | daily 08:10 and 18:10 Asia/Taipei | `event_catalyst_update.yml` |
| `triggerTdccHistoryGapRepair` | Tuesday 09:30 Asia/Taipei | `repair_tdcc_monthly_history_gaps.yml` |
| `triggerTdccWeeklyReport` | Saturday 15:30 Asia/Taipei | `tdcc_weekly.yml` |
| `orchestrateTdccIndividualRefresh` | temporary every 5 minutes only while the TDCC/individual chain is active | conditional `individual_stock_data_refresh.yml` after run/main gates pass |
| `resumeTdccIndividualRefreshRetry` | one-time, 30 minutes after an allowlisted official-data/readiness failure | conditional `tdcc_weekly.yml` retry for the pinned target week |
| `triggerWeeklyThemeReview` | Sunday 19:30 Asia/Taipei | `weekly_theme_review.yml` |
| `triggerResearchBacktestPipeline` | every 2 weeks, Sunday 21:10 Asia/Taipei | `research_backtest_pipeline.yml` |

The trigger times are intentionally staggered. Workflows that may dispatch on
the same day should have at least a 60-minute gap between their nominal trigger
times. The daily stock monitor trigger still exists on weekends, but its handler
self-skips before dispatching GitHub Actions.

The 5-minute orchestrator is not installed by `installAllWorkflowTriggers` and
does not run while no TDCC chain exists. It is created by the Saturday TDCC
event, switches to a one-time 30-minute trigger while official data is absent,
and removes itself after the TDCC and individual refresh chain completes. It
must never be replaced with a fixed sleep or fixed post-TDCC clock time. The
independent daily 22:20 individual refresh remains installed as a safety net.

Research/backtest cadence is intentionally external to
`research_backtest_pipeline.yml`. The GitHub workflow itself is
`workflow_dispatch` only; the biweekly cadence belongs to Apps Script so that a
workflow run always executes the requested research steps without a hidden
internal date gate.

## Deployment Note

This repository stores the canonical Apps Script source, but it does not include
a `.clasp.json` deployment binding. If the Apps Script editor still has an older
copy, paste the current contents of `docs/apps_script_workflow_trigger.gs` into
the Apps Script project before running the recovery flow.
