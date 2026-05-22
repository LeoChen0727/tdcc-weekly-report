# 權證官方資料抓取 Debug

- 產生時間：`2026-05-23 00:40:23 Asia/Taipei`

- note：`mapping_rows=29584, quote_rows=46, final_rows=0`

- debug csv：`output/debug/warrant_fetch_debug_latest.csv`

| source_name | market | table_index | rows | parsed_as | columns |
|---|---|---:|---:|---|---|
| TWSE_WARRANT_STOCK_JSON | TWSE | 0 | 29584 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 |
| TWSE_WARRANT_STOCK_JSON | TWSE | 1 | 3 | mapping | start / span / title |
| TWSE_WARRANT_STOCK_CSV | TWSE | 0 | 29585 | mapping | 權證收盤資訊 / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / 標的收盤資訊 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / 權證基本資訊 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / Unnamed: 12 / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / Unnamed: 17 / Unnamed: 18 |
| TWSE_WARRANT_STOCK_CSV | TWSE | 1 | 29584 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌.1 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 / Unnamed: 18 |
| TWSE_MI_INDEX_0999_JSON | TWSE | 0 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999_CSV | TWSE | 0 | 1 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999P_JSON | TWSE | 0 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999P_CSV | TWSE | 0 | 1 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999C_JSON | TWSE | 0 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999C_CSV | TWSE | 0 | 1 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999B_JSON | TWSE | 0 | 46 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 牛熊證觸及限制價格 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999B_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999B_CSV | TWSE | 0 | 1 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |