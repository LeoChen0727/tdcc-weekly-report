# 權證官方資料抓取 Debug

- 產生時間：`2026-08-05 10:41:39 Asia/Taipei`

- note：`mapping_rows=29890, quote_rows=29827, final_rows=29827`

- debug csv：`output/debug/warrant_fetch_debug_latest.csv`

| source_name | market | table_index | rows | parsed_as | columns |
|---|---|---:|---:|---|---|
| TWSE_MI_INDEX_0999_JSON | TWSE | 0 | 27541 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999P_JSON | TWSE | 0 | 2286 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999P_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_WARRANT_STOCK_JSON | TWSE | 0 | 29890 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 |
| TWSE_WARRANT_STOCK_JSON | TWSE | 1 | 3 | mapping | start / span / title |