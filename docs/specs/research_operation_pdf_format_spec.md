# 全模型操作表格 PDF 格式契約

本文件定義 research/backtest 端的操作表格格式預演。這不是正式 daily production PDF，
也不直接修改 daily PDF generator。正式接入前，先用本契約確認所有模型的版面、空表格、
欄位名稱與狀態順序。

輸出檔：

- `output/latest/research_operation_pdf_format_preview_latest.pdf`

## 固定狀態

每個 PDF core model 都必須固定顯示三個表格：

1. `已確認可進場`
2. `操作中`
3. `待確認`

即使沒有資料，也必須保留表格並顯示「目前沒有...資料」或「尚未接入操作回測」。
PDF 不應因為某狀態沒有資料就整段消失。

## 目前接入狀態

- `volume_range_breakout`：已有 research operation preview，可顯示已確認與待確認。
- 其他 PDF core model：先保留固定表格，顯示尚未接入操作回測。
- `操作中`：需有持有追蹤狀態後才能填入；目前先固定空表格。

## 欄位原則

- 停損顯示使用「日期最低價」，例如 `跌破 6/13 最低價 49.00`。
- 報酬顯示使用中文，例如 `中位數報酬`，不可在 PDF 顯示 raw 欄位 `median`。
- PDF 端只讀 research artifact，不在 PDF 端重新判斷買點、停損、持有或出場。
- 尚未接入操作回測的模型，不可用 daily model score 假裝產生操作建議。

## 接入 daily PDF 前條件

- 每個模型要有明確 artifact 來源。
- 已確認、操作中、待確認三個狀態都要有固定資料欄位。
- 空狀態必須可驗證。
- PDF validator 必須抽文字確認固定表格存在。
