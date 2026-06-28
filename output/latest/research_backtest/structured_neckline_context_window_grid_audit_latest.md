# Structured-Neckline Context Window Grid Audit

- research_id: `structured_neckline_context_window_grid_audit`
- parameter_set_id: `structured_neckline_context_window_grid_audit_20260629`
- context_window_grid_scope_id: `pre_signal_context_window_grid_30_45_60_90`
- windows: `30;45;60;90`
- detail_rows: `1496`
- source_events: `374`
- approved_for_daily: `false`
- production_readiness: `not_production_ready_research_only`

## Manual Alignment

- window `30`: good_false_negative=`2` / good=`9`, bad_false_positive=`1` / bad=`1`, avg_return_pct=`13.6046`
- window `45`: good_false_negative=`1` / good=`9`, bad_false_positive=`0` / bad=`1`, avg_return_pct=`13.6046`
- window `60`: good_false_negative=`2` / good=`9`, bad_false_positive=`0` / bad=`1`, avg_return_pct=`13.6046`
- window `90`: good_false_negative=`2` / good=`9`, bad_false_positive=`0` / bad=`1`, avg_return_pct=`13.6046`

## Low-Position Bull Context Summary

- window `30` / `sideways_or_consolidation`: sample=`45`, success=`62.2222`, avg_return_pct=`2.2367`
- window `30` / `slow_uptrend`: sample=`44`, success=`72.7273`, avg_return_pct=`4.2408`
- window `30` / `volatile_mixed`: sample=`3`, success=`100.0000`, avg_return_pct=`9.4375`
- window `45` / `sideways_or_consolidation`: sample=`38`, success=`60.5263`, avg_return_pct=`2.1951`
- window `45` / `slow_uptrend`: sample=`36`, success=`80.5556`, avg_return_pct=`5.9967`
- window `45` / `volatile_mixed`: sample=`13`, success=`69.2308`, avg_return_pct=`2.5504`
- window `60` / `sideways_or_consolidation`: sample=`27`, success=`59.2593`, avg_return_pct=`2.1894`
- window `60` / `slow_uptrend`: sample=`22`, success=`95.4545`, avg_return_pct=`9.6306`
- window `60` / `volatile_mixed`: sample=`21`, success=`66.6667`, avg_return_pct=`2.0040`
- window `90` / `sideways_or_consolidation`: sample=`7`, success=`57.1429`, avg_return_pct=`2.5884`
- window `90` / `slow_uptrend`: sample=`16`, success=`93.7500`, avg_return_pct=`10.0183`
- window `90` / `volatile_mixed`: sample=`25`, success=`76.0000`, avg_return_pct=`3.4914`

## Boundary

- This grid changes only the research pre-signal context observation window.
- It uses the same classifier thresholds as the previous auto context audit to isolate window-length effects.
- It is not a production filter, score, rank, or model condition.
- It does not write research variants back to production baseline.
