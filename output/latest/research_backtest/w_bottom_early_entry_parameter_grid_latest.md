# W-Bottom Early-Entry Parameter Grid

- generated_at: `2026-06-26 23:46:43 Asia/Taipei`
- source_research_id: `w_bottom_split_entry_outcome_backtest`
- production impact: `none`
- price convention: entry uses next trading day's open; exit uses exit day's close.
- surface: `w_bottom_right_low_early_entry` only.
- purpose: compare second-low early-entry conditions before any production model promotion.
- added outcome rules: `take_profit_10pct_close_40d` and `tp10_or_neutral_after_5pct_close_40d`.
- neutral rule: after a close return first exceeds +5%, a later close back to +5% before +10% remains in `sample_size` but is excluded from win/loss denominator.

## Top Variant Rows

| outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | neutral_count | neutral_rate_pct | avg_return_pct | median_return_pct | delta_success_rate_pct_vs_all | delta_avg_return_pct_vs_all | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 69.7674 | 0 | 0.0000 | 0.4039 | 2.1572 | 36.2510 | 1.0739 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 63.3803 | 0 | 0.0000 | 0.3958 | 0.8889 | 29.8638 | 1.0659 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 61.7284 | 0 | 0.0000 | 0.1579 | 0.8889 | 28.2119 | 0.8280 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 60.2410 | 0 | 0.0000 | 0.0642 | 1.2384 | 26.7245 | 0.7342 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_price_le40_right_rebound_5_20 | 158 | 128 | 59.3750 | 0 | 0.0000 | 0.0320 | 0.8903 | 25.8585 | 0.7021 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20 | 172 | 142 | 59.1549 | 0 | 0.0000 | -0.0211 | 0.8903 | 25.6384 | 0.6490 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 56.3380 | 0 | 0.0000 | 5.3175 | 3.0000 | 16.7089 | 4.5492 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 81 | 55.5556 | 0 | 0.0000 | 5.3924 | 1.3627 | 13.3235 | 4.4358 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 91 | 54.9451 | 0 | 0.0000 | 4.9967 | 1.0638 | 12.7130 | 4.0401 | medium_mature_sample_research_only |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 53 | 54.7170 | 28 | 29.4737 | 3.3359 | 10.2767 | 18.0632 | 2.1320 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 54.3210 | 0 | 0.0000 | 4.9891 | 1.7708 | 14.6919 | 4.2208 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 76 | 53.9474 | 0 | 0.0000 | 5.7587 | 2.9223 | 12.4615 | 4.9328 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 346 | 53.7572 | 0 | 0.0000 | 5.6751 | 0.9009 | 11.5251 | 4.7185 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 346 | 53.7572 | 0 | 0.0000 | 5.6751 | 0.9009 | 11.5251 | 4.7185 | medium_mature_sample_research_only |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 45 | 53.3333 | 26 | 30.5882 | 3.6998 | 10.2767 | 16.6796 | 2.4959 | medium_mature_sample_research_only |
| take_profit_10pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 53.0864 | 0 | 0.0000 | 4.7071 | 10.1338 | 16.6166 | 2.4316 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 83 | 53.0120 | 0 | 0.0000 | 1.2491 | 0.1414 | 11.8213 | 1.2423 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 311 | 52.4116 | 0 | 0.0000 | 8.0543 | 0.4071 | 12.7825 | 7.2860 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 311 | 52.4116 | 0 | 0.0000 | 8.0543 | 0.4071 | 12.7825 | 7.2860 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 332 | 52.4096 | 0 | 0.0000 | 6.6293 | 1.2202 | 10.9238 | 5.8033 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 332 | 52.4096 | 0 | 0.0000 | 6.6293 | 1.2202 | 10.9238 | 5.8033 | medium_mature_sample_research_only |
| take_profit_10pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 52.1127 | 0 | 0.0000 | 5.0272 | 10.0427 | 15.6429 | 2.7517 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 86 | 51.1628 | 0 | 0.0000 | 5.0172 | 1.4823 | 9.6769 | 4.1913 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 94 | 51.0638 | 0 | 0.0000 | 3.7154 | 0.6647 | 9.5780 | 2.8894 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 158 | 128 | 50.7812 | 0 | 0.0000 | 2.2788 | 0.3133 | 11.1521 | 1.5105 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 50.6024 | 0 | 0.0000 | 2.8015 | 0.3425 | 10.9733 | 2.0332 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 93 | 50.5376 | 0 | 0.0000 | 1.2454 | 0.1048 | 9.3469 | 1.2386 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 97 | 50.5155 | 0 | 0.0000 | 3.2452 | 0.2793 | 8.2834 | 2.2886 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 50.0000 | 0 | 0.0000 | 3.1972 | 0.0996 | 10.3709 | 2.4289 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 90 | 50.0000 | 0 | 0.0000 | 2.9555 | 0.1396 | 7.7679 | 1.9989 | medium_mature_sample_research_only |

