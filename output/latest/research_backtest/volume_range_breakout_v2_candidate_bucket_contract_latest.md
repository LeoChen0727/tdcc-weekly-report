# volume_range_breakout_v2_candidate_bucket_contract

research-only artifact; no production registry change.

Candidate buckets are based on the 120d position-shape matrix under the D+15 close-only next-day continuation baseline.
Sample count is reported as context only and is not a disqualifier.

## Candidate Models

| model_id | model_zh | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | meets_win_return_metric |
|---|---|---:|---:|---:|---:|---:|---|
| volume_range_breakout_v2_low_position_volume_attack | 低位放量攻擊 | 26 | 80.7692 | 19.2308 | 28.7704 | 18.7857 | True |
| volume_range_breakout_v2_mid_position_momentum_attack | 中位動能放量攻擊 | 25 | 80.0 | 20.0 | 12.7599 | 14.6953 | True |

## High Position Rescue/Audit Stratification

High-position stratification rows meeting the metric: 10
High-position buckets remain audit-only until a separate promotion decision.
