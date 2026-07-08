# volume_range_breakout v2 split feature audit

- status: research-only; this does not change production model conditions, ranking, scoring, registry, operation adapter, or PDF behavior.
- source population: same-stock non-overlap rows from `volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv`.
- purpose: split low-base/consolidated rows from momentum-continuation rows, then compare success common features, failure common features, discriminative feature gaps, and candidate condition matrix rows.
- guardrail: success feature rows include `failure_share_pct` so a feature cannot be promoted from win-rate-only evidence.

## Group Baselines

| split_group_id | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | loss_le_minus5_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_non_overlap | 576 | 50.69 | 0.52 | 48.78 | 4.3175 | 0.5599 | 35.07 |
| low_base_consolidated | 223 | 45.29 | 0.9 | 53.81 | 2.7971 | -1.5038 | 34.98 |
| momentum_continuation | 353 | 54.11 | 0.28 | 45.61 | 5.278 | 1.8433 | 35.13 |

## Candidate Condition Matrix

| candidate_id | split_group_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_status | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| momentum_volume_control_wide20 | momentum_continuation | 221 | 57.01 | 42.99 | 5.3197 | 2.4691 | research_only_candidate | best_current_direction_but_not_production_gate |
| momentum_locked_wide_nonconsolidation | momentum_continuation | 222 | 55.86 | 44.14 | 5.8533 | 2.6631 | research_only_candidate | possible_momentum_continuation_semantic_not_low_base |
| momentum_close_loc95_volume2to6 | momentum_continuation | 194 | 57.22 | 42.27 | 5.5019 | 2.1354 | research_only_candidate | technical_signal_quality_candidate |
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
| low_base_consolidated | close_gt_ma20 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma60 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma120 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma20 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma60 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma120 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | pos60_ge85 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | ma20_gt_ma60 | 335 | 54.93 | 44.78 | 96.34 | 93.17 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation | 340 | 54.12 | 45.88 | 96.34 | 96.89 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 337 | 53.12 | 46.59 | 93.72 | 97.52 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | long_consolidation | 212 | 43.87 | 55.19 | 92.08 | 97.5 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | overheat | 202 | 46.04 | 53.47 | 92.08 | 90.0 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | signal_ret_5_to_10 | 326 | 53.37 | 46.32 | 91.1 | 93.79 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | range60_le35 | 209 | 44.02 | 55.02 | 91.09 | 95.83 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 311 | 55.31 | 44.37 | 90.05 | 85.71 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | signal_ret_5_to_10 | 194 | 45.88 | 53.61 | 88.12 | 86.67 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_60d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_20d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation_and_wide20 | 292 | 55.14 | 44.86 | 84.29 | 81.37 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 292 | 55.14 | 44.86 | 84.29 | 81.37 | True | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 290 | 55.17 | 44.48 | 83.77 | 80.12 | True | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | dist_ma20_0_to_20 | 189 | 44.44 | 54.5 | 83.17 | 85.83 | True | common_in_success_and_failure_do_not_use_alone |

## Failure Common Features

| split_group_id | feature_id | sample_size | win_rate_pct | loss_rate_pct | success_share_pct | failure_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| low_base_consolidated | consolidated_any | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | pos60_ge85 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma20 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma60 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_gt_ma120 | 223 | 45.29 | 53.81 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma20 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma60 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_gt_ma120 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | pos60_ge85 | 353 | 54.11 | 45.61 | 100.0 | 100.0 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 337 | 53.12 | 46.59 | 93.72 | 97.52 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | long_consolidation | 212 | 43.87 | 55.19 | 92.08 | 97.5 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation | 340 | 54.12 | 45.88 | 96.34 | 96.89 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | range60_le35 | 209 | 44.02 | 55.02 | 91.09 | 95.83 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | signal_ret_5_to_10 | 326 | 53.37 | 46.32 | 91.1 | 93.79 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | ma20_gt_ma60 | 335 | 54.93 | 44.78 | 96.34 | 93.17 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | overheat | 202 | 46.04 | 53.47 | 92.08 | 90.0 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | signal_ret_5_to_10 | 194 | 45.88 | 53.61 | 88.12 | 86.67 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_60d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | dist_ma20_0_to_20 | 189 | 44.44 | 54.5 | 83.17 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | near_20d_high | 193 | 46.11 | 53.37 | 88.12 | 85.83 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 311 | 55.31 | 44.37 | 90.05 | 85.71 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 292 | 55.14 | 44.86 | 84.29 | 81.37 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | non_consolidation_and_wide20 | 292 | 55.14 | 44.86 | 84.29 | 81.37 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 290 | 55.17 | 44.48 | 83.77 | 80.12 | common_in_success_and_failure_do_not_use_alone |

