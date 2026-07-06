# Official Daily Price Fetch Report

- generated_at: `2026-07-06 23:23:59 Asia/Taipei`
- target_date: `20260706`
- saved_price_date: `20260706`
- is_target_date: `True`
- result: `success_target_full_market`
- reason: 成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows: `1237`
- tpex_rows: `900`
- total_rows: `2137`
- full_market_ok: `True`

## Output Paths

- dated_csv: `data/daily_price/20260706.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260706.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## Fetch Attempts

- 20260706: TWSE=1237 / TPEx=900 / Total=2137 / full_market_ok=True

## Fetch Logs

- Start official daily price fetch target_date=20260706 max_seconds=480
- ===== Fetch price for date 20260706 =====
- Loaded universe rows=1986
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260706
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260706&type=ALLBUT0999&response=json -> status=200, chars=231706
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1237
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1237
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260706
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/06&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260706
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/07/06&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OTC_QUOTES_NO1430_JSON date=20260706
- GET https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d=115/07/06&se=EW -> status=200, chars=141510
- TPEX_OTC_QUOTES_NO1430_JSON: parsed TPEx JSON rows=900
- TPEx batch selected source=TPEX_OTC_QUOTES_NO1430_JSON, rows=900
- Applied canonical stock names from metadata snapshot changed_rows=14
- date=20260706 twse_rows=1237 tpex_rows=900 total_rows=2137 full_market_ok=True