# Revenue Unreacted Range Feature Contrast Audit

- generated_at: `2026-07-12 17:22:35 Asia/Taipei`
- status: `research_only_feature_contrast_not_promotion_ready`
- baseline: strong monthly revenue plus recent 23-day range/no-active-attack proxy; signal-date close confirmation, next trading day open entry, D+20 close exit, no stop.
- duplicate_control: same-stock 20-trading-day non-overlap; overlap_pair_count must be zero.
- anomaly_basis: both including known anomalies and excluding known revenue/price anomalies are published; only the excluding basis may support interpretation after the return-dominance audit passes.
- feature_method: every binary feature reports its hit rate in high-return and failure groups plus the feature subset's true win/neutral/failure/return metrics.
- combination_policy: this audit tests single features only. It does not stack conditions or claim a combination benefit.
- sample_policy: sample count is reported but is not used by itself to reject a feature.
- scope: monthly revenue only. Quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income remain out of scope until a formal shared point-in-time financial-statement layer exists.
- production_change: `none`

## Anomaly Check

| anomaly_exclusion_basis | accepted_trade_count | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | return_path_discontinuity_count_after_non_overlap | return_path_discontinuity_count_excluded | return_path_discontinuity_count_in_metric_sample | top1_abs_return_share_pct | top5_abs_return_share_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_known_revenue_and_price_anomalies | 4144 | 152.5 | 8042 | 20260429 | -48.7869 | 1589 | 20260223 | 5 | 5 | 0 | 0.34 | 1.54 | 2.7145 | anomaly_check_pass |
| including_known_anomalies | 4750 | 220.1893 | 4414 | 20250609 | -91.0164 | 4763 | 20250609 | 7 | 0 | 7 | 0.43 | 1.54 | 2.413 | not_decision_basis_known_anomalies_included |

## Baseline And Binary Feature Matrix

