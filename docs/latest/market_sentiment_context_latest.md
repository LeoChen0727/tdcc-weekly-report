# Market Sentiment Context

- generated_at: `2026-11-02 19:45:39 Asia/Taipei`
- date: `20261102`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `31.28`
- 252D high / low: `44.33` / `21.18`
- 252D percentile: `43.26%`
- 504D percentile: `-`
- z-score 252D: `-0.28`
- vix_return_5d / 10d / 20d: `3.06%` / `2.19%` / `35.76%`
- vix_context_label: `normal_range`
- vix_index_interpretation: `vix_context_neutral_observe`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `6,899`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `43.62%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_normal_range`
- retail_mtx_index_interpretation: `retail_positioning_normal`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 44,920 | -9.84% | -9.84% | -9.84% | False | False |
| TPEx | 369.24 | -14.62% | -14.62% | -18.58% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- foreign_tx_futures_net_oi: `-89,379`
- foreign_futures_net_oi: `-465,891` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `61.58%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
