# PR 繼承緊急休市來源驗證

本控制由 `repo_infrastructure` 維護，只供 PR 判斷既存來源狀態是否可合法繼承。
它不宣告來源 ready、不發布快照、不產生 PDF、不改選股或操作條件，也不提供模型績效或升級證據。

只有 `market_session_status=closed_emergency` 可以進入新增分支；`closed_scheduled`、缺值、其他市場狀態與新增來源錯誤均不適用。
既有 historical replay 分支及正式 runtime validators 保留原行為。
`scripts/pr_inherited_market_closure.py` 是兩個 PR wrapper 共用的低階來源身分及不可變性檢查，不解讀任何模型條件。

## 不可變的來源與權威證據

下列 13 個依賴必須保有可驗證的 Git blob 身分、基準繼承關係及工作目錄內容；僅允許 LF/CRLF 差異。
禁止替換來源、重寫 release manifest、任意清空 freshness 或藉 sparse checkout 跳過證據。
稀疏工作目錄缺檔時仍須核對 Git/index 與 skip-worktree 身分；不得發動網路擷取補足證據。

1. `output/latest/market_session_status_latest.json`
2. `output/latest/data_freshness_latest.csv`
3. `output/latest/data_freshness_latest.md`
4. `output/latest/daily_authority_release_latest.json`
5. `data/market_calendar/exceptional_non_trading_days.csv`
6. `config/twse_non_trading_days.csv`
7. `scripts/daily_authority_release.py`
8. `scripts/market_session_calendar.py`
9. `build_data_freshness_latest.py`
10. `config/external_data_source_contract.csv`
11. `.github/workflows/daily_full_pipeline.yml`
12. `scripts/validate_daily_publish_freshness_gate.py`
13. `scripts/validate_repo_advanced_integrity.py`

還須核對緊急休市官方來源身分、日期與時間順序、release ID/base commit、三個 manifest surface 的 SHA-256、行事曆及前一交易日。
新 PR 不得把休市狀態改成 ready，或用服務失敗替代官方休市證據。

## 精確 runtime 錯誤邊界

advanced-integrity wrapper 必須先通過全部 static contracts，並只觀察以下四項未變更的 runtime 錯誤，才可考慮繼承。
缺少、重複、替換來源或多出任何錯誤都拒絕。

```text
external source official_daily_price readiness report_ready is not True
external source daily_stock_monitor readiness report_ready is not True
external source all_candidates readiness report_ready is not True
external source daily_pdf_source readiness daily_pdf_ready is not True
```

snapshot wrapper 同樣只可繼承既有 `report_ready=False` 的指定錯誤：

```text
report_ready must be True before publishing model snapshots; observed=False
```

來源身分、價格日期、發佈快照或其他正式檢查失敗仍必須阻擋；正式 validator 在相同未 ready 狀態仍失敗。

## PR 控制差異與獨立授權

PR 可新增已註冊且無寫入權限的驗證程式、測試及說明文件；既有 inventory 只可增加精確的驗證執行或 lineage 參照。
不得刪除既有 row、修改 owner/status/用途、增加資料讀寫或 production stage 權限，亦不得由本 PR 自寫 lifecycle 授權 migration。
新增 workflow step 必須無條件使用 bash 及 `set -euo pipefail`，只執行明確的 validator/audit/pytest 文法；audit receipt 必須逐一獨立驗證。
不得修改既有 steps、permissions、triggers 或 jobs；scope detector 只可擴充實際變更或可證明與 base 相同的精確 validation 路徑。既有 routes 與 routing 函式必須保持相同。

`trust-root-maintenance-approved` maintainer label 由 **base-owned** trust-root guard 獨立檢查；新增 closure module 也納入受保護控制範圍。
本 PR 不得靠 head 版本自行授權其 wrapper 或 module，不改 repository ruleset、required checks、branch protection 或 maintainer approval 規則。
CI 中 snapshot wrapper 的 pin 必須符合該檔案 canonical LF SHA-256。

## 回歸與結果解讀

實作入口為 `scripts/validate_repo_advanced_integrity_pr_safe.py` 與
`scripts/validate_daily_published_model_snapshots_pr_safe.py`；兩者呼叫上述低階 closure module，snapshot wrapper 也委託 advanced-integrity wrapper 檢查控制差異。
指定回歸檔案為：

- `tests/test_pr_inherited_market_closure.py`
- `tests/test_repo_advanced_integrity_pr_safe.py`
- `tests/test_daily_published_model_snapshots_pr_safe.py`
- `tests/test_repo_production_inventory.py`
- `tests/test_daily_model_maintenance_pr_validation_workflow.py`

`repo_current_contracts` 必須無條件執行 closure、兩個 PR wrapper、production inventory 及 workflow wiring 的針對性回歸。
正向測試證明合法的原封不動休市來源可由 PR 繼承；反向測試須拒絕權威證據、來源、runtime 錯誤、inventory 權限、workflow 與 scope 漂移。
回歸通過僅表示 PR 控制邊界驗證通過；不等於自然日 Daily Full、正式來源 ready、PDF 驗收或模型可靠性驗證完成。
