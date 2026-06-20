# TDCC Phase Distribution

- generated_at: 2026-06-20 15:37:03 Asia/Taipei
- latest_signal_count: 1119
- phase_mature_d5_count: 161
- phase_mature_d10_count: 119
- phase_mature_d20_count: 82

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 808.0 | 72.21 |
| tdcc_price_divergence | 139.0 | 12.42 |
| tdcc_leading_price | 77.0 | 6.88 |
| overheated_after_tdcc | 50.0 | 4.47 |
| price_leading_tdcc | 35.0 | 3.13 |
| tdcc_price_confirmed | 9.0 | 0.80 |
| failed_after_tdcc | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 434.0 |
| 1 | overheated_after_tdcc | 18.0 |
| 1 | price_leading_tdcc | 9.0 |
| 2 | failed_after_tdcc | 1.0 |
| 2 | insufficient_price_context | 157.0 |
| 2 | overheated_after_tdcc | 13.0 |
| 2 | price_leading_tdcc | 9.0 |
| 2 | tdcc_leading_price | 13.0 |
| 2 | tdcc_price_confirmed | 4.0 |
| 2 | tdcc_price_divergence | 41.0 |
| 3 | insufficient_price_context | 70.0 |
| 3 | overheated_after_tdcc | 6.0 |
| 3 | price_leading_tdcc | 5.0 |
| 3 | tdcc_leading_price | 20.0 |
| 3 | tdcc_price_confirmed | 2.0 |
| 3 | tdcc_price_divergence | 26.0 |
| 4 | insufficient_price_context | 46.0 |
| 4 | overheated_after_tdcc | 4.0 |
| 4 | price_leading_tdcc | 3.0 |
| 4 | tdcc_leading_price | 11.0 |
| 4 | tdcc_price_confirmed | 1.0 |
| 4 | tdcc_price_divergence | 14.0 |
| 5 | insufficient_price_context | 29.0 |
| 5 | overheated_after_tdcc | 4.0 |
| 5 | price_leading_tdcc | 3.0 |
| 5 | tdcc_leading_price | 8.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 18.0 |
| 6 | insufficient_price_context | 20.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 3.0 |
| 6 | tdcc_leading_price | 7.0 |
| 6 | tdcc_price_confirmed | 1.0 |
| 6 | tdcc_price_divergence | 9.0 |
| 7 | insufficient_price_context | 52.0 |
| 7 | overheated_after_tdcc | 4.0 |
| 7 | price_leading_tdcc | 3.0 |
| 7 | tdcc_leading_price | 18.0 |
| 7 | tdcc_price_divergence | 31.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 163.0 |
| all_thresholds_up | tdcc_price_divergence | 127.0 |
| all_thresholds_up | tdcc_leading_price | 75.0 |
| all_thresholds_up | overheated_after_tdcc | 45.0 |
| all_thresholds_up | price_leading_tdcc | 27.0 |
| all_thresholds_up | tdcc_price_confirmed | 9.0 |
| high_thresholds_up | insufficient_price_context | 269.0 |
| high_thresholds_up | tdcc_price_divergence | 139.0 |
| high_thresholds_up | tdcc_leading_price | 77.0 |
| high_thresholds_up | overheated_after_tdcc | 50.0 |
| high_thresholds_up | price_leading_tdcc | 35.0 |
| high_thresholds_up | tdcc_price_confirmed | 9.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 510.0 |
| over_800_or_above | tdcc_price_divergence | 139.0 |
| over_800_or_above | tdcc_leading_price | 77.0 |
| over_800_or_above | overheated_after_tdcc | 50.0 |
| over_800_or_above | price_leading_tdcc | 35.0 |
| over_800_or_above | tdcc_price_confirmed | 9.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | insufficient_price_context | 95.0 |
| consecutive_2w | insufficient_price_context | 374.0 |
| consecutive_2w | tdcc_price_divergence | 139.0 |
| consecutive_2w | tdcc_leading_price | 77.0 |
| consecutive_2w | overheated_after_tdcc | 32.0 |
| consecutive_2w | price_leading_tdcc | 26.0 |
| consecutive_2w | tdcc_price_confirmed | 9.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 217.0 |
| consecutive_3w | tdcc_price_divergence | 98.0 |
| consecutive_3w | tdcc_leading_price | 64.0 |
| consecutive_3w | overheated_after_tdcc | 19.0 |
| consecutive_3w | price_leading_tdcc | 17.0 |
| consecutive_3w | tdcc_price_confirmed | 5.0 |
| quiet_accumulation | tdcc_price_divergence | 75.0 |
| quiet_accumulation | insufficient_price_context | 52.0 |
| quiet_accumulation | tdcc_leading_price | 51.0 |
| quiet_accumulation | price_leading_tdcc | 1.0 |
| early_breakout | tdcc_leading_price | 2.0 |
| early_breakout | insufficient_price_context | 2.0 |
| early_breakout | price_leading_tdcc | 2.0 |
| strong_momentum | insufficient_price_context | 19.0 |
| strong_momentum | price_leading_tdcc | 14.0 |
| strong_momentum | tdcc_price_divergence | 7.0 |
| strong_momentum | tdcc_leading_price | 5.0 |
| strong_momentum | tdcc_price_confirmed | 2.0 |
| overheated | overheated_after_tdcc | 50.0 |
| overheated | insufficient_price_context | 11.0 |
| overheated | price_leading_tdcc | 11.0 |
| overheated | tdcc_price_confirmed | 1.0 |
| overheated | tdcc_price_divergence | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 39.0 | 2.77 | 2.06 | 26.0 | 9.43 | 5.74 | 18.0 | 7.37 | 7.55 | 20.99 | -8.66 |
| overheated_after_tdcc | 63.0 | 5.45 | 3.14 | 57.0 | 7.72 | 4.39 | 39.0 | 16.50 | 13.23 | 20.34 | -9.98 |
| price_leading_tdcc | 35.0 | 4.53 | 3.63 | 26.0 | 3.75 | 1.33 | 16.0 | -0.19 | -5.01 | 17.65 | -7.65 |
| tdcc_leading_price | 15.0 | 1.02 | 0.79 | 7.0 | 0.73 | -5.89 | 6.0 | -2.07 | -6.46 | 11.79 | -6.04 |
| tdcc_price_confirmed | 6.0 | -3.78 | -3.95 | 2.0 | 21.87 | 20.03 | 2.0 | 21.99 |  | 23.17 | -3.99 |
| tdcc_price_divergence | 3.0 | -7.14 | -6.58 | 1.0 | 19.34 | 11.44 | 1.0 | 5.57 | 3.50 | 19.34 | -11.15 |
