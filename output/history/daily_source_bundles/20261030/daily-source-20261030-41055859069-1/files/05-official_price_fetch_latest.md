# Official Daily Price Fetch Report

- generated_at: `2026-10-30 19:33:50 Asia/Taipei`
- target_date: `20261030`
- saved_price_date: `20261030`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1249`
- tpex_rows: `891`
- total_rows: `2140`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20261030.csv`
- dated_alt_csv: `data/daily_price/daily_price_20261030.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20261030: TWSE=1249 / TPEx=891 / Total=2140 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20261030 max_seconds=480
- ===== Fetch price for date 20261030 =====
- Loaded universe rows=2129
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20261030
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261030&type=ALLBUT0999&response=json -> status=200, chars=236117
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1249
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1249
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20261030
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/30&type=EW&response=json -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20261030
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/10/30&type=EW&response=csv -> status=200, chars=11429
- TPEX_NEW_AFTERTRADING_CSV: rejected TPEx schema: ',' expected after '"'
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20261030
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/10/30&se=EW -> status=200, chars=141090
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=891
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=891
- Applied canonical stock names from metadata snapshot changed_rows=12
- date=20261030 twse_rows=1249 tpex_rows=891 total_rows=2140 full_market_ok=True
