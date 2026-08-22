# 營收低反應模型：固定確認口徑勝敗特徵比較

- generated_at: `2026-08-23 07:14:39 Asia/Taipei`
- status: `blocked_pending_root_cause_anomaly_candidate_review`
- 固定候選：強月營收且股價仍在近期 23 日區間、攻擊尚未開始。
- 固定確認：候選後最多三個交易日，收盤突破候選日前 23 日最高收盤價。
- 固定操作：確認後次一交易日開盤進場；確認日 D+20 收盤出場；本輪不加停損。
- 特徵時點：分開比較候選訊號日收盤已知與確認日收盤已知資訊，兩者不得混用。
- 去重：同股操作區間不得重疊；decision basis 同股同月營收期間不得重複計算。
- 候選異常：|報酬| >= 80% 只產生 anomaly candidate；未完成底層根因查核前不得定名為極端值。
- 門檻敏感度：另列排除候選列的數字影響，但不得稱為異常排除、修正後績效或 promotion evidence。
- 月營收候選：未完成底層根因查核前，交易與已觀測 feature value 都保留在 primary evidence；候選排除只能另列 sensitivity。
- 條件政策：本 artifact 只比較單一特徵，不任意疊條件；組合必須另行真實重算。
- 樣本政策：樣本數揭露但不單獨作為否定條件。
- 財務範圍：本輪僅使用 PIT 月營收；EPS、毛利率、營益率、營業利益、業外、淨利及季／年財報全部排除。
- production_change: `none`

## 數字異常檢查

| anomaly_exclusion_basis | accepted_trade_count | same_stock_overlap_pair_count | same_stock_revenue_period_repeat_count | price_path_anomaly_candidate_count | return_abs_ge80_anomaly_candidate_count | source_revenue_or_price_anomaly_candidate_count | signal_feature_context_revenue_anomaly_candidate_count | confirmation_feature_context_revenue_anomaly_candidate_count | feature_context_candidate_values_retained_in_feature_evidence | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | top1_abs_return_share_pct | top5_abs_return_share_pct | avg_realized_return_pct | median_realized_return_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| excluding_abs_ge80_anomaly_candidates_sensitivity_only | 2006 | 0 | 0 | 1 | 0 | 222 | 131 | 130 | True | 79.0657 | 3624 | 20260504 | -54.3003 | 8042 | 20260626 | 0.3329 | 1.5963 | 2.0702 | -1.4867 | 1.7524 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| excluding_unresolved_anomaly_candidates_sensitivity_only | 1802 | 0 | 0 | 0 | 15 | 0 | 0 | 6 | True | 220.603 | 5386 | 20260127 | -54.3003 | 8042 | 20260626 | 0.9638 | 2.822 | 3.2334 | -1.1487 | 2.6198 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 2021 | 0 | 0 | 1 | 15 | 222 | 131 | 130 | True | 220.603 | 5386 | 20260127 | -54.3003 | 8042 | 20260626 | 0.8715 | 2.5516 | 2.8271 | -1.4205 | 2.2376 | blocked_pending_root_cause_anomaly_candidate_review |

## 固定基準

| feature_time_basis_zh | accepted_trade_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | timing_accepted_trade_count_parity_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | 2021.0 | 32.2118 | 13.7556 | 54.0327 | 2.8271 | -1.4205 | 26.1257 | 35.329 | pass |
| 候選訊號日收盤已知 | 2021.0 | 32.2118 | 13.7556 | 54.0327 | 2.8271 | -1.4205 | 26.1257 | 35.329 | pass |

