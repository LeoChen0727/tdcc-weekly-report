# Structured Neckline Non-Bearish Exit Rule Comparison

- generated_at: `2026-06-29 00:30:30 Asia/Taipei`
- research_id: `structured_neckline_non_bearish_exit_rule_comparison_audit`
- source_research_id: `structured_neckline_context_filter_entry_exit_audit`
- comparison_scope_id: `visual_context_non_bearish_signal_low_stop`
- sample_size: `23`
- stop_rule_id: `signal_low_stop`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Why This Exists

- The previous audit supported excluding bearish pre-signal context first.
- This audit compares only the remaining non-bearish events.
- It compares two sell/outcome definitions on the same entry event set.
- Pure win rate and neutral-inclusive success rate remain separate metrics.

## Rule Summary

| exit_rule_comparison_id | sample_size | win_count | neutral_count | loss_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | avg_mae_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tp10_intraday_touch | 23 | 16 | 0 | 7 | 69.5652 | 69.5652 | 73.9130 | 4.6638 | 10.0000 | -6.7176 |
| tp10_close_with_5pct_pullback_neutral | 23 | 8 | 10 | 5 | 61.5385 | 78.2609 | 69.5652 | 3.0639 | 3.6290 | -6.8108 |

## Outcome Transition Counts

| outcome_transition | interpretation_bucket | events | unique_stocks |
| --- | --- | --- | --- |
| win_to_neutral | intraday_touch_win_close_rule_neutral | 8 | 8 |
| win_to_win | both_rules_win | 8 | 8 |
| loss_to_loss | both_rules_loss | 5 | 5 |
| loss_to_neutral | intraday_loss_close_rule_neutral | 2 | 2 |

## Rows To Review

- `intraday_touch_win_close_rule_loss`: the stock touched +10% intraday, but the close-based rule did not produce a win or neutral.
- `intraday_touch_win_close_rule_neutral`: the stock touched +10% intraday, but the close-based rule treats the trade as an escape/neutral.
- `both_rules_loss`: both candidate sell definitions fail; these are the highest-priority chart review rows.

| stock_id | stock_name | signal_date | retest_entry_date | visual_pre_signal_context | entry_price | intraday_outcome | intraday_return_pct | close_neutral_outcome | close_neutral_return_pct | outcome_transition | interpretation_bucket |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3163 | 波若威 | 20250106 | 20250109 | mixed | 156.0 | win | 10.0000 | neutral | -2.2436 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 3260 | 威剛 | 20250217 | 20250226 | mixed | 87.7 | win | 10.0000 | neutral | 3.3067 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 2368 | 金像電 | 20250630 | 20250707 | bullish | 299.5 | win | 10.0000 | neutral | 4.8414 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 3037 | 欣興 | 20250703 | 20250710 | mixed | 124.0 | win | 10.0000 | neutral | 3.6290 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 2316 | 楠梓電 | 20250723 | 20250730 | bullish | 76.2 | win | 10.0000 | neutral | 2.6247 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 6706 | 惠特 | 20250918 | 20250930 | sideways_or_consolidation | 83.9 | win | 10.0000 | neutral | 2.8605 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 6197 | 佳必琪 | 20260311 | 20260316 | mixed | 178.5 | win | 10.0000 | neutral | 0.8403 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 8358 | 金居 | 20260415 | 20260420 | bullish | 373.0 | win | 10.0000 | neutral | -0.8043 | win_to_neutral | intraday_touch_win_close_rule_neutral |
| 1528 | 恩德 | 20250221 | 20250227 | mixed | 14.8 | loss | 0.0000 | loss | 0.0000 | loss_to_loss | both_rules_loss |
| 3051 | 力特 | 20260116 | 20260121 | mixed | 27.1 | loss | -14.5756 | loss | -14.5756 | loss_to_loss | both_rules_loss |
| 2363 | 矽統 | 20260121 | 20260128 | mixed | 62.0 | loss | -17.7419 | loss | -17.7419 | loss_to_loss | both_rules_loss |
| 6290 | 良維 | 20260224 | 20260306 | bullish | 233.0 | loss | -16.9528 | loss | -16.9528 | loss_to_loss | both_rules_loss |
| 6488 | 環球晶 | 20260421 | 20260428 | bullish | 603.0 | loss | -7.9602 | loss | -7.9602 | loss_to_loss | both_rules_loss |

## Boundary Notes

- This is research/backtest advisory-only output.
- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.
- No production model condition, scoring, ranking, PDF logic, or baseline was changed.
