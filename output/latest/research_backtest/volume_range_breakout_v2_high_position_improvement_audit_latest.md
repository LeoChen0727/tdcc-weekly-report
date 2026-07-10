# volume_range_breakout v2 high-position improvement audit

- status: research-only; no production registry, ranking, operation adapter, packet, or PDF change.
- reference universe: 120d high position + non-consolidation or wide-range shape.
- baseline model for this audit: reference universe + MA60 > MA120.
- add-score rule: mild_bull and other technical/TDCC features are research-only score candidates, not hidden buy gates.
- operation basis: D+15 close-only next-day continuation with MA20/EMA23 four-close stop from the source artifact.
- sample_count_context: sample count is reported, not used as an automatic disqualifier.

## Reference Universe And Baseline

| row_type | feature_id | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reference_universe | high_pos_gt75_non_consolidation_or_wide | 279 | 59.4982 | 0.3584 | 40.1434 | 8.1201 | 4.875 | research_only_positive_return_but_win_below_threshold |
| baseline | high_pos_gt75_nonconsolidation_or_wide_ma60_gt_ma120 | 231 | 62.3377 | 0.0 | 37.6623 | 9.4824 | 6.6055 | research_only_candidate_metric_met |

## Add-Score / Risk-Filter Candidate Conditions

| feature_id | condition_role | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_status | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| high_pos_base_plus_dist_ema23_0_15 | add_score_research_only_not_hidden_gate | 8 | 87.5 | 12.5 | 11.8073 | 11.4151 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_close_location_le80 | add_score_research_only_not_hidden_gate | 24 | 79.1667 | 20.8333 | 9.2121 | 7.7825 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_tdcc_weekly_increase_top20 | add_score_research_only_not_hidden_gate | 9 | 77.7778 | 22.2222 | 30.405 | 14.5 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_volume_lt2 | add_score_research_only_not_hidden_gate | 31 | 77.4194 | 22.5806 | 13.7578 | 15.8784 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_signal_body_le3 | add_score_research_only_not_hidden_gate | 66 | 72.7273 | 27.2727 | 10.3361 | 6.9226 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_not_limit_up_like | add_score_research_only_not_hidden_gate | 55 | 70.9091 | 29.0909 | 10.3499 | 7.1829 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_breakout_2_5 | add_score_research_only_not_hidden_gate | 98 | 67.3469 | 32.6531 | 9.8476 | 9.2248 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_market_mild_bull | add_score_research_only_not_hidden_gate | 24 | 66.6667 | 33.3333 | 12.2534 | 11.4151 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_kdj_overheated | add_score_research_only_not_hidden_gate | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_confirmation_return_3_7 | add_score_research_only_not_hidden_gate | 53 | 66.0377 | 33.9623 | 9.8174 | 5.6604 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_ma20_gt_ma60 | add_score_research_only_not_hidden_gate | 224 | 62.9464 | 37.0536 | 9.7519 | 6.939 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_exclude_volume_gt6 | risk_filter_research_only_not_hidden_gate | 223 | 62.7803 | 37.2197 | 9.2904 | 6.6055 | research_only_candidate_metric_met | risk_filter_candidate_research_only |
| high_pos_base_plus_kd_value_rising_3d | add_score_research_only_not_hidden_gate | 227 | 62.1145 | 37.8855 | 9.5243 | 6.31 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_confirmation_return_gt3 | add_score_research_only_not_hidden_gate | 203 | 62.069 | 37.931 | 9.0106 | 6.25 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_ret20_0_25 | add_score_research_only_not_hidden_gate | 47 | 61.7021 | 38.2979 | 9.9656 | 6.31 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_kdj_j_gt100 | add_score_research_only_not_hidden_gate | 127 | 61.4173 | 38.5827 | 10.544 | 5.2083 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_volume_2_to_6 | add_score_research_only_not_hidden_gate | 192 | 60.4167 | 39.5833 | 8.5691 | 5.5594 | research_only_candidate_metric_met | add_score_candidate_research_only |
| high_pos_base_plus_close_location_gt95 | add_score_research_only_not_hidden_gate | 144 | 58.3333 | 41.6667 | 8.6727 | 4.9878 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_tdcc_any_top20 | add_score_research_only_not_hidden_gate | 12 | 58.3333 | 41.6667 | 20.9398 | 10.0439 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_kd_bull_cross_signal | add_score_research_only_not_hidden_gate | 33 | 57.5758 | 42.4242 | 7.9993 | 9.1346 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_kd_bullish_not_overheated | add_score_research_only_not_hidden_gate | 106 | 57.5472 | 42.4528 | 6.9002 | 2.8263 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_kd_not_overheated | add_score_research_only_not_hidden_gate | 106 | 57.5472 | 42.4528 | 6.9002 | 2.8263 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_kdj_bullish_not_overheated | add_score_research_only_not_hidden_gate | 106 | 57.5472 | 42.4528 | 6.9002 | 2.8263 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |
| high_pos_base_plus_signal_body_3_7 | add_score_research_only_not_hidden_gate | 68 | 55.8824 | 44.1176 | 6.7132 | 5.3333 | research_only_positive_return_but_win_below_threshold | risk_or_negative_stratification_subject |

