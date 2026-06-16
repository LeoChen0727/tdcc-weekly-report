# Market Regime / Futures Options Data Source Plan

This module is separate from the daily all-market candidate stock report. Its job is to collect market-background data for Taiwan index futures, options, risk regime, and exposure review.

## Scope

The first version tracks:

- TWSE / TAIEX index
- TPEx / OTC index
- TAIFEX three-institution futures and options positioning
- Mini-TAIEX non-three-institution net open interest proxy
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

### Retail Mini-TAIEX Futures Proxy

TAIFEX does not publish a direct "retail account" MTX net-position field in the current repo source. The dashboard therefore derives a contrarian proxy from the official three-institution mini-TAIEX futures data:

`retail_mtx_net_oi_proxy = -1 * (dealer_mtx_net_oi + trust_mtx_net_oi + foreign_mtx_net_oi)`

This is best read as non-three-institution MTX net positioning. It may include retail and other non-three-institution participants, so reports must call it a proxy rather than an official retail count.

Stored in:

- `output/latest/futures_options_indicators_latest.csv`
- `output/latest/market_regime_latest.csv`
- `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

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

The PDF is an internal source/reference artifact. Daily production must not
publish `market_risk_dashboard_latest.pdf` under `docs/latest` as a daily
recommendation PDF.

## Interpretation Rules

Use this dashboard as background only.

- `market_regime` describes index trend state.
- `risk_level` is a conservative risk-control label.
- Taiwan VIX and Put/Call ratio are fear/hedging gauges, not standalone trading signals.
- Three-institution futures/options data are aggregate positioning data, not a single institution's strategy.
- `retail_mtx_net_oi_proxy` is a contrarian sentiment gauge. Positive and crowded readings mean non-three-institution MTX accounts are net long and should raise caution; negative and extreme readings may support a contrarian risk-on backdrop, but still require index trend confirmation.
- The daily all-market candidate stock report may cite `market_regime` only as background.

## Known Limits

- TAIFEX open-data endpoints generally provide latest daily official data, not a complete paid tick database.
- Taiwan VIX file availability depends on the monthly official text files.
- The retail MTX field is a proxy derived from official three-institution MTX net open interest. It is not an official account-level retail disclosure.
