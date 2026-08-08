# TDCC Phase Distribution

- generated_at: 2026-08-08 15:53:29 Asia/Taipei
- latest_signal_count: 1178
- phase_mature_d5_count: 491
- phase_mature_d10_count: 433
- phase_mature_d20_count: 350

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 886.0 | 75.21 |
| tdcc_price_divergence | 123.0 | 10.44 |
| overheated_after_tdcc | 76.0 | 6.45 |
| tdcc_leading_price | 68.0 | 5.77 |
| price_leading_tdcc | 19.0 | 1.61 |
| failed_after_tdcc | 5.0 | 0.42 |
| tdcc_price_confirmed | 1.0 | 0.08 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 456.0 |
| 1 | overheated_after_tdcc | 39.0 |
| 1 | price_leading_tdcc | 3.0 |
| 10 | insufficient_price_context | 4.0 |
| 10 | tdcc_leading_price | 2.0 |
| 11 | insufficient_price_context | 2.0 |
| 11 | tdcc_price_divergence | 3.0 |
| 12 | insufficient_price_context | 7.0 |
| 12 | tdcc_leading_price | 2.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 3.0 |
| 14 | insufficient_price_context | 6.0 |
| 14 | price_leading_tdcc | 1.0 |
| 14 | tdcc_leading_price | 2.0 |
| 14 | tdcc_price_divergence | 4.0 |
| 15 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 161.0 |
| 2 | overheated_after_tdcc | 15.0 |
| 2 | price_leading_tdcc | 3.0 |
| 2 | tdcc_leading_price | 21.0 |
| 2 | tdcc_price_confirmed | 1.0 |
| 2 | tdcc_price_divergence | 40.0 |
| 26 | insufficient_price_context | 1.0 |
| 3 | failed_after_tdcc | 2.0 |
| 3 | insufficient_price_context | 106.0 |
| 3 | overheated_after_tdcc | 14.0 |
| 3 | price_leading_tdcc | 2.0 |
| 3 | tdcc_leading_price | 12.0 |
| 3 | tdcc_price_divergence | 30.0 |
| 36 | tdcc_price_divergence | 1.0 |
| 4 | failed_after_tdcc | 1.0 |
| 4 | insufficient_price_context | 56.0 |
| 4 | overheated_after_tdcc | 5.0 |
| 4 | price_leading_tdcc | 4.0 |
| 4 | tdcc_leading_price | 9.0 |
| 4 | tdcc_price_divergence | 16.0 |
| 5 | insufficient_price_context | 43.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 3.0 |
| 5 | tdcc_leading_price | 7.0 |
| 5 | tdcc_price_divergence | 8.0 |
| 6 | insufficient_price_context | 18.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 7.0 |
| 6 | tdcc_price_divergence | 8.0 |
| 7 | insufficient_price_context | 12.0 |
| 7 | tdcc_leading_price | 3.0 |
| 7 | tdcc_price_divergence | 3.0 |
| 8 | insufficient_price_context | 8.0 |
| 8 | price_leading_tdcc | 1.0 |
| 8 | tdcc_leading_price | 2.0 |
| 8 | tdcc_price_divergence | 4.0 |
| 9 | insufficient_price_context | 3.0 |
| 9 | price_leading_tdcc | 1.0 |
| 9 | tdcc_leading_price | 1.0 |
| 9 | tdcc_price_divergence | 4.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 187.0 |
| all_thresholds_up | tdcc_price_divergence | 112.0 |
| all_thresholds_up | tdcc_leading_price | 61.0 |
| all_thresholds_up | overheated_after_tdcc | 61.0 |
| all_thresholds_up | price_leading_tdcc | 19.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| all_thresholds_up | tdcc_price_confirmed | 1.0 |
| high_thresholds_up | insufficient_price_context | 307.0 |
| high_thresholds_up | tdcc_price_divergence | 123.0 |
| high_thresholds_up | overheated_after_tdcc | 76.0 |
| high_thresholds_up | tdcc_leading_price | 68.0 |
| high_thresholds_up | price_leading_tdcc | 19.0 |
| high_thresholds_up | failed_after_tdcc | 5.0 |
| high_thresholds_up | tdcc_price_confirmed | 1.0 |
| over_800_or_above | insufficient_price_context | 564.0 |
| over_800_or_above | tdcc_price_divergence | 123.0 |
| over_800_or_above | overheated_after_tdcc | 76.0 |
| over_800_or_above | tdcc_leading_price | 68.0 |
| over_800_or_above | price_leading_tdcc | 19.0 |
| over_800_or_above | failed_after_tdcc | 5.0 |
| over_800_or_above | tdcc_price_confirmed | 1.0 |
| over_1000_only | insufficient_price_context | 100.0 |
| consecutive_2w | insufficient_price_context | 430.0 |
| consecutive_2w | tdcc_price_divergence | 123.0 |
| consecutive_2w | tdcc_leading_price | 68.0 |
| consecutive_2w | overheated_after_tdcc | 37.0 |
| consecutive_2w | price_leading_tdcc | 16.0 |
| consecutive_2w | failed_after_tdcc | 5.0 |
| consecutive_2w | tdcc_price_confirmed | 1.0 |
| consecutive_3w | insufficient_price_context | 269.0 |
| consecutive_3w | tdcc_price_divergence | 83.0 |
| consecutive_3w | tdcc_leading_price | 47.0 |
| consecutive_3w | overheated_after_tdcc | 22.0 |
| consecutive_3w | price_leading_tdcc | 13.0 |
| consecutive_3w | failed_after_tdcc | 3.0 |
| quiet_accumulation | insufficient_price_context | 88.0 |
| quiet_accumulation | tdcc_price_divergence | 77.0 |
| quiet_accumulation | tdcc_leading_price | 44.0 |
| quiet_accumulation | price_leading_tdcc | 5.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 5.0 |
| strong_momentum | insufficient_price_context | 4.0 |
| overheated | overheated_after_tdcc | 76.0 |
| overheated | price_leading_tdcc | 1.0 |
| overheated | insufficient_price_context | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 2.0 | -8.28 | -7.06 | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 185.0 | -0.60 | -0.88 | 153.0 | -1.78 | -1.49 | 107.0 | -7.39 | -4.21 | 12.17 | -10.54 |
| overheated_after_tdcc | 124.0 | 2.69 | 1.60 | 119.0 | 2.76 | 1.87 | 116.0 | -2.19 | -1.83 | 19.25 | -11.63 |
| price_leading_tdcc | 116.0 | 1.06 | -0.39 | 107.0 | -0.88 | -0.46 | 82.0 | -3.76 | -1.90 | 13.44 | -10.31 |
| tdcc_leading_price | 33.0 | -0.30 | 0.34 | 30.0 | -0.82 | -2.12 | 25.0 | -4.28 | -3.14 | 9.78 | -9.68 |
| tdcc_price_confirmed | 11.0 | -1.99 | -1.91 | 11.0 | 0.23 | 0.73 | 11.0 | -3.80 | -2.80 | 12.27 | -11.85 |
| tdcc_price_divergence | 20.0 | -6.38 | -5.86 | 13.0 | -8.25 | -6.20 | 9.0 | -6.80 | 1.58 | 8.65 | -16.86 |