## PDF Add-Score Exact Combo Metrics

| feature_id | feature_label | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | candidate_status | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pdf_combo__mild_bull__not_limit_up_like__breakout_2_5__signal_body_le3__close_location_le80 | mild_bull;not_limit_up_like;breakout_2_5;signal_body_le3;close_location_le80 | 1 | 100.0 | 0.0 | 0.0 | 11.6667 | 11.6667 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__breakout_2_5__signal_body_le3__close_location_le80 | not_limit_up_like;breakout_2_5;signal_body_le3;close_location_le80 | 6 | 100.0 | 0.0 | 0.0 | 18.2511 | 14.0715 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__breakout_2_5__volume_lt2__signal_body_le3 | mild_bull;breakout_2_5;volume_lt2;signal_body_le3 | 1 | 100.0 | 0.0 | 0.0 | 19.3133 | 19.3133 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__not_limit_up_like__breakout_2_5__close_location_le80 | mild_bull;not_limit_up_like;breakout_2_5;close_location_le80 | 2 | 50.0 | 0.0 | 50.0 | 5.1824 | 5.1824 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__not_limit_up_like__breakout_2_5 | mild_bull;not_limit_up_like;breakout_2_5 | 3 | 100.0 | 0.0 | 0.0 | 23.7866 | 16.8207 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__breakout_2_5__signal_body_le3 | not_limit_up_like;breakout_2_5;signal_body_le3 | 2 | 100.0 | 0.0 | 0.0 | 21.3732 | 21.3732 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__breakout_2_5__close_location_le80 | not_limit_up_like;breakout_2_5;close_location_le80 | 9 | 88.8889 | 0.0 | 11.1111 | 8.2677 | 5.6604 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__breakout_2_5__volume_lt2__signal_body_le3 | breakout_2_5;volume_lt2;signal_body_le3 | 4 | 75.0 | 0.0 | 25.0 | 12.4312 | 17.0032 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__signal_body_le3__close_location_le80 | not_limit_up_like;signal_body_le3;close_location_le80 | 2 | 50.0 | 0.0 | 50.0 | 2.7655 | 2.7655 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__not_limit_up_like__close_location_le80 | mild_bull;not_limit_up_like;close_location_le80 | 1 | 0.0 | 0.0 | 100.0 | -16.2162 | -16.2162 | research_only_not_candidate_metric | pdf_row_combo_metric_research_only |
| pdf_combo__breakout_2_5__signal_body_le3 | breakout_2_5;signal_body_le3 | 5 | 80.0 | 0.0 | 20.0 | 4.1054 | 6.6055 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__volume_lt2__signal_body_le3 | volume_lt2;signal_body_le3 | 26 | 76.9231 | 0.0 | 23.0769 | 13.7483 | 15.0952 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__breakout_2_5 | mild_bull;breakout_2_5 | 8 | 75.0 | 0.0 | 25.0 | 17.485 | 11.0871 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__close_location_le80 | not_limit_up_like;close_location_le80 | 3 | 66.6667 | 0.0 | 33.3333 | 8.6097 | 6.1966 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__breakout_2_5 | not_limit_up_like;breakout_2_5 | 16 | 50.0 | 0.0 | 50.0 | 7.2066 | 1.9083 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like__signal_body_le3 | not_limit_up_like;signal_body_le3 | 2 | 50.0 | 0.0 | 50.0 | -10.5742 | -10.5742 | research_only_not_candidate_metric | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__not_limit_up_like | mild_bull;not_limit_up_like | 1 | 0.0 | 0.0 | 100.0 | -0.9029 | -0.9029 | research_only_not_candidate_metric | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull__signal_body_le3 | mild_bull;signal_body_le3 | 1 | 0.0 | 0.0 | 100.0 | -13.7218 | -13.7218 | research_only_not_candidate_metric | pdf_row_combo_metric_research_only |
| pdf_combo__not_limit_up_like | not_limit_up_like | 7 | 85.7143 | 0.0 | 14.2857 | 20.1133 | 13.7405 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__mild_bull | mild_bull | 6 | 66.6667 | 0.0 | 33.3333 | 12.0565 | 11.2278 | research_only_candidate_metric_met | pdf_row_combo_metric_research_only |
| pdf_combo__signal_body_le3 | signal_body_le3 | 16 | 56.25 | 0.0 | 43.75 | 6.2863 | 1.1425 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |
| pdf_combo__breakout_2_5 | breakout_2_5 | 41 | 56.0976 | 0.0 | 43.9024 | 7.3235 | 2.4911 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |
| pdf_combo__none | none | 68 | 51.4706 | 0.0 | 48.5294 | 8.4535 | 0.9501 | research_only_positive_return_but_win_below_threshold | pdf_row_combo_metric_research_only |

