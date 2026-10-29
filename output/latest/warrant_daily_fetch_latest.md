# 官方權證每日資料抓取狀態

- 產生時間：`2026-10-29 19:39:26 Asia/Taipei`
- 資料日期：`20261029`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`38616`
- 權證成交行情筆數：`38556`
- 最終可彙總筆數：`38556`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- failed source=TWSE_MI_INDEX_0999_JSON, error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261029&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261029&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261029&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261029&type=0999P&response=csv
- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20261029&response=json
- ok source=TWSE_WARRANT_STOCK_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20261029&response=csv