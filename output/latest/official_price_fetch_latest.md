# Official Daily Price Fetch Report

- generated_at: `2026-07-14 16:02:16 Asia/Taipei`
- target_date: `20260713`
- saved_price_date: `20260713`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1239`
- tpex_rows: `894`
- total_rows: `2133`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260713.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260713.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260713: TWSE=1239 / TPEx=894 / Total=2133 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260713 max_seconds=480
- ===== Fetch price for date 20260713 =====
- Loaded universe rows=2133
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260713
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260713&type=ALLBUT0999&response=json -> status=200, chars=232790
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1239
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1239
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260713
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/13&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260713
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/13&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260713
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/07/13&se=EW -> status=200, chars=141183
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=894
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=894
- Applied canonical stock names from metadata snapshot changed_rows=16
- date=20260713 twse_rows=1239 tpex_rows=894 total_rows=2133 full_market_ok=True