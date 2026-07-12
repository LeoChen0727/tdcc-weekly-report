# 營收低反應模型：固定確認口徑勝敗特徵比較

- generated_at: `2026-07-12 17:20:58 Asia/Taipei`
- status: `research_only_fixed_feature_contrast_not_promotion_ready`
- 固定候選：強月營收且股價仍在近期 23 日區間、攻擊尚未開始。
- 固定確認：候選後最多三個交易日，收盤突破候選日前 23 日最高收盤價。
- 固定操作：確認後次一交易日開盤進場；確認日 D+20 收盤出場；本輪不加停損。
- 特徵時點：分開比較候選訊號日收盤已知與確認日收盤已知資訊，兩者不得混用。
- 去重：同股操作區間不得重疊；decision basis 同股同月營收期間不得重複計算。
- 異常敏感度：另列排除 |報酬| >= 80% 的敏感度，不把連續價格路徑的極端報酬直接當成錯價。
- 月營收異常：交易基準保留，但 feature context 已標記的月營收數字異常不得進 binary 或 numeric feature evidence。
- 條件政策：本 artifact 只比較單一特徵，不任意疊條件；組合必須另行真實重算。
- 樣本政策：樣本數揭露但不單獨作為否定條件。
- 財務範圍：本輪僅使用 PIT 月營收；EPS、毛利率、營益率、營業利益、業外、淨利及季／年財報全部排除。
- production_change: `none`

## 數字異常檢查

| anomaly_exclusion_basis | accepted_trade_count | same_stock_overlap_pair_count | same_stock_revenue_period_repeat_count | price_path_anomaly_count | return_abs_ge80_count | signal_feature_context_revenue_anomaly_count | confirmation_feature_context_revenue_anomaly_count | feature_context_revenue_anomalies_excluded_from_feature_evidence | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | top1_abs_return_share_pct | top5_abs_return_share_pct | avg_realized_return_pct | median_realized_return_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_known_revenue_and_price_anomalies | 1530 | 0 | 0 | 0 | 14 | 0 | 6 | True | 115.6923 | 2327 | 20260424 | -40.676 | 2540 | 20250902 | 0.5878 | 2.6298 | 4.5061 | -0.1421 | 3.9194 | anomaly_check_pass_with_abs_ge80_sensitivity_required |
| excluding_known_revenue_price_and_abs_ge80_return_sensitivity | 1516 | 0 | 0 | 0 | 0 | 0 | 6 | True | 79.0657 | 3624 | 20260504 | -40.676 | 2540 | 20250902 | 0.4307 | 2.0208 | 3.6739 | -0.3528 | 3.3122 | abs_ge80_return_sensitivity_only_not_automatic_exclusion |
| including_known_anomalies | 1702 | 0 | 0 | 1 | 14 | 102 | 101 | True | 117.3077 | 6949 | 20250710 | -40.676 | 2540 | 20250902 | 0.542 | 2.4732 | 4.0604 | -0.6229 | 3.4718 | not_decision_basis_known_anomalies_included |

## 固定基準

| feature_time_basis_zh | accepted_trade_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | timing_accepted_trade_count_parity_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | 1530.0 | 35.3595 | 14.5098 | 50.1307 | 4.5061 | -0.1421 | 28.6928 | 32.2222 | pass |
| 候選訊號日收盤已知 | 1530.0 | 35.3595 | 14.5098 | 50.1307 | 4.5061 | -0.1421 | 28.6928 | 32.2222 | pass |

