# W-Bottom Early-Entry Parameter Grid

- generated_at: `2026-06-26 16:56:29 Asia/Taipei`
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
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_red_ratio_gt_first | 83 | 53 | 62.2642 | 0 | 0.0000 | 0.9897 | 0.5000 | 19.6412 | 1.2610 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_red | 83 | 53 | 62.2642 | 0 | 0.0000 | 0.9897 | 0.5000 | 19.6412 | 1.2610 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 33 | 30 | 60.0000 | 0 | 0.0000 | 1.0110 | 0.3128 | 17.2271 | 0.2418 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_exclude_wv | 63 | 40 | 57.5000 | 0 | 0.0000 | 0.8013 | 0.4133 | 14.8770 | 1.0726 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_exclude_wv | 63 | 40 | 57.5000 | 0 | 0.0000 | 0.8013 | 0.4133 | 14.8770 | 1.0726 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | right_rebound_5_20 | 236 | 154 | 57.1429 | 0 | 0.0000 | 0.0736 | 0.5146 | 14.5199 | 0.3449 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_right_rebound_5_20 | 40 | 37 | 56.7568 | 0 | 0.0000 | 1.2305 | 0.2809 | 13.9839 | 0.4613 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | 13.9427 | 1.1775 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_gte1_2 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | 13.9427 | 1.1775 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_gap_m5_p8_rebound_3_20 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | 13.9427 | 1.1775 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le25 | 95 | 61 | 55.7377 | 0 | 0.0000 | 0.3774 | 0.2845 | 13.1148 | 0.6487 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le30 | 114 | 70 | 55.7143 | 0 | 0.0000 | 0.1123 | 0.3240 | 13.0913 | 0.3836 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_gap_m3_p6_rebound_3_12 | 137 | 87 | 54.0230 | 0 | 0.0000 | 4.4038 | 1.7708 | 10.9902 | 0.9772 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | 10.5026 | 2.1528 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_gte1_2 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | 10.5026 | 2.1528 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_gap_m5_p8_rebound_3_20 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | 10.5026 | 2.1528 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40_exclude_wv | 63 | 58 | 53.4483 | 0 | 0.0000 | 2.2837 | 0.2620 | 10.6754 | 1.5145 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 63 | 58 | 53.4483 | 0 | 0.0000 | 2.2837 | 0.2620 | 10.6754 | 1.5145 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | second_red_delta_gte10 | 84 | 47 | 53.1915 | 0 | 0.0000 | 3.7373 | 1.5190 | 10.1587 | 0.3107 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | price_le40_red_ratio_gt_first | 158 | 95 | 52.6316 | 0 | 0.0000 | 0.1875 | 0.0000 | 10.0086 | 0.4588 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | price_le40_volume_red | 158 | 95 | 52.6316 | 0 | 0.0000 | 0.1875 | 0.0000 | 10.0086 | 0.4588 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_exclude_wv | 63 | 40 | 52.5000 | 0 | 0.0000 | 3.2653 | 1.0777 | 9.4672 | -0.1613 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 63 | 40 | 52.5000 | 0 | 0.0000 | 3.2653 | 1.0777 | 9.4672 | -0.1613 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | bottom_or_low_volume_red | 170 | 107 | 52.3364 | 0 | 0.0000 | 0.1602 | 0.0000 | 9.7135 | 0.4315 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | second_red_ratio_gt_first | 185 | 121 | 52.0661 | 0 | 0.0000 | 0.2518 | 0.0000 | 9.4432 | 0.5231 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_gap_m3_p6_rebound_3_12 | 137 | 87 | 51.7241 | 0 | 0.0000 | 0.5011 | 0.2845 | 9.1012 | 0.7724 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40_below_neckline5 | 80 | 66 | 51.5152 | 0 | 0.0000 | -0.0090 | 0.2234 | 8.7423 | -0.7782 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40 | 157 | 140 | 51.4286 | 0 | 0.0000 | 1.6458 | 0.2069 | 8.6557 | 0.8766 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40_volume_gte1_2 | 157 | 140 | 51.4286 | 0 | 0.0000 | 1.6458 | 0.2069 | 8.6557 | 0.8766 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | core_mainstream_price_le40_gap_m5_p8_rebound_3_20 | 157 | 140 | 51.4286 | 0 | 0.0000 | 1.6458 | 0.2069 | 8.6557 | 0.8766 | medium_mature_sample_research_only |