| feature_id | feature_family | feature_independence_status | equivalent_to_feature_id | feature_hit_count | high_return_feature_hit_rate_pct | failure_feature_hit_rate_pct | high_return_minus_failure_hit_rate_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | evidence_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_revenue_production_strong | baseline | baseline_not_applicable |  | 4144 |  |  |  | 31.23 | 18.58 | 50.19 | 3.27 | -0.12 | 24.95 | 28.69 | baseline_anchor |
| volume_ratio_le2 | volume | distinct_observed_mask |  | 3975 | 95.26 | 96.01 | -0.75 | 31.02 | 18.74 | 50.24 | 3.2 | -0.13 | 24.78 | 28.6 | failure_associated_risk_feature_candidate |
| technical_macd_hist_gt0 | technical | distinct_observed_mask |  | 1725 | 41.88 | 43.12 | -1.24 | 30.78 | 17.22 | 52.0 | 2.92 | -0.67 | 25.1 | 30.03 | failure_associated_risk_feature_candidate |
| candle_bullish_attack | candle | distinct_observed_mask |  | 1500 | 35.01 | 36.25 | -1.24 | 30.2 | 19.53 | 50.27 | 3.02 | -0.14 | 24.13 | 29.0 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_ge100 | monthly_revenue | distinct_observed_mask |  | 425 | 9.57 | 10.96 | -1.39 | 30.12 | 16.24 | 53.65 | 2.86 | -0.94 | 23.29 | 31.53 | failure_associated_risk_feature_candidate |
| revenue_cumulative_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1541 | 36.27 | 37.93 | -1.66 | 30.63 | 18.17 | 51.2 | 2.87 | -0.34 | 24.33 | 31.15 | failure_associated_risk_feature_candidate |
| candle_solid_red | candle | distinct_observed_mask |  | 779 | 17.31 | 18.99 | -1.68 | 28.88 | 20.41 | 50.71 | 2.71 | -0.33 | 22.98 | 28.37 | failure_associated_risk_feature_candidate |
| technical_kdj_j_ge100 | technical_risk | distinct_observed_mask |  | 136 | 1.93 | 3.89 | -1.96 | 19.12 | 21.32 | 59.56 | -0.73 | -2.24 | 14.71 | 33.09 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1132 | 25.44 | 28.46 | -3.02 | 29.59 | 18.11 | 52.3 | 2.63 | -0.42 | 23.23 | 31.1 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_delta_ge20 | monthly_revenue | distinct_observed_mask |  | 1606 | 35.3 | 41.73 | -6.43 | 28.52 | 17.43 | 54.05 | 2.41 | -0.78 | 22.73 | 31.01 | failure_associated_risk_feature_candidate |
| shape_near_range23_high | price_shape | distinct_observed_mask |  | 1058 | 20.12 | 27.31 | -7.19 | 24.95 | 21.36 | 53.69 | 2.16 | -0.62 | 19.66 | 25.61 | failure_associated_risk_feature_candidate |
| market_strong_bull | market_regime | distinct_observed_mask |  | 2327 | 53.68 | 61.01 | -7.33 | 29.27 | 16.2 | 54.53 | 2.44 | -1.16 | 23.85 | 33.35 | failure_associated_risk_feature_candidate |
| market_bull | market_regime | distinct_observed_mask |  | 3463 | 79.21 | 87.88 | -8.67 | 29.63 | 17.59 | 52.79 | 2.52 | -0.76 | 23.65 | 31.16 | failure_associated_risk_feature_candidate |
| shape_range23_width_le10 | price_shape | distinct_observed_mask |  | 652 | 7.93 | 16.73 | -8.8 | 17.94 | 28.68 | 53.37 | 0.6 | -0.38 | 12.58 | 18.4 | failure_associated_risk_feature_candidate |
| technical_kdj_bullish_not_extreme | technical | distinct_observed_mask |  | 1672 | 34.53 | 44.71 | -10.18 | 26.08 | 18.3 | 55.62 | 1.58 | -1.28 | 21.35 | 32.6 | failure_associated_risk_feature_candidate |
| position120_low_le40 | price_position | distinct_observed_mask |  | 1766 | 32.69 | 44.62 | -11.93 | 25.2 | 22.25 | 52.55 | 1.23 | -0.56 | 19.14 | 27.52 | failure_associated_risk_feature_candidate |
| technical_kd_bullish_not_overheated | technical | distinct_observed_mask |  | 1657 | 33.17 | 45.14 | -11.97 | 25.35 | 17.98 | 56.67 | 1.3 | -1.52 | 20.7 | 33.55 | failure_associated_risk_feature_candidate |
| shape_range23_width_le15 | price_shape | distinct_observed_mask |  | 1454 | 21.66 | 36.92 | -15.26 | 21.66 | 25.52 | 52.82 | 1.16 | -0.42 | 15.41 | 22.97 | failure_associated_risk_feature_candidate |
| shape_range23_width_le20 | price_shape | distinct_observed_mask |  | 2183 | 38.39 | 54.86 | -16.47 | 23.96 | 23.77 | 52.27 | 1.56 | -0.41 | 18.19 | 25.19 | failure_associated_risk_feature_candidate |
| technical_close_above_ma20_ema23 | technical | distinct_observed_mask |  | 1692 | 46.32 | 41.11 | 5.21 | 33.87 | 15.6 | 50.53 | 4.14 | -0.3 | 28.31 | 30.97 | mixed_or_low_discrimination_research_only |
| position120_mid_40_75 | price_position | distinct_observed_mask |  | 1654 | 42.84 | 40.05 | 2.79 | 33.13 | 16.51 | 50.36 | 3.91 | -0.19 | 26.78 | 29.87 | mixed_or_low_discrimination_research_only |
| technical_rsi14_40_70 | technical | distinct_observed_mask |  | 2728 | 68.09 | 65.96 | 2.13 | 32.18 | 17.52 | 50.29 | 3.6 | -0.13 | 25.81 | 29.29 | mixed_or_low_discrimination_research_only |
| volume_ratio_le1_5 | volume | distinct_observed_mask |  | 3643 | 87.33 | 87.31 | 0.02 | 31.07 | 19.08 | 49.85 | 3.19 | 0.0 | 24.79 | 28.55 | mixed_or_low_discrimination_research_only |
| market_mild_bull | market_regime | distinct_observed_mask |  | 1136 | 25.53 | 26.88 | -1.35 | 30.37 | 20.42 | 49.21 | 2.7 | 0.0 | 23.24 | 26.67 | mixed_or_low_discrimination_research_only |
| market_range_bound | market_regime | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| market_unknown | market_regime_coverage | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| technical_ema23_slope_positive | technical | distinct_observed_mask |  | 1973 | 56.67 | 45.67 | 11.0 | 36.34 | 15.51 | 48.15 | 4.85 | 0.43 | 29.7 | 29.7 | positive_discriminator_single_feature_candidate |
| technical_ma20_above_ma60 | technical | distinct_observed_mask |  | 1649 | 47.97 | 37.07 | 10.9 | 37.42 | 15.83 | 46.76 | 5.14 | 1.07 | 30.08 | 28.74 | positive_discriminator_single_feature_candidate |
| momentum_return20_0_25 | price_momentum | distinct_observed_mask |  | 2221 | 61.32 | 51.88 | 9.44 | 35.03 | 16.39 | 48.58 | 4.45 | 0.29 | 28.55 | 29.76 | positive_discriminator_single_feature_candidate |
| position120_high_gt75 | price_position | distinct_observed_mask |  | 724 | 24.47 | 15.34 | 9.13 | 41.57 | 14.36 | 44.06 | 6.79 | 1.81 | 34.94 | 28.87 | positive_discriminator_single_feature_candidate |
| market_correction_or_high_risk | market_regime_risk | distinct_observed_mask |  | 681 | 20.79 | 12.12 | 8.67 | 39.35 | 23.64 | 37.0 | 7.08 | 2.44 | 31.57 | 16.15 | positive_discriminator_single_feature_candidate |
| technical_rsi14_ge60 | technical | distinct_observed_mask |  | 996 | 30.37 | 22.6 | 7.77 | 37.85 | 14.96 | 47.19 | 5.25 | 0.95 | 31.53 | 28.31 | positive_discriminator_single_feature_candidate |
| technical_obv_above_ma20 | technical | distinct_observed_mask |  | 2072 | 53.87 | 49.28 | 4.59 | 32.77 | 17.76 | 49.47 | 3.75 | 0.0 | 26.88 | 29.49 | positive_discriminator_single_feature_candidate |
| revenue_latest30_and_cumulative20 | monthly_revenue | distinct_observed_mask |  | 1895 | 49.81 | 45.53 | 4.28 | 33.19 | 16.83 | 49.97 | 3.83 | 0.0 | 27.18 | 30.03 | positive_discriminator_single_feature_candidate |
| revenue_latest50_and_cumulative30 | monthly_revenue | distinct_observed_mask |  | 946 | 26.4 | 22.69 | 3.71 | 34.36 | 15.75 | 49.89 | 4.47 | 0.0 | 28.86 | 31.92 | positive_discriminator_single_feature_candidate |
| tdcc_high_thresholds_up | tdcc | distinct_observed_mask |  | 242 | 7.54 | 4.76 | 2.78 | 43.39 | 15.7 | 40.91 | 5.01 | 3.02 | 32.23 | 28.51 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge1 | tdcc | distinct_observed_mask |  | 335 | 9.67 | 7.07 | 2.6 | 39.4 | 16.72 | 43.88 | 4.11 | 1.43 | 29.85 | 29.85 | positive_discriminator_single_feature_candidate |
| tdcc_all_thresholds_up | tdcc | distinct_observed_mask |  | 125 | 4.55 | 2.02 | 2.53 | 49.6 | 16.8 | 33.6 | 6.99 | 4.47 | 37.6 | 23.2 | positive_discriminator_single_feature_candidate |
| tdcc_four_thresholds_sync_up | tdcc | duplicate_mask_not_independent_evidence | tdcc_all_thresholds_up | 125 | 4.55 | 2.02 | 2.53 | 49.6 | 16.8 | 33.6 | 6.99 | 4.47 | 37.6 | 23.2 | positive_discriminator_single_feature_candidate |
| technical_bb_width_not_extreme | technical | distinct_observed_mask |  | 1957 | 49.42 | 46.92 | 2.5 | 32.09 | 18.04 | 49.87 | 3.45 | 0.0 | 26.11 | 29.54 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge2 | tdcc | distinct_observed_mask |  | 201 | 6.0 | 3.85 | 2.15 | 42.79 | 17.41 | 39.8 | 5.28 | 2.78 | 30.85 | 26.87 | positive_discriminator_single_feature_candidate |

