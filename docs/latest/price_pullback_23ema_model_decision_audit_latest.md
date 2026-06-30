# Price Pullback 23EMA Model Decision Audit

- generated_at: `2026-06-30 17:49:19 Asia/Taipei`
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
| baseline_operation | baseline:production_replay_operation_anchor | baseline | 100.0 | 261695 | 41.32 | 0.0 | 45.81 | 0.0 | 0.38 | 0.0 | 12.49 | baseline_anchor | 作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。 |
| entry_filter | entry_filter:volume_red_k_vol1.2 | entry_filter | 10.18 | 25673 | 59.4 | 18.08 | 33.39 | -12.42 | -0.07 | -0.45 | 9.66 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.2 | entry_filter | 5.33 | 13381 | 60.72 | 19.4 | 31.89 | -13.92 | -0.14 | -0.52 | 9.45 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.5 | entry_filter | 3.43 | 8539 | 63.04 | 21.72 | 30.38 | -15.43 | -0.27 | -0.65 | 8.9 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:prior_ext20_ema10_runup20_pullback5 | entry_filter | 19.59 | 48853 | 29.15 | -12.17 | 56.14 | 10.33 | 1.18 | 0.8 | 12.39 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext30_ema12_runup25_pullback8 | entry_filter | 21.56 | 54948 | 30.7 | -10.62 | 55.59 | 9.78 | 0.95 | 0.57 | 12.18 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext60_ema15_runup35_pullback10 | entry_filter | 30.39 | 81187 | 35.86 | -5.46 | 50.93 | 5.12 | 0.76 | 0.38 | 12.17 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:prior_ext20_ema10_runup20_pullback5 | prior_extension | 19.59 | 48853 | 29.15 | -12.17 | 56.14 | 10.33 | 1.18 | 0.8 | 12.39 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:macd_hist_gt0 | technical | 42.52 | 112118 | 53.77 | 12.45 | 37.85 | -7.96 | 0.22 | -0.16 | 11.5 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:kd_bullish_not_overheated | technical | 43.31 | 113850 | 44.93 | 3.61 | 43.34 | -2.47 | 0.1 | -0.28 | 12.28 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:macd_kd_confirm | technical | 22.49 | 59731 | 55.63 | 14.31 | 36.41 | -9.4 | 0.06 | -0.32 | 11.18 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:rsi14_40_70 | technical | 63.63 | 165777 | 49.31 | 7.99 | 40.9 | -4.91 | 0.46 | 0.08 | 12.1 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:bb_width_not_extreme | technical | 53.36 | 137972 | 44.49 | 3.17 | 44.06 | -1.75 | 0.45 | 0.07 | 12.25 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:obv_above_ma20 | technical_volume | 43.46 | 110495 | 54.55 | 13.23 | 37.5 | -8.31 | 0.33 | -0.05 | 11.2 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:tdcc_history_available | chip | 21.07 | 34647 | 46.36 | 5.04 | 39.42 | -6.39 | 1.43 | 1.05 | 11.72 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_weeks_ge1 | chip | 11.05 | 17035 | 50.2 | 8.88 | 36.95 | -8.86 | 1.55 | 1.17 | 11.43 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up | chip | 8.31 | 13133 | 51.17 | 9.85 | 36.5 | -9.31 | 1.58 | 1.2 | 11.39 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_all_thresholds_up | chip | 4.52 | 7136 | 52.02 | 10.7 | 36.49 | -9.32 | 1.39 | 1.01 | 11.22 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:return20_0_25 | risk_control | 39.27 | 102047 | 57.14 | 15.82 | 35.47 | -10.34 | 0.4 | 0.02 | 10.92 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:pattern45_bull_pullback | price_structure | 10.58 | 25799 | 44.24 | 2.92 | 45.54 | -0.27 | 1.31 | 0.93 | 12.31 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25 | combo_chip_risk_control | 3.89 | 5141 | 66.58 | 25.26 | 27.84 | -17.97 | 1.28 | 0.9 | 9.82 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_ge1_return20_0_25 | combo_chip_risk_control | 5.1 | 6601 | 65.75 | 24.43 | 28.5 | -17.31 | 1.28 | 0.9 | 9.84 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_obv_above_ma20 | combo_chip_technical_volume | 3.85 | 5281 | 64.27 | 22.95 | 30.05 | -15.76 | 1.2 | 0.82 | 10.02 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_macd_kd_confirm | combo_chip_technical | 2.18 | 3325 | 65.41 | 24.09 | 28.0 | -17.81 | 1.16 | 0.78 | 9.95 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20 | combo_chip_risk_control_technical_volume | 2.72 | 3645 | 69.36 | 28.04 | 26.15 | -19.66 | 1.13 | 0.75 | 9.27 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:revenue_positive_or_strong | revenue |  | 0 |  |  |  |  |  |  |  | blocked_data_gap_required_before_gate | 營收可以當必要條件或加分討論，但目前缺 point-in-time 歷史營收 panel，不能先寫進 production。 |
| feature_filter | feature_filter:market_background_regime | market_background |  | 0 |  |  |  |  |  |  |  | blocked_market_join_required | 大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。 |