## 成功共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | extreme_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1523 | 699 | 52.7523 | 42.9882 | 9.7641 | 40.4864 | 12.5894 | 46.9242 | 5.3355 | 0.996 | 31.0443 | stable_positive |
| 確認日收盤已知 | position120_high_gt75 | price_position | 1530 | 942 | 68.7927 | 60.3651 | 8.4276 | 38.535 | 12.3142 | 49.1507 | 5.5923 | 0.0675 | 32.9087 | stable_positive |
| 確認日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1523 | 331 | 26.8349 | 19.5282 | 7.3067 | 41.994 | 12.9909 | 45.0151 | 6.0671 | 1.7003 | 31.1178 | stable_positive |
| 確認日收盤已知 | technical_ma20_above_ma60 | technical | 1185 | 687 | 63.2184 | 56.5517 | 6.6667 | 38.7191 | 13.5371 | 47.7438 | 5.7321 | 0.5398 | 32.1689 | stable_positive |
| 確認日收盤已知 | technical_rsi14_40_70 | technical | 1530 | 1063 | 71.754 | 67.927 | 3.827 | 36.1242 | 14.8636 | 49.0122 | 4.858 | 0.0 | 31.1383 | stable_positive |
| 確認日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1530 | 101 | 7.5171 | 5.9974 | 1.5197 | 37.6238 | 16.8317 | 45.5446 | 7.8865 | 1.8868 | 32.6733 | stable_positive |
| 確認日收盤已知 | market_mild_bull | market_regime | 1530 | 336 | 22.5513 | 21.2516 | 1.2997 | 35.4167 | 16.0714 | 48.5119 | 4.8545 | 0.343 | 29.7619 | stable_positive |
| 確認日收盤已知 | technical_ema23_slope_positive | technical | 1424 | 1328 | 94.2308 | 93.617 | 0.6138 | 36.3705 | 13.9307 | 49.6988 | 4.8375 | 0.0 | 32.003 | stable_positive |
| 候選訊號日收盤已知 | position120_high_gt75 | price_position | 1530 | 518 | 41.2301 | 31.2907 | 9.9394 | 42.278 | 11.39 | 46.332 | 6.478 | 1.1588 | 29.9228 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1529 | 713 | 52.6196 | 43.8642 | 8.7554 | 39.9719 | 12.9032 | 47.1248 | 5.2699 | 0.9346 | 30.8555 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1529 | 333 | 26.8793 | 19.4517 | 7.4276 | 41.7417 | 13.5135 | 44.7447 | 6.2869 | 1.8564 | 30.3303 | stable_positive |
| 候選訊號日收盤已知 | technical_ma20_above_ma60 | technical | 1174 | 655 | 60.8696 | 54.1812 | 6.6884 | 38.9313 | 13.5878 | 47.4809 | 5.8216 | 0.5772 | 31.6031 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_40_70 | technical | 1530 | 1209 | 82.6879 | 77.8357 | 4.8522 | 36.7246 | 13.8958 | 49.3797 | 5.0263 | 0.0 | 31.5136 | stable_positive |
| 候選訊號日收盤已知 | volume_ratio_le1_5 | volume | 1530 | 1180 | 80.1822 | 76.0104 | 4.1718 | 36.3559 | 14.2373 | 49.4068 | 4.6389 | 0.0 | 31.8644 | stable_positive |
| 候選訊號日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1530 | 184 | 13.4396 | 10.8214 | 2.6182 | 41.3043 | 13.587 | 45.1087 | 6.8355 | 1.9627 | 28.2609 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_ge60 | technical | 1530 | 621 | 41.9134 | 39.7653 | 2.1481 | 37.5201 | 13.3655 | 49.1143 | 4.7846 | 0.2903 | 31.0789 | stable_positive |
| 候選訊號日收盤已知 | technical_ema23_slope_positive | technical | 1405 | 1031 | 75.6627 | 73.8817 | 1.781 | 37.5364 | 12.8031 | 49.6605 | 5.2353 | 0.0 | 32.2017 | stable_positive |
| 候選訊號日收盤已知 | momentum_return20_0_25 | price_momentum | 1530 | 1144 | 75.8542 | 74.3155 | 1.5387 | 35.9266 | 14.2483 | 49.8252 | 4.7208 | 0.0 | 31.6434 | stable_positive |
| 候選訊號日收盤已知 | technical_close_above_ma20_ema23 | technical | 1461 | 1118 | 77.6722 | 76.3411 | 1.3311 | 36.6726 | 13.6852 | 49.6422 | 4.9561 | 0.0 | 31.7531 | stable_positive |

