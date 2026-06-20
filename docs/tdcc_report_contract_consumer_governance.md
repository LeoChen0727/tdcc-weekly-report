# TDCC Report Contract Consumer Governance

TDCC weekly report code is a consumer of the repository model and
event/catalyst contracts. It may read only fields and model IDs that are
explicitly allowed for `tdcc_weekly_pdf`.

## Required Contracts

- `config/stock_model_contract_registry.csv`
- `config/event_catalyst_overlay_contract.csv`

The TDCC weekly report validator is:

```text
python scripts/validate_tdcc_report_contract_consumers.py
```

The validator is required in `.github/workflows/tdcc_weekly.yml`. Unit coverage
for the contract consumer guard is:

```text
python -m pytest tests/test_tdcc_report_contract_consumers.py -q
```

## Model Contract Rule

Any `model_id` used by TDCC weekly report-ready CSVs, model-cross output, or
TDCC weekly report source allowlists must exist in
`config/stock_model_contract_registry.csv`.

The model row must have:

```text
approved_for_tdcc_weekly_pdf=true
```

TDCC weekly report code must not create a private model allowlist that bypasses
the registry.

## Event / Catalyst Contract Rule

Any event or catalyst field used by TDCC weekly report source, output CSV/MD, or
published TDCC weekly PDF surfaces must exist in
`config/event_catalyst_overlay_contract.csv`.

The field row must have:

```text
approved_for_tdcc_weekly_pdf=true
tdcc_weekly_pdf in allowed_consumers
```

Phase-one event/catalyst fields are disclosure-only. Unless the contract is
explicitly promoted with reviewed evidence:

- `disclosure_only=true` fields must not affect TDCC ranking or score.
- `score_allowed=false` fields must not enter TDCC score calculation.
- `ranking_allowed=false` fields must not affect TDCC ordering.
- `reason_text_allowed=false` fields must not become TDCC recommendation,
  strengthening, or selection-reason text.
- degraded event/catalyst sources must not strengthen TDCC recommendation
  reasons.

TDCC weekly PDFs may render program-side fields, but the PDF layer must not add
its own judgment, scoring, ranking, or recommendation rules.

## Current Consumer State

The current TDCC weekly report consumes this model contract ID:

```text
tdcc_short_term_continuation_d5_d10
```

The current TDCC weekly report-ready CSVs do not consume event/catalyst contract
fields. Future disclosure of contract-approved catalyst/event fields is allowed
only if the validator continues to pass.
