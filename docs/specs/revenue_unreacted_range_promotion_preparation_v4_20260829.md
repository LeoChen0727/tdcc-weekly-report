# revenue_unreacted_range promotion preparation v4

日期：2026-08-29
授權：`user_authorized_3A_3C_20260829`

## 模型與資料邊界

- 唯一模型範圍為 `revenue_unreacted_range`／`source_mid_falling`；條件、門檻、樣本、進出場與 `D+30` 規則均未變更。
- promotion evidence 僅使用月營收與既有價量 operation replay。EPS、毛利率、營益率、營業利益、業外損益、淨利及年度／季度財報欄位不納入條件、分數或 evidence。
- `low_mid_falling_candidate_v3_20260829` 只修復 trigger-as-of anomaly attribution；53 筆 operation business projection與 Primary metrics均與 v2 相同。
- v1、v2、v3 decision與既有 migration immutable；v4與 v3→v4 migration為 append-only。

## Anomaly gate 結論

- 九筆 candidate均完成 identity/non-overlap、formal operation replay、PIT/calendar、raw lineage、units/formula、authoritative event history、independent public-provider corroboration與 reproducible evidence八項查核。
- 八筆 disposition為 `verified_real_extreme`，保留於 Primary metrics；排除版本只屬 sensitivity。
- 6177為 `verified_data_error`，錯誤僅存在於衍生 attribution future leakage。修復後 operation business fields變更數為0、Primary metrics不變、anomaly attribution row-set改變，且未把 202512/20260119 的 future source納入 20251204 trigger-as-of attribution。
- 最新 effective anomaly blocker為0；目前八筆 current anomaly rows均是已驗證且保留的 real extremes，不是 unresolved blockers。

## Promotion與production邊界

- `research-only` 更新與 disabled adapter preparation為 non-hard gate。
- promotion candidate仍需 `forward_holdout_v2` 依預註冊規則自然成熟至20筆；bridge、right-censored與未成熟事件不得納入正式結果。
- formal production approval仍是 hard gate；目前 adapter尚未完成，因此 `formal_model_use_allowed=False`、`approved_for_daily=False`、`presentation_allowed=False`、`production_change=False`。
- 本階段不執行 production、Daily Full、PDF、packet renderer或 Apps Script，也不產生正式買賣指令。

## Canonical identity

- anomaly disposition、evidence、repair closure與 migration由 `scripts/validate_revenue_unreacted_range_anomaly_dispositions.py` 單一 canonical gate驗證。
- promotion hard identity使用 canonical semantic SHA、cutoff/row count、canonical monthly-revenue row hashes、canonical candidate row hashes與 repaired-rerun equality/difference bindings。
- raw HTTP/file/blob SHA、byte count及 CRLF/LF差異僅為 provenance diagnostic，不得單獨阻擋 promotion。
