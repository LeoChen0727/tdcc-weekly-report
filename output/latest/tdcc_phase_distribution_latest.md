# TDCC Phase Distribution

- generated_at: 2026-10-03 15:42:45 Asia/Taipei
- latest_signal_count: 1075
- phase_mature_d5_count: 887
- phase_mature_d10_count: 834
- phase_mature_d20_count: 738

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 725.0 | 67.44 |
| tdcc_leading_price | 177.0 | 16.47 |
| tdcc_price_divergence | 72.0 | 6.70 |
| price_leading_tdcc | 43.0 | 4.00 |
| overheated_after_tdcc | 34.0 | 3.16 |
| tdcc_price_confirmed | 20.0 | 1.86 |
| failed_after_tdcc | 4.0 | 0.37 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 389.0 |
| 1 | overheated_after_tdcc | 5.0 |
| 1 | price_leading_tdcc | 8.0 |
| 10 | insufficient_price_context | 1.0 |
| 10 | overheated_after_tdcc | 1.0 |
| 10 | tdcc_leading_price | 3.0 |
| 10 | tdcc_price_confirmed | 1.0 |
| 10 | tdcc_price_divergence | 2.0 |
| 11 | insufficient_price_context | 2.0 |
| 11 | price_leading_tdcc | 1.0 |
| 11 | tdcc_leading_price | 3.0 |
| 11 | tdcc_price_divergence | 2.0 |
| 12 | tdcc_leading_price | 4.0 |
| 12 | tdcc_price_confirmed | 1.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 1.0 |
| 13 | tdcc_leading_price | 1.0 |
| 14 | price_leading_tdcc | 1.0 |
| 14 | tdcc_leading_price | 2.0 |
| 14 | tdcc_price_divergence | 2.0 |
| 15 | tdcc_leading_price | 1.0 |
| 15 | tdcc_price_confirmed | 1.0 |
| 15 | tdcc_price_divergence | 1.0 |
| 16 | tdcc_leading_price | 2.0 |
| 16 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 155.0 |
| 2 | overheated_after_tdcc | 9.0 |
| 2 | price_leading_tdcc | 11.0 |
| 2 | tdcc_leading_price | 58.0 |
| 2 | tdcc_price_confirmed | 7.0 |
| 2 | tdcc_price_divergence | 17.0 |
| 22 | tdcc_leading_price | 3.0 |
| 22 | tdcc_price_divergence | 2.0 |
| 23 | tdcc_leading_price | 1.0 |
| 3 | failed_after_tdcc | 1.0 |
| 3 | insufficient_price_context | 67.0 |
| 3 | overheated_after_tdcc | 9.0 |
| 3 | price_leading_tdcc | 11.0 |
| 3 | tdcc_leading_price | 40.0 |
| 3 | tdcc_price_confirmed | 7.0 |
| 3 | tdcc_price_divergence | 9.0 |
| 4 | insufficient_price_context | 46.0 |
| 4 | overheated_after_tdcc | 6.0 |
| 4 | price_leading_tdcc | 6.0 |
| 4 | tdcc_leading_price | 27.0 |
| 4 | tdcc_price_confirmed | 3.0 |
| 4 | tdcc_price_divergence | 15.0 |
| 5 | insufficient_price_context | 24.0 |
| 5 | overheated_after_tdcc | 3.0 |
| 5 | price_leading_tdcc | 2.0 |
| 5 | tdcc_leading_price | 13.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | insufficient_price_context | 15.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 3.0 |
| 6 | tdcc_leading_price | 5.0 |
| 6 | tdcc_price_divergence | 3.0 |
| 7 | insufficient_price_context | 12.0 |
| 7 | tdcc_leading_price | 7.0 |
| 7 | tdcc_price_divergence | 6.0 |
| 8 | insufficient_price_context | 8.0 |
| 8 | tdcc_leading_price | 4.0 |
| 8 | tdcc_price_divergence | 6.0 |
| 9 | failed_after_tdcc | 1.0 |
| 9 | insufficient_price_context | 5.0 |
| 9 | tdcc_leading_price | 3.0 |
| 9 | tdcc_price_divergence | 2.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | tdcc_leading_price | 121.0 |
| all_thresholds_up | insufficient_price_context | 99.0 |
| all_thresholds_up | tdcc_price_divergence | 55.0 |
| all_thresholds_up | price_leading_tdcc | 33.0 |
| all_thresholds_up | overheated_after_tdcc | 26.0 |
| all_thresholds_up | tdcc_price_confirmed | 17.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| high_thresholds_up | tdcc_leading_price | 177.0 |
| high_thresholds_up | insufficient_price_context | 150.0 |
| high_thresholds_up | tdcc_price_divergence | 72.0 |
| high_thresholds_up | price_leading_tdcc | 43.0 |
| high_thresholds_up | overheated_after_tdcc | 34.0 |
| high_thresholds_up | tdcc_price_confirmed | 20.0 |
| high_thresholds_up | failed_after_tdcc | 4.0 |
| over_800_or_above | insufficient_price_context | 410.0 |
| over_800_or_above | tdcc_leading_price | 177.0 |
| over_800_or_above | tdcc_price_divergence | 72.0 |
| over_800_or_above | price_leading_tdcc | 43.0 |
| over_800_or_above | overheated_after_tdcc | 34.0 |
| over_800_or_above | tdcc_price_confirmed | 20.0 |
| over_800_or_above | failed_after_tdcc | 4.0 |
| over_1000_only | insufficient_price_context | 104.0 |
| consecutive_2w | insufficient_price_context | 336.0 |
| consecutive_2w | tdcc_leading_price | 177.0 |
| consecutive_2w | tdcc_price_divergence | 72.0 |
| consecutive_2w | price_leading_tdcc | 35.0 |
| consecutive_2w | overheated_after_tdcc | 29.0 |
| consecutive_2w | tdcc_price_confirmed | 20.0 |
| consecutive_2w | failed_after_tdcc | 4.0 |
| consecutive_3w | insufficient_price_context | 181.0 |
| consecutive_3w | tdcc_leading_price | 119.0 |
| consecutive_3w | tdcc_price_divergence | 55.0 |
| consecutive_3w | price_leading_tdcc | 24.0 |
| consecutive_3w | overheated_after_tdcc | 20.0 |
| consecutive_3w | tdcc_price_confirmed | 13.0 |
| consecutive_3w | failed_after_tdcc | 2.0 |
| quiet_accumulation | tdcc_leading_price | 118.0 |
| quiet_accumulation | tdcc_price_divergence | 56.0 |
| quiet_accumulation | insufficient_price_context | 11.0 |
| quiet_accumulation | tdcc_price_confirmed | 6.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| quiet_accumulation | price_leading_tdcc | 1.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 22.0 |
| strong_momentum | insufficient_price_context | 4.0 |
| strong_momentum | tdcc_price_confirmed | 2.0 |
| strong_momentum | overheated_after_tdcc | 2.0 |
| strong_momentum | tdcc_leading_price | 2.0 |
| overheated | overheated_after_tdcc | 34.0 |
| overheated | price_leading_tdcc | 7.0 |
| overheated | insufficient_price_context | 1.0 |
| overheated | tdcc_leading_price | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 6.0 | 3.07 | 2.01 | 6.0 | 13.47 | 11.06 | 5.0 | 22.03 | 17.10 | 23.61 | -8.31 |
| insufficient_price_context | 348.0 | 1.56 | -0.03 | 328.0 | 2.26 | 0.16 | 287.0 | 2.51 | -0.36 | 12.93 | -8.48 |
| overheated_after_tdcc | 191.0 | 3.19 | 2.10 | 185.0 | 2.45 | 1.31 | 171.0 | 0.09 | -0.73 | 17.63 | -11.23 |
| price_leading_tdcc | 185.0 | 1.73 | 0.29 | 174.0 | 0.48 | -0.12 | 154.0 | -0.58 | -1.83 | 12.63 | -9.76 |
| tdcc_leading_price | 61.0 | 0.33 | -0.10 | 57.0 | -0.29 | -2.16 | 50.0 | -0.02 | -2.01 | 8.98 | -8.04 |
| tdcc_price_confirmed | 27.0 | 0.45 | 0.04 | 21.0 | 4.28 | 3.69 | 17.0 | -1.20 | -2.08 | 13.19 | -7.87 |
| tdcc_price_divergence | 69.0 | 2.95 | 0.61 | 63.0 | 5.77 | 2.01 | 54.0 | 9.80 | 5.06 | 16.07 | -7.14 |
