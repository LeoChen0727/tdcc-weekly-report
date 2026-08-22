# Revenue Unreacted Range Revenue Condition Matrix

- generated_at: `2026-08-23 07:25:15 Asia/Taipei`
- status: `not_production_ready_research_only`
- production_change: `none`
- revenue_join_rule: `source_table_date <= signal_date`
- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.

| anomaly_exclusion_basis | condition_test_id | condition_family | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avg_revenue_latest_yoy_pct | avg_revenue_cumulative_yoy_pct | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_unresolved_anomaly_candidates_sensitivity_only | price_range_no_attack_without_revenue_gate | baseline | 369586 | 336501 | 100.0 | 22.58 | 23.12 | 54.3 | 1.04 | -0.72 | 16.17 | 25.58 | 6.13 | 7.29 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | revenue_context_ready | revenue_coverage | 363433 | 333090 | 98.99 | 22.54 | 22.96 | 54.49 | 1.03 | -0.75 | 16.16 | 25.71 | 6.13 | 7.29 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | revenue_production_strong | revenue_strength | 93804 | 83220 | 24.73 | 27.17 | 19.18 | 53.65 | 1.61 | -0.81 | 20.78 | 29.89 | 49.48 | 45.46 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest_revenue_yoy_ge50 | revenue_strength | 33472 | 29119 | 8.65 | 28.07 | 17.3 | 54.62 | 1.42 | -1.08 | 22.01 | 32.93 | 101.26 | 64.29 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest_revenue_yoy_ge100 | revenue_strength | 11838 | 10285 | 3.06 | 26.59 | 17.79 | 55.61 | 1.01 | -1.3 | 21.13 | 33.41 | 159.29 | 101.29 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | cumulative_revenue_yoy_ge30 | revenue_strength | 47728 | 42698 | 12.69 | 28.3 | 17.38 | 54.32 | 1.67 | -1.01 | 22.17 | 31.93 | 60.59 | 73.73 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| excluding_unresolved_anomaly_candidates_sensitivity_only | latest30_and_cumulative20 | revenue_strength_combo | 42989 | 37855 | 11.25 | 29.08 | 17.25 | 53.67 | 1.71 | -0.9 | 22.93 | 32.17 | 77.52 | 66.18 | blocked_operation_rule_and_model_specific_promotion_pr_required |
| including_unresolved_anomaly_candidates_primary | price_range_no_attack_without_revenue_gate | baseline | 378300 | 344345 | 100.0 | 22.57 | 23.0 | 54.42 | 1.0 | -0.74 | 16.18 | 25.79 | 617.26 | 343.02 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | revenue_context_ready | revenue_coverage | 372147 | 340934 | 99.01 | 22.53 | 22.85 | 54.61 | 1.0 | -0.77 | 16.17 | 25.92 | 617.26 | 343.02 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | revenue_production_strong | revenue_strength | 102175 | 90721 | 26.35 | 26.77 | 19.03 | 54.2 | 1.42 | -0.92 | 20.45 | 30.38 | 2342.83 | 1301.97 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest_revenue_yoy_ge50 | revenue_strength | 41022 | 35958 | 10.44 | 26.92 | 17.28 | 55.8 | 1.01 | -1.33 | 20.91 | 33.54 | 5865.44 | 3006.79 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest_revenue_yoy_ge100 | revenue_strength | 19256 | 16992 | 4.93 | 24.87 | 17.62 | 57.51 | 0.35 | -1.64 | 19.27 | 34.4 | 12334.58 | 6310.53 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | cumulative_revenue_yoy_ge30 | revenue_strength | 55090 | 49283 | 14.31 | 27.47 | 17.29 | 55.24 | 1.32 | -1.19 | 21.44 | 32.58 | 4216.72 | 2384.16 | blocked_pending_root_cause_anomaly_candidate_review |
| including_unresolved_anomaly_candidates_primary | latest30_and_cumulative20 | revenue_strength_combo | 49620 | 43850 | 12.73 | 28.1 | 17.16 | 54.74 | 1.34 | -1.11 | 22.04 | 32.84 | 4727.0 | 2480.86 | blocked_pending_root_cause_anomaly_candidate_review |
