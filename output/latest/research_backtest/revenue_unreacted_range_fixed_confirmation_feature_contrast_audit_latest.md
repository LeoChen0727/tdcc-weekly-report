# 營收低反應模型：固定確認口徑勝敗特徵比較

- generated_at: `2026-07-14 14:26:43 Asia/Taipei`
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
| excluding_abs_ge80_anomaly_candidates_sensitivity_only | 1696 | 0 | 0 | 1 | 0 | 178 | 105 | 104 | True | 79.0657 | 3624 | 20260504 | -40.676 | 2540 | 20250902 | 0.3876 | 1.8352 | 3.3145 | -0.7526 | 2.9691 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| excluding_unresolved_anomaly_candidates_sensitivity_only | 1533 | 0 | 0 | 0 | 14 | 0 | 0 | 6 | True | 115.6923 | 2327 | 20260424 | -40.676 | 2540 | 20250902 | 0.5872 | 2.6274 | 4.4858 | -0.1761 | 3.8999 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 1710 | 0 | 0 | 1 | 14 | 178 | 105 | 104 | True | 117.3077 | 6949 | 20250710 | -40.676 | 2540 | 20250902 | 0.5394 | 2.4613 | 4.0763 | -0.651 | 3.4908 | blocked_pending_root_cause_anomaly_candidate_review |

## 固定基準

| feature_time_basis_zh | accepted_trade_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | timing_accepted_trade_count_parity_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | 1710.0 | 34.5029 | 13.8596 | 51.6374 | 4.0763 | -0.651 | 28.1871 | 33.1579 | pass |
| 候選訊號日收盤已知 | 1710.0 | 34.5029 | 13.8596 | 51.6374 | 4.0763 | -0.651 | 28.1871 | 33.1579 | pass |

