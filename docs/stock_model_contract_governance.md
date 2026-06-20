# Stock Model Contract Governance

## Purpose

`config/stock_model_contract_registry.csv` is the formal contract registry for production stock models. It gives TDCC weekly, daily PDF, individual PDF, and research/backtest consumers a stable way to identify which model outputs they may read.

The registry records ownership and consumer approval. It does not define model conditions, scoring weights, ranking rules, or promotion decisions.

## Ownership

- `owner_lane` owns the contract row and consumer approval flags.
- `production_source_file` points to the production implementation source.
- `condition_function`, `score_function`, and `score_profile_id` must match `config/daily_model_condition_spec.csv` for existing production models.
- Any field that cannot be proven from current source must use `pending_review`.

## Consumer Rules

- Daily PDF consumers may use rows with `approved_for_daily_pdf=true`.
- TDCC weekly consumers may use rows with `approved_for_tdcc_weekly_pdf=true`.
- Individual PDF consumers may use rows with `approved_for_individual_pdf=true`.
- Consumers must not treat a missing approval as implicit permission.
- Research/backtest may compare against this registry, but must not write research recommendations into production baseline tables without an explicit promotion PR.
- Changing a model condition, score function, score profile, or approval flag requires a reviewed PR and validation evidence.

## Validation

Run:

```text
python scripts/validate_stock_model_contract_registry.py
```

The validator checks the registry schema, unique `model_id`, strict true/false values for the three `approved_for_*` columns, source-file existence, and alignment with `config/daily_model_condition_spec.csv`.

The initial registry intentionally keeps `input_columns=pending_review` because existing model conditions read columns through helper functions. That field should be replaced by model-specific input column lists only after a source-backed audit.
