# price_pullback_23ema Operation Candidate Spec

- model_id: `price_pullback_23ema`
- model_name_zh: 股價回檔模型
- candidate_version: `price_pullback_23ema_operation_candidate_v1_20260630`
- operation_module_id: `price_pullback_23ema_prev20_breakout_stop_v1`
- source_research_artifact: `output/latest/research_backtest/price_pullback_23ema_feature_confirmation_research_latest.csv`
- selected_filter_id: `tdcc_high_thresholds_up_return20_0_25`
- production_scoring_policy_id: `price_pullback_loose_gate_tdcc_return20_score_v2_20260630`
- production_scoring_status: `promoted_for_scoring_only`
- discussion_status: `discussion_ready_pending_latest_research_frame`
- production_status: not approved for daily operation guidance

## 白話定義

這個 candidate 找的是「股價回到 23EMA 或近端支撐附近，但均線/短線動能還沒有轉弱的股票」。production proxy 條件是：

1. `near_ema23_or_support`：收盤價距 23EMA 約 -2.5% 到 +5%，或貼近平台低點 / 近 20 日低點支撐。
2. `ema23_slope_proxy_up`：MA5 或 MA10 轉上，或 EMA23 斜率向上，或收盤仍在 EMA23 上方，或 EMA23 未明顯跌破 MA20。

operation candidate v1 不是直接把所有 production proxy 訊號都買進，而是在 production proxy 上再要求訊號當天同時具備：

1. 大戶 TDCC 高門檻持股增加。
2. 20 日漲幅介於 0% 到 25%，排除已明顯轉弱或過度延伸的股票。

這不是帶量紅 K 模型，也不是大漲後回月線模型。帶量紅 K 與 prior extension 測試目前不升格。

目前這份 spec 的用途是開始模型決策討論，不是 production promotion。

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

Scoring promotion v2 changes:

- `scripts/build_daily_candidate_model_layer.py`: `score_pullback()` keeps the loose `cond_pullback` gate and adds price-pullback-only TDCC / 20-day-return scoring.
- `config/stock_model_contract_registry.csv`: `price_pullback_23ema` contract_version moves to `v2` and records TDCC 400/1000 columns as scoring inputs.

This spec still does not change:

- production selection conditions
- PDF layout
- other model scoring profiles
- operation approval status

This candidate remains blocked from daily operation guidance until latest research-frame freshness is complete and a separate explicit promotion/sync PR opens `approved_for_daily=True`. The v2 scoring promotion only changes ranking order inside the existing loose `price_pullback_23ema` candidate universe.

## Daily Row Parity Audit

The research pipeline writes `output/latest/research_backtest/price_pullback_23ema_daily_row_parity_latest.csv` and validates it with `scripts/validate_price_pullback_daily_row_parity.py`.

Current discussion-readiness evidence:

- 10 published daily snapshots are covered: `20260615`, `20260616`, `20260617`, `20260618`, `20260622`, `20260623`, `20260624`, `20260626`, `20260629`, `20260630`.
- All 10 snapshots have dated `all_candidates/source-row` replay.
- All 10 snapshots have `candidate_universe_replay_exact_match`.
- Published-not-replayed rows: `0`.
- Replayed-not-published rows: `0`.
- Remaining blocker: `20260630` is still missing from the research frame, so production guidance remains blocked even though daily production row replay is exact.

## Discussion Agenda

The next model decision should discuss these items explicitly:

1. Required entry filter: whether v1 should use only `tdcc_high_thresholds_up_return20_0_25`, or add revenue / technical / market-background gates.
2. Revenue treatment: whether revenue should be a hard gate, a score boost, or only a risk note.
3. Entry timing: keep `signal_date_next_open` after the production proxy plus chosen entry filter, or require same-day confirmation.
4. Exit target: keep prior 20-day high as the first v1 target, since wider prior-high windows have not shown a better decision advantage.
5. Stop rule: keep consecutive close-based failure logic to avoid 23EMA intraday stop sweeps; current candidate uses 4 consecutive closes below the lower of MA20/EMA23 by 4%.
6. Neutral/failure rule: keep D+20 no-hit positive return as neutral, D+20 no-hit negative return as failure.
7. Ranking/scoring: decide only after entry/exit/stop are agreed; do not silently reuse scoring from the other three completed models.
