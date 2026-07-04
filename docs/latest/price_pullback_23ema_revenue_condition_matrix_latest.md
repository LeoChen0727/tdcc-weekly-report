# Price Pullback 23EMA Revenue Condition Matrix

- generated_at: `2026-07-05 04:40:31 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_known_price_or_revenue_anomalies | base_v1_without_revenue_gate | baseline | 4062 | 1128 | 100.0 | 66.22 | 5.5 | 28.28 | 3.12 | 1.57 | 22.78 | 15.51 | 8.79 | 6.84 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_context_ready | revenue_coverage | 4057 | 1126 | 99.82 | 66.16 | 5.51 | 28.33 | 3.09 | 1.56 | 22.65 | 15.54 | 8.79 | 6.84 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_positive | revenue_direction | 2744 | 793 | 70.3 | 66.08 | 5.3 | 28.63 | 3.25 | 1.85 | 23.2 | 15.13 | 22.32 | 17.19 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_production_strong | revenue_strength | 840 | 277 | 24.56 | 62.09 | 4.33 | 33.57 | 3.09 | 2.63 | 32.13 | 21.66 | 51.46 | 43.15 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 282 | 103 | 9.13 | 66.02 | 3.88 | 30.1 | 3.13 | 3.95 | 34.95 | 24.27 | 93.26 | 63.01 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 398 | 127 | 11.26 | 61.42 | 4.72 | 33.86 | 3.3 | 3.39 | 35.43 | 21.26 | 69.5 | 73.67 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 443 | 156 | 13.83 | 63.46 | 3.85 | 32.69 | 3.26 | 3.84 | 35.9 | 21.15 | 71.54 | 56.22 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_2m | revenue_turnaround | 920 | 293 | 25.98 | 67.58 | 5.8 | 26.62 | 3.05 | 2.66 | 23.55 | 15.36 | 21.74 | 7.91 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_3m | revenue_turnaround | 224 | 71 | 6.29 | 66.2 | 7.04 | 26.76 | 1.88 | 0.97 | 16.9 | 16.9 | 33.7 | 17.01 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1179 | 350 | 31.03 | 66.29 | 7.43 | 26.29 | 2.79 | 1.68 | 21.43 | 13.71 | 22.56 | 7.5 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive | revenue_turnaround | 868 | 285 | 25.27 | 64.91 | 5.26 | 29.82 | 3.16 | 1.85 | 24.21 | 15.44 | 18.69 | 3.38 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 406 | 124 | 10.99 | 68.55 | 4.03 | 27.42 | 3.25 | 1.32 | 22.58 | 13.71 | 15.0 | -5.6 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 293 | 99 | 8.78 | 58.59 | 9.09 | 32.32 | 2.56 | 2.37 | 23.23 | 22.22 | 24.43 | 7.35 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 867 | 283 | 25.09 | 59.72 | 6.01 | 34.28 | 3.27 | 2.85 | 28.98 | 19.79 | 34.31 | 13.03 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 770 | 254 | 22.52 | 66.54 | 5.12 | 28.35 | 3.56 | 2.22 | 25.98 | 14.96 | 20.14 | 2.26 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 843 | 271 | 24.02 | 67.9 | 5.9 | 26.2 | 3.18 | 2.74 | 24.35 | 15.5 | 23.29 | 7.31 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_negative_both_risk | revenue_risk | 1308 | 376 | 33.33 | 65.69 | 6.12 | 28.19 | 2.9 | 1.28 | 22.61 | 16.76 | -19.85 | -16.04 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | base_v1_without_revenue_gate | baseline | 4192 | 1161 | 100.0 | 66.06 | 5.6 | 28.34 | 3.17 | 1.65 | 22.74 | 15.59 | 262.4 | 75.55 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 4187 | 1159 | 99.83 | 66.01 | 5.61 | 28.39 | 3.15 | 1.64 | 22.61 | 15.62 | 262.4 | 75.55 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_positive | revenue_direction | 2869 | 825 | 71.06 | 65.82 | 5.45 | 28.73 | 3.33 | 1.86 | 23.15 | 15.27 | 379.22 | 113.62 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 964 | 309 | 26.61 | 61.81 | 4.85 | 33.33 | 3.22 | 2.93 | 31.07 | 21.36 | 1004.41 | 297.92 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 396 | 133 | 11.46 | 65.41 | 5.26 | 29.32 | 3.46 | 3.66 | 31.58 | 21.8 | 2305.41 | 627.29 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 515 | 157 | 13.52 | 61.78 | 5.73 | 32.48 | 3.7 | 3.41 | 33.76 | 19.75 | 1383.53 | 570.41 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 551 | 184 | 15.85 | 63.59 | 4.89 | 31.52 | 3.56 | 3.69 | 34.24 | 19.57 | 1190.27 | 470.35 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_2m | revenue_turnaround | 965 | 309 | 26.61 | 67.96 | 6.15 | 25.89 | 3.23 | 2.88 | 23.95 | 15.21 | 487.06 | 154.15 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_3m | revenue_turnaround | 239 | 75 | 6.46 | 65.33 | 9.33 | 25.33 | 2.37 | 1.24 | 18.67 | 16.0 | 83.08 | 74.88 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1227 | 365 | 31.44 | 66.3 | 7.67 | 26.03 | 2.89 | 1.73 | 21.37 | 13.7 | 720.98 | 162.78 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive | revenue_turnaround | 909 | 294 | 25.32 | 63.61 | 5.44 | 30.95 | 2.97 | 1.66 | 23.47 | 15.99 | 383.38 | 25.79 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 427 | 128 | 11.02 | 67.19 | 3.91 | 28.91 | 3.06 | 1.23 | 21.88 | 14.84 | 787.49 | -1.22 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 321 | 108 | 9.3 | 58.33 | 10.19 | 31.48 | 2.43 | 2.39 | 21.3 | 21.3 | 1073.42 | 407.02 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 972 | 312 | 26.87 | 60.26 | 6.09 | 33.65 | 3.38 | 2.94 | 28.21 | 19.23 | 981.7 | 256.0 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 810 | 262 | 22.57 | 65.27 | 5.34 | 29.39 | 3.39 | 1.91 | 25.19 | 15.27 | 429.26 | 24.31 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 888 | 287 | 24.72 | 68.29 | 6.27 | 25.44 | 3.36 | 2.94 | 24.74 | 15.33 | 524.19 | 164.79 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_negative_both_risk | revenue_risk | 1313 | 378 | 32.56 | 65.87 | 6.08 | 28.04 | 2.89 | 1.28 | 22.49 | 16.67 | -22.03 | -16.42 | blocked_model_specific_promotion_pr_required |
