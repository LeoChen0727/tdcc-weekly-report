# 官方每日價格資料抓取狀態

- 產生時間：`2026-05-23 00:35:19 Asia/Taipei`
- target_date：`20260523`
- saved_price_date：`20260523`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1233`
- tpex_rows：`5684`
- total_rows：`6917`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260523.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260523.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260523: TWSE=1233 / TPEx=5684 / Total=6917 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260523
- ===== Fetch price for date 20260523 =====
- Loaded universe rows=6917
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260523
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=ALLBUT0999&response=json -> status=200, chars=25
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_RWD_CSV_MI_INDEX date=20260523
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260523&type=ALLBUT0999&response=csv -> status=200, chars=0
- Trying TWSE batch source=TWSE_LEGACY_JSON_MI_INDEX date=20260523
- GET https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20260523&type=ALLBUT0999 -> status=200, chars=25
- TWSE_LEGACY_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_OPENAPI_STOCK_DAY_ALL date=20260523
- GET https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL -> status=200, chars=306596
- TWSE_OPENAPI_STOCK_DAY_ALL: parsed TWSE OpenAPI rows=1233
- TWSE batch selected source=TWSE_OPENAPI_STOCK_DAY_ALL, rows=1233
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260523
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/23&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260523
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/23&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260523
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/05/23&s=0,asc,0 -> status=200, chars=1458501
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5684
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5684
- date=20260523 twse_rows=1233 tpex_rows=5684 total_rows=6917 full_market_ok=True