# 放量攻擊操作表格契約

本文件先定義 research/backtest 產出的 PDF preview 表格，不直接修改 daily PDF。
daily PDF 之後若要接入，應只讀 preview 欄位，不在 PDF 端重新判斷買點、停損、排序或英文代碼翻譯。

## 共同規則

- 只使用 `volume_range_breakout` 現行模型命中後的研究結果。
- 已確認操作的進場基準固定為「確認後下一交易日開盤」。
- 停損顯示必須用日期最低點，例如 `跌破 6/13 最低價 49.00`。
- 不使用 `訊號 K 低點`、`signal_low`、`median` 等內部或英文顯示文字。
- `中位數報酬` 是同類歷史樣本依同一套進場、停損、出場規則跑完後的報酬中位數。
- `歷史勝率` 是同類歷史樣本中，完整操作後報酬率大於 0 的比例。
- 所有欄位仍是 research-derived，不代表已正式 approved 到 daily production。

## 精華版 confirmed 表

用途：放量攻擊模型中，已完成確認且歷史證據正向的隔日操作參考。

篩選：

- `歷史樣本數 >= 10`
- `歷史勝率 >= 50%`
- `中位數報酬 > 0`
- `研究排序分數 > 0`
- 依 `operation_rank` / `ranking_research_score` 排序
- 最多 10 檔；若符合條件少於 5 檔，就只顯示實際符合檔數

欄位：

| 欄位 ID | 中文欄名 | 範例 |
|---|---|---|
| `display_order` | 顯示順序 | `1` |
| `stock_display` | 股票 | `2243 宏旭-KY` |
| `operation_status_zh` | 操作狀態 | `已確認` |
| `trigger_zh` | 確認型態 | `隔日續強確認` |
| `entry_basis_zh` | 進場基準 | `確認後下一交易日開盤` |
| `stop_basis_zh` | 停損基準 | `跌破 6/11 最低價 30.30` |
| `exit_rule_zh` | 出場規則 | `先跌破停損基準出場，否則進場後第 10 個交易日收盤出場` |
| `sample_size` | 歷史樣本數 | `12` |
| `win_rate_zh` | 歷史勝率 | `66.67%` |
| `avg_return_zh` | 平均報酬 | `+21.67%` |
| `median_return_zh` | 中位數報酬 | `+21.09%` |
| `confidence_zh` | 信心等級 | `低` |

## 完整版 confirmed 表

用途：完整列出當天 confirmed operation rank。

篩選：

- 全部 confirmed rows
- evidence 正向與否由 `quality_status_zh` 顯示

## pending 表

用途：今天或最近 10 個交易日內進入放量攻擊模型，但尚未確認隔日續強、回測 5MA 或回測 10MA 的股票。

顯示原則：

- PDF preview 先以股票去重；同一股票只顯示最新有效 pending 訊號。
- `same_stock_pending_count` 顯示同股仍有幾筆有效 pending 訊號。
- raw pending 明細仍留在 `volume_breakout_pending_operation_queue_latest.csv`。

欄位：

| 欄位 ID | 中文欄名 | 範例 |
|---|---|---|
| `stock_display` | 股票 | `3285 微端` |
| `operation_status_zh` | 操作狀態 | `待確認` |
| `pending_age_zh` | 等待天數 | `D+2，剩 8 個交易日` |
| `pending_group_zh` | 待確認分組 | `D+2-D+5 等回測 5MA/10MA` |
| `stop_basis_zh` | 停損基準 | `跌破 6/11 最低價 41.40` |
| `pending_confirmation_zh` | 等待確認 | `等待隔日續強 / 回測 5MA / 回測 10MA` |

## holding 表

holding 需要 daily production 有持有追蹤狀態後才可正式接入。

建議欄位：

| 欄位 ID | 中文欄名 | 範例 |
|---|---|---|
| `stock_display` | 股票 | `2243 宏旭-KY` |
| `entry_date_zh` | 進場日 | `6/15 開盤` |
| `holding_age_zh` | 持有天數 | `已持有 D+3，剩 7 個交易日` |
| `stop_basis_zh` | 停損基準 | `跌破 6/11 最低價 30.30` |
| `planned_exit_zh` | 預定出場 | `進場後第 10 個交易日收盤` |

在 holding 狀態尚未接入前，PDF preview 不應硬生假持有表。
