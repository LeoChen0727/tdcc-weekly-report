# Price Pullback 23EMA Model Decision Audit

- generated_at: `2026-06-30 22:43:07 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `discussion_ready_research_only`; this does not change production condition, scoring, ranking, or contract registry
- fixed_operation_module_candidate_id: `next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit`
- buy_point: current production proxy signal plus the tested entry/feature filter on signal date; buy next open only after both hold
- sell_point: first intraday breakout above signal-day previous 20-day high before stop through D+20
- stop: close stays at least 4% below the lower of 20MA and 23EMA for 4 consecutive trading days
- model_decision_use: compare baseline, volume red K, prior extension, chip, technical, 45d structure, revenue gap, and market-background gap in one table
- rule: rows marked `reject_as_required_gate` must not become production gates without new evidence; blocked rows require data joins before scoring

## Decision Status Counts

| decision_status | count |
| --- | --- |
| score_bonus_candidate | 11 |
| score_bonus_candidate_winrate_tradeoff | 6 |
| reject_as_required_gate | 4 |
| mixed_discussion_candidate | 3 |
| baseline_anchor | 1 |
| blocked_data_gap_required_before_gate | 1 |
| blocked_market_join_required | 1 |

## Decision Rows

| decision_axis | decision_item_id | feature_family | selected_share_of_baseline_pct | mature_count | win_rate_pct | delta_vs_baseline_win_rate_pct | failure_rate_pct | delta_vs_baseline_failure_rate_pct | avg_realized_return_pct | delta_vs_baseline_avg_realized_return_pct | avg_realized_or_d20_days | decision_status | plain_conclusion_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_operation | baseline:production_replay_operation_anchor | baseline | 100.0 | 263065 | 41.37 | 0.0 | 45.76 | 0.0 | 0.39 | 0.0 | 12.48 | baseline_anchor | 作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。 |
| entry_filter | entry_filter:volume_red_k_vol1.2 | entry_filter | 10.16 | 25899 | 59.5 | 18.13 | 33.28 | -12.48 | -0.06 | -0.45 | 9.64 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.2 | entry_filter | 5.32 | 13513 | 60.81 | 19.44 | 31.77 | -13.99 | -0.12 | -0.51 | 9.43 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.5 | entry_filter | 3.43 | 8619 | 63.13 | 21.76 | 30.25 | -15.51 | -0.26 | -0.65 | 8.89 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:prior_ext20_ema10_runup20_pullback5 | entry_filter | 19.69 | 49225 | 29.15 | -12.22 | 56.17 | 10.41 | 1.16 | 0.77 | 12.38 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext30_ema12_runup25_pullback8 | entry_filter | 21.63 | 55332 | 30.71 | -10.66 | 55.63 | 9.87 | 0.94 | 0.55 | 12.17 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext60_ema15_runup35_pullback10 | entry_filter | 30.41 | 81559 | 35.86 | -5.51 | 50.95 | 5.19 | 0.75 | 0.36 | 12.16 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:prior_ext20_ema10_runup20_pullback5 | prior_extension | 19.69 | 49225 | 29.15 | -12.22 | 56.17 | 10.41 | 1.16 | 0.77 | 12.38 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:macd_hist_gt0 | technical | 42.46 | 112824 | 53.85 | 12.48 | 37.78 | -7.98 | 0.23 | -0.16 | 11.48 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:kd_bullish_not_overheated | technical | 43.17 | 114572 | 45.01 | 3.64 | 43.27 | -2.49 | 0.11 | -0.28 | 12.27 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:macd_kd_confirm | technical | 22.41 | 60175 | 55.74 | 14.37 | 36.33 | -9.43 | 0.07 | -0.32 | 11.16 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:rsi14_40_70 | technical | 63.65 | 166597 | 49.38 | 8.01 | 40.85 | -4.91 | 0.46 | 0.07 | 12.08 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:bb_width_not_extreme | technical | 53.49 | 139038 | 44.58 | 3.21 | 44.0 | -1.76 | 0.45 | 0.06 | 12.23 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:obv_above_ma20 | technical_volume | 43.43 | 111009 | 54.59 | 13.22 | 37.47 | -8.29 | 0.33 | -0.06 | 11.19 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:tdcc_history_available | chip | 21.48 | 36014 | 46.6 | 5.23 | 39.3 | -6.46 | 1.42 | 1.03 | 11.67 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_weeks_ge1 | chip | 11.29 | 17860 | 50.49 | 9.12 | 36.81 | -8.95 | 1.54 | 1.15 | 11.37 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up | chip | 8.48 | 13752 | 51.47 | 10.1 | 36.32 | -9.44 | 1.58 | 1.19 | 11.32 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_all_thresholds_up | chip | 4.61 | 7480 | 52.23 | 10.86 | 36.31 | -9.45 | 1.39 | 1.0 | 11.17 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:return20_0_25 | risk_control | 39.28 | 102587 | 57.18 | 15.81 | 35.45 | -10.31 | 0.4 | 0.01 | 10.91 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:pattern45_bull_pullback | price_structure | 10.62 | 26048 | 44.17 | 2.8 | 45.67 | -0.09 | 1.27 | 0.88 | 12.29 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25 | combo_chip_risk_control | 3.97 | 5398 | 66.84 | 25.47 | 27.81 | -17.95 | 1.24 | 0.85 | 9.71 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_ge1_return20_0_25 | combo_chip_risk_control | 5.21 | 6937 | 65.91 | 24.54 | 28.57 | -17.19 | 1.22 | 0.83 | 9.73 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_obv_above_ma20 | combo_chip_technical_volume | 3.92 | 5538 | 64.46 | 23.09 | 29.94 | -15.82 | 1.18 | 0.79 | 9.94 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_macd_kd_confirm | combo_chip_technical | 2.18 | 3548 | 66.09 | 24.72 | 27.54 | -18.22 | 1.21 | 0.82 | 9.76 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20 | combo_chip_risk_control_technical_volume | 2.77 | 3827 | 69.53 | 28.16 | 26.13 | -19.63 | 1.09 | 0.7 | 9.18 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:revenue_positive_or_strong | revenue |  | 0 |  |  |  |  |  |  |  | blocked_data_gap_required_before_gate | 營收可以當必要條件或加分討論，但目前缺 point-in-time 歷史營收 panel，不能先寫進 production。 |
| feature_filter | feature_filter:market_background_regime | market_background |  | 0 |  |  |  |  |  |  |  | blocked_market_join_required | 大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。 |
