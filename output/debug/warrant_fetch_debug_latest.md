# 權證官方資料抓取 Debug

- 產生時間：`2026-05-22 01:39:28 Asia/Taipei`

- note：`mapping_rows=30018, quote_rows=30039, final_rows=30018`

- debug csv：`output/debug/warrant_fetch_debug_latest.csv`

| source_name | market | table_index | rows | parsed_as | columns |
|---|---|---:|---:|---|---|
| TWSE_WARRANT_STOCK_JSON | TWSE | 0 | 30018 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 |
| TWSE_WARRANT_STOCK_JSON | TWSE | 1 | 3 | mapping | start / span / title |
| TWSE_WARRANT_STOCK_CSV | TWSE | 0 | 30019 | mapping | 權證收盤資訊 / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / 標的收盤資訊 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / 權證基本資訊 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / Unnamed: 12 / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / Unnamed: 17 / Unnamed: 18 |
| TWSE_WARRANT_STOCK_CSV | TWSE | 1 | 30018 | mapping | 權證代號 / 權證簡稱 / 收盤價 / 漲跌 / 標的代號 / 標的名稱 / 收盤價/指數 / 漲跌.1 / 權證類型 / 履約方式 / 上市日期 / 履約開始日 / 最後交易日 / 履約截止日 / 行使比例 / 履約價格(元)/點數 / 上限價格(元)/點數 / 下限價格(元)/點數 / Unnamed: 18 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 0 | 56 | quote | 指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 1 | 48 | quote | 指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 2 | 34 | quote | 指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 3 | 47 | quote | 報酬指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 4 | 49 | quote | 報酬指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 5 | 33 | quote | 報酬指數 / 收盤指數 / 漲跌(+/-) / 漲跌點數 / 漲跌百分比(%) / 特殊處理註記 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 6 | 17 | quote | 成交統計 / 成交金額(元) / 成交股數(股) / 成交筆數 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 7 | 5 | quote | 類型 / 整體市場 / 股票 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 8 | 31379 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 |
| TWSE_MI_INDEX_ALL_JSON | TWSE | 9 | 2 | quote | start / span / title |
| TWSE_MI_INDEX_0999_JSON | TWSE | 0 | 27229 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999_CSV | TWSE | 0 | 27236 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999_CSV | TWSE | 1 | 27235 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 / Unnamed: 20 |
| TWSE_MI_INDEX_0999P_JSON | TWSE | 0 | 2723 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999P_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999P_CSV | TWSE | 0 | 2730 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999P_CSV | TWSE | 1 | 2729 | quote | 暫停交易 / 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 標的代號 / 標的名稱 / 標的收盤價/指數 / Unnamed: 20 |
| TWSE_MI_INDEX_0999C_JSON | TWSE | 0 | 34 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 牛熊證觸及限制價格 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999C_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999C_CSV | TWSE | 0 | 41 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999C_CSV | TWSE | 1 | 40 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 牛熊證觸及限制價格 / 標的代號 / 標的名稱 / 標的收盤價/指數 / Unnamed: 20 |
| TWSE_MI_INDEX_0999B_JSON | TWSE | 0 | 9 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 牛熊證觸及限制價格 / 標的代號 / 標的名稱 / 標的收盤價/指數 |
| TWSE_MI_INDEX_0999B_JSON | TWSE | 1 | 3 | quote | start / span / title |
| TWSE_MI_INDEX_0999B_CSV | TWSE | 0 | 16 | quote | (元,股) / Unnamed: 1 / Unnamed: 2 / Unnamed: 3 / Unnamed: 4 / Unnamed: 5 / Unnamed: 6 / Unnamed: 7 / Unnamed: 8 / Unnamed: 9 / Unnamed: 10 / Unnamed: 11 / (元,交易單位) / Unnamed: 13 / Unnamed: 14 / Unnamed: 15 / Unnamed: 16 / 標的資訊 / Unnamed: 18 / Unnamed: 19 / Unnamed: 20 |
| TWSE_MI_INDEX_0999B_CSV | TWSE | 1 | 15 | quote | 證券代號 / 證券名稱 / 成交股數 / 成交筆數 / 成交金額 / 開盤價 / 最高價 / 最低價 / 收盤價 / 漲跌(+/-) / 漲跌價差 / 最後揭示買價 / 最後揭示買量 / 最後揭示賣價 / 最後揭示賣量 / 本益比 / 牛熊證觸及限制價格 / 標的代號 / 標的名稱 / 標的收盤價/指數 / Unnamed: 20 |