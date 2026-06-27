# Apps Script GitHub Actions Trigger

This document is the standard operating note for the Google Apps Script source
that dispatches GitHub Actions workflows for this repository.

Canonical source file:

```text
docs/apps_script_workflow_trigger.gs
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
- Repository permissions: Actions = read and write.
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
triggerTdccHistoryGapRepair
triggerIndividualStockDataRefresh
triggerEventCatalystUpdate
triggerWeeklyThemeReview
triggerResearchBacktestPipeline
installBiweeklyResearchBacktestTrigger
installAllWorkflowTriggers
listAllTriggers
testGithubTokenAndWorkflowAccess
```

`triggerDailyStockMonitor` dispatches `.github/workflows/daily_full_pipeline.yml`
and is the function used by the scheduled daily stock monitor trigger.

`triggerDailyFullPipeline` is the manual full daily pipeline dispatcher.

`triggerDailyPriceGapRepair` dispatches
`.github/workflows/repair_recent_daily_price_gaps.yml` with a 7 calendar-day
lookback and a maximum of 5 automatic repair dates. The workflow excludes the
current Asia/Taipei date and uses the repository non-trading-day calendar before
attempting repairs.

`triggerTdccWeeklyReport` dispatches the TDCC weekly report workflow.

`triggerTdccHistoryGapRepair` dispatches
`.github/workflows/repair_tdcc_monthly_history_gaps.yml`. The workflow checks
official TDCC query-form dates in the current calendar month, excludes the
current Asia/Taipei ISO week, and repairs missing TDCC history rows only for the
bounded TDCC report universe.

`triggerIndividualStockDataRefresh` dispatches
`.github/workflows/individual_stock_data_refresh.yml`.

`triggerEventCatalystUpdate` dispatches `.github/workflows/event_catalyst_update.yml`.

`triggerWeeklyThemeReview` dispatches `.github/workflows/weekly_theme_review.yml`.

`triggerResearchBacktestPipeline` dispatches
`.github/workflows/research_backtest_pipeline.yml` with all research inputs set
to `true`. It is the function used by the scheduled biweekly research/backtest
trigger.

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
403 = token lacks Actions read/write permission
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

The canonical Apps Script source currently installs:

| handler | cadence | workflow |
|---|---|---|
| `triggerDailyPriceGapRepair` | daily 08:30 Asia/Taipei, skips Saturday/Sunday in handler | `repair_recent_daily_price_gaps.yml` |
| `triggerDailyStockMonitor` | daily 19:30 Asia/Taipei, skips Saturday/Sunday in handler | `daily_full_pipeline.yml` |
| `triggerIndividualStockDataRefresh` | daily 22:20 Asia/Taipei | `individual_stock_data_refresh.yml` |
| `triggerEventCatalystUpdate` | daily 08:10 and 18:10 Asia/Taipei | `event_catalyst_update.yml` |
| `triggerTdccHistoryGapRepair` | Tuesday 09:00 Asia/Taipei | `repair_tdcc_monthly_history_gaps.yml` |
| `triggerTdccWeeklyReport` | Saturday 15:30 Asia/Taipei | `tdcc_weekly.yml` |
| `triggerWeeklyThemeReview` | Sunday 18:30 Asia/Taipei | `weekly_theme_review.yml` |
| `triggerResearchBacktestPipeline` | every 2 weeks, Sunday 20:30 Asia/Taipei | `research_backtest_pipeline.yml` |

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
