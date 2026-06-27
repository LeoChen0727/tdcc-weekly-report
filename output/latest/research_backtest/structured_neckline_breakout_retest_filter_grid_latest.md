# Structured Neckline Breakout Retest Filter Grid

- generated_at: `2026-06-27 18:08:28 Asia/Taipei`
- research_id: `structured_neckline_breakout_retest_filter_grid`
- source_research_id: `breakout_family_retest_grid`
- source_parameter_set_id: `breakout_family_retest_grid_20260627`
- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.

## Scope

This is the second-pass research grid for the broad structured-neckline breakout model. It keeps W-bottom / triple-bottom / other labels advisory and does not split them into separate production models yet.

The confirmation-signal reference intentionally uses the existing `volume_breakout_confirmed_operation` rules, entry_rule_id `confirmation_next_open`, and max confirmation window `10` trading days. This is not the initial `cond_volume_breakout` stock-screening gate, and it is not a replay of the initial volume/candle entry filter. The reference asks a different question: after a structured neckline breakout signal exists, does the existing confirmed-operation logic later produce a usable operation entry?

Confirmation trigger ids referenced here: `pullback_5ma_confirmed`, `next_day_break_signal_high_confirmed`, `next_day_continuation_confirmed`, and `pullback_10ma_confirmed`. Confirmed-operation performance uses the existing rule: buy at the next open after confirmation, stop at the signal-day low, otherwise exit at the fixed 10-trading-day close.

The main entry hypotheses are now compared separately: direct next-open after neckline breakout, retest-not-broken then renewed attack, and existing confirmed-operation signal after the neckline event. Limit special cases remain diagnostic tags: locked limit-up may be part of the source attack-volume confirmation, while locked limit-down is risk and must not count as confirmation. TDCC is included only as an observation layer because historical coverage is short. Revenue remains pending because a point-in-time historical revenue panel is not available in this worktree.

Market regime is included as a research-only segmentation layer, using the same `strong_bull`, `mild_bull`, `range_or_mixed`, `correction`, and `unknown` categories used by W-bottom early-entry research. These rows test whether broad-market context improves structured-neckline behavior; they are not production gates.

## Filter Grid

