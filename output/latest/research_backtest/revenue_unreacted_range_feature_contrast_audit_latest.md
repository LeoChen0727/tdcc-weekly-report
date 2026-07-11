# Revenue Unreacted Range Feature Contrast Audit

- generated_at: `2026-07-11 16:08:10 Asia/Taipei`
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
| excluding_known_revenue_and_price_anomalies | 4646 | 411.4754 | 8291 | 20260416 | -48.7869 | 1589 | 20260223 | 4 | 4 | 0 | 0.83 | 1.95 | 2.7713 | anomaly_check_pass |
| including_known_anomalies | 5327 | 411.4754 | 8291 | 20260416 | -83.0769 | 7780 | 20251219 | 6 | 0 | 6 | 0.73 | 1.73 | 2.4171 | not_decision_basis_known_anomalies_included |

## Baseline And Binary Feature Matrix

| feature_id | feature_family | feature_independence_status | equivalent_to_feature_id | feature_hit_count | high_return_feature_hit_rate_pct | failure_feature_hit_rate_pct | high_return_minus_failure_hit_rate_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | evidence_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_revenue_production_strong | baseline | baseline_not_applicable |  | 4646 |  |  |  | 31.62 | 18.53 | 49.85 | 3.41 | 0.0 | 24.67 | 28.58 | baseline_anchor |
| technical_macd_hist_gt0 | technical | distinct_observed_mask |  | 1707 | 37.87 | 38.08 | -0.21 | 31.58 | 16.75 | 51.67 | 3.21 | -0.48 | 25.42 | 29.76 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1264 | 26.35 | 27.94 | -1.59 | 30.7 | 18.12 | 51.19 | 2.84 | -0.33 | 23.89 | 30.38 | failure_associated_risk_feature_candidate |
| technical_kdj_j_ge100 | technical_risk | distinct_observed_mask |  | 143 | 1.83 | 3.63 | -1.8 | 20.28 | 20.98 | 58.74 | -0.39 | -2.14 | 14.69 | 28.67 | failure_associated_risk_feature_candidate |
| candle_bullish_attack | candle | distinct_observed_mask |  | 1795 | 36.82 | 39.03 | -2.21 | 30.31 | 19.33 | 50.36 | 2.93 | -0.16 | 23.51 | 28.75 | failure_associated_risk_feature_candidate |
| candle_solid_red | candle | distinct_observed_mask |  | 901 | 17.1 | 20.16 | -3.06 | 28.75 | 19.42 | 51.83 | 2.45 | -0.39 | 21.75 | 29.86 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_delta_ge20 | monthly_revenue | distinct_observed_mask |  | 1747 | 36.04 | 39.72 | -3.68 | 29.77 | 17.57 | 52.66 | 3.0 | -0.63 | 23.64 | 29.77 | failure_associated_risk_feature_candidate |
| shape_near_range23_high | price_shape | distinct_observed_mask |  | 1334 | 24.61 | 29.75 | -5.14 | 27.74 | 20.61 | 51.65 | 2.6 | -0.33 | 21.14 | 24.29 | failure_associated_risk_feature_candidate |
| shape_range23_width_le10 | price_shape | distinct_observed_mask |  | 623 | 6.81 | 15.07 | -8.26 | 17.98 | 26.0 | 56.02 | 0.39 | -0.62 | 12.52 | 17.82 | failure_associated_risk_feature_candidate |
| technical_kdj_bullish_not_extreme | technical | distinct_observed_mask |  | 1727 | 32.11 | 41.97 | -9.86 | 25.94 | 17.78 | 56.28 | 1.66 | -1.62 | 21.31 | 33.24 | failure_associated_risk_feature_candidate |
| market_bull | market_regime | distinct_observed_mask |  | 3527 | 70.94 | 80.92 | -9.98 | 29.52 | 17.35 | 53.13 | 2.61 | -0.8 | 23.05 | 31.81 | failure_associated_risk_feature_candidate |
| market_strong_bull | market_regime | distinct_observed_mask |  | 2577 | 51.22 | 61.49 | -10.27 | 28.68 | 16.07 | 55.26 | 2.37 | -1.45 | 22.78 | 34.42 | failure_associated_risk_feature_candidate |
| technical_kd_bullish_not_overheated | technical | distinct_observed_mask |  | 1705 | 30.8 | 41.93 | -11.13 | 25.4 | 17.65 | 56.95 | 1.48 | -1.72 | 20.7 | 33.9 | failure_associated_risk_feature_candidate |
| position120_low_le40 | price_position | distinct_observed_mask |  | 2025 | 33.68 | 46.16 | -12.48 | 26.02 | 21.19 | 52.79 | 1.87 | -0.66 | 19.06 | 27.95 | failure_associated_risk_feature_candidate |
| shape_range23_width_le15 | price_shape | distinct_observed_mask |  | 1399 | 18.06 | 32.34 | -14.28 | 21.73 | 24.73 | 53.54 | 1.04 | -0.61 | 14.8 | 22.87 | failure_associated_risk_feature_candidate |
| shape_range23_width_le20 | price_shape | distinct_observed_mask |  | 2129 | 32.46 | 48.4 | -15.94 | 23.81 | 23.53 | 52.65 | 1.39 | -0.56 | 17.47 | 25.36 | failure_associated_risk_feature_candidate |
| technical_close_above_ma20_ema23 | technical | distinct_observed_mask |  | 1826 | 43.8 | 40.07 | 3.73 | 33.02 | 16.16 | 50.82 | 4.05 | -0.33 | 27.49 | 31.11 | mixed_or_low_discrimination_research_only |
| technical_bb_width_not_extreme | technical | distinct_observed_mask |  | 1946 | 44.33 | 42.14 | 2.19 | 32.48 | 17.37 | 50.15 | 3.43 | -0.11 | 26.1 | 30.16 | mixed_or_low_discrimination_research_only |
| technical_rsi14_40_70 | technical | distinct_observed_mask |  | 2692 | 60.65 | 58.72 | 1.93 | 32.32 | 17.16 | 50.52 | 3.59 | -0.2 | 25.82 | 29.83 | mixed_or_low_discrimination_research_only |
| volume_ratio_le1_5 | volume | distinct_observed_mask |  | 4070 | 87.26 | 86.87 | 0.39 | 31.72 | 18.85 | 49.43 | 3.27 | 0.0 | 24.57 | 28.33 | mixed_or_low_discrimination_research_only |
| market_mild_bull | market_regime | distinct_observed_mask |  | 950 | 19.72 | 19.43 | 0.29 | 31.79 | 20.84 | 47.37 | 3.24 | 0.14 | 23.79 | 24.74 | mixed_or_low_discrimination_research_only |
| market_range_bound | market_regime | distinct_observed_mask |  | 248 | 4.71 | 4.45 | 0.26 | 35.48 | 22.98 | 41.53 | 2.72 | 1.76 | 21.77 | 22.98 | mixed_or_low_discrimination_research_only |
| revenue_cumulative_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1739 | 37.43 | 37.52 | -0.09 | 31.86 | 18.17 | 49.97 | 3.47 | 0.0 | 24.67 | 29.79 | mixed_or_low_discrimination_research_only |
| revenue_latest_yoy_ge100 | monthly_revenue | distinct_observed_mask |  | 481 | 10.38 | 11.1 | -0.72 | 32.22 | 14.35 | 53.43 | 4.23 | -0.98 | 24.74 | 32.02 | mixed_or_low_discrimination_research_only |
| volume_ratio_le2 | volume | distinct_observed_mask |  | 4446 | 94.85 | 95.64 | -0.79 | 31.47 | 18.71 | 49.82 | 3.22 | 0.0 | 24.45 | 28.41 | mixed_or_low_discrimination_research_only |
| market_unknown | market_regime_coverage | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| technical_ema23_slope_positive | technical | distinct_observed_mask |  | 1983 | 51.92 | 41.15 | 10.77 | 36.81 | 15.13 | 48.06 | 4.96 | 0.43 | 30.01 | 29.85 | positive_discriminator_single_feature_candidate |
| technical_ma20_above_ma60 | technical | distinct_observed_mask |  | 1634 | 43.46 | 32.99 | 10.47 | 37.88 | 15.36 | 46.76 | 5.27 | 1.0 | 30.48 | 29.31 | positive_discriminator_single_feature_candidate |
| market_correction_or_high_risk | market_regime_risk | distinct_observed_mask |  | 871 | 24.35 | 14.64 | 9.71 | 39.04 | 22.04 | 38.92 | 6.83 | 2.2 | 32.03 | 17.11 | positive_discriminator_single_feature_candidate |
| momentum_return20_0_25 | price_momentum | distinct_observed_mask |  | 2172 | 55.06 | 45.68 | 9.38 | 35.45 | 15.84 | 48.71 | 4.71 | 0.22 | 29.05 | 30.16 | positive_discriminator_single_feature_candidate |
| position120_high_gt75 | price_position | distinct_observed_mask |  | 1505 | 39.62 | 30.27 | 9.35 | 36.88 | 16.54 | 46.58 | 4.88 | 0.77 | 30.17 | 28.11 | positive_discriminator_single_feature_candidate |
| technical_rsi14_ge60 | technical | distinct_observed_mask |  | 1009 | 27.49 | 20.73 | 6.76 | 37.76 | 14.67 | 47.57 | 5.24 | 0.65 | 31.22 | 27.65 | positive_discriminator_single_feature_candidate |
| revenue_latest50_and_cumulative30 | monthly_revenue | distinct_observed_mask |  | 1039 | 27.49 | 21.55 | 5.94 | 36.86 | 15.11 | 48.03 | 5.24 | 0.5 | 30.32 | 31.47 | positive_discriminator_single_feature_candidate |
| revenue_latest30_and_cumulative20 | monthly_revenue | distinct_observed_mask |  | 2095 | 49.56 | 44.3 | 5.26 | 34.37 | 16.66 | 48.97 | 4.12 | 0.18 | 27.11 | 29.64 | positive_discriminator_single_feature_candidate |
| technical_obv_above_ma20 | technical | distinct_observed_mask |  | 2076 | 48.87 | 44.13 | 4.74 | 32.9 | 17.87 | 49.23 | 3.91 | 0.0 | 26.97 | 29.29 | positive_discriminator_single_feature_candidate |
| position120_mid_40_75 | price_position | distinct_observed_mask |  | 1116 | 26.7 | 23.58 | 3.12 | 34.68 | 16.4 | 48.92 | 4.2 | 0.25 | 27.42 | 30.38 | positive_discriminator_single_feature_candidate |
| tdcc_high_thresholds_up | tdcc | distinct_observed_mask |  | 244 | 6.63 | 4.19 | 2.44 | 43.03 | 17.21 | 39.75 | 4.9 | 3.0 | 31.15 | 28.69 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge1 | tdcc | distinct_observed_mask |  | 337 | 8.64 | 6.22 | 2.42 | 40.06 | 17.21 | 42.73 | 4.25 | 1.61 | 29.38 | 29.97 | positive_discriminator_single_feature_candidate |
| tdcc_all_thresholds_up | tdcc | distinct_observed_mask |  | 126 | 4.01 | 1.86 | 2.15 | 47.62 | 18.25 | 34.13 | 6.58 | 3.79 | 36.51 | 24.6 | positive_discriminator_single_feature_candidate |
| tdcc_four_thresholds_sync_up | tdcc | duplicate_mask_not_independent_evidence | tdcc_all_thresholds_up | 126 | 4.01 | 1.86 | 2.15 | 47.62 | 18.25 | 34.13 | 6.58 | 3.79 | 36.51 | 24.6 | positive_discriminator_single_feature_candidate |
| tdcc_consecutive_up_ge2 | tdcc | distinct_observed_mask |  | 204 | 5.41 | 3.45 | 1.96 | 42.16 | 18.63 | 39.22 | 5.42 | 2.26 | 30.39 | 26.47 | positive_discriminator_single_feature_candidate |