## 成功共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | position120_high_gt75 | price_position | 2021 | 1176 | 66.8561 | 54.9451 | 11.911 | 36.2245 | 12.7551 | 51.0204 | 4.1202 | -0.5437 | 35.2041 | stable_positive |
| 確認日收盤已知 | market_strong_bull | market_regime | 2021 | 1315 | 66.6667 | 63.4615 | 3.2052 | 33.308 | 13.9924 | 52.6996 | 3.4059 | -1.1494 | 34.7529 | stable_positive |
| 確認日收盤已知 | technical_rsi14_40_70 | technical | 2021 | 1412 | 71.9697 | 69.0476 | 2.9221 | 32.6487 | 13.9518 | 53.3994 | 2.999 | -1.157 | 34.6317 | stable_positive |
| 確認日收盤已知 | candle_bullish_attack | candle | 2021 | 1781 | 89.9621 | 87.9121 | 2.05 | 32.7344 | 13.3633 | 53.9023 | 2.9189 | -1.4368 | 35.598 | stable_positive |
| 候選訊號日收盤已知 | position120_high_gt75 | price_position | 2021 | 660 | 38.6364 | 30.2198 | 8.4166 | 37.8788 | 12.1212 | 50.0 | 4.3816 | -0.0821 | 32.7273 | stable_positive |
| 候選訊號日收盤已知 | technical_ma20_above_ma60 | technical | 1600 | 875 | 58.6957 | 53.7757 | 4.92 | 33.7143 | 12.5714 | 53.7143 | 3.0675 | -1.2397 | 35.6571 | stable_positive |
| 候選訊號日收盤已知 | position120_mid_40_75 | price_position | 2021 | 759 | 40.9091 | 36.4469 | 4.4622 | 33.5968 | 13.9657 | 52.4374 | 3.9987 | -0.9836 | 34.7826 | stable_positive |
| 候選訊號日收盤已知 | technical_close_above_ma20_ema23 | technical | 1927 | 1443 | 76.9685 | 73.5067 | 3.4618 | 33.264 | 13.86 | 52.876 | 3.4188 | -1.0309 | 34.0956 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_40_70 | technical | 2021 | 1603 | 82.0076 | 78.663 | 3.3446 | 33.0006 | 13.4124 | 53.587 | 3.1488 | -1.3672 | 34.9345 | stable_positive |
| 候選訊號日收盤已知 | technical_ema23_slope_positive | technical | 1873 | 1341 | 73.8866 | 70.6575 | 3.2291 | 33.4825 | 12.8262 | 53.6913 | 3.4057 | -1.2956 | 34.9739 | stable_positive |
| 候選訊號日收盤已知 | momentum_return20_0_25 | price_momentum | 2021 | 1491 | 75.1894 | 72.8022 | 2.3872 | 32.8638 | 13.8162 | 53.3199 | 3.3894 | -1.1966 | 34.6076 | stable_positive |
| 候選訊號日收盤已知 | technical_obv_above_ma20 | technical | 2021 | 1453 | 72.1591 | 70.6044 | 1.5547 | 33.0351 | 13.9023 | 53.0626 | 2.9298 | -1.1429 | 34.8933 | stable_positive |
| 候選訊號日收盤已知 | market_strong_bull | market_regime | 2021 | 1208 | 60.4167 | 58.9744 | 1.4423 | 32.7815 | 13.9073 | 53.3113 | 3.1209 | -1.3808 | 35.4305 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_ge60 | technical | 2021 | 797 | 40.1515 | 38.7363 | 1.4152 | 33.5006 | 13.4253 | 53.074 | 3.3339 | -1.2397 | 33.6261 | stable_positive |

