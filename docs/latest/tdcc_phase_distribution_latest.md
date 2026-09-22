# TDCC Phase Distribution

- generated_at: 2026-09-19 15:48:07 Asia/Taipei
- latest_signal_count: 1162
- phase_mature_d5_count: 832
- phase_mature_d10_count: 783
- phase_mature_d20_count: 684

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 826.0 | 71.08 |
| tdcc_price_divergence | 151.0 | 12.99 |
| tdcc_leading_price | 140.0 | 12.05 |
| price_leading_tdcc | 22.0 | 1.89 |
| overheated_after_tdcc | 12.0 | 1.03 |
| tdcc_price_confirmed | 10.0 | 0.86 |
| failed_after_tdcc | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 426.0 |
| 1 | overheated_after_tdcc | 6.0 |
| 1 | price_leading_tdcc | 4.0 |
| 10 | insufficient_price_context | 2.0 |
| 10 | tdcc_leading_price | 2.0 |
| 10 | tdcc_price_divergence | 3.0 |
| 11 | insufficient_price_context | 3.0 |
| 11 | tdcc_leading_price | 1.0 |
| 11 | tdcc_price_divergence | 1.0 |
| 12 | insufficient_price_context | 2.0 |
| 12 | tdcc_leading_price | 3.0 |
| 12 | tdcc_price_divergence | 3.0 |
| 13 | insufficient_price_context | 2.0 |
| 13 | tdcc_leading_price | 1.0 |
| 13 | tdcc_price_divergence | 2.0 |
| 14 | tdcc_leading_price | 1.0 |
| 14 | tdcc_price_divergence | 2.0 |
| 15 | tdcc_price_divergence | 1.0 |
| 17 | insufficient_price_context | 1.0 |
| 2 | insufficient_price_context | 188.0 |
| 2 | overheated_after_tdcc | 2.0 |
| 2 | price_leading_tdcc | 6.0 |
| 2 | tdcc_leading_price | 49.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 54.0 |
| 20 | insufficient_price_context | 1.0 |
| 20 | tdcc_leading_price | 4.0 |
| 21 | tdcc_leading_price | 1.0 |
| 3 | insufficient_price_context | 93.0 |
| 3 | overheated_after_tdcc | 4.0 |
| 3 | price_leading_tdcc | 7.0 |
| 3 | tdcc_leading_price | 18.0 |
| 3 | tdcc_price_confirmed | 4.0 |
| 3 | tdcc_price_divergence | 33.0 |
| 4 | insufficient_price_context | 44.0 |
| 4 | price_leading_tdcc | 2.0 |
| 4 | tdcc_leading_price | 10.0 |
| 4 | tdcc_price_confirmed | 1.0 |
| 4 | tdcc_price_divergence | 27.0 |
| 42 | insufficient_price_context | 1.0 |
| 5 | insufficient_price_context | 23.0 |
| 5 | price_leading_tdcc | 1.0 |
| 5 | tdcc_leading_price | 14.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 9.0 |
| 6 | insufficient_price_context | 20.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 13.0 |
| 6 | tdcc_price_divergence | 7.0 |
| 7 | insufficient_price_context | 10.0 |
| 7 | price_leading_tdcc | 1.0 |
| 7 | tdcc_leading_price | 11.0 |
| 7 | tdcc_price_confirmed | 1.0 |
| 7 | tdcc_price_divergence | 4.0 |
| 8 | failed_after_tdcc | 1.0 |
| 8 | insufficient_price_context | 6.0 |
| 8 | tdcc_leading_price | 5.0 |
| 8 | tdcc_price_divergence | 4.0 |
| 9 | insufficient_price_context | 4.0 |
| 9 | tdcc_leading_price | 7.0 |
| 9 | tdcc_price_confirmed | 1.0 |
| 9 | tdcc_price_divergence | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 133.0 |
| all_thresholds_up | tdcc_price_divergence | 127.0 |
| all_thresholds_up | tdcc_leading_price | 123.0 |
| all_thresholds_up | price_leading_tdcc | 20.0 |
| all_thresholds_up | overheated_after_tdcc | 12.0 |
| all_thresholds_up | tdcc_price_confirmed | 9.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | insufficient_price_context | 244.0 |
| high_thresholds_up | tdcc_price_divergence | 151.0 |
| high_thresholds_up | tdcc_leading_price | 140.0 |
| high_thresholds_up | price_leading_tdcc | 22.0 |
| high_thresholds_up | overheated_after_tdcc | 12.0 |
| high_thresholds_up | tdcc_price_confirmed | 10.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 499.0 |
| over_800_or_above | tdcc_price_divergence | 151.0 |
| over_800_or_above | tdcc_leading_price | 140.0 |
| over_800_or_above | price_leading_tdcc | 22.0 |
| over_800_or_above | overheated_after_tdcc | 12.0 |
| over_800_or_above | tdcc_price_confirmed | 10.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | insufficient_price_context | 104.0 |
| consecutive_2w | insufficient_price_context | 400.0 |
| consecutive_2w | tdcc_price_divergence | 151.0 |
| consecutive_2w | tdcc_leading_price | 140.0 |
| consecutive_2w | price_leading_tdcc | 18.0 |
| consecutive_2w | tdcc_price_confirmed | 10.0 |
| consecutive_2w | overheated_after_tdcc | 6.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 212.0 |
| consecutive_3w | tdcc_price_divergence | 97.0 |
| consecutive_3w | tdcc_leading_price | 91.0 |
| consecutive_3w | price_leading_tdcc | 12.0 |
| consecutive_3w | tdcc_price_confirmed | 8.0 |
| consecutive_3w | overheated_after_tdcc | 4.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | tdcc_price_divergence | 93.0 |
| quiet_accumulation | tdcc_leading_price | 78.0 |
| quiet_accumulation | insufficient_price_context | 56.0 |
| quiet_accumulation | tdcc_price_confirmed | 2.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout | tdcc_leading_price | 1.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | insufficient_price_context | 17.0 |
| strong_momentum | price_leading_tdcc | 10.0 |
| strong_momentum | tdcc_leading_price | 5.0 |
| strong_momentum | tdcc_price_confirmed | 1.0 |
| overheated | overheated_after_tdcc | 12.0 |
| overheated | price_leading_tdcc | 8.0 |
| overheated | insufficient_price_context | 4.0 |
| overheated | tdcc_price_divergence | 2.0 |
| overheated | tdcc_leading_price | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 6.0 | 3.07 | 2.01 | 6.0 | 13.47 | 11.06 | 5.0 | 22.03 | 17.10 | 23.61 | -8.31 |
| insufficient_price_context | 325.0 | 1.59 | -0.06 | 301.0 | 2.03 | 0.06 | 265.0 | 1.76 | -1.10 | 13.11 | -8.82 |
| overheated_after_tdcc | 185.0 | 2.81 | 1.70 | 179.0 | 2.13 | 1.09 | 160.0 | -0.02 | -0.71 | 17.49 | -11.16 |
| price_leading_tdcc | 174.0 | 1.51 | 0.00 | 163.0 | -0.44 | -0.84 | 143.0 | -0.92 | -2.06 | 11.89 | -9.92 |
| tdcc_leading_price | 57.0 | 0.10 | -0.31 | 55.0 | -0.32 | -2.10 | 46.0 | -1.56 | -3.44 | 9.26 | -8.28 |
| tdcc_price_confirmed | 21.0 | 0.88 | 0.48 | 21.0 | 4.28 | 3.69 | 15.0 | -1.73 | -2.36 | 13.19 | -7.87 |
| tdcc_price_divergence | 64.0 | 3.04 | 0.54 | 58.0 | 5.85 | 2.06 | 50.0 | 10.22 | 5.26 | 16.02 | -7.36 |
