# Official Daily Price Fetch Report

- generated_at: `2026-06-18 19:34:38 Asia/Taipei`
- target_date: `20260618`
- saved_price_date: `20260618`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1237`
- tpex_rows: `5314`
- total_rows: `6551`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260618.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260618.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260618: TWSE=1237 / TPEx=5314 / Total=6551 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260618 max_seconds=480
- ===== Fetch price for date 20260618 =====
- Loaded universe rows=6551
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260618
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260618&type=ALLBUT0999&response=json -> status=200, chars=231312
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1237
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1237
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260618
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/18&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260618
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/18&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260618
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/18&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260618
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/06/18&s=0,asc,0 -> status=200, chars=1408708
- TPEX_OLD_DAILY_CSV: parsed TPEx CSV rows=5314
- TPEx batch selected source=TPEX_OLD_DAILY_CSV, rows=5314
- date=20260618 twse_rows=1237 tpex_rows=5314 total_rows=6551 full_market_ok=True