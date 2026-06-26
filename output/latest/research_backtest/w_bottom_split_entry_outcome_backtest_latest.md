# W-Bottom Split Entry Outcome Backtest

- generated_at: `2026-06-26 21:12:48 Asia/Taipei`
- source_research_id: `w_bottom_combined_condition_backtest`
- production impact: `none`
- price convention: entry uses next trading day's open; exit uses exit day's close.
- breakout surface: neckline volume breakout confirmation and optional post-confirmation entries.
- early-entry surface: second-low/right-low observation entry before neckline completion.
- success definition is outcome-rule specific; fixed-horizon rules use positive return, target rules use target-before-stop.

## Top Variant Rows By Split Surface

| surface_id | entry_rule_id | outcome_rule_id | condition_set_id | sample_size | mature_sample_size | success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | core_mainstream_price_le40 | 89 | 77 | 55.8442 | 55.8442 | 5.1809 | 1.0638 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | core_mainstream | 100 | 88 | 55.6818 | 55.6818 | 4.6852 | 1.0950 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 119 | 115 | 55.6522 | 55.6522 | 3.0916 | 2.0979 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | core_mainstream | 135 | 131 | 54.9618 | 54.9618 | 3.0741 | 1.9108 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream_price_le40 | 119 | 102 | 54.9020 | 54.9020 | 7.9173 | 2.7142 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | price_le40_exclude_wv | 89 | 73 | 54.7945 | 54.7945 | 5.9388 | 2.1739 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | core_mainstream | 135 | 117 | 54.7009 | 54.7009 | 8.2070 | 3.0220 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream | 135 | 125 | 54.4000 | 54.4000 | 5.7712 | 2.3707 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | exclude_wv_multiple_turn | 101 | 85 | 54.1176 | 54.1176 | 5.9812 | 1.9672 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream_price_le40 | 119 | 116 | 53.4483 | 53.4483 | 3.1098 | 0.7424 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | core_mainstream | 135 | 132 | 53.0303 | 53.0303 | 2.9462 | 0.6826 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | core_mainstream_price_le40 | 119 | 110 | 52.7273 | 52.7273 | 5.3804 | 1.5009 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | exclude_wv_multiple_turn | 101 | 93 | 52.6882 | 52.6882 | 6.1400 | 1.6835 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | price_le40_exclude_wv | 89 | 81 | 51.8519 | 51.8519 | 6.4258 | 1.4673 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | exclude_wv_multiple_turn | 75 | 63 | 49.2063 | 49.2063 | 2.3442 | -0.2740 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | price_le40_exclude_wv | 67 | 55 | 49.0909 | 49.0909 | 2.5380 | -0.2740 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream_price_le40 | 89 | 87 | 48.2759 | 48.2759 | 2.5846 | -0.5302 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 143 | 125 | 48.0000 | 48.0000 | 2.6993 | -0.3731 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 133 | 115 | 47.8261 | 47.8261 | 2.6448 | -0.3731 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_30d_close_positive_return | all | 150 | 132 | 47.7273 | 47.7273 | 2.3864 | -0.4385 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | price_le40_exclude_wv | 67 | 65 | 47.6923 | 47.6923 | 1.2581 | 0.0000 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_le40_exclude_wv | 89 | 86 | 47.6744 | 47.6744 | 3.6240 | -0.1976 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | bottom_or_low_level | 143 | 139 | 47.4820 | 47.4820 | 1.4972 | -0.4167 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | all | 209 | 205 | 47.3171 | 47.3171 | 2.0975 | -0.5249 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | all | 150 | 146 | 47.2603 | 47.2603 | 1.3436 | -0.4362 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_position_252_le_40 | 184 | 180 | 47.2222 | 47.2222 | 2.1132 | -0.6079 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | bottom_or_low_level | 199 | 195 | 47.1795 | 47.1795 | 2.1238 | -0.6908 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | bottom_or_low_level | 199 | 193 | 47.1503 | 47.1503 | 1.6941 | -0.4926 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_5d_close_positive_return | price_le40_exclude_wv | 89 | 87 | 47.1264 | 47.1264 | 2.3438 | -0.3497 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | core_mainstream_price_le40 | 89 | 87 | 47.1264 | 47.1264 | 1.5483 | -0.3413 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | bottom_or_low_level | 199 | 170 | 47.0588 | 47.0588 | 4.2327 | -0.6606 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_10d_close_positive_return | core_mainstream | 100 | 98 | 46.9388 | 46.9388 | 2.3844 | -0.8732 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | all | 209 | 203 | 46.7980 | 46.7980 | 1.6592 | -0.4926 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | price_position_252_le_40 | 184 | 156 | 46.7949 | 46.7949 | 4.2982 | -0.6606 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_30d_close_positive_return | all | 209 | 180 | 46.6667 | 46.6667 | 4.5498 | -0.9324 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_20d_close_positive_return | all | 209 | 191 | 46.5969 | 46.5969 | 3.4780 | -1.4124 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | price_position_252_le_40 | 133 | 129 | 46.5116 | 46.5116 | 1.3796 | -0.4556 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | price_position_252_le_40 | 184 | 178 | 46.0674 | 46.0674 | 1.4103 | -0.5128 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | neckline_volume_breakout_next_open | fixed_10d_close_positive_return | exclude_wv_multiple_turn | 101 | 98 | 45.9184 | 45.9184 | 3.2281 | -0.4973 | medium_mature_sample_research_only |
| w_bottom_neckline_volume_breakout_confirmation | post_confirmation_next_open | fixed_5d_close_positive_return | core_mainstream | 100 | 98 | 45.9184 | 45.9184 | 1.1692 | -0.4362 | medium_mature_sample_research_only |

## Guardrails

- This is research/backtest advisory-only work.
- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.
- The prior 10-day hold metric is only one outcome rule, not the W model definition.
- Early-entry success is separated from breakout-confirmation success.
