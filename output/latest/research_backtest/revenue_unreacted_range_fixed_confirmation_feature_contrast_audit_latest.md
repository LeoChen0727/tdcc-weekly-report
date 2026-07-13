# 營收低反應模型：固定確認口徑勝敗特徵比較

- generated_at: `2026-07-13 20:50:41 Asia/Taipei`
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
| excluding_abs_ge80_anomaly_candidates_sensitivity_only | 1688 | 0 | 0 | 1 | 0 | 173 | 102 | 101 | True | 79.0657 | 3624 | 20260504 | -40.676 | 2540 | 20250902 | 0.3896 | 1.8447 | 3.2949 | -0.7406 | 2.9481 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| excluding_unresolved_anomaly_candidates_sensitivity_only | 1530 | 0 | 0 | 0 | 14 | 0 | 0 | 6 | True | 115.6923 | 2327 | 20260424 | -40.676 | 2540 | 20250902 | 0.5878 | 2.6298 | 4.5061 | -0.1421 | 3.9194 | candidate_threshold_sensitivity_only_not_anomaly_disposition |
| including_unresolved_anomaly_candidates_primary | 1702 | 0 | 0 | 1 | 14 | 173 | 102 | 101 | True | 117.3077 | 6949 | 20250710 | -40.676 | 2540 | 20250902 | 0.542 | 2.4732 | 4.0604 | -0.6229 | 3.4718 | blocked_pending_root_cause_anomaly_candidate_review |

## 固定基準

| feature_time_basis_zh | accepted_trade_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | timing_accepted_trade_count_parity_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | 1702.0 | 34.4888 | 13.9248 | 51.5864 | 4.0604 | -0.6229 | 28.2021 | 33.1962 | pass |
| 候選訊號日收盤已知 | 1702.0 | 34.4888 | 13.9248 | 51.5864 | 4.0604 | -0.6229 | 28.2021 | 33.1962 | pass |

## 成功共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | position120_high_gt75 | price_position | 1702 | 1019 | 67.5 | 57.7449 | 9.7551 | 38.0765 | 12.1688 | 49.7547 | 5.2018 | 0.0 | 33.8567 | stable_positive |
| 確認日收盤已知 | technical_ma20_above_ma60 | technical | 1311 | 747 | 62.3037 | 55.0989 | 7.2048 | 38.1526 | 13.3869 | 48.4605 | 5.465 | 0.4175 | 32.5301 | stable_positive |
| 確認日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1701 | 818 | 53.3333 | 46.6363 | 6.697 | 38.1418 | 11.8582 | 50.0 | 4.5483 | -0.0964 | 32.6406 | stable_positive |
| 確認日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1701 | 447 | 29.7917 | 25.9977 | 3.794 | 37.5839 | 11.4094 | 51.0067 | 4.4916 | -0.5256 | 34.2282 | stable_positive |
| 確認日收盤已知 | technical_rsi14_40_70 | technical | 1702 | 1189 | 71.6667 | 68.451 | 3.2157 | 35.0715 | 14.3818 | 50.5467 | 4.3658 | -0.3268 | 32.2119 | stable_positive |
| 確認日收盤已知 | technical_bb_width_not_extreme | technical | 1702 | 868 | 51.875 | 49.3166 | 2.5584 | 35.2535 | 14.8618 | 49.8848 | 4.1093 | 0.0 | 32.1429 | stable_positive |
| 確認日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1702 | 116 | 7.5 | 6.3781 | 1.1219 | 36.2069 | 15.5172 | 48.2759 | 6.9817 | 0.4409 | 34.4828 | stable_positive |
| 確認日收盤已知 | technical_ema23_slope_positive | technical | 1579 | 1464 | 93.6264 | 92.9016 | 0.7248 | 35.6557 | 13.388 | 50.9563 | 4.4874 | -0.4299 | 32.7186 | stable_positive |
| 確認日收盤已知 | market_mild_bull | market_regime | 1702 | 377 | 22.2917 | 21.8679 | 0.4238 | 33.9523 | 15.1194 | 50.9284 | 4.415 | -0.4367 | 31.0345 | stable_positive |
| 候選訊號日收盤已知 | position120_high_gt75 | price_position | 1702 | 555 | 39.5833 | 29.9544 | 9.6289 | 41.4414 | 11.1712 | 47.3874 | 6.1319 | 0.9063 | 31.1712 | stable_positive |
| 候選訊號日收盤已知 | technical_ma20_above_ma60 | technical | 1300 | 707 | 59.3668 | 52.5346 | 6.8322 | 38.1895 | 13.4371 | 48.3734 | 5.4969 | 0.4175 | 32.1075 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest30_and_cumulative20 | monthly_revenue | 1701 | 827 | 53.125 | 47.0924 | 6.0326 | 37.8476 | 12.2128 | 49.9395 | 4.4761 | 0.0 | 32.5272 | stable_positive |
| 候選訊號日收盤已知 | revenue_latest50_and_cumulative30 | monthly_revenue | 1701 | 441 | 29.5833 | 25.3136 | 4.2697 | 37.6417 | 12.0181 | 50.3401 | 4.668 | -0.2829 | 33.5601 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_40_70 | technical | 1702 | 1348 | 82.0833 | 78.4738 | 3.6095 | 35.5341 | 13.3531 | 51.1128 | 4.4866 | -0.4398 | 32.4926 | stable_positive |
| 候選訊號日收盤已知 | technical_ema23_slope_positive | technical | 1559 | 1119 | 74.4493 | 71.7722 | 2.6771 | 36.908 | 12.4218 | 50.6702 | 4.9733 | -0.3724 | 32.7078 | stable_positive |
| 候選訊號日收盤已知 | momentum_return20_0_25 | price_momentum | 1702 | 1258 | 75.4167 | 72.8929 | 2.5238 | 35.2146 | 13.911 | 50.8744 | 4.4189 | -0.4179 | 32.2734 | stable_positive |
| 候選訊號日收盤已知 | technical_rsi14_ge60 | technical | 1702 | 678 | 41.4583 | 39.0661 | 2.3922 | 36.8732 | 12.5369 | 50.59 | 4.4575 | -0.4515 | 32.0059 | stable_positive |
| 候選訊號日收盤已知 | market_correction_or_high_risk | market_regime_risk | 1702 | 216 | 13.9583 | 11.8451 | 2.1132 | 39.3519 | 12.5 | 48.1481 | 6.0657 | 0.5116 | 29.6296 | stable_positive |
| 候選訊號日收盤已知 | technical_close_above_ma20_ema23 | technical | 1622 | 1231 | 76.9565 | 75.9326 | 1.0239 | 35.7433 | 12.9976 | 51.2591 | 4.5701 | -0.4902 | 32.9001 | stable_positive |

