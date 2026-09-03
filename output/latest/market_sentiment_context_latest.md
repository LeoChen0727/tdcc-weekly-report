# Market Sentiment Context

- generated_at: `2026-09-03 19:50:10 Asia/Taipei`
- date: `20260903`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `25.66`
- 252D high / low: `44.33` / `24.46`
- 252D percentile: `2.84%`
- 504D percentile: `-`
- z-score 252D: `-1.95`
- vix_return_5d / 10d / 20d: `-5.31%` / `-14.52%` / `-28.86%`
- vix_context_label: `complacency_low_vol`
- vix_index_interpretation: `vix_context_neutral_observe`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `387`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-1,332`
- 252D percentile: `2.9%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_extreme_short`
- retail_mtx_index_interpretation: `retail_extreme_short_possible_rebound_watch`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 45,858 | -2.32% | -3.95% | -3.95% | True | True |
| TPEx | 395.25 | -3.78% | -12.84% | -12.84% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `possible_contrarian_rebound_watch`
- sentiment_warning_level: `low`
- foreign_tx_futures_net_oi: `-81,575`
- foreign_futures_net_oi: `-504,806` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `77.16%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
