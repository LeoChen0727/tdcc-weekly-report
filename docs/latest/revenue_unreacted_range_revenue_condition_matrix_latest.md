# Revenue Unreacted Range Revenue Condition Matrix

- generated_at: `2026-07-05 00:49:30 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_revenue_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 333970 | 304025 | 100.0 | 23.75 | 23.25 | 53.0 | 1.66 | -0.52 | 17.15 | 23.9 | 4.72 | 6.77 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_context_ready | revenue_coverage | 330654 | 302000 | 99.33 | 23.69 | 23.2 | 53.11 | 1.65 | -0.53 | 17.1 | 23.94 | 4.72 | 6.77 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_production_strong | revenue_strength | 81242 | 72812 | 23.95 | 29.29 | 19.53 | 51.17 | 2.81 | -0.33 | 22.49 | 26.96 | 47.29 | 44.99 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 27538 | 24162 | 7.95 | 31.49 | 17.93 | 50.58 | 3.25 | -0.23 | 24.98 | 28.73 | 101.19 | 63.66 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 9657 | 8499 | 2.8 | 29.73 | 18.18 | 52.09 | 2.74 | -0.53 | 23.79 | 29.34 | 159.56 | 99.02 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 41697 | 37363 | 12.29 | 30.99 | 18.05 | 50.96 | 3.15 | -0.31 | 24.26 | 28.09 | 57.95 | 72.57 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 36174 | 31745 | 10.44 | 32.21 | 17.89 | 49.89 | 3.47 | 0.0 | 25.58 | 27.71 | 76.74 | 66.0 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 341516 | 310658 | 100.0 | 23.74 | 23.13 | 53.13 | 1.63 | -0.54 | 17.16 | 24.12 | 875.75 | 517.03 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 338200 | 308633 | 99.35 | 23.68 | 23.08 | 53.24 | 1.62 | -0.56 | 17.11 | 24.16 | 875.75 | 517.03 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 88448 | 79122 | 25.47 | 28.81 | 19.29 | 51.9 | 2.6 | -0.45 | 22.12 | 27.59 | 3438.75 | 2028.39 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 34141 | 29944 | 9.64 | 29.78 | 17.67 | 52.54 | 2.63 | -0.62 | 23.49 | 29.89 | 9036.05 | 5193.23 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 16130 | 14155 | 4.56 | 27.0 | 17.61 | 55.39 | 1.69 | -1.18 | 21.28 | 31.42 | 19037.59 | 10933.19 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 47950 | 42803 | 13.78 | 29.98 | 17.79 | 52.23 | 2.73 | -0.54 | 23.45 | 29.05 | 6235.51 | 3736.71 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 41907 | 36740 | 11.83 | 30.92 | 17.66 | 51.42 | 2.98 | -0.39 | 24.48 | 28.74 | 7245.62 | 4248.68 | blocked_operation_rule_and_model_specific_promotion_pr_required |
