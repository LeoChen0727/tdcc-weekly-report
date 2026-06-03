# 官方每日價格資料抓取狀態

- 產生時間：`2026-06-03 23:09:22 Asia/Taipei`
- target_date：`20260603`
- saved_price_date：`20260603`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1239`
- tpex_rows：`5585`
- total_rows：`6824`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260603.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260603.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260603: TWSE=1239 / TPEx=5585 / Total=6824 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260603
- ===== Fetch price for date 20260603 =====
- Loaded universe rows=6825
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260603
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260603&type=ALLBUT0999&response=json -> status=200, chars=232531
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1239
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1239
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260603
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/03&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260603
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/03&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260603
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/03&s=0,asc,0 -> status=200, chars=1469207
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5585
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5585
- date=20260603 twse_rows=1239 tpex_rows=5585 total_rows=6824 full_market_ok=True