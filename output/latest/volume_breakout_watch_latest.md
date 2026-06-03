# Volume Breakout Watch

- generated_at: `2026-06-04 01:48:37 Asia/Taipei`
- main_price_date: `20250711`
- total_watch_rows: `1`
- priority_distribution: `{'B_confirm_needed': 1}`
- type_distribution: `{'neckline_volume_breakout': 1}`
- scope_distribution: `{'confirmed_attack': 1}`
- selection_status_distribution: `{'not_selected_by_candidate_model': 1}`

## Interpretation

- `strict_60d_volume_breakout` is the strict breakout bucket used by the original breakout list.
- `platform_volume_breakout`, `neckline_volume_breakout`, and `right_side_volume_attack` are volume-confirmed attacks that may be routed to range rebound or pattern watch instead of strict breakout.
- Loose event types are broad recall rows. They intentionally catch early W-bottom/right-side/platform setups, then rely on score, TDCC, repeat appearance, and overheat risk for ranking.
- This list is a visibility and backtest layer. It is not a standalone buy list.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2888 | 新光金 | neckline_volume_breakout | confirmed_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 6.5454 | 4.8889 | 0.0 | 2.67565803785077 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |

