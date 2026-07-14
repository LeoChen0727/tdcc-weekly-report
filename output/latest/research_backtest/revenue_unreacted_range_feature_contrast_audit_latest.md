# Revenue Unreacted Range Feature Contrast Audit

- generated_at: `2026-07-14 14:45:45 Asia/Taipei`
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
| excluding_unresolved_anomaly_candidates_sensitivity_only | 4151 | 152.5 | 8042 | 20260429 | -48.7869 | 1589 | 20260223 | 5 | 5 | 0 | 0.34 | 1.54 | 2.732 | sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 4762 | 220.1893 | 4414 | 20250609 | -91.0164 | 4763 | 20250609 | 7 | 0 | 7 | 0.43 | 1.53 | 2.4161 | blocked_pending_root_cause_anomaly_candidate_review |

## Baseline And Binary Feature Matrix

| feature_id | feature_family | feature_independence_status | equivalent_to_feature_id | feature_hit_count | high_return_feature_hit_rate_pct | failure_feature_hit_rate_pct | high_return_minus_failure_hit_rate_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | evidence_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_revenue_production_strong | baseline | baseline_not_applicable |  | 4762 |  |  |  | 29.97 | 18.75 | 51.28 | 2.94 | -0.35 | 23.88 | 29.42 | baseline_anchor |
| revenue_cumulative_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1772 | 36.85 | 38.08 | -1.23 | 29.57 | 17.95 | 52.48 | 2.6 | -0.63 | 23.65 | 31.66 | failure_associated_risk_feature_candidate |
| technical_macd_hist_gt0 | technical | distinct_observed_mask |  | 1959 | 41.16 | 42.75 | -1.59 | 29.3 | 17.41 | 53.29 | 2.39 | -0.92 | 23.89 | 31.04 | failure_associated_risk_feature_candidate |
| candle_bullish_attack | candle | distinct_observed_mask |  | 1719 | 34.56 | 36.45 | -1.89 | 28.56 | 19.66 | 51.77 | 2.54 | -0.39 | 22.86 | 29.84 | failure_associated_risk_feature_candidate |
| technical_kdj_j_ge100 | technical_risk | distinct_observed_mask |  | 149 | 1.76 | 3.73 | -1.97 | 17.45 | 21.48 | 61.07 | -1.08 | -2.68 | 13.42 | 34.23 | failure_associated_risk_feature_candidate |
| candle_solid_red | candle | distinct_observed_mask |  | 889 | 16.89 | 19.16 | -2.27 | 27.11 | 20.25 | 52.64 | 2.24 | -0.55 | 21.6 | 29.58 | failure_associated_risk_feature_candidate |
| market_mild_bull | market_regime | distinct_observed_mask |  | 1313 | 25.07 | 27.6 | -2.53 | 28.41 | 20.26 | 51.33 | 2.19 | -0.36 | 21.71 | 27.88 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1285 | 25.33 | 28.01 | -2.68 | 28.79 | 17.98 | 53.23 | 2.4 | -0.66 | 22.41 | 32.06 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_ge100 | monthly_revenue | distinct_observed_mask |  | 860 | 15.39 | 20.15 | -4.76 | 25.7 | 17.09 | 57.21 | 1.65 | -1.68 | 20.35 | 33.6 | failure_associated_risk_feature_candidate |
| market_strong_bull | market_regime | distinct_observed_mask |  | 2666 | 53.83 | 59.99 | -6.16 | 28.32 | 16.73 | 54.95 | 2.17 | -1.2 | 22.96 | 33.68 | failure_associated_risk_feature_candidate |
| shape_near_range23_high | price_shape | distinct_observed_mask |  | 1191 | 19.7 | 26.66 | -6.96 | 23.85 | 21.49 | 54.66 | 1.68 | -0.84 | 18.81 | 25.78 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_delta_ge20 | monthly_revenue | distinct_observed_mask |  | 1930 | 36.76 | 43.73 | -6.97 | 27.2 | 17.46 | 55.34 | 2.06 | -1.1 | 21.66 | 32.18 | failure_associated_risk_feature_candidate |
| shape_range23_width_le10 | price_shape | distinct_observed_mask |  | 752 | 8.53 | 16.63 | -8.1 | 17.95 | 28.06 | 53.99 | 0.48 | -0.39 | 12.9 | 19.02 | failure_associated_risk_feature_candidate |
| market_bull | market_regime | distinct_observed_mask |  | 3979 | 78.89 | 87.59 | -8.7 | 28.35 | 17.89 | 53.76 | 2.17 | -0.9 | 22.54 | 31.77 | failure_associated_risk_feature_candidate |
| technical_kdj_bullish_not_extreme | technical | distinct_observed_mask |  | 1915 | 33.95 | 44.27 | -10.32 | 25.17 | 18.38 | 56.45 | 1.14 | -1.43 | 20.16 | 33.05 | failure_associated_risk_feature_candidate |
| technical_kd_bullish_not_overheated | technical | distinct_observed_mask |  | 1895 | 32.54 | 44.51 | -11.97 | 24.43 | 18.21 | 57.36 | 0.89 | -1.65 | 19.53 | 34.04 | failure_associated_risk_feature_candidate |
| position120_low_le40 | price_position | distinct_observed_mask |  | 2132 | 33.95 | 47.09 | -13.14 | 24.2 | 21.86 | 53.94 | 0.95 | -0.84 | 18.11 | 28.61 | failure_associated_risk_feature_candidate |
| shape_range23_width_le15 | price_shape | distinct_observed_mask |  | 1692 | 22.43 | 36.9 | -14.47 | 21.28 | 25.47 | 53.25 | 0.97 | -0.48 | 15.07 | 23.58 | failure_associated_risk_feature_candidate |
| shape_range23_width_le20 | price_shape | distinct_observed_mask |  | 2533 | 39.49 | 54.75 | -15.26 | 23.61 | 23.61 | 52.78 | 1.45 | -0.48 | 17.73 | 25.7 | failure_associated_risk_feature_candidate |
| technical_close_above_ma20_ema23 | technical | distinct_observed_mask |  | 1870 | 44.77 | 39.6 | 5.17 | 32.3 | 15.99 | 51.71 | 3.75 | -0.54 | 27.22 | 31.5 | mixed_or_low_discrimination_research_only |
| revenue_latest30_and_cumulative20 | monthly_revenue | distinct_observed_mask |  | 2319 | 51.54 | 49.55 | 1.99 | 31.0 | 16.82 | 52.18 | 3.08 | -0.55 | 25.27 | 31.09 | mixed_or_low_discrimination_research_only |
| volume_ratio_le1_5 | volume | distinct_observed_mask |  | 4174 | 87.51 | 86.98 | 0.53 | 29.97 | 19.14 | 50.89 | 2.88 | -0.29 | 23.84 | 29.23 | mixed_or_low_discrimination_research_only |
| revenue_latest50_and_cumulative30 | monthly_revenue | distinct_observed_mask |  | 1353 | 30.08 | 29.69 | 0.39 | 30.3 | 16.11 | 53.58 | 3.0 | -0.88 | 25.28 | 33.11 | mixed_or_low_discrimination_research_only |
| volume_ratio_le2 | volume | distinct_observed_mask |  | 4562 | 95.43 | 95.7 | -0.27 | 29.88 | 18.9 | 51.23 | 2.89 | -0.34 | 23.78 | 29.31 | mixed_or_low_discrimination_research_only |
| market_range_bound | market_regime | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| market_unknown | market_regime_coverage | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| technical_ma20_above_ma60 | technical | distinct_observed_mask |  | 1848 | 47.93 | 35.59 | 12.34 | 36.47 | 16.5 | 47.02 | 5.07 | 0.79 | 29.49 | 28.84 | positive_discriminator_single_feature_candidate |
| technical_ema23_slope_positive | technical | distinct_observed_mask |  | 2192 | 54.97 | 44.51 | 10.46 | 34.67 | 15.74 | 49.59 | 4.43 | 0.11 | 28.51 | 30.61 | positive_discriminator_single_feature_candidate |
| momentum_return20_0_25 | price_momentum | distinct_observed_mask |  | 2486 | 59.98 | 50.82 | 9.16 | 33.55 | 16.53 | 49.92 | 4.07 | 0.0 | 27.43 | 30.53 | positive_discriminator_single_feature_candidate |
| position120_high_gt75 | price_position | distinct_observed_mask |  | 793 | 23.48 | 14.54 | 8.94 | 39.85 | 15.38 | 44.77 | 6.2 | 1.57 | 33.67 | 29.38 | positive_discriminator_single_feature_candidate |
| market_correction_or_high_risk | market_regime_risk | distinct_observed_mask |  | 783 | 21.11 | 12.41 | 8.7 | 38.19 | 23.12 | 38.7 | 6.85 | 2.12 | 30.65 | 17.5 | positive_discriminator_single_feature_candidate |
| technical_rsi14_ge60 | technical | distinct_observed_mask |  | 1094 | 28.85 | 21.99 | 6.86 | 35.74 | 15.17 | 49.09 | 4.72 | 0.24 | 29.98 | 29.34 | positive_discriminator_single_feature_candidate |
| position120_mid_40_75 | price_position | distinct_observed_mask |  | 1837 | 42.57 | 38.37 | 4.2 | 32.39 | 16.6 | 51.01 | 3.86 | -0.32 | 26.35 | 30.38 | positive_discriminator_single_feature_candidate |
| technical_obv_above_ma20 | technical | distinct_observed_mask |  | 2349 | 52.77 | 49.02 | 3.75 | 31.08 | 17.97 | 50.96 | 3.23 | -0.32 | 25.54 | 30.18 | positive_discriminator_single_feature_candidate |
| technical_bb_width_not_extreme | technical | distinct_observed_mask |  | 2250 | 50.04 | 46.44 | 3.6 | 31.33 | 18.27 | 50.4 | 3.29 | -0.15 | 25.29 | 29.91 | positive_discriminator_single_feature_candidate |
| tdcc_high_thresholds_up | tdcc | distinct_observed_mask |  | 298 | 8.09 | 4.91 | 3.18 | 41.28 | 18.46 | 40.27 | 5.02 | 2.25 | 30.87 | 26.51 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge1 | tdcc | distinct_observed_mask |  | 410 | 10.47 | 7.33 | 3.14 | 38.05 | 18.29 | 43.66 | 4.06 | 1.31 | 29.02 | 28.78 | positive_discriminator_single_feature_candidate |
| tdcc_all_thresholds_up | tdcc | distinct_observed_mask |  | 159 | 5.1 | 2.25 | 2.85 | 46.54 | 18.87 | 34.59 | 6.43 | 3.79 | 36.48 | 22.64 | positive_discriminator_single_feature_candidate |
| tdcc_four_thresholds_sync_up | tdcc | duplicate_mask_not_independent_evidence | tdcc_all_thresholds_up | 159 | 5.1 | 2.25 | 2.85 | 46.54 | 18.87 | 34.59 | 6.43 | 3.79 | 36.48 | 22.64 | positive_discriminator_single_feature_candidate |
| technical_rsi14_40_70 | technical | distinct_observed_mask |  | 3098 | 67.55 | 64.95 | 2.6 | 30.96 | 17.85 | 51.19 | 3.36 | -0.31 | 24.79 | 29.83 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge2 | tdcc | distinct_observed_mask |  | 254 | 6.68 | 4.1 | 2.58 | 41.34 | 19.29 | 39.37 | 4.97 | 2.35 | 29.92 | 25.59 | positive_discriminator_single_feature_candidate |

