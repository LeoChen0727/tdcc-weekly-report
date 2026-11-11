# Official Daily Price Fetch Report

- generated_at: `2026-11-11 19:33:37 Asia/Taipei`
- target_date: `20261111`
- saved_price_date: `20261111`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1251`
- tpex_rows: `890`
- total_rows: `2141`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261111.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261111.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261111: TWSE=1251 / TPEx=890 / Total=2141 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261111 max_seconds=480
- ===== Fetch price for date 20261111 =====
- Loaded universe rows=2137
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261111
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261111&type=ALLBUT0999&response=json -> status=200, chars=232719
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1251
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1251
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261111
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/11&type=EW&response=json -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261111
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/11&type=EW&response=csv -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261111
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/11/11&se=EW -> status=200, chars=140847
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=890
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=890
- Applied canonical stock names from metadata snapshot changed_rows=14
- date=20261111 twse_rows=1251 tpex_rows=890 total_rows=2141 full_market_ok=True
