# Volume Range Breakout V2 Promotion Readiness Audit

This spec defines a research-only audit for deciding whether the v2
`volume_range_breakout` split has enough evidence for a later promotion
discussion.

It does not change `config/stock_model_contract_registry.csv`, production
ranking, scoring, operation adapters, packets, or PDF behavior.

## Source

The audit consumes:

`output/latest/research_backtest/volume_range_breakout_v2_research_contract_detail_latest.csv`

The source must already be research-only, same-stock non-overlap, confirmed by
`next_day_continuation_confirmed_close_only`, and split into:

- `volume_range_breakout_v2_momentum_continuation`
- `volume_range_breakout_v2_low_base_consolidation`

## Return Windows

The audit must compare:

- D+10 close
- D+15 close
- D+20 close
- D+30 close

Each window is tested with:

- no-stop reference
- close-confirmed MA20/EMA23 stop

The MA20/EMA23 stop is:

`sustained_close_below_lower_ma20_ema23_4pct_4d`

It exits at the next trading day open after four consecutive closes below
`min(MA20, EMA23) * 0.96`.

## Required Checks

The audit must report:

- base performance by model, holding window, and stop policy
- invalid return counts and invalid return rates
- 1% tail-trim anomaly sensitivity
- stop-exit counts
- TDCC top20 stratification
- 23EMA-like technical stratification
- 120/240-day low-base redefinition stratification

## Promotion Boundary

Rows can only set `metric_threshold_met=True` when sample size, win rate,
average return, and median return meet the configured metric threshold.

Even then, rows remain research-only and must carry promotion blockers until a
separate production promotion PR updates registry, parity, operation adapter,
packet/PDF contracts, and post-merge evidence.

Stratification rows must use:

`condition_role=stratification_only_not_candidate_or_confirmation_gate`

No TDCC, 23EMA, or low-base redefinition row may become a hidden gate in this
audit.
