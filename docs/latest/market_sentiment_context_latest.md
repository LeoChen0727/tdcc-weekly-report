# Market Sentiment Context

- generated_at: `2026-11-11 19:49:03 Asia/Taipei`
- date: `20261111`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `38.34`
- 252D high / low: `46.62` / `21.18`
- 252D percentile: `82.16%`
- 504D percentile: `-`
- z-score 252D: `0.91`
- vix_return_5d / 10d / 20d: `7.58%` / `39.82%` / `52.38%`
- vix_context_label: `elevated_hedging`
- vix_index_interpretation: `possible_panic_contrarian_signal`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `3,386`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `17.17%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_short_elevated`
- retail_mtx_index_interpretation: `retail_positioning_observe`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 44,257 | -8.98% | -11.17% | -11.17% | False | False |
| TPEx | 344.11 | -18.09% | -20.43% | -24.12% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `possible_contrarian_rebound_watch`
- sentiment_warning_level: `medium`
- foreign_tx_futures_net_oi: `-104,271`
- foreign_futures_net_oi: `-381,366` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `65.17%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