## 失敗共同特徵候選

| feature_time_basis_zh | feature_id | feature_family | feature_observed_count | feature_hit_count | high_return_feature_hit_rate_within_observed_pct | failure_feature_hit_rate_within_observed_pct | high_return_minus_failure_hit_rate_within_observed_pct | win_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | loss_5_rate_pct | candidate_threshold_sensitivity_direction_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 確認日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 1701 | 259 | 15.2083 | 16.9897 | -1.7814 | 32.4324 | 57.529 | 1.9902 | -2.1417 | 35.1351 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1694 | 411 | 22.547 | 25.8324 | -3.2854 | 32.1168 | 54.7445 | 2.9041 | -1.4218 | 35.0365 | stable_risk |
| 確認日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1698 | 612 | 34.4468 | 38.0571 | -3.6103 | 32.1895 | 54.4118 | 3.0626 | -1.3917 | 34.4771 | stable_risk |
| 確認日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1698 | 670 | 35.0 | 43.3638 | -8.3638 | 30.1493 | 56.5672 | 2.6452 | -1.8134 | 36.7164 | stable_risk |
| 確認日收盤已知 | technical_obv_above_ma20 | technical | 1702 | 1621 | 93.9583 | 96.0137 | -2.0554 | 34.0531 | 52.0049 | 3.9331 | -0.7331 | 33.4978 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le10 | price_shape | 1702 | 413 | 12.5 | 26.9932 | -14.4932 | 21.7918 | 57.385 | 0.5533 | -1.4599 | 28.0872 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le15 | price_shape | 1702 | 842 | 33.75 | 53.4169 | -19.6669 | 26.247 | 55.7007 | 1.2294 | -1.3314 | 30.4038 | stable_risk |
| 確認日收盤已知 | shape_range23_width_le20 | price_shape | 1702 | 1125 | 53.75 | 70.2733 | -16.5233 | 29.5111 | 54.8444 | 2.0729 | -1.3672 | 32.3556 | stable_risk |
| 確認日收盤已知 | position120_low_le40 | price_position | 1702 | 231 | 8.125 | 15.0342 | -6.9092 | 22.5108 | 57.1429 | 0.2839 | -1.7105 | 32.0346 | stable_risk |
| 確認日收盤已知 | position120_mid_40_75 | price_position | 1702 | 452 | 24.375 | 27.221 | -2.846 | 32.5221 | 52.8761 | 3.4172 | -0.7329 | 32.3009 | stable_risk |
| 確認日收盤已知 | momentum_return20_0_25 | price_momentum | 1702 | 1598 | 91.25 | 94.7608 | -3.5108 | 33.6671 | 52.0651 | 3.6661 | -0.7406 | 33.229 | stable_risk |
| 確認日收盤已知 | market_strong_bull | market_regime | 1702 | 1209 | 70.2083 | 71.754 | -1.5457 | 34.4913 | 52.1092 | 3.6695 | -0.7712 | 33.7469 | stable_risk |
| 確認日收盤已知 | market_bull | market_regime | 1702 | 1586 | 92.5 | 93.6219 | -1.1219 | 34.3632 | 51.8285 | 3.8468 | -0.7353 | 33.1021 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_ge100 | monthly_revenue | 1701 | 257 | 15.0 | 16.7617 | -1.7617 | 32.6848 | 57.1984 | 2.009 | -2.1417 | 35.0195 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_improving_2m | monthly_revenue | 1694 | 433 | 22.547 | 27.7842 | -5.2372 | 30.7159 | 55.8891 | 2.4089 | -1.7717 | 36.2587 | stable_risk |
| 候選訊號日收盤已知 | revenue_cumulative_yoy_improving_2m | monthly_revenue | 1698 | 630 | 34.6555 | 39.2 | -4.5445 | 32.0635 | 54.4444 | 2.9817 | -1.3143 | 34.4444 | stable_risk |
| 候選訊號日收盤已知 | revenue_latest_yoy_delta_ge20 | monthly_revenue | 1698 | 683 | 34.375 | 44.3936 | -10.0186 | 29.2826 | 56.8082 | 2.392 | -1.8667 | 36.896 | stable_risk |
| 候選訊號日收盤已知 | tdcc_consecutive_up_ge2 | tdcc | 300 | 90 | 23.4568 | 32.6389 | -9.1821 | 30.0 | 52.2222 | 0.3782 | -0.6043 | 32.2222 | stable_risk |
| 候選訊號日收盤已知 | technical_kd_bullish_not_overheated | technical | 1702 | 990 | 54.1667 | 61.0478 | -6.8811 | 32.4242 | 54.1414 | 3.1246 | -1.3314 | 34.5455 | stable_risk |
| 候選訊號日收盤已知 | technical_kdj_bullish_not_extreme | technical | 1702 | 982 | 55.4167 | 60.2506 | -4.8339 | 32.9939 | 53.8697 | 3.3303 | -1.3422 | 35.0305 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le10 | price_shape | 1702 | 413 | 11.25 | 27.4487 | -16.1987 | 19.8547 | 58.3535 | 0.0172 | -1.5238 | 28.8136 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le15 | price_shape | 1702 | 818 | 32.0833 | 51.8223 | -19.739 | 25.7946 | 55.6235 | 1.3517 | -1.2873 | 30.4401 | stable_risk |
| 候選訊號日收盤已知 | shape_range23_width_le20 | price_shape | 1702 | 1104 | 52.0833 | 69.1344 | -17.0511 | 29.3478 | 54.9819 | 2.0645 | -1.3314 | 32.337 | stable_risk |
| 候選訊號日收盤已知 | shape_near_range23_high | price_shape | 1702 | 937 | 45.4167 | 57.8588 | -12.4421 | 30.6297 | 54.2156 | 2.6212 | -1.1429 | 32.0171 | stable_risk |
| 候選訊號日收盤已知 | position120_low_le40 | price_position | 1702 | 501 | 22.0833 | 32.0046 | -9.9213 | 27.1457 | 56.0878 | 1.1997 | -1.9231 | 35.7285 | stable_risk |
| 候選訊號日收盤已知 | market_mild_bull | market_regime | 1702 | 411 | 22.5 | 25.6264 | -3.1264 | 30.9002 | 54.7445 | 3.7279 | -1.3889 | 34.5499 | stable_risk |
| 候選訊號日收盤已知 | market_bull | market_regime | 1702 | 1486 | 86.0417 | 88.1549 | -2.1132 | 33.782 | 52.0861 | 3.7689 | -0.7793 | 33.7147 | stable_risk |

## Large Detail Policy

逐筆重算 evidence 僅保留於 `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv`；不複製到 docs/latest 或 output/history。
