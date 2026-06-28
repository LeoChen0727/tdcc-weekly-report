# Structured-Neckline Manual Chart Label Audit

- research_id: `structured_neckline_manual_chart_label_audit`
- parameter_set_id: `structured_neckline_manual_chart_label_audit_20260629`
- manual_label_scope_id: `user_good_bad_chart_folder_labels`
- label_rows: `14`
- unique_events: `11`
- conflict_rows: `2`
- approved_for_daily: `false`
- production_readiness: `not_production_ready_research_only`

## Summary

- all_manual_labels / evidence_shortlist / bad: rows=`1`, unique_events=`1`, conflicting_event_rows=`0`, avg_return_pct=`10.1517`, median_return_pct=`10.1517`
- all_manual_labels / evidence_shortlist / good: rows=`9`, unique_events=`9`, conflicting_event_rows=`1`, avg_return_pct=`13.9232`, median_return_pct=`12.0507`
- all_manual_labels / review_shortlist / bad: rows=`1`, unique_events=`1`, conflicting_event_rows=`1`, avg_return_pct=`10.1365`, median_return_pct=`10.1365`
- all_manual_labels / review_shortlist / good: rows=`3`, unique_events=`3`, conflicting_event_rows=`0`, avg_return_pct=`13.9082`, median_return_pct=`10.7216`
- packet_evidence_shortlist / evidence_shortlist / bad: rows=`1`, unique_events=`1`, conflicting_event_rows=`0`, avg_return_pct=`10.1517`, median_return_pct=`10.1517`
- packet_evidence_shortlist / evidence_shortlist / good: rows=`9`, unique_events=`9`, conflicting_event_rows=`1`, avg_return_pct=`13.9232`, median_return_pct=`12.0507`
- packet_review_shortlist / review_shortlist / bad: rows=`1`, unique_events=`1`, conflicting_event_rows=`1`, avg_return_pct=`10.1365`, median_return_pct=`10.1365`
- packet_review_shortlist / review_shortlist / good: rows=`3`, unique_events=`3`, conflicting_event_rows=`0`, avg_return_pct=`13.9082`, median_return_pct=`10.7216`

## Boundary

- This audit records user chart-review labels from Good/Bad folders.
- It is research/backtest evidence only.
- It does not change production model conditions, scoring, ranking, PDF logic, or production baselines.
