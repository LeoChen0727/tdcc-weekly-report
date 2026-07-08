# Volume Range Breakout V2 Overlap Sensitivity

- research_id: `volume_range_breakout_v2_overlap_sensitivity`
- artifact_version: `volume_range_breakout_v2_overlap_sensitivity_20260708`
- source: `output\latest\research_backtest\volume_range_breakout_v2_deep_low_base_matrix_detail_latest.csv`
- status: research-only; not a production registry, daily adapter, or PDF change.
- purpose: separate event-level metrics from same-stock non-overlap metrics.

## Baseline Rows

| selection_basis        |   sample_size |   unique_stocks |   suppressed_same_stock_overlap_count |   overlap_pair_count |   win_rate_pct |   loss_rate_pct |   avg_return_pct |   median_return_pct |
|:-----------------------|--------------:|----------------:|--------------------------------------:|---------------------:|---------------:|----------------:|-----------------:|--------------------:|
| event_level_all_events |           808 |             432 |                                     0 |                  330 |        52.4752 |         47.0297 |           4.9893 |              1.3482 |
| first_event_per_stock  |           432 |             432 |                                   376 |                    0 |        49.7685 |         49.7685 |           3.3272 |              0      |
| same_stock_non_overlap |           574 |             432 |                                   234 |                    0 |        50.6969 |         48.7805 |           4.336  |              0.5599 |

## Same-Stock Suppression Examples

|   stock_id | stock_name   |   signal_date |   entry_date |   exit_date |   return_pct | suppressed_by_source_event_key                                                            |   suppressed_by_entry_date |   suppressed_by_exit_date |
|-----------:|:-------------|--------------:|-------------:|------------:|-------------:|:------------------------------------------------------------------------------------------|---------------------------:|--------------------------:|
|       1256 | 鮮活果汁-KY  |      20250902 |     20250904 |    20250923 |      -0.8671 | 1256|20250901|20250902|next_day_break_signal_high_confirmed|20250903|20250922|157.5|174.0 |                   20250903 |                  20250922 |
|       1303 | 南亞         |      20251113 |     20251117 |    20251126 |     -11.6725 | 1303|20251112|20251113|next_day_break_signal_high_confirmed|20251114|20251127|52.1|56.2   |                   20251114 |                  20251127 |
|       1314 | 中石化       |      20251105 |     20251107 |    20251111 |     -21.5238 | 1314|20251104|20251105|next_day_break_signal_high_confirmed|20251106|20251119|9.37|8.2    |                   20251106 |                  20251119 |
|       1409 | 新纖         |      20260528 |     20260601 |    20260612 |       1.7964 | 1409|20260527|20260528|next_day_break_signal_high_confirmed|20260529|20260611|22.8|24.65  |                   20260529 |                  20260611 |
|       1409 | 新纖         |      20260529 |     20260602 |    20260615 |      -7.6225 | 1409|20260527|20260528|next_day_break_signal_high_confirmed|20260529|20260611|22.8|24.65  |                   20260529 |                  20260611 |
|       1504 | 東元         |      20250822 |     20250826 |    20250902 |     -12.1172 | 1504|20250821|20250822|next_day_break_signal_high_confirmed|20250825|20250905|71.8|68.0   |                   20250825 |                  20250905 |
|       1522 | 堤維西       |      20251027 |     20251029 |    20251105 |      -7.1    | 1522|20251022|20251023|next_day_break_signal_high_confirmed|20251027|20251107|47.95|45.2  |                   20251027 |                  20251107 |
|       1524 | 耿鼎         |      20251027 |     20251029 |    20251104 |      -7.485  | 1524|20251022|20251023|next_day_break_signal_high_confirmed|20251027|20251107|31.55|30.65 |                   20251027 |                  20251107 |
|       1528 | 恩德         |      20251226 |     20251230 |    20260113 |      -1.3363 | 1528|20251224|20251226|next_day_break_signal_high_confirmed|20251229|20260112|21.3|22.45  |                   20251229 |                  20260112 |
|       1528 | 恩德         |      20251229 |     20251231 |    20260107 |     -14.7541 | 1528|20251224|20251226|next_day_break_signal_high_confirmed|20251229|20260112|21.3|22.45  |                   20251229 |                  20260112 |
|       1563 | 巧新         |      20260527 |     20260529 |    20260611 |     -10.7143 | 1563|20260526|20260527|next_day_break_signal_high_confirmed|20260528|20260610|61.1|58.0   |                   20260528 |                  20260610 |
|       1568 | 倉佑         |      20260528 |     20260601 |    20260605 |     -12.6882 | 1568|20260526|20260527|next_day_break_signal_high_confirmed|20260528|20260610|41.25|38.0  |                   20260528 |                  20260610 |
