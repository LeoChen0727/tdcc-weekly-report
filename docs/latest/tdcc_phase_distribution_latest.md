# TDCC Phase Distribution

- generated_at: 2026-06-28 02:50:56 Asia/Taipei
- latest_signal_count: 1105
- phase_mature_d5_count: 266
- phase_mature_d10_count: 161
- phase_mature_d20_count: 119

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 756.0 | 68.42 |
| tdcc_price_divergence | 151.0 | 13.67 |
| tdcc_leading_price | 110.0 | 9.95 |
| price_leading_tdcc | 53.0 | 4.80 |
| overheated_after_tdcc | 19.0 | 1.72 |
| tdcc_price_confirmed | 11.0 | 1.00 |
| failed_after_tdcc | 5.0 | 0.45 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 406.0 |
| 1 | overheated_after_tdcc | 2.0 |
| 1 | price_leading_tdcc | 11.0 |
| 2 | failed_after_tdcc | 5.0 |
| 2 | insufficient_price_context | 166.0 |
| 2 | overheated_after_tdcc | 7.0 |
| 2 | price_leading_tdcc | 26.0 |
| 2 | tdcc_leading_price | 24.0 |
| 2 | tdcc_price_confirmed | 3.0 |
| 2 | tdcc_price_divergence | 45.0 |
| 3 | insufficient_price_context | 65.0 |
| 3 | overheated_after_tdcc | 4.0 |
| 3 | price_leading_tdcc | 7.0 |
| 3 | tdcc_leading_price | 21.0 |
| 3 | tdcc_price_confirmed | 4.0 |
| 3 | tdcc_price_divergence | 23.0 |
| 4 | insufficient_price_context | 51.0 |
| 4 | overheated_after_tdcc | 4.0 |
| 4 | price_leading_tdcc | 2.0 |
| 4 | tdcc_leading_price | 21.0 |
| 4 | tdcc_price_confirmed | 1.0 |
| 4 | tdcc_price_divergence | 17.0 |
| 5 | insufficient_price_context | 19.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 2.0 |
| 5 | tdcc_leading_price | 6.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 15.0 |
| 6 | insufficient_price_context | 14.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 8.0 |
| 6 | tdcc_price_confirmed | 1.0 |
| 6 | tdcc_price_divergence | 16.0 |
| 7 | insufficient_price_context | 35.0 |
| 7 | price_leading_tdcc | 4.0 |
| 7 | tdcc_leading_price | 30.0 |
| 7 | tdcc_price_confirmed | 1.0 |
| 7 | tdcc_price_divergence | 35.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 125.0 |
| all_thresholds_up | tdcc_price_divergence | 120.0 |
| all_thresholds_up | tdcc_leading_price | 98.0 |
| all_thresholds_up | price_leading_tdcc | 49.0 |
| all_thresholds_up | overheated_after_tdcc | 16.0 |
| all_thresholds_up | tdcc_price_confirmed | 11.0 |
| all_thresholds_up | failed_after_tdcc | 4.0 |
| high_thresholds_up | insufficient_price_context | 203.0 |
| high_thresholds_up | tdcc_price_divergence | 151.0 |
| high_thresholds_up | tdcc_leading_price | 110.0 |
| high_thresholds_up | price_leading_tdcc | 53.0 |
| high_thresholds_up | overheated_after_tdcc | 19.0 |
| high_thresholds_up | tdcc_price_confirmed | 11.0 |
| high_thresholds_up | failed_after_tdcc | 5.0 |
| over_800_or_above | insufficient_price_context | 445.0 |
| over_800_or_above | tdcc_price_divergence | 151.0 |
| over_800_or_above | tdcc_leading_price | 110.0 |
| over_800_or_above | price_leading_tdcc | 53.0 |
| over_800_or_above | overheated_after_tdcc | 19.0 |
| over_800_or_above | tdcc_price_confirmed | 11.0 |
| over_800_or_above | failed_after_tdcc | 5.0 |
| over_1000_only | insufficient_price_context | 93.0 |
| consecutive_2w | insufficient_price_context | 350.0 |
| consecutive_2w | tdcc_price_divergence | 151.0 |
| consecutive_2w | tdcc_leading_price | 110.0 |
| consecutive_2w | price_leading_tdcc | 42.0 |
| consecutive_2w | overheated_after_tdcc | 17.0 |
| consecutive_2w | tdcc_price_confirmed | 11.0 |
| consecutive_2w | failed_after_tdcc | 5.0 |
| consecutive_3w | insufficient_price_context | 184.0 |
| consecutive_3w | tdcc_price_divergence | 106.0 |
| consecutive_3w | tdcc_leading_price | 86.0 |
| consecutive_3w | price_leading_tdcc | 16.0 |
| consecutive_3w | overheated_after_tdcc | 10.0 |
| consecutive_3w | tdcc_price_confirmed | 8.0 |
| quiet_accumulation | tdcc_price_divergence | 93.0 |
| quiet_accumulation | tdcc_leading_price | 68.0 |
| quiet_accumulation | insufficient_price_context | 33.0 |
| quiet_accumulation | price_leading_tdcc | 6.0 |
| quiet_accumulation | tdcc_price_confirmed | 5.0 |
| quiet_accumulation | failed_after_tdcc | 4.0 |
| quiet_accumulation | overheated_after_tdcc | 1.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 15.0 |
| strong_momentum | insufficient_price_context | 9.0 |
| strong_momentum | tdcc_leading_price | 5.0 |
| strong_momentum | tdcc_price_divergence | 3.0 |
| strong_momentum | overheated_after_tdcc | 1.0 |
| strong_momentum | tdcc_price_confirmed | 1.0 |
| overheated | overheated_after_tdcc | 19.0 |
| overheated | price_leading_tdcc | 8.0 |
| overheated | insufficient_price_context | 2.0 |
| overheated | tdcc_price_divergence | 2.0 |
| overheated | tdcc_leading_price | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 87.0 | 1.87 | 0.11 | 45.0 | 6.71 | 1.85 | 32.0 | 3.59 | -0.65 | 16.61 | -9.45 |
| overheated_after_tdcc | 94.0 | 3.85 | 2.22 | 63.0 | 7.90 | 4.38 | 57.0 | 14.39 | 8.43 | 20.13 | -10.04 |
| price_leading_tdcc | 59.0 | 4.86 | 2.74 | 35.0 | 5.94 | 2.75 | 26.0 | 2.32 | -7.52 | 18.25 | -8.92 |
| tdcc_leading_price | 13.0 | -3.12 | -1.12 | 10.0 | 4.51 | -0.62 | 2.0 | 4.13 | -13.87 | 13.32 | -10.01 |
| tdcc_price_confirmed | 6.0 | -3.78 | -3.95 | 6.0 | 6.66 | 2.22 | 2.0 | 21.99 | 14.85 | 11.97 | -10.68 |
| tdcc_price_divergence | 7.0 | -5.31 | -4.78 | 2.0 | -13.66 | -19.22 | 0.0 |  |  | 7.24 | -25.69 |
