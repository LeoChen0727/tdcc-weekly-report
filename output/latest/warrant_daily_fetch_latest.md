# 官方權證每日資料抓取狀態

- 產生時間：`2026-06-16 19:38:11 Asia/Taipei`
- 資料日期：`20260616`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`29269`
- 權證成交行情筆數：`29208`
- 最終可彙總筆數：`29208`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260616&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260616&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260616&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260616&type=0999P&response=csv
- empty_or_unparsed source=TWSE_WARRANT_STOCK_JSON, status=200, chars=31, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260616&response=json
- ok source=TWSE_WARRANT_STOCK_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260616&response=csv