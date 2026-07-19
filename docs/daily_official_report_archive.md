# Daily Official Report Verified Archive

此 contract 僅管理 `chatgpt_side_outputs_official` 內的每日正式報告日期 bundle。
TDCC weekly、individual-stock、其他 `output/history` 與 PDF 內容均不在此範圍。

## Retention Authority

程式不得依電腦日期推定報告日期。

- `current` 來自同一個 immutable `origin/main` commit 的
  `output/latest/report_manifest_latest.json` 與
  `output/latest/data_freshness_latest.csv`。兩者日期必須一致，正式 readiness
  欄位也必須全部通過。
- `baseline` 是 source family 中緊鄰 `current` 的前一個日期 bundle；其
  `chatgpt_daily_report_runtime_manifest.json` 與六份 PDF contract 必須通過。
- 只有早於 `baseline` 的完整日期 bundle 可進入 archive selection。
- current 與 baseline 絕不刪除。指定 `--include-date` 也不能繞過此限制。

只接受 PDF、PNG、CSV、JSON。reparse point、unsupported 或 unlisted 檔案、
authority 衝突、current/baseline 缺件都會 fail closed。

## Command Modes

預設只驗證與產生 readiness evidence，不複製也不刪來源：

```powershell
python scripts/archive_daily_official_report_bundles.py `
  --repo-root . `
  --authority-ref origin/main `
  --source-root C:\Users\p4693\Documents\Codex\projects\taiwan-stock-recommendation\production\tdcc-daily-production\chatgpt_side_outputs_official `
  --destination-root F:\CodexStorage\report-archive\taiwan-stock-recommendation `
  --expected-destination-volume F: `
  --execution-report-dir C:\Users\p4693\Documents\Codex\workspace_admin\reports
```

`--copy` 只做非破壞性 copy/verify。它不刪除、搬移、改名或改寫任何 C 槽
來源。`--move-after-verify` 才啟用 verified-transfer；兩個參數互斥。可用
`--include-date YYYYMMDD` 將執行限制在已被 retention authority 判定為 eligible
的日期。

獨立驗證 repository contract：

```powershell
python scripts/validate_daily_official_report_archive_contract.py
```

repository 不硬編碼 F 槽 runtime dependency。operator 必須傳入 absolute
destination root 與 expected volume。程式會驗證 root 分離、NTFS、可用空間與
reparse 邊界。

## Verified-Transfer Gate

目的結構為：

```text
<destination-root>\daily\<YYYYMMDD>\<bundle-relative-path>
```

每個日期 bundle 必須依序通過：

1. 全 bundle 的 destination collision preflight。
2. 每檔 copy 後 bytes 與 SHA-256 parity；已存在同 SHA 視為 idempotent pass。
3. 寫入 content-digest 綁定且不再改寫的
   `daily_official_report_pre_delete_*.json`。
4. 再次驗證 immutable authority、current/baseline、manifest digest、完整檔案集合、
   source absolute path、非 reparse、bytes/SHA 與 destination parity。
5. 只以 `Path.unlink()` 刪除 manifest 精確列出的 source files。每一檔刪除前都重驗
   路徑、日期、hash 與 destination parity。
6. 全部列檔刪除後，逐層驗證並以 `Path.rmdir()` 移除 bundle 內的空子目錄，最後才
   移除空的日期資料夾；不得對 source root 使用 recursive delete。

任何 bundle 級 pre-delete 條件失敗時，該 bundle 不開始刪除。若逐檔刪除中途失敗，
completion state 為 `partial_source_cleanup`；F 槽資料保留，execution evidence 逐檔記錄
已刪、失敗與未執行狀態，重跑仍以剩餘 source 作新的精確 manifest。
若前次已刪完檔案但空目錄清理失敗，重跑必須先由 F archive index 證明該日期已有
完整 entries、全部 `source_removed=true` 且 destination parity 仍通過，才能只收尾
空目錄。

## Evidence And Canonical Delivery

每次執行都在 execution report directory 寫入：

- `daily_official_report_archive_*.csv`：逐檔 readiness／copy／delete 狀態。
- `daily_official_report_archive_*.json`：authority、fingerprint、manifest/index digest 與
  completion state。
- verified-transfer 額外寫入 immutable
  `daily_official_report_pre_delete_*.json`。

目的 root 以原子更新方式維護
`daily/archive_index_latest.json`。index 只把 F 槽的
`canonical_archive_path` 當交付路徑，包含 report date、artifact type、relative path、
bytes、SHA-256、`source_removed`、`execution_id` 與 `archived_at`。原 C source path 只存在
execution/pre-delete audit lineage，不是 archived artifact 的交付路徑。

## Automation Boundary

本工程變更不新增或修改 automation，`automation_allowed=false`。只有正式 production
全部成功後，才可由 `workflow_automation_maintenance` 另案將
`--move-after-verify` 接入外部自動化；不得在本 PR 直接更動 Daily Full Pipeline、
official PDF entrypoint 或 GitHub Actions。
