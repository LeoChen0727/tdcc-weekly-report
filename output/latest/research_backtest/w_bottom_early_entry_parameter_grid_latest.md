# W-Bottom Early-Entry Parameter Grid

- generated_at: `2026-06-26 21:27:05 Asia/Taipei`
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
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 69.7674 | 0 | 0.0000 | 0.4039 | 2.1572 | 36.4571 | 1.1573 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 62.8571 | 0 | 0.0000 | 0.3887 | 0.8638 | 29.5468 | 1.1422 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 61.2500 | 0 | 0.0000 | 0.1488 | 0.8638 | 27.9397 | 0.9022 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 60.2410 | 0 | 0.0000 | 0.0642 | 1.2384 | 26.9306 | 0.8176 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_price_le40_right_rebound_5_20 | 158 | 127 | 59.0551 | 0 | 0.0000 | 0.0253 | 0.8889 | 25.7448 | 0.7787 | medium_mature_sample_research_only |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20 | 172 | 141 | 58.8652 | 0 | 0.0000 | -0.0275 | 0.8889 | 25.5549 | 0.7259 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 55.7143 | 0 | 0.0000 | 5.0277 | 2.7321 | 16.1281 | 4.3394 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 81 | 55.5556 | 0 | 0.0000 | 5.3924 | 1.3627 | 13.2356 | 4.4439 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 91 | 54.9451 | 0 | 0.0000 | 4.9967 | 1.0638 | 12.6251 | 4.0482 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 76 | 53.9474 | 0 | 0.0000 | 5.7587 | 2.9223 | 12.4517 | 4.9508 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 345 | 53.9130 | 0 | 0.0000 | 5.7226 | 0.9019 | 11.5931 | 4.7741 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 345 | 53.9130 | 0 | 0.0000 | 5.7226 | 0.9019 | 11.5931 | 4.7741 | medium_mature_sample_research_only |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 52 | 53.8462 | 28 | 29.4737 | 3.1845 | 10.2052 | 17.5002 | 2.1303 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 53.7500 | 0 | 0.0000 | 4.7314 | 1.2963 | 14.1638 | 4.0431 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 83 | 53.0120 | 0 | 0.0000 | 1.2491 | 0.1414 | 11.6518 | 1.2037 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 330 | 52.7273 | 0 | 0.0000 | 6.7242 | 1.2986 | 11.2316 | 5.9162 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 330 | 52.7273 | 0 | 0.0000 | 6.7242 | 1.2986 | 11.2316 | 5.9162 | medium_mature_sample_research_only |
| take_profit_10pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 52.5000 | 0 | 0.0000 | 4.6259 | 10.0883 | 16.2241 | 2.4465 | medium_mature_sample_research_only |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 44 | 52.2727 | 26 | 30.5882 | 3.5291 | 10.1573 | 15.9268 | 2.4750 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 310 | 52.2581 | 0 | 0.0000 | 7.9977 | 0.3959 | 12.6719 | 7.3094 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 310 | 52.2581 | 0 | 0.0000 | 7.9977 | 0.3959 | 12.6719 | 7.3094 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 93 | 51.6129 | 0 | 0.0000 | 3.8340 | 0.8368 | 10.1172 | 3.0260 | medium_mature_sample_research_only |
| take_profit_10pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 51.4286 | 0 | 0.0000 | 4.9389 | 10.0403 | 15.1527 | 2.7595 | medium_mature_sample_research_only |
| fixed_30d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 86 | 51.1628 | 0 | 0.0000 | 5.0172 | 1.4823 | 9.6671 | 4.2093 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 50.6024 | 0 | 0.0000 | 2.8015 | 0.3425 | 11.0162 | 2.1133 | medium_mature_sample_research_only |
| fixed_10d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 93 | 50.5376 | 0 | 0.0000 | 1.2454 | 0.1048 | 9.1773 | 1.2000 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 97 | 50.5155 | 0 | 0.0000 | 3.2452 | 0.2793 | 8.1955 | 2.2967 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 158 | 127 | 50.3937 | 0 | 0.0000 | 2.0951 | 0.2841 | 10.8075 | 1.4068 | medium_mature_sample_research_only |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 50.0000 | 0 | 0.0000 | 3.1972 | 0.0996 | 10.4138 | 2.5089 | medium_mature_sample_research_only |
| fixed_20d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 90 | 50.0000 | 0 | 0.0000 | 2.9555 | 0.1396 | 7.6801 | 2.0070 | medium_mature_sample_research_only |

