# Breakout Family Retest Grid

- generated_at: `2026-06-27 16:57:23 Asia/Taipei`
- research_id: `breakout_family_retest_grid`
- parameter_set_id: `breakout_family_retest_grid_20260627`
- detail_rows: `7786`
- production impact: `none`; this grid is advisory-only and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.

## Scope

This grid is no longer limited to W-bottom. It compares broad structured-neckline proxy breakouts, descending-resistance proxy breakouts, and the current bottom/base volume-attack reference family.

First-pass sampling limit: the builder uses the latest daily-price file to keep the top 600 individual stocks by latest trading volume, then scans at most the latest 25 candidate signal days per stock. Use this to compare rule direction before expanding to a heavier full-market replay.

The 20-session line used by the bottom/base volume-attack reference is only a short local base ceiling used as a breakout threshold. It is not a previous-high model definition.

## Entry Definitions

- `direct_breakout_next_open`: buy next open after the breakout signal day.
- `retest_hold_then_attack_next_open`: after the breakout, wait up to 10 trading days for a neckline/resistance retest that does not close below the reference by more than 3%, then buy next open after a renewed attack within 5 trading days.
- Exit: stop if the relevant signal/retest support is broken; otherwise sell at the 10th trading-day close.

## Summary

| event_family_id | pattern_subtype | entry_variant | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct | retest_not_found_count | retest_found_but_no_attack_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | base_attack_position_review | direct_breakout_next_open | 734 | 734 | 30.9264 | 0.4897 | -2.6360 | 153 | 156 |
| bottom_base_volume_attack_reference | base_attack_position_review | retest_hold_then_attack_next_open | 734 | 207 | 48.7923 | 2.7200 | 0.0000 | 153 | 156 |
| bottom_base_volume_attack_reference | low_position_base_attack | direct_breakout_next_open | 395 | 395 | 35.4430 | 1.0828 | -2.8070 | 81 | 98 |
| bottom_base_volume_attack_reference | low_position_base_attack | retest_hold_then_attack_next_open | 395 | 116 | 49.1379 | 3.9508 | 0.0000 | 81 | 98 |
| bottom_base_volume_attack_reference | wide_base_review | direct_breakout_next_open | 339 | 339 | 37.1681 | 1.1342 | -2.9126 | 56 | 61 |
| bottom_base_volume_attack_reference | wide_base_review | retest_hold_then_attack_next_open | 339 | 121 | 44.6281 | 1.4144 | -1.9656 | 56 | 61 |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | direct_breakout_next_open | 1172 | 1172 | 32.8498 | 0.5633 | -2.5210 | 243 | 306 |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | retest_hold_then_attack_next_open | 1172 | 365 | 49.0411 | 1.8955 | -0.2401 | 243 | 306 |
| structured_neckline_volume_breakout_proxy | double_bottom_or_structured_bottom_proxy | direct_breakout_next_open | 51 | 51 | 33.3333 | -1.3421 | -3.6145 | 7 | 12 |
| structured_neckline_volume_breakout_proxy | double_bottom_or_structured_bottom_proxy | retest_hold_then_attack_next_open | 51 | 13 | 23.0769 | -6.9674 | -3.0576 | 7 | 12 |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | direct_breakout_next_open | 1202 | 1202 | 30.2829 | 0.2663 | -2.7067 | 143 | 219 |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | retest_hold_then_attack_next_open | 1202 | 361 | 44.0443 | 1.1027 | -1.7143 | 143 | 219 |

## Direct Entry Only

| event_family_id | pattern_subtype | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | base_attack_position_review | 734 | 734 | 30.9264 | 0.4897 | -2.6360 |
| bottom_base_volume_attack_reference | low_position_base_attack | 395 | 395 | 35.4430 | 1.0828 | -2.8070 |
| bottom_base_volume_attack_reference | wide_base_review | 339 | 339 | 37.1681 | 1.1342 | -2.9126 |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | 1172 | 1172 | 32.8498 | 0.5633 | -2.5210 |
| structured_neckline_volume_breakout_proxy | double_bottom_or_structured_bottom_proxy | 51 | 51 | 33.3333 | -1.3421 | -3.6145 |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | 1202 | 1202 | 30.2829 | 0.2663 | -2.7067 |

## Retest Entry Only

| event_family_id | pattern_subtype | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | base_attack_position_review | 734 | 207 | 48.7923 | 2.7200 | 0.0000 |
| bottom_base_volume_attack_reference | low_position_base_attack | 395 | 116 | 49.1379 | 3.9508 | 0.0000 |
| bottom_base_volume_attack_reference | wide_base_review | 339 | 121 | 44.6281 | 1.4144 | -1.9656 |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | 1172 | 365 | 49.0411 | 1.8955 | -0.2401 |
| structured_neckline_volume_breakout_proxy | double_bottom_or_structured_bottom_proxy | 51 | 13 | 23.0769 | -6.9674 | -3.0576 |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | 1202 | 361 | 44.0443 | 1.1027 | -1.7143 |

## Interpretation

Use this as a first sample-finding grid, not as a production recommendation. If pattern subtypes do not show materially different results after validation, the neckline model can remain one broad structured-neckline model instead of separate W-bottom / triple-bottom / other models.
