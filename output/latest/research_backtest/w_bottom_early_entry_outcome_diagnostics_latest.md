# W-Bottom Early-Entry Outcome Diagnostics

- generated_at: `2026-06-26 16:58:37 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- purpose: separate +10% wins, +5%-then-back-to-5% neutral rows, and losses for the right-low early-entry model.
- rates: `win_rate_excl_neutral_pct` excludes neutral rows from the win/loss denominator; `neutral_rate_evaluated_pct` uses win+neutral+loss as denominator.

## Variant Neutral Rule Candidate Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | delta_win_rate_pct_vs_all | delta_neutral_rate_pct_vs_all | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_rounded_w_like | 64 | 42 | 30 | 15 | 12 | 15 | 50.0000 | 28.5714 | 10.2273 | 0.7026 | improves_win_but_neutral_watch |
| second_red_delta_gte10 | 84 | 47 | 30 | 14 | 17 | 16 | 46.6667 | 36.1702 | 6.8939 | 8.3014 | improves_win_but_neutral_watch |
| right_rebound_5_20 | 236 | 154 | 104 | 48 | 50 | 56 | 46.1538 | 32.4675 | 6.3811 | 4.5987 | improves_win_but_neutral_watch |
| core_mainstream_price_le40 | 157 | 99 | 65 | 30 | 34 | 35 | 46.1538 | 34.3434 | 6.3811 | 6.4746 | improves_win_but_neutral_watch |
| second_red_ratio_gt_first | 185 | 121 | 76 | 35 | 45 | 41 | 46.0526 | 37.1901 | 6.2799 | 9.3212 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_red_ratio_gt_first | 83 | 53 | 31 | 14 | 22 | 17 | 45.1613 | 41.5094 | 5.3886 | 13.6406 | improves_win_but_neutral_watch |
| near_neckline_m5_to_0 | 137 | 102 | 72 | 32 | 30 | 40 | 44.4444 | 29.4118 | 4.6717 | 1.5429 | mixed_small_win_improvement |
| core_mainstream | 211 | 146 | 101 | 44 | 45 | 57 | 43.5644 | 30.8219 | 3.7916 | 2.9531 | mixed_small_win_improvement |
| price_position_le_40 | 298 | 179 | 126 | 52 | 53 | 74 | 41.2698 | 29.6089 | 1.4971 | 1.7401 | mixed_small_win_improvement |
| exclude_wv_multiple_turn | 160 | 103 | 78 | 32 | 25 | 46 | 41.0256 | 24.2718 | 1.2529 | -3.5970 | reduces_neutral_only |
| bottom_or_low_level | 340 | 217 | 156 | 64 | 61 | 92 | 41.0256 | 28.1106 | 1.2529 | 0.2417 | mixed_small_win_improvement |
| all_rows | 372 | 244 | 176 | 70 | 68 | 106 | 39.7727 | 27.8689 | 0.0000 | 0.0000 | baseline_reference |
| price_position_le_25 | 191 | 112 | 72 | 26 | 40 | 46 | 36.1111 | 35.7143 | -3.6616 | 7.8454 | not_better_than_all_same_event |
| bottom_quartile_level | 191 | 112 | 72 | 26 | 40 | 46 | 36.1111 | 35.7143 | -3.6616 | 7.8454 | not_better_than_all_same_event |
| non_mainstream | 161 | 98 | 75 | 26 | 23 | 49 | 34.6667 | 23.4694 | -5.1061 | -4.3995 | reduces_neutral_only |
| slope_break_discontinuous | 76 | 48 | 36 | 12 | 12 | 24 | 33.3333 | 25.0000 | -6.4394 | -2.8689 | reduces_neutral_only |
| below_neckline_5_to_30 | 204 | 124 | 90 | 30 | 34 | 60 | 33.3333 | 27.4194 | -6.4394 | -0.4495 | reduces_neutral_only |
| second_arc_volume_gte1_5 | 150 | 105 | 76 | 25 | 29 | 51 | 32.8947 | 27.6190 | -6.8780 | -0.2498 | reduces_neutral_only |

## Variant Outcome Feature Profiles

| segment_id | sample_size | avg_price_position_252_pct | median_price_position_252_pct | avg_second_arc_volume_ratio | avg_red_ratio_delta_pct | avg_neckline_distance_pct | avg_signal_rebound_from_right_low_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| outcome_win | 70 | 30.8642 | 32.2404 | 1.5362 | 0.6258 | -5.7308 | 7.1670 |
| outcome_neutral | 68 | 26.0336 | 21.5838 | 1.5911 | 2.6019 | -6.9946 | 6.7151 |
| outcome_loss | 106 | 29.7486 | 29.3295 | 1.6220 | -1.6725 | -8.0696 | 6.6052 |

## Strict Smooth-Rebound Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 40 | 25 | 17 | 11 | 8 | 6 | 64.7059 | 32.0000 | directional_only_below_promotion_review_size | too_small_for_parameter_decision |
| smooth_price_le40_right_rebound_5_20 | 33 | 18 | 13 | 8 | 5 | 5 | 61.5385 | 27.7778 | low_mature_sample_research_only | too_small_for_parameter_decision |
| smooth_core_mainstream_right_rebound_5_20 | 22 | 16 | 10 | 7 | 6 | 3 | 70.0000 | 37.5000 | low_mature_sample_research_only | too_small_for_parameter_decision |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 17 | 11 | 7 | 4 | 4 | 3 | 57.1429 | 36.3636 | low_mature_sample_research_only | too_small_for_parameter_decision |
| smooth_right_rebound_5_20_red_ratio_gt_first | 25 | 15 | 9 | 5 | 6 | 4 | 55.5556 | 40.0000 | low_mature_sample_research_only | too_small_for_parameter_decision |
| smooth_right_rebound_5_20_near_neckline | 22 | 17 | 12 | 7 | 5 | 5 | 58.3333 | 29.4118 | low_mature_sample_research_only | too_small_for_parameter_decision |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This diagnostic does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Strong-looking segments are research candidates only; they are not production rules.