## Candidate Review Rows

| outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | neutral_count | neutral_rate_pct | avg_return_pct | median_return_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_red_ratio_gt_first | 83 | 53 | 62.2642 | 0 | 0.0000 | 0.9897 | 0.5000 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_red | 83 | 53 | 62.2642 | 0 | 0.0000 | 0.9897 | 0.5000 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 33 | 30 | 60.0000 | 0 | 0.0000 | 1.0110 | 0.3128 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_exclude_wv | 63 | 40 | 57.5000 | 0 | 0.0000 | 0.8013 | 0.4133 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_exclude_wv | 63 | 40 | 57.5000 | 0 | 0.0000 | 0.8013 | 0.4133 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | right_rebound_5_20 | 236 | 154 | 57.1429 | 0 | 0.0000 | 0.0736 | 0.5146 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | smooth_right_rebound_5_20 | 40 | 37 | 56.7568 | 0 | 0.0000 | 1.2305 | 0.2809 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_volume_gte1_2 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_gap_m5_p8_rebound_3_20 | 157 | 99 | 56.5657 | 0 | 0.0000 | 0.9062 | 0.4630 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le25 | 95 | 61 | 55.7377 | 0 | 0.0000 | 0.3774 | 0.2845 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le30 | 114 | 70 | 55.7143 | 0 | 0.0000 | 0.1123 | 0.3240 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_gap_m3_p6_rebound_3_12 | 137 | 87 | 54.0230 | 0 | 0.0000 | 4.4038 | 1.7708 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | core_mainstream_price_le40_exclude_wv | 63 | 58 | 53.4483 | 0 | 0.0000 | 2.2837 | 0.2620 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 63 | 58 | 53.4483 | 0 | 0.0000 | 2.2837 | 0.2620 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_gte1_2 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_gap_m5_p8_rebound_3_20 | 157 | 99 | 53.5354 | 0 | 0.0000 | 5.5794 | 1.7708 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | second_red_delta_gte10 | 84 | 47 | 53.1915 | 0 | 0.0000 | 3.7373 | 1.5190 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | price_le40_red_ratio_gt_first | 158 | 95 | 52.6316 | 0 | 0.0000 | 0.1875 | 0.0000 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | price_le40_volume_red | 158 | 95 | 52.6316 | 0 | 0.0000 | 0.1875 | 0.0000 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_exclude_wv | 63 | 55 | 50.9091 | 0 | 0.0000 | 5.4912 | 0.4219 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 63 | 55 | 50.9091 | 0 | 0.0000 | 5.4912 | 0.4219 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | bottom_or_low_volume_red | 170 | 107 | 52.3364 | 0 | 0.0000 | 0.1602 | 0.0000 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | second_red_ratio_gt_first | 185 | 121 | 52.0661 | 0 | 0.0000 | 0.2518 | 0.0000 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream_price_le40_gap_m3_p6_rebound_3_12 | 137 | 87 | 51.7241 | 0 | 0.0000 | 0.5011 | 0.2845 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | smooth_right_rebound_5_20 | 40 | 32 | 50.0000 | 0 | 0.0000 | 2.3546 | -0.0919 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | core_mainstream | 211 | 146 | 51.3699 | 0 | 0.0000 | 0.5655 | 0.1422 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | second_red_delta_gte10 | 84 | 54 | 50.0000 | 0 | 0.0000 | 2.0803 | -0.0257 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | core_mainstream_price_le40 | 157 | 140 | 51.4286 | 0 | 0.0000 | 1.6458 | 0.2069 | candidate_for_manual_promotion_review |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This grid does not modify production conditions, scoring, ranking, PDFs, or baselines.
- Neutral outcomes remain research-only and must not be treated as production approval.
- Strong-looking rows are promotion-review candidates only; they are not production rules.
