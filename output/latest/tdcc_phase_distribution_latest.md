# TDCC Phase Distribution

- generated_at: 2026-05-30 12:49:26 Asia/Taipei
- latest_signal_count: 1217
- phase_mature_d5_count: 81
- phase_mature_d10_count: 41
- phase_mature_d20_count: 0

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 491.0 | 40.35 |
| tdcc_leading_price | 281.0 | 23.09 |
| tdcc_price_divergence | 223.0 | 18.32 |
| overheated_after_tdcc | 104.0 | 8.55 |
| price_leading_tdcc | 80.0 | 6.57 |
| failed_after_tdcc | 19.0 | 1.56 |
| tdcc_price_confirmed | 19.0 | 1.56 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 373.0 |
| 1 | overheated_after_tdcc | 39.0 |
| 1 | price_leading_tdcc | 37.0 |
| 10 | tdcc_leading_price | 1.0 |
| 11 | tdcc_leading_price | 1.0 |
| 13 | tdcc_price_divergence | 2.0 |
| 14 | tdcc_price_divergence | 1.0 |
| 15 | tdcc_leading_price | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 17 | tdcc_leading_price | 1.0 |
| 2 | failed_after_tdcc | 8.0 |
| 2 | insufficient_price_context | 49.0 |
| 2 | overheated_after_tdcc | 30.0 |
| 2 | price_leading_tdcc | 18.0 |
| 2 | tdcc_leading_price | 92.0 |
| 2 | tdcc_price_confirmed | 6.0 |
| 2 | tdcc_price_divergence | 64.0 |
| 25 | tdcc_leading_price | 2.0 |
| 25 | tdcc_price_divergence | 2.0 |
| 3 | failed_after_tdcc | 3.0 |
| 3 | insufficient_price_context | 27.0 |
| 3 | overheated_after_tdcc | 17.0 |
| 3 | price_leading_tdcc | 11.0 |
| 3 | tdcc_leading_price | 69.0 |
| 3 | tdcc_price_confirmed | 3.0 |
| 3 | tdcc_price_divergence | 38.0 |
| 4 | failed_after_tdcc | 7.0 |
| 4 | insufficient_price_context | 38.0 |
| 4 | overheated_after_tdcc | 17.0 |
| 4 | price_leading_tdcc | 14.0 |
| 4 | tdcc_leading_price | 103.0 |
| 4 | tdcc_price_confirmed | 10.0 |
| 4 | tdcc_price_divergence | 101.0 |
| 5 | overheated_after_tdcc | 1.0 |
| 5 | tdcc_leading_price | 2.0 |
| 5 | tdcc_price_divergence | 7.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 2.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 2.0 |
| 7 | insufficient_price_context | 1.0 |
| 7 | tdcc_leading_price | 3.0 |
| 7 | tdcc_price_divergence | 2.0 |
| 8 | tdcc_leading_price | 1.0 |
| 8 | tdcc_price_divergence | 4.0 |
| 9 | insufficient_price_context | 1.0 |
| 9 | tdcc_leading_price | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 169.0 |
| all_thresholds_up | tdcc_leading_price | 138.0 |
| all_thresholds_up | tdcc_price_divergence | 110.0 |
| all_thresholds_up | overheated_after_tdcc | 55.0 |
| all_thresholds_up | price_leading_tdcc | 40.0 |
| all_thresholds_up | failed_after_tdcc | 9.0 |
| all_thresholds_up | tdcc_price_confirmed | 9.0 |
| high_thresholds_up | insufficient_price_context | 213.0 |
| high_thresholds_up | tdcc_leading_price | 181.0 |
| high_thresholds_up | tdcc_price_divergence | 142.0 |
| high_thresholds_up | overheated_after_tdcc | 60.0 |
| high_thresholds_up | price_leading_tdcc | 50.0 |
| high_thresholds_up | failed_after_tdcc | 11.0 |
| high_thresholds_up | tdcc_price_confirmed | 10.0 |
| over_800_or_above | insufficient_price_context | 327.0 |
| over_800_or_above | tdcc_leading_price | 231.0 |
| over_800_or_above | tdcc_price_divergence | 175.0 |
| over_800_or_above | overheated_after_tdcc | 78.0 |
| over_800_or_above | price_leading_tdcc | 65.0 |
| over_800_or_above | failed_after_tdcc | 15.0 |
| over_800_or_above | tdcc_price_confirmed | 15.0 |
| over_1000_only | insufficient_price_context | 50.0 |
| over_1000_only | tdcc_leading_price | 19.0 |
| over_1000_only | tdcc_price_divergence | 10.0 |
| over_1000_only | overheated_after_tdcc | 9.0 |
| over_1000_only | price_leading_tdcc | 2.0 |
| over_1000_only | tdcc_price_confirmed | 1.0 |
| consecutive_2w | tdcc_leading_price | 281.0 |
| consecutive_2w | tdcc_price_divergence | 223.0 |
| consecutive_2w | insufficient_price_context | 118.0 |
| consecutive_2w | overheated_after_tdcc | 65.0 |
| consecutive_2w | price_leading_tdcc | 43.0 |
| consecutive_2w | failed_after_tdcc | 19.0 |
| consecutive_2w | tdcc_price_confirmed | 19.0 |
| consecutive_3w | tdcc_leading_price | 189.0 |
| consecutive_3w | tdcc_price_divergence | 159.0 |
| consecutive_3w | insufficient_price_context | 69.0 |
| consecutive_3w | overheated_after_tdcc | 35.0 |
| consecutive_3w | price_leading_tdcc | 25.0 |
| consecutive_3w | tdcc_price_confirmed | 13.0 |
| consecutive_3w | failed_after_tdcc | 11.0 |
| quiet_accumulation | tdcc_leading_price | 106.0 |
| quiet_accumulation | tdcc_price_divergence | 98.0 |
| quiet_accumulation | insufficient_price_context | 28.0 |
| quiet_accumulation | failed_after_tdcc | 7.0 |
| quiet_accumulation | price_leading_tdcc | 3.0 |
| quiet_accumulation | tdcc_price_confirmed | 1.0 |
| early_breakout | tdcc_leading_price | 2.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | insufficient_price_context | 42.0 |
| strong_momentum | price_leading_tdcc | 25.0 |
| strong_momentum | tdcc_leading_price | 10.0 |
| strong_momentum | tdcc_price_confirmed | 7.0 |
| strong_momentum | tdcc_price_divergence | 4.0 |
| strong_momentum | overheated_after_tdcc | 1.0 |
| overheated | overheated_after_tdcc | 104.0 |
| overheated | insufficient_price_context | 34.0 |
| overheated | price_leading_tdcc | 29.0 |
| overheated | tdcc_leading_price | 6.0 |

## Phase 後續成熟績效

- phase-level D+20 尚未成熟，不可做 phase 勝率結論。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 11.0 | 13.80 | 10.44 | 9.0 | 20.05 | 11.05 | 0.0 |  |  | 29.87 | -3.55 |
| overheated_after_tdcc | 42.0 | 8.41 | 6.26 | 18.0 | 22.85 | 13.31 | 0.0 |  |  | 29.50 | -6.79 |
| price_leading_tdcc | 18.0 | 6.17 | 3.62 | 8.0 | 13.39 | 10.33 | 0.0 |  |  | 21.08 | -7.07 |
| tdcc_leading_price | 6.0 | 4.11 | 0.78 | 5.0 | 3.11 | 4.43 | 0.0 |  |  | 11.62 | -5.94 |
| tdcc_price_confirmed | 3.0 | 2.10 |  | 0.0 |  |  | 0.0 |  |  |  |  |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 |  | 0.0 |  |  | 19.34 | -11.15 |
