# revenue_unreacted_range anomaly disposition v3

## 範圍與結果

本契約只適用於 `revenue_unreacted_range`／`source_mid_falling` v2 的九筆
`unresolved_anomaly_candidate`。模型輸入仍限月營收；EPS、毛利率、營益率、營業利益、
業外損益、淨利及季度／年度財報欄位不得成為條件、分數或 promotion evidence。

九筆操作均逐筆完成 identity／non-overlap、formal operation replay、PIT trading-calendar
continuity、raw-source lineage、單位／公式／調整基礎、官方事件歷史、公開獨立來源佐證及
可重現證據八項查核。結果為：

- 2408、2451、2478、2527、3535（兩筆）、4142、5484 共八筆為
  `verified_real_extreme`，全部保留在 Primary。
- 6177 為 `verified_data_error`，錯誤只在衍生的 episode-level anomaly attribution：
  2025-12 月營收異常的 source table date為 2026-01-17、trade-aligned available date為
  2026-01-19，卻曾被錯誤回填至 2025-12-04 trigger。
  原始月營收、價格、操作 identity、進出價格、報酬、模型條件與門檻均不變。
- 沒有 `verified_non_comparable`、沒有核准排除，也沒有用數值門檻把任何筆數移出 Primary。

6177 只有在 research owner lane 完成固定規則的 v3 trigger-as-of rerun，且
`config/revenue_unreacted_range_anomaly_repair_closure_registry.csv` 對上實際 artifact
canonical semantic SHA、53 筆操作 identity、Primary 指標與修復後八筆 anomaly key-set
後，才視為 anomaly gate 的 effective blocker 已清除。舊 v2 artifact 與九筆 v2 registry
保持 immutable。

## 唯一 canonical gate

`scripts/validate_revenue_unreacted_range_anomaly_dispositions.py` 是本模型 anomaly
disposition 的唯一 canonical gate。promotion validator 與 readiness sync 只能委派此
validator，不得各自複製 disposition/business gate。

Hard gate 綁定：

- evidence JSON 的 `schema_version`、`evidence_id`、`semantic_payload` canonical SHA-256；
- registry 的 canonical columns／rows，排除純 transport provenance 欄位；
- 月營收 cutoff row 的 canonical row SHA-256；
- repaired v3 summary/detail 的 canonical semantic SHA-256；
- 53 筆 operation key、candidate row hashes、Primary 與 sensitivity metric signatures；
- 6177 修復後不再帶 future-contaminated anomaly flag，其他八筆 anomaly identity 不變。

Raw HTTP bytes、local raw-file SHA、Git blob SHA、檔案位元組數與 CRLF/LF 差異只屬
provenance／diagnostic，不能取代或阻擋已一致的 canonical semantic payload。未保存的外部
HTTP response 不得虛構 hash；公開 URL 只作來源與佐證。公開 provider 的分類一律是
`independent_public_provider_corroboration`，且
`independent_underlying_measurement=False`。

## 上線邊界

本階段完成 anomaly disposition 與 research-only 修復 closure，但不是 production approval。
以下權限維持 `False`：

- `formal_model_use_allowed`
- `approved_for_daily`
- `presentation_allowed`
- `production_allowed`

Forward holdout v2 尚需依預註冊規則自然累積到 20 筆成熟 Primary events；bridge、
right-censored 或未成熟事件不得算入。disabled formal adapter preparation 另由 3C
append-only 接續。本變更不得接入 production、Daily Full、PDF、packet 或 Apps Script，
也不得產生正式買賣指令。
