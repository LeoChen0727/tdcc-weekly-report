# TDCC Phase Distribution

- generated_at: 2026-07-18 15:42:01 Asia/Taipei
- latest_signal_count: 1122
- phase_mature_d5_count: 353
- phase_mature_d10_count: 306
- phase_mature_d20_count: 214

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 875.0 | 77.99 |
| price_leading_tdcc | 116.0 | 10.34 |
| tdcc_price_divergence | 89.0 | 7.93 |
| tdcc_leading_price | 33.0 | 2.94 |
| overheated_after_tdcc | 7.0 | 0.62 |
| failed_after_tdcc | 2.0 | 0.18 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 455.0 |
| 1 | overheated_after_tdcc | 2.0 |
| 1 | price_leading_tdcc | 36.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 172.0 |
| 2 | overheated_after_tdcc | 1.0 |
| 2 | price_leading_tdcc | 24.0 |
| 2 | tdcc_leading_price | 12.0 |
| 2 | tdcc_price_divergence | 40.0 |
| 3 | insufficient_price_context | 82.0 |
| 3 | overheated_after_tdcc | 1.0 |
| 3 | price_leading_tdcc | 20.0 |
| 3 | tdcc_leading_price | 4.0 |
| 3 | tdcc_price_divergence | 17.0 |
| 4 | insufficient_price_context | 63.0 |
| 4 | overheated_after_tdcc | 2.0 |
| 4 | price_leading_tdcc | 10.0 |
| 4 | tdcc_leading_price | 5.0 |
| 4 | tdcc_price_divergence | 11.0 |
| 5 | insufficient_price_context | 32.0 |
| 5 | price_leading_tdcc | 2.0 |
| 5 | tdcc_leading_price | 3.0 |
| 5 | tdcc_price_divergence | 9.0 |
| 6 | insufficient_price_context | 57.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 15.0 |
| 6 | tdcc_leading_price | 7.0 |
| 6 | tdcc_price_divergence | 11.0 |
| 7 | insufficient_price_context | 14.0 |
| 7 | price_leading_tdcc | 9.0 |
| 7 | tdcc_leading_price | 2.0 |
| 7 | tdcc_price_divergence | 1.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 220.0 |
| all_thresholds_up | price_leading_tdcc | 102.0 |
| all_thresholds_up | tdcc_price_divergence | 74.0 |
| all_thresholds_up | tdcc_leading_price | 27.0 |
| all_thresholds_up | overheated_after_tdcc | 7.0 |
| all_thresholds_up | failed_after_tdcc | 2.0 |
| high_thresholds_up | insufficient_price_context | 330.0 |
| high_thresholds_up | price_leading_tdcc | 116.0 |
| high_thresholds_up | tdcc_price_divergence | 89.0 |
| high_thresholds_up | tdcc_leading_price | 33.0 |
| high_thresholds_up | overheated_after_tdcc | 7.0 |
| high_thresholds_up | failed_after_tdcc | 2.0 |
| over_800_or_above | insufficient_price_context | 572.0 |
| over_800_or_above | price_leading_tdcc | 116.0 |
| over_800_or_above | tdcc_price_divergence | 89.0 |
| over_800_or_above | tdcc_leading_price | 33.0 |
| over_800_or_above | overheated_after_tdcc | 7.0 |
| over_800_or_above | failed_after_tdcc | 2.0 |
| over_1000_only | insufficient_price_context | 91.0 |
| consecutive_2w | insufficient_price_context | 420.0 |
| consecutive_2w | tdcc_price_divergence | 89.0 |
| consecutive_2w | price_leading_tdcc | 80.0 |
| consecutive_2w | tdcc_leading_price | 33.0 |
| consecutive_2w | overheated_after_tdcc | 5.0 |
| consecutive_2w | failed_after_tdcc | 2.0 |
| consecutive_3w | insufficient_price_context | 248.0 |
| consecutive_3w | price_leading_tdcc | 56.0 |
| consecutive_3w | tdcc_price_divergence | 49.0 |
| consecutive_3w | tdcc_leading_price | 21.0 |
| consecutive_3w | overheated_after_tdcc | 4.0 |
| quiet_accumulation | insufficient_price_context | 108.0 |
| quiet_accumulation | tdcc_price_divergence | 47.0 |
| quiet_accumulation | price_leading_tdcc | 40.0 |
| quiet_accumulation | tdcc_leading_price | 19.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 10.0 |
| strong_momentum | insufficient_price_context | 2.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| strong_momentum | tdcc_leading_price | 1.0 |
| overheated | price_leading_tdcc | 7.0 |
| overheated | overheated_after_tdcc | 7.0 |
| overheated | tdcc_price_divergence | 1.0 |
| overheated | insufficient_price_context | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 122.0 | 0.28 | -0.71 | 107.0 | 2.88 | 0.45 | 77.0 | -0.42 | -2.56 | 15.55 | -9.09 |
| overheated_after_tdcc | 118.0 | 3.36 | 2.02 | 104.0 | 6.50 | 3.85 | 77.0 | 9.68 | 5.59 | 20.05 | -9.81 |
| price_leading_tdcc | 83.0 | 6.02 | 3.82 | 76.0 | 4.99 | 3.13 | 52.0 | 2.69 | 0.93 | 19.65 | -6.07 |
| tdcc_leading_price | 16.0 | 1.11 | 1.62 | 11.0 | -2.47 | -6.50 | 6.0 | -0.39 | -3.95 | 9.07 | -7.92 |
| tdcc_price_confirmed | 5.0 | 0.17 | 0.53 | 2.0 | 6.93 | 5.11 | 0.0 |  |  | 15.86 | -2.81 |
| tdcc_price_divergence | 9.0 | -3.38 | -3.34 | 6.0 | 4.19 | 2.21 | 2.0 | 6.37 | 4.68 | 11.46 | -6.61 |
