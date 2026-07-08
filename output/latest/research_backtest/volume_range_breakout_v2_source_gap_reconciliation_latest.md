# Volume Range Breakout V2 Source-Gap Reconciliation

- research_id: `volume_range_breakout_v2_source_gap_reconciliation`
- artifact_version: `volume_range_breakout_v2_source_gap_reconciliation_20260708`
- source_research_id: `volume_range_breakout_v2_raw_market_rerun`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This is a research-only source reconciliation artifact and does not change `stock_model_contract_registry.csv`.
- It compares raw price-history v2 rerun rows against timing-audit 60d rows, semantic-audit rows, and formal operation events.
- Rows after the timing artifact max signal date are classified as freshness extension, not promotion evidence.
- Rows inside the timing artifact date window that exist only in the raw rerun are a source-gap blocker before promotion.
- Current formal producer single-stock replay reproduces the raw-minus-timing rows; the gap is an unsynchronized artifact/source issue, not a standalone v2-only signal.

## Source Profile

| sample_size | value_a | value_b | value_c | status |
| --- | --- | --- | --- | --- |
| 808 | raw_detail_count=808;timing_60d_count=798 | semantic_detail_count=3136;formal_event_count=3245 | raw_max_signal_date=20260622;timing_max_signal_date=20260617;formal_max_signal_date=20260617 | research_only_source_profile |

## Gap Classification

| audit_key | sample_size | status | value_a |
| --- | --- | --- | --- |
| freshness_extension_after_timing_window | 8 | requires_research_artifact_refresh_before_promotion | 2061|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260706|59.9|80.1;2492|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260629|645.0|501.0;4551|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260629|226.0|216.0;5489|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260706|56.3|66.7;6259|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260706|39.35|38.75;6834|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260706|112.0|128.0;8081|20260618|20260622|next_day_break_signal_high_confirmed|20260623|20260702|342.0|287.0;5489|20260622|20260623|next_day_break_signal_high_confirmed|20260624|20260707|61.9|64.3 |
| source_gap_inside_timing_window_promotion_blocker | 2 | promotion_blocked_pending_research_source_sync | 8077|20260529|20260601|pullback_5ma_confirmed|20260602|20260616|49.0|49.65;8077|20260603|20260604|pullback_5ma_confirmed|20260605|20260612|54.6|49.0 |

## Promotion Gate

| sample_size | status | value_a | value_b | value_c |
| --- | --- | --- | --- | --- |
| 2 | promotion_blocked_pending_research_source_sync | inside_timing_window_gap_count=2 | expected_action=research_backtest_source_sync_or_exclusion_rule | production_registry_changed=False |

## Root Cause

| sample_size | status | value_a | value_b | value_c |
| --- | --- | --- | --- | --- |
| 10 | current_formal_producer_reproduces_all_raw_minus_timing_rows | raw_minus_timing_count=10 | current_formal_reproducer_match_count=10 | writes_output=False |

## Gap Detail

| stock_id | signal_date | confirmation_date | entry_date | return_pct | gap_scope | gap_classification | present_in_current_formal_reproducer | present_in_semantic_audit | present_in_formal_operation_events | root_cause_classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8077 | 20260529 | 20260601 | 20260602 | 1.3265 | inside_timing_artifact_window | source_gap_inside_timing_window_promotion_blocker | True | False | False | current_formal_producer_reproduces_event_existing_artifact_unsynced |
| 8077 | 20260603 | 20260604 | 20260605 | -10.2564 | inside_timing_artifact_window | source_gap_inside_timing_window_promotion_blocker | True | False | False | current_formal_producer_reproduces_event_existing_artifact_unsynced |
| 2061 | 20260618 | 20260622 | 20260623 | 33.7229 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 2492 | 20260618 | 20260622 | 20260623 | -22.3256 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 4551 | 20260618 | 20260622 | 20260623 | -4.4248 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 5489 | 20260618 | 20260622 | 20260623 | 18.4725 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 6259 | 20260618 | 20260622 | 20260623 | -1.5248 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 6834 | 20260618 | 20260622 | 20260623 | 14.2857 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 8081 | 20260618 | 20260622 | 20260623 | -16.0819 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |
| 5489 | 20260622 | 20260623 | 20260624 | 3.8772 | after_timing_artifact_window | freshness_extension_after_timing_window | True | False | False | current_formal_producer_reproduces_event_after_artifact_window |

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_source_gap_reconciliation_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_source_gap_reconciliation_detail_latest.csv`
- detail_rows: `10`
