# Market Risk Dashboard

- generated_at: `2026-05-25 01:00:46 Asia/Taipei`
- data_date: `20260522`
- market_regime: `strong_bull`
- risk_level: `elevated_risk`
- risk_score: `3`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260522 |
| futures_contracts | ok | 66 | 20260522 |
| options_call_put | ok | 30 | 20260522 |
| put_call_ratio | ok | 22 | 20260522 |
| taiwan_vix | ok | 69 | 20260522 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 42,267.97 | +2.66% | +12.07% | True | True | strong_bull |
| TPEx | 423.25 | +2.94% | +11.00% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -46,483 | foreign_heavy_net_short |
| Dealer TX futures net OI | +929 |  |
| Trust TX futures net OI | +42,047 |  |
| Retail MTX net OI proxy | +4,129 | neutral |
| Foreign TXO call net OI | +1,901 |  |
| Foreign TXO put net OI | +3,893 |  |
| TXO put/call OI ratio | 156.25% | put_hedge_elevated |
| Taiwan VIX | 33.09 | risk_elevated |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=4, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=4, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=16, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=16, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=24, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=32, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=32, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=44, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Important limitation: the current repo stores TWSE/TPEx index close, MA20, MA60, and return history, but not a complete index OHLC/volume raw table. Therefore this dashboard labels the index chart as a close/MA technical chart, not a candlestick K-line chart. After index_ohlc_history.csv is added, the next version should draw standard index K-line charts.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 42,267.97; 6M range 26,504.24-42,267.97; distance from 6M high +0.00%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 423.25; 6M range 250.34-426.57; distance from 6M high -0.78%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+4,129`
- state: `neutral`
- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.
- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.

## Risk Notes

- TWSE strong bull
- TPEx strong bull
- Taiwan VIX elevated
- TXO put/call OI hedge elevated
- Foreign TX futures heavy net short

## Usage Boundary

- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.
- Do not treat a single futures/options indicator as a buy or sell signal.
- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.
