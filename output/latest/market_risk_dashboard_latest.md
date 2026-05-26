# Market Risk Dashboard

- generated_at: `2026-05-26 22:10:32 Asia/Taipei`
- data_date: `20260526`
- market_regime: `strong_bull`
- risk_level: `elevated_risk`
- risk_score: `3`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260526 |
| futures_contracts | ok | 66 | 20260526 |
| options_call_put | ok | 30 | 20260526 |
| put_call_ratio | ok | 21 | 20260526 |
| taiwan_vix | ok | 71 | 20260526 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 43,525.37 | +8.34% | +9.87% | True | True | strong_bull |
| TPEx | 439.30 | +10.33% | +16.51% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -54,391 | foreign_heavy_net_short |
| Dealer TX futures net OI | +1,993 |  |
| Trust TX futures net OI | +43,336 |  |
| Retail MTX net OI proxy | +13,753 | retail_net_long_watch |
| Foreign TXO call net OI | +3,321 |  |
| Foreign TXO put net OI | +7,043 |  |
| TXO put/call OI ratio | 125.76% | neutral |
| Taiwan VIX | 32.91 | risk_elevated |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=2, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=2, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=14, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=14, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=22, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=30, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=30, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=42, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 43,525.37; 6M range 27,342.53-43,644.40; distance from 6M high -0.27%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 439.30; 6M range 256.14-439.30; distance from 6M high +0.00%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+13,753`
- state: `retail_net_long_watch`
- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.
- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.

## Risk Notes

- TWSE strong bull
- TPEx strong bull
- Taiwan VIX elevated
- Foreign TX futures heavy net short
- Retail MTX proxy net long watch

## Usage Boundary

- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.
- Do not treat a single futures/options indicator as a buy or sell signal.
- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.
