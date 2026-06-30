# price_pullback_23ema Operation Candidate Spec

- model_id: `price_pullback_23ema`
- model_name_zh: 股價回檔模型
- candidate_version: `price_pullback_23ema_operation_candidate_v1_20260630`
- operation_module_id: `price_pullback_23ema_prev20_breakout_stop_v1`
- source_research_artifact: `output/latest/research_backtest/price_pullback_23ema_feature_confirmation_research_latest.csv`
- selected_filter_id: `tdcc_high_thresholds_up_return20_0_25`
- production_status: not approved for daily operation guidance

## 白話定義

這個 candidate 找的是「原本已符合 `price_pullback_23ema` production proxy 的回檔股」，再要求訊號當天同時具備：

1. 大戶 TDCC 高門檻持股增加。
2. 20 日漲幅介於 0% 到 25%，排除已明顯轉弱或過度延伸的股票。

這不是帶量紅 K 模型，也不是大漲後回月線模型。帶量紅 K 與 prior extension 測試目前不升格。

## 操作規則候選

買點：

- `price_pullback_23ema` 訊號成立當天，同時符合 `tdcc_high_thresholds_up_return20_0_25`。
- 下一個交易日開盤買進。

賣點 / 勝利定義：

- 持有期間到 D+20 為止。
- 若盤中高點先突破「訊號日前 20 日高點」，歸類為勝利。

停損 / 失敗定義：

- 停損參考為當下 `MA20` 與 `EMA23` 較低者。
- 若收盤價連續 4 個交易日低於該停損參考 4% 以上，且早於前高突破，歸類為失敗。

和局 / 到期定義：

- 若 D+20 前沒有突破前高，也沒有觸發停損，D+20 收盤報酬率 >= 0% 歸類為和局。
- 若 D+20 前沒有突破前高，也沒有觸發停損，D+20 收盤報酬率 < 0% 歸類為失敗。
- 若同一日 K 棒同時出現 target 與 stop，研究輸出歸類為 `same_day_unresolved`。

## Research Evidence

Selected candidate row:

| metric | value |
| --- | ---: |
| selected_stock_days | 11,606 |
| selected_unique_stocks | 1,304 |
| mature_count | 5,141 |
| win_count | 3,423 |
| neutral_count | 287 |
| failure_count | 1,431 |
| win_rate_pct | 66.58 |
| neutral_rate_pct | 5.58 |
| failure_rate_pct | 27.84 |
| avg_d20_close_return_pct | 3.06 |
| median_d20_close_return_pct | 0.83 |
| avg_realized_return_pct | 1.28 |
| avg_realized_or_d20_days | 9.82 |

Baseline replay reference:

| metric | value |
| --- | ---: |
| mature_count | 261,695 |
| win_rate_pct | 41.32 |
| neutral_rate_pct | 12.87 |
| failure_rate_pct | 45.81 |
| avg_realized_return_pct | 0.38 |
| avg_realized_or_d20_days | 12.49 |

Delta vs baseline:

| metric | value |
| --- | ---: |
| win_rate_delta_pct | +25.26 |
| failure_rate_delta_pct | -17.97 |
| avg_realized_return_delta_pct | +0.90 |
| avg_realized_or_d20_days_delta | -2.67 |

## Governance Boundary

This spec does not change:

- `scripts/build_daily_candidate_model_layer.py`
- production selection conditions
- production scoring
- production ranking
- `config/stock_model_contract_registry.csv` input/output contract

This candidate remains blocked from daily operation guidance until exact daily candidate row parity is completed and a separate explicit promotion/sync PR opens `approved_for_daily=True`.