## Add-Score Overlap Effects

| feature_family | feature_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| overlap_pair | overlap__mild_bull__volume_lt2 | 1 | 100.0 | 0.0 | 19.3133 | 19.3133 | positive_stratification_research_only |
| overlap_pair | overlap__breakout_2_5__signal_body_le3 | 19 | 89.4737 | 10.5263 | 13.3413 | 9.5455 | positive_stratification_research_only |
| overlap_pair | overlap__breakout_2_5__close_location_le80 | 18 | 88.8889 | 11.1111 | 11.4415 | 10.4909 | positive_stratification_research_only |
| overlap_pair | overlap__signal_body_le3__close_location_le80 | 9 | 88.8889 | 11.1111 | 14.0782 | 13.6986 | positive_stratification_research_only |
| overlap_pair | overlap__not_limit_up_like__signal_body_le3 | 13 | 84.6154 | 15.3846 | 11.4079 | 11.6667 | positive_stratification_research_only |
| overlap_pair | overlap__mild_bull__breakout_2_5 | 15 | 80.0 | 20.0 | 16.839 | 12.4211 | positive_stratification_research_only |
| overlap_pair | overlap__breakout_2_5__volume_lt2 | 5 | 80.0 | 20.0 | 13.8076 | 19.3133 | positive_stratification_research_only |
| overlap_pair | overlap__not_limit_up_like__close_location_le80 | 24 | 79.1667 | 20.8333 | 9.2121 | 7.7825 | positive_stratification_research_only |
| overlap_pair | overlap__volume_lt2__signal_body_le3 | 31 | 77.4194 | 22.5806 | 13.7578 | 15.8784 | positive_stratification_research_only |
| overlap_pair | overlap__not_limit_up_like__breakout_2_5 | 39 | 74.359 | 25.641 | 11.163 | 9.3151 | positive_stratification_research_only |
| overlap_pair | overlap__mild_bull__signal_body_le3 | 3 | 66.6667 | 33.3333 | 5.7527 | 11.6667 | positive_stratification_research_only |
| overlap_pair | overlap__mild_bull__not_limit_up_like | 8 | 62.5 | 37.5 | 9.534 | 11.4151 | positive_stratification_research_only |
| overlap_pair | overlap__mild_bull__close_location_le80 | 4 | 50.0 | 50.0 | 1.4538 | 1.192 | risk_or_negative_stratification_subject |
| overlap_score_count | add_score_count_ge4 | 10 | 90.0 | 10.0 | 15.0851 | 14.0715 | positive_stratification_research_only |
| overlap_score_count | add_score_count_ge3 | 31 | 83.871 | 16.129 | 12.2066 | 11.6667 | positive_stratification_research_only |
| overlap_score_count | add_score_count_ge2 | 93 | 72.043 | 27.957 | 10.7702 | 9.3151 | positive_stratification_research_only |
| overlap_score_count | add_score_count_ge1 | 163 | 66.8712 | 33.1288 | 9.9117 | 7.2398 | positive_stratification_research_only |
| overlap_unique | unique__not_limit_up_like | 7 | 85.7143 | 14.2857 | 20.1133 | 13.7405 | positive_stratification_research_only |
| overlap_unique | unique__mild_bull | 6 | 66.6667 | 33.3333 | 12.0565 | 11.2278 | positive_stratification_research_only |
| overlap_unique | unique__signal_body_le3 | 16 | 56.25 | 43.75 | 6.2863 | 1.1425 | risk_or_negative_stratification_subject |
| overlap_unique | unique__breakout_2_5 | 41 | 56.0976 | 43.9024 | 7.3235 | 2.4911 | risk_or_negative_stratification_subject |

