# Structured Neckline Strict 45/90 Confirmation Entry Audit

- generated_at: `2026-06-29 03:34:05 Asia/Taipei`
- research_id: `structured_neckline_strict_45_90_confirmation_entry_audit`
- source_research_id: `structured_neckline_strict_45_90_follow_through_audit`
- source_parameter_set_id: `structured_neckline_strict_45_90_follow_through_audit_20260629`
- confirmation_scope_id: `follow_through_close_confirmation_next_open_grid`
- exit_rule_id: `tp10_close_win_5pct_pullback_neutral_else_20d_close_loss`
- max_holding_sessions: `20`
- detail_rows: `367`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Boundary

This is a tradable follow-through hypothesis because entry is the next open after the confirmation close is already known. It is still research-only and not a production promotion.

## Summary

| confirmation_rule_id | source_accepted_count | tradable_entry_count | win_count | neutral_count | loss_count | neutral_inclusive_success_rate_pct | avg_return_pct | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| close_ge_1pct_within_3_sessions_next_open | 32 | 32 | 20 | 7 | 5 | 84.3750 | 7.4967 | confirmation_next_open_research_only_not_production_ready |
| close_ge_1pct_within_1_sessions_next_open | 19 | 19 | 13 | 3 | 3 | 84.2105 | 8.0665 | confirmation_next_open_research_only_not_production_ready |
| close_ge_1pct_within_5_sessions_next_open | 37 | 37 | 24 | 7 | 6 | 83.7838 | 8.0214 | confirmation_next_open_research_only_not_production_ready |
| close_ge_1pct_within_2_sessions_next_open | 30 | 30 | 19 | 6 | 5 | 83.3333 | 7.3811 | confirmation_next_open_research_only_not_production_ready |
| close_ge_3pct_within_5_sessions_next_open | 28 | 28 | 17 | 6 | 5 | 82.1429 | 6.9858 | confirmation_next_open_research_only_not_production_ready |
| close_ge_5pct_within_5_sessions_next_open | 26 | 26 | 15 | 6 | 5 | 80.7692 | 6.4255 | confirmation_next_open_research_only_not_production_ready |
| close_ge_2pct_within_5_sessions_next_open | 30 | 30 | 18 | 6 | 6 | 80.0000 | 7.0362 | confirmation_next_open_research_only_not_production_ready |
| close_ge_3pct_within_3_sessions_next_open | 25 | 25 | 15 | 5 | 5 | 80.0000 | 6.4098 | confirmation_next_open_research_only_not_production_ready |
| close_ge_2pct_within_1_sessions_next_open | 15 | 15 | 10 | 2 | 3 | 80.0000 | 7.2422 | confirmation_next_open_research_only_not_production_ready |
| close_ge_2pct_within_2_sessions_next_open | 23 | 23 | 14 | 4 | 5 | 78.2609 | 6.1717 | confirmation_next_open_research_only_not_production_ready |
| close_ge_2pct_within_3_sessions_next_open | 27 | 27 | 16 | 5 | 6 | 77.7778 | 6.5084 | confirmation_next_open_research_only_not_production_ready |
| close_ge_3pct_within_2_sessions_next_open | 21 | 21 | 12 | 4 | 5 | 76.1905 | 5.5148 | confirmation_next_open_research_only_not_production_ready |
| close_ge_5pct_within_3_sessions_next_open | 21 | 21 | 12 | 4 | 5 | 76.1905 | 5.3161 | confirmation_next_open_research_only_not_production_ready |
| close_ge_5pct_within_2_sessions_next_open | 16 | 16 | 9 | 3 | 4 | 75.0000 | 4.9385 | confirmation_next_open_research_only_not_production_ready |
| close_ge_3pct_within_1_sessions_next_open | 11 | 11 | 7 | 1 | 3 | 72.7273 | 6.4743 | confirmation_next_open_research_only_not_production_ready |
| close_ge_5pct_within_1_sessions_next_open | 6 | 6 | 3 | 1 | 2 | 66.6667 | 3.7524 | confirmation_next_open_research_only_not_production_ready |
