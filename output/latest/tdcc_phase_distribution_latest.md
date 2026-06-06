# TDCC Phase Distribution

- generated_at: 2026-06-06 15:42:29 Asia/Taipei
- latest_signal_count: 1130
- phase_mature_d5_count: 119
- phase_mature_d10_count: 82
- phase_mature_d20_count: 0

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 792.0 | 70.09 |
| tdcc_leading_price | 154.0 | 13.63 |
| tdcc_price_divergence | 89.0 | 7.88 |
| price_leading_tdcc | 49.0 | 4.34 |
| overheated_after_tdcc | 28.0 | 2.48 |
| tdcc_price_confirmed | 17.0 | 1.50 |
| failed_after_tdcc | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 368.0 |
| 1 | overheated_after_tdcc | 7.0 |
| 1 | price_leading_tdcc | 15.0 |
| 2 | insufficient_price_context | 165.0 |
| 2 | overheated_after_tdcc | 10.0 |
| 2 | price_leading_tdcc | 13.0 |
| 2 | tdcc_leading_price | 44.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 25.0 |
| 3 | insufficient_price_context | 101.0 |
| 3 | overheated_after_tdcc | 6.0 |
| 3 | price_leading_tdcc | 10.0 |
| 3 | tdcc_leading_price | 26.0 |
| 3 | tdcc_price_confirmed | 6.0 |
| 3 | tdcc_price_divergence | 15.0 |
| 4 | insufficient_price_context | 58.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 6.0 |
| 4 | tdcc_leading_price | 16.0 |
| 4 | tdcc_price_divergence | 11.0 |
| 5 | failed_after_tdcc | 1.0 |
| 5 | insufficient_price_context | 87.0 |
| 5 | overheated_after_tdcc | 3.0 |
| 5 | price_leading_tdcc | 5.0 |
| 5 | tdcc_leading_price | 55.0 |
| 5 | tdcc_price_confirmed | 8.0 |
| 5 | tdcc_price_divergence | 31.0 |
| 6 | insufficient_price_context | 4.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 2.0 |
| 7 | insufficient_price_context | 9.0 |
| 7 | tdcc_leading_price | 10.0 |
| 7 | tdcc_price_confirmed | 1.0 |
| 7 | tdcc_price_divergence | 5.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 154.0 |
| all_thresholds_up | tdcc_leading_price | 151.0 |
| all_thresholds_up | tdcc_price_divergence | 85.0 |
| all_thresholds_up | price_leading_tdcc | 47.0 |
| all_thresholds_up | overheated_after_tdcc | 27.0 |
| all_thresholds_up | tdcc_price_confirmed | 17.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | insufficient_price_context | 279.0 |
| high_thresholds_up | tdcc_leading_price | 154.0 |
| high_thresholds_up | tdcc_price_divergence | 89.0 |
| high_thresholds_up | price_leading_tdcc | 49.0 |
| high_thresholds_up | overheated_after_tdcc | 28.0 |
| high_thresholds_up | tdcc_price_confirmed | 17.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 510.0 |
| over_800_or_above | tdcc_leading_price | 154.0 |
| over_800_or_above | tdcc_price_divergence | 89.0 |
| over_800_or_above | price_leading_tdcc | 49.0 |
| over_800_or_above | overheated_after_tdcc | 28.0 |
| over_800_or_above | tdcc_price_confirmed | 17.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | insufficient_price_context | 78.0 |
| consecutive_2w | insufficient_price_context | 424.0 |
| consecutive_2w | tdcc_leading_price | 154.0 |
| consecutive_2w | tdcc_price_divergence | 89.0 |
| consecutive_2w | price_leading_tdcc | 34.0 |
| consecutive_2w | overheated_after_tdcc | 21.0 |
| consecutive_2w | tdcc_price_confirmed | 17.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 259.0 |
| consecutive_3w | tdcc_leading_price | 110.0 |
| consecutive_3w | tdcc_price_divergence | 64.0 |
| consecutive_3w | price_leading_tdcc | 21.0 |
| consecutive_3w | tdcc_price_confirmed | 15.0 |
| consecutive_3w | overheated_after_tdcc | 11.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | tdcc_leading_price | 99.0 |
| quiet_accumulation | insufficient_price_context | 69.0 |
| quiet_accumulation | tdcc_price_divergence | 60.0 |
| quiet_accumulation | tdcc_price_confirmed | 1.0 |
| quiet_accumulation | price_leading_tdcc | 1.0 |
| early_breakout | tdcc_leading_price | 3.0 |
| early_breakout | tdcc_price_confirmed | 1.0 |
| early_breakout | insufficient_price_context | 1.0 |
| strong_momentum | price_leading_tdcc | 17.0 |
| strong_momentum | insufficient_price_context | 9.0 |
| strong_momentum | tdcc_price_confirmed | 7.0 |
| strong_momentum | tdcc_leading_price | 6.0 |
| strong_momentum | tdcc_price_divergence | 3.0 |
| overheated | overheated_after_tdcc | 28.0 |
| overheated | price_leading_tdcc | 19.0 |
| overheated | insufficient_price_context | 7.0 |
| overheated | tdcc_leading_price | 3.0 |

## Phase 後續成熟績效

- phase-level D+20 尚未成熟，不可做 phase 勝率結論。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 26.0 | 5.21 | 3.03 | 18.0 | 14.38 | 7.79 | 0.0 |  |  | 24.57 | -6.95 |
| overheated_after_tdcc | 57.0 | 5.54 | 2.72 | 39.0 | 16.22 | 10.14 | 0.0 |  |  | 24.48 | -6.54 |
| price_leading_tdcc | 26.0 | 6.24 | 4.19 | 16.0 | 9.09 | 3.09 | 0.0 |  |  | 19.56 | -5.94 |
| tdcc_leading_price | 7.0 | 4.36 | 1.40 | 6.0 | 2.15 | -5.78 | 0.0 |  |  | 11.42 | -5.64 |
| tdcc_price_confirmed | 2.0 | 5.29 | 0.47 | 2.0 | 21.87 | 20.03 | 0.0 |  |  | 23.17 | -3.99 |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 | 11.44 | 0.0 |  |  | 19.34 | -11.15 |
