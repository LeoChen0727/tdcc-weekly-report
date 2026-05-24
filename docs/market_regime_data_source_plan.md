# Market Regime / Futures Options Data Source Plan

This module is separate from the daily all-market candidate stock report. Its job is to collect market-background data for Taiwan index futures, options, risk regime, and exposure review.

## Scope

The first version tracks:

- TWSE / TAIEX index
- TPEx / OTC index
- TAIFEX three-institution futures and options positioning
- TAIFEX TXO Put/Call ratio
- TAIFEX Taiwan VIX

It does not generate personal position advice. It is a market-background dashboard.

## Official Sources

### Market Indices

- TWSE index history: `https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK`
- TPEx index history: `https://www.tpex.org.tw/www/zh-tw/indexInfo/inx`

Stored in:

- `data/market_index_history.csv`
- `output/latest/market_benchmark_latest.csv`

### TAIFEX Three-Institution Futures / Options

Official open-data endpoints:

- Futures vs options daily: `MarketDataOfMajorInstitutionalTradersDividedByFuturesAndOptionsBytheDate`
- Futures contracts daily: `MarketDataOfMajorInstitutionalTradersDetailsOfFuturesContractsBytheDate`
- Options call/put daily: `MarketDataOfMajorInstitutionalTradersDetailsOfCallsAndPutsBytheDate`

Stored in:

- `data/futures_options/taifex_institutional_fo_history.csv`
- `data/futures_options/taifex_futures_contracts_history.csv`
- `data/futures_options/taifex_options_call_put_history.csv`

### TXO Put/Call Ratio

Official open-data endpoint:

- `PutCallRatio`

Stored in:

- `data/futures_options/put_call_ratio_history.csv`
- `output/latest/futures_options_put_call_ratio_latest.csv`

### Taiwan VIX

Official TAIFEX monthly text files:

- `https://www.taifex.com.tw/file/taifex/Dailydownload/vix/log2data/YYYYMMnew.txt`

Stored in:

- `data/futures_options/taiwan_vix_history.csv`
- `output/latest/taiwan_vix_latest.csv`

## Outputs

- `output/latest/futures_options_indicators_latest.csv`
- `output/latest/futures_options_source_status_latest.json`
- `output/latest/futures_options_source_status_latest.md`
- `output/latest/market_regime_latest.csv`
- `output/latest/market_risk_dashboard_latest.md`
- `output/latest/market_risk_dashboard_latest.pdf`
- `docs/latest/market_risk_dashboard_latest.pdf`

## Interpretation Rules

Use this dashboard as background only.

- `market_regime` describes index trend state.
- `risk_level` is a conservative risk-control label.
- Taiwan VIX and Put/Call ratio are fear/hedging gauges, not standalone trading signals.
- Three-institution futures/options data are aggregate positioning data, not a single institution's strategy.
- The daily all-market candidate stock report may cite `market_regime` only as background.

## Known Limits

- TAIFEX open-data endpoints generally provide latest daily official data, not a complete paid tick database.
- Taiwan VIX file availability depends on the monthly official text files.
- Retail sentiment is initially approximated by TXO Put/Call ratio and Taiwan VIX. More retail-specific indicators can be added later if a reliable official source is confirmed.
