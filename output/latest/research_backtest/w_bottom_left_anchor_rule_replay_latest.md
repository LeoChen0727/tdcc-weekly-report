# W-Bottom Left-Anchor Rule Replay

- generated_at: `2026-06-25 14:10:23 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- research_id: `w_bottom_left_anchor_rule_replay`
- source_research_id: `w_bottom_left_anchor_rule_grid`
- detail_rows: `2355`
- summary_rows: `5`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this replay does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: left-anchor rules are replayed as candidate filters/quality segments, not as production logic.

## Replay Summary

| rule_id | selected_rows | outcome_available_rows | volume_breakout_rate_pct | mature_sample_size | win_rate_pct | avg_a_return_pct | delta_volume_breakout_rate_pct | delta_win_rate_pct | delta_avg_a_return_pct | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current_detector_left_peak | 471 | 470 | 11.9149 | 52 | 30.7692 | 0.1621 | 0.0 | 0.0 | 0.0 | sample_size_ok_for_research_review |
| highest_high_45d_before_left_low | 471 | 470 | 11.9149 | 52 | 30.7692 | 0.1621 | 0.0 | 0.0 | 0.0 | sample_size_ok_for_research_review |
| highest_high_90d_before_left_low | 471 | 470 | 11.9149 | 52 | 30.7692 | 0.1621 | 0.0 | 0.0 | 0.0 | sample_size_ok_for_research_review |
| nearest_micro_pressure_45d_min15_before_left_low | 309 | 308 | 12.987 | 37 | 35.1351 | 0.6327 | 1.0721 | 4.3659 | 0.4706 | sample_size_ok_for_research_review |
| nearest_micro_pressure_90d_min15_before_left_low | 425 | 424 | 12.0283 | 48 | 31.25 | 0.1664 | 0.1134 | 0.4808 | 0.0043 | sample_size_ok_for_research_review |

## Key Cases

| stock_id | stock_name | rule_id | source_audit_scope | candidate_left_peak_date | candidate_matches_human_left_peak | outcome_available | selected_for_rule_replay | sym1_5_quality_bucket | a_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6415 | 矽力*-KY | current_detector_left_peak | current_model_candidate | 20250918 | false | true | true | neckline_volume_breakout | 13.8462 |
| 6415 | 矽力*-KY | highest_high_90d_before_left_low | current_model_candidate | 20250718 | false | true | true | neckline_volume_breakout | 13.8462 |
| 6415 | 矽力*-KY | nearest_micro_pressure_45d_min15_before_left_low | current_model_candidate | 20251107 | false | true | true | neckline_volume_breakout | 13.8462 |
| 6415 | 矽力*-KY | nearest_micro_pressure_90d_min15_before_left_low | current_model_candidate | 20251107 | false | true | true | neckline_volume_breakout | 13.8462 |
| 8069 | 元太 | current_detector_left_peak | manual_positive_missed_case | 20260211 | false | false | true |  |  |
| 8069 | 元太 | highest_high_90d_before_left_low | manual_positive_missed_case | 20251121 | false | false | true |  |  |
| 8069 | 元太 | nearest_micro_pressure_45d_min15_before_left_low | manual_positive_missed_case | 20260311 | true | false | true |  |  |
| 8069 | 元太 | nearest_micro_pressure_90d_min15_before_left_low | manual_positive_missed_case | 20260311 | true | false | true |  |  |

## Reading Notes

- This replay does not recompute production candidates. It compares existing W candidate outcomes after applying left-anchor rule selection.
- Manual positive rows such as `8069` can appear in key-case detail but are excluded from outcome metrics when no production-like outcome row exists.
- A better human anchor match is not enough for promotion; the selected subset must also improve confirmation and return metrics with enough mature rows.