## Numeric High-Return Versus Failure Contrast

| feature_id | feature_family | high_return_feature_mean | high_return_feature_median | failure_feature_mean | failure_feature_median | high_return_minus_failure_feature_mean | high_return_minus_failure_feature_median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_latest_yoy_pct | monthly_revenue | 47.94 | 39.3 | 49.06 | 37.77 | -1.12 | 1.53 |
| revenue_cumulative_yoy_pct | monthly_revenue | 40.73 | 31.02 | 38.83 | 29.79 | 1.9 | 1.23 |
| revenue_latest_yoy_delta_1m | monthly_revenue | 7.02 | 6.18 | 16.38 | 11.82 | -9.36 | -5.64 |
| revenue_cumulative_yoy_delta_1m | monthly_revenue | 2.92 | 1.3 | 8.56 | 2.8 | -5.64 | -1.5 |
| range23_width_pct | price_shape | 28.66 | 24.06 | 23.59 | 18.37 | 5.07 | 5.69 |
| distance_to_range23_high_pct | price_shape | -10.95 | -10.06 | -9.84 | -8.48 | -1.11 | -1.58 |
| close_position_120d_pct | price_position | 52.43 | 57.32 | 44.56 | 45.13 | 7.87 | 12.19 |
| return_5d_pct | price_momentum | -1.43 | -0.99 | -0.6 | 0.0 | -0.83 | -0.99 |
| return_20d_pct | price_momentum | 3.34 | 3.06 | 1.01 | 0.3 | 2.33 | 2.76 |
| volume_ratio_prev20 | volume | 0.87 | 0.76 | 0.87 | 0.77 | 0.0 | -0.01 |
| rsi14 | technical | 51.2 | 52.56 | 48.5 | 48.84 | 2.7 | 3.72 |
| macd_hist | technical | -0.69 | -0.02 | -0.89 | -0.0 | 0.2 | -0.02 |
| kd_k_value | technical | 45.24 | 44.71 | 45.02 | 44.83 | 0.22 | -0.12 |
| kd_d_value | technical | 48.12 | 48.59 | 45.14 | 44.92 | 2.98 | 3.67 |
| kdj_j_value | technical | 39.49 | 36.91 | 44.79 | 45.66 | -5.3 | -8.75 |
| bb_width_pct | technical | 20.64 | 18.19 | 16.65 | 14.09 | 3.99 | 4.1 |
| ema23_slope_5d_pct | technical | 1.21 | 0.78 | 0.46 | 0.08 | 0.75 | 0.7 |
| distance_to_ema23_pct | technical | 0.82 | 0.76 | 0.09 | 0.12 | 0.73 | 0.64 |
| tdcc_consecutive_up_weeks | tdcc | 1.31 | 1.0 | 1.06 | 0.5 | 0.25 | 0.5 |
