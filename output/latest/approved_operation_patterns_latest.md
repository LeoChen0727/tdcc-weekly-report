# Approved Operation Patterns

- generated_at: `2026-06-29 10:12:18 Asia/Taipei`
- purpose: explicit promotion gate from research/backtest evidence to daily operation guidance
- rule: raw research backtest rows can remain research-only; this artifact is the explicit approval layer

| model_id | operation_module_id | approval_version | approved_for_daily | operation_directive_level | entry_rule_id | stop_loss_rule_id | exit_rule_id | buy_filter_id | evidence_positive_rank_rows | best_evidence_sample_size | best_evidence_win_rate | best_evidence_median_return | evidence_source_kind | approval_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | volume_breakout_confirmed_operation_v1 | volume_breakout_operation_v1_20260615 | True | approved_daily_operation_guidance | confirmation_next_open | signal_low_stop | signal_low_stop_or_fixed_10d_close | positive_evidence_oos_rank_v1 | 4 | 10 | 70.0 | 16.9871 |  | 以目前 repo 可用歷史資料批准放量攻擊 v1 操作建議。後續固定 research/backtest 可用新版 approval_version 調整參數與條件。 |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | w_bottom_early_entry_operation_v2_20260629 | True | approved_daily_operation_guidance | right_low_signal_next_open | w_structure_low_close_stop | d20_gain10_else_d40_close | smooth_core_mainstream_right_rebound_5_20_bull | 1 | 31 | 58.0645 | 6.2374 | w_bottom_early_entry_operation_spec | W底右低點早期進場 v2 已批准為 daily operation guidance；raw research candidate rows 仍維持 research-only，正式 production 使用只能讀 approval artifact。 |