## 失敗共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | extreme_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1520 | 376 | 23.1651 | 26.3158 | -3.1507 | 33.2447 | 53.1915 | 3.2611 | -1.0465 | 34.0426 | stable_risk |
| 確認日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1523 | 554 | 34.4037 | 38.9253 | -4.5216 | 32.852 | 53.6101 | 3.2146 | -1.1684 | 33.935 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1521 | 581 | 34.4037 | 42.0499 | -7.6462 | 31.1532 | 55.0775 | 3.2421 | -1.5537 | 35.8003 | stable_risk |
| 確認日收盤已知 | technical_obv_above_ma20 | technical | 1530 | 1461 | 94.533 | 96.219 | -1.686 | 34.976 | 50.5133 | 4.4477 | -0.3268 | 32.3066 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le10 | price_shape | 1530 | 362 | 10.9339 | 27.1186 | -16.1847 | 20.7182 | 57.4586 | 0.2789 | -1.5124 | 28.453 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le15 | price_shape | 1530 | 738 | 31.4351 | 52.9335 | -21.4984 | 26.0163 | 55.0136 | 1.2441 | -1.1936 | 30.3523 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le20 | price_shape | 1530 | 996 | 52.3918 | 69.4915 | -17.0997 | 30.0201 | 53.5141 | 2.358 | -1.0402 | 31.7269 | stable_risk |
| 確認日收盤已知 | position120_low_le40 | price_position | 1530 | 196 | 7.5171 | 13.9505 | -6.4334 | 22.449 | 54.5918 | 0.3094 | -1.6576 | 32.6531 | stable_risk |
| 確認日收盤已知 | momentum_return20_0_25 | price_momentum | 1530 | 1434 | 90.8884 | 94.7849 | -3.8965 | 34.4491 | 50.6974 | 4.0416 | -0.3886 | 32.357 | stable_risk |
| 確認日收盤已知 | market_strong_bull | market_regime | 1530 | 1093 | 69.9317 | 72.751 | -2.8193 | 35.1327 | 51.0522 | 4.0866 | -0.4902 | 32.9369 | stable_risk |
| 確認日收盤已知 | market_bull | market_regime | 1530 | 1429 | 92.4829 | 94.0026 | -1.5197 | 35.1994 | 50.4549 | 4.2672 | -0.3268 | 32.1903 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1526 | 396 | 23.4624 | 27.9161 | -4.4537 | 32.3232 | 53.7879 | 3.0506 | -1.3171 | 34.596 | stable_risk |
| 候選訊號日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1529 | 569 | 34.6241 | 39.6867 | -5.0626 | 32.8647 | 53.4271 | 3.277 | -1.1429 | 33.9192 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1527 | 592 | 34.1686 | 42.4084 | -8.2398 | 30.7432 | 54.7297 | 3.1957 | -1.5256 | 35.3041 | stable_risk |
| 候選訊號日收盤已知 | technical_kd_bullish_not_overheated | technical | 1530 | 898 | 54.6697 | 61.9296 | -7.2599 | 33.1849 | 52.8953 | 3.4394 | -0.9047 | 34.0757 | stable_risk |
| 候選訊號日收盤已知 | technical_kdj_bullish_not_extreme | technical | 1530 | 888 | 55.3531 | 61.1473 | -5.7942 | 33.6712 | 52.8153 | 3.5844 | -0.9977 | 34.7973 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le10 | price_shape | 1530 | 360 | 9.5672 | 27.3794 | -17.8122 | 18.6111 | 58.3333 | -0.2064 | -1.6426 | 28.6111 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le15 | price_shape | 1530 | 720 | 29.8405 | 51.7601 | -21.9196 | 25.4167 | 55.1389 | 1.3576 | -1.1936 | 30.2778 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le20 | price_shape | 1530 | 976 | 50.5695 | 68.3181 | -17.7486 | 29.8156 | 53.6885 | 2.3283 | -0.9977 | 31.6598 | stable_risk |
| 候選訊號日收盤已知 | shape_near_range23_high | price_shape | 1530 | 835 | 43.7358 | 57.8879 | -14.1521 | 30.7784 | 53.1737 | 2.72 | -0.8969 | 31.7365 | stable_risk |
| 候選訊號日收盤已知 | position120_low_le40 | price_position | 1530 | 433 | 20.7289 | 30.7692 | -10.0403 | 27.2517 | 54.5035 | 1.445 | -1.6393 | 35.7968 | stable_risk |
| 候選訊號日收盤已知 | market_mild_bull | market_regime | 1530 | 372 | 22.5513 | 25.8149 | -3.2636 | 31.4516 | 53.2258 | 4.0847 | -0.9916 | 32.5269 | stable_risk |
| 候選訊號日收盤已知 | market_bull | market_regime | 1530 | 1346 | 86.5604 | 89.1786 | -2.6182 | 34.5468 | 50.8172 | 4.1876 | -0.4179 | 32.7637 | stable_risk |

## Large Detail Policy

逐筆重算 evidence 僅保留於 `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv`；不複製到 docs/latest 或 output/history。
