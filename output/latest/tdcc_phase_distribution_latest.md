# TDCC Phase Distribution

- generated_at: 2026-08-01 15:47:49 Asia/Taipei
- latest_signal_count: 1135
- phase_mature_d5_count: 434
- phase_mature_d10_count: 351
- phase_mature_d20_count: 304

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 801.0 | 70.57 |
| price_leading_tdcc | 233.0 | 20.53 |
| tdcc_price_divergence | 87.0 | 7.67 |
| tdcc_leading_price | 13.0 | 1.15 |
| failed_after_tdcc | 1.0 | 0.09 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 380.0 |
| 1 | price_leading_tdcc | 42.0 |
| 10 | insufficient_price_context | 6.0 |
| 11 | insufficient_price_context | 7.0 |
| 11 | price_leading_tdcc | 5.0 |
| 12 | insufficient_price_context | 1.0 |
| 12 | price_leading_tdcc | 2.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 7.0 |
| 13 | price_leading_tdcc | 9.0 |
| 14 | price_leading_tdcc | 1.0 |
| 2 | failed_after_tdcc | 1.0 |
| 2 | insufficient_price_context | 180.0 |
| 2 | price_leading_tdcc | 48.0 |
| 2 | tdcc_leading_price | 3.0 |
| 2 | tdcc_price_divergence | 48.0 |
| 25 | price_leading_tdcc | 1.0 |
| 3 | insufficient_price_context | 95.0 |
| 3 | price_leading_tdcc | 33.0 |
| 3 | tdcc_leading_price | 2.0 |
| 3 | tdcc_price_divergence | 15.0 |
| 35 | insufficient_price_context | 1.0 |
| 4 | insufficient_price_context | 58.0 |
| 4 | price_leading_tdcc | 31.0 |
| 4 | tdcc_leading_price | 7.0 |
| 4 | tdcc_price_divergence | 9.0 |
| 5 | insufficient_price_context | 29.0 |
| 5 | price_leading_tdcc | 20.0 |
| 5 | tdcc_price_divergence | 4.0 |
| 6 | insufficient_price_context | 13.0 |
| 6 | price_leading_tdcc | 19.0 |
| 6 | tdcc_leading_price | 1.0 |
| 6 | tdcc_price_divergence | 5.0 |
| 7 | insufficient_price_context | 10.0 |
| 7 | price_leading_tdcc | 11.0 |
| 7 | tdcc_price_divergence | 5.0 |
| 8 | insufficient_price_context | 7.0 |
| 8 | price_leading_tdcc | 4.0 |
| 9 | insufficient_price_context | 7.0 |
| 9 | price_leading_tdcc | 7.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | price_leading_tdcc | 195.0 |
| all_thresholds_up | insufficient_price_context | 124.0 |
| all_thresholds_up | tdcc_price_divergence | 62.0 |
| all_thresholds_up | tdcc_leading_price | 10.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | price_leading_tdcc | 233.0 |
| high_thresholds_up | insufficient_price_context | 212.0 |
| high_thresholds_up | tdcc_price_divergence | 87.0 |
| high_thresholds_up | tdcc_leading_price | 13.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 470.0 |
| over_800_or_above | price_leading_tdcc | 233.0 |
| over_800_or_above | tdcc_price_divergence | 87.0 |
| over_800_or_above | tdcc_leading_price | 13.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | insufficient_price_context | 100.0 |
| consecutive_2w | insufficient_price_context | 421.0 |
| consecutive_2w | price_leading_tdcc | 191.0 |
| consecutive_2w | tdcc_price_divergence | 87.0 |
| consecutive_2w | tdcc_leading_price | 13.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 241.0 |
| consecutive_3w | price_leading_tdcc | 143.0 |
| consecutive_3w | tdcc_price_divergence | 39.0 |
| consecutive_3w | tdcc_leading_price | 10.0 |
| quiet_accumulation | price_leading_tdcc | 127.0 |
| quiet_accumulation | insufficient_price_context | 77.0 |
| quiet_accumulation | tdcc_price_divergence | 43.0 |
| quiet_accumulation | tdcc_leading_price | 10.0 |
| early_breakout | price_leading_tdcc | 3.0 |
| strong_momentum | price_leading_tdcc | 4.0 |
| overheated |  | 0.0 |

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
