# TDCC Phase Distribution

- generated_at: 2026-05-25 14:08:26 Asia/Taipei
- latest_signal_count: 1195
- phase_mature_d5_count: 3592
- phase_mature_d10_count: 2457
- phase_mature_d20_count: 1229

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 472.0 | 39.50 |
| tdcc_price_divergence | 337.0 | 28.20 |
| tdcc_leading_price | 159.0 | 13.31 |
| price_leading_tdcc | 119.0 | 9.96 |
| overheated_after_tdcc | 85.0 | 7.11 |
| tdcc_price_confirmed | 18.0 | 1.51 |
| failed_after_tdcc | 5.0 | 0.42 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 391.0 |
| 1 | overheated_after_tdcc | 28.0 |
| 1 | price_leading_tdcc | 38.0 |
| 10 | tdcc_leading_price | 1.0 |
| 12 | tdcc_price_divergence | 2.0 |
| 13 | tdcc_leading_price | 1.0 |
| 14 | tdcc_leading_price | 1.0 |
| 15 | tdcc_leading_price | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 37.0 |
| 2 | overheated_after_tdcc | 18.0 |
| 2 | price_leading_tdcc | 33.0 |
| 2 | tdcc_leading_price | 54.0 |
| 2 | tdcc_price_confirmed | 7.0 |
| 2 | tdcc_price_divergence | 101.0 |
| 25 | tdcc_leading_price | 3.0 |
| 25 | tdcc_price_divergence | 1.0 |
| 3 | failed_after_tdcc | 2.0 |
| 3 | insufficient_price_context | 42.0 |
| 3 | overheated_after_tdcc | 39.0 |
| 3 | price_leading_tdcc | 48.0 |
| 3 | tdcc_leading_price | 81.0 |
| 3 | tdcc_price_confirmed | 11.0 |
| 3 | tdcc_price_divergence | 216.0 |
| 4 | insufficient_price_context | 2.0 |
| 4 | tdcc_leading_price | 6.0 |
| 4 | tdcc_price_divergence | 4.0 |
| 5 | tdcc_leading_price | 6.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 4.0 |
| 7 | failed_after_tdcc | 1.0 |
| 7 | tdcc_leading_price | 1.0 |
| 7 | tdcc_price_divergence | 3.0 |
| 8 | tdcc_price_divergence | 2.0 |
| 9 | tdcc_price_divergence | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | tdcc_price_divergence | 161.0 |
| all_thresholds_up | insufficient_price_context | 133.0 |
| all_thresholds_up | tdcc_leading_price | 82.0 |
| all_thresholds_up | price_leading_tdcc | 49.0 |
| all_thresholds_up | overheated_after_tdcc | 48.0 |
| all_thresholds_up | tdcc_price_confirmed | 11.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| high_thresholds_up | tdcc_price_divergence | 204.0 |
| high_thresholds_up | insufficient_price_context | 195.0 |
| high_thresholds_up | tdcc_leading_price | 93.0 |
| high_thresholds_up | price_leading_tdcc | 56.0 |
| high_thresholds_up | overheated_after_tdcc | 53.0 |
| high_thresholds_up | tdcc_price_confirmed | 11.0 |
| high_thresholds_up | failed_after_tdcc | 3.0 |
| over_800_or_above | insufficient_price_context | 319.0 |
| over_800_or_above | tdcc_price_divergence | 272.0 |
| over_800_or_above | tdcc_leading_price | 132.0 |
| over_800_or_above | price_leading_tdcc | 80.0 |
| over_800_or_above | overheated_after_tdcc | 69.0 |
| over_800_or_above | tdcc_price_confirmed | 14.0 |
| over_800_or_above | failed_after_tdcc | 5.0 |
| over_1000_only | insufficient_price_context | 46.0 |
| over_1000_only | tdcc_price_divergence | 17.0 |
| over_1000_only | tdcc_leading_price | 12.0 |
| over_1000_only | overheated_after_tdcc | 7.0 |
| over_1000_only | price_leading_tdcc | 7.0 |
| over_1000_only | failed_after_tdcc | 2.0 |
| over_1000_only | tdcc_price_confirmed | 2.0 |
| consecutive_2w | tdcc_price_divergence | 337.0 |
| consecutive_2w | tdcc_leading_price | 159.0 |
| consecutive_2w | insufficient_price_context | 81.0 |
| consecutive_2w | price_leading_tdcc | 81.0 |
| consecutive_2w | overheated_after_tdcc | 57.0 |
| consecutive_2w | tdcc_price_confirmed | 18.0 |
| consecutive_2w | failed_after_tdcc | 5.0 |
| consecutive_3w | tdcc_price_divergence | 236.0 |
| consecutive_3w | tdcc_leading_price | 105.0 |
| consecutive_3w | price_leading_tdcc | 48.0 |
| consecutive_3w | insufficient_price_context | 44.0 |
| consecutive_3w | overheated_after_tdcc | 39.0 |
| consecutive_3w | tdcc_price_confirmed | 11.0 |
| consecutive_3w | failed_after_tdcc | 3.0 |
| quiet_accumulation | tdcc_price_divergence | 142.0 |
| quiet_accumulation | tdcc_leading_price | 61.0 |
| quiet_accumulation | insufficient_price_context | 19.0 |
| quiet_accumulation | failed_after_tdcc | 3.0 |
| quiet_accumulation | price_leading_tdcc | 2.0 |
| quiet_accumulation | tdcc_price_confirmed | 1.0 |
| early_breakout | tdcc_price_confirmed | 2.0 |
| early_breakout | insufficient_price_context | 2.0 |
| early_breakout | tdcc_leading_price | 1.0 |
| strong_momentum | insufficient_price_context | 32.0 |
| strong_momentum | price_leading_tdcc | 31.0 |
| strong_momentum | tdcc_leading_price | 6.0 |
| strong_momentum | overheated_after_tdcc | 3.0 |
| strong_momentum | tdcc_price_confirmed | 3.0 |
| strong_momentum | tdcc_price_divergence | 2.0 |
| overheated | overheated_after_tdcc | 85.0 |
| overheated | price_leading_tdcc | 37.0 |
| overheated | insufficient_price_context | 12.0 |
| overheated | tdcc_price_divergence | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 12.0 | -0.55 | -4.77 | 8.0 | 2.48 | -7.86 | 8.0 | -2.46 | -18.51 | 6.32 | -5.13 |
| insufficient_price_context | 1907.0 | 0.31 | -0.67 | 1482.0 | 1.57 | -1.28 | 467.0 | 0.71 | -8.60 | 6.93 | -5.23 |
| overheated_after_tdcc | 133.0 | 4.42 | 3.40 | 73.0 | 9.38 | 7.10 | 5.0 | 1.16 | -8.88 | 17.53 | -9.59 |
| price_leading_tdcc | 149.0 | 4.43 | 2.58 | 83.0 | 4.14 | 0.98 | 33.0 | -2.52 | -14.22 | 12.97 | -6.74 |
| tdcc_leading_price | 569.0 | 0.87 | -1.54 | 380.0 | -0.22 | -4.47 | 358.0 | -0.34 | -9.03 | 3.90 | -3.54 |
| tdcc_price_confirmed | 44.0 | 3.51 | 1.33 | 23.0 | -0.44 | -2.91 | 22.0 | -3.90 | -12.75 | 8.76 | -5.99 |
| tdcc_price_divergence | 778.0 | 0.79 | -1.86 | 408.0 | -0.32 | -4.58 | 336.0 | 0.49 | -8.25 | 4.67 | -3.90 |
