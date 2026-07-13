# Revenue Unreacted Range Feature Contrast Audit

- generated_at: `2026-07-13 12:44:58 Asia/Taipei`
- status: `research_only_feature_contrast_not_promotion_ready`
- baseline: strong monthly revenue plus recent 23-day range/no-active-attack proxy; signal-date close confirmation, next trading day open entry, D+20 close exit, no stop.
- duplicate_control: same-stock 20-trading-day non-overlap; overlap_pair_count must be zero.
- anomaly_basis: primary metrics retain unresolved anomaly candidates; the candidate-exclusion basis is sensitivity-only and cannot replace primary performance.
- feature_method: every binary feature reports its hit rate in high-return and failure groups plus the feature subset's true win/neutral/failure/return metrics.
- combination_policy: this audit tests single features only. It does not stack conditions or claim a combination benefit.
- sample_policy: sample count is reported but is not used by itself to reject a feature.
- scope: monthly revenue only. Quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income remain out of scope until a formal shared point-in-time financial-statement layer exists.
- production_change: `none`

## Anomaly Check

| anomaly_exclusion_basis | accepted_trade_count | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | return_path_discontinuity_count_after_non_overlap | return_path_discontinuity_count_excluded | return_path_discontinuity_count_in_metric_sample | top1_abs_return_share_pct | top5_abs_return_share_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_unresolved_anomaly_candidates_sensitivity_only | 4144 | 152.5 | 8042 | 20260429 | -48.7869 | 1589 | 20260223 | 5 | 5 | 0 | 0.34 | 1.54 | 2.7145 | sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 4750 | 220.1893 | 4414 | 20250609 | -91.0164 | 4763 | 20250609 | 7 | 0 | 7 | 0.43 | 1.54 | 2.413 | blocked_pending_root_cause_anomaly_candidate_review |

## Baseline And Binary Feature Matrix

