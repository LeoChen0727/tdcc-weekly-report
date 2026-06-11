# Apps Script Daily Monitor Recovery

Use this when the Apps Script executions page shows
`triggerDailyStockMonitor` failed quickly, especially in about 1-2 seconds.

If GitHub Actions has no matching `Daily Full Pipeline` `workflow_dispatch`
run at that scheduled time, GitHub did not receive the dispatch. Treat that as
an Apps Script token/configuration failure, not as a daily pipeline runtime
failure.

## Manual Recovery

Run these functions manually in Apps Script, in this order:

```text
diagnoseDailyStockMonitorTrigger
installDailyStockMonitorTrigger
triggerDailyStockMonitor
```

Expected diagnostic success signs:

```text
Status code: 200
GitHub token and workflow access OK.
Daily stock monitor diagnostics OK.
```

## Required Script Property

Set this in Apps Script Project Settings:

```text
GITHUB_PAT=<token>
```

`GITHUB_TOKEN` is accepted only as a fallback property name.

The token must be able to access `LeoChen0727/tdcc-weekly-report` and must have
repository Actions read/write permission.

## Failure Meanings

- `Missing Script Property`: set `GITHUB_PAT` or `GITHUB_TOKEN`.
- `401`: replace the token; it is missing, expired, or invalid.
- `403`: token lacks repository Actions read/write permission or is blocked.
- `404`: token cannot see the repo or `daily_full_pipeline.yml`.
- `422`: workflow dispatch ref/payload is invalid.

After updating the Apps Script source or token, run
`installDailyStockMonitorTrigger` to recreate the scheduled trigger. This
removes old `triggerDailyStockMonitor` triggers and installs a fresh daily
19:30 Asia/Taipei trigger.
