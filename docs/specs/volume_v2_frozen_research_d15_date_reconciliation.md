# Volume V2 凍結研究 D15 日期對帳

本工具記錄低位及高位研究樣本的 D10 admission 與 D15 持倉日期差異。
它是只讀來源的 audit receipt 工具，不是模型 producer、回測、正式持倉重建或模型升級證據。
原研究逐筆、主要統計、異常標記、價格、正式條件、核准與 readiness 均不更動。
不產生 `output/latest` 或被模型消費的研究資料家族，也不計算刪除重疊列後的績效。

## 固定來源

來源 commit 固定為 `e74d928fd34fc0f5e0c7c91ac1e5041f310851e5`，透過
`git show <commit>:<path>` 讀既有 blob，不依賴工作目錄的 mutable latest。
`GIT_NO_LAZY_FETCH=1` 禁止讀取時隱性下載；工具不讀市場價格、不補資料。
CLI 不接受替換來源 hash 或 commit 的參數。

| 模型／來源 | SHA-256 |
|---|---|
| 低位 D15 `volume_range_breakout_v2_candidate_bucket_contract_detail_latest.csv` | `d6eb16844bba1857b9028335aceb50524d4319d9726a6f5ed91ab0a89e098de5` |
| 高位 D15 `volume_range_breakout_v2_high_position_improvement_audit_detail_latest.csv` | `30e9be57e9f4d5456cb57255ff0d181c5a1da5b1246ff91a6c14e5aef9b0c941` |
| 原 D10 admission `volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv` | `46ec3908143b2e89720ca23b3c90a2cb253655b3f72084374c8f04032218294e` |

低位選取原 `model_id=volume_range_breakout_v2_low_position_volume_attack` 的全部 26 筆；
高位選取原高位 artifact 中 `base_model_member=True` 的全部 231 筆。
這是原 artifact 已標記的研究集合，不重算選股條件或正式買入排名。

## 獨立入口

- 低位 audit：`scripts/audit_volume_v2_low_position_d15_reconciliation.py`
- 低位獨立 validator：`scripts/validate_volume_v2_low_position_d15_reconciliation.py`
- 高位 audit：`scripts/audit_volume_v2_high_position_d15_reconciliation.py`
- 高位獨立 validator：`scripts/validate_volume_v2_high_position_d15_reconciliation.py`

兩模型各自維護判斷，不共享 business helper；validator 不 import audit、producer 或正式業務函式，
而是從原 bytes 自行核 hash、原列、D10 admission 與 D15 closed-interval overlap。
validator 的獨立性限於這項歷史日期事實，不能延伸為策略正確、PIT、報酬或正式持倉的獨立證明。

receipt 保存來源整體 SHA、artifact version、每筆原事件身份、CSV logical record number（含表頭）、
原始所有欄位及 canonical JSON row SHA，並保留空白報酬與任何原未決標記。
原 D10 `same_stock_non_overlap_included=True` 必須逐筆存在且身份日期一致。
同日開盤進場與前單同日收盤出場屬重疊；釘選來源重現低位 1 對、高位 5 對。

## 執行與寫入界線

例如低位（高位使用對應獨立檔名）：

```powershell
python scripts/audit_volume_v2_low_position_d15_reconciliation.py --repo-root . --output F:/CodexStorage/retained-evidence/taiwan-stock-recommendation/model-evidence-integrity-repair-20261026/volume-reconciliation/low-position-d15-reconciliation.json
python scripts/validate_volume_v2_low_position_d15_reconciliation.py --repo-root . --receipt F:/CodexStorage/retained-evidence/taiwan-stock-recommendation/model-evidence-integrity-repair-20261026/volume-reconciliation/low-position-d15-reconciliation.json
```

`--output` 必填，拒絕 repo 內輸出，使用 exclusive create，不能覆寫既有證據。
本案本機保留證據目錄是上列 `volume-reconciliation`；PR／main 驗證可在各自的
`RUNNER_TEMP` 建立一次性 receipt。這些 receipt 均不供模型或正式 consumer 讀取。
來源或 schema 錯誤返回 1，不產可通過核對的 receipt。

預設 exit 0 僅表示 `audit_record_complete=True`、事實記錄完整；**不表示持倉 parity 通過**。
四個入口的 `--require-formal-position-parity` 都返回非零（2），
因為本工具未核對正式確認發布、買入排名及跨三個 volume 模型的單股持倉競合。
receipt 永遠明列：

- `formal_publication_parity_verified=False`
- `formal_position_parity_verified=False`
- `promotion_allowed=False`
- `return_evidence_allowed=False`

正式 adapter 在確認日即由 active 壓制新 confirmed，出場當日仍可能 active；
不能把這裡只觀察研究 entry/exit 的重疊判斷直接當正式持倉重放。
這次只修補「D10 admission 被誤解為各期間持倉皆不重疊」的證據界線，
不取消原核准、不更新 canonical pin，也不宣稱上線模型已可靠。
