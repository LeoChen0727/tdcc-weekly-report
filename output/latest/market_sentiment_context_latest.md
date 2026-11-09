# Market Sentiment Context

- generated_at: `2026-11-09 19:50:31 Asia/Taipei`
- date: `20261109`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `43.7`
- 252D high / low: `46.62` / `21.18`
- 252D percentile: `97.81%`
- 504D percentile: `-`
- z-score 252D: `1.86`
- vix_return_5d / 10d / 20d: `39.71%` / `43.99%` / `87.63%`
- vix_context_label: `extreme_fear_or_hedging`
- vix_index_interpretation: `possible_panic_contrarian_signal`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `6,404`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `39.18%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_normal_range`
- retail_mtx_index_interpretation: `retail_positioning_normal`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 41,662 | -15.52% | -16.38% | -16.38% | False | False |
| TPEx | 321.97 | -24.76% | -25.55% | -29% | False | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `possible_contrarian_rebound_watch`
- sentiment_warning_level: `medium`
- foreign_tx_futures_net_oi: `-101,771`
- foreign_futures_net_oi: `-392,152` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `51.19%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
