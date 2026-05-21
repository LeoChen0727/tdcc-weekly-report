# 官方權證每日資料抓取狀態

- 產生時間：`2026-05-21 17:18:25 Asia/Taipei`
- 資料日期：`20260520`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 筆數：`0`

- warning：`官方權證資料抓取失敗或格式無法解析，已輸出空檔避免 workflow 失敗。`

## Fetch logs

- ok: https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260520&response=csv
- empty_or_unparsed: https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date=115/05/20&response=csv, status=200
- empty_or_unparsed: https://www.tpex.org.tw/web/stock/aftertrading/warrant_quotes/warrant_quotes_result.php?l=zh-tw&d=115/05/20, status=200
- ok: https://www.tpex.org.tw/ch/extend/warrant/dailyQ/wntQuts.php?l=zh-tw&d=115/05/20&s=0,asc,0