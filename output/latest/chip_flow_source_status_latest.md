# 主力-三大法人-八大行庫連續轉強股

- generated_at: `2026-05-23 23:02:32 Asia/Taipei`
- main_price_date: `20260523`
- status: `disabled_missing_required_data`
- broker_branch_data_required: `True`
- broker_branch_source_dir: `data/broker_branch_trading`

## 定義

- 主力買賣超：每檔股票當日買超前 15 名券商分點合計 - 賣超前 15 名券商分點合計。
- 三大法人買賣超：TWSE / TPEx 官方三大法人個股買賣超。
- 八大行庫買賣超：依 config/eight_public_bank_brokers.csv 對券商名稱做家族比對後加總。
- 入選條件：主力買賣超 - 三大法人買賣超 - 八大行庫買賣超 > 0，且最新資料日往前連續 3 個交易日以上都為正。

## 今日狀態

此分類今日未啟用，因為尚未取得可計算主力與八大行庫的券商分點買賣日報資料。
ChatGPT 不得自行推算或編造此分類。
