# W-Bottom Split Entry Outcome Backtest

- generated_at: `2026-06-26 23:32:11 Asia/Taipei`
- source_research_id: `w_bottom_combined_condition_backtest`
- production impact: `none`
- price convention: entry uses next trading day's open; exit uses exit day's close.
- breakout surface: neckline volume breakout confirmation and optional post-confirmation entries.
- early-entry surface: second-low/right-low observation entry before neckline completion.
- success definition is outcome-rule specific; fixed-horizon rules use positive return, target rules use target-before-stop.

## Top Variant Rows By Split Surface

| surface_id | entry_rule_id | outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 119 | 115 | 55.6522 | 55.6522 | 3.0916 | 2.0979 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | core_mainstream_price_le40 | 89 | 78 | 55.1282 | 55.1282 | 5.0420 | 1.0638 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | core_mainstream | 100 | 89 | 55.0562 | 55.0562 | 4.5691 | 1.0638 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream | 135 | 131 | 54.9618 | 54.9618 | 3.0741 | 1.9108 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream_price_le40 | 119 | 103 | 54.3689 | 54.3689 | 7.7558 | 2.4064 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream | 135 | 118 | 54.2373 | 54.2373 | 8.0635 | 2.7142 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream | 135 | 126 | 53.9683 | 53.9683 | 5.7218 | 2.0703 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream_price_le40 | 119 | 117 | 53.8462 | 53.8462 | 3.1190 | 0.8021 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream | 135 | 133 | 53.3835 | 53.3835 | 2.9555 | 0.6826 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | price_le40_exclude_wv | 89 | 75 | 53.3333 | 53.3333 | 5.4715 | 0.9913 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | exclude_wv_multiple_turn | 101 | 87 | 52.8736 | 52.8736 | 5.5774 | 0.9913 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream_price_le40 | 119 | 111 | 52.2523 | 52.2523 | 5.3278 | 1.4673 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | exclude_wv_multiple_turn | 101 | 95 | 51.5789 | 51.5789 | 5.8440 | 1.4673 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | price_le40_exclude_wv | 89 | 83 | 50.6024 | 50.6024 | 6.0801 | 1.4118 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | exclude_wv_multiple_turn | 75 | 64 | 48.4375 | 48.4375 | 2.2193 | -0.5756 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 89 | 87 | 48.2759 | 48.2759 | 2.5846 | -0.5302 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | price_le40_exclude_wv | 67 | 56 | 48.2143 | 48.2143 | 2.3918 | -0.5756 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 143 | 126 | 47.6190 | 47.6190 | 2.6331 | -0.4385 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 133 | 116 | 47.4138 | 47.4138 | 2.5733 | -0.4385 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | all | 150 | 133 | 47.3684 | 47.3684 | 2.3260 | -0.5038 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | all | 209 | 207 | 47.3430 | 47.3430 | 2.0930 | -0.5249 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_position_252_le_40 | 184 | 182 | 47.2527 | 47.2527 | 2.1079 | -0.6079 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | bottom_or_low_level | 199 | 197 | 47.2081 | 47.2081 | 2.1189 | -0.6908 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | core_mainstream_price_le40 | 89 | 89 | 47.1910 | 47.1910 | 1.4484 | -0.3413 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | bottom_or_low_level | 143 | 142 | 47.1831 | 47.1831 | 1.4248 | -0.3790 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_le40_exclude_wv | 89 | 87 | 47.1264 | 47.1264 | 3.5731 | -0.3953 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | all | 150 | 149 | 46.9799 | 46.9799 | 1.2777 | -0.4167 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | price_le40_exclude_wv | 67 | 66 | 46.9697 | 46.9697 | 1.2390 | 0.0000 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream | 100 | 98 | 46.9388 | 46.9388 | 2.3844 | -0.8732 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | bottom_or_low_level | 199 | 194 | 46.9072 | 46.9072 | 1.6812 | -0.5027 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_le40_exclude_wv | 89 | 88 | 46.5909 | 46.5909 | 2.3067 | -0.4373 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | all | 209 | 204 | 46.5686 | 46.5686 | 1.6471 | -0.5027 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 199 | 172 | 46.5116 | 46.5116 | 4.0488 | -0.9324 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | price_position_252_le_40 | 133 | 132 | 46.2121 | 46.2121 | 1.3044 | -0.4362 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 184 | 158 | 46.2025 | 46.2025 | 4.0972 | -0.9324 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | all | 209 | 182 | 46.1538 | 46.1538 | 4.3725 | -1.0475 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | all | 209 | 193 | 46.1140 | 46.1140 | 3.3598 | -1.4124 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | core_mainstream | 100 | 100 | 46.0000 | 46.0000 | 1.0879 | -0.4362 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_position_252_le_40 | 184 | 179 | 45.8101 | 45.8101 | 1.3979 | -0.5128 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | exclude_wv_multiple_turn | 101 | 99 | 45.4545 | 45.4545 | 3.1873 | -0.5780 | medium_mature_sample_research_only |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- The prior 10-day hold metric is only one outcome rule, not the W model definition.
- Early-entry success is separated from breakout-confirmation success.
