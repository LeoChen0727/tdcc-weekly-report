# TDCC Phase Distribution

- generated_at: 2026-06-13 18:27:56 Asia/Taipei
- latest_signal_count: 1094
- phase_mature_d5_count: 119
- phase_mature_d10_count: 82
- phase_mature_d20_count: 41

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 840.0 | 76.78 |
| price_leading_tdcc | 113.0 | 10.33 |
| tdcc_price_divergence | 65.0 | 5.94 |
| tdcc_leading_price | 35.0 | 3.20 |
| overheated_after_tdcc | 35.0 | 3.20 |
| tdcc_price_confirmed | 5.0 | 0.46 |
| failed_after_tdcc | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 403.0 |
| 1 | overheated_after_tdcc | 9.0 |
| 1 | price_leading_tdcc | 21.0 |
| 2 | insufficient_price_context | 153.0 |
| 2 | overheated_after_tdcc | 8.0 |
| 2 | price_leading_tdcc | 32.0 |
| 2 | tdcc_leading_price | 7.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 17.0 |
| 3 | insufficient_price_context | 90.0 |
| 3 | overheated_after_tdcc | 7.0 |
| 3 | price_leading_tdcc | 13.0 |
| 3 | tdcc_leading_price | 6.0 |
| 3 | tdcc_price_divergence | 15.0 |
| 4 | insufficient_price_context | 59.0 |
| 4 | overheated_after_tdcc | 5.0 |
| 4 | price_leading_tdcc | 17.0 |
| 4 | tdcc_leading_price | 3.0 |
| 4 | tdcc_price_divergence | 12.0 |
| 5 | insufficient_price_context | 36.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 12.0 |
| 5 | tdcc_leading_price | 1.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 8.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 86.0 |
| 6 | overheated_after_tdcc | 4.0 |
| 6 | price_leading_tdcc | 16.0 |
| 6 | tdcc_leading_price | 14.0 |
| 6 | tdcc_price_confirmed | 2.0 |
| 6 | tdcc_price_divergence | 8.0 |
| 7 | insufficient_price_context | 13.0 |
| 7 | price_leading_tdcc | 2.0 |
| 7 | tdcc_leading_price | 4.0 |
| 7 | tdcc_price_divergence | 5.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 189.0 |
| all_thresholds_up | price_leading_tdcc | 94.0 |
| all_thresholds_up | tdcc_price_divergence | 45.0 |
| all_thresholds_up | tdcc_leading_price | 31.0 |
| all_thresholds_up | overheated_after_tdcc | 30.0 |
| all_thresholds_up | tdcc_price_confirmed | 4.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | insufficient_price_context | 296.0 |
| high_thresholds_up | price_leading_tdcc | 113.0 |
| high_thresholds_up | tdcc_price_divergence | 65.0 |
| high_thresholds_up | tdcc_leading_price | 35.0 |
| high_thresholds_up | overheated_after_tdcc | 35.0 |
| high_thresholds_up | tdcc_price_confirmed | 5.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 540.0 |
| over_800_or_above | price_leading_tdcc | 113.0 |
| over_800_or_above | tdcc_price_divergence | 65.0 |
| over_800_or_above | tdcc_leading_price | 35.0 |
| over_800_or_above | overheated_after_tdcc | 35.0 |
| over_800_or_above | tdcc_price_confirmed | 5.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | insufficient_price_context | 87.0 |
| consecutive_2w | insufficient_price_context | 437.0 |
| consecutive_2w | price_leading_tdcc | 92.0 |
| consecutive_2w | tdcc_price_divergence | 65.0 |
| consecutive_2w | tdcc_leading_price | 35.0 |
| consecutive_2w | overheated_after_tdcc | 26.0 |
| consecutive_2w | tdcc_price_confirmed | 5.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 284.0 |
| consecutive_3w | price_leading_tdcc | 60.0 |
| consecutive_3w | tdcc_price_divergence | 48.0 |
| consecutive_3w | tdcc_leading_price | 28.0 |
| consecutive_3w | overheated_after_tdcc | 18.0 |
| consecutive_3w | tdcc_price_confirmed | 3.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | insufficient_price_context | 107.0 |
| quiet_accumulation | tdcc_price_divergence | 33.0 |
| quiet_accumulation | price_leading_tdcc | 25.0 |
| quiet_accumulation | tdcc_leading_price | 23.0 |
| quiet_accumulation | tdcc_price_confirmed | 5.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout | price_leading_tdcc | 3.0 |
| strong_momentum | price_leading_tdcc | 23.0 |
| strong_momentum | insufficient_price_context | 9.0 |
| strong_momentum | tdcc_leading_price | 2.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| overheated | overheated_after_tdcc | 35.0 |
| overheated | price_leading_tdcc | 16.0 |
| overheated | insufficient_price_context | 4.0 |
| overheated | tdcc_price_divergence | 3.0 |
| overheated | tdcc_leading_price | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 26.0 | 5.21 | 3.03 | 18.0 | 14.38 | 7.79 | 11.0 | 10.70 | 5.78 | 24.57 | -6.95 |
| overheated_after_tdcc | 57.0 | 5.54 | 2.72 | 39.0 | 16.22 | 10.14 | 16.0 | 22.64 | 17.96 | 24.48 | -6.54 |
| price_leading_tdcc | 26.0 | 6.24 | 4.19 | 16.0 | 9.09 | 3.09 | 8.0 | -1.66 | -6.99 | 19.56 | -5.94 |
| tdcc_leading_price | 7.0 | 4.36 | 1.40 | 6.0 | 2.15 | -5.78 | 5.0 | -2.69 | -6.85 | 11.42 | -5.64 |
| tdcc_price_confirmed | 2.0 | 5.29 | 0.47 | 2.0 | 21.87 | 20.03 | 0.0 |  |  | 23.17 | -3.99 |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 | 11.44 | 1.0 | 5.75 | 3.67 | 19.34 | -11.15 |
