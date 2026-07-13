# 營收改善尚未反應：前向確認與特徵稽核規格

## 邊界

- `model_id`: `revenue_unreacted_range`
- `artifact_id`: `revenue_unreacted_range_forward_confirmation_feature_audit`
- 狀態固定為 `research_only`，不得直接變成 production gate、加減分、排名、PDF 指標或操作列。
- 來源母體固定使用 `absolute_or_two_month_yoy_ge15` 的 source-first episodes，並沿用同股不重疊 lifecycle。

## 事件與績效

- `source_first_close_above_prev20_reference` 只用來逐筆對齊舊 source-first 的第一天高於前 20 日最高收盤價，不是新確認建議。
- 可操作研究事件使用 close crossover，也就是前一日未突破而當日收盤突破前 N 日最高收盤價。
- 每條規則只能採 episode 內第一次符合事件。較早事件一旦通過該規則，後來成功不得回頭取代先前失敗。
- 需要隔日確認的規則，以隔日收盤判定；確認後下一交易日開盤才是研究進場價。
- 研究固定出場為確認日起算 D+20 收盤。本 artifact 尚未定義停損，不得把無停損結果當成正式 operation contract。
- 嚴格成功為觸發收盤後 D+15 內達 +20%，且至 D+20 每日收盤均未跌回 +20% 以下。
- 本次沒有核准和局定義。未滿 D+20 的資料列為 right-censored，不能算失敗。

## 特徵對照

- 成功組使用 source artifact 標記的全部真正發動日。
- 失敗組每個 episode 最多使用第一個成熟失敗突破日。
- 此對照用於找成功與失敗的特徵差異，不是前向交易勝率。
- 技術、TDCC、月營收強度、營收時間差、位階、型態與大盤特徵都必須同時揭露成功組與失敗組命中率。
- 盤中 high/low 只能是 advisory K 棒或風險觀察，不能作為 entry、exit、stop、勝敗或 realized return 價格。

## 防錯

- Primary metrics 保留未完成根因判定的 anomaly candidates；另列排除候選的 sensitivity，兩者不得互換。
- D+20 絕對操作報酬達 80% 只能觸發 review candidate，不能直接判成極端值或異常。Primary 必須保留，另列排除候選的敏感度，並逐筆輸出 raw/analysis 單日收盤變動、開盤跳空、價格修正 id 與尚缺的公司行動資料層。
- `episode_key + rule_id` 必須唯一，且每個來源 episode 對每條規則恰有一列。
- 成功／失敗事件表的 `episode_key + contrast_group` 必須唯一。
- 規則 detail 不重複寫完整特徵；完整特徵只保留在 event detail，且 rule detail 必須小於 50 MB。
- 4916 事欣科必須保留 `20251209` 第一個成熟失敗與 `20260518` 真正成功；1303 南亞必須保留 `20260527` 真正成功。
- 月營收與季／年財報分離。本 artifact 未使用 EPS、毛利率、營益率、營業利益、業外或淨利；未建立正式 PIT 財報資料層前不得加入。