## Candidate Review Rows

| outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | neutral_count | neutral_rate_pct | avg_return_pct | median_return_pct | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 69.7674 | 0 | 0.0000 | 0.4039 | 2.1572 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 62.8571 | 0 | 0.0000 | 0.3887 | 0.8638 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 61.2500 | 0 | 0.0000 | 0.1488 | 0.8638 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 60.2410 | 0 | 0.0000 | 0.0642 | 1.2384 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_price_le40_right_rebound_5_20 | 158 | 127 | 59.0551 | 0 | 0.0000 | 0.0253 | 0.8889 | candidate_for_manual_promotion_review |
| reach_neckline_close_before_right_low_stop_40d | smooth_right_rebound_5_20 | 172 | 141 | 58.8652 | 0 | 0.0000 | -0.0275 | 0.8889 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 52 | 53.8462 | 28 | 29.4737 | 3.1845 | 10.2052 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 52.5000 | 0 | 0.0000 | 4.6259 | 10.0883 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 55.7143 | 0 | 0.0000 | 5.0277 | 2.7321 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 44 | 52.2727 | 26 | 30.5882 | 3.5291 | 10.1573 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 70 | 51.4286 | 0 | 0.0000 | 4.9389 | 10.0403 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 80 | 53.7500 | 0 | 0.0000 | 4.7314 | 1.2963 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 81 | 55.5556 | 0 | 0.0000 | 5.3924 | 1.3627 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 310 | 52.2581 | 0 | 0.0000 | 7.9977 | 0.3959 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 310 | 52.2581 | 0 | 0.0000 | 7.9977 | 0.3959 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | smooth_core_mainstream_right_rebound_5_20 | 95 | 91 | 54.9451 | 0 | 0.0000 | 4.9967 | 1.0638 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 76 | 53.9474 | 0 | 0.0000 | 5.7587 | 2.9223 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | core_mainstream_price_le40_exclude_wv | 357 | 220 | 48.6364 | 90 | 25.2101 | 8.1921 | 4.7259 | candidate_for_manual_promotion_review |
| tp10_or_neutral_after_5pct_close_40d | core_mainstream_price_le40_volume_exclude_wv | 357 | 220 | 48.6364 | 90 | 25.2101 | 8.1921 | 4.7259 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | core_mainstream_price_le40_exclude_wv | 357 | 310 | 48.0645 | 0 | 0.0000 | 10.5406 | 5.0757 | candidate_for_manual_promotion_review |
| take_profit_10pct_close_40d | core_mainstream_price_le40_volume_exclude_wv | 357 | 310 | 48.0645 | 0 | 0.0000 | 10.5406 | 5.0757 | candidate_for_manual_promotion_review |
| fixed_10d_close_positive_return | smooth_core_mainstream_price_le40_right_rebound_5_20 | 85 | 83 | 53.0120 | 0 | 0.0000 | 1.2491 | 0.1414 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 345 | 53.9130 | 0 | 0.0000 | 5.7226 | 0.9019 | candidate_for_manual_promotion_review |
| fixed_20d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 345 | 53.9130 | 0 | 0.0000 | 5.7226 | 0.9019 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | core_mainstream_price_le40_exclude_wv | 357 | 330 | 52.7273 | 0 | 0.0000 | 6.7242 | 1.2986 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | core_mainstream_price_le40_volume_exclude_wv | 357 | 330 | 52.7273 | 0 | 0.0000 | 6.7242 | 1.2986 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_red_ratio_gt_first | 100 | 83 | 50.6024 | 0 | 0.0000 | 2.8015 | 0.3425 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_price_le40_right_rebound_5_20 | 158 | 127 | 50.3937 | 0 | 0.0000 | 2.0951 | 0.2841 | candidate_for_manual_promotion_review |
| fixed_40d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 86 | 50.0000 | 0 | 0.0000 | 3.1972 | 0.0996 | candidate_for_manual_promotion_review |
| fixed_30d_close_positive_return | smooth_right_rebound_5_20_near_neckline | 102 | 93 | 51.6129 | 0 | 0.0000 | 3.8340 | 0.8368 | candidate_for_manual_promotion_review |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- This grid does not modify production conditions, scoring, ranking, PDFs, or baselines.
- Neutral outcomes remain research-only and must not be treated as production approval.
- Strong-looking rows are promotion-review candidates only; they are not production rules.
