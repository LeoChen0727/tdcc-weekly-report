# Volume Range Breakout V2 Raw-Market Rerun

- research_id: `volume_range_breakout_v2_raw_market_rerun`
- artifact_version: `volume_range_breakout_v2_raw_market_rerun_20260708`
- source_research_id: `volume_range_breakout_v2_next_day_continuation_timing_audit`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This raw-market rerun is research-only and does not change `stock_model_contract_registry.csv`.
- Gate tested: base v1 volume_range_breakout signal, signal close >= previous 60d high + 2pct, and next-day continuation confirmed.
- Entry/exit basis stays unchanged: confirmation next open entry, signal-low stop, otherwise fixed 10-trading-day close exit.
- Membership is compared against the prior timing-audit 60d subset to check whether the earlier artifact was biased by a narrower sample.
- Any raw row inside the timing-audit date window that is absent from the timing artifact is a research/backtest source-gap blocker before promotion.

## Raw V2 Metrics

| sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | trim_avg_return_pct | trim_median_return_pct | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 808 | 52.48 | 0.5 | 47.03 | 4.9893 | 1.3482 | 4.5094 | 1.3482 | raw_rerun_matches_timing_window |

## Data Scope

| scanned_price_files | equity_price_files | base_v1_signal_count | base_v1_mature_trade_count | next_day_trigger_mature_count | trigger_only_excluded_by_follow_through_count | v2_raw_candidate_count | v2_raw_mature_event_count | timing_audit_60d_event_count | timing_audit_max_signal_date | raw_extension_after_timing_count | raw_minus_timing_within_timing_window_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2376 | 1948 | 4752 | 3175 | 1256 | 448 | 808 | 808 | 808 | 20260622 | 0 | 0 |

## Out Of Sample

| sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | status |
| --- | --- | --- | --- | --- | --- |
| 353 | 58.07 | 41.93 | 6.9907 | 3.5354 | research_only_oos_check |

## Anomaly Check

| sample_size | win_rate_pct | avg_return_pct | median_return_pct | anomaly_count | status |
| --- | --- | --- | --- | --- | --- |
| 790 | 52.53 | 4.5094 | 1.3482 | 18 | anomaly_rows_marked_review_before_promotion |

## Membership Check

| audit_key | sample_size | status | value_a |
| --- | --- | --- | --- |
| raw_minus_timing_count | 0 | match |  |
| timing_minus_raw_count | 0 | match |  |
| raw_minus_timing_within_timing_window_count | 0 | match |  |

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_raw_market_rerun_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_raw_market_rerun_detail_latest.csv`
- detail_rows: `808`
