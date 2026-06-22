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
- Research/backtest contract parity validation reads this registry directly as the source of truth. It does not require or recreate `output/latest/stock_model_contract_snapshot_latest.json`.
- Changing a model condition, score function, score profile, or approval flag requires a reviewed PR and validation evidence.

## Validation

Run:

```text
python scripts/validate_stock_model_contract_registry.py
```

The validator checks the registry schema, unique `model_id`, strict true/false values for the three `approved_for_*` columns, source-file existence, and alignment with `config/daily_model_condition_spec.csv`.

`input_columns` must list the source-backed model inputs used by each model's condition and scoring path. Include fallback alias columns that helper functions read, and use explicit source prefixes such as `stock_price_history.*` when a model depends on sibling data outside the current candidate row. Do not return an audited model to `pending_review` unless the source path changes and the field list can no longer be proven.
