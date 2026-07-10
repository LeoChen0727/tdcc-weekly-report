# Price Pullback 23EMA Revenue Condition Matrix

- generated_at: `2026-07-10 17:43:21 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_known_price_or_revenue_anomalies | base_v1_without_revenue_gate | baseline | 4883 | 1458 | 100.0 | 63.17 | 8.37 | 28.46 | 3.17 | 1.73 | 22.22 | 15.64 | 8.63 | 6.52 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_context_ready | revenue_coverage | 4878 | 1456 | 99.86 | 63.12 | 8.38 | 28.5 | 3.15 | 1.72 | 22.12 | 15.66 | 8.63 | 6.52 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_positive | revenue_direction | 3364 | 1031 | 70.71 | 63.34 | 7.95 | 28.71 | 3.39 | 1.92 | 22.99 | 15.52 | 21.78 | 16.77 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_production_strong | revenue_strength | 1031 | 355 | 24.35 | 61.13 | 6.48 | 32.39 | 3.3 | 2.95 | 30.42 | 21.41 | 50.11 | 42.22 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 348 | 132 | 9.05 | 65.15 | 3.79 | 31.06 | 3.18 | 3.84 | 31.82 | 25.76 | 89.96 | 61.65 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 469 | 162 | 11.11 | 59.88 | 5.56 | 34.57 | 3.69 | 3.17 | 34.57 | 22.84 | 66.43 | 71.32 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 533 | 197 | 13.51 | 61.93 | 5.08 | 32.99 | 3.47 | 3.73 | 33.5 | 22.34 | 70.04 | 55.51 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_2m | revenue_turnaround | 1216 | 410 | 28.12 | 63.66 | 10.49 | 25.85 | 3.48 | 2.8 | 23.41 | 14.39 | 20.21 | 6.08 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_3m | revenue_turnaround | 261 | 83 | 5.69 | 68.67 | 6.02 | 25.3 | 2.31 | 1.6 | 19.28 | 16.87 | 33.29 | 15.82 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1505 | 480 | 32.92 | 63.75 | 10.0 | 26.25 | 3.2 | 1.95 | 22.08 | 12.92 | 21.42 | 6.43 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive | revenue_turnaround | 1009 | 339 | 23.25 | 61.36 | 7.67 | 30.97 | 3.35 | 1.72 | 24.48 | 15.04 | 17.84 | 2.66 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 514 | 166 | 11.39 | 61.45 | 7.23 | 31.33 | 3.39 | 1.23 | 22.89 | 14.46 | 14.31 | -5.3 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 346 | 117 | 8.02 | 58.12 | 12.82 | 29.06 | 3.04 | 2.78 | 24.79 | 19.66 | 24.98 | 6.78 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 1001 | 335 | 22.98 | 58.81 | 7.46 | 33.73 | 3.26 | 2.85 | 28.66 | 19.7 | 34.55 | 11.89 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 899 | 305 | 20.92 | 62.3 | 7.87 | 29.84 | 3.69 | 1.86 | 25.9 | 14.75 | 19.0 | 1.37 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 1121 | 378 | 25.93 | 64.02 | 10.05 | 25.93 | 3.58 | 2.8 | 24.34 | 14.55 | 22.17 | 5.99 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_negative_both_risk | revenue_risk | 1509 | 467 | 32.03 | 62.31 | 9.21 | 28.48 | 2.7 | 1.33 | 20.99 | 16.27 | -20.49 | -16.92 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | base_v1_without_revenue_gate | baseline | 5047 | 1505 | 100.0 | 63.32 | 8.37 | 28.31 | 3.26 | 1.83 | 22.33 | 15.61 | 216.49 | 75.6 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 5042 | 1503 | 99.87 | 63.27 | 8.38 | 28.34 | 3.24 | 1.83 | 22.22 | 15.64 | 216.49 | 75.6 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_positive | revenue_direction | 3520 | 1076 | 71.5 | 63.48 | 7.99 | 28.53 | 3.51 | 2.01 | 23.14 | 15.52 | 312.7 | 113.11 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 1186 | 400 | 26.58 | 61.75 | 6.75 | 31.5 | 3.54 | 3.0 | 30.0 | 20.75 | 831.46 | 298.51 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 490 | 174 | 11.56 | 66.09 | 5.17 | 28.74 | 3.72 | 3.8 | 29.89 | 22.41 | 1883.61 | 616.27 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 617 | 205 | 13.62 | 61.95 | 6.34 | 31.71 | 4.23 | 3.66 | 33.66 | 20.49 | 1159.96 | 566.16 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 669 | 237 | 15.75 | 63.29 | 5.91 | 30.8 | 3.88 | 3.77 | 32.49 | 20.25 | 1014.79 | 467.78 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_2m | revenue_turnaround | 1266 | 428 | 28.44 | 64.02 | 10.51 | 25.47 | 3.61 | 2.98 | 23.83 | 14.49 | 358.26 | 113.03 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_3m | revenue_turnaround | 277 | 88 | 5.85 | 68.18 | 7.95 | 23.86 | 2.94 | 2.4 | 21.59 | 15.91 | 81.64 | 70.15 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1557 | 497 | 33.02 | 63.78 | 10.26 | 25.96 | 3.3 | 2.03 | 22.13 | 12.88 | 536.41 | 121.47 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive | revenue_turnaround | 1061 | 352 | 23.39 | 60.8 | 7.67 | 31.53 | 3.22 | 1.66 | 23.86 | 15.34 | 327.63 | 22.65 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 538 | 171 | 11.36 | 60.82 | 7.02 | 32.16 | 3.26 | 1.22 | 22.22 | 15.2 | 595.85 | -0.79 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 381 | 129 | 8.57 | 58.91 | 13.18 | 27.91 | 2.96 | 2.78 | 23.26 | 18.6 | 912.52 | 343.66 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 1129 | 373 | 24.78 | 60.05 | 7.24 | 32.71 | 3.5 | 3.05 | 28.42 | 19.03 | 857.58 | 241.49 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 950 | 317 | 21.06 | 61.83 | 7.89 | 30.28 | 3.57 | 1.85 | 25.24 | 14.83 | 362.89 | 21.02 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 1171 | 396 | 26.31 | 64.39 | 10.1 | 25.51 | 3.72 | 2.98 | 24.75 | 14.65 | 387.45 | 121.59 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_negative_both_risk | revenue_risk | 1517 | 470 | 31.23 | 62.55 | 9.15 | 28.3 | 2.7 | 1.34 | 20.85 | 16.17 | -22.55 | -17.27 | blocked_model_specific_promotion_pr_required |
