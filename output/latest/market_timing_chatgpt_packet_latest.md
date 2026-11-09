# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-11-09 19:50:30 Asia/Taipei
- main_price_date: 20261109
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20261109
- futures_options_indicators_latest.csv: 20261109
- TWSE market index: 20261109
- TPEx market index: 20261109

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20261109 | 41,662 | -7.25% | -16.35% | False | False | high_risk | very_high_risk |
| TPEx | 20261109 | 321.97 | -12.8% | -25.2% | False | False | high_risk | very_high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -101,771 | TX futures direction anchor |
| foreign_futures_net_oi | -392,152 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 51.19% | hedging background only |
| taiwan_vix | 43.7 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 6,404 | contrarian sentiment proxy only |
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
    latest: 43.7
    percentile_252d: 97.8142
    percentile_504d: 
    rank_label: top_decile
    context_label: extreme_fear_or_hedging
    index_interpretation: possible_panic_contrarian_signal
  retail_mtx:
    latest_proxy: 6404.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 39.1753
    percentile_504d: 
    rank_label: middle_range
    context_label: retail_normal_range
    index_interpretation: retail_positioning_normal
  combined:
    combined_sentiment_interpretation: possible_contrarian_rebound_watch
    sentiment_warning_level: medium
    sample_status: short_history
    data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

ChatGPT-friendly summary:
- VIX context: extreme_fear_or_hedging / possible_panic_contrarian_signal
- Retail MTX context: retail_normal_range / retail_positioning_normal
- Combined: possible_contrarian_rebound_watch (warning=medium)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
