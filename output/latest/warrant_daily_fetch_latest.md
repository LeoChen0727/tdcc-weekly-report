# 官方權證每日資料抓取狀態

- 產生時間：`2026-06-18 00:32:01 Asia/Taipei`
- 資料日期：`20260617`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`0`
- 權證成交行情筆數：`2416`
- 最終可彙總筆數：`2416`
- debug：`output/debug/warrant_fetch_debug_latest.md`

- warning：`official warrant fetch produced no usable stock-level rows; preserved existing same-date raw snapshot from output/latest/warrant_daily_raw_latest.csv.`

## Fetch logs

- empty_or_unparsed source=TWSE_MI_INDEX_0999_JSON, status=200, chars=32, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260617&type=0999&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_0999_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260617&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260617&type=0999P&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_0999P_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260617&type=0999P&response=csv
- empty_or_unparsed source=TWSE_WARRANT_STOCK_JSON, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260617&response=json
- empty_or_unparsed source=TWSE_WARRANT_STOCK_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260617&response=csv
- official_fetch_empty_preserved_existing_raw source=output/latest/warrant_daily_raw_latest.csv date=20260617 rows=2416