## Discriminative Feature Gaps

| split_group_id | feature_id | success_share_pct | failure_share_pct | success_minus_failure_share_pct | decision_hint |
| --- | --- | --- | --- | --- | --- |
| low_base_consolidated | ma60_gt_ma120 | 63.37 | 48.33 | 15.03 | more_common_in_success_research_signal |
| momentum_continuation | range60_le35 | 8.38 | 18.63 | -10.26 | more_common_in_failure_risk_signal |
| low_base_consolidated | volume_gt6 | 12.87 | 21.67 | -8.8 | weak_or_mixed_feature_difference |
| low_base_consolidated | off60_le35 | 67.33 | 75.83 | -8.51 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_loc_ge80 | 73.27 | 81.67 | -8.4 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | confirm_gain_ge3 | 82.18 | 74.17 | 8.01 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | close_loc_ge95 | 62.3 | 54.66 | 7.65 | weak_or_mixed_feature_difference |
| momentum_continuation | ma60_gt_ma120 | 83.25 | 76.4 | 6.85 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | confirm_gain_ge7 | 61.39 | 55.0 | 6.39 | weak_or_mixed_feature_difference |
| low_base_consolidated | signal_ret_ge9 | 70.3 | 64.17 | 6.13 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | dist_ma60_gt30 | 69.11 | 63.35 | 5.76 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | close_loc_ge95 | 58.42 | 64.17 | -5.75 | weak_or_mixed_feature_difference |
| low_base_consolidated | range20_le15 | 49.5 | 55.0 | -5.5 | weak_or_mixed_feature_difference |
| momentum_continuation | volume_2_to_6 | 80.63 | 75.16 | 5.47 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | volume_gt6 | 2.62 | 8.07 | -5.46 | weak_or_mixed_feature_difference |
| low_base_consolidated | long_consolidation | 92.08 | 97.5 | -5.42 | common_in_success_and_failure_do_not_use_alone |
| low_base_consolidated | not_locked_limit_up | 30.69 | 35.83 | -5.14 | weak_or_mixed_feature_difference |
| low_base_consolidated | locked_limit_up | 69.31 | 64.17 | 5.14 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | off60_gt60 | 57.07 | 52.17 | 4.89 | weak_or_mixed_feature_difference |
| low_base_consolidated | range60_le35 | 91.09 | 95.83 | -4.74 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | confirm_gain_ge3 | 90.05 | 85.71 | 4.34 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | locked_and_wide20 | 64.92 | 60.87 | 4.05 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | overheat | 93.72 | 97.52 | -3.8 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_20d_high | 83.77 | 80.12 | 3.65 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | near_60d_high | 83.77 | 80.12 | 3.65 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | locked_limit_up | 78.01 | 74.53 | 3.48 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | not_locked_limit_up | 21.99 | 25.47 | -3.48 | weak_or_mixed_feature_difference |
| low_base_consolidated | near_120d_high | 58.42 | 61.67 | -3.25 | weak_or_mixed_feature_difference |
| momentum_continuation | ma20_gt_ma60 | 96.34 | 93.17 | 3.17 | common_in_success_and_failure_do_not_use_alone |
| momentum_continuation | range20_gt25 | 84.29 | 81.37 | 2.93 | common_in_success_and_failure_do_not_use_alone |

## Promotion Boundary

This artifact is diagnostic. Any hard gate, score, deduct item, risk tag, model split, operation contract, or PDF presentation change still requires a separate promotion review and production PR.