## Win/Loss Feature Gaps

| feature_id | sample_size | success_share_pct | failure_share_pct | success_minus_failure_share_pct | win_rate_pct | loss_rate_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| signal_close_location_pct_ge_median | 137 | 54.8611 | 66.6667 | -11.8056 | 57.6642 | 42.3358 | numeric_feature_gap_for_win_loss_review |
| signal_close_location_bucket=close_loc_gt95 | 144 | 58.3333 | 68.9655 | -10.6322 | 58.3333 | 41.6667 | failure_feature_overrepresented_risk_review |
| kd_k_minus_d_signal_ge_median | 116 | 46.5278 | 56.3218 | -9.7941 | 57.7586 | 42.2414 | numeric_feature_gap_for_win_loss_review |
| signal_body_pct_ge_median | 116 | 46.5278 | 56.3218 | -9.7941 | 57.7586 | 42.2414 | numeric_feature_gap_for_win_loss_review |
| kd_bullish_not_overheated | 106 | 42.3611 | 51.7241 | -9.363 | 57.5472 | 42.4528 | weak_or_mixed_win_loss_feature_gap |
| kdj_k_bucket=kdj_k_50_80 | 106 | 42.3611 | 51.7241 | -9.363 | 57.5472 | 42.4528 | weak_or_mixed_win_loss_feature_gap |
| kd_k_bucket=kd_k_50_80 | 106 | 42.3611 | 51.7241 | -9.363 | 57.5472 | 42.4528 | weak_or_mixed_win_loss_feature_gap |
| kdj_phase=kdj_bullish_not_overheated | 106 | 42.3611 | 51.7241 | -9.363 | 57.5472 | 42.4528 | weak_or_mixed_win_loss_feature_gap |
| kd_phase=kd_bullish_not_overheated | 106 | 42.3611 | 51.7241 | -9.363 | 57.5472 | 42.4528 | weak_or_mixed_win_loss_feature_gap |
| kd_overheated | 125 | 57.6389 | 48.2759 | 9.363 | 66.4 | 33.6 | weak_or_mixed_win_loss_feature_gap |
| kd_k_bucket=kd_k_gt80 | 125 | 57.6389 | 48.2759 | 9.363 | 66.4 | 33.6 | weak_or_mixed_win_loss_feature_gap |
| breakout_bucket=breakout_2_5 | 98 | 45.8333 | 36.7816 | 9.0517 | 67.3469 | 32.6531 | weak_or_mixed_win_loss_feature_gap |
| limit_up_like_bool | 176 | 72.9167 | 81.6092 | -8.6925 | 59.6591 | 40.3409 | weak_or_mixed_win_loss_feature_gap |
| signal_body_bucket=body_3_7 | 68 | 26.3889 | 34.4828 | -8.0939 | 55.8824 | 44.1176 | weak_or_mixed_win_loss_feature_gap |
| volume_bucket=volume_2_to_6 | 192 | 80.5556 | 87.3563 | -6.8008 | 60.4167 | 39.5833 | weak_or_mixed_win_loss_feature_gap |
| kd_k_signal_ge_median | 116 | 52.7778 | 45.977 | 6.8008 | 65.5172 | 34.4828 | numeric_feature_gap_for_win_loss_review |
| range_width_60_pct_ge_median | 116 | 47.9167 | 54.023 | -6.1063 | 59.4828 | 40.5172 | numeric_feature_gap_for_win_loss_review |
| hist_return_20d_pct_ge_median | 116 | 52.0833 | 47.1264 | 4.9569 | 64.6552 | 35.3448 | numeric_feature_gap_for_win_loss_review |
| confirmation_return_bucket=confirm_ret_gt7 | 150 | 63.1944 | 67.8161 | -4.6216 | 60.6667 | 39.3333 | weak_or_mixed_win_loss_feature_gap |
| range60_bucket=range60_gt60 | 113 | 47.2222 | 51.7241 | -4.5019 | 60.177 | 39.823 | weak_or_mixed_win_loss_feature_gap |
| dist_ema23_bucket=dist_ema23_0_15 | 8 | 4.8611 | 1.1494 | 3.7117 | 87.5 | 12.5 | weak_or_mixed_win_loss_feature_gap |
| confirmation_return_bucket=confirm_ret_3_7 | 53 | 24.3056 | 20.6897 | 3.6159 | 66.0377 | 33.9623 | weak_or_mixed_win_loss_feature_gap |
| kd_d_signal_ge_median | 116 | 51.3889 | 48.2759 | 3.113 | 63.7931 | 36.2069 | numeric_feature_gap_for_win_loss_review |
| kd_bull_cross_signal | 33 | 13.1944 | 16.092 | -2.8975 | 57.5758 | 42.4242 | weak_or_mixed_win_loss_feature_gap |
| tdcc_weekly_increase_top20_bool | 9 | 4.8611 | 2.2989 | 2.5623 | 77.7778 | 22.2222 | weak_or_mixed_win_loss_feature_gap |
| ma20_gt_ma60_bool | 224 | 97.9167 | 95.4023 | 2.5144 | 62.9464 | 37.0536 | weak_or_mixed_win_loss_feature_gap |
| breakout_over_prev60_pct_ge_median | 116 | 49.3056 | 51.7241 | -2.4186 | 61.2069 | 38.7931 | numeric_feature_gap_for_win_loss_review |
| hist_return_60d_pct_ge_median | 116 | 49.3056 | 51.7241 | -2.4186 | 61.2069 | 38.7931 | numeric_feature_gap_for_win_loss_review |
| kdj_j_bucket=kdj_j_gt100 | 127 | 54.1667 | 56.3218 | -2.1552 | 61.4173 | 38.5827 | weak_or_mixed_win_loss_feature_gap |
| market_regime_bucket=mild_bull | 24 | 11.1111 | 9.1954 | 1.9157 | 66.6667 | 33.3333 | weak_or_mixed_win_loss_feature_gap |

