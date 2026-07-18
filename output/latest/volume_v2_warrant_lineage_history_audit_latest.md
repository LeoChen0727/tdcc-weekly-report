# Volume v2 warrant lineage history audit

- Audit version: `volume_v2_warrant_lineage_history_audit_v2`
- Audited trading dates: `20260709, 20260713, 20260714, 20260715, 20260716, 20260717`
- Dynamic source coverage: `6/6`
- Formal volume v2 rows: `30`
- Formal verified clean: `30`
- Formal superseded: `0`
- Formal quarantined: `0`
- Formal unreplayable: `0`
- Superseded advisory watch rows: `1`
- Independent component replay resolved: `30/30`
- Candidate-absent canonical score contexts: `9` stored as `{}`
- Warrant collision rows: `1`
- TDCC-status collision rows: `0`
- False-breakout collision rows: `0`
- Watch/candidate source score collisions: `0`
- Watch/candidate source rank collisions: `0`
- Historical daily snapshots were read only and were not rewritten.

## Daily coverage

| Report date | Formal v2 rows | Dispatcher warrant score source |
|---|---:|---|
| 20260709 | 4 | legacy_watch_overrides_candidate |
| 20260713 | 8 | legacy_watch_overrides_candidate |
| 20260714 | 6 | legacy_watch_overrides_candidate |
| 20260715 | 4 | legacy_watch_overrides_candidate |
| 20260716 | 5 | canonical_candidate_after_watch_merge |
| 20260717 | 3 | canonical_candidate_after_watch_merge |

## Watch collision disposition

| Report date | Stock | Model | Collision fields | Published → canonical values | Base | TDCC | Risk | Final | Rank | Disposition |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|
| 20260716 | 6505 | volume_range_breakout_v2_high_position_volume_attack | warrant_flow_signal | warrant=call_put_bullish/call_strong_inflow→call_strong_inflow; tdcc=/→; false_breakout=False/False→False | 64.0→64.0 | 0.0→0.0 | 0.0→0.0 | 73.0→73.0 | 1→1 | verified_clean |

## Conclusion

The dynamic historical/current coverage replays the legacy candidate-plus-watch collision context and the canonical candidate-only collision context independently for warrant, TDCC status, and false-breakout risk. Component deltas are applied to base_model_score, tdcc_score, and risk_penalty before final_rank_score is clamped, then rank is rebuilt by score descending, stock_id, and source_row_index. Candidate-absent canonical score contexts remain empty. Historical snapshots are never rewritten; superseded, quarantined, or unreplayable rows cannot be used as current formal evidence.
