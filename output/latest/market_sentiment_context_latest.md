# Market Sentiment Context

- generated_at: `2026-07-07 05:06:49 Asia/Taipei`
- date: `20260706`
- sample_status: `insufficient_history`
- data_quality_note: 資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。

## VIX Historical Context

- Taiwan VIX latest: `36.89`
- 252D high / low: `44.01` / `25.68`
- 252D percentile: `63.64%`
- 504D percentile: `-`
- z-score 252D: `0.42`
- vix_return_5d / 10d / 20d: `-7.73%` / `-2.48%` / `1.71%`
- vix_context_label: `normal_range`
- vix_index_interpretation: `trend_supported_no_extreme_vix`

VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `5,173`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low: `-` / `-`
- 252D percentile: `-`
- 504D percentile: `-`
- retail_mtx_context_label: `insufficient_history`
- retail_mtx_index_interpretation: `insufficient_history_observe_only`

Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.

## Index Position Inputs

| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| TWSE | 46,556 | -2.48% | -2.48% | -2.48% | True | True |
| TPEx | 439.8 | -3.02% | -3.02% | -3.02% | True | True |

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `insufficient_history_observe_only`
- sentiment_warning_level: `insufficient`
- foreign_tx_futures_net_oi: `-80,087`
- foreign_futures_net_oi: `-594,361` (whole futures exposure background only, not TX direction)
- put_call_oi_ratio_pct: `122.22%`

資料不足 / 僅能觀察：目前 VIX / 散戶小台缺少足夠歷史分位資料，不可作為反指標結論。

## Usage Boundary

- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Use this context as market-risk background for daily reports and opening-prep analysis.
