# 權證官方資料抓取 Debug

- 產生時間：`2026-07-26 15:09:43 Asia/Taipei`

- note：`mapping_rows=28961, quote_rows=0, final_rows=28961`

- debug csv：`output/debug/warrant_fetch_debug_latest.csv`

| source_name | market | table_index | rows | parsed_as | columns |
|---|---|---:|---:|---|---|
| TWSE_WARRANT_STOCK_JSON | TWSE | 0 | 28961 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 |
| TWSE_WARRANT_STOCK_JSON | TWSE | 1 | 3 | mapping | start / span / title |
| TWSE_WARRANT_STOCK_CSV | TWSE | 0 | 28962 | mapping | 權證收盤資訊 / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / 標的收盤資訊 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / 權證基本資訊 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / Unnamed: 12 / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / Unnamed: 17 / Unnamed: 18 |
| TWSE_WARRANT_STOCK_CSV | TWSE | 1 | 28961 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌.1 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 / Unnamed: 18 |