## 成功共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | position120_high_gt75 | price_position | 1710 | 1021 | 67.4274 | 57.5311 | 9.8963 | 38.0999 | 12.145 | 49.7551 | 5.2449 | 0.0 | 33.8883 | stable_positive |
| 確認日收盤已知 | technical_ma20_above_ma60 | technical | 1319 | 750 | 62.2396 | 54.9849 | 7.2547 | 38.1333 | 13.3333 | 48.5333 | 5.5085 | 0.376 | 32.6667 | stable_positive |
| 確認日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1708 | 823 | 53.3195 | 46.765 | 6.5545 | 38.1531 | 11.7861 | 50.0608 | 4.5196 | -0.1927 | 32.6853 | stable_positive |
| 確認日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1708 | 451 | 29.8755 | 26.1067 | 3.7688 | 37.694 | 11.3082 | 50.9978 | 4.4616 | -0.5256 | 34.1463 | stable_positive |
| 確認日收盤已知 | technical_rsi14_40_70 | technical | 1710 | 1194 | 71.5768 | 68.4032 | 3.1736 | 35.0921 | 14.3216 | 50.5863 | 4.3477 | -0.3268 | 32.1608 | stable_positive |
| 確認日收盤已知 | technical_bb_width_not_extreme | technical | 1710 | 874 | 51.8672 | 49.4904 | 2.3768 | 35.2403 | 14.7597 | 50.0 | 4.0871 | -0.0552 | 32.0366 | stable_positive |
| 確認日收盤已知 | volume_ratio_le2 | volume | 1710 | 892 | 52.6971 | 50.3964 | 2.3007 | 35.2018 | 14.9103 | 49.8879 | 4.736 | 0.0 | 29.5964 | stable_positive |
| 確認日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1710 | 124 | 7.8838 | 6.9083 | 0.9755 | 36.2903 | 14.5161 | 49.1935 | 7.0118 | 0.1525 | 33.871 | stable_positive |
| 確認日收盤已知 | technical_ema23_slope_positive | technical | 1587 | 1471 | 93.6543 | 92.8218 | 0.8325 | 35.69 | 13.3243 | 50.9857 | 4.5093 | -0.4367 | 32.6988 | stable_positive |
| 確認日收盤已知 | market_mild_bull | market_regime | 1710 | 377 | 22.1992 | 21.7441 | 0.4551 | 33.9523 | 15.1194 | 50.9284 | 4.415 | -0.4367 | 31.0345 | stable_positive |
| 候選訊號日收盤已知 | position120_high_gt75 | price_position | 1710 | 556 | 39.6266 | 29.7848 | 9.8418 | 41.5468 | 11.1511 | 47.3022 | 6.2388 | 0.9294 | 31.1151 | stable_positive |
| 候選訊號日收盤已知 | technical_ma20_above_ma60 | technical | 1308 | 710 | 59.3176 | 52.439 | 6.8786 | 38.169 | 13.3803 | 48.4507 | 5.5427 | 0.376 | 32.2535 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1708 | 832 | 53.112 | 47.2191 | 5.8929 | 37.8606 | 12.1394 | 50.0 | 4.4482 | -0.0964 | 32.5721 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1708 | 445 | 29.668 | 25.4257 | 4.2423 | 37.7528 | 11.9101 | 50.3371 | 4.636 | -0.2829 | 33.4831 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_40_70 | technical | 1710 | 1355 | 82.1577 | 78.4824 | 3.6753 | 35.572 | 13.2841 | 51.1439 | 4.5113 | -0.443 | 32.3985 | stable_positive |
| 候選訊號日收盤已知 | momentum_return20_0_25 | price_momentum | 1710 | 1263 | 75.5187 | 72.7067 | 2.812 | 35.3127 | 13.8559 | 50.8314 | 4.4614 | -0.4127 | 32.2249 | stable_positive |
| 候選訊號日收盤已知 | technical_ema23_slope_positive | technical | 1567 | 1125 | 74.5614 | 71.8239 | 2.7375 | 36.8889 | 12.3556 | 50.7556 | 4.9976 | -0.4049 | 32.7111 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_ge60 | technical | 1710 | 683 | 41.4938 | 39.1846 | 2.3092 | 36.896 | 12.4451 | 50.6589 | 4.5201 | -0.4902 | 31.918 | stable_positive |
| 候選訊號日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1710 | 217 | 13.9004 | 11.8913 | 2.0091 | 39.1705 | 12.4424 | 48.3871 | 6.0333 | 0.4464 | 29.4931 | stable_positive |
| 候選訊號日收盤已知 | technical_close_above_ma20_ema23 | technical | 1630 | 1238 | 77.0563 | 75.9569 | 1.0994 | 35.7835 | 12.9241 | 51.2924 | 4.5957 | -0.5049 | 32.8756 | stable_positive |

