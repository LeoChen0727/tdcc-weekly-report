# TDCC Phase Distribution

- generated_at: 2026-05-30 13:08:58 Asia/Taipei
- latest_signal_count: 1217
- phase_mature_d5_count: 81
- phase_mature_d10_count: 41
- phase_mature_d20_count: 0

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 866.0 | 71.16 |
| tdcc_leading_price | 134.0 | 11.01 |
| tdcc_price_divergence | 106.0 | 8.71 |
| overheated_after_tdcc | 55.0 | 4.52 |
| price_leading_tdcc | 39.0 | 3.20 |
| tdcc_price_confirmed | 9.0 | 0.74 |
| failed_after_tdcc | 8.0 | 0.66 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 420.0 |
| 1 | overheated_after_tdcc | 15.0 |
| 1 | price_leading_tdcc | 14.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 183.0 |
| 2 | overheated_after_tdcc | 19.0 |
| 2 | price_leading_tdcc | 10.0 |
| 2 | tdcc_leading_price | 31.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 20.0 |
| 3 | insufficient_price_context | 104.0 |
| 3 | overheated_after_tdcc | 10.0 |
| 3 | price_leading_tdcc | 5.0 |
| 3 | tdcc_leading_price | 27.0 |
| 3 | tdcc_price_confirmed | 2.0 |
| 3 | tdcc_price_divergence | 20.0 |
| 4 | failed_after_tdcc | 5.0 |
| 4 | insufficient_price_context | 145.0 |
| 4 | overheated_after_tdcc | 10.0 |
| 4 | price_leading_tdcc | 10.0 |
| 4 | tdcc_leading_price | 61.0 |
| 4 | tdcc_price_confirmed | 5.0 |
| 4 | tdcc_price_divergence | 54.0 |
| 5 | insufficient_price_context | 4.0 |
| 5 | overheated_after_tdcc | 1.0 |
| 5 | tdcc_leading_price | 2.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 3.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 1.0 |
| 7 | insufficient_price_context | 7.0 |
| 7 | tdcc_leading_price | 10.0 |
| 7 | tdcc_price_divergence | 8.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 179.0 |
| all_thresholds_up | tdcc_leading_price | 134.0 |
| all_thresholds_up | tdcc_price_divergence | 106.0 |
| all_thresholds_up | overheated_after_tdcc | 55.0 |
| all_thresholds_up | price_leading_tdcc | 39.0 |
| all_thresholds_up | tdcc_price_confirmed | 9.0 |
| all_thresholds_up | failed_after_tdcc | 8.0 |
| high_thresholds_up | insufficient_price_context | 316.0 |
| high_thresholds_up | tdcc_leading_price | 134.0 |
| high_thresholds_up | tdcc_price_divergence | 106.0 |
| high_thresholds_up | overheated_after_tdcc | 55.0 |
| high_thresholds_up | price_leading_tdcc | 39.0 |
| high_thresholds_up | tdcc_price_confirmed | 9.0 |
| high_thresholds_up | failed_after_tdcc | 8.0 |
| over_800_or_above | insufficient_price_context | 555.0 |
| over_800_or_above | tdcc_leading_price | 134.0 |
| over_800_or_above | tdcc_price_divergence | 106.0 |
| over_800_or_above | overheated_after_tdcc | 55.0 |
| over_800_or_above | price_leading_tdcc | 39.0 |
| over_800_or_above | tdcc_price_confirmed | 9.0 |
| over_800_or_above | failed_after_tdcc | 8.0 |
| over_1000_only | insufficient_price_context | 91.0 |
| consecutive_2w | insufficient_price_context | 446.0 |
| consecutive_2w | tdcc_leading_price | 134.0 |
| consecutive_2w | tdcc_price_divergence | 106.0 |
| consecutive_2w | overheated_after_tdcc | 40.0 |
| consecutive_2w | price_leading_tdcc | 25.0 |
| consecutive_2w | tdcc_price_confirmed | 9.0 |
| consecutive_2w | failed_after_tdcc | 8.0 |
| consecutive_3w | insufficient_price_context | 263.0 |
| consecutive_3w | tdcc_leading_price | 103.0 |
| consecutive_3w | tdcc_price_divergence | 86.0 |
| consecutive_3w | overheated_after_tdcc | 21.0 |
| consecutive_3w | price_leading_tdcc | 15.0 |
| consecutive_3w | tdcc_price_confirmed | 7.0 |
| consecutive_3w | failed_after_tdcc | 6.0 |
| quiet_accumulation | insufficient_price_context | 91.0 |
| quiet_accumulation | tdcc_leading_price | 86.0 |
| quiet_accumulation | tdcc_price_divergence | 76.0 |
| quiet_accumulation | failed_after_tdcc | 5.0 |
| quiet_accumulation | price_leading_tdcc | 2.0 |
| quiet_accumulation | tdcc_price_confirmed | 1.0 |
| early_breakout | tdcc_leading_price | 2.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | insufficient_price_context | 26.0 |
| strong_momentum | price_leading_tdcc | 15.0 |
| strong_momentum | tdcc_leading_price | 6.0 |
| strong_momentum | tdcc_price_confirmed | 4.0 |
| strong_momentum | tdcc_price_divergence | 2.0 |
| strong_momentum | overheated_after_tdcc | 1.0 |
| overheated | overheated_after_tdcc | 55.0 |
| overheated | price_leading_tdcc | 17.0 |
| overheated | insufficient_price_context | 9.0 |

## Phase 後續成熟績效

- phase-level D+20 尚未成熟，不可做 phase 勝率結論。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 17.0 | 8.52 | 6.22 | 11.0 | 18.69 | 8.67 | 0.0 |  |  | 27.23 | -5.27 |
| overheated_after_tdcc | 39.0 | 9.05 | 7.27 | 16.0 | 24.13 | 15.66 | 0.0 |  |  | 31.28 | -6.01 |
| price_leading_tdcc | 16.0 | 7.13 | 4.93 | 8.0 | 13.39 | 10.33 | 0.0 |  |  | 21.08 | -7.07 |
| tdcc_leading_price | 6.0 | 4.11 | 0.78 | 5.0 | 3.11 | 4.43 | 0.0 |  |  | 11.62 | -5.94 |
| tdcc_price_confirmed | 2.0 | 5.29 |  | 0.0 |  |  | 0.0 |  |  |  |  |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 |  | 0.0 |  |  | 19.34 | -11.15 |
