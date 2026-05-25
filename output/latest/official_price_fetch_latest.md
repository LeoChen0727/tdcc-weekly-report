# 官方每日價格資料抓取狀態

- 產生時間：`2026-05-26 06:25:22 Asia/Taipei`
- target_date：`20260526`
- saved_price_date：`20260526`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1237`
- tpex_rows：`5943`
- total_rows：`7180`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260526.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260526.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260526: TWSE=1237 / TPEx=5943 / Total=7180 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260526
- ===== Fetch price for date 20260526 =====
- Loaded universe rows=7180
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260526
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260526&type=ALLBUT0999&response=json -> status=200, chars=25
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_RWD_CSV_MI_INDEX date=20260526
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260526&type=ALLBUT0999&response=csv -> status=200, chars=0
- Trying TWSE batch source=TWSE_LEGACY_JSON_MI_INDEX date=20260526
- GET https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20260526&type=ALLBUT0999 -> status=200, chars=25
- TWSE_LEGACY_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_OPENAPI_STOCK_DAY_ALL date=20260526
- GET https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL -> status=200, chars=308033
- TWSE_OPENAPI_STOCK_DAY_ALL: parsed TWSE OpenAPI rows=1237
- TWSE batch selected source=TWSE_OPENAPI_STOCK_DAY_ALL, rows=1237
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260526
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/26&type=EW&response=json -> status=520, chars=959
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260526
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/26&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260526
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/05/26&s=0,asc,0 -> status=200, chars=1470601
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5943
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5943
- date=20260526 twse_rows=1237 tpex_rows=5943 total_rows=7180 full_market_ok=True