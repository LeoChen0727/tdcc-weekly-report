# 官方每日價格資料抓取狀態

- 產生時間：`2026-06-01 22:13:53 Asia/Taipei`
- target_date：`20260601`
- saved_price_date：`20260601`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1238`
- tpex_rows：`5654`
- total_rows：`6892`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260601.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260601.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260601: TWSE=1238 / TPEx=5654 / Total=6892 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260601
- ===== Fetch price for date 20260601 =====
- Loaded universe rows=6893
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260601
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260601&type=ALLBUT0999&response=json -> status=200, chars=232124
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1238
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1238
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260601
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/01&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260601
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/01&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260601
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/01&s=0,asc,0 -> status=200, chars=1473377
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5654
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5654
- date=20260601 twse_rows=1238 tpex_rows=5654 total_rows=6892 full_market_ok=True