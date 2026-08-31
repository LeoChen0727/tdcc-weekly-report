# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-08-31 19:48:20 Asia/Taipei
- main_price_date: 20260831
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20260831
- futures_options_indicators_latest.csv: 20260831
- TWSE market index: 20260831
- TPEx market index: 20260831

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20260831 | 46,128 | 3.05% | 6.32% | True | True | range_bound | elevated_risk |
| TPEx | 20260831 | 401.7 | 4.04% | 10.69% | True | False | range_bound | elevated_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -82,970 | TX futures direction anchor |
| foreign_futures_net_oi | -487,918 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 96.12% | hedging background only |
| taiwan_vix | 24.46 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 4,988 | contrarian sentiment proxy only |
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
    latest: 24.46
    percentile_252d: 0.7246
    percentile_504d: 
    rank_label: lower_quartile
    context_label: complacency_low_vol
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 4988.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 19.697
    percentile_504d: 
    rank_label: lower_quartile
    context_label: retail_short_elevated
    index_interpretation: retail_positioning_observe
  combined:
    combined_sentiment_interpretation: sentiment_mixed_observe
    sentiment_warning_level: low
    sample_status: short_history
    data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

ChatGPT-friendly summary:
- VIX context: complacency_low_vol / vix_context_neutral_observe
- Retail MTX context: retail_short_elevated / retail_positioning_observe
- Combined: sentiment_mixed_observe (warning=low)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
