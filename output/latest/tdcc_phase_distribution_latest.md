# TDCC Phase Distribution

- generated_at: 2026-09-05 15:45:29 Asia/Taipei
- latest_signal_count: 1052
- phase_mature_d5_count: 739
- phase_mature_d10_count: 686
- phase_mature_d20_count: 607

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 712.0 | 67.68 |
| tdcc_price_divergence | 173.0 | 16.44 |
| tdcc_leading_price | 113.0 | 10.74 |
| price_leading_tdcc | 26.0 | 2.47 |
| overheated_after_tdcc | 12.0 | 1.14 |
| tdcc_price_confirmed | 11.0 | 1.05 |
| failed_after_tdcc | 5.0 | 0.48 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 406.0 |
| 1 | overheated_after_tdcc | 1.0 |
| 1 | price_leading_tdcc | 6.0 |
| 10 | insufficient_price_context | 4.0 |
| 10 | tdcc_leading_price | 2.0 |
| 10 | tdcc_price_divergence | 8.0 |
| 11 | insufficient_price_context | 1.0 |
| 11 | tdcc_leading_price | 2.0 |
| 11 | tdcc_price_divergence | 4.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 1.0 |
| 13 | tdcc_leading_price | 1.0 |
| 13 | tdcc_price_divergence | 2.0 |
| 15 | insufficient_price_context | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 18 | tdcc_leading_price | 2.0 |
| 18 | tdcc_price_divergence | 4.0 |
| 19 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 126.0 |
| 2 | overheated_after_tdcc | 5.0 |
| 2 | price_leading_tdcc | 9.0 |
| 2 | tdcc_leading_price | 32.0 |
| 2 | tdcc_price_confirmed | 6.0 |
| 2 | tdcc_price_divergence | 42.0 |
| 3 | failed_after_tdcc | 1.0 |
| 3 | insufficient_price_context | 66.0 |
| 3 | overheated_after_tdcc | 3.0 |
| 3 | price_leading_tdcc | 6.0 |
| 3 | tdcc_leading_price | 24.0 |
| 3 | tdcc_price_confirmed | 2.0 |
| 3 | tdcc_price_divergence | 28.0 |
| 4 | insufficient_price_context | 43.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 3.0 |
| 4 | tdcc_leading_price | 18.0 |
| 4 | tdcc_price_divergence | 28.0 |
| 40 | tdcc_price_divergence | 1.0 |
| 5 | failed_after_tdcc | 1.0 |
| 5 | insufficient_price_context | 39.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 1.0 |
| 5 | tdcc_leading_price | 15.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 19.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 9.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 9.0 |
| 6 | tdcc_price_confirmed | 1.0 |
| 6 | tdcc_price_divergence | 14.0 |
| 7 | insufficient_price_context | 7.0 |
| 7 | tdcc_leading_price | 2.0 |
| 7 | tdcc_price_divergence | 11.0 |
| 8 | insufficient_price_context | 4.0 |
| 8 | tdcc_leading_price | 4.0 |
| 8 | tdcc_price_confirmed | 1.0 |
| 8 | tdcc_price_divergence | 6.0 |
| 9 | insufficient_price_context | 5.0 |
| 9 | tdcc_leading_price | 1.0 |
| 9 | tdcc_price_divergence | 4.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | tdcc_price_divergence | 126.0 |
| all_thresholds_up | insufficient_price_context | 108.0 |
| all_thresholds_up | tdcc_leading_price | 80.0 |
| all_thresholds_up | price_leading_tdcc | 22.0 |
| all_thresholds_up | overheated_after_tdcc | 11.0 |
| all_thresholds_up | tdcc_price_confirmed | 10.0 |
| all_thresholds_up | failed_after_tdcc | 3.0 |
| high_thresholds_up | tdcc_price_divergence | 173.0 |
| high_thresholds_up | insufficient_price_context | 162.0 |
| high_thresholds_up | tdcc_leading_price | 113.0 |
| high_thresholds_up | price_leading_tdcc | 26.0 |
| high_thresholds_up | overheated_after_tdcc | 12.0 |
| high_thresholds_up | tdcc_price_confirmed | 11.0 |
| high_thresholds_up | failed_after_tdcc | 5.0 |
| over_800_or_above | insufficient_price_context | 397.0 |
| over_800_or_above | tdcc_price_divergence | 173.0 |
| over_800_or_above | tdcc_leading_price | 113.0 |
| over_800_or_above | price_leading_tdcc | 26.0 |
| over_800_or_above | overheated_after_tdcc | 12.0 |
| over_800_or_above | tdcc_price_confirmed | 11.0 |
| over_800_or_above | failed_after_tdcc | 5.0 |
| over_1000_only | insufficient_price_context | 96.0 |
| consecutive_2w | insufficient_price_context | 306.0 |
| consecutive_2w | tdcc_price_divergence | 173.0 |
| consecutive_2w | tdcc_leading_price | 113.0 |
| consecutive_2w | price_leading_tdcc | 20.0 |
| consecutive_2w | tdcc_price_confirmed | 11.0 |
| consecutive_2w | overheated_after_tdcc | 11.0 |
| consecutive_2w | failed_after_tdcc | 5.0 |
| consecutive_3w | insufficient_price_context | 180.0 |
| consecutive_3w | tdcc_price_divergence | 131.0 |
| consecutive_3w | tdcc_leading_price | 81.0 |
| consecutive_3w | price_leading_tdcc | 11.0 |
| consecutive_3w | overheated_after_tdcc | 6.0 |
| consecutive_3w | tdcc_price_confirmed | 5.0 |
| consecutive_3w | failed_after_tdcc | 3.0 |
| quiet_accumulation | tdcc_price_divergence | 123.0 |
| quiet_accumulation | tdcc_leading_price | 63.0 |
| quiet_accumulation | insufficient_price_context | 12.0 |
| quiet_accumulation | price_leading_tdcc | 3.0 |
| quiet_accumulation | failed_after_tdcc | 2.0 |
| early_breakout | price_leading_tdcc | 1.0 |
| early_breakout | tdcc_leading_price | 1.0 |
| strong_momentum | price_leading_tdcc | 16.0 |
| strong_momentum | insufficient_price_context | 13.0 |
| strong_momentum | tdcc_price_confirmed | 4.0 |
| strong_momentum | tdcc_leading_price | 4.0 |
| strong_momentum | tdcc_price_divergence | 3.0 |
| overheated | overheated_after_tdcc | 12.0 |
| overheated | tdcc_leading_price | 3.0 |
| overheated | price_leading_tdcc | 3.0 |
| overheated | insufficient_price_context | 2.0 |
| overheated | tdcc_price_confirmed | 1.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 5.0 | 2.05 | 0.43 | 5.0 | 12.30 | 9.92 | 5.0 | 22.03 | 17.10 | 24.10 | -9.97 |
| insufficient_price_context | 286.0 | 1.50 | -0.17 | 265.0 | 1.69 | -0.46 | 245.0 | 1.81 | -1.03 | 13.29 | -9.14 |
| overheated_after_tdcc | 171.0 | 2.96 | 1.84 | 160.0 | 2.75 | 1.62 | 135.0 | -1.53 | -1.88 | 18.54 | -11.23 |
| price_leading_tdcc | 154.0 | 1.19 | -0.33 | 143.0 | -0.37 | -0.79 | 126.0 | -1.12 | -2.03 | 12.19 | -10.01 |
| tdcc_leading_price | 50.0 | 0.02 | -0.39 | 47.0 | -0.64 | -2.62 | 42.0 | -2.51 | -4.38 | 9.25 | -8.73 |
| tdcc_price_confirmed | 17.0 | 0.33 | -0.57 | 15.0 | 0.77 | 0.57 | 13.0 | -2.28 | -2.16 | 11.39 | -10.35 |
| tdcc_price_divergence | 56.0 | 2.88 | 0.18 | 51.0 | 6.03 | 1.80 | 41.0 | 10.70 | 5.78 | 16.53 | -7.99 |
