# Volume Range Breakout V2 Promotion Readiness Audit

- research_id: `volume_range_breakout_v2_promotion_readiness_audit`
- artifact_version: `volume_range_breakout_v2_promotion_readiness_audit_20260709`
- source_research_id: `volume_range_breakout_v2_research_contract`
- status: research-only; no production registry, ranking, adapter, packet, or PDF change.
- base metrics use confirmed same-stock non-overlap samples only.
- D+10/D+15/D+20/D+30 are compared with no-stop and close-confirmed MA20/EMA23 stop.
- TDCC, 23EMA, and low-base redefinition rows are stratification-only, not hidden gates.

## Base Performance

| model_id | holding_days | stop_policy_id | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | invalid_return_count | metric_threshold_met |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | 223 | 45.74 | 53.36 | 2.8868 | -1.1658 | 0 | False |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | 221 | 49.77 | 50.23 | 4.0468 | -0.3468 | 2 | False |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | 218 | 45.87 | 52.75 | 4.0275 | -1.3444 | 5 | False |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | 201 | 42.29 | 57.71 | 5.3186 | -3.7234 | 22 | False |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | 223 | 45.74 | 53.36 | 2.8868 | -1.1658 | 0 | False |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | 221 | 49.77 | 50.23 | 4.0477 | -0.3468 | 2 | False |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | 218 | 45.87 | 52.75 | 4.0648 | -1.3444 | 5 | False |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | 201 | 42.79 | 57.21 | 5.6387 | -3.2915 | 22 | False |
| volume_range_breakout_v2_momentum_continuation | 10 | ma20_ema23_close_stop_4d | 353 | 57.22 | 42.49 | 6.36 | 2.673 | 0 | False |
| volume_range_breakout_v2_momentum_continuation | 15 | ma20_ema23_close_stop_4d | 335 | 62.09 | 37.61 | 9.9636 | 6.3342 | 18 | True |
| volume_range_breakout_v2_momentum_continuation | 20 | ma20_ema23_close_stop_4d | 324 | 60.8 | 38.89 | 13.57 | 6.1762 | 29 | True |
| volume_range_breakout_v2_momentum_continuation | 30 | ma20_ema23_close_stop_4d | 302 | 65.23 | 34.77 | 19.7858 | 8.8089 | 51 | True |
| volume_range_breakout_v2_momentum_continuation | 10 | no_stop_reference | 353 | 57.22 | 42.49 | 6.36 | 2.673 | 0 | False |
| volume_range_breakout_v2_momentum_continuation | 15 | no_stop_reference | 335 | 62.09 | 37.61 | 9.975 | 6.3342 | 18 | True |
| volume_range_breakout_v2_momentum_continuation | 20 | no_stop_reference | 324 | 61.42 | 38.27 | 13.831 | 6.1762 | 29 | True |
| volume_range_breakout_v2_momentum_continuation | 30 | no_stop_reference | 302 | 66.56 | 33.11 | 20.3824 | 9.3796 | 51 | True |

## Metric Threshold Rows

| model_id | holding_days | stop_policy_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | promotion_blockers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_momentum_continuation | 15 | ma20_ema23_close_stop_4d | 335 | 62.09 | 9.9636 | 6.3342 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |
| volume_range_breakout_v2_momentum_continuation | 20 | ma20_ema23_close_stop_4d | 324 | 60.8 | 13.57 | 6.1762 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |
| volume_range_breakout_v2_momentum_continuation | 30 | ma20_ema23_close_stop_4d | 302 | 65.23 | 19.7858 | 8.8089 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |
| volume_range_breakout_v2_momentum_continuation | 15 | no_stop_reference | 335 | 62.09 | 9.975 | 6.3342 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |
| volume_range_breakout_v2_momentum_continuation | 20 | no_stop_reference | 324 | 61.42 | 13.831 | 6.1762 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |
| volume_range_breakout_v2_momentum_continuation | 30 | no_stop_reference | 302 | 66.56 | 20.3824 | 9.3796 | research_only_not_production_contract;no_registry_change;no_operation_adapter;invalid_return_rows_need_review |

## Low-Base Redefinition Matrix