## 失敗共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 1708 | 264 | 15.3527 | 17.2531 | -1.9004 | 32.5758 | 57.5758 | 1.9658 | -1.9167 | 34.8485 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1701 | 412 | 22.4532 | 25.8286 | -3.3754 | 32.0388 | 54.8544 | 2.8698 | -1.4462 | 35.1942 | stable_risk |
| 確認日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1705 | 614 | 34.3035 | 38.1115 | -3.808 | 32.0847 | 54.5603 | 3.0329 | -1.3917 | 34.5277 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1705 | 672 | 35.0622 | 43.2802 | -8.218 | 30.2083 | 56.5476 | 2.6507 | -1.7927 | 36.6071 | stable_risk |
| 確認日收盤已知 | technical_obv_above_ma20 | technical | 1710 | 1629 | 93.9834 | 96.0362 | -2.0528 | 34.07 | 52.0565 | 3.9503 | -0.7376 | 33.4561 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le10 | price_shape | 1710 | 417 | 12.6556 | 27.0668 | -14.4112 | 22.0624 | 57.3141 | 0.5585 | -1.454 | 28.0576 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le15 | price_shape | 1710 | 848 | 33.8174 | 53.5674 | -19.75 | 26.2972 | 55.7783 | 1.2185 | -1.2873 | 30.4245 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le20 | price_shape | 1710 | 1132 | 53.7344 | 70.4417 | -16.7073 | 29.5053 | 54.947 | 2.0547 | -1.3314 | 32.3322 | stable_risk |
| 確認日收盤已知 | position120_low_le40 | price_position | 1710 | 232 | 8.0913 | 15.0623 | -6.971 | 22.4138 | 57.3276 | 0.2648 | -1.9057 | 31.8966 | stable_risk |
| 確認日收盤已知 | position120_mid_40_75 | price_position | 1710 | 457 | 24.4813 | 27.4066 | -2.9253 | 32.6039 | 52.954 | 3.4003 | -0.7331 | 32.1663 | stable_risk |
| 確認日收盤已知 | momentum_return20_0_25 | price_momentum | 1710 | 1605 | 91.0788 | 94.7905 | -3.7117 | 33.6449 | 52.1495 | 3.6464 | -0.7617 | 33.2087 | stable_risk |
| 確認日收盤已知 | market_strong_bull | market_regime | 1710 | 1209 | 69.917 | 71.3477 | -1.4307 | 34.4913 | 52.1092 | 3.6695 | -0.7712 | 33.7469 | stable_risk |
| 確認日收盤已知 | market_bull | market_regime | 1710 | 1586 | 92.1162 | 93.0917 | -0.9755 | 34.3632 | 51.8285 | 3.8468 | -0.7353 | 33.1021 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 1708 | 262 | 15.1452 | 17.0261 | -1.8809 | 32.8244 | 57.2519 | 1.984 | -1.9167 | 34.7328 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1701 | 434 | 22.4532 | 27.7714 | -5.3182 | 30.6452 | 55.9908 | 2.3775 | -1.7758 | 36.4055 | stable_risk |
| 候選訊號日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1705 | 632 | 34.5114 | 39.2491 | -4.7377 | 31.962 | 54.5886 | 2.9531 | -1.3143 | 34.4937 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1705 | 685 | 34.4398 | 44.3052 | -9.8654 | 29.3431 | 56.7883 | 2.3982 | -1.8315 | 36.7883 | stable_risk |
| 候選訊號日收盤已知 | tdcc_consecutive_up_ge2 | tdcc | 308 | 95 | 25.3012 | 33.557 | -8.2558 | 30.5263 | 52.6316 | 1.0441 | -0.722 | 31.5789 | stable_risk |
| 候選訊號日收盤已知 | technical_kd_bullish_not_overheated | technical | 1710 | 995 | 54.1494 | 61.0419 | -6.8925 | 32.4623 | 54.1709 | 3.1092 | -1.2956 | 34.4724 | stable_risk |
| 候選訊號日收盤已知 | technical_kdj_bullish_not_extreme | technical | 1710 | 986 | 55.3942 | 60.2492 | -4.855 | 32.9615 | 53.9554 | 3.3058 | -1.4047 | 35.0913 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le10 | price_shape | 1710 | 416 | 11.2033 | 27.5198 | -16.3165 | 19.9519 | 58.4135 | 0.0037 | -1.5124 | 28.8462 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le15 | price_shape | 1710 | 824 | 32.1577 | 51.9819 | -19.8242 | 25.8495 | 55.7039 | 1.3396 | -1.2481 | 30.4612 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le20 | price_shape | 1710 | 1111 | 52.0747 | 69.3092 | -17.2345 | 29.3429 | 55.0855 | 2.0461 | -1.2956 | 32.3132 | stable_risk |
| 候選訊號日收盤已知 | shape_near_range23_high | price_shape | 1710 | 943 | 45.4357 | 57.9841 | -12.5484 | 30.6469 | 54.2948 | 2.6025 | -1.1329 | 32.0255 | stable_risk |
| 候選訊號日收盤已知 | position120_low_le40 | price_position | 1710 | 505 | 22.1992 | 32.1631 | -9.9639 | 27.1287 | 56.2376 | 1.1981 | -1.7483 | 35.4455 | stable_risk |
| 候選訊號日收盤已知 | market_mild_bull | market_regime | 1710 | 415 | 22.6141 | 25.8211 | -3.207 | 30.8434 | 54.9398 | 3.6661 | -1.4103 | 34.6988 | stable_risk |
| 候選訊號日收盤已知 | market_bull | market_regime | 1710 | 1493 | 86.0996 | 88.1087 | -2.0091 | 33.8245 | 52.1098 | 3.7918 | -0.7874 | 33.6906 | stable_risk |

## Large Detail Policy

逐筆重算 evidence 僅保留於 `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv`；不複製到 docs/latest 或 output/history。
