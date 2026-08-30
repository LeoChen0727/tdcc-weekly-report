# revenue_unreacted_range / source_mid_falling frozen-rule launch evidence v1

日期：2026-08-30

授權：`user_authorized_4A_4C_20260830`

evidence version：`revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830`

## 結論與使用邊界

這組 evidence 以已凍結且不得調參、不得重選樣的 53 筆歷史 operation rows，補做三項
model-specific 檢查：時序穩定性、同期間對照敏感度、交易成本敏感度。它支持的精確結論是：

```text
launch_evidence_status=provisional_backtest_supported_oos_unconfirmed
gross_chronological_status=positive_all_thirds
transaction_cost_status=robust_declared_grid
relative_edge_status=weak_and_time_unstable
regime_coverage_status=limited_no_range_or_high_risk
```

歷史 gross return 在三個時序區段均為正，且在已宣告的交易成本 grid 下仍為正；但相對同期
市場的優勢集中在較晚區段，早期區段落後市場。同日 `source_low_falling` 對照只有七組，平均
差為負而中位數略為正，因此只能當 sensitivity，不能宣稱穩健的獨立超額報酬證據。樣本也
沒有 `range_bound` 或 `high_risk` regime。這些限制不得被隱藏或改寫成 fully OOS confirmed。

本 evidence component 自身不授予任何 production 權限：

```text
evidence_permission_status=evidence_only_no_permission_grant
formal_model_use_allowed=False
approved_for_daily=False
presentation_allowed=False
production_allowed=False
```

正式 adapter、approval、runtime、Daily Full 與 PDF 整合必須由其各自 contract 另行明確
綁定與驗證；不得把本 evidence artifact 單獨當成 permission source。

## 凍結模型與樣本 identity

- `model_id=revenue_unreacted_range`
- `rule_spec_id=revenue_unreacted_range_source_mid_falling_d30_v1`
- `rule_canonical_sha256=1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633`
- source：`output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_v3_20260829.csv`
- `source_artifact_version=low_mid_falling_candidate_v3_20260829`
- `source_canonical_lf_sha256=7dc4f1f89a16dd77d39af175de1dfd3340059a863a670c77e0276d8ec91582d7`
- `source_artifact_canonical_sha256=24d9900c956273ba72c5f9f2d3e2b77be3bea201c4f2996b9e4ea782d67e2b3a`
- `source_candidate_row_set_sha256=f91dd55cab602224011fc68b65dcb4e7dfb59b7720fb1cce0941941234c78c93`
- lifecycle：`rearm_after_realized_exit_next_trade_day`
- confirmation：`delayed_next_close_continuation_bonus`
- variant：`absolute_or_two_month_yoy_ge15`
- membership：`mid_falling_member=True` 且 `primary_included=True`
- 固定 operation count：53；trigger span：2025-10-28 至 2026-05-26
- `sample_selection_policy=fixed_preselected_no_reselection`

任何條件、門檻、operation identity、entry/exit date、row SHA 或 53 筆 membership 的改變，
都不是這個 v1 evidence 的重跑；必須建立另一個 append-only evidence version。

## 時序穩定性

53 筆先依 `trigger_date`、`operation_key` 排序，再用 outcome-independent equal-count 切成
18／18／17 三段。切段後不得移動 rows 或依績效重切：

| 時序區段 | n | 正報酬率 | 平均 gross return | 中位 gross return |
| --- | ---: | ---: | ---: | ---: |
| early | 18 | 72.2222% | 4.5506% | 5.7072% |
| middle | 18 | 77.7778% | 16.6001% | 16.6782% |
| late | 17 | 82.3529% | 24.0425% | 14.1538% |

全樣本 gross return：n=53、正報酬率 77.3585%、平均 14.8950%、中位 9.4077%。
這證明各段 gross 為正，不證明樣本外績效或各市場 regime 都穩定。

## 同期間市場 benchmark

每一筆 operation 先從該股票 `data/stock_price_history/{stock_id}.csv` 的正式 `entry_date`
row 判斷 `TWSE` 或 `TPEX`，再從 `data/market_index_history.csv` 取得同一 index 的：

- benchmark entry：與 operation D+2 `entry_date` 完全相同日期的 index `open`；
- benchmark exit：與 operation D+30 `exit_date` 完全相同日期的 index `close`；
- benchmark return：`exit_close / entry_open - 1`；
- excess return：operation gross return 減 benchmark gross return。

不得使用 nearest-date、as-of fallback、前一交易日、次一交易日或不同 holding dates。53／53
都有 exact-date coverage；其中 52 筆 TWSE、1 筆 TPEX。

全樣本 benchmark outperformance rate 為 50.9434%，平均 excess return 為 2.9800%，中位
excess return 為 0.5765%。分段結果為：

| 時序區段 | n | 超越市場率 | 平均 excess return | 中位 excess return |
| --- | ---: | ---: | ---: | ---: |
| early | 18 | 33.3333% | -3.8632% | -8.4722% |
| middle | 18 | 50.0000% | 0.9467% | 1.5030% |
| late | 17 | 70.5882% | 12.3787% | 4.9823% |

因此 `relative_edge_status=weak_and_time_unstable`，不得只引用 late segment 掩蓋 early
segment，也不得把全期小幅正 excess 解讀為穩健 alpha。

## Market regime coverage

entry-date index regime 使用 frozen index row 的 close、MA20、MA60、20-day return 與
above-MA flags，沒有依結果調參：

```text
strong_bull=31
mild_bull=11
correction=11
range_bound=0
high_risk=0
```

