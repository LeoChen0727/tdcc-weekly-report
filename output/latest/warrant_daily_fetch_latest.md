# 官方權證每日資料抓取狀態

- 產生時間：`2026-07-10 19:29:46 Asia/Taipei`
- 資料日期：`20260709`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`29214`
- 權證成交行情筆數：`0`
- 最終可彙總筆數：`29153`
- debug：`output/debug/warrant_fetch_debug_latest.md`

- warning：`official warrant fetch produced no usable stock-level rows; preserved existing same-date raw snapshot from output/latest/warrant_daily_raw_latest.csv.`

## Fetch logs

- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_0999_CSV, status=200, chars=0, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999&response=csv
- empty_or_unparsed source=TWSE_MI_INDEX_0999P_JSON, status=200, chars=32, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999P&response=csv
- no_usable_quote_rows date=20260709, quote_rows=0; trying previous calendar date
- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260709&response=json
- empty_or_unparsed source=TWSE_WARRANT_STOCK_CSV, status=200, chars=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260709&response=csv
- official_fetch_empty_preserved_existing_raw source=output/latest/warrant_daily_raw_latest.csv date=20260709 rows=29153