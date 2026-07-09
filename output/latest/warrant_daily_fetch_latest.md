# 官方權證每日資料抓取狀態

- 產生時間：`2026-07-10 01:33:11 Asia/Taipei`
- 資料日期：`20260709`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`29214`
- 權證成交行情筆數：`29153`
- 最終可彙總筆數：`29153`
- debug：`output/debug/warrant_fetch_debug_latest.md`

## Fetch logs

- empty_or_unparsed source=TWSE_MI_INDEX_0999_JSON, status=403, chars=360, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999&response=csv
- empty_or_unparsed source=TWSE_MI_INDEX_0999P_JSON, status=403, chars=360, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260709&type=0999P&response=csv
- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260709&response=json
- empty_or_unparsed source=TWSE_WARRANT_STOCK_CSV, status=403, chars=360, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260709&response=csv