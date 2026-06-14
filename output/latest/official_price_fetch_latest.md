# Official Daily Price Fetch Report

- generated_at: `2026-06-15 03:43:34 Asia/Taipei`
- target_date: `20260615`
- saved_price_date: `20260612`
- is_target_date: `False`
- result: `failed_no_target_data`
- reason: 目標日官方來源與 fallback 都沒有取得任何可用日線資料；latest 保留上一個有效交易日。
- twse_rows: `0`
- tpex_rows: `0`
- total_rows: `0`
- full_market_ok: `False`
- data_quality_note: partial_market_stale_rejected: TPEx matched previous trading day file daily_price_20260612.csv
- stale_markets: `TPEx`
- stale_market_rows: `5037`

## Output Paths

- previous_valid_csv: `data/daily_price/daily_price_20260612.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260615: TWSE=0 / TPEx=0 / Total=0 / full_market_ok=False

## Fetch Logs

- Start official daily price fetch target_date=20260615 max_seconds=480
- ===== Fetch price for date 20260615 =====
- Loaded universe rows=6272
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260615
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260615&type=ALLBUT0999&response=json -> status=200, chars=25
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_RWD_CSV_MI_INDEX date=20260615
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260615&type=ALLBUT0999&response=csv -> status=200, chars=0
- Trying TWSE batch source=TWSE_LEGACY_JSON_MI_INDEX date=20260615
- GET https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20260615&type=ALLBUT0999 -> status=200, chars=25
- TWSE_LEGACY_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_OPENAPI_STOCK_DAY_ALL date=20260615
- GET https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL failed: ConnectTimeout: HTTPSConnectionPool(host='openapi.twse.com.tw', port=443): Max retries exceeded with url: /v1/exchangeReport/STOCK_DAY_ALL (Caused by ConnectTimeoutError(<HTTPSConnection(host='openapi.twse.com.tw', port=443) at 0x7f5e2cd064d0>, 'Connection to openapi.twse.com.tw timed out. (connect timeout=25)'))
- TWSE batch best rows=0
- TWSE batch insufficient rows=0; start individual fallback
- TWSE individual fallback start: stocks=1235 date=20260615 budget_seconds=180
- TWSE individual fallback parsed rows=0
- TWSE kept batch rows=0; fallback rows=0
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260615
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/15&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260615
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/15&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260615
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/15&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260615
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/06/15&s=0,asc,0 -> status=200, chars=1410530
- TPEX_OLD_DAILY_CSV: parsed TPEx CSV rows=5037
- TPEx batch selected source=TPEX_OLD_DAILY_CSV, rows=5037
- date=20260615 twse_rows=0 tpex_rows=5037 total_rows=5037 full_market_ok=False
- Reject stale TPEx target-date rows: 100.0% match previous file daily_price_20260612.csv
- Published previous valid daily price file as latest: data/daily_price/daily_price_20260612.csv