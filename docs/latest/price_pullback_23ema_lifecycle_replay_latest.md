# Price Pullback 23EMA Lifecycle Replay

- generated_at: `2026-07-04 21:42:54 Asia/Taipei`
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
| 00_baseline | baseline_replay | close_prev20_break_then_tp10_or_5ma_next_open | 265631 | 22358 | 100.0 | 81.3 | 95.96 | 243273 | 16.5 | 26.9 | 56.6 | 1.21 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp10_or_5ma_next_open | 5925 | 1299 | 5.81 | 4.72 | 11.92 | 4626 | 25.56 | 31.79 | 42.65 | 3.0 | 9.06 | 1.79 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp10_or_5ma_next_open | 4192 | 1023 | 4.58 | 3.72 | 9.56 | 3169 | 26.1 | 31.87 | 42.03 | 3.32 | 9.6 | 2.11 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp10_or_5ma_next_open | 26343 | 10663 | 47.69 | 38.77 | 45.76 | 15680 | 16.4 | 30.38 | 53.22 | 0.84 | -0.1 | -0.37 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp10_or_5ma_next_open | 13817 | 7696 | 34.42 | 27.99 | 33.03 | 6121 | 15.98 | 31.52 | 52.49 | 0.78 | -0.52 | -0.43 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp10_or_5ma_next_open | 8817 | 5786 | 25.88 | 21.04 | 24.83 | 3031 | 15.94 | 31.46 | 52.61 | 0.73 | -0.56 | -0.48 | mixed_or_neutral_review |
| 00_baseline | baseline_replay | close_prev20_break_then_tp5_or_5ma_next_open | 265631 | 22729 | 100.0 | 82.65 | 97.55 | 242902 | 23.64 | 20.52 | 55.84 | 1.19 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp5_or_5ma_next_open | 5925 | 1326 | 5.83 | 4.82 | 11.95 | 4599 | 40.12 | 19.53 | 40.35 | 3.14 | 16.48 | 1.95 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp5_or_5ma_next_open | 4192 | 1044 | 4.59 | 3.8 | 9.76 | 3148 | 41.86 | 18.39 | 39.75 | 3.38 | 18.22 | 2.19 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp5_or_5ma_next_open | 26343 | 10749 | 47.29 | 39.09 | 46.13 | 15594 | 27.3 | 20.54 | 52.16 | 0.83 | 3.66 | -0.36 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp5_or_5ma_next_open | 13817 | 7717 | 33.95 | 28.06 | 33.12 | 6100 | 27.56 | 21.11 | 51.33 | 0.77 | 3.92 | -0.42 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp5_or_5ma_next_open | 8817 | 5799 | 25.51 | 21.09 | 24.89 | 3018 | 27.33 | 21.33 | 51.34 | 0.67 | 3.69 | -0.52 | quality_filter_candidate_review |
| 00_baseline | baseline_replay | close_prev20_break_then_tp8_or_5ma_next_open | 265631 | 22447 | 100.0 | 81.63 | 96.34 | 243184 | 19.21 | 24.33 | 56.46 | 1.2 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_break_then_tp8_or_5ma_next_open | 5925 | 1306 | 5.82 | 4.75 | 11.98 | 4619 | 30.55 | 27.34 | 42.11 | 2.98 | 11.34 | 1.78 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_break_then_tp8_or_5ma_next_open | 4192 | 1027 | 4.58 | 3.73 | 9.6 | 3165 | 31.55 | 27.07 | 41.38 | 3.29 | 12.34 | 2.09 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_break_then_tp8_or_5ma_next_open | 26343 | 10679 | 47.57 | 38.83 | 45.83 | 15664 | 20.21 | 26.82 | 52.97 | 0.84 | 1.0 | -0.36 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_break_then_tp8_or_5ma_next_open | 13817 | 7702 | 34.31 | 28.01 | 33.06 | 6115 | 19.86 | 27.89 | 52.25 | 0.77 | 0.65 | -0.43 | mixed_or_neutral_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_break_then_tp8_or_5ma_next_open | 8817 | 5788 | 25.79 | 21.05 | 24.84 | 3029 | 19.68 | 28.02 | 52.3 | 0.72 | 0.47 | -0.48 | mixed_or_neutral_review |
| 00_baseline | baseline_replay | close_prev20_high_break_next_open | 265631 | 23838 | 100.0 | 86.68 | 102.31 | 241793 | 34.29 | 14.52 | 51.19 | 1.13 | 0.0 | 0.0 | baseline_trade_level_anchor |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high | close_prev20_high_break_next_open | 5925 | 1443 | 6.05 | 5.25 | 13.61 | 4482 | 61.61 | 7.62 | 30.77 | 2.92 | 27.32 | 1.79 | strong_gate_candidate_review |
| 05_v1_candidate_stack | v1_gate_return20_tdcc_high_obv | close_prev20_high_break_next_open | 4192 | 1161 | 4.87 | 4.22 | 11.27 | 3031 | 66.06 | 5.6 | 28.34 | 3.13 | 31.77 | 2.0 | strong_gate_candidate_review |
| 06_candle_quality_reference | volume_red_k_vol1.2 | close_prev20_high_break_next_open | 26343 | 11328 | 47.52 | 41.19 | 48.62 | 15015 | 45.72 | 10.97 | 43.31 | 0.76 | 11.43 | -0.37 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.2 | close_prev20_high_break_next_open | 13817 | 8048 | 33.76 | 29.27 | 34.54 | 5769 | 48.65 | 10.25 | 41.1 | 0.7 | 14.36 | -0.43 | quality_filter_candidate_review |
| 06_candle_quality_reference | solid_volume_red_k_vol1.5 | close_prev20_high_break_next_open | 8817 | 5983 | 25.1 | 21.76 | 25.68 | 2834 | 52.13 | 8.94 | 38.93 | 0.62 | 17.84 | -0.51 | quality_filter_candidate_review |
