# W-Bottom Combined Condition Backtest

- generated_at: `2026-06-26 04:40:32 Asia/Taipei`
- source_research_id: `w_bottom_nearest_micro_anchor_event_replay`
- baseline_event_set: `baseline_current_detector`
- variant_event_set: `variant_nearest_micro_45d_event_replay`
- production impact: `none`
- revenue/catalyst feature status: `pending_historical_feature_join_not_evaluated`
- note: revenue/catalyst current daily artifacts are not joined because they are not historical signal-date features in this research packet.

## Event Set Counts

| event_set_id | comparison_status | count |
| --- | --- | --- |
| baseline_current_detector | baseline_only | 216 |
| baseline_current_detector | common | 254 |
| variant_nearest_micro_45d_event_replay | common | 254 |
| variant_nearest_micro_45d_event_replay | variant_only | 118 |

## Price-Level Counts

| event_set_id | price_level_bucket | count |
| --- | --- | --- |
| baseline_current_detector | bottom_quartile_level | 261 |
| baseline_current_detector | low_level | 182 |
| baseline_current_detector | mid_level | 27 |
| variant_nearest_micro_45d_event_replay | bottom_quartile_level | 191 |
| variant_nearest_micro_45d_event_replay | low_level | 149 |
| variant_nearest_micro_45d_event_replay | mid_level | 32 |

## Top Variant A-Path Condition Rows

| condition_set_id | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct | delta_win_rate_pct_vs_baseline | delta_avg_return_pct_vs_baseline | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| has_post_confirmation_price_le40 | 27 | 25 | 52.0000 | 2.5825 | 0.7519 | 2.0000 | 0.1279 | directional_only_below_promotion_review_size | directionally_better_than_baseline_same_condition |
| has_post_confirmation | 33 | 31 | 51.6129 | 2.0035 | 0.7519 | 4.5541 | -0.0740 | medium_mature_sample_research_only | mixed_vs_baseline_same_condition |
| core_mainstream_price_le_40 | 157 | 29 | 41.3793 | 1.0093 | -0.4335 | -8.6207 | -0.5808 | directional_only_below_promotion_review_size | not_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream_price_le40 | 32 | 29 | 41.3793 | 1.0093 | -0.4335 | -8.6207 | -0.5808 | directional_only_below_promotion_review_size | not_better_than_baseline_same_condition |
| core_mainstream_price_le40_exclude_wv | 63 | 15 | 40.0000 | 1.2296 | -0.8152 | -35.0000 | -3.4425 | directional_only_below_promotion_review_size | not_better_than_baseline_same_condition |
| core_mainstream | 211 | 38 | 36.8421 | 0.3363 | -0.5523 | -6.9079 | -0.6766 | medium_mature_sample_research_only | not_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream | 41 | 38 | 36.8421 | 0.3363 | -0.5523 | -6.9079 | -0.6766 | medium_mature_sample_research_only | not_better_than_baseline_same_condition |
| price_position_le_40 | 298 | 39 | 35.8974 | 1.3469 | -0.8547 | 2.5641 | 0.8469 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_price_le40 | 43 | 39 | 35.8974 | 1.3469 | -0.8547 | 2.5641 | 0.8469 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| price_le40_exclude_wv | 133 | 20 | 35.0000 | 2.9844 | -0.8547 | -7.8571 | 1.5112 | directional_only_below_promotion_review_size | mixed_vs_baseline_same_condition |
| has_neckline_breakout_price_le40_exclude_wv | 22 | 20 | 35.0000 | 2.9844 | -0.8547 | -7.8571 | 1.5112 | directional_only_below_promotion_review_size | mixed_vs_baseline_same_condition |
| exclude_wv_multiple_turn | 160 | 26 | 34.6154 | 1.8895 | -1.0882 | -6.5611 | 0.4088 | directional_only_below_promotion_review_size | mixed_vs_baseline_same_condition |
| all_dedup_signals | 372 | 51 | 33.3333 | 0.6943 | -0.8547 | 2.5641 | 0.5322 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout | 55 | 51 | 33.3333 | 0.6943 | -0.8547 | 2.5641 | 0.5322 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_or_low_level | 340 | 45 | 33.3333 | 0.6340 | -0.8547 | 3.3333 | 0.6187 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_bottom_or_low | 49 | 45 | 33.3333 | 0.6340 | -0.8547 | 3.3333 | 0.6187 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_quartile_level | 191 | 20 | 25.0000 | 0.5315 | -2.5179 | -8.3333 | -2.4087 | directional_only_below_promotion_review_size | not_better_than_baseline_same_condition |
| non_mainstream | 161 | 13 | 23.0769 | 1.7407 | -3.0717 | 13.0769 | 2.9398 | low_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| hot_theme | 25 | 5 | 20.0000 | 7.3706 | -1.3216 | -5.0000 | 7.4425 | low_mature_sample_research_only | mixed_vs_baseline_same_condition |

## Guardrails

- This is a research/backtest grid, not a production model change.
- All rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- A higher win rate is not enough for promotion without sample size, average return, median return, and stability review.
- TDCC rows are very small in this sample and should be treated as directional only.
- Taxonomy is used as a read-only segment label, not as historical proof of theme state at the signal date.
