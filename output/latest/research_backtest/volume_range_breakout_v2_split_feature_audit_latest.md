# volume_range_breakout v2 split feature audit

- status: research-only; this does not change production model conditions, ranking, scoring, registry, operation adapter, or PDF behavior.
- source population: same-stock non-overlap rows from `volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv`.
- purpose: split low-base/consolidated rows from momentum-continuation rows, then compare success common features, failure common features, discriminative feature gaps, and candidate condition matrix rows.
- guardrail: success feature rows include `failure_share_pct` so a feature cannot be promoted from win-rate-only evidence.

## Group Baselines

| split_group_id | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | loss_le_minus5_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_non_overlap | 574 | 50.7 | 0.52 | 48.78 | 4.336 | 0.5599 | 35.02 |
| low_base_consolidated | 223 | 45.29 | 0.9 | 53.81 | 2.7971 | -1.5038 | 34.98 |
| momentum_continuation | 351 | 54.13 | 0.28 | 45.58 | 5.3137 | 1.8433 | 35.04 |

## Candidate Condition Matrix

| candidate_id | split_group_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_status | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| momentum_volume_control_wide20 | momentum_continuation | 219 | 57.08 | 42.92 | 5.3774 | 2.4691 | research_only_candidate | best_current_direction_but_not_production_gate |
| momentum_locked_wide_nonconsolidation | momentum_continuation | 221 | 55.66 | 44.34 | 5.8387 | 2.4691 | research_only_candidate | possible_momentum_continuation_semantic_not_low_base |
| momentum_close_loc95_volume2to6 | momentum_continuation | 193 | 56.99 | 42.49 | 5.4833 | 2.1064 | research_only_candidate | technical_signal_quality_candidate |
| momentum_volume_gt6_overheat | momentum_continuation | 18 | 27.78 | 72.22 | -1.9895 | -9.4203 | research_only_risk_tag_candidate | overheat_risk_tag_candidate_not_buy_gate |
| lowbase_vol2to6_confirm3 | low_base_consolidated | 125 | 48.8 | 50.4 | 3.1782 | -0.9524 | research_only_candidate | low_base_needs_more_evidence_currently_weak |
| lowbase_closehigh_confirm3 | low_base_consolidated | 132 | 43.18 | 56.06 | 2.4386 | -2.1698 | rejected_as_hard_gate_candidate | low_base_signal_still_common_in_failures |
| lowbase_ma60_gt_ma120 | low_base_consolidated | 124 | 51.61 | 46.77 | 5.0413 | 0.9961 | research_only_candidate | weak_low_base_quality_filter_needs_followup |
| lowbase_off60_le35 | low_base_consolidated | 160 | 42.5 | 56.88 | 2.0995 | -2.4886 | rejected_as_hard_gate_candidate | deeper_low_position_performed_worse_in_current_evidence |

## Success Common Features With Failure Check

| split_group_id | feature_id | sample_size | win_rate_pct | loss_rate_pct | success_share_pct | failure_share_pct | failure_common_flag | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| low_base_consolidated | consolidated_any | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | pos60_ge85 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma120 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma60 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma20 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | pos60_ge85 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma20 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma120 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma60 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | ma20_gt_ma60 | 333 | 54.95 | 44.74 | 96.32 | 93.12 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation | 338 | 54.14 | 45.86 | 96.32 | 96.88 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 335 | 53.13 | 46.57 | 93.68 | 97.5 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | overheat | 202 | 46.04 | 53.47 | 92.08 | 90.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | long_consolidation | 212 | 43.87 | 55.19 | 92.08 | 97.5 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | range60_le35 | 209 | 44.02 | 55.02 | 91.09 | 95.83 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | signal_ret_5_to_10 | 325 | 53.23 | 46.46 | 91.05 | 94.38 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 310 | 55.48 | 44.19 | 90.53 | 85.62 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_60d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_20d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | signal_ret_5_to_10 | 194 | 45.88 | 53.61 | 88.12 | 86.67 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 290 | 55.17 | 44.83 | 84.21 | 81.25 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation_and_wide20 | 290 | 55.17 | 44.83 | 84.21 | 81.25 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 289 | 55.02 | 44.64 | 83.68 | 80.62 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | dist_ma20_0_to_20 | 189 | 44.44 | 54.5 | 83.17 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |

## Failure Common Features

