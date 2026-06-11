# 官方權證每日資料抓取狀態

- 產生時間：`2026-06-11 14:20:14 Asia/Taipei`
- 資料日期：`20260611`
- 輸出檔：`output/latest/warrant_daily_raw_latest.csv`
- 權證對照表筆數：`0`
- 權證成交行情筆數：`0`
- 最終可彙總筆數：`0`
- debug：`output/debug/warrant_fetch_debug_latest.md`

- warning：`權證資料未能產出股票層級可彙總資料。若 mapping_rows > 0 但 quote_rows = 0，代表 MI_INDEX 沒抓到權證成交行情；若 quote_rows > 0 但 final_rows = 0，代表成交行情與權證對照表無法用權證代號合併。`

## Fetch logs

- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260611&type=0999&response=json
- failed source=TWSE_MI_INDEX_0999_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260611&type=0999&response=csv
- failed source=TWSE_MI_INDEX_0999P_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260611&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260611&type=0999P&response=csv
- no_usable_quote_rows date=20260611, quote_rows=0; trying previous calendar date
- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260610&type=0999&response=json
- failed source=TWSE_MI_INDEX_0999_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260610&type=0999&response=csv
- failed source=TWSE_MI_INDEX_0999P_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260610&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260610&type=0999P&response=csv
- no_usable_quote_rows date=20260610, quote_rows=0; trying previous calendar date
- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260609&type=0999&response=json
- failed source=TWSE_MI_INDEX_0999_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260609&type=0999&response=csv
- failed source=TWSE_MI_INDEX_0999P_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260609&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Read timed out. (read timeout=8.0), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260609&type=0999P&response=csv
- no_usable_quote_rows date=20260609, quote_rows=0; trying previous calendar date
- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Max retries exceeded with url: /rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999&response=json (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.twse.com.tw', port=443) at 0x7f50dac3e210>, 'Connection to www.twse.com.tw timed out. (connect timeout=8.0)')), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999&response=json
- failed source=TWSE_MI_INDEX_0999_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Max retries exceeded with url: /rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999&response=csv (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.twse.com.tw', port=443) at 0x7f50dac84b50>, 'Connection to www.twse.com.tw timed out. (connect timeout=8.0)')), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999&response=csv
- failed source=TWSE_MI_INDEX_0999P_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Max retries exceeded with url: /rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999P&response=json (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.twse.com.tw', port=443) at 0x7f50dac875d0>, 'Connection to www.twse.com.tw timed out. (connect timeout=8.0)')), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999P&response=json
- failed source=TWSE_MI_INDEX_0999P_CSV, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Max retries exceeded with url: /rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999P&response=csv (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.twse.com.tw', port=443) at 0x7f50dac3f810>, 'Connection to www.twse.com.tw timed out. (connect timeout=8.0)')), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260608&type=0999P&response=csv
- no_usable_quote_rows date=20260608, quote_rows=0; trying previous calendar date
- failed source=TWSE_MI_INDEX_0999_JSON, error=HTTPSConnectionPool(host='www.twse.com.tw', port=443): Max retries exceeded with url: /rwd/zh/afterTrading/MI_INDEX?date=20260607&type=0999&response=json (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.twse.com.tw', port=443) at 0x7f50dadbe9d0>, 'Connection to www.twse.com.tw timed out. (connect timeout=8.0)')), url=https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20260607&type=0999&response=json
- deadline_exceeded quote date=20260607, source=TWSE_MI_INDEX_0999_CSV
- deadline_exceeded quote date=20260607, qtype=0999P
- no_usable_quote_rows date=20260607, quote_rows=0; trying previous calendar date
- deadline_exceeded before quote fallback date=20260606