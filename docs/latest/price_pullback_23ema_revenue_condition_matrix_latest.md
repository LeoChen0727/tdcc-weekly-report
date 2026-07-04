# Price Pullback 23EMA Revenue Condition Matrix

- generated_at: `2026-07-04 21:42:54 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_known_price_or_revenue_anomalies | base_v1_without_revenue_gate | baseline | 4062 | 992 | 100.0 | 26.11 | 31.65 | 42.24 | 3.19 | 0.85 | 27.02 | 18.75 | 9.79 | 7.67 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_context_ready | revenue_coverage | 4057 | 990 | 99.8 | 26.06 | 31.62 | 42.32 | 3.17 | 0.84 | 26.97 | 18.79 | 9.79 | 7.67 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_positive | revenue_direction | 2744 | 706 | 71.17 | 26.77 | 30.45 | 42.78 | 3.39 | 0.76 | 27.9 | 18.56 | 23.32 | 18.09 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_production_strong | revenue_strength | 840 | 260 | 26.21 | 34.23 | 24.23 | 41.54 | 3.77 | 2.03 | 35.77 | 24.23 | 51.8 | 43.91 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 282 | 96 | 9.68 | 38.54 | 26.04 | 35.42 | 4.14 | 2.43 | 39.58 | 23.96 | 94.33 | 64.55 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 398 | 123 | 12.4 | 38.21 | 21.14 | 40.65 | 4.06 | 2.32 | 39.84 | 22.76 | 70.08 | 73.81 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 443 | 148 | 14.92 | 38.51 | 23.65 | 37.84 | 4.06 | 2.78 | 39.86 | 22.3 | 71.62 | 56.89 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_2m | revenue_turnaround | 920 | 261 | 26.31 | 26.44 | 31.03 | 42.53 | 2.85 | 0.97 | 26.82 | 18.01 | 22.86 | 8.83 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_improving_3m | revenue_turnaround | 224 | 61 | 6.15 | 21.31 | 39.34 | 39.34 | 2.03 | 0.49 | 24.59 | 19.67 | 35.28 | 19.59 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1179 | 310 | 31.25 | 23.87 | 35.81 | 40.32 | 2.82 | 0.93 | 25.16 | 17.1 | 24.12 | 8.62 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive | revenue_turnaround | 868 | 254 | 25.6 | 25.59 | 29.53 | 44.88 | 3.1 | 0.26 | 27.17 | 17.32 | 18.04 | 2.75 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 406 | 113 | 11.39 | 23.89 | 28.32 | 47.79 | 2.92 | 0.0 | 24.78 | 15.04 | 14.84 | -5.95 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 293 | 90 | 9.07 | 24.44 | 28.89 | 46.67 | 2.46 | 0.32 | 26.67 | 25.56 | 24.05 | 7.49 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 867 | 262 | 26.41 | 30.53 | 26.72 | 42.75 | 3.54 | 1.04 | 32.44 | 22.14 | 34.43 | 13.24 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 770 | 225 | 22.68 | 27.56 | 29.33 | 43.11 | 3.57 | 0.66 | 29.33 | 16.44 | 19.47 | 1.46 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 843 | 243 | 24.5 | 26.34 | 32.51 | 41.15 | 2.96 | 1.13 | 27.16 | 18.52 | 24.15 | 8.07 | blocked_model_specific_promotion_pr_required |
| excluding_known_price_or_revenue_anomalies | revenue_negative_both_risk | revenue_risk | 1308 | 328 | 33.06 | 25.3 | 34.45 | 40.24 | 2.86 | 0.9 | 25.61 | 18.9 | -20.17 | -16.46 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | base_v1_without_revenue_gate | baseline | 4192 | 1023 | 100.0 | 26.1 | 31.87 | 42.03 | 3.32 | 0.88 | 27.08 | 18.87 | 278.17 | 67.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 4187 | 1021 | 99.8 | 26.05 | 31.83 | 42.12 | 3.29 | 0.87 | 27.03 | 18.9 | 278.17 | 67.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_positive | revenue_direction | 2869 | 736 | 71.95 | 26.77 | 30.71 | 42.53 | 3.56 | 0.81 | 27.99 | 18.75 | 396.31 | 100.52 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 964 | 290 | 28.35 | 33.45 | 25.52 | 41.03 | 3.85 | 2.04 | 35.17 | 24.14 | 998.75 | 250.44 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 396 | 124 | 12.12 | 36.29 | 29.03 | 34.68 | 4.41 | 2.6 | 37.9 | 21.77 | 2307.57 | 518.1 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 515 | 151 | 14.76 | 36.42 | 24.5 | 39.07 | 4.33 | 2.53 | 38.41 | 21.85 | 1304.61 | 466.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 551 | 174 | 17.01 | 36.78 | 26.44 | 36.78 | 4.29 | 2.85 | 38.51 | 20.69 | 1140.91 | 386.79 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_2m | revenue_turnaround | 965 | 275 | 26.88 | 26.91 | 31.64 | 41.45 | 3.06 | 1.13 | 27.64 | 17.82 | 473.33 | 104.46 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_improving_3m | revenue_turnaround | 239 | 65 | 6.35 | 21.54 | 41.54 | 36.92 | 2.52 | 0.72 | 26.15 | 18.46 | 92.16 | 86.19 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_improving_2m | revenue_turnaround | 1227 | 323 | 31.57 | 24.46 | 35.91 | 39.63 | 3.01 | 0.98 | 26.01 | 17.03 | 751.72 | 125.61 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive | revenue_turnaround | 909 | 263 | 25.71 | 24.71 | 29.66 | 45.63 | 2.89 | 0.24 | 26.24 | 17.87 | 425.75 | 27.83 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_turn_positive_after_2_negative | revenue_turnaround | 427 | 117 | 11.44 | 23.08 | 28.21 | 48.72 | 2.72 | 0.0 | 23.93 | 16.24 | 859.96 | -1.15 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_yoy_turn_positive | revenue_turnaround | 321 | 98 | 9.58 | 22.45 | 31.63 | 45.92 | 2.32 | 0.57 | 24.49 | 24.49 | 988.41 | 256.06 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_yoy_delta_ge20 | revenue_turnaround | 972 | 289 | 28.25 | 30.45 | 27.34 | 42.21 | 3.66 | 1.19 | 32.18 | 21.45 | 988.49 | 210.24 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | turn_positive_and_cumulative_improving | revenue_turnaround_combo | 810 | 233 | 22.78 | 26.61 | 29.61 | 43.78 | 3.37 | 0.51 | 28.33 | 16.74 | 479.54 | 26.29 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_improving_2m_and_cumulative_improving | revenue_turnaround_combo | 888 | 257 | 25.12 | 26.85 | 33.07 | 40.08 | 3.19 | 1.48 | 28.02 | 18.29 | 506.11 | 110.44 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_negative_both_risk | revenue_risk | 1313 | 330 | 32.26 | 25.15 | 34.85 | 40.0 | 2.85 | 0.9 | 25.45 | 18.79 | -22.66 | -16.89 | blocked_model_specific_promotion_pr_required |
