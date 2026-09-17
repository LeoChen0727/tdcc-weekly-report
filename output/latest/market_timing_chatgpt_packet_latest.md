# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-09-17 19:50:16 Asia/Taipei
- main_price_date: 20260917
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20260917
- futures_options_indicators_latest.csv: 20260917
- TWSE market index: 20260917
- TPEx market index: 20260917

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20260917 | 46,288 | -1.39% | 3.01% | True | True | correction | high_risk |
| TPEx | 20260917 | 398.17 | -1.74% | 2.11% | False | True | correction | high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -78,674 | TX futures direction anchor |
| foreign_futures_net_oi | -442,274 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 76.5% | hedging background only |
| taiwan_vix | 24.05 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 7,957 | contrarian sentiment proxy only |
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
    latest: 24.05
    percentile_252d: 1.3245
    percentile_504d: 
    rank_label: lower_quartile
    context_label: complacency_low_vol
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 7957.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 61.039
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
- VIX context: complacency_low_vol / vix_context_neutral_observe
- Retail MTX context: retail_normal_range / retail_positioning_normal
- Combined: sentiment_mixed_observe (warning=low)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
