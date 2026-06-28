# Structured-Neckline Manual Label Context Classifier Audit

- research_id: `structured_neckline_manual_label_context_classifier_audit`
- parameter_set_id: `structured_neckline_manual_label_context_classifier_audit_20260629`
- classifier_audit_scope_id: `manual_good_bad_vs_auto_pre_signal_context`
- label_rows: `14`
- matched_auto_context_rows: `14`
- conflict_rows: `2`
- approved_for_daily: `false`
- production_readiness: `not_production_ready_research_only`

## Alignment Summary

- manual_bad_auto_bearish_match: rows=`1`, unique_events=`1`, avg_manual_return_pct=`10.1517`
- manual_good_auto_bearish_false_negative: rows=`3`, unique_events=`2`, avg_manual_return_pct=`17.3846`
- manual_good_auto_non_bearish_match: rows=`8`, unique_events=`7`, avg_manual_return_pct=`13.0929`
- manual_label_conflict_not_scored: rows=`2`, unique_events=`1`, avg_manual_return_pct=`10.1365`

## Boundary

- This audit compares user chart labels with the research-only auto pre-signal context classifier.
- It is not a production filter, score, rank, or model condition.
- It does not write research variants back to production baseline.
