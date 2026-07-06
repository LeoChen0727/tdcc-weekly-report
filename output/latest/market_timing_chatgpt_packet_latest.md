# MARKET TIMING CHATGPT PACKET

## Metadata
- generated_at: 2026-07-06 20:33:26 Asia/Taipei
- main_price_date: 20260706
- packet_source: daily_market_regime_dashboard
- packet_status: ready
- packet_status_note: all source rows aligned with main_price_date
- tuning_status: not_ready

## Source Dates
- market_regime_latest.csv: 20260706
- futures_options_indicators_latest.csv: 20260706
- TWSE market index: 20260706
- TPEx market index: 20260706

## Current Market Technical State
| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| TWSE | 20260706 | 46,556 | 3.46% | 3.3% | True | True | mild_bull | high_risk |
| TPEx | 20260706 | 439.8 | 6.51% | 2.03% | True | True | mild_bull | high_risk |

## Futures Options Context
| item | value | note |
| --- | ---: | --- |
| foreign_tx_futures_net_oi | -80,087 | TX futures direction anchor |
| foreign_futures_net_oi | -594,361 | broad futures exposure only, not TX direction |
| put_call_oi_ratio_pct | 122.22% | hedging background only |
| taiwan_vix | 36.89 | volatility / hedging context only |
| retail_mtx_net_oi_proxy | 5,173 | contrarian sentiment proxy only |
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
    latest: 36.89
    percentile_252d: 63.6364
    percentile_504d: 
    rank_label: middle_range
    context_label: normal_range
    index_interpretation: trend_supported_no_extreme_vix
  retail_mtx:
    latest_proxy: 5173.0
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
- VIX context: normal_range / trend_supported_no_extreme_vix
- Retail MTX context: insufficient_history / insufficient_history_observe_only
- Combined: insufficient_history_observe_only (warning=insufficient)
- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
