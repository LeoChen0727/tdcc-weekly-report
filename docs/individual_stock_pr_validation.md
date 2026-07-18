# Individual Stock Pull Request Validation

## Required check

Every pull request creates the stable GitHub check context
`individual-stock-pr-validation`. The workflow does not use a workflow-level
path filter because a globally required check must report a conclusion for
unrelated pull requests too.

The PR-safe workflow is
`.github/workflows/individual_stock_pr_validation.yml`. It uses
`scripts/detect_individual_stock_pr_scope.py` to classify changed paths inside
the job. Unrelated changes run the lightweight workflow contract test and
succeed without running the individual-stock data tests.

## Affected changes

Affected changes include individual-stock builders, validators, tests,
contracts, report workflows, generated individual-stock report roots, and the
repository lifecycle and production inventories. Changes to any of the twelve
registered production artifact-writer workflows are also affected so their
deploy-key authentication contract always runs in pull requests. The scope
contract and the historical PR #404 file set are fixed by
`tests/test_individual_stock_pr_validation_workflow.py`.

The registered artifact-writer workflows are:

```text
.github/workflows/current_holdings_pattern.yml
.github/workflows/daily_full_pipeline.yml
.github/workflows/individual_stock_data_refresh.yml
.github/workflows/individual_stock_report.yml
.github/workflows/repair_daily_price_range.yml
.github/workflows/repair_one_daily_price.yml
.github/workflows/repair_recent_daily_price_gaps.yml
.github/workflows/repair_tdcc_monthly_history_gaps.yml
.github/workflows/research_backtest_pipeline.yml
.github/workflows/tdcc_history_backfill.yml
.github/workflows/tdcc_weekly.yml
.github/workflows/warrant_flow.yml
```

Affected pull requests run these commands without generating or publishing
artifacts:

```text
python scripts/validate_repo_file_lifecycle_inventory.py
python scripts/validate_repo_production_inventory.py
python scripts/validate_individual_pdf_contract_consumers.py
python -m pytest tests/test_repo_production_inventory.py -q
python -m pytest tests/test_individual_stock_outputs.py -q
```

The workflow also runs `git diff --check` and the scoping regression test. Its
permissions are read-only. It must not commit, push, deploy Pages, or dispatch
another repository workflow.

## Main branch enforcement

Main is protected by two independent repository rulesets:

1. The policy ruleset requires pull requests and the
   `individual-stock-pr-validation` check from the GitHub Actions integration.
   Its only bypass actor is the dedicated write deploy key used by registered
   production artifact writers.
2. The ref-integrity ruleset blocks branch deletion and non-fast-forward
   updates without any bypass actor. The deploy key therefore cannot delete or
   force-push `main`.

Every registered artifact-writer job fails closed before checkout when
`PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY` is empty. Its writer checkout must use
that secret as `ssh-key` and set `persist-credentials: true` in the same
`actions/checkout` step. Non-writer jobs and pull-request workflows must never
receive the secret. `scripts/validate_repo_production_inventory.py` and its
regression tests enforce this contract.
