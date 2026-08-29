# revenue_unreacted_range promotion preparation v5

日期：2026-08-29  
授權：`user_authorized_3A_3C_20260829`

## 結論

- `decision_id=revenue_unreacted_range_source_mid_falling_promotion_preparation_v5_20260829`
- `contract_version=revenue_unreacted_range_promotion_preparation_contract_v6_20260829`
- `decision_status=promotion_blocked_waiting_forward_holdout_v2_maturity`
- `anomaly_disposition_gate=verified_8_real_extreme_1_data_error_repaired_effective_blockers_0`
- `formal_adapter_gate=disabled_adapter_preparation_validated_non_hard_production_approval_hard_gate`

本版只記錄 disabled adapter preparation 已通過 model-owned schema、empty state、
uniqueness、same-stock non-overlap 與 lifecycle monotonicity 驗證。它仍是 in-memory、
disabled、無 writer、無 runtime artifact、無 PDF／packet consumer 的準備模組，不是正式
production adapter，也不產生買賣、停損、出場或停利指令。

## Append-only 與 business invariants

- v1 至 v4 decision 與既有 migration 均 immutable；v5 與 v4→v5 migration 只能追加。
- v4 與 v5 的模型條件、門檻、月營收邊界、樣本、operation rows、績效、進出場與
  anomaly evidence 全部相同。
- `common_business_field_change_count=0`；v4→v5 的 source artifact version、trusted
  source revision、operation counts 與八筆 current anomaly canonical registry均相同。
- 本版不得新增條件、調整門檻、重新選樣，或使用 forward holdout 結果調參。
- EPS、毛利率、營益率、營業利益、業外損益、淨利及年度／季度財報欄位仍不得納入
  條件、分數、ranking、promotion evidence 或 adapter schema。

## Permission 與上線邊界

Registry 既有 schema 的四個 permission／production 欄位保持：

```text
formal_model_use_allowed=False
approved_for_daily=False
presentation_allowed=False
production_change=False
```

Disabled adapter module 自身的 `production_allowed=False` 亦保持不變；本 migration 不新增
或改名 registry schema 欄位。正式 production approval 仍須未來另一個 append-only contract，
並須通過成熟 forward holdout、正式 adapter/runtime artifact 與相關 production consumer gate。

本階段禁止 production、Daily Full、PDF、packet、runtime artifact 與 Apps Script；不修改
production/PDF/packet renderer，也不接入任何正式 daily workflow。

## Forward holdout

`forward_holdout_v2` 只能依預註冊規則自然累積。bridge、right-censored 與未成熟事件不得
納入正式結果；disabled adapter preparation 完成不會降低 maturity hard gate。

## 驗證

```text
python scripts/validate_revenue_unreacted_range_promotion_preparation.py --phase research-only --source-audit all
python -m pytest -q tests/test_validate_revenue_unreacted_range_promotion_preparation.py
```
