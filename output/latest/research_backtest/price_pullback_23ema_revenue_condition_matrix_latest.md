# Price Pullback 23EMA Revenue Condition Matrix

- generated_at: `2026-07-04 18:45:18 Asia/Taipei`
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
| excluding_known_price_or_revenue_anomalies | revenue_negative_both_risk | revenue_risk | 1308 | 328 | 33.06 | 25.3 | 34.45 | 40.24 | 2.86 | 0.9 | 25.61 | 18.9 | -20.17 | -16.46 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | base_v1_without_revenue_gate | baseline | 4192 | 1023 | 100.0 | 26.1 | 31.87 | 42.03 | 3.32 | 0.88 | 27.08 | 18.87 | 278.17 | 67.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 4187 | 1021 | 99.8 | 26.05 | 31.83 | 42.12 | 3.29 | 0.87 | 27.03 | 18.9 | 278.17 | 67.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_positive | revenue_direction | 2869 | 736 | 71.95 | 26.77 | 30.71 | 42.53 | 3.56 | 0.81 | 27.99 | 18.75 | 396.31 | 100.52 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 964 | 290 | 28.35 | 33.45 | 25.52 | 41.03 | 3.85 | 2.04 | 35.17 | 24.14 | 998.75 | 250.44 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 396 | 124 | 12.12 | 36.29 | 29.03 | 34.68 | 4.41 | 2.6 | 37.9 | 21.77 | 2307.57 | 518.1 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 515 | 151 | 14.76 | 36.42 | 24.5 | 39.07 | 4.33 | 2.53 | 38.41 | 21.85 | 1304.61 | 466.13 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 551 | 174 | 17.01 | 36.78 | 26.44 | 36.78 | 4.29 | 2.85 | 38.51 | 20.69 | 1140.91 | 386.79 | blocked_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_negative_both_risk | revenue_risk | 1313 | 330 | 32.26 | 25.15 | 34.85 | 40.0 | 2.85 | 0.9 | 25.45 | 18.79 | -22.66 | -16.89 | blocked_model_specific_promotion_pr_required |
