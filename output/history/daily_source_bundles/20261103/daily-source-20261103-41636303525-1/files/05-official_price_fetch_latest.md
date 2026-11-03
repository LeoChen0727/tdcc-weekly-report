# Official Daily Price Fetch Report

- generated_at: `2026-11-03 19:32:16 Asia/Taipei`
- target_date: `20261103`
- saved_price_date: `20261103`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1246`
- tpex_rows: `892`
- total_rows: `2138`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261103.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261103.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261103: TWSE=1246 / TPEx=892 / Total=2138 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261103 max_seconds=480
- ===== Fetch price for date 20261103 =====
- Loaded universe rows=2128
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261103
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261103&type=ALLBUT0999&response=json -> status=200, chars=236883
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1246
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1246
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261103
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/03&type=EW&response=json -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261103
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/03&type=EW&response=csv -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261103
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/11/03&se=EW -> status=200, chars=141243
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=892
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=892
- Applied canonical stock names from metadata snapshot changed_rows=13
- date=20261103 twse_rows=1246 tpex_rows=892 total_rows=2138 full_market_ok=True
