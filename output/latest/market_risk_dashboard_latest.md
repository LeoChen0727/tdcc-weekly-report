# Market Risk Dashboard

- generated_at: `2026-06-03 22:53:47 Asia/Taipei`
- data_date: `20260603`
- market_regime: `strong_bull`
- risk_level: `high_risk`
- risk_score: `5`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260603 |
| futures_contracts | ok | 66 | 20260603 |
| options_call_put | ok | 30 | 20260603 |
| put_call_ratio | ok | 23 | 20260603 |
| taiwan_vix | ok | 65 | 20260603 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 46,459.16 | +4.98% | +12.93% | True | True | strong_bull |
| TPEx | 446.82 | +1.51% | +8.90% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -66,772 | foreign_heavy_net_short |
| Dealer TX futures net OI | +2,474 |  |
| Trust TX futures net OI | +51,304 |  |
| Retail MTX net OI proxy | +11,026 | retail_net_long_watch |
| Foreign TXO call net OI | +2,667 |  |
| Foreign TXO put net OI | +7,029 |  |
| TXO put/call OI ratio | 217.69% | heavy_put_hedge |
| Taiwan VIX | 34.94 | risk_elevated |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=-6, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=-6, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=6, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=6, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=14, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=22, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=22, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=34, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 46,459.16; 6M range 27,468.53-46,459.16; distance from 6M high +0.00%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 446.82; 6M range 259.39-446.82; distance from 6M high +0.00%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+11,026`
- state: `retail_net_long_watch`
- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.
- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.

## Risk Notes

- TWSE strong bull
- TPEx strong bull
- Taiwan VIX elevated
- TXO put/call OI hedge high
- Foreign TX futures heavy net short
- Retail MTX proxy net long watch

## Usage Boundary

- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.
- Do not treat a single futures/options indicator as a buy or sell signal.
- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `34.94`
- 252D high / low / percentile: `41.5` / `25.68` / `53.25%`
- 504D percentile: `-`
- z-score: `0.29`
- vix_return_5d / 10d / 20d: `1.25%` / `-5.34%` / `-8.8%`
- TWSE / TPEx position: TWSE dist 60D high `0%`, TPEx dist 60D high `0%`
- vix_index_interpretation: `trend_supported_no_extreme_vix`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `11,026`
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
