# Official Daily Price Fetch Report

- generated_at: `2026-06-15 23:00:40 Asia/Taipei`
- target_date: `20260615`
- saved_price_date: `20260615`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1236`
- tpex_rows: `5143`
- total_rows: `6379`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260615.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260615.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260615: TWSE=1236 / TPEx=5143 / Total=6379 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260615 max_seconds=480
- ===== Fetch price for date 20260615 =====
- Loaded universe rows=6379
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260615
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260615&type=ALLBUT0999&response=json -> status=200, chars=231103
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1236
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1236
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260615
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/15&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260615
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/15&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260615
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/15&s=0,asc,0 -> status=200, chars=1426584
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5143
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5143
- date=20260615 twse_rows=1236 tpex_rows=5143 total_rows=6379 full_market_ok=True