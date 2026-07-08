# volume_range_breakout v2 split feature audit contract

Status: research-only.

This contract governs `volume_range_breakout_v2_split_feature_audit`.
It does not change production model gates, ranking, scoring, operation
contracts, stock model registry rows, packet behavior, or PDF behavior.

## Source Population

The artifact must consume:

```text
output/latest/research_backtest/volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv
```

Only rows with:

```text
same_stock_non_overlap_included=True
```

may enter the split feature audit detail. Event-level repeated same-stock active
windows are forbidden in this artifact.

The validator must fail if the detail contains same-stock active-window overlap
pairs. The historical `8454` overlap case is a regression fixture: if it exists
in the source, only one accepted row may remain in this artifact.

## Required Split

The artifact must split the accepted non-overlap population into:

```text
low_base_consolidated
momentum_continuation
```

`low_base_consolidated` is the current research proxy for the user's low-base
consolidation idea:

```text
low_base_loose_flag=True AND consolidated_any_flag=True
```

`momentum_continuation` is the complement. It must not be described as the same
model semantics as low-base consolidation.

## Required Analysis Surfaces

The summary CSV must include these row types:

```text
group_baseline
success_common_feature
failure_common_feature
discriminative_feature
candidate_condition_matrix
numeric_success_failure_gap
anomaly_check
```

Every row that discusses a successful common feature must include failure-side
evidence:

```text
failure_with_feature_count
failure_share_pct
failure_common_flag
```

This prevents win-rate-only or success-only interpretation.

The artifact must also include return distribution fields beyond win rate:

```text
neutral_rate_pct
loss_rate_pct
avg_return_pct
median_return_pct
high_return_ge10_rate_pct
loss_le_minus5_rate_pct
```

## Technical Analysis Fields

The detail CSV must include signal-day or earlier technical-analysis fields,
including at least:

```text
close_location_pct
signal_body_return_pct
confirm_vs_signal_close_pct
hist_ma20
hist_ma60
hist_ma120
hist_ema23
dist_ma20_pct
dist_ma60_pct
dist_high60_pct
close_gt_ma20
close_gt_ma60
ma20_gt_ma60
```

These fields are advisory feature diagnostics only. They cannot become
production gates, scores, risk tags, or operation rules without a separate
promotion PR.

## Candidate Matrix Boundary

Candidate matrix rows must use only these statuses:

```text
research_only_candidate
research_only_risk_tag_candidate
rejected_as_hard_gate_candidate
```

Any production-facing status is forbidden. The artifact must always keep:

```text
approved_for_daily=False
production_readiness=not_production_ready_research_only
```

## Promotion Boundary

This artifact can support discussion of `volume_range_breakout` v2 semantics.
It is not promotion evidence by itself. Any hard gate, score, deduct item, risk
tag, model split, operation contract, daily adapter, or PDF presentation change
requires a separate promotion review and production PR.
