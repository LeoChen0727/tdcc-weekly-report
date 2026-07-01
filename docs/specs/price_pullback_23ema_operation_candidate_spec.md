# price_pullback_23ema Operation Candidate Spec

- model_id: `price_pullback_23ema`
- model_name_zh: `股價回檔模型`
- candidate_version: `price_pullback_23ema_operation_candidate_v1_20260630`
- operation_module_id: `price_pullback_23ema_prev20_breakout_stop_v1`
- source_research_artifact: `output/latest/research_backtest/price_pullback_23ema_feature_confirmation_research_latest.csv`
- selected_filter_id: `tdcc_high_thresholds_up_return20_0_25`
- discussion_status: `discussion_ready_research_only`
- production_status: `not approved for daily operation guidance`

## 白話定義

`price_pullback_23ema` 目前研究中的 v1 候選，是在找「股價回到 23EMA 或支撐附近，但結構還沒有壞掉」的股票。它不是突破追價模型，也不是營收模型。

正式候選條件分兩層：

1. 先有 production proxy 訊號：股價接近 23EMA 或支撐，且 EMA23 / MA 結構仍偏向上或至少未破壞。
2. 再加上 v1 研究濾網：同日大戶高門檻籌碼增加，且 20 日漲幅介於 0% 到 25%。

`帶量紅K` 目前不是 v1 必要條件。研究結果顯示它可以提高勝率，但報酬率與樣本效率沒有優於目前 v1 候選，因此只能保留為 research-only 觀察項，不可直接升格為 production gate。

## 操作定義

買點：

- 訊號日同時符合 `price_pullback_23ema` production proxy 與 `tdcc_high_thresholds_up_return20_0_25`。
- 訊號日後的下一個交易日開盤買進。
- 不是每天隔日開盤買；必須先有訊號日條件成立。

賣點：

- D+20 內，盤中高點先突破訊號日前 20 日高點，視為 win。
- 已測過更長前高視窗；目前沒有比 20 日前高提供更好的決策優勢，v1 先保留 20 日前高。

停損 / failure：

- 使用 `MA20` 與 `EMA23` 較低者作為結構參考。
- 若收盤價連續 4 個交易日低於該參考線 4% 以上，視為 failure stop。
- 這是刻意放寬的收盤確認邏輯，用來避免市場盤中掃 23EMA 停損造成過早出場。

和局：

- D+20 內沒有觸發 target 或 stop，且 D+20 close return >= 0%，視為 neutral。
- D+20 內沒有觸發 target 或 stop，且 D+20 close return < 0%，視為 failure。
- 同一根日 K 同時首次看到 target 與 stop，標為 `same_day_unresolved`，不當作明確勝敗。

## Research Evidence

Selected candidate row:

| metric | value |
| --- | ---: |
| selected_stock_days | 11,908 |
| selected_unique_stocks | 1,315 |
| mature_count | 5,398 |
| win_count | 3,608 |
| neutral_count | 289 |
| failure_count | 1,501 |
| win_rate_pct | 66.84 |
| neutral_rate_pct | 5.35 |
| failure_rate_pct | 27.81 |
| avg_d20_close_return_pct | 2.99 |
| median_d20_close_return_pct | 0.73 |
| avg_realized_return_pct | 1.24 |
| avg_realized_or_d20_days | 9.71 |
| avg_days_to_win | 5.93 |
| avg_days_to_failure | 16.80 |

Baseline replay reference:

| metric | value |
| --- | ---: |
| selected_stock_days | 299,969 |
| mature_count | 263,065 |
| win_rate_pct | 41.37 |
| neutral_rate_pct | 12.86 |
| failure_rate_pct | 45.76 |
| avg_realized_return_pct | 0.39 |
| avg_realized_or_d20_days | 12.48 |

Decision interpretation:

- v1 候選相對 baseline 提高 win rate 約 25.47 個百分點。
- failure rate 約下降 17.95 個百分點。
- avg realized return 只提升約 0.85 個百分點，所以這不是大波段高報酬模型，而是提高短線命中率與降低失敗率的回檔模型。
- 平均決策天數約 9.71 天，比 baseline 約 12.48 天短，時間成本有下降。

## Parity Status

`price_pullback_23ema_daily_row_parity_latest.csv` 目前有 10 個 published daily snapshots exact pass：

- `20260615`
- `20260616`
- `20260617`
- `20260618`
- `20260622`
- `20260623`
- `20260624`
- `20260626`
- `20260629`
- `20260630`

所有 10 個日期的 production all_candidates/source-row replay 都是 exact match，published/proxy row gap = 0。

`20260630` 的 `outcome_research_frame_has_date=False` 是正常現象，因為最新訊號日還沒有足夠 D+20 outcome；但 `source_row_research_frame_has_date=True`，所以它可用於 as-of daily row parity，不應再被視為 latest research frame freshness blocker。

## PDF / Operation Adapter Boundary

本模型目前不得接入 PDF operation section，也不得產生 production 買進、賣出、停損或排名操作建議。

若未來要升格為第 4 個完整正式模型，promotion PR 必須同時補齊：

- formal daily operation-row producer / adapter artifact。
- adapter schema，至少能提供 `本日可買 / 已確認買入候選`、`操作中`、必要 empty-state、row status、entry date/price、stop reference、exit rule、holding days、report line、PDF buy eligibility。
- validator，確認 PDF renderer 只消費 adapter 欄位，不自行推論 23EMA lifecycle rows。
- digest PDF 僅顯示兩張主表：`本日可買 / 已確認買入候選` 與 `操作中`。
- 沒有可買列時，第一張表格內顯示 `本日無股票推薦`。
- 沒有操作中列時，第二張表格內顯示 `目前無操作中追蹤列`。
- `待確認` 只能在 full-list 且 adapter 明確提供時呈現。
- `已失效` / `已出場` 只能留在 audit/lifecycle artifact，不放 digest PDF 主表。

PDF renderer 不得從 23EMA candidate signals 自行推論 buy / active / pending / exit rows。

## Governance Boundary

這份 spec 不改：

- production selection conditions
- production scoring
- production ranking
- PDF layout
- `config/stock_model_contract_registry.csv`
- research variant into production baseline

目前 production model source 仍是 `scripts/build_daily_candidate_model_layer.py` 的 `cond_pullback` / `score_pullback`；本 spec 只說明 research-only operation candidate 與 promotion 前置條件。

目前 row parity validator 是 `scripts/validate_price_pullback_daily_row_parity.py`；它必須區分 outcome research frame maturity 與 production all_candidates/source-row replay freshness。

目前 readiness 應維持：

- `approved_for_daily=False`
- `presentation_allowed=False`
- `operation_directive_level=no_operation_directive`
- `pdf_integration_status=blocked_promotion_pr_and_daily_operation_adapter_required`
- `packet_integration_status=blocked_promotion_pr_and_daily_operation_adapter_required`

## Discussion Agenda

下一步模型決策應明確討論：

1. v1 必要條件是否採 `tdcc_high_thresholds_up_return20_0_25`，或放寬成籌碼加分。
2. `OBV / MACD / KD / RSI` 應作為必要條件、加分、扣分，或只作風險標籤。
3. 45 日型態只可作 23EMA 專用客觀價格背景，不可偷用 W-bottom 的 45 日語意。
4. 營收目前缺完整 point-in-time panel，不可當必要 gate；若要使用，需先補 revenue panel + validator。
5. 大盤背景可用 shared objective panel，但要定義如何對 TWSE / TPEX / stock market 做 point-in-time join。
6. 是否接受 avg realized return 不高、但 win rate / failure rate / time cost 改善的模型定位。
7. 若決定 promotion，必須另開正式 promotion PR，同步 contract、adapter、PDF consumer validator、research/backtest parity 與 post-merge Daily Full Pipeline。
