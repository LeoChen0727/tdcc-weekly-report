# Daily Model Signal Background Feature Panel

- generated_at: `2026-07-11 15:54:10 Asia/Taipei`
- feature_panel_id: `daily_model_signal_background_features_v1`
- owner: `research_backtest`
- scope: shared objective point-in-time background features for model research discussion.
- non_goal: not a production gate, not a score, not a recommendation, not a model-specific filter.
- model_specific_boundary: price_pullback_23ema, neckline, W-bottom, and volume-breakout interpretations must stay outside this shared panel.
- revenue_status: coverage-limited monthly revenue PIT context is joined from daily snapshot-observed rows; it remains research-only and cannot be a formal gate.

## Coverage

| point_in_time_status | rows |
| --- | --- |
| exact_signal_date | 5432 |

| tdcc_data_status | rows |
| --- | --- |
| missing_tdcc_history | 28 |
| ready | 5404 |

| theme_context_data_status | rows |
| --- | --- |
| no_theme_on_or_before_signal | 21 |
| ready_exact_signal_date | 5227 |
| ready_previous_signal_date | 184 |

## Feature Families

| feature_scope | feature_family | columns |
| --- | --- | --- |
| metadata | metadata | 10 |
| model_specific_not_in_shared_panel | model_specific_interpretation | 2 |
| shared_objective_point_in_time | holder_flow | 15 |
| shared_objective_point_in_time | market_index | 11 |
| shared_objective_point_in_time | price_context | 33 |
| shared_objective_point_in_time | price_ohlcv | 16 |
| shared_objective_point_in_time | revenue | 14 |
| shared_objective_point_in_time | technical_indicator | 12 |
| shared_objective_point_in_time | technical_price | 4 |
| shared_objective_point_in_time | theme_status_history | 24 |

## Sample

