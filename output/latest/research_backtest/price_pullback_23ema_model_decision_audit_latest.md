# Price Pullback 23EMA Model Decision Audit

- generated_at: `2026-07-04 21:42:54 Asia/Taipei`
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
| coverage_limited_score_discussion_not_required_gate | 2 |
| baseline_anchor | 1 |
| return_up_but_riskier_not_gate | 1 |
| score_bonus_candidate_not_required_gate | 1 |
| blocked_market_join_required | 1 |

## Decision Rows

| decision_axis | decision_item_id | feature_family | selected_share_of_baseline_pct | mature_count | win_rate_pct | delta_vs_baseline_win_rate_pct | failure_rate_pct | delta_vs_baseline_failure_rate_pct | avg_realized_return_pct | delta_vs_baseline_avg_realized_return_pct | avg_realized_or_d20_days | decision_status | plain_conclusion_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_operation | baseline:production_replay_operation_anchor | baseline | 100.0 | 266876 | 41.46 | 0.0 | 45.69 | 0.0 | 0.38 | 0.0 | 12.46 | baseline_anchor | 作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。 |
| entry_filter | entry_filter:volume_red_k_vol1.2 | entry_filter | 10.14 | 26606 | 59.72 | 18.26 | 33.04 | -12.65 | -0.05 | -0.43 | 9.6 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.2 | entry_filter | 5.32 | 13986 | 61.08 | 19.62 | 31.42 | -14.27 | -0.11 | -0.49 | 9.38 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:solid_volume_red_k_vol1.5 | entry_filter | 3.43 | 8933 | 63.42 | 21.96 | 29.87 | -15.82 | -0.25 | -0.63 | 8.83 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| entry_filter | entry_filter:prior_ext20_ema10_runup20_pullback5 | entry_filter | 19.95 | 50314 | 29.03 | -12.43 | 56.29 | 10.6 | 1.09 | 0.71 | 12.37 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext30_ema12_runup25_pullback8 | entry_filter | 21.83 | 56438 | 30.54 | -10.92 | 55.85 | 10.16 | 0.86 | 0.48 | 12.16 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| entry_filter | entry_filter:prior_ext60_ema15_runup35_pullback10 | entry_filter | 30.48 | 82590 | 35.77 | -5.69 | 51.08 | 5.39 | 0.71 | 0.33 | 12.14 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:prior_ext20_ema10_runup20_pullback5 | prior_extension | 19.95 | 50314 | 29.03 | -12.43 | 56.29 | 10.6 | 1.09 | 0.71 | 12.37 | reject_as_required_gate | 相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。 |
| feature_filter | feature_filter:macd_hist_gt0 | technical | 42.31 | 115126 | 53.93 | 12.47 | 37.68 | -8.01 | 0.22 | -0.16 | 11.44 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:kd_bullish_not_overheated | technical | 43.11 | 116762 | 45.19 | 3.73 | 43.09 | -2.6 | 0.11 | -0.27 | 12.23 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:macd_kd_confirm | technical | 22.32 | 61801 | 55.9 | 14.44 | 36.16 | -9.53 | 0.07 | -0.31 | 11.11 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:rsi14_40_70 | technical | 63.76 | 169367 | 49.41 | 7.95 | 40.84 | -4.85 | 0.44 | 0.06 | 12.05 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:bb_width_not_extreme | technical | 53.94 | 142029 | 44.68 | 3.22 | 43.92 | -1.77 | 0.43 | 0.05 | 12.19 | mixed_discussion_candidate | 有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。 |
| feature_filter | feature_filter:obv_above_ma20 | technical_volume | 43.4 | 112795 | 54.66 | 13.2 | 37.43 | -8.26 | 0.31 | -0.07 | 11.15 | score_bonus_candidate_winrate_tradeoff | 勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。 |
| feature_filter | feature_filter:tdcc_history_available | chip | 22.64 | 39820 | 46.65 | 5.19 | 39.42 | -6.27 | 1.25 | 0.87 | 11.58 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_weeks_ge1 | chip | 11.95 | 20114 | 50.59 | 9.13 | 36.87 | -8.82 | 1.38 | 1.0 | 11.24 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up | chip | 8.94 | 15418 | 51.61 | 10.15 | 36.22 | -9.47 | 1.46 | 1.08 | 11.21 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_all_thresholds_up | chip | 4.85 | 8417 | 52.09 | 10.63 | 36.35 | -9.34 | 1.26 | 0.88 | 11.09 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:return20_0_25 | risk_control | 39.23 | 104252 | 57.28 | 15.82 | 35.4 | -10.29 | 0.38 | 0.0 | 10.86 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:pattern45_bull_pullback | price_structure | 10.74 | 26790 | 43.72 | 2.26 | 46.19 | 0.5 | 1.13 | 0.75 | 12.25 | return_up_but_riskier_not_gate | 平均報酬提高但勝率或失敗率變差，若保留只能當高波動加分候選，不適合硬篩。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25 | combo_chip_risk_control | 4.15 | 6198 | 67.13 | 25.67 | 27.75 | -17.94 | 1.09 | 0.71 | 9.44 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_consecutive_up_ge1_return20_0_25 | combo_chip_risk_control | 5.47 | 7975 | 66.12 | 24.66 | 28.63 | -17.06 | 1.03 | 0.65 | 9.45 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_obv_above_ma20 | combo_chip_technical_volume | 4.13 | 6362 | 64.76 | 23.3 | 29.71 | -15.98 | 1.11 | 0.73 | 9.74 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_macd_kd_confirm | combo_chip_technical | 2.25 | 4279 | 66.09 | 24.63 | 27.32 | -18.37 | 1.15 | 0.77 | 9.63 | score_bonus_candidate | 相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20 | combo_chip_risk_control_technical_volume | 2.89 | 4392 | 70.2 | 28.74 | 25.61 | -20.08 | 1.02 | 0.64 | 8.89 | score_bonus_candidate_not_required_gate | OBV above MA20 對已篩出的 TDCC/20日報酬條件有加分討論價值，但目前定位是加分項，不是必要條件。 |
| feature_filter | feature_filter:theme_context_available | theme_context | 0.86 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_mainstream_supported | theme_context | 0.85 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_leadership_not_overheated | theme_context | 0.14 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:theme_context_volume_attack_selected | theme_context | 0.0 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported | combo_chip_risk_control_theme_context | 0.31 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_theme_context_leadership_not_overheated | combo_chip_risk_control_theme_context | 0.06 | 0 |  |  |  |  |  |  |  | insufficient_sample_review_only | 樣本不足，只能列為觀察，不能當必要條件。 |
| feature_filter | feature_filter:revenue_positive_or_strong | revenue | 0.73 | 0 |  |  |  |  |  |  |  | coverage_limited_score_discussion_not_required_gate | 營收資料已可做 coverage-limited research-only 觀察；因不是完整 release-date 歷史 panel，暫時只能當加分討論，不能升正式必要條件。 |
| feature_filter | feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20_revenue_positive_or_strong | combo_chip_risk_control_technical_volume_revenue | 0.2 | 0 |  |  |  |  |  |  |  | coverage_limited_score_discussion_not_required_gate | 營收資料已可做 coverage-limited research-only 觀察；因不是完整 release-date 歷史 panel，暫時只能當加分討論，不能升正式必要條件。 |
| feature_filter | feature_filter:market_background_regime | market_background |  | 0 |  |  |  |  |  |  |  | blocked_market_join_required | 大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。 |
