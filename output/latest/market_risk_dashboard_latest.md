# Market Risk Dashboard

- generated_at: `2026-06-02 19:46:49 Asia/Taipei`
- data_date: `20260602`
- market_regime: `strong_bull`
- risk_level: `high_risk`
- risk_score: `4`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260602 |
| futures_contracts | ok | 66 | 20260602 |
| options_call_put | ok | 30 | 20260602 |
| put_call_ratio | ok | 22 | 20260602 |
| taiwan_vix | ok | 64 | 20260602 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 45,557.31 | +4.67% | +11.74% | True | True | strong_bull |
| TPEx | 440.64 | +0.31% | +8.15% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -67,018 | foreign_heavy_net_short |
| Dealer TX futures net OI | +2,564 |  |
| Trust TX futures net OI | +49,765 |  |
| Retail MTX net OI proxy | +14,604 | retail_net_long_watch |
| Foreign TXO call net OI | +3,600 |  |
| Foreign TXO put net OI | +7,454 |  |
| TXO put/call OI ratio | 142.84% | neutral |
| Taiwan VIX | 36.58 | panic_high |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=-5, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=-5, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=7, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=7, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=15, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=23, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=23, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=35, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 45,557.31; 6M range 27,468.53-45,557.31; distance from 6M high +0.00%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 440.64; 6M range 259.13-446.02; distance from 6M high -1.21%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+14,604`
- state: `retail_net_long_watch`
- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.
- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.

## Risk Notes

- TWSE strong bull
- TPEx strong bull
- Taiwan VIX panic-high
- Foreign TX futures heavy net short
- Retail MTX proxy net long watch

## Usage Boundary

- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.
- Do not treat a single futures/options indicator as a buy or sell signal.
- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `36.58`
- 252D high / low / percentile: `41.5` / `25.68` / `71.05%`
- 504D percentile: `-`
- z-score: `0.7`
- vix_return_5d / 10d / 20d: `11.15%` / `-7.42%` / `-0.41%`
- TWSE / TPEx position: TWSE dist 60D high `0%`, TPEx dist 60D high `-1.21%`
- vix_index_interpretation: `trend_supported_no_extreme_vix`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `14,604`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low / percentile: `-` / `-` / `-`
- 504D percentile: `-`
- retail_mtx_index_interpretation: `insufficient_history_observe_only`

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `insufficient_history_observe_only`
- sentiment_warning_level: `insufficient`
- data_quality_note: 資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。

Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
