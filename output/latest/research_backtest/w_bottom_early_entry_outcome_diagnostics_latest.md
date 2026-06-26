# W-Bottom Early-Entry Outcome Diagnostics

- generated_at: `2026-06-26 21:31:47 Asia/Taipei`
- source_research_id: `w_bottom_early_entry_parameter_grid`
- production impact: `none`
- surface: `w_bottom_right_low_early_entry` only.
- purpose: separate +10% wins, +5%-then-back-to-5% neutral rows, and losses for the right-low early-entry model.
- rates: `win_rate_excl_neutral_pct` excludes neutral rows from the win/loss denominator; `neutral_rate_evaluated_pct` uses win+neutral+loss as denominator.

## Variant Neutral Rule Candidate Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | delta_win_rate_pct_vs_all | delta_neutral_rate_pct_vs_all | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 52 | 28 | 28 | 24 | 53.8462 | 35.0000 | 17.5002 | 5.9655 | improves_win_but_neutral_watch |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 44 | 23 | 26 | 21 | 52.2727 | 37.1429 | 15.9268 | 8.1084 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_smooth | 136 | 115 | 77 | 38 | 38 | 39 | 49.3506 | 33.0435 | 13.0047 | 4.0090 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_exclude_wv | 357 | 310 | 220 | 107 | 90 | 113 | 48.6364 | 29.0323 | 12.2904 | -0.0022 | candidate_improves_win_without_more_neutral |
| smooth_right_rebound_5_20_near_neckline | 102 | 86 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | 9.5557 | 0.0353 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_red_ratio_gt_first | 379 | 327 | 227 | 104 | 100 | 123 | 45.8150 | 30.5810 | 9.4690 | 1.5466 | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | 9.2681 | 2.2908 | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20 | 172 | 141 | 95 | 43 | 46 | 52 | 45.2632 | 32.6241 | 8.9172 | 3.5896 | improves_win_but_neutral_watch |
| smooth_price_le40_right_rebound_5_20 | 158 | 127 | 86 | 38 | 41 | 48 | 44.1860 | 32.2835 | 7.8401 | 3.2490 | improves_win_but_neutral_watch |
| core_mainstream_price_le40 | 795 | 681 | 476 | 206 | 205 | 270 | 43.2773 | 30.1028 | 6.9313 | 1.0683 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_volume_gte1_5 | 392 | 336 | 228 | 98 | 108 | 130 | 42.9825 | 32.1429 | 6.6365 | 3.1084 | improves_win_but_neutral_watch |
| core_mainstream | 910 | 788 | 552 | 231 | 236 | 321 | 41.8478 | 29.9492 | 5.5019 | 0.9148 | improves_win_but_neutral_watch |
| core_mainstream_price_le40_red_delta_gte10 | 173 | 147 | 98 | 41 | 49 | 57 | 41.8367 | 33.3333 | 5.4908 | 4.2989 | improves_win_but_neutral_watch |
| near_neckline_m5_to_0 | 521 | 450 | 324 | 132 | 126 | 192 | 40.7407 | 28.0000 | 4.3948 | -1.0345 | reduces_neutral_only |
| smooth_rounded_w_like | 285 | 236 | 166 | 66 | 70 | 100 | 39.7590 | 29.6610 | 3.4131 | 0.6265 | mixed_small_win_improvement |
| slope_break_discontinuous | 332 | 285 | 195 | 77 | 90 | 118 | 39.4872 | 31.5789 | 3.1412 | 2.5445 | mixed_small_win_improvement |
| second_red_ratio_gt_first | 794 | 681 | 476 | 186 | 205 | 290 | 39.0756 | 30.1028 | 2.7297 | 1.0683 | mixed_small_win_improvement |
| right_rebound_5_20 | 1084 | 934 | 663 | 256 | 271 | 407 | 38.6124 | 29.0150 | 2.2664 | -0.0195 | reduces_neutral_only |
| bottom_quartile_level | 1092 | 918 | 633 | 244 | 285 | 389 | 38.5466 | 31.0458 | 2.2006 | 2.0113 | mixed_small_win_improvement |
| price_position_le_25 | 1094 | 920 | 634 | 244 | 286 | 390 | 38.4858 | 31.0870 | 2.1398 | 2.0525 | mixed_small_win_improvement |
| second_red_delta_gte10 | 375 | 317 | 216 | 83 | 101 | 133 | 38.4259 | 31.8612 | 2.0800 | 2.8267 | mixed_small_win_improvement |
| exclude_wv_multiple_turn | 795 | 689 | 492 | 187 | 197 | 305 | 38.0081 | 28.5922 | 1.6622 | -0.4423 | reduces_neutral_only |
| price_position_le_40 | 1510 | 1287 | 909 | 337 | 378 | 572 | 37.0737 | 29.3706 | 0.7277 | 0.3361 | mixed_small_win_improvement |
| second_arc_volume_gte1_5 | 783 | 688 | 483 | 179 | 205 | 304 | 37.0600 | 29.7965 | 0.7141 | 0.7620 | mixed_small_win_improvement |
| bottom_or_low_level | 1626 | 1398 | 992 | 365 | 406 | 627 | 36.7944 | 29.0415 | 0.4484 | 0.0070 | mixed_small_win_improvement |
| all_rows | 1684 | 1450 | 1029 | 374 | 421 | 655 | 36.3460 | 29.0345 | 0.0000 | 0.0000 | baseline_reference |
| sharp_v_bottom_risk | 178 | 168 | 131 | 44 | 37 | 87 | 33.5878 | 22.0238 | -2.7582 | -7.0107 | reduces_neutral_only |
| below_neckline_5_to_30 | 1012 | 866 | 609 | 190 | 257 | 419 | 31.1987 | 29.6767 | -5.1473 | 0.6422 | not_better_than_all_same_event |
| non_mainstream | 774 | 662 | 477 | 143 | 185 | 334 | 29.9790 | 27.9456 | -6.3669 | -1.0889 | reduces_neutral_only |

