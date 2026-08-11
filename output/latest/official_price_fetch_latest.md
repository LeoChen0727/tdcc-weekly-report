# Official Daily Price Fetch Report

- generated_at: `2026-08-11 08:27:56 Asia/Taipei`
- target_date: `20260810`
- saved_price_date: `20260810`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1241`
- tpex_rows: `893`
- total_rows: `2134`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260810.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260810.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260810: TWSE=1241 / TPEx=893 / Total=2134 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260810 max_seconds=480
- ===== Fetch price for date 20260810 =====
- Loaded universe rows=2119
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260810
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260810&type=ALLBUT0999&response=json -> status=200, chars=231643
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1241
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1241
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260810
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/08/10&type=EW&response=json -> status=200, chars=11245
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260810
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/08/10&type=EW&response=csv -> status=200, chars=11245
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260810
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/08/10&se=EW -> status=200, chars=140442
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=893
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=893
- Applied canonical stock names from metadata snapshot changed_rows=15
- date=20260810 twse_rows=1241 tpex_rows=893 total_rows=2134 full_market_ok=True