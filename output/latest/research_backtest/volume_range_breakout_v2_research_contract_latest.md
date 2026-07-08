# Volume Range Breakout V2 Research Contract

- research_id: `volume_range_breakout_v2_research_contract`
- artifact_version: `volume_range_breakout_v2_research_contract_20260709`
- source_research_id: `volume_range_breakout_v2_split_feature_audit`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- status: research-only; does not change `stock_model_contract_registry.csv`, production ranking, operation adapter, or PDF behavior.
- Base metrics use confirmed same-stock non-overlap samples only.
- TDCC top20 and 23EMA-like technical conditions are stratification-only rows, not hidden gates.
- The two v2 model ids are mutually exclusive by split_group_id; their union equals the current raw v2 confirmed non-overlap sample.

## Model Contracts

| model_id | model_zh | candidate_condition_id | confirmation_rule_id | entry_rule_id | base_metric_scope | extra_condition_policy |
| --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_momentum_continuation | 動能放量攻擊 | prev60_breakout_momentum_continuation | next_day_continuation_confirmed_close_only | confirmation_next_open | confirmed_same_stock_non_overlap_only | stratification_only_no_hidden_gate |
| volume_range_breakout_v2_low_base_consolidation | 低位盤整放量突破 | prev60_breakout_low_base_consolidated | next_day_continuation_confirmed_close_only | confirmation_next_open | confirmed_same_stock_non_overlap_only | stratification_only_no_hidden_gate |

## Base Performance

| model_id | exit_policy_id | sample_size | win_rate_pct | neutral_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | stop_exit_count | invalid_return_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | 324.0 | 61.42 | 0.31 | 38.27 | 13.831 | 6.1762 | 0.0 | 29.0 |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | 324.0 | 60.8 | 0.31 | 38.89 | 13.57 | 6.1762 | 17.0 | 29.0 |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | 218.0 | 45.87 | 1.38 | 52.75 | 4.0648 | -1.3444 | 0.0 | 5.0 |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | 218.0 | 45.87 | 1.38 | 52.75 | 4.0275 | -1.3444 | 10.0 | 5.0 |

## TDCC Stratification

| model_id | exit_policy_id | stratification_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tdcc_weekly_increase_top20 | 6 | 50.0 | 2.8806 | 2.946 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tdcc_any_top20 | 6 | 50.0 | 2.8806 | 2.946 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tdcc_weekly_increase_top20 | 6 | 50.0 | 2.8806 | 2.946 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tdcc_any_top20 | 6 | 50.0 | 2.8806 | 2.946 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tdcc_weekly_increase_top20 | 8 | 75.0 | 31.6051 | 34.9126 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tdcc_any_top20 | 10 | 60.0 | 23.5013 | 9.4323 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tdcc_weekly_increase_top20 | 8 | 75.0 | 31.6051 | 34.9126 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tdcc_any_top20 | 10 | 60.0 | 23.5013 | 9.4323 | thin_sample_do_not_use_as_gate |

## 23EMA / Technical Stratification

| model_id | exit_policy_id | stratification_id | sample_size | win_rate_pct | avg_return_pct | median_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_close_gt_ema23 | 218 | 45.87 | 4.0648 | -1.3444 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_dist_ema23_0_to_15 | 134 | 40.3 | 2.069 | -2.6132 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_ret20_0_to_25 | 181 | 44.75 | 4.0716 | -1.9211 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_close_gt_ma20 | 218 | 45.87 | 4.0648 | -1.3444 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_ma20_gt_ma60 | 168 | 48.21 | 4.5285 | -0.388 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_no_stop_reference | tech_ma60_gt_ma120 | 123 | 57.72 | 6.7783 | 2.8758 | positive_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_close_gt_ema23 | 218 | 45.87 | 4.0275 | -1.3444 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_dist_ema23_0_to_15 | 134 | 40.3 | 2.022 | -2.6132 | risk_stratification_candidate_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_ret20_0_to_25 | 181 | 44.75 | 4.0266 | -1.9211 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_close_gt_ma20 | 218 | 45.87 | 4.0275 | -1.3444 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_ma20_gt_ma60 | 168 | 48.21 | 4.4927 | -0.388 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_low_base_consolidation | fixed_d20_close_with_23ema_close_stop | tech_ma60_gt_ma120 | 123 | 57.72 | 6.7403 | 2.8758 | positive_stratification_candidate_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_close_gt_ema23 | 324 | 61.42 | 13.831 | 6.1762 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_dist_ema23_0_to_15 | 17 | 82.35 | 14.6485 | 7.5472 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_ret20_0_to_25 | 74 | 66.22 | 17.615 | 10.7063 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_close_gt_ma20 | 324 | 61.42 | 13.831 | 6.1762 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_ma20_gt_ma60 | 306 | 62.42 | 14.2557 | 6.8213 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_no_stop_reference | tech_ma60_gt_ma120 | 261 | 64.37 | 14.7456 | 7.7908 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_close_gt_ema23 | 324 | 60.8 | 13.57 | 6.1762 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_dist_ema23_0_to_15 | 17 | 82.35 | 14.6485 | 7.5472 | thin_sample_do_not_use_as_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_ret20_0_to_25 | 74 | 64.86 | 17.5215 | 10.7063 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_close_gt_ma20 | 324 | 60.8 | 13.57 | 6.1762 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_ma20_gt_ma60 | 306 | 61.76 | 13.9794 | 6.8213 | mixed_or_weak_stratification_not_gate |
| volume_range_breakout_v2_momentum_continuation | fixed_d20_close_with_23ema_close_stop | tech_ma60_gt_ma120 | 261 | 64.37 | 14.637 | 7.7908 | mixed_or_weak_stratification_not_gate |

## Outputs

- contract_csv: `output/latest/research_backtest/volume_range_breakout_v2_research_contract_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_research_contract_detail_latest.csv`
- stratification_csv: `output/latest/research_backtest/volume_range_breakout_v2_research_contract_stratification_latest.csv`
