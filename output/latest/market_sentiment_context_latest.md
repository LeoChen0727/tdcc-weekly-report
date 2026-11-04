# Market Sentiment Context

- generated_at: `2026-11-04 19:47:26 Asia/Taipei`
- date: `20261104`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `35.64`
- 252D high / low: `44.33` / `21.18`
- 252D percentile: `59.44%`
- 504D percentile: `-`
- z-score 252D: `0.49`
- vix_return_5d / 10d / 20d: `29.98%` / `20%` / `62.74%`
- vix_context_label: `normal_range`
- vix_index_interpretation: `vix_context_neutral_observe`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `9,320`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `69.79%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_normal_range`
- retail_mtx_index_interpretation: `retail_positioning_normal`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 42,949 | -13.8% | -13.8% | -13.8% | False | False |
| TPEx | 343.5 | -20.57% | -20.57% | -24.26% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- foreign_tx_futures_net_oi: `-93,647`
- foreign_futures_net_oi: `-457,873` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `49.37%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
