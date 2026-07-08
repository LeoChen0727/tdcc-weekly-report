# volume_range_breakout v2 deep low-base matrix

Research-only artifact. This does not change production model conditions, ranking, scoring, registry, or PDF behavior.

Population basis: current v2 raw-market events, which still require previous-60-day high breakout and next-day continuation.
Purpose: test the user's stricter low-base meaning using 120/240-day distance from low and 60/120-day range width.

Coverage diagnostic rows are included because 120/240-day lookback windows may be unavailable for some source events.

Important boundary: if deep-low samples are too thin or weak inside this population, that does not disprove a future low-base model without the current 60d-high continuation gate.

## Baseline And Deep-Low Rows

| condition_set_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | sample_status | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_prev60_high_next_day_continuation | 808 | 52.48 | 47.03 | 4.9893 | 1.3482 | reviewable_sample | baseline_reference |
| coverage_off120_available | 525 | 48.19 | 51.43 | 3.9719 | -0.7643 | reviewable_sample | data_coverage_diagnostic_not_condition |
| coverage_range120_available | 525 | 48.19 | 51.43 | 3.9719 | -0.7643 | reviewable_sample | data_coverage_diagnostic_not_condition |
| coverage_off240_available | 167 | 53.29 | 46.71 | 6.1819 | 2.3585 | thin_but_reviewable_sample | data_coverage_diagnostic_not_condition |
| off120_le40_range60_le35 | 121 | 33.88 | 66.12 | 0.0263 | -4.6632 | thin_but_reviewable_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range120_le45 | 108 | 32.41 | 67.59 | -0.7683 | -4.7594 | thin_but_reviewable_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range120_le35 | 94 | 30.85 | 69.15 | -1.8298 | -4.8832 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range60_le25 | 85 | 36.47 | 63.53 | 0.7762 | -3.3019 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range60_le35 | 68 | 27.94 | 72.06 | -2.3261 | -5.2291 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range120_le45 | 66 | 27.27 | 72.73 | -2.8625 | -5.4147 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range60_le25 | 65 | 27.69 | 72.31 | -2.2708 | -5.0736 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range120_le35 | 60 | 25.0 | 75.0 | -3.6527 | -5.7716 | thin_sample | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range120_le25 | 45 | 28.89 | 71.11 | -2.7502 | -5.4449 | very_thin_sample | very_thin_sample_review_only |
| off120_le30_range120_le25 | 40 | 22.5 | 77.5 | -3.8813 | -6.0634 | very_thin_sample | very_thin_sample_review_only |
| off240_le40_range60_le35 | 22 | 31.82 | 68.18 | -0.6282 | -3.521 | very_thin_sample | very_thin_sample_review_only |
| off240_le40_range120_le45 | 21 | 33.33 | 66.67 | -0.5059 | -3.8462 | very_thin_sample | very_thin_sample_review_only |
| off240_le40_range120_le35 | 20 | 30.0 | 70.0 | -2.3034 | -4.4599 | very_thin_sample | very_thin_sample_review_only |
| off120_le20_range60_le25 | 16 | 6.25 | 93.75 | -7.4526 | -6.1733 | insufficient_sample | insufficient_sample_do_not_use |
| off120_le20_range60_le35 | 16 | 6.25 | 93.75 | -7.4526 | -6.1733 | insufficient_sample | insufficient_sample_do_not_use |
| off120_le20_range120_le35 | 16 | 6.25 | 93.75 | -7.4526 | -6.1733 | insufficient_sample | insufficient_sample_do_not_use |
| off120_le20_range120_le45 | 16 | 6.25 | 93.75 | -7.4526 | -6.1733 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le40_range60_le25 | 16 | 37.5 | 62.5 | 1.8587 | -2.7667 | insufficient_sample | insufficient_sample_do_not_use |
| off120_le20_range120_le25 | 14 | 7.14 | 92.86 | -8.217 | -6.8803 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le30_range60_le25 | 11 | 27.27 | 72.73 | -0.78 | -5.0736 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le30_range60_le35 | 11 | 27.27 | 72.73 | -0.78 | -5.0736 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le30_range120_le35 | 11 | 27.27 | 72.73 | -0.78 | -5.0736 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le30_range120_le45 | 11 | 27.27 | 72.73 | -0.78 | -5.0736 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le40_range120_le25 | 10 | 30.0 | 70.0 | -1.1953 | -4.1676 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le30_range120_le25 | 8 | 25.0 | 75.0 | -1.295 | -4.1676 | insufficient_sample | insufficient_sample_do_not_use |
| off240_le20_range60_le25 | 1 | 0.0 | 100.0 | -2.6432 | -2.6432 | insufficient_sample | insufficient_sample_do_not_use |

## Deep-Low Rows With At Least 20 Samples

| condition_set_id | sample_size | coverage_pct | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| off120_le40_range60_le25 | 85 | 10.52 | 36.47 | 63.53 | 0.7762 | -3.3019 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40 | 121 | 14.98 | 33.88 | 66.12 | 0.0263 | -4.6632 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range60_le35 | 121 | 14.98 | 33.88 | 66.12 | 0.0263 | -4.6632 | weaker_than_current_v2_do_not_promote_as_gate |
| off240_le40_range120_le45 | 21 | 2.6 | 33.33 | 66.67 | -0.5059 | -3.8462 | very_thin_sample_review_only |
| off240_le40 | 22 | 2.72 | 31.82 | 68.18 | -0.6282 | -3.521 | very_thin_sample_review_only |
| off240_le40_range60_le35 | 22 | 2.72 | 31.82 | 68.18 | -0.6282 | -3.521 | very_thin_sample_review_only |
| off120_le40_range120_le45 | 108 | 13.37 | 32.41 | 67.59 | -0.7683 | -4.7594 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range120_le35 | 94 | 11.63 | 30.85 | 69.15 | -1.8298 | -4.8832 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range60_le25 | 65 | 8.04 | 27.69 | 72.31 | -2.2708 | -5.0736 | weaker_than_current_v2_do_not_promote_as_gate |
| off240_le40_range120_le35 | 20 | 2.48 | 30.0 | 70.0 | -2.3034 | -4.4599 | very_thin_sample_review_only |
| off120_le30 | 68 | 8.42 | 27.94 | 72.06 | -2.3261 | -5.2291 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range60_le35 | 68 | 8.42 | 27.94 | 72.06 | -2.3261 | -5.2291 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le40_range120_le25 | 45 | 5.57 | 28.89 | 71.11 | -2.7502 | -5.4449 | very_thin_sample_review_only |
| off120_le30_range120_le45 | 66 | 8.17 | 27.27 | 72.73 | -2.8625 | -5.4147 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range120_le35 | 60 | 7.43 | 25.0 | 75.0 | -3.6527 | -5.7716 | weaker_than_current_v2_do_not_promote_as_gate |
| off120_le30_range120_le25 | 40 | 4.95 | 22.5 | 77.5 | -3.8813 | -6.0634 | very_thin_sample_review_only |

## Promotion Boundary

These rows are diagnostic and research-only. A production low-base breakout model still requires a separate raw producer/backtest that can remove or replace the current 60d-high continuation gate.
