# Daily Model Background Feature Catalog

- generated_at: `2026-06-30 19:36:49 Asia/Taipei`
- scope: documents which columns are shared objective background data and which ideas are explicitly model-specific.
- rule: shared objective data can be reused; model-specific interpretations require separate research evidence and promotion.

| feature_column | feature_family | feature_scope | allowed_use | model_specific_owner | point_in_time_rule |
| --- | --- | --- | --- | --- | --- |
| generated_at | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| feature_panel_id | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| feature_scope | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| stock_id | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| stock_name | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| signal_date | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| source_model_ids | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| source_snapshot_dates | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| source_snapshot_files | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| source_signal_rows | metadata | metadata | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| feature_as_of_date | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| price_history_max_date | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| price_history_rows_as_of | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| future_price_rows_ignored | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| point_in_time_status | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| open | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| high | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| low | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| volume | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| signal_return_1d_pct | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| volume_ratio_prev20 | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close_above_open | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| body_ratio | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| upper_shadow_ratio | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close_location | price_ohlcv | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close_return_20d_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_sessions | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_return_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_range_high | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_range_low | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_range_width_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_close_position_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_distance_to_high_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_drawdown_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre20_slope20_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close_return_45d_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_sessions | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_return_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_range_high | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_range_low | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_range_width_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_close_position_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_distance_to_high_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_drawdown_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre45_slope20_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| close_return_90d_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_sessions | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_return_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_range_high | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_range_low | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_range_width_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_close_position_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_distance_to_high_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_drawdown_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| pre90_slope20_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| ma20 | technical_price | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| ma60 | technical_price | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| ema23 | technical_price | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| distance_to_ma20_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| distance_to_ma60_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| distance_to_ema23_pct | price_context | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| ema23_slope_5d_pct | technical_price | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| macd_dif | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| macd_dea | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| macd_hist | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| rsi14 | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| kd_k_value | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| kd_d_value | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| kd_k_minus_d | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| obv | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| obv_ma20 | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| obv_slope_5d | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| bb_width_pct | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| bb_width_pct_rank_120d | technical_indicator | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_as_of_date | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_rows_as_of | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_future_rows_ignored | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_data_status | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_consecutive_up_weeks | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_400_ratio | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_400_change_1w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_400_change_3w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_600_ratio | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_600_change_1w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_800_ratio | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_800_change_1w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_1000_ratio | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_1000_change_1w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tdcc_over_1000_change_3w | holder_flow | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| market_index_as_of_date | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| twse_close | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| twse_return_5d_pct | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| twse_return_20d_pct | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| twse_above_ma20 | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| twse_above_ma60 | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tpex_close | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tpex_return_5d_pct | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tpex_return_20d_pct | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tpex_above_ma20 | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| tpex_above_ma60 | market_index | shared_objective_point_in_time | research_background_only_not_a_model_gate_or_score |  | use rows available on or before signal_date |
| monthly_revenue_point_in_time_panel | revenue | missing_shared_data_family | not_available_for_required_model_gate_until_panel_and_validator_exist |  | must use revenue release date on or before signal_date |
| price_pullback_23ema_operation_filter | model_specific_interpretation | model_specific_not_in_shared_panel | price_pullback_23ema_only_after_explicit_research_and_promotion | price_pullback_23ema | must consume shared objective columns without rewriting shared semantics |
| neckline_45d_non_bearish_filter | model_specific_interpretation | model_specific_not_in_shared_panel | neckline_volume_breakout_confirmation_only | neckline_volume_breakout_confirmation | must not be reused as a price_pullback_23ema gate |
