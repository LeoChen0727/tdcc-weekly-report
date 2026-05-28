# Market Risk Dashboard

- generated_at: `2026-05-28 20:06:19 Asia/Taipei`
- data_date: `20260528`
- market_regime: `strong_bull`
- risk_level: `high_risk`
- risk_score: `4`
- futures_options_source_status: `ready`

## Data Status

This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260528 |
| futures_contracts | ok | 66 | 20260528 |
| options_call_put | ok | 30 | 20260528 |
| put_call_ratio | ok | 22 | 20260528 |
| taiwan_vix | ok | 73 | 20260528 |

## Market Index Regime

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 43,636.44 | +5.48% | +11.02% | True | True | strong_bull |
| TPEx | 432.48 | +5.53% | +12.99% | True | True | strong_bull |

## Futures / Options Positioning

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -58,196 | foreign_heavy_net_short |
| Dealer TX futures net OI | +3,884 |  |
| Trust TX futures net OI | +44,767 |  |
| Retail MTX net OI proxy | +10,776 | retail_net_long_watch |
| Foreign TXO call net OI | +1,554 |  |
| Foreign TXO put net OI | +6,343 |  |
| TXO put/call OI ratio | 127.81% | neutral |
| Taiwan VIX | 36.28 | panic_high |

## Upcoming Macro Event Calendar

- 20260528 US_GDP: GDP (Second Estimate) and Corporate Profits, 1st Quarter 2026 (days=0, importance=medium)
- 20260528 US_PCE_personal_income: Personal Income and Outlays, April 2026 (days=0, importance=high)
- 20260609 US_trade: U.S. International Trade in Goods and Services, Annual Update (days=12, importance=medium)
- 20260609 US_trade: U.S. International Trade in Goods and Services, April 2026 (days=12, importance=medium)
- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=20, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=28, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=28, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=40, importance=medium)

## Six-Month Technical Charts

The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## Technical / Pattern Notes

- TWSE / TAIEX: strong_bull; close 43,636.44; 6M range 27,342.53-44,256.80; distance from 6M high -1.40%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 432.48; 6M range 259.13-440.19; distance from 6M high -1.75%; above MA20=True, above MA60=True.

## Retail Mini-TAIEX Futures Proxy

- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.
- latest_proxy_value: `+10,776`
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
