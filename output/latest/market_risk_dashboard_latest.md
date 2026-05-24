# Market Risk Dashboard

- generated_at: `2026-05-24 11:38:57 Asia/Taipei`
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
| Foreign TXO call net OI | +1,901 |  |
| Foreign TXO put net OI | +3,893 |  |
| TXO put/call OI ratio | 156.25% | put_hedge_elevated |
| Taiwan VIX | 33.09 | risk_elevated |

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
