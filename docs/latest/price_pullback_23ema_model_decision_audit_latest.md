# Price Pullback 23EMA Model Decision Audit

- generated_at: `2026-07-12 03:47:30 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `discussion_ready_research_only`; this does not change production condition, scoring, ranking, or contract registry
- fixed_operation_module_candidate_id: `next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit`
- buy_point: current production proxy signal plus the tested entry/feature filter on signal date; buy next open only after both hold
- sell_point: first intraday breakout above signal-day previous 20-day high before stop through D+20
- stop: close stays at least 4% below the lower of 20MA and 23EMA for 4 consecutive trading days, then exit at the next trading day open
- model_decision_use: compare baseline, volume red K, prior extension, chip, technical, theme context, 45d structure, revenue gap, and market-background gap in one table
- obv_scope: OBV combo rows are score-bonus candidates, not required gates.
- theme_context_scope: theme context rows are point-in-time coverage-limited score-bonus discussion candidates, not production gates.
- rule: rows marked `reject_as_required_gate` must not become production gates without new evidence; blocked rows require data joins before scoring

## Decision Status Counts

| decision_status | count |
| --- | --- |
| score_bonus_candidate | 8 |
| score_bonus_candidate_winrate_tradeoff | 7 |
| insufficient_sample_review_only | 6 |
| reject_as_required_gate | 4 |
| mixed_discussion_candidate | 3 |
| coverage_limited_score_discussion_not_required_gate | 2 |
| baseline_anchor | 1 |
| return_up_but_riskier_not_gate | 1 |
| score_bonus_candidate_not_required_gate | 1 |
| blocked_market_join_required | 1 |

## Decision Rows

| decision_axis | decision_item_id | feature_family | selected_share_of_baseline_pct | mature_count | win_rate_pct | delta_vs_baseline_win_rate_pct | failure_rate_pct | delta_vs_baseline_failure_rate_pct | avg_realized_return_pct | delta_vs_baseline_avg_realized_return_pct | avg_realized_or_d20_days | decision_status | plain_conclusion_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_operation | baseline:production_replay_operation_anchor | baseline | 100.0 | 272460 | 41.5 | 0.0 | 45.55 | 0.0 | 0.47 | 0.0 | 12.45 | baseline_anchor | 作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。 |
| entry_filter | entry_filter:volume_red_k_vol1.2 | entry_filter | 10.11 | 27585 | 59.55 | 18.05 | 33.01 | -12.54 | 0.01 | -0.46 | 9.64 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.2 | entry_filter | 5.31 | 14566 | 60.85 | 19.35 | 31.46 | -14.09 | -0.04 | -0.51 | 9.44 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.5 | entry_filter | 3.42 | 9344 | 62.99 | 21.49 | 30.09 | -15.46 | -0.18 | -0.65 | 8.93 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:prior_ext20_ema10_runup20_pullback5 | entry_filter | 20.21 | 52177 | 28.94 | -12.56 | 56.19 | 10.64 | 1.29 | 0.82 | 12.38 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext30_ema12_runup25_pullback8 | entry_filter | 20.35 | 52758 | 29.74 | -11.76 | 56.18 | 10.63 | 1.19 | 0.72 | 12.08 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext60_ema15_runup35_pullback10 | entry_filter | 20.37 | 52644 | 34.24 | -7.26 | 53.57 | 8.02 | 1.26 | 0.79 | 11.5 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:prior_ext20_ema10_runup20_pullback5 | prior_extension | 20.21 | 51679 | 28.96 | -12.54 | 56.19 | 10.64 | 1.28 | 0.81 | 12.37 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:macd_hist_gt0 | technical | 42.36 | 117820 | 53.88 | 12.38 | 37.52 | -8.03 | 0.3 | -0.17 | 11.46 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:kd_bullish_not_overheated | technical | 43.37 | 118567 | 45.28 | 3.78 | 42.88 | -2.67 | 0.17 | -0.3 | 12.23 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:macd_kd_confirm | technical | 22.49 | 63307 | 55.87 | 14.37 | 35.92 | -9.63 | 0.15 | -0.32 | 11.14 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:rsi14_40_70 | technical | 63.91 | 172662 | 49.3 | 7.8 | 40.79 | -4.76 | 0.53 | 0.06 | 12.05 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:bb_width_not_extreme | technical | 54.54 | 145163 | 44.68 | 3.18 | 43.78 | -1.77 | 0.53 | 0.06 | 12.18 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:obv_above_ma20 | technical_volume | 43.55 | 115003 | 54.59 | 13.09 | 37.33 | -8.22 | 0.39 | -0.08 | 11.16 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:tdcc_history_available | chip | 24.16 | 43962 | 46.32 | 4.82 | 39.33 | -6.22 | 1.43 | 0.96 | 11.62 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:tdcc_consecutive_up_weeks_ge1 | chip | 12.8 | 22518 | 50.12 | 8.62 | 36.77 | -8.78 | 1.56 | 1.09 | 11.29 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up | chip | 9.55 | 17198 | 51.27 | 9.77 | 36.0 | -9.55 | 1.66 | 1.19 | 11.26 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_all_thresholds_up | chip | 5.17 | 9420 | 51.85 | 10.35 | 36.02 | -9.53 | 1.46 | 0.99 | 11.18 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:return20_0_25 | risk_control | 39.25 | 106201 | 57.23 | 15.73 | 35.33 | -10.22 | 0.46 | -0.01 | 10.87 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:pattern45_bull_pullback | price_structure | 10.93 | 27876 | 43.25 | 1.75 | 46.43 | 0.88 | 1.33 | 0.86 | 12.23 | return_up_but_riskier_not_gate | 平均報酬提高但勝率或失敗率變差，若保留只能當高波動加分候選，不適合硬篩。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25 | combo_chip_risk_control | 4.42 | 7086 | 66.37 | 24.87 | 27.7 | -17.85 | 1.35 | 0.88 | 9.53 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_ge1_return20_0_25 | combo_chip_risk_control | 5.84 | 9154 | 65.14 | 23.64 | 28.74 | -16.81 | 1.27 | 0.8 | 9.59 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_obv_above_ma20 | combo_chip_technical_volume | 4.49 | 7376 | 63.6 | 22.1 | 29.38 | -16.17 | 1.4 | 0.93 | 9.88 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_macd_kd_confirm | combo_chip_technical | 2.49 | 4948 | 64.98 | 23.48 | 26.68 | -18.87 | 1.42 | 0.95 | 9.91 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20 | combo_chip_risk_control_technical_volume | 3.09 | 5047 | 69.45 | 27.95 | 25.42 | -20.13 | 1.27 | 0.8 | 8.98 | score_bonus_candidate_not_required_gate | OBV above MA20 對已篩出的 TDCC/20日報酬條件有加分討論價值，但目前定位是加分項，不是必要條件。 |
| feature_filter | feature_filter:theme_context_available | theme_context | 1.12 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_mainstream_supported | theme_context | 1.11 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_leadership_not_overheated | theme_context | 0.15 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_volume_attack_selected | theme_context | 0.0 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported | combo_chip_risk_control_theme_context | 0.41 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_leadership_not_overheated | combo_chip_risk_control_theme_context | 0.07 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:revenue_positive_or_strong | revenue | 0.97 | 0 |  |  |  |  |  |  |  | coverage_limited_score_discussion_not_required_gate | 營收資料已可做 coverage-limited research-only 觀察；因不是完整 release-date 歷史 panel，暫時只能當加分討論，不能升正式必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20_revenue_positive_or_strong | combo_chip_risk_control_technical_volume_revenue | 0.27 | 0 |  |  |  |  |  |  |  | coverage_limited_score_discussion_not_required_gate | 營收資料已可做 coverage-limited research-only 觀察；因不是完整 release-date 歷史 panel，暫時只能當加分討論，不能升正式必要條件。 |
| feature_filter | feature_filter:market_background_regime | market_background |  | 0 |  |  |  |  |  |  |  | blocked_market_join_required | 大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。 |
