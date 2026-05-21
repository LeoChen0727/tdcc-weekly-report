# 官方權證每日資料抓取狀態

- 產生時間：`2026-05-21 17:27:48 Asia/Taipei`
- 資料日期：`20260520`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 筆數：`59526`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- ok source=TWSE_JSON_RWD, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260520&response=json
- ok source=TWSE_CSV_RWD, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260520&response=csv
- empty_or_unparsed source=TWSE_JSON_OLD, status=200, chars=747, url=https://www.twse.com.tw/exchangeReport/warrantStock?date=20260520&response=json
- empty_or_unparsed source=TWSE_CSV_OLD, status=200, chars=747, url=https://www.twse.com.tw/exchangeReport/warrantStock?date=20260520&response=csv
- ok source=TPEX_DAILYQ_JSON, status=200, tables=1, url=https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date=115/05/20&response=json
- ok source=TPEX_DAILYQ_CSV, status=200, tables=1, url=https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date=115/05/20&response=csv
- ok source=TPEX_LEGACY_HTML, status=200, tables=1, url=https://www.tpex.org.tw/web/stock/aftertrading/warrant_quotes/warrant_quotes_result.php?l=zh-tw&d=115/05/20
- ok source=TPEX_EXTEND, status=200, tables=1, url=https://www.tpex.org.tw/ch/extend/warrant/dailyQ/wntQuts.php?l=zh-tw&d=115/05/20&s=0,asc,0