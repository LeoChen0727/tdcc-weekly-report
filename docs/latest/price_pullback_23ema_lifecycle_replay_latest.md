# Price Pullback 23EMA Lifecycle Replay

- generated_at: `2026-07-02 20:42:27 Asia/Taipei`
- model_id: `price_pullback_23ema`
- status: `not_production_ready_research_only`
- scope: trade-level replay that suppresses later same-stock signals while a prior accepted trade is still active.
- production_change: `none`
- entry_basis: `signal_date_next_open` after the production proxy signal and research-only condition filter.
- exit_basis: close-confirmed previous-20-day-high exits use next open; continuation exits use next open after close target or 5MA close exit.
- metric_boundary: PDF titles must not calculate win rate or return from candidate rows; they need a model-owned approved metric artifact or operation adapter.
- promotion_blocker: production use requires explicit model-rule decision, contract update when applicable, parity, validators, merge, post-merge main validation, and PDF metric consumer contract.

| test_stage | condition_test_id | exit_rule_id | source_mature_signal_stock_days | accepted_trade_count | accepted_trade_share_of_baseline_pct | accepted_avg_trades_per_research_day | accepted_avg_trades_per_signal_day | suppressed_signal_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | delta_vs_baseline_win_rate_pct | delta_vs_baseline_avg_realized_return_pct | decision_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00_baseline | baseline_replay | close_prev20_break_then_tp10_or_5ma_next_open | 264320 | 22254 | 100.0 | 81.22 | 95.92 | 242066 | 16.5 | 26.88 | 56.62 | 1.22 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp10_or_5ma_next_open | 5662 | 1265 | 5.68 | 4.62 | 11.71 | 4397 | 25.53 | 32.09 | 42.37 | 3.02 | 9.03 | 1.8 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp10_or_5ma_next_open | 4012 | 996 | 4.48 | 3.64 | 9.4 | 3016 | 26.1 | 31.73 | 42.17 | 3.3 | 9.6 | 2.08 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp10_or_5ma_next_open | 26210 | 10639 | 47.81 | 38.83 | 45.86 | 15571 | 16.4 | 30.37 | 53.23 | 0.84 | -0.1 | -0.38 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp10_or_5ma_next_open | 13720 | 7659 | 34.42 | 27.95 | 33.01 | 6061 | 15.93 | 31.48 | 52.59 | 0.77 | -0.57 | -0.45 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp10_or_5ma_next_open | 8752 | 5752 | 25.85 | 20.99 | 24.79 | 3000 | 15.94 | 31.36 | 52.69 | 0.72 | -0.56 | -0.5 | mixed_or_neutral_review |
| 00_baseline | baseline_replay | close_prev20_break_then_tp5_or_5ma_next_open | 264320 | 22621 | 100.0 | 82.56 | 97.5 | 241699 | 23.65 | 20.49 | 55.86 | 1.2 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp5_or_5ma_next_open | 5662 | 1287 | 5.69 | 4.7 | 11.7 | 4375 | 40.17 | 19.89 | 39.94 | 3.2 | 16.52 | 2.0 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp5_or_5ma_next_open | 4012 | 1013 | 4.48 | 3.7 | 9.56 | 2999 | 41.86 | 18.46 | 39.68 | 3.39 | 18.21 | 2.19 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp5_or_5ma_next_open | 26210 | 10724 | 47.41 | 39.14 | 46.22 | 15486 | 27.29 | 20.53 | 52.17 | 0.83 | 3.64 | -0.37 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp5_or_5ma_next_open | 13720 | 7681 | 33.96 | 28.03 | 33.11 | 6039 | 27.54 | 21.04 | 51.43 | 0.76 | 3.89 | -0.44 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp5_or_5ma_next_open | 8752 | 5765 | 25.49 | 21.04 | 24.85 | 2987 | 27.37 | 21.21 | 51.41 | 0.67 | 3.72 | -0.53 | quality_filter_candidate_review |
| 00_baseline | baseline_replay | close_prev20_break_then_tp8_or_5ma_next_open | 264320 | 22344 | 100.0 | 81.55 | 96.31 | 241976 | 19.21 | 24.31 | 56.48 | 1.21 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp8_or_5ma_next_open | 5662 | 1272 | 5.69 | 4.64 | 11.78 | 4390 | 30.5 | 27.75 | 41.75 | 3.0 | 11.29 | 1.79 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp8_or_5ma_next_open | 4012 | 1000 | 4.48 | 3.65 | 9.43 | 3012 | 31.5 | 27.1 | 41.4 | 3.28 | 12.29 | 2.07 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp8_or_5ma_next_open | 26210 | 10656 | 47.69 | 38.89 | 45.93 | 15554 | 20.2 | 26.81 | 52.98 | 0.84 | 0.99 | -0.37 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp8_or_5ma_next_open | 13720 | 7666 | 34.31 | 27.98 | 33.04 | 6054 | 19.81 | 27.84 | 52.35 | 0.76 | 0.6 | -0.45 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp8_or_5ma_next_open | 8752 | 5754 | 25.75 | 21.0 | 24.8 | 2998 | 19.69 | 27.93 | 52.38 | 0.71 | 0.48 | -0.5 | mixed_or_neutral_review |
| 00_baseline | baseline_replay | close_prev20_high_break_next_open | 264320 | 23721 | 100.0 | 86.57 | 102.25 | 240599 | 34.28 | 14.5 | 51.22 | 1.13 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_high_break_next_open | 5662 | 1386 | 5.84 | 5.06 | 13.2 | 4276 | 61.47 | 7.65 | 30.88 | 2.95 | 27.19 | 1.82 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_high_break_next_open | 4012 | 1116 | 4.7 | 4.07 | 10.94 | 2896 | 65.68 | 5.47 | 28.85 | 3.12 | 31.4 | 1.99 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_high_break_next_open | 26210 | 11295 | 47.62 | 41.22 | 48.69 | 14915 | 45.67 | 10.96 | 43.37 | 0.76 | 11.39 | -0.37 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_high_break_next_open | 13720 | 8007 | 33.75 | 29.22 | 34.51 | 5713 | 48.5 | 10.24 | 41.26 | 0.68 | 14.22 | -0.45 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_high_break_next_open | 8752 | 5947 | 25.07 | 21.7 | 25.63 | 2805 | 51.96 | 8.93 | 39.11 | 0.61 | 17.68 | -0.52 | quality_filter_candidate_review |
