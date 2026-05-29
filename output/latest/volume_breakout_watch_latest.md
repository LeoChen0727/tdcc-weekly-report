# Volume Breakout Watch

- generated_at: `2026-05-29 19:28:38 Asia/Taipei`
- main_price_date: `20260528`
- total_watch_rows: `1`
- priority_distribution: `{'D_risk_downgrade': 1}`
- type_distribution: `{'volume_expansion_watch': 1}`
- scope_distribution: `{'volume_attack': 1}`
- selection_status_distribution: `{'not_selected_by_candidate_model': 1}`

## Interpretation

- `strict_60d_volume_breakout` is the strict breakout bucket used by the original breakout list.
- `platform_volume_breakout`, `neckline_volume_breakout`, and `right_side_volume_attack` are volume-confirmed attacks that may be routed to range rebound or pattern watch instead of strict breakout.
- Loose event types are broad recall rows. They intentionally catch early W-bottom/right-side/platform setups, then rely on score, TDCC, repeat appearance, and overheat risk for ranking.
- This list is a visibility and backtest layer. It is not a standalone buy list.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7716 | 昱臺國際 | volume_expansion_watch | volume_attack | D_risk_downgrade | not_selected_by_candidate_model |  |  |  |  |  | 1.8657 | 2.834 | -0.7813 | 1.3264186695920888 | not_in_candidate_model/false_breakout_risk | risk first: avoid chasing until heat/TDCC/repeat risk improves |

