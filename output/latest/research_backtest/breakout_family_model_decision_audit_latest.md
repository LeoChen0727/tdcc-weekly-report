# Breakout Family Model Decision Audit

- generated_at: `2026-06-27 17:33:27 Asia/Taipei`
- research_id: `breakout_family_model_decision_audit`
- source_research_id: `breakout_family_retest_grid`
- source_parameter_set_id: `breakout_family_retest_grid_20260627`
- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.

## Decision Summary

- Primary research direction: keep testing `retest_hold_then_attack_next_open`; retest-not-broken then renewed attack is stronger than direct breakout in most reviewable families.
- Model split direction: do not split W-bottom / triple-bottom / other neckline subtypes yet. The current evidence supports a broad structured-neckline research surface first.
- Volume model meaning: `bottom_base_volume_attack_reference` is bottom/base volume attack after contracted consolidation; it is not a previous-high model definition.
- Volume range breakout research direction: future `volume_range_breakout` research should prioritize `low_position_base_attack`; `base_attack_position_review` is only a broad review bucket and must not define the model because it lacks a low-position gate.
- Production status: all rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.

## Family-Level Decisions

| event_family_id | direct_win_rate_pct | retest_win_rate_pct | win_rate_lift_pct | retest_trigger_rate_pct | entry_decision | split_decision | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | 33.5831 | 47.7477 | 14.1646 | 30.2452 | prioritize_retest_confirmation_research | keep_as_bottom_base_volume_attack_reference_not_previous_high | use_as_directional_research_only |
| descending_resistance_volume_breakout_proxy | 32.8498 | 49.0411 | 16.1913 | 31.1433 | prioritize_retest_confirmation_research | keep_separate_research_surface_line_definition_differs | continue_as_separate_descending_resistance_retest_research |
| structured_neckline_volume_breakout_proxy | 30.4070 | 43.3155 | 12.9085 | 29.8484 | mixed_retest_improvement_review | keep_broad_neckline_surface_until_subtypes_prove_separation | continue_broad_neckline_retest_research_before_splitting_w_triple_other |

## Subtype-Level Decisions

| event_family_id | pattern_subtype | direct_sample_size | retest_mature_sample_size | direct_win_rate_pct | retest_win_rate_pct | win_rate_lift_pct | sample_quality | entry_decision | split_decision | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | base_attack_position_review | 734 | 207 | 30.9264 | 48.7923 | 17.8658 | reviewable_sample | prioritize_retest_confirmation_research | do_not_split_yet_keep_family_surface | do_not_use_as_volume_range_definition_without_position_gate |
| bottom_base_volume_attack_reference | low_position_base_attack | 395 | 116 | 35.4430 | 49.1379 | 13.6949 | reviewable_sample | prioritize_retest_confirmation_research | do_not_split_yet_keep_family_surface | prioritize_low_position_base_volume_attack_retest_grid |
| bottom_base_volume_attack_reference | wide_base_review | 339 | 121 | 37.1681 | 44.6281 | 7.4600 | reviewable_sample | mixed_retest_improvement_review | do_not_split_yet_keep_family_surface | review_whether_wide_base_conflicts_with_contracted_base_semantics |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | 1172 | 365 | 32.8498 | 49.0411 | 16.1913 | reviewable_sample | prioritize_retest_confirmation_research | do_not_split_yet_keep_family_surface | continue_as_separate_descending_resistance_retest_research |
| structured_neckline_volume_breakout_proxy | double_bottom_or_structured_bottom_proxy | 51 | 13 | 33.3333 | 23.0769 | -10.2564 | thin_sample | insufficient_retest_sample | insufficient_evidence_for_separate_model | expand_sample_or_drop_subtype_before_model_discussion |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | 1202 | 361 | 30.2829 | 44.0443 | 13.7615 | reviewable_sample | prioritize_retest_confirmation_research | do_not_split_yet_keep_family_surface | continue_broad_neckline_retest_research_before_splitting_w_triple_other |

## Prioritized Follow-Up Rows

| event_family_id | pattern_subtype | retest_mature_sample_size | retest_win_rate_pct | retest_avg_return_pct | win_rate_lift_pct | next_action |
| --- | --- | --- | --- | --- | --- | --- |
| bottom_base_volume_attack_reference | base_attack_position_review | 207 | 48.7923 | 2.7200 | 17.8658 | do_not_use_as_volume_range_definition_without_position_gate |
| bottom_base_volume_attack_reference | low_position_base_attack | 116 | 49.1379 | 3.9508 | 13.6949 | prioritize_low_position_base_volume_attack_retest_grid |
| descending_resistance_volume_breakout_proxy | descending_resistance_line_proxy | 365 | 49.0411 | 1.8955 | 16.1913 | continue_as_separate_descending_resistance_retest_research |
| structured_neckline_volume_breakout_proxy | triple_or_multi_bottom_proxy | 361 | 44.0443 | 1.1027 | 13.7615 | continue_broad_neckline_retest_research_before_splitting_w_triple_other |

## Interpretation

The practical next step is not production promotion. It is a second research pass focused on retest-confirmed entries, with subtype splitting treated as unproven until a broader replay and chart-quality review show stable separation.
