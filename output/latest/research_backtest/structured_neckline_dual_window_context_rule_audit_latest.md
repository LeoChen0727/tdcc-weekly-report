# Structured-Neckline Dual Window Context Rule Audit

- research_id: `structured_neckline_dual_window_context_rule_audit`
- parameter_set_id: `structured_neckline_dual_window_context_rule_audit_20260629`
- dual_window_rule_scope_id: `dual_window_pre_signal_context_candidate_rules`
- candidate_rules: `single_45_non_bearish;single_90_non_bearish;dual_45_entry_90_risk_warning;dual_45_and_90_non_bearish;dual_45_repaired_90_bearish_watchlist;dual_45_or_90_non_bearish`
- source_events: `374`
- detail_rows: `2244`
- approved_for_daily: `false`
- production_readiness: `not_production_ready_research_only`

## Low-Position Bull Accepted Overall

- dual_45_and_90_non_bearish: sample=`48`, success=`79.1667`, avg_return_pct=`5.5353`, median_return_pct=`10.3780`
- dual_45_entry_90_risk_warning: sample=`87`, success=`70.1149`, avg_return_pct=`3.8213`, median_return_pct=`3.8202`
- dual_45_or_90_non_bearish: sample=`87`, success=`70.1149`, avg_return_pct=`3.8213`, median_return_pct=`3.8202`
- dual_45_repaired_90_bearish_watchlist: sample=`39`, success=`58.9744`, avg_return_pct=`1.7117`, median_return_pct=`2.7559`
- single_45_non_bearish: sample=`87`, success=`70.1149`, avg_return_pct=`3.8213`, median_return_pct=`3.8202`
- single_90_non_bearish: sample=`48`, success=`79.1667`, avg_return_pct=`5.5353`, median_return_pct=`10.3780`

## Manual Alignment

- dual_45_and_90_non_bearish: good_rejected=`2`/9`, bad_accepted=`0`/1`
- dual_45_entry_90_risk_warning: good_rejected=`1`/9`, bad_accepted=`0`/1`
- dual_45_or_90_non_bearish: good_rejected=`1`/9`, bad_accepted=`0`/1`
- dual_45_repaired_90_bearish_watchlist: good_rejected=`8`/9`, bad_accepted=`0`/1`
- single_45_non_bearish: good_rejected=`1`/9`, bad_accepted=`0`/1`
- single_90_non_bearish: good_rejected=`2`/9`, bad_accepted=`0`/1`

## Boundary

- This compares research-only pre-signal context candidate rules.
- It is not a production filter, score, rank, or model condition.
- It does not write research variants back to production baseline.
