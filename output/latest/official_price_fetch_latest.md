# Official Daily Price Fetch Report

- generated_at: `2026-08-25 19:43:39 Asia/Taipei`
- target_date: `20260825`
- saved_price_date: `20260825`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1238`
- tpex_rows: `880`
- total_rows: `2118`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260825.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260825.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260825: TWSE=1238 / TPEx=880 / Total=2118 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260825 max_seconds=480
- ===== Fetch price for date 20260825 =====
- Loaded universe rows=2122
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260825
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260825&type=ALLBUT0999&response=json -> status=200, chars=231085
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1238
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1238
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260825
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/08/25&type=EW&response=json -> status=200, chars=11245
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260825
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/08/25&type=EW&response=csv -> status=200, chars=11245
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260825
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/08/25&se=EW -> status=200, chars=139201
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=880
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=880
- Applied canonical stock names from metadata snapshot changed_rows=13
- date=20260825 twse_rows=1238 tpex_rows=880 total_rows=2118 full_market_ok=True