## 失敗共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 2019 | 321 | 15.1515 | 17.9817 | -2.8302 | 28.6604 | 61.0592 | 0.5736 | -2.682 | 38.9408 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 2012 | 512 | 24.8577 | 27.0295 | -2.1718 | 29.8828 | 57.2266 | 1.342 | -2.1465 | 38.6719 | stable_risk |
| 確認日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 2016 | 761 | 35.4839 | 39.3382 | -3.8543 | 29.9606 | 56.2418 | 1.9315 | -2.0513 | 37.3193 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 2016 | 789 | 35.4167 | 43.2383 | -7.8216 | 28.3904 | 59.5691 | 1.3582 | -2.6891 | 39.6705 | stable_risk |
| 確認日收盤已知 | tdcc_high_thresholds_up | tdcc | 570 | 257 | 39.8438 | 45.045 | -5.2012 | 27.2374 | 58.3658 | -2.2633 | -2.75 | 40.0778 | stable_risk |
| 確認日收盤已知 | tdcc_consecutive_up_ge1 | tdcc | 570 | 341 | 51.5625 | 61.2613 | -9.6988 | 26.0997 | 59.824 | -2.3694 | -3.2258 | 41.349 | stable_risk |
| 確認日收盤已知 | tdcc_consecutive_up_ge2 | tdcc | 570 | 227 | 33.5938 | 41.7417 | -8.1479 | 24.6696 | 61.2335 | -2.7162 | -3.4146 | 42.2907 | stable_risk |
| 確認日收盤已知 | technical_macd_hist_gt0 | technical | 1846 | 1679 | 88.7064 | 91.7413 | -3.0349 | 31.5664 | 54.9136 | 2.5749 | -1.5748 | 35.9738 | stable_risk |
| 確認日收盤已知 | technical_kd_bullish_not_overheated | technical | 2021 | 1562 | 77.8409 | 78.9377 | -1.0968 | 31.4341 | 55.1857 | 2.8126 | -1.6591 | 36.5557 | stable_risk |
| 確認日收盤已知 | technical_bb_width_not_extreme | technical | 2021 | 1097 | 53.5985 | 54.4872 | -0.8887 | 31.9052 | 54.2388 | 2.2192 | -1.3774 | 35.278 | stable_risk |
| 確認日收盤已知 | technical_obv_above_ma20 | technical | 2021 | 1928 | 94.5076 | 95.696 | -1.1884 | 32.0021 | 54.2012 | 2.7248 | -1.4293 | 35.5809 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le10 | price_shape | 2021 | 465 | 12.6894 | 24.5421 | -11.8527 | 22.5806 | 57.6344 | 0.2579 | -1.4205 | 27.5269 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le15 | price_shape | 2021 | 968 | 34.0909 | 50.1832 | -16.0923 | 25.5165 | 56.6116 | 0.8817 | -1.5029 | 30.6818 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le20 | price_shape | 2021 | 1309 | 54.1667 | 66.6667 | -12.5 | 28.6478 | 55.615 | 1.651 | -1.505 | 32.4675 | stable_risk |
| 確認日收盤已知 | position120_low_le40 | price_position | 2021 | 298 | 8.9015 | 16.6667 | -7.7652 | 20.8054 | 61.0738 | -0.6442 | -2.5571 | 34.2282 | stable_risk |
| 確認日收盤已知 | position120_mid_40_75 | price_position | 2021 | 547 | 24.2424 | 28.3883 | -4.1459 | 29.7989 | 56.6728 | 1.9382 | -1.7327 | 36.1974 | stable_risk |
| 確認日收盤已知 | momentum_return20_0_25 | price_momentum | 2021 | 1884 | 90.7197 | 93.956 | -3.2363 | 31.4756 | 54.4586 | 2.4625 | -1.4728 | 35.2442 | stable_risk |
| 確認日收盤已知 | market_mild_bull | market_regime | 2021 | 480 | 21.5909 | 24.9084 | -3.3175 | 29.5833 | 56.6667 | 1.2814 | -1.9838 | 35.8333 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 2019 | 323 | 15.1515 | 17.9817 | -2.8302 | 28.7926 | 60.6811 | 0.6698 | -2.6362 | 38.6997 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 2012 | 534 | 25.0474 | 28.4133 | -3.3659 | 29.0262 | 57.6779 | 1.085 | -2.202 | 38.764 | stable_risk |
| 候選訊號日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 2016 | 777 | 35.8634 | 40.2574 | -4.394 | 29.9871 | 56.3707 | 1.9057 | -2.0537 | 37.1943 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 2016 | 803 | 34.4697 | 44.3422 | -9.8725 | 27.3973 | 60.0249 | 1.1477 | -2.6549 | 39.477 | stable_risk |
| 候選訊號日收盤已知 | tdcc_high_thresholds_up | tdcc | 547 | 230 | 38.7931 | 41.2844 | -2.4913 | 26.9565 | 58.6957 | -2.6082 | -3.1585 | 41.3043 | stable_risk |
| 候選訊號日收盤已知 | tdcc_consecutive_up_ge1 | tdcc | 547 | 315 | 54.3103 | 58.4098 | -4.0995 | 26.6667 | 60.6349 | -2.5337 | -3.2803 | 41.9048 | stable_risk |
| 候選訊號日收盤已知 | tdcc_consecutive_up_ge2 | tdcc | 547 | 216 | 33.6207 | 41.896 | -8.2753 | 23.6111 | 63.4259 | -2.8504 | -3.4701 | 43.0556 | stable_risk |
| 候選訊號日收盤已知 | technical_macd_hist_gt0 | technical | 1817 | 1206 | 61.3169 | 67.0061 | -5.6892 | 31.1774 | 54.5605 | 2.4061 | -1.4122 | 34.2454 | stable_risk |
| 候選訊號日收盤已知 | technical_kd_bullish_not_overheated | technical | 2021 | 1157 | 54.3561 | 58.1502 | -3.7941 | 30.5964 | 54.8833 | 2.1591 | -1.5009 | 35.4365 | stable_risk |
| 候選訊號日收盤已知 | technical_kdj_bullish_not_extreme | technical | 2021 | 1160 | 55.6818 | 58.1502 | -2.4684 | 31.3793 | 54.7414 | 2.2909 | -1.5354 | 35.2586 | stable_risk |
| 候選訊號日收盤已知 | technical_bb_width_not_extreme | technical | 2021 | 1191 | 58.3333 | 59.9817 | -1.6484 | 31.822 | 54.9958 | 2.0297 | -1.5 | 36.6079 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le10 | price_shape | 2021 | 464 | 11.553 | 24.8168 | -13.2638 | 21.3362 | 58.4052 | -0.0921 | -1.5563 | 28.6638 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le15 | price_shape | 2021 | 933 | 32.0076 | 48.3516 | -16.344 | 25.1876 | 56.5916 | 0.9839 | -1.4726 | 30.4394 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le20 | price_shape | 2021 | 1273 | 52.0833 | 65.1099 | -13.0266 | 28.5939 | 55.8523 | 1.6308 | -1.505 | 32.5216 | stable_risk |
| 候選訊號日收盤已知 | shape_near_range23_high | price_shape | 2021 | 1082 | 44.1288 | 54.9451 | -10.8163 | 28.9279 | 55.4529 | 1.9396 | -1.4173 | 32.2551 | stable_risk |
| 候選訊號日收盤已知 | position120_low_le40 | price_position | 2021 | 602 | 20.4545 | 33.3333 | -12.8788 | 24.2525 | 60.4651 | -0.3542 | -2.7465 | 38.8704 | stable_risk |
| 候選訊號日收盤已知 | market_mild_bull | market_regime | 2021 | 443 | 19.697 | 22.8022 | -3.1052 | 29.5711 | 56.2077 | 2.4181 | -1.676 | 35.2144 | stable_risk |

## Large Detail Policy

逐筆重算 evidence 僅保留於 `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv`；不複製到 docs/latest 或 output/history。