| feature_id | feature_family | feature_independence_status | equivalent_to_feature_id | feature_hit_count | high_return_feature_hit_rate_pct | failure_feature_hit_rate_pct | high_return_minus_failure_hit_rate_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | evidence_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_revenue_production_strong | baseline | baseline_not_applicable |  | 4750 |  |  |  | 29.94 | 18.76 | 51.31 | 2.94 | -0.35 | 23.87 | 29.41 | baseline_anchor |
| revenue_cumulative_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1769 | 36.86 | 38.12 | -1.26 | 29.51 | 17.98 | 52.52 | 2.61 | -0.63 | 23.63 | 31.66 | failure_associated_risk_feature_candidate |
| technical_macd_hist_gt0 | technical | distinct_observed_mask |  | 1957 | 41.27 | 42.76 | -1.49 | 29.33 | 17.42 | 53.24 | 2.4 | -0.9 | 23.91 | 31.02 | failure_associated_risk_feature_candidate |
| candle_bullish_attack | candle | distinct_observed_mask |  | 1715 | 34.66 | 36.44 | -1.78 | 28.57 | 19.65 | 51.78 | 2.55 | -0.39 | 22.92 | 29.8 | failure_associated_risk_feature_candidate |
| technical_kdj_j_ge100 | technical_risk | distinct_observed_mask |  | 149 | 1.76 | 3.73 | -1.97 | 17.45 | 21.48 | 61.07 | -1.08 | -2.68 | 13.42 | 34.23 | failure_associated_risk_feature_candidate |
| candle_solid_red | candle | distinct_observed_mask |  | 889 | 16.93 | 19.2 | -2.27 | 27.11 | 20.25 | 52.64 | 2.24 | -0.55 | 21.6 | 29.58 | failure_associated_risk_feature_candidate |
| market_mild_bull | market_regime | distinct_observed_mask |  | 1313 | 25.13 | 27.66 | -2.53 | 28.41 | 20.26 | 51.33 | 2.19 | -0.36 | 21.71 | 27.88 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1284 | 25.4 | 28.07 | -2.67 | 28.74 | 17.99 | 53.27 | 2.39 | -0.67 | 22.43 | 32.09 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_ge100 | monthly_revenue | distinct_observed_mask |  | 855 | 15.43 | 20.02 | -4.59 | 25.73 | 17.19 | 57.08 | 1.71 | -1.67 | 20.47 | 33.45 | failure_associated_risk_feature_candidate |
| market_strong_bull | market_regime | distinct_observed_mask |  | 2666 | 53.97 | 60.11 | -6.14 | 28.32 | 16.73 | 54.95 | 2.17 | -1.2 | 22.96 | 33.68 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_delta_ge20 | monthly_revenue | distinct_observed_mask |  | 1927 | 36.86 | 43.78 | -6.92 | 27.19 | 17.44 | 55.37 | 2.06 | -1.1 | 21.69 | 32.23 | failure_associated_risk_feature_candidate |
| shape_near_range23_high | price_shape | distinct_observed_mask |  | 1191 | 19.75 | 26.71 | -6.96 | 23.85 | 21.49 | 54.66 | 1.68 | -0.84 | 18.81 | 25.78 | failure_associated_risk_feature_candidate |
| shape_range23_width_le10 | price_shape | distinct_observed_mask |  | 752 | 8.55 | 16.66 | -8.11 | 17.95 | 28.06 | 53.99 | 0.48 | -0.39 | 12.9 | 19.02 | failure_associated_risk_feature_candidate |
| market_bull | market_regime | distinct_observed_mask |  | 3979 | 79.1 | 87.77 | -8.67 | 28.35 | 17.89 | 53.76 | 2.17 | -0.9 | 22.54 | 31.77 | failure_associated_risk_feature_candidate |
| technical_kdj_bullish_not_extreme | technical | distinct_observed_mask |  | 1911 | 33.95 | 44.28 | -10.33 | 25.12 | 18.42 | 56.46 | 1.14 | -1.43 | 20.15 | 33.02 | failure_associated_risk_feature_candidate |
| technical_kd_bullish_not_overheated | technical | distinct_observed_mask |  | 1891 | 32.54 | 44.52 | -11.98 | 24.38 | 18.24 | 57.38 | 0.89 | -1.65 | 19.51 | 34.0 | failure_associated_risk_feature_candidate |
| position120_low_le40 | price_position | distinct_observed_mask |  | 2126 | 33.95 | 47.07 | -13.12 | 24.18 | 21.87 | 53.95 | 0.96 | -0.84 | 18.11 | 28.55 | failure_associated_risk_feature_candidate |
| shape_range23_width_le15 | price_shape | distinct_observed_mask |  | 1692 | 22.49 | 36.97 | -14.48 | 21.28 | 25.47 | 53.25 | 0.97 | -0.48 | 15.07 | 23.58 | failure_associated_risk_feature_candidate |
| shape_range23_width_le20 | price_shape | distinct_observed_mask |  | 2533 | 39.59 | 54.86 | -15.27 | 23.61 | 23.61 | 52.78 | 1.45 | -0.48 | 17.73 | 25.7 | failure_associated_risk_feature_candidate |
| technical_close_above_ma20_ema23 | technical | distinct_observed_mask |  | 1867 | 44.8 | 39.6 | 5.2 | 32.3 | 16.01 | 51.69 | 3.74 | -0.53 | 27.21 | 31.49 | mixed_or_low_discrimination_research_only |
| revenue_latest30_and_cumulative20 | monthly_revenue | distinct_observed_mask |  | 2310 | 51.59 | 49.45 | 2.14 | 31.0 | 16.84 | 52.16 | 3.1 | -0.54 | 25.32 | 31.04 | mixed_or_low_discrimination_research_only |
| volume_ratio_le1_5 | volume | distinct_observed_mask |  | 4166 | 87.57 | 87.03 | 0.54 | 29.96 | 19.13 | 50.91 | 2.89 | -0.3 | 23.84 | 29.21 | mixed_or_low_discrimination_research_only |
| revenue_latest50_and_cumulative30 | monthly_revenue | distinct_observed_mask |  | 1346 | 30.07 | 29.59 | 0.48 | 30.24 | 16.2 | 53.57 | 3.03 | -0.87 | 25.33 | 33.06 | mixed_or_low_discrimination_research_only |
| volume_ratio_le2 | volume | distinct_observed_mask |  | 4552 | 95.5 | 95.73 | -0.23 | 29.86 | 18.89 | 51.25 | 2.89 | -0.34 | 23.79 | 29.31 | mixed_or_low_discrimination_research_only |
| market_range_bound | market_regime | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| market_unknown | market_regime_coverage | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| technical_ma20_above_ma60 | technical | distinct_observed_mask |  | 1840 | 47.8 | 35.58 | 12.22 | 36.41 | 16.47 | 47.12 | 5.05 | 0.73 | 29.46 | 28.91 | positive_discriminator_single_feature_candidate |
| technical_ema23_slope_positive | technical | distinct_observed_mask |  | 2187 | 54.94 | 44.52 | 10.42 | 34.61 | 15.78 | 49.61 | 4.42 | 0.1 | 28.49 | 30.64 | positive_discriminator_single_feature_candidate |
| momentum_return20_0_25 | price_momentum | distinct_observed_mask |  | 2479 | 59.96 | 50.8 | 9.16 | 33.52 | 16.54 | 49.94 | 4.07 | 0.0 | 27.43 | 30.54 | positive_discriminator_single_feature_candidate |
| position120_high_gt75 | price_position | distinct_observed_mask |  | 791 | 23.46 | 14.57 | 8.89 | 39.7 | 15.42 | 44.88 | 6.19 | 1.54 | 33.63 | 29.46 | positive_discriminator_single_feature_candidate |
| market_correction_or_high_risk | market_regime_risk | distinct_observed_mask |  | 771 | 20.9 | 12.23 | 8.67 | 38.13 | 23.22 | 38.65 | 6.91 | 2.08 | 30.74 | 17.25 | positive_discriminator_single_feature_candidate |
| technical_rsi14_ge60 | technical | distinct_observed_mask |  | 1093 | 28.92 | 21.99 | 6.93 | 35.77 | 15.19 | 49.04 | 4.73 | 0.25 | 30.01 | 29.37 | positive_discriminator_single_feature_candidate |
| position120_mid_40_75 | price_position | distinct_observed_mask |  | 1833 | 42.59 | 38.37 | 4.22 | 32.41 | 16.58 | 51.01 | 3.84 | -0.32 | 26.35 | 30.39 | positive_discriminator_single_feature_candidate |
| technical_obv_above_ma20 | technical | distinct_observed_mask |  | 2344 | 52.82 | 49.08 | 3.74 | 31.02 | 17.96 | 51.02 | 3.22 | -0.33 | 25.55 | 30.25 | positive_discriminator_single_feature_candidate |
| technical_bb_width_not_extreme | technical | distinct_observed_mask |  | 2244 | 50.0 | 46.49 | 3.51 | 31.24 | 18.27 | 50.49 | 3.27 | -0.18 | 25.27 | 29.95 | positive_discriminator_single_feature_candidate |
| tdcc_high_thresholds_up | tdcc | distinct_observed_mask |  | 296 | 8.11 | 4.92 | 3.19 | 40.88 | 18.58 | 40.54 | 5.01 | 2.06 | 31.08 | 26.69 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge1 | tdcc | distinct_observed_mask |  | 406 | 10.41 | 7.3 | 3.11 | 37.68 | 18.47 | 43.84 | 4.06 | 1.25 | 29.06 | 28.82 | positive_discriminator_single_feature_candidate |
| tdcc_all_thresholds_up | tdcc | distinct_observed_mask |  | 159 | 5.11 | 2.26 | 2.85 | 46.54 | 18.87 | 34.59 | 6.43 | 3.79 | 36.48 | 22.64 | positive_discriminator_single_feature_candidate |
| tdcc_four_thresholds_sync_up | tdcc | duplicate_mask_not_independent_evidence | tdcc_all_thresholds_up | 159 | 5.11 | 2.26 | 2.85 | 46.54 | 18.87 | 34.59 | 6.43 | 3.79 | 36.48 | 22.64 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge2 | tdcc | distinct_observed_mask |  | 250 | 6.61 | 4.06 | 2.55 | 40.8 | 19.6 | 39.6 | 4.98 | 2.12 | 30.0 | 25.6 | positive_discriminator_single_feature_candidate |
| technical_rsi14_40_70 | technical | distinct_observed_mask |  | 3092 | 67.55 | 65.0 | 2.55 | 30.89 | 17.88 | 51.23 | 3.35 | -0.32 | 24.77 | 29.85 | positive_discriminator_single_feature_candidate |

