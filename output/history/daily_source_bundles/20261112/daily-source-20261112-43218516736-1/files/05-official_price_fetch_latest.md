# Official Daily Price Fetch Report

- generated_at: `2026-11-12 19:33:10 Asia/Taipei`
- target_date: `20261112`
- saved_price_date: `20261112`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1250`
- tpex_rows: `889`
- total_rows: `2139`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261112.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261112.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261112: TWSE=1250 / TPEx=889 / Total=2139 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261112 max_seconds=480
- ===== Fetch price for date 20261112 =====
- Loaded universe rows=2141
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261112
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261112&type=ALLBUT0999&response=json -> status=200, chars=234426
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1250
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1250
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261112
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/12&type=EW&response=json -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261112
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/11/12&type=EW&response=csv -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261112
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/11/12&se=EW -> status=200, chars=141089
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=889
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=889
- Applied canonical stock names from metadata snapshot changed_rows=15
- date=20261112 twse_rows=1250 tpex_rows=889 total_rows=2139 full_market_ok=True
