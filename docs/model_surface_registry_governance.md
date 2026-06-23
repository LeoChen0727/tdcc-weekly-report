# Model Surface Registry Governance

`config/model_surface_registry.csv` is the top-level governance registry for
Taiwan stock model surfaces. It is broader than the stock model contract.

Its job is to classify each model or model-adjacent surface before work is
routed to an implementation lane.

## What It Covers

The registry covers:

- formal individual-stock entry models;
- TDCC/chip-related stock models;
- TDCC weekly report ranking formulas such as `tdcc_weekly_ranking_formula`;
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

`tdcc_weekly_ranking_formula` also belongs in `model_surface_registry.csv`, not
in `stock_model_contract_registry.csv`. It ranks TDCC weekly holder-flow report
sections and is approved for TDCC weekly PDF use, but it is not a daily stock
entry signal and must not be treated as a production buy model. The
research/backtest mirror is advisory-only unless a separate promotion PR changes
that status.

Taiwan stock taxonomy is an upstream classification layer, not an individual
stock entry model by itself. Mainstream / non-mainstream grouping, hot-theme
classification, industry/theme mapping, and theme-level fund rotation inputs
should be owned by a dedicated taxonomy maintenance role once that role is
registered in the project-level conversation lane registry. Those taxonomy
surfaces may feed stock models, PDFs, and research/backtest, but taxonomy
changes must not silently change model scoring or ranking without a formal
model-change PR.

For breakout-related model work, use
`docs/specs/breakout_model_taxonomy_governance_handoff.md` as the handoff
between taxonomy classification, breakout event features, and formal stock
entry models.

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
script-declared `MODEL_ID` / `*_MODEL_ID` coverage, and the required non-stock
classification for `group_fund_rotation` and `tdcc_weekly_ranking_formula`.