| segment_id | event_count | direct_win_rate_pct | retest_mature_sample_size | retest_win_rate_pct | win_rate_lift_pct | retest_avg_return_pct | tdcc_fresh_sample_size | tdcc_supportive_sample_size | confirmation_signal_sample_size | confirmation_signal_rate_pct | confirmation_signal_win_rate_pct | confirmation_signal_avg_return_pct | interpretation | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_structured_neckline | 1253 | 30.4070 | 374 | 43.3155 | 12.9085 | 0.8222 | 108 | 55 | 864 | 68.9545 | 36.8056 | 0.6313 | broad_neckline_retest_improves_win_rate_but_not_ready | continue_retest_confirmation_grid_not_production |
| triple_or_multi_bottom_proxy | 1202 | 30.2829 | 361 | 44.0443 | 13.7615 | 1.1027 | 103 | 54 | 821 | 68.3028 | 37.0280 | 0.7752 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| double_bottom_or_structured_bottom_proxy | 51 | 33.3333 | 13 | 23.0769 | -10.2564 | -6.9674 | 5 | 1 | 43 | 84.3137 | 32.5581 | -2.1152 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| low_position_le60 | 330 | 34.2424 | 105 | 47.6190 | 13.3766 | 2.2714 | 17 | 8 | 248 | 75.1515 | 37.9032 | 1.1643 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| mid_position_60_100 | 326 | 28.2209 | 89 | 42.6966 | 14.4758 | 0.9726 | 30 | 13 | 222 | 68.0982 | 34.6847 | 0.2551 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| high_position_gt100 | 597 | 29.4807 | 180 | 41.1111 | 11.6304 | -0.0976 | 61 | 34 | 394 | 65.9966 | 37.3096 | 0.5079 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| base_width_le15 | 377 | 25.4642 | 102 | 42.1569 | 16.6927 | 0.7319 | 20 | 12 | 249 | 66.0477 | 31.7269 | -0.0051 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| base_width_15_30 | 465 | 30.9677 | 152 | 42.1053 | 11.1375 | 1.0075 | 37 | 18 | 322 | 69.2473 | 39.1304 | 1.8503 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| base_width_gt30 | 411 | 34.3066 | 120 | 45.8333 | 11.5268 | 0.6642 | 51 | 25 | 293 | 71.2895 | 38.5666 | -0.1674 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| support_touches_ge3 | 1202 | 30.2829 | 361 | 44.0443 | 13.7615 | 1.1027 | 103 | 54 | 821 | 68.3028 | 37.0280 | 0.7752 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| clean_attack_candle | 1005 | 32.9353 | 297 | 43.4343 | 10.4990 | 0.8955 | 93 | 47 | 751 | 74.7264 | 37.4168 | 0.6709 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| weak_or_upper_shadow_candle | 248 | 20.1613 | 77 | 42.8571 | 22.6959 | 0.5395 | 15 | 8 | 113 | 45.5645 | 32.7434 | 0.3681 | mixed_filter_improvement | keep_as_advisory_filter_until_broader_replay |
| normal_volume_breakout | 1212 | 30.4455 | 365 | 43.5616 | 13.1161 | 0.8327 | 101 | 51 | 831 | 68.5644 | 36.9434 | 0.6712 | candidate_filter_for_second_pass_review | review_chart_quality_and_expand_replay |
| locked_limit_up_breakout | 50 | 28.0000 | 10 | 30.0000 | 2.0000 | -2.6599 | 8 | 5 | 39 | 78.0000 | 30.7692 | -0.8198 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| locked_limit_down_risk | 0 |  | 0 |  |  |  | 0 | 0 | 0 |  |  |  | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| market_regime_strong_bull | 867 | 31.0265 | 279 | 46.2366 | 15.2100 | 1.7820 | 96 | 47 | 622 | 71.7416 | 36.1736 | 0.6283 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| market_regime_bull | 1037 | 31.4368 | 323 | 44.8916 | 13.4548 | 1.2894 | 98 | 49 | 730 | 70.3954 | 37.1233 | 0.7441 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| market_regime_not_correction | 1158 | 31.5199 | 350 | 44.0000 | 12.4801 | 1.0007 | 107 | 55 | 818 | 70.6390 | 36.9193 | 0.6588 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| market_regime_range_or_mixed | 121 | 32.2314 | 27 | 33.3333 | 1.1019 | -2.4531 | 9 | 6 | 88 | 72.7273 | 35.2273 | -0.0486 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| market_regime_correction | 95 | 16.8421 | 24 | 33.3333 | 16.4912 | -1.7808 | 1 | 0 | 46 | 48.4211 | 34.7826 | 0.1424 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| market_regime_unknown | 0 |  | 0 |  |  |  | 0 | 0 | 0 |  |  |  | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| low_position_le60_market_bull | 285 | 34.3860 | 95 | 46.3158 | 11.9298 | 2.3243 | 17 | 8 | 218 | 76.4912 | 36.6972 | 0.9786 | market_regime_research_filter_only | compare_market_regime_stability_not_production_gate |
| confirmation_signal_reference | 864 | 44.0972 | 330 | 44.8485 | 0.7513 | 1.0749 | 84 | 39 | 864 | 100.0000 | 36.8056 | 0.6313 | existing_volume_breakout_operation_confirmation_reference | compare_confirmation_entry_against_retest_entry_not_production |
| confirmation_signal_low_position_le60 | 248 | 45.5645 | 95 | 49.4737 | 3.9092 | 3.0012 | 15 | 7 | 248 | 100.0000 | 37.9032 | 1.1643 | existing_volume_breakout_operation_confirmation_reference | compare_confirmation_entry_against_retest_entry_not_production |
| confirmation_signal_market_bull | 730 | 44.6575 | 287 | 45.9930 | 1.3355 | 1.6115 | 76 | 34 | 730 | 100.0000 | 37.1233 | 0.7441 | existing_volume_breakout_operation_confirmation_reference | compare_confirmation_entry_against_retest_entry_not_production |
| confirmation_signal_low_position_le60_market_bull | 218 | 44.9541 | 86 | 47.6744 | 2.7203 | 3.0422 | 15 | 7 | 218 | 100.0000 | 36.6972 | 0.9786 | existing_volume_breakout_operation_confirmation_reference | compare_confirmation_entry_against_retest_entry_not_production |
| tdcc_fresh_supportive | 55 | 49.0909 | 20 | 75.0000 | 25.9091 | 10.4791 | 55 | 55 | 39 | 70.9091 | 69.2308 | 11.2365 | tdcc_layer_is_observation_only_due_coverage | keep_tdcc_as_scoring_research_not_required_gate |
| tdcc_fresh_supportive_market_bull | 49 | 48.9796 | 18 | 77.7778 | 28.7982 | 11.4987 | 49 | 49 | 34 | 69.3878 | 73.5294 | 12.6226 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| tdcc_no_fresh_support | 1198 | 29.5492 | 354 | 41.5254 | 11.9762 | 0.2766 | 53 | 0 | 825 | 68.8648 | 35.2727 | 0.1300 | tdcc_layer_is_observation_only_due_coverage | keep_tdcc_as_scoring_research_not_required_gate |
| confirmation_trigger_pullback_5ma_confirmed | 281 | 37.7224 | 113 | 48.6726 | 10.9501 | 2.2015 | 26 | 13 | 281 | 100.0000 | 33.8078 | 0.3721 | trigger_specific_confirmation_reference_only | keep_trigger_as_research_diagnostic |
| confirmation_trigger_next_day_break_signal_high_confirmed | 554 | 48.3755 | 208 | 42.7885 | -5.5870 | 0.5136 | 54 | 22 | 554 | 100.0000 | 38.4477 | 0.6020 | trigger_specific_confirmation_reference_only | keep_trigger_as_research_diagnostic |
| confirmation_trigger_next_day_continuation_confirmed | 0 |  | 0 |  |  |  | 0 | 0 | 0 |  |  |  | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |
| confirmation_trigger_pullback_10ma_confirmed | 29 | 24.1379 | 9 | 44.4444 | 20.3065 | -0.0990 | 4 | 4 | 29 | 100.0000 | 34.4828 | 3.7025 | sample_too_thin_for_model_decision | expand_or_drop_segment_before_promotion_discussion |

