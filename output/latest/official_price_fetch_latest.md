# 官方每日價格資料抓取狀態

- 產生時間：`2026-05-28 19:07:30 Asia/Taipei`
- target_date：`20260528`
- saved_price_date：`20260528`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1239`
- tpex_rows：`5742`
- total_rows：`6981`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260528.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260528.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260528: TWSE=1239 / TPEx=5742 / Total=6981 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260528
- ===== Fetch price for date 20260528 =====
- Loaded universe rows=6961
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260528
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260528&type=ALLBUT0999&response=json -> status=200, chars=232575
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1239
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1239
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260528
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/28&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260528
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/28&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260528
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/05/28&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260528
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/05/28&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES date=20260528
- GET https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes -> status=200, chars=4020346
- TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES: parsed TPEx JSON rows=5742
- TPEx batch selected source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES, rows=5742
- date=20260528 twse_rows=1239 tpex_rows=5742 total_rows=6981 full_market_ok=True