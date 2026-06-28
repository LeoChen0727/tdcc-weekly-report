# W-Bottom Early-Entry Candidate Spec

- generated_at: `2026-06-27 15:58:36 Asia/Taipei`
- model_id: `w_bottom_right_side`
- surface_id: `w_bottom_right_low_early_entry`
- candidate_status: `current_best_research_candidate`
- selected_segment_id: `smooth_core_mainstream_right_rebound_5_20_bull`
- source_research_id: `w_bottom_market_regime_gated_review`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this spec does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Boundary

Early-entry only. This does not define W-bottom neckline breakout, inverse head-and-shoulders, or generic neckline breakout confirmation.

This spec is only for the W-bottom right-low early-entry candidate. W-bottom neckline breakout confirmation must be reviewed as a separate model surface.

## Candidate Conditions

- Market regime is `strong_bull` or `mild_bull`.
- Stock is `core_mainstream`.
- Path shape is `smooth_rounded_w_like`.
- `signal_rebound_from_right_low_pct` is 5 to 20: the signal close is 5% to 20% above the detected right-low price.

## Buy / Sell / Evaluation

- buy point: Buy next open after the right-low observation signal.
- sell and evaluation: Within 40 trading days after entry: first close return >= +10% is a win; if close return first exceeds +5% but later returns to <= +5% before +10%, record neutral and exclude it from pure win/loss; otherwise sell day-40 close and record loss if +10% was not reached.

## Evidence Line For Model Title

目前回測：純勝率 65.0%，含平局成功率 77.4%，已評估 31 筆，未成熟 13 筆；買點為右低點觀察訊號後下一交易日開盤，40 個交易日內以收盤 +10% / +5% 平局規則評估。

## Metrics

| metric | value |
| --- | ---: |
| sample_size | 44 |
| evaluated_sample_size | 31 |
| mature_sample_size | 20 |
| win_count | 13 |
| neutral_count | 11 |
| loss_count | 7 |
| incomplete_count | 13 |
| pure_win_rate_pct | 65.0000 |
| neutral_inclusive_success_rate_pct | 77.4194 |
| total_sample_win_or_neutral_rate_pct | 54.5455 |
| incomplete_rate_pct | 29.5455 |
| avg_return_pct | 2.9504 |
| median_return_pct | 4.7478 |
| unique_stock_count | 44 |
| max_rows_single_stock | 1 |
| max_single_stock_row_share_pct | 2.2727 |

## Next Review

Review chart quality for s03/s04 folders, then optimize buy/sell points; do not promote before a separate production model-change PR.
