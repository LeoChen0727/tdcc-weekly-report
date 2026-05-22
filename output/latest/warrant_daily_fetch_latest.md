# 官方權證每日資料抓取狀態

- 產生時間：`2026-05-22 23:43:46 Asia/Taipei`
- 資料日期：`20260522`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`29764`
- 權證成交行情筆數：`29785`
- 最終可彙總筆數：`29764`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260522&response=json
- ok source=TWSE_WARRANT_STOCK_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260522&response=csv
- ok source=TWSE_MI_INDEX_ALL_JSON, status=200, tables=10, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=ALL&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_ALL_CSV, status=200, chars=3447907, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=ALL&response=csv
- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999P&response=csv
- ok source=TWSE_MI_INDEX_0999C_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999C&response=json
- ok source=TWSE_MI_INDEX_0999C_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999C&response=csv
- ok source=TWSE_MI_INDEX_0999B_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999B&response=json
- ok source=TWSE_MI_INDEX_0999B_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999B&response=csv