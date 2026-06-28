# W Bottom Right Side Early Entry Operation Spec

This document records the promoted v1 production operation rule and PDF evidence
display rule for `w_bottom_right_side`.

The promotion PR that owns this spec changes the formal W-bottom early-entry
production surface: it tightens the W-bottom detector, adds the W-bottom
arc-volume / red-candle / long-position fields to the contract, and registers
`w_bottom_early_entry_operation_v1` as the model's operation contract. Raw
research rows remain advisory-only; the production approval path is the explicit
approval artifact described below.

## Scope

`w_bottom_right_side` is the W-bottom right-low / right-side early-entry model.
It is not the confirmed neckline breakout model.

The model is intended to find stocks after the second low has formed and the
right side has started to rise, before the neckline breakout is confirmed.

The confirmed W-bottom neckline breakout belongs to
`neckline_volume_breakout_confirmation` with a W-bottom subtype. That surface
must keep a separate entry point, outcome rule, and evidence line.

## Production Model Boundary

The v1 production detector is intentionally separate from the neckline-breakout
model. Its hard entry shape requirements are:

```text
left peak -> first low -> neckline -> second low -> current right-side rebound
```

Current production thresholds:

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

This model must stay pre-breakout. If the stock has already entered a confirmed
neckline-breakout state, it belongs to `neckline_volume_breakout_confirmation`,
not `w_bottom_right_side`.

## Current Evidence Sources

Use these evidence sources in this order:

1. Research candidate spec:
   `output/latest/research_backtest/w_bottom_early_entry_candidate_spec_latest.csv`
2. Research parameter grid:
   `output/latest/research_backtest/w_bottom_early_entry_parameter_grid_latest.csv`
3. Production broad parameter snapshot:
   `docs/latest/daily_candidate_model_parameters_latest.csv`

The production broad parameter snapshot is not the primary operation evidence
for W-bottom early entry. It currently labels `w_bottom_right_side` as
`intraday_target_watch` and warns that high-return / high-hit metrics should
not be presented as close-hold win rate.

Therefore the daily PDF model header must not mix the broad D+10/D+20 watch
statistics with the W-bottom early-entry operation rule unless the labels make
the distinction explicit.

## Selected Research Candidate

Promoted selected candidate:

```text
model_id: w_bottom_right_side
candidate_status: current_best_research_candidate
selected_segment_id: smooth_core_mainstream_right_rebound_5_20_bull
approved_for_daily: true through approved_operation_patterns_latest.csv
production_readiness: approved_operation_v1
```

Segment definition:

```text
Market regime is strong_bull or mild_bull;
effective_mainstream_label = core_mainstream;
slope_curvature_category = smooth_rounded_w_like;
signal_rebound_from_right_low_pct is 5 to 20.
```

Important interpretation:

```text
signal_rebound_from_right_low_pct means the signal close is 5% to 20% above the
detected right-low price. It is not neckline distance and not realized return.
```

## Buy Point And Outcome Rule

Buy point:

```text
Buy next open after the right-low observation signal.
```

Evaluation window:

```text
Within 40 trading days after entry.
```

Win / neutral / loss rule:

| outcome | definition |
|---|---|
| win | First close return reaches `>= +10%` within 40 trading days. |
| neutral | Close return first exceeds `+5%`, but later returns to `<= +5%` before reaching `+10%`. Neutral rows are excluded from pure win/loss. |
| loss | `+10%` is not reached by day 40; evaluate by day-40 close. |
| incomplete | The event does not yet have enough future trading days to evaluate the 40-day rule. |

This rule uses close prices, not intraday high prices.

## Current Research Statistics

Current research candidate statistics from
`w_bottom_early_entry_candidate_spec_latest.csv`:

| metric | value |
|---|---:|
| sample_size | 44 |
| evaluated_sample_size | 31 |
| mature_sample_size | 20 |
| win_count | 13 |
| neutral_count | 11 |
| loss_count | 7 |
| incomplete_count | 13 |
| pure_win_rate_pct | 65.0000 |
| neutral_inclusive_success_rate_pct | 77.4194 |
| total_sample_win_or_neutral_rate_pct | 54.5455 |
| incomplete_rate_pct | 29.5455 |
| avg_return_pct | 2.9504 |
| median_return_pct | 4.7478 |
| unique_stock_count | 44 |

Definitions:

```text
pure_win_rate_pct =
  win_count / (win_count + loss_count)

neutral_inclusive_success_rate_pct =
  (win_count + neutral_count) / (win_count + neutral_count + loss_count)
```

Neutral and incomplete rows must not be hidden. If the PDF shows the inclusive
success rate, it must also state that neutral rows are included and incomplete
rows are excluded.

## PDF Header Evidence Rule

The W-bottom early-entry model header may show this evidence block under the
model title:

Preferred Traditional Chinese display:

```text
純勝率: 65.0%
含和局成功率: 77.4%
平均報酬: 2.95%
評估期: D+40
買進: 右低點觀察訊號成立後，下一個交易日開盤買進。
出場: 40 個交易日內收盤報酬先達 +10% 記為勝。
和局: 曾超過 +5%，但未達 +10% 前又回到 <= +5%，記為和局。
失敗: 未達 +10% 者，以 D+40 收盤評估。
樣本: 44；已評估 31；成熟樣本 20；勝 13；和局 11；敗 7；未成熟 13。
```

The label must not simply say "勝率 77.4%". The 77.4% value is an inclusive
success rate, not pure win rate.

If D+10 / D+20 statistics are also displayed, they must be shown as secondary
watch statistics, not as the operation rule:

```text
D+10 / D+20 觀察統計 from daily_candidate_model_parameters_latest.csv
```

Do not merge D+10 / D+20 watch metrics into the D+40 operation win-rate line.

## Promotion Boundary

Raw research candidate rows remain research-only:

```text
approved_for_daily: false
production_readiness: not_production_ready_research_only
```

Formal daily production usage is approved only through:

```text
approved_operation_patterns_latest.csv
model_operation_readiness_latest.csv
```

The promotion/sync PR must:

1. Update the formal operation evidence registry or readiness artifact used by
   daily PDF consumers.
2. Keep `w_bottom_right_side` separate from
   `neckline_volume_breakout_confirmation`.
3. Update `config/stock_model_contract_registry.csv` and
   `config/daily_model_condition_spec.csv` when the production contract surface
   or operation contract changes.
4. Keep research/backtest advisory output out of production baseline unless the
   PR is explicitly a promotion/sync PR.
5. Make the PDF display source explicit so the PDF layer does not invent or
   recalculate win-rate text.

## Forbidden Shortcuts

- Do not call inclusive success rate "win rate".
- Do not use intraday high statistics as close-return win rate.
- Do not promote raw research candidate rows directly into production baseline;
  production usage must go through the approved operation artifact.
- Do not hide scoring/ranking changes inside an evidence-display-only change.
  Any future scoring/ranking change must be explicit and must update contracts
  and parity evidence.
- Do not fold W-bottom early entry into the neckline breakout model.
- Do not use D+10 / D+20 broad watch statistics as the primary W-bottom
  early-entry operation evidence.

## Required Validation For A Promotion PR

When a formal promotion PR changes production model, operation, or PDF consumer
behavior, run at minimum:

```text
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_daily_pdf_contract_consumers.py
python scripts/validate_research_against_stock_model_contract.py
python scripts/validate_daily_model_research_parity.py
python scripts/validate_repo_semantic_integrity.py
```

Because this promotion changes the formal production model surface and operation
contract, repository lifecycle, production inventory, model-surface, operation
readiness, and focused unit tests should also pass before the PR is marked ready
for review.
