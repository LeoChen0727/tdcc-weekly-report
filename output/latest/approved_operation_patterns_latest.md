# Approved Operation Patterns

- generated_at: `2026-06-20 07:40:19 Asia/Taipei`
- purpose: explicit promotion gate from research/backtest evidence to daily operation guidance
- rule: raw research backtest rows can remain research-only; this artifact is the explicit approval layer

| model_id | operation_module_id | approval_version | approved_for_daily | operation_directive_level | entry_rule_id | stop_loss_rule_id | exit_rule_id | buy_filter_id | evidence_positive_rank_rows | best_evidence_sample_size | best_evidence_win_rate | best_evidence_median_return | approval_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | volume_breakout_confirmed_operation_v1 | volume_breakout_operation_v1_20260615 | True | approved_daily_operation_guidance | confirmation_next_open | signal_low_stop | signal_low_stop_or_fixed_10d_close | positive_evidence_oos_rank_v1 | 4 | 10 | 70.0 | 16.9871 | 以目前 repo 可用歷史資料批准放量攻擊 v1 操作建議。後續固定 research/backtest 可用新版 approval_version 調整參數與條件。 |
