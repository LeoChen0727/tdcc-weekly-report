# Structured Neckline Strict 45/90 Confirmation Expansion Audit

- generated_at: `2026-06-29 03:45:56 Asia/Taipei`
- research_id: `structured_neckline_strict_45_90_confirmation_expansion_audit`
- source_research_id: `structured_neckline_dual_window_risk_penalty_audit`
- source_parameter_set_id: `structured_neckline_dual_window_risk_penalty_audit_20260629`
- confirmation_scope_id: `strict_45_90_all_sample_confirmation_next_open_expansion`
- source_events: `313`
- detail_rows: `1782`
- exit_rule_id: `tp10_close_win_5pct_pullback_neutral_else_20d_close_loss`
- max_holding_sessions: `20`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Boundary

This expands the strict 45/90 confirmation-next-open hypothesis from the 48-row low-position bull subset to all strict 45/90 accepted events. It remains research-only and is not a production promotion.

## Key Scope Summary

| analysis_scope_id | confirmation_rule_id | scope_event_count | tradable_entry_count | win_count | neutral_count | loss_count | neutral_inclusive_success_rate_pct | avg_return_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_strict_45_90 | close_ge_1pct_within_1_sessions_next_open | 313 | 94 | 50 | 22 | 22 | 76.5957 | 5.2187 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_2pct_within_1_sessions_next_open | 313 | 74 | 38 | 17 | 19 | 74.3243 | 4.4356 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_2pct_within_3_sessions_next_open | 313 | 139 | 67 | 34 | 38 | 72.6619 | 4.1979 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_3pct_within_3_sessions_next_open | 313 | 124 | 56 | 34 | 34 | 72.5806 | 3.5776 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_1pct_within_3_sessions_next_open | 313 | 152 | 72 | 38 | 42 | 72.3684 | 4.4137 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_3pct_within_1_sessions_next_open | 313 | 54 | 27 | 12 | 15 | 72.2222 | 3.3028 | reviewable_small_sample |
| all_strict_45_90 | close_ge_5pct_within_3_sessions_next_open | 313 | 97 | 44 | 25 | 28 | 71.1340 | 3.0518 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_2pct_within_2_sessions_next_open | 313 | 113 | 54 | 26 | 33 | 70.7965 | 3.6588 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_1pct_within_2_sessions_next_open | 313 | 132 | 62 | 31 | 39 | 70.4545 | 4.1027 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_5pct_within_2_sessions_next_open | 313 | 71 | 35 | 15 | 21 | 70.4225 | 3.2511 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_1pct_within_5_sessions_next_open | 313 | 175 | 79 | 43 | 53 | 69.7143 | 3.4377 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_2pct_within_5_sessions_next_open | 313 | 160 | 72 | 39 | 49 | 69.3750 | 2.9562 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_3pct_within_5_sessions_next_open | 313 | 148 | 63 | 39 | 46 | 68.9189 | 2.8801 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_5pct_within_5_sessions_next_open | 313 | 123 | 52 | 32 | 39 | 68.2927 | 2.4553 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_3pct_within_2_sessions_next_open | 313 | 94 | 43 | 21 | 30 | 68.0851 | 2.8876 | reviewable_broader_sample |
| all_strict_45_90 | close_ge_5pct_within_1_sessions_next_open | 313 | 32 | 15 | 6 | 11 | 65.6250 | 0.9940 | reviewable_small_sample |
| low_position_le60_market_bull | close_ge_1pct_within_3_sessions_next_open | 48 | 32 | 20 | 7 | 5 | 84.3750 | 7.4967 | reviewable_small_sample |
| low_position_le60_market_bull | close_ge_1pct_within_1_sessions_next_open | 48 | 19 | 13 | 3 | 3 | 84.2105 | 8.0665 | thin_sample |
| low_position_le60_market_bull | close_ge_1pct_within_5_sessions_next_open | 48 | 37 | 24 | 7 | 6 | 83.7838 | 8.0214 | reviewable_small_sample |
| low_position_le60_market_bull | close_ge_1pct_within_2_sessions_next_open | 48 | 30 | 19 | 6 | 5 | 83.3333 | 7.3811 | reviewable_small_sample |
| low_position_le60_market_bull | close_ge_3pct_within_5_sessions_next_open | 48 | 28 | 17 | 6 | 5 | 82.1429 | 6.9858 | thin_sample |
| low_position_le60_market_bull | close_ge_5pct_within_5_sessions_next_open | 48 | 26 | 15 | 6 | 5 | 80.7692 | 6.4255 | thin_sample |
| low_position_le60_market_bull | close_ge_2pct_within_5_sessions_next_open | 48 | 30 | 18 | 6 | 6 | 80.0000 | 7.0362 | reviewable_small_sample |
| low_position_le60_market_bull | close_ge_3pct_within_3_sessions_next_open | 48 | 25 | 15 | 5 | 5 | 80.0000 | 6.4098 | thin_sample |
| low_position_le60_market_bull | close_ge_2pct_within_1_sessions_next_open | 48 | 15 | 10 | 2 | 3 | 80.0000 | 7.2422 | thin_sample |
| low_position_le60_market_bull | close_ge_2pct_within_2_sessions_next_open | 48 | 23 | 14 | 4 | 5 | 78.2609 | 6.1717 | thin_sample |
| low_position_le60_market_bull | close_ge_2pct_within_3_sessions_next_open | 48 | 27 | 16 | 5 | 6 | 77.7778 | 6.5084 | thin_sample |
| low_position_le60_market_bull | close_ge_3pct_within_2_sessions_next_open | 48 | 21 | 12 | 4 | 5 | 76.1905 | 5.5148 | thin_sample |
| low_position_le60_market_bull | close_ge_5pct_within_3_sessions_next_open | 48 | 21 | 12 | 4 | 5 | 76.1905 | 5.3161 | thin_sample |
| low_position_le60_market_bull | close_ge_5pct_within_2_sessions_next_open | 48 | 16 | 9 | 3 | 4 | 75.0000 | 4.9385 | thin_sample |
| low_position_le60_market_bull | close_ge_3pct_within_1_sessions_next_open | 48 | 11 | 7 | 1 | 3 | 72.7273 | 6.4743 | thin_sample |
| low_position_le60_market_bull | close_ge_5pct_within_1_sessions_next_open | 48 | 6 | 3 | 1 | 2 | 66.6667 | 3.7524 | thin_sample |
| non_low_position_le60_market_bull | close_ge_1pct_within_1_sessions_next_open | 265 | 75 | 37 | 19 | 19 | 74.6667 | 4.4972 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_2pct_within_1_sessions_next_open | 265 | 59 | 28 | 15 | 16 | 72.8814 | 3.7221 | reviewable_small_sample |
| non_low_position_le60_market_bull | close_ge_3pct_within_1_sessions_next_open | 265 | 43 | 20 | 11 | 12 | 72.0930 | 2.4915 | reviewable_small_sample |
| non_low_position_le60_market_bull | close_ge_2pct_within_3_sessions_next_open | 265 | 112 | 51 | 29 | 32 | 71.4286 | 3.6409 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_3pct_within_3_sessions_next_open | 265 | 99 | 41 | 29 | 29 | 70.7071 | 2.8623 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_5pct_within_3_sessions_next_open | 265 | 76 | 32 | 21 | 23 | 69.7368 | 2.4261 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_1pct_within_3_sessions_next_open | 265 | 120 | 52 | 31 | 37 | 69.1667 | 3.5915 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_5pct_within_2_sessions_next_open | 265 | 55 | 26 | 12 | 17 | 69.0909 | 2.7602 | reviewable_small_sample |
| non_low_position_le60_market_bull | close_ge_2pct_within_2_sessions_next_open | 265 | 90 | 40 | 22 | 28 | 68.8889 | 3.0166 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_2pct_within_5_sessions_next_open | 265 | 130 | 54 | 33 | 43 | 66.9231 | 2.0147 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_1pct_within_2_sessions_next_open | 265 | 102 | 43 | 25 | 34 | 66.6667 | 3.1384 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_1pct_within_5_sessions_next_open | 265 | 138 | 55 | 36 | 47 | 65.9420 | 2.2087 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_3pct_within_5_sessions_next_open | 265 | 120 | 46 | 33 | 41 | 65.8333 | 1.9220 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_3pct_within_2_sessions_next_open | 265 | 73 | 31 | 17 | 25 | 65.7534 | 2.1319 | reviewable_broader_sample |
| non_low_position_le60_market_bull | close_ge_5pct_within_1_sessions_next_open | 265 | 26 | 12 | 5 | 9 | 65.3846 | 0.3574 | thin_sample |
| non_low_position_le60_market_bull | close_ge_5pct_within_5_sessions_next_open | 265 | 97 | 37 | 26 | 34 | 64.9485 | 1.3912 | reviewable_broader_sample |
