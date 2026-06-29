# W Bottom Right Side Early Entry Operation Spec

本文件記錄 `w_bottom_right_side` 的正式 W 底右低點早期進場操作規則與 PDF
標題下方 evidence 口徑。

## Scope

`w_bottom_right_side` 是 W 底右低點 / 右側成形早期進場模型，不是頸線突破模型。

這個模型的目的，是在第二個低點已形成、右側開始往上時提早觀察或進場。已經
帶量突破頸線的股票，應歸到 `neckline_volume_breakout_confirmation`，不能混在
這個模型裡。

本次 v2 只更新正式操作規則與 evidence 口徑：

- 不修改 `cond_w_bottom_right`。
- 不修改 `score_w_bottom`。
- 不修改 ranking / scoring。
- 不把 raw research candidate rows 寫回 production baseline。

## Production Model Boundary

目前 production detector 的硬性形狀條件仍維持不變：

```text
left peak -> first low -> neckline -> second low -> current right-side rebound
```

主要條件摘要：

| rule | production treatment |
|---|---|
| second-low gap | hard gate: `-3%` to `+6%` versus the first low |
| right-side rebound | hard gate: current close is `3%` to `15%` above the right low |
| second-arc volume | hard gate: second arc average daily volume is at least `1.2x` the first arc baseline |
| long-position context | hard gate: current close is at or below the recent `252` trading-day median, with at least `180` valid close rows |
| W continuity | hard gate: connected swing sequence; repeated undercuts or faded right side are rejected |
| neckline distance | score/risk only; being closer to the neckline is not an entry gate |
| low-position percentile | score/risk only; lower position scores better, higher position is penalized |
| second-arc red-candle ratio | score bonus when the second arc has a higher red-candle ratio than the first arc |

## Evidence Sources

正式 operation v2 evidence 來源：

1. `output/latest/research_backtest/w_bottom_early_entry_stop_loss_audit_latest.csv`
2. `output/latest/research_backtest/w_bottom_early_entry_stop_loss_audit_detail_latest.csv`
3. `output/latest/research_backtest/w_bottom_early_entry_candidate_spec_latest.csv`
4. `output/latest/research_backtest/w_bottom_early_entry_parameter_grid_latest.csv`
5. `docs/latest/daily_candidate_model_parameters_latest.csv`

正式 daily/PDF consumer 只能讀 approval/readiness artifact，不得直接把 raw research
candidate rows 當成 production baseline：

```text
approved_operation_patterns_latest.csv
model_operation_readiness_latest.csv
```

## Approved Candidate

```text
model_id: w_bottom_right_side
operation_module_id: w_bottom_early_entry_operation_v2
approval_version: w_bottom_early_entry_operation_v2_20260629
selected_segment_id: smooth_core_mainstream_right_rebound_5_20_bull
production_readiness: approved_operation_v2
```

Segment 定義：

```text
Market regime is strong_bull or mild_bull;
effective_mainstream_label = core_mainstream;
slope_curvature_category = smooth_rounded_w_like;
signal_rebound_from_right_low_pct is 5 to 20.
```

`signal_rebound_from_right_low_pct` 是訊號收盤價相對右低點的反彈幅度，不是頸線距離，
也不是事後報酬。

## Buy / Stop / Exit

買點：

```text
Buy next open after the right-low observation signal.
```

停損：

```text
Sell on close when price breaks the W-structure low.
W-structure low = min(detected left-low price, detected right-low price).
```

出場：

```text
If D+20 close return >= +10%, exit on D+20 close.
Otherwise hold to D+40 close, unless the W-structure-low close stop fires first.
```

這套規則全部使用開盤買進與收盤出場，不使用盤中最高價當作規則。

## Outcome Metrics

目前採用的 operation v2 統計：

| metric | value |
|---|---:|
| sample_size | 44 |
| evaluated_sample_size | 31 |
| mature_sample_size | 31 |
| positive_count | 18 |
| neutral_count | 0 |
| loss_count | 13 |
| stop_count | 10 |
| incomplete_count | 13 |
| positive_return_rate_pct | 58.0645 |
| avg_return_pct | 11.2532 |
| median_return_pct | 6.2374 |
| min_return_pct | -12.7202 |
| unique_stock_count | 44 |

定義：

```text
positive_return_rate_pct = positive_count / evaluated_sample_size
avg_return_pct = average exit return under the W-structure-low stop plus D+20/D+40 exit rule
```

`positive_return_rate_pct` 不是舊 v1 的 `+10%` 勝率，也不是含平局成功率。若 PDF
標題下方要寫「勝率」，必須同時說明它是「D+20/D+40 操作正報酬率」。

## PDF Header Evidence Rule

PDF 標題下方建議顯示：

```text
操作正報酬率: 58.1%
平均報酬: 11.25%
中位報酬: 6.24%
最低報酬: -12.72%
買進: 右低點觀察訊號後，下一個交易日開盤買進
停損: 收盤跌破 W 結構低點出場
出場: D+20 收盤若已達 +10% 出場，否則持有到 D+40 收盤
樣本: 44，已評估 31，正報酬 18，負報酬 13，停損 10，未成熟 13
```

如果 PDF 同時顯示 D+10 / D+20 broad watch 統計，必須標成次要觀察數據，不得混入
operation v2 的主勝率 / 主報酬行。

## Promotion Boundary

Raw research candidate rows 維持 research-only：

```text
approved_for_daily: false
production_readiness: not_production_ready_research_only
```

正式 production 使用狀態：

```text
research_baseline_status: production_parity
research_baseline_parameter_set_id: w_bottom_early_entry_operation_v2
production usage: approved_operation_patterns_latest.csv only
raw candidate rows: advisory-only
```

## Forbidden Shortcuts

- 不得把 `positive_return_rate_pct` 簡寫成未定義的泛用勝率。
- 不得用盤中最高價統計冒充收盤出場規則。
- 不得把 raw research candidate rows 直接 promote 到 production baseline。
- 不得把 W 底早期進場合併進頸線突破模型。
- 不得把 D+10 / D+20 broad watch stats 當成 W 底早期進場的主 operation evidence。
- 不得在 evidence-display-only 變更中偷改 scoring / ranking。

## Required Validation

正式 promotion PR 至少要跑：

```text
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_daily_pdf_contract_consumers.py
python scripts/validate_research_against_stock_model_contract.py
python scripts/validate_daily_model_research_parity.py
python scripts/validate_repo_semantic_integrity.py
```

本模型還需要 operation/readiness 相關驗證：

```text
python scripts/validate_approved_operation_patterns.py
python scripts/validate_model_operation_readiness.py
python -m pytest tests/test_approved_operation_patterns.py tests/test_daily_model_parameter_recommendations.py tests/test_model_operation_readiness.py -q
```
