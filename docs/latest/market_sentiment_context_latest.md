# Market Sentiment Context

- generated_at: `2026-11-12 19:44:50 Asia/Taipei`
- date: `20261112`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `40.28`
- 252D high / low: `46.62` / `21.18`
- 252D percentile: `92.47%`
- 504D percentile: `-`
- z-score 252D: `1.24`
- vix_return_5d / 10d / 20d: `0.88%` / `42.53%` / `50.75%`
- vix_context_label: `extreme_fear_or_hedging`
- vix_index_interpretation: `possible_panic_contrarian_signal`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `4,155`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `25%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_short_elevated`
- retail_mtx_index_interpretation: `retail_positioning_observe`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 43,092 | -11.38% | -13.51% | -13.51% | False | False |
| TPEx | 335.73 | -20.09% | -22.37% | -25.97% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `possible_contrarian_rebound_watch`
- sentiment_warning_level: `medium`
- foreign_tx_futures_net_oi: `-99,573`
- foreign_futures_net_oi: `-386,853` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `66.69%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