## Best Feature Slices By Win Rate

| feature_family | feature_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| market | market_regime_bucket=correction | 2 | 100.0 | 0.0 | 38.5106 | 38.5106 | positive_stratification_research_only |
| classification | risk_type=stop_loss_easy_trigger | 2 | 100.0 | 0.0 | 21.1684 | 21.1684 | positive_stratification_research_only |
| classification | risk_type=volume_overheat | 2 | 100.0 | 0.0 | 46.1597 | 46.1597 | positive_stratification_research_only |
| price_shape_60d | off60_bucket=off60_le35 | 1 | 100.0 | 0.0 | 1.4908 | 1.4908 | positive_stratification_research_only |
| technical | breakout_bucket=breakout_gt10 | 1 | 100.0 | 0.0 | 10.0 | 10.0 | positive_stratification_research_only |
| technical | dist_ema23_bucket=dist_ema23_0_15 | 8 | 87.5 | 12.5 | 11.8073 | 11.4151 | positive_stratification_research_only |
| classification | candle_quality=upper_shadow | 7 | 85.7143 | 14.2857 | 9.5656 | 6.1966 | positive_stratification_research_only |
| technical | signal_close_location_bucket=close_loc_le80 | 24 | 79.1667 | 20.8333 | 9.2121 | 7.7825 | positive_stratification_research_only |
| tdcc | tdcc_weekly_increase_top20_bool | 9 | 77.7778 | 22.2222 | 30.405 | 14.5 | positive_stratification_research_only |
| technical | volume_bucket=volume_lt2 | 31 | 77.4194 | 22.5806 | 13.7578 | 15.8784 | positive_stratification_research_only |
| market | market_regime_bucket=range_or_mixed | 16 | 75.0 | 25.0 | 10.604 | 8.1476 | positive_stratification_research_only |
| classification | attack_method=volume_attack | 27 | 74.0741 | 25.9259 | 15.7014 | 13.7405 | positive_stratification_research_only |
| technical | signal_body_bucket=body_le3 | 66 | 72.7273 | 27.2727 | 10.3361 | 6.9226 | positive_stratification_research_only |
| technical | signal_close_location_bucket=missing | 33 | 72.7273 | 27.2727 | 10.0188 | 12.2 | positive_stratification_research_only |
| classification | risk_type=normal_risk | 7 | 71.4286 | 28.5714 | 11.6874 | 6.25 | positive_stratification_research_only |
| classification | classification_id=high_position_breakout | 55 | 70.9091 | 29.0909 | 10.3499 | 7.1829 | positive_stratification_research_only |
| price_shape_60d | hist60_bucket=hist60_0_25 | 23 | 69.5652 | 30.4348 | 11.0721 | 6.31 | positive_stratification_research_only |
| price_shape_60d | off60_bucket=off60_35_50 | 51 | 68.6275 | 31.3725 | 8.4814 | 9.1346 | positive_stratification_research_only |
| price_shape_60d | range60_bucket=range60_le35 | 22 | 68.1818 | 31.8182 | 9.788 | 5.5386 | positive_stratification_research_only |
| classification | attack_method=general_breakout | 28 | 67.8571 | 32.1429 | 5.1895 | 5.5594 | positive_stratification_research_only |
| technical | dist_ema23_bucket=dist_ema23_gt30 | 40 | 67.5 | 32.5 | 10.2272 | 8.31 | positive_stratification_research_only |
| technical | breakout_bucket=breakout_2_5 | 98 | 67.3469 | 32.6531 | 9.8476 | 9.2248 | positive_stratification_research_only |
| market | market_regime_bucket=mild_bull | 24 | 66.6667 | 33.3333 | 12.2534 | 11.4151 | positive_stratification_research_only |
| technical_kdj | kdj_phase=kdj_bullish_overheated | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | positive_stratification_research_only |
| technical_kdj | kdj_k_bucket=kdj_k_gt80 | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | positive_stratification_research_only |
| technical_kdj | kd_phase=kd_bullish_overheated | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | positive_stratification_research_only |
| technical_kdj | kd_k_bucket=kd_k_gt80 | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | positive_stratification_research_only |
| technical_kdj | kd_overheated | 125 | 66.4 | 33.6 | 11.6722 | 9.3156 | positive_stratification_research_only |
| technical | confirmation_return_bucket=confirm_ret_3_7 | 53 | 66.0377 | 33.9623 | 9.8174 | 5.6604 | positive_stratification_research_only |
| classification | candle_quality=explosive_long_red | 26 | 65.3846 | 34.6154 | 15.2429 | 13.7196 | positive_stratification_research_only |
| technical | confirmation_return_bucket=confirm_ret_0_3 | 28 | 64.2857 | 35.7143 | 12.9033 | 11.1463 | positive_stratification_research_only |
| price_shape_60d | range60_bucket=range60_45_60 | 53 | 64.1509 | 35.8491 | 13.5613 | 9.5455 | positive_stratification_research_only |
| price_shape_60d | hist60_bucket=hist60_25_50 | 78 | 64.1026 | 35.8974 | 10.6873 | 9.3401 | positive_stratification_research_only |
| market | market=TWSE | 135 | 63.7037 | 36.2963 | 10.8618 | 6.7174 | positive_stratification_research_only |
| technical_kdj | kdj_j_bucket=kdj_j_50_100 | 104 | 63.4615 | 36.5385 | 8.1861 | 8.5971 | positive_stratification_research_only |
| technical_kdj | kd_j_bucket=kd_j_50_100 | 104 | 63.4615 | 36.5385 | 8.1861 | 8.5971 | positive_stratification_research_only |
| shape | shape_bucket=non_consolidation | 162 | 62.963 | 37.037 | 10.0765 | 5.9852 | positive_stratification_research_only |
| technical | ma20_gt_ma60_bool | 224 | 62.9464 | 37.0536 | 9.7519 | 6.939 | positive_stratification_research_only |
| tdcc | tdcc_list_type=no_tdcc | 205 | 62.9268 | 37.0732 | 8.7446 | 6.25 | positive_stratification_research_only |
| price_shape_60d | range60_bucket=range60_35_45 | 43 | 62.7907 | 37.2093 | 7.4232 | 5.2083 | positive_stratification_research_only |

## Promotion Boundary

This artifact is diagnostic only. Any hard gate, score, risk tag, model split, operation contract, or PDF presentation change still requires a separate promotion review and production PR.