| stock_id | signal_date | source_model_ids | feature_as_of_date | point_in_time_status | close | distance_to_ema23_pct | pre45_return_pct | pre45_range_width_pct | pre45_drawdown_pct | macd_hist | rsi14 | tdcc_as_of_date | tdcc_over_400_change_1w | monthly_revenue_context_as_of_date | monthly_revenue_data_status | monthly_revenue_latest_yoy_pct | monthly_revenue_strong_flag | theme_context_as_of_date | theme_context_status_group | theme_context_volume_attack_status | twse_return_20d_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0050 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 105.25 | 4.7547 | 26.2539 | 34.8968 | -7.2026 | -0.612 | 58.6265 |  |  |  | no_revenue_on_or_before_signal |  |  | 20260615 | mainstream_supported |  | 11.0173 |
| 0052 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 61.6 | 4.5465 | 24.3221 | 34.2953 | -8.5692 | -0.4033 | 56.546 |  |  |  | no_revenue_on_or_before_signal |  |  | 20260615 | mainstream_supported |  | 11.0173 |
| 1102 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 35.45 | 3.0294 | -1.2623 | 11.5741 | -10.1248 | 0.2102 | 69.6429 | 20260612 | -0.06 | 20260615 | ready_exact_signal_date | -1.156 | False | 20260615 | non_mainstream |  | 11.0173 |
| 1210 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 55.8 | 3.5298 | 1.8416 | 8.5271 | -6.1706 | 0.3343 | 79.3651 | 20260612 | 1.0 | 20260615 | ready_exact_signal_date | 10.1609 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1216 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 76.3 | 3.5763 | 6.546 | 11.9708 | -7.2655 | 0.3679 | 75.7009 | 20260612 | 0.25 | 20260615 | ready_exact_signal_date | 2.6981 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1227 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 28.95 | 1.1727 | -3.1614 | 11.3106 | -9.2683 | 0.1347 | 59.2105 | 20260612 | -0.13 | 20260615 | ready_exact_signal_date | 5.4404 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1229 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 41.75 | 1.1859 | -6.0879 | 18.1579 | -13.7387 | 0.1673 | 59.7884 | 20260612 | 0.07 | 20260615 | ready_exact_signal_date | -8.84 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1316 | 20260615 | price_pullback_23ema;revenue_unreacted_range | 20260615 | exact_signal_date | 10.95 | 1.7251 | -6.9959 | 24.5 | -17.2131 | 0.1305 | 64.1509 | 20260612 | -1.03 | 20260615 | ready_exact_signal_date | 152.96 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1326 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 51.6 | 5.1295 | 7.3707 | 35.1661 | -18.5897 | -0.1085 | 62.7698 | 20260612 | -0.57 | 20260615 | ready_exact_signal_date | 15.4529 | True | 20260615 | mainstream_overheated |  | 11.0173 |
| 1402 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 27.55 | 2.9766 | 1.3133 | 21.03 | -13.7868 | 0.1294 | 56.8807 | 20260612 | 0.56 | 20260615 | ready_exact_signal_date | 19.4379 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1434 | 20260615 | price_pullback_23ema | 20260615 | exact_signal_date | 16.75 | 4.2257 | 1.5244 | 16.2162 | -12.3167 | 0.1289 | 74.6479 | 20260612 | 0.09 | 20260615 | ready_exact_signal_date | 5.6255 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1440 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 13.15 | 1.0547 | 3.5294 | 40.8889 | -17.8182 | -0.0075 | 60.5839 | 20260612 | 0.09 | 20260615 | ready_exact_signal_date | -13.4339 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1447 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 6.18 | 1.7237 | 21.7822 | 48.1633 | -11.7647 | -0.0425 | 61.1296 | 20260612 | -0.1 | 20260615 | ready_exact_signal_date | -45.5633 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1449 | 20260615 | revenue_unreacted_range | 20260615 | exact_signal_date | 14.2 | 3.0589 | -8.8889 | 41.4938 | -23.1746 | 0.1173 | 62.6582 | 20260612 | -0.06 | 20260615 | ready_exact_signal_date | 98.72 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1504 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 73.2 | 0.7355 | 18.928 | 52.381 | -21.3793 | -0.8897 | 50.6903 | 20260612 | -2.46 | 20260615 | ready_exact_signal_date | 10.5521 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1513 | 20260615 | hot_theme_pullback;price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 170.0 | 2.7958 | 10.9635 | 37.2014 | -12.2995 | -0.6845 | 54.2373 | 20260612 | -1.9 | 20260615 | ready_exact_signal_date | 3.6163 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1514 | 20260615 | pullback_short_reclaim | 20260615 | exact_signal_date | 121.0 | -1.8763 | 14.3541 | 45.8537 | -21.0702 | -1.5585 | 47.7273 | 20260612 | -3.55 | 20260615 | ready_exact_signal_date | -30.8278 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1560 | 20260615 | hot_theme_pullback;price_pullback_23ema;pullback_short_reclaim;revenue_unreacted_range | 20260615 | exact_signal_date | 703.0 | 6.2326 | 26.3566 | 49.7006 | -17.9245 | -10.3056 | 43.9252 | 20260612 | -0.91 | 20260615 | ready_exact_signal_date | 17.7806 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1597 | 20260615 | revenue_unreacted_range | 20260615 | exact_signal_date | 154.5 | -5.5258 | 51.8668 | 123.0071 | -35.0679 | -5.4894 | 19.9095 | 20260612 | 0.61 | 20260615 | ready_exact_signal_date | 51.38 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1605 | 20260615 | pullback_short_reclaim | 20260615 | exact_signal_date | 40.0 | 8.3341 | 19.1153 | 48.9002 | -19.6721 | -0.2651 | 55.9252 | 20260612 | -0.94 | 20260615 | ready_exact_signal_date | 11.1307 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1608 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 35.25 | 2.4063 | 6.1728 | 26.8921 | -14.8477 | -0.1221 | 55.9603 | 20260612 | -1.75 | 20260615 | ready_exact_signal_date | 7.8326 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1609 | 20260615 | hot_theme_pullback;price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 38.3 | 3.2589 | 11.6766 | 40.8517 | -15.5814 | -0.2286 | 55.4217 | 20260612 | -1.34 | 20260615 | ready_exact_signal_date | 21.98 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1612 | 20260615 | hot_theme_pullback;price_pullback_23ema | 20260615 | exact_signal_date | 38.1 | 1.6568 | 7.5606 | 23.5465 | -8.7331 | -0.0923 | 56.0209 | 20260612 | -0.13 | 20260615 | ready_exact_signal_date | -13.6269 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1618 | 20260615 | hot_theme_pullback;price_pullback_23ema;pullback_short_reclaim;revenue_unreacted_range | 20260615 | exact_signal_date | 42.45 | 1.8593 | 10.3947 | 23.0159 | -9.6239 | -0.0547 | 50.4373 | 20260612 | 1.54 | 20260615 | ready_exact_signal_date | 153.1627 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1710 | 20260615 | price_pullback_23ema;pullback_short_reclaim | 20260615 | exact_signal_date | 13.75 | -0.43 | 0.0 | 44.9782 | -21.7687 | -0.0801 | 57.3427 | 20260612 | -0.39 | 20260615 | ready_exact_signal_date | -28.8957 | False | 20260615 | mainstream_supported |  | 11.0173 |
| 1714 | 20260615 | volume_range_breakout | 20260615 | exact_signal_date | 16.7 | 40.4718 | 49.0196 | 74.0576 | -10.3922 | 0.6141 | 85.0049 | 20260612 | 0.47 | 20260615 | ready_exact_signal_date | 84.8471 | True | 20260615 | mainstream_supported | non_mainstream_volume_watch | 11.0173 |
| 1723 | 20260615 | pullback_short_reclaim | 20260615 | exact_signal_date | 90.0 | 7.4895 | 11.3956 | 15.2344 | -7.443 | 0.4586 | 73.8095 | 20260612 | 0.3 | 20260615 | ready_exact_signal_date | 58.4405 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1727 | 20260615 | hot_theme_pullback;revenue_unreacted_range | 20260615 | exact_signal_date | 85.6 | -2.8867 | 53.3214 | 115.7996 | -18.2775 | -2.2236 | 20.0 | 20260612 | 0.44 | 20260615 | ready_exact_signal_date | 39.07 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1795 | 20260615 | price_pullback_23ema;revenue_unreacted_range | 20260615 | exact_signal_date | 195.5 | -2.4106 | -8.8167 | 32.967 | -20.6751 | 1.2017 | 52.809 | 20260612 | 0.03 | 20260615 | ready_exact_signal_date | 105.79 | True | 20260615 | mainstream_supported |  | 11.0173 |
| 1802 | 20260615 | hot_theme_pullback;price_pullback_23ema | 20260615 | exact_signal_date | 67.4 | 1.0753 | 11.0919 | 43.2099 | -20.7219 | -0.7984 | 43.0636 | 20260612 | -1.41 | 20260615 | ready_exact_signal_date | 17.7144 | False | 20260615 | non_mainstream |  | 11.0173 |
