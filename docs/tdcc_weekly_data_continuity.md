# TDCC Weekly Data Continuity Contract

PR 內的 continuity 程式變更由唯讀 workflow `.github/workflows/tdcc_weekly_pr_validation.yml` 驗證；它不產生、不提交也不推送正式 artifact。合併後仍必須執行 main 的 `.github/workflows/tdcc_weekly.yml`，以官方來源完成實際回補、衍生欄位重算與正式週報交付。

初次週六 dispatch 會把 Asia/Taipei 當日寫入 `target_as_of_date`；後續 retry 固定沿用該值，因此即使來源延遲跨週也不會自行滑到下一個報告週。

## 歷史資料層與回測

- `output/history/tdcc/tdcc_holder_ratio_YYYYMMDD.csv` 是逐期全市場 canonical fact snapshot，回測必須以這一層的正式期別為基礎。
- `data/tdcc_stock_history_raw/{stock_id}.csv` 保存官方級距原始列；`data/tdcc_stock_history/{stock_id}.csv` 是依 canonical snapshots 重建的個股衍生特徵，不是獨立事實來源。
- 目前沒有以 SQLite、DuckDB 或 Parquet 取代上述 canonical history。現有回測可直接讀逐期 snapshot；未來若新增 DuckDB/Parquet，只能是可由 canonical history 重建的分析加速層，不能掩蓋缺期或改寫官方期別。

## 目的

TDCC 週報必須先取得該報告週由 TDCC 官方查詢頁公布的資料期別，再補齊該期以前的必要歷史資料，最後才可計算籌碼變化與產生 PDF。電腦日期、既有 PDF、舊 snapshot 或檔名都不是正式期別來源。

## 正式流程

`.github/workflows/tdcc_weekly.yml` 的順序固定為：

1. `scripts/tdcc_weekly_data_readiness.py`：依 Asia/Taipei 判定 target week，要求 TDCC 官方查詢頁至少出現一個位於該週的正式日期。
2. `tdcc_holder_ratio_top10.py --fetch-only`：抓取全市場最新資料，且資料日期必須等於 readiness 選出的正式日期。
3. `scripts/repair_tdcc_weekly_history_continuity.py`：以最新 snapshot 股票集合檢查自 `20260430` 全市場完整 baseline 起的所有官方期別，逐檔回補缺少的正式歷史列。
4. `tdcc_holder_ratio_top10.py --build-only`：只使用相鄰官方期別計算週變化與連續增加。
5. `scripts/build_tdcc_stock_history.py` 與 `scripts/validate_tdcc_weekly_history_continuity.py`：重建個股歷史，驗證 `change_1w` 與 streak 沒有跨過缺期。
6. 上述 gate 全部通過後，才可繼續建立候選資料、PDF、Pages mirror 與 output commit。

## 延後發布與自動重試

週六外部 Apps Script 仍是初次派送來源。若官方新期別尚未公布、全市場 source 尚未切換到該期，或歷史回補遇到暫時性錯誤，workflow 會在命名的資料步驟失敗，不會沿用舊 snapshot。

既有 `orchestrateTdccIndividualRefresh` 每 5 分鐘檢查該 run。它只對以下 allowlist 步驟排定 30 分鐘後重試：

- `Wait for expected TDCC period`
- `Fetch current TDCC snapshot`
- `Repair TDCC weekly history continuity`

重試沒有固定次數上限；一旦資料 gate 通過，流程恢復正常並在 main 發布後才派送 downstream individual refresh。其他程式、renderer、validator 或 git publish 失敗仍是 terminal failure，不會被誤當成資料延遲無限重試。

外部 Apps Script 的正式部署內容必須與 `docs/apps_script_workflow_trigger.gs` 一致，並重新執行 `installAllWorkflowTriggers` 或至少確認 `orchestrateTdccIndividualRefresh` 的 5 分鐘 trigger 存在。

## 計算契約

- `change_1w` 只能比較官方日期序列中緊鄰的兩期。
- `change_2w` 與 `change_3w` 必須分別找到官方序列中前 2、前 3 期的同一股票資料。
- 任一必要期別缺少該股票且沒有明確 `official_no_data` 證據時，該衍生值不得產生。
- `tdcc_consecutive_up_weeks` 遇到官方期別缺列時必須停止，不得跨缺期延續。
- 單一股票經官方查詢連續三次都無資料，可記錄為 `official_no_data`；無效的單一持有人占比資料可記錄為 `invalid_holder_distribution`。兩類歷史例外合計若超過當期股票數 1%（至少 5 檔），視為系統性來源異常並阻擋整份週報。

## 2026-07-09 事件

2026-07-10 因颱風休市，該週正式 TDCC 日期為 `20260709`。舊流程只保留 80 檔的該期歷史，導致 `20260717` 對部分股票直接比較 `20260703`，卻標為一週變化。本契約要求先補入 `20260709`，再重算 7/9 與 7/17 的變化、同步門檻與連續週數。
