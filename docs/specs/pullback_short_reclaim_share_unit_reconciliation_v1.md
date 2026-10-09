# 回檔後短線轉強：固定來源股份單位補充 v1

## 範圍與結論界線

本次處理 `pullback_short_reclaim` 舊發布訊號研究中的寶雅（5904）換股價格單位問題；不是模型升級，不改選股條件、分數、排名、訊號名單、進出日期、持有期、正式 adapter/readiness 或 PDF。僅新增此模型獨立 producer、獨立 validator、三份不可變補充產物及必要登錄。其他模型與舊研究保持原位、原 bytes。

授權參照：`user_requested_remaining_model_repairs_20261009`。

## 固定證據

- 研究來源 commit：`50baf29c849e5ca54a54e0f59800cef3fbe410c0`。
- 原始 5904 行情 commit：`12b817cbac0e198ac614a542e5cbf057959ed4a5`；內容 SHA-256 必須與舊研究宣告的原始來源一致。
- config：`config/pullback_short_reclaim_share_unit_reconciliation_v1.json`，逐件列明 Git commit、path、原始 bytes SHA-256。
- [櫃買中心公告，證櫃監字第11500046541號](https://www.tpex.org.tw/storage/eb_data/11507/11500046541.html)：寶雅面額 10 元改為 1 元，每舊股換發 10 股；2026/07/30 至 2026/08/07 暫停交易，2026/08/10 新股開始交易。
- 官方回應原始 UTF-8 bytes 以 base64 收於本模型 config，SHA-256 `5a8f94d8d4707589b59920e3791bf303eab4a966f0bc47ae3f04a503097338ee`。收件時間僅證明本次取得，不是首次發布或完整更正版本鏈證明。

只從既存 Git objects 讀取五份精確固定來源；不得以 mutable latest 替代，不自動 fetch、不下載全市場、不物化完整資料樹。來源不存在或 hash 不符即停止。

## 計算契約

逐格保留原 3,020 筆事件及 2,992 筆 primary canonical signals；三期原始摘要、全部原欄位與未解 disposition 均保留。新欄位是並列補充，不覆蓋原報酬。

僅 `stock_id=5904` 且 `entry_date < 20260810 <= exit_date` 的已成熟觀察可使用股份係數 10；其餘係數為 1，但不代表已全面核實其他公司行動。補充價格報酬為 `(exit_close * share_factor / entry_open - 1) * 100`。

本事件原進場日為 20260714、open=665；D+5 為 20260720 close=611，D+10 為 20260727 close=668，D+20 為 20260819 close=78。原 D+20 以可取得的個股行情列數計數，停牌期間沒有行情列；不得在此修復默默改成大盤交易日計數或改出場日。

`partial_known_share_unit_...` 摘要沿用原 primary population，保留未解候選，不作刪除候選後的美化。僅處理一件已知換股的價格單位，不能稱為 corrected primary、全市場完整還原價、完整總報酬、正式勝率、嚴格首次發布 PIT 或可升級證據。現金股利、零股處分及完整公司行動覆蓋未證實，`cash_flow_status=not_modelled_not_total_return`；原 `formal_use_allowed`、`trade_eligible`、`promotion_evidence_allowed` 維持 False。

`unresolved_anomaly_candidate` 不因套用係數而自動解除。正式模型仍缺完整操作契約及獨立升級證據。往後若要變更門檻或操作規則，須先在同買賣規則下比較高、低報酬交易特徵；本次不做條件堆疊或勝率調參。

## 執行與驗證

- Producer：`scripts/build_pullback_short_reclaim_share_unit_reconciliation.py`，僅本地明確執行，不加入研究 workflow 自動產生。
- 獨立 validator：`scripts/validate_pullback_short_reclaim_share_unit_reconciliation.py`，不得 import producer 或 production business functions；自行讀固定來源及核算欄位、官方 receipt、價格列與 manifest。
- Regression：`tests/test_pullback_short_reclaim_research.py`；既有 CI shared-model-research 選取，不修改 workflow YAML。
- 新資料三 family 各自以 exact path 登錄；writer/consumer 只屬本模型的新研究階段。

唯一可寫研究輸出：

1. `output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_detail.csv`
2. `output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_summary.csv`
3. `output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_manifest.json`

已存在且內容不同時不得覆寫；必須另行確認新版本。輸出前後核對既有 protected sentinels 及舊研究的 Git tree/index/實體 bytes；sparse worktree 不為了驗證而載入保護資料樹。
