# Market Sentiment Context

- generated_at: `2026-10-27 19:43:43 Asia/Taipei`
- date: `20261027`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `29.86`
- 252D high / low: `44.33` / `21.18`
- 252D percentile: `34.48%`
- 504D percentile: `-`
- z-score 252D: `-0.54`
- vix_return_5d / 10d / 20d: `13.41%` / `21.63%` / `35.42%`
- vix_context_label: `normal_range`
- vix_index_interpretation: `vix_context_neutral_observe`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `12,631`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `92.22%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_extreme_long`
- retail_mtx_index_interpretation: `retail_positioning_observe`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 46,096 | -7.48% | -7.48% | -7.48% | False | False |
| TPEx | 379.2 | -12.32% | -12.32% | -16.38% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `medium`
- foreign_tx_futures_net_oi: `-86,043`
- foreign_futures_net_oi: `-479,757` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `61.96%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
