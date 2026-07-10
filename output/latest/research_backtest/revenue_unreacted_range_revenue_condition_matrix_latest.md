# Revenue Unreacted Range Revenue Condition Matrix

- generated_at: `2026-07-10 17:43:21 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_revenue_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 340453 | 309841 | 100.0 | 23.89 | 23.33 | 52.78 | 1.7 | -0.49 | 17.25 | 23.8 | 4.85 | 6.82 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_context_ready | revenue_coverage | 336572 | 307789 | 99.34 | 23.83 | 23.28 | 52.89 | 1.7 | -0.5 | 17.2 | 23.84 | 4.85 | 6.82 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_production_strong | revenue_strength | 83084 | 74499 | 24.04 | 29.4 | 19.57 | 51.02 | 2.82 | -0.31 | 22.57 | 26.89 | 47.36 | 44.99 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 28349 | 24775 | 8.0 | 31.56 | 17.92 | 50.51 | 3.21 | -0.22 | 24.96 | 28.71 | 100.99 | 63.65 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 9972 | 8681 | 2.8 | 29.77 | 18.25 | 51.99 | 2.71 | -0.51 | 23.78 | 29.39 | 159.36 | 99.03 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 42656 | 38248 | 12.34 | 31.09 | 18.07 | 50.83 | 3.15 | -0.28 | 24.34 | 28.06 | 58.04 | 72.54 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 37194 | 32615 | 10.53 | 32.3 | 17.89 | 49.81 | 3.44 | 0.0 | 25.59 | 27.73 | 76.62 | 65.9 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 348224 | 316652 | 100.0 | 23.88 | 23.21 | 52.91 | 1.67 | -0.51 | 17.26 | 24.02 | 862.89 | 510.66 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 344343 | 314600 | 99.35 | 23.82 | 23.16 | 53.02 | 1.66 | -0.52 | 17.21 | 24.06 | 862.89 | 510.66 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 90512 | 80985 | 25.58 | 28.93 | 19.34 | 51.73 | 2.61 | -0.42 | 22.22 | 27.5 | 3374.79 | 1995.3 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 35151 | 30721 | 9.7 | 29.89 | 17.7 | 52.41 | 2.61 | -0.59 | 23.52 | 29.82 | 8845.36 | 5079.35 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 16640 | 14501 | 4.58 | 27.12 | 17.72 | 55.17 | 1.7 | -1.14 | 21.36 | 31.32 | 18661.48 | 10707.9 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 49111 | 43853 | 13.85 | 30.11 | 17.83 | 52.07 | 2.74 | -0.51 | 23.55 | 28.98 | 6114.04 | 3672.02 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 43106 | 37763 | 11.93 | 31.03 | 17.68 | 51.29 | 2.96 | -0.36 | 24.52 | 28.71 | 7080.12 | 4148.2 | blocked_operation_rule_and_model_specific_promotion_pr_required |
