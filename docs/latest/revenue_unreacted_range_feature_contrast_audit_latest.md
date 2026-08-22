# Revenue Unreacted Range Feature Contrast Audit

- generated_at: `2026-08-23 07:25:15 Asia/Taipei`
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
| excluding_unresolved_anomaly_candidates_sensitivity_only | 5268 | 161.6137 | 6265 | 20251223 | -48.7869 | 1589 | 20260223 | 5 | 5 | 0 | 0.28 | 1.29 | 1.8147 | sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 6045 | 252.6646 | 4414 | 20250605 | -91.0164 | 4763 | 20250609 | 6 | 0 | 6 | 0.39 | 1.33 | 1.5085 | blocked_pending_root_cause_anomaly_candidate_review |

## Baseline And Binary Feature Matrix

| feature_id | feature_family | feature_independence_status | equivalent_to_feature_id | feature_hit_count | high_return_feature_hit_rate_pct | failure_feature_hit_rate_pct | high_return_minus_failure_hit_rate_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | evidence_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_revenue_production_strong | baseline | baseline_not_applicable |  | 6045 |  |  |  | 28.19 | 18.69 | 53.12 | 2.02 | -0.77 | 22.2 | 31.17 | baseline_anchor |
| volume_ratio_le2 | volume | distinct_observed_mask |  | 5796 | 95.53 | 95.98 | -0.45 | 28.16 | 18.67 | 53.17 | 1.96 | -0.75 | 22.12 | 31.14 | failure_associated_risk_feature_candidate |
| technical_kdj_j_ge100 | technical_risk | distinct_observed_mask |  | 171 | 1.86 | 3.08 | -1.22 | 19.3 | 22.81 | 57.89 | 0.19 | -1.74 | 14.62 | 28.65 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 1727 | 27.87 | 29.18 | -1.31 | 28.14 | 17.6 | 54.26 | 1.79 | -0.84 | 21.66 | 32.77 | failure_associated_risk_feature_candidate |
| tdcc_consecutive_up_ge1 | tdcc | distinct_observed_mask |  | 1080 | 16.77 | 18.22 | -1.45 | 28.15 | 17.69 | 54.17 | -0.56 | -1.13 | 20.83 | 37.13 | failure_associated_risk_feature_candidate |
| candle_solid_red | candle | distinct_observed_mask |  | 1097 | 16.69 | 18.65 | -1.96 | 27.07 | 18.32 | 54.6 | 1.65 | -0.99 | 20.42 | 30.63 | failure_associated_risk_feature_candidate |
| candle_bullish_attack | candle | distinct_observed_mask |  | 2166 | 34.2 | 36.5 | -2.3 | 27.24 | 18.65 | 54.11 | 1.8 | -0.9 | 21.19 | 31.53 | failure_associated_risk_feature_candidate |
| market_mild_bull | market_regime | distinct_observed_mask |  | 1315 | 18.7 | 22.39 | -3.69 | 25.17 | 20.15 | 54.68 | 0.56 | -1.05 | 19.09 | 31.48 | failure_associated_risk_feature_candidate |
| technical_macd_hist_gt0 | technical | distinct_observed_mask |  | 2471 | 38.38 | 42.54 | -4.16 | 26.06 | 18.66 | 55.28 | 1.45 | -1.3 | 20.84 | 32.86 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_ge100 | monthly_revenue | distinct_observed_mask |  | 1112 | 16.17 | 20.55 | -4.38 | 24.55 | 16.1 | 59.35 | 0.73 | -2.1 | 19.51 | 36.24 | failure_associated_risk_feature_candidate |
| shape_near_range23_high | price_shape | distinct_observed_mask |  | 1451 | 19.97 | 24.63 | -4.66 | 23.57 | 21.92 | 54.51 | 1.72 | -0.71 | 18.47 | 23.98 | failure_associated_risk_feature_candidate |
| market_strong_bull | market_regime | distinct_observed_mask |  | 3078 | 47.84 | 53.78 | -5.94 | 26.35 | 17.54 | 56.11 | 1.63 | -1.47 | 20.86 | 34.6 | failure_associated_risk_feature_candidate |
| revenue_latest_yoy_delta_ge20 | monthly_revenue | distinct_observed_mask |  | 2454 | 37.26 | 43.63 | -6.37 | 25.71 | 17.2 | 57.09 | 1.15 | -1.43 | 20.37 | 33.94 | failure_associated_risk_feature_candidate |
| shape_range23_width_le10 | price_shape | distinct_observed_mask |  | 876 | 7.75 | 15.1 | -7.35 | 16.78 | 27.85 | 55.37 | 0.37 | -0.54 | 11.87 | 17.69 | failure_associated_risk_feature_candidate |
| technical_kdj_bullish_not_extreme | technical | distinct_observed_mask |  | 2361 | 33.53 | 42.88 | -9.35 | 24.14 | 17.53 | 58.32 | 0.45 | -1.79 | 19.06 | 34.39 | failure_associated_risk_feature_candidate |
| market_bull | market_regime | distinct_observed_mask |  | 4393 | 66.54 | 76.18 | -9.64 | 26.0 | 18.32 | 55.68 | 1.31 | -1.35 | 20.33 | 33.67 | failure_associated_risk_feature_candidate |
| technical_kd_bullish_not_overheated | technical | distinct_observed_mask |  | 2321 | 32.19 | 42.42 | -10.23 | 23.7 | 17.62 | 58.68 | 0.33 | -1.85 | 18.61 | 34.68 | failure_associated_risk_feature_candidate |
| position120_low_le40 | price_position | distinct_observed_mask |  | 2613 | 32.19 | 44.69 | -12.5 | 22.77 | 22.31 | 54.92 | 0.62 | -1.03 | 16.53 | 28.7 | failure_associated_risk_feature_candidate |
| shape_range23_width_le15 | price_shape | distinct_observed_mask |  | 2000 | 20.94 | 33.91 | -12.97 | 20.45 | 25.1 | 54.45 | 0.77 | -0.65 | 14.05 | 22.8 | failure_associated_risk_feature_candidate |
| technical_close_above_ma20_ema23 | technical | distinct_observed_mask |  | 2321 | 42.18 | 39.3 | 2.88 | 29.04 | 16.59 | 54.37 | 2.47 | -1.07 | 24.39 | 33.56 | mixed_or_low_discrimination_research_only |
| technical_bb_width_not_extreme | technical | distinct_observed_mask |  | 3263 | 55.59 | 54.22 | 1.37 | 28.65 | 17.99 | 53.36 | 1.69 | -0.84 | 22.86 | 32.73 | mixed_or_low_discrimination_research_only |
| revenue_latest30_and_cumulative20 | monthly_revenue | distinct_observed_mask |  | 2934 | 50.89 | 49.64 | 1.25 | 28.87 | 16.8 | 54.33 | 1.89 | -1.01 | 23.28 | 33.67 | mixed_or_low_discrimination_research_only |
| revenue_cumulative_yoy_improving_2m | monthly_revenue | distinct_observed_mask |  | 2396 | 39.87 | 39.02 | 0.85 | 28.92 | 18.78 | 52.3 | 1.99 | -0.59 | 22.33 | 32.47 | mixed_or_low_discrimination_research_only |
| tdcc_all_thresholds_up | tdcc | distinct_observed_mask |  | 385 | 7.0 | 6.45 | 0.55 | 31.17 | 15.06 | 53.77 | 0.0 | -0.74 | 24.42 | 34.55 | mixed_or_low_discrimination_research_only |
| tdcc_four_thresholds_sync_up | tdcc | duplicate_mask_not_independent_evidence | tdcc_all_thresholds_up | 385 | 7.0 | 6.45 | 0.55 | 31.17 | 15.06 | 53.77 | 0.0 | -0.74 | 24.42 | 34.55 | mixed_or_low_discrimination_research_only |
| tdcc_high_thresholds_up | tdcc | distinct_observed_mask |  | 755 | 12.59 | 12.39 | 0.2 | 29.8 | 17.48 | 52.72 | -0.03 | -0.77 | 22.38 | 35.36 | mixed_or_low_discrimination_research_only |
| revenue_latest50_and_cumulative30 | monthly_revenue | distinct_observed_mask |  | 1711 | 30.03 | 29.87 | 0.16 | 28.4 | 15.55 | 56.05 | 1.93 | -1.54 | 23.55 | 35.18 | mixed_or_low_discrimination_research_only |
| volume_ratio_le1_5 | volume | distinct_observed_mask |  | 5348 | 88.23 | 88.51 | -0.28 | 28.25 | 18.61 | 53.14 | 2.03 | -0.75 | 22.14 | 30.98 | mixed_or_low_discrimination_research_only |
| tdcc_consecutive_up_ge2 | tdcc | distinct_observed_mask |  | 714 | 11.33 | 11.71 | -0.38 | 29.41 | 17.93 | 52.66 | -0.1 | -0.95 | 21.29 | 35.85 | mixed_or_low_discrimination_research_only |
| shape_range23_width_le20 | price_shape | distinct_observed_mask |  | 3004 | 38.23 | 49.27 | -11.04 | 23.44 | 23.9 | 52.66 | 1.48 | -0.48 | 17.08 | 24.73 | mixed_or_low_discrimination_research_only |
| market_range_bound | market_regime | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| market_unknown | market_regime_coverage | no_observed_hits_not_evaluable |  | 0 | 0.0 | 0.0 | 0.0 |  |  |  |  |  |  |  | no_feature_hits |
| market_correction_or_high_risk | market_regime_risk | distinct_observed_mask |  | 1652 | 33.46 | 23.82 | 9.64 | 34.02 | 19.67 | 46.31 | 3.93 | 0.82 | 27.18 | 24.52 | positive_discriminator_single_feature_candidate |
| momentum_return20_0_25 | price_momentum | distinct_observed_mask |  | 3192 | 60.13 | 51.64 | 8.49 | 31.11 | 16.95 | 51.94 | 2.85 | -0.55 | 25.28 | 32.08 | positive_discriminator_single_feature_candidate |
| position120_high_gt75 | price_position | distinct_observed_mask |  | 1027 | 23.25 | 15.82 | 7.43 | 35.93 | 14.61 | 49.46 | 4.47 | 0.0 | 30.38 | 32.52 | positive_discriminator_single_feature_candidate |
| technical_ma20_above_ma60 | technical | distinct_observed_mask |  | 2619 | 49.4 | 42.7 | 6.7 | 31.62 | 16.04 | 52.35 | 2.46 | -0.61 | 25.32 | 34.29 | positive_discriminator_single_feature_candidate |
| technical_ema23_slope_positive | technical | distinct_observed_mask |  | 2857 | 53.28 | 46.99 | 6.29 | 30.52 | 16.66 | 52.82 | 2.73 | -0.76 | 25.03 | 33.5 | positive_discriminator_single_feature_candidate |
| technical_rsi14_ge60 | technical | distinct_observed_mask |  | 1353 | 26.9 | 21.55 | 5.35 | 32.3 | 16.56 | 51.15 | 3.7 | -0.34 | 26.68 | 29.93 | positive_discriminator_single_feature_candidate |
| position120_mid_40_75 | price_position | distinct_observed_mask |  | 2405 | 44.56 | 39.49 | 5.07 | 30.77 | 16.51 | 52.72 | 2.5 | -0.64 | 24.86 | 33.26 | positive_discriminator_single_feature_candidate |
| technical_rsi14_40_70 | technical | distinct_observed_mask |  | 3957 | 68.78 | 65.34 | 3.44 | 28.94 | 18.04 | 53.02 | 2.23 | -0.68 | 23.33 | 31.31 | positive_discriminator_single_feature_candidate |
| technical_obv_above_ma20 | technical | distinct_observed_mask |  | 2943 | 52.09 | 48.68 | 3.41 | 28.85 | 18.04 | 53.11 | 2.31 | -0.77 | 23.75 | 31.06 | positive_discriminator_single_feature_candidate |

