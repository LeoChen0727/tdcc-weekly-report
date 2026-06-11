# TDCC Phase Distribution

- generated_at: 2026-06-11 23:13:55 Asia/Taipei
- latest_signal_count: 1130
- phase_mature_d5_count: 5993
- phase_mature_d10_count: 4772
- phase_mature_d20_count: 2437

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 440.0 | 38.94 |
| tdcc_leading_price | 308.0 | 27.26 |
| tdcc_price_divergence | 199.0 | 17.61 |
| price_leading_tdcc | 94.0 | 8.32 |
| overheated_after_tdcc | 52.0 | 4.60 |
| tdcc_price_confirmed | 33.0 | 2.92 |
| failed_after_tdcc | 4.0 | 0.35 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 338.0 |
| 1 | overheated_after_tdcc | 17.0 |
| 1 | price_leading_tdcc | 35.0 |
| 11 | tdcc_leading_price | 1.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 14 | tdcc_leading_price | 2.0 |
| 15 | tdcc_price_divergence | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 17 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 1.0 |
| 2 | insufficient_price_context | 38.0 |
| 2 | overheated_after_tdcc | 19.0 |
| 2 | price_leading_tdcc | 24.0 |
| 2 | tdcc_leading_price | 103.0 |
| 2 | tdcc_price_confirmed | 8.0 |
| 2 | tdcc_price_divergence | 66.0 |
| 27 | tdcc_leading_price | 2.0 |
| 27 | tdcc_price_divergence | 1.0 |
| 3 | insufficient_price_context | 26.0 |
| 3 | overheated_after_tdcc | 8.0 |
| 3 | price_leading_tdcc | 19.0 |
| 3 | tdcc_leading_price | 61.0 |
| 3 | tdcc_price_confirmed | 9.0 |
| 3 | tdcc_price_divergence | 41.0 |
| 4 | failed_after_tdcc | 1.0 |
| 4 | insufficient_price_context | 16.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 9.0 |
| 4 | tdcc_leading_price | 36.0 |
| 4 | tdcc_price_confirmed | 1.0 |
| 4 | tdcc_price_divergence | 28.0 |
| 5 | failed_after_tdcc | 2.0 |
| 5 | insufficient_price_context | 21.0 |
| 5 | overheated_after_tdcc | 6.0 |
| 5 | price_leading_tdcc | 7.0 |
| 5 | tdcc_leading_price | 88.0 |
| 5 | tdcc_price_confirmed | 14.0 |
| 5 | tdcc_price_divergence | 52.0 |
| 6 | insufficient_price_context | 1.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | tdcc_leading_price | 5.0 |
| 6 | tdcc_price_divergence | 3.0 |
| 7 | tdcc_leading_price | 4.0 |
| 7 | tdcc_price_divergence | 2.0 |
| 8 | tdcc_leading_price | 4.0 |
| 8 | tdcc_price_confirmed | 1.0 |
| 8 | tdcc_price_divergence | 1.0 |
| 9 | tdcc_leading_price | 1.0 |
| 9 | tdcc_price_divergence | 2.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 154.0 |
| all_thresholds_up | tdcc_leading_price | 151.0 |
| all_thresholds_up | tdcc_price_divergence | 85.0 |
| all_thresholds_up | price_leading_tdcc | 47.0 |
| all_thresholds_up | overheated_after_tdcc | 27.0 |
| all_thresholds_up | tdcc_price_confirmed | 17.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | insufficient_price_context | 208.0 |
| high_thresholds_up | tdcc_leading_price | 182.0 |
| high_thresholds_up | tdcc_price_divergence | 113.0 |
| high_thresholds_up | price_leading_tdcc | 56.0 |
| high_thresholds_up | overheated_after_tdcc | 35.0 |
| high_thresholds_up | tdcc_price_confirmed | 21.0 |
| high_thresholds_up | failed_after_tdcc | 2.0 |
| over_800_or_above | insufficient_price_context | 299.0 |
| over_800_or_above | tdcc_leading_price | 248.0 |
| over_800_or_above | tdcc_price_divergence | 155.0 |
| over_800_or_above | price_leading_tdcc | 72.0 |
| over_800_or_above | overheated_after_tdcc | 44.0 |
| over_800_or_above | tdcc_price_confirmed | 27.0 |
| over_800_or_above | failed_after_tdcc | 3.0 |
| over_1000_only | insufficient_price_context | 33.0 |
| over_1000_only | tdcc_leading_price | 18.0 |
| over_1000_only | tdcc_price_divergence | 12.0 |
| over_1000_only | price_leading_tdcc | 8.0 |
| over_1000_only | overheated_after_tdcc | 5.0 |
| over_1000_only | tdcc_price_confirmed | 2.0 |
| consecutive_2w | tdcc_leading_price | 308.0 |
| consecutive_2w | tdcc_price_divergence | 199.0 |
| consecutive_2w | insufficient_price_context | 102.0 |
| consecutive_2w | price_leading_tdcc | 59.0 |
| consecutive_2w | overheated_after_tdcc | 35.0 |
| consecutive_2w | tdcc_price_confirmed | 33.0 |
| consecutive_2w | failed_after_tdcc | 4.0 |
| consecutive_3w | tdcc_leading_price | 205.0 |
| consecutive_3w | tdcc_price_divergence | 133.0 |
| consecutive_3w | insufficient_price_context | 64.0 |
| consecutive_3w | price_leading_tdcc | 35.0 |
| consecutive_3w | tdcc_price_confirmed | 25.0 |
| consecutive_3w | overheated_after_tdcc | 16.0 |
| consecutive_3w | failed_after_tdcc | 3.0 |
| quiet_accumulation | tdcc_leading_price | 116.0 |
| quiet_accumulation | tdcc_price_divergence | 76.0 |
| quiet_accumulation | insufficient_price_context | 28.0 |
| quiet_accumulation | tdcc_price_confirmed | 4.0 |
| quiet_accumulation | price_leading_tdcc | 3.0 |
| quiet_accumulation | overheated_after_tdcc | 2.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout | tdcc_leading_price | 3.0 |
| early_breakout | tdcc_price_confirmed | 1.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | price_leading_tdcc | 17.0 |
| strong_momentum | insufficient_price_context | 9.0 |
| strong_momentum | tdcc_price_confirmed | 7.0 |
| strong_momentum | tdcc_leading_price | 6.0 |
| strong_momentum | tdcc_price_divergence | 3.0 |
| overheated | overheated_after_tdcc | 52.0 |
| overheated | price_leading_tdcc | 19.0 |
| overheated | insufficient_price_context | 7.0 |
| overheated | tdcc_leading_price | 3.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 36.0 | 2.79 | 0.90 | 17.0 | 1.68 | -6.71 | 8.0 | -2.46 | -18.51 | 7.61 | -4.99 |
| insufficient_price_context | 2870.0 | 0.74 | -0.69 | 2374.0 | 2.64 | -1.53 | 1462.0 | 5.02 | -2.91 | 8.64 | -5.01 |
| overheated_after_tdcc | 322.0 | 4.14 | 2.57 | 218.0 | 12.03 | 7.20 | 73.0 | 15.41 | 8.18 | 23.16 | -7.45 |
| price_leading_tdcc | 325.0 | 3.37 | 0.60 | 267.0 | 6.33 | 0.97 | 83.0 | 6.10 | -2.62 | 17.53 | -6.37 |
| tdcc_leading_price | 1028.0 | 1.53 | -0.49 | 724.0 | 2.21 | -3.17 | 380.0 | -0.09 | -9.04 | 6.91 | -3.61 |
| tdcc_price_confirmed | 78.0 | 2.27 | -0.32 | 62.0 | 4.09 | -0.75 | 23.0 | -3.46 | -12.22 | 12.33 | -5.22 |
| tdcc_price_divergence | 1334.0 | 1.18 | -1.57 | 1110.0 | 1.80 | -3.96 | 408.0 | 0.64 | -8.92 | 6.83 | -3.89 |
