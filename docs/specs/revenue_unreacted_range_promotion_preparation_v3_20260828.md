# revenue_unreacted_range promotion preparation v3

日期：2026-08-28
授權：`user_authorized_3A_3C_20260828`

## 不變的模型範圍

- 唯一模型為 `revenue_unreacted_range`／`source_mid_falling` v2。
- 固定使用既有月營收條件、門檻、樣本、進出場與 `D+30` 規則；本契約不新增條件、不調參、不重選樣。
- EPS、毛利率、營益率、營業利益、業外損益、淨利及年度／季度財報欄位均不納入條件、分數或 promotion evidence。
- v1、v2 registry row及 v1→v2 migration 保持 immutable；v3與 v2→v3 migration只允許 append-only。

## 分階段 gate

`scripts/validate_revenue_unreacted_range_promotion_preparation.py` 的預設 phase 是 `research-only`。未顯式傳入 phase 的既有研究 workflow不得因 forward holdout 尚未成熟或 disabled adapter preparation 而失敗。

1. `research-only`
   - 硬 gate：固定模型語意、PIT／lineage、canonical row identity、anomaly retention、artifact ownership邊界及所有 formal／production flags為 false。
   - CLI phase必須搭配 `--source-audit v2` 或 `--source-audit all`；只驗 registry／anomaly不得宣稱完成 research-only gate。
   - non-hard：九筆 anomaly仍未完成 disposition、forward holdout尚未達 20 筆、disabled formal adapter preparation。
2. `promotion-candidate`
   - 增加 hard gate：九筆均須完成 root-cause disposition且不得留有 blocking disposition policy。
   - 增加 hard gate：`forward_holdout_v2` 的 `primary_mature_count >= 20`；bridge、right-censored及未成熟事件必須分開列帳，不得計入 mature結果。
   - `primary_mature_count`只與 `source_mid_falling` primary summary核對；不得與包含 challenger variants的全體 `mature_event_count`或 `holdout_event_count`互相比較。
   - 必須由 `validate_revenue_unreacted_range_forward_holdout_v2.py`完整重播 manifest、detail、summary、comparison、anomaly、append-only histories、source projection及顯式 price bundle；單列自報 manifest不得成為 promotion evidence。
3. `production-pdf`
   - 包含前述全部 hard gates，另須有後續 append-only正式核准、formal adapter readiness及 `pdf_integrated_daily_adapter` consumer契約。
   - `model_operation_readiness_latest.csv`必須包含 `formal_model_use_allowed=True`、`approved_for_daily=True`、`presentation_allowed=True`與 `production_allowed=True`，並綁定 model-owned module、artifact/schema/lifecycle versions及 canonical SHA-256。
   - 必須由 model-owned adapter validator驗證 lifecycle、empty state、uniqueness、同股不重疊及 monotonicity，再通過 canonical readiness與 PDF consumer validators；readiness字串本身不是證據。
   - 目前不存在 `output/latest/daily_revenue_unreacted_range_operation_section_latest.csv`，因此 disabled preparation不得使本 phase通過。
   - 本 phase只做靜態、read-only驗證，不執行 production、Daily Full、PDF renderer或 Apps Script。

## Raw blob與 canonical lineage

`monthly_revenue_history_blob_sha256`只記錄可變原始檔 bytes provenance。CRLF／LF或其他不改變資料語意的 raw-only差異只能產生 diagnostic，不得單獨阻擋研究或 promotion。

下列項目仍為 hard gate：

- canonical monthly-revenue table SHA-256；
- cutoff row count與 cutoff semantic SHA-256；
- qualifying source row canonical SHA-256；
- cross-market resolution canonical SHA-256；
- immutable v1 predecessor、Git blob及 evidence bytes。

## 現況

v3仍固定：

- `formal_model_use_allowed=False`
- `approved_for_daily=False`
- `presentation_allowed=False`
- `production_allowed=False`（disabled preparation readiness contract）
- `production_change=False`

因此目前只完成 research contract分階段化。promotion仍等待九筆 anomaly disposition與 forward holdout自然成熟；production/PDF另等待 formal adapter正式核准及 consumer契約。
