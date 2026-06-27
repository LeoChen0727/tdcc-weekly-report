# W-Bottom Left-Anchor And Pattern-Family Audit

- generated_at: `2026-06-25 13:36:49 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- research_id: `w_bottom_left_anchor_pattern_family_audit`
- source_research_id: `w_bottom_candidate_quality_audit`
- manual_source_research_id: `w_bottom_manual_positive_missed_case_audit`
- detail_rows: `472`
- summary_rows: `13`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: this is a research-only left_peak_start_selection and pattern-family audit.

## What This Tests

- Current detector picks the left peak from at most `45` trading days before the first low.
- This audit checks whether the selected left peak is near that search-window edge, or whether a pre-low peak at least `20.0`% higher exists in a `90`-trading-day window.
- It also separates `standard_double_bottom_w` from `higher_right_low_base_w` so those families do not get mixed by simply widening the second-low gap.

## Pattern-Family Summary

| summary_value | row_count | current_candidate_count | manual_positive_count | anchor_issue_count | search_window_edge_count | higher_alt_peak_count |
| --- | --- | --- | --- | --- | --- | --- |
| standard_double_bottom_w | 471 | 470 | 1 | 137 | 81 | 65 |
| higher_right_low_base_w | 1 | 0 | 1 | 1 | 0 | 0 |

## Anchor-Issue Summary

| summary_value | row_count | current_candidate_count | manual_positive_count | anchor_issue_rate_pct |
| --- | --- | --- | --- | --- |
| no_anchor_issue_detected | 334 | 334 | 0 | 0.0 |
| auto_left_peak_near_search_window_edge | 71 | 71 | 0 | 100.0 |
| higher_pre_left_low_peak_outside_45d_window | 65 | 65 | 0 | 100.0 |
| human_auto_left_peak_mismatch | 1 | 0 | 1 | 100.0 |
| manual_positive_no_current_auto_anchor | 1 | 0 | 1 | 100.0 |

## Key Review Cases

| stock_id | stock_name | case_review_tag | computed_pattern_family | human_left_peak_date | auto_left_peak_date | auto_left_peak_days_before_left_low | anchor_issue_type | recommended_next_research_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6415 | 矽力*-KY | user_question_auto_anchor_only | standard_double_bottom_w |  | 20250918 | 41 | higher_pre_left_low_peak_outside_45d_window | review_left_anchor_window_or_structural_start_rule |
| 4916 | 事欣科 | user_manual_positive | higher_right_low_base_w | 20260319 |  |  | manual_positive_no_current_auto_anchor | split_higher_right_low_base_from_standard_w |
| 8069 | 元太 | user_manual_positive | standard_double_bottom_w | 20260312 | 20260211 | 26 | human_auto_left_peak_mismatch | audit_left_start_selection_before_model_change |

## Reading Notes

- `4916` supports a separate higher-right-low base/W family rather than widening the current standard-W gate.
- `8069` shows a standard-W-like manual positive where the auto anchor can differ from the human visual anchor once the history gate is bypassed.
- `6415` is not assigned a replacement human anchor here; it is preserved as a user-questioned auto-anchor case for manual confirmation.
- This audit is not a production promotion artifact.
