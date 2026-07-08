# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-07-08 20:01:23 Asia/Taipei
- main_price_date: 20260708
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20260708
- futures_options_indicators_latest.csv: 20260708
- TWSE market index: 20260708
- TPEx market index: 20260708

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20260708 | 45,734 | -2.73% | 2.3% | False | True | correction | very_high_risk |
| TPEx | 20260708 | 421.39 | -2.28% | -0.78% | False | True | correction | very_high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -81,268 | TX futures direction anchor |
| foreign_futures_net_oi | -565,577 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 129.81% | hedging background only |
| taiwan_vix | 38.13 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 8,953 | contrarian sentiment proxy only |
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
    latest: 38.13
    percentile_252d: 74.2574
    percentile_504d: 
    rank_label: middle_range
    context_label: normal_range
    index_interpretation: vix_context_neutral_observe
  retail_mtx:
    latest_proxy: 8953.0
    proxy_method: negative_sum_of_three_institution_mtx_net_oi
    percentile_252d: 
    percentile_504d: 
    rank_label: insufficient_history
    context_label: insufficient_history
    index_interpretation: insufficient_history_observe_only
  combined:
    combined_sentiment_interpretation: insufficient_history_observe_only
    sentiment_warning_level: insufficient
    sample_status: insufficient_history
    data_quality_note: 資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。

ChatGPT-friendly summary:
- VIX context: normal_range / vix_context_neutral_observe
- Retail MTX context: insufficient_history / insufficient_history_observe_only
- Combined: insufficient_history_observe_only (warning=insufficient)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
