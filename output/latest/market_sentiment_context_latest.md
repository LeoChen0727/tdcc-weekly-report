# Market Sentiment Context

- generated_at: `2026-08-21 04:35:11 Asia/Taipei`
- date: `20260820`
- sample_status: `short_history`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

## VIX Historical Context

- Taiwan VIX latest: `30.83`
- 252D high / low: `44.33` / `25.68`
- 252D percentile: `22.14%`
- 504D percentile: `-`
- z-score 252D: `-1.05`
- vix_return_5d / 10d / 20d: `-3.29%` / `-12.84%` / `-14.69%`
- vix_context_label: `complacency_low_vol`
- vix_index_interpretation: `vix_context_neutral_observe`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `8,964`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `16,227` / `1,266`
- 252D percentile: `60.66%`
- 504D percentile: `-`
- retail_mtx_context_label: `retail_normal_range`
- retail_mtx_index_interpretation: `retail_positioning_normal`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 44,934 | -2.36% | -5.88% | -5.88% | True | True |
| TPEx | 389.96 | -3.98% | -14.01% | -14.01% | True | False |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- foreign_tx_futures_net_oi: `-81,501`
- foreign_futures_net_oi: `-438,016` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `102.27%`

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
