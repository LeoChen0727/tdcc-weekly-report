# W-Bottom Combined Condition Backtest

- generated_at: `2026-06-26 23:29:29 Asia/Taipei`
- source_research_id: `w_bottom_nearest_micro_anchor_event_replay`
- baseline_event_set: `baseline_current_detector`
- variant_event_set: `variant_nearest_micro_45d_event_replay`
- production impact: `none`
- revenue/catalyst feature status: `pending_historical_feature_join_not_evaluated`
- note: revenue/catalyst current daily artifacts are not joined because they are not historical signal-date features in this research packet.

## Event Set Counts

| event_set_id | comparison_status | count |
| --- | --- | --- |
| baseline_current_detector | baseline_only | 846 |
| baseline_current_detector | common | 1083 |
| variant_nearest_micro_45d_event_replay | common | 1083 |
| variant_nearest_micro_45d_event_replay | variant_only | 608 |

## Price-Level Counts

| event_set_id | price_level_bucket | count |
| --- | --- | --- |
| baseline_current_detector | bottom_quartile_level | 1244 |
| baseline_current_detector | low_level | 619 |
| baseline_current_detector | mid_level | 66 |
| variant_nearest_micro_45d_event_replay | bottom_quartile_level | 1098 |
| variant_nearest_micro_45d_event_replay | low_level | 535 |
| variant_nearest_micro_45d_event_replay | mid_level | 58 |

## Top Variant A-Path Condition Rows

| condition_set_id | sample_size | mature_sample_size | win_rate_pct | avg_return_pct | median_return_pct | delta_win_rate_pct_vs_baseline | delta_avg_return_pct_vs_baseline | sample_warning | research_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core_mainstream_price_le40_exclude_wv | 358 | 57 | 54.3860 | 5.1225 | 1.9108 | 10.4835 | 2.0961 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_post_confirmation | 150 | 147 | 51.7007 | 3.0946 | 0.9709 | 10.9864 | 1.6007 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_post_confirmation_price_le40 | 133 | 130 | 51.5385 | 2.8968 | 0.9432 | 11.2023 | 1.4795 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| core_mainstream_price_le_40 | 799 | 115 | 47.8261 | 2.8613 | 0.0000 | 9.6818 | 1.5459 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream_price_le40 | 119 | 115 | 47.8261 | 2.8613 | 0.0000 | 9.6818 | 1.5459 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| hot_theme | 123 | 32 | 46.8750 | 6.0255 | 0.0000 | -0.4934 | 1.8666 | medium_mature_sample_research_only | mixed_vs_baseline_same_condition |
| core_mainstream | 914 | 131 | 45.8015 | 2.4796 | 0.0000 | 8.8646 | 1.5754 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_core_mainstream | 135 | 131 | 45.8015 | 2.4796 | 0.0000 | 8.8646 | 1.5754 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| hot_theme_price_le_40 | 100 | 25 | 44.0000 | 4.6890 | -0.4255 | 4.0000 | 2.6836 | directional_only_below_promotion_review_size | directionally_better_than_baseline_same_condition |
| price_le40_exclude_wv | 723 | 87 | 41.3793 | 3.1487 | -0.8547 | 10.6101 | 2.3698 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_price_le40_exclude_wv | 89 | 87 | 41.3793 | 3.1487 | -0.8547 | 10.6101 | 2.3698 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_quartile_level | 1098 | 129 | 40.3101 | 2.1365 | -1.5748 | 7.5101 | 0.9350 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| bottom_or_low_level | 1633 | 194 | 39.1753 | 1.7373 | -1.5507 | 10.1597 | 1.5733 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_bottom_or_low | 199 | 194 | 39.1753 | 1.7373 | -1.5507 | 10.1597 | 1.5733 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| price_position_le_40 | 1517 | 179 | 39.1061 | 1.6079 | -1.5748 | 10.0364 | 1.5031 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout_price_le40 | 184 | 179 | 39.1061 | 1.6079 | -1.5748 | 10.0364 | 1.5031 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| all_dedup_signals | 1691 | 204 | 38.7255 | 1.6363 | -1.5471 | 9.5176 | 1.4855 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| has_neckline_breakout | 209 | 204 | 38.7255 | 1.6363 | -1.5471 | 9.5176 | 1.4855 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| exclude_wv_multiple_turn | 798 | 99 | 38.3838 | 2.5257 | -1.3867 | 9.4949 | 2.1832 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |
| non_mainstream | 773 | 72 | 25.0000 | 0.0896 | -3.3948 | 6.1111 | 0.8945 | medium_mature_sample_research_only | directionally_better_than_baseline_same_condition |

## Guardrails

- This is a research/backtest grid, not a production model change.
- All rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- A higher win rate is not enough for promotion without sample size, average return, median return, and stability review.
- TDCC rows are very small in this sample and should be treated as directional only.
- Taxonomy is used as a read-only segment label, not as historical proof of theme state at the signal date.
