# 官方權證每日資料抓取狀態

- 產生時間：`2026-08-10 20:48:02 Asia/Taipei`
- 資料日期：`20260807`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`30099`
- 權證成交行情筆數：`30038`
- 最終可彙總筆數：`30038`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- failed source=TWSE_MI_INDEX_0999_JSON, error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=30.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260807&type=0999&response=json
- retry historical warrant family=quote type=0999 source=TWSE_MI_INDEX_0999_JSON attempt=1/3 delay_seconds=1 error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=30.0)
- failed source=TWSE_MI_INDEX_0999_JSON, error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=30.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260807&type=0999&response=json
- retry historical warrant family=quote type=0999 source=TWSE_MI_INDEX_0999_JSON attempt=2/3 delay_seconds=2 error=ReadTimeout: HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=30.0)
- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260807&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260807&type=0999P&response=json
- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260807&response=json