# W-Bottom Early-Entry Outcome Diagnostics

- generated_at: `2026-06-26 23:51:16 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- purpose: separate +10% wins, +5%-then-back-to-5% neutral rows, and losses for the right-low early-entry model.
- rates: `win_rate_excl_neutral_pct` excludes neutral rows from the win/loss denominator; `neutral_rate_evaluated_pct` uses win+neutral+loss as denominator.

## Variant Neutral Rule Candidate Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | delta_win_rate_pct_vs_all | delta_neutral_rate_pct_vs_all | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 53 | 29 | 28 | 24 | 54.7170 | 34.5679 | 18.0632 | 5.5844 | improves_win_but_neutral_watch |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 45 | 24 | 26 | 21 | 53.3333 | 36.6197 | 16.6796 | 7.6362 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_smooth | 136 | 116 | 78 | 39 | 38 | 39 | 50.0000 | 32.7586 | 13.3462 | 3.7751 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_exclude_wv | 358 | 311 | 221 | 108 | 90 | 113 | 48.8688 | 28.9389 | 12.2150 | -0.0446 | candidate_improves_win_without_more_neutral |
| smooth_right_rebound_5_20_near_neckline | 102 | 86 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | 9.2479 | 0.0863 | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20 | 172 | 142 | 96 | 44 | 46 | 52 | 45.8333 | 32.3944 | 9.1796 | 3.4108 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_red_ratio_gt_first | 382 | 327 | 227 | 104 | 100 | 123 | 45.8150 | 30.5810 | 9.1612 | 1.5975 | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | 8.9603 | 2.3418 | improves_win_but_neutral_watch |
| smooth_price_le40_right_rebound_5_20 | 158 | 128 | 87 | 39 | 41 | 48 | 44.8276 | 32.0312 | 8.1738 | 3.0477 | improves_win_but_neutral_watch |
| core_mainstream_price_le40 | 799 | 683 | 478 | 208 | 205 | 270 | 43.5146 | 30.0146 | 6.8609 | 1.0311 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_volume_gte1_5 | 395 | 337 | 229 | 99 | 108 | 130 | 43.2314 | 32.0475 | 6.5777 | 3.0640 | improves_win_but_neutral_watch |
| core_mainstream | 914 | 791 | 555 | 234 | 236 | 321 | 42.1622 | 29.8357 | 5.5084 | 0.8521 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_red_delta_gte10 | 174 | 147 | 98 | 41 | 49 | 57 | 41.8367 | 33.3333 | 5.1830 | 4.3498 | improves_win_but_neutral_watch |
| near_neckline_m5_to_0 | 523 | 453 | 326 | 134 | 127 | 192 | 41.1043 | 28.0353 | 4.4505 | -0.9482 | reduces_neutral_only |
| smooth_rounded_w_like | 286 | 237 | 167 | 67 | 70 | 100 | 40.1198 | 29.5359 | 3.4660 | 0.5523 | mixed_small_win_improvement |
| slope_break_discontinuous | 334 | 286 | 196 | 78 | 90 | 118 | 39.7959 | 31.4685 | 3.1421 | 2.4850 | mixed_small_win_improvement |
| second_red_ratio_gt_first | 799 | 685 | 479 | 189 | 206 | 290 | 39.4572 | 30.0730 | 2.8034 | 1.0895 | mixed_small_win_improvement |
| second_red_delta_gte10 | 378 | 320 | 218 | 85 | 102 | 133 | 38.9908 | 31.8750 | 2.3371 | 2.8915 | mixed_small_win_improvement |
| right_rebound_5_20 | 1088 | 939 | 667 | 260 | 272 | 407 | 38.9805 | 28.9670 | 2.3267 | -0.0165 | reduces_neutral_only |
| bottom_quartile_level | 1098 | 923 | 637 | 248 | 286 | 389 | 38.9325 | 30.9859 | 2.2787 | 2.0024 | mixed_small_win_improvement |
| price_position_le_25 | 1100 | 925 | 638 | 248 | 287 | 390 | 38.8715 | 31.0270 | 2.2177 | 2.0435 | mixed_small_win_improvement |
| exclude_wv_multiple_turn | 798 | 691 | 494 | 189 | 197 | 305 | 38.2591 | 28.5094 | 1.6053 | -0.4741 | reduces_neutral_only |
| second_arc_volume_gte1_5 | 786 | 692 | 487 | 183 | 205 | 304 | 37.5770 | 29.6243 | 0.9232 | 0.6408 | mixed_small_win_improvement |
| price_position_le_40 | 1517 | 1292 | 913 | 341 | 379 | 572 | 37.3494 | 29.3344 | 0.6956 | 0.3508 | mixed_small_win_improvement |
| bottom_or_low_level | 1633 | 1404 | 997 | 370 | 407 | 627 | 37.1113 | 28.9886 | 0.4576 | 0.0051 | mixed_small_win_improvement |
| all_rows | 1691 | 1456 | 1034 | 379 | 422 | 655 | 36.6538 | 28.9835 | 0.0000 | 0.0000 | baseline_reference |
| sharp_v_bottom_risk | 178 | 168 | 131 | 44 | 37 | 87 | 33.5878 | 22.0238 | -3.0660 | -6.9597 | reduces_neutral_only |
| below_neckline_5_to_30 | 1016 | 868 | 611 | 192 | 257 | 419 | 31.4239 | 29.6083 | -5.2299 | 0.6248 | not_better_than_all_same_event |
| non_mainstream | 777 | 665 | 479 | 145 | 186 | 334 | 30.2714 | 27.9699 | -6.3824 | -1.0136 | reduces_neutral_only |

## Variant Outcome Feature Profiles

| segment_id | sample_size | avg_price_position_252_pct | median_price_position_252_pct | avg_second_arc_volume_ratio | avg_red_ratio_delta_pct | avg_neckline_distance_pct | avg_signal_rebound_from_right_low_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| outcome_win | 379 | 21.4879 | 19.3277 | 1.7356 | 0.7706 | -10.2856 | 7.4746 |
| outcome_neutral | 422 | 21.0874 | 18.3096 | 1.7227 | 0.4076 | -9.4812 | 7.1668 |
| outcome_loss | 655 | 24.0109 | 21.5827 | 1.6535 | -0.5520 | -8.7871 | 7.1878 |

## Strict Smooth-Rebound Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 172 | 142 | 96 | 44 | 46 | 52 | 45.8333 | 32.3944 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_price_le40_right_rebound_5_20 | 158 | 128 | 87 | 39 | 41 | 48 | 44.8276 | 32.0312 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 53 | 29 | 28 | 24 | 54.7170 | 34.5679 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 45 | 24 | 26 | 21 | 53.3333 | 36.6197 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_near_neckline | 102 | 86 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | medium_mature_sample_research_only | improves_win_but_neutral_watch |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This diagnostic does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Strong-looking segments are research candidates only; they are not production rules.
