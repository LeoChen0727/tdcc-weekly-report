# Apps Script GitHub Actions Trigger

這份文件保存 Google Apps Script 觸發 GitHub Actions 的標準版本。

正式程式碼：

- `docs/apps_script_workflow_trigger.gs`

## 必要設定

Apps Script 不要把 GitHub token 寫死在程式碼裡。請在 Apps Script 專案設定新增 Script Property：

```text
GITHUB_PAT=<your GitHub token>
```

Token 權限：

- Fine-grained token：Repository 選 `LeoChen0727/tdcc-weekly-report`
- Repository permissions：`Actions` 設為 `Read and write`
- Metadata 會自動是 read

如果使用 classic token，private repo 通常需要 `repo` scope。

## 可執行函式

```text
testGithubTokenAndWorkflowAccess
triggerDailyStockMonitor
triggerDailyFullPipeline
triggerTdccWeeklyReport
```

`triggerDailyStockMonitor` 會觸發 `daily_full_pipeline.yml`，用來保留既有 Apps Script 每日台股推薦標的排程。

`triggerDailyFullPipeline` 是同一件事的別名，方便手動測試。

## 驗收方式

1. 在 Apps Script 執行 `testGithubTokenAndWorkflowAccess`
2. 開啟 Apps Script 執行紀錄
3. 確認 log 出現：

```text
Status code: 200
GitHub token and workflow access OK.
```

4. 執行其中一個 trigger function
5. GitHub Actions 對應 workflow 頁面應該要在幾秒內出現新的 run

## 判讀錯誤碼

```text
200 / 201 / 202 / 204 = GitHub 接受請求
401 = token 錯誤、過期或已被撤銷
403 = token 權限不足，常見是缺 Actions read/write
404 = token 看不到 repo 或 workflow，或 workflow 檔名錯
422 = ref 或 payload 錯誤
```

舊版 Apps Script 使用 `muteHttpExceptions: true` 但沒有丟錯，會造成 Apps Script 顯示成功、GitHub Actions 卻沒有真的被觸發。新版會在非成功狀態碼時直接 `throw Error`，讓觸發失敗可以被看見。
