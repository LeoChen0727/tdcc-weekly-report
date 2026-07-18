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
repository lifecycle and production inventories. The scope contract and the
historical PR #404 file set are fixed by
`tests/test_individual_stock_pr_validation_workflow.py`.

Affected pull requests run these commands without generating or publishing
artifacts:

```text
python scripts/validate_repo_file_lifecycle_inventory.py
python scripts/validate_repo_production_inventory.py
python scripts/validate_individual_pdf_contract_consumers.py
python -m pytest tests/test_individual_stock_outputs.py -q
```

The workflow also runs `git diff --check` and the scoping regression test. Its
permissions are read-only. It must not commit, push, deploy Pages, or dispatch
another repository workflow.

## Main branch enforcement

The repository main ruleset requires `individual-stock-pr-validation` from the
GitHub Actions integration. Human changes must enter `main` through a pull
request. The GitHub Actions integration is the only direct-push bypass actor so
production workflows can continue committing generated artifacts. Force pushes
and branch deletion remain blocked for all non-bypass actors.
