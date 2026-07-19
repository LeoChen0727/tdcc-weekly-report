# TDCC Phase Distribution

- generated_at: 2026-07-19 11:55:29 Asia/Taipei
- latest_signal_count: 1105
- phase_mature_d5_count: 352
- phase_mature_d10_count: 305
- phase_mature_d20_count: 214

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 876.0 | 79.28 |
| price_leading_tdcc | 105.0 | 9.50 |
| tdcc_price_divergence | 85.0 | 7.69 |
| tdcc_leading_price | 29.0 | 2.62 |
| overheated_after_tdcc | 7.0 | 0.63 |
| failed_after_tdcc | 3.0 | 0.27 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 472.0 |
| 1 | overheated_after_tdcc | 1.0 |
| 1 | price_leading_tdcc | 13.0 |
| 2 | failed_after_tdcc | 3.0 |
| 2 | insufficient_price_context | 170.0 |
| 2 | overheated_after_tdcc | 1.0 |
| 2 | price_leading_tdcc | 31.0 |
| 2 | tdcc_leading_price | 6.0 |
| 2 | tdcc_price_divergence | 38.0 |
| 3 | insufficient_price_context | 84.0 |
| 3 | price_leading_tdcc | 18.0 |
| 3 | tdcc_leading_price | 10.0 |
| 3 | tdcc_price_divergence | 20.0 |
| 4 | insufficient_price_context | 49.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 17.0 |
| 4 | tdcc_leading_price | 4.0 |
| 4 | tdcc_price_divergence | 10.0 |
| 5 | insufficient_price_context | 35.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 5.0 |
| 5 | tdcc_leading_price | 1.0 |
| 5 | tdcc_price_divergence | 2.0 |
| 6 | insufficient_price_context | 18.0 |
| 6 | tdcc_price_divergence | 5.0 |
| 7 | insufficient_price_context | 48.0 |
| 7 | overheated_after_tdcc | 2.0 |
| 7 | price_leading_tdcc | 21.0 |
| 7 | tdcc_leading_price | 8.0 |
| 7 | tdcc_price_divergence | 10.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 208.0 |
| all_thresholds_up | price_leading_tdcc | 91.0 |
| all_thresholds_up | tdcc_price_divergence | 59.0 |
| all_thresholds_up | tdcc_leading_price | 22.0 |
| all_thresholds_up | overheated_after_tdcc | 7.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| high_thresholds_up | insufficient_price_context | 282.0 |
| high_thresholds_up | price_leading_tdcc | 105.0 |
| high_thresholds_up | tdcc_price_divergence | 85.0 |
| high_thresholds_up | tdcc_leading_price | 29.0 |
| high_thresholds_up | overheated_after_tdcc | 7.0 |
| high_thresholds_up | failed_after_tdcc | 3.0 |
| over_800_or_above | insufficient_price_context | 535.0 |
| over_800_or_above | price_leading_tdcc | 105.0 |
| over_800_or_above | tdcc_price_divergence | 85.0 |
| over_800_or_above | tdcc_leading_price | 29.0 |
| over_800_or_above | overheated_after_tdcc | 7.0 |
| over_800_or_above | failed_after_tdcc | 3.0 |
| over_1000_only | insufficient_price_context | 97.0 |
| consecutive_2w | insufficient_price_context | 404.0 |
| consecutive_2w | price_leading_tdcc | 92.0 |
| consecutive_2w | tdcc_price_divergence | 85.0 |
| consecutive_2w | tdcc_leading_price | 29.0 |
| consecutive_2w | overheated_after_tdcc | 6.0 |
| consecutive_2w | failed_after_tdcc | 3.0 |
| consecutive_3w | insufficient_price_context | 234.0 |
| consecutive_3w | price_leading_tdcc | 61.0 |
| consecutive_3w | tdcc_price_divergence | 47.0 |
| consecutive_3w | tdcc_leading_price | 23.0 |
| consecutive_3w | overheated_after_tdcc | 5.0 |
| quiet_accumulation | insufficient_price_context | 87.0 |
| quiet_accumulation | price_leading_tdcc | 50.0 |
| quiet_accumulation | tdcc_price_divergence | 48.0 |
| quiet_accumulation | tdcc_leading_price | 17.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 8.0 |
| strong_momentum | insufficient_price_context | 4.0 |
| strong_momentum | tdcc_price_divergence | 1.0 |
| overheated | price_leading_tdcc | 8.0 |
| overheated | overheated_after_tdcc | 7.0 |
| overheated | insufficient_price_context | 2.0 |
| overheated | tdcc_price_divergence | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 114.0 | 0.38 | -0.38 | 99.0 | 2.25 | -0.16 | 69.0 | -1.04 | -2.55 | 15.38 | -9.24 |
| overheated_after_tdcc | 119.0 | 3.28 | 1.91 | 105.0 | 6.57 | 3.87 | 78.0 | 10.17 | 5.96 | 20.05 | -9.83 |
| price_leading_tdcc | 84.0 | 3.13 | 0.84 | 77.0 | 2.40 | 0.49 | 54.0 | 1.88 | -0.19 | 16.26 | -8.69 |
| tdcc_leading_price | 18.0 | 0.62 | 0.91 | 13.0 | 0.39 | -3.11 | 8.0 | -0.45 | -3.87 | 11.50 | -7.57 |
| tdcc_price_confirmed | 8.0 | 0.89 | -0.69 | 5.0 | 10.12 | 8.28 | 3.0 | 10.55 | 3.40 | 16.76 | -5.04 |
| tdcc_price_divergence | 9.0 | -3.38 | -3.34 | 6.0 | 4.19 | 2.21 | 2.0 | 6.37 | 4.68 | 11.46 | -6.61 |
