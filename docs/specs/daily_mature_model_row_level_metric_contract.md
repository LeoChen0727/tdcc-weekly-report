# Daily Mature Model Row-Level Metric Contract

## Scope

This contract applies to these formal operation models:

- `w_bottom_right_side`
- `neckline_volume_breakout_confirmation`
- `price_pullback_23ema`
- `volume_range_breakout_v2_low_position_volume_attack`
- `volume_range_breakout_v2_mid_position_momentum_attack`
- `volume_range_breakout_v2_high_position_volume_attack`

Whole-model baseline performance is model-header evidence. It is not a stock-row
performance metric and must not be used as a fallback inside PDF or packet
operation tables.

## Adapter Fields

Every model-owned operation adapter must expose:

```text
row_metric_status
row_metric_scope
row_metric_id
row_metric_label_zh
row_metric_matched_add_score_ids
row_metric_sample_size
row_metric_win_rate_zh
row_metric_neutral_rate_zh
row_metric_failure_rate_zh
row_metric_avg_return_zh
row_metric_median_return_zh
row_metric_source
row_metric_selection_status
```

`row_metric_status=ready` requires a performance-backed single item or an exact
recomputed combination under the same entry, exit, stop, anomaly-exclusion, and
same-stock non-overlap basis as the model. Win, neutral, and failure rates must
form one mutually exclusive partition and sum to 100% within rounding tolerance.

When no approved performance-backed add-score metric applies, the adapter must
set `row_metric_status=unavailable_no_approved_add_score_metric`. All row-level
metric payload fields remain blank, and `row_metric_selection_status` must state
`baseline_not_permitted_in_operation_row`.

Empty-state rows use `row_metric_status=not_applicable_empty_state`.

## Single And Combination Selection

A single add-score item may use only its own approved same-basis metric. Multiple
matched items may use only the exact recomputed combination for the displayed
feature set. The adapter must not average single-item rates or copy the model
baseline.

If the exact combination is worse than the best matching approved single item on
win rate, average realized return, or median realized return, the adapter must
fall back to that best single item. Sample size is always disclosed but does not
by itself disqualify a rare valid combination.

## Current Model Policies

| model | row-level metric policy |
| --- | --- |
| `w_bottom_right_side` | Existing score components are ranking-only until a same-basis performance package is promoted. Stock-row metric is unavailable. |
| `neckline_volume_breakout_confirmation` | Existing score components are ranking-only until a same-basis performance package is promoted. Stock-row metric is unavailable. |
| `price_pullback_23ema` | `RSI14 >= 60` plus `MACD histogram > 0` uses the approved exact technical package. Base rows are unavailable at stock-row level. |
| `volume_range_breakout_v2_low_position_volume_attack` | Existing score components are ranking-only until separately validated. Stock-row metric is unavailable. |
| `volume_range_breakout_v2_mid_position_momentum_attack` | Existing score components are ranking-only until separately validated. Stock-row metric is unavailable. |
| `volume_range_breakout_v2_high_position_volume_attack` | Approved single metrics and exact recomputed combinations are allowed; a worse combination falls back to the best matching single item. |

## Ownership And Consumers

The model lane owns the adapter fields and their evidence. Current producers are:

- `scripts/build_daily_w_bottom_operation_sections.py`
- `scripts/build_daily_price_pullback_23ema_operation_section.py`
- `scripts/build_daily_volume_breakout_operation_section.py`

The PDF and packet lanes may consume only `row_metric_*`. They must not infer
features from candidate rows, read research detail directly, or fall back to
`win_rate_zh`, `neutral_rate_zh`, `failure_rate_zh`, or `avg_return_zh` inside a
stock row.

The enforcing audit is:

```text
python scripts/build_mature_model_row_level_metric_contract_audit.py
python scripts/validate_mature_model_row_level_metric_contract_audit.py
```

Mature-model audit rows use
`production_readiness=adapter_contract_ready_pdf_packet_consumers_integrated`.
That status is valid only while the audit validator also passes both the PDF
renderer `row_metric_*` consumer guard and the daily packet baseline-fallback
guard. A model adapter alone cannot claim integrated consumer readiness.

Its row artifact is
`output/latest/mature_model_row_level_metric_row_audit_latest.csv`.
