# Volume Breakout Watch

- generated_at: `2026-06-01 22:22:09 Asia/Taipei`
- main_price_date: `20260529`
- total_watch_rows: `2`
- priority_distribution: `{'B_confirm_needed': 1, 'C_watch_only': 1}`
- type_distribution: `{'volume_expansion_watch': 1, 'loose_platform_volume_watch': 1}`
- scope_distribution: `{'volume_attack': 1, 'broad_watch': 1}`
- selection_status_distribution: `{'not_selected_by_candidate_model': 2}`

## Interpretation

- `strict_60d_volume_breakout` is the strict breakout bucket used by the original breakout list.
- `platform_volume_breakout`, `neckline_volume_breakout`, and `right_side_volume_attack` are volume-confirmed attacks that may be routed to range rebound or pattern watch instead of strict breakout.
- Loose event types are broad recall rows. They intentionally catch early W-bottom/right-side/platform setups, then rely on score, TDCC, repeat appearance, and overheat risk for ranking.
- This list is a visibility and backtest layer. It is not a standalone buy list.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6762 | 達亞 | volume_expansion_watch | volume_attack | B_confirm_needed | not_selected_by_candidate_model |  |  |  |  |  | 2.8087 | -6.383 | 18.1208 | 6.200030170463111 | not_in_candidate_model | confirm close above MA20/EMA23 and avoid long upper shadow |
| 2 | 2948 | 寶陞 | loose_platform_volume_watch | broad_watch | C_watch_only | not_selected_by_candidate_model |  |  |  |  |  | 2.2823 | 2.7027 | -0.1314 | 0.8894198858356628 | not_in_candidate_model | broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength |

