# TDCC Phase Distribution

- generated_at: 2026-08-22 15:53:40 Asia/Taipei
- latest_signal_count: 1140
- phase_mature_d5_count: 642
- phase_mature_d10_count: 608
- phase_mature_d20_count: 485

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 829.0 | 72.72 |
| tdcc_leading_price | 126.0 | 11.05 |
| tdcc_price_divergence | 119.0 | 10.44 |
| price_leading_tdcc | 31.0 | 2.72 |
| overheated_after_tdcc | 19.0 | 1.67 |
| tdcc_price_confirmed | 13.0 | 1.14 |
| failed_after_tdcc | 3.0 | 0.26 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 399.0 |
| 1 | overheated_after_tdcc | 2.0 |
| 1 | price_leading_tdcc | 5.0 |
| 10 | tdcc_leading_price | 1.0 |
| 10 | tdcc_price_divergence | 1.0 |
| 11 | insufficient_price_context | 2.0 |
| 11 | tdcc_leading_price | 4.0 |
| 11 | tdcc_price_divergence | 2.0 |
| 13 | insufficient_price_context | 2.0 |
| 13 | tdcc_leading_price | 1.0 |
| 14 | overheated_after_tdcc | 1.0 |
| 14 | tdcc_leading_price | 2.0 |
| 15 | price_leading_tdcc | 1.0 |
| 16 | insufficient_price_context | 1.0 |
| 16 | tdcc_leading_price | 4.0 |
| 16 | tdcc_price_divergence | 4.0 |
| 17 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 187.0 |
| 2 | overheated_after_tdcc | 2.0 |
| 2 | price_leading_tdcc | 4.0 |
| 2 | tdcc_leading_price | 33.0 |
| 2 | tdcc_price_confirmed | 1.0 |
| 2 | tdcc_price_divergence | 33.0 |
| 3 | insufficient_price_context | 130.0 |
| 3 | overheated_after_tdcc | 7.0 |
| 3 | price_leading_tdcc | 11.0 |
| 3 | tdcc_leading_price | 36.0 |
| 3 | tdcc_price_confirmed | 4.0 |
| 3 | tdcc_price_divergence | 29.0 |
| 38 | tdcc_price_confirmed | 1.0 |
| 4 | failed_after_tdcc | 1.0 |
| 4 | insufficient_price_context | 40.0 |
| 4 | overheated_after_tdcc | 2.0 |
| 4 | price_leading_tdcc | 1.0 |
| 4 | tdcc_leading_price | 20.0 |
| 4 | tdcc_price_confirmed | 2.0 |
| 4 | tdcc_price_divergence | 18.0 |
| 5 | insufficient_price_context | 29.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 3.0 |
| 5 | tdcc_leading_price | 6.0 |
| 5 | tdcc_price_confirmed | 2.0 |
| 5 | tdcc_price_divergence | 15.0 |
| 6 | insufficient_price_context | 16.0 |
| 6 | price_leading_tdcc | 2.0 |
| 6 | tdcc_leading_price | 7.0 |
| 6 | tdcc_price_confirmed | 1.0 |
| 6 | tdcc_price_divergence | 7.0 |
| 7 | insufficient_price_context | 9.0 |
| 7 | overheated_after_tdcc | 1.0 |
| 7 | price_leading_tdcc | 4.0 |
| 7 | tdcc_leading_price | 3.0 |
| 7 | tdcc_price_confirmed | 2.0 |
| 7 | tdcc_price_divergence | 5.0 |
| 8 | insufficient_price_context | 11.0 |
| 8 | overheated_after_tdcc | 2.0 |
| 8 | tdcc_leading_price | 4.0 |
| 8 | tdcc_price_divergence | 3.0 |
| 9 | insufficient_price_context | 3.0 |
| 9 | tdcc_leading_price | 5.0 |
| 9 | tdcc_price_divergence | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 156.0 |
| all_thresholds_up | tdcc_leading_price | 99.0 |
| all_thresholds_up | tdcc_price_divergence | 89.0 |
| all_thresholds_up | price_leading_tdcc | 27.0 |
| all_thresholds_up | overheated_after_tdcc | 18.0 |
| all_thresholds_up | tdcc_price_confirmed | 10.0 |
| all_thresholds_up | failed_after_tdcc | 2.0 |
| high_thresholds_up | insufficient_price_context | 261.0 |
| high_thresholds_up | tdcc_leading_price | 126.0 |
| high_thresholds_up | tdcc_price_divergence | 119.0 |
| high_thresholds_up | price_leading_tdcc | 31.0 |
| high_thresholds_up | overheated_after_tdcc | 19.0 |
| high_thresholds_up | tdcc_price_confirmed | 13.0 |
| high_thresholds_up | failed_after_tdcc | 3.0 |
| over_800_or_above | insufficient_price_context | 516.0 |
| over_800_or_above | tdcc_leading_price | 126.0 |
| over_800_or_above | tdcc_price_divergence | 119.0 |
| over_800_or_above | price_leading_tdcc | 31.0 |
| over_800_or_above | overheated_after_tdcc | 19.0 |
| over_800_or_above | tdcc_price_confirmed | 13.0 |
| over_800_or_above | failed_after_tdcc | 3.0 |
| over_1000_only | insufficient_price_context | 102.0 |
| consecutive_2w | insufficient_price_context | 430.0 |
| consecutive_2w | tdcc_leading_price | 126.0 |
| consecutive_2w | tdcc_price_divergence | 119.0 |
| consecutive_2w | price_leading_tdcc | 26.0 |
| consecutive_2w | overheated_after_tdcc | 17.0 |
| consecutive_2w | tdcc_price_confirmed | 13.0 |
| consecutive_2w | failed_after_tdcc | 3.0 |
| consecutive_3w | insufficient_price_context | 243.0 |
| consecutive_3w | tdcc_leading_price | 93.0 |
| consecutive_3w | tdcc_price_divergence | 86.0 |
| consecutive_3w | price_leading_tdcc | 22.0 |
| consecutive_3w | overheated_after_tdcc | 15.0 |
| consecutive_3w | tdcc_price_confirmed | 12.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | tdcc_leading_price | 82.0 |
| quiet_accumulation | tdcc_price_divergence | 69.0 |
| quiet_accumulation | insufficient_price_context | 62.0 |
| quiet_accumulation | tdcc_price_confirmed | 5.0 |
| quiet_accumulation | failed_after_tdcc | 3.0 |
| quiet_accumulation | price_leading_tdcc | 3.0 |
| early_breakout | insufficient_price_context | 3.0 |
| early_breakout | tdcc_price_confirmed | 2.0 |
| early_breakout | price_leading_tdcc | 1.0 |
| strong_momentum | price_leading_tdcc | 18.0 |
| strong_momentum | insufficient_price_context | 8.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| strong_momentum | tdcc_leading_price | 1.0 |
| overheated | overheated_after_tdcc | 19.0 |
| overheated | price_leading_tdcc | 4.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 5.0 | 2.05 | 0.43 | 5.0 | 12.30 | 9.92 | 2.0 | 23.55 | 19.95 | 24.10 | -9.97 |
| insufficient_price_context | 254.0 | 1.29 | -0.39 | 245.0 | 1.85 | -0.28 | 182.0 | -3.08 | -3.44 | 13.79 | -9.10 |
| overheated_after_tdcc | 149.0 | 3.15 | 2.14 | 135.0 | 2.49 | 1.53 | 124.0 | -2.45 | -2.39 | 18.71 | -11.58 |
| price_leading_tdcc | 133.0 | 0.70 | -0.85 | 126.0 | -0.56 | -0.75 | 115.0 | -1.68 | -1.95 | 12.59 | -10.42 |
| tdcc_leading_price | 45.0 | -0.49 | -0.80 | 42.0 | -0.76 | -2.74 | 33.0 | -2.69 | -3.20 | 9.19 | -9.15 |
| tdcc_price_confirmed | 13.0 | -2.06 | -2.67 | 13.0 | 0.39 | 0.68 | 11.0 | -3.80 | -2.80 | 11.13 | -10.96 |
| tdcc_price_divergence | 43.0 | 1.40 | -1.52 | 42.0 | 5.47 | 1.05 | 18.0 | 0.37 | 2.29 | 16.59 | -9.09 |
