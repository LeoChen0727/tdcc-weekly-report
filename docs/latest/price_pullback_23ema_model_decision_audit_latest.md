# Price Pullback 23EMA Model Decision Audit

- generated_at: `2026-07-02 14:05:49 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `discussion_ready_research_only`; this does not change production condition, scoring, ranking, or contract registry
- fixed_operation_module_candidate_id: `next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit`
- buy_point: current production proxy signal plus the tested entry/feature filter on signal date; buy next open only after both hold
- sell_point: first intraday breakout above signal-day previous 20-day high before stop through D+20
- stop: close stays at least 4% below the lower of 20MA and 23EMA for 4 consecutive trading days
- model_decision_use: compare baseline, volume red K, prior extension, chip, technical, theme context, 45d structure, revenue gap, and market-background gap in one table
- obv_scope: OBV combo rows are score-bonus candidates, not required gates.
- theme_context_scope: theme context rows are point-in-time coverage-limited score-bonus discussion candidates, not production gates.
- rule: rows marked `reject_as_required_gate` must not become production gates without new evidence; blocked rows require data joins before scoring

## Decision Status Counts

| decision_status | count |
| --- | --- |
| score_bonus_candidate | 10 |
| score_bonus_candidate_winrate_tradeoff | 6 |
| insufficient_sample_review_only | 6 |
| reject_as_required_gate | 4 |
| mixed_discussion_candidate | 2 |
| baseline_anchor | 1 |
| return_up_but_riskier_not_gate | 1 |
| score_bonus_candidate_not_required_gate | 1 |
| blocked_data_gap_required_before_gate | 1 |
| blocked_market_join_required | 1 |

## Decision Rows

| decision_axis | decision_item_id | feature_family | selected_share_of_baseline_pct | mature_count | win_rate_pct | delta_vs_baseline_win_rate_pct | failure_rate_pct | delta_vs_baseline_failure_rate_pct | avg_realized_return_pct | delta_vs_baseline_avg_realized_return_pct | avg_realized_or_d20_days | decision_status | plain_conclusion_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_operation | baseline:production_replay_operation_anchor | baseline | 100.0 | 264349 | 41.42 | 0.0 | 45.72 | 0.0 | 0.38 | 0.0 | 12.47 | baseline_anchor | 作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。 |
| entry_filter | entry_filter:volume_red_k_vol1.2 | entry_filter | 10.15 | 26214 | 59.63 | 18.21 | 33.12 | -12.6 | -0.05 | -0.43 | 9.62 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.2 | entry_filter | 5.32 | 13723 | 60.96 | 19.54 | 31.55 | -14.17 | -0.11 | -0.49 | 9.41 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.5 | entry_filter | 3.42 | 8755 | 63.24 | 21.82 | 30.06 | -15.66 | -0.25 | -0.63 | 8.87 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:prior_ext20_ema10_runup20_pullback5 | entry_filter | 19.78 | 49559 | 29.11 | -12.31 | 56.2 | 10.48 | 1.14 | 0.76 | 12.38 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext30_ema12_runup25_pullback8 | entry_filter | 21.7 | 55679 | 30.67 | -10.75 | 55.68 | 9.96 | 0.91 | 0.53 | 12.17 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext60_ema15_runup35_pullback10 | entry_filter | 30.44 | 81897 | 35.83 | -5.59 | 51.0 | 5.28 | 0.74 | 0.36 | 12.16 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:prior_ext20_ema10_runup20_pullback5 | prior_extension | 19.78 | 49559 | 29.11 | -12.31 | 56.2 | 10.48 | 1.14 | 0.76 | 12.38 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:macd_hist_gt0 | technical | 42.39 | 113558 | 53.91 | 12.49 | 37.72 | -8.0 | 0.23 | -0.15 | 11.46 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:kd_bullish_not_overheated | technical | 43.11 | 115338 | 45.09 | 3.67 | 43.19 | -2.53 | 0.11 | -0.27 | 12.25 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:macd_kd_confirm | technical | 22.35 | 60693 | 55.84 | 14.42 | 36.24 | -9.48 | 0.07 | -0.31 | 11.14 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:rsi14_40_70 | technical | 63.67 | 167486 | 49.42 | 8.0 | 40.82 | -4.9 | 0.46 | 0.08 | 12.07 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:bb_width_not_extreme | technical | 53.63 | 140043 | 44.64 | 3.22 | 43.95 | -1.77 | 0.45 | 0.07 | 12.21 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:obv_above_ma20 | technical_volume | 43.42 | 111575 | 54.63 | 13.21 | 37.44 | -8.28 | 0.33 | -0.05 | 11.17 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:tdcc_history_available | chip | 21.87 | 37296 | 46.72 | 5.3 | 39.21 | -6.51 | 1.37 | 0.99 | 11.63 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_weeks_ge1 | chip | 11.51 | 18620 | 50.63 | 9.21 | 36.7 | -9.02 | 1.5 | 1.12 | 11.31 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up | chip | 8.64 | 14314 | 51.63 | 10.21 | 36.15 | -9.57 | 1.55 | 1.17 | 11.27 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_all_thresholds_up | chip | 4.7 | 7794 | 52.28 | 10.86 | 36.19 | -9.53 | 1.36 | 0.98 | 11.13 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:return20_0_25 | risk_control | 39.28 | 103141 | 57.23 | 15.81 | 35.42 | -10.3 | 0.39 | 0.01 | 10.89 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:pattern45_bull_pullback | price_structure | 10.65 | 26255 | 44.04 | 2.62 | 45.83 | 0.11 | 1.22 | 0.84 | 12.28 | return_up_but_riskier_not_gate | 平均報酬提高但勝率或失敗率變差，若保留只能當高波動加分候選，不適合硬篩。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25 | combo_chip_risk_control | 4.04 | 5664 | 67.07 | 25.65 | 27.68 | -18.04 | 1.19 | 0.81 | 9.59 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_ge1_return20_0_25 | combo_chip_risk_control | 5.31 | 7281 | 66.1 | 24.68 | 28.5 | -17.22 | 1.16 | 0.78 | 9.62 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_obv_above_ma20 | combo_chip_technical_volume | 3.99 | 5810 | 64.68 | 23.26 | 29.69 | -16.03 | 1.17 | 0.79 | 9.86 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_macd_kd_confirm | combo_chip_technical | 2.2 | 3790 | 66.39 | 24.97 | 27.18 | -18.54 | 1.22 | 0.84 | 9.64 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20 | combo_chip_risk_control_technical_volume | 2.81 | 4013 | 69.8 | 28.38 | 25.89 | -19.83 | 1.07 | 0.69 | 9.08 | score_bonus_candidate_not_required_gate | OBV above MA20 對已篩出的 TDCC/20日報酬條件有加分討論價值，但目前定位是加分項，不是必要條件。 |
| feature_filter | feature_filter:theme_context_available | theme_context | 0.71 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_mainstream_supported | theme_context | 0.7 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_leadership_not_overheated | theme_context | 0.13 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_volume_attack_selected | theme_context | 0.0 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported | combo_chip_risk_control_theme_context | 0.27 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_leadership_not_overheated | combo_chip_risk_control_theme_context | 0.06 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:revenue_positive_or_strong | revenue |  | 0 |  |  |  |  |  |  |  | blocked_data_gap_required_before_gate | 營收可以當必要條件或加分討論，但目前缺 point-in-time 歷史營收 panel，不能先寫進 production。 |
| feature_filter | feature_filter:market_background_regime | market_background |  | 0 |  |  |  |  |  |  |  | blocked_market_join_required | 大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。 |
