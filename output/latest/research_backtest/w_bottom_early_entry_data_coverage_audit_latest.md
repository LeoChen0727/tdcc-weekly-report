# W-Bottom Early-Entry Data Coverage Audit

- generated_at: `2026-06-26 23:51:16 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- scope: right-low early-entry W-bottom research data coverage only.
- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.

## Price History Coverage

- price history files with dates: `2389`
- price rows: `1032866`
- global date range: `20240102` to `20260626`
- files with at least 180 observed trading dates: `2020`
- earliest 180th observed date across files: `20240930`

## W-Bottom Signal Windows

| artifact | rows | unique signals | min date | max date | months |
| --- | --- | --- | --- | --- | --- |
| `nearest_micro_detail_signal_window` | 2537 | 2537 | 20240930 | 20260625 | 22 |
| `combined_variant_signal_window` | 1691 | 1691 | 20240930 | 20260625 | 22 |
| `split_variant_early_entry_signal_window` | 10146 | 1691 | 20240930 | 20260625 | 22 |
| `parameter_grid_variant_signal_window` | 13528 | 1691 | 20240930 | 20260625 | 22 |

## `smooth_right_rebound_5_20` Monthly Maturity

| month | sample | evaluated | mature | win | neutral | loss | incomplete | maturity status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-10 | 3 | 3 | 2 | 1 | 1 | 1 | 0 | `partially_mature` |
| 2024-11 | 4 | 4 | 4 | 2 | 0 | 2 | 0 | `partially_mature` |
| 2024-12 | 18 | 18 | 10 | 3 | 8 | 7 | 0 | `partially_mature` |
| 2025-01 | 8 | 8 | 4 | 1 | 4 | 3 | 0 | `partially_mature` |
| 2025-02 | 10 | 10 | 4 | 3 | 6 | 1 | 0 | `partially_mature` |
| 2025-03 | 8 | 8 | 8 | 2 | 0 | 6 | 0 | `partially_mature` |
| 2025-04 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | `partially_mature` |
| 2025-06 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | `partially_mature` |
| 2025-07 | 10 | 10 | 8 | 5 | 2 | 3 | 0 | `partially_mature` |
| 2025-08 | 9 | 9 | 7 | 5 | 2 | 2 | 0 | `partially_mature` |
| 2025-09 | 4 | 4 | 2 | 0 | 2 | 2 | 0 | `partially_mature` |
| 2025-10 | 2 | 2 | 1 | 0 | 1 | 1 | 0 | `partially_mature` |
| 2025-11 | 6 | 6 | 4 | 1 | 2 | 3 | 0 | `partially_mature` |
| 2025-12 | 9 | 9 | 4 | 2 | 5 | 2 | 0 | `partially_mature` |
| 2026-01 | 18 | 18 | 12 | 6 | 6 | 6 | 0 | `partially_mature` |
| 2026-02 | 7 | 7 | 6 | 1 | 1 | 5 | 0 | `partially_mature` |
| 2026-03 | 12 | 12 | 8 | 3 | 4 | 5 | 0 | `partially_mature` |
| 2026-04 | 14 | 12 | 10 | 8 | 2 | 2 | 2 | `partially_mature` |
| 2026-05 | 14 | 0 | 0 | 0 | 0 | 0 | 14 | `future_window_incomplete` |
| 2026-06 | 14 | 0 | 0 | 0 | 0 | 0 | 14 | `future_window_incomplete` |

## Conclusion

- promotion_readiness: `blocked_research_stability_sample_too_thin`
- blocker_reason: `input_coverage_extended_but_strict_segment_has_only_3_months_with_mature_ge10`
- mature signal months for `smooth_right_rebound_5_20`: `18`
- months with mature sample >= 5: `8`
- months with mature sample >= 10: `3`
- Interpretation: the approved official price backfill extends the W-bottom input and signal window, but the strict smooth/rebound segment remains research-only until stability and mature-sample thresholds are reviewed.
- Required follow-up owner: `research_backtest_data_governance` for continued coverage, stability, and mature-month validation.
