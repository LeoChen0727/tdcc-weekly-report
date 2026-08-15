# TDCC Phase Distribution

- generated_at: 2026-08-15 15:54:15 Asia/Taipei
- latest_signal_count: 1190
- phase_mature_d5_count: 609
- phase_mature_d10_count: 556
- phase_mature_d20_count: 426

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 890.0 | 74.79 |
| tdcc_leading_price | 140.0 | 11.76 |
| tdcc_price_divergence | 62.0 | 5.21 |
| price_leading_tdcc | 44.0 | 3.70 |
| overheated_after_tdcc | 39.0 | 3.28 |
| tdcc_price_confirmed | 10.0 | 0.84 |
| failed_after_tdcc | 5.0 | 0.42 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 419.0 |
| 1 | overheated_after_tdcc | 6.0 |
| 1 | price_leading_tdcc | 7.0 |
| 10 | insufficient_price_context | 2.0 |
| 10 | price_leading_tdcc | 1.0 |
| 10 | tdcc_leading_price | 4.0 |
| 10 | tdcc_price_confirmed | 1.0 |
| 10 | tdcc_price_divergence | 1.0 |
| 11 | insufficient_price_context | 1.0 |
| 11 | tdcc_leading_price | 1.0 |
| 12 | insufficient_price_context | 1.0 |
| 12 | tdcc_leading_price | 1.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 4.0 |
| 13 | tdcc_leading_price | 1.0 |
| 13 | tdcc_price_divergence | 1.0 |
| 14 | overheated_after_tdcc | 1.0 |
| 15 | insufficient_price_context | 4.0 |
| 15 | tdcc_leading_price | 3.0 |
| 15 | tdcc_price_divergence | 6.0 |
| 16 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 3.0 |
| 2 | insufficient_price_context | 237.0 |
| 2 | overheated_after_tdcc | 19.0 |
| 2 | price_leading_tdcc | 21.0 |
| 2 | tdcc_leading_price | 47.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 20.0 |
| 27 | tdcc_leading_price | 1.0 |
| 3 | failed_after_tdcc | 1.0 |
| 3 | insufficient_price_context | 88.0 |
| 3 | overheated_after_tdcc | 9.0 |
| 3 | price_leading_tdcc | 7.0 |
| 3 | tdcc_leading_price | 24.0 |
| 3 | tdcc_price_confirmed | 2.0 |
| 3 | tdcc_price_divergence | 12.0 |
| 37 | insufficient_price_context | 1.0 |
| 4 | failed_after_tdcc | 1.0 |
| 4 | insufficient_price_context | 58.0 |
| 4 | overheated_after_tdcc | 3.0 |
| 4 | price_leading_tdcc | 6.0 |
| 4 | tdcc_leading_price | 21.0 |
| 4 | tdcc_price_confirmed | 5.0 |
| 4 | tdcc_price_divergence | 4.0 |
| 5 | insufficient_price_context | 30.0 |
| 5 | price_leading_tdcc | 1.0 |
| 5 | tdcc_leading_price | 12.0 |
| 5 | tdcc_price_divergence | 7.0 |
| 6 | insufficient_price_context | 21.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | tdcc_leading_price | 10.0 |
| 6 | tdcc_price_divergence | 4.0 |
| 7 | insufficient_price_context | 17.0 |
| 7 | price_leading_tdcc | 1.0 |
| 7 | tdcc_leading_price | 6.0 |
| 7 | tdcc_price_divergence | 2.0 |
| 8 | insufficient_price_context | 5.0 |
| 8 | tdcc_leading_price | 8.0 |
| 8 | tdcc_price_divergence | 1.0 |
| 9 | insufficient_price_context | 2.0 |
| 9 | tdcc_leading_price | 1.0 |
| 9 | tdcc_price_divergence | 2.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 195.0 |
| all_thresholds_up | tdcc_leading_price | 137.0 |
| all_thresholds_up | tdcc_price_divergence | 62.0 |
| all_thresholds_up | price_leading_tdcc | 42.0 |
| all_thresholds_up | overheated_after_tdcc | 39.0 |
| all_thresholds_up | tdcc_price_confirmed | 10.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| high_thresholds_up | insufficient_price_context | 315.0 |
| high_thresholds_up | tdcc_leading_price | 140.0 |
| high_thresholds_up | tdcc_price_divergence | 62.0 |
| high_thresholds_up | price_leading_tdcc | 44.0 |
| high_thresholds_up | overheated_after_tdcc | 39.0 |
| high_thresholds_up | tdcc_price_confirmed | 10.0 |
| high_thresholds_up | failed_after_tdcc | 5.0 |
| over_800_or_above | insufficient_price_context | 551.0 |
| over_800_or_above | tdcc_leading_price | 140.0 |
| over_800_or_above | tdcc_price_divergence | 62.0 |
| over_800_or_above | price_leading_tdcc | 44.0 |
| over_800_or_above | overheated_after_tdcc | 39.0 |
| over_800_or_above | tdcc_price_confirmed | 10.0 |
| over_800_or_above | failed_after_tdcc | 5.0 |
| over_1000_only | insufficient_price_context | 77.0 |
| consecutive_2w | insufficient_price_context | 471.0 |
| consecutive_2w | tdcc_leading_price | 140.0 |
| consecutive_2w | tdcc_price_divergence | 62.0 |
| consecutive_2w | price_leading_tdcc | 37.0 |
| consecutive_2w | overheated_after_tdcc | 33.0 |
| consecutive_2w | tdcc_price_confirmed | 10.0 |
| consecutive_2w | failed_after_tdcc | 5.0 |
| consecutive_3w | insufficient_price_context | 234.0 |
| consecutive_3w | tdcc_leading_price | 93.0 |
| consecutive_3w | tdcc_price_divergence | 42.0 |
| consecutive_3w | price_leading_tdcc | 16.0 |
| consecutive_3w | overheated_after_tdcc | 14.0 |
| consecutive_3w | tdcc_price_confirmed | 8.0 |
| consecutive_3w | failed_after_tdcc | 2.0 |
| quiet_accumulation | insufficient_price_context | 93.0 |
| quiet_accumulation | tdcc_leading_price | 85.0 |
| quiet_accumulation | tdcc_price_divergence | 49.0 |
| quiet_accumulation | price_leading_tdcc | 6.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| quiet_accumulation | tdcc_price_confirmed | 2.0 |
| quiet_accumulation | overheated_after_tdcc | 2.0 |
| early_breakout | insufficient_price_context | 1.0 |
| early_breakout | tdcc_leading_price | 1.0 |
| strong_momentum | insufficient_price_context | 13.0 |
| strong_momentum | price_leading_tdcc | 12.0 |
| strong_momentum | overheated_after_tdcc | 6.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| strong_momentum | tdcc_leading_price | 1.0 |
| overheated | overheated_after_tdcc | 39.0 |
| overheated | price_leading_tdcc | 5.0 |
| overheated | tdcc_price_confirmed | 3.0 |
| overheated | insufficient_price_context | 2.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 5.0 | 2.05 | 2.34 | 3.0 | 20.48 | 12.57 | 0.0 |  |  | 30.67 | -12.90 |
| insufficient_price_context | 245.0 | 1.55 | -0.38 | 224.0 | 1.69 | -1.03 | 150.0 | -5.12 | -4.21 | 13.75 | -9.48 |
| overheated_after_tdcc | 135.0 | 3.25 | 1.60 | 124.0 | 2.31 | 1.40 | 119.0 | -2.09 | -1.83 | 18.69 | -12.10 |
| price_leading_tdcc | 126.0 | 0.76 | -0.67 | 120.0 | -0.50 | -0.34 | 104.0 | -2.61 | -1.90 | 12.91 | -10.60 |
| tdcc_leading_price | 42.0 | -0.61 | -0.14 | 36.0 | 0.04 | -1.86 | 30.0 | -3.30 | -3.14 | 9.43 | -9.01 |
| tdcc_price_confirmed | 13.0 | -2.06 | -1.91 | 11.0 | 0.23 | 0.73 | 11.0 | -3.80 | -2.80 | 12.27 | -11.85 |
| tdcc_price_divergence | 43.0 | 1.40 | -1.83 | 38.0 | 5.98 | -4.63 | 12.0 | -4.80 | 1.58 | 17.25 | -9.90 |