## Candidate Review Rows

| outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | neutral_count | neutral_rate_pct | avg_return_pct | median_return_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 69.7674 | 0 | 0.0000 | 0.4039 | 2.1572 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 63.3803 | 0 | 0.0000 | 0.3958 | 0.8889 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 61.7284 | 0 | 0.0000 | 0.1579 | 0.8889 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 60.2410 | 0 | 0.0000 | 0.0642 | 1.2384 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_price_le40_right_rebound_5_20 | 158 | 128 | 59.3750 | 0 | 0.0000 | 0.0320 | 0.8903 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20 | 172 | 142 | 59.1549 | 0 | 0.0000 | -0.0211 | 0.8903 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 53 | 54.7170 | 28 | 29.4737 | 3.3359 | 10.2767 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 56.3380 | 0 | 0.0000 | 5.3175 | 3.0000 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 45 | 53.3333 | 26 | 30.5882 | 3.6998 | 10.2767 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 53.0864 | 0 | 0.0000 | 4.7071 | 10.1338 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 71 | 52.1127 | 0 | 0.0000 | 5.0272 | 10.0427 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 81 | 54.3210 | 0 | 0.0000 | 4.9891 | 1.7708 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 81 | 55.5556 | 0 | 0.0000 | 5.3924 | 1.3627 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 311 | 52.4116 | 0 | 0.0000 | 8.0543 | 0.4071 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 311 | 52.4116 | 0 | 0.0000 | 8.0543 | 0.4071 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 91 | 54.9451 | 0 | 0.0000 | 4.9967 | 1.0638 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 76 | 53.9474 | 0 | 0.0000 | 5.7587 | 2.9223 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | core_mainstream_price_le40_exclude_wv | 358 | 221 | 48.8688 | 90 | 25.1397 | 8.2058 | 5.2632 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | core_mainstream_price_le40_volume_exclude_wv | 358 | 221 | 48.8688 | 90 | 25.1397 | 8.2058 | 5.2632 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 83 | 53.0120 | 0 | 0.0000 | 1.2491 | 0.1414 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | core_mainstream_price_le40_exclude_wv | 358 | 311 | 48.2315 | 0 | 0.0000 | 10.5428 | 5.1056 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | core_mainstream_price_le40_volume_exclude_wv | 358 | 311 | 48.2315 | 0 | 0.0000 | 10.5428 | 5.1056 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 346 | 53.7572 | 0 | 0.0000 | 5.6751 | 0.9009 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 346 | 53.7572 | 0 | 0.0000 | 5.6751 | 0.9009 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 158 | 128 | 50.7812 | 0 | 0.0000 | 2.2788 | 0.3133 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 50.6024 | 0 | 0.0000 | 2.8015 | 0.3425 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | core_mainstream_price_le40_exclude_wv | 358 | 332 | 52.4096 | 0 | 0.0000 | 6.6293 | 1.2202 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 358 | 332 | 52.4096 | 0 | 0.0000 | 6.6293 | 1.2202 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 50.0000 | 0 | 0.0000 | 3.1972 | 0.0996 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 86 | 51.1628 | 0 | 0.0000 | 5.0172 | 1.4823 | candidate_for_manual_promotion_review |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This grid does not modify production conditions, scoring, ranking, PDFs, or baselines.
- Neutral outcomes remain research-only and must not be treated as production approval.
- Strong-looking rows are promotion-review candidates only; they are not production rules.
