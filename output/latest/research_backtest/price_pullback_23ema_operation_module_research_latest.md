# Price Pullback 23EMA Operation Module Research

- generated_at: `2026-06-29 23:34:32 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- scope: advisory operation module candidates only; this does not approve daily production use
- entry_basis: `signal_date_next_open`
- win_definition: target hit before stop
- neutral_definition: no target/stop by D+20 and D+20 close return >= 0%
- failure_definition: stop hit before target, or no target/stop by D+20 and D+20 close return < 0%
- same_day_rule: if target and stop are first seen on the same daily candle, classify as `same_day_unresolved`
- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use

| entry_filter_id | operation_module_candidate_id | selected_stock_days | mature_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | same_day_unresolved_rate_pct | avg_d20_close_return_pct | avg_realized_or_d20_days | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | next_open_tp5_intraday_stop5_d20_close_exit | 298431 | 270127 | 41.03 | 7.82 | 51.03 | 0.11 | 1.63 | 9.34 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_tp5_structure_stop_d20_close_exit | 298431 | 260743 | 24.41 | 4.1 | 70.98 | 0.52 | 1.65 | 5.29 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_tp8_intraday_stop5_d20_close_exit | 298431 | 270127 | 28.35 | 13.76 | 57.87 | 0.02 | 1.63 | 11.04 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_tp8_structure_stop_d20_close_exit | 298431 | 260743 | 17.08 | 6.98 | 75.84 | 0.1 | 1.65 | 6.19 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_prev20_high_breakout_monthline_stop1pct_2d_d20_close_exit | 298431 | 262544 | 28.14 | 2.09 | 69.74 | 0.03 | 1.63 | 4.97 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_prev20_high_breakout_monthline_stop2pct_2d_d20_close_exit | 298431 | 262544 | 32.52 | 4.69 | 62.78 | 0.01 | 1.63 | 6.81 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_prev20_high_breakout_monthline_stop1pct_3d_d20_close_exit | 298431 | 262544 | 31.79 | 3.53 | 64.67 | 0.01 | 1.63 | 6.44 | blocked_exact_daily_row_parity_and_operation_approval_required |
| baseline_replay | next_open_prev20_high_breakout_monthline_stop2pct_3d_d20_close_exit | 298431 | 262544 | 35.59 | 6.5 | 57.91 | 0.0 | 1.63 | 8.28 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_tp5_intraday_stop5_d20_close_exit | 30382 | 26748 | 39.44 | 7.9 | 52.53 | 0.12 | 1.25 | 9.31 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_tp5_structure_stop_d20_close_exit | 30382 | 25517 | 32.88 | 5.55 | 61.21 | 0.36 | 1.24 | 7.2 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_tp8_intraday_stop5_d20_close_exit | 30382 | 26748 | 27.59 | 13.62 | 58.76 | 0.02 | 1.25 | 10.91 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_tp8_structure_stop_d20_close_exit | 30382 | 25517 | 23.42 | 9.74 | 66.75 | 0.09 | 1.24 | 8.47 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop1pct_2d_d20_close_exit | 30382 | 25751 | 50.08 | 1.69 | 48.2 | 0.03 | 1.24 | 4.71 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop2pct_2d_d20_close_exit | 30382 | 25751 | 53.75 | 3.37 | 42.87 | 0.01 | 1.24 | 6.16 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop1pct_3d_d20_close_exit | 30382 | 25751 | 52.87 | 2.57 | 44.55 | 0.01 | 1.24 | 5.72 | blocked_exact_daily_row_parity_and_operation_approval_required |
| volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop2pct_3d_d20_close_exit | 30382 | 25751 | 55.89 | 4.28 | 39.84 | 0.0 | 1.24 | 7.11 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_tp5_intraday_stop5_d20_close_exit | 15913 | 13938 | 38.87 | 8.72 | 52.27 | 0.14 | 1.11 | 9.52 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_tp5_structure_stop_d20_close_exit | 15913 | 13300 | 32.91 | 6.34 | 60.42 | 0.33 | 1.1 | 7.55 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_tp8_intraday_stop5_d20_close_exit | 15913 | 13938 | 26.98 | 14.64 | 58.36 | 0.03 | 1.11 | 11.15 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_tp8_structure_stop_d20_close_exit | 15913 | 13300 | 23.29 | 10.76 | 65.86 | 0.08 | 1.1 | 8.87 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop1pct_2d_d20_close_exit | 15913 | 13419 | 52.0 | 1.86 | 46.1 | 0.04 | 1.11 | 4.67 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop2pct_2d_d20_close_exit | 15913 | 13419 | 55.66 | 3.7 | 40.62 | 0.02 | 1.11 | 6.12 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop1pct_3d_d20_close_exit | 15913 | 13419 | 54.83 | 2.79 | 42.38 | 0.01 | 1.11 | 5.66 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.2 | next_open_prev20_high_breakout_monthline_stop2pct_3d_d20_close_exit | 15913 | 13419 | 57.68 | 4.57 | 37.75 | 0.0 | 1.11 | 7.06 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_tp5_intraday_stop5_d20_close_exit | 10239 | 8891 | 38.36 | 8.2 | 53.32 | 0.11 | 0.94 | 9.3 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_tp5_structure_stop_d20_close_exit | 10239 | 8488 | 33.87 | 6.09 | 59.66 | 0.38 | 0.93 | 7.69 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_tp8_intraday_stop5_d20_close_exit | 10239 | 8891 | 26.57 | 13.8 | 59.62 | 0.01 | 0.94 | 10.89 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_tp8_structure_stop_d20_close_exit | 10239 | 8488 | 24.02 | 10.5 | 65.37 | 0.11 | 0.93 | 9.03 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_prev20_high_breakout_monthline_stop1pct_2d_d20_close_exit | 10239 | 8565 | 55.17 | 1.75 | 43.05 | 0.04 | 0.94 | 4.47 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_prev20_high_breakout_monthline_stop2pct_2d_d20_close_exit | 10239 | 8565 | 58.42 | 3.39 | 38.16 | 0.04 | 0.94 | 5.81 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_prev20_high_breakout_monthline_stop1pct_3d_d20_close_exit | 10239 | 8565 | 57.66 | 2.63 | 39.7 | 0.01 | 0.94 | 5.39 | blocked_exact_daily_row_parity_and_operation_approval_required |
| solid_volume_red_k_vol1.5 | next_open_prev20_high_breakout_monthline_stop2pct_3d_d20_close_exit | 10239 | 8565 | 60.34 | 4.21 | 35.45 | 0.0 | 0.94 | 6.68 | blocked_exact_daily_row_parity_and_operation_approval_required |
