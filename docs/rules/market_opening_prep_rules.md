# Market Opening Prep Rules

Last updated: 2026-06-03

## Purpose

This rule file controls market opening preparation, market-risk context, international background, market technical status, futures/options, VIX, Put/Call, retail MTX sentiment, and how those inputs affect daily candidate tracking.

This task is not:

- daily full-market stock recommendation
- holdings management
- single-stock analysis
- TDCC weekly report
- backtest monthly / quarterly / half-year reports

## Required Reading Order

1. `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
2. `rules/master_priority_rules.md`
3. `rules/market_opening_prep_rules.md`
4. `rules/futures_options_vix_rules.md`
5. Market and sentiment packets / CSV / Markdown.

## Required Data

Prefer repo structured data:

- `output/latest/market_regime_latest.csv`
- `output/latest/market_risk_dashboard_latest.md`
- `output/latest/market_sentiment_context_latest.csv`
- `output/latest/market_sentiment_context_latest.md`
- `output/latest/futures_options_indicators_latest.csv`
- `data/market_index_history.csv`
- `data/market_index_ohlc_history.csv`
- `output/latest/market_timing_chatgpt_packet_latest.md`
- market timing backtest files when available

PDF is a presentation artifact only and must not replace structured data.

## Market Sentiment Context

VIX and retail MTX must use historical context:

- historical high / low
- percentile
- rank
- z-score
- TWSE / TPEx index position
- market_regime
- risk_level
- Put/Call
- foreign_tx_futures_net_oi

Do not infer market direction from a single VIX, Put/Call, or retail MTX value.

If `sample_status=insufficient_history`, report:

`資料不足 / 僅能觀察`

## Output Sections

Market opening prep reports should include:

1. Data date and data status
2. Opening market conclusion
3. TWSE / TPEx technical structure
4. Futures/options and retail sentiment
5. International events and risks
6. Trading rhythm for the day
7. Effect on daily stock candidate tracking

## Required Interpretation Boundaries

- High VIX while index is strong means hedging is elevated, not direct bearish confirmation.
- High VIX after market correction can be a contrarian rebound watch only when price / breadth stabilize.
- Retail MTX extreme long at index highs means chase risk, not standalone short.
- Retail MTX extreme short after correction means rebound watch only, not standalone buy.
- `foreign_tx_futures_net_oi` is the TX direction anchor; `foreign_futures_net_oi` is broad exposure background only.
- Market context can adjust trading tempo, but cannot replace stock-level model conditions.
