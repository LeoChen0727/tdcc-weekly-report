# 官方每日價格資料抓取狀態

- 產生時間：`2026-05-27 19:26:54 Asia/Taipei`
- target_date：`20260527`
- saved_price_date：`20260527`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1237`
- tpex_rows：`5724`
- total_rows：`6961`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260527.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260527.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260527: TWSE=1237 / TPEx=5724 / Total=6961 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260527
- ===== Fetch price for date 20260527 =====
- Loaded universe rows=6977
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260527
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260527&type=ALLBUT0999&response=json -> status=200, chars=232105
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1237
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1237
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260527
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/27&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260527
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/05/27&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260527
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/05/27&s=0,asc,0 -> status=200, chars=1484535
- TPEX_OLD_DAILY_JSON: parsed TPEx JSON rows=5724
- TPEx batch selected source=TPEX_OLD_DAILY_JSON, rows=5724
- date=20260527 twse_rows=1237 tpex_rows=5724 total_rows=6961 full_market_ok=True