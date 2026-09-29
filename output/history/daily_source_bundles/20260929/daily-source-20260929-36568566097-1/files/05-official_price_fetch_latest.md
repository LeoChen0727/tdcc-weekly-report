# Official Daily Price Fetch Report

- generated_at: `2026-09-29 19:32:18 Asia/Taipei`
- target_date: `20260929`
- saved_price_date: `20260929`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1244`
- tpex_rows: `886`
- total_rows: `2130`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260929.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260929.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260929: TWSE=1244 / TPEx=886 / Total=2130 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260929 max_seconds=480
- ===== Fetch price for date 20260929 =====
- Loaded universe rows=2126
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260929
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260929&type=ALLBUT0999&response=json -> status=200, chars=232599
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1244
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1244
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260929
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/09/29&type=EW&response=json -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260929
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/09/29&type=EW&response=csv -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260929
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/09/29&se=EW -> status=200, chars=140435
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=886
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=886
- Applied canonical stock names from metadata snapshot changed_rows=11
- date=20260929 twse_rows=1244 tpex_rows=886 total_rows=2130 full_market_ok=True