| model_id | holding_days | stop_policy_id | stratification_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | off240_le50_range240_le80 | 129 | 37.21 | 0.1951 | -2.9046 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | off120_le40_range120_le60 | 125 | 36.8 | 0.4892 | -3.3019 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | off240_le40_range240_le60 | 83 | 33.73 | -1.8865 | -4.6053 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | off120_le30_range120_le45 | 77 | 32.47 | -1.8138 | -4.6053 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | ma20_ema23_close_stop_4d | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 36.59 | 0.8219 | -3.3019 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | off240_le50_range240_le80 | 129 | 37.21 | 0.1951 | -2.9046 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | off120_le40_range120_le60 | 125 | 36.8 | 0.4892 | -3.3019 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | off240_le40_range240_le60 | 83 | 33.73 | -1.8865 | -4.6053 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | off120_le30_range120_le45 | 77 | 32.47 | -1.8138 | -4.6053 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 10 | no_stop_reference | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 36.59 | 0.8219 | -3.3019 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | off240_le50_range240_le80 | 127 | 38.58 | 0.0773 | -3.0837 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | off120_le40_range120_le60 | 123 | 38.21 | 0.435 | -3.0812 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | off240_le40_range240_le60 | 81 | 30.86 | -2.5178 | -4.1667 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | off120_le30_range120_le45 | 75 | 30.67 | -1.9427 | -3.4865 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | ma20_ema23_close_stop_4d | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 46.34 | 1.1359 | -1.7682 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | off240_le50_range240_le80 | 127 | 38.58 | 0.079 | -3.0837 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | off120_le40_range120_le60 | 123 | 38.21 | 0.4367 | -3.0812 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | off240_le40_range240_le60 | 81 | 30.86 | -2.5152 | -4.1667 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | off120_le30_range120_le45 | 75 | 30.67 | -1.9427 | -3.4865 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 15 | no_stop_reference | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 46.34 | 1.1411 | -1.7682 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | off240_le50_range240_le80 | 124 | 37.9 | -0.4226 | -3.5739 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | off120_le40_range120_le60 | 122 | 31.97 | -0.0329 | -4.2431 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | off240_le40_range240_le60 | 80 | 26.25 | -3.3113 | -4.7592 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | off120_le30_range120_le45 | 74 | 27.03 | -2.2427 | -4.4265 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | ma20_ema23_close_stop_4d | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 34.15 | 0.1652 | -5.5866 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | off240_le50_range240_le80 | 124 | 37.9 | -0.3791 | -3.5739 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | off120_le40_range120_le60 | 122 | 31.97 | 0.0036 | -4.2431 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | off240_le40_range240_le60 | 80 | 26.25 | -3.3 | -4.7592 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | off120_le30_range120_le45 | 74 | 27.03 | -2.1713 | -4.4265 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 20 | no_stop_reference | off120_le40_range120_le60_ma60_gt_ma120 | 41 | 34.15 | 0.1891 | -5.5866 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | off240_le50_range240_le80 | 112 | 36.61 | 0.348 | -5.2377 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | off120_le40_range120_le60 | 106 | 33.02 | -0.1819 | -6.7178 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | off240_le40_range240_le60 | 70 | 27.14 | -4.309 | -7.2125 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | off120_le30_range120_le45 | 63 | 26.98 | -1.7686 | -7.4519 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | ma20_ema23_close_stop_4d | off120_le40_range120_le60_ma60_gt_ma120 | 38 | 34.21 | 0.6094 | -6.4031 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | off240_le50_range240_le80 | 112 | 37.5 | 0.852 | -4.9833 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | off120_le40_range120_le60 | 106 | 33.96 | 0.3945 | -6.7178 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | off240_le40_range240_le60 | 70 | 28.57 | -3.7126 | -7.0923 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | off120_le30_range120_le45 | 63 | 28.57 | -1.2657 | -6.9731 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | 30 | no_stop_reference | off120_le40_range120_le60_ma60_gt_ma120 | 38 | 34.21 | 1.3362 | -5.7225 | risk_stratification_candidate_not_gate |

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_promotion_readiness_audit_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_promotion_readiness_audit_detail_latest.csv`
- matrix_csv: `output/latest/research_backtest/volume_range_breakout_v2_promotion_readiness_audit_matrix_latest.csv`
