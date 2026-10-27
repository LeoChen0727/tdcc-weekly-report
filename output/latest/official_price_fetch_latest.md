# Official Daily Price Fetch Report

- generated_at: `2026-10-27 19:32:19 Asia/Taipei`
- target_date: `20261027`
- saved_price_date: `20261027`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1248`
- tpex_rows: `891`
- total_rows: `2139`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261027.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261027.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261027: TWSE=1248 / TPEx=891 / Total=2139 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261027 max_seconds=480
- ===== Fetch price for date 20261027 =====
- Loaded universe rows=2132
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261027
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261027&type=ALLBUT0999&response=json -> status=200, chars=233243
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1248
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1248
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261027
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/27&type=EW&response=json -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261027
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/27&type=EW&response=csv -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261027
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/10/27&se=EW -> status=200, chars=140914
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=891
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=891
- Applied canonical stock names from metadata snapshot changed_rows=14
- date=20261027 twse_rows=1248 tpex_rows=891 total_rows=2139 full_market_ok=True