## Variant Outcome Feature Profiles

| segment_id | sample_size | avg_price_position_252_pct | median_price_position_252_pct | avg_second_arc_volume_ratio | avg_red_ratio_delta_pct | avg_neckline_distance_pct | avg_signal_rebound_from_right_low_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| outcome_win | 374 | 21.5179 | 19.3792 | 1.7339 | 0.7463 | -10.3179 | 7.4523 |
| outcome_neutral | 421 | 21.1020 | 18.3857 | 1.7239 | 0.3819 | -9.5024 | 7.1544 |
| outcome_loss | 655 | 24.0109 | 21.5827 | 1.6535 | -0.5520 | -8.7871 | 7.1878 |

## Strict Smooth-Rebound Segments

| segment_id | sample_size | evaluated_sample_size | mature_sample_size | win_count | neutral_count | loss_count | win_rate_excl_neutral_pct | neutral_rate_evaluated_pct | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smooth_right_rebound_5_20 | 172 | 141 | 95 | 43 | 46 | 52 | 45.2632 | 32.6241 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_price_le40_right_rebound_5_20 | 158 | 127 | 86 | 38 | 41 | 48 | 44.1860 | 32.2835 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 52 | 28 | 28 | 24 | 53.8462 | 35.0000 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 44 | 23 | 26 | 21 | 52.2727 | 37.1429 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 57 | 26 | 26 | 31 | 45.6140 | 31.3253 | medium_mature_sample_research_only | improves_win_but_neutral_watch |
| smooth_right_rebound_5_20_near_neckline | 102 | 86 | 61 | 28 | 25 | 33 | 45.9016 | 29.0698 | medium_mature_sample_research_only | improves_win_but_neutral_watch |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This diagnostic does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.
- Strong-looking segments are research candidates only; they are not production rules.
