# Price Pullback 23EMA Feature Confirmation Research

- generated_at: `2026-06-30 10:05:05 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- scope: advisory feature confirmation only; this does not approve daily production use
- fixed_operation_module_candidate_id: `next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit`
- entry_basis: `signal_date_next_open` after production proxy replay plus the feature filter under test
- target: previous 20-day high breakout before stop through D+20
- stop: close stays at least 4% below lower of MA20 and EMA23 for 4 consecutive trading days
- blocked rows: revenue and market background are documented as data/join gaps, not scored as backtest results
- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use

| feature_filter_id | feature_family | feature_test_status | data_status | selected_stock_days | selected_share_of_baseline_pct | mature_count | mature_share_of_baseline_pct | win_rate_pct | delta_vs_baseline_win_rate_pct | neutral_rate_pct | failure_rate_pct | delta_vs_baseline_failure_rate_pct | same_day_unresolved_rate_pct | avg_realized_return_pct | delta_vs_baseline_avg_realized_return_pct | avg_realized_or_d20_days | delta_vs_baseline_avg_realized_or_d20_days | promotion_readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_replay | baseline | tested_point_in_time | available_point_in_time_research_frame | 298431 | 100.0 | 261695 | 100.0 | 41.32 | 0.0 | 12.87 | 45.81 | 0.0 | 0.0 | 0.38 | 0.0 | 12.49 | 0.0 | blocked_exact_daily_row_parity_and_operation_approval_required |
| prior_ext20_ema10_runup20_pullback5 | prior_extension | tested_point_in_time | available_point_in_time_research_frame | 58473 | 19.59 | 48853 | 18.67 | 29.15 | -12.17 | 14.72 | 56.14 | 10.33 | 0.0 | 1.18 | 0.8 | 12.39 | -0.1 | blocked_exact_daily_row_parity_and_operation_approval_required |
| macd_hist_gt0 | technical | tested_point_in_time | available_point_in_time_research_frame | 126901 | 42.52 | 112118 | 42.84 | 53.77 | 12.45 | 8.38 | 37.85 | -7.96 | 0.0 | 0.22 | -0.16 | 11.5 | -0.99 | blocked_exact_daily_row_parity_and_operation_approval_required |
| kd_bullish_not_overheated | technical | tested_point_in_time | available_point_in_time_research_frame | 129264 | 43.31 | 113850 | 43.5 | 44.93 | 3.61 | 11.73 | 43.34 | -2.47 | 0.0 | 0.1 | -0.28 | 12.28 | -0.21 | blocked_exact_daily_row_parity_and_operation_approval_required |
| macd_kd_confirm | technical | tested_point_in_time | available_point_in_time_research_frame | 67107 | 22.49 | 59731 | 22.82 | 55.63 | 14.31 | 7.96 | 36.41 | -9.4 | 0.0 | 0.06 | -0.32 | 11.18 | -1.31 | blocked_exact_daily_row_parity_and_operation_approval_required |
| rsi14_40_70 | technical | tested_point_in_time | available_point_in_time_research_frame | 189878 | 63.63 | 165777 | 63.35 | 49.31 | 7.99 | 9.79 | 40.9 | -4.91 | 0.0 | 0.46 | 0.08 | 12.1 | -0.39 | blocked_exact_daily_row_parity_and_operation_approval_required |
| bb_width_not_extreme | technical | tested_point_in_time | available_point_in_time_research_frame | 159228 | 53.36 | 137972 | 52.72 | 44.49 | 3.17 | 11.45 | 44.06 | -1.75 | 0.0 | 0.45 | 0.07 | 12.25 | -0.24 | blocked_exact_daily_row_parity_and_operation_approval_required |
| obv_above_ma20 | technical_volume | tested_point_in_time | computed_from_point_in_time_price_volume | 129702 | 43.46 | 110495 | 42.22 | 54.55 | 13.23 | 7.94 | 37.5 | -8.31 | 0.0 | 0.33 | -0.05 | 11.2 | -1.29 | blocked_exact_daily_row_parity_and_operation_approval_required |
| tdcc_history_available | chip | tested_point_in_time | available_point_in_time_research_frame | 62891 | 21.07 | 34647 | 13.24 | 46.36 | 5.04 | 14.22 | 39.42 | -6.39 | 0.0 | 1.43 | 1.05 | 11.72 | -0.77 | blocked_exact_daily_row_parity_and_operation_approval_required |
| tdcc_consecutive_up_weeks_ge1 | chip | tested_point_in_time | available_point_in_time_research_frame | 32989 | 11.05 | 17035 | 6.51 | 50.2 | 8.88 | 12.85 | 36.95 | -8.86 | 0.0 | 1.55 | 1.17 | 11.43 | -1.06 | blocked_exact_daily_row_parity_and_operation_approval_required |
| tdcc_high_thresholds_up | chip | tested_point_in_time | available_point_in_time_research_frame | 24807 | 8.31 | 13133 | 5.02 | 51.17 | 9.85 | 12.33 | 36.5 | -9.31 | 0.0 | 1.58 | 1.2 | 11.39 | -1.1 | blocked_exact_daily_row_parity_and_operation_approval_required |
| tdcc_all_thresholds_up | chip | tested_point_in_time | available_point_in_time_research_frame | 13502 | 4.52 | 7136 | 2.73 | 52.02 | 10.7 | 11.49 | 36.49 | -9.32 | 0.0 | 1.39 | 1.01 | 11.22 | -1.27 | blocked_exact_daily_row_parity_and_operation_approval_required |
| return20_0_25 | risk_control | tested_point_in_time | available_point_in_time_research_frame | 117181 | 39.27 | 102047 | 38.99 | 57.14 | 15.82 | 7.39 | 35.47 | -10.34 | 0.0 | 0.4 | 0.02 | 10.92 | -1.57 | blocked_exact_daily_row_parity_and_operation_approval_required |
| pattern45_bull_pullback | price_structure | tested_point_in_time | computed_from_point_in_time_price_history | 31573 | 10.58 | 25799 | 9.86 | 44.24 | 2.92 | 10.22 | 45.54 | -0.27 | 0.0 | 1.31 | 0.93 | 12.31 | -0.18 | blocked_exact_daily_row_parity_and_operation_approval_required |
| revenue_positive_or_strong | revenue | blocked_data_panel_incomplete | historical revenue panel is not complete enough for point-in-time replay in this research frame |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  | blocked_exact_daily_row_parity_and_operation_approval_required |
| market_background_regime | market_background | deferred_join_required | market feature panel exists, but this artifact does not yet join it into stock-day rows |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  | blocked_exact_daily_row_parity_and_operation_approval_required |
