# 主力扣八大連續為正使用規則

這份規則給 ChatGPT 對話使用。此清單是獨立候選池，不和每日全市場候選股的其他指標混合排名。

## 資料入口

優先讀 GitHub Pages：

```text
https://LeoChen0727.github.io/tdcc-weekly-report/latest/main_force_eight_positive_latest.md
https://LeoChen0727.github.io/tdcc-weekly-report/latest/main_force_eight_positive_latest.csv
```

Pages 讀不到時改讀 raw：

```text
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/main_force_eight_positive_latest.md
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/main_force_eight_positive_latest.csv
```

狀態檔：

```text
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/main_force_eight_positive_latest.json
```

## 判斷規則

只使用以下條件：

```text
主力買賣超 - 八大法人買賣超 - 八大行庫買賣超 > 0
```

且最新資料日往前連續三個交易日以上都為正。

不要加入價格、成交量、均線、TDCC、權證、營收、型態或其他指標。

## 欄位說明

```text
date: 最新資料日期
stock_id: 股票代號
stock_name: 股票名稱
positive_streak_days: 連續為正天數
streak_start_date: 連續為正起始日
streak_end_date: 連續為正結束日
latest_value: 最新日的主力扣八大值
previous_1_value: 前一個交易日的主力扣八大值
previous_2_value: 前兩個交易日的主力扣八大值
latest_main_force_net_buy: 最新日主力買賣超
latest_eight_institution_net_buy: 最新日八大法人買賣超
latest_eight_bank_net_buy: 最新日八大行庫買賣超
```

## 對話回覆格式

請先確認 status：

- `ok`: 可以列出股票。
- `no_candidates`: 最新資料日沒有符合條件股票。
- `missing_source_data`: repo 尚未有可計算的主力 / 八大法人 / 八大行庫原始資料。

若 status 是 `missing_source_data`，請直接說資料來源尚未建立，不要假裝有清單。

若 status 是 `ok`，請只列出符合條件股票，並顯示：

```text
股票代號 / 股票名稱
連續為正天數
最新主力扣八大值
近三日數值
```

不要給個人持股、成本、損益或操作建議。
