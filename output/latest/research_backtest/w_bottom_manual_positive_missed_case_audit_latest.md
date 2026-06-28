# W-Bottom Manual Positive Missed-Case Audit

- generated_at: `2026-06-25 13:19:29 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- research_id: `w_bottom_manual_positive_missed_case_audit`
- source_research_id: `manual_user_positive_examples`
- rows: `2`
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.
- interpretation boundary: manual positive examples are research evidence only and require a separate model-change or promotion PR before production use.

## Missed-Case Summary

| stock_id | stock_name | manual_pattern_type | user_interval_start | user_interval_end | second_low_gap_pct | observation_rebound_from_right_low_pct | valid_close_count_at_observation | primary_blocker | relaxed_history_detection_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4916 | 事欣科 | higher_right_low_w_base | 20260319 | 20260515 | 15.9774 | 9.7245 | 252 | second_low_gap_above_standard_w_max | still_not_detected_if_history_gate_bypassed |
| 8069 | 元太 | standard_w_missed_by_history_gate | 20260312 | 20260508 | -0.7353 | 20.0 | 123 | insufficient_long_position_history | detected_if_history_gate_bypassed |

## Human-Review Interpretation

- `4916` is a higher-right-low W/base candidate: it is user-positive, but it is not the same family as the current standard W gate because the right low is far above the left low.
- `8069` is closer to a standard W: the current code misses it mainly because the 180-valid-close price-position history gate fails before shape evaluation.
- Both cases also show that left-start selection needs a separate audit: the algorithm can pick the highest available pre-low peak, while the human visual anchor may use a nearer local pressure high.
- This file is meant to preserve those positive missed examples for research/backtest iteration, not to approve production changes.

## Chart Files

| stock_id | manual_case_id | chart_path |
| --- | --- | --- |
| 4916 | user_4916_20260319_20260515 | output/latest/research_backtest/w_bottom_manual_positive_missed_case_audit/4916_20260319_20260515.png |
| 8069 | user_8069_20260312_20260508 | output/latest/research_backtest/w_bottom_manual_positive_missed_case_audit/8069_20260312_20260508.png |