| split_group_id | feature_id | sample_size | win_rate_pct | loss_rate_pct | success_share_pct | failure_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| low_base_consolidated | consolidated_any | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | pos60_ge85 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma120 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma60 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma20 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | pos60_ge85 | 351 | 54.13 | 45.58 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma20 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma60 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma120 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | long_consolidation | 212 | 43.87 | 55.19 | 92.08 | 97.5 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 335 | 53.13 | 46.57 | 93.68 | 97.5 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation | 338 | 54.14 | 45.86 | 96.32 | 96.88 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | range60_le35 | 209 | 44.02 | 55.02 | 91.09 | 95.83 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | signal_ret_5_to_10 | 325 | 53.23 | 46.46 | 91.05 | 94.38 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | ma20_gt_ma60 | 333 | 54.95 | 44.74 | 96.32 | 93.12 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | overheat | 202 | 46.04 | 53.47 | 92.08 | 90.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | signal_ret_5_to_10 | 194 | 45.88 | 53.61 | 88.12 | 86.67 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | dist_ma20_0_to_20 | 189 | 44.44 | 54.5 | 83.17 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_60d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_20d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 310 | 55.48 | 44.19 | 90.53 | 85.62 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 290 | 55.17 | 44.83 | 84.21 | 81.25 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation_and_wide20 | 290 | 55.17 | 44.83 | 84.21 | 81.25 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 289 | 55.02 | 44.64 | 83.68 | 80.62 | common_in_success_and_failure_do_not_use_alone |

## Discriminative Feature Gaps

| split_group_id | feature_id | success_share_pct | failure_share_pct | success_minus_failure_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- |
| low_base_consolidated | ma60_gt_ma120 | 63.37 | 48.33 | 15.03 | more_common_in_success_research_signal |
| momentum_continuation | range60_le35 | 7.89 | 18.12 | -10.23 | more_common_in_failure_risk_signal |
| low_base_consolidated | volume_gt6 | 12.87 | 21.67 | -8.8 | weak_or_mixed_feature_difference |
| low_base_consolidated | off60_le35 | 67.33 | 75.83 | -8.51 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_loc_ge80 | 73.27 | 81.67 | -8.4 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | confirm_gain_ge3 | 82.18 | 74.17 | 8.01 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_loc_ge95 | 62.11 | 55.0 | 7.11 | weak_or_mixed_feature_difference |
| momentum_continuation | ma60_gt_ma120 | 83.68 | 76.88 | 6.81 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | confirm_gain_ge7 | 61.39 | 55.0 | 6.39 | weak_or_mixed_feature_difference |
| low_base_consolidated | signal_ret_ge9 | 70.3 | 64.17 | 6.13 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_loc_ge95 | 58.42 | 64.17 | -5.75 | weak_or_mixed_feature_difference |
| momentum_continuation | dist_ma60_gt30 | 69.47 | 63.75 | 5.72 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | volume_2_to_6 | 80.53 | 75.0 | 5.53 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | range20_le15 | 49.5 | 55.0 | -5.5 | weak_or_mixed_feature_difference |
| momentum_continuation | volume_gt6 | 2.63 | 8.12 | -5.49 | weak_or_mixed_feature_difference |
| low_base_consolidated | long_consolidation | 92.08 | 97.5 | -5.42 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | not_locked_limit_up | 30.69 | 35.83 | -5.14 | weak_or_mixed_feature_difference |
| low_base_consolidated | locked_limit_up | 69.31 | 64.17 | 5.14 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 90.53 | 85.62 | 4.9 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | off60_gt60 | 57.37 | 52.5 | 4.87 | weak_or_mixed_feature_difference |
| low_base_consolidated | range60_le35 | 91.09 | 95.83 | -4.74 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 93.68 | 97.5 | -3.82 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | locked_and_wide20 | 64.74 | 61.25 | 3.49 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | signal_ret_5_to_10 | 91.05 | 94.38 | -3.32 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_120d_high | 58.42 | 61.67 | -3.25 | weak_or_mixed_feature_difference |
| momentum_continuation | ma20_gt_ma60 | 96.32 | 93.12 | 3.19 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 83.68 | 80.62 | 3.06 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_60d_high | 83.68 | 80.62 | 3.06 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 84.21 | 81.25 | 2.96 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation_and_wide20 | 84.21 | 81.25 | 2.96 | common_in_success_and_failure_do_not_use_alone |

## Promotion Boundary

This artifact is diagnostic. Any hard gate, score, deduct item, risk tag, model split, operation contract, or PDF presentation change still requires a separate promotion review and production PR.
