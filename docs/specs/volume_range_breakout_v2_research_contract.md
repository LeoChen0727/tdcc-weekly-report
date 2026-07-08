# Volume Range Breakout V2 Research Contract

This spec defines a research-only contract for splitting the legacy
`volume_range_breakout` study into two candidate semantics:

- `volume_range_breakout_v2_momentum_continuation`
- `volume_range_breakout_v2_low_base_consolidation`

It does not change `config/stock_model_contract_registry.csv`, production
ranking, production scoring, operation adapters, packets, or PDF behavior.

## Source Scope

The contract consumes:

`output/latest/research_backtest/volume_range_breakout_v2_split_feature_audit_detail_latest.csv`

The source must already be:

- `approved_for_daily=False`
- `production_readiness=not_production_ready_research_only`
- same-stock non-overlap
- split into `momentum_continuation` and `low_base_consolidated`

## Model Split

`volume_range_breakout_v2_momentum_continuation` uses the complement of the
low-base/consolidated group. It represents a research-only strong momentum
continuation candidate.

`volume_range_breakout_v2_low_base_consolidation` uses rows where:

- `off_60d_low_pct <= 50`
- `range_width_60_pct <= 45`
- `consolidation_type` is `short_consolidation` or `long_consolidation`

The two research model ids must be mutually exclusive, and their union must
equal the confirmed same-stock non-overlap source sample.

## Candidate And Confirmation

Candidate conditions are model-owned rows in
`volume_range_breakout_v2_research_contract_latest.csv`.

The confirmation rule is:

`next_day_continuation_confirmed_close_only`

The confirmation rule is close-confirmed: the next trading day close must be
above the signal-day close and no lower than the signal-day high. Entry is the
next trading day open after the confirmation close.

## Return Basis

The base performance rows must use confirmed samples only. They must not include
pending, unconfirmed, rejected, or same-stock overlapping rows.

The artifact compares two research return bases:

- `fixed_d20_close_no_stop_reference`
- `fixed_d20_close_with_23ema_close_stop`

The 23EMA-like stop is close-confirmed:

`sustained_close_below_lower_ma20_ema23_4pct_4d`

It exits at the next trading day open after four consecutive closes below
`min(MA20, EMA23) * 0.96`.

## Stratification-Only Conditions

TDCC top20 and 23EMA-like technical conditions must be emitted only in
`volume_range_breakout_v2_research_contract_stratification_latest.csv` with:

`condition_role=stratification_only_not_candidate_or_confirmation_gate`

They must not become hidden candidate, confirmation, ranking, or buy gates in
this research contract.

Promotion into production requires a separate model-promotion PR, registry
changes, parity validation, operation adapter contract, and post-merge evidence.
