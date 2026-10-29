# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-10-29 19:49:30 Asia/Taipei
- main_price_date: 20261029
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20261029
- futures_options_indicators_latest.csv: 20261029
- TWSE market index: 20261029
- TPEx market index: 20261029

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20261029 | 46,368 | 0.16% | -3.45% | False | False | high_risk | very_high_risk |
| TPEx | 20261029 | 387.37 | -0.13% | -6.2% | False | False | high_risk | very_high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -89,522 | TX futures direction anchor |
| foreign_futures_net_oi | -496,089 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 64.46% | hedging background only |
| taiwan_vix | 28.26 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 12,913 | contrarian sentiment proxy only |
| retail_mtx_proxy_method | negative_sum_of_three_institution_mtx_net_oi | source method |

## Usage Boundary
- This packet is daily market context only; it is not a stock recommendation list.
- VIX, Put/Call, retail MTX, and foreign futures fields must be cross-checked with TWSE / TPEx position and market_regime.
- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.
- Research/backtest scripts must not overwrite this daily packet in the daily pipeline.

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## MARKET_SENTIMENT_CONTEXT

market_sentiment_context:
  taiwan_vix:
    latest: 28.26
    percentile_252d: 25.0
    percentile_504d: 
    rank_label: lower_quartile
    context_label: complacency_low_vol
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 12913.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 93.4783
    percentile_504d: 
    rank_label: top_decile
    context_label: retail_extreme_long
    index_interpretation: retail_positioning_observe
  combined:
    combined_sentiment_interpretation: sentiment_mixed_observe
    sentiment_warning_level: medium
    sample_status: short_history
    data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

ChatGPT-friendly summary:
- VIX context: complacency_low_vol / vix_context_neutral_observe
- Retail MTX context: retail_extreme_long / retail_positioning_observe
- Combined: sentiment_mixed_observe (warning=medium)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
