# 23EMA 原始確認歷史 consumer 啟用契約

本文件保留 2026-10-23 已授權啟用的追蹤契約。歷史核准績效證據仍固定於
`docs/specs/price_pullback_23ema_operation_candidate_spec.md`，其 canonical SHA-256
`a11d540368868d1854865b1d8a64f466ff368e0e618bc666c3411770cf61dd5e`
與 `config/formal_model_evidence_pins.csv` 均不變。新增追蹤說明不得改寫該固定證據。

## 2026-10-23 原始確認歷史 consumer 啟用契約

- 使用者授權：`user_20261023_authorize_23ema_confirmation_history_consumer_activation`。
- migration：`price_pullback_23ema_confirmation_history_consumer_activation_20261023`。
- 首次真實發布 `r1` 日期固定為 `20261019`，canonical path 為
  `output/history/daily_model_snapshots/daily_price_pullback_23ema_operation_section_20261019_r1_d41214b72349.csv`，
  canonical SHA-256 為 `d41214b72349a9683cd686636a5c750b03752caebfd2c85bbb5dcee718b9008f`。
- 唯一 writer 仍是 `scripts/update_daily_published_model_snapshots.py`，
  唯一 consumer 模型仍是 `price_pullback_23ema`；維持 model-private，不新增跨模型共享或資料 family。
- consumer 只能承接早於 operation as-of 的原始 `r1` `confirmed_operation`：
  原發布日必須 `buy_rank_eligible=True`，三項原排名完整，full／highlight 雙列一致。
  後續 active rows 必須保留原始 artifact SHA、full-row SHA、revision、確認日期及凍結欄位。
- 按原確認時間依序承接持倉。同一股票／report line 的前一持倉尚未結束時，
  後到確認永久不納入持倉；即使前一持倉之後已出場，也不得復活該確認。
- 缺 manifest／history family／首次真實 `r1`，或 path、SHA、原始雙 view 身份不符時停止。
  `r2` 不得取代原始 `r1` 排名或把原始 unranked 確認升格；不得從舊 signal、latest 或 research 補倉。
- 不回填 `20261019` 前的確認或舊發布 snapshot。原 11 families、正式 source/runtime gates、
  PDF adapter 消費邊界與既有空態／列數契約均保留。
- 本次不變更 selector、條件、評分、排名或正式價格規則：訊號確認後隔日開盤進場；
  收盤突破訊號日前 20 個交易日高點後隔日開盤出場；
  收盤連續 4 個交易日低於 `0.96 * min(MA20, EMA23)` 後隔日開盤停損。
- 本次是原始發布確認與後續 lifecycle 的承接；不構成實際交易、完整 selector PIT、
  新回測報酬或 promotion 證據，既有 unresolved anomaly 與研究升級限制維持。
