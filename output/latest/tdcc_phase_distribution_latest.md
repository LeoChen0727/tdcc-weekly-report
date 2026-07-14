# TDCC Phase Distribution

- generated_at: 2026-07-14 09:49:21 Asia/Taipei
- latest_signal_count: 64
- phase_mature_d5_count: 11553
- phase_mature_d10_count: 10420
- phase_mature_d20_count: 7121

## Phase 分布

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 30.0 | 46.88 |
| tdcc_leading_price | 20.0 | 31.25 |
| tdcc_price_divergence | 8.0 | 12.50 |
| price_leading_tdcc | 3.0 | 4.69 |
| overheated_after_tdcc | 2.0 | 3.12 |
| failed_after_tdcc | 1.0 | 1.56 |

## 連續週數 x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 2 | insufficient_price_context | 2.0 |
| 3 | failed_after_tdcc | 1.0 |
| 3 | insufficient_price_context | 28.0 |
| 3 | overheated_after_tdcc | 2.0 |
| 3 | price_leading_tdcc | 3.0 |
| 3 | tdcc_leading_price | 20.0 |
| 3 | tdcc_price_divergence | 8.0 |

## TDCC 條件 x Phase

| condition_name | tdcc_price_phase | signal_count |
| --- | --- | --- |
| all_thresholds_up | insufficient_price_context | 19.0 |
| all_thresholds_up | tdcc_leading_price | 12.0 |
| all_thresholds_up | tdcc_price_divergence | 5.0 |
| all_thresholds_up | price_leading_tdcc | 3.0 |
| all_thresholds_up | overheated_after_tdcc | 2.0 |
| all_thresholds_up | failed_after_tdcc | 1.0 |
| high_thresholds_up | insufficient_price_context | 23.0 |
| high_thresholds_up | tdcc_leading_price | 14.0 |
| high_thresholds_up | tdcc_price_divergence | 6.0 |
| high_thresholds_up | price_leading_tdcc | 3.0 |
| high_thresholds_up | overheated_after_tdcc | 2.0 |
| high_thresholds_up | failed_after_tdcc | 1.0 |
| over_800_or_above | insufficient_price_context | 25.0 |
| over_800_or_above | tdcc_leading_price | 18.0 |
| over_800_or_above | tdcc_price_divergence | 7.0 |
| over_800_or_above | price_leading_tdcc | 3.0 |
| over_800_or_above | overheated_after_tdcc | 2.0 |
| over_800_or_above | failed_after_tdcc | 1.0 |
| over_1000_only | tdcc_leading_price | 2.0 |
| over_1000_only | insufficient_price_context | 2.0 |
| over_1000_only | tdcc_price_divergence | 1.0 |
| consecutive_2w | insufficient_price_context | 30.0 |
| consecutive_2w | tdcc_leading_price | 20.0 |
| consecutive_2w | tdcc_price_divergence | 8.0 |
| consecutive_2w | price_leading_tdcc | 3.0 |
| consecutive_2w | overheated_after_tdcc | 2.0 |
| consecutive_2w | failed_after_tdcc | 1.0 |
| consecutive_3w | insufficient_price_context | 28.0 |
| consecutive_3w | tdcc_leading_price | 20.0 |
| consecutive_3w | tdcc_price_divergence | 8.0 |
| consecutive_3w | price_leading_tdcc | 3.0 |
| consecutive_3w | overheated_after_tdcc | 2.0 |
| consecutive_3w | failed_after_tdcc | 1.0 |
| quiet_accumulation | insufficient_price_context | 23.0 |
| quiet_accumulation | tdcc_leading_price | 14.0 |
| quiet_accumulation | tdcc_price_divergence | 6.0 |
| quiet_accumulation | price_leading_tdcc | 1.0 |
| quiet_accumulation | failed_after_tdcc | 1.0 |
| early_breakout |  | 0.0 |
| strong_momentum | price_leading_tdcc | 2.0 |
| overheated | overheated_after_tdcc | 2.0 |

## Phase 後續成熟績效



| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 31.0 | -0.15 | -1.05 | 24.0 | 2.09 | -2.34 | 21.0 | 0.04 | -6.14 | 8.50 | -5.23 |
| insufficient_price_context | 7805.0 | 0.67 | -0.84 | 7280.0 | 1.79 | -0.50 | 4647.0 | 4.02 | -1.42 | 9.11 | -5.52 |
| overheated_after_tdcc | 436.0 | 2.27 | 1.90 | 369.0 | 7.39 | 4.68 | 268.0 | 13.96 | 8.96 | 19.96 | -9.53 |
| price_leading_tdcc | 596.0 | 2.99 | 0.83 | 508.0 | 4.73 | 1.79 | 276.0 | 7.36 | 1.01 | 16.83 | -6.63 |
| tdcc_leading_price | 1191.0 | 0.16 | 0.01 | 988.0 | 1.33 | -2.44 | 867.0 | 1.63 | -3.56 | 6.30 | -4.48 |
| tdcc_price_confirmed | 98.0 | 0.35 | 0.24 | 87.0 | 0.57 | -3.39 | 72.0 | 1.54 | -3.88 | 9.61 | -6.98 |
| tdcc_price_divergence | 1396.0 | 0.00 | -0.34 | 1164.0 | 1.37 | -2.96 | 970.0 | 1.94 | -3.99 | 6.87 | -4.41 |