由於 `range_bound` 與 `high_risk` 均沒有樣本，狀態固定為
`limited_no_range_or_high_risk`。它是 post-launch monitoring 必須持續揭露的 coverage gap，
不是重選歷史樣本或調整規則的理由。

## 交易成本敏感度

declared assumptions：

- broker commission：每邊 `0.001425`（0.1425%）；這是保守的明示假設，不宣稱所有券商
  或所有帳戶都收同一費率；
- sell transaction tax：`0.003`（0.3%）；
- slippage：每邊 0 bp、10 bp、25 bp；
- 不另建模券商最低手續費、流動性容量、市場衝擊、融資／借券成本或稅費優惠。

每筆成本後報酬以固定 entry/exit prices 計算：

```text
buy_execution = entry_price * (1 + slippage_each_side)
sell_execution = exit_price * (1 - slippage_each_side)
net_return = sell_execution * (1 - commission - sell_tax)
             / (buy_execution * (1 + commission)) - 1
```

| 每邊 slippage | 正報酬率 | 平均 net return | 中位 net return |
| ---: | ---: | ---: | ---: |
| 0 bp | 75.4717% | 14.2238% | 8.7685% |
| 10 bp | 75.4717% | 13.9956% | 8.5512% |
| 25 bp | 73.5849% | 13.6541% | 8.2261% |

`transaction_cost_status=robust_declared_grid` 只代表上述已宣告 grid 仍為正，不代表任何
交易規模、券商條件或極端流動性環境都已驗證。

## Exact same-date source-low control sensitivity

對照只使用與 treated row 具有完全相同 `trigger_date|entry_date|exit_date` 的
`source_low_falling` rows；不做 nearest-date matching、regression adjustment 或事後配對。
可配對資料只有 7 個 date groups、10 筆 treated、11 筆 comparator：

```text
equal-weight date-group average difference=-13.3660 percentage points
equal-weight date-group median difference=0.8096 percentage points
status=sensitivity_sparse_not_independent
```

這個結果不支持宣稱穩健的 matched-control edge。它保留為如實 sensitivity，且不得用來
新增條件、調門檻、重選樣或否定原本 53 筆 primary metrics。

## Anomaly 與 evidence binding

九筆 anomaly disposition 保留在 primary evidence lineage，並由 producer 與獨立 validator
綁定：

- registry：`config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv`
- `anomaly_registry_canonical_lf_sha256=d56fb059cb008b504cb6f64464277e5252566059512ba723668e3cd5f824d489`
- `anomaly_evidence_binding_set_sha256=8d82f5b691ed676a71ddf4df313e103f4737445549abc9944b876b52354c7f0e`
- 8 筆 `verified_real_extreme` 保留在 primary metrics；
- 6177 為 `verified_data_error`，已完成 source repair 並使用 repaired rerun；
- `effective_anomaly_blocker_count=0`。

validator 逐筆要求 identity/non-overlap、formal operation replay、PIT/calendar、raw lineage、
units/formula/adjustment、authoritative event history、independent corroboration 與 reproducible
reference 都為 `pass`，並重算九份 JSON 的 canonical semantic SHA。只改 disposition 字串而
沒有底層 evidence 不會通過。

## 固定資料範圍與 forward monitoring

模型條件及 evidence 僅使用月營收。EPS、毛利率、營益率、營業利益、業外損益、淨利、
年度與季度財報欄位均不納入條件、分數、ranking、promotion evidence 或本 artifact schema：

```text
financial_statement_scope=monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_non_operating_income_net_income_excluded
```

`forward_holdout_v2` 的用途固定為
`post_launch_monitoring_non_hard_no_tuning`。這組歷史 evidence 不讀 forward holdout 結果，
也不得因未來監控結果反向修改這個 v1 的規則、樣本或歷史 conclusion。

## Immutable artifact family

本 version 只有下列三個 model-owned members：

1. `config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_detail.csv`
2. `config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_matrix.csv`
3. `config/approved_operation_evidence/revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830_manifest.csv`

manifest 固定 detail/matrix 的 canonical-LF byte count、canonical-LF SHA、semantic SHA 與排序後
member bundle SHA：

```text
detail_canonical_lf_sha256=077cbd1da3ed550d4a709d3ba7a2a44acd67b1a2df7ed021b43719fb113a47db
detail_semantic_sha256=e0ee6f4ecfda69dd2c88a2f3feead4bcfe8cd31650776fc5d6e8e32615be36ef
matrix_canonical_lf_sha256=bb4e6520cabccffec4513b2705b0106ec22514ac97cffaceeff9d80824c20cc1
matrix_semantic_sha256=b6d6e6857f16adc947e1c5d551c3e9f8eb9684fd9ac8f4bc276d668b5f2576e4
evidence_payload_bundle_sha256=7fec1b5d38725bef8cad132edade596e858ad759365cbd658a62fc5d46846f3f
```

LF 與完整 CRLF checkout transport 視為相同 canonical bytes；lone CR、非 UTF-8 或任何非換行
byte drift 一律 fail closed。raw Windows working-tree SHA 不作 promotion gate。

## Reproducibility

producer 只建構本模型 versioned evidence family；independent validator 不 import producer、
operation adapter 或 production business semantics：

```text
python scripts/build_revenue_unreacted_range_frozen_rule_launch_evidence.py --check
python scripts/validate_revenue_unreacted_range_frozen_rule_launch_evidence.py
python -m pytest -q tests/test_revenue_unreacted_range_frozen_rule_launch_evidence.py
```
