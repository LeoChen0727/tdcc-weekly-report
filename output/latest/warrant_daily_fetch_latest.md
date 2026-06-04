# 官方權證每日資料抓取狀態

- 產生時間：`2026-06-04 22:39:24 Asia/Taipei`
- 資料日期：`20260604`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`0`
- 權證成交行情筆數：`29780`
- 最終可彙總筆數：`0`
- debug：`output/debug/warrant_fetch_debug_latest.md`

- warning：`權證資料未能產出股票層級可彙總資料。若 mapping_rows > 0 但 quote_rows = 0，代表 MI_INDEX 沒抓到權證成交行情；若 quote_rows > 0 但 final_rows = 0，代表成交行情與權證對照表無法用權證代號合併。`

## Fetch logs

- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260604&type=0999&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_0999_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260604&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260604&type=0999P&response=json
- empty_or_unparsed source=TWSE_MI_INDEX_0999P_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260604&type=0999P&response=csv
- empty_or_unparsed source=TWSE_WARRANT_STOCK_JSON, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260604&response=json
- empty_or_unparsed source=TWSE_WARRANT_STOCK_CSV, status=307, chars=686, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260604&response=csv