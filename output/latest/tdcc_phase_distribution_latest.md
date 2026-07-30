# TDCC Phase Distribution

- generated_at: 2026-07-31 00:54:28 Asia/Taipei
- latest_signal_count: 1130
- phase_mature_d5_count: 434
- phase_mature_d10_count: 351
- phase_mature_d20_count: 304

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 894.0 | 79.12 |
| tdcc_price_divergence | 84.0 | 7.43 |
| price_leading_tdcc | 83.0 | 7.35 |
| tdcc_leading_price | 55.0 | 4.87 |
| overheated_after_tdcc | 8.0 | 0.71 |
| failed_after_tdcc | 6.0 | 0.53 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 427.0 |
| 1 | overheated_after_tdcc | 2.0 |
| 1 | price_leading_tdcc | 20.0 |
| 10 | insufficient_price_context | 4.0 |
| 10 | price_leading_tdcc | 4.0 |
| 10 | tdcc_leading_price | 4.0 |
| 10 | tdcc_price_divergence | 2.0 |
| 11 | insufficient_price_context | 1.0 |
| 11 | price_leading_tdcc | 3.0 |
| 11 | tdcc_leading_price | 1.0 |
| 12 | insufficient_price_context | 13.0 |
| 12 | price_leading_tdcc | 3.0 |
| 12 | tdcc_leading_price | 2.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 2.0 |
| 2 | failed_after_tdcc | 3.0 |
| 2 | insufficient_price_context | 190.0 |
| 2 | price_leading_tdcc | 23.0 |
| 2 | tdcc_leading_price | 19.0 |
| 2 | tdcc_price_divergence | 37.0 |
| 24 | insufficient_price_context | 1.0 |
| 3 | failed_after_tdcc | 3.0 |
| 3 | insufficient_price_context | 112.0 |
| 3 | overheated_after_tdcc | 1.0 |
| 3 | price_leading_tdcc | 9.0 |
| 3 | tdcc_leading_price | 7.0 |
| 3 | tdcc_price_divergence | 20.0 |
| 34 | tdcc_leading_price | 1.0 |
| 4 | insufficient_price_context | 55.0 |
| 4 | overheated_after_tdcc | 2.0 |
| 4 | price_leading_tdcc | 6.0 |
| 4 | tdcc_leading_price | 9.0 |
| 4 | tdcc_price_divergence | 13.0 |
| 5 | insufficient_price_context | 35.0 |
| 5 | overheated_after_tdcc | 1.0 |
| 5 | price_leading_tdcc | 5.0 |
| 5 | tdcc_leading_price | 6.0 |
| 5 | tdcc_price_divergence | 8.0 |
| 6 | insufficient_price_context | 20.0 |
| 6 | overheated_after_tdcc | 2.0 |
| 6 | price_leading_tdcc | 6.0 |
| 6 | tdcc_leading_price | 2.0 |
| 7 | insufficient_price_context | 12.0 |
| 7 | price_leading_tdcc | 4.0 |
| 7 | tdcc_leading_price | 2.0 |
| 7 | tdcc_price_divergence | 1.0 |
| 8 | insufficient_price_context | 12.0 |
| 8 | tdcc_leading_price | 2.0 |
| 9 | insufficient_price_context | 10.0 |
| 9 | tdcc_price_divergence | 2.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 200.0 |
| all_thresholds_up | price_leading_tdcc | 67.0 |
| all_thresholds_up | tdcc_price_divergence | 62.0 |
| all_thresholds_up | tdcc_leading_price | 42.0 |
| all_thresholds_up | overheated_after_tdcc | 8.0 |
| all_thresholds_up | failed_after_tdcc | 5.0 |
| high_thresholds_up | insufficient_price_context | 305.0 |
| high_thresholds_up | tdcc_price_divergence | 84.0 |
| high_thresholds_up | price_leading_tdcc | 83.0 |
| high_thresholds_up | tdcc_leading_price | 55.0 |
| high_thresholds_up | overheated_after_tdcc | 8.0 |
| high_thresholds_up | failed_after_tdcc | 6.0 |
| over_800_or_above | insufficient_price_context | 578.0 |
| over_800_or_above | tdcc_price_divergence | 84.0 |
| over_800_or_above | price_leading_tdcc | 83.0 |
| over_800_or_above | tdcc_leading_price | 55.0 |
| over_800_or_above | overheated_after_tdcc | 8.0 |
| over_800_or_above | failed_after_tdcc | 6.0 |
| over_1000_only | insufficient_price_context | 105.0 |
| consecutive_2w | insufficient_price_context | 467.0 |
| consecutive_2w | tdcc_price_divergence | 84.0 |
| consecutive_2w | price_leading_tdcc | 63.0 |
| consecutive_2w | tdcc_leading_price | 55.0 |
| consecutive_2w | failed_after_tdcc | 6.0 |
| consecutive_2w | overheated_after_tdcc | 6.0 |
| consecutive_3w | insufficient_price_context | 277.0 |
| consecutive_3w | tdcc_price_divergence | 47.0 |
| consecutive_3w | price_leading_tdcc | 40.0 |
| consecutive_3w | tdcc_leading_price | 36.0 |
| consecutive_3w | overheated_after_tdcc | 6.0 |
| consecutive_3w | failed_after_tdcc | 3.0 |
| quiet_accumulation | insufficient_price_context | 113.0 |
| quiet_accumulation | tdcc_price_divergence | 42.0 |
| quiet_accumulation | price_leading_tdcc | 36.0 |
| quiet_accumulation | tdcc_leading_price | 33.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| early_breakout | price_leading_tdcc | 1.0 |
| strong_momentum | insufficient_price_context | 5.0 |
| strong_momentum | price_leading_tdcc | 5.0 |
| overheated | overheated_after_tdcc | 8.0 |
| overheated | price_leading_tdcc | 3.0 |
| overheated | insufficient_price_context | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 153.0 | 0.68 | -0.78 | 107.0 | -0.39 | -0.40 | 92.0 | -4.89 | -3.10 | 14.55 | -10.72 |
| overheated_after_tdcc | 119.0 | 3.48 | 2.18 | 116.0 | 3.36 | 2.31 | 102.0 | 2.00 | 1.31 | 19.36 | -11.22 |
| price_leading_tdcc | 107.0 | 2.04 | 0.11 | 82.0 | 0.90 | 0.29 | 75.0 | -2.08 | -1.18 | 15.60 | -9.75 |
| tdcc_leading_price | 30.0 | -0.18 | 0.17 | 25.0 | 0.72 | -0.98 | 20.0 | -3.40 | -4.35 | 10.60 | -8.60 |
| tdcc_price_confirmed | 11.0 | -1.99 | -1.91 | 11.0 | 0.23 | 0.73 | 8.0 | 3.12 | 0.37 | 12.27 | -11.85 |
| tdcc_price_divergence | 14.0 | -4.37 | -4.15 | 10.0 | -5.68 | -4.52 | 7.0 | -0.35 | 5.14 | 9.70 | -14.84 |
