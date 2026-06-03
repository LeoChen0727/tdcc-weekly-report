# Futures / Options / VIX Rules

Last updated: 2026-06-03

## Purpose

This rule file controls Taiwan index futures, options, Taiwan VIX, Put/Call, and retail MTX sentiment interpretation for tdcc-weekly-report tasks.

## Required Data

Always prefer repo structured data:

- `output/latest/futures_options_indicators_latest.csv`
- `output/latest/market_sentiment_context_latest.csv`
- `output/latest/market_sentiment_context_latest.md`
- `output/history/market_risk/vix_history.csv`
- `output/history/market_risk/retail_mtx_sentiment_history.csv`
- `output/history/market_risk/futures_options_indicators_history.csv`

## VIX Context

Taiwan VIX must not be interpreted only by the latest value or 5D / 10D / 20D return.

Required context:

- 252D high / low / percentile
- 504D high / low / percentile when available
- 252D z-score
- rank label
- context label
- TWSE / TPEx position
- market_regime
- risk_level
- Put/Call
- foreign_tx_futures_net_oi

If history is insufficient, use:

- `sample_status=insufficient_history`
- `vix_context_label=insufficient_history`
- report wording: `資料不足 / 僅能觀察`

## Retail MTX Context

Retail MTX proxy must not be interpreted only by the latest number.

Required context:

- 252D high / low / percentile
- 504D high / low / percentile when available
- 252D z-score
- rank label
- context label
- TWSE / TPEx position
- market_regime
- risk_level

If history is insufficient, use:

- `sample_status=insufficient_history`
- `retail_mtx_context_label=insufficient_history`
- report wording: `資料不足 / 僅能觀察`

## Interpretation Rules

- `foreign_tx_futures_net_oi` is the TX futures direction anchor.
- `foreign_futures_net_oi` is broad foreign futures exposure background only; do not treat it as TX direction.
- Put/Call can indicate hedging demand, but cannot be used alone to forecast market direction.
- Taiwan VIX, Put/Call, and retail MTX are auxiliary market-risk context only.
- Do not use VIX or retail MTX as standalone buy/sell signals.

## Cross Labels

- `index_strong_but_hedging_elevated`: VIX percentile is elevated while TWSE / TPEx remain strong. This means hedging demand is higher, not direct bearish confirmation.
- `possible_panic_contrarian_signal`: VIX is high while index has corrected or entered high-risk regime. This is only a rebound watch after price / breadth stabilization, not a buy signal.
- `low_vol_complacency_at_high`: VIX is low while index is near highs. This is high-level complacency / chase-risk context, not an immediate short signal.
- `retail_overlong_chase_risk`: retail MTX proxy is extreme long while index is high. This is crowded-chase risk, not a standalone short signal.
- `retail_extreme_short_possible_rebound_watch`: retail MTX proxy is extreme short while market has corrected. This is rebound watch only after price / breadth confirmation.
- `insufficient_history_observe_only`: required VIX or retail MTX history is insufficient. Report `資料不足 / 僅能觀察`.

## Output Rule

Reports must use `market_sentiment_context_latest.csv` / `.md` when available and must clearly state whether the conclusion is ready, short-history, or insufficient-history.
