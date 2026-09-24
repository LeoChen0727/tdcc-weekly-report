# Market Sentiment Context

- generated_at: `2026-09-24 19:49:20 Asia/Taipei`
- date: `20260924`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `23.12`
- 252D high / low: `44.33` / `21.18`
- 252D percentile: `3.21%`
- 504D percentile: `-`
- z-score 252D: `-1.98`
- vix_return_5d / 10d / 20d: `-3.87%` / `-12.02%` / `-14.69%`
- vix_context_label: `complacency_low_vol`
- vix_index_interpretation: `low_vol_complacency_at_high`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `7,415`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `-3,246`
- 252D percentile: `54.88%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_normal_range`
- retail_mtx_index_interpretation: `retail_positioning_normal`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 48,025 | -0.28% | -0.28% | -0.28% | True | True |
| TPEx | 412.99 | -0.53% | -7.27% | -8.93% | True | True |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- foreign_tx_futures_net_oi: `-77,031`
- foreign_futures_net_oi: `-479,535` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `85.33%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
