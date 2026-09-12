# TDCC Phase Distribution

- generated_at: 2026-09-12 15:37:14 Asia/Taipei
- latest_signal_count: 1157
- phase_mature_d5_count: 784
- phase_mature_d10_count: 738
- phase_mature_d20_count: 638

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 864.0 | 74.68 |
| tdcc_price_divergence | 174.0 | 15.04 |
| tdcc_leading_price | 75.0 | 6.48 |
| price_leading_tdcc | 31.0 | 2.68 |
| overheated_after_tdcc | 10.0 | 0.86 |
| failed_after_tdcc | 2.0 | 0.17 |
| tdcc_price_confirmed | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 498.0 |
| 1 | overheated_after_tdcc | 6.0 |
| 1 | price_leading_tdcc | 2.0 |
| 10 | insufficient_price_context | 2.0 |
| 10 | tdcc_price_divergence | 4.0 |
| 11 | insufficient_price_context | 5.0 |
| 11 | tdcc_leading_price | 2.0 |
| 11 | tdcc_price_divergence | 3.0 |
| 12 | insufficient_price_context | 2.0 |
| 12 | tdcc_leading_price | 3.0 |
| 12 | tdcc_price_divergence | 2.0 |
| 13 | insufficient_price_context | 2.0 |
| 13 | tdcc_price_divergence | 1.0 |
| 14 | insufficient_price_context | 1.0 |
| 14 | tdcc_price_divergence | 1.0 |
| 16 | insufficient_price_context | 1.0 |
| 19 | insufficient_price_context | 1.0 |
| 19 | tdcc_leading_price | 3.0 |
| 19 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 1.0 |
| 2 | insufficient_price_context | 154.0 |
| 2 | overheated_after_tdcc | 2.0 |
| 2 | price_leading_tdcc | 9.0 |
| 2 | tdcc_leading_price | 22.0 |
| 2 | tdcc_price_confirmed | 1.0 |
| 2 | tdcc_price_divergence | 58.0 |
| 20 | tdcc_price_divergence | 1.0 |
| 3 | insufficient_price_context | 89.0 |
| 3 | overheated_after_tdcc | 2.0 |
| 3 | price_leading_tdcc | 7.0 |
| 3 | tdcc_leading_price | 6.0 |
| 3 | tdcc_price_divergence | 32.0 |
| 4 | insufficient_price_context | 44.0 |
| 4 | price_leading_tdcc | 6.0 |
| 4 | tdcc_leading_price | 14.0 |
| 4 | tdcc_price_divergence | 16.0 |
| 41 | tdcc_leading_price | 1.0 |
| 5 | insufficient_price_context | 24.0 |
| 5 | price_leading_tdcc | 5.0 |
| 5 | tdcc_leading_price | 7.0 |
| 5 | tdcc_price_divergence | 22.0 |
| 6 | insufficient_price_context | 25.0 |
| 6 | tdcc_leading_price | 4.0 |
| 6 | tdcc_price_divergence | 15.0 |
| 7 | failed_after_tdcc | 1.0 |
| 7 | insufficient_price_context | 7.0 |
| 7 | price_leading_tdcc | 2.0 |
| 7 | tdcc_leading_price | 4.0 |
| 7 | tdcc_price_divergence | 11.0 |
| 8 | insufficient_price_context | 3.0 |
| 8 | tdcc_leading_price | 5.0 |
| 8 | tdcc_price_divergence | 6.0 |
| 9 | insufficient_price_context | 6.0 |
| 9 | tdcc_leading_price | 4.0 |
| 9 | tdcc_price_divergence | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 178.0 |
| all_thresholds_up | tdcc_price_divergence | 143.0 |
| all_thresholds_up | tdcc_leading_price | 70.0 |
| all_thresholds_up | price_leading_tdcc | 28.0 |
| all_thresholds_up | overheated_after_tdcc | 10.0 |
| all_thresholds_up | failed_after_tdcc | 2.0 |
| all_thresholds_up | tdcc_price_confirmed | 1.0 |
| high_thresholds_up | insufficient_price_context | 275.0 |
| high_thresholds_up | tdcc_price_divergence | 174.0 |
| high_thresholds_up | tdcc_leading_price | 75.0 |
| high_thresholds_up | price_leading_tdcc | 31.0 |
| high_thresholds_up | overheated_after_tdcc | 10.0 |
| high_thresholds_up | failed_after_tdcc | 2.0 |
| high_thresholds_up | tdcc_price_confirmed | 1.0 |
| over_800_or_above | insufficient_price_context | 518.0 |
| over_800_or_above | tdcc_price_divergence | 174.0 |
| over_800_or_above | tdcc_leading_price | 75.0 |
| over_800_or_above | price_leading_tdcc | 31.0 |
| over_800_or_above | overheated_after_tdcc | 10.0 |
| over_800_or_above | failed_after_tdcc | 2.0 |
| over_800_or_above | tdcc_price_confirmed | 1.0 |
| over_1000_only | insufficient_price_context | 101.0 |
| consecutive_2w | insufficient_price_context | 366.0 |
| consecutive_2w | tdcc_price_divergence | 174.0 |
| consecutive_2w | tdcc_leading_price | 75.0 |
| consecutive_2w | price_leading_tdcc | 29.0 |
| consecutive_2w | overheated_after_tdcc | 4.0 |
| consecutive_2w | failed_after_tdcc | 2.0 |
| consecutive_2w | tdcc_price_confirmed | 1.0 |
| consecutive_3w | insufficient_price_context | 212.0 |
| consecutive_3w | tdcc_price_divergence | 116.0 |
| consecutive_3w | tdcc_leading_price | 53.0 |
| consecutive_3w | price_leading_tdcc | 20.0 |
| consecutive_3w | overheated_after_tdcc | 2.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | tdcc_price_divergence | 108.0 |
| quiet_accumulation | tdcc_leading_price | 53.0 |
| quiet_accumulation | insufficient_price_context | 45.0 |
| quiet_accumulation | price_leading_tdcc | 2.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout | insufficient_price_context | 4.0 |
| early_breakout | price_leading_tdcc | 2.0 |
| strong_momentum | price_leading_tdcc | 16.0 |
| strong_momentum | insufficient_price_context | 7.0 |
| strong_momentum | tdcc_leading_price | 2.0 |
| strong_momentum | tdcc_price_divergence | 2.0 |
| overheated | overheated_after_tdcc | 10.0 |
| overheated | price_leading_tdcc | 4.0 |
| overheated | insufficient_price_context | 2.0 |
| overheated | tdcc_price_divergence | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 6.0 | 3.07 | 2.01 | 5.0 | 12.30 | 9.92 | 5.0 | 22.03 | 17.10 | 24.10 | -9.97 |
| insufficient_price_context | 301.0 | 1.28 | -0.24 | 286.0 | 2.08 | 0.12 | 253.0 | 1.75 | -0.99 | 13.37 | -8.81 |
| overheated_after_tdcc | 179.0 | 2.72 | 1.71 | 171.0 | 2.19 | 1.19 | 149.0 | -0.56 | -0.88 | 17.91 | -11.21 |
| price_leading_tdcc | 163.0 | 0.86 | -0.53 | 154.0 | -0.53 | -0.86 | 133.0 | -1.41 | -2.30 | 12.11 | -9.89 |
| tdcc_leading_price | 55.0 | 0.06 | -0.20 | 50.0 | -0.86 | -2.64 | 44.0 | -2.49 | -4.21 | 9.20 | -8.59 |
| tdcc_price_confirmed | 21.0 | 0.88 | 0.48 | 17.0 | 1.37 | 1.23 | 13.0 | -2.28 | -2.16 | 11.30 | -9.15 |
| tdcc_price_divergence | 59.0 | 2.67 | 0.19 | 55.0 | 6.11 | 2.22 | 41.0 | 10.70 | 5.78 | 16.62 | -7.60 |
