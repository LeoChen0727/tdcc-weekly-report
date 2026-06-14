# 放量攻擊操作研究 artifact 規格

本文件定義 research/backtest 產出的放量攻擊操作研究表。它不是 standalone PDF 報告，也不取代正式每日台股推薦 PDF。

正式 daily PDF 若接入本 artifact，只能在 `model_id=volume_range_breakout` 的模型區塊中呈現，不得改動其他模型的表格、欄位或操作文字。

## 輸出檔

- `output/latest/volume_breakout_operation_pdf_preview_latest.csv`
- `output/latest/volume_breakout_operation_pdf_preview_latest.md`

不再輸出 `volume_breakout_operation_pdf_preview_latest.pdf`。完整 PDF 呈現由 daily production 的 `scripts/generate_chatgpt_side_daily_reports.py` 負責。

## 基本原則

- artifact 只包含 `model_id=volume_range_breakout`。
- 進場基準以「確認後下一交易日開盤」呈現。
- 停損基準用日期最低點，例如 `跌破 6/13 最低價 49.00`。
- 統計欄位使用中文，例如 `中位數報酬`，不得露出 `median`、`signal_low`、`next_open` 等 raw token。
- 所有 row 都是 research-derived，不自動 approved 到 daily production。
- daily production 可讀取本 CSV/MD 做 PDF 呈現，但不得在 PDF 端重新計算買點、停損、排序或跨模型套用。

## 區段

### 已確認操作

用於顯示已滿足 confirmation rule 的放量攻擊股票。

必要欄位：

| 欄位 | 說明 |
|---|---|
| `model_id` | 固定 `volume_range_breakout` |
| `pdf_view` | `highlight` 或 `full` |
| `pdf_section` | `confirmed_operation` |
| `display_order` | 顯示順序 |
| `stock_id` / `stock_display` | 股票代號與顯示文字 |
| `trigger_zh` | 確認觸發方式 |
| `entry_basis_zh` | 買進基準 |
| `entry_price_status_zh` | 進場價狀態 |
| `stop_basis_zh` | 停損基準 |
| `exit_rule_zh` | 賣出/出場規則 |
| `sample_size` | 回測樣本數 |
| `win_rate_zh` | 勝率 |
| `avg_return_zh` | 平均報酬 |
| `median_return_zh` | 中位數報酬 |
| `confidence_zh` | 信心狀態 |
| `pdf_note_zh` | pattern 分類摘要 |

### 待確認

用於顯示尚未完成 confirmation rule，但仍在觀察期限內的放量攻擊股票。

必要欄位：

| 欄位 | 說明 |
|---|---|
| `pdf_section` | `pending_confirmation` |
| `pending_age_zh` | pending 天數 |
| `pending_group_zh` | pending 群組 |
| `pending_confirmation_zh` | 等待確認條件 |
| `same_stock_pending_count` | 同股票 pending 訊號數 |

### 操作中

目前 research artifact 尚未輸出操作中 row。正式 daily PDF 可以保留「操作中」空表格並顯示目前無資料，但不得硬生假持有資料。

## Daily PDF 接入限制

- 只讀最新 artifact，不阻塞 daily pipeline。
- 若 artifact 缺失或為空，daily PDF 仍需完成。
- 欄位顯示只限放量攻擊模型。
- 其他模型不得共用放量攻擊的進場、停損、賣出規則。
