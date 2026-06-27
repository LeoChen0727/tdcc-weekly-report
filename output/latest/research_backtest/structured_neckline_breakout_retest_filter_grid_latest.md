# Structured Neckline Breakout Retest Filter Grid

- generated_at: `2026-06-27 17:33:27 Asia/Taipei`
- research_id: `structured_neckline_breakout_retest_filter_grid`
- source_research_id: `breakout_family_retest_grid`
- source_parameter_set_id: `breakout_family_retest_grid_20260627`
- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.

## Scope

This is the second-pass research grid for the broad structured-neckline breakout model. It keeps W-bottom / triple-bottom / other labels advisory and does not split them into separate production models yet.

The main entry hypothesis remains retest-not-broken then renewed attack, not direct breakout chasing. TDCC is included only as an observation layer because historical coverage is short. Revenue remains pending because a point-in-time historical revenue panel is not available in this worktree.

## Filter Grid

| segment_id | event_count | direct_win_rate_pct | retest_mature_sample_size | retest_win_rate_pct | win_rate_lift_pct | retest_avg_return_pct | tdcc_fresh_sample_size | tdcc_supportive_sample_size | interpretation | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_structured_neckline | 1253 | 30.4070 | 374 | 43.3155 | 12.9085 | 0.8222 | 108 | 55 | broad_neckline_retest_improves_win_rate_but_not_ready | continue_retest_confirmation_grid_not_production |
| triple_or_multi_bottom_proxy | 1202 | 30.2829 | 361 | 44.0443 | 13.7615 | 1.1027 | 103 | 54 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| double_bottom_or_structured_bottom_proxy | 51 | 33.3333 | 13 | 23.0769 | -10.2564 | -6.9674 | 5 | 1 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| low_position_le60 | 330 | 34.2424 | 105 | 47.6190 | 13.3766 | 2.2714 | 17 | 8 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| mid_position_60_100 | 326 | 28.2209 | 89 | 42.6966 | 14.4758 | 0.9726 | 30 | 13 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| high_position_gt100 | 597 | 29.4807 | 180 | 41.1111 | 11.6304 | -0.0976 | 61 | 34 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| base_width_le15 | 377 | 25.4642 | 102 | 42.1569 | 16.6927 | 0.7319 | 20 | 12 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| base_width_15_30 | 465 | 30.9677 | 152 | 42.1053 | 11.1375 | 1.0075 | 37 | 18 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| base_width_gt30 | 411 | 34.3066 | 120 | 45.8333 | 11.5268 | 0.6642 | 51 | 25 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| support_touches_ge3 | 1202 | 30.2829 | 361 | 44.0443 | 13.7615 | 1.1027 | 103 | 54 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| clean_attack_candle | 1005 | 32.9353 | 297 | 43.4343 | 10.4990 | 0.8955 | 93 | 47 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| weak_or_upper_shadow_candle | 248 | 20.1613 | 77 | 42.8571 | 22.6959 | 0.5395 | 15 | 8 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| normal_volume_breakout | 1212 | 30.4455 | 365 | 43.5616 | 13.1161 | 0.8327 | 101 | 51 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| locked_limit_up_breakout | 50 | 28.0000 | 10 | 30.0000 | 2.0000 | -2.6599 | 8 | 5 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| tdcc_fresh_supportive | 55 | 49.0909 | 20 | 75.0000 | 25.9091 | 10.4791 | 55 | 55 | tdcc_layer_is_observation_only_due_coverage | keep_tdcc_as_scoring_research_not_required_gate |
| tdcc_no_fresh_support | 1198 | 29.5492 | 354 | 41.5254 | 11.9762 | 0.2766 | 53 | 0 | tdcc_layer_is_observation_only_due_coverage | keep_tdcc_as_scoring_research_not_required_gate |

## Priority Rows

| segment_id | event_count | retest_mature_sample_size | retest_win_rate_pct | retest_avg_return_pct | win_rate_lift_pct | next_action |
| --- | --- | --- | --- | --- | --- | --- |
| all_structured_neckline | 1253 | 374 | 43.3155 | 0.8222 | 12.9085 | continue_retest_confirmation_grid_not_production |
| triple_or_multi_bottom_proxy | 1202 | 361 | 44.0443 | 1.1027 | 13.7615 | review_chart_quality_and_expand_replay |
| low_position_le60 | 330 | 105 | 47.6190 | 2.2714 | 13.3766 | review_chart_quality_and_expand_replay |
| mid_position_60_100 | 326 | 89 | 42.6966 | 0.9726 | 14.4758 | review_chart_quality_and_expand_replay |
| base_width_le15 | 377 | 102 | 42.1569 | 0.7319 | 16.6927 | review_chart_quality_and_expand_replay |
| support_touches_ge3 | 1202 | 361 | 44.0443 | 1.1027 | 13.7615 | review_chart_quality_and_expand_replay |
| clean_attack_candle | 1005 | 297 | 43.4343 | 0.8955 | 10.4990 | review_chart_quality_and_expand_replay |
| normal_volume_breakout | 1212 | 365 | 43.5616 | 0.8327 | 13.1161 | review_chart_quality_and_expand_replay |

## Interpretation

Current evidence supports continuing broad neckline retest-confirmation research. It does not yet support production promotion or splitting the neckline model into W-bottom / triple-bottom / other subtype models.
