# 官方權證每日資料抓取狀態

- 產生時間：`2026-06-30 12:00:30 Asia/Taipei`
- 資料日期：`20260629`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`0`
- 權證成交行情筆數：`26566`
- 最終可彙總筆數：`26566`
- debug：`output/debug/warrant_fetch_debug_latest.md`

- warning：`official warrant fetch produced no usable stock-level rows; preserved existing same-date raw snapshot from output/latest/warrant_daily_raw_latest.csv.`

## Fetch logs

- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260629&type=0999&response=json
- failed source=TWSE_MI_INDEX_0999_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260629&type=0999&response=csv
- failed source=TWSE_MI_INDEX_0999P_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260629&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260629&type=0999P&response=csv
- failed source=TWSE_WARRANT_STOCK_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260629&response=json
- failed source=TWSE_WARRANT_STOCK_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260629&response=csv
- official_fetch_empty_preserved_existing_raw source=output/latest/warrant_daily_raw_latest.csv date=20260629 rows=26566