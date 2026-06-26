# W-Bottom Combined Condition Backtest

- generated_at: `2026-06-26 21:10:07 Asia/Taipei`
- source_research_id: `w_bottom_nearest_micro_anchor_event_replay`
- baseline_event_set: `baseline_current_detector`
- variant_event_set: `variant_nearest_micro_45d_event_replay`
- production impact: `none`
- revenue/catalyst feature status: `pending_historical_feature_join_not_evaluated`
- note: revenue/catalyst current daily artifacts are not joined because they are not historical signal-date features in this research packet.

## Event Set Counts

| event_set_id | comparison_status | count |
| --- | --- | --- |
| baseline_current_detector | baseline_only | 845 |
| baseline_current_detector | common | 1079 |
| variant_nearest_micro_45d_event_replay | common | 1079 |
| variant_nearest_micro_45d_event_replay | variant_only | 605 |

## Price-Level Counts

| event_set_id | price_level_bucket | count |
| --- | --- | --- |
| baseline_current_detector | bottom_quartile_level | 1240 |
| baseline_current_detector | low_level | 618 |
| baseline_current_detector | mid_level | 66 |
| variant_nearest_micro_45d_event_replay | bottom_quartile_level | 1092 |
| variant_nearest_micro_45d_event_replay | low_level | 534 |
| variant_nearest_micro_45d_event_replay | mid_level | 58 |

## Top Variant A-Path Condition Rows

| condition_set_id | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct | delta_win_rate_pct_vs_baseline | delta_avg_return_pct_vs_baseline | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core_mainstream_price_le40_exclude_wv | 357 | 57 | 54.3860 | 5.1225 | 1.9108 | 10.4835 | 2.0961 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_post_confirmation | 150 | 146 | 52.0548 | 3.1213 | 1.0527 | 11.0476 | 1.6109 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_post_confirmation_price_le40 | 133 | 129 | 51.9380 | 2.9255 | 1.1345 | 11.2600 | 1.4894 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| core_mainstream_price_le_40 | 795 | 115 | 47.8261 | 2.8613 | 0.0000 | 9.6818 | 1.5459 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream_price_le40 | 119 | 115 | 47.8261 | 2.8613 | 0.0000 | 9.6818 | 1.5459 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| hot_theme | 122 | 32 | 46.8750 | 6.0255 | 0.0000 | -0.4934 | 1.8666 | medium_mature_sample_research_only | mixed_vs_baseline_same_condition |
| core_mainstream | 910 | 131 | 45.8015 | 2.4796 | 0.0000 | 8.8646 | 1.5754 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream | 135 | 131 | 45.8015 | 2.4796 | 0.0000 | 8.8646 | 1.5754 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| hot_theme_price_le_40 | 99 | 25 | 44.0000 | 4.6890 | -0.4255 | 4.0000 | 2.6836 | directional_only_below_promotion_review_size | directionally_better_than_baseline_same_condition |
| price_le40_exclude_wv | 720 | 86 | 41.8605 | 3.1947 | -1.0524 | 10.6916 | 2.3952 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_price_le40_exclude_wv | 89 | 86 | 41.8605 | 3.1947 | -1.0524 | 10.6916 | 2.3952 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_quartile_level | 1092 | 128 | 40.6250 | 2.1595 | -1.6242 | 7.5605 | 0.9418 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_or_low_level | 1626 | 193 | 39.3782 | 1.7505 | -1.5748 | 10.2116 | 1.5814 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_bottom_or_low | 199 | 193 | 39.3782 | 1.7505 | -1.5748 | 10.2116 | 1.5814 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| price_position_le_40 | 1510 | 178 | 39.3258 | 1.6215 | -1.6242 | 10.0861 | 1.5113 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_price_le40 | 184 | 178 | 39.3258 | 1.6215 | -1.6242 | 10.0861 | 1.5113 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| all_dedup_signals | 1684 | 203 | 38.9163 | 1.6483 | -1.5674 | 9.5630 | 1.4928 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout | 209 | 203 | 38.9163 | 1.6483 | -1.5674 | 9.5630 | 1.4928 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| exclude_wv_multiple_turn | 795 | 98 | 38.7755 | 2.5597 | -1.4770 | 9.5620 | 2.2043 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| non_mainstream | 771 | 71 | 25.3521 | 0.1023 | -3.4188 | 6.2510 | 0.9071 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |

## Guardrails

- This is a research/backtest grid, not a production model change.
- All rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- A higher win rate is not enough for promotion without sample size, average return, median return, and stability review.
- TDCC rows are very small in this sample and should be treated as directional only.
- Taxonomy is used as a read-only segment label, not as historical proof of theme state at the signal date.
