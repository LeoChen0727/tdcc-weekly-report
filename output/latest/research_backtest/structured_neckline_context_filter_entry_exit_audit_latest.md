# Structured Neckline Context Filter Entry/Exit Audit

- generated_at: `2026-06-29 00:20:00 Asia/Taipei`
- research_id: `structured_neckline_context_filter_entry_exit_audit`
- source_entry_exit_research_id: `structured_neckline_retest_entry_exit_grid`
- source_evidence_research_id: `structured_neckline_retest_evidence_shortlist`
- target_segment_id: `low_position_le60_market_bull`
- exclusion_rule: `visual_pre_signal_context != bearish`
- evidence_event_count: `38`
- pass_event_count: `23`
- excluded_event_count: `15`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Interpretation

- This audit treats bearish pre-signal context as the first-pass exclusion before comparing entry/exit/neutral rules.
- The three e04 folders are outcome buckets from the current exit rule: win, neutral, and loss. They are not manual pattern folders.
- Because the user's visual conclusion came from the evidence charts, the filter uses `visual_pre_signal_context`, which is computed from the same visible chart span.
- This is not a production gate. It is a research-only candidate filter for the next entry/exit grid discussion.

## Context Filter Counts

| visual_context_filter_result | visual_pre_signal_context | events | unique_stocks |
| --- | --- | --- | --- |
| excluded | bearish | 15 | 14 |
| pass | bullish | 10 | 10 |
| pass | mixed | 11 | 11 |
| pass | sideways_or_consolidation | 2 | 2 |

## Current e04 Rule Before/After Filter

| cohort_id | sample_size | win_count | neutral_count | loss_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | avg_return_pct | median_return_pct | avg_mae_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_review_shortlist_events | 38 | 11 | 13 | 14 | 44.0000 | 63.1579 | 1.8378 | 2.8387 | -7.1894 |
| visual_context_bearish_excluded | 15 | 3 | 3 | 9 | 25.0000 | 40.0000 | -0.0421 | 1.8657 | -7.7698 |
| visual_context_non_bearish | 23 | 8 | 10 | 5 | 61.5385 | 78.2609 | 3.0639 | 3.6290 | -6.8108 |

## Top Non-Bearish Entry/Exit Rows

| stop_rule_id | exit_rule_id | outcome_rule_id | sample_size | win_count | neutral_count | loss_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | avg_return_pct | median_return_pct | avg_mae_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| signal_low_stop | tp10_intraday_or_fixed_20d_close | tp10_intraday_required_else_loss | 23 | 16 | 0 | 7 | 69.5652 | 69.5652 | 4.6638 | 10.0000 | -6.7176 |
| neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | tp10_intraday_required_else_loss | 23 | 16 | 0 | 7 | 69.5652 | 69.5652 | 4.7301 | 10.0000 | -6.7176 |
| source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | tp10_intraday_required_else_loss | 23 | 16 | 0 | 7 | 69.5652 | 69.5652 | 4.7301 | 10.0000 | -6.7176 |
| signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | tp10_close_win_5pct_pullback_neutral | 23 | 8 | 10 | 5 | 61.5385 | 78.2609 | 3.0639 | 3.6290 | -6.8108 |
| neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | tp10_close_win_5pct_pullback_neutral | 23 | 8 | 10 | 5 | 61.5385 | 78.2609 | 3.1302 | 3.6290 | -6.8108 |
| source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | tp10_close_win_5pct_pullback_neutral | 23 | 8 | 10 | 5 | 61.5385 | 78.2609 | 3.1302 | 3.6290 | -6.8108 |
| retest_low_stop | tp10_intraday_or_fixed_20d_close | tp10_intraday_required_else_loss | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 2.3841 | 10.0000 | -6.5703 |
| signal_low_stop | fixed_10d_close | positive_return_after_fixed_10d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 4.2508 | 5.4732 | -8.5609 |
| neckline_minus_2pct_stop | fixed_10d_close | positive_return_after_fixed_10d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 4.2216 | 5.4732 | -8.5609 |
| source_retest_or_neckline_2pct_stop | fixed_10d_close | positive_return_after_fixed_10d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 4.2216 | 5.4732 | -8.5609 |
| signal_low_stop | fixed_20d_close | positive_return_after_fixed_20d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 12.2683 | 3.9909 | -9.6350 |
| neckline_minus_2pct_stop | fixed_20d_close | positive_return_after_fixed_20d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 12.3407 | 3.9909 | -9.6350 |
| source_retest_or_neckline_2pct_stop | fixed_20d_close | positive_return_after_fixed_20d | 23 | 13 | 0 | 10 | 56.5217 | 56.5217 | 12.3407 | 3.9909 | -9.6350 |
| retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | tp10_close_win_5pct_pullback_neutral | 23 | 7 | 8 | 8 | 46.6667 | 65.2174 | 1.2286 | 2.8605 | -6.6635 |
| retest_low_stop | fixed_20d_close | positive_return_after_fixed_20d | 23 | 10 | 0 | 13 | 43.4783 | 43.4783 | 5.8581 | -0.5579 | -8.7577 |
| retest_low_stop | fixed_10d_close | positive_return_after_fixed_10d | 23 | 10 | 0 | 13 | 43.4783 | 43.4783 | 1.3586 | -1.5342 | -8.2582 |

## Boundary Notes

- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.
- This audit only filters existing evidence-shortlist events. It does not change the structured-neckline detector or production stock model registry.