## Numeric High-Return Versus Failure Contrast

| feature_id | feature_family | high_return_feature_mean | high_return_feature_median | failure_feature_mean | failure_feature_median | high_return_minus_failure_feature_mean | high_return_minus_failure_feature_median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_latest_yoy_pct | monthly_revenue | 1071.13 | 41.29 | 3741.73 | 41.59 | -2670.6 | -0.3 |
| revenue_cumulative_yoy_pct | monthly_revenue | 278.55 | 32.89 | 2114.33 | 33.02 | -1835.78 | -0.13 |
| revenue_latest_yoy_delta_1m | monthly_revenue | -1105.61 | 6.44 | -833.8 | 12.94 | -271.81 | -6.5 |
| revenue_cumulative_yoy_delta_1m | monthly_revenue | 21.83 | 1.5 | -612.26 | 3.09 | 634.09 | -1.59 |
| range23_width_pct | price_shape | 28.97 | 24.04 | 23.98 | 18.46 | 4.99 | 5.58 |
| distance_to_range23_high_pct | price_shape | -11.16 | -10.16 | -10.1 | -8.66 | -1.06 | -1.5 |
| close_position_120d_pct | price_position | 51.61 | 56.68 | 43.12 | 42.63 | 8.49 | 14.05 |
| return_5d_pct | price_momentum | -1.58 | -1.13 | -0.7 | -0.17 | -0.88 | -0.96 |
| return_20d_pct | price_momentum | 3.18 | 2.95 | 0.73 | 0.0 | 2.45 | 2.95 |
| volume_ratio_prev20 | volume | 0.86 | 0.75 | 0.87 | 0.77 | -0.01 | -0.02 |
| rsi14 | technical | 50.84 | 52.15 | 48.08 | 48.52 | 2.76 | 3.63 |
| macd_hist | technical | -0.71 | -0.02 | -0.79 | -0.0 | 0.08 | -0.02 |
| kd_k_value | technical | 44.75 | 44.32 | 44.33 | 43.74 | 0.42 | 0.58 |
| kd_d_value | technical | 47.7 | 48.29 | 44.52 | 44.25 | 3.18 | 4.04 |
| kdj_j_value | technical | 38.85 | 36.44 | 43.96 | 43.84 | -5.11 | -7.4 |
| bb_width_pct | technical | 20.59 | 17.95 | 16.92 | 14.05 | 3.67 | 3.9 |
| ema23_slope_5d_pct | technical | 1.14 | 0.68 | 0.36 | 0.04 | 0.78 | 0.64 |
| distance_to_ema23_pct | technical | 0.66 | 0.65 | -0.15 | -0.0 | 0.81 | 0.65 |
| tdcc_consecutive_up_weeks | tdcc | 1.3 | 1.0 | 1.11 | 0.0 | 0.19 | 1.0 |
