# 官方權證每日資料抓取狀態

- 產生時間：`2026-05-25 01:04:27 Asia/Taipei`
- 資料日期：`20260522`
- 輸出檔：`output\latest\warrant_daily_raw_latest.csv`
- 權證對照表筆數：`29764`
- 權證成交行情筆數：`29700`
- 最終可彙總筆數：`29700`
- debug：`output\debug\warrant_fetch_debug_latest.md`

- warning：`requested_date=20260524 had no usable warrant quote rows; used latest available quote_date=20260522.`

## Fetch logs

- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260524&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260524&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260524&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260524&type=0999P&response=csv
- no_usable_quote_rows date=20260524, quote_rows=0; trying previous calendar date
- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=1, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=0999P&response=csv
- no_usable_quote_rows date=20260523, quote_rows=0; trying previous calendar date
- ok source=TWSE_MI_INDEX_0999_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999&response=json
- ok source=TWSE_MI_INDEX_0999_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999&response=csv
- ok source=TWSE_MI_INDEX_0999P_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999P&response=json
- ok source=TWSE_MI_INDEX_0999P_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260522&type=0999P&response=csv
- ok source=TWSE_WARRANT_STOCK_JSON, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260522&response=json
- ok source=TWSE_WARRANT_STOCK_CSV, status=200, tables=2, url=https://www.twse.com.tw/rwd/zh/stock/warrantStock?date=20260522&response=csv