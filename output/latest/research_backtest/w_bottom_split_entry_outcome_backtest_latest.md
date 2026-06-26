# W-Bottom Split Entry Outcome Backtest

- generated_at: `2026-06-26 13:47:10 Asia/Taipei`
- source_research_id: `w_bottom_combined_condition_backtest`
- production impact: `none`
- price convention: entry uses next trading day's open; exit uses exit day's close.
- breakout surface: neckline volume breakout confirmation and optional post-confirmation entries.
- early-entry surface: second-low/right-low observation entry before neckline completion.
- success definition is outcome-rule specific; fixed-horizon rules use positive return, target rules use target-before-stop.

## Top Variant Rows By Split Surface

| surface_id | entry_rule_id | outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | core_mainstream | 24 | 19 | 57.8947 | 57.8947 | 5.4257 | 1.4493 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream | 41 | 30 | 56.6667 | 56.6667 | 5.6025 | 5.3452 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_20d_close_positive_return | core_mainstream_price_le40 | 19 | 16 | 56.2500 | 56.2500 | 4.1518 | 6.3629 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream_price_le40 | 32 | 22 | 54.5455 | 54.5455 | 2.8345 | 5.3452 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 32 | 29 | 51.7241 | 51.7241 | 0.3406 | 0.7519 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream | 41 | 33 | 51.5152 | 51.5152 | 2.1008 | 1.4118 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_le40_exclude_wv | 22 | 20 | 50.0000 | 50.0000 | 3.1451 | 0.0870 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_20d_close_positive_return | price_position_252_le_40 | 27 | 20 | 50.0000 | 50.0000 | 1.9330 | 0.8606 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream | 41 | 38 | 50.0000 | 50.0000 | 0.2967 | 0.0870 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_position_252_le_40 | 43 | 39 | 48.7179 | 48.7179 | 0.8836 | -0.5780 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | exclude_wv_multiple_turn | 28 | 27 | 48.1481 | 48.1481 | 2.8204 | -1.0116 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream_price_le40 | 32 | 25 | 48.0000 | 48.0000 | 1.5331 | -4.1118 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | all | 33 | 23 | 47.8261 | 47.8261 | 2.3142 | -2.4648 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_le40_exclude_wv | 22 | 21 | 47.6190 | 47.6190 | 4.0816 | -1.0116 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | exclude_wv_multiple_turn | 28 | 21 | 47.6190 | 47.6190 | 3.4841 | -4.0000 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_20d_close_positive_return | core_mainstream | 24 | 21 | 47.6190 | 47.6190 | 2.2699 | -2.0666 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | all | 55 | 42 | 47.6190 | 47.6190 | 1.3301 | -2.9756 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 29 | 19 | 47.3684 | 47.3684 | 2.9899 | -2.4648 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 27 | 17 | 47.0588 | 47.0588 | 4.1771 | -2.4648 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | all | 55 | 51 | 47.0588 | 47.0588 | 0.3326 | -0.5780 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | bottom_or_low_level | 49 | 45 | 46.6667 | 46.6667 | -0.0284 | -0.5780 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | exclude_wv_multiple_turn | 28 | 26 | 46.1538 | 46.1538 | 1.9933 | -0.9498 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 43 | 26 | 46.1538 | 46.1538 | 0.6007 | -4.1826 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | all | 55 | 37 | 45.9459 | 45.9459 | 2.1791 | -1.2800 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_20d_close_positive_return | bottom_or_low_level | 29 | 22 | 45.4545 | 45.4545 | 0.8977 | -2.8666 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | price_position_252_le_40 | 43 | 31 | 45.1613 | 45.1613 | 1.5168 | -4.1118 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 49 | 31 | 45.1613 | 45.1613 | -1.0550 | -7.2195 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 19 | 18 | 44.4444 | 44.4444 | -0.1813 | -1.7300 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | exclude_wv_multiple_turn | 28 | 18 | 44.4444 | 44.4444 | -1.0270 | -1.2128 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_position_252_le_40 | 43 | 41 | 43.9024 | 43.9024 | 1.8217 | -1.0116 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream | 41 | 39 | 43.5897 | 43.5897 | 0.3446 | -1.0116 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream | 24 | 23 | 43.4783 | 43.4783 | -0.6747 | -1.4599 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | all | 55 | 53 | 43.3962 | 43.3962 | 0.6844 | -1.0116 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream_price_le40 | 32 | 30 | 43.3333 | 43.3333 | 1.1350 | -0.7058 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_20d_close_positive_return | all | 33 | 26 | 42.3077 | 42.3077 | 0.6585 | -2.5161 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | all | 33 | 31 | 41.9355 | 41.9355 | -0.6886 | -2.0000 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | bottom_or_low_level | 49 | 36 | 41.6667 | 41.6667 | -0.3194 | -4.5470 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | bottom_or_low_level | 29 | 27 | 40.7407 | 40.7407 | -0.9454 | -2.4648 | directional_only_below_promotion_review_size |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | bottom_or_low_level | 49 | 47 | 40.4255 | 40.4255 | 0.6574 | -1.1507 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | price_le40_exclude_wv | 22 | 15 | 40.0000 | 40.0000 | 5.0609 | -4.5113 | directional_only_below_promotion_review_size |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- The prior 10-day hold metric is only one outcome rule, not the W model definition.
- Early-entry success is separated from breakout-confirmation success.
