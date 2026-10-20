# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-10-20 19:47:07 Asia/Taipei
- main_price_date: 20261020
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20261020
- futures_options_indicators_latest.csv: 20261020
- TWSE market index: 20261020
- TPEx market index: 20261020

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20261020 | 46,293 | -4.24% | 0.01% | False | True | high_risk | very_high_risk |
| TPEx | 20261020 | 387.88 | -6.38% | -2.58% | False | False | high_risk | very_high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -89,748 | TX futures direction anchor |
| foreign_futures_net_oi | -532,129 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 66.17% | hedging background only |
| taiwan_vix | 30.82 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 9,142 | contrarian sentiment proxy only |
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
    latest: 30.82
    percentile_252d: 39.7661
    percentile_504d: 
    rank_label: middle_range
    context_label: normal_range
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 9142.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 71.5909
    percentile_504d: 
    rank_label: middle_range
    context_label: retail_normal_range
    index_interpretation: retail_positioning_normal
  combined:
    combined_sentiment_interpretation: sentiment_mixed_observe
    sentiment_warning_level: low
    sample_status: short_history
    data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

ChatGPT-friendly summary:
- VIX context: normal_range / vix_context_neutral_observe
- Retail MTX context: retail_normal_range / retail_positioning_normal
- Combined: sentiment_mixed_observe (warning=low)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
