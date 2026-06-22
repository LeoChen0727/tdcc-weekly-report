# Model Surface Registry Governance

`config/model_surface_registry.csv` is the top-level governance registry for
Taiwan stock model surfaces. It is broader than the stock model contract.

Its job is to classify each model or model-adjacent surface before work is
routed to an implementation lane.

## What It Covers

The registry covers:

- formal individual-stock entry models;
- TDCC/chip-related stock models;
- theme-level fund-flow models such as `group_fund_rotation`;
- event and catalyst overlay surfaces;
- research/backtest advisory variants;
- PDF consumer surfaces that read model outputs without owning model logic.

This registry does not replace the formal contracts:

- `config/stock_model_contract_registry.csv` remains the source of truth for
  formal stock entry model contracts.
- `config/event_catalyst_overlay_contract.csv` remains the source of truth for
  event/catalyst overlay effects.

## Boundary

`group_fund_rotation` belongs in `model_surface_registry.csv`, not in
`stock_model_contract_registry.csv`. It observes theme-level fund movement and
does not produce an individual-stock entry signal.

That distinction matters because stock-model consumers, research parity checks,
and TDCC weekly model allowlists should not treat a theme rotation section as a
stock entry model.

## Change Rule

When adding or reclassifying a model surface:

1. Update `config/model_surface_registry.csv`.
2. If the surface is a stock entry model, also update
   `config/stock_model_contract_registry.csv` when the stock contract surface is
   affected.
3. If the surface is an event/catalyst overlay, also update
   `config/event_catalyst_overlay_contract.csv` when overlay effects change.
4. Keep research/backtest variants advisory-only unless there is an explicit
   promotion or sync PR.
5. Do not use this registry to change scoring, ranking, or production model
   conditions.

## Validation

Run:

```text
python scripts/validate_model_surface_registry.py
```

The validator checks schema, unique `surface_id`, strict boolean fields,
repo-relative source paths, alignment with `stock_model_contract_registry.csv`,
and the required non-stock classification for `group_fund_rotation`.
