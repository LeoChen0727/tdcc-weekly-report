# 回檔後短線轉強：23EMA 條件獨立比較 v1

授權：`user_20261010_pullback_short_reclaim_23ema_condition_comparison`。
這是 `pullback_short_reclaim` 自有研究，不是正式模型修改或升級。

## 固定來源與問題

從 main `03387e6a610491078538c633d8ec5245c027db50` 的已釘選股份單位補充明細及摘要，
讀取 3020 原列／2992 去重訊號；從固定 `50baf29c849e5ca54a54e0f59800cef3fbe410c0`
讀取每列指定的發布快照。核對原列位置、完整 row SHA、身分及快照 transport SHA。
legacy raw/LF/CRLF 僅沿用既有傳輸身分契約；不修改快照、BOM 或內容。
不抓新資料、不重跑原 producer、不重算股價或訊號、不 import 23EMA 的 business functions。

使用者授權將同一股票訊號快照內既有 `price_pullback_*` 欄位供本模型研究比較，
不建立兩模型共用判斷函式，也不改 23EMA 欄位的 writer 或正式語意。

## 比較先後與口徑

先看高報酬、一般非負、虧損訊號的特徵分布，再比較既定單項條件。
描述性高報酬為 >=10%，虧損為 <0%，尾端虧損為 <=-10%；這些是預先固定的報表分組，
不是選股門檻、異常 disposition、移除樣本的依據或調參目標。

固定原進出價與第 5／10／20 筆個股行情收盤口徑，不加入 23EMA 的賣點或停損。
去重訊號不等於無重疊操作交易；不宣稱正式勝率、首次發布 PIT、完整總報酬或 OOS。
每期僅統計該期成熟樣本；未成熟不補零。保留原主結果、原異常排除敏感度、
已知股份單位補充三個平行口徑。第三種不是「修正後 primary」。

## 預先固定的單項條件

- 20 日漲幅 5%～25%；保留原至少 5% 的意圖。
- TDCC 高門檻增加發布旗標；其當前定義是 800 張以上或 1000 張以上持股比率週增，非全部同步。
- OBV 高於自身 20 日均線的發布旗標。
- RSI14 >=60 且 MACD histogram >0，僅研究品質分組，不升為必要條件。

不搜尋新門檻，不做所有條件排列最佳化，不將當月分組宣稱獨立樣本外。
每組列成熟數、勝／和／敗、平均／中位報酬、>=10% 命中、虧損及 <=-10% 尾端損失。
TDCC／OBV 組必須同時呈現相同 schema 樣本 baseline，不與全期間 baseline 混比。
TDCC 另外呈現 history-available baseline。高低報酬特徵分布亦同時提供這三種母體，
不能拿全期間的 True 比例比較而忽略早期缺欄。

## 缺資料與保護

早期 1146 primary 沒有新 context schema。缺欄、空值與 TDCC history unavailable 均為 unknown。
記錄的 False 不代表原始 OBV／籌碼資料已證實完整；不能拿 RSI 非空推論 OBV 完整。
raw TDCC as-of date、原始 OBV／MA20 未在這些快照保存，故不升級資料可信度。
所有原 cells/order、未解異常、舊研究、原始來源、正式 adapter/readiness、六份 PDF 保持不變。
本研究不新增月營收條件，也不納入 EPS、毛利率、營益率、營業利益、業外損益、淨利或季年財報。

## 輸出與驗證

唯一 owner `pullback_short_reclaim_23ema_condition_comparison`；四份版本化輸出為
`output/research/pullback_short_reclaim/pullback_short_reclaim_23ema_condition_comparison_v1_`
加 `detail.csv`、`summary.csv`、`features.csv`、`manifest.json`。
寫入前要求 exact owner 登錄，producer 保護 HEAD/index/所有已登錄 sentinel 與原來源。
獨立 validator 不 import producer 或正式模型 business functions。
分析結論須先檢視極大極小值、集中度與原未解異常，不能以平均值直接宣稱可用。
初次數值查核已向使用者報告約 +60%～+69% 與 -50.65% 等待查值；本次新增
`comparison_anomaly_candidate` 將原 candidate 或原報酬絕對值 >=50% 標為待查。
這只是調查觸發，不是資料錯誤或不可比較的最終處置，也不修改原 anomaly 欄位。
所有新候選留在 primary。`raw_original_candidate_exclusion_sensitivity` 僅重現排除原候選的
舊敏感度，新候選仍在其中；不得宣稱這是已處理完所有異常的乾淨數據。