## Priority Rows

| segment_id | event_count | retest_mature_sample_size | retest_win_rate_pct | retest_avg_return_pct | confirmation_signal_mature_sample_size | confirmation_signal_win_rate_pct | confirmation_signal_avg_return_pct | win_rate_lift_pct | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_structured_neckline | 1253 | 374 | 43.3155 | 0.8222 | 864 | 36.8056 | 0.6313 | 12.9085 | continue_retest_confirmation_grid_not_production |
| triple_or_multi_bottom_proxy | 1202 | 361 | 44.0443 | 1.1027 | 821 | 37.0280 | 0.7752 | 13.7615 | review_chart_quality_and_expand_replay |
| low_position_le60 | 330 | 105 | 47.6190 | 2.2714 | 248 | 37.9032 | 1.1643 | 13.3766 | review_chart_quality_and_expand_replay |
| mid_position_60_100 | 326 | 89 | 42.6966 | 0.9726 | 222 | 34.6847 | 0.2551 | 14.4758 | review_chart_quality_and_expand_replay |
| base_width_le15 | 377 | 102 | 42.1569 | 0.7319 | 249 | 31.7269 | -0.0051 | 16.6927 | review_chart_quality_and_expand_replay |
| support_touches_ge3 | 1202 | 361 | 44.0443 | 1.1027 | 821 | 37.0280 | 0.7752 | 13.7615 | review_chart_quality_and_expand_replay |
| clean_attack_candle | 1005 | 297 | 43.4343 | 0.8955 | 751 | 37.4168 | 0.6709 | 10.4990 | review_chart_quality_and_expand_replay |
| normal_volume_breakout | 1212 | 365 | 43.5616 | 0.8327 | 831 | 36.9434 | 0.6712 | 13.1161 | review_chart_quality_and_expand_replay |

## Interpretation

Current evidence supports continuing broad neckline retest-confirmation research. It does not yet support production promotion or splitting the neckline model into W-bottom / triple-bottom / other subtype models.
