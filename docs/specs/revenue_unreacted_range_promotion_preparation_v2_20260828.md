# revenue_unreacted_range promotion-preparation v2 migration（2026-08-28）

## 授權與停止邊界

本次依 `user_authorized_2A_20260828` 只執行 append-only promotion-preparation／anomaly migration，以及 research-only `forward_holdout_v2` migration。禁止 production、Daily Full、PDF、Apps Script；`approved_for_daily=False`、`presentation_allowed=False`、`formal_model_use_allowed=False`、`production_change=False`。

v2 的 `decision_status` 固定為 `selected_pending_anomaly_resolution_forward_holdout_v2_maturity_and_formal_adapter`。這代表本次只準備證據，不能被描述為正式 promotion；剩餘硬阻擋包括 9 筆 anomaly root-cause disposition、6177 trigger-as-of attribution reconciliation、`forward_holdout_v2` maturity，以及 model-owned formal adapter。

本模型仍只使用 point-in-time 月營收與調整後價格。EPS、毛利率、營業利益率、營業利益、業外損益、淨利及其他季／年財報欄位不在範圍內，不得從月營收推論，也不得成為 gate、score、ranking、PDF metric 或 promotion evidence。

## Append-only 契約

- `config/revenue_unreacted_range_promotion_preparation_registry.csv` 的 2026-08-12 v1 row 必須逐欄、順序不變；v2 只能追加在其後。
- v1 anomaly archive `config/revenue_unreacted_range_anomaly_disposition_registry.csv` 維持 exact 8 rows，不改 schema、不覆寫歷史 identity。
- v2 worklist 位於 `config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv`，同 schema、exact 9 rows。分檔是為了避免七個跨版本相同 `operation_key` 被誤判為同一版本內重複。
- `config/revenue_unreacted_range_promotion_preparation_migrations.csv` 精確綁定 v1/v2 decision、trusted Git blobs、source-projection diff/supersede evidence、operation reconciliation 與兩版 anomaly registries。

## v2 選定 slice

選定條件仍為 `absolute_or_two_month_yoy_ge15`、`rearm_after_realized_exit_next_trade_day`、`delayed_next_close_continuation_bonus`、`holding_days=30`、`none_no_stop_reference`、`mid_falling_member=True`、`primary_candidate_retaining`。規則公式與 v1 相同，`rule_formula_sha256=1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633`。

可信來源為 commit `8b72df7090536a49258b7d27192585c3f4b4f75d`：

- summary blob `a3343c5fcf163eda469ee2423d32e6372da14b91`，bytes `54494`，SHA-256 `1268f4bfe825a30ea876cc9eac20800d21802d1fbd212b91ab4829f70752e281`。
- detail blob `656ad7ac399bb93090bb478733c9c0baa1ed6f64`，bytes `1012187`，SHA-256 `0d272c9263b60816cace92f8ed790a1b376cad7952c7ad13a689961cd45920ad`。

v2 主結果為 N=53、48 檔股票、48 episodes、41 勝、0 中立、12 敗；勝率 77.3585%、平均 14.895%、中位數 9.4077%、p10 -11.04%、p90 42.2669%、最小 -19.6694%、最大 82.5095%；`>=20%` 19 筆、`<=-20%` 0 筆。8 筆 source anomaly candidate 加 1 筆 operation-return review candidate 全部保留在 primary metrics；排除 9 筆只能稱 sensitivity analysis。

## v1 → v2 reconciliation

| 項目 | exact count |
|---|---:|
| v1 operations | 52 |
| v2 operations | 53 |
| exact common `operation_key` | 46 |
| raw added keys | 7 |
| raw removed keys | 6 |
| episode identity rekeys | 2 |
| semantic persistent trajectories | 48 |
| true added operations | 5 |
| true removed operations | 4 |
| common-key business-field changes | 0 |

兩個 rekey stock 固定為 `2451` 與 `3665`；它們的 trigger、confirmation、entry、exit、realized return 與 outcome 沒有改變，只是 v2 source projection 修正 episode identity。任何 count 或共同 business field 漂移都必須 fail closed。

source projection evidence 綁定：diff summary SHA-256 `e2124dc58b95ff1e11a7add5bf671ca142b5cc1cc6b538ce57090735d56beeed`、diff detail SHA-256 `68c9cfb143a663bd86f62a356d5dd09cd38edd7e16f2cb726d1a3f4aa62ef4d6`、supersede evidence SHA-256 `33a7ac67a98c0e6fd3836e8bedd250940ccadd567e71c50bb94e9cbda70ef79b`。

## 6177 future leakage

`6177` 的 v2 row 在 trigger `20251204` 前沒有可歸因的 anomalous qualifying source event。published episode-level flag 來自 episode 後續資料；第一個 future anomalous event 是 period `202512`、available date `20260117`、canonical SHA-256 `d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1`，晚於 trigger，不能倒灌成 trigger-as-of attribution。

因此 6177 必須維持：

- `anomaly_attribution_mode=published_episode_level_source_flag_no_trigger_asof_event_requires_reconciliation`
- 四個 source attribution fields 均為 `not_applicable_pending_trigger_asof_reconciliation`
- `pit_calendar_continuity_status=fail`
- `raw_source_lineage_status=fail`
- `final_disposition=unresolved_anomaly_candidate`
- primary metrics 保留、promotion blocked。

## 驗證

一般 validation 驗證 exact two-row decision registry、v1 exact 8、v2 exact 9、migration ledger 與 formal flags。PR validation 使用完整 Git history 執行：

```text
python scripts/validate_revenue_unreacted_range_promotion_preparation.py --source-audit all
python -m pytest tests/test_validate_revenue_unreacted_range_promotion_preparation.py
```

`--source-audit all` 必須分別從 pinned v1/v2 Git blobs 重算 N52/N53 metrics、anomaly SHA binding，並驗證 46/7/6 與 2 rekeys。任何 blob、byte count、SHA-256、ancestry、row set、6177 attribution 或 formal flag 漂移都失敗。
