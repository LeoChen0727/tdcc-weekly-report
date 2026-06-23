請用 tdcc-weekly-report 的正式每日台股推薦流程產出報告。這份文件是給新對話的入口規則；不要用舊的 Pages-first 或 repo artifact PDF 流程。

## 正式 PDF 產生入口

正式產出六份 ChatGPT-side PDF 時，只能在固定 daily production worktree 執行：

`C:\Users\p4693\Documents\Codex\2026-06-11\tdcc-daily-production`

先執行 source gate：

`python scripts/run_chatgpt_daily_report_entrypoint.py --source-gate-only`

只有 gate 通過後，才執行正式產生：

`python scripts/run_chatgpt_daily_report_entrypoint.py`

不要直接執行 `scripts/generate_chatgpt_side_daily_reports.py`。那是 renderer，不是正式入口。

## 日期與來源規則

- 不准自己判斷今天日期。
- 正式 report date 只能使用 `origin/main:output/latest/data_freshness_latest.csv` 的 `main_price_date`。
- 必須全部成立才可產出 PDF：
  - `report_ready=True`
  - `warrant_ready=True`, or `warrant_ready=False` only when `warrant_daily_publish_allowed=True` and `warrant_pdf_visibility=hidden_unavailable`
  - `daily_pdf_ready=True`
- If `warrant_pdf_visibility=hidden_unavailable`, do not use old warrant data in the report; treat warrant analysis as unavailable/observe-only.
- source gate 必須用 `git fetch origin main` 與 `git show origin/main:<path>` 讀遠端 main。
- 不准用本機 `output/latest`、OneDrive/helper、GitHub Pages、raw URL cache 或舊 PDF 檔名來決定日期。
- raw / GitHub API / Pages 只能作為人工診斷輔助；如果它們和 `git show origin/main` 不一致，以 `git show origin/main` 為準。

## 必須一致的 structured source

source gate 必須交叉確認以下三份都屬於同一個 `main_price_date`，且 readiness 欄位一致：

1. `origin/main:output/latest/data_freshness_latest.csv`
2. `origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
3. `origin/main:output/latest/chatgpt_daily_report_packet_latest.txt`

任一份讀不到、日期不一致、ready 欄位不一致，都必須停止，不可用舊資料補產。

## 六份正式 ChatGPT-side PDF

正式交付是六份 PDF：

1. 主流股每日推薦精華
2. 主流股完整候選名單
3. 非主流股每日推薦精華
4. 非主流股完整候選名單
5. 權證市場輔助分析
6. 市場風險與大盤期權背景

repo 內 `docs/latest/*.pdf` 或 `output/latest/*.pdf` 是 pipeline artifact / shareable reference，不等於使用者要求的六份 ChatGPT-side PDF。

## PDF 內容邊界

- PDF renderer 只能 render program-side structured artifact。
- 不准在 PDF 端重新計算買點、停損、出場、排名、主流/非主流分類或模型判斷。
- 不准把 pending 股票寫成已確認操作。
- 放量攻擊 operation 只能讀 `output/latest/daily_volume_breakout_operation_section_latest.csv`。
- 其他模型尚未有 approved operation guidance 時，不可把模型命中寫成買進建議。

## 成功輸出證據

正式 entrypoint 完成後，輸出資料夾必須包含：

- 六份檔名含 `<main_price_date>_requested_repo<main_price_date>` 的 PDF。
- `chatgpt_daily_report_runtime_manifest.json`，記錄 `source_ref`、`source_commit_sha`、`main_price_date`、三個 gate 檔與六份 PDF 路徑。

回覆使用者時，要提供可直接開啟的 PDF 資料夾連結與六份 PDF 路徑。
