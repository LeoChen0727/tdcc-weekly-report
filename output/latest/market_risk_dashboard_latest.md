# Market Risk Dashboard

- generated_at: `2026-06-01 22:24:58 Asia/Taipei`
- data_date: `20260601`
- market_regime: `strong_bull`
- risk_level: `high_risk`
- risk_score: `5`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260601 |
| futures_contracts | ok | 66 | 20260601 |
| options_call_put | ok | 30 | 20260601 |
| put_call_ratio | ok | 21 | 20260601 |
| taiwan_vix | ok | 63 | 20260601 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 45,337.91 | +3.88% | +11.38% | True | True | strong_bull |
| TPEx | 446.02 | +2.54% | +11.99% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -64,673 | foreign_heavy_net_short |
| Dealer TX futures net OI | +2,456 |  |
| Trust TX futures net OI | +48,419 |  |
| Retail MTX net OI proxy | +12,784 | retail_net_long_watch |
| Foreign TXO call net OI | +3,596 |  |
| Foreign TXO put net OI | +6,817 |  |
| TXO put/call OI ratio | 171.12% | put_hedge_elevated |
| Taiwan VIX | 36.52 | panic_high |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=-4, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=-4, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=8, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=8, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=16, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=24, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=24, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=36, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 45,337.91; 6M range 27,342.53-45,337.91; distance from 6M high +0.00%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 446.02; 6M range 259.13-446.02; distance from 6M high +0.00%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+12,784`
- state: `retail_net_long_watch`
- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.
- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.

## Risk Notes

- TWSE strong bull
- TPEx strong bull
- Taiwan VIX panic-high
- TXO put/call OI hedge elevated
- Foreign TX futures heavy net short
- Retail MTX proxy net long watch

## Usage Boundary

- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.
- Do not treat a single futures/options indicator as a buy or sell signal.
- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.
