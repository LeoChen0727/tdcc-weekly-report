# TDCC Phase Distribution

- generated_at: 2026-07-19 07:20:37 Asia/Taipei
- latest_signal_count: 1284
- phase_mature_d5_count: 353
- phase_mature_d10_count: 306
- phase_mature_d20_count: 214

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 1029.0 | 80.14 |
| price_leading_tdcc | 114.0 | 8.88 |
| tdcc_price_divergence | 98.0 | 7.63 |
| tdcc_leading_price | 31.0 | 2.41 |
| overheated_after_tdcc | 8.0 | 0.62 |
| failed_after_tdcc | 4.0 | 0.31 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 552.0 |
| 1 | overheated_after_tdcc | 2.0 |
| 1 | price_leading_tdcc | 16.0 |
| 2 | failed_after_tdcc | 4.0 |
| 2 | insufficient_price_context | 210.0 |
| 2 | overheated_after_tdcc | 1.0 |
| 2 | price_leading_tdcc | 34.0 |
| 2 | tdcc_leading_price | 8.0 |
| 2 | tdcc_price_divergence | 43.0 |
| 3 | insufficient_price_context | 98.0 |
| 3 | price_leading_tdcc | 19.0 |
| 3 | tdcc_leading_price | 10.0 |
| 3 | tdcc_price_divergence | 23.0 |
| 4 | insufficient_price_context | 58.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 18.0 |
| 4 | tdcc_leading_price | 4.0 |
| 4 | tdcc_price_divergence | 13.0 |
| 5 | insufficient_price_context | 37.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 5.0 |
| 5 | tdcc_leading_price | 1.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | insufficient_price_context | 26.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_price_divergence | 6.0 |
| 7 | insufficient_price_context | 48.0 |
| 7 | overheated_after_tdcc | 2.0 |
| 7 | price_leading_tdcc | 21.0 |
| 7 | tdcc_leading_price | 8.0 |
| 7 | tdcc_price_divergence | 10.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 235.0 |
| all_thresholds_up | price_leading_tdcc | 100.0 |
| all_thresholds_up | tdcc_price_divergence | 71.0 |
| all_thresholds_up | tdcc_leading_price | 24.0 |
| all_thresholds_up | overheated_after_tdcc | 8.0 |
| all_thresholds_up | failed_after_tdcc | 4.0 |
| high_thresholds_up | insufficient_price_context | 329.0 |
| high_thresholds_up | price_leading_tdcc | 114.0 |
| high_thresholds_up | tdcc_price_divergence | 98.0 |
| high_thresholds_up | tdcc_leading_price | 31.0 |
| high_thresholds_up | overheated_after_tdcc | 8.0 |
| high_thresholds_up | failed_after_tdcc | 4.0 |
| over_800_or_above | insufficient_price_context | 628.0 |
| over_800_or_above | price_leading_tdcc | 114.0 |
| over_800_or_above | tdcc_price_divergence | 98.0 |
| over_800_or_above | tdcc_leading_price | 31.0 |
| over_800_or_above | overheated_after_tdcc | 8.0 |
| over_800_or_above | failed_after_tdcc | 4.0 |
| over_1000_only | insufficient_price_context | 114.0 |
| consecutive_2w | insufficient_price_context | 477.0 |
| consecutive_2w | price_leading_tdcc | 98.0 |
| consecutive_2w | tdcc_price_divergence | 98.0 |
| consecutive_2w | tdcc_leading_price | 31.0 |
| consecutive_2w | overheated_after_tdcc | 6.0 |
| consecutive_2w | failed_after_tdcc | 4.0 |
| consecutive_3w | insufficient_price_context | 267.0 |
| consecutive_3w | price_leading_tdcc | 64.0 |
| consecutive_3w | tdcc_price_divergence | 55.0 |
| consecutive_3w | tdcc_leading_price | 23.0 |
| consecutive_3w | overheated_after_tdcc | 5.0 |
| quiet_accumulation | insufficient_price_context | 97.0 |
| quiet_accumulation | price_leading_tdcc | 54.0 |
| quiet_accumulation | tdcc_price_divergence | 54.0 |
| quiet_accumulation | tdcc_leading_price | 19.0 |
| quiet_accumulation | failed_after_tdcc | 3.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 8.0 |
| strong_momentum | insufficient_price_context | 4.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| overheated | price_leading_tdcc | 9.0 |
| overheated | overheated_after_tdcc | 8.0 |
| overheated | insufficient_price_context | 2.0 |
| overheated | tdcc_price_divergence | 1.0 |

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
