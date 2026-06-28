# W Bottom Right Side Early Entry Operation Spec

This document records the promoted v1 operation evidence for
`w_bottom_right_side`.

Scope:

- `w_bottom_right_side` is the W-bottom right-low / right-side early-entry model.
- It is not the confirmed neckline breakout model.
- It does not change production model conditions, scoring, or ranking.
- Raw research candidate rows remain research-only; formal daily usage must go
  through `approved_operation_patterns_latest.csv`.

Selected candidate:

```text
model_id: w_bottom_right_side
surface_id: w_bottom_right_low_early_entry
selected_segment_id: smooth_core_mainstream_right_rebound_5_20_bull
buy point: next trading day open after the right-low observation signal
evaluation window: 40 trading days
```

Outcome rule:

| outcome | definition |
|---|---|
| win | First close return reaches `>= +10%` within 40 trading days. |
| neutral | Close return first exceeds `+5%`, then returns to `<= +5%` before reaching `+10%`. |
| loss | `+10%` is not reached by day 40; evaluate by day-40 close. |
| incomplete | The event does not yet have enough future trading days to evaluate the 40-day rule. |

Current promoted evidence:

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
| avg_return_pct | 2.9504 |
| median_return_pct | 4.7478 |
| unique_stock_count | 44 |

PDF/reporting boundary:

- `pure_win_rate_pct` is `win_count / (win_count + loss_count)`.
- `neutral_inclusive_success_rate_pct` includes neutral rows and must not be
  labeled as pure win rate.
- D+10/D+20 broad watch statistics must not replace this D+40 operation rule.
