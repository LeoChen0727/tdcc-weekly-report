# TDCC Phase Distribution

- generated_at: 2026-05-30 19:19:25 Asia/Taipei
- latest_signal_count: 1217
- phase_mature_d5_count: 4781
- phase_mature_d10_count: 3568
- phase_mature_d20_count: 1292

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 490.0 | 40.26 |
| tdcc_leading_price | 308.0 | 25.31 |
| tdcc_price_divergence | 223.0 | 18.32 |
| overheated_after_tdcc | 104.0 | 8.55 |
| price_leading_tdcc | 57.0 | 4.68 |
| failed_after_tdcc | 19.0 | 1.56 |
| tdcc_price_confirmed | 16.0 | 1.31 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 380.0 |
| 1 | overheated_after_tdcc | 39.0 |
| 1 | price_leading_tdcc | 30.0 |
| 10 | tdcc_leading_price | 1.0 |
| 11 | tdcc_leading_price | 1.0 |
| 13 | tdcc_price_divergence | 2.0 |
| 14 | tdcc_price_divergence | 1.0 |
| 15 | tdcc_leading_price | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 17 | tdcc_leading_price | 1.0 |
| 2 | failed_after_tdcc | 8.0 |
| 2 | insufficient_price_context | 44.0 |
| 2 | overheated_after_tdcc | 30.0 |
| 2 | price_leading_tdcc | 12.0 |
| 2 | tdcc_leading_price | 105.0 |
| 2 | tdcc_price_confirmed | 4.0 |
| 2 | tdcc_price_divergence | 64.0 |
| 26 | tdcc_leading_price | 2.0 |
| 26 | tdcc_price_divergence | 2.0 |
| 3 | failed_after_tdcc | 3.0 |
| 3 | insufficient_price_context | 28.0 |
| 3 | overheated_after_tdcc | 17.0 |
| 3 | price_leading_tdcc | 5.0 |
| 3 | tdcc_leading_price | 74.0 |
| 3 | tdcc_price_confirmed | 3.0 |
| 3 | tdcc_price_divergence | 38.0 |
| 4 | failed_after_tdcc | 7.0 |
| 4 | insufficient_price_context | 36.0 |
| 4 | overheated_after_tdcc | 17.0 |
| 4 | price_leading_tdcc | 10.0 |
| 4 | tdcc_leading_price | 110.0 |
| 4 | tdcc_price_confirmed | 9.0 |
| 4 | tdcc_price_divergence | 101.0 |
| 5 | overheated_after_tdcc | 1.0 |
| 5 | tdcc_leading_price | 2.0 |
| 5 | tdcc_price_divergence | 7.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | tdcc_leading_price | 5.0 |
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
| all_thresholds_up | insufficient_price_context | 166.0 |
| all_thresholds_up | tdcc_leading_price | 151.0 |
| all_thresholds_up | tdcc_price_divergence | 110.0 |
| all_thresholds_up | overheated_after_tdcc | 55.0 |
| all_thresholds_up | price_leading_tdcc | 30.0 |
| all_thresholds_up | failed_after_tdcc | 9.0 |
| all_thresholds_up | tdcc_price_confirmed | 9.0 |
| high_thresholds_up | insufficient_price_context | 212.0 |
| high_thresholds_up | tdcc_leading_price | 195.0 |
| high_thresholds_up | tdcc_price_divergence | 142.0 |
| high_thresholds_up | overheated_after_tdcc | 60.0 |
| high_thresholds_up | price_leading_tdcc | 37.0 |
| high_thresholds_up | failed_after_tdcc | 11.0 |
| high_thresholds_up | tdcc_price_confirmed | 10.0 |
| over_800_or_above | insufficient_price_context | 328.0 |
| over_800_or_above | tdcc_leading_price | 251.0 |
| over_800_or_above | tdcc_price_divergence | 175.0 |
| over_800_or_above | overheated_after_tdcc | 78.0 |
| over_800_or_above | price_leading_tdcc | 46.0 |
| over_800_or_above | failed_after_tdcc | 15.0 |
| over_800_or_above | tdcc_price_confirmed | 13.0 |
| over_1000_only | insufficient_price_context | 50.0 |
| over_1000_only | tdcc_leading_price | 21.0 |
| over_1000_only | tdcc_price_divergence | 10.0 |
| over_1000_only | overheated_after_tdcc | 9.0 |
| over_1000_only | price_leading_tdcc | 1.0 |
| consecutive_2w | tdcc_leading_price | 308.0 |
| consecutive_2w | tdcc_price_divergence | 223.0 |
| consecutive_2w | insufficient_price_context | 110.0 |
| consecutive_2w | overheated_after_tdcc | 65.0 |
| consecutive_2w | price_leading_tdcc | 27.0 |
| consecutive_2w | failed_after_tdcc | 19.0 |
| consecutive_2w | tdcc_price_confirmed | 16.0 |
| consecutive_3w | tdcc_leading_price | 203.0 |
| consecutive_3w | tdcc_price_divergence | 159.0 |
| consecutive_3w | insufficient_price_context | 66.0 |
| consecutive_3w | overheated_after_tdcc | 35.0 |
| consecutive_3w | price_leading_tdcc | 15.0 |
| consecutive_3w | tdcc_price_confirmed | 12.0 |
| consecutive_3w | failed_after_tdcc | 11.0 |
| quiet_accumulation | tdcc_leading_price | 122.0 |
| quiet_accumulation | tdcc_price_divergence | 100.0 |
| quiet_accumulation | insufficient_price_context | 27.0 |
| quiet_accumulation | failed_after_tdcc | 7.0 |
| quiet_accumulation | overheated_after_tdcc | 3.0 |
| quiet_accumulation | tdcc_price_confirmed | 2.0 |
| early_breakout | tdcc_leading_price | 2.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | insufficient_price_context | 27.0 |
| strong_momentum | price_leading_tdcc | 11.0 |
| strong_momentum | tdcc_leading_price | 9.0 |
| strong_momentum | tdcc_price_confirmed | 4.0 |
| strong_momentum | tdcc_price_divergence | 2.0 |
| strong_momentum | overheated_after_tdcc | 1.0 |
| overheated | overheated_after_tdcc | 104.0 |
| overheated | price_leading_tdcc | 16.0 |
| overheated | insufficient_price_context | 9.0 |
| overheated | tdcc_leading_price | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 17.0 | -0.66 | -5.30 | 12.0 | 1.81 | -7.72 | 8.0 | -2.46 | -18.51 | 6.76 | -5.32 |
| insufficient_price_context | 2376.0 | 0.41 | -1.44 | 1895.0 | 2.51 | -1.52 | 483.0 | 0.85 | -8.59 | 8.11 | -5.03 |
| overheated_after_tdcc | 218.0 | 6.64 | 3.91 | 133.0 | 14.24 | 9.22 | 5.0 | 1.16 | -8.88 | 22.58 | -8.53 |
| price_leading_tdcc | 268.0 | 3.99 | 0.50 | 149.0 | 9.34 | 3.87 | 33.0 | -2.52 | -14.22 | 18.30 | -6.21 |
| tdcc_leading_price | 726.0 | 0.85 | -2.21 | 565.0 | 1.84 | -3.73 | 365.0 | -0.29 | -9.27 | 6.30 | -3.61 |
| tdcc_price_confirmed | 62.0 | 2.56 | -0.51 | 44.0 | 4.16 | -1.15 | 23.0 | -3.46 | -12.22 | 12.65 | -5.06 |
| tdcc_price_divergence | 1114.0 | 0.82 | -2.67 | 770.0 | 0.64 | -5.55 | 375.0 | 0.47 | -9.25 | 5.89 | -4.00 |
