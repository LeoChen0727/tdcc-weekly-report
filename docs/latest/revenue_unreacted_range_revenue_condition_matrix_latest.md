# Revenue Unreacted Range Revenue Condition Matrix

- generated_at: `2026-07-12 18:22:30 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_revenue_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 305604 | 276714 | 100.0 | 24.18 | 23.53 | 52.29 | 1.81 | -0.42 | 17.49 | 23.46 | 4.58 | 6.6 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_context_ready | revenue_coverage | 303575 | 274961 | 99.37 | 24.13 | 23.48 | 52.39 | 1.81 | -0.43 | 17.45 | 23.5 | 4.58 | 6.6 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | revenue_production_strong | revenue_strength | 74269 | 65732 | 23.75 | 29.44 | 19.56 | 51.0 | 2.86 | -0.31 | 22.73 | 27.0 | 47.88 | 45.4 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 25729 | 22183 | 8.02 | 31.17 | 18.01 | 50.82 | 3.06 | -0.29 | 24.77 | 29.03 | 100.8 | 64.42 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 9039 | 7768 | 2.81 | 29.74 | 18.92 | 51.34 | 2.58 | -0.38 | 23.84 | 28.95 | 158.96 | 101.33 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 38252 | 33881 | 12.24 | 31.01 | 18.0 | 51.0 | 3.17 | -0.32 | 24.46 | 28.28 | 58.86 | 73.12 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_revenue_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 33597 | 29052 | 10.5 | 32.08 | 17.86 | 50.06 | 3.4 | -0.12 | 25.56 | 28.02 | 76.82 | 66.53 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | price_range_no_attack_without_revenue_gate | baseline | 312677 | 282838 | 100.0 | 24.17 | 23.41 | 52.42 | 1.78 | -0.44 | 17.5 | 23.68 | 670.73 | 354.96 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_context_ready | revenue_coverage | 310648 | 281085 | 99.38 | 24.12 | 23.36 | 52.52 | 1.78 | -0.45 | 17.46 | 23.72 | 670.73 | 354.96 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | revenue_production_strong | revenue_strength | 81017 | 71549 | 25.3 | 29.0 | 19.33 | 51.67 | 2.64 | -0.41 | 22.4 | 27.61 | 2661.08 | 1408.28 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge50 | revenue_strength | 31905 | 27514 | 9.73 | 29.69 | 17.77 | 52.54 | 2.49 | -0.61 | 23.46 | 30.1 | 6871.86 | 3470.54 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest_revenue_yoy_ge100 | revenue_strength | 15093 | 12985 | 4.59 | 27.35 | 18.12 | 54.53 | 1.61 | -1.0 | 21.59 | 31.09 | 14483.04 | 7300.49 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | cumulative_revenue_yoy_ge30 | revenue_strength | 44179 | 38958 | 13.77 | 30.15 | 17.77 | 52.08 | 2.75 | -0.51 | 23.74 | 29.15 | 4784.91 | 2573.8 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_numerical_anomalies | latest30_and_cumulative20 | revenue_strength_combo | 39012 | 33703 | 11.92 | 30.96 | 17.67 | 51.37 | 2.92 | -0.39 | 24.59 | 28.96 | 5515.28 | 2849.12 | blocked_operation_rule_and_model_specific_promotion_pr_required |
