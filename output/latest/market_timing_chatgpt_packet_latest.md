# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-08-28 21:01:13 Asia/Taipei
- main_price_date: 20260828
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20260828
- futures_options_indicators_latest.csv: 20260828
- TWSE market index: 20260828
- TPEx market index: 20260828

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20260828 | 46,331 | 2.45% | 7.45% | True | True | range_bound | elevated_risk |
| TPEx | 20260828 | 402.83 | 4.02% | 15.81% | True | False | range_bound | elevated_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -83,655 | TX futures direction anchor |
| foreign_futures_net_oi | -470,011 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 101.44% | hedging background only |
| taiwan_vix | 25 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 2,630 | contrarian sentiment proxy only |
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
    latest: 25.0
    percentile_252d: 0.7299
    percentile_504d: 
    rank_label: lower_quartile
    context_label: complacency_low_vol
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 2630.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 6.1538
    percentile_504d: 
    rank_label: bottom_decile
    context_label: retail_extreme_short
    index_interpretation: retail_positioning_observe
  combined:
    combined_sentiment_interpretation: sentiment_mixed_observe
    sentiment_warning_level: low
    sample_status: short_history
    data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

ChatGPT-friendly summary:
- VIX context: complacency_low_vol / vix_context_neutral_observe
- Retail MTX context: retail_extreme_short / retail_positioning_observe
- Combined: sentiment_mixed_observe (warning=low)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
