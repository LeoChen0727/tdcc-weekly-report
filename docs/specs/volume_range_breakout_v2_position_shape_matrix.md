# volume_range_breakout_v2_position_shape_matrix

This artifact is research-only. It must not change production model registry
rows, daily operation adapters, PDF operation rows, ranking, scoring, or buy
approval gates.

## Scope

The source is
`output/latest/research_backtest/volume_range_breakout_v2_promotion_readiness_audit_detail_latest.csv`
filtered to the current discussion baseline:

```text
holding_days = 15
stop_policy_id = ma20_ema23_close_stop_4d
confirmation_rule_id = next_day_continuation_confirmed_close_only
entry_rule_id = confirmation_next_open
```

This scope represents:

```text
D+15 / close-only next-day continuation / MA20+EMA23 close-confirmed stop
```

## Bucket Axes

The artifact must classify every source event on both position axes:

```text
position_120d
position_240d
```

Position buckets are:

```text
low_pos_le40: position_in_*_range_pct <= 40
mid_pos_40_75: 40 < position_in_*_range_pct <= 75
high_pos_gt75: position_in_*_range_pct > 75
unknown_position: missing or non-numeric position input; kept as an audit bucket
```

Shape buckets are:

```text
wide_range: range_width_60_pct > 80
consolidation: consolidation_type is short_consolidation or long_consolidation
non_consolidation: every remaining assigned row
```

Each row must have exactly one position bucket per position axis and exactly one
shape bucket. No source event may be dropped or assigned to more than one
bucket per position axis.

## Metrics

The matrix reports:

- sample size
- valid and invalid return counts
- win, neutral, and loss counts
- win, neutral, and loss rates
- average and median return
- p10 and p90 return
- stop-exit count and rate
- `meets_win_return_metric`

`meets_win_return_metric=True` means:

```text
win_rate_pct >= 60
avg_return_pct > 0
median_return_pct > 0
```

Sample size is evidence context only. A bucket must not be rejected, hidden, or
excluded only because sample size is small. Rare high-performance buckets remain
visible as research-only candidates for discussion.

## Required Guardrails

The validator must fail when:

- latest/history CSV schemas or row counts diverge
- source event keys are missing, duplicated, or not equal to the source scope
- any position axis does not sum back to the source sample
- any position-shape bucket overlaps with another bucket on the same axis
- `approved_for_daily` is anything other than false
- production decision fields are introduced
- decision text rejects a bucket because of sample count
