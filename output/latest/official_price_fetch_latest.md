# 官方每日價格資料抓取狀態

- 產生時間：`2026-06-02 19:34:01 Asia/Taipei`
- target_date：`20260602`
- saved_price_date：`20260602`
- is_target_date：`True`
- result：`success_target_full_market`
- reason：成功取得目標日 TWSE + TPEx 官方日線資料。
- twse_rows：`1236`
- tpex_rows：`5395`
- total_rows：`6631`
- full_market_ok：`True`

## 輸出檔案

- dated_csv: `data/daily_price/20260602.csv`
- dated_alt_csv: `data/daily_price/daily_price_20260602.csv`
- latest_csv: `output/latest/official_daily_price_latest.csv`

## 嘗試紀錄

- 20260602: TWSE=1236 / TPEx=5395 / Total=6631 / full_market_ok=True

## Fetch logs

- Start official daily price fetch target_date=20260602
- ===== Fetch price for date 20260602 =====
- Loaded universe rows=6893
- Trying TWSE batch source=TWSE_RWD_JSON_MI_INDEX date=20260602
- GET https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260602&type=ALLBUT0999&response=json -> status=200, chars=232012
- TWSE_RWD_JSON_MI_INDEX: parsed TWSE rows=1236
- TWSE batch selected source=TWSE_RWD_JSON_MI_INDEX, rows=1236
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_JSON date=20260602
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/02&type=EW&response=json -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_JSON: JSON parse failed
- Trying TPEx batch source=TPEX_NEW_AFTERTRADING_CSV date=20260602
- GET https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date=2026/06/02&type=EW&response=csv -> status=200, chars=11371
- TPEX_NEW_AFTERTRADING_CSV: parsed TPEx CSV rows=0
- Trying TPEx batch source=TPEX_OLD_DAILY_JSON date=20260602
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d=115/06/02&s=0,asc,0 failed: ChunkedEncodingError: Response ended prematurely
- Trying TPEx batch source=TPEX_OLD_DAILY_CSV date=20260602
- GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=115/06/02&s=0,asc,0 -> status=200, chars=1459769
- TPEX_OLD_DAILY_CSV: parsed TPEx CSV rows=5395
- TPEx batch selected source=TPEX_OLD_DAILY_CSV, rows=5395
- date=20260602 twse_rows=1236 tpex_rows=5395 total_rows=6631 full_market_ok=True