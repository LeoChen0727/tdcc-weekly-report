# Official Daily Price Fetch Report

- generated_at: `2026-10-28 19:32:27 Asia/Taipei`
- target_date: `20261028`
- saved_price_date: `20261028`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1251`
- tpex_rows: `890`
- total_rows: `2141`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261028.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261028.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261028: TWSE=1251 / TPEx=890 / Total=2141 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261028 max_seconds=480
- ===== Fetch price for date 20261028 =====
- Loaded universe rows=2139
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261028
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261028&type=ALLBUT0999&response=json -> status=200, chars=231921
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1251
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1251
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261028
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/28&type=EW&response=json -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261028
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/28&type=EW&response=csv -> status=200, chars=11253
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261028
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/10/28&se=EW -> status=200, chars=140605
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=890
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=890
- Applied canonical stock names from metadata snapshot changed_rows=13
- date=20261028 twse_rows=1251 tpex_rows=890 total_rows=2141 full_market_ok=True
