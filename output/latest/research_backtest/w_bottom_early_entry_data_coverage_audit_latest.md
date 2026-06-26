# W-Bottom Early-Entry Data Coverage Audit

- generated_at: `2026-06-26 18:50:50 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- scope: right-low early-entry W-bottom research data coverage only.
- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.

## Price History Coverage

- price history files with dates: `2373`
- price rows: `444844`
- global date range: `20250407` to `20260624`
- files with at least 180 observed trading dates: `1054`
- earliest 180th observed date across files: `20260105`

## W-Bottom Signal Windows

| artifact | rows | unique signals | min date | max date | months |
| --- | --- | --- | --- | --- | --- |
| `nearest_micro_detail_signal_window` | 588 | 588 | 20260105 | 20260623 | 6 |
| `combined_variant_signal_window` | 372 | 372 | 20260105 | 20260623 | 6 |
| `split_variant_early_entry_signal_window` | 2232 | 372 | 20260105 | 20260623 | 6 |
| `parameter_grid_variant_signal_window` | 2976 | 372 | 20260105 | 20260623 | 6 |

## `smooth_right_rebound_5_20` Monthly Maturity

| month | sample | evaluated | mature | win | neutral | loss | incomplete | maturity status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01 | 13 | 13 | 9 | 5 | 4 | 4 | 0 | `partially_mature` |
| 2026-02 | 4 | 4 | 3 | 1 | 1 | 2 | 0 | `partially_mature` |
| 2026-03 | 3 | 3 | 1 | 1 | 2 | 0 | 0 | `partially_mature` |
| 2026-04 | 7 | 5 | 4 | 4 | 1 | 0 | 2 | `partially_mature` |
| 2026-05 | 5 | 0 | 0 | 0 | 0 | 0 | 5 | `future_window_incomplete` |
| 2026-06 | 8 | 0 | 0 | 0 | 0 | 0 | 8 | `future_window_incomplete` |

## Conclusion

- promotion_readiness: `blocked_data_window_too_short`
- blocker_reason: `need_longer_historical_price_backfill_or_more_future_mature_months_before_promotion_review`
- mature signal months for `smooth_right_rebound_5_20`: `4`
- months with mature sample >= 5: `1`
- months with mature sample >= 10: `0`
- Interpretation: the current W-bottom strict smooth/rebound result is a useful research lead, but the available data window is too short for production promotion.
- Required follow-up owner: `research_backtest_data_governance` for longer historical input coverage or future mature-month accumulation.