## Numeric High-Return Versus Failure Contrast

| feature_id | feature_family | high_return_feature_mean | high_return_feature_median | failure_feature_mean | failure_feature_median | high_return_minus_failure_feature_mean | high_return_minus_failure_feature_median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_latest_yoy_pct | monthly_revenue | 49.28 | 39.76 | 48.13 | 36.87 | 1.15 | 2.89 |
| revenue_cumulative_yoy_pct | monthly_revenue | 41.18 | 31.38 | 38.12 | 29.3 | 3.06 | 2.08 |
| revenue_latest_yoy_delta_1m | monthly_revenue | 8.55 | 6.41 | 14.36 | 9.8 | -5.81 | -3.39 |
| revenue_cumulative_yoy_delta_1m | monthly_revenue | 3.8 | 1.5 | 7.66 | 2.46 | -3.86 | -0.96 |
| range23_width_pct | price_shape | 162.53 | 26.87 | 88.21 | 20.71 | 74.32 | 6.16 |
| distance_to_range23_high_pct | price_shape | -12.39 | -9.6 | -12.32 | -8.52 | -0.07 | -1.08 |
| close_position_120d_pct | price_position | 55.06 | 65.1 | 46.04 | 47.41 | 9.02 | 17.69 |
| return_5d_pct | price_momentum | -1.38 | -0.71 | -0.64 | -0.11 | -0.74 | -0.6 |
| return_20d_pct | price_momentum | 3.48 | 3.43 | 0.88 | 0.17 | 2.6 | 3.26 |
| volume_ratio_prev20 | volume | 0.87 | 0.77 | 0.87 | 0.76 | 0.0 | 0.01 |
| rsi14 | technical | 52.1 | 53.35 | 48.94 | 49.29 | 3.16 | 4.06 |
| macd_hist | technical | -0.61 | -0.03 | -0.86 | -0.01 | 0.25 | -0.02 |
| kd_k_value | technical | 46.1 | 45.78 | 45.6 | 46.19 | 0.5 | -0.41 |
| kd_d_value | technical | 48.74 | 49.28 | 45.44 | 45.55 | 3.3 | 3.73 |
| kdj_j_value | technical | 40.87 | 39.4 | 45.79 | 47.26 | -4.92 | -7.86 |
| bb_width_pct | technical | 20.92 | 18.5 | 16.73 | 14.18 | 4.19 | 4.32 |
| ema23_slope_5d_pct | technical | 1.23 | 0.8 | 0.46 | 0.09 | 0.77 | 0.71 |
| distance_to_ema23_pct | technical | 0.83 | 0.83 | 0.11 | 0.09 | 0.72 | 0.74 |
| tdcc_consecutive_up_weeks | tdcc | 1.27 | 1.0 | 1.06 | 0.0 | 0.21 | 1.0 |