## Numeric High-Return Versus Failure Contrast

| feature_id | feature_family | high_return_feature_mean | high_return_feature_median | failure_feature_mean | failure_feature_median | high_return_minus_failure_feature_mean | high_return_minus_failure_feature_median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| revenue_latest_yoy_pct | monthly_revenue | 1271.78 | 41.82 | 3384.95 | 42.2 | -2113.17 | -0.38 |
| revenue_cumulative_yoy_pct | monthly_revenue | 684.44 | 31.68 | 1756.45 | 32.3 | -1072.01 | -0.62 |
| revenue_latest_yoy_delta_1m | monthly_revenue | -983.46 | 6.65 | -814.98 | 12.81 | -168.48 | -6.16 |
| revenue_cumulative_yoy_delta_1m | monthly_revenue | -8.53 | 2.14 | -639.4 | 3.1 | 630.87 | -0.96 |
| range23_width_pct | price_shape | 29.29 | 24.05 | 25.98 | 20.31 | 3.31 | 3.74 |
| distance_to_range23_high_pct | price_shape | -11.7 | -10.35 | -10.95 | -9.47 | -0.75 | -0.88 |
| close_position_120d_pct | price_position | 51.94 | 55.91 | 44.69 | 44.92 | 7.25 | 10.99 |
| return_5d_pct | price_momentum | -2.01 | -1.32 | -1.33 | -0.64 | -0.68 | -0.68 |
| return_20d_pct | price_momentum | 2.44 | 2.55 | 0.81 | 0.23 | 1.63 | 2.32 |
| volume_ratio_prev20 | volume | 0.84 | 0.73 | 0.85 | 0.73 | -0.01 | 0.0 |
| rsi14 | technical | 50.34 | 51.24 | 48.41 | 48.71 | 1.93 | 2.53 |
| macd_hist | technical | -1.53 | -0.05 | -0.92 | -0.02 | -0.61 | -0.03 |
| kd_k_value | technical | 43.46 | 41.63 | 43.64 | 42.99 | -0.18 | -1.36 |
| kd_d_value | technical | 46.42 | 45.71 | 44.57 | 44.26 | 1.85 | 1.45 |
| kdj_j_value | technical | 37.52 | 33.54 | 41.77 | 40.57 | -4.25 | -7.03 |
| bb_width_pct | technical | 20.57 | 17.96 | 17.85 | 14.99 | 2.72 | 2.97 |
| ema23_slope_5d_pct | technical | 0.82 | 0.5 | 0.29 | 0.05 | 0.53 | 0.45 |
| distance_to_ema23_pct | technical | 0.04 | 0.19 | -0.52 | -0.18 | 0.56 | 0.37 |
| tdcc_consecutive_up_weeks | tdcc | 1.58 | 1.0 | 1.61 | 1.0 | -0.03 | 0.0 |
