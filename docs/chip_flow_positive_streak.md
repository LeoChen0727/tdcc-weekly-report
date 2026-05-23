# 主力-三大法人-八大行庫連續轉強模型

這個模型用來建立一個獨立觀察群組：

`主力買賣超 - 三大法人買賣超 - 八大行庫買賣超 > 0`

且最新資料日往前連續 3 個交易日以上都為正。

## 資料來源

三大法人買賣超可以由官方資料取得：

- TWSE 三大法人買賣超日報 T86
- TPEx 三大法人買賣明細資訊

主力買賣超與八大行庫買賣超不能只靠三大法人資料取得。兩者都需要券商分點買賣日報：

- 主力買賣超：由每檔股票的券商分點買進/賣出資料計算。
- 八大行庫買賣超：由券商分點資料中屬於八大公股行庫體系的券商加總。

因此，若沒有券商分點買賣日報，這個模型不得啟用，也不得讓 ChatGPT 自行推算。

## 主力買賣超定義

本 repo 固定採用：

`買超前 15 名券商分點合計 - 賣超前 15 名券商分點合計`

其中賣超前 15 名用絕對賣超量計算。

不同看盤軟體可能使用前 10 名、前 15 名，或加入集中度條件。為了追蹤與回測一致性，本 repo 固定使用前 15 名。

## 八大行庫定義

設定檔：

`config/eight_public_bank_brokers.csv`

目前使用以下券商名稱關鍵字歸類：

- 合庫
- 土銀
- 臺銀 / 台銀
- 臺企銀 / 台企銀 / 臺灣企銀 / 台灣企銀
- 彰銀
- 第一金
- 兆豐
- 華南永昌 / 華南

實際計算時會依券商分點資料的 `broker_name` 做 pattern match，並加總淨買賣超。

## 需要的券商分點資料格式

每日檔案放在：

`data/broker_branch_trading/YYYYMMDD.csv`

至少需要欄位：

- `date` 或由檔名提供
- `stock_id`
- `stock_name`
- `broker_name`
- `buy_lots` 或 `buy_shares`
- `sell_lots` 或 `sell_shares`
- `market` 可選

若欄位使用中文，程式也會嘗試辨識：

- `證券代號`
- `證券名稱`
- `券商名稱`
- `分點`
- `買進張數`
- `買進股數`
- `賣出張數`
- `賣出股數`

## 輸出檔案

- `output/latest/institutional_investor_flow_latest.csv`
- `output/latest/chip_flow_positive_streak_latest.csv`
- `output/latest/chip_flow_positive_streak_latest.md`
- `output/latest/chip_flow_source_status_latest.json`
- `output/latest/chip_flow_source_status_latest.md`
- `output/history/chip_flow/chip_flow_positive_streak_history.csv`

## 缺資料處理

若 `data/broker_branch_trading/` 沒有最新連續交易日資料：

- `chip_flow_positive_streak_latest.csv` 只會輸出空表頭。
- `chip_flow_source_status_latest.json` 會標示 `disabled_missing_broker_branch_data`。
- 每日報告與 ChatGPT 規則不得把這個群組當成已啟用分類。

這樣可以避免因為資料源不足而產生假訊號。
