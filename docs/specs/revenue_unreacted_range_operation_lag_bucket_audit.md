# 營收低反應區間模型：營收轉強後發動時間差績效稽核

## 邊界

- `model_id`: `revenue_unreacted_range`
- `artifact_id`: `revenue_unreacted_range_operation_lag_bucket_audit`
- 本 artifact 為 model-owned、research-only，不修改 production registry、正式 operation adapter、PDF、ranking 或 scoring。
- 固定消費 `revenue_unreacted_range_rearmed_operation_grid` 中已採用的 research grid：`rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|d30|none_no_stop_reference`。
- Primary 保留待查來源與報酬資料；排除待查資料只作敏感度，不能取代 Primary。

## 時間口徑

- 每筆交易的「最新合格營收」只能取 trigger 當日以前已知的最後一筆合格營收。
- episode 結束時的 `latest_qualifying_trade_date` 若晚於 trigger，視為未來資料，不得回填本筆交易。
- `source_first_condition_audit` 必須提供彼此對齊的 `qualifying_revenue_periods`、`qualifying_source_dates`、`qualifying_trade_dates` 與 `qualifying_sequence_indices`。
- 距最新合格營收的固定時間桶為 `0-20`、`21-40`、`41-60`、`61-90`、`91-126` 個交易日。
- 距 episode 首次合格營收使用相同五桶，另加 `127+`，因後續合格月營收可能延長 active horizon；不得遺漏或重疊任何交易。
- 觀察期限決策另以不重疊的 `0-60` 與 `61-126` 兩段輸出，兩段加總必須等於全部交易；固定五桶仍須保留，不能只留下合併結果。
- 最新合格營收到 trigger 的時間差不得超過 126 個交易日。

## 操作與績效口徑

- 基礎訊號：收盤突破前 20 日最高收盤價，且 `MA60 > MA120`。
- 加分確認：D+1 收盤續攻，D+2 開盤進場。
- 出場：進場後固定 D+30 收盤，不停損。
- 重新武裝：前次實際出場後，下一交易日才重新掃描。
- 同股重疊必須為 0。
- 勝／和／敗沿用 operation grid：實現報酬 `>0`／`=0`／`<0`。
- 每個時間桶必須輸出筆數、勝／和／敗率、平均／中位數、P10／P90、報酬至少 20% 比率，以及相對全體的勝率與平均報酬差。
- 樣本數只揭露，不得因樣本少自動否定條件。

## 防錯

- Summary 各時間桶加總必須等於同一 analysis basis 的 overall 筆數。
- Detail 必須與 adopted mature operation grid 一對一，不能多列、漏列或重複。
- Validator 必須從 source operation detail、source episode lineage 與股票交易日重新計算時間差，不能只相信輸出欄位。
- Validator 必須保留一個「episode 最終營收日晚於 trigger」的 regression case，證明未來更新確實被忽略。
- Markdown 必須列出 `0-60` 與 `61-126` 的 Primary／敏感度比較，以及晚段待查交易；觀察期限候選不等於 promotion。
- Primary 中數字異常只可標為待查，不能因絕對值、分位數或統計門檻直接刪除；敏感度需獨立標示。

## 財務資料範圍

- 本輪只使用月營收 point-in-time 資料。
- EPS、毛利率、營益率、營業利益、業外、淨利及季／年財報欄位未納入。
- 在正式 PIT 財報資料層建立並驗證以前，上述欄位不得成為 gate、加分、扣分、排名、PDF metric 或 promotion evidence。