## Numeric High-Return Versus Failure Contrast

| feature_id | feature_family | high_return_feature_mean | high_return_feature_median | failure_feature_mean | failure_feature_median | high_return_minus_failure_feature_mean | high_return_minus_failure_feature_median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_latest_yoy_pct | monthly_revenue | 1073.93 | 41.31 | 3736.55 | 41.57 | -2662.62 | -0.26 |
| revenue_cumulative_yoy_pct | monthly_revenue | 279.21 | 32.95 | 2103.1 | 32.94 | -1823.89 | 0.01 |
| revenue_latest_yoy_delta_1m | monthly_revenue | -1108.47 | 6.47 | -812.89 | 13.1 | -295.58 | -6.63 |
| revenue_cumulative_yoy_delta_1m | monthly_revenue | 21.91 | 1.5 | -612.68 | 3.09 | 634.59 | -1.59 |
| range23_width_pct | price_shape | 28.92 | 23.97 | 23.86 | 18.4 | 5.06 | 5.57 |
| distance_to_range23_high_pct | price_shape | -11.14 | -10.15 | -10.07 | -8.63 | -1.07 | -1.52 |
| close_position_120d_pct | price_position | 51.58 | 56.67 | 43.13 | 42.65 | 8.45 | 14.02 |
| return_5d_pct | price_momentum | -1.57 | -1.11 | -0.68 | -0.16 | -0.89 | -0.95 |
| return_20d_pct | price_momentum | 3.19 | 2.94 | 0.73 | 0.0 | 2.46 | 2.94 |
| volume_ratio_prev20 | volume | 0.86 | 0.75 | 0.87 | 0.77 | -0.01 | -0.02 |
| rsi14 | technical | 50.86 | 52.19 | 48.09 | 48.53 | 2.77 | 3.66 |
| macd_hist | technical | -0.7 | -0.02 | -0.79 | -0.0 | 0.09 | -0.02 |
| kd_k_value | technical | 44.78 | 44.38 | 44.35 | 43.75 | 0.43 | 0.63 |
| kd_d_value | technical | 47.73 | 48.3 | 44.53 | 44.25 | 3.2 | 4.05 |
| kdj_j_value | technical | 38.89 | 36.5 | 43.99 | 43.92 | -5.1 | -7.42 |
| bb_width_pct | technical | 20.57 | 17.94 | 16.85 | 14.04 | 3.72 | 3.9 |
| ema23_slope_5d_pct | technical | 1.15 | 0.68 | 0.37 | 0.04 | 0.78 | 0.64 |
| distance_to_ema23_pct | technical | 0.67 | 0.64 | -0.13 | 0.0 | 0.8 | 0.64 |
| tdcc_consecutive_up_weeks | tdcc | 1.31 | 1.0 | 1.11 | 0.0 | 0.2 | 1.0 |
