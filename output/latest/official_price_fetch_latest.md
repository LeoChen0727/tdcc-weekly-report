# Official Daily Price Fetch Report

- generated_at: `2026-07-12 16:40:29 Asia/Taipei`
- target_date: `20260712`
- saved_price_date: `20260709`
- is_target_date: `False`
- result: `failed_no_target_data`
- reason: 目標日官方來源與 fallback 都沒有取得任何可用日線資料；latest 保留上一個有效交易日。
- twse_rows: `0`
- tpex_rows: `0`
- total_rows: `0`
- full_market_ok: `False`
- data_quality_note: partial_market_stale_rejected: TWSE matched previous trading day file daily_price_20260709.csv
- stale_markets: `TWSE`
- stale_market_rows: `1240`

## Output Paths

- previous_valid_csv: `data/daily_price/daily_price_20260709.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260712: TWSE=0 / TPEx=0 / Total=0 / full_market_ok=False

## Fetch Logs

- Start official daily price fetch target_date=20260712 max_seconds=480
- ===== Fetch price for date 20260712 =====
- Loaded universe rows=2132
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260712
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260712&type=ALLBUT0999&response=json -> status=200, chars=45
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_RWD_CSV_MI_INDEX date=20260712
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260712&type=ALLBUT0999&response=csv -> status=200, chars=0
- Trying TWSE batch source=TWSE_LEGACY_JSON_MI_INDEX date=20260712
- GET https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20260712&type=ALLBUT0999 -> status=200, chars=45
- TWSE_LEGACY_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_OPENAPI_STOCK_DAY_ALL date=20260712
- GET https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL -> status=200, chars=308855
- TWSE_OPENAPI_STOCK_DAY_ALL: parsed TWSE OpenAPI rows=1240
- TWSE batch selected source=TWSE_OPENAPI_STOCK_DAY_ALL, rows=1240
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260712
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/12&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260712
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/12&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260712
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/07/12&se=EW -> status=200, chars=393
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_CSV date=20260712
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=csv&d=115/07/12&se=EW -> status=200, chars=219
- TPEX_OTC_QUOTES_NO1430_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260712
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/07/12&s=0,asc,0 -> status=200, chars=1413463
- TPEX_OLD_DAILY_JSON: rejected response dates ['20260709']; target date is 20260712
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260712
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/07/12&s=0,asc,0 -> status=200, chars=1402838
- TPEX_OLD_DAILY_CSV: rejected response date 20260709; target date is 20260712
- Trying TPEx batch source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES date=20260712
- GET https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes -> status=200, chars=3845953
- TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES: rejected response dates ['20260709']; target date is 20260712
- TPEx batch best rows=0
- date=20260712 twse_rows=1240 tpex_rows=0 total_rows=1240 full_market_ok=False
- Reject stale TWSE target-date rows: 100.0% match previous file daily_price_20260709.csv
- Published previous valid daily price file as latest: data/daily_price/daily_price_20260709.csv