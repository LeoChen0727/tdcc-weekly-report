# Revenue Unreacted Range Revenue Condition Matrix

- generated_at: `2026-07-14 14:45:44 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_unresolved_anomaly_candidates_sensitivity_only | price_range_no_attack_without_revenue_gate | baseline | 307246 | 278256 | 100.0 | 24.15 | 23.54 | 52.31 | 1.81 | -0.42 | 17.47 | 23.49 | 4.62 | 6.62 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | revenue_context_ready | revenue_coverage | 305207 | 276496 | 99.37 | 24.1 | 23.49 | 52.41 | 1.81 | -0.43 | 17.43 | 23.54 | 4.62 | 6.62 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | revenue_production_strong | revenue_strength | 74781 | 66170 | 23.78 | 29.39 | 19.56 | 51.05 | 2.83 | -0.32 | 22.69 | 27.06 | 47.9 | 45.39 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest_revenue_yoy_ge50 | revenue_strength | 25952 | 22342 | 8.03 | 31.11 | 17.99 | 50.9 | 3.03 | -0.31 | 24.7 | 29.11 | 100.73 | 64.4 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest_revenue_yoy_ge100 | revenue_strength | 9122 | 7810 | 2.81 | 29.69 | 18.87 | 51.43 | 2.55 | -0.42 | 23.76 | 29.05 | 158.9 | 101.34 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | cumulative_revenue_yoy_ge30 | revenue_strength | 38518 | 34102 | 12.26 | 30.95 | 17.98 | 51.06 | 3.13 | -0.33 | 24.42 | 28.37 | 58.89 | 73.1 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest30_and_cumulative20 | revenue_strength_combo | 33879 | 29285 | 10.52 | 32.02 | 17.85 | 50.13 | 3.36 | -0.13 | 25.51 | 28.12 | 76.77 | 66.48 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_unresolved_anomaly_candidates_primary | price_range_no_attack_without_revenue_gate | baseline | 314376 | 284427 | 100.0 | 24.15 | 23.41 | 52.44 | 1.77 | -0.44 | 17.49 | 23.72 | 669.02 | 353.62 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | revenue_context_ready | revenue_coverage | 312337 | 282667 | 99.38 | 24.1 | 23.36 | 52.54 | 1.77 | -0.45 | 17.45 | 23.76 | 669.02 | 353.62 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | revenue_production_strong | revenue_strength | 81585 | 72033 | 25.33 | 28.96 | 19.33 | 51.71 | 2.62 | -0.42 | 22.36 | 27.67 | 2651.33 | 1401.42 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest_revenue_yoy_ge50 | revenue_strength | 32179 | 27716 | 9.74 | 29.65 | 17.74 | 52.61 | 2.46 | -0.63 | 23.41 | 30.17 | 6842.51 | 3451.23 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest_revenue_yoy_ge100 | revenue_strength | 15226 | 13070 | 4.6 | 27.32 | 18.07 | 54.61 | 1.58 | -1.02 | 21.53 | 31.16 | 14432.2 | 7265.3 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | cumulative_revenue_yoy_ge30 | revenue_strength | 44496 | 39222 | 13.79 | 30.1 | 17.75 | 52.15 | 2.72 | -0.53 | 23.7 | 29.23 | 4767.47 | 2561.15 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest30_and_cumulative20 | revenue_strength_combo | 39340 | 33976 | 11.95 | 30.9 | 17.65 | 51.45 | 2.89 | -0.41 | 24.53 | 29.06 | 5487.89 | 2831.24 | blocked_pending_root_cause_anomaly_candidate_review |
