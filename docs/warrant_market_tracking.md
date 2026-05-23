# Warrant Market Tracking

新增全市場權證資料分析與追蹤，不只分析單一股票權證。

## Data files

- `data/warrant_daily/{date}.csv`
- `data/warrant_flow_by_stock/{date}.csv`
- `output/latest/warrant_flow_by_stock_latest.csv`
- `output/latest/warrant_sector_heat_latest.csv`

## Reports

- `output/latest/warrant_market_report_latest.md`
- `output/latest/warrant_market_report_latest.pdf`
- `output/latest/warrant_signal_performance_latest.md`

## Scope

權證資料會從 raw warrant rows 彙總到標的股票層級，並與每日候選分類、TDCC、族群資訊交叉比對。

報告包含：

- 全市場認購/認售總覽
- 認購前 20 名
- 認售前 20 名
- Call/Put 比異常
- 族群權證熱度
- 過熱與反指標風險
- 後續追蹤名單

## Important rule

權證只作輔助訊號，不可單獨作為買進理由。

若官方清單日期已更新，但成交金額或報價資料缺失，報告會明確標示資料不足，不會用舊資料假裝是今天資料。
