# Official Daily Price Fetch Report

- generated_at: `2026-06-12 13:46:29 Asia/Taipei`
- target_date: `20260612`
- saved_price_date: `20260611`
- is_target_date: `False`
- result: `failed_no_target_data`
- reason: 目標日官方來源與 fallback 都沒有取得任何可用日線資料；latest 保留上一個有效交易日。
- twse_rows: `1085`
- tpex_rows: `0`
- total_rows: `1085`
- full_market_ok: `False`
- data_quality_note: partial_market_stale_rejected: TPEx matched previous trading day file daily_price_20260611.csv
- stale_markets: `TPEx`
- stale_market_rows: `4809`

## Output Paths

- previous_valid_csv: `data/daily_price/daily_price_20260611.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260612: TWSE=1085 / TPEx=0 / Total=1085 / full_market_ok=False

## Fetch Logs

- Start official daily price fetch target_date=20260612 max_seconds=480
- ===== Fetch price for date 20260612 =====
- Loaded universe rows=6046
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260612
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260612&type=ALLBUT0999&response=json -> status=200, chars=25
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=0
- Trying TWSE batch source=TWSE_RWD_CSV_MI_INDEX date=20260612
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260612&type=ALLBUT0999&response=csv -> status=200, chars=178478
- TWSE_RWD_CSV_MI_INDEX: parsed TWSE CSV rows=1085
- TWSE batch selected source=TWSE_RWD_CSV_MI_INDEX, rows=1085
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260612
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/12&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260612
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/12&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260612
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/12&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260612
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/06/12&s=0,asc,0 -> status=200, chars=1422210
- TPEX_OLD_DAILY_CSV: parsed TPEx CSV rows=4809
- TPEx batch selected source=TPEX_OLD_DAILY_CSV, rows=4809
- date=20260612 twse_rows=1085 tpex_rows=4809 total_rows=5894 full_market_ok=True
- Reject stale TPEx target-date rows: 100.0% match previous file daily_price_20260611.csv
- Published previous valid daily price file as latest: data/daily_price/daily_price_20260611.csv