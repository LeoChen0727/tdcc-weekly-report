# Daily Official Report External Archive

This contract owns non-destructive archival copies of dated official daily
report bundles under `chatgpt_side_outputs_official`.

## Retention Authority

The command never derives a report date from the computer clock.

- `current` comes from `origin/main:output/latest/report_manifest_latest.json`
  and `origin/main:output/latest/data_freshness_latest.csv`. Both must agree,
  and all formal readiness fields must pass.
- `baseline` is the dated bundle immediately before `current`. Its
  `chatgpt_daily_report_runtime_manifest.json` and six-PDF contract must pass.
- Only bundles older than `baseline` are eligible. An older incomplete bundle,
  including a historical five-PDF bundle, is copied exactly as found. The
  command does not invent or replace missing files.

Only PDF, PNG, CSV, and JSON files are admitted. A source reparse point,
unsupported extension, authority conflict, missing current/baseline contract,
or unexpected source-root entry fails closed.

## Command

Run validation first from the merged repository code:

```powershell
python scripts/archive_daily_official_report_bundles.py `
  --repo-root . `
  --authority-ref origin/main `
  --source-root C:\Users\p4693\Documents\Codex\projects\taiwan-stock-recommendation\production\tdcc-daily-production\chatgpt_side_outputs_official `
  --destination-root F:\CodexStorage\report-archive\taiwan-stock-recommendation `
  --expected-destination-volume F: `
  --execution-report-dir C:\Users\p4693\Documents\Codex\workspace_admin\reports
```

Add `--copy` only after validation passes. A bounded pilot may add one or more
`--include-date YYYYMMDD` arguments; the date must already be older than the
contract-derived baseline.

Validate the repository contract independently with:

```powershell
python scripts/validate_daily_official_report_archive_contract.py
```

The destination layout is:

```text
<destination-root>\daily\<YYYYMMDD>\<bundle-relative-path>
```

The Python code and repository contract do not hard-code an F-drive runtime
dependency. The operator supplies the authorized absolute destination and
expected volume. The command verifies that the destination exists, is on the
expected volume, uses NTFS, is outside the source tree, and has selected bytes
plus a 64 MiB safety margin.

## Copy And Evidence Contract

- Existing destination content with the same SHA-256 is an idempotent pass.
- Existing destination content with a different SHA-256 is a collision and
  blocks all copying during preflight.
- New files are copied to a destination-side temporary file, hashed, then
  committed without overwriting an existing destination.
- Every run writes a CSV file manifest and JSON execution report. Failure after
  a partial copy is still reported as failure, with each completed and pending
  row preserved.
- The report records relative path, bytes, SHA-256, source, destination, report
  date, retention reason, copy action, destination verification, and source
  recheck evidence.
- The complete source-family fingerprint is computed before and after the run.

This command is copy-only. It **不得刪除、搬移、改名或改寫** any C-drive
source, current bundle, baseline bundle, official output, or validator evidence.

## Automation Boundary

This PR does not add or change automation. The archive command must not be
called by `Daily Full Pipeline`, the official PDF entrypoint, or any GitHub
Actions workflow. Automation integration belongs to
`workflow_automation_maintenance` only after this PR is merged and a
post-merge copy/verify pilot succeeds.
